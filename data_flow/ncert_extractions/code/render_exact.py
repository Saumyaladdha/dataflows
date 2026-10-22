#!/usr/bin/env python3
"""Render a chapter EXACTLY as the book sets it: one positioned block per measured box.

    python code/render_exact.py BIO11L-ch01      -> .../chapter-exact.html

WHY THERE ARE TWO RENDERERS
---------------------------
`render_from_tree.py` reflows the semantic tree into a page. It is the right renderer for
reading, search, translation and a PYQ citing "1.2.1 Species, paragraph 2" -- and it can never
be pixel-exact, because reflow depends on the reader's font metrics, which are not the book's.

This renderer does the opposite and makes no attempt to be semantic. Every node is drawn at the
coordinates the book printed it at, absolutely positioned, with no flow at all. Nothing can
drift, overlap, overflow or move to another page, because nothing is being laid out -- it is
being PLACED.

Two external reviews of this pipeline, on two different chapters, reached the same conclusion
independently:

    Keep two linked representations: a semantic chapter tree for reading and search, and a
    page-layout representation for PDF-faithful rendering. The current HTML tries to recover
    the second from the first after the layout information has been discarded.

That is what this file is. The two renders come from ONE chapter.json and stay in step, because
the boxes and the `char_ranges` that place things here are the same ones the tree carries.

WHAT IT WILL NOT DO
-------------------
It refuses to place a box whose `src` is `estimated`. An estimated box is a reading-order guess
-- 0.10-0.90 wide, evenly subdivided -- and placing it confidently would put content in a
precise, wrong position, which is worse than not placing it. Chapters built from scans with no
a2l-layout-reader read therefore render nothing here, and say so.
"""

import argparse
import glob
import html as html_mod
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import book_design as design_lib   # noqa: E402

PT_MM = 25.4 / 72.0


def esc(s):
    return html_mod.escape(s or "", quote=True)


def marked(body, marks):
    """The body with its character-offset marks as real tags."""
    if not marks:
        return esc(body)
    cuts = sorted({0, len(body)} | {m["from"] for m in marks} | {m["to"] for m in marks})
    out = []
    for a, b in zip(cuts, cuts[1:]):
        if b <= a:
            continue
        here = [m for m in marks if m["from"] <= a and m["to"] >= b]
        piece = esc(body[a:b])
        for m in here:
            if m.get("sub"):
                piece = f"<sub>{piece}</sub>"
            if m.get("sup"):
                piece = f"<sup>{piece}</sup>"
            if m.get("i"):
                piece = f"<i>{piece}</i>"
            if m.get("b"):
                piece = f"<b>{piece}</b>"
            if m.get("sc"):
                piece = f'<span class="sc">{piece}</span>'
        out.append(piece)
    return "".join(out)


def _walk(nodes):
    for n in nodes:
        yield n
        if n.get("children"):
            yield from _walk(n["children"])


def render(doc, chapter_dir):
    d = design_lib.design_for(doc["book_id"])
    pages = doc.get("pages") or []
    sp = next((p.get("sheet_pt") for p in pages if p.get("sheet_pt")), [612.0, 784.0])
    W_pt, H_pt = float(sp[0]), float(sp[1])
    W, H = W_pt * PT_MM, H_pt * PT_MM

    # Bucket every PLACEABLE fragment by the page file it printed on.
    #
    # ONE BOX, ONE FRAGMENT. Getting this wrong is what made the first version of this file
    # worse than the reflowed render, not better: a node with four boxes had its WHOLE body
    # drawn into each of them (the four nomenclature rules appeared four times over), and a
    # paragraph split across two pages was drawn complete on both. Absolute positioning does
    # not forgive duplication the way a flow does -- it stacks it in place.
    folio_to_file = {p.get("printed"): p.get("page_file")
                     for p in pages if p.get("printed") is not None}

    def _pf_for_folio(folio):
        """The page FILE for a printed folio.

        A box records whichever of the two it has. The nomenclature list's fourth rule carries
        `page: 5` and no `page_file`, so resolving only on `page_file` fell through to the
        node's own page and printed rule 4 on page 4, on top of that page's opening
        continuation. Both routes must be tried before a box is attributed.
        """
        return folio_to_file.get(folio)

    def fragments(n):
        """[(bbox, page_file, text, marks)] -- what this node printed, box by box."""
        boxes = [b for b in (n.get("boxes") or [])
                 if b.get("bbox") and len(b["bbox"]) == 4 and b.get("src") != "estimated"]
        if not boxes:
            return []
        body = n.get("body") or n.get("title") or n.get("caption") or ""
        if n.get("kind") == "section":
            body = " ".join(x for x in (n.get("number"), n.get("title")) if x)
        marks = n.get("marks") or []

        # A LIST PRINTS ONE ITEM PER BOX. Four boxes and four items is not a coincidence --
        # the extractor measured each rule where the book set it.
        items = n.get("items") or []
        # Rule 4 of the nomenclature list prints on the NEXT page. Each item carries its own
        # measured box with its own `page_file`, so the item is bucketed by that -- not by
        # the node's first box, which put all four rules on page 4 and left page 5 empty.
        if n.get("kind") == "list" and len(items) == len(boxes):
            return [(b["bbox"], b.get("page_file") or _pf_for_folio(b.get("page")),
                     (("%s. " % it["number"]) if it.get("number") else "")
                     + (it.get("body") or ""), it.get("marks") or [])
                    for b, it in zip(boxes, items)]

        # A PARAGRAPH BROKEN ACROSS PAGES prints its own characters in each box.
        rngs = [r for r in (n.get("char_ranges") or [])
                if r.get("to", 0) > r.get("from", 0)]
        if len(boxes) > 1 and len(rngs) == len(boxes):
            out = []
            for b, r in zip(boxes, rngs):
                a, z = r["from"], min(r["to"], len(body))
                frag = body[a:z]
                if not frag.strip():
                    continue
                fm = [{**m, "from": max(m["from"], a) - a, "to": min(m["to"], z) - a}
                      for m in marks if min(m["to"], z) > max(m["from"], a)]
                out.append((b["bbox"],
                            b.get("page_file") or r.get("page_file")
                            or _pf_for_folio(b.get("page")), frag, fm))
            return out

        # Anything else prints ONCE, at its first measured box. Drawing it at every box is
        # how the duplication happened; a box we cannot attribute text to is better left
        # empty than filled with a copy.
        return [(boxes[0]["bbox"],
                 boxes[0].get("page_file") or _pf_for_folio(boxes[0].get("page")),
                 body, marks)]

    by_page, skipped = {}, 0
    for n in _walk(doc["tree"]):
        frags = fragments(n)
        if not frags:
            skipped += len([b for b in (n.get("boxes") or []) if b.get("bbox")])
            continue
        for bb, pf, text, marks in frags:
            if pf is None:
                pf = next((p["page_file"] for p in pages
                           if p.get("printed") == (n.get("pages") or [None])[0]), None)
            if pf is None:
                skipped += 1
                continue
            by_page.setdefault(pf, []).append((n, bb, text, marks))

    # SEVERAL NODES SHARING ONE BOX FLOW INSIDE IT. They are not sliced.
    #
    # The ten exercises are children of one `exercises` node and inherit its single measured
    # box, so absolute positioning stacked all ten at the same coordinates. Slicing that box
    # into ten shares by estimated text length was the first attempt and it was still wrong:
    # the estimate cannot know that question 7 carries three option rows and question 9 five
    # terms, so those questions ran past their slice and over the ones below -- the same
    # overlap, now harder to see.
    #
    # A measurement we do not have cannot be invented. What we DO know is the region the book
    # gave the whole group. So the group is positioned once, at that region, and its members
    # flow inside it in reading order -- which is what the book does within that region too.
    # Flow is the correct tool here precisely because the sub-positions were never measured.
    grouped = {}
    for pf, items in by_page.items():
        keyed, order = {}, []
        for n, bb, text, marks in items:
            k = tuple(round(v, 4) for v in bb)
            if k not in keyed:
                keyed[k] = []
                order.append(k)
            keyed[k].append((n, bb, text, marks))
        grouped[pf] = [(k, keyed[k]) for k in order]

    sheets = []
    for p in pages:
        pf = p.get("page_file")
        items = by_page.get(pf, [])
        art = "".join(
            f'<img class="art" src="{esc(a.get("url") or a["file"])}" '
            f'style="left:{a["bbox"][0] * W:.2f}mm;top:{a["bbox"][1] * H:.2f}mm;'
            f'width:{(a["bbox"][2] - a["bbox"][0]) * W:.2f}mm;'
            f'height:{(a["bbox"][3] - a["bbox"][1]) * H:.2f}mm">'
            for a in (p.get("art") or []))
        rail = "".join(
            f'<div class="blk rail" style="left:{r["bbox"][0] * W:.2f}mm;'
            f'top:{r["bbox"][1] * H:.2f}mm;'
            f'width:{max((r["bbox"][2] - r["bbox"][0]) * W, 28):.2f}mm">{esc(r["text"])}</div>'
            for r in (p.get("contents_rail") or []))

        blocks = []
        for _box_key, members in grouped.get(pf, []):
          shared = len(members) > 1
          inner = []
          for n, bb, body, marks in members:
            kind = n.get("kind")
            w_mm = max((bb[2] - bb[0]) * W, 4.0)
            style = f'left:{bb[0] * W:.2f}mm;top:{bb[1] * H:.2f}mm;width:{w_mm:.2f}mm'
            # SET THE TYPE TO THE LINES THE BOOK GAVE IT. The block's printed height is
            # `line_count x line_pitch_pt`, both measured off the page, so the fragment
            # occupies the rectangle it occupied in the book. That is the one thing a
            # reflowed render can never guarantee, because reflow depends on the reader's
            # font metrics rather than the book's.
            if n.get("line_pitch_pt"):
                style += f';line-height:{float(n["line_pitch_pt"]):.2f}pt'
            # THE TYPE MUST FIT THE BOX IT WAS MEASURED IN.
            #
            # A title given a flat 24pt inside a box measured for the book's own setting wraps
            # to three lines and spills downward over whatever is positioned beneath it --
            # which is how "CHAPTER 1 / THE LIVING WORLD" came to sit on top of the opening
            # paragraph, and "UNIT 1" on top of its own subtitle. Absolute positioning gives
            # a block no room to push its neighbours away; it simply overlaps them.
            #
            # The box height and the printed line count are both measured, so the size that
            # fits is arithmetic: one line gets the box's height divided by the leading.
            # This is the same reasoning as `fit_factor`, applied per block instead of per
            # page, and it means a heading can never overlap the text under it.
            box_h_pt = (bb[3] - bb[1]) * H_pt
            lines = int(n.get("line_count") or 0) or 1
            fitted = (box_h_pt / lines) / 1.21 if box_h_pt > 0 else 0
            if kind in ("chapter_title", "section", "summary", "exercises") and fitted >= 6:
                style += f';font-size:{min(fitted, 40.0):.2f}pt'
            elif n.get("size_pt"):
                style += f';font-size:{float(n["size_pt"]):.2f}pt'
            elif n.get("size_rel") and abs(float(n["size_rel"]) - 1.0) > 0.02:
                # 1.000em is not a size, it is noise that overrides the stylesheet with the
                # value the stylesheet already has.
                style += f';font-size:{float(n["size_rel"]):.3f}em'
            if n.get("text_color"):
                style += f';color:{n["text_color"]}'
            # A FILL IS A TINT BEHIND THE TYPE, NEVER THE TYPE'S OWN INK.
            # `fill` is measured per node and on this corpus it is frequently #000000 -- the
            # ink, not a panel. Painting it as a background put seven black rectangles behind
            # black text, erasing the chapter title and both figure captions. Only a LIGHT
            # tint can be a background, so anything dark is ignored.
            fill = n.get("layout_fill") or n.get("fill")
            if isinstance(fill, str) and re.fullmatch(r"#[0-9a-fA-F]{6}", fill or ""):
                r_, g_, b_ = (int(fill[i:i + 2], 16) for i in (1, 3, 5))
                if (r_ * 299 + g_ * 587 + b_ * 114) / 1000 >= 160:
                    style += f';background:{fill}'
            if (n.get("align") or "") in ("center", "right", "justify"):
                style += f';text-align:{n["align"]}'

            if kind == "figure" and (n.get("image") or n.get("image_local")):
                src = n.get("image") or n.get("image_local")
                h_mm = (bb[3] - bb[1]) * H
                blocks.append(
                    f'<figure class="blk fig" style="{style};height:{h_mm:.2f}mm">'
                    f'<img src="{esc(src)}" alt="{esc(n.get("caption") or "")}">'
                    f'</figure>')
                continue
            if kind == "table" and n.get("table_grid"):
                # THE GRID, NOT A RUN-ON SENTENCE. Flattening the cells into one block loses
                # every row and column relationship -- which in a taxonomy table IS the
                # content: it is what says Panthera belongs to Felidae.
                g = n["table_grid"]
                rows = g["cells"]
                head = rows[0] if rows else []
                t = [f'<table class="blk grid" style="{style}">',
                     "<thead><tr>" + "".join(f"<th>{esc(c)}</th>" for c in head)
                     + "</tr></thead><tbody>"]
                for r in rows[1:]:
                    t.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>")
                t.append("</tbody></table>")
                blocks.append("".join(t))
                continue
            if not (body or "").strip():
                continue
            cls = {"section": "h", "chapter_title": "ct", "question": "q",
                   "figure": "cap", "table": "cap", "summary": "h",
                   "exercises": "h"}.get(kind, "p")
            num = (n.get("number") or "").strip() if kind == "question" else ""
            lead = f'<span class="qn">{esc(num)}.</span> ' if num else ""
            # A QUESTION'S SUB-PARTS ARE ITS CONTENT, not decoration.
            # Moving them into `parts` made the Markdown correct and silently emptied this
            # render: question 7 lost all three sequences to compare and question 9 lost all
            # five terms to define, leaving two questions that cannot be answered. Anything
            # that moves content must be followed into every consumer of that content.
            subs = "".join(
                f'<div class="qsub">{marked(sp.get("body", ""), sp.get("marks") or [])}</div>'
                for sp in (n.get("parts") or []) if (sp.get("body") or "").strip())
            if shared:
                # inside a shared container: static, so they stack in reading order
                inner.append(f'<div class="grp {cls}">{lead}'
                             f'{marked(body, marks)}{subs}</div>')
            else:
                blocks.append(f'<div class="blk {cls}" style="{style}">'
                              f'{lead}{marked(body, marks)}{subs}</div>')
          if shared and inner:
            bb0 = members[0][1]
            blocks.append(
                f'<div class="blk grpbox" style="left:{bb0[0] * W:.2f}mm;'
                f'top:{bb0[1] * H:.2f}mm;width:{max((bb0[2] - bb0[0]) * W, 4.0):.2f}mm">'
                f'{"".join(inner)}</div>')

        # PAGE FURNITURE -- the header band, the running head, the folio and the imprint.
        #
        # These are deliberately NOT in the tree (they repeat on every page and are drawn from
        # the book's design, not written by NCERT as content), which is why they were absent
        # here: this renderer only placed tree nodes. But a page without its header band,
        # running head and folio does not look like the book, and this render exists for
        # exactly one reason -- to look like the book. They come from the design plus the page
        # record, which is where they have been all along.
        furn = ""
        kind_p = p.get("page_kind") or "ordinary"
        if kind_p == "ordinary":
            band = getattr(d, "header_band", None)
            strip = getattr(d, "header_strip", None)
            foot = getattr(d, "footer_band", None) or getattr(d, "foot_band", None)
            if band:
                furn += (f'<div class="furn band" style="left:0;top:{band["y0_pt"] * PT_MM:.2f}mm;'
                         f'width:{W:.2f}mm;height:{(band["y1_pt"] - band["y0_pt"]) * PT_MM:.2f}mm;'
                         f'background:{band["fill"]}"></div>')
            if strip:
                furn += (f'<div class="furn band" style="left:0;'
                         f'top:{strip["y0_pt"] * PT_MM:.2f}mm;width:{W:.2f}mm;'
                         f'height:{(strip["y1_pt"] - strip["y0_pt"]) * PT_MM:.2f}mm;'
                         f'background:{strip["fill"]}"></div>')
            if foot:
                furn += (f'<div class="furn band" style="left:0;'
                         f'top:{foot["y0_pt"] * PT_MM:.2f}mm;width:{W:.2f}mm;'
                         f'height:{(foot["y1_pt"] - foot["y0_pt"]) * PT_MM:.2f}mm;'
                         f'background:{foot["fill"]}"></div>')
            head = (p.get("header") or "").strip()
            if head:
                side = (p.get("page_side") or "recto").lower()
                hx = 17.0 if side == "recto" else W * 0.34
                furn += (f'<div class="furn rhead" style="left:{hx:.2f}mm;'
                         f'top:{(strip or {"y0_pt": 64}).get("y0_pt", 64) * PT_MM:.2f}mm">'
                         f'{esc(head)}</div>')
            fol = getattr(d, "folio", None)
            if fol and p.get("printed") is not None:
                fx = (fol.get("x_recto_pt") if (p.get("page_side") or "recto").lower()
                      == "recto" else fol.get("x_verso_pt")) or 0
                furn += (f'<div class="furn folio" style="left:{fx * PT_MM:.2f}mm;'
                         f'top:{fol.get("y0_pt", 50) * PT_MM:.2f}mm;'
                         f'width:{fol.get("w_pt", 35) * PT_MM:.2f}mm;'
                         f'height:{fol.get("h_pt", 36) * PT_MM:.2f}mm;'
                         f'background:{fol.get("fill", "#fff")};'
                         f'color:{fol.get("ink", "#231f20")}">{p["printed"]}</div>')
        imp = (p.get("footer") or doc.get("reprint") or "").strip()
        if imp:
            furn += (f'<div class="furn imprint" style="left:0;width:{W:.2f}mm;'
                     f'top:{H - 12:.2f}mm">{esc(imp)}</div>')
        sheets.append(
            f'<section class="sheet" id="x{pf}">{furn}{art}{rail}'
            f'{"".join(blocks)}</section>')

    css = f"""
*{{box-sizing:border-box}}
body{{margin:0;background:#8a8a8a;font-family:"TeX Gyre Bonum",Bookman,Georgia,serif;
     color:#231f20}}
.sheet{{position:relative;width:{W:.2f}mm;height:{H:.2f}mm;background:#fff;margin:6mm auto;
        overflow:hidden;box-shadow:0 1px 10px rgba(0,0,0,.45)}}
.blk{{position:absolute;margin:0;line-height:1.27;font-size:10.5pt;text-align:justify;
      hyphens:auto}}
.art{{position:absolute;z-index:0}}
.fig{{z-index:2}} .fig img{{width:100%;height:100%;object-fit:contain;display:block}}
.h{{font-weight:700;color:#00adef;text-align:left}}
.ct{{font-weight:700;color:#0073bd;text-align:left;line-height:1.08}}
.cap{{font-size:9pt;color:#6d6e71;text-align:left}}
.rail{{font-style:italic;font-size:8.6pt;color:#00adef;text-align:left}}
.sc{{font-variant:small-caps}}
/* Page furniture. These are NOT .blk, so they carry no positioning of their own -- without
   this rule their left/top are inert and the header bands join the normal flow instead of
   sitting at the top of the sheet. */
.furn{{position:absolute;margin:0}}
.furn.band{{z-index:0}}
.furn.rhead{{z-index:2;font-variant:small-caps;letter-spacing:.3pt;font-size:9.5pt;
            color:#231f20;white-space:nowrap}}
.furn.folio{{z-index:3;display:flex;align-items:center;justify-content:center;
            font-weight:700;font-size:13pt;border-radius:2mm 2mm 0 0}}
.furn.imprint{{z-index:2;text-align:center;font-size:8pt;color:#333}}
/* A question's sub-parts: their own lines, indented past the number. */
.qn{{font-weight:400}}
.qsub{{margin:.6mm 0 0 7mm;text-align:left}}
/* A group the book positioned as a whole: members flow inside, never stacked on top of
   each other. Used where the sub-positions were measured for the group but not per item. */
.blk.grpbox{{display:block}}
.grp{{position:static;margin:0 0 1.3mm;text-align:justify}}
.grp.h{{margin:2.4mm 0 1.2mm;text-align:center}}
/* The table: the book sets its cells smaller than the body, with light internal rules and
   the orange-toned ground it prints, not the dark borders a default table gets. */
table.grid{{border-collapse:collapse;font-size:9.5pt;line-height:1.22}}
table.grid th,table.grid td{{border:.4pt solid #f0c89a;padding:.5mm 1.2mm;
                            text-align:left;vertical-align:top}}
table.grid th{{font-weight:700;background:#fdd9b0}}
table.grid td{{background:#fef1e1}}
.bar{{position:sticky;top:0;z-index:9;background:#111;color:#eee;font:12px ui-monospace,
      monospace;padding:7px 12px;display:flex;gap:10px;flex-wrap:wrap}}
.tag{{background:#2a2a2a;padding:2px 7px;border-radius:3px}}
.warn{{background:#7a2a2a}}
@media print{{body{{background:#fff}}.bar{{display:none}}
  .sheet{{margin:0;box-shadow:none;break-after:page;page-break-after:always}}
  .sheet:last-of-type{{break-after:auto}}
  @page{{size:{W_pt:.2f}pt {H_pt:.2f}pt;margin:0}}}}
"""
    placed = sum(len(v) for v in by_page.values())
    warn = (f'<span class="tag warn">{skipped} box(es) NOT placed — estimated geometry</span>'
            if skipped else f'<span class="tag">every box measured</span>')
    bar = (f'<div class="bar"><b>{esc(doc["book_id"])}-ch'
           f'{doc["chapter"]["number"]:02d}</b>'
           f'<span class="tag">EXACT render — one positioned block per measured box</span>'
           f'<span class="tag">{len(pages)} sheets</span>'
           f'<span class="tag">{placed} boxes placed</span>{warn}'
           f'<span class="tag">{W_pt:.1f}×{H_pt:.1f}pt</span></div>')
    title = (f'{doc["book_id"]} ch{doc["chapter"]["number"]:02d} — '
             f'{doc["chapter"].get("title") or "untitled"} (exact)')
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title)}</title><style>{css}</style></head>'
            f'<body>{bar}{"".join(sheets)}</body></html>')


def write(doc, chapter_dir):
    out = os.path.join(chapter_dir, "chapter-exact.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(render(doc, chapter_dir))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapters", nargs="*")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    for p in sorted(glob.glob(os.path.join(ROOT, "data", "*_ncert", "class_*", "*", "*",
                                            "chapter.json"))):
        with open(p, encoding="utf-8") as fh:
            doc = json.load(fh)
        cid = f"{doc['book_id']}-ch{doc['chapter']['number']:02d}"
        if a.chapters and cid not in a.chapters:
            continue
        out = write(doc, os.path.dirname(p))
        print(f"{cid}: {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
