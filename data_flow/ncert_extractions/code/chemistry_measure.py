#!/usr/bin/env python3
"""Measures the PRINTED LAYOUT of an NCERT Inorganic Chemistry chapter straight from the source
PDF's own text and vector layer -- no agent, no page images, no eye-sampling.

    python3 scripts/inorganic_chemistry_measure.py CHE12L-ch05

Writes `exports/review/html_data/<CHAPTER>_inorganic_layout.json`.

WHY THIS EXISTS, AND WHY IT IS NOT STEP A2L
-------------------------------------------
Every other subject flow in this project gets its layout from step A2L, where an agent looks at a
rendered page image and reports what it sees. That is the right instrument for Biology and
Physics, whose NCERT sources are flat scans: a bitmap is genuinely all there is to measure.

The latest-edition Chemistry PDFs are not scans. `Chapter_5.pdf` carries a complete text layer
(fonts, sizes, colours, per-span origins) and a complete vector layer (every panel, tab, rule and
table fill as a real filled rectangle). Measuring those by asking an agent to look at a picture of
them throws away exact numbers and replaces them with estimates -- and it leaves holes, because an
agent step only runs on pages the runner has queued. Measured on CHE12L-ch05 at the time of
writing: A2L covered 14 of 23 pages, and the 9 it missed included p001, the chapter opener, which
is the single page whose layout matters most.

So this module reads the numbers instead of estimating them. It covers every page unconditionally,
it is deterministic (same PDF in, same JSON out, no run-to-run drift), and the colours it reports
are the book's own ink values rather than a pixel sampled near them.

WHAT IT DOES NOT DO
-------------------
It makes no judgement about CONTENT. Reading order, what a block means, whether a region is a
figure or a table, which words are bold -- all of that stays with A2/A2S/A2B/A2N exactly as in
every other flow, and `export_inorganic_chemistry_html.py` joins the two. This module answers only
"where is it printed, in what colour, at what size", which is a measurement, not a reading.
"""

import argparse
import collections
import json
import os
import sys

import pymupdf as fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402


# --------------------------------------------------------------------------------------------
# The book's measured typographic system.
#
# Read off the PDF itself (font name + point size + ink colour per span, counted across the
# chapter), not guessed. Every value here is a FACT about how NCERT sets Chemistry Class 12:
#
#   Bookman-Light       10.5  #231f20   body prose
#   Bookman-Demi        10.5  #6d6f71   bold run inside prose -- GREY, not black
#   Bookman-Demi        10.5  #6d6f71   numbered sub-heading (5.4.2 Optical Isomerism)
#   Bookman-DemiItalic   9.5  #6d6f71   lettered sub-heading ((a) Coordination entity)
#                                       and figure/table captions
#   BallroomTango       14.0  #231f20   margin section heading (5.2 Definitions of ...)
#   BallroomTango       24.0  #e11b22   "Objectives"
#   BallroomTango       13.0  #00aeef   "Example 5.4" / "Solution"
#   Crazy1              30.0  #231f20   chapter title on the opener
#   Garamond,Bold      110.0  #231f20   the unit numeral
#   Bookman-LightItalic  9.0  #ec008c   the opener's pink strap line
#   Bookman-Light        6.1/5.5        superscripts and subscripts
#
# The sizes are matched with a tolerance because a few spans sit a tenth of a point off.
_BODY_SIZE = 10.5
_SCRIPT_FONTS = ("BallroomTango", "Crazy1")

# Latin codepoints a Symbol-encoded face actually prints as Greek or as an arrow.
_SYMBOL_MAP = {"a": "\u03b1", "b": "\u03b2", "g": "\u03b3", "d": "\u03b4", "e": "\u03b5",
               "h": "\u03b7", "l": "\u03bb", "m": "\u03bc", "n": "\u03bd", "p": "\u03c0",
               "r": "\u03c1", "s": "\u03c3", "t": "\u03c4", "w": "\u03c9",
               "D": "\u0394", "S": "\u03a3", "W": "\u03a9",
               "\u00ae": "\u2192", "\u00ac": "\u2190", "\u00ad": "\u2191"}

# A span this much smaller than its line's dominant size is script-sized (a sub/superscript).
_SCRIPT_SIZE_RATIO = 0.80
# ... and then its BASELINE decides which: a superscript's origin sits above the line's, a
# subscript's below. Measured on p002: baseline 665.16, superscript 659.88 (-5.3), subscript
# 667.08 (+1.9). A tolerance of 1pt separates them with room to spare.
_BASELINE_EPS = 1.0

# Vector fills the book uses as furniture, keyed to what each one IS. Taken from the PDF's own
# fill values, so these are the book's inks rather than colours sampled near them.
_PANEL_TABS = {
    "#81c4e2": "example",     # worked-example panel: pale blue tab down the right edge
    "#fecb03": "feature",     # scientist portrait panel and feature box: yellow bar
    "#c8dc5c": "summary",     # end-of-chapter Summary: yellow-green bar
}
_MARGIN_BAR = "#f48480"       # the salmon bar beside Objectives and beside Exercises
_TABLE_HEAD = "#f48480"       # table header band (same ink as the margin bar)
_FOLIO_FILL = "#fecb03"       # folio tab and the rule that runs off the page from it
_OPENER_BANNER = "#d0afd3"    # lavender title panel on the chapter-opening page
_OPENER_STRIP = "#bc9dca"     # its darker foot
_OPENER_TAB = "#ffeda9"       # the cream tab that bleeds off the top edge behind the numeral
_HAIRLINE = "#939597"         # the thin rule around a white panel

# A drawing smaller than this is a glyph stroke or a diagram line, not furniture.
_MIN_FURNITURE_AREA = 300.0   # pt^2
# A page-sized OVERLAY -- the watermark bitmap and the paper background -- covers essentially the
# whole sheet and starts at or outside its corner.
#
# This was 0.70 x 0.50 of the sheet, which is not a page overlay, it is just "big": the Summary
# panel measures 0.768 x 0.549 and was discarded as an overlay on every page it runs across, so
# the chapter's single most distinctive panel never reached the render at all. The bar is now set
# where a genuine full-page object sits and nothing else does.
_FULLPAGE_W, _FULLPAGE_H = 0.95, 0.95
_FULLPAGE_ORIGIN = 0.03       # ... and begins within this fraction of the top-left corner


def _hex(colour):
    """A PyMuPDF colour (float triple, or a packed int) as #rrggbb, or None."""
    if colour is None:
        return None
    if isinstance(colour, (int, float)):
        v = int(colour)
        return "#%06x" % (v & 0xFFFFFF)
    try:
        r, g, b = colour[:3]
    except (TypeError, ValueError):
        return None
    return "#%02x%02x%02x" % (int(round(r * 255)), int(round(g * 255)), int(round(b * 255)))


# PyMuPDF hands back each ink as three floats, and float->byte rounding moves the last bit:
# the same yellow reads #fecb03 on one rect and #ffcb04 on the next, the same blue #81c4e2 and
# #81c5e2. Matching furniture by string equality therefore recognised NOTHING -- the first run of
# this module found 0 panels on a chapter that prints 23 of them. Colours are matched by distance
# instead, with a radius far tighter than the gap between any two inks this book uses.
_INK_TOL = 10   # max per-channel distance, in 0-255 units


def _rgb(hexstr):
    h = (hexstr or "").lstrip("#")
    if len(h) != 6:
        return None
    try:
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return None


def _is_ink(measured, named, tol=_INK_TOL):
    """True when a measured fill IS one of the book's named furniture inks."""
    a, b = _rgb(measured), _rgb(named)
    if not a or not b:
        return False
    return all(abs(x - y) <= tol for x, y in zip(a, b))


def _ink_name(measured, table, tol=_INK_TOL):
    """The table key whose ink this measured fill matches, or None."""
    for named, value in table.items():
        if _is_ink(measured, named, tol):
            return value
    return None


def _frac(rect, w, h):
    return [rect.x0 / w, rect.y0 / h, rect.x1 / w, rect.y1 / h]


def _near(a, b, tol=0.012):
    return abs(a - b) <= tol


def _is_page_overlay(r, w, h):
    """True for the watermark bitmap and the paper background: the two objects every page of this
    book carries that cover the whole sheet and mean nothing. Everything else, however large, is
    content -- see the note on _FULLPAGE_W."""
    return (r.width >= _FULLPAGE_W * w and r.height >= _FULLPAGE_H * h
            and r.x0 <= _FULLPAGE_ORIGIN * w and r.y0 <= _FULLPAGE_ORIGIN * h)


def _runs_from_line(line, block_size=None):
    r"""One printed line as a list of typed runs: [{"t": text, "v": ""|"sup"|"sub"}].

    This is the whole reason displayed formulae in this chapter can be set as TEXT rather than
    shipped as screenshots. NCERT prints `[Co(NH3)6]3+` as five separate spans at three different
    point sizes with three different baselines; `page.get_text()` flattens that to the literal
    string "[Co(NH3)6]3+", which is why every earlier render of this book showed chemistry with
    its subscripts inlined. The size and baseline that distinguish them are right there in the
    span records, so the distinction is recovered rather than approximated.

    The dominant size is taken by PRINTED WIDTH, not by span count: a line can carry more
    subscript spans than body spans (p002's "[CoCl2(NH3)4]+Cl-" has four of them), and counting
    spans would then elect the subscript size as the baseline size and mark the prose superscript.
    """
    spans = [s for s in line.get("spans") or [] if (s.get("text") or "").strip()]
    if not spans:
        return []
    width_by_size = collections.Counter()
    for s in spans:
        width_by_size[round(s["size"], 1)] += max(0.0, s["bbox"][2] - s["bbox"][0])
    base_size = width_by_size.most_common(1)[0][0]
    # A line carrying almost nothing BUT script text elects the script size as its own base and
    # then marks none of it. Real case: the tail of p004's paragraph wraps as a line holding just
    # "3+" (6.1pt, 7.4pt wide) and "." (10.5pt, 3.4pt wide), so the superscript outweighed the
    # body text and `[Co(NH3)6]3+` came out flat at the end of an otherwise correctly typeset
    # sentence. The BLOCK's dominant size is the stable reference; the line's own is used only
    # where the block has none.
    if block_size and base_size < block_size * _SCRIPT_SIZE_RATIO:
        base_size = block_size
    base_origin = None
    for s in spans:
        if _near(round(s["size"], 1), base_size, 0.05):
            base_origin = s["origin"][1]
            break
    if base_origin is None:
        # No span at the reference size on this line: take the largest one's baseline, which is
        # the closest thing to the body baseline the line actually has.
        base_origin = max(spans, key=lambda s: s["size"])["origin"][1]

    # The dominant INK of the line, so a run can record only where it departs from it. NCERT
    # colour-codes its chemistry -- amino groups magenta, halogens and leaving groups green -- and
    # that colouring is meaning, not decoration: it is how the book shows which part of a molecule
    # is doing the reacting.
    width_by_ink = collections.Counter()
    for s in spans:
        width_by_ink[_hex(s.get("color"))] += max(0.0, s["bbox"][2] - s["bbox"][0])
    base_ink = width_by_ink.most_common(1)[0][0] if width_by_ink else None

    runs = []
    for s in spans:
        variant = ""
        if s["size"] < base_size * _SCRIPT_SIZE_RATIO:
            delta = s["origin"][1] - base_origin
            if delta < -_BASELINE_EPS:
                variant = "sup"
            elif delta > _BASELINE_EPS:
                variant = "sub"
        face = (s.get("font") or "").split("+")[-1]
        italic = "Italic" in face or "Oblique" in face
        ink = _hex(s.get("color"))
        ink = ink if (ink and ink != base_ink) else None
        # A span set in a SYMBOL face carries Greek and arrows under Latin codepoints. Repairing
        # it here, where the face is still known, is the only place the distinction exists: by the
        # time the characters reach the model they are indistinguishable from ordinary prose.
        face = (s.get("font") or "").split("+")[-1]
        if face.startswith(("Symbol", "MT-Extra", "MTSY", "CMSY")):
            text = "".join(_SYMBOL_MAP.get(ch, ch) for ch in s["text"])
        else:
            text = s["text"].replace("\u00ae", "\u2192")
        if runs and runs[-1]["v"] == variant and runs[-1].get("i") == italic \
                and runs[-1].get("c") == ink:
            runs[-1]["t"] += text
        else:
            run = {"t": text, "v": variant}
            if italic:
                run["i"] = True
            if ink:
                run["c"] = ink
            runs.append(run)
    return runs


def _dedupe_fake_bold(lines):
    """Drop the repeated draws a fake-bold display font emits.

    BallroomTango (the script face NCERT sets its margin headings and Example labels in) has no
    bold weight, so the typesetter simulates one by printing the same string five times at
    sub-point offsets. PyMuPDF reports each draw as its own line, which is why the raw text layer
    reads "5.25.25.25.25.2 Definitions ofDefinitions of...". Measured on p004: three draws of
    "5.2" at origins (43.17, 75.93), (42.75, 75.93), (43.17, 75.51) -- same glyphs, under half a
    point apart. Collapsing lines that repeat an earlier line's text within ~1.5pt recovers the
    heading as printed.
    """
    kept = []
    for ln in lines:
        text = "".join(s.get("text", "") for s in ln.get("spans") or [])
        if not text.strip():
            continue
        org = (ln.get("spans") or [{}])[0].get("origin") or (0, 0)
        dup = False
        for prev_text, prev_org in kept:
            if prev_text == text and abs(prev_org[0] - org[0]) < 1.5 and abs(prev_org[1] - org[1]) < 1.5:
                dup = True
                break
        if dup:
            continue
        kept.append((text, org))
        yield ln


def _font_role(font, size, colour):
    """What KIND of type this is, from the measured (face, size, ink) triple."""
    f = font or ""
    base = f.split("+")[-1]
    if any(base.startswith(s) for s in _SCRIPT_FONTS):
        if base.startswith("Crazy"):
            return "chapter_title"
        if size >= 20:
            return "display_script"       # "Objectives" / "Unit"
        if colour == "#00aeef":
            return "panel_label"          # "Example 5.4" / "Solution"
        return "margin_heading"           # 5.2 Definitions of ...
    if base.startswith("Garamond"):
        return "unit_numeral"
    if base.startswith("Arial"):
        return "imprint"
    if base.startswith("Bookman-DemiItalic"):
        return "caption_or_letter_heading"
    if base.startswith("Bookman-Demi"):
        return "demi"                     # numbered sub-heading, table head, bold run
    if base.startswith("Bookman-LightItalic"):
        return "italic"
    return "body"


# How far apart two pieces of ink can sit and still belong to the same diagram, as a fraction of
# the sheet. Measured against this chapter: the widest real gap INSIDE one figure is the stem
# between the two halves of a mirror-image pair on p009 (about 0.03 of the page), while the
# narrowest gap BETWEEN two separate figures on a page is roughly 0.05. Sitting between them
# keeps the pairs whole without merging neighbours.
_CLUSTER_GAP = 0.038


def _cluster(ink, w, h):
    """Group raw strokes and images into the diagram REGIONS they form.

    Returns [(kind, fitz.Rect, stroke_count)]. Plain agglomeration on bounding boxes: start each
    stroke as its own region, then repeatedly merge any two regions whose boxes are within
    _CLUSTER_GAP of each other in both axes. The page has at most a few hundred strokes, so the
    quadratic pass costs nothing and avoids the tuning a grid or a tree would need.
    """
    regions = []
    for kind, r in ink:
        regions.append([kind, fitz.Rect(r), 1])

    gap_x, gap_y = _CLUSTER_GAP * w, _CLUSTER_GAP * h
    merged = True
    while merged:
        merged = False
        out = []
        for region in regions:
            for other in out:
                a, b = region[1], other[1]
                if (a.x0 <= b.x1 + gap_x and b.x0 <= a.x1 + gap_x
                        and a.y0 <= b.y1 + gap_y and b.y0 <= a.y1 + gap_y):
                    other[1] = fitz.Rect(min(a.x0, b.x0), min(a.y0, b.y0),
                                         max(a.x1, b.x1), max(a.y1, b.y1))
                    other[2] += region[2]
                    # An image anywhere in the region makes the whole region an image region:
                    # a photograph with a drawn frame around it is still a photograph.
                    if region[0] == "image":
                        other[0] = "image"
                    merged = True
                    break
            else:
                out.append(region)
        regions = out

    # A region of one or two strokes is a rule, an underline or a stray tick, not a diagram.
    # The threshold is on INK, not on area: a large sparse region (an axis pair) is real artwork,
    # a small dense one (a superscript bracket) is not.
    keep = []
    for kind, rect, n in regions:
        area = (rect.width / w) * (rect.height / h)
        if kind == "image" or n >= 6 or area > 0.01:
            keep.append((kind, rect, n))
    return sorted(keep, key=lambda t: (t[1].y0, t[1].x0))


def _repeated_overlays(doc):
    """Bounding boxes of the objects printed in the SAME place on nearly every page.

    The watermark is one of these and cannot be recognised any other way. It is an ordinary image
    object -- 1894x1894 px covering x 0.082-0.891, y 0.246-0.840 -- comfortably under any
    "is this the whole page" bar, so a size test leaves it in; and left in, it touches every
    diagram on the page at once and the stroke clustering collapses the whole page into one
    region. What actually distinguishes it is that it is the SAME rectangle on all 23 pages,
    which no real figure ever is. The paper background is caught by the same test.

    Returns a list of fractional [x0, y0, x1, y1]; anything matching one is skipped as furniture.
    """
    seen = collections.Counter()
    for i in range(doc.page_count):
        page = doc[i]
        w, h = page.rect.width, page.rect.height
        here = set()
        for im in page.get_image_info(xrefs=True):
            r = fitz.Rect(im["bbox"])
            if r.is_empty or r.width < 0.3 * w or r.height < 0.3 * h:
                continue        # only page-scale objects can be the watermark or the paper
            here.add(tuple(round(v, 2) for v in _frac(r, w, h)))
        for key in here:
            seen[key] += 1
    threshold = max(2, int(doc.page_count * 0.6))
    return [list(k) for k, n in seen.items() if n >= threshold]


def _matches_overlay(bbox_frac, overlays, tol=0.02):
    for o in overlays:
        if all(abs(a - b) <= tol for a, b in zip(bbox_frac, o)):
            return True
    return False


def _measure_page(page, page_num, overlays=()):
    w, h = page.rect.width, page.rect.height
    out = {
        "page": page_num,
        "width_pt": round(w, 2),
        "height_pt": round(h, 2),
        "text_blocks": [],
        "furniture": [],
        "panels": [],
        "art_regions": [],
    }

    # ---- text --------------------------------------------------------------------------
    sizes = collections.Counter()
    for bl in page.get_text("dict")["blocks"]:
        if bl.get("type") != 0:
            continue
        lines = list(_dedupe_fake_bold(bl.get("lines") or []))
        if not lines:
            continue
        block_width_by_size = collections.Counter()
        for ln in lines:
            for sp in ln.get("spans") or []:
                if (sp.get("text") or "").strip():
                    block_width_by_size[round(sp["size"], 1)] += max(
                        0.0, sp["bbox"][2] - sp["bbox"][0])
        block_size = (block_width_by_size.most_common(1)[0][0]
                      if block_width_by_size else None)
        line_recs, fonts = [], collections.Counter()
        for ln in lines:
            runs = _runs_from_line(ln, block_size)
            if not runs:
                continue
            spans = [s for s in ln["spans"] if (s.get("text") or "").strip()]
            lead = spans[0]
            role = _font_role(lead.get("font"), lead.get("size", 0), _hex(lead.get("color")))
            fonts[role] += 1
            for s in spans:
                sizes[round(s["size"], 1)] += max(0.0, s["bbox"][2] - s["bbox"][0])
            line_recs.append({
                "runs": runs,
                "bbox": [round(v, 4) for v in _frac(fitz.Rect(ln["bbox"]), w, h)],
                "size": round(lead.get("size", 0), 1),
                "color": _hex(lead.get("color")),
                "font": (lead.get("font") or "").split("+")[-1],
                "role": role,
            })
        if not line_recs:
            continue
        out["text_blocks"].append({
            "bbox": [round(v, 4) for v in _frac(fitz.Rect(bl["bbox"]), w, h)],
            "role": fonts.most_common(1)[0][0],
            "text": "".join(r["t"] for ln in line_recs for r in ln["runs"]),
            "lines": line_recs,
        })
    out["body_size_pt"] = sizes.most_common(1)[0][0] if sizes else _BODY_SIZE

    # ---- vector furniture --------------------------------------------------------------
    # Collected in paint order, because order carries meaning: the opener paints a white patch
    # OVER its folio tab to suppress it (the book prints no folio on a chapter-opening page), and
    # a flow that ignored that stamped a page number the book does not show.
    rects = []
    for dr in page.get_drawings():
        r = dr["rect"]
        if r.is_empty or r.width <= 0 or r.height <= 0:
            continue
        fill = _hex(dr.get("fill"))
        stroke = _hex(dr.get("color"))
        if _is_page_overlay(r, w, h):
            continue                                   # watermark / paper overlay
        # Anything fully outside the trim is the FACING page's furniture, bleeding across the
        # spread in the imposed file: p002 reports the opener's lavender banner at x -0.62..-0.03.
        # It is real ink, but it is not printed on this sheet.
        if r.x1 <= 0 or r.x0 >= w or r.y1 <= 0 or r.y0 >= h:
            continue
        area = r.width * r.height
        # A RULE is kept whatever its area: the folio bar measures 21.9 x 5.5pt (area 120), and a
        # 3pt thinness bar plus a 300pt^2 area bar between them discarded every folio in the
        # chapter -- the first run of this module found none at all.
        thin = r.width < 9 or r.height < 9
        if area < _MIN_FURNITURE_AREA and not thin:
            continue
        rects.append({"fill": fill, "stroke": stroke,
                      "bbox": [round(v, 4) for v in _frac(r, w, h)],
                      "pt": [r.x0, r.y0, r.x1, r.y1]})

    covered = [r for r in rects if _is_ink(r["fill"], "#ffffff", 4)]

    def _suppressed(rec):
        """True when a later white patch paints over this furniture (the opener's folio)."""
        x0, y0, x1, y1 = rec["bbox"]
        for c in covered:
            cx0, cy0, cx1, cy1 = c["bbox"]
            if cx0 <= x0 + 0.002 and cy0 <= y0 + 0.002 and cx1 >= x1 - 0.002 and cy1 >= y1 - 0.002:
                return True
        return False

    # Panels: a coloured tab bar paired with the white body it sits against.
    tabs = [r for r in rects if _ink_name(r["fill"], _PANEL_TABS)]
    bodies = [r for r in rects if _is_ink(r["fill"], "#ffffff", 4)
              and (r["bbox"][2] - r["bbox"][0]) > 0.3
              and (r["bbox"][3] - r["bbox"][1]) > 0.03]
    used_bodies = set()
    for tab in tabs:
        tx0, ty0, tx1, ty1 = tab["bbox"]
        best, best_gap = None, 9.0
        for i, body in enumerate(bodies):
            bx0, by0, bx1, by1 = body["bbox"]
            if min(ty1, by1) - max(ty0, by0) < 0.4 * (ty1 - ty0):
                continue                                # not vertically paired
            # Distance to WHICHEVER edge the tab abuts. Measuring only the right edge found
            # the two panels in this chapter whose tab is set right and missed the three whose
            # tab is set left (p007, p010, p014 all print it in the outer margin at x~0.10
            # against a body running to 0.925, which reads as a gap of 0.82 and was rejected).
            gap = min(abs(bx1 - tx0), abs(bx0 - tx1))
            if gap < best_gap:
                best, best_gap, best_i = body, gap, i
        if best is not None and best_gap < 0.06:
            used_bodies.add(best_i)
            x0 = min(best["bbox"][0], tx0)
            y0 = min(best["bbox"][1], ty0)
            x1 = max(best["bbox"][2], tx1)
            y1 = max(best["bbox"][3], ty1)
            out["panels"].append({
                "kind": _ink_name(tab["fill"], _PANEL_TABS),
                "tab_fill": tab["fill"],
                # By CENTRE, not by edge. The tab is painted to OVERLAP the panel's edge, so
                # "does the tab start after the panel ends" is false for every tab in the book and
                # reported all of them as left-hand tabs, which is the one side the book never
                # prints them on.
                "tab_side": ("right" if (tx0 + tx1) / 2 > (best["bbox"][0] + best["bbox"][2]) / 2
                             else "left"),
                "tab_width_frac": round(tx1 - tx0, 4),
                "bbox": [round(x0, 4), round(y0, 4), round(x1, 4), round(y1, 4)],
                "body_bbox": best["bbox"],
            })

    for rec in rects:
        fill = rec["fill"]
        x0, y0, x1, y1 = rec["bbox"]
        wfrac, hfrac = x1 - x0, y1 - y0
        if _is_ink(fill, _FOLIO_FILL) and hfrac < 0.03 and wfrac < 0.10 and y0 > 0.85:
            if not _suppressed(rec):
                out["furniture"].append({"role": "folio_tab", "fill": fill, "bbox": rec["bbox"]})
        elif _is_ink(fill, _FOLIO_FILL) and hfrac < 0.01 and y0 > 0.85:
            if not _suppressed(rec):
                out["furniture"].append({"role": "folio_rule", "fill": fill, "bbox": rec["bbox"]})
        elif _is_ink(fill, _MARGIN_BAR) and wfrac < 0.06 and hfrac > 0.08:
            out["furniture"].append({"role": "margin_bar", "fill": fill, "bbox": rec["bbox"]})
        elif _is_ink(fill, _TABLE_HEAD) and wfrac > 0.2:
            out["furniture"].append({"role": "table_head", "fill": fill, "bbox": rec["bbox"]})
        elif _is_ink(fill, _OPENER_BANNER) and wfrac > 0.25 and hfrac > 0.08:
            # Size-gated on purpose. p019's figure is a SHADED drawing whose gradient is emitted
            # as ~250 one-pixel strips, every one of them within tolerance of the opener's
            # lavender; ungated, that single figure filed 250 chapter banners on one page.
            out["furniture"].append({"role": "opener_banner", "fill": fill, "bbox": rec["bbox"]})
        elif _is_ink(fill, _OPENER_STRIP) and wfrac > 0.25:
            out["furniture"].append({"role": "opener_strip", "fill": fill, "bbox": rec["bbox"]})
        elif _is_ink(fill, _OPENER_TAB) and wfrac > 0.05 and hfrac > 0.05:
            out["furniture"].append({"role": "opener_tab", "fill": fill, "bbox": rec["bbox"]})

    # ---- artwork -----------------------------------------------------------------------
    # A diagram's ink: vector strokes and real images that are NOT furniture and NOT the
    # page-sized overlays.
    #
    # These must be CLUSTERED, not listed. A chemical structure is drawn as hundreds of
    # individual strokes -- one per bond, one per arc, one per arrowhead -- so the raw list ran to
    # 6483 entries across this chapter, which names no diagrams at all. What the exporter needs is
    # the handful of REGIONS those strokes form, so that a figure block from A2 can be matched to
    # the artwork it refers to and cropped at exactly its extent.
    ink = []
    for dr in page.get_drawings():
        r = dr["rect"]
        if r.is_empty:
            continue
        if _is_page_overlay(r, w, h):
            continue
        fill = _hex(dr.get("fill"))
        if _ink_name(fill, _PANEL_TABS) or any(
                _is_ink(fill, named) for named in (_FOLIO_FILL, _MARGIN_BAR, _TABLE_HEAD,
                                                   _OPENER_BANNER, _OPENER_STRIP, _OPENER_TAB,
                                                   "#ffffff")):
            continue
        # The watermark's own path is a single black rect 0.081-0.892 x 0.245-0.840 on EVERY
        # page -- under the full-page bar but far larger than any diagram. Left in, it bridged
        # every separate figure on a page into one cluster, so each page reported exactly one
        # enormous "diagram" covering all its artwork.
        if (r.width * r.height) > 0.30 * w * h:
            continue
        ink.append(("vector", r))
    for im in page.get_image_info(xrefs=True):
        r = fitz.Rect(im["bbox"])
        if r.is_empty:
            continue
        if _is_page_overlay(r, w, h) or _matches_overlay(_frac(r, w, h), overlays):
            continue                                   # watermark / paper
        if r.width < 4 or r.height < 4:
            continue                                   # gradient slivers of a tinted panel
        ink.append(("image", r))
    out["art_regions"] = [
        {"kind": kind, "strokes": n,
         "bbox": [round(v, 4) for v in _frac(rect, w, h)]}
        for kind, rect, n in _cluster(ink, w, h)
    ]

    # ---- columns -----------------------------------------------------------------------
    # Derived from where body-sized prose is actually SET, which is the only honest measure of a
    # column. NCERT Chemistry prints a narrow left margin column (section headings, small
    # structural diagrams and figure captions) and a wide body column beside it; some pages leave
    # the margin empty and some run figures across both.
    body_x = [(b["bbox"][0], b["bbox"][2]) for b in out["text_blocks"]
              if b["role"] in ("body", "italic", "demi") and (b["bbox"][2] - b["bbox"][0]) > 0.25]
    if body_x:
        out["body_column"] = [round(min(x0 for x0, _ in body_x), 4),
                              round(max(x1 for _, x1 in body_x), 4)]
    else:
        out["body_column"] = None
    margin_x = [(b["bbox"][0], b["bbox"][2]) for b in out["text_blocks"]
                if b["role"] in ("margin_heading", "caption_or_letter_heading")
                and b["bbox"][2] < (out["body_column"][0] if out["body_column"] else 0.30) + 0.02]
    out["margin_column"] = ([round(min(x0 for x0, _ in margin_x), 4),
                             round(max(x1 for _, x1 in margin_x), 4)] if margin_x else None)
    return out


def measure(pdf_path):
    """The whole chapter measured. Returns the dict this module writes to disk."""
    doc = fitz.open(pdf_path)
    overlays = _repeated_overlays(doc)
    pages = [_measure_page(doc[i], i + 1, overlays) for i in range(doc.page_count)]
    widths = collections.Counter((p["width_pt"], p["height_pt"]) for p in pages)
    trim = widths.most_common(1)[0][0]
    body = collections.Counter(p["body_size_pt"] for p in pages).most_common(1)[0][0]

    # The text measure, taken across the chapter rather than per page, so a page that happens to
    # carry one short paragraph does not define its own narrower column.
    lefts = [p["body_column"][0] for p in pages if p.get("body_column")]
    rights = [p["body_column"][1] for p in pages if p.get("body_column")]
    margins = [p["margin_column"] for p in pages if p.get("margin_column")]
    doc.close()
    return {
        "chapter_source": os.path.basename(pdf_path),
        "what_this_file_is": (
            "Measured printed layout of one NCERT Inorganic Chemistry chapter, read directly from "
            "the source PDF's text and vector layer by scripts/inorganic_chemistry_measure.py. "
            "Unlike step A2L (an agent looking at a page image) this is exact and covers every "
            "page, because the latest-edition Chemistry PDFs are not scans -- every panel, tab, "
            "rule and table fill is a real vector rectangle and every glyph carries its own font, "
            "size, colour and baseline."
        ),
        "produced_by": "scripts/inorganic_chemistry_measure.py",
        "trim_pt": [trim[0], trim[1]],
        "trim_mm": [round(trim[0] / 72 * 25.4, 2), round(trim[1] / 72 * 25.4, 2)],
        "body_size_pt": body,
        "text_measure": {
            "body_column": [round(sorted(lefts)[len(lefts) // 2], 4),
                            round(sorted(rights)[len(rights) // 2], 4)] if lefts else [0.30, 0.90],
            "margin_column": [round(min(m[0] for m in margins), 4),
                              round(max(m[1] for m in margins), 4)] if margins else None,
        },
        "palette": {
            "body_ink": "#231f20", "furniture_ink": "#6d6f71",
            "panel_label_ink": "#00aeef", "objectives_ink": "#e11b22",
            "strapline_ink": "#ec008c",
            "example_tab": "#81c4e2", "feature_tab": _FOLIO_FILL,
            "summary_tab": "#c8dc5c", "margin_bar": _MARGIN_BAR,
            "table_head": _TABLE_HEAD, "folio": _FOLIO_FILL, "hairline": _HAIRLINE,
            "opener_banner": _OPENER_BANNER, "opener_strip": _OPENER_STRIP,
            "opener_tab": _OPENER_TAB,
        },
        "page_overlays_ignored": overlays,
        "pages_measured": len(pages),
        "pages": pages,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", help="e.g. CHE12L-ch05")
    ap.add_argument("--pdf", required=True, help="path to the source PDF for this chapter")
    args = ap.parse_args()
    if not os.path.exists(args.pdf):
        print("source PDF not found: " + args.pdf, file=sys.stderr)
        return 1

    data = measure(args.pdf)
    data["chapter"] = args.chapter
    out_dir = rc.pp("exports", "review", "html_data")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, args.chapter + "_inorganic_layout.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    n_panels = sum(len(p["panels"]) for p in data["pages"])
    n_art = sum(len(p["art_regions"]) for p in data["pages"])
    print("%s: %d pages measured" % (args.chapter, data["pages_measured"]))
    print("  trim          : %.1f x %.1f pt  (%.1f x %.1f mm)"
          % (data["trim_pt"][0], data["trim_pt"][1], data["trim_mm"][0], data["trim_mm"][1]))
    print("  body type     : %.1f pt" % data["body_size_pt"])
    print("  body column   : %s" % (data["text_measure"]["body_column"],))
    print("  margin column : %s" % (data["text_measure"]["margin_column"],))
    print("  panels found  : %d   art regions: %d" % (n_panels, n_art))
    print("wrote " + os.path.relpath(path, rc.pp()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
