#!/usr/bin/env python3
"""Crop every real figure out of a chapter PDF, into that chapter's own figures/ folder.

    python code/cut_figures.py BIO11L-ch03 --layout <layout.json> --out <chapter>/figures

Figures are the `figure` elements the extractor left after it removed the page ground, the
watermark, the header art and the QR code (see `book_design.is_watermark` and friends for the
measurement behind each). This script only cuts what that pass kept.

WHY THE CROP IS GROWN BEYOND THE MEASURED BOX
---------------------------------------------
The measured box is the ink, and NCERT's figures carry leader lines and labels that sit a few
points outside the artwork's own bounding box. Cutting exactly on the measured box shaves the
labels off -- `Daughter colony`, `Holdfast` and `Air bladder` on BIO11L ch3 p003 all end outside
it. The box is therefore grown by a small pad and clamped to the page.

WHY EACH FIGURE IS NAMED FOR ITS PAGE AND POSITION
---------------------------------------------------
`p003_fig01.png` says which printed page it came from and which figure on it, so a crop can be
checked against the book without opening the layout JSON. The printed FOLIO is used, not the
PDF's page index, because the folio is what the book itself prints and what an evidence
citation quotes.
"""

import argparse
import hashlib
import json
import os
import re
import sys

import pymupdf

PAD_PT = 4.0
DPI = 200


# The header artwork and the QR code are CUT, not redrawn.
#
# An earlier version of the renderer rebuilt the Class 11 chapter-opening page as a four-stop
# CSS gradient sampled off the scan. That is a guess at a photograph: the real opener is a
# single full-bleed IMAGE (block 0,0 -> 612,340.9 on BIO11L ch3 p001) carrying a gradient, its
# own soft edge, and the paper texture under it. Approximating it produced a cover that was
# visibly "a different green" from the book, which is exactly the kind of difference nobody can
# fix by nudging a hex value -- the shape of the fade is wrong, not the colour.
#
# Cutting the artwork out of the page instead makes the header EXACTLY right for every book,
# both classes and both editions, with no per-book colour tuning at all. The watermark and the
# page ground stay excluded -- they are furniture we deliberately do not draw.
# `ornament`: the narrow strip beside a Class 12 summary / exercises (`join_agent_text`).
CUT_FURNITURE = {"header art": "header", "qr code": "qr", "ornament": "ornament"}

# THE PAGE GROUND IS ART WHEN IT CARRIES SOMETHING. Most pages have a full-page ground image
# that draws nothing visible -- measured on BIO11L ch01, every page carries one solid 2480x3508
# grey mask -- and those stay excluded. But the unit opener's ground IS its artwork: the green
# diagonal panel and the seahorse are one full-page image (p001, xref 66), so excluding every
# ground left that page bare white. A ground is cut only when the extracted image is not
# uniform, only by xref (never by rendering the region, which would bake the page's text into
# it), and only on a page with a text layer -- on a scan the ground IS the page, words and all.
GROUND_MIN_STDDEV = 4.0


def _is_blank(path):
    """True when an image is one flat tone -- a mask or a plain sheet, nothing to draw."""
    from PIL import Image, ImageStat
    with Image.open(path) as im:
        im = im.convert("RGB")
        im.thumbnail((256, 256))
        return max(ImageStat.Stat(im).stddev) < GROUND_MIN_STDDEV


def _is_page_raster(path, rect, prose):
    """True when a page-sized picture is a RASTER OF THE PAGE ITSELF, text included.

    The Class 11 Physics PDF (Bullzip print of the PageMaker file) places a 2480x3508 picture of
    the whole printed page -- every line of prose in it -- under the live text on every page.
    Its box (x 0.04-0.96) is too narrow for a page ground, so it was cut as `header art` and
    drawn under the text: every line of PHY11L-ch01 printed twice, slightly out of register.
    Biology's page pictures hold only the page's decoration. So a picture is a page raster when
    it is INKED where the text layer's prose lines are: sampled at each prose line's box, most
    lines are darker than the picture's own paper."""
    if not prose or not rect:
        return False
    from PIL import Image, ImageStat
    with Image.open(path) as im:
        im = im.convert("L")
        w, h = im.size
        rx0, ry0, rx1, ry1 = rect
        if rx1 <= rx0 or ry1 <= ry0:
            return False
        sx, sy = w / (rx1 - rx0), h / (ry1 - ry0)
        paper = max(ImageStat.Stat(im.resize((64, 64))).extrema[0][1], 1)
        inked = 0
        sample = prose[:: max(1, len(prose) // 40)]
        for x0, y0, x1, y1 in sample:
            box = (int((x0 - rx0) * sx), int((y0 - ry0) * sy), int((x1 - rx0) * sx), int((y1 - ry0) * sy))
            if box[0] < 0 or box[1] < 0 or box[2] > w or box[3] > h or box[2] <= box[0] or box[3] <= box[1]:
                continue
            if ImageStat.Stat(im.crop(box)).mean[0] < paper * 0.85:
                inked += 1
        return inked >= 0.6 * len(sample)


def _extract_embedded(doc, page, el, out_path, tol=3.0):
    """Write the page's own embedded image for this element, or return False.

    Matched by placement: the element's bbox is where the image is drawn on the page, so the
    xref whose draw rectangle matches that bbox is the image to pull. Returns False when no
    single image accounts for the box -- a composed figure, or a vector band with no image at
    all -- and the caller falls back to rendering the region.
    """
    try:
        x0, y0, x1, y1 = el["bbox_pt"]
        pr = page.rect
        for info in page.get_images(full=True):
            xref = info[0]
            for r in page.get_image_rects(xref):
                # COMPARE AGAINST THE RECT CLIPPED TO THE PAGE. `get_text("dict")` clips an
                # image block to the sheet, `get_image_rects` does not: the Class 11 opener's
                # panel is placed at y -19.1 and reported as y 0 by the block list, a 19pt
                # disagreement that no sane tolerance bridges. Matching the raw rects therefore
                # never fired, every header silently fell back to a rendered crop, and the
                # rendered crop carried the chapter title as baked-in pixels -- which is why
                # the title appeared twice, once as an image and once as live text.
                c = (max(r.x0, pr.x0), max(r.y0, pr.y0), min(r.x1, pr.x1), min(r.y1, pr.y1))
                if (abs(c[0] - x0) <= tol and abs(c[1] - y0) <= tol
                        and abs(c[2] - x1) <= tol and abs(c[3] - y1) <= tol):
                    pix = pymupdf.Pixmap(doc, xref)
                    if pix.colorspace and pix.colorspace.n > 3:      # CMYK -> RGB
                        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
                    pix.save(out_path)
                    # The UNCLIPPED draw rectangle, truthy: where the image really sits, which
                    # for a bleed image is partly off the sheet.
                    return (r.x0, r.y0, r.x1, r.y1)
    except Exception:
        return False
    return False


def cut(pdf_path, layout, out_dir, dpi=DPI):
    os.makedirs(out_dir, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    import pdf_watermark
    pdf_watermark.strip(doc)                  # crops never carry `© NCERT not to be republished`
    written = []
    for pi, page in enumerate(layout["pages"]):
        # A table is cropped exactly like a figure -- see `_mark_tables` for why a ruled
        # grid is reproduced as an image rather than re-typeset from a text layer that
        # carries no columns.
        figs = [e for e in page["elements_in_reading_order"]
                if e["role"] in ("figure", "table")]
        furn = [e for e in page["elements_in_reading_order"]
                if e["role"] == "page_furniture" and e.get("furniture") in CUT_FURNITURE]
        grounds = [e for e in page["elements_in_reading_order"]
                   if e["role"] == "page_furniture" and e.get("furniture") == "page ground"
                   and page.get("has_text_layer")]
        if not figs and not furn and not grounds:
            continue
        p = doc[pi]
        pw, ph = p.rect.width, p.rect.height
        folio = page.get("printed_page_number")
        stem = f"p{folio:03d}" if isinstance(folio, int) else f"i{pi + 1:03d}"

        # The page's PROSE lines: a crop is a render of a page region, so a pad that reaches into
        # the text column bakes slivers of its last letters into the picture. Figure 2.4's crop
        # (BIO11L ch02 p015) began 0.2pt left of the justified right edge of the prose beside it
        # and carried a column of half-letters down its left side.
        prose = [ln["bbox"] for b in p.get_text("dict")["blocks"] for ln in b.get("lines", [])
                 if len("".join(s["text"] for s in ln["spans"]).strip()) > 12]

        def _clear_of_prose(rect, own):
            """Shrink `rect` off every prose line whose centre lies outside `own`."""
            x0, y0, x1, y1 = rect
            for lx0, ly0, lx1, ly1 in prose:
                cx, cy = (lx0 + lx1) / 2, (ly0 + ly1) / 2
                if own[0] <= cx <= own[2] and own[1] <= cy <= own[3]:
                    continue                      # the figure's own label or caption line
                if lx1 <= x0 or lx0 >= x1 or ly1 <= y0 or ly0 >= y1:
                    continue
                # move the edge the line pokes through, choosing the side it sits on
                if lx1 <= own[0] + 1:
                    x0 = max(x0, lx1 + 0.5)
                elif lx0 >= own[2] - 1:
                    x1 = min(x1, lx0 - 0.5)
                elif ly1 <= own[1] + 1:
                    y0 = max(y0, ly1 + 0.5)
                elif ly0 >= own[3] - 1:
                    y1 = min(y1, ly0 - 0.5)
            return x0, y0, x1, y1

        # The CAPTION TINTS: the filled box a caption is set on. A figure's pad stops at its
        # edge -- Figures 6.2, 6.6, 6.10 and 6.11 (BIO12L ch06) are printed 2-3pt above their
        # tinted caption, and the pad baked a peach strip into the foot of each crop, drawn as
        # a stray rule above the live caption's own tint.
        caps = [e["bbox_pt"] for e in page["elements_in_reading_order"]
                if e["role"] == "figure_caption" and e.get("bbox_pt")]
        tints = []
        if caps:
            from extract_page_layout import visible_drawings
            for d in visible_drawings(p):
                r = d["rect"]
                if d.get("fill") and not d.get("coarse") and r.width < 0.95 * pw and any(
                        r.x0 <= c[0] + 2 and r.y0 <= c[1] + 2 and r.x1 >= c[2] - 2
                        and r.y1 >= c[3] - 2 for c in caps):
                    tints.append((r.x0, r.y0, r.x1, r.y1))

        def _clear_of_tints(rect, own):
            x0, y0, x1, y1 = rect
            for tx0, ty0, tx1, ty1 in tints:
                if tx1 <= x0 or tx0 >= x1:
                    continue
                if own[3] - 1 <= ty0 < y1:
                    y1 = min(y1, ty0 - 0.3)
                elif y0 < ty1 <= own[1] + 1:
                    y0 = max(y0, ty1 + 0.3)
            return x0, y0, x1, y1

        def _save(el, name, pad, own=None):
            x0, y0, x1, y1 = el["bbox_pt"]
            x0, y0, x1, y1 = _clear_of_prose((x0 - pad, y0 - pad, x1 + pad, y1 + pad),
                                             own or el["bbox_pt"])
            x0, y0, x1, y1 = _clear_of_tints((x0, y0, x1, y1), own or el["bbox_pt"])
            rect = pymupdf.Rect(max(0, x0), max(0, y0), min(pw, x1), min(ph, y1))
            if rect.width < 8 or rect.height < 8:
                return None
            # WHERE THE PICTURE WAS CUT. The crop is the box plus a pad (trimmed by the two
            # passes above), so it is larger than the box -- and a render that fits it INTO the
            # box shrinks it: BIO12L ch05 p084's one-row Griffith diagram printed at 0.8 of the
            # book's size, the 4pt pad being a quarter of its height. The exact page places the
            # picture at this rect instead.
            el["crop_bbox_pt"] = [round(rect.x0, 2), round(rect.y0, 2),
                                  round(rect.x1, 2), round(rect.y1, 2)]
            pix = p.get_pixmap(dpi=dpi, clip=rect)
            # A PROSE LINE THAT RUNS INTO THE CROP IS LEFT OUT OF IT. The book wraps text into a
            # figure's space -- `... the variety of architecture -` (BIO12L ch01 p007) ends inside
            # Figure 1.5 (b)'s box, and no edge can be moved without cutting the drawing -- so the
            # crop carried `tecture -` as pixels over the live line. Those pixels are made clear,
            # and the live text shows through. A crop no line enters is saved unchanged.
            own_box = own or el["bbox_pt"]
            # Figures and their panels only: a table's crop holds its own cell text.
            holes = [] if el.get("role") == "table" else [
                     (lx0, ly0, lx1, ly1) for lx0, ly0, lx1, ly1 in prose
                     if not (own_box[0] <= (lx0 + lx1) / 2 <= own_box[2]
                             and own_box[1] <= (ly0 + ly1) / 2 <= own_box[3])
                     and lx1 > rect.x0 and lx0 < rect.x1 and ly1 > rect.y0 and ly0 < rect.y1]
            if holes:
                from PIL import Image, ImageDraw
                img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("RGBA")
                alpha = Image.new("L", img.size, 255)
                draw = ImageDraw.Draw(alpha)
                k = dpi / 72.0
                for lx0, ly0, lx1, ly1 in holes:
                    draw.rectangle([(lx0 - rect.x0 - 0.5) * k, (ly0 - rect.y0 - 0.5) * k,
                                    (lx1 - rect.x0 + 0.5) * k, (ly1 - rect.y0 + 0.5) * k], fill=0)
                img.putalpha(alpha)
                img.save(os.path.join(out_dir, name))
            else:
                pix.save(os.path.join(out_dir, name))
            return name

        for k, el in enumerate(sorted(figs, key=lambda e: (e["bbox_pt"][1], e["bbox_pt"][0])), 1):
            kind = "table" if el["role"] == "table" else "fig"
            name = _save(el, f"{stem}_{kind}{k:02d}.png", PAD_PT)
            if name:
                el["figure_file"] = name
                el["figure_dpi"] = dpi
                written.append(name)
            # ONE CROP PER PANEL, beside the whole-figure crop: `p017_fig01a.png`,
            # `p017_fig01b.png` ... Each is a picture the book prints on its own, so each gets
            # its own file, and later its own CDN link (`join_agent_text._find_panels`).
            # A panel crop never reaches into ANOTHER panel: Figure 2.5 (c)'s padded crop took
            # in the `(b)` printed just above it. Each side's pad stops at the nearest edge of a
            # sibling panel that faces it.
            panels = el.get("panels") or []
            for panel in panels:
                # A named panel (`Cocci`, Figure 2.1) carries its file letter as `key`.
                letter = panel.get("key") or re.sub(r"[^a-z]", "", panel.get("label") or "")
                x0, y0, x1, y1 = panel["bbox_pt"]
                ex = [x0 - PAD_PT, y0 - PAD_PT, x1 + PAD_PT, y1 + PAD_PT]
                for o in panels:
                    if o is panel:
                        continue
                    ox0, oy0, ox1, oy1 = o["bbox_pt"]
                    # Neighbours whose boxes OVERLAP a little part at the middle of the overlap:
                    # Figure 2.4's (b) and (c) share 2pt (BIO11L ch02 p015), so neither edge
                    # test fired and (b)'s crop carried the top of the slime mould.
                    if min(x1, ox1) > max(x0, ox0):            # stacked: same columns
                        if oy1 <= y0 or (oy0 < y0 < oy1 < y1):
                            ex[1] = max(ex[1], (y0 + oy1) / 2 if oy1 > y0 else oy1)
                        if oy0 >= y1 or (y0 < oy0 < y1 < oy1):
                            ex[3] = min(ex[3], (oy0 + y1) / 2 if oy0 < y1 else oy0)
                    if min(y1, oy1) > max(y0, oy0):            # side by side: same rows
                        if ox1 <= x0 or (ox0 < x0 < ox1 < x1):
                            ex[0] = max(ex[0], (x0 + ox1) / 2 if ox1 > x0 else ox1)
                        if ox0 >= x1 or (x0 < ox0 < x1 < ox1):
                            ex[2] = min(ex[2], (ox0 + x1) / 2 if ox0 < x1 else ox0)
                if panel.get("raster"):
                    # A panel split out of ONE scanned picture (Figure 3.1) is cut from that
                    # picture, its own drawing only: a page render of its box would carry the
                    # neighbouring drawing that reaches into it, and the watermark.
                    import join_agent_text
                    pname = f"{stem}_{kind}{k:02d}{letter}.png"
                    join_agent_text.raster_panel_image(doc, panel["raster"]).save(
                        os.path.join(out_dir, pname))
                else:
                    pname = _save({"bbox_pt": ex}, f"{stem}_{kind}{k:02d}{letter}.png", 0.0,
                                  own=panel["bbox_pt"])
                if pname:
                    panel["figure_file"] = pname
                    written.append(pname)
        # Furniture is cut with NO pad: it bleeds to the trim, and a pad would pull in a strip
        # of the neighbouring page content and print it inside the header.
        #
        # AND IT IS EXTRACTED, NOT RENDERED. Rendering the page region bakes in whatever TEXT
        # sits over the artwork -- the Class 11 opener's green panel spans y 0 to 0.435 of the
        # sheet, and `CHAPTER 3 / PLANT KINGDOM` is set inside it at y 0.325. A rendered crop
        # therefore carries the title as pixels, and the renderer then draws the same title
        # again as live text on top of it: the same words twice, slightly out of register, and
        # unselectable underneath. Pulling the embedded image out by its xref gives the panel
        # alone, so the title stays real text set over real artwork.
        seen = {}
        for el in furn:
            kind = CUT_FURNITURE[el["furniture"]]
            seen[kind] = seen.get(kind, 0) + 1
            suffix = "" if seen[kind] == 1 else f"{seen[kind]}"
            name = f"{stem}_{kind}{suffix}.png"
            rect = _extract_embedded(doc, p, el, os.path.join(out_dir, name))
            if isinstance(rect, tuple) and _is_page_raster(os.path.join(out_dir, name), rect, prose):
                os.remove(os.path.join(out_dir, name))
                continue
            if rect or _save(el, name, 0.0):
                el["furniture_file"] = name
                written.append(name)
            # A BLEED PICTURE IS PLACED WHERE THE BOOK PLACES IT, as a ground is (below). Class
            # 12's header art is drawn from -0.038 to 1.038 across and from -0.028 down: the
            # whole image squeezed into the clipped box set the green band 11pt too deep on
            # every page (BIO12L ch06; ch01-05 the same).
            if isinstance(rect, tuple) and (rect[0] < -0.5 or rect[1] < -0.5
                                            or rect[2] > pw + 0.5 or rect[3] > ph + 0.5):
                dx, dy = page.get("sheet_offset_pt") or (0.0, 0.0)
                sw, sh = page.get("sheet_pt") or (pw, ph)
                el["bbox_sheet"] = [round((rect[0] + dx) / sw, 4), round((rect[1] + dy) / sh, 4),
                                    round((rect[2] + dx) / sw, 4), round((rect[3] + dy) / sh, 4)]
        cut_grounds = {}
        for k, el in enumerate(grounds, 1):
            name = f"{stem}_ground{'' if k == 1 else k}.png"
            path = os.path.join(out_dir, name)
            rect = _extract_embedded(doc, p, el, path)
            if not rect:
                continue
            with open(path, "rb") as fh:
                digest = hashlib.sha256(fh.read()).hexdigest()
            # Two full-page grounds share the page's box, so both can match the same image:
            # measured on BIO11L ch01 p001, both pulled xref 66. One picture is drawn once.
            if _is_blank(path) or digest in cut_grounds or _is_page_raster(path, rect, prose):
                os.remove(path)
                continue
            cut_grounds[digest] = name
            # PLACED WHERE THE BOOK PLACES IT. The ground bleeds past the trim (p001: -6..615 by
            # -19..802pt); squeezing it into the clipped page box shifted the seahorse left.
            # `bbox_sheet` takes the chapter offset exactly as `_apply_chapter_offset` does.
            dx, dy = page.get("sheet_offset_pt") or (0.0, 0.0)
            sw, sh = page.get("sheet_pt") or (pw, ph)
            el["bbox_sheet"] = [round((rect[0] + dx) / sw, 4), round((rect[1] + dy) / sh, 4),
                                round((rect[2] + dx) / sw, 4), round((rect[3] + dy) / sh, 4)]
            el["furniture_file"] = name
            written.append(name)
    doc.close()
    return written


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("--layout", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--dpi", type=int, default=DPI)
    a = ap.parse_args()
    with open(a.layout, encoding="utf-8") as fh:
        layout = json.load(fh)
    written = cut(layout["source_pdf"], layout, a.out, a.dpi)
    # The layout is rewritten so each figure element now names its own file -- the renderer
    # reads `figure_file` and would otherwise have nothing to point an <img> at.
    with open(a.layout, "w", encoding="utf-8") as fh:
        json.dump(layout, fh, indent=1, ensure_ascii=False)
    print(f"{a.chapter}: {len(written)} figures -> {a.out}")


if __name__ == "__main__":
    main()
