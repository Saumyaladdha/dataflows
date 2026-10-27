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


_SUB_CH, _SUP_CH = "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
_PLAIN = "0123456789+-=()"
_SUB_RUN = re.compile("[" + _SUB_CH + "]+")
_SUP_RUN = re.compile("[" + _SUP_CH + "]+")


def _scripts(html):
    """Unicode sub/superscript digits and combining under/overlines, set as real type.

    A floral formula is stored as the book prints it -- `K₍₅₎ C₍₅₎ A₅ G̲₍₂₎` -- and the
    body face has no glyphs for those characters, so a fallback font drew them at a different
    size and the line's fit shrank it into an unreadable smear (BIO11L ch05 p069). The text
    stays exactly as stored; only the page sets it with <sub>/<sup> and a drawn line.
    """
    html = _SUB_RUN.sub(lambda m: "<sub>" + m.group(0).translate(
        str.maketrans(_SUB_CH, _PLAIN)) + "</sub>", html)
    html = _SUP_RUN.sub(lambda m: "<sup>" + m.group(0).translate(
        str.maketrans(_SUP_CH, _PLAIN)) + "</sup>", html)
    html = re.sub("(.)[̲̱]", r'<u>\1</u>', html)
    html = re.sub("(.)[̅̄]",
                  r'<span style="text-decoration:overline">\1</span>', html)
    return html


def marked(body, marks, breaks=()):
    """The body with its character-offset marks as real tags, and a line break before each
    offset in `breaks` -- where the book started a new printed line."""
    breaks = {b for b in breaks if 0 < b < len(body)}
    if not marks and not breaks:
        return _scripts(esc(body))
    cuts = sorted({0, len(body)} | {m["from"] for m in marks} | {m["to"] for m in marks}
                  | breaks)
    out = []
    for a, b in zip(cuts, cuts[1:]):
        if b <= a:
            continue
        if a in breaks:
            out.append("<br>")
        here = [m for m in marks if m["from"] <= a and m["to"] >= b]
        piece = _scripts(esc(body[a:b]))
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
            # Coloured type (BIO12L ch05 p097 prints the inserted `B`, `BI`, `BIG` red).
            if re.fullmatch(r"#[0-9a-fA-F]{6}", str(m.get("color") or "")):
                piece = f'<span style="color:{m["color"]}">{piece}</span>'
        out.append(piece)
    return "".join(out)


def _walk(nodes):
    for n in nodes:
        yield n
        if n.get("children"):
            yield from _walk(n["children"])


# The faces NCERT prints with, mapped to what a browser can draw. The book's own fonts are not
# shipped, so each maps to its nearest metric family: AvantGarde (the unit openers) is a
# geometric sans; Bookman is the body serif the stylesheet already defaults to.
_SANS_FACES = ("AvantGarde", "CenturyGothic", "Century Gothic", "Gothic", "Futura")
# Single quotes: this goes inside a double-quoted style attribute, which a `"` would end early.
_SANS_STACK = "NcertDisplay,'URW Gothic','Century Gothic','Avant Garde Gothic',Futura,sans-serif"


def _cell(text, italics):
    """A table cell, with the fragments the page printed in italic set in italic."""
    out = esc(text)
    for frag in sorted(italics, key=len, reverse=True):
        e = esc(frag)
        if e in out and f"<i>{e}" not in out:
            out = out.replace(e, f"<i>{e}</i>")
    return out


def _join_items(items):
    """(text, marks) for list items joined one per line as `N. body`, marks re-based."""
    parts, marks, at = [], [], 0
    for it in items:
        lead = f'{it["number"]}. ' if it.get("number") else ""
        body = it.get("body") or ""
        for m in it.get("marks") or []:
            marks.append({**m, "from": m["from"] + at + len(lead),
                          "to": m["to"] + at + len(lead)})
        parts.append(lead + body)
        at += len(lead) + len(body) + 1
    return "\n".join(parts), marks


def _items_html(text, marks, pitch_mm=None, bullet=False, hang_mm=None):
    """Each `N. body` / `(i) body` / `(a) body` line as its own row with a hanging marker,
    marks sliced to the row. `pitch_mm`: the book's measured line pitch -- the stylesheet's 1.2mm
    gap under each row made BIO12L ch04 p010's three items 1.9mm deeper than their box, and the
    fit script shrank them to 8pt. `hang_mm`: where a bulleted row's text starts, measured from
    the bullet at the box's left edge (BIO11L ch12 p161: 18pt)."""
    css = [f"margin:0;line-height:{pitch_mm:.2f}mm"] if pitch_mm else []
    if bullet and hang_mm:
        css.append(f"padding-left:{hang_mm:.2f}mm")
    row_css = f' style="{";".join(css)}"' if css else ""
    ln_css = ' style="text-align:left"' if bullet and hang_mm else ""
    rows, at = [], 0
    for line in text.split("\n"):
        m = re.match(r"^(\d{1,2}\.|\((?:[ivx]+|[a-z])\))\s*", line)
        # a bulleted list (`marker` on the node, BIO11L ch10): the book's bullet hangs on each row
        lead = m.group(1) if m else ("●" if bullet else "")
        start = at + (len(m.group(0)) if m else 0)
        end = at + len(line)
        sub = [{**mk, "from": max(mk["from"], start) - start, "to": min(mk["to"], end) - start}
               for mk in marks if min(mk["to"], end) > max(mk["from"], start)]
        rows.append(f'<div class="li"{row_css}><span class="ln"{ln_css}>{esc(lead)}</span>'
                    f'{marked(text[start:end], sub)}</div>')
        at = end + 1
    return "".join(rows)


def _face(font):
    """CSS for a PDF font name -- family, weight and style -- or "" for the default body face."""
    if not font:
        return ""
    css = ""
    if any(k in font for k in _SANS_FACES):
        css += f";font-family:{_SANS_STACK}"
    elif any(k in font for k in ("Arial", "Helvetica")):
        css += ";font-family:Arial,Helvetica,sans-serif"
    css += ";font-weight:" + ("700" if re.search(r"Demi|Bold|Heavy|Black", font) else "400")
    if re.search(r"Italic|Oblique", font):
        css += ";font-style:italic"
    return css


# FIT EACH BLOCK TO THE HEIGHT THE BOOK PRINTED IT AT.
#
# Positions are measured; the type that fills them is not quite the book's. NCERT sets its body
# in Bookman Light, and no free font has its metrics: TeX Gyre Bonum (Bookman regular) and
# Georgia both set wider, so a paragraph the book prints on 2 lines took 3 and its last line
# printed over the next block -- `living or non-living?` on top of `Virus means venom` on BIO11L
# ch02 p020, and the same on most dense pages. An absolutely positioned block cannot push its
# neighbour down, so the only correct fix is for the block to take the room it was measured in.
#
# Each block carries `data-h`, its measured height. Once the fonts have loaded, a block taller
# than that is tightened in small steps -- word spacing first (the book's own tool), then
# letter-spacing, then size -- until it fits, with a floor so nothing becomes unreadable. Nothing moves; the
# type is only ever adjusted inside the box the book gave it.
_FIT_JS = """<script>
(function(){
  var MM = 96 / 25.4;
  function fit(el){
    var want = parseFloat(el.dataset.h) * MM + 1.5;
    if (!(want > 0) || el.offsetHeight <= want) return;
    var fs = parseFloat(getComputedStyle(el).fontSize), base = fs, ls = 0;
    // A GROUP OF QUESTIONS GIVES UP LEADING FIRST. Each question carries its own measured
    // pitch, and the gaps between questions are where a group overruns; closing word spacing
    // first ran `Mangifera Indica` together on BIO11L ch01 p009 while the leading stayed loose.
    if (el.classList.contains('grpbox')) {
      var k = 1.0;
      while (el.offsetHeight > want && k > 0.88) {
        k -= 0.01;
        el.querySelectorAll('.grp').forEach(function(g){
          if (!g.dataset.lh) g.dataset.lh = parseFloat(getComputedStyle(g).lineHeight);
          g.style.lineHeight = (g.dataset.lh * k) + 'px';
        });
      }
    }
    var ws = -0.7;
    while (el.offsetHeight > want && ws > -1.3) { ws -= 0.1; el.style.wordSpacing = ws + 'pt'; }
    while (el.offsetHeight > want && ls > -0.3) { ls -= 0.05; el.style.letterSpacing = ls + 'pt'; }
    while (el.offsetHeight > want && fs > base * 0.86) {
      fs -= base * 0.01; el.style.fontSize = fs + 'px';
      el.querySelectorAll('.grp').forEach(function(g){
        g.style.fontSize = (parseFloat(getComputedStyle(g).fontSize) * 0.99) + 'px';
      });
    }
  }
  // NO TEXT IS EVER CLIPPED. A placed line holds exactly the words the book printed on it,
  // in a font with the book's own widths; if a line still does not fit its box (a substitute
  // glyph, a symbol), it is tightened -- spacing, then size -- until every word shows. A line
  // running off the sheet and losing its last words is the one outcome this page must never
  // produce, so this runs on every placed line, whatever else the page does.
  function unclip(el){
    var ls = 0, fs = parseFloat(getComputedStyle(el).fontSize), base = fs;
    while (el.scrollWidth > el.clientWidth + 1 && ls > -0.6) { ls -= 0.05; el.style.letterSpacing = ls + 'pt'; }
    while (el.scrollWidth > el.clientWidth + 1 && fs > base * 0.75) { fs -= base * 0.01; el.style.fontSize = fs + 'px'; }
  }
  // A TABLE STAYS INSIDE THE WIDTH THE BOOK GAVE IT. The book fits Table 4.2's nine columns
  // (BIO11L ch04 p051) into its measure by hyphenating `Organi-sation` and `Segmen-tation`;
  // with no hyphenation dictionary the grid ran past the page edge and lost its last column.
  // Cell padding gives way first, then spacing, then size -- the same order as a line.
  function fitTable(el){
    var t = el.querySelector('table.grid');
    if (!t) return;
    // The grid gets the box's depth less its caption AS SET: a two-line caption (Table 9.1,
    // BIO11L ch09 p105) left a grid sized for one line, and the last row fell onto the footnote.
    var cap = el.querySelector('.tcap');
    if (el.dataset.boxh && t.style.height) {
      var room = parseFloat(el.dataset.boxh) * MM - (cap ? cap.offsetHeight + 8 : 0);
      if (room > 20) t.style.height = (room / MM) + 'mm';
    }
    var cells = t.querySelectorAll('th,td'), pad = 1.2, ls = 0;
    var fs = parseFloat(getComputedStyle(t).fontSize), base = fs;
    while (t.offsetWidth > el.clientWidth + 1 && pad > 0.5) {
      pad -= 0.1;
      cells.forEach(function(c){ c.style.paddingLeft = c.style.paddingRight = pad + 'mm'; });
    }
    while (t.offsetWidth > el.clientWidth + 1 && ls > -0.3) { ls -= 0.05; t.style.letterSpacing = ls + 'pt'; }
    while (t.offsetWidth > el.clientWidth + 1 && fs > base * 0.8) { fs -= base * 0.01; t.style.fontSize = fs + 'px'; }
    // ...and inside the DEPTH: narrower columns wrap more, and the grid then ran over the foot
    // (Table 9.1, BIO11L ch09 p105, over its own `* Adapted from` footnote). The book's rows are
    // tight: row padding and leading give way first, then the size.
    var want = parseFloat(t.style.height) * MM + 1.5;
    var vp = 0.5, lh = 1.2;
    while (want > 0 && t.offsetHeight > want && vp > 0.1) {
      vp -= 0.1;
      cells.forEach(function(c){ c.style.paddingTop = c.style.paddingBottom = vp + 'mm'; });
    }
    while (want > 0 && t.offsetHeight > want && lh > 1.02) { lh -= 0.03; t.style.lineHeight = lh; }
    while (want > 0 && t.offsetHeight > want && fs > base * 0.75) {
      fs -= base * 0.01; t.style.fontSize = fs + 'px';
    }
  }
  function run(){
    document.querySelectorAll('.blk.tbl').forEach(fitTable);
    document.querySelectorAll('[data-h]').forEach(fit);
    document.querySelectorAll('.blk.ln, .blk[style*="nowrap"]').forEach(unclip);
  }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(run); else run();
})();
</script>"""


# LaTeX that plain text cannot set: fractions, words above/below a formula, labelled arrows.
_TEX_NEEDED = re.compile(r"\\(?:frac|dfrac|overset|underset|stackrel|xrightarrow|xleftarrow|"
                         r"xrightleftharpoons|sqrt|longrightarrow|longleftarrow|quad|qquad)\b")
_KATEX = "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/"
_KATEX_HEAD = (f'<link rel="stylesheet" href="{_KATEX}katex.min.css">'
               f'<script src="{_KATEX}katex.min.js"></script>')
# Typeset BEFORE the fit script measures: a typeset equation is taller than its flat text.
# Text inside `\text{}` keeps the page's Bookman; the formula's letters take KaTeX's math face.
_KATEX_RUN = """<script>
(function(){
  if (!window.katex) return;
  document.querySelectorAll('.tex[data-tex]').forEach(function(el){
    try { katex.render(el.dataset.tex, el, {throwOnError: true, displayMode: false}); }
    catch (e) { /* the flat text stays */ }
  });
})();
</script>"""


def render(doc, chapter_dir):
    uses_tex = [False]

    def _qnodes(ns):
        for x in ns:
            yield x
            yield from _qnodes(x.get("children") or [])
    q_measure = [max([b["bbox"][2] - b["bbox"][0] for x in _qnodes(doc.get("tree") or [])
                      if x.get("kind") == "question" for b in x.get("boxes") or []
                      if b.get("bbox")] or [0.0])]
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
        # `SUMMARY` / `EXERCISES` in the case the page prints (BIO12L sets plain capitals),
        # carried as `printed_title`; the title stays true case for the data.
        if (n.get("kind") in ("summary", "exercises") and n.get("printed_title")
                and body.strip().lower() == n["printed_title"].strip().lower()):
            body = n["printed_title"]
        marks = n.get("marks") or []
        # A heading's own italic (`5.8.1 The *Lac* operon`), at its offset after the number.
        if n.get("kind") == "section" and n.get("title_marks"):
            off = len(body) - len(n.get("title") or "")
            marks = [{**m, "from": m["from"] + off, "to": m["to"] + off}
                     for m in n["title_marks"]]

        # A LIST PRINTS ONE ITEM PER BOX. Four boxes and four items is not a coincidence --
        # the extractor measured each rule where the book set it.
        items = n.get("items") or []
        # Rule 4 of the nomenclature list prints on the NEXT page. Each item carries its own
        # measured box with its own `page_file`, so the item is bucketed by that -- not by
        # the node's first box, which put all four rules on page 4 and left page 5 empty.
        if n.get("kind") == "list" and len(items) == len(boxes):
            # The `N. ` lead is prepended to the item's text, so its marks move right by the
            # lead's length -- unshifted, rule 4 printed `*of Mangifera ind*ica` (BIO11L ch01).
            out = []
            for b, it in zip(boxes, items):
                lead = ("%s. " % it["number"]) if it.get("number") else ""
                out.append((b["bbox"], b.get("page_file") or _pf_for_folio(b.get("page")),
                            lead + (it.get("body") or ""),
                            [{**m, "from": m["from"] + len(lead), "to": m["to"] + len(lead)}
                             for m in it.get("marks") or []]))
            return out

        # MORE ITEMS THAN BOXES: each box takes the items that fill the lines it was measured
        # to hold. BIO11L ch01's nomenclature rules are 4 items in 2 boxes -- rules 1-3 in a
        # 116pt box on p004 (8 lines at 14.1pt), rule 4 on p005 -- and printing the whole list
        # at the first box ran all four together as one paragraph and left p005 short a rule.
        # An item's lines are estimated from its length at the box's measure; the last box
        # always takes what remains, so no item can be lost, and `_FIT_JS` absorbs a small miss.
        # ONE BOX, SEVERAL POINTS: every item still prints on its own line, as the book sets
        # it. BIO11L ch02 p017's three steps -- `(i) Fusion of protoplasms ...`, `(ii) Fusion of
        # two nuclei ...`, `(iii) Meiosis ...` -- were joined into one run-on paragraph because
        # the list had a single measured box. The items are correct in the tree; only the
        # render joined them.
        if n.get("kind") == "list" and len(items) > 1 and len(boxes) == 1:
            b = boxes[0]
            return [(b["bbox"], b.get("page_file") or _pf_for_folio(b.get("page")),
                     *_join_items(items))]
        if (n.get("kind") == "list" and n.get("ordered") and len(boxes) > 1
                and len(items) > len(boxes)):
            pitch = float(n.get("line_pitch_pt") or 14.0)
            out, k = [], 0
            for bi, b in enumerate(boxes):
                bb = b["bbox"]
                cap_lines = (bb[3] - bb[1]) * H_pt / pitch + 0.6
                cpl = max(20.0, ((bb[2] - bb[0]) * W_pt - 24.0) / 5.0)
                take, used = [], 0.0
                while k < len(items):
                    need = max(1, -(-len(items[k].get("body") or "") // int(cpl)))
                    if take and bi < len(boxes) - 1 and used + need > cap_lines:
                        break
                    take.append(items[k]); used += need; k += 1
                if take:
                    out.append((bb, b.get("page_file") or _pf_for_folio(b.get("page")),
                                *_join_items(take)))
            return out

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

        # A QUESTION BUILT FROM A LIST'S ITEMS holds one box per printed line -- BIO12L ch02's
        # question 1 is `1. Fill in the blanks:` (0.18 of the page wide) and five full-width
        # parts. Set in its first box alone, every part wrapped a word a line and ran off the
        # sheet. It prints once, in the union of its boxes on its own page.
        pf0 = boxes[0].get("page_file") or _pf_for_folio(boxes[0].get("page"))
        if n.get("kind") == "question" and len(boxes) > 1:
            same = [b["bbox"] for b in boxes
                    if (b.get("page_file") or _pf_for_folio(b.get("page"))) == pf0]
            return [([min(x[0] for x in same), min(x[1] for x in same),
                      max(x[2] for x in same), max(x[3] for x in same)], pf0, body, marks)]

        # Anything else prints ONCE, at its first measured box. Drawing it at every box is
        # how the duplication happened; a box we cannot attribute text to is better left
        # empty than filled with a copy.
        return [(boxes[0]["bbox"],
                 boxes[0].get("page_file") or _pf_for_folio(boxes[0].get("page")),
                 body, marks)]

    def _caption_block(n, pf):
        """A figure's caption, set at its own measured box on this sheet -- or nothing."""
        cap = (n.get("caption") or "").strip()
        cb = n.get("caption_box") or {}
        bb = cb.get("bbox")
        if not cap or not bb or cb.get("src") == "estimated":
            return ""
        if (cb.get("page_file") or _pf_for_folio(cb.get("page"))) != pf:
            return ""
        get = lambda k: n.get(f"caption_{k}", n.get(k))          # noqa: E731
        style = (f'left:{bb[0] * W:.2f}mm;top:{bb[1] * H:.2f}mm;'
                 f'width:{max((bb[2] - bb[0]) * W, 4.0):.2f}mm')
        if get("print_size_pt"):
            style += f';font-size:{float(get("print_size_pt")):.2f}pt'
        if get("ink"):
            style += f';color:{get("ink")}'
        # Family and slant from the measured font, but NOT its weight: the most-printed run of a
        # caption is often the bold `Figure 1.1` label, which made the whole caption bold. The
        # label is bolded on its own below; the description is set regular, as the book does.
        style += re.sub(r";font-weight:\d+", "", _face(get("print_font"))) + ";font-weight:400"
        # The caption's own bold and italic as printed, at the book's own line breaks (a caption
        # set as a little table, like Figure 3.1's, keeps its rows). Without measured marks,
        # the `Figure n.m` label alone is bolded.
        cm = list(n.get("caption_marks") or [])
        m = re.match(r"^((?:Figure|Fig\.|TABLE|Table)\s*[\d.]+)", cap)
        if m and not any(mk.get("b") and mk["from"] == 0 for mk in cm):
            cm.append({"from": 0, "to": m.end(), "b": True})
        # AT THE BOOK'S OWN LINES, where measured: the turnover hangs under the text after the
        # label (Figure 6.2), or is centred (Figure 6.1), and full lines are justified -- set as
        # one block, every line began at the box edge (BIO12L ch06, every caption).
        if n.get("caption_line_geom"):
            return _line_blocks(n, cap, cm, n["caption_line_geom"], "cap", style)
        breaks = get("line_starts") or []
        if breaks:
            style += ";white-space:nowrap"
        return (f'<div class="blk cap" style="{style}">'
                f'{marked(cap, cm, breaks)}</div>')

    def _line_blocks(n, body, marks, geom, cls, style, ends=True):
        """One absolutely placed div per printed line (see `line_geom` in build_chapter_json)."""
        # The block's type (size, ink, face, spacing) without its box or its indent: each line
        # brings its own measured box, and the indent is already in the first line's x.
        # `min-width` too: a one-line block's width is a minimum, and left on each line it
        # stretched the unit rail's `Chapter 12` to the rail's full measure, justified.
        base = re.sub(r"(?:^|;)(?:left|top|width|min-width|text-indent|line-height|text-align):"
                      r"[^;]*", "", style).strip(";")
        out = []
        for k, g in enumerate(geom):
            a = g["from"]
            z = geom[k + 1]["from"] if k + 1 < len(geom) else len(body)
            seg = body[a:z].rstrip()
            lead_ws = len(seg) - len(seg.lstrip())
            seg, a = seg.lstrip(), a + lead_ws
            # The book hyphenated a word across the break; the body holds it whole.
            hyph = (g.get("hyphen") and seg and not seg.endswith("-")
                    and z < len(body) and body[z - 1].isalpha() and body[z].isalpha())
            sm = [{**m, "from": max(m["from"], a) - a, "to": min(m["to"], a + len(seg)) - a}
                  for m in marks if min(m["to"], a + len(seg)) > max(m["from"], a)]
            bb = g["bbox"]
            # Justified only where the book justified: a full-width line that is not the
            # paragraph's last. A piece of a multi-column row (a match table) is set ragged.
            last = (g.get("row") == geom[-1].get("row") if "row" in g else k == len(geom) - 1)
            # the last line before a page break is a full justified line: the sentence goes on
            last = (last and ends) or not g.get("solo", True)
            out.append(
                f'<div class="blk {cls} ln" style="{base};left:{bb[0] * W:.2f}mm;'
                f'top:{bb[1] * H:.2f}mm;width:{max((bb[2] - bb[0]) * W, 2.0):.2f}mm;'
                f'line-height:{max((bb[3] - bb[1]) * H, 1.0):.2f}mm;text-align:justify;'
                f'text-align-last:{"left" if last else "justify"}">'
                f'{marked(seg, sm)}{"-" if hyph else ""}</div>')
        return "".join(out)

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
        # A QUESTION'S PARTS CAN PRINT ON THE NEXT PAGE. BIO12L ch02's question 1 sets (a)-(e)
        # on p039 and (f)-(k) at the head of p040; each such part says where (`page_file`,
        # `region`). They are drawn there, unnumbered, and left off the question's own page.
        if n.get("kind") == "question":
            own = {pf for _bb, pf, _t, _m in frags}
            away = {}
            for sp in n.get("parts") or []:
                if sp.get("page_file") and sp["page_file"] not in own and sp.get("region"):
                    away.setdefault(sp["page_file"], []).append(sp)
            for pf2, sps in away.items():
                cont = {**n, "number": "", "body": "", "marks": [], "parts": sps,
                        "parts_inline": False, "_cont": True}
                by_page.setdefault(pf2, []).append((cont, list(sps[0]["region"]), "", []))
    # ...clipped to end above the first question of that page, which has its own box.
    for pf, items in by_page.items():
        for k, (n, bb, text, marks) in enumerate(items):
            if not n.get("_cont"):
                continue
            below = [b[1] for m, b, _t, _mk in items
                     if m.get("kind") == "question" and not m.get("_cont") and b[1] > bb[1]]
            if below:
                items[k] = (n, [bb[0], bb[1], bb[2], min(below) - 0.004], text, marks)

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
    #
    # Questions now carry their OWN measured boxes (`_finalise_for_consumers`), which is right
    # for the data. But placed one by one, each was fitted to its own box and the ones with
    # sub-parts were shrunk to fit (BIO11L ch01 Q5, Q7, Q9 printed small, Q7 crowding Q8). The
    # exercises still print as one group: the questions of one Exercises block on one page flow
    # together inside the union of their measured boxes, which is the region the book gave them.
    q_parent = {}

    def _mark_q(ns, parent=None):
        for x in ns or []:
            if x.get("kind") == "question" and parent is not None:
                q_parent[id(x)] = id(parent)
            _mark_q(x.get("children"), x)
    _mark_q(doc["tree"])
    grouped = {}
    for pf, items in by_page.items():
        keyed, order, unions = {}, [], {}
        for n, bb, text, marks in items:
            if id(n) in q_parent:
                k = ("questions", q_parent[id(n)])
                u = unions.get(k)
                unions[k] = bb if u is None else [min(u[0], bb[0]), min(u[1], bb[1]),
                                                  max(u[2], bb[2]), max(u[3], bb[3])]
            else:
                k = tuple(round(v, 4) for v in bb)
            if k not in keyed:
                keyed[k] = []
                order.append(k)
            keyed[k].append((n, bb, text, marks))
        for k, u in unions.items():
            keyed[k] = [(n, u, text, marks) for n, _bb, text, marks in keyed[k]]
        grouped[pf] = [(k, keyed[k]) for k in order]

    sheets = []
    for p in pages:
        pf = p.get("page_file")
        items = by_page.get(pf, [])
        # Page art carries an `alt` too: the QR code says what it is; the header band, page
        # ground and decor are decoration, so theirs is empty (screen readers skip them).
        def _art(a):
            alt = "QR code" if "qr" in (a.get("kind") or "").lower() else ""
            return (f'<img class="art" src="{esc(a.get("url") or a["file"])}" alt="{alt}" '
                    f'style="left:{a["bbox"][0] * W:.2f}mm;top:{a["bbox"][1] * H:.2f}mm;'
                    f'width:{(a["bbox"][2] - a["bbox"][0]) * W:.2f}mm;'
                    f'height:{(a["bbox"][3] - a["bbox"][1]) * H:.2f}mm">')

        fig_boxes = [bb for n_, bb, _t, _m in by_page.get(pf, []) if n_.get("kind") == "figure"]

        def _decor(dc):
            b = dc["bbox"]
            css = (f'left:{b[0] * W:.2f}mm;top:{b[1] * H:.2f}mm;'
                   f'width:{max((b[2] - b[0]) * W, 0.1):.2f}mm;'
                   f'height:{max((b[3] - b[1]) * H, 0.1):.2f}mm')
            if dc.get("fill"):
                css += f';background:{dc["fill"]}'
            if dc.get("stroke") and dc.get("width"):
                css += f';border:{dc["width"]:.2f}pt solid {dc["stroke"]}'
            if dc.get("radius"):
                css += f';border-radius:{dc["radius"]:.1f}pt'
            if dc.get("opacity"):
                css += f';opacity:{dc["opacity"]}'
            # A TAB AT THE TRIM COVERS THE CROP UNDER IT. Figure 3.4 (b)'s rectangle reaches
            # into the corner where p045's folio tab bleeds off the edge (BIO12L ch03), so the
            # crop carried part of the tab and its `4`, and drawn over the tab it printed `4 45`.
            # Edge decor overlapping a figure on this page sits above figures, under the text.
            edge = b[0] <= 0.005 or b[1] <= 0.005 or b[2] >= 0.995 or b[3] >= 0.995
            if edge and any(min(b[2], f[2]) > max(b[0], f[0]) and min(b[3], f[3]) > max(b[1], f[1])
                            for f in fig_boxes):
                return f'<div class="furn decor" style="{css};z-index:2"></div>'
            return f'<div class="furn decor" style="{css}"></div>'

        # THE PAGE'S OWN DECORATION, IN THE BOOK'S PAINT ORDER. Measured panels, bands, boxes
        # and rules (`pages[].decor`) and the page's art share one layer ordered by `z`, the
        # PDF's own sequence: the Class 12 opener paints its green panel OVER the header
        # picture's lower half, which is why the book shows no leaf there.
        decor = p.get("decor")
        if decor is not None:
            layer = sorted([(dc.get("z") if dc.get("z") is not None else -1, 1, _decor(dc))
                            for dc in decor] +
                           [(a.get("z") if a.get("z") is not None else -1, 0, _art(a))
                            for a in (p.get("art") or [])], key=lambda t: (t[0], t[1]))
            art = "".join(h for _z, _k, h in layer)
        else:
            art = "".join(_art(a) for a in (p.get("art") or []))

        def _rail(r):
            st = r.get("style") or {}
            if not r.get("items") or not st:
                return (f'<div class="blk rail" style="left:{r["bbox"][0] * W:.2f}mm;'
                        f'top:{r["bbox"][1] * H:.2f}mm;'
                        f'width:{max((r["bbox"][2] - r["bbox"][0]) * W, 28):.2f}mm">'
                        f'{esc(r["text"])}</div>')
            # As printed: each entry its own number, the title hung at the measured indent,
            # in the rail's measured face, size and colour.
            size = st.get("size") or 10.0
            ind = r.get("indent_pt")
            if ind:
                rows = "".join(
                    f'<div class="ri" style="padding-left:{ind:.1f}pt;text-indent:-{ind:.1f}pt">'
                    f'<span class="rn" style="width:{ind:.1f}pt">{esc(it.get("num") or "")}</span>'
                    f'{esc(it["title"])}</div>' for it in r["items"])
            else:
                # No measured indent (Class 11 sets each entry as one line, `2.1 Kingdom
                # Monera`): number and title inline, one space apart, as printed.
                rows = "".join(
                    f'<div class="ri">{esc(" ".join(x for x in (it.get("num"), it["title"]) if x))}'
                    f'</div>' for it in r["items"])
            return (f'<div class="blk railx" style="left:{r["bbox"][0] * W:.2f}mm;'
                    f'top:{r["bbox"][1] * H - size * 0.25 * PT_MM:.2f}mm;'
                    f'width:{(r["bbox"][2] - r["bbox"][0]) * W + 2:.2f}mm;font-size:{size}pt;'
                    f'line-height:{size * 1.4:.2f}pt;color:{st.get("color") or "#231f20"}'
                    f'{_face(st.get("font"))}">{rows}</div>')
        rail = "".join(_rail(r) for r in (p.get("contents_rail") or []))

        blocks = []
        for _box_key, members in grouped.get(pf, []):
          shared = len(members) > 1
          inner = []
          for n, bb, body, marks in members:
            kind = n.get("kind")
            # TEXT PRINTED INSIDE A FIGURE IS ALREADY IN ITS CROP. Figure 5.16's floral formula
            # (BIO11L ch05 p067) is a line of text under the diagram, inside the artwork box; the
            # crop shows it as printed, and setting it again as live text overprinted the two.
            # It stays in the JSON and the Markdown -- only the page does not draw it twice.
            # The crop is the artwork box plus its pad, so the test uses that region (0.008 of
            # the sheet); across every built chapter only that one formula line matches.
            crops = [[f[0] - 0.008, f[1] - 0.008, f[2] + 0.008, f[3] + 0.008] for f in fig_boxes]
            if kind == "para" and any(
                    min(bb[2], f[2]) > max(bb[0], f[0]) and min(bb[3], f[3]) > max(bb[1], f[1])
                    and (min(bb[2], f[2]) - max(bb[0], f[0])) * (min(bb[3], f[3]) - max(bb[1], f[1]))
                    >= 0.8 * (bb[2] - bb[0]) * (bb[3] - bb[1]) for f in crops):
                continue
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
            # A FRAGMENT OF A PARAGRAPH BROKEN ACROSS PAGES has its own number of lines.
            # `line_count` is the node's first box's -- BIO11L ch01's `... All` / `these,
            # based on ...` counted p007's 2 lines, so p008's 4-line half was fitted to a box
            # that runs only from the first line's top to the last glyph's foot, and its type
            # came out a size smaller than the page around it. The box spans (lines - 1)
            # pitches plus one line's glyphs, so the count follows from the measured pitch.
            pitch_pt = float(n.get("line_pitch_pt") or 0)
            if pitch_pt and body != (n.get("body") or "") and box_h_pt > pitch_pt:
                lines = max(1, round((box_h_pt - 0.75 * pitch_pt) / pitch_pt) + 1)
            fitted = (box_h_pt / lines) / 1.21 if box_h_pt > 0 else 0
            # THE PRINTED SIZE, WHEN THE TEXT LAYER MEASURED ONE, BEATS EVERY ESTIMATE.
            # The box-fitted size is a reconstruction from height; `print_size_pt` is what the
            # PDF says the book set. Fitting gave `Unit 1` a size that wrapped it.
            if n.get("print_size_pt"):
                style += f';font-size:{float(n["print_size_pt"]):.2f}pt'
            elif kind in ("chapter_title", "section", "summary", "exercises") and fitted >= 6:
                style += f';font-size:{min(fitted, 40.0):.2f}pt'
            elif n.get("size_pt"):
                style += f';font-size:{float(n["size_pt"]):.2f}pt'
            elif n.get("size_rel") and abs(float(n["size_rel"]) - 1.0) > 0.02:
                # 1.000em is not a size, it is noise that overrides the stylesheet with the
                # value the stylesheet already has.
                style += f';font-size:{float(n["size_rel"]):.3f}em'
            # THE PRINTED INK AND FACE, NOT A COLOUR CHOSEN BY KIND. The stylesheet painted
            # every title blue and every block Bookman; the unit opener prints near-black
            # AvantGarde. Measured ink wins; A2L's image-sampled colour is the fallback.
            if n.get("ink") or n.get("text_color"):
                style += f';color:{n.get("ink") or n["text_color"]}'
            style += _face(n.get("print_font"))
            # A face read off the FIRST run is not the block's face when the bold is a mark on
            # part of it: `Floral Formula:` is bold and the formula after it is not (BIO11L ch05
            # p069), but the whole line printed bold. The marks carry the bold; the block is set
            # regular when they cover less than nine-tenths of it.
            _bm = [m for m in (marks or []) if m.get("b")]
            if kind in ("para", "list", "question") and _bm and sum(
                    m["to"] - m["from"] for m in _bm) < 0.9 * len((body or "").strip()):
                style += ";font-weight:400"
            # Overprinted ("fake bold") type prints bold whatever its face's name says.
            if n.get("print_bold"):
                style += ";font-weight:700"
            # Small caps where the book set them -- a heading's title is true case now, and
            # its face is the node's `small_caps`, not capital letters in the text.
            if n.get("small_caps"):
                style += ";font-variant:small-caps"
            # A LINE THE BOOK SET AS ONE LINE STAYS ONE LINE. A substitute font is never quite
            # the book's width, and a one-line title that wraps prints its second line over
            # whatever is placed beneath it. Lines the book broke are broken at the same place.
            # Only for TITLES AND LABELS. A short justified paragraph also carries line starts,
            # but forcing its breaks would set it ragged-left; it flows in its measured box.
            breaks = n.get("line_starts") or []
            if kind in ("para", "list", "question") and len(body or "") > 60:
                breaks = []
            # Never on a table or figure: their `line_count` describes the caption line, and
            # inherited `nowrap` ran every table cell into its neighbour.
            # `line_count` must be MEASURED as 1 -- a node without one (an exercise question
            # cut from a larger block) is not a one-liner, and forbidding it to wrap ran
            # BIO11L ch03's exercises 2 and 4 off the right of the sheet.
            # A HEADING ONE LINE DEEP IS ONE LINE even unmeasured: `11.8 THE C4 PATHWAY` (BIO11L
            # ch11 p145) came with an agent box and no `line_count`, wrapped `PATHWAY` and set
            # it over the paragraph below.
            sz = float(n.get("print_size_pt") or 0) or 13.0
            one_line = n.get("line_count") == 1 or (
                kind == "section" and not n.get("line_count") and 0 < box_h_pt < 1.8 * sz)
            if (one_line or breaks) and kind not in ("table", "figure"):
                style += ";white-space:nowrap"
                if not n.get("align"):
                    style += ";text-align:left"
                # A one-line paragraph is never squeezed into a box the text layer measured
                # short: the floral formula's glyphs sit outside its extent (BIO11L ch05 p069),
                # and the fit shrank the whole line to fit 36mm. Its width is a minimum.
                if kind == "para":
                    style = style.replace(f"width:{w_mm:.2f}mm", f"min-width:{w_mm:.2f}mm", 1)
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
            # A paragraph's first-line indent, as measured on the page -- applied only to the
            # fragment that starts the paragraph, never to a page-break continuation.
            if n.get("first_indent_pt") and kind in ("para", "box") and (
                    not n.get("char_ranges") or body == (n.get("body") or "")[:len(body)]):
                style += f';text-indent:{float(n["first_indent_pt"]):.1f}pt'
            if (n.get("align") or "") in ("center", "right", "justify"):
                style += f';text-align:{n["align"]}'

            # A lettered figure is carried by its panels alone -- no combined image to fall back on.
            if kind == "figure" and (n.get("image") or n.get("image_local") or any(
                    q.get("image") or q.get("image_local") for q in n.get("panels") or [])):
                src = n.get("image") or n.get("image_local")
                h_mm = (bb[3] - bb[1]) * H
                panels = [q for q in n.get("panels") or []
                          if (q.get("image") or q.get("image_local")) and q.get("bbox")]
                if panels:
                    # Each panel at its OWN measured box, from its own file -- the page shows
                    # exactly what the book prints, and every picture is separately addressable.
                    num = f"Figure {n['number']}" if n.get("number") else "Figure"
                    for q in panels:
                        qb = q["bbox"]
                        blocks.append(
                            f'<figure class="blk fig" style="left:{qb[0] * W:.2f}mm;'
                            f'top:{qb[1] * H:.2f}mm;width:{(qb[2] - qb[0]) * W:.2f}mm;'
                            f'height:{(qb[3] - qb[1]) * H:.2f}mm">'
                            f'<img src="{esc(q.get("image") or q["image_local"])}" '
                            f'alt="{esc(num + " " + q["label"])}"></figure>')
                else:
                    # At the CROP's rect when it is known: the crop is the box plus a pad, and
                    # fitted into the box it shrank (BIO12L ch05 p084 Griffith diagram, 0.8x).
                    ib = n.get("image_bbox")
                    fstyle = (f"{style};height:{h_mm:.2f}mm" if not ib or n.get("page_file") != pf
                              else f"left:{ib[0] * W:.2f}mm;top:{ib[1] * H:.2f}mm;"
                                   f"width:{(ib[2] - ib[0]) * W:.2f}mm;"
                                   f"height:{(ib[3] - ib[1]) * H:.2f}mm")
                    blocks.append(
                        f'<figure class="blk fig" style="{fstyle}">'
                        f'<img src="{esc(src)}" alt="{esc(n.get("caption") or n.get("alt") or "")}">'
                        f'</figure>')
                # THE CAPTION IS PRINTED TEXT AND IS DRAWN AS TEXT, at its own measured box.
                # Only the artwork was being placed, so every figure lost its caption on the
                # page -- `Figure 1.1 Taxonomic categories ...` existed in the data and
                # nowhere on the sheet.
                blocks.append(_caption_block(n, pf))
                continue
            # A TABLE THE BOOK DRAWS is printed from its crop: rules, tints and outlined glyphs,
            # with no text layer to set a grid from (BIO12L ch05 Table 5.1, the genetic code).
            # The caption is live text at its own box; the crop is shown from under it.
            cb = (n.get("caption_box") or {}).get("bbox")
            ib = n.get("image_bbox") or bb
            if kind == "table" and n.get("grid_drawn") and cb and (
                    n.get("image") or n.get("image_local")):
                top = max(cb[3], ib[1])
                blocks.append(
                    f'<div class="blk fig" style="left:{ib[0] * W:.2f}mm;top:{top * H:.2f}mm;'
                    f'width:{(ib[2] - ib[0]) * W:.2f}mm;height:{(ib[3] - top) * H:.2f}mm;'
                    f'overflow:hidden"><img src="{esc(n.get("image") or n["image_local"])}" '
                    f'alt="{esc(n.get("caption") or "")}" style="position:absolute;left:0;'
                    f'top:{(ib[1] - top) * H:.2f}mm;width:100%;height:{(ib[3] - ib[1]) * H:.2f}mm;'
                    f'object-fit:fill"></div>')
                blocks.append(_caption_block(n, pf))
                continue
            if kind == "table" and n.get("table_grid"):
                # THE GRID, NOT A RUN-ON SENTENCE. Flattening the cells into one block loses
                # every row and column relationship -- which in a taxonomy table IS the
                # content: it is what says Panthera belongs to Felidae.
                g = n["table_grid"]
                rows = g["cells"]
                head = rows[0] if rows else []
                # The table's box starts at its `TABLE n.m` caption, so the caption is set
                # first and the grid under it -- drawing only the grid put the grid where the
                # caption prints and left the caption out entirely.
                cap = (n.get("caption") or "").strip()
                ital = n.get("cell_italics") or []
                t = [f'<div class="blk tbl" data-boxh="{(bb[3] - bb[1]) * H:.2f}" '
                     f'style="{style}">']
                if cap:
                    # with its marks: `Table 11.1` is set in small caps
                    cm = n.get("caption_marks") or []
                    t.append(f'<div class="tcap">{marked(cap, cm) if cm else esc(cap)}</div>')
                # A table the book prints with no tint (exercise 10's Column I / Column II) is
                # set plain: no ruled grid, no peach ground the page does not have.
                tinted = bool(n.get("table_fill") or n.get("table_header_fill"))
                # THE GRID FILLS THE DEPTH THE BOOK GAVE IT. The stylesheet's rows came out at
                # their minimum height, so Table 2.1 (BIO11L ch02 p011) ended 50mm above where
                # the book's does and left a hole before the next paragraph. A table's height
                # is spread over its rows and never clips: content taller than this still grows.
                ts = []
                if tinted:
                    grid_mm = (bb[3] - bb[1]) * H - (6.2 if cap else 0.0)
                    if grid_mm > 10:
                        ts.append(f"height:{grid_mm:.2f}mm")
                # THE CELLS IN THE SIZE THE BOOK PRINTED THEM. The stylesheet's 9pt set BIO11L
                # ch11 p145's `In | Out` table (10.5pt in the book) visibly small, and as a plain
                # grid at `width:auto` it huddled in the left of its own tinted box.
                if n.get("print_size_pt"):
                    ts.append(f"font-size:{float(n['print_size_pt']):.2f}pt")
                if not tinted and n.get("fill") and str(n["fill"]).lower() not in (
                        "#000000", "#231f20", "#ffffff"):
                    ts.append("width:100%")
                tstyle = f' style="{";".join(ts)}"' if ts else ""
                import join_agent_special

                def cell_html(ri, ci, c):
                    # A cell with sup/sub marks (`I<sup>A</sup>`) is set from its marks.
                    mk = join_agent_special.cell_marks(g, ri, ci, ital)
                    return marked(c, mk) if mk else _cell(c, ital)
                t.append(f'<table class="grid{"" if tinted else " plain"}"{tstyle}><thead><tr>'
                         + "".join(f"<th>{cell_html(0, ci, c)}</th>" for ci, c in enumerate(head))
                         + "</tr></thead><tbody>")
                for ri, r in enumerate(rows[1:], 1):
                    # A row holding text in its first cell only is a note set ACROSS the table
                    # (Table 4.3's `Can you tell which of these columns ...`, BIO12L ch04 p016):
                    # squeezed into column A it ran three lines deep, past the grid's box.
                    if len(r) > 1 and (r[0] or "").strip() and not any(
                            (c or "").strip() for c in r[1:]):
                        centre = (' style="text-align:center"' if len(r[0].strip()) > 40
                                  else "")
                        t.append(f'<tr><td colspan="{len(r)}"{centre}>'
                                 f'{cell_html(ri, 0, r[0])}</td></tr>')
                        continue
                    # A short cell is one printed line in the book: `Magnesium (Mg)` wrapped in
                    # Table 9.1 (BIO11L ch09 p105) and pushed the grid over its own footnote.
                    t.append("<tr>" + "".join(f"<td{' class=\"nw\"' if len(c or '') <= 16 else ''}>"
                                              f"{cell_html(ri, ci, c)}</td>"
                                              for ci, c in enumerate(r)) + "</tr>")
                t.append("</tbody></table></div>")
                blocks.append("".join(t))
                continue
            if not (body or "").strip() and not n.get("_cont"):
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
            sps = [sp for sp in (n.get("parts") or []) if (sp.get("body") or "").strip()
                   and sp.get("page_file") in (None, pf)]

            # `(a)` hangs: a wrapped sub-part line aligns under its text, as the book sets it.
            def hang(p_):
                return re.sub(r"^(\(\s?(?:[a-z]|[ivx]{1,4})\s?\))\s*",
                              r'<span class="ql">\1</span>', p_)
            first = next((i for i, sp in enumerate(sps) if sp.get("columns")), None)
            grid = ""
            if first is not None:
                # MATCH THE FOLLOWING: two aligned columns, as the book sets question 14
                # (BIO11L ch04 p054) -- not `(a) Operculum (i) Ctenophora` run together.
                head = sps[first - 2:first] if first >= 2 and not any(
                    sp.get("columns") for sp in sps[first - 2:first]) else []
                cells = [f'<div class="mh">{marked(sp.get("body", ""), sp.get("marks") or [])}'
                         f'</div>' for sp in head]
                # ...or ONE part `Column I Column II`, as the agent reads the header line
                # (BIO11L ch15-ch19): it printed as a loose line, not over its two columns.
                hm = (re.match(r"^\s*(Column\s+I)\s+(Column\s+II)\s*$",
                               sps[first - 1].get("body", ""), re.I)
                      if not head and first >= 1 and not sps[first - 1].get("columns")
                      else None)
                if hm:
                    head = [sps[first - 1]]
                    bold = any(mk.get("b") for mk in sps[first - 1].get("marks") or [])
                    cells = [f'<div class="mh">{"<b>%s</b>" % esc(g) if bold else esc(g)}</div>'
                             for g in hm.groups()]
                for sp in sps[first:]:
                    if sp.get("columns"):
                        cm = sp.get("column_marks") or [[], []]
                        cells += [f'<div class="mc">{hang(marked(sp["columns"][k], cm[k]))}</div>'
                                  for k in (0, 1)]
                grid = f'<div class="qsub qmatch">{"".join(cells)}</div>'
                taken = {id(sp) for sp in head} | {id(sp) for sp in sps if sp.get("columns")}
                sps = [sp for sp in sps if id(sp) not in taken]
            parts = [hang(marked(sp.get("body", ""), sp.get("marks") or [])) for sp in sps]
            # One printed line when the book set the parts on one line (`parts_inline`).
            subs = (f'<div class="qsub">{"&ensp; ".join(parts)}</div>' if n.get("parts_inline")
                    else "".join(f'<div class="qsub">{p_}</div>' for p_ in parts)) + grid
            if shared:
                # inside a shared container: static, so they stack in reading order -- each in
                # the size, pitch and ink the book printed it in, so the group takes the height
                # the book gave it instead of the stylesheet's default 10.5pt at 1.27.
                gs = ""
                if n.get("print_size_pt"):
                    gs += f'font-size:{float(n["print_size_pt"]):.2f}pt;'
                if n.get("line_pitch_pt"):
                    gs += f'line-height:{float(n["line_pitch_pt"]):.2f}pt;'
                if n.get("ink"):
                    gs += f'color:{n["ink"]};'
                gs += _face(n.get("print_font")).lstrip(";")
                # lines split from one labelled block are the book's consecutive lines
                if n.get("label_line"):
                    gs += ";margin:0"
                # The text hangs where the book hung it (`hang_pt`, measured), first line and
                # turnovers alike. With the stylesheet's 6.5mm column plus a justified word space,
                # BIO11L ch13's first lines started 3mm right of their own turnover lines.
                if lead and n.get("hang_pt"):
                    h = float(n["hang_pt"]) * PT_MM
                    gs += f";padding-left:{h:.2f}mm;text-indent:-{h:.2f}mm"
                    lead = f'<span class="qn" style="width:{h:.2f}mm">{esc(num)}.</span>'
                inner.append(f'<div class="grp {cls}" style="{gs}">{lead}'
                             f'{marked(body, marks)}{subs}</div>')
            else:
                # `data-h`: the height the book printed this block at, for `_FIT_JS`. Only on
                # prose that wraps -- a one-line title or label is held by `nowrap` instead.
                # The target is `line_count x pitch` when both are measured: that is the height
                # N lines occupy at that line-height. The box itself runs only from the first
                # line's top to the last glyph's foot -- about 4pt short -- and fitting to it
                # squeezed paragraphs that were already set on exactly the book's lines.
                fit = ""
                if cls in ("p", "q") and lines > 1 and not breaks and box_h_pt > 0:
                    pitch = float(n.get("line_pitch_pt") or 0)
                    want_pt = max(box_h_pt, lines * pitch) if pitch else box_h_pt * 1.06
                    fit = f' data-h="{want_pt * PT_MM:.2f}"'
                # LINE BY LINE, AT THE BOOK'S OWN BREAKS, where every printed line was measured
                # and matched (`line_geom`). Nothing is laid out: each line is placed in the box
                # it printed in, so a paragraph set around a figure keeps its shape and no
                # paragraph can run into the block below it. Fallback: the flowed block below.
                # AN EQUATION THE BOOK TYPESETS -- a stacked fraction, words set under formulas,
                # an arrow with its enzyme over it -- is typeset from its LaTeX. Printed as the
                # flat text, `rate = δP/δt` broke over two lines and the carbonic anhydrase
                # equilibrium lost its layout (BIO11L ch09 p113). The flat text stays inside the
                # span as the fallback when KaTeX cannot load.
                tex = n.get("latex") or ""
                # NCERT sets chemistry and enzyme schemes upright (`E + S   ES ⟶ EP`); a formula
                # that names no face of its own is set in roman, and a fraction keeps its italics.
                if tex and "\\frac" not in tex and not re.search(r"\\(?:text|mathrm|mathbf)", tex):
                    tex = "\\mathrm{" + tex + "}"
                # At the book's size: a displayed fraction, and names under a formula set as text
                # (`carbon dioxide` under CO₂ prints at body size, not KaTeX's script size).
                tex = "\\displaystyle " + tex.replace("\\underset{", "\\underset{\\textstyle ")
                if kind == "para" and _TEX_NEEDED.search(tex):
                    uses_tex[0] = True
                    blocks.append(f'<div class="blk {cls} eqtex"{fit} style="{style}">'
                                  f'<span class="tex" data-tex="{esc(tex)}">'
                                  f'{marked(body, marks)}</span></div>')
                    continue
                # A list in one box prints its items joined by newlines (`_join_items`), its body
                # by spaces -- same length, same offsets -- so the measured lines still apply.
                # Compared strictly, BIO12L ch07 p147's list was reflowed and ran over the Summary.
                geom = (n.get("line_geom")
                        if body.replace("\n", " ") == (n.get("body") or "").replace("\n", " ")
                        else None)
                ends = True
                # a page-break fragment carries its own lines (`frag_line_geom`)
                if not geom and n.get("frag_line_geom"):
                    whole = n.get("body") or ""
                    for r, fg in zip(n.get("char_ranges") or [], n["frag_line_geom"]):
                        if fg and body == whole[r["from"]:min(r["to"], len(whole))]:
                            geom, ends = fg, r["to"] >= len(whole.rstrip())
                            break
                if geom and not subs and not lead and not n.get("marker"):
                    blocks.append(_line_blocks(n, body, marks, geom, cls, style, ends))
                    continue
                # A numbered list fragment carries its items one per line (`_join_items`).
                # Rows at the book's line pitch: the box's depth over its measured printed lines
                # (an item may wrap -- p009's three items print on four lines).
                n_rows = (body or "").count("\n") + 1
                n_lines = n.get("line_count") or 0
                pitch_mm = (box_h_pt * PT_MM / n_lines
                            if box_h_pt > 0 and n_lines >= n_rows else None)
                # A BULLETED LIST KEEPS ITS LINE PITCH AND OPENS UP BETWEEN ITEMS. Each `•` sits on
                # a baseline of its own, so `line_count` counts the bullets as lines (13 for
                # BIO11L ch12 p161's 9 printed lines): depth over that set the rows 3.8mm apart
                # against the book's 5.2mm and left the foot of the box empty. The book sets
                # lines at `line_pitch_pt` and a few points more between items.
                if n.get("marker") and n.get("line_pitch_pt") and box_h_pt > 0:
                    pitch_mm = float(n["line_pitch_pt"]) * PT_MM
                    style += (f";min-height:{box_h_pt * PT_MM:.2f}mm;display:flex;"
                              "flex-direction:column;justify-content:space-between")
                # ...and ONE item hangs too: BIO12L ch05 p095's list fragment is item (ii) alone
                # (item (i) printed on p094), and set as plain text its turnover lines ran out
                # to the margin instead of under `The`.
                hang = n.get("first_indent_pt")
                content = (_items_html(body, marks, pitch_mm, bullet=bool(n.get("marker")),
                                       hang_mm=float(hang) * PT_MM if hang else None)
                           if kind == "list" and ("\n" in (body or "") or n.get("marker") or re.match(
                               r"^(\d{1,2}\.|\((?:[ivx]+|[a-z])\))\s", body or ""))
                           else marked(body, marks, breaks))
                blocks.append(f'<div class="blk {cls}"{fit} style="{style}">'
                              f'{lead}{content}{subs}</div>')
          if shared and inner:
            bb0 = members[0][1]
            # A PAGE OF QUESTIONS FILLS THE DEPTH THE BOOK GAVE IT. Flowed at the stylesheet's
            # spacing, BIO12L ch03 p050's twelve questions ended at y 0.59 where the book ends
            # them at 0.67, each one higher than printed. Spread over the measured region (a
            # MINIMUM height, so content that is taller still triggers the fit script's shrink).
            spread = ""
            right = bb0[2]
            if all(m[0].get("kind") == "question" for m in members):
                spread = (f";min-height:{(bb0[3] - bb0[1]) * H:.2f}mm;display:flex;"
                          f"flex-direction:column;justify-content:space-between")
                # SHORT QUESTIONS GET THE COLUMN'S WIDTH. A page of one-line questions has a box
                # only as wide as the longest of them, and the substitute face sets a touch wider
                # than Bookman: `What is the average cell cycle span for a mammalian cell?`
                # (BIO11L ch10 p129) wrapped `cell?` onto a line of its own and pushed 2-4 down.
                # The measure the book allows is the widest question it prints in this chapter
                # (its exercise column); a one-line question only gains room, and a justified
                # long one is never set wider than the book sets its own.
                right = max(bb0[2], min(bb0[0] + q_measure[0], 0.95))
            blocks.append(
                f'<div class="blk grpbox" data-h="{(bb0[3] - bb0[1]) * H:.2f}" '
                f'style="left:{bb0[0] * W:.2f}mm;'
                f'top:{bb0[1] * H:.2f}mm;width:{max((right - bb0[0]) * W, 4.0):.2f}mm{spread}">'
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
        measured = decor is not None
        if kind_p == "ordinary":
            # A page whose decoration was measured draws it from `decor` (above); the design's
            # band, strip, tab and foot bar are Class 11 measurements and only stand in for a
            # page that could not be measured.
            band = None if measured else getattr(d, "header_band", None)
            strip = None if measured else getattr(d, "header_strip", None)
            if band:
                furn += (f'<div class="furn band" style="left:0;top:{band["y0_pt"] * PT_MM:.2f}mm;'
                         f'width:{W:.2f}mm;height:{(band["y1_pt"] - band["y0_pt"]) * PT_MM:.2f}mm;'
                         f'background:{band["fill"]}"></div>')
            if strip:
                furn += (f'<div class="furn band" style="left:0;'
                         f'top:{strip["y0_pt"] * PT_MM:.2f}mm;width:{W:.2f}mm;'
                         f'height:{(strip["y1_pt"] - strip["y0_pt"]) * PT_MM:.2f}mm;'
                         f'background:{strip["fill"]}"></div>')
            head = (p.get("header") or "").strip()
            hst = p.get("header_style")
            if head and hst and p.get("header_bbox"):
                # The running head in the book's own type and place: BIO12L sets it in
                # AvantGarde-Demi 8pt grey #6d6f71, Class 11 in Bookman small caps.
                hb = p["header_bbox"]
                side = (p.get("page_side") or "recto").lower()
                furn += (f'<div class="furn rhead" style="left:{hb[0] * W:.2f}mm;'
                         f'top:{hb[1] * H:.2f}mm;width:{(hb[2] - hb[0]) * W:.2f}mm;'
                         f'font-size:{hst.get("size") or 9.5}pt;letter-spacing:0;'
                         f'line-height:{(hb[3] - hb[1]) * H:.2f}mm;'
                         f'color:{hst.get("color") or "#231f20"}{_face(hst.get("font"))};'
                         f'text-align:{"right" if side == "verso" else "left"}">'
                         f'{esc(head)}</div>')
            elif head:
                side = (p.get("page_side") or "recto").lower()
                top = (strip or {"y0_pt": 64}).get("y0_pt", 64) * PT_MM
                hb = p.get("header_bbox")
                if hb:
                    # The measured box, with the head at its outer end (see `header_bbox`).
                    furn += (f'<div class="furn rhead" style="left:{hb[0] * W:.2f}mm;'
                             f'top:{top:.2f}mm;width:{(hb[2] - hb[0]) * W:.2f}mm;'
                             f'text-align:{"right" if side == "verso" else "left"}">'
                             f'{esc(head)}</div>')
                else:
                    hx = 17.0 if side == "recto" else W * 0.34
                    furn += (f'<div class="furn rhead" style="left:{hx:.2f}mm;'
                             f'top:{top:.2f}mm">{esc(head)}</div>')
            fol = getattr(d, "folio", None)
            mf = p.get("folio")
            if measured and mf and p.get("printed") is not None:
                # The folio's figure at its measured box and type; its tab is in `decor`.
                fb, fst = mf["bbox"], mf.get("style") or {}
                furn += (f'<div class="furn folio" style="left:{fb[0] * W:.2f}mm;'
                         f'top:{fb[1] * H:.2f}mm;width:{(fb[2] - fb[0]) * W:.2f}mm;'
                         f'height:{(fb[3] - fb[1]) * H:.2f}mm;background:none;border-radius:0;'
                         f'font-size:{fst.get("size") or 13}pt;'
                         f'color:{fst.get("color") or "#231f20"}{_face(fst.get("font"))}">'
                         f'{p["printed"]}</div>')
            elif fol and p.get("printed") is not None and not measured:
                fx = (fol.get("x_recto_pt") if (p.get("page_side") or "recto").lower()
                      == "recto" else fol.get("x_verso_pt")) or 0
                furn += (f'<div class="furn folio" style="left:{fx * PT_MM:.2f}mm;'
                         f'top:{fol.get("y0_pt", 50) * PT_MM:.2f}mm;'
                         f'width:{fol.get("w_pt", 35) * PT_MM:.2f}mm;'
                         f'height:{fol.get("h_pt", 36) * PT_MM:.2f}mm;'
                         f'background:{fol.get("fill", "#fff")};'
                         f'color:{fol.get("ink", "#231f20")}">{p["printed"]}</div>')
        # THE GREEN FOOT BAR, on the opener as on every ordinary page. The design records it as
        # `footer_bar` (fill and top edge; it bleeds off the foot) and this looked only for
        # `footer_band` / `foot_band`, so no page ever drew it (BIO11L ch02: all 13 sheets).
        foot = (getattr(d, "footer_bar", None) or getattr(d, "footer_band", None)
                or getattr(d, "foot_band", None))
        if foot and kind_p in ("ordinary", "chapter_opener") and not measured:
            y0 = foot["y0_pt"] * PT_MM
            y1 = foot["y1_pt"] * PT_MM if foot.get("y1_pt") else H
            furn += (f'<div class="furn band" style="left:0;top:{y0:.2f}mm;width:{W:.2f}mm;'
                     f'height:{max(y1 - y0, 0.5):.2f}mm;background:{foot["fill"]}"></div>')
        imp = (p.get("footer") or doc.get("reprint") or "").strip()
        im_ = p.get("imprint") or {}
        if imp and im_.get("bbox"):
            # Where and in what type the book prints it (Class 12: Arial 8pt, black, y 0.971).
            st_ = im_.get("style") or {}
            ib = im_["bbox"]
            furn += (f'<div class="furn imprint" style="left:0;width:{W:.2f}mm;'
                     f'top:{ib[1] * H:.2f}mm;line-height:{max((ib[3] - ib[1]) * H, 1):.2f}mm;'
                     f'font-size:{st_.get("size") or 8}pt;color:{st_.get("color") or "#000"}'
                     f'{_face(st_.get("font"))}">{esc(imp)}</div>')
        elif imp:
            furn += (f'<div class="furn imprint" style="left:0;width:{W:.2f}mm;'
                     f'top:{H - 12:.2f}mm">{esc(imp)}</div>')
        sheets.append(
            f'<section class="sheet" id="x{pf}">{furn}{art}{rail}'
            f'{"".join(blocks)}</section>')

    # THE BOOK'S OWN TYPE METRICS. TeX Gyre Bonum is a Bookman clone and Adventor an
    # AvantGarde clone -- the faces NCERT sets in. Without them the page fell back to Georgia,
    # which sets wider: a paragraph the book prints on 2 lines took 3 and ran into the next.
    # Embedded, not linked, so the page stays one self-contained file.
    import render_from_tree
    css = render_from_tree.fonts() + f"""
*{{box-sizing:border-box}}
body{{margin:0;background:#8a8a8a;font-family:NcertBody,"TeX Gyre Bonum",Bookman,Georgia,serif;
     color:#231f20}}
.sheet{{position:relative;width:{W:.2f}mm;height:{H:.2f}mm;background:#fff;margin:6mm auto;
        overflow:hidden;box-shadow:0 1px 10px rgba(0,0,0,.45)}}
/* THE BOOK'S WORD SPACING. Bonum's glyphs match Bookman Light exactly (measured ratio 1.00), but
   its space is 3.36pt at 10.5pt and the book's justified lines set a median word gap of 2.64pt.
   Justification can only STRETCH a space, never shrink it, so at the font's own space every
   line held fewer words than the book's and paragraphs ran a line long. -0.7pt brings the
   natural space to the book's measured gap; justification then stretches from there. */
/* A typeset equation, centred in the box (and tint) the book gave it. */
.blk.eqtex{{display:flex;align-items:center;justify-content:center;text-align:center;
           line-height:1.2;white-space:nowrap}}
.blk.eqtex .katex{{font-size:1.05em}}
.blk{{position:absolute;margin:0;line-height:1.27;font-size:10.5pt;text-align:justify;
      hyphens:auto;word-spacing:-0.7pt}}
.art{{position:absolute;z-index:0}}
/* LIVE TEXT IS NEVER UNDER A PICTURE. The book wraps prose into a figure's space (BIO12L ch01
   p007: `... architecture -` ends inside Figure 1.5 (b)'s box); with figures above the text the
   crop hid the line's end. Crops clear any prose pixels (`cut_figures`), so text goes on top. */
.fig{{z-index:1}} .fig img{{width:100%;height:100%;object-fit:contain;display:block}}
.blk:not(.fig){{z-index:2}}
.h{{font-weight:700;color:#00adef;text-align:left}}
.ct{{font-weight:700;color:#0073bd;text-align:left;line-height:1.08}}
.cap{{font-size:9pt;color:#6d6e71;text-align:left}}
.rail{{font-style:italic;font-size:8.6pt;color:#00adef;text-align:left}}
.sc{{font-variant:small-caps}}
/* A superscript or subscript must not make its line taller. Browsers grow the line box to
   fit a raised `th`, which pushed the line holding `20<sup>th</sup>` down onto the line below
   it on the Ernst Mayr page. line-height:0 keeps every placed line at the book's own pitch. */
sup,sub{{line-height:0}}
/* Page furniture. These are NOT .blk, so they carry no positioning of their own -- without
   this rule their left/top are inert and the header bands join the normal flow instead of
   sitting at the top of the sheet. */
.furn{{position:absolute;margin:0}}
.furn.band{{z-index:0}}
.furn.decor{{z-index:0}}
.blk.railx{{text-align:left}} .railx .ri{{margin:0 0 .45em}}
.railx .rn{{display:inline-block;text-indent:0}}
.furn.rhead{{z-index:2;font-variant:small-caps;letter-spacing:.3pt;font-size:9.5pt;
            color:#231f20;white-space:nowrap}}
.furn.folio{{z-index:3;display:flex;align-items:center;justify-content:center;
            font-weight:700;font-size:13pt;border-radius:2mm 2mm 0 0}}
.furn.imprint{{z-index:2;text-align:center;font-size:8pt;color:#333}}
/* A question's sub-parts: their own lines, indented past the number. */
.qn{{font-weight:400}}
.qsub{{margin:.6mm 0 0 7mm;text-align:left}}
/* The label hangs outside a group too: a question alone on its page (BIO12L ch02 q1) printed
   `(a)Humans` with no gap, because only `.grp.q` gave the label its column. */
.qsub{{padding-left:7.2mm;text-indent:-7.2mm}}
.qsub .ql{{display:inline-block;width:7.2mm;text-indent:0}}
/* One printed line, placed: it never wraps; the book's own breaks are the only breaks. */
.blk.ln{{white-space:nowrap;hyphens:manual}}
/* A numbered list row: the number hangs in the margin, the text keeps its own measure. */
.li{{position:relative;padding-left:9mm;margin:0 0 1.2mm}} .li .ln{{position:absolute;left:0;width:7mm;text-align:right}}
/* A group the book positioned as a whole: members flow inside, never stacked on top of
   each other. Used where the sub-positions were measured for the group but not per item. */
.blk.grpbox{{display:block}}
.grp{{position:static;margin:0 0 1.3mm;text-align:justify}}
.grp.h{{margin:2.4mm 0 1.2mm;text-align:center}}
/* Questions sit on the book's own line pitch with only a hairline between them. */
/* The book hangs the question number in its own column and wraps the text under the text,
   not under the number; the sub-parts sit under the text. */
.grp.q{{margin:0;text-align:justify;padding-left:6.5mm;text-indent:-6.5mm;word-spacing:0}}
.grp.q .qn{{display:inline-block;width:6.5mm;text-indent:0}}
.grp.q .qsub{{margin:0 0 0 1.4mm;padding-left:7.2mm;text-indent:-7.2mm;text-align:left}}
.grp.q .qsub .ql{{display:inline-block;width:7.2mm;text-indent:0}}
/* Match the following: column I as wide as its widest entry, column II beside it. Set AFTER
   the question rules above, which would otherwise pin every label to 7.2mm and run `(viii)`
   into `Osteichthyes`. */
.qsub.qmatch,.grp.q .qsub.qmatch{{display:grid;grid-template-columns:max-content 1fr;
            column-gap:9mm;row-gap:.9mm;padding-left:0;text-indent:0;margin-top:.9mm}}
.qsub.qmatch .mc{{padding-left:8.4mm;text-indent:-8.4mm}}
.qsub.qmatch .mc .ql{{width:8.4mm}}
/* Column II's roman labels end flush, as printed: `(i)` and `(viii)` both stop at the text. */
.qsub.qmatch .mc:nth-child(even){{padding-left:12mm;text-indent:-12mm}}
.qsub.qmatch .mc:nth-child(even) .ql{{width:12mm;text-align:right;padding-right:1.8mm;
            box-sizing:border-box}}
.qsub.qmatch .mh{{font-weight:700}}
/* The table: the book sets its cells smaller than the body, with light internal rules and
   the orange-toned ground it prints, not the dark borders a default table gets. */
/* Columns sized by their content, as the book sets them. `fixed` gave every column the same
   width and `anywhere` then broke words to fit it: Table 1.1 printed `Anacardiace/ae`,
   `Dicotyledona/e` and `Angiosperma/e`, which the book never does. */
table.grid{{border-collapse:collapse;font-size:9pt;line-height:1.2;width:100%;
           table-layout:auto;overflow-wrap:break-word;hyphens:manual}}
.tbl{{text-align:left}}
table.grid.plain th,table.grid.plain td{{border:none;background:none;padding:.4mm 3mm .4mm 0}}
table.grid.plain{{width:auto}} .tcap{{font-weight:700;font-size:9.5pt;text-align:center;margin:0 0 2.2mm}}
/* The caption prints on the page, above the tinted table -- not on the table's ground. */
.tbl .tcap{{background:#fff;margin:0;padding:0 0 2.2mm}}
table.grid th,table.grid td{{border:.4pt solid #f0c89a;padding:.5mm 1.2mm;
                            text-align:left;vertical-align:top}}
table.grid th{{font-weight:700;background:#fdd9b0}}
table.grid td.nw{{white-space:nowrap}}
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
    tex_head = _KATEX_HEAD if uses_tex[0] else ""
    tex_run = _KATEX_RUN if uses_tex[0] else ""
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title)}</title>{tex_head}<style>{css}</style></head>'
            f'<body>{bar}{"".join(sheets)}{tex_run}{_FIT_JS}</body></html>')


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
