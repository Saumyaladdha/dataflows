#!/usr/bin/env python3
"""Render one extracted NCERT chapter as a faithful, self-contained HTML book.

    python code/render_chapter_html.py BIO11L-ch03
    python code/render_chapter_html.py BIO12O-ch07 --out some/where/chapter.html

Reads the layout JSON written by `extract_page_layout.py` and the measured page design from
`book_design.py`, and writes ONE html file holding every page of the chapter at the book's real
trim size, with the book's own furniture drawn in CSS.

WHAT MAKES THIS DIFFERENT FROM THE EXPORTER IT REPLACES
-------------------------------------------------------
1. THE PAGE IS THE BOOK'S PAGE. Every sheet is 215.9 x 276.6mm -- the canonical NCERT trim --
   for Class 11 and Class 12, old edition and new. The previous exporter took each PDF's own
   page size, so the new Class 12 Biology scans (568.8 x 777.6pt, a 21.6pt crop of the same
   physical sheet) rendered 7% narrower than Class 11 and narrower than their own older
   edition: three page sizes for one book. The extractor measures that crop and the renderer
   draws on the real sheet.

2. THE FURNITURE IS PER (SUBJECT, CLASS), NOT PER SUBJECT. Class 11 Biology prints a pale-green
   band closed by a grey strip with the folio in a white tab on it and a green bar across the
   foot. Class 12 Biology prints a dark-green rule with a brown block on the outer end, a leaf
   motif, no footer bar, and the folio in an orange tab two-thirds down the outer margin. They
   are different books. Keying the design on `BIO` rendered one of them as the other.

3. THE PAGE MIRRORS. NCERT sets a 60pt inner margin and a 192pt outer rail, and swaps them
   every page. The folio, the running head and the marginal notes all follow the outer edge.
   A render that does not mirror puts half the book's furniture in the gutter.

4. NO WATERMARK. The `(c) NCERT / not to be republished` overlay is detected during extraction
   -- it must be, or a figure cutter files it as artwork -- and deliberately not drawn.

5. THE RUNNING HEAD IS REAL. It is read off the page (`24 Biology` / `Plant Kingdom 29`), split
   into its folio and its head text, and re-set at the two ends of the measure. The old
   exporter synthesised a band and guessed what belonged on it.
"""

import argparse
import base64
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import book_design as design_lib  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONT_DIR = os.path.join(ROOT, "assets", "fonts")

# Roles that are page furniture and are drawn from the DESIGN, never from the extracted
# element -- drawing both paints the same thing twice, slightly out of register.
FURNITURE_ROLES = {"page_furniture", "running_header", "page_number", "reprint_line"}


def esc(s):
    return html.escape(s or "", quote=False)


def _font_face(name, file, weight, style):
    path = os.path.join(FONT_DIR, file)
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode("ascii")
    return (f"@font-face{{font-family:'{name}';"
            f"src:url(data:font/otf;base64,{b64}) format('opentype');"
            f"font-weight:{weight};font-style:{style};font-display:swap;}}")


def embedded_fonts():
    """NCERT sets its English body in Bookman and its display type in a Century Gothic class.
    Neither ships with most machines, so the free metric clones are embedded -- the file is then
    one artifact that looks the same wherever it is opened, which is what the reference pages do
    and what makes a render reviewable by someone who does not have the repo."""
    return "".join([
        _font_face("NcertBody", "texgyrebonum-regular.otf", 400, "normal"),
        _font_face("NcertBody", "texgyrebonum-bold.otf", 700, "normal"),
        _font_face("NcertBody", "texgyrebonum-italic.otf", 400, "italic"),
        _font_face("NcertBody", "texgyrebonum-bolditalic.otf", 700, "italic"),
        _font_face("NcertDisplay", "texgyreadventor-regular.otf", 400, "normal"),
    ])


def runs_html(el):
    """The element's formatted runs as inline HTML, preserving what the page prints."""
    out = []
    for r in el.get("runs") or []:
        t = esc(r.get("t", ""))
        if not t:
            continue
        if r.get("script") == "sup":
            t = f"<sup>{t}</sup>"
        elif r.get("script") == "sub":
            t = f"<sub>{t}</sub>"
        cls = []
        if r.get("b"):
            cls.append("b")
        if r.get("i"):
            cls.append("i")
        if r.get("sc"):
            cls.append("sc")
        if cls:
            t = f'<span class="{" ".join(cls)}">{t}</span>'
        out.append(t)
    return "".join(out) or esc(el.get("text", ""))


def mm(pt):
    return design_lib.pt_to_mm(pt)


# ------------------------------------------------------------------------------------------
# FURNITURE
# ------------------------------------------------------------------------------------------

def cut_furniture_html(d, page, fig_rel, kinds):
    """The page's own header artwork and QR, placed where the page prints them.

    These are cut from the PDF rather than redrawn -- see the note in cut_figures.py. Using the
    real artwork is what makes the green at the head of a Class 11 page the book's green, and
    the Class 12 leaf motif the book's motif, with no per-book colour constants at all.
    """
    W, H = d.trim_pt
    out = []
    for el in page["elements_in_reading_order"]:
        if el["role"] != "page_furniture" or el.get("furniture") not in kinds:
            continue
        name = el.get("furniture_file")
        if not name:
            continue
        x0, y0, x1, y1 = el.get("bbox_sheet") or el["bbox"]
        out.append(
            f'<img class="fx art" src="{fig_rel}/{name}" alt="" '
            f'style="left:{mm(x0 * W):.2f}mm;top:{mm(y0 * H):.2f}mm;'
            f'width:{mm((x1 - x0) * W):.2f}mm;height:{mm((y1 - y0) * H):.2f}mm;">')
    return "".join(out)


def has_cut_header(page, below_pt=None, page_h_pt=784.0):
    """True if the page carries cut header artwork.

    `below_pt` asks a sharper question: does that artwork reach at least this far down the
    sheet? It matters because the two Biology classes cut very different things. Class 11's
    opener artwork IS the whole green head (down to y 341pt), so the CSS reconstruction of it
    must be suppressed or the two are painted over each other. Class 12's is only the
    dark-green rule and leaf motif at the very top (down to y 77pt), and its pale-green HERO
    and orange DIVIDER are vector -- there is nothing to cut. Treating "has artwork" as "has a
    complete header" suppressed the hero and the divider on every Class 12 opener, which is
    why that page came out as a bare rule over white paper.
    """
    for e in page["elements_in_reading_order"]:
        if (e["role"] == "page_furniture" and e.get("furniture") == "header art"
                and e.get("furniture_file")):
            if below_pt is None:
                return True
            bb = e.get("bbox_sheet") or e["bbox"]
            if bb[3] * page_h_pt >= below_pt:
                return True
    return False


def furniture_html(d, page, chapter_title, subject_name, edition, fig_rel=""):
    """Every piece of page furniture the book prints, positioned from the measured design."""
    side = page.get("page_side") or "recto"
    W, H = d.trim_pt
    out = []

    # The page's OWN header artwork wins over the CSS reconstruction of it. Class 12 body pages
    # carry a real motif strip; Class 11 body pages draw their band in vector, so there is no
    # image to cut and the measured band below is what paints it.
    cut_header = has_cut_header(page)
    if cut_header:
        out.append(cut_furniture_html(d, page, fig_rel, {"header art"}))

    band = None if cut_header else getattr(d, "header_band", None)
    if band:
        out.append(f'<div class="fx band" style="top:{mm(band["y0_pt"]):.2f}mm;'
                   f'height:{mm(band["y1_pt"] - band["y0_pt"]):.2f}mm;'
                   f'background:{band["fill"]};"></div>')
    strip = None if cut_header else getattr(d, "header_strip", None)
    if strip:
        out.append(f'<div class="fx band" style="top:{mm(strip["y0_pt"]):.2f}mm;'
                   f'height:{mm(strip["y1_pt"] - strip["y0_pt"]):.2f}mm;'
                   f'background:{strip["fill"]};"></div>')
    corner = None if cut_header else getattr(d, "header_corner", None)
    if corner and band:
        # The brown block sits on the OUTER end of the rule and mirrors with the page.
        edge = "right" if side == "recto" else "left"
        out.append(f'<div class="fx" style="{edge}:0;top:{mm(band["y0_pt"]):.2f}mm;'
                   f'width:{mm(corner["w_pt"]):.2f}mm;'
                   f'height:{mm(band["y1_pt"] - band["y0_pt"]):.2f}mm;'
                   f'background:{corner["fill"]};"></div>')

    # --- running head -----------------------------------------------------------------------
    rh = getattr(d, "running_head", None)
    head_text = ""
    if rh:
        # The book prints the SUBJECT on the verso and the CHAPTER TITLE on the recto.
        want = rh["verso"] if side == "verso" else rh["recto"]
        head_text = subject_name if want == "subject" else chapter_title
        measured = next((e["text"] for e in page["elements_in_reading_order"]
                         if e["role"] == "running_header" and e.get("text")), "")
        if measured:
            head_text = measured          # what the page actually prints wins
    if rh and head_text:
        # The head sits at the INNER end of the measure, the folio taking the outer end.
        edge = "left" if side == "recto" else "right"
        style = (f'{edge}:{mm(rh["inset_pt"]):.2f}mm;top:{mm(rh["y_pt"]):.2f}mm;'
                 f'font-size:{rh["size_pt"]:.1f}pt;color:{rh["ink"]};'
                 f'font-family:var(--font-{rh["font"]});')
        if rh.get("smallcaps"):
            style += "font-variant:small-caps;"
        if rh.get("uppercase"):
            style += "text-transform:uppercase;letter-spacing:.06em;"
        if rh.get("weight"):
            style += f'font-weight:{rh["weight"]};'
        out.append(f'<div class="fx head" style="{style}">{esc(head_text)}</div>')
        if rh.get("rule"):
            out.append(f'<div class="fx" style="left:{mm(60):.2f}mm;right:{mm(60):.2f}mm;'
                       f'top:{mm(rh["y_pt"] + 14):.2f}mm;height:{mm(rh["rule_h_pt"]):.2f}mm;'
                       f'background:{rh["rule"]};"></div>')

    # --- folio ------------------------------------------------------------------------------
    folio = getattr(d, "folio", None)
    n = page.get("printed_page_number")
    if folio and n is not None:
        x_pt = folio["x_recto_pt"] if side == "recto" else folio["x_verso_pt"]
        style = (f'left:{mm(x_pt):.2f}mm;top:{mm(folio["y0_pt"]):.2f}mm;'
                 f'width:{mm(folio["w_pt"]):.2f}mm;height:{mm(folio["h_pt"]):.2f}mm;'
                 f'font-family:var(--font-{folio["font"]});font-size:{folio["size_pt"]:.1f}pt;'
                 f'font-weight:{folio.get("weight", 700)};')
        if folio.get("fill"):
            style += f'background:{folio["fill"]};'
        style += f'color:{folio["ink"]};'
        if folio.get("radius_pt"):
            r = mm(folio["radius_pt"])
            style += (f'border-radius:{r:.2f}mm {r:.2f}mm 0 0;'
                      if folio.get("radius_corners") == "top"
                      else f'border-radius:{r:.2f}mm;')
        # The number ranges toward the INNER edge; the tab bleeds outward off the trim.
        if folio.get("align") == "inner":
            pad = mm(folio.get("pad_pt", 0.0))
            if side == "recto":
                style += f'justify-content:flex-start;padding-left:{pad:.2f}mm;'
            else:
                style += f'justify-content:flex-end;padding-right:{pad:.2f}mm;'
        else:
            style += "justify-content:center;"
        out.append(f'<div class="fx folio" style="{style}">{n}</div>')
        if folio.get("underbar_h_pt"):
            y = folio["y0_pt"] + folio["h_pt"] + folio.get("underbar_gap_pt", 0.0)
            out.append(f'<div class="fx" style="left:{mm(x_pt):.2f}mm;top:{mm(y):.2f}mm;'
                       f'width:{mm(folio["w_pt"]):.2f}mm;'
                       f'height:{mm(folio["underbar_h_pt"]):.2f}mm;'
                       f'background:{folio["fill"]};"></div>')
        if folio.get("rule"):
            y = folio["y0_pt"] + folio["h_pt"]
            out.append(f'<div class="fx" style="left:{mm(x_pt):.2f}mm;top:{mm(y):.2f}mm;'
                       f'width:{mm(folio["w_pt"]):.2f}mm;height:0.4mm;'
                       f'background:{folio["rule"]};"></div>')

    # --- foot -------------------------------------------------------------------------------
    bar = getattr(d, "footer_bar", None)
    if bar:
        out.append(f'<div class="fx band" style="top:{mm(bar["y0_pt"]):.2f}mm;bottom:0;'
                   f'background:{bar["fill"]};"></div>')
    imp = getattr(d, "imprint", None)
    if imp:
        text = page.get("imprint") or d.imprint(edition)
        out.append(f'<div class="fx imprint" style="top:{mm(imp["y_pt"]):.2f}mm;'
                   f'font-family:var(--font-{imp["font"]});font-size:{imp["size_pt"]:.1f}pt;'
                   f'color:{imp["ink"]};">{esc(text)}</div>')
    return "".join(out)


def opener_html(d, page, fig_rel):
    """The chapter-opening page, drawn as the book prints it.

    Two kinds so far, both measured: Class 11 Biology sets the whole head of the page as a green
    gradient fading to white with the title and a contents rail below it; Class 12 Biology sets
    a pale-green hero closed by an orange divider, with the contents in a tinted panel.
    """
    o = getattr(d, "opener", None)
    if not o:
        return ""
    out = []
    # The opener's artwork, cut from the page itself. This is the whole head of a Class 11
    # opener (the green fading to white) and the rule-and-motif strip of a Class 12 one.
    out.append(cut_furniture_html(d, page, fig_rel, {"header art", "qr code"}))

    if o["kind"] == "gradient":
        # FALLBACK ONLY -- used when the page carries no cuttable artwork. The real opener is an
        # image and is cut above; this reconstruction exists so a page whose artwork failed to
        # cut still shows a green head rather than bare white.
        #
        # `left:0;right:0` is not decoration. Without them this div had NO horizontal
        # constraint at all, so it computed to zero width and the entire green head of every
        # Class 11 chapter-opening page rendered as blank white paper -- the defect the owner
        # reported as "green colour at top is not coming". `.fx` sets position/z-index only;
        # only `.fx.band` sets left/right, and this div did not carry `band`.
        if not has_cut_header(page, o["gradient_stops_pt"][-1] * 0.8, d.trim_pt[1]):
            stops = ", ".join(f"{c} {mm(y):.1f}mm"
                              for c, y in zip(o["gradient"], o["gradient_stops_pt"]))
            out.append(f'<div class="fx band" style="left:0;right:0;top:0;'
                       f'height:{mm(o["gradient_stops_pt"][-1]):.2f}mm;'
                       f'background:linear-gradient(to bottom, {stops});z-index:0;"></div>')
    elif o["kind"] == "hero" and not has_cut_header(page, o["hero"]["y1_pt"] * 0.8,
                                                    d.trim_pt[1]):
        h = o["hero"]
        out.append(f'<div class="fx band" style="top:{mm(h["y0_pt"]):.2f}mm;'
                   f'height:{mm(h["y1_pt"] - h["y0_pt"]):.2f}mm;background:{h["fill"]};'
                   f'z-index:0;"></div>')
        dv = o["divider"]
        out.append(f'<div class="fx band" style="top:{mm(dv["y0_pt"]):.2f}mm;'
                   f'height:{mm(dv["y1_pt"] - dv["y0_pt"]):.2f}mm;background:{dv["fill"]};'
                   f'z-index:0;"></div>')
        pl = o.get("plate")
        if pl:
            out.append(f'<div class="fx" style="left:{mm(pl["x_pt"]):.2f}mm;'
                       f'top:{mm(pl["y_pt"]):.2f}mm;width:{mm(pl["w_pt"]):.2f}mm;'
                       f'height:{mm(pl["h_pt"]):.2f}mm;background:{pl["fill"]};z-index:0;"></div>')

    # The contents panel's tint, behind the entries the page itself carries.
    c = o.get("contents") or {}
    if c.get("panel_fill"):
        entries = [e for e in page["elements_in_reading_order"] if e["role"] == "contents_entry"]
        if entries:
            top = min(e["bbox_sheet"][1] for e in entries) * d.trim_pt[1] - 14
            bot = max(e["bbox_sheet"][3] for e in entries) * d.trim_pt[1] + 14
            r = mm(c.get("panel_radius_pt", 0))
            out.append(f'<div class="fx" style="left:{mm(c["x_pt"]):.2f}mm;'
                       f'top:{mm(top):.2f}mm;width:{mm(c["width_pt"]):.2f}mm;'
                       f'height:{mm(bot - top):.2f}mm;background:{c["panel_fill"]};'
                       f'border-radius:0 0 {r:.1f}mm {r:.1f}mm;z-index:0;"></div>')
            if c.get("panel_shadow"):
                out.append(f'<div class="fx" style="left:{mm(c["x_pt"] + 18):.2f}mm;'
                           f'top:{mm(bot + 4):.2f}mm;'
                           f'width:{mm(c["width_pt"] - 36):.2f}mm;height:1.0mm;'
                           f'background:{c["panel_shadow"]};z-index:0;"></div>')
    return "".join(out)


def element_html(d, el, fig_rel, is_opener):
    """One extracted element, placed where the page puts it."""
    role = el["role"]
    if role in FURNITURE_ROLES:
        return ""
    bb = el.get("bbox_sheet") or el["bbox"]
    W, H = d.trim_pt
    x0, y0, x1, y1 = bb
    left, top = x0 * W, y0 * H
    width = max(1.0, (x1 - x0) * W)

    if role in ("figure", "table"):
        src = el.get("figure_file")
        if not src:
            return ""
        alt = esc(el.get("table_text", ""))[:300] if role == "table" else ""
        return (f'<div class="el fig" style="left:{mm(left):.2f}mm;top:{mm(top):.2f}mm;'
                f'width:{mm(width):.2f}mm;">'
                f'<img src="{fig_rel}/{src}" alt="{alt}">' + "</div>")

    body = runs_html(el)
    if not body.strip():
        return ""
    size = (el.get("size_rel") or 1.0) * d.body_pt
    cls = {"paragraph": "p", "list": "li", "section_heading": "h",
           "figure_caption": "cap", "side_note": "note",
           "contents_entry": "toc", "chapter_title": "title"}.get(role, "p")
    style = (f'left:{mm(left):.2f}mm;top:{mm(top):.2f}mm;width:{mm(width):.2f}mm;'
             f'font-size:{size:.2f}pt;')
    # The PRINTED line pitch, so the block occupies the height the book gives it. Without this
    # every block was set at the stylesheet's leading, each came out a little taller than the
    # page prints, and the error accumulated down the sheet -- headings landing on top of the
    # paragraph below them and gaps opening where the book has none.
    pitch = el.get("line_pitch_pt")
    if pitch and (el.get("line_count") or 0) > 1:
        style += f"line-height:{pitch:.2f}pt;"
    if role == "section_heading":
        style += f"color:{d.heading_ink};"
    elif role == "contents_entry":
        c = (getattr(d, "opener", None) or {}).get("contents") or {}
        style += f'color:{c.get("ink", d.accent)};'
        if c.get("italic"):
            style += "font-style:italic;"
    elif role == "chapter_title":
        t = (getattr(d, "opener", None) or {}).get("title") or {}
        style += f'color:{t.get("ink", d.accent)};'
        style += f'font-family:var(--font-{t.get("font", "body")});'
        if t.get("smallcaps"):
            style += "font-variant:small-caps;"
        if t.get("letter_spacing_pt"):
            style += f'letter-spacing:{t["letter_spacing_pt"]:.2f}pt;'
        style += f'font-weight:{t.get("weight", 700)};'
    return f'<div class="el {cls}" style="{style}">{body}</div>'


def page_measure(d, page):
    """(x0, x1) in points of THIS page's own text measure.

    The book's standard measure is right for a body page and WRONG for the chapter opener. The
    opener sets its section-contents list in a narrow rail at x 60-149pt and its opening prose
    beside it at x 173-534pt -- so the standard recto measure (60-420pt) swallows the contents
    rail, and every `3.1 Algae` / `3.2 Bryophytes` entry was flowed into the body column as if
    it were a paragraph, interleaved between the opening paragraphs. Measured on BIO11L ch3
    p001 and BIO12L ch6 p001; both openers did it.

    The extractor already measures each page's own columns, so the page is asked rather than
    assumed. The design's measure remains the fallback for a page with no measured column --
    a figure-only page, or a textless scan.
    """
    W = d.trim_pt[0]
    cols = page.get("columns") or []
    body_cols = [c for c in cols if c.get("name") in ("body", "full")]
    if body_cols:
        # The widest measured body column: a page split into two body columns is still one
        # measure as far as placement is concerned.
        x0 = min(c["x0"] for c in body_cols) * W
        x1 = max(c["x1"] for c in body_cols) * W
        if x1 - x0 > 0.25 * W:
            dx = (page.get("sheet_offset_pt") or [0.0, 0.0])[0]
            return x0 + dx, x1 + dx
    bx0, _, bx1, _ = d.text_box(page.get("page_side") or "recto")
    return bx0, bx1


def page_rail(d, page):
    """(x0, x1) of THIS page's margin rail -- everything outside its own measure.

    Derived from the page's measured measure rather than the book's standard one, for the same
    reason `page_measure` is: the opener's rail is at x 60-149pt, nowhere near the standard
    outer margin, so clamping its contents list into the standard rail squashed every entry
    into a 40pt-wide column.
    """
    W = d.trim_pt[0]
    mx0, mx1 = page_measure(d, page)
    left, right = mx0, W - mx1
    return (0.0, max(mx0 - 4.0, 20.0)) if left >= right else (min(mx1 + 4.0, W - 20.0), W)


def _split_measure_and_rail(d, page):
    """(body, rail) -- what sits in the text measure, and what sits in the outer margin.

    WHY THE BODY COLUMN FLOWS AND IS NOT ABSOLUTELY POSITIONED
    ----------------------------------------------------------
    Placing every block at its own measured y is exact only if the rendered block is exactly as
    tall as the printed one. It never quite is: a substitute face wraps a justified line a word
    earlier or later, and one extra wrapped line pushes a block past the next block's measured
    top. The result is text printed over text -- measured on BIO12L ch4 p060, where the body
    column ran straight through two marginal figures and their captions, and on BIO11L ch3 p036
    where list items `(i)`-`(vi)` stacked on top of each other.

    Nudging constants cannot fix that, because the error is cumulative and content-dependent.
    So the body column is laid out the way the page itself is: one column, in reading order,
    flowing. Collisions become impossible rather than unlikely. Vertical registration against
    the printed page is given up INSIDE a page -- which is the right trade, because the page
    still begins and ends where the book's does, and the words are all there and all readable.

    The outer rail keeps absolute placement: marginal figures and side notes genuinely sit at a
    measured height beside the prose, and they cannot collide with the column because they are
    on the other side of the measure.
    """
    mx0, mx1 = page_measure(d, page)
    W = d.trim_pt[0]
    body, rail = [], []
    for el in page["elements_in_reading_order"]:
        if el["role"] in FURNITURE_ROLES:
            continue
        bb = el.get("bbox_sheet") or el["bbox"]
        x0, x1 = bb[0] * W, bb[2] * W
        width = max(1.0, x1 - x0)
        overlap = max(0.0, min(x1, mx1) - max(x0, mx0))
        # More than a third of it inside the measure makes it part of the column. A figure that
        # starts in the margin and reaches well into the measure is a full-measure figure, not
        # a marginal one -- treating it as marginal is what let it sit under the prose.
        (body if overlap / width > 0.34 else rail).append(el)
    body.sort(key=lambda e: ((e.get("bbox_sheet") or e["bbox"])[1],
                             (e.get("bbox_sheet") or e["bbox"])[0]))
    return body, rail


def _rail_html(d, page, rail, fig_rel):
    """Marginal figures, side notes and the opener's contents rail, in the outer margin.

    THE RAIL IS ABSOLUTE BUT NOT BLINDLY SO. Placing each item at its own measured top has the
    same failure the body column had: a two-line entry that rewraps to three overruns the next
    entry's top. Measured on BIO12O ch7 p001, whose contents rail printed
    `7.3 What are the Evidences for Evolution?` straight through `7.4 What is Adaptive
    Radiation?`, and again on 7.5/7.6 and 7.6/7.7.

    So each item is placed at its measured top OR just below the previous item, whichever is
    lower. A well-separated marginal figure keeps its measured position exactly; a run of
    entries that would have collided is pushed down just enough not to. The printed height is
    the estimate, grown by a quarter to cover a substitute face setting the same words taller.
    """
    rx0, rx1 = page_rail(d, page)
    W, H = d.trim_pt
    out = []
    floor = None
    for el in sorted(rail, key=lambda e: ((e.get("bbox_sheet") or e["bbox"])[1],
                                          (e.get("bbox_sheet") or e["bbox"])[0])):
        bb = el.get("bbox_sheet") or el["bbox"]
        x0, y0, x1, y1 = bb[0] * W, bb[1] * H, bb[2] * W, bb[3] * H
        # Clamped to the rail: a block measured a few points into the measure would otherwise
        # be drawn over the first words of every line it sits beside.
        x0 = min(max(x0, rx0), rx1)
        x1 = min(max(x1, x0 + 10.0), rx1)
        if floor is not None and y0 < floor:
            y0 = floor
        slack = 1.25 if el["role"] not in ("figure", "table") else 1.0
        floor = y0 + max(6.0, (y1 - bb[1] * H) * slack) + 2.0
        style = f'left:{mm(x0):.2f}mm;top:{mm(y0):.2f}mm;width:{mm(x1 - x0):.2f}mm;'
        if el["role"] in ("figure", "table"):
            src = el.get("figure_file")
            if not src:
                continue
            out.append(f'<div class="el fig" style="{style}">'
                       f'<img src="{fig_rel}/{src}" alt=""></div>')
            continue
        body = runs_html(el)
        if not body.strip():
            continue
        size = (el.get("size_rel") or 1.0) * d.body_pt
        style += f"font-size:{size:.2f}pt;"
        pitch = el.get("line_pitch_pt")
        if pitch and (el.get("line_count") or 0) > 1:
            style += f"line-height:{pitch:.2f}pt;"
        cls = "cap" if el["role"] == "figure_caption" else "note"
        out.append(f'<div class="el {cls}" style="{style}">{body}</div>')
    return "".join(out)


def _flow_html(d, page, body, fig_rel):
    """The body column: every element in reading order, flowing inside the printed measure."""
    side = page.get("page_side") or "recto"
    x0, y0, x1, y1 = d.text_box(side)
    out = [f'<div class="measure" style="left:{mm(x0):.2f}mm;top:{mm(y0):.2f}mm;'
           f'width:{mm(x1 - x0):.2f}mm;">']
    W, H = d.trim_pt
    prev_bottom = None
    for el in body:
        bb = el.get("bbox_sheet") or el["bbox"]
        # The measured white space ABOVE this block, so the page keeps the book's own rhythm --
        # the gap before a section heading, the space around a figure -- without inheriting the
        # absolute positions that caused the collisions.
        gap_pt = 0.0
        if prev_bottom is not None:
            gap_pt = max(0.0, (bb[1] - prev_bottom) * H)
        prev_bottom = bb[3]
        margin = f"margin-top:{min(gap_pt, 26.0):.1f}pt;" if gap_pt > 1.5 else ""

        if el["role"] in ("figure", "table"):
            src = el.get("figure_file")
            if not src:
                continue
            w = min((bb[2] - bb[0]) * W, x1 - x0)
            out.append(f'<figure class="flow-fig" style="{margin}width:{mm(w):.2f}mm;">'
                       f'<img src="{fig_rel}/{src}" alt="'
                       f'{esc(el.get("table_text", ""))[:300]}"></figure>')
            continue
        inner = runs_html(el)
        if not inner.strip():
            continue
        size = (el.get("size_rel") or 1.0) * d.body_pt
        style = f"{margin}font-size:{size:.2f}pt;"
        pitch = el.get("line_pitch_pt")
        if pitch and (el.get("line_count") or 0) > 1:
            style += f"line-height:{pitch:.2f}pt;"
        role = el["role"]
        if role == "section_heading":
            style += f"color:{d.heading_ink};"
        elif role == "chapter_title":
            t = (getattr(d, "opener", None) or {}).get("title") or {}
            style += (f'color:{t.get("ink", d.accent)};'
                      f'font-family:var(--font-{t.get("font", "body")});'
                      f'font-weight:{t.get("weight", 700)};')
            if t.get("smallcaps"):
                style += "font-variant:small-caps;"
        cls = {"paragraph": "p", "list": "li", "section_heading": "h",
               "figure_caption": "cap", "side_note": "note",
               "contents_entry": "toc", "chapter_title": "title"}.get(role, "p")
        out.append(f'<div class="fl {cls}" style="{style}">{inner}</div>')
    out.append("</div>")
    return "".join(out)


def opener_grid_html(d, page, fig_rel):
    """The chapter-opening page as a real two-column GRID, or "" if this page is not one.

    WHY A GRID AND NOT COORDINATES
    ------------------------------
    The opener is the one page in the book with a genuine two-column structure: a narrow
    section-contents rail and the opening prose set beside it. Both reference pages the owner
    supplied build it exactly that way -- `grid-template-columns: 142px 536px` on the Class 11
    opener, `288px 501px` on the Class 12 one.

    Placing those blocks by measured coordinate instead produced two separate failures that no
    amount of nudging fixes. Where the rail fell inside the standard measure, every `3.1 Algae`
    entry was flowed into the prose column and printed BETWEEN the opening paragraphs. Where it
    did not, the entries were absolutely placed and the ones that rewrapped to two lines ran
    through the entry below them. A grid has neither failure mode available to it: the columns
    cannot interleave, and either column growing pushes its own content down.

    The column widths are still MEASURED -- taken from this page's own contents and prose
    boxes, so the proportions are the book's and not a guess.
    """
    entries = [e for e in page["elements_in_reading_order"] if e["role"] == "contents_entry"]
    if not entries:
        return ""
    W, H = d.trim_pt
    prose = [e for e in page["elements_in_reading_order"]
             if e["role"] in ("paragraph", "list", "section_heading")
             and ((e.get("bbox_sheet") or e["bbox"])[2]
                  - (e.get("bbox_sheet") or e["bbox"])[0]) * W > 0.25 * W]
    if not prose:
        return ""
    ebb = [e.get("bbox_sheet") or e["bbox"] for e in entries]
    pbb = [e.get("bbox_sheet") or e["bbox"] for e in prose]
    c_x0, c_x1 = min(b[0] for b in ebb) * W, max(b[2] for b in ebb) * W
    p_x0, p_x1 = min(b[0] for b in pbb) * W, max(b[2] for b in pbb) * W
    top = min(min(b[1] for b in ebb), min(b[1] for b in pbb)) * H
    gap = max(8.0, p_x0 - c_x1)
    # The rail is given the room the book gives it, with a floor so a two-word entry does not
    # collapse the column to the width of its longest word.
    c_w = max(c_x1 - c_x0, 90.0)

    c = (getattr(d, "opener", None) or {}).get("contents") or {}
    panel = ""
    if c.get("panel_fill"):
        r = c.get("panel_radius_pt", 0)
        pad = c.get("panel_pad_pt", 0)
        panel = (f'background:{c["panel_fill"]};'
                 f'border-radius:0 0 {mm(r):.1f}mm {mm(r):.1f}mm;'
                 f'padding:{mm(pad):.1f}mm {mm(pad * 0.7):.1f}mm;')

    out = [f'<div class="opener-grid" style="left:{mm(c_x0):.2f}mm;top:{mm(top):.2f}mm;'
           f'width:{mm(p_x1 - c_x0):.2f}mm;'
           f'grid-template-columns:{mm(c_w):.2f}mm 1fr;column-gap:{mm(gap):.2f}mm;">']
    out.append(f'<aside class="opener-toc" style="{panel}'
               f'color:{c.get("ink", d.accent)};'
               f'{"font-style:italic;" if c.get("italic") else ""}">')
    for e in entries:
        size = (e.get("size_rel") or 1.0) * d.body_pt
        out.append(f'<p style="font-size:{size:.2f}pt;">{runs_html(e)}</p>')
    out.append("</aside>")

    out.append('<article class="opener-prose">')
    for e in sorted(prose, key=lambda x: (x.get("bbox_sheet") or x["bbox"])[1]):
        inner = runs_html(e)
        if not inner.strip():
            continue
        size = (e.get("size_rel") or 1.0) * d.body_pt
        style = f"font-size:{size:.2f}pt;"
        pitch = e.get("line_pitch_pt")
        if pitch and (e.get("line_count") or 0) > 1:
            style += f"line-height:{pitch:.2f}pt;"
        if e["role"] == "section_heading":
            style += f"color:{d.heading_ink};"
            out.append(f'<div class="fl h" style="{style}">{inner}</div>')
        else:
            out.append(f'<div class="fl p" style="{style}">{inner}</div>')
    out.append("</article></div>")
    return "".join(out)


def opener_title_html(d, page):
    """`CHAPTER n` and the chapter title, at the position the opener prints them."""
    W, H = d.trim_pt
    out = []
    titles = [e for e in page["elements_in_reading_order"] if e["role"] == "chapter_title"]
    if not titles:
        return ""
    t = (getattr(d, "opener", None) or {}).get("title") or {}
    bbs = [e.get("bbox_sheet") or e["bbox"] for e in titles]
    x0 = min(b[0] for b in bbs) * W
    y0 = min(b[1] for b in bbs) * H
    style = (f'left:{mm(x0):.2f}mm;top:{mm(y0):.2f}mm;'
             f'width:{mm(W - x0 - 12):.2f}mm;'
             f'color:{t.get("ink", d.accent)};'
             f'font-family:var(--font-{t.get("font", "body")});'
             f'font-weight:{t.get("weight", 700)};')
    if t.get("smallcaps"):
        style += "font-variant:small-caps;"
    if t.get("letter_spacing_pt"):
        style += f'letter-spacing:{t["letter_spacing_pt"]:.2f}pt;'
    out.append(f'<header class="opener-title" style="{style}">')
    for e in sorted(titles, key=lambda x: (x.get("bbox_sheet") or x["bbox"])[1]):
        size = (e.get("size_rel") or 1.0) * d.body_pt
        out.append(f'<div style="font-size:{size:.2f}pt;">{runs_html(e)}</div>')
    out.append("</header>")
    return "".join(out)


def page_html(d, page, index, chapter_title, subject_name, edition, fig_rel):
    is_opener = index == 0
    parts = [f'<section class="sheet {page.get("page_side", "recto")}" '
             f'data-folio="{page.get("printed_page_number") or ""}">']
    if is_opener:
        parts.append(opener_html(d, page, fig_rel))
    else:
        parts.append(furniture_html(d, page, chapter_title, subject_name, edition, fig_rel))
    if is_opener:
        # The opener still carries the folio and the imprint.
        parts.append(furniture_html(d, page, chapter_title, subject_name, edition, fig_rel)
                     if not getattr(d, "opener", None) else
                     _opener_furniture(d, page, edition))
    grid = opener_grid_html(d, page, fig_rel) if is_opener else ""
    if grid:
        # The opener lays itself out: title block, then the contents/prose grid. Figures and
        # tables still get placed, but the text is the grid's.
        parts.append(opener_title_html(d, page))
        parts.append(grid)
        placed = {id(e) for e in page["elements_in_reading_order"]
                  if e["role"] in ("contents_entry", "chapter_title")
                  or (e["role"] in ("paragraph", "list", "section_heading"))}
        leftovers = [e for e in page["elements_in_reading_order"]
                     if id(e) not in placed and e["role"] in ("figure", "table",
                                                              "figure_caption", "side_note")]
        parts.append(_rail_html(d, page, leftovers, fig_rel))
    else:
        body, rail = _split_measure_and_rail(d, page)
        parts.append(_rail_html(d, page, rail, fig_rel))
        parts.append(_flow_html(d, page, body, fig_rel))
    parts.append("</section>")
    return "".join(parts)


def _opener_furniture(d, page, edition):
    """On the opening page the band is replaced by the opener art, but the folio and the
    imprint are still printed -- measured on BIO11L ch3 p001 (folio 23 in its white tab) and
    BIO12L ch6 p001 (the `Reprint 2026-27` line)."""
    out = []
    folio = getattr(d, "folio", None)
    n = page.get("printed_page_number")
    side = page.get("page_side") or "recto"
    # THE OPENER'S FOLIO AND RUNNING HEAD ARE PRINTED BUT NOT VISIBLE. The text layer of
    # BIO11L ch3 p001 carries `Plant Kingdom 23` at y 0.081 -- the same running-head line every
    # body page has -- but the opener's full-bleed artwork is drawn OVER it, so the book shows
    # neither. Drawing them on top of our render put a `23` and a chapter title in the green
    # head that the real page does not print. When the artwork is there, it covers them.
    if has_cut_header(page):
        folio = None
    if folio and n is not None and getattr(d, "opener", {}).get("kind") == "gradient":
        x_pt = folio["x_recto_pt"] if side == "recto" else folio["x_verso_pt"]
        r = mm(folio.get("radius_pt", 0))
        out.append(f'<div class="fx folio" style="left:{mm(x_pt):.2f}mm;'
                   f'top:{mm(folio["y0_pt"]):.2f}mm;width:{mm(folio["w_pt"]):.2f}mm;'
                   f'height:{mm(folio["h_pt"]):.2f}mm;background:{folio["fill"]};'
                   f'color:{folio["ink"]};border-radius:{r:.1f}mm {r:.1f}mm 0 0;'
                   f'font-family:var(--font-{folio["font"]});'
                   f'font-size:{folio["size_pt"]:.1f}pt;font-weight:700;'
                   f'justify-content:center;">{n}</div>')
    bar = getattr(d, "footer_bar", None)
    if bar:
        out.append(f'<div class="fx band" style="top:{mm(bar["y0_pt"]):.2f}mm;bottom:0;'
                   f'background:{bar["fill"]};"></div>')
    imp = getattr(d, "imprint", None)
    if imp:
        text = page.get("imprint") or d.imprint(edition)
        out.append(f'<div class="fx imprint" style="top:{mm(imp["y_pt"]):.2f}mm;'
                   f'font-family:var(--font-{imp["font"]});font-size:{imp["size_pt"]:.1f}pt;'
                   f'color:{imp["ink"]};">{esc(text)}</div>')
    return "".join(out)


CSS = """
*{box-sizing:border-box}
html{background:#8f9190}
body{margin:0;padding:8mm 0;font-family:var(--font-body);color:var(--ink);
     -webkit-print-color-adjust:exact;print-color-adjust:exact}
:root{
  --font-body:'NcertBody','Bookman Old Style',Bookman,Georgia,serif;
  --font-display:'NcertDisplay','Century Gothic',Avenir,Futura,sans-serif;
  --font-sans:Arial,Helvetica,sans-serif;
  --ink:@INK@;
}
/* ONE SHEET = ONE BOOK PAGE, at the book's real trim. Fixed, not minimum: a sheet that grows
   with its content is no longer a page, and printing then splits it across two. */
.sheet{position:relative;width:@PW@mm;height:@PH@mm;margin:0 auto 6mm;background:#fff;
       box-shadow:0 1px 5px rgba(0,0,0,.45);overflow:hidden}
/* Page furniture: absolutely placed from the measured design, full-bleed where the book bleeds. */
.fx{position:absolute;z-index:2}
/* Cut page artwork sits on the paper, UNDER the text the page sets over it. */
.fx.art{z-index:0;display:block}
.fx.band{left:0;right:0}
.fx.head{display:flex;align-items:center;white-space:nowrap}
.fx.folio{display:flex;align-items:center}
.fx.imprint{left:0;right:0;text-align:center}
/* Content: placed at its measured position, flowing inside its own measured width. */
.el{position:absolute;z-index:1;margin:0}
/* The body column: one flowing column at the book's own measure. Flowing rather than
   absolutely placing each block is what makes a collision impossible -- see
   _split_measure_and_rail for the pages this was measured on. */
.measure{position:absolute;z-index:1}
/* THE CHAPTER OPENER. A real two-column grid, as the book sets it and as the reference pages
   build it -- a contents rail beside the opening prose. Columns cannot interleave, so the
   section list can never again be flowed in between the opening paragraphs. */
.opener-grid{position:absolute;z-index:1;display:grid;align-items:start}
.opener-toc{align-self:start}
.opener-toc p{margin:0 0 .55em;line-height:1.3}
.opener-toc p:last-child{margin-bottom:0}
.opener-prose .fl.p{margin:0 0 .35em}
.opener-title{position:absolute;z-index:3}
.opener-title div{line-height:1.22;margin:0 0 .18em}
.fl{margin:0;text-align:justify;hyphens:auto}
.fl.h{font-weight:700;font-variant:small-caps;line-height:1.25;text-align:left}
.fl.cap{font-size:.92em;line-height:1.3;text-align:left}
.fl.note{line-height:1.3;text-align:left}
.fl.toc{line-height:1.35;text-align:left}
.fl.title{line-height:1.2;text-align:left}
.fl.li{text-align:left}
figure.flow-fig{margin:0 auto;padding:0}
figure.flow-fig img{display:block;width:100%;height:auto}
.el.p,.el.li{text-align:justify;line-height:@LEAD@;hyphens:auto}
.el.h{font-weight:700;font-variant:small-caps;line-height:1.25}
.el.cap{font-size:.9em;line-height:1.25}
.el.note{line-height:1.3}
.el.toc{line-height:1.3;white-space:normal}
.el.title{line-height:1.2}
.el.fig img{display:block;width:100%;height:auto}
.b{font-weight:700}
.i{font-style:italic}
.sc{font-variant:small-caps}
sup,sub{font-size:.7em;line-height:0}
/* A reading strip so the file is usable as a document, not only as a proof. */
.bar{position:sticky;top:0;z-index:50;background:#2f2f2f;color:#eee;padding:6px 14px;
     font:13px/1.4 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
     display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.bar b{font-weight:600}
.bar .tag{background:#4a4a4a;border-radius:3px;padding:1px 7px}
@page{size:@PW@mm @PH@mm;margin:0}
@media print{
  html,body{background:#fff;padding:0}
  .bar{display:none}
  .sheet{margin:0;box-shadow:none;break-after:page;page-break-after:always}
  .sheet:last-child{break-after:auto;page-break-after:auto}
}
"""


def render(layout, fig_rel="figures", title=None):
    book_id = layout["book_id"]
    d = design_lib.design_for(book_id)
    subject, klass, edition = design_lib.parse_book_id(book_id)
    subject_name = {"BIO": "Biology", "CHE": "Chemistry", "PHY": "Physics"}[subject]
    pages = layout["pages"]

    chapter_title = title or ""
    if not chapter_title:
        titles = [e["text"] for e in pages[0]["elements_in_reading_order"]
                  if e["role"] == "chapter_title"]
        # The opener prints "CHAPTER n" and the title as two elements; the title is the one
        # that is not just the chapter number.
        for t in titles:
            if not re.fullmatch(r"(?i)chapter\s*\d+", t.strip()):
                chapter_title = re.sub(r"(?i)^chapter\s*\d+\s*", "", t).strip()
                break
    W, H = d.trim_pt
    css = (CSS.replace("@PW@", f"{mm(W):.2f}").replace("@PH@", f"{mm(H):.2f}")
              .replace("@LEAD@", f"{d.leading}").replace("@INK@", d.ink))

    ed_word = {"L": "new", "O": "old"}[edition]
    body = [f'<div class="bar"><b>{esc(d.name)}</b>'
            f'<span class="tag">{ed_word} NCERT</span>'
            f'<span class="tag">chapter {layout["chapter_num"]}</span>'
            f'<span class="tag">{esc(chapter_title)}</span>'
            f'<span class="tag">{len(pages)} pages</span>'
            f'<span class="tag">{mm(W):.0f} x {mm(H):.0f} mm</span>'
            f'<span class="tag">{esc(book_id)}</span></div>']
    for i, page in enumerate(pages):
        body.append(page_html(d, page, i, chapter_title, subject_name, edition, fig_rel))

    head_title = f"{ed_word.title()} NCERT {d.name} - Chapter {layout['chapter_num']}"
    if chapter_title:
        head_title += f": {chapter_title}"
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(head_title)}</title>'
            f'<style>{embedded_fonts()}{css}</style></head>'
            f'<body>{"".join(body)}</body></html>')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", help="e.g. BIO11L-ch03")
    ap.add_argument("--layout", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--figures", default="figures")
    ap.add_argument("--title", default=None)
    ap.add_argument("--allow-unmeasured", action="store_true")
    a = ap.parse_args()

    if not design_lib.is_measured(a.chapter) and not a.allow_unmeasured:
        raise SystemExit(
            f"{a.chapter}: this book's page design has not been measured page by page yet.\n"
            f"Only {sorted(design_lib.MEASURED_KEYS)} have been. Re-run with --allow-unmeasured "
            f"to render it on the provisional design in book_design.py, knowing the result is "
            f"a draft, not a faithful render.")

    layout_path = a.layout or os.path.join(ROOT, "data", "_layouts", f"{a.chapter}.json")
    with open(layout_path, encoding="utf-8") as fh:
        layout = json.load(fh)
    out = a.out or os.path.join(ROOT, "data", f"{a.chapter}.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(render(layout, fig_rel=a.figures, title=a.title))
    print(f"{a.chapter}  {len(layout['pages'])} pages -> {out}")


if __name__ == "__main__":
    main()
