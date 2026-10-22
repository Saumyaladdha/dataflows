#!/usr/bin/env python3
"""Builds a side-by-side HTML review page for one NCERT chapter: the original scanned PDF page
on the left, this pipeline's extracted data on the right, page by page.

    python3 scripts/export_ncert_chapter_html.py PHY12O-ch01 \\
        --pdf "/path/to/Old_ncert_Physics_Chapter_1.pdf"

Writes `exports/review/<CHAPTER>_REVIEW.html` plus `exports/review/<CHAPTER>_html_pages/*.png`
(one full-page render per page, for the left column). Figure/table crops reuse the files already
written by `export_ncert_chapter_review.py` under `exports/review/<CHAPTER>_figures/` -- run that
script first (or this one still works without it, it just won't find crops to show).

This is a REVIEW AID, not a pipeline deliverable, same as the Markdown exporter it shares data
loading with (see that module's docstring for the three defects an earlier version had, now
fixed in the shared helpers both scripts import). It exists so a person can SEE the original page
and the extraction next to each other and judge quality directly, without opening the PDF
separately.
"""

import argparse
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
import lib.pdf as lib_pdf  # noqa: E402
from export_ncert_chapter_review import (  # noqa: E402
    _best_page_outputs,
    _load_sibling_json,
    _crop_for,
    _mark_target_box,
    _trim_caption_band,
)

_PAGE_DPI = 170  # full-page render for the left column -- readable without being huge on disk


def _esc(s):
    return html.escape(s or "", quote=False)


def _bold_applied(text, bold_terms):
    """Wrap each bold term in <strong>, longest-first so a shorter term inside a longer one
    doesn't steal the match (mirrors the Markdown exporter's same longest-first rule)."""
    text = _esc(text)
    for term in sorted(bold_terms or [], key=len, reverse=True):
        esc_term = _esc(term)
        if esc_term in text:
            text = text.replace(esc_term, f"<strong>{esc_term}</strong>", 1)
    return text


_LATEX_ENVS = ("\\begin{", "\\aligned", "\\gathered", "\\matrix", "\\cases", "\\array")


# A2S's documented unsure form for an equation is the literal string "unsure" in `latex`. It is a
# declaration that nothing was transcribable, NOT a transcription -- rendering it as maths printed
# the word "unsure" where PHY12O-ch01 p022 should show E_A = 7.2 x 10^4 N C^-1, and the page still
# reported "Every block on this page is transcribed".
_UNSURE_LATEX = {"unsure", "unsure.", "n/a", "none", "-"}


def _is_real_latex(latex):
    t = (latex or "").strip().lower().rstrip(".")
    return bool(t) and t not in _UNSURE_LATEX


def _table_fit_style(n_cols):
    """Inline font-size for a table, stepped down by column count so a wide one fits the measure.

    A printed sheet has no scrollbar, so a table wider than the measure is not scrolled but cut.
    Scaling the type is the only content-preserving option in CSS: a 20-column table set small is
    readable, a 20-column table with 14 columns missing is not. Thresholds are deliberately coarse
    -- the aim is "all of it on the page", not typographic perfection.
    """
    if n_cols <= 6:
        return ""
    # Harder than first set. At 0.48em a 20-column table still overran the measure, and with
    # `overflow-x: visible` it bled past the trim -- turning a contained-but-clipped table into an
    # uncontained one, which cost CHE11L-ch02 eight sheets and three blank pages. The table has to
    # actually FIT, so the steps go down far enough that it does.
    scale = (0.80 if n_cols <= 10 else
             0.55 if n_cols <= 14 else
             0.34 if n_cols <= 20 else
             0.26)
    return f' style="font-size: {scale:.2f}em;"'


def _latex_for_display(latex):
    r"""Make an A2S latex string safe to render as DISPLAY math.

    KaTeX only accepts `\\` (a line break) inside an alignment environment. A2S legitimately
    returns multi-line derivations with bare `\\` -- the step's own brief tells transcribers to
    join a two-line printed derivation into one `latex` value, because the schema has a single
    latex field per block. Rendered as-is those throw, and with throwOnError the reader sees red
    source text instead of an equation. Wrapping them in `aligned` is the fix, and it is also
    what the page actually shows: consecutive lines of one derivation.
    """
    s = (latex or "").strip()
    if "\\\\" in s and not any(env in s for env in _LATEX_ENVS):
        return "\\begin{aligned}" + s + "\\end{aligned}"
    return s


def _column_map_for_page(layout, page_num, derive=False):
    """({block_n: column}, {column_id: (x0, x1)}) measured by A2L for this page, else ({}, {}).

    This is what makes the render match the book's ARRANGEMENT rather than just its colours:
    NCERT's chapter-opening page sets the section-contents panel in a narrow LEFT column with
    the opening prose running beside it on the RIGHT, and several body pages narrow the text
    beside a figure. Stacking every block in one column -- what this exporter did before -- loses
    that entirely.
    """
    page_key = f"page_{page_num:03d}"
    detail = ((layout or {}).get("full_detail_by_page") or {}).get(page_key) or {}
    els = detail.get("elements_in_reading_order") or []

    # The column is derived from each element's MEASURED bbox, not from its `column` label.
    # The labels disagree with the agents' own measurements: on PHY12O-ch01 p006 the page is
    # declared a single `full` column spanning x 0.127-0.903, while the very bboxes beneath it put
    # FIGURE 1.4 at x 0.127-0.296 and every line of text at x 0.313-0.903 -- plainly two columns.
    # Chapter-wide 621 elements claim `full` on that evidence. Trusting the label meant no figure
    # ever floated and no prose ever wrapped beside one, which is the whole of the gap between our
    # 10% ink and the book's 20%. The bboxes are a measurement; the label is a summary of it, and
    # where they conflict the measurement wins.
    def _is_side_tab(e):
        """A filled element over 3x taller than it is wide is a rotated side tab -- furniture
        belonging to a box, not a column of the page. Counting it as a column squeezed a worked
        example into a third of the measure with its own tab stranded in a separate column to the
        right and two-thirds of the sheet left empty (p017: box measured x 0.127-0.666, tab
        x 0.696-0.738, and the renderer made those two facing columns). Running prose never takes
        that shape, so the test is safe."""
        bb = e.get("bbox")
        if not e.get("fill") or not isinstance(bb, list) or len(bb) != 4:
            return False
        return (bb[3] - bb[1]) > 3 * (bb[2] - bb[0])

    body = [e for e in els
            if e.get("role") not in ("page_header_band", "footer_rule", "rule_bar", "page_number",
                                     "running_header", "chapter_banner", "qr_code",
                                     "decorative_image")
            and isinstance(e.get("bbox"), list) and len(e["bbox"]) == 4
            and not _is_side_tab(e)]
    # The measure is the FULL printed text block -- every body element's extent, narrow ones
    # included. Taking only the wide elements measured just the TEXT column, against which that
    # column is by definition 100% wide, so nothing on the page ever looked like a column at all.
    measure = None
    if body:
        measure = (min(e["bbox"][0] for e in body), max(e["bbox"][2] for e in body))

    def _side(el):
        """'left'/'right' when this element shares a horizontal band with something beside it,
        else None -- i.e. it really is one of two columns rather than full measure."""
        if measure is None:
            return None
        x0, y0, x1, y1 = el["bbox"]
        span = (x1 - x0) / max(1e-6, measure[1] - measure[0])
        if span > 0.62:                      # occupies most of the measure: it is full width
            return None
        for other in body:
            if other is el:
                continue
            ox0, oy0, ox1, oy1 = other["bbox"]
            # NO width test on the neighbour. Gating it the same way as the element itself was the
            # bug: on p006 the prose beside FIGURE 1.4 spans 0.76 of the measure, so it was skipped
            # as "full width" and the figure concluded nothing sat beside it at all. What makes a
            # narrow element a column is that SOMETHING is printed alongside it, whatever that
            # thing's own width -- and the wide text column is exactly what wraps around the float.
            # vertical overlap of at least a third of the shorter element
            ov = min(y1, oy1) - max(y0, oy0)
            if ov <= 0 or ov < 0.33 * min(y1 - y0, oy1 - oy0):
                continue
            if ox0 >= x1 - 0.01:             # something sits to our RIGHT -> we are the left col
                return "left"
            if ox1 <= x0 + 0.01:             # something sits to our LEFT  -> we are the right col
                return "right"
        return None

    by_n = {}
    derived = {"left": [], "right": []}
    for el in els:
        n = el.get("n")
        side = _side(el) if derive else None
        if side:
            derived[side].append(el["bbox"])
        if not isinstance(n, int):
            continue
        col = side or el.get("column")
        if col:
            by_n[n] = col
    cols = {}
    for c in (((layout or {}).get("column_layout_by_page") or {}).get(page_key) or {}
              ).get("columns_left_to_right") or []:
        cid = c.get("id")
        x0 = c.get("starts_at_fraction_of_page_width")
        x1 = c.get("ends_at_fraction_of_page_width")
        if cid and isinstance(x0, (int, float)) and isinstance(x1, (int, float)):
            cols[cid] = (x0, x1)
    # Where the agent declared no side columns but the geometry shows them, take each side's
    # bounds from the MEASURED extent of the elements actually sitting in it. Without this the
    # exporter fell back to a flat 48% for every float, so FIGURE 1.4 -- which the book prints
    # 0.169 of the page wide, about a quarter of the measure -- came out nearly twice its size
    # and pushed the prose that should wrap beside it off the page.
    for side, boxes in derived.items():
        if boxes and side not in cols:
            cols[side] = (min(b[0] for b in boxes), max(b[2] for b in boxes))
    return by_n, cols


def _style_map_for_page(layout, page_num):
    """{block_n: {"fill":..., "ink":...}} measured for THIS page's blocks.

    The consolidated palette keeps one colour per role for the whole chapter, which is right for a
    consistently-designed book and wrong for one that is not. Physics measures FOUR box designs --
    grey #dbdcde worked examples (51), pale blue #c6eafb feature boxes (5), a blue #9cdcf8
    scientist panel (1) and grey #d1d2d4 "Points to Ponder" (2) -- and TWO section-heading inks
    (#6d6e71 for x.y headings, #00adef for x.y.z). Collapsing those to one fill and one ink made
    every box look alike and half the headings the wrong colour. The per-element measurement was
    there all along; this reads it instead of discarding it.
    """
    rec = ((layout or {}).get("full_detail_by_page") or {}).get(f"page_{page_num:03d}") or {}
    out = {}
    for el in rec.get("elements_in_reading_order") or []:
        n = el.get("n")
        if not isinstance(n, int):
            continue
        style = {}
        if el.get("fill"):
            style["fill"] = el["fill"]
        if el.get("text_color"):
            style["ink"] = el["text_color"]
        if el.get("role"):
            style["role"] = el["role"]
        if el.get("font"):
            style["font"] = el["font"]
        if style:
            out[n] = style
    return out


def _role_map_for_page(layout, page_num):
    """{block_n: measured role} from A2L, e.g. chapter_title / section_heading / major_heading.

    Without this the exporter guessed a heading's rank from its TEXT -- all-caps and short meant
    "chapter title" -- and got it badly wrong on CHE12L-ch09 p001: "I. AMINES" is all-caps and
    short, so it was wrapped in the full lavender chapter banner, while the real title "Amines"
    was demoted. The measurement says plainly what each one is: "I. AMINES" is a `major_heading`
    set at size_rel 1.0 (body-text size), "Amines" is the `chapter_title` at 3.0. Measured rank
    beats a text heuristic every time, so it wins wherever a measurement exists.
    """
    page_key = f"page_{page_num:03d}"
    detail = ((layout or {}).get("full_detail_by_page") or {}).get(page_key) or {}
    out = {}
    for el in detail.get("elements_in_reading_order") or []:
        n, role = el.get("n"), el.get("role")
        if isinstance(n, int) and role:
            out[n] = role
    return out


def _box_furniture_for_page(layout, page_num):
    """The coloured furniture the book prints ON this page's boxes, from A2L's own measurement.

    NCERT physics does not print a plain tinted rectangle. Measured off
    Old_ncert_Physics_Chapter_1.pdf at 144dpi, a worked example on p021 is a grey #dbdcde panel
    x 0.113-0.686 with a 9pt #00adef rule down its INNER edge, a 6pt white gap, and a 25.5pt
    #00adef TAB at x 0.696-0.738 carrying "EXAMPLE 1.8" in white caps, set vertically and
    bottom-aligned (text y 668-728 against a tab ending at 734.5). The Coulomb panel on p011 is
    the same device at a different scale: pale #9cdcf8 body x 0.579-0.833, a 4.5pt gap, then a
    19.5pt #00adef tab x 0.840-0.873 reading "CHARLES AUGUSTIN DE COULOMB (1736 -1806)". A
    feature box instead gets a TITLE BAR along its top edge -- p003's runs x 0.255-0.712 at the
    panel's own top (both at y 0.287), 24pt tall, white small caps on #00adef.

    A2L records every one of these as an unnumbered `major_heading` carrying a fill, so this is a
    read of the measurement rather than a new guess. Returns
    {"tabs": [...], "bars": [...], "bbox": {n: bbox}, "fill": {n: fill}, "inside_box": {n}}
    where `inside_box` is the set of FIGURE blocks whose measured bbox sits wholly inside a box's
    -- the portrait in a scientist panel, which the book prints inside the panel and we were
    rendering as a second tinted box floating above it.
    """
    rec = ((layout or {}).get("full_detail_by_page") or {}).get(f"page_{page_num:03d}") or {}
    els = [e for e in rec.get("elements_in_reading_order") or []
           if isinstance(e.get("bbox"), list) and len(e["bbox"]) == 4]
    boxes = [e for e in els if e.get("role") == "box"]
    tabs, bars = [], []
    for e in els:
        if e.get("role") not in ("major_heading", "section_heading") or not e.get("fill"):
            continue
        x0, y0, x1, y1 = e["bbox"]
        w, h = x1 - x0, y1 - y0
        if h > 3 * w:
            # SHAPE decides, not whether A2L matched a block number to it. A filled element three
            # times taller than it is wide, carrying light text, is a rotated side tab -- that is
            # not a shape running prose ever takes. Skipping every numbered element here is what
            # dropped the Coulomb panel's title bar: one A2L read left it unnumbered (so it was
            # painted) and the re-read correctly matched it to block 8 (so it vanished), for a
            # page whose printed design had not changed at all. The block number is useful rather
            # than disqualifying -- it tells us WHICH text belongs on the tab -- so it is carried
            # through as `n` and the block is suppressed from the body flow by the caller.
            tabs.append({"bbox": e["bbox"], "fill": e["fill"], "n": e.get("n"),
                         "ink": e.get("text_color") or "#ffffff"})
        elif e.get("n") is not None:
            # Anything else numbered really is the page's own text; a wide filled heading is only
            # a box title bar when A2L left it unnumbered.
            continue
        elif w > 3 * h and any(abs(b["bbox"][1] - y0) < 0.02 for b in boxes):
            bars.append({"bbox": e["bbox"], "fill": e["fill"],
                         "ink": e.get("text_color") or "#ffffff"})
    inside = set()
    for e in els:
        if e.get("role") != "figure" or not isinstance(e.get("n"), int):
            continue
        fx0, fy0, fx1, fy1 = e["bbox"]
        for b in boxes:
            bx0, by0, bx1, by1 = b["bbox"]
            if bx0 - 0.01 <= fx0 and fx1 <= bx1 + 0.01 and by0 - 0.01 <= fy0 and fy1 <= by1 + 0.01:
                inside.add(e["n"])
                break
    return {
        "tabs": tabs, "bars": bars, "inside_box": inside,
        # Blocks whose whole content IS a rotated tab. The caller must not render these in the
        # body flow as well, or the scientist's name appears twice -- once painted on the bar and
        # once as a stray cyan heading in the prose, which is exactly what p011 was doing.
        "tab_blocks": {t["n"] for t in tabs if isinstance(t.get("n"), int)},
        "bbox": {e["n"]: e["bbox"] for e in els if isinstance(e.get("n"), int)},
        "fill": {b["n"]: b["fill"] for b in boxes
                 if isinstance(b.get("n"), int) and b.get("fill")},
    }


def _page_panel_for_page(layout, page_num):
    """The page-wide tinted panel this page's body sits inside, or None.

    SUMMARY (pp.42-44) and POINTS TO PONDER (pp.45-46) are not boxes around a block -- the whole
    page body is printed on a tint, measured as an unnumbered `box` spanning the full text block
    (p042's is #c6eafb x 0.314-0.901, y 0.135-0.937; p045's is #d1d2d4 x 0.098-0.685). Because it
    carries no `n` it never reached a block, so those five pages rendered as plain white. The
    SUMMARY pages also print a grey margin band beside the panel (p042: #d1d2d4 x 0.2198-0.3039
    with a 12.5pt #00adef rule inside it at x 0.2721-0.2925), recorded as a `decorative_image`.
    """
    rec = ((layout or {}).get("full_detail_by_page") or {}).get(f"page_{page_num:03d}") or {}
    els = [e for e in rec.get("elements_in_reading_order") or []
           if isinstance(e.get("bbox"), list) and len(e["bbox"]) == 4]
    best = None
    for e in els:
        if e.get("role") != "box" or e.get("n") is not None or not e.get("fill"):
            continue
        x0, y0, x1, y1 = e["bbox"]
        # "the whole page body": at least half the sheet wide and three quarters of it tall.
        if (x1 - x0) > 0.50 and (y1 - y0) > 0.70:
            if best is None or (y1 - y0) > (best["bbox"][3] - best["bbox"][1]):
                best = {"bbox": e["bbox"], "fill": e["fill"]}
    if not best:
        return None
    # The grey margin band, if the book prints one beside this panel.
    bx0 = best["bbox"][0]
    for e in els:
        if e.get("role") != "decorative_image" or not e.get("fill"):
            continue
        x0, y0, x1, y1 = e["bbox"]
        if (y1 - y0) > 0.70 and x1 <= bx0 + 0.02 and (x1 - x0) < 0.15:
            best["band"] = {"bbox": e["bbox"], "fill": e["fill"]}
            break
    return best


_BOX_N_RE = re.compile(r'class="block-n">\[(\d+)\]')


def _apply_box_furniture(items, furn, page_w_mm, state):
    """Give every box panel on this page the fill and the furniture the book prints on it.

    Runs AFTER _merge_box_runs, so one worked example is already one panel. Three things happen
    here, all driven by A2L's measurement of this page:

      * the panel is painted with the fill measured on ITS OWN blocks, not the chapter's single
        --box-fill. Physics prints four designs (grey #dbdcde worked examples, pale #c6eafb
        feature boxes, #9cdcf8 the scientist panel, #d1d2d4 Points to Ponder) and a merged group
        was taking the chapter default for all of them;
      * a vertical TAB is painted into the panel's own background gradient on the outer side,
        with its lettering placed over it -- "EXAMPLE 1.8", or the scientist's name;
      * a figure measured INSIDE a box's bbox (the Coulomb portrait) is moved into the panel
        instead of floating above it as a second tinted box of its own.

    `state` carries the last example label across pages, because the book continues one example's
    tab onto the next page (p013, p014, p017 and p022 all open inside an example started earlier).
    """
    if not furn:
        return items
    bbox_by_n, fill_by_n = furn["bbox"], furn["fill"]
    tabs, bars, inside = list(furn["tabs"]), list(furn["bars"]), furn["inside_box"]
    out, held, held_n = [], "", None

    def span(ns):
        bbs = [bbox_by_n[n] for n in ns if n in bbox_by_n]
        if not bbs:
            return None
        return (min(b[0] for b in bbs), min(b[1] for b in bbs),
                max(b[2] for b in bbs), max(b[3] for b in bbs))

    for col, html in items:
        ns = [int(x) for x in _BOX_N_RE.findall(html)]
        if ('class="block block-figure' in html and len(ns) == 1 and ns[0] in inside):
            # Hold it for the panel it was measured inside; it is emitted there, not here.
            held, held_n = html, ns[0]
            continue
        if 'class="block block-box' not in html:
            if held:
                out.append((col, held))
                held, held_n = "", None
            out.append((col, html))
            continue

        box_ns = ns + ([held_n] if held_n is not None else [])
        bs = span(box_ns)
        fill = next((fill_by_n[n] for n in ns if n in fill_by_n), None)
        is_sci = bool(held)

        # The tab whose measured y-range this panel sits in. Two examples on one page each get
        # their own (p017 and p022 both measure two), so a matched tab is consumed.
        tab = None
        if bs is not None:
            for t in tabs:
                tb = t["bbox"]
                ov = min(bs[3], tb[3]) - max(bs[1], tb[1])
                if ov > 0 and ov > 0.5 * min(bs[3] - bs[1], tb[3] - tb[1]):
                    tab = t
                    break
        if tab is not None:
            tabs.remove(tab)
        bar = None
        if bs is not None:
            for bb in bars:
                if abs(bb["bbox"][1] - bs[1]) < 0.03:
                    bar = bb
                    break
        if bar is not None:
            bars.remove(bar)

        # The tab's words. "Example 1.8" is A2B's own bold term at the head of the example; a
        # scientist panel's is the bold name line. A continuation page has neither, and takes the
        # label the book carried over with it.
        label = ""
        strongs = re.findall(r"<strong>(.*?)</strong>", html, re.S)
        plain = [re.sub(r"<[^>]+>", "", t).strip() for t in strongs]
        ex = next((t for t in plain if re.match(r"^Example\s+[0-9.]+$", t)), "")
        if ex:
            state["example"] = ex
        if is_sci:
            label = plain[0] if plain else ""
        elif tab is not None:
            label = ex or state.get("example", "")

        # Paint the tab into the box's own background so it survives a page break, and reserve
        # its width inside the panel. Measured on p021: tab 25.5pt of a 612pt sheet with a 6pt
        # gap; on p011, 19.5pt with a 4.5pt gap.
        style_bits = []
        pad_side = ""
        if tab is not None:
            tb = tab["bbox"]
            tab_mm = max(3.0, (tb[2] - tb[0]) * page_w_mm)
            gap_mm = max(0.8, (abs(tb[0] - bs[2]) if tb[0] >= bs[2]
                               else abs(bs[0] - tb[2])) * page_w_mm) if bs else 1.6
            side = "right" if (bs is None or tb[0] >= bs[2]) else "left"
            total = tab_mm + gap_mm
            to = "right" if side == "right" else "left"
            style_bits.append(
                f"background: linear-gradient(to {to}, "
                f"{fill or 'var(--box-fill)'} 0, {fill or 'var(--box-fill)'} "
                f"calc(100% - {total:.2f}mm), "
                f"transparent calc(100% - {total:.2f}mm), "
                f"transparent calc(100% - {tab_mm:.2f}mm), "
                f"{tab['fill']} calc(100% - {tab_mm:.2f}mm), {tab['fill']} 100%)")
            pad_side = f"padding-{side}: {total + 3.0:.2f}mm"
            style_bits.append(pad_side)
            tab_html = (f'<span class="boxed-tab" style="--tab-w: {tab_mm:.2f}mm; '
                        f'--tab-ink: {tab["ink"]};">{_esc(label.upper())}</span>'
                        if label else "")
        else:
            side, tab_html = "right", ""
            if fill:
                style_bits.append(f"background: {fill}")

        body = html
        if style_bits:
            # The fill is rewritten, not appended: _block_html already wrote an inline
            # `background` on this div and an inline style cannot be beaten from a stylesheet.
            body = re.sub(r'^<div class="block block-box([^"]*)"(?:\s+style="[^"]*")?',
                          lambda m: f'<div class="block block-box{m.group(1)}" '
                                    f'style="{"; ".join(style_bits)};"',
                          body, count=1)
        if bar is not None and tab is None:
            # The bar's words are the box's own opening line, which the book sets INSIDE the bar
            # rather than as the first line of the prose -- p003 opens "UNIFICATION OF
            # ELECTRICITY AND MAGNETISM In olden days, ...", p041 "ON SYMMETRY OPERATIONS In
            # Physics, we often ...". Lifting it out is what stops the title printing twice.
            m = re.search(r"<p>\s*([A-Z][A-Z0-9 \u2019'(),.\-]{5,70}?)\s*(?=[A-Z][a-z])",
                          body)
            if m:
                body = body[:m.start(1)] + body[m.end(0):]
                body = body.replace(
                    "</span>",
                    f'</span><div class="box-title-bar" style="--bar-fill: {bar["fill"]}; '
                    f'color: {bar["ink"]};">{_esc(m.group(1).strip())}</div>', 1)
        if held:
            body = body.replace("</span>", "</span>" + held, 1)
            held, held_n = "", None
        cls = "boxed boxed-" + side + (" sci-panel" if is_sci else "")
        wrap_style = ""
        if is_sci and bs is not None and tab is not None:
            # Hard to its measured width (p011: 179.5pt = 63.3mm of the sheet) and hard against
            # the outer margin, as the book sets it. Without this the float took its whole
            # normalised column, about a fifth wider than the page prints.
            wrap_style = (f' style="width: {max(tab["bbox"][2], bs[2]) * page_w_mm - bs[0] * page_w_mm:.1f}mm;"')
        out.append((col, f'<div class="{cls}"{wrap_style}>{body}{tab_html}</div>'))

    if held:
        out.append(("full", held))
    return out


def _merge_box_runs(items):
    """Collapse a consecutive run of box/equation/figure fragments into ONE box panel.

    A2 blocks a worked example as several pieces -- prose, display equation, figure, more prose --
    and rendering each as its own panel chopped the book's single continuous grey box into a stack
    of separate ones with the equations falling between them. PHY12O-ch01 p021 is one Example
    spanning blocks n=2..n=12 with no prose break at all, and it rendered as six panels.

    Column equality is deliberately NOT required: a figure inside an example is often measured in
    a side column while the surrounding prose is `full`, and requiring a match broke every run at
    its figure.
    """
    out, run, run_col = [], [], None

    def flush():
        if not run:
            return
        if len(run) == 1:
            out.append((run_col, run[0]))
        else:
            out.append((run_col, f'<div class="block block-box box-group">{"".join(run)}</div>'))
        run.clear()

    for col, html in items:
        is_box = 'class="block block-box' in html
        is_eqfig = ('class="block block-equation' in html
                    or 'class="block block-figure' in html)
        if is_box and not run:
            flush()
            run_col = col
            run.append(html)
        elif run and (is_box or is_eqfig):
            run.append(html)
        else:
            flush()
            run_col = None
            out.append((col, html))
    flush()
    return out


def _tall_for_column(html):
    """True when this single-side element is too tall to be a float.

    Judged from the CONTENT rather than a measured height, because the height a block will take
    depends on the rendered width and is not known here. A run carrying several blocks, or a lot
    of prose, will occupy most of a column; a lone figure or a short note will not. The threshold
    is deliberately generous -- being wrong in this direction only costs a text wrap, while being
    wrong in the other direction can empty a whole sheet.
    """
    blocks = html.count('class="block ')
    text_len = len(re.sub(r"<[^>]+>", "", html))
    return blocks >= 3 or text_len > 900


def _assemble_columns(items, cols, prefer_float=False):
    """items is [(column, html)] in reading order -> HTML placing each block in its measured
    column. Consecutive left/right blocks become one two-column grid; `full` blocks span.

    Segmenting rather than one global grid matters because a real page alternates: full-measure
    prose, then a narrowed stretch beside a figure, then full measure again. One grid for the
    whole page would force unrelated blocks into a column they were never in.
    """
    if not cols or not any(c in ("left", "right") for c, _ in items):
        return "".join(h for _, h in items)

    left_w = cols.get("left")
    right_w = cols.get("right")
    if left_w and right_w:
        # `fr` units split the CONTENT box, but the measured fractions are of the whole page --
        # which includes the outer margins the sheet already applies. Using them raw squeezed the
        # left column (BIO12O-ch03 p001's contents panel wrapped "Gametogenesis" over three
        # lines). Normalising the two against their own sum restores the real ratio between them.
        lw = max(0.12, left_w[1] - left_w[0])
        rw = max(0.12, right_w[1] - right_w[0])
        total = lw + rw
        template = f"{lw / total:.3f}fr {rw / total:.3f}fr"
    else:
        template = "1fr 1fr"

    out, run = [], []

    def flush_run():
        if not run:
            return
        left = "".join(h for c, h in run if c == "left")
        right = "".join(h for c, h in run if c == "right")
        if left and right and prefer_float:
            # The book's own arrangement: the NARROW side sits in the outer margin and the prose
            # runs around it, then carries on underneath. A CSS grid cannot do that -- and worse,
            # a grid item does not fragment in Chrome's print, so every measured two-column
            # stretch became one unbreakable lump. Measured case: PHY12O-ch01 p011 put five
            # paragraphs and the whole Coulomb panel in a single `col-split`, which then
            # overflowed by two lines onto a sheet carrying nothing but a footnote. Floating the
            # narrow side restores both the book's wrap AND the ability to break a paragraph at
            # the foot of a sheet, which is what fills the page.
            lw = max(0.12, (left_w[1] - left_w[0]) if left_w else 0.5)
            rw = max(0.12, (right_w[1] - right_w[0]) if right_w else 0.5)
            side, html_f, html_flow, w = (("right", right, left, rw) if rw <= lw
                                          else ("left", left, right, lw))
            # Normalised against the pair, as the grid template was: the measured fractions are
            # of the whole sheet, the float's width is of the content box.
            frac = max(0.18, min(0.60, w / (lw + rw)))
            out.append(f'<div class="fig-float float-{side}" '
                       f'style="width: {frac * 100:.1f}%;">{html_f}</div>{html_flow}')
        elif left and right:
            out.append(
                f'<div class="col-split" style="grid-template-columns: {template};">'
                f'<div class="col col-left">{left}</div>'
                f'<div class="col col-right">{right}</div></div>'
            )
        else:
            # Only ONE side has content -- a marginal sidebar, or a figure sitting in the outer
            # margin with no facing column. Rendering that as a two-cell grid leaves a wide
            # empty half, which is exactly the "weird placement" it produced on BIO12O-ch03 p010
            # (the "Menstrual Hygiene" sidebar, measured in the right column at x 0.696-0.877
            # with nothing beside it). Offset it to its measured position instead.
            # FLOAT it to its measured side so the prose wraps around it and then carries on
            # underneath -- which is how the book fills these pages (NCERT p047 floats Figure 3.5
            # right with text down its left; p048 floats Figure 3.6 left). A rigid two-column grid
            # was used here before and it left the rest of each line-width empty, which is the
            # whole reason our pages ran at 7.8% ink against the book's 14%.
            side = "left" if left else "right"
            bounds = cols.get(side)
            html_one = left or right
            # Floor lowered from 0.38: NCERT's marginal figure column is about a quarter of the
            # measure (FIGURE 1.4 at 0.169 of the page), and a 0.38 floor inflated every one of
            # them to half the line, leaving too little beside it for prose to wrap.
            width = max(0.22, min(0.62, (bounds[1] - bounds[0]) if bounds else 0.30))
            # A resource link ("Interactive animation on Coulomb's law: http://...") is printed
            # ROTATED in the outer margin beside the vertical PHYSICS label, not as a column of
            # body text. Measured in a side column it was coming out as a 48%-wide float that ate
            # half the measure; as a body line it was stretched edge to edge by justification.
            if ("block-paragraph" in html_one and "http" in html_one
                    and html_one.count("<p>") == 1 and len(re.sub(r"<[^>]+>", "", html_one)) < 260):
                out.append(f'<div class="margin-link">{html_one}</div>')
            # A TALL single-side element is not a float. A float exists so prose can wrap beside
            # it; something occupying most of the column height has nothing to wrap beside it, and
            # as a float it carries `break-inside: avoid`, so when it does not fit the space left
            # it jumps whole to the next sheet. On CHE11L-ch02 p015 -- two tall pink problem
            # panels, one per column -- that emptied the sheet `break-before` had just created,
            # leaving it holding nothing but the folio while its 2,672 characters moved on. In
            # normal flow the same content fragments across the break instead.
            elif _tall_for_column(html_one):
                out.append(f'<div class="col-tall col-tall-{side}">{html_one}</div>')
            else:
                out.append(
                    f'<div class="fig-float float-{side}" '
                    f'style="width: {width * 100:.1f}%;">{html_one}</div>'
                )
        run.clear()

    for col, html in items:
        if col in ("left", "right"):
            # A NEW left-column item that arrives after right-column content has already
            # accumulated starts a FRESH row. Without this every margin heading on a page piled
            # into one cell at the top while its prose ran on beside the first of them -- real
            # case CHE12L-ch09 p002, where "9.2 Classification" and "9.3 Nomenclature" sat
            # stacked together even though the book prints 9.3 much further down, beside the
            # section it actually introduces. Blocks arrive in reading order, so a margin
            # heading followed by prose is exactly the pairing the page shows.
            # Start a fresh row only once the current run already holds a COMPLETE pair -- a
            # left AND a right. Flushing on "a left after any right" was too eager: on
            # PHY12O-ch01 p002 the prose comes first (right) and the figure second (left), so
            # that rule split one real side-by-side row into two stacked one-sided offsets.
            # Requiring a completed pair keeps both orderings right: chemistry's
            # heading-then-prose (left, right | left, right) and physics' prose-then-figure
            # (right, left).
            if (col == "left"
                    and any(c == "left" for c, _ in run)
                    and any(c == "right" for c, _ in run)):
                flush_run()
            run.append((col, html))
        else:
            flush_run()
            out.append(html)
    flush_run()
    return "".join(out)


def _flush_banner(out, banner_lines, banner_bleed=""):
    """Emit any buffered chapter-title lines as the book's single coloured opening panel."""
    if banner_lines:
        out.append(f'<div class="chapter-banner">{"".join(banner_lines)}</div>')
        banner_lines.clear()


def _banner_html(banner_lines, banner_bleed=""):
    """The buffered chapter-title lines as one coloured panel, or "" if there are none."""
    if not banner_lines:
        return ""
    html_out = (f'<div class="chapter-banner"{banner_bleed}>'
                f'{"".join(banner_lines)}</div>')
    banner_lines.clear()
    return html_out


def _is_title_heading(txt):
    """A chapter/unit title is printed large on an opening page ("CHAPTER 3", "HUMAN
    REPRODUCTION"); a numbered section heading ("3.1 The Male Reproductive System") is printed
    smaller, in the subject's colour. Both arrive upper-cased in A2 output, so case alone cannot
    tell them apart -- the leading section number is what distinguishes a section from a title."""
    txt = txt.strip()
    if re.match(r"^\d+\.\d+", txt):
        return False
    letters = [c for c in txt if c.isalpha()]
    return bool(letters) and all(c.isupper() for c in letters) and len(txt) <= 60


def _block_html(b, n, kind, corr_by_n, bold_by_n, is_opener=False,
                measured_role=None, style=None):
    """Returns (html, is_banner_line). A banner line is a chapter title that the book prints
    inside its coloured opening panel; the caller groups consecutive ones into one panel."""
    fix = corr_by_n.get(n)
    txt = (fix["corrected_text"] if fix else (b.get("text") or "")).strip()
    bold = bold_by_n.get(n) or []
    body = _bold_applied(txt, bold)
    tag = "h4" if kind == "heading" else "p"   # decided BEFORE kind is re-labelled below
    if kind == "heading" and measured_role:
        # A measured role is a fact read off the page; the text heuristic below is a guess.
        if measured_role == "chapter_title" and is_opener:
            return (f'<div class="banner-line"><span class="block-n">[{n}]</span>{body}</div>', True)
        if measured_role in ("major_heading", "section_heading"):
            kind = "heading major" if measured_role == "major_heading" else "heading"
            # This heading's OWN measured ink. Physics sets x.y headings grey #6d6e71 and x.y.z
            # sub-headings cyan #00adef; one chapter-wide accent made half of them wrong.
            _ink = (style or {}).get("ink")
            _st = f' style="color: {_ink};"' if _ink else ""
            return (f'<div class="block block-{kind}"><span class="block-n">[{n}]</span>'
                    f'<{tag}{_st}>{body}</{tag}></div>', False)
    if kind == "heading" and _is_title_heading(txt):
        if is_opener:
            # NCERT prints "CHAPTER 3" and "HUMAN REPRODUCTION" as two lines of ONE green panel,
            # not as two separate headings -- so emit just the line and let the caller wrap them.
            return (f'<div class="banner-line"><span class="block-n">[{n}]</span>{body}</div>', True)
        # An all-caps title ANYWHERE ELSE in the chapter ("EXERCISES", "SUMMARY") is a section
        # heading the book sets in type, not a coloured opening banner. Giving it the banner was
        # a real defect: BIO12O-ch03 p015's "EXERCISES" rendered with the full green chapter panel.
        kind = "heading major"
    extra = ""
    if fix:
        n_fixes = len(fix.get("fixes") or [])
        extra = f'<div class="qa-tag">notation corrected by A2N ({n_fixes} fix{"es" if n_fixes != 1 else ""})</div>'
    # This block's OWN measured colours win over the chapter-wide palette.
    inline = ""
    if style:
        bits = []
        if style.get("fill") and kind == "box":
            bits.append(f"background: {style['fill']}")
        # Measured ink applies to ANY block, not just headings. CHE11L-ch02's opener sets its
        # objectives intro and list in cyan (#00adef measured on both), and this chapter prints a
        # good deal of coloured body text besides -- all of it was rendering in the default body
        # colour because the measurement was only consulted for headings. A2L measures text_color
        # per element precisely so the page can be reproduced; honour it wherever it was measured.
        if style.get("ink"):
            bits.append(f"color: {style['ink']}")
        if bits:
            inline = f' style="{"; ".join(bits)};"'
    if inline and kind.startswith("heading"):
        body = f'<span{inline}>{body}</span>'
        inline = ""
    # A FOOTNOTE is a paragraph the page prints below a rule, in smaller type. Measured on
    # Old_ncert_Physics_Chapter_1.pdf: footnote lines in the bottom margin set at 9.0pt against a
    # 10.5pt body (0.86x). Rendering them at full body size with no separator both misread the
    # page -- a page-by-page audit reported "footnotes run into the body text with no separator
    # line" on nine pages -- and cost height: the flux footnote on p026 was pushed onto a sheet of
    # its own carrying 289 characters and nothing else. Smaller type with a rule above is what the
    # book does AND what makes it fit.
    _is_footnote = (kind == "paragraph"
                    and re.match(r'^\s*(?:<[^>]+>\s*)*[*\u2217]', body or ""))
    # EPIGRAPH. Preferred signal is A2L's own `epigraph` role, now an allowed value -- but the
    # chapters measured before that role existed cannot report it, so fall back to the measurement
    # that distinguishes it anyway: on a chapter-opening page the quotation is set in a DIFFERENT
    # FACE from the body around it (CHE11L-ch02 p001 measures the quotation `sans` where its
    # objectives are `serif`). That is a measured difference, not a guess about the words.
    _role = (style or {}).get("role")
    _is_epigraph = (_role == "epigraph"
                    or (kind == "paragraph" and is_opener
                        and (style or {}).get("font") == "sans"))
    _cls = ("block block-{}".format(kind)
            + (" block-footnote" if _is_footnote else "")
            + (" block-epigraph" if _is_epigraph else ""))
    return (f'<div class="{_cls}"{inline}><span class="block-n">[{n}]</span>'
            f'<{tag}>{body}</{tag}>{extra}</div>', False)


def _figure_table_html(args, page_num, b, n, kind, fig_dir, fig_rel_prefix, blocks,
                       mm_per_px=0.0, layout=None, inside_box=False, clamp_top=False):
    """`inside_box` = this figure was measured wholly INSIDE a box's own bbox (the Coulomb
    portrait on p011). The book prints the name under it as the panel's own bold opening line,
    which is also the prose we render inside the panel, so the caption is dropped here and the
    printed band is cut out of the crop -- otherwise the same sentence appears twice, once of
    them sliced in half ("arles Augustin d" was what the sheet actually showed)."""
    bbox = b.get("bbox")
    if not bbox:
        return _equation_html(args, page_num, n, kind, b, blocks, fig_dir, fig_rel_prefix)
    a2s = _load_sibling_json("A2S", f"{args.chapter}-p{page_num:03d}-b{n}")
    # Trim the printed caption band out of a FIGURE crop when we are about to print that same
    # caption as text underneath it -- otherwise the reader shows the caption twice.
    _has_caption = bool(a2s and kind == "figure" and (a2s.get("caption") or "").strip())
    _drop_caption = inside_box and _has_caption
    box, needs_border = _crop_for(bbox, kind, blocks, n, bool(a2s), tight_x=(kind == "figure"))
    cut = (_caption_cut_px(layout, page_num, bbox, pad_frac=0.006 if clamp_top else 0.0)
           if _has_caption else None)
    if cut is not None and cut > box[1] + 40:
        box = [box[0], box[1], box[2], min(box[3], cut)]
    if inside_box:
        # A figure printed INSIDE a box has the panel's own text directly beneath it, so the
        # bottom-weighted margin _tight_bbox adds (56px, about 20pt of the sheet) runs straight
        # into it -- p011's portrait came out with a half-height band of "arles Augustin d"
        # under it. A2's own bbox for that block is the photograph exactly (383.4-484.2pt
        # across, 122.4-261.0pt down, against a photo measured at 385.5-478.5 / 127.1-258.8),
        # so there is nothing to recover below it and the crop stops at the block.
        box = [box[0], box[1], box[2], min(box[3], bbox[3] + 2)]
    if clamp_top:
        ty = _figure_y_clamp(layout, page_num, bbox)
        if ty is not None and ty < bbox[1] + 4 and ty > box[1]:
            box = [box[0], ty, box[2], box[3]]
    lx, rx = _furniture_x_clamp(layout, page_num, bbox)
    if rx is not None and rx > box[0] + 40:
        box = [box[0], box[1], min(box[2], rx), box[3]]
    if lx is not None and lx < box[2] - 40:
        box = [max(box[0], lx), box[1], box[2], box[3]]
    img_path = os.path.join(fig_dir, f"p{page_num:03d}_b{n}.png")
    lib_pdf.crop_box(args.pdf, page_num, box, img_path, unit="px")
    if needs_border:
        _mark_target_box(img_path, bbox, box)
    elif _drop_caption or (_has_caption and cut is None):
        # The caption is about to be printed as text below the image, so take the printed band
        # out of the picture rather than showing the same sentence twice.
        _trim_caption_band(img_path)
    rel = f"{fig_rel_prefix}/p{page_num:03d}_b{n}.png"
    # Printed width in mm, so the figure sits on the sheet at the size the book prints it
    # rather than stretching to whatever the column happens to be.
    wmm = ""
    if mm_per_px and bbox:
        # max-width, not width: a fixed width would force the full height and defeat the height
        # cap in the stylesheet, distorting the figure instead of scaling it.
        wmm = f' style="max-width: {max(10.0, (bbox[2] - bbox[0]) * mm_per_px):.1f}mm"'
    body = f'<img class="crop" src="{rel}"{wmm} alt="{kind} p{page_num} block {n}">'
    if needs_border:
        body += ('<div class="crop-note">red box = this block; the surrounding page is shown '
                 'only because no transcription exists yet to name its caption</div>')
    if a2s and kind == "figure":
        cap = (a2s.get("caption") or "").strip()
        labs = a2s.get("labels") or []
        # No caption is the NORMAL case for a reaction scheme or a sub-panel diagram -- NCERT
        # simply prints none. Announcing "(no caption printed)" in alarm colours on every one of
        # them was pure noise that read as a defect; say nothing when there is nothing to say.
        if cap and _drop_caption:
            pass
        elif cap:
            # The book bolds only the "Figure 3.2" label and sets the rest of the sentence in
            # regular weight on the same line. Bolding the whole caption, as this did before,
            # is a different typographic statement from the one the page makes.
            m = re.match(r"^\s*((?:Fig(?:ure)?\.?)\s*[\dA-Za-z.()]+)\s*(.*)$", cap, re.S)
            if m:
                body += (f'<div class="caption"><strong>{_esc(m.group(1))}</strong> '
                         f'{_esc(m.group(2))}</div>')
            else:
                body += f'<div class="caption">{_esc(cap)}</div>'
        if labs:
            body += f'<div class="labels">labels: {_esc(", ".join(labs))}</div>'
    elif a2s and kind == "table":
        hdr, rows = a2s.get("header") or [], a2s.get("rows") or []
        if hdr:
            thead = "".join(f"<th>{_esc(c)}</th>" for c in hdr)
            trows = "".join(
                "<tr>" + "".join(f"<td>{_esc(str(c))}</td>" for c in r) + "</tr>" for r in rows
            )
            # The IMAGE is the authoritative rendering of an NCERT table: its first column is
            # routinely a DRAWN chemical structure (a benzene ring with substituents) that no
            # text cell can carry -- A2S honestly records those as "NH2 (on a drawn benzene
            # ring, ortho)". Printing the text table open underneath the image therefore showed
            # the same table twice, the second copy visibly poorer, which read as broken data.
            # The structured rows still matter for search and reuse, so they stay -- folded
            # away behind a disclosure rather than competing with the image.
            # ...but that reasoning only holds for a table that ACTUALLY carries drawn
            # structures. CHE11L-ch02's Table 2.6 is 53 and 56 rows of element, atomic number and
            # orbital occupancies -- pure text, not one drawn ring -- and folding it away left
            # sheets 38 and 39 showing a caption, a footnote and a crop. That crop is exactly the
            # "low-resolution screenshot with 2022-23 and a watermark, not real text" a
            # page-by-page audit reported for PHY12O-ch01's own table. So decide from the DATA:
            # a transcription whose cells mention a drawn structure keeps the image primary; one
            # that does not gets its real text table rendered open, where it belongs.
            _flat = " ".join(str(c) for r in rows for c in (r if isinstance(r, list) else [r]))
            _has_drawn = any(k in _flat.lower()
                             for k in ("drawn", "benzene ring", "on a ring", "structure)"))
            # A table longer than a sheet MUST be allowed to fragment. `break-inside: avoid` is
            # right for a short table -- the book keeps those whole -- but CHE11L-ch02's Table 2.6
            # runs to 54 and 57 rows, far taller than any sheet, so as an unbreakable block each
            # one jumped whole and emptied the sheet `break-before` had just created (sheets 5, 7,
            # 18 and 26 came out blank, and the chapter went from the book's own 45 sheets to 53).
            # Row count decides, not subject: a long table behaves this way in any book.
            # Threshold lowered from 14. The point is not "is this table enormous" but "could it
            # fail to fit the space left on a sheet" -- and because each book page starts a fresh
            # sheet, a table that is the first element of a page and does not fit empties that
            # whole sheet. CHE11L-ch02 p005's table is only 11 rows and did exactly that: sheet 5
            # came out with zero characters while sheet 6 opened with the table's header row.
            # Anything past a handful of rows is allowed to fragment; a genuinely short table
            # still stays whole, which is what the book does with those.
            _long = len(rows) > 5
            _tbl = (f'<div class="table-wrap{" table-long" if _long else ""}"'
                    f'{_table_fit_style(len(rows[0]) if rows else 0)}>'
                    f'<table class="data-table">'
                    f'<thead><tr>{thead}</tr></thead><tbody>{trows}</tbody></table></div>')
            if _has_drawn:
                body += (f'<details class="table-rows"><summary>structured rows '
                         f'({len(rows)}) — drawn structures cannot be carried as text</summary>'
                         f'{_tbl}</details>')
            else:
                # DROP THE CROP when the real text table is shown. The crop was previously the
                # only visible copy, with the text folded away behind a disclosure; rendering the
                # text open without removing the image left the same table printed TWICE, which
                # both duplicated the content and doubled the block's height. Because the block
                # carries `break-inside: avoid` and each book page starts a fresh sheet, that
                # doubled block no longer fit and jumped whole -- CHE11L-ch02 sheet 5 came out
                # with zero characters while sheet 6 opened on the table's header row.
                body = re.sub(r'<img class="crop"[^>]*>', "", body, count=1)
                body += _tbl
    elif not a2s:
        body += '<div class="pending">not yet transcribed by A2S — image above is the real crop</div>'
    return f'<div class="block block-{kind}"><span class="block-n">[{n}]</span>{body}</div>'


def _equation_html(args, page_num, n, kind, b=None, blocks=None, fig_dir=None,
                   fig_rel_prefix=None):
    """Render an equation/box block.

    **The crop is always shown when the block has a bbox.** Every equation block in the corpus has
    one (measured: 84/84 in CHE12L-ch09, 103/103 in PHY12O-ch01), so "not yet transcribed" was
    never a MISSING-CONTENT problem -- the content was always available as an image and this
    exporter simply was not showing it. Leaving a reader staring at a placeholder where the book
    prints an equation is the worst failure this document can have, and it was entirely avoidable.

    The image is also the FAITHFUL rendering, which matters most in chemistry: NCERT prints its
    reaction schemes as drawn structures (benzene rings, bond lines, charges set over atoms) that
    a single `latex` string can only approximate. So the crop leads, and the LaTeX transcription
    -- the searchable, reusable form -- is folded behind a disclosure beneath it.
    """
    a2s = _load_sibling_json("A2S", f"{args.chapter}-p{page_num:03d}-b{n}")
    bbox = (b or {}).get("bbox")
    parts = []

    if bbox and fig_dir:
        box, _ = _crop_for(bbox, kind, blocks or [], n, True)
        img_path = os.path.join(fig_dir, f"p{page_num:03d}_b{n}.png")
        lib_pdf.crop_box(args.pdf, page_num, box, img_path, unit="px")
        rel = f"{fig_rel_prefix}/p{page_num:03d}_b{n}.png"
        parts.append(f'<img class="crop eqn-crop" src="{rel}" alt="{kind} p{page_num} block {n}">')

    box_text = (a2s or {}).get("text") if kind == "box" else None
    num = (a2s or {}).get("number")
    label = f" {_esc(num)}" if num else ""

    if box_text:
        # Box: `text` is what makes it quotable -- a box returned with latex only reads as
        # complete and can never actually be cited.
        parts.append(f'<p>{_esc(box_text)}</p>')
    if _is_real_latex((a2s or {}).get("latex")):
        # The TRANSCRIPTION is the equation. Showing the crop as the equation and folding the
        # LaTeX away was the right call while A2S was incomplete (a placeholder is worse than a
        # picture), but once a chapter is transcribed it inverts: a rendered equation is sharp,
        # selectable and scales, whereas the crop is a small bitmap that the figure-width rule
        # stretched to the full measure and blurred. The crop stays, folded, as the printed
        # original to check against.
        # The equation NUMBER is printed at the right margin in the book and the prose refers to
        # it constantly ("Eq. (1.3)", "Eq. (1.31)"). It used to survive only inside the collapsed
        # toggle's label; once that toggle was hidden in the reader the numbers disappeared from
        # the document altogether. They are now a real right-aligned label beside the equation.
        _num = (num or "").strip()
        # A2S may legitimately return PROSE CARRYING INLINE MATHS rather than a bare expression:
        # the brief tells transcribers to defer a sentence whose notation the text layer scrambles,
        # and the honest transcription of such a sentence is its words with `$...$` spans where the
        # maths is printed (PHY12O-ch01 p024 b6 is exactly this). Wrapping that in `$$...$$` hands
        # KaTeX prose as display maths, which throws and prints the raw source in the error colour
        # -- a whole sentence of visible LaTeX in the middle of the page. Detect it and render it
        # as a paragraph, leaving the inline spans for KaTeX's inline pass, which is what the page
        # actually shows.
        _tex = a2s["latex"] or ""
        _inline_prose = ("$" in _tex
                         and not _tex.lstrip().startswith("$")
                         and len(re.sub(r"\$[^$]*\$", "", _tex).strip()) > 24)
        if _inline_prose:
            # Inline spans are emitted as \(...\), NOT as $...$. KaTeX's auto-render is
            # configured for display `$$...$$` only, so a bare `$...$` span was never rendered and
            # printed as literal source -- that is the raw LaTeX the audit saw on p024. Enabling a
            # bare `$` delimiter instead would also capture a currency symbol in running prose, so
            # the span is rewritten to the unambiguous \(...\) form and that delimiter is
            # registered alongside the display one.
            _tex_inline = re.sub(r"\$([^$]+)\$", r"\\(\1\\)", _tex)
            rendered = (
                f'<div class="eqn-row eqn-prose">'
                f'<p class="eqn-inline">{_tex_inline}</p>'
                + (f'<div class="eqn-no">{_esc(_num)}</div>' if _num else "")
                + f'</div>'
            )
        else:
            # SCALE A WIDE EQUATION TO FIT. `.eqn` carried `overflow-x: auto`, which gives a
            # scrollbar on screen and CLIPS on paper -- there is no scrollbar on a printed sheet.
            # A display equation wider than the measure was therefore cut off mid-expression, and
            # the reader saw a truncated formula with no indication anything was missing. Two
            # items reported as "missing results" in a page-by-page audit of PHY12O-ch01 were
            # exactly this: p031's torque derivation ended at "Magnitude of torque = q", and
            # p021's substitution line ended at "h = 1.5 x 10^-2 m" while its own LaTeX carries
            # "t_e = 2.9 x 10^-9 s" to the end. 70 equations in that one chapter exceed 60
            # characters and the longest runs to 456, so this was losing content across the book.
            # KaTeX cannot reflow maths, so the deterministic fix is to step the type down with
            # length. The thresholds are coarse on purpose: a slightly small equation is legible,
            # a clipped one is wrong.
            _n_chars = len(_tex)
            _scale = (1.0 if _n_chars <= 90 else
                      0.90 if _n_chars <= 150 else
                      0.80 if _n_chars <= 240 else
                      0.70)
            _sty = "" if _scale == 1.0 else f' style="font-size: {_scale:.2f}em;"'
            rendered = (
                f'<div class="eqn-row">'
                f'<div class="eqn"{_sty}>$${_latex_for_display(_tex)}$$</div>'
                + (f'<div class="eqn-no">{_esc(_num)}</div>' if _num else "")
                + f'</div>'
            )
        parts.insert(0, rendered)
        if bbox and fig_dir and parts and parts[-1].startswith("<img"):
            img = parts.pop()
            parts.append(f'<details class="eqn-src"><summary>printed original'
                         f'{label}</summary>{img}</details>')
    elif (a2s or {}).get("note", "").strip().lower().startswith(("defect", "unsure")):
        # The transcriber looked and reported that the region A2 recorded is NOT this block --
        # real case CHE12L-ch09-p004-b12, where an `equation` bbox encloses prose. The crop above
        # is faithful to the recorded region, so presenting it unlabelled implies the page prints
        # that here, which it does not. Say so instead. Five such blocks exist across the three
        # measured chapters; see docs/OPEN_QUESTIONS.md on target_box_in_crop undersizing.
        parts.append('<div class="pending">the region recorded for this block does not contain '
                     'it — the transcriber flagged this; the image above is that recorded region, '
                     'not this block</div>')
    elif not bbox:
        # No crop possible AND no transcription: the only case that is genuinely a content gap.
        parts.append(f'<div class="pending">not yet transcribed ({_esc(kind)}) and no region '
                     f'recorded to crop</div>')
    else:
        parts.append('<div class="await">LaTeX transcription pending — the image above is the '
                     'page itself, so no content is missing here</div>')

    cls = "block-box" if kind == "box" else "block-equation"
    return (f'<div class="block {cls}"><span class="block-n">[{n}]</span>'
            f'{"".join(parts)}</div>')


# Palette sampled PIXEL-BY-PIXEL from the real rendered NCERT pages (not guessed): a vertical
# colour-band scan down the chapter-opening page, plus a glyph-core sample of the section
# heading. Biology Class 12 measured exactly:
#   section-heading green  #01b44c      chapter banner  #d4ead3   banner top strip  #4b7334
#   rule bar               #f7941d      contents panel  #ffe5ca   paper             #ffffff
# Chemistry and Physics follow the same structural recipe in their own book colours.
# Fields: (heading, banner, banner_strip, bar, panel)
_SUBJECT_ACCENTS = {
    "BIO": ("#01b44c", "#d4ead3", "#4b7334", "#f7941d", "#ffe5ca"),
    "CHE": ("#b23a2e", "#f3dcd6", "#8c3326", "#e8762c", "#fde3d4"),
    "PHY": ("#1a5f9c", "#d6e4f2", "#27486e", "#e8a32c", "#dfeaf6"),
}
_DEFAULT_ACCENT = ("#6b5a3e", "#ece2cf", "#5a4b33", "#d59a3c", "#f6e9d6")


def _load_measured_layout(chapter):
    """The consolidated A2L measurement for this chapter, or None.

    This is the whole point of step A2L: the palette and type scale below were originally
    hand-picked by sampling ONE chapter's opening page by eye, which is correct for that book
    and generalises to nothing. When a measurement exists it WINS over the hard-coded table,
    because it was read off this chapter's own pages.
    """
    path = rc.pp("exports", "review", "html_data", f"{chapter}_layout.json")
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError):
        return None


def _saturation(hex_colour):
    """0-1 saturation of a #rrggbb colour. Used to tell a real accent from a neutral."""
    h = (hex_colour or "").lstrip("#")
    if len(h) != 6:
        return 0.0
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    mx, mn = max(r, g, b), min(r, g, b)
    return 0.0 if mx == 0 else (mx - mn) / mx


def _pick_strip(colors, fallback):
    """The banner's top strip colour: whichever of the header band / opener rule bar is stronger.

    There is no dedicated role for the strip across the head of a chapter-opening page, so the
    layout agents filed it differently per book -- physics as `rule_bar`, biology inside
    `chapter_banner`. Choosing the more saturated of the two candidates recovers the right colour
    for both without inventing a new role.
    """
    best, best_sat = fallback, -1.0
    for key in ("page_header_band_fill", "opener_rule_bar_fill"):
        entry = colors.get(key)
        val = entry.get("value") if isinstance(entry, dict) else None
        if not val:
            continue
        sat = _saturation(val)
        if sat > best_sat:
            best, best_sat = val, sat
    return best


def _pick_accent(colors, fallback):
    """The chapter's accent: the most saturated measured heading/caption colour.

    Taking `section_heading_text_color` as the accent was wrong for PHY12O-ch01, whose numbered
    headings are grey #6d6e71 while the book's actual accent -- sub-headings, figure captions,
    box bars, table headers -- is cyan #00adef. A grey (#6d6e71), a white (#ffffff, reverse-out
    type on a coloured bar) and a near-black body colour are all neutrals, never accents, so the
    accent is chosen by saturation rather than by which role happened to be looked up first.
    """
    best, best_sat = fallback, 0.0
    for key in ("figure_caption_text_color", "section_heading_text_color",
                "major_heading_text_color"):
        entry = colors.get(key)
        val = entry.get("value") if isinstance(entry, dict) else None
        if not val:
            continue
        sat = _saturation(val)
        if sat > best_sat and sat >= 0.15:   # below this it is a neutral, not an accent
            best, best_sat = val, sat
    return best


# Viewer behaviour: a page counter that follows the scroll, jump-to-page, zoom in PDF-viewer
# steps, and two DOM fixes that CSS alone cannot do -- float-wrapping a marginal figure next to
# the paragraph it belongs beside, and title-casing headings so `font-variant: small-caps`
# can render real caps-and-small-caps (A2 stores them ALL CAPS, from which small-caps renders
# uniformly small and wrong).
_VIEWER_JS = """<script>
(function () {
  var viewer = document.getElementById('viewer');
  var pages = Array.prototype.slice.call(document.querySelectorAll('#viewer .page-row'));
  if (!viewer || !pages.length) return;
  var input = document.getElementById('pdf-page');
  var label = document.getElementById('pdf-zoom');
  var bar = document.querySelector('.pdf-toolbar');
  var STEPS = [0.25, 0.33, 0.5, 0.67, 0.75, 0.8, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2, 2.5, 3, 4];
  var pageW = pages[0].offsetWidth;
  var zoom = 1;

  /* A marginal figure/sidebar wraps the paragraph that sits beside it on the page. If the next
     sibling is not a paragraph (a heading or another figure follows), move it above the previous
     paragraph so that one wraps instead. */
  document.querySelectorAll('#viewer .col-offset, #viewer .fig-float').forEach(function (f) {
    var next = f.nextElementSibling, prev = f.previousElementSibling;
    var isPara = function (el) { return el && el.classList.contains('block-paragraph'); };
    if (!isPara(next) && isPara(prev)) prev.parentNode.insertBefore(f, prev);
    if (f.classList.contains('col-offset')) f.classList.add('wrap');
  });

  var MINOR = /^(a|an|and|as|at|by|for|in|of|on|or|the|to)$/;
  document.querySelectorAll('.block-heading:not(.major) h4').forEach(function (h) {
    h.textContent = h.textContent.toLowerCase().split(' ').map(function (w, i) {
      return i > 1 && MINOR.test(w) ? w : w.charAt(0).toUpperCase() + w.slice(1);
    }).join(' ');
  });

  function current() {
    var line = bar.offsetHeight + (window.innerHeight - bar.offsetHeight) / 3, n = 0;
    pages.forEach(function (p, i) { if (p.getBoundingClientRect().top <= line) n = i; });
    return n;
  }
  function goTo(i) {
    i = Math.max(0, Math.min(pages.length - 1, i));
    window.scrollTo(0, pages[i].getBoundingClientRect().top + window.scrollY - bar.offsetHeight - 8);
  }
  function setZoom(z) {
    var i = current(), r = pages[i].getBoundingClientRect();
    var into = (bar.offsetHeight - r.top) / r.height;
    zoom = Math.max(STEPS[0], Math.min(STEPS[STEPS.length - 1], z));
    viewer.style.zoom = zoom;
    label.textContent = Math.round(zoom * 100) + '%';
    var r2 = pages[i].getBoundingClientRect();
    window.scrollTo(0, r2.top + window.scrollY + into * r2.height - bar.offsetHeight);
  }
  function fitZoom() { return (document.documentElement.clientWidth - 48) / pageW; }
  function step(dir) {
    var next = dir > 0 ? STEPS.find(function (s) { return s > zoom + 0.001; })
                       : STEPS.slice().reverse().find(function (s) { return s < zoom - 0.001; });
    if (next) setZoom(next);
  }
  document.getElementById('pdf-zoom-in').onclick = function () { step(1); };
  document.getElementById('pdf-zoom-out').onclick = function () { step(-1); };
  document.getElementById('pdf-fit').onclick = function () { setZoom(fitZoom()); };
  document.getElementById('pdf-print').onclick = function () { window.print(); };
  input.addEventListener('change', function () { goTo(parseInt(input.value, 10) - 1 || 0); input.blur(); });
  input.addEventListener('keydown', function (e) { if (e.key === 'Enter') input.dispatchEvent(new Event('change')); });
  window.addEventListener('scroll', function () {
    if (document.activeElement !== input) input.value = current() + 1;
  }, { passive: true });
  /* Fit each book page onto its own sheet.
     The sheet is a fixed A4 box with overflow:hidden, so content taller than 297mm was simply
     CLIPPED on screen -- invisible, with no indication anything was missing -- while printing
     spilled it onto extra sheets (15 sheets produced 27 PDF pages). Scaling the pane down to the
     sheet keeps every page whole, makes the screen show what the PDF shows, and restores
     one-book-page-per-printed-page. Pages that already fit are left untouched. */
  /* No fit-to-sheet scaling.
     Scaling the pane was tried twice and both ways were wrong: per-page scaling gave every page
     a different type size, and one uniform scale pulled the WHOLE chapter down to whatever the
     densest page needed (7.5pt against the book's 9.5pt). It also made the screen and the PDF
     disagree, because the screen applies the viewer's zoom on top of the transform while the
     print path does not. Type size and density now match the book exactly, and a page whose
     reflowed content runs longer than the sheet simply continues onto the next one. */
  setZoom(Math.min(1, fitZoom()));
  if (location.hash) { var t = document.querySelector(location.hash); if (t) goTo(pages.indexOf(t)); }
})();
</script>"""

_MM_PER_IN, _PT_PER_IN = 25.4, 72.0
# Cap height as a fraction of the em, for the Bookman-class body face. 0.70 is the generic
# serif figure and gave 10.29pt for biology, against the ~9.5pt the book actually sets --
# Bookman is a large-on-body face with a cap height nearer 0.76, and using the generic value
# inflated every derived size by about 8%.
_CAP_RATIO = 0.76

# The derived size matches the book's own body type, but our reflowed setting needs a little more
# room for the SAME words: NCERT's typesetter breaks lines and places figures by hand, so the
# printed page packs tighter than any automatic layout of it can. Without this, seven of fifteen
# biology pages ran a few millimetres past the sheet and each spilled onto a near-empty second
# one. Trimming the body size slightly is the cheapest way to buy that room -- it costs a little
# scale, where clipping cost whole sentences and uniform down-scaling cost 20% of the type size.
_FIT_FACTOR = 1.0


# --------------------------------------------------------------------------------------------
# SUBJECT PROFILES
#
# Every layout constant that differs between books lives here, keyed by the chapter-id prefix.
# It exists because the alternative failed concretely: tuning the trim, the leading and the
# column rules for physics silently re-rendered biology, whose layout had already been approved.
# A global constant is a promise that all three books are typeset the same way, and they are not
# -- NCERT prints physics on a 612x784pt sheet with marginal figure columns, and biology on A4
# with a single measure. Shared machinery stays shared; anything a book sets differently is a
# field here, so a physics change cannot reach biology at all.
#
#   trim_pt       the book's printed sheet in points, or None for A4
#   leading       body line-height as a ratio of body size (measured off the source PDF)
#   cap_ratio     figure height cap as a fraction of the page
#   break_per_page  True = each book page starts a new sheet; False = continuous flow
#   derive_columns  True = infer side columns from measured bboxes, ignoring A2L's label
#   corner_hang_mm  how far the corner artwork hangs BELOW the band, measured off the
#                   source PDF (biology 14.0-14.2mm on every body page). The band
#                   reserves this as bottom margin so body text starts clear of it.
#   band_tab        True = the grey tab with the square mark (physics); False = plain
#                   small-caps running header beside the band (biology, chemistry)
#   para_indent_mm  first-line indent of a body paragraph, measured off the source PDF.
#                   Physics indents 18pt (78.0 - 60.0 on p011/p003/p021) and sets NO space
#                   between paragraphs; biology/chemistry keep this at 0 and are untouched.
#   para_gap_pt     space BETWEEN body paragraphs, or None to keep the stylesheet default.
#                   A book that indents does not also space: physics measures a 3.1pt gap
#                   between the end of one paragraph and the start of the next (p011's three
#                   body paragraphs run 0.135-0.389, 0.393-0.468, 0.473-0.666), i.e. the
#                   normal line pitch and nothing more.
#   box_tabs        True = the book prints coloured furniture ON its boxes -- a vertical side
#                   tab in the outer margin naming the worked example or the scientist, a
#                   title bar straddling the top of a feature box, a thin rule down the inner
#                   edge -- and a DIFFERENT fill per box design. Physics measures four fills
#                   and sixteen tabs in this chapter; biology and chemistry measure none, so
#                   they keep the single-fill plain panel they were approved with.
#   float_side_columns  True = a measured two-column stretch is laid out as the book sets it --
#                   the NARROW side floated into the outer margin with the prose flowing around
#                   it in normal flow. False = the approved CSS grid. The grid is what biology's
#                   opening page needs (contents panel beside the title), but a grid item cannot
#                   fragment in Chrome's print, so on physics -- where almost every body page has
#                   a measured side column -- each stretch became one unbreakable lump that
#                   jumped whole to the next sheet. Measured on p011: five paragraphs and the
#                   Coulomb panel in one `col-split`, overflowing by two lines onto a sheet
#                   carrying nothing but a footnote.
#   fit_factor    body type as a fraction of the size measured from this book's own cap height.
#                   All three books sit at 1.0 -- the measured size. Trimming physics to 0.97 to
#                   absorb its last few one-line overflows was TRIED and measured WORSE: the
#                   sheet count did not move (55), mean ink fell from 7.28% to 7.06% (below the
#                   0.75 floor against the source), and a sheet started clipping glyphs at the
#                   trim edge. Leave it at 1.0; the overflow is a spacing problem, not a size one.
#   band_fill_measured  True = paint the page band with A2L's measured page_header_band_fill
#                   and hang the running-header tab off its outer end, as physics prints it.
#                   False = keep --banner-strip and the 73%-bar-plus-corner-block band that
#                   biology measured and was approved with.
#   page_panels     True = an unnumbered page-wide `box` element tints the whole body of a
#                   page (physics sets SUMMARY on pale blue #c6eafb across pp.42-44 and
#                   POINTS TO PONDER on grey #d1d2d4 across pp.45-46). False = ignore it.
_SUBJECT_PROFILES = {
    # Approved and frozen. 13 sheets, A4, 0 blank. Measured leading 1.28, single measure.
    # Do not change these to fix another subject -- add a field and set it per subject instead.
    # break_per_page is TRUE: the approved biology PDF is 15 sheets, one per book page, with the
    # band at the head of each. Continuous flow collapsed it to 13 and left bands stranded
    # mid-sheet -- the exact regression this table exists to prevent.
    "BIO": {"trim_pt": None, "leading": 1.28, "cap_ratio": 0.76,
            "break_per_page": True, "derive_columns": False, "band_tab": False, "corner_hang_mm": 14.3,
            "para_indent_mm": 0.0, "para_gap_pt": None,
            "box_tabs": False, "page_panels": False, "float_side_columns": False,
            "band_fill_measured": False, "fit_factor": 1.0, "fig_max_frac": 0.28, "pad_bottom_max_mm": 16, "has_header_band": True, "block_gap_mm": None, "box_pad_mm": None, "opener_in_body_face": False},
    # Measured off Old_ncert_Physics_Chapter_1.pdf: 612x784pt trim, 10.5pt body on 12.7pt
    # leading (= 1.21), and marginal figure columns the prose wraps around.
    "PHY": {"trim_pt": (612, 784), "leading": 1.21, "cap_ratio": 0.76,
            "break_per_page": True, "derive_columns": True, "band_tab": True, "corner_hang_mm": 6.0,
            "para_indent_mm": 6.4, "para_gap_pt": 0.0,
            "box_tabs": True, "page_panels": True, "float_side_columns": True,
            "band_fill_measured": True, "fit_factor": 1.0, "fig_max_frac": 0.21, "pad_bottom_max_mm": 13, "has_header_band": True, "block_gap_mm": None, "box_pad_mm": None, "opener_in_body_face": False},
    # Measured off inputs/ncert/latest/Class_11th/Chemistry/Chapter_2.pdf, not inherited:
    #   trim 630x784pt (0.803) -- wider than physics' 612 and far from A4
    #   10.5pt body on 12.6pt leading = 1.20
    #   NO page header band anywhere: 43 of 43 measured pages print none, and the consolidated
    #     palette has an opener rule bar and a footer rule but no page_header_band_fill at all.
    #     So band_tab and corner_hang are inert for this book.
    #   TWO-COLUMN body on every prose page (left ~0.124-0.486, right ~0.513-0.877), with blocks
    #     routinely running over the gutter -- derive_columns must be on, and it fires on nearly
    #     every page here rather than occasionally as in physics.
    #   Footnote rules are red #ed1c24; headings cyan #00adef; panels pink #f8c1d9 (problems),
    #     green #cbe7d3 with a #00a550 keyline (biographies), yellow #fffbd5 (figures),
    #     lavender #e0deef over peach #ffe4b8 (tables).
    #   Two body settings: two-column prose at 20.0px cap height, and the closing summary and
    #     exercises pages single-column at 18.0px. Nothing here forces one size on both.
    #   para_indent_mm 6.4 -- an 18pt first-line indent is present in the measured set, matching
    #     physics; para_gap_pt 0 because the measured median gap between consecutive body lines is
    #     1.75pt, i.e. the book runs its paragraphs on without extra leading.
    #   box_tabs True -- not because this book prints physics' rotated EXAMPLE tabs (it does not),
    #     but because that flag also gates the per-box measured FILL, and this chapter's pink,
    #     green, yellow and lavender panels are the whole point of its page design. The tabs list
    #     simply comes back empty.
    #   page_panels True -- the closing summary and exercises pages are printed on a tint covering
    #     the entire text block, recorded by A2L as an unnumbered box; without this they render
    #     white, which is the same defect physics had on its SUMMARY pages.
    #   float_side_columns False -- physics floats a NARROW marginal column beside full-measure
    #     prose. This book is genuinely two equal columns, so floating is the wrong model; the
    #     measured columns drive a real two-column split instead.
    #   band_fill_measured False -- there is no band to fill.
    "CHE": {"trim_pt": (630, 784), "leading": 1.20, "cap_ratio": 0.76,
            "break_per_page": True, "derive_columns": True, "band_tab": False,
            "corner_hang_mm": 2.0, "fig_max_frac": 0.15, "pad_bottom_max_mm": 13,
            "para_indent_mm": 6.4, "para_gap_pt": 0.0, "box_tabs": True,
            "page_panels": True, "float_side_columns": False,
            "band_fill_measured": False, "fit_factor": 1.0, "has_header_band": False, "block_gap_mm": 0.8, "box_pad_mm": None, "opener_in_body_face": True},
}
_DEFAULT_PROFILE = {"trim_pt": None, "leading": 1.28, "cap_ratio": 0.76,
                    "break_per_page": False, "derive_columns": False, "band_tab": False,
                    "corner_hang_mm": 6.0, "para_indent_mm": 0.0, "para_gap_pt": None,
                    "box_tabs": False, "page_panels": False, "float_side_columns": False,
                    "band_fill_measured": False, "fit_factor": 1.0, "fig_max_frac": 0.28, "pad_bottom_max_mm": 16, "has_header_band": True, "block_gap_mm": None, "box_pad_mm": None, "opener_in_body_face": False}


def subject_profile(chapter):
    """The layout profile for this chapter's subject. Unknown prefixes get the conservative
    default -- biology's approved settings -- rather than the newest subject's experiment."""
    # Merged OVER the defaults, so a row that predates a newly added field still resolves. Without
    # this, adding a field to one subject's row and not the others made `profile["new_field"]`
    # raise KeyError and abort the entire build -- which is exactly what happened when the CHE row
    # was rewritten without the seven fields a later change had introduced. A missing field should
    # fall back to the conservative default, never crash.
    merged = dict(_DEFAULT_PROFILE)
    merged.update(_SUBJECT_PROFILES.get((chapter or "")[:3].upper(), {}))
    return merged


def _print_geometry(layout, profile=None):
    """Real print dimensions for this book, derived from the measured page, not hardcoded.

    An earlier hand-built version of this reader carried biology's numbers literally (a 98.9mm
    banner, a 52.9mm contents panel, 107.7mm figures). Those are right for ONE chapter: chemistry
    measures 0.734 w/h and physics 0.781, neither of them A4, so literal millimetres would put
    both books on the wrong sheet. Everything here is therefore computed from A2L's measured
    page ratio and body cap height.

    Returns {page_w_mm, page_h_mm, body_pt, px_per_mm} -- px_per_mm converts a measured pixel
    bbox into millimetres on the printed sheet.
    """
    geo = (layout or {}).get("page_geometry") or {}
    ratio = geo.get("page_width_over_height") or (210 / 297)
    # The sheet comes from the subject profile, never from a global constant. Biology's approved
    # output is A4 (595x842pt, 13 sheets); physics measures 612x784pt off its own source PDF.
    # Hardcoding physics' trim here is exactly what silently re-paginated biology.
    prof = profile or _DEFAULT_PROFILE
    cap_ratio = prof.get("cap_ratio", _CAP_RATIO)
    trim = prof.get("trim_pt")
    if trim:
        page_w_mm, page_h_mm = trim[0] / 72 * 25.4, trim[1] / 72 * 25.4
    else:
        page_w_mm, page_h_mm = 210.0, 297.0

    # Body point size from the measured cap height: cap_px -> fraction of page height -> mm -> pt.
    pages = (layout or {}).get("full_detail_by_page") or {}
    caps, heights = [], []
    for rec in pages.values():
        c, h = rec.get("body_text_size_px_on_this_page"), rec.get("page_height_px")
        if isinstance(c, (int, float)) and isinstance(h, (int, float)) and h:
            caps.append(float(c))
            heights.append(float(h))
    if caps:
        cap_px = sorted(caps)[len(caps) // 2]
        page_h_px = sorted(heights)[len(heights) // 2]
        cap_mm = cap_px / page_h_px * page_h_mm
        body_pt = ((cap_mm / cap_ratio) / _MM_PER_IN * _PT_PER_IN
                   * _FIT_FACTOR * prof.get("fit_factor", 1.0))
        px_per_mm = page_h_px / page_h_mm
    else:
        body_pt, px_per_mm = 9.5, 8.0
    return {
        "page_w_mm": round(page_w_mm, 1),
        "page_h_mm": round(page_h_mm, 1),
        "body_pt": round(max(7.0, min(13.0, body_pt)), 2),
        "px_per_mm": px_per_mm,
    }


_BLEED_ROLES = {"chapter_banner", "rule_bar", "page_header_band", "footer_rule",
                "decorative_image", "page_number"}


def _content_inset_mm(layout, geo, profile=None):
    """(left_mm, right_mm, top_mm, bottom_mm) of the real printed text block.

    A fixed 22mm padding was used before, and it was wrong twice over: it is not the book's
    margin, and the measured column fractions were then applied INSIDE it, so the margin got
    counted a second time and the columns came out squeezed with dead space at the corners.
    These insets come from the measured bboxes of actual CONTENT elements -- full-bleed bands,
    decorative art and the folio tab are excluded, since those deliberately sit outside the
    text block and would drag the inset to zero.
    """
    xs0, xs1, ys0, ys1 = [], [], [], []
    for rec in ((layout or {}).get("full_detail_by_page") or {}).values():
        for el in rec.get("elements_in_reading_order") or []:
            bb = el.get("bbox")
            if not bb or el.get("role") in _BLEED_ROLES:
                continue
            xs0.append(bb[0]); ys0.append(bb[1]); xs1.append(bb[2]); ys1.append(bb[3])
    if not xs0:
        return 20.0, 20.0, 18.0, 18.0
    W, H = geo["page_w_mm"], geo["page_h_mm"]

    def pct(vals, q):
        vals = sorted(vals)
        return vals[max(0, min(len(vals) - 1, int(len(vals) * q)))]

    # 10th/90th percentile rather than min/max: one stray element should not define the margin.
    left = pct(xs0, 0.10) * W
    right = (1.0 - pct(xs1, 0.90)) * W
    top = pct(ys0, 0.10) * H
    bottom = (1.0 - pct(ys1, 0.90)) * H
    clamp = lambda v, lo, hi: max(lo, min(hi, v))   # noqa: E731
    # SIDE margins are capped tighter than the book's own. NCERT's generous outer margin exists to
    # hold marginal figures and the folio tab; this render puts figures in the measure instead, so
    # honouring that margin just threw away a quarter of the sheet (two 24mm margins out of 210mm)
    # and forced wide figures to overflow. A 16mm cap keeps a real printed margin while returning
    # ~17mm of usable measure per page, which is what lets the content fit.
    # Bottom cap is per subject. Physics was reserving 16mm below its text block while the book
    # reserves about 12.3mm -- its "2022-23" line sits at y 0.956 of a 784pt sheet, so only ~35pt
    # lies below the text. That extra 3.7mm is why book page 31 spilled its last two lines onto a
    # sheet of their own: the spill needed 33pt and the padding left only 26pt free. Tightening to
    # 13mm is MORE faithful to the measured page, not less. Biology keeps 16mm -- its approved
    # 15-sheet output is built on it.
    bottom_cap = (profile or _DEFAULT_PROFILE).get("pad_bottom_max_mm", 16)
    return (round(clamp(left, 8, 12), 1), round(clamp(right, 8, 12), 1),
            round(clamp(top, 6, 18), 1), round(clamp(bottom, 8, bottom_cap), 1))


def _page_measure(layout, page_num, fallback):
    """(left_frac, right_frac) of THIS page's own printed text block.

    A single chapter-wide measure was wrong for the opening page: BIO12O-ch03's body pages set a
    narrow ~0.56 column, but p001 spans 0.147-0.882 (0.73 of the width) because its contents panel
    and opening prose sit side by side under a full-width banner. Applying the body measure there
    squeezed the opener into a narrow column and left a third of the sheet blank down one side.
    Each page therefore uses the span A2L measured on it, falling back to the chapter median only
    where a page has no measured text.
    """
    rec = ((layout or {}).get("full_detail_by_page") or {}).get(f"page_{page_num:03d}") or {}
    txt = [e for e in rec.get("elements_in_reading_order") or []
           if e.get("role") in ("paragraph", "list", "box", "section_heading",
                                "major_heading", "contents_panel")
           and e.get("bbox")]
    # Figures are deliberately NOT counted. They overhang into the outer margin (that is what the
    # .recto/.verso margin rule is for), so including them stretched every body page's measure
    # from the book's 0.56 out to 0.71 and undid the narrow column entirely. The contents panel IS
    # counted, because on the opening page it genuinely shares the measure with the prose.
    if not txt:
        return fallback
    x0 = min(e["bbox"][0] for e in txt)
    x1 = max(e["bbox"][2] for e in txt)
    if x1 - x0 < 0.25:                      # implausibly narrow: trust the chapter instead
        return fallback
    return (max(0.02, x0), max(0.02, 1.0 - x1))


def _text_measure(layout):
    """(measure_frac, inner_frac, recto_pages) -- the book's real text column.

    Measured across BIO12O-ch03: the text column is ~0.57 of page width and is MIRRORED, starting
    at x~0.12 on a recto and x~0.32 on a verso, leaving a ~0.32 outer margin that the folio tab
    and the figures spill into (8 of 15 pages have a figure overhanging the text column by up to
    0.18 of page width).

    This replaces a symmetric margin, which was the single biggest reason the render did not look
    like the book: symmetric 12mm margins gave a ~186mm measure against the book's ~119mm, so
    every line ran about 40% long, nothing mirrored, and figures sized at their true printed width
    had no outer margin left to extend into.
    """
    inners, measures, recto = [], [], set()
    for key, rec in ((layout or {}).get("full_detail_by_page") or {}).items():
        txt = [e for e in rec.get("elements_in_reading_order") or []
               if e.get("role") in ("paragraph", "list", "box") and e.get("bbox")]
        if not txt:
            continue
        x0 = min(e["bbox"][0] for e in txt)
        x1 = max(e["bbox"][2] for e in txt)
        measures.append(x1 - x0)
        inners.append(min(x0, 1.0 - x1))
        try:
            num = int(key.split("_")[1])
        except (IndexError, ValueError):
            continue
        if x0 < 0.5 - (x1 - x0) / 2:      # column sits toward the LEFT edge
            recto.add(num)
    if not measures:
        return 0.80, 0.10, recto
    measures.sort(); inners.sort()
    return (measures[len(measures) // 2], inners[len(inners) // 2], recto)


def _opener_mm(layout, geo):
    """Banner / rule-bar / contents-panel sizes in mm, from their measured bboxes on page 1."""
    first = sorted(((layout or {}).get("full_detail_by_page") or {}))
    out = {"banner_h": 0.0, "banner_strip_h": 0.0, "bar_h": 0.0, "toc_w": 0.0}
    if not first:
        return out
    els = (layout["full_detail_by_page"][first[0]].get("elements_in_reading_order") or [])
    H, W = geo["page_h_mm"], geo["page_w_mm"]
    for el in els:
        bb, role = el.get("bbox"), el.get("role")
        if not bb or len(bb) != 4:
            continue
        if role == "chapter_banner":
            out["banner_h"] = max(out["banner_h"], (bb[3] - bb[1]) * H)
        elif role == "rule_bar":
            out["bar_h"] = max(out["bar_h"], (bb[3] - bb[1]) * H)
        elif role == "contents_panel":
            out["toc_w"] = max(out["toc_w"], (bb[2] - bb[0]) * W)
    return {k: round(v, 1) for k, v in out.items()}


def _banner_element(layout, page_num, role="chapter_banner"):
    """The measured element of `role` on this page, or (None, detail)."""
    detail = ((layout or {}).get("full_detail_by_page") or {}).get(f"page_{page_num:03d}") or {}
    for el in detail.get("elements_in_reading_order") or []:
        if el.get("role") == role and el.get("bbox"):
            return el, detail
    return None, detail


def _banner_image_html(args, layout, page_num, fig_dir, fig_rel_prefix,
                       role="chapter_banner", cls="banner-img"):
    """Crop the REAL chapter banner out of the page and return it as an <img>, or "".

    The banner was being rebuilt synthetically -- a tinted div with the title set in a substitute
    sans. That threw away everything else the real banner carries: on BIO12O-ch03 p001 that is the
    QR code and the uterus illustration, both inside the banner's own bbox. No amount of CSS
    reproduces artwork, so the honest render of a graphic panel is the graphic itself.
    """
    el, detail = _banner_element(layout, page_num, role)
    if not el:
        return ""
    pw = detail.get("page_width_px")
    ph = detail.get("page_height_px")
    if not (isinstance(pw, (int, float)) and isinstance(ph, (int, float))):
        return ""
    x0, y0, x1, y1 = el["bbox"]
    box = [x0 * pw, y0 * ph, x1 * pw, y1 * ph]
    img_path = os.path.join(fig_dir, f"p{page_num:03d}_{role}.png")
    try:
        lib_pdf.crop_box(args.pdf, page_num, box, img_path, unit="px")
    except Exception:
        return ""
    rel = f"{fig_rel_prefix}/p{page_num:03d}_{role}.png"
    return f'<img class="{cls}" src="{rel}" alt="{role}">'


def _page_strip_html(args, layout, page_num, fig_dir, fig_rel_prefix, which="top"):
    """Crop the page's whole FURNITURE STRIP -- everything above the first content element, or
    below the last -- and return it as an <img>, or "".

    Cropping decorative furniture element-by-element turned into an endless series of one-off
    additions: the header band, then the brown corner block, then the leaf logo, then the folio
    tab, then the print-year line. Each is a separate measured element (or, like the corner block,
    not measured at all), so each needed its own case. The strip above the text block IS all of
    that furniture at once, printed exactly as the book prints it -- so one crop replaces the lot
    and nothing new has to be added when a book decorates its margin differently.

    Bounds come from this page's own content: the topmost / bottommost element that is not
    full-bleed furniture. That is per-page rather than per-chapter, so recto/verso mirroring and
    pages with an unusually high first element are all handled without special-casing.
    """
    detail = ((layout or {}).get("full_detail_by_page") or {}).get(f"page_{page_num:03d}") or {}
    pw, ph = detail.get("page_width_px"), detail.get("page_height_px")
    if not (isinstance(pw, (int, float)) and isinstance(ph, (int, float))):
        return ""
    ys0, ys1 = [], []
    for el in detail.get("elements_in_reading_order") or []:
        bb = el.get("bbox")
        if bb and el.get("role") not in _BLEED_ROLES:
            ys0.append(bb[1])
            ys1.append(bb[3])
    if not ys0:
        return ""
    if which == "top":
        edge = min(ys0)
        # Extend past any TOP-ANCHORED full-bleed band so the strip swallows it whole. On a
        # chapter-opening page the banner runs well below the first content element, and cropping
        # only down to that element sliced the banner in half -- then the separate banner crop
        # drew the rest, so the green/brown band appeared TWICE. One strip, one band.
        for el in detail.get("elements_in_reading_order") or []:
            bb = el.get("bbox")
            if bb and el.get("role") in _BLEED_ROLES and bb[1] < 0.12:
                edge = max(edge, bb[3])
        if edge < 0.015:                       # content starts at the very top: no strip
            return ""
        box = [0, 0, pw, max(1.0, (edge * ph) - 4)]
    else:
        edge = max(ys1)
        # Reach UP to take in any bottom-anchored furniture. The print-year imprint measures
        # y 0.893-0.900 while content runs to 0.900, so a strip starting at the content edge
        # began just BELOW the year and came out blank -- 0.01% ink over 230px. Starting at the
        # top of the lowest furniture captures the imprint and the folio tab as printed.
        for el in detail.get("elements_in_reading_order") or []:
            bb = el.get("bbox")
            if bb and el.get("role") in _BLEED_ROLES and bb[3] > 0.80:
                edge = min(edge, bb[1])
        if edge > 0.985:
            return ""
        # A little headroom: the imprint sits only ~7 thousandths of the page tall, so a 4px
        # margin clipped its ascenders and it came out looking half-erased.
        box = [0, max(0.0, min(ph - 2, (edge * ph) - 16)), pw, ph]
    if box[3] - box[1] < 12:                   # too thin to carry anything
        return ""
    img_path = os.path.join(fig_dir, f"p{page_num:03d}_strip_{which}.png")
    try:
        lib_pdf.crop_box(args.pdf, page_num, box, img_path, unit="px")
    except Exception:
        return ""
    rel = f"{fig_rel_prefix}/p{page_num:03d}_strip_{which}.png"
    return f'<img class="page-strip strip-{which}" src="{rel}" alt="page {which} furniture">'


_ABS_FURNITURE_ROLES = ("page_number", "marginal_note")


def _abs_furniture_html(args, layout, page_num, fig_dir, fig_rel_prefix,
                        margin_mm=0.0):
    """Furniture that sits mid-page in the outer margin, placed at its MEASURED position.

    The folio tab is the case this exists for: BIO12O-ch03 prints it as an orange block carrying
    the page number at y 0.745-0.779, in the outer margin -- x 0.800-0.975 on a recto and
    0.025-0.202 on a verso, mirroring per spread. It is too high to fall in the bottom strip and
    too low for the top one, so neither crop reached it and every page was missing it. Absolute
    placement from the measured fractions handles the mirroring with no special-casing.
    """
    detail = ((layout or {}).get("full_detail_by_page") or {}).get(f"page_{page_num:03d}") or {}
    pw, ph = detail.get("page_width_px"), detail.get("page_height_px")
    if not (isinstance(pw, (int, float)) and isinstance(ph, (int, float))):
        return "", []
    out, lanes = [], []
    for i, el in enumerate(detail.get("elements_in_reading_order") or []):
        if el.get("role") not in _ABS_FURNITURE_ROLES:
            continue
        bb = el.get("bbox")
        if not bb:
            continue
        img_path = os.path.join(fig_dir, f"p{page_num:03d}_folio{i}.png")
        try:
            lib_pdf.crop_box(args.pdf, page_num,
                             [bb[0] * pw, bb[1] * ph, bb[2] * pw, bb[3] * ph],
                             img_path, unit="px")
        except Exception:
            continue
        rel = f"{fig_rel_prefix}/p{page_num:03d}_folio{i}.png"
        # Pin it to the OUTER SHEET EDGE rather than its measured x. In the book the folio sits
        # in a margin no text enters; in a reflowed document the content does not land at the same
        # vertical positions, so placing it at its measured x dropped the orange tab straight on
        # top of a paragraph. Pinned to the edge, with the matching side reserved by `lane` below,
        # it has a clear column of its own on whichever side the spread puts it.
        side = "left" if (bb[0] + bb[2]) / 2 < 0.5 else "right"
        # CLAMP it to the margin on its side. The measured tab is 17.5% of the page wide while
        # the margin is only ~11.8%, so honouring the measured width pushed it into the text
        # column and it landed on top of prose -- twice. A tab that is slightly narrower than the
        # book's is a far smaller fidelity loss than one sitting across a paragraph.
        margin_pct = (margin_mm / 210.0) * 100 if margin_mm else 11.0
        wpct = min((bb[2] - bb[0]) * 100, max(6.0, margin_pct - 1.0))
        out.append(
            f'<img class="abs-furniture" src="{rel}" alt="{el["role"]}" '
            f'style="{side}: 0; top: {bb[1] * 100:.2f}%; width: {wpct:.2f}%;">'
        )
        lanes.append((side, wpct))
    return "".join(out), lanes


def _caption_cut_px(layout, page_num, bbox, pad_frac=0.0):
    """The y (in page pixels) just above this figure's printed caption band, or None.

    A2L measures the caption as its own `figure_caption` element, so the band's top edge is a
    KNOWN number -- on BIO12O-ch03 p003 the figure ends at 1039px and its caption runs 1081-1118.
    Cutting there is exact. Every pixel heuristic tried before this half-worked: a fixed fraction
    sliced a caption mid-line, a brightness test fired on dense artwork and deleted two thirds of
    a diagram, and a tint test missed the band entirely because #fff2e2 has R=255. Use the
    measurement where it exists; the pixel detector stays only as the fallback for pages A2L has
    not measured.
    """
    detail = ((layout or {}).get("full_detail_by_page") or {}).get(f"page_{page_num:03d}") or {}
    ph, pw = detail.get("page_height_px"), detail.get("page_width_px")
    if not (isinstance(ph, (int, float)) and isinstance(pw, (int, float))):
        return None
    fy1, fx0, fx1 = bbox[3], bbox[0], bbox[2]
    best = None
    for el in detail.get("elements_in_reading_order") or []:
        if el.get("role") != "figure_caption" or not el.get("bbox"):
            continue
        cb = el["bbox"]
        cy0, cx0, cx1 = cb[1] * ph, cb[0] * pw, cb[2] * pw
        # The caption may sit just BELOW the figure's bbox or INSIDE it -- A2 often records a
        # bbox that already encloses the caption band (p004's figure is y 386-1100 while its
        # caption measures 1006-1104). Accept either, as long as the caption begins in the lower
        # part of the block, so a label near the top of the artwork is never mistaken for it.
        fy0 = bbox[1]
        lower = fy0 + 0.45 * max(1.0, fy1 - fy0)
        if cy0 < lower or cy0 > fy1 + 0.09 * ph:
            continue
        if min(fx1, cx1) - max(fx0, cx0) <= 0:
            continue
        best = cy0 if best is None else min(best, cy0)
    # A flat 6px lead-in is 2.2pt of a 2178px page, and A2L reports the caption's top edge to
    # three decimals -- a rounding of 0.001 is 2.2px on its own. On PHY12O-ch01 p015 that left a
    # sliced half-line of "FIGURE 1.8 A system of ..." along the bottom of the crop, printed
    # again as text directly underneath. `pad_frac` lets a book ask for a proportional lead-in;
    # at 0.0 the behaviour is exactly the flat 6px biology was approved with.
    return (best - max(6.0, pad_frac * ph)) if best is not None else None


def _figure_y_clamp(layout, page_num, bbox):
    """A top y limit (page px) so a figure crop does not swallow the line printed above it.

    _tight_bbox adds a proportional top margin to every crop to recover artwork that A2 recorded
    a few pixels short. On a page whose figure sits inside a worked example that margin runs
    straight into the example's prose: PHY12O-ch01 p021's FIGURE 1.13 came out with a sliced
    half-line reading "gravity ." floating above the diagram. A2's paragraph blocks carry no
    bbox, so _grown_bbox has nothing to stop against -- but A2L measured every one of them, so
    the bottom edge of whatever is printed directly above is a known number.
    """
    detail = ((layout or {}).get("full_detail_by_page") or {}).get(f"page_{page_num:03d}") or {}
    ph, pw = detail.get("page_height_px"), detail.get("page_width_px")
    if not (isinstance(ph, (int, float)) and isinstance(pw, (int, float))):
        return None
    fy0, fx0, fx1 = bbox[1], bbox[0], bbox[2]
    best = None
    for el in detail.get("elements_in_reading_order") or []:
        if el.get("role") not in ("paragraph", "list", "box", "equation",
                                  "section_heading", "major_heading") or not el.get("bbox"):
            continue
        eb = el["bbox"]
        ey1, ex0, ex1 = eb[3] * ph, eb[0] * pw, eb[2] * pw
        if ey1 >= fy0 + 0.004 * ph:            # not above this figure
            continue
        if min(fx1, ex1) - max(fx0, ex0) <= 0:  # not in the same column
            continue
        best = ey1 if best is None else max(best, ey1)
    return (best + 4) if best is not None else None


def _furniture_x_clamp(layout, page_num, bbox):
    """A right/left x limit for a figure crop so it does not swallow margin furniture.

    The folio tab is measured at x 0.800-0.975 on a recto, and figure bboxes reach 0.86 -- so the
    crop took the tab in with the artwork and the PDF showed a clipped orange tab reading "5"
    beside Figure 3.10. The tab is already drawn separately from its own measurement, so the crop
    simply has to stop short of it.
    """
    rec = ((layout or {}).get("full_detail_by_page") or {}).get(f"page_{page_num:03d}") or {}
    pw, ph = rec.get("page_width_px"), rec.get("page_height_px")
    if not (isinstance(pw, (int, float)) and isinstance(ph, (int, float))):
        return None, None
    x0, y0, x1, y1 = bbox
    left_lim = right_lim = None
    for el in rec.get("elements_in_reading_order") or []:
        if el.get("role") not in ("page_number", "marginal_note") or not el.get("bbox"):
            continue
        fb = el["bbox"]
        fy0, fy1 = fb[1] * ph, fb[3] * ph
        if min(y1, fy1) - max(y0, fy0) <= 0:        # no vertical overlap: cannot collide
            continue
        fx0, fx1 = fb[0] * pw, fb[2] * pw
        if fx0 >= x1 - 4:
            continue
        if (fx0 + fx1) / 2 > (x0 + x1) / 2:         # furniture to the RIGHT of the figure
            right_lim = fx0 - 6 if right_lim is None else min(right_lim, fx0 - 6)
        else:
            left_lim = fx1 + 6 if left_lim is None else max(left_lim, fx1 + 6)
    return left_lim, right_lim


def _palette_from_measurement(layout, fallback, sampled_strip=""):
    """(heading, banner, banner_strip, bar, panel_tint) sourced from the measured layout where
    it has a value, falling back per-slot to the hard-coded subject default. Per-slot rather
    than all-or-nothing: a chapter whose pages never show a contents panel still gets a correct
    heading colour from its own measurement instead of being thrown back wholesale."""
    if not layout:
        return fallback
    colors = dict(layout.get("colors_used_by_the_book") or {})
    if sampled_strip:
        colors["banner_strip_sampled"] = {"value": sampled_strip}

    def got(key, default):
        entry = colors.get(key)
        if isinstance(entry, dict) and entry.get("value"):
            return entry["value"]
        return default

    heading, banner, strip, bar, panel, box = fallback
    return (
        _pick_accent(colors, heading),
        got("chapter_banner_fill", banner),
        got("banner_strip_sampled", strip),
        got("opener_rule_bar_fill", bar),
        got("contents_panel_fill", panel),
        # A box panel's own tint, when the book gives it one. No sensible subject default
        # exists, so the fallback is empty and the CSS keeps its derived wash in that case.
        got("box_panel_fill", box),
    )


def _type_scale_from_measurement(layout):
    """{role: size_rel} measured for this chapter, used to set real type sizes in CSS."""
    out = {}
    for role, entry in ((layout or {}).get("type_scale_relative_to_body_text") or {}).items():
        v = entry.get("size_relative_to_body_text") if isinstance(entry, dict) else None
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            out[role] = float(v)
    return out


def _accent_for(chapter, layout=None):
    """The chapter's five core colours -- MEASURED where A2L measured them, hand-picked only as a
    fallback for whatever it did not.

    The hand-picked table below was sampled by eye from one chapter per subject, and for chemistry
    it is simply wrong: it names a dark red #b23a2e as the heading colour, while all 43 measured
    pages of CHE11L-ch02 report cyan -- #00adef on 23 pages for section headings and #29abe2 on 6
    for major headings. The only red anywhere in that book is its footnote rule (#ed1c24 on 8
    pages). The guessed red produced red headings and a dark red strip the page never prints.

    A hand-picked palette is exactly what step A2L exists to replace, so the measurement wins and
    the table is only consulted for a value that was never measured.
    """
    base = list(_SUBJECT_ACCENTS.get(chapter[:3].upper(), _DEFAULT_ACCENT))
    cols = ((layout or {}).get("colors_used_by_the_book") or {})

    def measured(key):
        v = (cols.get(key) or {}).get("value")
        return v if isinstance(v, str) and re.fullmatch(r"#[0-9a-fA-F]{6}", v) else None

    def _chromatic(v):
        """True when a colour carries real hue. The accent is a STRUCTURAL colour -- it paints
        rules, captions, box bars and tabs -- so an achromatic value must never become it.
        PHY12O-ch01 is the case that matters: its numbered x.y headings are genuinely grey
        (#6d6e71), while the rules, captions and box bars the accent drives are cyan (#00adef).
        Taking the heading colour blindly turned the whole book grey."""
        r, g, b_ = (int(v[i:i + 2], 16) for i in (1, 3, 5))
        return max(r, g, b_) - min(r, g, b_) > 25

    # The accent is whichever measured colour actually carries the book's hue, tried in order of
    # how reliably each role reports it.
    for key in ("section_heading_text_color", "major_heading_text_color",
                "figure_caption_text_color", "opener_rule_bar_fill", "footer_rule_fill"):
        got = measured(key)
        if got and _chromatic(got):
            base[0] = got
            break
    for idx, key in ((1, "chapter_banner_fill"), (2, "page_header_band_fill"),
                     (3, "opener_rule_bar_fill"), (4, "contents_panel_fill")):
        got = measured(key)
        if got:
            base[idx] = got
        elif base[0] != _SUBJECT_ACCENTS.get(chapter[:3].upper(), _DEFAULT_ACCENT)[0]:
            # This value was never measured AND the accent has been corrected away from the
            # hand-picked one, so the hand-picked companion tints no longer belong to the same
            # book. CHE11L-ch02 prints no chapter banner and no header band, so those two were
            # falling back to a pale red (#f3dcd6) and a dark red strip (#8c3326) chosen to go
            # with an accent the measurement has just disproved. Derive them from the colour the
            # book actually uses instead of leaving a red wash under a cyan book.
            soft, wash = _tints(base[0])
            base[idx] = wash if idx in (1, 4) else soft
    return tuple(base)


def _tints(hex_colour):
    """(soft, wash) -- the heading colour mixed toward white at ~82% and ~95%. Used for rules and
    very light panel fills, so adding a subject means naming five real book colours, not nine."""
    h = hex_colour.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))

    def mix(f):
        return "#%02x%02x%02x" % tuple(round(c + (255 - c) * f) for c in (r, g, b))

    return mix(0.82), mix(0.95)


# The page deliberately commits to ONE light look instead of offering a dark theme: it exists to
# be read directly against a photograph of a printed white page, and a dark extraction column
# beside a white scan is exactly what made the first version hard to follow. Every colour is
# painted explicitly so the page holds its own look whatever the viewer's OS theme is.
_CSS_TMPL = """
/* NCERT sets its English body in a Bookman-class face (wide, round letterforms, visible on the
   scan). Bookman Old Style is not installed on most machines, so TeX Gyre Bonum -- a free metric
   clone -- ships in fonts/ and is listed after it, so a real install still wins. The chapter
   title is a light geometric sans (Century Gothic class); TeX Gyre Adventor is the stand-in. */
@font-face { font-family: "TeX Gyre Bonum"; src: url("fonts/texgyrebonum-regular.otf") format("opentype"); font-weight: 400; font-style: normal; font-display: swap; }
@font-face { font-family: "TeX Gyre Bonum"; src: url("fonts/texgyrebonum-italic.otf") format("opentype"); font-weight: 400; font-style: italic; font-display: swap; }
@font-face { font-family: "TeX Gyre Bonum"; src: url("fonts/texgyrebonum-bold.otf") format("opentype"); font-weight: 700; font-style: normal; font-display: swap; }
@font-face { font-family: "TeX Gyre Bonum"; src: url("fonts/texgyrebonum-bolditalic.otf") format("opentype"); font-weight: 700; font-style: italic; font-display: swap; }
@font-face { font-family: "TeX Gyre Adventor"; src: url("fonts/texgyreadventor-regular.otf") format("opentype"); font-weight: 400; font-style: normal; font-display: swap; }
:root {
  --font-body: "Bookman Old Style", "Bookman", "TeX Gyre Bonum", "Times New Roman", Times, serif;
  --font-display: "Century Gothic", "TeX Gyre Adventor", "Avenir Next", Futura, sans-serif;
  --font-figure: Arial, Helvetica, sans-serif;
  --font-math: "Latin Modern Math", "CMU Serif", "Times New Roman", serif;
  --viewer-bg: #282828;
  --viewer-bar: #3c3c3c;
  --viewer-ink: #f1f1f1;
  --paper: #ffffff;
  /* The book's paper is WHITE. Measured on the real page scan (#ffffff); an earlier version of
     this stylesheet set a cream #fffdf8 here, which was an invention -- NCERT's body pages are
     plain white, and a tinted ground is immediately visible as "not the book". */
  --book-paper: #ffffff;
  --ink: #1f1b16;
  --rule: #d9d2c4;
@SIZE_VARS@
  --accent: @ACCENT@;
  --heading: @ACCENT@;
  --banner: @BANNER@;
  --banner-strip: @BANNER_STRIP@;
  --bar: @BAR@;
  --panel-tint: @PANEL_TINT@;
  --box-fill: @BOX_FILL@;
  --caption-ink: @CAPTION_INK@;
  --caption-band: @CAPTION_BAND@;
  --folio-fill: @FOLIO_FILL@;
  --folio-ink: @FOLIO_INK@;
  --accent-soft: @ACCENT_SOFT@;
  --accent-wash: @ACCENT_WASH@;
  --panel: #f3efe7;
  --muted: #847b6b;
  --mono: "IBM Plex Mono", "SF Mono", Menlo, monospace;
}
* { box-sizing: border-box; }
/* Pages are laid out at TRUE PRINT SIZE, so type is in print units: @BODY_PT@pt body on the
   measured line pitch, derived from this book's own cap height and page ratio (see
   _print_geometry). Every rem below scales from that, and the toolbar's zoom scales the whole
   sheet the way a PDF viewer does -- so proportions never drift with the window width. */
html { font-size: @BODY_PT@pt; }
body {
  margin: 0; background: var(--viewer-bg); color: var(--ink);
  font-family: var(--font-body);
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
  /* NCERT sets its body text TIGHT. Measured independently by the layout workers on all three
     books: cap-to-baseline ~20-21px on a ~36px line pitch, i.e. a pitch of about 1.75x the cap
     height. Georgia's cap height is ~0.70em, so that pitch is ~1.25em -- against the 1.62 this
     stylesheet used before, which set the page ~30% looser than the book and was the single
     biggest reason the type "looked different" even once the colours and sizes were right.
     (The pitch itself is not yet an A2L schema field -- see docs/OPEN_QUESTIONS.md -- so this
     is derived from the three agents' reported measurements rather than read from the data.) */
  /* 12.7pt leading on 10.5pt body, measured off the source PDF = 1.21. We were setting 1.28,
     which costs roughly one line of text in every seventeen. */
  line-height: @LEADING@;
}
/* === PDF-viewer chrome: a toolbar and one real sheet per page on a dark ground === */
.pdf-toolbar {
  position: sticky; top: 0; z-index: 30; height: 52px; padding: 0 20px;
  display: flex; align-items: center; justify-content: space-between; gap: 16px;
  background: var(--viewer-bar); color: var(--viewer-ink);
  font: 15px/1 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  box-shadow: 0 1px 4px rgba(0,0,0,.5);
}
.pdf-name { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-width: 0; }
.pdf-mid { display: flex; align-items: center; gap: 6px; flex-shrink: 0; }
.pdf-toolbar input {
  width: 42px; height: 28px; text-align: center; font: inherit; color: inherit;
  background: #191919; border: 0; border-radius: 2px;
}
.pdf-of { margin-right: 4px; }
.pdf-sep { width: 1px; height: 22px; background: #5f6368; margin: 0 8px; }
.pdf-zoom { background: #191919; padding: 6px 8px; border-radius: 2px; min-width: 56px; text-align: center; }
.pdf-toolbar button {
  width: 32px; height: 32px; border: 0; border-radius: 50%; background: transparent;
  color: inherit; font: 20px/1 inherit; cursor: pointer;
}
.pdf-toolbar button:hover { background: rgba(255,255,255,.1); }
#viewer { padding: 10px 0 30px; }
/* One book page = one sheet at this book's measured size, centred like a PDF page. */
#viewer .page-row {
  /* A FIXED sheet, not a minimum. With `min-height` the sheet simply grew past the page height
     when its content did -- nothing was clipped and nothing was hidden, but printing then split
     the oversized box across several sheets (15 sheets became 27 PDF pages). Pinning the height
     is what makes a sheet a sheet; the script scales each page's content to fit inside it. */
  /* Content height, not a forced full sheet. Padding every page out to @PAGE_H@mm meant any
     page that ran even slightly over produced a second, near-empty sheet carrying just the
     footer -- 7 of 23 pages were blank that way. Letting each page be as tall as its content
     makes the chapter flow continuously: content slides on and the next page follows it. */
  display: block; width: @PAGE_W@mm; margin: 0 auto 10px;
  background: var(--book-paper); border: 0; box-shadow: 0 1px 6px rgba(0,0,0,.55);
  position: relative;
}
/* The pane is scaled to fit its sheet by the script below; the transform needs a fixed origin
   and a width that compensates for the scale, or the text reflows as it shrinks. */
#viewer .page-row.single .pane.extracted { transform-origin: top left; }
/* Hard containment. Every repeated "content running off the side" was something inside the page
   being wider than the page: a figure at its printed mm width, a table, a negative margin. One
   rule makes that impossible regardless of what any other rule asks for. */
#viewer .page-row, #viewer .pane.extracted { max-width: 100%; }
/* Containment WITHOUT `!important` on the elements that carry a per-page inline width.
   A stylesheet `!important` beats an inline style, so the earlier version silently overrode every
   per-page figure width and strip bleed -- which is why three rounds of changes produced no
   measurable difference at all. The page box itself still clips anything that overruns. */
#viewer .pane.extracted > *, #viewer .col-split, #viewer .col-offset,
#viewer .block, #viewer .crop { max-width: 100% !important; }
#viewer .table-wrap { max-width: 100%; overflow-x: hidden; }
/* Padding = the book's own measured text-block inset, so the content box IS the printed
   measure and the measured column fractions land where the page puts them. */
#viewer .page-row.single .pane.extracted {
  max-width: none; margin: 0; padding: @PAD_T@mm @PAD_R@mm @PAD_B@mm @PAD_L@mm;
}
@page { size: @PAGE_W@mm @PAGE_H@mm; margin: 0; }
@media print {
  body { background: #fff; }
  .pdf-toolbar { display: none; }
  #viewer { zoom: 1 !important; padding: 0; }
  /* In PRINT a sheet is only as tall as its content. On screen the sheet is padded out to the
     full page height so it looks like a page, but carrying that `min-height` into print meant a
     book page whose content ran a few millimetres over occupied a second sheet that held nothing
     but the footer strip -- 9 of 24 pages came out near-empty (0.03% ink, no text). With the
     minimum dropped, `break-after: page` still gives one sheet per book page and the empty tails
     disappear. */
  /* Exactly ONE sheet per book page. With the bottom strip anchored, the only thing still
     pushing a page over the edge is slack padding, so clipping to the sheet costs whitespace
     rather than content -- verified by comparing the PDF's extracted text before and after. */
  /* NOT clipped to the sheet. Clipping was tried and measured: it dropped the closing words of
     six paragraphs (p002, p003, p004, p007, p010, p011), each verified present in the unclipped
     PDF and absent from the clipped one. Losing a sentence to win a page count is never the right
     trade, so a page that still runs long continues onto the next sheet. */
  /* NO forced page break per book page. `break-after: page` is what created the empty sheets:
     a page whose content overran by a few millimetres got a whole sheet for the remainder. With
     it gone the text flows across sheets and every printed page fills. */
  /* break-BEFORE, not break-after. Each book page begins a fresh sheet, so its band is always at
     the head of a sheet -- with break-after the band landed wherever the previous page happened
     to end, often near the foot. And because there is no min-height, a page whose content runs
     long simply continues onto the next sheet instead of leaving a blank one behind, which is
     what break-after + min-height produced. */
  /* CONTINUOUS FLOW. Forcing a sheet per book page put every band at a sheet top, but a book
     page's reflowed content almost never fills a sheet exactly, so each ended early -- measured
     63% of sheet height used against the book's 100%, with 21 of 70 pages under half. Letting the
     text run on fills every sheet the way the book does; the band and folio still mark where each
     book page begins. */
  /* Each book page starts a fresh sheet, so its band is always at the head of a sheet rather
     than landing wherever the previous page ended. Combined with the merged example boxes,
     splittable prose and the 28%-of-sheet figure cap, this no longer leaves the blank sheets it
     did before those fixes. */
  /* CONTINUOUS FLOW -- the book's own behaviour. NCERT fills every page to 100% of its height;
     forcing a sheet per book page gave 63% fill with 5 blank and 15 half-empty pages in physics,
     because a reflowed page rarely matches a sheet exactly. Making the sheet A4 did not help
     (a taller sheet just leaves more room empty on a short page). Flowing the text fills every
     sheet; the band and the folio still mark where each book page begins. */
  /* Each book page STARTS a new sheet, so its band is always at the head of a sheet -- never
     mid-page. Height is AUTO, not a fixed sheet: a book page whose content runs long simply
     continues onto a second sheet rather than being clipped, and one that runs short ends the
     sheet early rather than padding it out to a blank. Forcing a FIXED sheet height was what
     produced 5 blank and 15 half-empty pages; the page break itself was never the problem. */
  #viewer .page-row {
    margin: 0; box-shadow: none; min-height: 0; height: auto;
  }
  /* Sheet-per-book-page is opt-in per chapter. Physics needs it (its bands drifted to mid-sheet
     under continuous flow); biology measured better flowing -- 13 sheets, 0 blank, 84% fill --
     so it keeps flowing and is not forced into breaks it does not need. */
  #viewer.break-per-page .page-row { break-before: page; page-break-before: always; }
  #viewer.break-per-page .page-row:first-child { break-before: auto; page-break-before: auto; }
  /* The band must not be orphaned at the foot of a sheet by its own content. */
  #viewer .page-band { break-after: avoid; page-break-after: avoid; }
  .print-band { display: none !important; }
  #viewer .page-row > .pane.extracted { padding-bottom: 6mm; }

  /* PRINT SAFETY: no floats, no absolute positioning, no fixed heights.
     Those three are fine on screen but do not paginate reliably -- Chrome was CLIPPING paragraphs
     mid-line at the sheet edge rather than carrying them over, because a floated figure and an
     absolutely-positioned furniture strip cannot be split across printed sheets. Correctness of
     the text comes before fidelity of the furniture's placement, so for print everything becomes
     ordinary flow content that can break where it needs to.
     Note this also invalidated my earlier verification: searching the PDF's TEXT LAYER found the
     clipped words (they are still in the layer) and reported no loss, while the page visibly cut
     them. Visual clipping has to be checked by rendering, not by text search. */
  /* Floats are KEPT in print. They were disabled here when the sheet still had a fixed height
     and absolutely-positioned furniture, a combination Chrome could not paginate -- but those are
     both gone now, and without floats the text cannot wrap around a figure, which is exactly what
     fills the book's pages. */
  /* Floats really are kept now. The rule that used to sit here read `float: none !important`,
     flatly contradicting the comment above it, so in print every figure became a full-width block
     and no text ever wrapped beside one. That single override is why our sheets carried 10% ink
     against the book's 20%: NCERT's p2 runs six rod diagrams and their caption down a left column
     with prose beside them, then resumes full width below. */
  #viewer .fig-float { break-inside: avoid; }
  /* The folio stays visible in print too -- it was hidden because absolute positioning cannot
     paginate, but a tab the reader cannot see is not a page number. It is drawn from CSS at the
     sheet edge instead of cropped, so there is nothing to paginate. */
  #viewer .abs-furniture { display: none; }
  #viewer .folio-tab { display: block; }
  #viewer .strip-bottom { position: static !important; margin: 3mm 0 0 !important; }
  #viewer .page-foot { position: static !important; }
  /* Only artwork is unbreakable. `break-inside: avoid` on every block meant a paragraph that did
     not fit moved whole to the next sheet, leaving the rest of the page blank -- but real books
     split paragraphs across pages and only keep figures intact. Allowing prose to break is what
     fills the foot of a page. */
  #viewer .crop, #viewer .fig-float, #viewer .block-figure,
  #viewer .block-table { break-inside: avoid; }
  /* ...except a table too long to fit a sheet, which must fragment or it empties its own page.
     Rows stay intact and the header repeats, so a split table still reads correctly. */
  #viewer .block-table:has(.table-long) { break-inside: auto; }
  #viewer .table-long { break-inside: auto; }
  #viewer .table-long table { break-inside: auto; }
  #viewer .table-long thead { display: table-header-group; }
  #viewer .table-long tr { break-inside: avoid; }
  /* A merged worked example MAY split across sheets -- the book splits long examples too. Keeping
     it whole made each one an unbreakable block that jumped to the next sheet when it did not fit,
     leaving the rest of the page empty (8 blank and 15 sparse pages in physics). Only the artwork
     inside it stays intact. */
  /* A box taller than a sheet must be allowed to break, but `auto` alone stranded a two-line
     fragment on the following sheet, below a band, with the rest of the page empty. */
  #viewer .box-group { break-inside: auto; orphans: 2; widows: 2; }
  #viewer .block-heading { break-after: avoid; }
}
header.doc-head {
  padding: 26px 32px 18px; border-bottom: 3px solid var(--accent);
  background: var(--panel); position: sticky; top: 0; z-index: 20;
}
header.doc-head h1 { margin: 0 0 6px; font-size: 1.55rem; letter-spacing: .01em; }
header.doc-head .meta { color: var(--muted); font-size: .84rem; font-family: var(--mono); }

/* Two panes side by side, each its own natural height (align-items: start) rather than both
   stretched to the row's height. The pane LABEL is sticky inside the row, so while scrolling
   a tall page you always know which page and which side you are looking at. */
.page-row {
  display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 0;
  border-bottom: 2px solid var(--accent-soft);
  align-items: start;
}
@media screen and (max-width: 1000px) { .page-row { grid-template-columns: 1fr; } }
/* --no-scans: one column of this pipeline's own rendering, centred like a book page. */
.page-row.single { grid-template-columns: minmax(0, 1fr); }
/* Measured two-column stretches: the contents panel beside the opening prose, or text
   narrowed beside a figure. Column widths come from A2L's measured fractions, not a guess. */
.col-split { display: grid; gap: 0 26px; align-items: start; margin: 0 0 4px; }
.col-split > .col { min-width: 0; overflow-wrap: break-word; }
.col-split > .col > * { max-width: 100%; }
/* A one-sided column run: a marginal sidebar or an outer-margin figure, offset to the
   position it was measured at rather than padded out into an empty half-grid. */
.col-offset { min-width: 0; margin-bottom: 4px; }
/* On the page the book wraps prose beside a marginal figure or sidebar, so it floats and the
   neighbouring paragraph runs down its side. `clear` keeps headings/figures/lists off the float. */
.col-offset.wrap { float: right; margin: 1mm 0 2mm 5mm !important; }
/* A figure set into the measure, with prose wrapping around it -- the book's own arrangement. */
/* A floated figure takes the share the page measured for it, up to most of the measure. */
.fig-float { max-width: 62%; }\n/* A tall single-side run stays in normal flow so it can fragment across a sheet. */\n.col-tall { break-inside: auto; margin: 0 0 2mm; }
.fig-float.float-right { float: right; margin: 0 0 3mm 5mm; }
.fig-float.float-left  { float: left;  margin: 0 5mm 3mm 0; }
.fig-float .block { max-width: none; margin-bottom: 2mm; }
.fig-float .caption { max-width: none; }
.block-heading, .block-figure, .block-table, .block-list, .col-split, .gaps { clear: both; }
.col-offset .block { max-width: none; }
/* NO negative-margin overhang. The book does let a figure reach into the outer margin, but
   reproducing it with negative margins repeatedly pushed figures off the sheet edge and clipped
   the text beside them. Nothing may exceed the page box; a faithful overhang is not worth a
   cut paragraph. */
@media screen and (max-width: 760px) {
  .col-offset { margin-left: 0 !important; width: 100% !important; }
}
.col-split .block { max-width: none; }
@media screen and (max-width: 760px) { .col-split { grid-template-columns: 1fr !important; } }
.page-row.single .pane.extracted {
  max-width: 54rem; margin: 0 auto; padding: 26px 34px 36px;
}
/* Review-only scaffolding has no place in a clean render of the chapter itself. */
body.clean .block-n,
body.clean .furniture-note,
body.clean .crop-note,
body.clean .gaps,
body.clean .qa-tag,
body.clean .labels,
body.clean details.table-rows > summary,
body.clean details.eqn-src > summary,
body.clean details.latex-fold > summary { display: none; }
body.clean details.table-rows > *:not(summary),
body.clean details.latex-fold > *:not(summary) { display: block; }
/* The equation's printed original stays FOLDED in the reader: the rendered LaTeX is the
   equation, and the crop is only there to check against. Its summary text ("printed original")
   was leaking into the page as body copy. */
body.clean details.eqn-src,
/* ".await" is a review note ("LaTeX transcription pending ..."). It was printing on
   the page, and on p022 it contradicted that page's own gap note. */
body.clean .await { display: none; }
body.clean details.eqn-src { display: none; }
/* The toolbar carries the page number; the marks below are review aids the printed page lacks. */
body.clean .pane-label { display: none; }
body.clean strong { border-bottom: none; }
body.clean .crop { border: none; }
body.clean .pane-label { opacity: .45; }
.pane { padding: 18px 26px 28px; min-width: 0; }
/* Both panes sit on book-white paper so the extraction reads as the same page, not as a
   different medium. The grey chrome is confined to the header/TOC and the small mono labels. */
.pane.original { background: var(--panel); border-right: 1px solid var(--rule); }
.pane.extracted { background: var(--book-paper); }
.pane-label {
  font-family: var(--mono); font-size: .74rem; letter-spacing: .08em; text-transform: uppercase;
  color: var(--accent); margin-bottom: 14px; position: sticky; top: 92px;
  background: inherit; padding: 5px 0; z-index: 5;
  border-bottom: 1px solid var(--accent-soft);
}
.page-badge {
  display: inline-block; font-family: var(--mono); font-size: .76rem; color: var(--muted);
  border: 1px solid var(--rule); border-radius: 3px; padding: 1px 8px; margin-left: 8px;
}
/* The scan fills its pane -- it is the reference the extraction is judged against, so it
   should be as large as the column allows, not a thumbnail floating in whitespace. */
.original img.page-scan {
  width: 100%; height: auto; border: 1px solid var(--rule);
  box-shadow: 0 2px 14px rgba(0,0,0,.16); display: block; background: #fff;
}
.furniture-note {
  font-family: var(--mono); font-size: .74rem; color: var(--muted); margin-bottom: 22px;
  padding: 7px 11px; border-left: 2px solid var(--rule); background: var(--panel);
  word-break: break-word;
}
/* === The chapter-opening page, rebuilt as the book prints it ===
   Measured off the real scan: a dark strip, then a tall tinted banner carrying the chapter
   number and name in a LIGHT GEOMETRIC SANS (not the body serif), then a full-width coloured
   rule bar, then a tinted section-contents panel. */
/* The page band: a full-bleed bar at the head of every page, in the book's own proportions --
   a coloured bar over ~73% of the width with a darker corner block beyond it, mirrored per
   spread, and the running header set small beneath it. */
/* The band as the book prints it: a tinted strip closed by a rule in the accent colour, with a
   grey tab hanging below it carrying the small square mark and the running header. */
.print-band { display: none; }
.page-band {
  display: flex; height: 12mm; position: relative;
  border-bottom: 1.1mm solid var(--accent);
  /* Opaque, and painted ABOVE the page body. A tall box or equation on the PREVIOUS book page can
     overflow past its own page-row and land in this row; without an opaque fill and a z-index the
     band showed that stray panel straight through it, with the overflowing line sitting level
     with the running header. The band is page furniture and always reads on top. */
  /* No fill on the band itself: the bar carries the colour and the gap beside the
     corner artwork is bare paper in the book. Filling the whole band painted that
     gap green. z-index keeps furniture above any content that overflows into it. */
  background: transparent; z-index: 6; isolation: isolate;
  /* max-width: none -- the band is given the SHEET width inline, and a `max-width: 100%`
     inherited from the pane clamped it back to the content box, scaling every measured
     proportion inside it by 0.86. box-sizing:content-box so the width IS the width. */
  /* ANCHORED TO THE SHEET, not offset out of the text pane. The band used to be a flow item
     inside the pane pulled left by a negative margin equal to the pane's padding; that arithmetic
     disagreed with the pane on recto pages (the pane pads with _ol, the band was offset by pad_l)
     and put the band 24mm outside the sheet, with the corner artwork hanging off the page. The
     page-row IS the sheet, so position against it and there is no arithmetic left to get wrong --
     and the band is genuinely sheet-wide, which is what the measured mm proportions inside it
     (73.2% bar, 13.6% artwork) were measured against. */
  position: absolute; left: 0; top: 0; width: 100%; margin: 0 !important;
  max-width: none !important; box-sizing: border-box;
  /* Reserve the corner artwork's measured hang. The artwork is positioned absolutely inside the
     band and drops past its lower edge -- 14.0mm on every measured biology body page -- so a flat
     5mm left it covering the first two lines of prose ("The morula continues to d......astocyst"
     was unreadable on p012). The book starts its body text clear of the artwork; so do we. */
  margin-bottom: @CORNER_HANG@mm;
}
/* The page body stacks below the band, never over it. */
#viewer .page-row { position: relative; }
#viewer .page-band + * { margin-top: 0; }
.band-tab {
  /* INSIDE the band, not hanging below it. Hanging worked while each book page started a sheet,
     but under continuous flow the band sits wherever the previous page ended, and a tab hanging
     past it was drawn straight over the following lines. */
  position: absolute; left: 16%; top: 0; height: 100%; z-index: 2;
  background: var(--panel); color: #3c3c3c;
  font: 400 1.02rem/1 var(--font-display);
  padding: 0 6mm 0 4mm; display: flex; align-items: center; gap: 3mm;
  white-space: nowrap;
}
/* Biology sets its running header as small plain caps beside the band -- measured with no fill
   on 29 pages -- rather than in physics' grey tab. */
.band-running {
  position: absolute; left: 3mm; top: 0; height: 100%;
  display: flex; align-items: center;
  font: 700 .60rem/1 var(--font-display); letter-spacing: .13em;
  color: var(--accent); white-space: nowrap; z-index: 2;
}
.band-verso .band-running { left: auto; right: 3mm; }
.band-mark {
  width: 3.2mm; height: 3.2mm; flex: 0 0 auto; position: relative; display: inline-block;
  background: #8a8a8a;
}
.band-mark::after {
  content: ""; position: absolute; left: 1.6mm; top: 1.6mm;
  width: 3.2mm; height: 3.2mm; background: var(--accent);
}
.page-band .band-bar { background: var(--banner-strip); }
/* No CSS fill on the corner block: the cropped corner artwork already contains the book's brown
   block, so painting one behind it showed TWO browns, offset from each other. The image is the
   corner. */
.page-band .band-corner { background: transparent; position: relative; }
/* The corner mark sits on the dark block and hangs just below the band, as printed. */
/* The artwork fills the corner block and hangs below the band, as the book prints it. */
/* 219% of the band: measured artwork spans y 0.0684-0.1547 against a band of
   0.0684-0.1077, i.e. 25.6mm over an 11.7mm band. */
.band-logo { position: absolute; left: 0; top: 0; height: @LOGO_H@%; width: 100%;
             object-fit: fill; object-position: left top; }
.band-verso .band-logo { left: auto; right: 0; transform: scaleX(-1); }
/* Measured off the source PDF's body pages, not approximated by a single flex value:
     verso  green x 0.024-0.756 | gap 0.756-0.837 | brown x 0.837-0.973
     recto  brown x 0.024-0.161 | gap 0.161-0.241 | green x 0.241-0.973
   The green bar is 73.2% of the sheet and the corner artwork 13.6%, separated by a bare-paper
   GAP of ~8% and inset ~2.5% from the trim edge. `flex: 1 1 auto` on the corner gave it
   everything the bar left over -- 27% of the sheet, bled to the edge, with no gap -- so the
   artwork read as twice its printed width and the paper gap the book prints disappeared. */
.band-recto .band-bar { flex: 0 0 73.2%; margin-left: 2.4%; }
.band-recto .band-corner { flex: 0 0 13.6%; margin-left: 8.1%; margin-right: 2.7%; }
.band-verso { flex-direction: row-reverse; }
.band-verso .band-bar { flex: 0 0 73.2%; margin-right: 2.4%; }
.band-verso .band-corner { flex: 0 0 13.6%; margin-right: 8.1%; margin-left: 2.7%; }
.band-caption {
  display: none;
  overflow: hidden;
  font: 700 .62rem/1 var(--font-display); letter-spacing: .14em; color: var(--muted);
  margin: 2mm 0 6mm; text-transform: uppercase;
}
.band-verso + .band-caption { text-align: right; }
/* The year sits on the side AWAY from the corner block, which the corner mark overhangs. */
.band-year { float: left; opacity: .75; }
.band-verso + .band-caption .band-year { float: right; }
/* The page's furniture strips -- band, corner block, logo, running header, folio tab, print
   year -- cropped straight from the page and bled to the sheet edges, exactly as printed. */
/* Mid-page margin furniture (the folio tab), positioned on the SHEET from its measured
   fractions -- so it lands in the outer margin and mirrors recto/verso by itself. */
.abs-furniture { position: absolute; z-index: 2; height: auto; }
/* The folio tab, as the book prints it: a filled block carrying the page number, set in the
   outer margin and bleeding to the sheet edge. Drawn in CSS so it survives printing. */
.folio-tab {
  position: absolute; top: 74.5%; z-index: 3;
  background: var(--folio-fill); color: var(--folio-ink);
  font: 700 0.95rem/1 var(--font-display);
  padding: 2.6mm 3mm; min-width: 16mm; text-align: center;
}
.folio-right { right: 0; }
.folio-left { left: 0; }
.page-strip {
  display: block; width: calc(100% + @PAD_L@mm + @PAD_R@mm); height: auto; clear: both;
}
.strip-top { margin: calc(-1 * @PAD_T@mm) calc(-1 * @PAD_R@mm) 4mm calc(-1 * @PAD_L@mm); }
/* The bottom strip is page FURNITURE at a fixed position, not flow content. Leaving it in the
   flow added its own height to every page, which pushed 9 of 15 pages a few millimetres past the
   sheet -- and each of those spilled onto a second, near-empty sheet (0.03% ink, no text).
   Anchoring it to the foot of the sheet takes it out of the height calculation entirely. */
.strip-bottom {
  position: absolute; left: 0; right: 0; bottom: 0; width: 100%;
  margin: 0;
}
/* The real banner, cropped from the page: full sheet width, bleeding past the page padding. */
.banner-img {
  display: block; width: calc(100% + 2 * @MARGIN@mm);
  margin: calc(-1 * @MARGIN@mm) calc(-1 * @MARGIN@mm) 4mm; height: auto;
}
/* The print-year imprint, centred at the foot of the sheet as the book sets it. */
.page-foot {
  position: absolute; left: 0; right: 0; bottom: 8mm; text-align: center;
  font-size: .78rem; color: var(--ink); clear: both;
}
.chapter-banner {
  background: var(--banner); border-top: 11mm solid var(--banner-strip);
  height: @BANNER_H@mm; padding: 38% 0 0 9mm;
  margin: 0;   /* bleed set inline per page, like the band */
  display: flex; flex-direction: column; justify-content: flex-end; padding-bottom: 8mm;
}
/* NO text-transform. The A2 agents transcribe the case the page prints, so the data already
   carries it: block 1 is "Chapter One" and block 2 is "ELECTRIC CHARGES AND FIELDS". Uppercasing
   here was redundant on the title and destroyed the opener, printing "CHAPTER ONE" where the book
   sets "Chapter One". Re-casing transcribed text in CSS is always wrong -- if the case looks
   wrong, the transcription is the thing to check. */
.banner-line {
  font-family: var(--font-display);
  font-size: var(--size-chapter-title, 2.1rem); font-weight: 300; letter-spacing: .055em;
  color: #262626;
  line-height: 1.3; margin: 0 0 28px;
}
.banner-line:last-child { margin-bottom: 0; }
.banner-line .block-n { color: var(--heading); }
/* The orange/accent rule bar the book sets between the banner and the contents panel. */
.chapter-bar { height: @BAR_H@mm; background: var(--bar);
  margin: 2mm calc(-1 * @MARGIN@mm) 2mm; }
/* NCERT's section-contents panel: tinted box, italic serif names, numbers in their own column. */
.chapter-toc {
  background: var(--panel-tint); padding: 3mm 2.5mm 8mm; margin: 0 0 6mm;
  /* max-width only. `min-width` was forcing the panel to its measured 52.9mm, but once the text
     measure narrowed to the book's real ~118mm the panel's grid cell is only ~43mm wide -- so the
     panel overflowed its cell and was drawn straight over the opening paragraph. A panel that
     fits its column is worth more than one that keeps its measured width and collides. */
  max-width: @TOC_W@mm; border-radius: 0 0 3mm 3mm;
}
.chapter-toc ul { list-style: none; margin: 0; padding: 0; }
.chapter-toc li {
  /* The number column was 3.4rem, which left so little room that "Gametogenesis" wrapped to
     three lines. The book sets the number tight against a roomy name column. */
  display: grid; grid-template-columns: 2.3rem 1fr; gap: 1mm;
  font-style: italic; font-size: var(--size-contents-panel, 1rem); margin: 0 0 13px;
  line-height: 1.38;
}
.chapter-toc li:last-child { margin-bottom: 0; }
.chapter-toc .sec-no { font-style: italic; font-variant-numeric: tabular-nums; }
/* Running prose is held near a readable measure instead of stretching the full pane --
   a 150-character line is the single biggest reason the first version was unreadable. */
/* No second width cap. The pane's padding already sets the page's measured column, so a 42rem
   cap on top of it held every block narrower than the measure -- and on a floated figure it
   compounded, leaving artwork at roughly half the book's area (measured 29% of page height against
   NCERT's 44% on p002, 12% against 28% on p007) and the SUMMARY box at half width. */
.block { margin: 0 0 4pt; }
.block-n {
  font-family: var(--mono); font-size: .7rem; color: var(--accent); vertical-align: super;
  margin-right: 5px; user-select: none;
}
.block-heading { max-width: none; }
/* NCERT prints its section headings in the subject's own colour, in small caps -- "3.1 The Male
   Reproductive System" is green in the Biology book, brick red in Chemistry. Mirrored here so a
   heading is recognisable as the same heading at a glance across the two panes. */
.block-heading h4 {
  color: var(--accent); font-size: var(--size-section-heading, 1.22rem);
  margin: 30px 0 12px; font-variant: small-caps;
  letter-spacing: .02em; padding-bottom: 4px; text-wrap: balance;
  border-bottom: 2px solid var(--accent-soft);
}
/* A chapter-level title away from the opening page ("EXERCISES", "SUMMARY"): the book sets it
   large and in caps, in type rather than inside the coloured opening banner. */
.block-heading.major h4 {
  font-size: var(--size-major-heading, 1.5rem); font-variant: normal;
  text-transform: uppercase; letter-spacing: .06em;
  border-bottom: 3px solid var(--accent); padding-bottom: 7px; margin: 38px 0 16px;
  font-family: var(--font-display);
  font-weight: 400;
}
/* NCERT sets its running prose JUSTIFIED with hyphenation -- the single most recognisable
   feature of the printed column, and what makes the two panes scan as the same text. */
.block p {
  margin: 4px 0; text-align: justify; hyphens: auto;
  /* The final line of a justified paragraph sets flush left, as the book prints it. Without
     this a short last line (a URL, a trailing clause) was stretched across the whole measure
     with word gaps several characters wide. */
  text-align-last: left;
  /* orphans/widows stay at the CSS default of 2. Raising them to 3 made a paragraph jump WHOLE
     to the next sheet rather than begin in the space left at the foot of this one, which is the
     opposite of what the book does -- NCERT splits a paragraph mid-sentence across a page turn
     (its p2 ends "...acquired by the objects" and p3 opens "neutralise or nullify"). A paragraph
     must always be free to start wherever there is room. */
  orphans: 2; widows: 2;
  /* NCERT justifies tightly and hyphenates rather than opening big word gaps. */
  word-spacing: -0.01em; text-justify: inter-word;
}
/* A `list` or `box` block's newlines are STRUCTURAL -- one per numbered question, per option,
   per line of a worked example -- so they must survive into the rendering. A `paragraph`'s are
   not: they are incidental hard-wraps from the PDF column ("...assumes\\nthat the atom..."),
   measured across the corpus, and collapsing those is correct. `pre-line` is exactly that
   split: it keeps newlines and collapses runs of spaces. Lists are also left-aligned and
   un-hyphenated, as the book prints them -- justifying a numbered list looks nothing like
   the page. Real defect this fixes: BIO12O-ch03 p015's 21-question EXERCISES list (35 real
   newlines in the stored text) rendered as one unbroken wall of prose. */
.block-list p, .block-box p {
  white-space: pre-line; text-align: left; hyphens: none;
}
/* A worked example / "Do you know?" / SUMMARY panel is printed as a tinted box in the book,
   in ITS OWN colour -- measured per chapter, not derived from the heading hue. */
.block-box {
  background: var(--box-fill); border-left: 3px solid var(--accent);
  padding: 12px 16px; border-radius: 2px;
}
/* Inside a merged example the fragments are content, not panels of their own -- otherwise one
   worked example renders as a stack of separate grey boxes with its equations falling between
   them (six panels for one Example on PHY12O-ch01 p021). */
.box-group > .block-box, .box-group > .block-equation, .box-group > .block-figure {
  background: transparent; border-left: 0; padding: 0; margin: 0 0 2mm; border-radius: 0;
}
.box-group > .block:last-child { margin-bottom: 0; }
.block-figure, .block-table, .block-box, .block-list { max-width: none; width: 100%; }
.fig-float .block-box, .fig-float .block-figure { width: 100%; }
/* Natural size, capped by the column. `width: 100%` stretched every small diagram to the
   full measure and blurred it -- the same bug that was blowing up equation crops. */
.block-figure .crop, .block-table .crop { width: auto; max-width: 100%; }
.qa-tag {
  font-family: var(--mono); font-size: .72rem; color: var(--muted); margin-top: 6px;
}
/* NCERT sets its own key vocabulary in plain black bold, not in colour -- so A2B's captured
   terms are shown exactly that way, matching the printed page beside them. The thin underline
   is the one addition: it makes which terms A2B actually caught scannable without changing
   how the term itself reads. */
strong {
  color: var(--ink); font-weight: 700;
  border-bottom: 2px solid var(--accent-soft);
}
/* Figures are capped in HEIGHT as well as width. At their true printed size the tall diagrams
   pushed seven of fifteen pages a few millimetres past the sheet, and each of those spilled onto a
   near-empty second sheet. Capping the height shrinks only the oversized ones -- most figures sit
   well inside it -- and costs a little scale rather than a paragraph, which is the trade clipping
   got backwards. */
/* A figure is capped to the TEXT COLUMN. In the book it overhangs into the outer margin, but
   that margin is on the left of a verso page and the right of a recto -- allowing the overhang
   without knowing the side pushed figures clean off the right edge of every verso sheet
   (67mm outer padding + a 166mm figure on a 210mm page). Overhang is a refinement; content
   staying on the paper is not. */
.crop {
  max-width: 100%; width: auto; height: auto; max-height: @FIG_MAX_H@mm;
  border: 1px solid var(--rule); display: block; margin: 6px auto;
  background: #fff;
}
.crop-note { font-family: var(--mono); font-size: .7rem; color: var(--muted); margin-bottom: 10px; }
/* NCERT prints a figure caption CENTRED and bold directly under the artwork, in the subject's
   colour, at a size below body text -- e.g. "Figure 3.1(a) Diagrammatic sectional view of male
   pelvis showing reproductive system". Matched here rather than left as a generic bold line. */
.caption {
  margin: 12px auto 2px; text-align: center; font-size: var(--size-figure-caption, .95rem);
  line-height: 1.45;
  /* Measured per book: biology prints its captions in black, physics in cyan. Taking the
     chapter accent here painted biology captions green, which the page does not do. */
  color: var(--caption-ink); max-width: 38rem;
  background: var(--caption-band); padding: 1.2mm 3mm;
}
.caption strong { color: inherit; border-bottom: none; font-weight: 700; }
/* The figure's labels are not printed as a list in the book (they sit on the artwork itself),
   so they are shown as what they are: a transcription record, set apart from the caption. */
.labels {
  font-family: var(--font-figure); font-size: .84rem; color: var(--muted); max-width: 100%; margin-top: 10px;
  padding: 7px 11px; background: var(--panel); border-left: 2px solid var(--accent-soft);
  line-height: 1.5;
}
.pending {
  font-family: var(--mono); font-size: .8rem; color: var(--accent); background: var(--accent-soft);
  padding: 5px 9px; border-radius: 3px; display: inline-block;
}
/* NCERT prints its "Interactive animation on ..." resource links ROTATED in the outer margin,
   beside the vertical PHYSICS label -- never as a body line. Set full width it was stretched
   edge to edge by justification and ate a line of the measure. */
.margin-link {
  position: absolute; right: 2mm; top: 22%;
  writing-mode: vertical-rl; transform: rotate(180deg);
  font: 400 .72rem/1.25 var(--font-body); color: var(--accent);
  max-height: 56%; overflow: hidden; text-align: left;
}
.margin-link a { color: inherit; text-decoration: none; word-break: break-all; }
.eqn-label { font-family: var(--mono); font-size: .68rem; color: var(--muted); }
/* Equation plus its printed number, the number held at the right margin as the book sets it. */
.eqn-row { display: flex; align-items: center; gap: 4mm; width: 100%; }
.eqn-row > .eqn { flex: 1 1 auto; min-width: 0; }
.eqn-no {
  flex: 0 0 auto; font-size: .9rem; color: var(--ink); white-space: nowrap;
  font-variant-numeric: tabular-nums;
}
.eqn { margin: 8px 0; overflow-x: auto; font-family: var(--font-math); }
/* NCERT tables print a solid coloured header band with white bold type over ruled cells
   (Table 9.1 in the Chemistry book is the reference), not a plain grey header row. */
.table-wrap { overflow-x: auto; margin: 12px 0; }
details.table-rows { margin: 10px 0; }
details.table-rows > summary {
  cursor: pointer; font-family: var(--mono); font-size: .72rem; color: var(--muted);
  padding: 5px 0; user-select: none;
}
details.table-rows > summary:hover { color: var(--accent); }
details.latex-fold { margin: 8px 0 0; }
details.latex-fold > summary {
  cursor: pointer; font-family: var(--mono); font-size: .72rem; color: var(--muted);
  padding: 4px 0; user-select: none;
}
details.latex-fold > summary:hover { color: var(--accent); }
/* An equation crop is the page itself -- centred like the book sets it, and never stretched. */
/* An equation crop is a small bitmap: stretching it to the measure (which the figure width
   rule did) blurs it badly. It keeps its natural size, capped by the column. */
/* An equation crop is a FALLBACK shown when A2S could not transcribe the maths (p022's block
   came back "unsure"), so it stands in for a line of text and must be sized like one. Capped by
   WIDTH alone it rendered at the crop's own resolution -- two lines of ~28pt type sprawling
   across the measure and colliding with the prose above. Height is what matters for a stand-in
   line: cap it to a few body lines and let the width follow the aspect ratio. */
.crop.eqn-crop {
  display: block; margin: 1.5mm auto; border: none;
  width: auto !important; max-width: 100%;
  max-height: 11mm; height: auto;
  object-fit: contain; object-position: left center;
}
/* A crop standing in for a whole prose line, not an equation, gets the same treatment. */
.block-equation .crop.eqn-crop { max-height: 11mm; }
details.eqn-src { margin: 1mm 0 2mm; }
details.eqn-src > summary {
  cursor: pointer; font-family: var(--mono); font-size: .68rem; color: var(--muted);
  padding: 2px 0; user-select: none;
}
details.eqn-src > summary:hover { color: var(--accent); }
/* A display equation cannot wrap, so a wide one MUST scroll rather than be clipped at the pane
   edge -- real defect: a long chemistry reaction scheme was cut off mid-arrow with no scrollbar. */
.block-equation { max-width: none; }
/* Prose carrying inline maths, not a display equation -- set as body text. */
/* Footnote: 0.86 of body size with a short rule above, as the book prints it (measured 9.0pt
   against a 10.5pt body in the bottom margin). */
.block-footnote { font-size: 0.86em; margin-top: 3mm; padding-top: 1.6mm; }
.block-footnote > p { margin: 0; line-height: 1.22; text-align: justify; text-align-last: left; }
.block-footnote::before {
  content: ""; display: block; width: 38mm; height: 0.35mm;
  background: var(--rule); margin: 0 0 1.6mm;
}
/* EPIGRAPH -- the quotation a chapter opens with. NCERT sets it in bold italic beside a large
   decorative quotation mark, before any section begins (CHE11L-ch02 p001: "The rich diversity of
   chemical behaviour..."). Rendered as ordinary body prose it read as a stray first paragraph. */
.block-epigraph > p {
  font: italic 700 1.05em/1.45 var(--font-display);
  margin: 2mm 0 4mm; padding-left: 11mm; position: relative; text-align: left;
}
.block-epigraph > p::before {
  content: "“"; position: absolute; left: 0; top: -2mm;
  font: 700 3.2em/1 var(--font-display); color: var(--accent-soft);
}
.eqn-prose { display: block; }
.eqn-inline { margin: 4px 0; text-align: justify; text-align-last: left; }
.eqn { overflow-x: auto; max-width: 100%; padding-bottom: 4px; }
.eqn .katex-display { margin: 0.3em 0; }
/* Inside a worked example the book sets displayed maths INDENTED LEFT and tight against the prose
   -- Example 1.4 runs "F_e = -1/4pe0 e^2/r^2" directly under its sentence with no blank line.
   Centring each one with a 0.3em display margin plus the block's own margin opened a gap the
   height of two text lines around every equation, which is most of why that page ran long. */
/* Tight, because a worked example interleaves prose and display maths many times over: book
   page 30 is 15 blocks -- seven display equations between seven prose segments -- and at 0.1em
   plus 0.6mm each, the accumulated vertical margin pushed its closing 163-character sentence
   onto a sheet of its own. The book sets these lines close together; 0.04em keeps them legible
   while reclaiming roughly a line per equation on a page like that. */
.box-group .eqn .katex-display { margin: 0.04em 0; text-align: left; padding-left: 6mm; }
.box-group > .block-equation { margin: 0 0 0.2mm; }
/* Prose segments inside a merged example need no gap either -- the book runs them on. */
.box-group > .block-box { margin: 0 0 0.4mm; }
.box-group > .block-box p { margin: 0.4mm 0; }
.box-group .eqn { padding-bottom: 0; }
.await {
  font-family: var(--mono); font-size: .7rem; color: var(--muted);
  border-left: 2px solid var(--accent-soft); padding: 4px 9px; margin-top: 4px;
}
table.data-table {
  border-collapse: collapse; font-size: .9rem; border: 1px solid var(--accent);
}
table.data-table th, table.data-table td {
  border: 1px solid var(--rule); padding: 6px 11px; text-align: left; vertical-align: top;
}
table.data-table th {
  background: var(--accent); color: #fff; font-weight: 700; text-align: center;
  letter-spacing: .02em; border-color: var(--accent);
}
table.data-table tbody tr:nth-child(even) { background: var(--accent-wash); }
.toc {
  padding: 12px 32px; background: var(--panel); font-family: var(--mono); font-size: .84rem;
  border-bottom: 1px solid var(--rule); position: sticky; top: 88px; z-index: 15;
}
.toc a { color: var(--accent); margin-right: 9px; text-decoration: none; }
.toc a:hover { text-decoration: underline; }
/* A page with anything still untranscribed is flagged in the index, so gaps are findable
   without scrolling the whole chapter looking for them. */
.toc a.cls-gap {
  color: #b23a2e; border-bottom: 2px solid #e8a79d; font-weight: 700;
}
.gaps {
  margin: 26px 0 8px; padding: 11px 15px; border-radius: 3px; max-width: 42rem;
  background: #fdf3f1; border-left: 3px solid #b23a2e;
  font-family: var(--mono); font-size: .76rem; line-height: 1.6; color: #6e3029;
}
.gaps-head { font-weight: 700; margin-bottom: 5px; letter-spacing: .02em; }
.gaps ul { margin: 0; padding-left: 18px; }
.gaps li { margin: 2px 0; }
.gaps.complete {
  background: var(--accent-wash); border-left-color: var(--accent); color: var(--accent);
  font-size: .74rem;
}
/* Everything this BOOK sets differently from the others. Emitted from the subject profile, so a
   physics rule cannot reach biology's approved sheet -- see _subject_css and _SUBJECT_PROFILES. */
@SUBJECT_CSS@
"""


def _subject_css(profile, geo, band_fill="", tab_fill=""):
    """The stylesheet rules that belong to THIS book only, built from its profile row.

    Lives here rather than in _CSS_TMPL because every rule below was measured on one book and is
    wrong on the others: physics indents its paragraphs and sets no space between them, and prints
    coloured tabs and title bars on its boxes; biology's approved sheet does neither. A profile
    whose fields are all at their defaults returns "" and the stylesheet is unchanged.
    """
    out = []
    indent = profile.get("para_indent_mm") or 0.0
    gap = profile.get("para_gap_pt")
    # Space between BLOCKS, which is separate from and larger than the space between paragraphs.
    # The stylesheet's 2mm is right for biology's airy single column, but CHE11L-ch02's problem
    # panels stack up to 14 blocks on one page -- 28mm of inter-block margin on a book that runs
    # its panel content on, which is what pushed a single 58-character equation line onto a sheet
    # of its own (sheet 16 of 49). Note the book is NOT short of margin: it reserves 22.5mm below
    # its text where we reserve 13mm, so the excess height is ours, not the page's.
    block_gap = profile.get("block_gap_mm")
    if block_gap is not None:
        out.append(f"#viewer .block {{ margin-bottom: {block_gap:.2f}mm; }}")
    # Vertical padding inside a tinted panel. The stylesheet's 12px top and bottom is fine for a
    # book with one or two panels a page, but CHE11L-ch02 stacks several solved-problem panels per
    # page and the padding accumulates -- enough that three pages ran one or two lines long and
    # pushed a single equation line onto a sheet of its own (sheets 16, 24 and 27 held 58, 128 and
    # 224 characters). Trimming the vertical padding alone keeps the panel's horizontal inset,
    # which is what reads as a panel, while reclaiming the height.
    # MEASURED AND REJECTED for CHE11L-ch02: trimming panel padding to 1.2mm took the chapter
    # from 51 sheets to 52 and its spill count from 1 to 3. Removing height from inside a panel
    # just moves the break, it does not reliably save a page. The knob stays because it may suit
    # another book; it is simply not the lever for this one.
    # Opener face. Measured off Chapter_2.pdf page 1: "STRUCTURE OF ATOM" is BookmanOldStyle-Bold
    # 19.0pt #2e3092, "Objectives" the same face at 15.5pt, and the epigraph
    # BookmanOldStyle-BoldItal 9.0pt -- i.e. this book sets its opener in the BODY face, bold, not
    # in a display sans. Ours used Century Gothic throughout, which is a different typographic
    # statement from the one the page makes.
    if profile.get("opener_in_body_face"):
        out.append(".chapter-banner .banner-line { font-family: var(--font-body);"
                   " font-weight: 700; }")
        out.append(".block-epigraph > p { font-family: var(--font-body); }")
        out.append(".block-epigraph > p::before { font-family: var(--font-body); }")

    box_pad = profile.get("box_pad_mm")
    if box_pad is not None:
        out.append(f"#viewer .block-box {{ padding-top: {box_pad:.2f}mm;"
                   f" padding-bottom: {box_pad:.2f}mm; }}")
    if indent > 0:
        # Measured: every body paragraph starts 18pt in (x0 78.0 against a column at 60.0 on
        # p003, p011 and p021) EXCEPT one carried over from the previous page, which starts
        # flush. `.block-paragraph + .block-paragraph` is deliberate -- a paragraph that follows
        # an equation or a figure is a continuation and the book sets it flush too.
        out.append(f".block-paragraph.indent > p {{ text-indent: {indent:.2f}mm; }}")
        # A display equation beside a floated panel. `.eqn-row` is a FLEX container, which
        # establishes its own formatting context and therefore refuses to sit beside a float --
        # Chrome pushed every one of them below the Coulomb panel, leaving a 60pt hole in the
        # column. The book sets these flush left at the paragraph indent anyway ("F = 9 x 10^9 N"
        # at x 78.0 on p011), not centred, so a plain block with the equation number floated out
        # to the margin is both the book's setting and the one that paginates.
        out.append(".eqn-row { display: block; }")
        # ABSOLUTE, not floated. `.eqn-row` is set to `display: block` here so an equation can
        # sit beside a floated panel, but a float only aligns with content that FOLLOWS it in
        # source order -- and `.eqn-no` is emitted after `.eqn`. So every number dropped a line or
        # two below its own equation, which a page-by-page audit of PHY12O-ch01 found on almost
        # every page ((1.1) on p010, (1.13b) and (1.14)-(1.21) on pp027-028). Positioning it
        # against the row removes the dependence on source order entirely.
        out.append(".eqn-row { position: relative; padding-right: 16mm; }")
        out.append(".eqn-row > .eqn-no { position: absolute; right: 0; top: 50%;"
                   " transform: translateY(-50%); margin: 0; }")
        out.append(f".eqn .katex-display {{ text-align: left; padding-left: {indent:.2f}mm; "
                   f"margin: 0.15em 0; }}")
        out.append(".eqn .katex-display > .katex { text-align: left; }")
    if gap is not None:
        # The book puts NOTHING between paragraphs -- p011's three run 0.135-0.389, 0.393-0.468,
        # 0.473-0.666, i.e. consecutive lines. The indent is what separates them. Our 4pt block
        # margin plus 4px either side of every <p> cost about 10pt a paragraph, roughly four
        # lines a page, which is most of why 50 book pages printed on 66 sheets.
        out.append(f".block {{ margin: 0 0 {gap:.1f}pt; }}")
        out.append(f".block p {{ margin: {gap:.1f}pt 0; }}")
        out.append(".block-paragraph + .block-paragraph { margin-top: 0; }")
    if profile.get("band_fill_measured") and band_fill:
        # The band's own measured fill. A2L reads #c6eafb (pale blue) in the physics header band
        # on 49 of 50 pages; the render was painting #00adef, the ACCENT, because --banner-strip
        # is chosen by SATURATION between the header band and the opener's rule bar and the rule
        # bar wins that contest every time. #00adef is right for the rule UNDER the band, for
        # captions and for the box tabs -- not for the band itself. The book also paints the band
        # edge to edge rather than as a 73% bar with a corner block (measured bbox 0.0-1.0), and
        # hangs the grey running-header tab off its OUTER end (x 0.550-0.873 on recto p011,
        # mirrored to 0.127-0.451 on verso p042).
        out.append(f".page-band {{ background: {band_fill}; }}")
        out.append(".page-band .band-bar, .page-band .band-corner { display: none; }")
        out.append(".band-tab { left: auto; right: 12.7%; }")
        out.append(".band-verso .band-tab { right: auto; left: 12.7%; }")
        # The folio. Measured by masking #c6eafb in the lower fifth of the source page: it sits
        # at y 0.9152-0.9363 on EVERY page checked (p2, p5, p11, p21, p42, p45), 0.058 of the
        # sheet wide and 0.021 tall, inset 0.1275 from the trim on a verso and 0.1283 on a recto
        # -- i.e. at the FOOT of the page, in from the edge, and alternating to the outer corner.
        # It was being drawn at 74.5% of the page height and bled hard against the trim.
        out.append(".folio-tab { top: auto; bottom: 6.37%; padding: 0; min-width: 12.5mm; "
                   "height: 5.8mm; display: flex; align-items: center; "
                   "justify-content: center; font-size: .92rem; }")
        # The book insets the folio 0.128 of the sheet from the trim, but it can afford to: its
        # text block stops at 0.686 on a recto. Ours runs to the pane padding, so honouring 12.8%
        # would stamp the number on top of the text. Inset to the pane's own margin instead --
        # a real printed margin, in the right corner, at the right height.
        out.append(".folio-right { right: 3mm; }")
        out.append(".folio-left  { left: 3mm; }")
        # Headings. Measured on p005: "1.3 CONDUCTORS AND INSULATORS" is grey #6d6e71 serif
        # BOLD small caps at size_rel 1.45 with NO rule under it and about one blank line above.
        # The stylesheet's accent underline is an addition that reads as an invention on this
        # book, and the 30px/38px margins around it cost most of a line each time.
        out.append(".block-heading h4 { border-bottom: 0; padding-bottom: 0; "
                   "margin: 4.0mm 0 1.2mm; }")
        out.append(".block-heading.major h4 { border-bottom: 0; padding-bottom: 0; "
                   "margin: 4.5mm 0 2.0mm; font-family: var(--font-body); font-weight: 700; "
                   "letter-spacing: .02em; }")
        # A figure caption prints on BARE PAPER here: 29 of the 35 measured `figure_caption`
        # elements carry no fill at all, and the six that do are captions sitting inside a grey
        # example box, where the tint is the box's, not the caption's. --caption-band took the
        # minority value and painted a grey strip behind every caption in the chapter.
        out.append(".caption { background: transparent; padding: 0.6mm 0; margin-top: 2mm; }")
        # A section heading does NOT clear a floated figure in this book. Measured on p015:
        # "1.7 FORCES BETWEEN MULTIPLE CHARGES" sits at x 0.102-0.545, y 0.430-0.444 with
        # FIGURE 1.8 printed beside it at x 0.546-0.872, y 0.400-0.875. `clear: both` pushed the
        # heading and everything after it BELOW the figure, leaving a third of that sheet blank
        # and spilling the last two equations onto a sheet of their own.
        out.append(".block-heading, .block-list { clear: none; }")
        if tab_fill:
            out.append(f".band-tab {{ background: {tab_fill}; }}")
    if profile.get("box_tabs"):
        # The box, its tab and the gap between them, in the proportions measured off the source
        # page (p021: grey panel 0.113-0.686, 6pt white gap, 25.5pt #00adef tab 0.696-0.738 with
        # "EXAMPLE 1.8" in white caps set vertically and bottom-aligned; p011's Coulomb panel is
        # the same device at 19.5pt). The tab is painted as part of the BOX's own background --
        # a horizontal gradient is invariant down the page, so every fragment of a box that
        # splits across sheets paints its strip correctly, which an absolutely-positioned
        # element cannot do.
        out.append("""
.boxed { position: relative; margin: 0 0 1.4mm; }
.boxed > .block-box { margin-bottom: 0; }
/* The tab's LETTERING. Only the text is positioned; the coloured strip itself is painted by the
   box's background gradient, so a box that breaks across sheets keeps its strip on both halves. */
.boxed-tab {
  position: absolute; bottom: 0; width: var(--tab-w); text-align: center;
  color: var(--tab-ink, #fff); font-family: var(--font-display);
  writing-mode: vertical-rl; text-orientation: mixed;
  font-variant: small-caps; letter-spacing: .06em; white-space: nowrap;
  overflow: hidden; max-height: 100%;
  padding-bottom: 2.2mm; line-height: var(--tab-w);
}
.boxed-right > .boxed-tab { right: 0; }
.boxed-left  > .boxed-tab { left: 0; }
/* A feature box's title bar sits ON the panel's top edge, inset from the left -- measured
   x 0.255-0.712 against a panel at 0.098-0.872, both starting at y 0.287, 24pt tall. */
.box-title-bar {
  display: inline-block; margin: 0 0 2.2mm 11%;
  padding: 1.0mm 5mm; color: #fff; background: var(--bar-fill, var(--accent));
  font-family: var(--font-display); font-variant: small-caps;
  font-size: .98rem; letter-spacing: .05em; line-height: 1.25;
}
/* The scientist panel. Measured on p011: pale #9cdcf8 body 155.5pt wide, a 4.5pt gap, then a
   19.5pt #00adef bar down the right edge in white caps -- 179.5pt (63.3mm) of the 612pt sheet
   all told, hard against the outer margin. Its portrait is 93pt wide (60% of the panel),
   centred, 20.6pt below the panel top. */
.sci-panel { margin-left: auto; }
.sci-panel > .boxed-tab {
  font-size: 1.12rem; letter-spacing: .03em; padding-bottom: 7mm;
}
.sci-panel .block-figure { margin: 1.2mm auto 2.4mm; text-align: center; }
.sci-panel .block-figure .crop {
  width: 60%; max-width: 60%; border: 0; margin: 0 auto; background: transparent;
}
.sci-panel .block-box > p:first-of-type { text-indent: 0; }
/* SUMMARY / POINTS TO PONDER: the whole page body printed on a tint, with the grey margin band
   the SUMMARY pages set beside it (#d1d2d4 with a 12.5pt #00adef rule inside it). */
.page-panel { padding: 5mm 6mm 6mm; }
.page-panel > .block-heading.major h4 {
  border-bottom: 0; text-align: center; font-family: var(--font-body);
  font-weight: 700; font-size: 1.12rem; letter-spacing: .04em; margin: 1mm 0 4mm;
  color: var(--ink); text-transform: uppercase;
}
@media print { #viewer .boxed { break-inside: auto; } }
""".strip())
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", help="e.g. PHY12O-ch01")
    ap.add_argument("--pdf", required=True, help="path to the source PDF for this chapter")
    ap.add_argument("--title", default=None, help="chapter title for the header, if known")
    ap.add_argument("--no-scans", action="store_true",
                    help="render ONLY this pipeline's extracted data -- no original page images. "
                         "The source PDFs are watermarked scans ('(c) NCERT / not to be "
                         "republished' baked into the page bitmap, not a layer that can be "
                         "switched off), so a page scan always carries that mark. The extracted "
                         "data does not: text, headings, bold terms, table rows and equation "
                         "LaTeX are this pipeline's own output and render clean. This mode is "
                         "also much faster, because the full-page renders are the slow part.")
    args = ap.parse_args()

    if not os.path.exists(args.pdf):
        print(f"source PDF not found: {args.pdf}", file=sys.stderr)
        return 1

    pages = _best_page_outputs(args.chapter)
    if not pages:
        print(f"no A2 output found for chapter {args.chapter}", file=sys.stderr)
        return 1

    review_dir = rc.pp("exports", "review")
    html_dir = os.path.join(review_dir, "html")
    os.makedirs(html_dir, exist_ok=True)

    # Images live alongside the Markdown export's own copies (one shared set per chapter, not
    # duplicated per format) -- the HTML page just references them one directory up.
    fig_dir_name = f"{args.chapter}_figures"
    fig_dir = os.path.join(review_dir, fig_dir_name)
    page_dir_name = f"{args.chapter}_html_pages"
    page_dir = os.path.join(review_dir, page_dir_name)
    os.makedirs(fig_dir, exist_ok=True)
    os.makedirs(page_dir, exist_ok=True)
    fig_rel_prefix = f"../{fig_dir_name}"
    page_rel_prefix = f"../{page_dir_name}"

    title = args.title or args.chapter
    pdf_rel = os.path.relpath(args.pdf, rc.pp()) if args.pdf.startswith(rc.pp()) else os.path.basename(args.pdf)

    first_page_num = min(pages)
    # Loaded BEFORE the page loop: the loop needs each page's measured column structure.
    measured = _load_measured_layout(args.chapter)
    # Geometry is needed INSIDE the loop (figure widths in mm, caption cuts), so it is
    # computed here rather than beside the palette further down.
    # The banner's top strip has no role of its own -- physics' agent filed it as `rule_bar`,
    # biology's folded it into `chapter_banner` -- so deriving it from neighbouring roles got
    # biology wrong (it picked the orange divider, not the green strip). Sample the pixel instead.
    banner_strip_sampled = ""
    try:
        from PIL import Image as _Im
        _p1 = os.path.join(page_dir, "p%03d.png" % first_page_num)
        if not os.path.exists(_p1):
            lib_pdf.render_page_to_png(args.pdf, first_page_num, dpi=_PAGE_DPI, out_path=_p1)
        _im = _Im.open(_p1).convert("RGB")
        _w, _h = _im.size
        _px = [_im.getpixel((int(_w * fx), int(_h * 0.03))) for fx in (0.2, 0.35, 0.5)]
        _best = max(_px, key=lambda c: (max(c) - min(c)))
        if max(_best) - min(_best) > 25:
            banner_strip_sampled = "#%02x%02x%02x" % _best
    except Exception:
        banner_strip_sampled = ""
    profile = subject_profile(args.chapter)
    geo = _print_geometry(measured, profile)
    opener = _opener_mm(measured, geo)
    pad_l, pad_r, pad_t, pad_b = _content_inset_mm(measured, geo, profile)
    measure_frac, inner_frac, recto_pages = _text_measure(measured)
    measure_mm = measure_frac * geo["page_w_mm"]
    inner_mm = inner_frac * geo["page_w_mm"]
    outer_mm = max(6.0, geo["page_w_mm"] - measure_mm - inner_mm)
    page_margin_mm = max(pad_l, pad_r)   # the bleed amount for full-width bands
    mm_per_px = (1.0 / geo["px_per_mm"]) if geo.get("px_per_mm") else 0.0
    # The corner mark (the figure-and-leaf graphic on the band's dark block) is real artwork, so
    # it must be an image -- but ONE image, cropped once and reused on every page, rather than a
    # strip cropped per page. Its measured box is identical on every body page, mirroring per
    # spread, so a single crop plus a CSS flip covers both sides.
    corner_img = ""
    _c_el = _c_rec = None
    for _rec in (measured or {}).get("full_detail_by_page", {}).values():
        for _e in _rec.get("elements_in_reading_order") or []:
            if _e.get("role") == "decorative_image" and _e.get("bbox") and _e["bbox"][1] < 0.12:
                _c_el, _c_rec = _e, _rec
                break
        if _c_el:
            break
    if _c_el and _c_rec.get("page_width_px"):
        _pw, _ph = _c_rec["page_width_px"], _c_rec["page_height_px"]
        _bb = _c_el["bbox"]
        try:
            lib_pdf.crop_box(args.pdf, 2,
                             [_bb[0] * _pw, _bb[1] * _ph, _bb[2] * _pw, _bb[3] * _ph],
                             os.path.join(fig_dir, "_corner.png"), unit="px")
            corner_img = f'<img class="band-logo" src="{fig_rel_prefix}/_corner.png" alt="">'
        except Exception:
            corner_img = ""
    body_parts = []
    # The book carries one worked example's side tab onto the next page -- p013, p014,
    # p017 and p022 all open inside an example started earlier -- so the label it last
    # printed travels with the page loop.
    box_state = {"example": ""}
    toc = []
    n_blocks = n_fig_cropped = n_eq_shown = n_eq_pending = 0

    for page_seq, (page_num, (run_label, rec)) in enumerate(pages.items(), start=1):
        if args.no_scans:
            page_rel = None
        else:
            page_png = os.path.join(page_dir, f"p{page_num:03d}.png")
            lib_pdf.render_page_to_png(args.pdf, page_num, dpi=_PAGE_DPI, out_path=page_png)
            page_rel = f"{page_rel_prefix}/p{page_num:03d}.png"

        blocks = rec.get("blocks") or []
        n2_item = f"{args.chapter}-p{page_num:03d}"
        n2b = _load_sibling_json("A2B", n2_item)
        n2n = _load_sibling_json("A2N", n2_item)
        bold_by_n = {b["n"]: b.get("bold_terms") or [] for b in (n2b or {}).get("blocks", [])}
        corr_by_n = {b["n"]: b for b in (n2n or {}).get("blocks", []) if b.get("corrected_text")}

        # This page's own padding, computed BEFORE the furniture strips because their bleed
        # margins are derived from it. The text column mirrors per spread, so the padding differs
        # page to page and the stylesheet's fixed tokens cannot express it.
        # Parity, anchored to the measured set. Physics' measured recto set starts at page 3, so
        # a bare membership test classified page 1 as a verso -- it is a recto, and the opener's
        # mirroring was inverted for the whole chapter as a result.
        if recto_pages:
            _anchor = min(recto_pages)
            is_recto = (page_num - _anchor) % 2 == 0
        else:
            is_recto = page_num % 2 == 1
        pl_frac, pr_frac = _page_measure(
            measured, page_num,
            (inner_frac, 1.0 - inner_frac - measure_frac) if is_recto
            else (1.0 - inner_frac - measure_frac, inner_frac))
        pl_mm = max(6.0, pl_frac * geo["page_w_mm"])
        pr_mm = max(6.0, pr_frac * geo["page_w_mm"])

        right_html = []  # page-level furniture notes, emitted before the body
        # The book prints a coloured band across the top of each body page, carrying the running
        # header and its logo. It was simply absent from the render; like the chapter banner it is
        # artwork, so it is cropped from the page rather than approximated with a CSS block.
        # NO cropped furniture. The reference build draws the banner in CSS and crops only the
        # FIGURES (15 <img> tags in total); every strip, banner and folio image added here showed
        # up as a partial green band that never reached the sheet edge, because a crop of a page
        # region can only ever be as wide as the region measured. CSS can paint a full-bleed band;
        # a crop cannot. This is what the owner asked for and I added crops anyway.
        year_imprint = next((t for t in (rec.get("running_header_footer_removed") or [])
                             if re.fullmatch(r"\s*\d{4}\s*-\s*\d{2,4}\s*", t)), "")
        # The page band, drawn in CSS. Measured on the real pages: a green bar #4a7435 running
        # y 0.068-0.108 (about 12mm tall) and spanning ~73% of the width, with a brown corner
        # block filling the rest on the OUTER side -- mirrored per spread. Cropping it from the
        # scan could never reach the sheet edge (a crop is only as wide as the region measured),
        # which is why the band kept appearing short and adrift. CSS paints it full-bleed.
        # The running header is the chapter or subject name. Excluded: the folio, the print-year
        # imprint, and the QR print code (e.g. "12083CH03") -- that last one is the publisher's
        # plate number and was being set as the page's header.
        _hdr = next((t for t in (rec.get("running_header_footer_removed") or [])
                     if t.strip() and not t.strip().isdigit()
                     and not re.fullmatch(r"\s*\d{4}\s*-\s*\d{2,4}\s*", t)
                     and not re.fullmatch(r"\s*\d+[A-Z]+\d*\s*", t.strip())
                     # a section-contents line ("3.1 The Male Reproductive System") is panel text,
                     # not a running header -- it was being set as page 1's header
                     and not re.match(r"^\s*\d+\.\d+\s", t)), "")
        # NOT on the chapter-opening page: that page carries the chapter banner, which has its
        # own dark strip across the top, so a page band above it showed two stacked bars.
        # Bleed computed from THIS page's padding. It was hardcoded to 25mm, which matched the
        # flat 25mm padding; once the measured 12-18mm margins returned, the band started ~7mm
        # above the sheet and spilled past both side edges onto the viewer background.
        # These must MATCH the padding emitted below, not mirror it. They were swapped, so each
        # band poked 6mm past one edge and left a 6mm white gap at the other -- recto padded
        # 12/18 but bled -18/-12.
        _wide = max(pad_l, pad_r) + 6.0
        _narrow = min(pad_l, pad_r)
        _ol = _narrow if is_recto else _wide     # left padding on a recto is the narrow one
        _or = _wide if is_recto else _narrow
        # The band is exactly the SHEET wide, so the measured percentages inside it (the 73.2%
        # green bar, the 13.6% corner artwork, the gap between them) are fractions of the printed
        # page -- which is what they were measured against. `calc(100% + bleed)` made the band
        # 86% of the sheet, because the content box plus this bleed falls short of the trim, and
        # every proportion inside it came out scaled by that same 0.86.
        _band_style = (f' style="'
                       # Bottom margin reserves the corner artwork's measured hang. A flat 4mm
                       # here silently beat the stylesheet's own margin-bottom (an inline style
                       # outranks it), so the artwork kept covering the first lines of prose
                       # however the rule was edited.
                       # -_ol, NOT -pad_l. The pane pads its left with _ol (the narrow inner
                       # margin on a recto, the wide outer one on a verso); offsetting the band by
                       # pad_l instead disagreed with that by 6mm on every recto, which pushed the
                       # whole band off the sheet and, with row-reverse anchoring to the band's
                       # right edge, dragged the artwork outside the page entirely.
                       f'"')
        # Some books print NO running header band at all. CHE11L-ch02 is one: all 43 of its
        # measured pages report none, and the consolidated palette has no page_header_band_fill.
        # Emitting one anyway invented a dark strip (the fallback colour resolved to #8b3325),
        # printed the running header on it in cyan at almost no contrast, hid body text behind it
        # on two sheets, and cost vertical space on every page. A book without a band gets no band.
        header_band = "" if (page_num == first_page_num
                             or not profile["has_header_band"]) else (
            # Band geometry in MILLIMETRES of the sheet, measured off the source PDF's body
            # pages. Percentages were wrong here: a flex child resolves them against the pane's
            # 180mm content box, not the band's 210mm sheet width, so every proportion came out
            # at 0.86 of its measured value (73.2% x 180 = 131.9mm instead of 153.7mm).
            #   verso  green x 0.024-0.756 | gap | brown x 0.837-0.973
            #   recto  brown x 0.024-0.161 | gap | green x 0.241-0.973
            f'<div class="page-band band-{"recto" if is_recto else "verso"}"{_band_style}>'
            f'<span class="band-bar" style="flex: 0 0 {0.732 * geo["page_w_mm"]:.1f}mm; '
            f'margin-{"left" if is_recto else "right"}: {0.024 * geo["page_w_mm"]:.1f}mm;">'
            f'</span>'
            f'<span class="band-corner" style="flex: 0 0 {0.136 * geo["page_w_mm"]:.1f}mm; '
            f'margin-{"left" if is_recto else "right"}: {0.081 * geo["page_w_mm"]:.1f}mm;">'
            f'{corner_img}</span>'
            # The grey tab carrying the square mark is a PHYSICS device. A2L measures it on that
            # book and NOT on biology, whose 29 measured `running_header` elements carry no fill
            # at all -- the chapter name is set as small plain caps beside the green band, with the
            # brown corner artwork as the only other furniture. Printing physics' tab on biology
            # put a grey panel and a two-square mark on every page that the book never prints.
            + (f'<span class="band-tab"><i class="band-mark"></i>'
               # NOT .title(): the book prints "Electric Charges and Fields", and .title()
               # turned the conjunction into "And". The running header is printed text --
               # reproduce the case the page sets, never re-case it.
               f'{_esc(_hdr.strip())}</span>'
               if profile["band_tab"] else
               f'<span class="band-running">{_esc(_hdr.strip().upper())}</span>')
            + f'</div>'
            f'<div class="band-caption">{_esc(_hdr.strip())}'
            f'<span class="band-year">{_esc(year_imprint.strip())}</span></div>'
        )
        # The strips must bleed to the SHEET edges, but the page's padding is set per page (the
        # measured column mirrors), so the stylesheet's fixed @PAD_L@/@PAD_R@ negative margins no
        # longer matched it and the bands stopped short of the edge. Give each strip this page's
        # own bleed inline.
        # Full bleed to all four corners: the strip is as wide as the sheet and pulled out over
        # the 25mm padding on every side it touches.
        bleed_t = ' style="width: calc(100% + 50mm); margin: -25mm -25mm 4mm -25mm;"' 
        bleed_b = ' style="width: calc(100% + 50mm); margin: 3mm -25mm -25mm -25mm;"' 
        if header_band:
            header_band = header_band.replace('<img class="page-strip strip-top"',
                                              f'<img class="page-strip strip-top"{bleed_t}', 1)
        # NCERT's figures are WIDER than the text measure -- they reach into the outer margin,
        # which is why its figure pages carry ~38% artwork against our 27%. The overhang has to be
        # on the outer side, and that side swaps per spread, so it is emitted inline per page
        # rather than from a stylesheet token (an earlier CSS attempt always grew rightward and
        # pushed figures off verso sheets).
        outer_px = max(0.0, (pr_mm if is_recto else pl_mm) - 10.0)
        fig_style = (f'width: calc(100% + {outer_px:.1f}mm); max-width: none; '
                     + (f'margin-right: -{outer_px:.1f}mm;' if is_recto
                        else f'margin-left: -{outer_px:.1f}mm;')) if outer_px > 4 else ""
        if header_band:
            right_html.append(header_band)
        foot_strip = ""
        if foot_strip:
            foot_strip = foot_strip.replace('<img class="page-strip strip-bottom"',
                                            f'<img class="page-strip strip-bottom"{bleed_b}', 1)
        abs_furniture, folio_lanes = "", []   # the CSS .folio-tab below replaces the crop
        # The printed folio number, drawn as a CSS tab rather than a crop: a crop has to be
        # absolutely positioned (which cannot paginate, so it vanished from the PDF) and kept
        # colliding with prose. The number itself comes from the page's own removed furniture --
        # NCERT prints the book's running folio, not our sequence index.
        # Sequential 1, 2, 3 ... as the owner asked. The book's own folio (43, 44 ...) was used
        # here before, which is more faithful to the source but confusing in a standalone reader
        # where it does not match the page you are on.
        # Only where the book actually prints a folio. A2L measures no `page_number` on the
        # chapter-opening page, and the book prints none there -- we were stamping a "1" on it.
        # Every page except the opener. Keying this off a measured `page_number` element dropped
        # the folio from any page where A2L simply had not recorded one -- p24 lost its "24".
        folio_num = "" if page_num == first_page_num else str(page_seq)
        folio_side = "right" if (page_num in recto_pages if recto_pages
                                 else page_num % 2 == 0) else "left"
        folio_tab = (f'<div class="folio-tab folio-{folio_side}">{_esc(folio_num)}</div>'
                     if folio_num else "")
        # Reserve the folio's column on its own side, so body content never flows beneath it.
        # The text column is MIRRORED: the narrow inner margin is on the left of a recto page and
        # on the right of a verso, with the wide outer margin opposite. The folio tab and figure
        # overhang live in that outer margin, which is why it is left empty of text.
        side_cls = "recto" if is_recto else "verso"
        # Symmetric 25mm, as in the reference build. The mirrored per-page measure was measured
        # from the book and is strictly more faithful on paper, but in practice it made every page
        # look worse: narrow columns, wide dead margins, figures with nowhere to go, and strips
        # whose bleed no longer matched the padding. A simple even margin reads far closer to the
        # book than a technically-correct mirror that nothing else in the layout cooperates with.
        # Measured margins, with the wider one on the OUTER edge as the book sets it. The flat
        # 25mm was a deliberate simplification while the mirrored measure was misbehaving; it
        # overrode the measured 12/12/18/16mm and made every margin equal.
        # The band is positioned against the sheet, so the pane must RESERVE its full height --
        # the 12mm strip plus the corner artwork's measured hang below it. Without this the first
        # lines of prose started under the band instead of below it.
        _band_h = 0.0 if page_num == first_page_num else (12.0 + profile["corner_hang_mm"])
        _pane_top = max(pad_t, _band_h + 2.0)
        lane_style = (
            f' class="pane extracted {side_cls}" style="padding: {_pane_top:.1f}mm '
            f'{_or:.1f}mm {pad_b:.1f}mm {_ol:.1f}mm;"')
        rh = rec.get("running_header_footer_removed") or []
        # NCERT's chapter-opening page prints a section-contents panel in a tinted box beside the
        # title. A2 correctly strips it as furniture, which means it is real text we HAVE and were
        # simply not showing. Rendering it as the panel the book prints makes the opening page
        # recognisable instead of starting with a bare metadata line.
        toc_entries = [s for s in rh if re.match(r"^\d+\.\d+\s+\S", s.strip())]
        other_furniture = [s for s in rh if s not in toc_entries]
        if toc_entries:
            items = "".join(
                f'<li><span class="sec-no">{_esc(m.group(1))}</span>'
                f'<span class="sec-name">{_esc(m.group(2))}</span></li>'
                for m in (re.match(r"^(\d+\.\d+)\s+(.*)$", s.strip()) for s in toc_entries) if m
            )
            # Deferred: the banner is emitted from inside the block loop (the title blocks come
            # after this furniture line in reading order), so the bar + panel are queued to be
            # placed straight after it rather than before the title they sit under in the book.
            # The bar SPANS the page; the contents panel sits in the LEFT column with the
            # opening prose beside it. Emitting both as one full-width lump left the measured
            # left column empty and the prose stranded alone on the right -- the exact defect
            # this page was supposed to demonstrate.
            deferred_bar = '<div class="chapter-bar"></div>'
            deferred_toc = f'<div class="chapter-toc"><ul>{items}</ul></div>'
        else:
            deferred_bar = deferred_toc = ""
        if other_furniture and not args.no_scans:
            # Review mode only. In the reader this note repeated the running header and the year
            # that the band already prints, which read as the header appearing twice.
            right_html.append(
                f'<div class="furniture-note">removed furniture: '
                f'{_esc(", ".join(other_furniture))}</div>'
            )
        # The print-year imprint ("2022-23") really is printed at the foot of every page. A2
        # strips it as furniture, correctly -- it is not chapter content -- but a reader that
        # drops it is missing something the page visibly has, so it is put back where it belongs.


        # Only the chapter's FIRST page carries the coloured opening banner.
        is_opener = (page_num == first_page_num)
        page_gaps = []  # what this page's extraction is still missing, named concretely
        banner_lines = []  # consecutive chapter-title lines, grouped into one coloured panel
        banner_col = None  # the column those title lines were MEASURED in
        # The real banner, cropped from the page -- it carries the QR code and the
        # chapter illustration that no synthetic panel can reproduce.
        # No separate banner crop: the top furniture strip above already covers it (it extends
        # past top-anchored bands), and cropping both drew the band twice.
        banner_img = ""
        # The column each block was MEASURED to sit in (step A2L), so the render reproduces the
        # page's arrangement rather than stacking everything in one column.
        col_by_n, col_bounds = _column_map_for_page(
            measured, page_num, derive=profile["derive_columns"])
        # The coloured furniture the book prints on this page's boxes, and the page-wide tint it
        # prints SUMMARY and POINTS TO PONDER on. Both are measurements A2L already records and
        # the render was discarding; both are per-subject, because only physics prints them.
        box_furn = _box_furniture_for_page(measured, page_num) if profile["box_tabs"] else None
        page_panel = _page_panel_for_page(measured, page_num) if profile["page_panels"] else None
        role_by_n = _role_map_for_page(measured, page_num)
        style_by_n = _style_map_for_page(measured, page_num)
        first_block_n = next((b.get("n") for b in blocks if isinstance(b.get("n"), int)),
                             None)
        placed = []  # [(column, html)] in reading order
        for b in blocks:
            n_blocks += 1
            kind, n = b.get("kind", "?"), b.get("n", "?")
            if b.get("needs_special"):
                a2s_id = f"{args.chapter}-p{page_num:03d}-b{n}"
                a2s = _load_sibling_json("A2S", a2s_id)
                if kind in ("figure", "table"):
                    _fig = _figure_table_html(
                        args, page_num, b, n, kind, fig_dir, fig_rel_prefix, blocks,
                        mm_per_px, measured,
                        inside_box=bool(box_furn and n in box_furn["inside_box"]),
                        clamp_top=profile["box_tabs"])
                    placed.append((col_by_n.get(n, "full"), _fig))
                    n_fig_cropped += 1
                    if not a2s:
                        page_gaps.append(f"[{n}] {kind} not transcribed (crop only)")
                    elif kind == "figure" and not (a2s.get("caption") or "").strip():
                        page_gaps.append(f"[{n}] figure has no caption — not printed inside the crop")
                    elif kind == "table" and not (a2s.get("header") or []):
                        page_gaps.append(f"[{n}] table has no structured rows — image only")
                else:
                    _note = (a2s or {}).get("note", "").strip().lower()
                    if _note.startswith(("defect", "unsure")) or (
                            a2s and not _is_real_latex(a2s.get("latex"))
                            and not (kind == "box" and a2s.get("text"))):
                        n_eq_pending += 1
                        page_gaps.append(f"[{n}] {kind}: recorded region does not contain this "
                                         f"block (flagged by the transcriber)")
                    elif a2s and (a2s.get("latex") or (kind == "box" and a2s.get("text"))):
                        n_eq_shown += 1
                    elif b.get("bbox"):
                        # Has a crop, so the content IS in the document -- only its LaTeX form
                        # is outstanding. Reporting that as "not captured" overstated the gap.
                        n_eq_pending += 1
                        page_gaps.append(f"[{n}] {kind}: shown as page image, LaTeX pending")
                    else:
                        n_eq_pending += 1
                        page_gaps.append(f"[{n}] {kind} not transcribed and no region to crop")
                    placed.append((col_by_n.get(n, "full"),
                                   _equation_html(args, page_num, n, kind, b, blocks,
                                                  fig_dir, fig_rel_prefix)))
            else:
                frag, is_banner = _block_html(b, n, kind, corr_by_n, bold_by_n, is_opener,
                                              role_by_n.get(n), style_by_n.get(n))
                # NCERT physics separates paragraphs with a FIRST-LINE INDENT and no space at
                # all -- measured 18pt on p003/p011/p021. The one exception is a paragraph
                # carried over from the previous page, which the book sets flush; A2 records
                # exactly that as first_block_continues_from_previous.
                if (profile["para_indent_mm"] and kind == "paragraph"
                        and not (n == first_block_n
                                 and rec.get("first_block_continues_from_previous"))):
                    frag = frag.replace('class="block block-paragraph"',
                                        'class="block block-paragraph indent"', 1)
                if is_banner:
                    banner_lines.append(frag)
                    if banner_col is None:
                        banner_col = role_by_n.get(n) and col_by_n.get(n)
                    continue
                if banner_lines:
                    # The banner is NOT always full width. On CHE12L-ch09 p001 it is measured in
                    # the RIGHT column (x 0.410-1.000) with the Objectives box beside it on the
                    # LEFT -- rendering it full width pushed it below the box and left a wide
                    # empty gap, which is nothing like the page. Use the measured column.
                    # Do NOT clear the title here. This used to drop the banner when a cropped
                    # strip already carried the artwork -- but the band is now drawn in CSS on
                    # EVERY page, so the condition was always true and the chapter heading
                    # ("CHAPTER 3 / HUMAN REPRODUCTION") vanished from the opening page.
                    bh = banner_img or _banner_html(banner_lines, _band_style)
                    if banner_img:
                        banner_lines.clear()
                        banner_img = ""
                    if bh:
                        placed.append(("full" if banner_img == "" and bh.startswith("<img")
                                       else (banner_col or "full"), bh))
                    banner_col = None
                    if deferred_bar:
                        placed.append(("full", deferred_bar))
                        deferred_bar = ""
                    if deferred_toc:
                        placed.append(("left" if "left" in col_bounds else "full", deferred_toc))
                        deferred_toc = ""
                placed.append((col_by_n.get(n, "full"), frag))
        if banner_lines:
            bh = banner_img or _banner_html(banner_lines, _band_style)
            if banner_img:
                banner_lines.clear()
                banner_img = ""
            if bh:
                placed.append(("full", bh))
            banner_col = None
            if deferred_bar:
                placed.append(("full", deferred_bar))
                deferred_bar = ""
            if deferred_toc:
                placed.append(("left" if "left" in col_bounds else "full", deferred_toc))
                deferred_toc = ""
        if deferred_bar:
            placed.insert(0, ("full", deferred_bar))
        if deferred_toc:   # contents panel on a page with no title block of its own
            placed.insert(0, ("left" if "left" in col_bounds else "full", deferred_toc))

        # The owner's standing ask: make what the extraction MISSES as visible as what it got.
        # A silent omission reads as completeness, which is the failure mode that matters most.
        placed = _merge_box_runs(placed)
        if box_furn:
            placed = _apply_box_furniture(placed, box_furn, geo["page_w_mm"], box_state)
        body_html = _assemble_columns(placed, col_bounds,
                                      prefer_float=profile["float_side_columns"])
        if page_panel:
            # SUMMARY / POINTS TO PONDER: the book prints the whole body on a tint, with the grey
            # margin band beside it on the SUMMARY pages. A2L records both, but the panel carries
            # no block number so it never reached the render and those five pages came out white.
            _b = page_panel.get("band")
            _edge = (f'border-left: {(_b["bbox"][2] - _b["bbox"][0]) * geo["page_w_mm"]:.1f}mm '
                     f'solid {_b["fill"]}; ' if _b else "")
            body_html = (f'<div class="page-panel" style="{_edge}'
                         f'background: {page_panel["fill"]};">{body_html}</div>')
        if page_gaps:
            items = "".join(f"<li>{_esc(g)}</li>" for g in page_gaps)
            right_html.append(
                f'<div class="gaps"><div class="gaps-head">Not yet captured on this page '
                f'({len(page_gaps)})</div><ul>{items}</ul></div>'
            )
        else:
            right_html.append('<div class="gaps complete">Every block on this page is transcribed.</div>')
        # The bottom strip already carries the folio tab and the print-year line as printed,
        # so the text version of the imprint would duplicate them.
        # No flowing footer: with content running continuously, anything appended after a page's
        # blocks lands wherever that page happens to end -- which is how "2022-23" ended up in the
        # middle of a sheet. It rides with the band at the head of the page instead.

        toc_cls = " cls-gap" if page_gaps else ""
        toc.append(f'<a class="toc-link{toc_cls}" href="#p{page_num:03d}">{page_num:03d}</a>')
        if args.no_scans:
            original_pane = ""
        else:
            original_pane = (
                f'<div class="pane original">'
                f'<div class="pane-label">Original scan'
                f'<span class="page-badge">page {page_num:03d}</span></div>'
                f'<img class="page-scan" src="{page_rel}" alt="original page {page_num}"></div>'
            )
        body_parts.append(f"""
<section class="page-row{' single' if args.no_scans else ''}" id="p{page_num:03d}">
  {abs_furniture}{folio_tab}
  {original_pane}
  <div{lane_style}>
    <div class="pane-label">{'Page' if args.no_scans else 'Extracted'}<span class="page-badge">{page_num:03d}</span></div>
    {''.join(right_html[:1])}{body_html}{''.join(right_html[1:])}
  </div>
</section>""")

    # The band's own two measured fills, read straight off A2L rather than derived: the strip
    # colour and the grey tab behind the running header (physics #c6eafb / #d1d2d4, each measured
    # on 48-49 pages). Only used where the profile asks for them, so biology's approved band is
    # untouched.
    _bc = (measured or {}).get("colors_used_by_the_book") or {}
    band_fill = ((_bc.get("page_header_band_fill") or {}).get("value") or "")
    band_tab_fill = ((_bc.get("running_header_fill") or {}).get("value") or "")
    if not band_tab_fill:
        for _r in ((measured or {}).get("full_detail_by_page") or {}).values():
            for _e in _r.get("elements_in_reading_order") or []:
                if _e.get("role") == "running_header" and _e.get("fill"):
                    band_tab_fill = _e["fill"]
                    break
            if band_tab_fill:
                break
    heading, banner, banner_strip, bar, panel_tint, box_fill = _palette_from_measurement(
        measured, _accent_for(args.chapter, measured) + ("",), banner_strip_sampled)
    # Captions: measured colour, falling back to body ink -- never the chapter accent.
    _cap = ((measured or {}).get("colors_used_by_the_book") or {}).get("figure_caption_text_color")
    caption_ink = (_cap or {}).get("value") or "var(--ink)"
    _band = ((measured or {}).get("colors_used_by_the_book") or {}).get("figure_caption_band_fill")
    caption_band = (_band or {}).get("value") or "transparent"
    _folio = ((measured or {}).get("colors_used_by_the_book") or {}).get("page_number_fill")
    folio_fill = (_folio or {}).get("value") or bar
    # Dark type on a light tab, white on a saturated one -- decided from the measured fill rather
    # than assumed, since physics' tab is pale blue and biology's is a strong orange.
    _h = folio_fill.lstrip("#")
    try:
        _lum = sum(int(_h[i:i + 2], 16) for i in (0, 2, 4)) / 3
    except ValueError:
        _lum = 0
    folio_ink = "#221f1f" if _lum > 170 else "#ffffff"
    scale = _type_scale_from_measurement(measured)
    # Type sizes come from the chapter's own measured ratios where available. Body prose is
    # 1.0 by definition, so every other role is expressed as a multiple of it -- exactly the
    # relationship A2L reports, carried straight into CSS with no second guess.
    size_vars = "\n".join(
        f"  --size-{role.replace('_','-')}: {v:.3f}rem;"
        for role, v in sorted(scale.items())
    )
    # Derived tints: a soft rule colour and a very light wash, mixed from the heading colour so
    # every subject gets a consistent set without hand-maintaining five hexes per subject.
    accent_soft, accent_wash = _tints(heading)
    # Token replacement, not %-formatting: the stylesheet is full of literal `%` (width: 100%).
    css = (_CSS_TMPL
           .replace("@ACCENT_SOFT@", accent_soft)
           .replace("@ACCENT_WASH@", accent_wash)
           .replace("@BANNER_STRIP@", banner_strip)
           .replace("@BANNER@", banner)
           .replace("@BAR@", bar)
           .replace("@PANEL_TINT@", panel_tint)
           .replace("@BODY_PT@", f"{geo['body_pt']:.2f}")
           .replace("@LEADING@", f"{profile['leading']:.2f}")
           .replace("@CORNER_HANG@", f"{profile['corner_hang_mm']:.1f}")
           .replace("@LOGO_H@", f"{100 + profile['corner_hang_mm'] / 11.7 * 100:.0f}")
           .replace("@PAGE_W@", f"{geo['page_w_mm']:.1f}")
           .replace("@PAGE_H@", f"{geo['page_h_mm']:.1f}")
           # Figure height cap, per subject. 0.28 of the sheet let FIGURE 1.18 take nearly a
           # third of p018 and push the closing lines off the foot; the book sets that artwork
           # at roughly a fifth. Biology keeps 0.28 -- its approved output is built on it and its
           # full-width diagrams need the room.
           .replace("@FIG_MAX_H@",
                    f"{geo['page_h_mm'] * profile.get('fig_max_frac', 0.28):.1f}")
           .replace("@OVERHANG@", f"{max(0.0, outer_mm - 14.0) * 0.55:.1f}")
           .replace("@MARGIN@", f"{page_margin_mm:.1f}")
           .replace("@PAD_T@", f"{pad_t:.1f}")
           .replace("@PAD_R@", f"{pad_r:.1f}")
           .replace("@PAD_B@", f"{pad_b:.1f}")
           .replace("@PAD_L@", f"{pad_l:.1f}")
           .replace("@BANNER_H@", f"{opener['banner_h'] or 95.0:.1f}")
           .replace("@BAR_H@", f"{opener['bar_h'] or 8.0:.1f}")
           .replace("@TOC_W@", f"{opener['toc_w'] or 55.0:.1f}")
           .replace("@BOX_FILL@", box_fill or "var(--accent-wash)")
           .replace("@CAPTION_INK@", caption_ink)
           .replace("@CAPTION_BAND@", caption_band)
           .replace("@FOLIO_FILL@", folio_fill)
           .replace("@FOLIO_INK@", folio_ink)
           .replace("@SIZE_VARS@", size_vars)
           .replace("@SUBJECT_CSS@", _subject_css(profile, geo, band_fill, band_tab_fill))
           .replace("@ACCENT@", heading))

    body_class = "clean" if args.no_scans else "review"
    subtitle = ("rendered from this pipeline's extracted data — no page scans, so none of the "
                "source PDF's watermark"
                if args.no_scans else
                "side-by-side review — left is the original scan, right is this pipeline's "
                "extraction")
    # In reader mode the page IS the product, so it gets PDF-viewer chrome instead of a web
    # header: a page counter that follows the scroll, zoom that scales the whole sheet, and a
    # print button that saves real pages at this book's measured size.
    if args.no_scans:
        chrome_open = (
            '<div class="pdf-toolbar" role="toolbar" aria-label="Page viewer">'
            f'<span class="pdf-name">{_esc(args.chapter)}</span>'
            '<div class="pdf-mid">'
            '<input id="pdf-page" type="text" inputmode="numeric" value="1" aria-label="Page number">'
            f'<span class="pdf-of">/ <span id="pdf-count">{len(pages)}</span></span>'
            '<span class="pdf-sep"></span>'
            '<button id="pdf-zoom-out" type="button" aria-label="Zoom out">&minus;</button>'
            '<span id="pdf-zoom" class="pdf-zoom">100%</span>'
            '<button id="pdf-zoom-in" type="button" aria-label="Zoom in">+</button>'
            '<span class="pdf-sep"></span>'
            '<button id="pdf-fit" type="button" aria-label="Fit to width" title="Fit to width">&#8596;</button>'
            '</div>'
            '<button id="pdf-print" type="button" title="Print / save as PDF">&#9113;</button>'
            # Sheet-per-book-page is a per-chapter decision, measured not assumed: physics'
            # bands drift to mid-sheet under continuous flow, biology's do not.
            f'</div>\n<main id="viewer"'
            f'{" class=\"break-per-page\"" if profile["break_per_page"] else ""}>'
        )
        chrome_close = (
            # A single FIXED band. Chrome repeats a position:fixed element at the top of every
            # printed sheet, which is what a running header needs to be: under continuous flow a
            # per-page band lands wherever the previous page ended, so it kept appearing mid-sheet.
            # The per-page bands stay in the HTML (they mark where each book page starts on screen)
            # and are hidden in print, where this one takes over.
            f'<div class="print-band band-recto">'
            f'<span class="band-bar"></span><span class="band-corner">{corner_img}</span>'
            f'<span class="band-tab"><i class="band-mark"></i>{_esc((title or args.chapter).split("—")[-1].strip()[:38])}</span>'
            f'</div>\n</main>\n' + _VIEWER_JS)
    else:
        chrome_open = (
            f'<header class="doc-head"><h1>{_esc(title)}</h1>'
            f'<div class="meta">chapter {_esc(args.chapter)} · source: {_esc(pdf_rel)} · '
            f'{len(pages)} pages · {subtitle}</div></header>'
            f'<nav class="toc">{"".join(toc)}</nav>'
        )
        chrome_close = ""
    html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{_esc(title)} — review</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="vendor/katex.min.css">
<style>{css}</style>
</head>
<body class="{body_class}">
{chrome_open}
{''.join(body_parts)}
{chrome_close}
<script defer src="vendor/katex.min.js"></script>
<script defer src="vendor/auto-render.min.js" onload="renderMathInElement(document.body, {{
  delimiters: [{{left: '$$', right: '$$', display: true}},
               {{left: '\\\\(', right: '\\\\)', display: false}}],
  throwOnError: false, errorColor: '#b23a2e', strict: false}});"></script>
</body>
</html>"""

    suffix = "READER" if args.no_scans else "REVIEW"
    out_path = os.path.join(html_dir, f"{args.chapter}_{suffix}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_doc)

    print(f"pages: {len(pages)} | blocks: {n_blocks} | figures/tables cropped: {n_fig_cropped}")
    print(f"equations shown: {n_eq_shown} | equations still pending A2S: {n_eq_pending}")
    print(f"wrote {os.path.relpath(out_path, rc.pp())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
