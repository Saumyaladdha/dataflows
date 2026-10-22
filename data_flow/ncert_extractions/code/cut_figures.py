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
import json
import os
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
CUT_FURNITURE = {"header art": "header", "qr code": "qr"}


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
                    return True
    except Exception:
        return False
    return False


def cut(pdf_path, layout, out_dir, dpi=DPI):
    os.makedirs(out_dir, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    written = []
    for pi, page in enumerate(layout["pages"]):
        # A table is cropped exactly like a figure -- see `_mark_tables` for why a ruled
        # grid is reproduced as an image rather than re-typeset from a text layer that
        # carries no columns.
        figs = [e for e in page["elements_in_reading_order"]
                if e["role"] in ("figure", "table")]
        furn = [e for e in page["elements_in_reading_order"]
                if e["role"] == "page_furniture" and e.get("furniture") in CUT_FURNITURE]
        if not figs and not furn:
            continue
        p = doc[pi]
        pw, ph = p.rect.width, p.rect.height
        folio = page.get("printed_page_number")
        stem = f"p{folio:03d}" if isinstance(folio, int) else f"i{pi + 1:03d}"

        def _save(el, name, pad):
            x0, y0, x1, y1 = el["bbox_pt"]
            rect = pymupdf.Rect(max(0, x0 - pad), max(0, y0 - pad),
                                min(pw, x1 + pad), min(ph, y1 + pad))
            if rect.width < 8 or rect.height < 8:
                return None
            p.get_pixmap(dpi=dpi, clip=rect).save(os.path.join(out_dir, name))
            return name

        for k, el in enumerate(sorted(figs, key=lambda e: (e["bbox_pt"][1], e["bbox_pt"][0])), 1):
            kind = "table" if el["role"] == "table" else "fig"
            name = _save(el, f"{stem}_{kind}{k:02d}.png", PAD_PT)
            if name:
                el["figure_file"] = name
                el["figure_dpi"] = dpi
                written.append(name)
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
            if _extract_embedded(doc, p, el, os.path.join(out_dir, name)) or \
                    _save(el, name, 0.0):
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
