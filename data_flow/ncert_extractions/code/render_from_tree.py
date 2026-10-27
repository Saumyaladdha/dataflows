#!/usr/bin/env python3
"""Render chapter.html FROM chapter.json -- nothing else.

    python code/render_from_tree.py data/old_ncert/class_11/biology/ch02_.../chapter.json

THE POINT IS THE CONSTRAINT. This renderer may not open the PDF. If a page cannot be rebuilt
from the stored tree plus the style row, the stored data is incomplete and that is a defect to
fix in the extraction -- not something to paper over by reaching back to the source. Every
other consumer (the app, the search index, an AI prompt) has exactly this much to work with,
so the HTML is the honest test of whether the data is enough.

It renders the chapter as a READING view, not a facsimile: the book's measure, type, colours,
header band, folio tab and footer, with the content flowing in reading order. The printed
position of every node is still in `boxes` for anyone who wants a facsimile instead.

NOTHING OVERFLOWS. The sheet is a fixed box; the column is the book's own measure; figures and
tables are capped at the measure; and the page is allowed to GROW rather than clip, because
losing a sentence to keep a page count is never the right trade.
"""

import argparse
import base64
import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import book_design as design_lib  # noqa: E402

FONT_DIR = os.path.join(ROOT, "assets", "fonts")


def esc(s):
    return html.escape(s or "", quote=False)


def _face(name, file, weight, style):
    p = os.path.join(FONT_DIR, file)
    if not os.path.exists(p):
        return ""
    with open(p, "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode("ascii")
    return (f"@font-face{{font-family:'{name}';src:url(data:font/otf;base64,{b64})"
            f" format('opentype');font-weight:{weight};font-style:{style};font-display:swap;}}")


def fonts():
    return "".join([
        _face("NcertBody", "texgyrebonum-regular.otf", 400, "normal"),
        _face("NcertBody", "texgyrebonum-bold.otf", 700, "normal"),
        _face("NcertBody", "texgyrebonum-italic.otf", 400, "italic"),
        _face("NcertBody", "texgyrebonum-bolditalic.otf", 700, "italic"),
        _face("NcertDisplay", "texgyreadventor-regular.otf", 400, "normal"),
        _greek_faces(),
    ])


def _greek_faces():
    """GREEK IN THE BOOK'S FACE. NCERT sets alpha/beta in a Times-style TrueType face or Symbol,
    upright; Bonum's own beta is a curled form that reads as `6` (BIO12L ch04 p025: `a and 6
    chains`). Declared after the Bonum faces, for the Greek block only, so it wins there and
    nowhere else; with no Times on the viewer's machine the text falls back to Bonum as before."""
    src = ('local("Times New Roman"),local("TimesNewRomanPSMT"),local("Times"),'
           'local("Liberation Serif"),local("Nimbus Roman")')
    return "".join(
        f"@font-face{{font-family:'NcertBody';src:{src};font-weight:{w};font-style:{s};"
        f"unicode-range:U+0370-03FF;}}"
        for w, s in ((400, "normal"), (700, "normal"), (400, "italic"), (700, "italic")))


def marked_html(body, marks):
    """`body` + character-offset `marks` -> inline HTML.

    This is the same arithmetic a product does to pull one sentence out with its italics, so
    rendering it here exercises the stored format rather than a parallel one.
    """
    if not body:
        return ""
    if not marks:
        return esc(body)
    edits = sorted(marks, key=lambda m: m["from"])
    out, pos = [], 0
    for m in edits:
        a, b = max(m["from"], pos), m["to"]
        if b <= a:
            continue
        out.append(esc(body[pos:a]))
        cls = " ".join(k for k in ("b", "i", "sc") if m.get(k))
        inner = esc(body[a:b])
        if m.get("sup"):
            inner = f"<sup>{inner}</sup>"
        if m.get("sub"):
            inner = f"<sub>{inner}</sub>"
        out.append(f'<span class="{cls}">{inner}</span>' if cls else inner)
        pos = b
    out.append(esc(body[pos:]))
    return "".join(out)


CSS = """
*{box-sizing:border-box}
html{background:#8f9190}
body{margin:0;padding:8mm 0;font-family:var(--body-font);color:var(--ink)}
:root{--body-font:'NcertBody','Bookman Old Style',Bookman,Georgia,serif;
      --disp-font:'NcertDisplay','Century Gothic',Avenir,sans-serif;
      --sans:Arial,Helvetica,sans-serif;--ink:@INK@}
/* One sheet at the book's real trim. Fixed width, growing height -- a page that runs long
   continues rather than clipping. */
/* THE SHEET GROWS; IT NEVER CLIPS. A reading view holds a whole chapter in one column, so a
   fixed height with `overflow:hidden` does not "fit the page" -- it DELETES whatever did not
   fit. Measured on BIO11O ch02, the last third of the chapter rendered underneath the footer
   bar and off the bottom of the sheet. Losing a sentence to keep a page count is never the
   right trade, so the box is a MINIMUM and the footer is flow content at the end of it. */
/* ONE SHEET PER PRINTED PAGE. The chapter was previously rendered as a single endless column,
   so the book's own pagination vanished: no folio, no running head, no page break anywhere
   after the first. The tree is structure-ordered, but every node records which printed page it
   came from, so the pages can be put back. Height is a MINIMUM, never a clip. */
/* ONE SHEET IS EXACTLY ONE NCERT PAGE. Height is FIXED at the book's trim, not a minimum:
   a sheet that grows with its content is no longer a page, and the chapter stops matching the
   book page for page. The content is made to fit instead, by the per-page `--fit` factor the
   build computes from the measured line counts and the printed line pitch -- so the type is
   scaled the way a typesetter would, rather than the page being stretched. */
.sheet{position:relative;width:@PW@mm;height:@PH@mm;margin:0 auto 7mm;background:#fff;
       box-shadow:0 1px 5px rgba(0,0,0,.45);overflow:hidden}
.sheet .measure{font-size:calc(1em * var(--fit, 1))}
.sheet::after{content:"";display:block;clear:both}
.band,.strip,.footbar{position:absolute;left:0;right:0}
/* Cut page artwork: the opener's panel and its QR, drawn beneath the type the page sets over
   them -- which is why the title stays live, selectable text rather than baked-in pixels. */
img.art{position:absolute;z-index:0;display:block}
/* The opener's section-contents rail, where the book prints it: in the margin beside the
   opening prose, italic in the book's accent. Content-wise it is furniture -- it duplicates
   the chapter's own headings -- so it is drawn from the PAGE record, never from the tree. */
.toc-entry{position:absolute;z-index:1;font-style:italic;font-size:.82em;line-height:1.3;
           color:@HEAD@}
.sheet.opener .measure{position:relative;z-index:1}
.rhead{position:absolute;display:flex;align-items:center;white-space:nowrap}
.folio{position:absolute;display:flex;align-items:center;justify-content:center}
.imprint{position:absolute;left:0;right:0;text-align:center}
/* The measure: the book's own column, mirrored by page side. Everything flows inside it, so
   two blocks can never land on top of each other. */
/* The book's own measure. Absolute only in X -- the column flows down the sheet and the
   sheet grows to hold it. */
.measure{position:relative;width:@MEASURE@mm;max-width:100%}
.p{margin:0 0 .34em;text-align:justify;hyphens:auto;line-height:@LEAD@}
/* HEADINGS AS THE BOOK SETS THEM: small caps in the book's own accent, stepped by level.
   `2.1 KINGDOM MONERA` is a topic, `2.1.1 Archaebacteria` a subtopic -- the level is the dot
   count in the printed number, so the hierarchy a reader sees matches the tree a query walks. */
.h{margin:.9em 0 .32em;font-weight:700;font-variant:small-caps;line-height:1.26;
   color:@HEAD@;letter-spacing:.012em;clear:both}
.h.lvl1{font-size:1.12em}
.h.lvl2{font-size:1.0em;font-variant:small-caps;font-weight:700}
.h.lvl3{font-size:.94em;font-variant:normal;font-weight:700}
.h.plain{font-size:1.12em}
.li{margin:0 0 .25em;text-align:left}
ul.list{margin:.3em 0 .5em;padding-left:1.1em}
/* A FIGURE SITS ON THE SIDE THE BOOK PRINTS IT. Every node carries the bbox it was measured
   at, so the side is known, not guessed: a figure whose box lies in the outer rail is floated
   there and the prose runs beside it, exactly as the page sets it; one that spans the measure
   runs full width. Without this every diagram stacked in the middle of the column and the
   page lost the arrangement that makes it readable. */
figure{margin:.6em 0;padding:0;max-width:100%}
figure img{display:block;width:100%;max-width:100%;height:auto}
figure.rail-left{float:left;margin:.2em 5mm .5em 0;clear:left}
figure.rail-right{float:right;margin:.2em 0 .5em 5mm;clear:right}
figure.full{clear:both}
/* Tables are set as TABLES. The grid is measured from the printed column positions, so the
   cells line up the way the book sets them without a picture standing in for the data. */
/* THE TABLE FITS THE MEASURE. `width:100%` alone is not enough: with auto layout a long cell
   widens its column and pushes the last one off the sheet -- measured, Table 1.1's
   `Phylum/Division` column was cut in half at the trim. `table-layout:fixed` divides the
   measure between the columns and lets the text wrap inside them, which is what the book does. */
table.grid{border-collapse:collapse;table-layout:fixed;width:100%;max-width:100%;
           margin:.6em 0;font-size:.8em;line-height:1.28;clear:both;
           word-wrap:break-word;overflow-wrap:break-word}
table.grid caption{caption-side:top;text-align:left;font-variant:small-caps;font-weight:700;
                   padding-bottom:.3em;color:@HEAD@}
/* The rule colour is the book's own, darkened from the measured fill rather than
   borrowed from the heading colour -- a cyan rule on a peach table is not the page. */
table.grid th,table.grid td{border:.3mm solid rgba(0,0,0,.28);padding:1mm 1.4mm;
                            vertical-align:top;text-align:left}
table.grid thead th{font-weight:700}
figcaption{font-size:.88em;line-height:1.3;margin-top:.25em;color:#333}
.box{margin:.4em 0;font-size:.95em;line-height:1.3}
.b{font-weight:700}.i{font-style:italic}.sc{font-variant:small-caps}
sup,sub{font-size:.7em;line-height:0}
.bar{position:sticky;top:0;z-index:50;background:#2f2f2f;color:#eee;padding:6px 14px;
     font:13px/1.45 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
     display:flex;gap:14px;flex-wrap:wrap;align-items:center}
.bar .tag{background:#4a4a4a;border-radius:3px;padding:1px 7px}
.bar .warn{background:#8a4b22}
@page{size:@PW@mm @PH@mm;margin:0}
/* Furniture measured by a2l-layout-reader, for books with no hand-measured design. */
.mfurn{position:absolute;z-index:0;overflow:hidden;display:flex;align-items:center;
       justify-content:center;font-size:.8em;white-space:nowrap}
.mfurn.running-header{z-index:2;font-variant:small-caps;letter-spacing:.3pt;
                      justify-content:flex-start}
.mfurn.page-number{z-index:3;font-weight:700;font-size:1.25em;color:#fff}
/* A paragraph continued from the previous page takes no first-line indent. */
.p.cont{text-indent:0}
/* Content the book sets in the margin, positioned where it printed. */
.inrail{position:absolute;z-index:1;font-size:.86em;line-height:1.3;text-align:left;margin:0}
/* A figure positioned where the page printed it, out of the text flow entirely. */
.fig.placed{position:absolute;margin:0;z-index:2}
/* CONTAIN THE IMAGE INSIDE ITS MEASURED BOX.
   `height:auto` keeps the file's own aspect and ignores the box height, so a 289x725 crop
   placed in a 41x53mm box rendered 104mm tall -- double its box -- and every figure on the
   page overlapped the next and ran off the sheet. `object-fit:contain` fits the artwork
   inside the measured rectangle without distorting it, and `overflow:hidden` means a crop
   whose aspect does not match its measurement can never spill over the page again. */
.fig.placed{overflow:hidden}
.fig.placed img{width:100%;height:100%;object-fit:contain;object-position:top left;
                display:block}
.fig.placed figcaption{font-size:.84em;line-height:1.25;margin-top:1.1mm}
/* EXERCISES -- a hanging indent, the way the book sets them. */
.q{display:flex;gap:2.2mm;margin:0 0 1.1mm}
.qn{flex:0 0 auto;min-width:6mm;text-align:right;font-variant-numeric:tabular-nums}
.qt{flex:1 1 auto;text-align:justify}
.qsub{margin:0 0 .8mm 8.2mm}
@media print{html,body{background:#fff;padding:0}.bar{display:none}
  /* ONE SHEET PER PRINTED PAGE. Without an explicit break the browser paginates on its own
     and a 784pt sheet lands across two A4 leaves, so Cmd-P does not give back the book.
     `break-after` is the modern property; `page-break-after` is kept for older engines. */
  .sheet{margin:0;box-shadow:none;break-after:page;page-break-after:always;
         break-inside:avoid;page-break-inside:avoid}
  .sheet:last-of-type{break-after:auto;page-break-after:auto}
  @page{size:var(--sheet-w,612pt) var(--sheet-h,784pt);margin:0}}
"""


def render(doc, fig_base=None):
    d = design_lib.design_for(doc["book_id"])
    mm = design_lib.pt_to_mm
    # THE SHEET IS THE BOOK'S SHEET, NOT THE DESIGN'S DEFAULT.
    # Class 12 Biology ch01 is an A4 scan -- 595.32 x 841.92pt. Rendering it on the design's
    # canonical 612 x 784 made every sheet 2.8% too wide and 6.9% too short, so no coordinate
    # could line up and even the QR code came out rectangular on a square original. The page
    # records its own measured size; use it, and fall back to the design only when it is
    # absent. Measured per chapter: all pages of a chapter share one trim.
    _sp = next((p.get("sheet_pt") for p in doc.get("pages") or [] if p.get("sheet_pt")), None)
    W, H = (float(_sp[0]), float(_sp[1])) if _sp and len(_sp) == 2 else d.trim_pt
    ed = "new" if doc["edition"] == "latest" else "old"
    head_ink = d.heading_ink

    css = (CSS.replace("@PW@", f"{mm(W):.2f}").replace("@PH@", f"{mm(H):.2f}")
              .replace("@INK@", d.ink).replace("@HEAD@", head_ink)
              .replace("@LEAD@", str(d.leading))
              .replace("@MEASURE@", f"{mm(d.measure_pt):.2f}")
              .replace("@TINT@", getattr(d, "accent_wash", None) or "#f4f4ef")
              .replace("@FOOT@", f"{mm(H - d.text_foot_pt):.2f}"))

    # --- furniture, drawn once per sheet from the measured design -------------------------
    def furniture(side, folio, imprint, running):
        out = []
        band = getattr(d, "header_band", None)
        if band:
            out.append(f'<div class="band" style="top:{mm(band["y0_pt"]):.2f}mm;'
                       f'height:{mm(band["y1_pt"]-band["y0_pt"]):.2f}mm;'
                       f'background:{band["fill"]}"></div>')
        strip = getattr(d, "header_strip", None)
        if strip:
            out.append(f'<div class="strip" style="top:{mm(strip["y0_pt"]):.2f}mm;'
                       f'height:{mm(strip["y1_pt"]-strip["y0_pt"]):.2f}mm;'
                       f'background:{strip["fill"]}"></div>')
        corner = getattr(d, "header_corner", None)
        if corner and band:
            edge = "right" if side == "recto" else "left"
            out.append(f'<div style="position:absolute;{edge}:0;top:{mm(band["y0_pt"]):.2f}mm;'
                       f'width:{mm(corner["w_pt"]):.2f}mm;'
                       f'height:{mm(band["y1_pt"]-band["y0_pt"]):.2f}mm;'
                       f'background:{corner["fill"]}"></div>')
        rh = getattr(d, "running_head", None)
        if rh and running:
            edge = "left" if side == "recto" else "right"
            st = (f'{edge}:{mm(rh["inset_pt"]):.2f}mm;top:{mm(rh["y_pt"]):.2f}mm;'
                  f'font-size:{rh["size_pt"]:.1f}pt;color:{rh["ink"]};'
                  f'font-family:var(--{"disp-font" if rh["font"]=="display" else "sans" if rh["font"]=="sans" else "body-font"})')
            if rh.get("smallcaps"):
                st += ";font-variant:small-caps"
            if rh.get("uppercase"):
                st += ";text-transform:uppercase;letter-spacing:.06em"
            out.append(f'<div class="rhead" style="{st}">{esc(running)}</div>')
        fo = getattr(d, "folio", None)
        if fo and folio is not None:
            x = fo["x_recto_pt"] if side == "recto" else fo["x_verso_pt"]
            st = (f'left:{mm(x):.2f}mm;top:{mm(fo["y0_pt"]):.2f}mm;'
                  f'width:{mm(fo["w_pt"]):.2f}mm;height:{mm(fo["h_pt"]):.2f}mm;'
                  f'font-family:var(--{"sans" if fo["font"]=="sans" else "disp-font"});'
                  f'font-size:{fo["size_pt"]:.1f}pt;font-weight:{fo.get("weight",700)};'
                  f'color:{fo["ink"]}')
            if fo.get("fill"):
                st += f';background:{fo["fill"]}'
            if fo.get("radius_pt"):
                r = mm(fo["radius_pt"])
                st += (f';border-radius:{r:.1f}mm {r:.1f}mm 0 0'
                       if fo.get("radius_corners") == "top" else f';border-radius:{r:.1f}mm')
            out.append(f'<div class="folio" style="{st}">{folio}</div>')
        return "".join(out)

    def foot(imprint):
        """Anchored to the FOOT OF THE SHEET.

        It was briefly flow content, from when a sheet could grow and content would otherwise
        slide under it. The sheet is now exactly one NCERT page and the content is scaled to
        fit, so the footer belongs where the book prints it -- at the bottom of the page -- and
        in flow it floated up to wherever the text happened to stop.
        """
        fb = getattr(d, "footer_bar", None)
        im = getattr(d, "imprint", None)
        out = []
        if fb:
            out.append(f'<div class="footbar" style="top:{mm(fb["y0_pt"]):.2f}mm;bottom:0;'
                       f'background:{fb["fill"]}"></div>')
        if im:
            out.append(f'<div class="imprint" style="top:{mm(im["y_pt"]):.2f}mm;'
                       f'font-family:var(--sans);font-size:{im["size_pt"]:.1f}pt;'
                       f'color:{im["ink"]}">{esc(imprint or "")}</div>')
        return "".join(out)

    # --- content, PAGE BY PAGE ------------------------------------------------------------
    # Walk the tree once, remembering the open headings, and bucket every leaf by the printed
    # page it came from. A heading is re-emitted at the top of a page its section continues
    # onto, so a page never opens with orphaned prose under no heading.
    pages_order, buckets, heading_stack = [], {}, []
    page_nodes = {}

    # One page, ONE key. A page that prints a folio is keyed by the folio; one that does not
    # is keyed by its file. Mixing the two splits a single page into two sheets -- Figure 1.1
    # carries `page_file: 008` and no folio, so it opened a second sheet `f008` beside page
    # 8's own `p8`, and the chapter rendered 10 sheets for a 9-page source.
    file_to_folio = {p_["page_file"]: p_.get("printed")
                     for p_ in doc.get("pages") or [] if p_.get("page_file")}

    def page_of(n):
        """The key a node buckets under: its printed folio, or its page file when the page
        prints no folio (the chapter-opening page)."""
        ps = n.get("pages") or []
        if ps:
            return ps[0]
        pf = n.get("page_file")
        if not pf:
            return None
        folio = file_to_folio.get(pf)
        return folio if folio is not None else f"f{pf}"

    def note_node(pg, n):
        if pg is not None:
            page_nodes.setdefault(pg, []).append(n)

    def emit(pg, html_str):
        if pg is None:
            pg = pages_order[-1] if pages_order else None
        if pg is None:
            return
        if pg not in buckets:
            buckets[pg] = []
            pages_order.append(pg)
            # A HEADING PRINTS ONCE, ON THE PAGE THE BOOK PRINTS IT.
            #
            # Every open heading used to be re-emitted at the top of each new page, so that a
            # page never opened with orphaned prose. The book does not do this: NCERT runs
            # section 1.1 across pages 3 to 5 and prints its heading once, on page 3. The
            # re-emit put "1.1 DIVERSITY IN THE LIVING WORLD" at the top of pages 4, 5 and 6
            # and "1.2 TAXONOMIC CATEGORIES" again on page 8 -- text the book does not print
            # there, which also pushed each page's real content down and contributed to the
            # overflow. The running head is what tells a reader where they are mid-section,
            # and that is already emitted per page.
            pass
        buckets[pg].append(html_str)

    body = []

    def node_html(n, depth):
        k = n["kind"]
        if k in ("section", "summary", "exercises"):
            head = " ".join(x for x in (n.get("number"), n.get("title")) if x)
            lvl = (n.get("number") or "").count(".") if n.get("number") else 0
            cls = f"h lvl{min(lvl,3)}" if n.get("number") else "h plain"
            ink = n.get("layout_text_color")
            style = f' style="color:{ink}"' if ink else ""
            html_h = f'<div class="{cls}"{style}>{esc(head)}</div>'
            emit(page_of(n), html_h)
            heading_stack.append((lvl, html_h))
            for c in n.get("children") or []:
                node_html(c, depth + 1)
            while heading_stack and heading_stack[-1][0] >= lvl:
                heading_stack.pop()
            return
        if k == "table" and n.get("table_grid"):
            # THE GRID, NOT A PICTURE OF IT. A cell is what a flashcard or a PYQ cites, so the
            # table is set as a real table and stays selectable, searchable and translatable.
            g = n["table_grid"]
            cap = n.get("caption") or ""
            rows = g["cells"]
            head = rows[0] if rows else []
            # The book's own tints, measured off the page rather than chosen.
            tfill = n.get("table_fill") or ""
            hfill = n.get("table_header_fill") or tfill
            tstyle = f' style="background:{tfill}"' if tfill else ""
            hstyle = f' style="background:{hfill}"' if hfill else ""
            html_t = [f'<table class="grid"{tstyle}>']
            if cap:
                html_t.append(f"<caption>{esc(cap)}</caption>")
            html_t.append(f"<thead><tr{hstyle}>"
                          + "".join(f"<th>{esc(c)}</th>" for c in head)
                          + "</tr></thead><tbody>")
            for r in rows[1:]:
                html_t.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>")
            html_t.append("</tbody></table>")
            emit(page_of(n), "".join(html_t))
            return
        if k in ("figure", "table"):
            src = n.get("image") or n.get("image_local")
            cap = n.get("caption") or ""
            if src:
                if fig_base and not src.startswith("http"):
                    src = os.path.join(fig_base, os.path.basename(src))
                note_node(page_of(n), n)
                fill = n.get("layout_fill")
                bx = (n.get("boxes") or [{}])[0]
                bb = bx.get("bbox")
                # PLACE IT WHERE THE BOOK PRINTS IT.
                #
                # Floating a figure into the text flow puts it wherever the preceding
                # paragraph happens to end, which is not where the page prints it and loses
                # every multi-panel arrangement. Page 13 of Class 11 ch01 prints Figure 1.3 as
                # four photographs in a 2x2 grid; the extractor cut it as two side-by-side
                # crops (x 0.098-0.474 and 0.508-0.873, the same vertical band), and floating
                # them stacked the two columns one above the other, ran off the bottom of the
                # sheet and cut the last photograph in half.
                #
                # The measured box says exactly where the artwork sat, so it is positioned
                # there -- which reproduces the grid, the side-by-side pairs and the figures
                # the book sets in the outer rail, all from the same rule. Only a MEASURED box
                # may be used this way; an estimated one is a reading-order guess and would
                # place the figure confidently in the wrong place, so those still float.
                if bb and bx.get("src") in ("measured", "a2l-agent") and bb[2] > bb[0]:
                    style = (f'left:{mm(bb[0] * W):.2f}mm;top:{mm(bb[1] * H):.2f}mm;'
                             f'width:{mm((bb[2] - bb[0]) * W):.2f}mm')
                    if bb[3] > bb[1]:
                        style += f';height:{mm((bb[3] - bb[1]) * H):.2f}mm'
                    if fill:
                        style += f';background:{fill}'
                    emit(page_of(n),
                         f'<figure class="fig placed" style="{style}">'
                         f'<img src="{esc(src)}" alt="{esc(cap)}">'
                         f'{f"<figcaption>{esc(cap)}</figcaption>" if cap else ""}</figure>')
                    return
                side_cls, width = _figure_placement(n, d)
                fstyle = f";background:{fill};padding:1.5mm" if fill else ""
                emit(page_of(n),
                     f'<figure class="{side_cls}" style="width:{width:.1f}mm{fstyle}">'
                     f'<img src="{esc(src)}" alt="{esc(cap)}">'
                     f'{f"<figcaption>{esc(cap)}</figcaption>" if cap else ""}</figure>')
            elif cap:
                emit(page_of(n), f'<div class="box">{esc(cap)}</div>')
            return
        if k == "list":
            items = n.get("items") or []
            emit(page_of(n), '<ul class="list">' + "".join(
                f'<li class="li">{marked_html(i.get("body",""), i.get("marks") or [])}</li>'
                for i in items) + "</ul>")
            return
        if k == "question":
            # THE NUMBER IS PART OF THE QUESTION. The tree carries `number` "1".."18" and the
            # renderer dropped it, so eighteen numbered exercises came out as eighteen
            # anonymous paragraphs -- unusable for a question bank, and not what the book
            # prints. NCERT sets them as a hanging indent: the numeral in its own column, the
            # text and every turnover line aligned past it (A2L measured numerals at x=181px
            # and all text at x=232px on BIO11L p009).
            num = (n.get("number") or "").strip()
            body = marked_html(n.get("body", ""), n.get("marks") or [])
            parts = [f'<div class="q">'
                     f'<span class="qn">{esc(num)}.</span>'
                     f'<span class="qt">{body}</span></div>']
            # Sub-parts print on their OWN lines -- (a)(b)(c) options, (i)-(v) terms, the two
            # Mangifera spellings. Run inline they stop being alternatives to choose between.
            for sub in n.get("parts") or n.get("items") or []:
                parts.append(f'<div class="qsub">'
                             f'{marked_html(sub.get("body", ""), sub.get("marks") or [])}'
                             f'</div>')
            emit(page_of(n), "".join(parts))
            note_node(page_of(n), n)
            return
        cls = "box" if k == "box" else "p"
        # CONTENT THE BOOK SETS IN THE MARGIN BELONGS IN THE MARGIN.
        #
        # The unit opener prints its chapter list down the left rail (x 0.098-0.287) beside
        # the opening prose, which runs in the right column (x 0.324-0.873). Both were poured
        # into one column in reading order, so the chapter list came out as four bold
        # paragraphs underneath the prose instead of a panel beside it -- and the same is true
        # of every marginal note and side box in the corpus.
        #
        # The measured box already says which. A node whose box barely overlaps the body
        # column is not body text; it is set in the rail, and it is positioned there.
        bx0 = (n.get("boxes") or [{}])[0]
        bb = bx0.get("bbox")
        if bb and bx0.get("src") in ("measured", "a2l-agent") and bb[2] > bb[0]:
            # `column` is the page's OWN column, measured per page -- the unit opener sets a
            # 0.098-0.300 rail beside a 0.324-0.874 text column, which is nothing like the
            # design's default measure, so comparing against that default placed only one
            # node of five. The page's own answer is the one to use; the design's measure is
            # only the fallback for pages no agent has measured.
            col = (n.get("column") or "").lower()
            if col in ("side", "left", "rail", "margin"):
                overlap = 0.0
            else:
                mx0, mx1 = d.text_box(1)[0] / d.trim_pt[0], d.text_box(1)[2] / d.trim_pt[0]
                overlap = max(0.0, min(bb[2], mx1) - max(bb[0], mx0))
            if overlap < 0.55 * (bb[2] - bb[0]):
                emit(page_of(n),
                     f'<div class="{cls} inrail" style="left:{mm(bb[0] * W):.2f}mm;'
                     f'top:{mm(bb[1] * H):.2f}mm;'
                     f'width:{mm(max((bb[2] - bb[0]) * W, 28)):.2f}mm">'
                     f'{marked_html(n.get("body", ""), n.get("marks") or [])}</div>')
                note_node(page_of(n), n)
                return
        # A PARAGRAPH PRINTED ACROSS TWO PAGES IS PRINTED ACROSS TWO PAGES.
        #
        # The tree keeps it as ONE node, which is right -- it is one paragraph, and a product
        # asking for "1.2.1 Species, paragraph 2" wants all of it. But the RENDER is the book,
        # and the book breaks it. Emitting the whole node on the first of its pages put the
        # continuation on the wrong page, overfilled that page and left the next one starting
        # mid-thought. Four of this chapter's paragraphs are affected, and an external review
        # named every one of their break points:
        #     page 3 ends "...biodiversity or the number and"
        #     page 5 ends "...systematic arrangement of organisms. Linnaeus"
        #     page 6 ends "...Solanum includes species like nigrum and"
        #     page 7 ends "...the next higher category called Phylum. All"
        # `char_ranges` records exactly that -- which characters of the node printed on which
        # page -- so each page gets its own fragment, and the node stays whole in the data.
        body_all = n.get("body", "")
        marks_all = n.get("marks") or []
        ranges = [r for r in (n.get("char_ranges") or []) if r.get("to", 0) > r.get("from", 0)]
        if len(ranges) > 1 and body_all:
            for i, r in enumerate(ranges):
                a, b = r["from"], min(r["to"], len(body_all))
                frag = body_all[a:b]
                if not frag.strip():
                    continue
                # Marks are character offsets into the WHOLE body, so each is clipped to this
                # fragment and re-based onto it; a mark spanning the break survives on both.
                fm = []
                for m in marks_all:
                    f0, t0 = max(m["from"], a), min(m["to"], b)
                    if t0 > f0:
                        fm.append({**m, "from": f0 - a, "to": t0 - a})
                pg_key = (r.get("page") if r.get("page") is not None
                          else f"f{r.get('page_file')}")
                # A continued fragment takes no first-line indent -- it is not a new paragraph.
                frag_cls = f"{cls} cont" if i else cls
                emit(pg_key, f'<div class="{frag_cls}">{marked_html(frag, fm)}</div>')
                note_node(pg_key, n)
            return
        note_node(page_of(n), n)
        emit(page_of(n), f'<div class="{cls}">'
                         f'{marked_html(n.get("body",""), n.get("marks") or [])}</div>')

    # THE UNIT PAGES ARE PAGES OF THIS FILE AND MUST GET SHEETS.
    # Class 11 ch01's PDF is 9 pages: the Unit 1 opener, the Ernst Mayr biography, then the 7
    # chapter pages. They belong to the BOOK rather than the chapter, so they are stored
    # separately -- but storing them elsewhere is not a reason to stop PRINTING them, and
    # rendering 7 sheets for a 9-page file is simply wrong. They are rendered first, in the
    # order the book binds them.
    for n in doc["tree"]:
        node_html(n, 0)

    # EVERY PAGE OF THE SOURCE GETS A SHEET, even one whose content all sits in a figure we
    # could not crop or on a page we have not read. A missing sheet silently renumbers the
    # whole chapter: Class 12 ch01 printed 22 sheets for 23 pages, so from that point on
    # every folio in the render was one short of the book.
    for _p in doc["pages"]:
        for key in ((_p["printed"],) if _p.get("printed") is not None else ()) + \
                   ((f"f{_p['page_file']}",) if _p.get("page_file") else ()):
            if key in buckets:
                break
        else:
            key = (_p["printed"] if _p.get("printed") is not None
                   else f"f{_p.get('page_file')}")
            buckets.setdefault(key, [])
            if key not in pages_order:
                pages_order.append(key)

    running = doc["chapter"]["title"]
    page_meta = {}
    for _p in doc["pages"]:
        if _p.get("printed") is not None:
            page_meta[_p["printed"]] = _p
        if _p.get("page_file"):
            page_meta[f"f{_p['page_file']}"] = _p

    join = doc.get("text_join") or {}
    unread = len(join.get("pages_missing") or [])
    warn = (f'<span class="tag warn">{unread} page(s) WITHOUT an agent read</span>'
            if unread else
            f'<span class="tag">agent text {join.get("pages_with_agent",0)}/'
            f'{join.get("pages",0)} pages</span>')

    # ONE TYPE SIZE FOR THE WHOLE CHAPTER -- UNTIL THAT WOULD CLIP.
    #
    # NCERT picks one size for a chapter and lets the looser pages end early, so the chapter
    # size is the right default and is what the fullest page allows. But when a single page
    # needs more shrink than the rest, setting the WHOLE chapter to that size makes every
    # other page tiny; and refusing to shrink that page at all clips it. So: the chapter is
    # set at the size its pages generally need, and a page that still will not fit is given
    # its own smaller factor rather than being cut off. A page needing less than 0.72 is not
    # scaled further -- it is reported, because at that point the content is on the wrong page.
    # Previously the tightest page decided for all, and a page with room to
    # spare simply ends sooner, exactly as the printed book's do.
    per_page = {pg: fit_factor(page_nodes.get(pg) or [], d, d.text_top_pt, d.text_foot_pt)
                for pg in pages_order}
    # The chapter size is the MEDIAN need, not the extreme: one unusually full page should not
    # shrink the other twenty-three. Pages tighter than that keep their own factor.
    vals = sorted(per_page.values()) or [1.0]
    chapter_fit = min(1.0, vals[len(vals) // 2])

    sheets = []
    for pg in pages_order:
        meta = page_meta.get(pg, {})
        folio = meta.get("printed")
        # THE RUNNING HEAD IS WHAT THAT PAGE PRINTS. NCERT alternates: the verso carries the
        # SUBJECT (`Biology`) and the recto the CHAPTER TITLE. The page record already holds
        # the measured string; passing the chapter title for every page printed
        # `THE LIVING WORLD` on the even pages, where the book prints `BIOLOGY`.
        head_text = meta.get("header") or running
        side = meta.get("page_side") or ("recto" if (folio or 1) % 2 else "verso")
        x0, y0, _x1, _y1 = d.text_box(side)
        # THE COLUMN STARTS WHERE THE PAGE STARTS IT.
        #
        # `text_box` gives the design's ORDINARY page: its top is where body text begins on a
        # page with a header band above it. An opener is not that page -- the book sets its
        # title block first and begins the prose far down the sheet -- so starting the column
        # at the ordinary top ran the opener's text straight up under its own title and
        # through the contents rail, which IS positioned at its measured place. The two
        # collided on screen.
        #
        # Every flowed node now carries a measured box, so the page can say where its own text
        # begins. Taking the top from the first measured node fixes the opener without a
        # special case, and leaves ordinary pages where they already were.
        _first = [b for n in (page_nodes.get(pg) or [])
                  for b in (n.get("boxes") or [])[:1]
                  if b.get("src") in ("measured", "a2l-agent") and b.get("bbox")
                  and n.get("kind") not in ("figure", "table")
                  and (n.get("column") or "").lower() not in ("side", "left", "rail", "margin")]
        if _first:
            _top = min(b["bbox"][1] for b in _first) * H
            # Trust it only when it is BELOW the design's top -- a measured box above the
            # band is furniture leaking in, and would pull the column off the page.
            if _top > y0:
                y0 = _top
        # THE CHAPTER-OPENING PAGE IS NOT A BODY PAGE. It prints a full-bleed panel and a QR
        # instead of the band-and-strip header, and its contents rail sits beside the title.
        # Both are already cut as assets; drawing them is what makes the first page look like
        # the book's first page rather than body text with no heading.
        art = (page_meta.get(pg) or {}).get("art") or []
        rail = (page_meta.get(pg) or {}).get("contents_rail") or []
        rail_html = "".join(
            f'<div class="toc-entry" style="left:{mm(r["bbox"][0]*W):.2f}mm;'
            f'top:{mm(r["bbox"][1]*H):.2f}mm;'
            f'width:{mm(max((r["bbox"][2]-r["bbox"][0])*W, 70)):.2f}mm">'
            f'{esc(r["text"])}</div>' for r in rail)
        art_html = "".join(
            f'<img class="art" src="{esc(a.get("url") or a["file"])}" alt="" '
            f'style="left:{mm(a["bbox"][0]*W):.2f}mm;top:{mm(a["bbox"][1]*H):.2f}mm;'
            f'width:{mm((a["bbox"][2]-a["bbox"][0])*W):.2f}mm;'
            f'height:{mm((a["bbox"][3]-a["bbox"][1])*H):.2f}mm">'
            for a in art)
        # FURNITURE A2L MEASURED, drawn when the book has no hand-measured design.
        #
        # `book_design.py` covers six designs. Every other book -- every scan, every subject
        # not yet measured -- rendered with no header band, no running head and no folio at
        # all, because nothing knew what they looked like. A2L measures them per page off the
        # image, so a page it has read can be drawn correctly without its book ever being
        # hand-measured. The design still wins where it exists: it was measured across whole
        # books and is steadier than a single page's read.
        # The design wins only when it actually describes THIS sheet. BIO12 has a measured
        # design -- for the 568.8 x 777.6pt printing. This chapter is an A4 scan of a
        # different physical book, so that design's bands and folio boxes are measured for a
        # sheet 2.8% narrower and 8% shorter and land in the wrong places. When the page's own
        # size disagrees with the design's trim, the page's own measurements are the truth.
        _sheet = (meta or {}).get("sheet_pt") or []
        _off_design = bool(_sheet) and (
            abs(_sheet[0] - d.trim_pt[0]) > 6 or abs(_sheet[1] - d.trim_pt[1]) > 6)
        a2l_furn = ""
        if _off_design or not design_lib.is_measured(doc["book_id"]):
            for f in (meta or {}).get("furniture") or []:
                bb = f.get("bbox") or []
                if len(bb) != 4 or bb[2] <= bb[0]:
                    continue
                # Same rule as the `art` list: a "band" covering a third of the sheet is a
                # page scan, and drawing it under live text prints the page twice.
                if (bb[2] - bb[0]) * (bb[3] - bb[1]) > 0.34:
                    continue
                kind_f = (f.get("kind") or "").replace("_", "-")
                st = (f'left:{mm(bb[0] * W):.2f}mm;top:{mm(bb[1] * H):.2f}mm;'
                      f'width:{mm((bb[2] - bb[0]) * W):.2f}mm;'
                      f'height:{mm((bb[3] - bb[1]) * H):.2f}mm')
                if f.get("fill"):
                    st += f';background:{f["fill"]}'
                if f.get("color"):
                    st += f';color:{f["color"]}'
                txt = esc(f.get("text") or "")
                a2l_furn += f'<div class="mfurn {esc(kind_f)}" style="{st}">{txt}</div>'

        # THE PAGE SAYS WHAT IT IS. See `page_kind` in build_chapter_json.
        kind = (meta or {}).get("page_kind") or (
            "chapter_opener" if any(a["kind"] == "header art" for a in art) else "ordinary")
        is_opener = kind in ("chapter_opener", "unit_opener")
        # A unit opener prints no running head and no folio; a chapter opener prints no
        # running head but the book does set its page number.
        # This page's own factor if it is tighter than the chapter's, so it is never clipped.
        _fit = min(chapter_fit, per_page.get(pg, 1.0))
        sheets.append(
            f'<section class="sheet {kind}{" opener" if is_opener else ""}" id="p{pg}" '
            f'style="--fit:{_fit}">'
            f'{a2l_furn}{art_html}{rail_html}'
            f'{"" if is_opener else furniture(side, folio, doc.get("reprint"), head_text)}'
            f'<div class="measure" style="margin-left:{mm(x0):.2f}mm;'
            f'padding-top:{mm(y0):.2f}mm">{"".join(buckets[pg])}</div>'
            f'{foot(doc.get("reprint"))}</section>')
    sheet = "".join(sheets)

    title = (f'{"New" if ed=="new" else "Old"} NCERT {d.name} — Chapter '
             f'{doc["chapter"]["number"]}: {doc["chapter"]["title"]}')
    bar = (f'<div class="bar"><b>{esc(d.name)}</b>'
           f'<span class="tag">{ed} NCERT</span>'
           f'<span class="tag">ch {doc["chapter"]["number"]}</span>'
           f'<span class="tag">{esc(doc["chapter"]["title"])}</span>'
           f'<span class="tag">reprint {esc(doc.get("reprint") or "?")}</span>'
           f'<span class="tag">{len(doc["pages"])} pages</span>{warn}'
           f'<span class="tag">rendered from chapter.json</span></div>')
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title)}</title><style>{fonts()}{css}</style></head>'
            f'<body>{bar}{sheet}</body></html>')


def fit_factor(nodes, d, top_pt, foot_pt):
    """How much the type must be scaled for this page's content to occupy the page's measure.

    Predicted from what was MEASURED, not from rendering: each text node knows how many printed
    lines it had and the pitch those lines were set at, so its printed height is
    `line_count x line_pitch`. A figure contributes the height of its own box. Summed against
    the height the page actually gives the text block, that is the ratio the type needs.

    Capped at 1.0 -- a page with room to spare is set at its proper size, never inflated.

    NOT floored. A floor does not make the content fit; it makes the overflow INVISIBLE,
    because the sheet is a fixed height with `overflow:hidden`. Measured on Class 11 ch01,
    nine pages of twenty-four need more room than the sheet gives -- page 4 of the new edition
    needs 142% -- so the 0.72 floor was clipping the bottom of every one of them, which is
    what "the text runs under the footer and stops mid-sentence" looks like. The factor now
    says what the content actually needs; `check_chapter.py` FAILS the build when that is
    below 0.72, which is the honest response: a page needing that much shrink is a page whose
    content was assigned wrongly, and hiding it does not fix it.
    """
    avail = foot_pt - top_pt
    if avail <= 0:
        return 1.0
    used = 0.0
    for n in nodes:
        if n.get("kind") in ("figure", "table"):
            bx0 = (n.get("boxes") or [{}])[0]
            bx = bx0.get("bbox")
            # A figure placed at its measured position is OUT OF THE TEXT FLOW -- it occupies
            # the margin or sits beside the prose, exactly as the book sets it, and counting
            # its height against the text column reports an overflow that does not exist.
            # Page 13 of Class 11 ch01 is two side-by-side crops of one 2x2 figure: counted in
            # flow they read as two full-height blocks stacked, and the page "needed" 71%.
            if bx and bx0.get("src") in ("measured", "a2l-agent") and bx[2] > bx[0]:
                continue
            used += (bx[3] - bx[1]) * d.trim_pt[1] if bx else 60.0
            continue
        # A NOTE IN THE SIDE RAIL is out of the text flow too. BIO12L ch03 p046 prints the MTP
        # Act (45 lines) in the left rail beside the prose; summed into the column it "needed"
        # 65% and failed PAGE_OVERFLOW on a page that fits as printed.
        bx0 = (n.get("boxes") or [{}])[0]
        if (n.get("column") == "side" and bx0.get("src") in ("measured", "a2l-agent")
                and (bx0.get("bbox") or [0, 0, 0, 0])[2] - (bx0.get("bbox") or [0, 0, 0, 0])[0]
                < 0.35):
            continue
        lines = n.get("line_count")
        pitch = n.get("line_pitch_pt") or d.body_pt * d.leading
        if not lines:
            body = n.get("body") or n.get("title") or ""
            # ~62 characters to a line at this book's measure, measured off its own pages.
            lines = max(1, round(len(body) / 62))
        used += lines * pitch + 2.0
    if used <= avail:
        return 1.0
    return round(avail / used, 3)


def _figure_placement(node, d):
    """(css class, width in mm) -- which side of the measure this figure is printed on.

    Read off the measured bbox, not guessed. The book sets a diagram either across the full
    measure or in the outer rail with the prose running beside it; the bbox says which, so the
    render reproduces the arrangement instead of stacking everything down the middle.
    """
    mm = design_lib.pt_to_mm
    W = d.trim_pt[0]
    box = (node.get("boxes") or [{}])[0].get("bbox")
    measure_mm = mm(d.measure_pt)
    # A2L DECIDED THE COLUMNS; the bbox heuristic below is only the fallback for pages the
    # layout agent has not read. The agent is asked to settle the page's columns first and
    # then place elements in them, which is exactly the judgement a bbox cluster stands in for
    # -- and gets wrong: on BIO11L ch02 the heuristic produced 9 right-rail figures, 1 left and
    # 0 full-width, on a chapter that prints several across the full measure.
    col = node.get("column")
    if node.get("layout_source") == "a2l-agent" and col in ("full", "left", "right"):
        if col == "full":
            return "full", measure_mm
        w = measure_mm * 0.46
        if box:
            w = min(mm(max(box[2] * W - box[0] * W, 20.0)), measure_mm * 0.55)
        return ("rail-left" if col == "left" else "rail-right"), w
    if not box:
        return "full", measure_mm
    x0, x1 = box[0] * W, box[2] * W
    w = mm(max(x1 - x0, 20.0))
    if w >= 0.72 * measure_mm:
        return "full", min(w, measure_mm)
    # Narrower than three-quarters of the measure: a marginal figure. Which rail it sits in is
    # decided by the side of the measure its box leans to.
    page = (node.get("pages") or [None])[0]
    side = "recto" if (page or 1) % 2 else "verso"
    mx0, _, mx1, _ = d.text_box(side)
    centre = (x0 + x1) / 2.0
    lean_left = centre < (mx0 + mx1) / 2.0
    return ("rail-left" if lean_left else "rail-right"), min(w, 0.55 * measure_mm)


def write(doc, chapter_dir):
    out = os.path.join(chapter_dir, "chapter.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(render(doc))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter_json")
    a = ap.parse_args()
    with open(a.chapter_json, encoding="utf-8") as fh:
        doc = json.load(fh)
    print(write(doc, os.path.dirname(a.chapter_json)))


if __name__ == "__main__":
    main()
