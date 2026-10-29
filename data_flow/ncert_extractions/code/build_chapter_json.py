#!/usr/bin/env python3
"""Build one chapter's CHAPTER JSON -- the nested tree that is the truth.

    python code/build_chapter_json.py BIO11L-ch01
    python code/build_chapter_json.py BIO11O-ch01 --no-agent-text

Pipeline for one chapter, in order:

    extract_page_layout   geometry        bbox, font, colour, pitch, folio, side   [script]
    join_agent_text       words           A2 agent text onto the measured boxes    [script]
    cut_figures           crops           figures and tables as PNG                [script]
    THIS MODULE           structure       the tree, ids, marks, sentences          [script]

What this module decides, and the measurement behind each:

  * UNIT PAGES ARE NOT CHAPTER PAGES. `Chapter_1.pdf` opens with the UNIT opener (`Unit 1 ·
    Diversity in the Living World`, with the unit's chapter list) and then the Ernst Mayr
    biography box, and only then the chapter itself. Measured on both editions: p001 carries a
    `chapter_title` reading `Unit 1` and p002 the Mayr box; the chapter's own title page is
    p003. Filed as chapter content those two pages put another chapter's name and a scientist's
    biography inside Chapter 1.

  * A PARAGRAPH BROKEN BY A PAGE IS ONE PIECE. A2 reports `first_block_continues_from_previous`
    and `last_block_continues_on_next` for exactly this, so the two halves are joined into one
    node with two `boxes`.

  * A LIST IS ONE PIECE. The four universal rules of nomenclature run from page 4 to page 5;
    as four loose nodes the list has no head and no order.

  * A FIGURE BELONGS WHERE IT IS MENTIONED. Figure 1.1 is printed beside the end of 1.2.6 and
    belongs to 1.2.7, the section that discusses it. The printed position stays in `boxes`.
"""

import argparse
import collections
import hashlib
import json
import os
import re
import unicodedata
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import book_design as design_lib          # noqa: E402
import chapter_tree as ct                 # noqa: E402
import cut_figures                        # noqa: E402
import extract_page_layout as extract_mod  # noqa: E402
import join_agent_layout                  # noqa: E402
import join_agent_special                 # noqa: E402
import join_agent_structure               # noqa: E402
import join_agent_text                    # noqa: E402

EDITION_WORD = {"L": "new", "O": "old"}
SUBJECT_WORD = {"BIO": "biology", "CHE": "chemistry", "PHY": "physics"}
SUBJECT_SHORT = {"BIO": "Bio", "CHE": "Chem", "PHY": "Phy"}

_UNIT_RE = re.compile(r"^\s*unit\s+(\d+)\s*$", re.I)
_FIG_REF = re.compile(r"\b(?:Figure|Fig\.)\s*(\d+\.\d+)", re.I)
_TAB_REF = re.compile(r"\bTable\s*(\d+\.\d+)", re.I)
_FIG_NUM = re.compile(r"^\s*(?:Figure|Fig\.)\s*(\d+\.\d+)", re.I)
_TAB_NUM = re.compile(r"^\s*TABLE\s*(\d+\.\d+)", re.I)
_Q_RE = re.compile(r"^\s*(?:Q\.?\s*)?(\d{1,2})\s*[.)]\s+(\S)")


def split_unit_pages(layout):
    """(unit_pages, chapter_pages). The unit opener and the pages before the chapter's own
    title page belong to the BOOK partition, not to this chapter."""
    first_chapter_page = None
    for i, p in enumerate(layout["pages"]):
        titles = [e["text"] for e in p["elements_in_reading_order"]
                  if e["role"] == "chapter_title"]
        if any(re.match(r"^\s*chapter\s+\d+", t, re.I) for t in titles):
            first_chapter_page = i
            break
    if first_chapter_page is None:
        # The A2 reader may drop the `CHAPTER 5` label as furniture and keep only the name, so
        # the agent-joined title no longer says `Chapter N`. Measured on BIO11L ch05: no page
        # matched, the Unit 2 opener and the Esau page stayed in the chapter, and the chapter
        # was titled -- and its folder named -- `Unit 2`. After a unit opener, the chapter
        # starts at the first page whose title is not the unit's.
        seen_unit = False
        for i, p in enumerate(layout["pages"]):
            titles = [(e.get("text") or "").strip() for e in p["elements_in_reading_order"]
                      if e["role"] == "chapter_title"]
            if any(_UNIT_RE.match(t) for t in titles):
                seen_unit = True
            elif seen_unit and any(titles):
                first_chapter_page = i
                break
    first_chapter_page = first_chapter_page or 0
    return layout["pages"][:first_chapter_page], layout["pages"][first_chapter_page:]


def unit_number(pages):
    for p in pages:
        for e in p["elements_in_reading_order"]:
            m = _UNIT_RE.match(e.get("text", "") or "")
            if m:
                return int(m.group(1))
    return None


def _page_no(page, idx):
    n = page.get("printed_page_number")
    return n if isinstance(n, int) else None


def _bullet_columns(page):
    """A column of symbol bullets glued to ONE of its items: every item beside it is a list item.

    The text layer gives BIO11L ch10 p121's three bullets (U+F06C, a Wingdings face) as one
    element with the middle item, `\\uf06c \\uf06c S phase (Synthesis) \\uf06c`, spanning all three
    lines, while `G1 phase (Gap 1)` and `G2 phase (Gap 2)` stood alone as paragraphs. The page
    printed S phase over both, and the tree had a two-bullet S item and two loose paragraphs.
    The glued item is cut back to its own line; each short paragraph that starts on a bullet's
    line, at the items' left edge, becomes `• <item>`.
    """
    els = page["elements_in_reading_order"]
    # BARE BULLETS MARK WHERE ITEMS START. A2 reads a bulleted list without its glyphs -- the
    # bullets are a separate Wingdings column -- so `Chromosomal material condenses ...` and
    # `Centrosome which had undergone duplication ...` (BIO11L ch10 p122) came out as ONE item.
    # Each bare bullet sits on the first printed line of its item: that line is cut as a new item.
    # bullets only -- one glyph, or a column of them (` `, BIO11L ch10 p121's
    # Interphase / M Phase): each glyph's own printed line gives a bullet position
    bare_els = [e for e in els if (e.get("text") or "").strip()
                and not (e.get("text") or "").replace("", "").strip() and e.get("bbox_pt")]
    bare = []
    for b in bare_els:
        lns = [ln["bbox_pt"] for ln in b.get("line_boxes_pt") or []
               if "" in (ln.get("text") or "")] or [b["bbox_pt"]]
        bare += [{"bbox_pt": bx} for bx in lns]
    for e in els:
        lbs = sorted(e.get("line_boxes_pt") or [], key=lambda ln: ln["bbox_pt"][1])
        raw = "".join(r.get("t") or "" for r in e.get("runs") or [])
        # bullets printed INSIDE the block's own lines (`Interphase` / `M Phase`, p121)
        if e not in bare_els and any((ln.get("text") or "").strip() == "" for ln in lbs):
            e["_bulleted"] = True
            # the glyph lines sit on the text lines: counted as lines of their own they halved
            # the row pitch and the render set `Interphase` over `M Phase (Mitosis phase)`
            e["line_count"] = len({round(ln["bbox_pt"][3]) for ln in lbs
                                   if (ln.get("text") or "").replace("", "").strip()}) or 1
        if not bare or e in bare_els or len(lbs) < 2 or "\n" not in raw.strip():
            continue

        def on_line(ln):
            # a bullet stands on a line when it covers at least half the line's height -- a
            # column of two glyphs read as ONE line box spans both of its lines
            y0, y1 = ln["bbox_pt"][1], ln["bbox_pt"][3]
            h = max(1.0, y1 - y0)
            return any(min(y1, b["bbox_pt"][3]) - max(y0, b["bbox_pt"][1]) >= 0.5 * h
                       and b["bbox_pt"][0] <= ln["bbox_pt"][0] + 2 for b in bare)
        nl = [i for i, ch in enumerate(raw) if ch == "\n"]
        if on_line(lbs[0]):
            e["_bulleted"] = True           # the list prints the book's bullet (`marker`)
        if raw.count("\n") == len(lbs) - 1:
            # one break per printed line: the bulleted lines start items
            starts = [k for k, ln in enumerate(lbs) if on_line(ln)]
            at = sorted({0 if k == 0 else nl[k - 1] + 1 for k in starts})
        elif on_line(lbs[0]) and raw.count("\n") + 1 <= len(lbs) // 2:
            # A2 joined each item's wrapped lines and broke only BETWEEN items
            at = [0] + [i + 1 for i in nl if raw[:i].strip()]
        else:
            continue
        if not at:
            continue
        new_runs, pos = [], 0
        for r in e.get("runs") or []:
            t = r.get("t") or ""
            out, last = [], 0
            for a in at:
                if pos <= a < pos + len(t) or (a == pos + len(t) and r is e["runs"][-1]):
                    out.append(t[last:a - pos])
                    out.append("• ")
                    last = a - pos
            out.append(t[last:])
            new_runs.append(dict(r, t="".join(out)))
            pos += len(t)
        e["runs"] = new_runs
        e["text"] = "".join(r["t"] for r in new_runs)
        e["role"] = "list"
    for e in els:
        t = e.get("text") or ""
        if t.count("") < 2 or not e.get("bbox_pt") or not e.get("bbox_sheet"):
            continue
        rows = [ln for ln in e.get("line_boxes_pt") or []
                if (ln.get("text") or "").replace("", "").strip()]
        rest = t.replace("", " ").strip()
        if len(rows) != 1 or not rest or len(rest) > 60:
            continue
        bp, bs = e["bbox_pt"], e["bbox_sheet"]
        sx = (bs[2] - bs[0]) / max(1e-6, bp[2] - bp[0])
        sy = (bs[3] - bs[1]) / max(1e-6, bp[3] - bp[1])
        y0, y1 = bp[1], bp[3]
        lx = rows[0]["bbox_pt"][0]
        for o in els:
            ob = o.get("bbox_pt")
            ot = (o.get("text") or "").strip()
            if (o is e or not ob or o.get("role") != "paragraph" or not ot or len(ot) > 60
                    or not (y0 - 2 <= (ob[1] + ob[3]) / 2 <= y1 + 2) or abs(ob[0] - lx) > 14):
                continue
            o["text"] = "• " + ot
            o["runs"] = [dict((o.get("runs") or [{}])[0], t="• ")] + list(o.get("runs") or [])
            o["role"] = "list"
            o.pop("line_pitch_pt", None)        # measured against a bullet's baseline, too
        lb = rows[0]["bbox_pt"]
        e["bbox_pt"] = list(lb)
        e["bbox_sheet"] = [round(bs[0] + (lb[0] - bp[0]) * sx, 4), round(bs[1] + (lb[1] - bp[1]) * sy, 4),
                           round(bs[0] + (lb[2] - bp[0]) * sx, 4), round(bs[1] + (lb[3] - bp[1]) * sy, 4)]
        e["bbox"] = e["bbox_sheet"]
        e["text"] = "• " + rest
        e["runs"] = [dict(r, t=(r.get("t") or "").replace("", "")) for r in e.get("runs") or []]
        e["runs"] = [dict((e["runs"] or [{}])[0], t="• ")] + [r for r in e["runs"] if (r.get("t") or "").strip()]
        e["role"] = "list"
        e["line_boxes_pt"] = rows
        # its pitch was measured between the bullets' baselines and the text's, 3pt apart; the
        # render then set the three phases 3pt apart, one over the next
        e["line_count"] = 1
        e.pop("line_pitch_pt", None)


def _two_column_order(elements):
    """A page set in TWO TEXT COLUMNS is read down the left column, then down the right.

    Down-the-page order (below) interleaved the columns of every Physics page: PHY11L ch01 p003
    read `Note that ...` (left, y 0.39), `the first uncertain digit ...` (right, y 0.39), `We
    employ ...` (left) -- so a paragraph's other-column half joined the wrong paragraph, the
    passages were scrambled and `As discussed above` landed before its own heading 1.3. Only a
    page with at least two narrow text blocks in EACH half is two-column; a biology page (one
    measure, a side rail) never is. Full-width elements (a table, a footnote) cut the page into
    bands, and each band is read left column, then right column."""
    def box(e):
        return e.get("bbox_sheet") or e["bbox"]

    def side(e):
        x0, _y0, x1, _y1 = box(e)
        if x1 - x0 > 0.55:
            return "full"
        return "left" if x1 <= 0.52 else ("right" if x0 >= 0.46 else "full")

    texty = [e for e in elements if e["role"] in ("paragraph", "list", "section_heading")]
    if (sum(side(e) == "left" for e in texty) < 2 or sum(side(e) == "right" for e in texty) < 2):
        return elements
    out, band = [], []

    def flush():
        band.sort(key=lambda e: (side(e) == "right", box(e)[1], box(e)[0]))
        out.extend(band)
        band.clear()
    for e in elements:                       # already sorted down the page
        if e["role"] not in ct._FURNITURE and side(e) == "full":
            flush()
            out.append(e)
        else:
            band.append(e)
    flush()
    return out


def collect_blocks(pages, two_col=False):
    """Every content element of the chapter, in reading order, with its page attached.

    READING ORDER IS DOWN THE PAGE, not column-by-column. `elements_in_reading_order` groups
    the side rail before the body, which is right for the renderer and wrong for the tree:
    measured on BIO11L ch01 p009, the headings `Summary` (y 0.134) and `Exercises` (y 0.512)
    fell into a different measured column from the prose, so they sorted AFTER paragraphs at
    y 0.168 -- and both sections came out empty, with the summary text filed under 1.2.7
    Kingdom instead.
    """
    out = []
    for p in pages:
        folio = _page_no(p, None)
        _bullet_columns(p)
        elements = sorted(p["elements_in_reading_order"],
                          key=lambda e: ((e.get("bbox_sheet") or e["bbox"])[1],
                                         (e.get("bbox_sheet") or e["bbox"])[0]))
        if two_col:                    # physics only: measured books keep down-the-page order
            elements = _two_column_order(elements)
        for e in elements:
            if e["role"] in ct._FURNITURE:
                continue
            # A SYMBOL-FONT BULLET IS A BULLET. NCERT sets list bullets in a Wingdings face whose
            # glyph reaches the text layer as the private-use U+F06C, so `Prophase` / `Metaphase`
            # / ... (BIO11L ch10 p122) came out as four loose paragraphs reading `
            # Prophase`, and a bullet whose item A2 had already read stayed behind as an empty
            # paragraph on four pages. As `•` the list rule takes the items; a bullet alone goes.
            if "" in (e.get("text") or ""):
                e = dict(e, text=e["text"].replace("", "•"),
                         runs=[dict(r, t=(r.get("t") or "").replace("", "•"))
                               for r in e.get("runs") or []])
                if not e["text"].replace("•", "").strip():
                    continue
                if e["role"] == "paragraph" and e["text"].lstrip().startswith("•"):
                    e["role"] = "list"
            if not (e.get("text") or "").strip() and e["role"] not in ("figure", "table"):
                continue
            out.append({"el": e, "page": folio, "page_file": p["page_file"],
                        "continues_from_previous": bool(
                            e.get("continues_from_previous")),
                        "source": e.get("text_source", "text_layer")})
    return out


def stitch_across_pages(blocks):
    """Join a paragraph that A2 says continues across the page break into ONE piece."""
    out = []
    for b in blocks:
        prev = out[-1] if out else None
        # A FIGURE SET ACROSS THE MEASURE CUTS A PARAGRAPH ON ITS OWN PAGE too: `...The name
        # cnidaria is derived from the` | Figure 4.6 | `cnidoblasts or cnidocytes ...` (BIO11L
        # ch04 p041). A2 reads the halves as two blocks and no page break joins them, so the
        # JSON and the Markdown carried two paragraphs, the first ending mid-sentence. The
        # halves are one paragraph when a figure or caption stands between them on the same
        # page, the first stops without closing punctuation and the second opens in lowercase.
        if (not b["continues_from_previous"] and b["el"]["role"] == "paragraph"
                and (b["el"].get("text") or "").lstrip()[:1].islower()):
            k = len(out) - 1
            while (k >= 0 and out[k].get("page_file") == b.get("page_file")
                   and out[k]["el"]["role"] in ("figure", "table", "figure_caption")):
                k -= 1
            if (0 <= k < len(out) - 1 and out[k]["el"]["role"] == "paragraph"
                    and out[k].get("page_file") == b.get("page_file")
                    and not re.search(r"[.!?:;)\]\"'’”]\s*$", out[k]["el"].get("text") or "")):
                b = dict(b, continues_from_previous=True)
        # A PAGE THAT ENDS MID-SENTENCE CONTINUES ON THE NEXT. A2 read p087's last block as
        # continuing and p088's first as NOT continued (BIO11L ch08), and only the second flag
        # reached here, so `... At about the same time, Theodore` | `Schwann (1839), a British
        # Zoologist ...` shipped as two paragraphs. A paragraph that closes its page on a letter
        # or a comma is unfinished; the next page's first paragraph -- past figures, captions
        # and a running head filed as a title -- is the rest of it, whatever its case.
        if not b["continues_from_previous"] and b["el"]["role"] == "paragraph":
            k = len(out) - 1
            while k >= 0 and (out[k]["el"]["role"] in ("figure", "table", "figure_caption")
                              or (out[k]["el"]["role"] == "chapter_title"
                                  and out[k].get("page_file") == b.get("page_file"))):
                k -= 1
            pf_prev, pf_b = out[k].get("page_file") if k >= 0 else None, b.get("page_file")
            if (k >= 0 and out[k]["el"]["role"] == "paragraph" and pf_prev and pf_b
                    and pf_prev.isdigit() and pf_b.isdigit() and int(pf_b) == int(pf_prev) + 1
                    and re.search(r"[A-Za-z,]\s*$", out[k]["el"].get("text") or "")
                    # prose, not a list entry: the Unit 3 opener's `Chapter 10 Cell Cycle and
                    # Cell Division` also ends on a letter, and joined the biography overleaf.
                    and len((out[k]["el"].get("text") or "").split()) >= 15):
                b = dict(b, continues_from_previous=True)
        # A FIGURE PRINTED AT THE TOP OF THE NEXT PAGE sits between the two halves in reading
        # order, so the halves never met: `...fixing nitrogen in legume` | Figure 2.3 |
        # `roots, etc.` (BIO11L ch02 p013-014), and Figure 2.6 inside `...outside the living
        # cell. Once they infect a cell...` (p019-020). The sentence was cut by a picture in the
        # JSON and the Markdown. Artwork and captions are stepped over; the figure then follows
        # the whole paragraph.
        if b["continues_from_previous"] and b["el"]["role"] == "paragraph":
            # A caption's second line that opens with a panel letter (`(b) Aspergillus (c)
            # Agaricus`, p017) is typed a list here; it is caption, so it is stepped over too.
            def caption_like(x):
                t = (x["el"].get("text") or "").strip()
                # ...and the continuation page's running head when the extractor filed it as a
                # title (`Animal Kingdom`, BIO11L ch04 p051; `_running_head_titles` returns it
                # to the page later): it stood between `The skin of` and `mammals is unique`.
                bb = x["el"].get("bbox_sheet") or x["el"].get("bbox") or [0, 1, 0, 1]
                if (x["el"]["role"] == "chapter_title" and x.get("page_file") == b.get("page_file")
                        and bb[1] < 0.11):
                    return True
                return (x["el"]["role"] in ("figure", "table", "figure_caption")
                        or (x["el"]["role"] == "list" and len(t) < 120
                            and re.match(r"^\(\s?[a-h]\s?\)\s*\S", t)
                            and x.get("page_file") != b.get("page_file")))
            k = len(out) - 1
            while k >= 0 and caption_like(out[k]):
                k -= 1
            if k >= 0:
                prev = out[k]
        if (prev and b["continues_from_previous"]
                and prev["el"]["role"] == b["el"]["role"] == "paragraph"):
            # Each page's printed lines, kept per fragment, so the halves can be placed line
            # by line on their own pages (`_apply_line_geom`) instead of reflowed.
            if "frag_rows" not in prev:
                prev["frag_rows"] = [_print_rows(prev["el"])]
            prev["frag_rows"].append(_print_rows(b["el"]))
            prev["el"] = dict(prev["el"])
            prev_runs = list(prev["el"].get("runs") or [])
            next_runs = list(b["el"].get("runs") or [])
            # A SEPARATOR RUN, or the words fuse. `body` is built by concatenating run texts,
            # so joining the runs without one produced `andtypes`, `Linnaeusused`,
            # `andmelongena` and `Allthese` -- four real corruptions in one chapter, each at a
            # page break. The TEXT field was being joined with a space and the RUNS were not,
            # and `body` comes from the runs.
            if prev_runs and next_runs:
                tail = (prev_runs[-1].get("t") or "")
                head = (next_runs[0].get("t") or "")
                if tail and head and not tail.endswith((" ", "-")) \
                        and not head.startswith(" "):
                    prev_runs.append({"t": " ", "b": False, "i": False, "sc": False,
                                      "script": None,
                                      "color": prev_runs[-1].get("color"),
                                      "size": prev_runs[-1].get("size"),
                                      "font": prev_runs[-1].get("font")})
            # WHICH CHARACTERS CAME FROM WHICH PAGE. A paragraph printed across a page break is
            # one piece with two boxes, and without a character range per box nothing can say
            # which words belong in which box -- so a page-faithful renderer cannot place the
            # halves, and the fragment the book prints on page 4 cannot be shown on page 4.
            prev_len = len("".join(r.get("t", "") for r in prev_runs))
            prev["el"]["runs"] = prev_runs + next_runs
            prev["el"]["text"] = "".join(r.get("t", "") for r in prev["el"]["runs"]).strip()
            first = prev.get("extra_boxes")
            if not first:
                prev["char_ranges"] = [{"page": prev["page"],
                                        "page_file": prev.get("page_file"),
                                        "from": 0, "to": prev_len}]
            total = len("".join(r.get("t", "") for r in prev["el"]["runs"]))
            prev["char_ranges"] = (prev.get("char_ranges") or []) + [
                {"page": b["page"], "page_file": b.get("page_file"),
                 "from": prev_len, "to": total}]
            prev["extra_boxes"] = prev.get("extra_boxes", []) + [
                {"page": b["page"], "page_file": b.get("page_file"),
                 "bbox": b["el"].get("bbox_sheet") or b["el"]["bbox"]}]
            continue
        out.append(dict(b))
    return out


def collapse_lists(blocks):
    """A run of consecutive `list` blocks becomes ONE list node holding its items."""
    out, run = [], []

    def flush():
        if not run:
            out.extend(deferred)
            deferred.clear()
            return
        head = dict(run[0])
        head["items"] = [{"text": r["el"].get("text", ""),
                          "runs": r["el"].get("runs") or []} for r in run]
        head["extra_boxes"] = head.get("extra_boxes", []) + [
            {"page": r["page"], "bbox": r["el"].get("bbox_sheet") or r["el"]["bbox"]}
            for r in run[1:]]
        out.append(head)
        run.clear()
        out.extend(deferred)
        deferred.clear()

    # A BLOCK IN ANOTHER COLUMN DOES NOT END A LIST. BIO11L ch10 p121's margin box `How do plants
    # and animals continue to grow ...?` sorts between `S phase (Synthesis)` and `G2 phase (Gap
    # 2)`, so the three phases came out as two lists. With a list open, a block on the same page
    # lying wholly beside the list's items, followed by more of the list, waits until it ends.
    deferred = []

    def beside(b, nxt):
        if not run or b["el"]["role"] == "list" or nxt is None or nxt["el"]["role"] != "list":
            return False
        if b.get("page_file") != run[-1].get("page_file") or nxt.get("page_file") != b.get("page_file"):
            return False
        bb = b["el"].get("bbox_sheet") or b["el"]["bbox"]
        xs = [(r["el"].get("bbox_sheet") or r["el"]["bbox"]) for r in run]
        return bb[0] > max(x[2] for x in xs) + 0.02 or bb[2] < min(x[0] for x in xs) - 0.02

    for i, b in enumerate(blocks):
        if beside(b, blocks[i + 1] if i + 1 < len(blocks) else None):
            deferred.append(b)
            continue
        # AN ITEM TYPED AS A PARAGRAPH IS STILL AN ITEM. Question 14's match table (BIO11L ch04
        # p054) extracted `(a)`..`(d)` as list lines and `(e)`..`(h)` as paragraphs, so the list
        # stopped at (d) and four rows printed as loose paragraphs after it. A paragraph that
        # directly follows list items on the same page and opens with a list marker continues
        # the list.
        if (b["el"]["role"] == "paragraph" and run
                and run[-1].get("page_file") == b.get("page_file")
                and _MARK_AT_START.match(b["el"].get("text") or "")):
            b = dict(b, el=dict(b["el"], role="list"))
        if b["el"]["role"] == "list":
            # A LIST PRINTED ON TWO PAGES IS TWO LIST NODES, one on each page. Run together,
            # BIO11L ch04's Exercises took p054's `14. Match the following ... (h)` into p053's
            # list, every question it split into carried p053's page and both pages' boxes, and
            # the render squeezed question 14 into p053's box at a fraction of its size. Questions
            # continue their numbering across blocks (`_split_exercise_questions`), so nothing is
            # lost by keeping each page's items on their page.
            if run and run[-1].get("page_file") != b.get("page_file"):
                flush()
            run.append(b)
            continue
        flush()
        out.append(b)
    flush()
    return out


# A line that opens a new list item: `(ii)`, `(b)`, `2.`, `3)` or a bullet.
# `(f )` with a space inside is how BIO11L ch04's match table prints (f), so the bracket
# may hold spaces round the label.
_ITEM_START = re.compile(
    r"\n(?=[ \t]*(?:\(\s?([ivxlc]{1,5}|[a-z])\s?\)|(\d{1,2})[.)]\s|([•▪◦])))")
_MARK_AT_START = re.compile(
    r"^\s*(?:\(\s?([ivxlc]{1,5}|[a-z])\s?\)|(\d{1,2})[.)]\s|([•▪◦]))")
_ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii"]
_ROMAN_MISPRINT = {"iiii": "iii"}


def _next_markers(m):
    """The markers that may follow marker `m` as the NEXT item of the same list."""
    if m is None:
        return None                                     # anything may start the run
    if m in "•▪◦":
        return {m}
    if m.isdigit():
        return {str(int(m) + 1)}
    nxt = set()
    if m in _ROMAN[:-1]:
        nxt.add(_ROMAN[_ROMAN.index(m) + 1])
    if len(m) == 1 and m < "z":
        nxt.add(chr(ord(m) + 1))
    return nxt


def _split_item_runs(runs):
    """One list element's runs, cut into one run list per printed item.

    A2 reads `(i) open type ...` and `(ii) closed type ...` as ONE list block with the items
    on separate lines, and the join keeps that `\\n`. Turning the runs into a body collapses
    it to a space, so both items came out as one item and printed as one run-on line
    (BIO11L ch04 p002). The cut is made only at a line break that starts the NEXT marker in
    sequence -- (i) then (ii), (a) then (b), 1. then 2. A match-the-following table sets
    `(a) Operculum` and `(i) Ctenophora` on lines of their own too, and there `(i)` is the
    other column, not a new item: cutting on any marker broke question 14 into sixteen parts.
    """
    text = "".join(r.get("t") or "" for r in runs)
    m0 = _MARK_AT_START.match(text)
    cur = next((g for g in m0.groups() if g), None) if m0 else None
    # TWO LEVELS: numbered questions and their lettered parts. BIO12L ch02's p040 list runs
    # `(f) ... (k) ...` then `2.` .. `21.`; with one sequence, nothing could follow `(k)` but
    # `(l)`, and questions 2-21 stayed inside part (k). A number continues the numbered level
    # (any number when the list opened mid-question), and `(a)`/`(i)` opens a question's parts.
    top = int(cur) if cur and cur.isdigit() else None
    cuts = []
    for m in _ITEM_START.finditer(text):
        mk = next(g for g in m.groups() if g)
        # A MISPRINTED NUMERAL keeps its place in the sequence. BIO12L ch05 p102 prints the
        # HGP goals `(i) (ii) (iiii) (iv) (v) (vi)`; `(iiii)` was no successor of `(ii)`, so
        # items (iii)-(vi) all stayed inside (ii). The printed label is left as printed.
        mk = _ROMAN_MISPRINT.get(mk, mk)
        allowed = _next_markers(cur)
        if cur and cur.isdigit():
            allowed = allowed | {"a", "i"}
        elif cur and cur not in "•▪◦" and mk.isdigit():
            allowed = (allowed or set()) | ({str(top + 1)} if top is not None else {mk})
        if allowed is None or mk in allowed:
            cuts.append(m.start())
            cur = mk
            if mk.isdigit():
                top = int(mk)
        # A LETTER PRINTED TWICE opens a row of its own. BIO11L ch16 p215's match table prints
        # `(d) Uricotelism` and then `(d) ADH` on the next line; `(d)` was no successor of `(d)`,
        # so ADH's row ran on inside Uricotelism's. The sequence stays where it was.
        elif mk == cur and len(mk) == 1 and mk.isalpha():
            cuts.append(m.start())
    # A LIST WITH NO PRINTED MARKERS IN ITS TEXT is still one item per line when every line is
    # short: the book's bullets are glyphs in a separate column, so A2 read `Interphase\nM Phase
    # (Mitosis phase)` (BIO11L ch10 p121) as one block and it shipped as ONE item. A long line
    # is a wrapped item, and then nothing is cut.
    if not cuts and m0 is None and "\n" in text.strip():
        lines = text.strip().split("\n")
        if len(lines) >= 2 and all(0 < len(ln.strip()) <= 45 for ln in lines):
            cuts = [k for k, ch in enumerate(text) if ch == "\n" and text[:k].strip()]
    if not cuts:
        return [runs]
    bounds = [0] + cuts + [len(text)]
    out = []
    for a, b in zip(bounds, bounds[1:]):
        # The piece starts at the `\n` it was cut on. Trim it off the TEXT, not off a body
        # derived later: a body trimmed after its marks were computed shifts every mark by
        # one, and `(ii) closed type` came out bold on `losed type `.
        piece = join_agent_text._slice_runs(runs, a, b)
        while piece and not (piece[0].get("t") or "").strip():
            piece = piece[1:]
        if piece:
            piece[0] = dict(piece[0], t=piece[0]["t"].lstrip())
            out.append(piece)
    return out


def node_from(block, book_base, chapter_num, path):
    """One tree node, with everything the schema asks a node to carry."""
    el = block["el"]
    role = el["role"]
    kind = ct._KIND.get(role, "para")
    if block.get("items"):
        kind = "list"

    node = {"kind": kind}
    # EVERY BOX SAYS WHERE ITS GEOMETRY CAME FROM.
    #   measured  -- from the PDF text layer, exact
    #   agent     -- from a2l-layout-reader measuring the page image
    #   estimated -- INVENTED. A reading-order guess, 0.10-0.90 wide. Carries no information
    #                about the printed layout and must never be rendered as though it did.
    # An external review of Class 12 ch01 found 127 boxes sharing one x-range with nothing to
    # distinguish them from measurements. A guess that cannot be told from a measurement is
    # worse than no guess at all, because it is trusted.
    src = el.get("layout_source") or ("agent" if el.get("from_a2l") else "measured")
    boxes = [{"page": block["page"], "src": src,
              "bbox": [round(v, 4) for v in (el.get("bbox_sheet") or el["bbox"])]}]
    boxes += block.get("extra_boxes", [])
    # A PAGE THAT PRINTS NO FOLIO IS STILL A PAGE. The textless Class 12 scans carry no page
    # numbers at all, so filtering boxes on `page is not None` emptied every node's `boxes`
    # AND its `pages` -- and the renderer, which buckets by page, then put all 23 pages of the
    # chapter onto one sheet with every paragraph overlapping the next. The box is kept either
    # way; the folio is simply absent, which is the truth about that page.
    pf = block.get("page_file")
    for b in boxes:
        if b.get("page") is None:
            b["page_file"] = pf
        # A box with NO provenance is the thing being fixed here -- it reads as a measurement
        # to anyone who does not know the pipeline. Continuation boxes and merged caption
        # boxes come from the same extractor as the first box, so they inherit its source.
        b.setdefault("src", src)
    node["boxes"] = boxes
    node["pages"] = sorted({b["page"] for b in boxes if b.get("page") is not None})
    # THE CHAPTER-OPENING PAGE PRINTS NO FOLIO. NCERT starts numbering at the first body page,
    # so `Chapter 1 / The Living World` and the contents rail have `pages: []` -- and anything
    # that buckets content by printed page then drops them entirely. The page FILE always
    # exists, so it is carried as the fallback key.
    node["page_file"] = block.get("page_file")
    if block.get("char_ranges"):
        node["char_ranges"] = block["char_ranges"]

    # A TITLE PRINTED INSIDE THE ARTWORK. BIO12L ch05's Central dogma diagram has no `Figure
    # n.m` caption; `Central dogma` is set under the arrows, inside the crop, and A2S read it as
    # the caption. Kept aside here; a figure still captionless at the end takes it (no caption
    # box: it is already in the picture).
    if kind == "figure" and el.get("figure_caption") and not _CAPTION_LABEL.match(
            el["figure_caption"].strip()):
        node["_art_caption"] = el["figure_caption"].strip()
    if kind in ("figure", "table"):
        caption = (el.get("text") or "").strip()
        # A LINE BREAK IN A LETTER-SPACED CAPTION IS A WORD BREAK. Figure 1.1's caption is set
        # in a narrow rail with tracking, one word per line (`c a t e g o r i e s`,
        # `s h o w i n g`). Joined with single spaces, the gap between two lines looks exactly
        # like the gap between two letters, and closing up the tracking fused the words into
        # `categoriesshowinghierarchial` -- which also ran out of the rail over the body text.
        # The printed lines are measured; joining them with the word gap `_despace` already
        # honours keeps every word separate.
        _lines = _printed_lines(el)
        if len(_lines) > 1 and any(_SPACED.search(x) for x in _lines):
            caption = "  ".join(_lines)
        m = (_FIG_NUM if kind == "figure" else _TAB_NUM).match(caption)
        if m:
            node["number"] = m.group(1)
        node["caption"] = caption
        # THE CAPTION'S ITALICS. `Figure 3.3 Pteridophytes : (a) Selaginella (b) Equisetum`
        # prints every genus in italic; only the text was kept, so they came out upright.
        # Kept only when the runs spell exactly the caption, so no offset can drift.
        cbody, cmarks = ct.runs_to_body_marks(el.get("runs") or [])
        if cmarks and cbody == caption:
            node["caption_marks"] = cmarks
        if el.get("figure_file"):
            node["image_local"] = f"figures/{el['figure_file']}"
        if el.get("table_text"):
            node["table_text"] = el["table_text"]
        if el.get("table_grid"):
            node["table_grid"] = el["table_grid"]
            if el.get("cell_italics"):
                node["cell_italics"] = el["cell_italics"]
        # A table the book DRAWS (`join_agent_text.apply_agent_figures`): its crop is the
        # printed grid, and its caption keeps the box it was measured at.
        if el.get("grid_drawn"):
            node["grid_drawn"] = True
            if el.get("caption_bbox_sheet"):
                node["caption_box"] = {"page": el.get("page"), "src": "measured",
                                       "bbox": [round(v, 4) for v in el["caption_bbox_sheet"]]}
            # THE CELLS ARE TEXT. Storing only the grid left every cell out of `body`, so a
            # search for `Monocotyledonae` or `Anacardiaceae` found nothing -- 17 words of
            # Table 1.1 were absent from the chapter's text entirely.
            node["body"] = " ".join(c for row in el["table_grid"]["cells"] for c in row if c)
        for _k in ("table_fill", "table_header_fill", "fill"):
            if el.get(_k):
                node[_k] = el[_k]
        if el.get("table_caption"):
            node["caption"] = el["table_caption"]
        if el.get("special_source"):
            node["special_source"] = el["special_source"]
        if el.get("latex"):
            node["latex"] = el["latex"]
    elif kind == "list":
        node["items"] = []
        if el.get("_bulleted"):
            node["marker"] = "•"
        for it in block["items"]:
            for runs in (_split_item_runs(it["runs"]) if it["runs"] else [None]):
                body, marks = ct.runs_to_body_marks(runs) if runs else (it["text"], [])
                # THE BULLET IS THE LIST'S, NOT THE ITEM'S TEXT. Kept, it printed twice in the
                # Markdown (`- •  G1 phase`, BIO11L ch10 p121) and split the item's bold run.
                lead = re.match(r"^\s*[•▪◦]\s*", body or "")
                if lead and lead.end() < len(body):
                    # ...and says so once: the render hangs the book's bullet on every row
                    node["marker"] = "•"
                    cut = lead.end()
                    body = body[cut:]
                    marks = [{**m, "from": max(0, m["from"] - cut), "to": m["to"] - cut}
                             for m in marks if m["to"] > cut]
                item = {"body": body, "marks": marks, "body_md": ct.to_body_md(body, marks)}
                # The item's printed lines, for `_question_text` (and dropped once it has run):
                # a question's sub-lines are lost once the body joins them with spaces.
                raw = "".join(r.get("t") or "" for r in runs or [])
                if "\n" in raw.strip():
                    # Each line starts AFTER its `\n`: a slice that starts on it is trimmed by
                    # `runs_to_body_marks` without moving the marks, one character late.
                    nl = [k for k, ch in enumerate(raw) if ch == "\n"]
                    item["_lines"] = [ct.runs_to_body_marks(join_agent_text._slice_runs(runs, a, b))
                                      for a, b in zip([0] + [k + 1 for k in nl], nl + [len(raw)])]
                node["items"].append(item)
        node["body"] = " ".join(i["body"] for i in node["items"])
    else:
        body, marks = ct.runs_to_body_marks(el.get("runs") or [])
        # A HYPHEN THAT ENDS A PRINTED LINE belongs to the word: `four-` / `chambered` is
        # `four-chambered`. The line break became a space, so the JSON and the Markdown read
        # `Heart is four- chambered`, `well- developed`, `Sea- hare` (BIO11L ch04). The space
        # goes, and everything that indexes the body moves with it -- the marks AND each page's
        # `char_ranges`: shifting only the marks started p050's half of a paragraph one letter
        # late (`ungs.` for `lungs.`).
        cuts = ct.line_end_hyphen_cuts(body)
        if cuts:
            def shift(o, cuts=cuts):
                return o - sum(1 for c in cuts if c < o)
            body = "".join(ch for k, ch in enumerate(body) if k not in set(cuts))
            marks = [{**m, "from": shift(m["from"]), "to": shift(m["to"])} for m in marks]
            if node.get("char_ranges"):
                node["char_ranges"] = [{**r, "from": shift(r["from"]), "to": shift(r["to"])}
                                       for r in node["char_ranges"]]
        if not body:
            body = (el.get("text") or "").strip()
        node["body"] = body
        if marks:
            node["marks"] = marks
        # AN EQUATION KEEPS ITS LaTeX. Only figures and tables carried A2S's `latex`, so
        # `rate = δP/δt` and the carbonic anhydrase equilibrium (BIO11L ch09) reached the JSON as
        # flattened text alone, and the page could only print it flat -- the book's stacked
        # fraction and labelled arrow were gone. The body stays the readable flat form.
        if el.get("latex"):
            node["latex"] = el["latex"]
        node["body_md"] = ct.to_body_md(body, marks)
        node["sentences"] = ct.split_sentences(body)
        terms = ct.terms_in(body, marks)
        if terms:
            node["terms"] = terms

    node["id"] = ct.stable_id(kind, book_base, chapter_num, path)
    node["source"] = ("page_image" if block.get("source") in ("a2-agent", "a2s-agent")
                      else "text_layer")
    node["qa"] = "auto"
    # The ARRANGEMENT travels with the node, so a consumer reading only chapter.json can place
    # it the way the book does without re-deriving anything.
    if el.get("layout_source"):
        node["layout_source"] = el["layout_source"]
    # ---- A2L's MEASURED LAYOUT -------------------------------------------------------------
    # Everything a2l-layout-reader measures off the page image, carried through verbatim so a
    # renderer can reproduce the printed page instead of re-deriving it from heuristics. These
    # are the fields that answer "which side does this sit on, how big is the type, what
    # colour is the panel behind it, how much air is above it".
    for key, out in (("column", "column"), ("size_rel", "size_rel"), ("size_pt", "size_pt"),
                     ("space_before", "space_before"), ("indent", "indent"),
                     ("align", "align"), ("fill", "fill"), ("text_color", "text_color"),
                     ("face", "face"), ("a2l_role", "printed_role")):
        if el.get(key) is not None:
            node[out] = el[key]
    for k in ("layout_align", "layout_font", "layout_fill", "layout_text_color",
              "layout_role"):
        if el.get(k) is not None:
            node[k] = el[k]
    if el.get("column"):
        node["column"] = el["column"]
    if el.get("line_pitch_pt"):
        node["line_pitch_pt"] = el["line_pitch_pt"]
    # HOW MANY LINES THE BOOK ACTUALLY SET, and where each one sat.
    #
    # The extractor measures both and they were dropped here, so everything downstream fell
    # back to guessing "about 62 characters to a line" from the character count. That guess
    # drives `fit_factor`, which decides whether a page overflows and by how much the type is
    # scaled -- so every page's size was being set from an estimate when the real number was
    # measured two steps earlier and thrown away.
    #
    # With the real count, a block's printed height is `line_count x line_pitch_pt` exactly,
    # and a renderer can set the type so it occupies the lines the book gave it.
    if el.get("line_count"):
        node["line_count"] = el["line_count"]
    if el.get("line_boxes"):
        node["line_boxes"] = el["line_boxes"]
    node.update(_typography(el, node.get("body") or ""))
    # The printed lines, for line-by-line placement (`_apply_line_geom`, after the text passes).
    if kind in ("para", "box") and not block.get("extra_boxes"):
        rows = _print_rows(el)
        if rows:
            node["_print_rows"] = rows
    elif kind == "list" and not block.get("extra_boxes"):
        # A LIST ITEM SET AROUND A FIGURE is placed line by line too. BIO12L ch13 p220's
        # `(ii) Species-Area relationships` runs its lines beside Figure 13.2 at x 0.59 and
        # flowed in its full-width box ran over the graph. Only a list that wraps round
        # something -- a line starting far right of the block's edge, not a hanging indent --
        # takes this, so every ordinary list keeps its marker-and-hang setting.
        rows = _print_rows(el)
        if rows and max(r["bbox"][0] for r in rows) - min(r["bbox"][0] for r in rows) >= 0.15:
            node["_print_rows"] = rows
    elif kind == "para" and block.get("frag_rows"):
        node["_frag_rows"] = block["frag_rows"]
    elif (kind == "figure" and (node.get("caption") or "").strip()
          and not node.get("image_local") and not el.get("table_grid")):
        # A CAPTION'S PRINTED LINES. The book hangs a caption's turnover lines under the text
        # after `Figure 6.2`, or centres them (Figure 6.1), and justifies the rest; set as one
        # flowing block the render started every line at the box edge (BIO12L ch06, every
        # caption). Its lines are kept, as a paragraph's are, for `caption_line_geom`.
        rows = _print_rows(el)
        if rows:
            node["_caption_rows"] = rows
    # A numbered block's printed lines travel with it as far as the exercise split, so a
    # question can tell whether the book set its sub-parts on one line or one per line.
    # Removed again before the file is written (`_mark_inline_parts`).
    if re.match(r"^\s*\d{1,2}[.)]\s", node.get("body") or ""):
        pl = _printed_lines(el)
        if pl:
            node["print_lines"] = pl
    # A3 groups blocks into passages by the number A2 gave them, so the number has to survive
    # into the tree or the passage join has nothing to match on.
    if el.get("a2_block_n") is not None:
        node["a2_block_n"] = el["a2_block_n"]
    return node


def _printed_lines(el):
    """The text of each line the book printed in this block, top to bottom. Line objects on
    one baseline (a bold run, then the rest of the line) are one printed line."""
    rows = []
    for ln in sorted(el.get("line_boxes_pt") or [],
                     key=lambda ln: (ln["bbox_pt"][3], ln["bbox_pt"][0])):
        if rows and abs(ln["bbox_pt"][3] - rows[-1][0]) < 2.0:
            rows[-1][1].append(ln["text"])
        else:
            rows.append([ln["bbox_pt"][3], [ln["text"]]])
    return [" ".join(t).strip() for _y, t in rows]


def _print_rows(el):
    """The block's printed pieces as [{text, bbox (sheet fractions), row}], in reading order.

    A ROW is one printed line. Within a row, pieces separated by a real gap stay separate: a
    match table prints `(a) Chlamydomonas` and `(i) Moss` on one row in two columns, and each
    must be placed at its own x. Pieces that touch -- `20` and its superscript `th` -- are one.
    """
    lines = [ln for ln in (el.get("line_boxes_pt") or []) if (ln.get("text") or "").strip()]
    pt, sh = el.get("bbox_pt"), el.get("bbox_sheet") or el.get("bbox")
    if len(lines) < 2 or not pt or not sh or (pt[2] - pt[0]) <= 0 or (pt[3] - pt[1]) <= 0:
        return None
    sx = (sh[2] - sh[0]) / (pt[2] - pt[0])
    sy = (sh[3] - sh[1]) / (pt[3] - pt[1])
    rows = []                                   # grouped by vertical overlap, as the extractor
    for ln in sorted(lines, key=lambda l: (l["bbox_pt"][1] + l["bbox_pt"][3]) / 2):
        y0, y1 = ln["bbox_pt"][1], ln["bbox_pt"][3]
        for r in rows:
            if min(y1, r["y1"]) - max(y0, r["y0"]) >= 0.5 * min(y1 - y0, r["y1"] - r["y0"]):
                r["lines"].append(ln)
                r["y0"], r["y1"] = min(r["y0"], y0), max(r["y1"], y1)
                break
        else:
            rows.append({"y0": y0, "y1": y1, "lines": [ln]})
    rows.sort(key=lambda r: r["y0"])
    out = []
    for k, r in enumerate(rows):
        parts = []
        for ln in sorted(r["lines"], key=lambda l: l["bbox_pt"][0]):
            b = ln["bbox_pt"]
            if parts and b[0] - parts[-1]["pt"][2] < 6.0:
                q = parts[-1]
                q["pt"] = [min(q["pt"][0], b[0]), min(q["pt"][1], b[1]),
                           max(q["pt"][2], b[2]), max(q["pt"][3], b[3])]
                q["text"] += ln["text"] if b[0] - q["pt"][2] < 0.5 else " " + ln["text"]
            else:
                parts.append({"pt": list(b), "text": ln["text"]})
        for q in parts:
            out.append({"text": q["text"], "row": k, "solo": len(parts) == 1,
                        "bbox": [round(sh[0] + (q["pt"][0] - pt[0]) * sx, 4),
                                 round(sh[1] + (q["pt"][1] - pt[1]) * sy, 4),
                                 round(sh[0] + (q["pt"][2] - pt[0]) * sx, 4),
                                 round(sh[1] + (q["pt"][3] - pt[1]) * sy, 4)]})
    return out


# Characters that are "letters" to Python but not to a line match: NCERT's Symbol-font arrow
# reaches the text layer as `à` where A2 writes `→`, and A2 writes `10⁶` where the layer has the
# 6 as a separate piece (BIO12L ch05 p090, p095, p105 -- each block lost its line placement,
# flowed, and printed shrunk).
_NOT_LETTER = set("àÀ⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉")


def _is_letter(ch):
    # Letters only: a DIGIT may be a script on one side and plain on the other -- the body's
    # `CO₂` is the page line's `CO2` (BIO11L ch09 p105), so counting digits left that paragraph
    # unplaced and flowed across Table 9.1. Every line still has its letters to match on.
    return ch.isalpha() and ch not in _NOT_LETTER


def _fold(ch):
    """`₂` and `²` match the `2` the text layer prints: `CO₂` in the body is `CO2` on the page
    line, and the mismatch left BIO11L ch09 p105's paragraph unplaced, flowed across Table 9.1."""
    return unicodedata.normalize("NFKC", ch).lower()[:1] or ch.lower()


def _letters(s):
    return "".join(_fold(ch) for ch in (s or "") if _is_letter(ch))


def _line_geom(rows, body):
    """Each printed piece of a block: its measured box and where it starts in `body`.

    A paragraph set around a figure is not a rectangle. BIO11L ch02 p014 prints the Mycoplasma
    paragraph's first lines in the narrow column beside Figure 2.3 and the rest at full width;
    flowed as one rectangle, it ran over the figure's caption. And any paragraph flowed in a
    substitute font breaks its lines differently from the book. Placing each line at its own
    measured box reproduces the book's breaks exactly and cannot overrun a neighbour.

    WHERE A LINE STARTS IS SEARCHED NEAR WHERE IT MUST START. The first version took the first
    match of a line's opening letters after the previous one, and a repeated word defeated it:
    on BIO11L ch03 p032 the line beginning `pteridophytes all the spores` matched the earlier
    `pteridophytes. In majority` -- so one line was stretched across the measure with half its
    words and the next ran off the sheet, CUT. A line starts about where the previous one plus
    its own letter count says; the occurrence nearest that point wins.

    AND EVERY PIECE IS CHECKED. Each piece's text must hold about as many letters as the book
    printed on that line. If any does not, nothing is returned and the block flows as a whole
    -- a placed line holding the wrong words is never shipped.
    """
    # A piece that is only a script's digits (`6` of `10⁶`, set a little above its line) is not
    # a printed line of its own.
    rows = [r for r in (rows or []) if not re.fullmatch(r"\s*\d{1,3}\s*", r.get("text") or "")]
    if not rows or len(rows) < 2 or not body:
        return None
    # A PRINTED LINE WITH NO LETTERS -- `11.5).` closing `... electron flow (Figure` on BIO11L
    # ch11 p140 -- has nothing to match letters on, and it used to sink the whole paragraph:
    # flowed in its full-width box, the column beside Figure 11.6 ran across the figure. The
    # lettered lines are placed first; a bare line is then found by its own characters between
    # its neighbours.
    if any(not _letters(r["text"]) for r in rows):
        keep = [r for r in rows if _letters(r["text"])]
        if not keep:
            return None
        geom = (_line_geom(keep, body) if len(keep) > 1 else
                [{"from": 0, "row": keep[0]["row"], "solo": keep[0]["solo"],
                  "hyphen": keep[0]["text"].rstrip().endswith("-"), "bbox": list(keep[0]["bbox"])}])
        if not geom:
            return None
        placed = dict(zip((id(r) for r in keep), geom))
        nb = unicodedata.normalize("NFKC", body)
        nb = nb if len(nb) == len(body) else body
        out, lo = [], 0
        for k, r in enumerate(rows):
            if id(r) in placed:
                out.append(placed[id(r)])
                lo = placed[id(r)]["from"] + 1
                continue
            nxt = next((placed[id(q)]["from"] for q in rows[k + 1:] if id(q) in placed), len(body))
            at = nb.find(r["text"].strip(), lo, nxt)
            if at < 0:
                return None
            out.append({"from": at, "row": r["row"], "solo": r["solo"], "hyphen": False,
                        "bbox": list(r["bbox"])})
            lo = at + 1
        return out
    letters = [(i, _fold(ch)) for i, ch in enumerate(body) if _is_letter(ch)]
    flat = "".join(ch for _i, ch in letters)
    want = [_letters(r["text"]) for r in rows]
    if any(not w for w in want):
        return None
    starts, expect = [], 0
    for k, w in enumerate(want):
        if k == 0:
            starts.append(0)
            expect = len(w)
            continue
        probe = w[:16]
        hits, at = [], flat.find(probe, max(starts[-1] + 1, expect - 60))
        while 0 <= at <= expect + 60:
            hits.append(at)
            at = flat.find(probe, at + 1)
        if not hits:
            return None
        at = min(hits, key=lambda h: abs(h - expect))
        starts.append(at)
        expect = at + len(w)
    # Every piece must carry the letters the book printed there, give or take a hyphen
    # rejoined or a symbol the agent wrote differently.
    for k, w in enumerate(want):
        end = starts[k + 1] if k + 1 < len(starts) else len(flat)
        got = end - starts[k]
        if abs(got - len(w)) > max(4, 0.12 * len(w)):
            return None
    out = []
    for k, (r, at) in enumerate(zip(rows, starts)):
        start = letters[at][0] if k else 0
        # A line opens with the bracket or quote the book printed there, not with its first
        # letter: `(Figure 2.1)`, `(1898)`, `"virus"` began on the next line in the book and
        # left their `(` / `"` dangling at the end of the line above.
        # OPENING marks only: a `/` or `-` ending the line above stays there (`categories/`).
        while k and start > 0 and body[start - 1] in "([{“‘\"'":
            start -= 1
        # ...and so does a SYMBOL printed in the gap before a piece. The book draws `♂`, `♀`,
        # `⚥` as glyphs outside the text layer's line pieces (BIO11L ch05 p067), so a piece
        # starts at `for male` and the slice before it ends `... ovary, ♂ ` -- the symbol
        # printed at the end of the wrong piece and `♀` closed the line above instead of
        # opening its own. A symbol token just before a piece starts that piece, and the
        # piece's box reaches back into the gap (or to the margin, at a line's start).
        bbox = list(r["bbox"])
        if k and start > 0:
            j = start
            while j > 0 and body[j - 1].isspace():
                j -= 1
            i = j
            while i > 0 and unicodedata.category(body[i - 1]).startswith("S"):
                i -= 1
            if i < j and (i == 0 or body[i - 1].isspace()):
                start = i
                prev = out[-1] if out else None
                if prev and prev["row"] == r["row"]:
                    bbox[0] = round(prev["bbox"][2] + 0.002, 4)
                else:
                    bbox[0] = round(min(x["bbox"][0] for x in rows), 4)
        out.append({"from": start, "row": r["row"], "solo": r["solo"],
                    "hyphen": r["text"].rstrip().endswith("-"), "bbox": bbox})
    return out


def _apply_line_geom(tree):
    """Turn each node's measured `_print_rows` into `line_geom` against its FINAL body.

    Run after every pass that edits text (`_clean_text` adds a sentence space, `_despace`
    closes tracking), because the offsets index the body as it will be written. Prose printed
    on one page only: a paragraph stitched across a page break carries its first page's lines.
    """
    for n in _walk_nodes(tree):
        # A caption's lines, against the FINAL caption (`_line_geom` refuses a caption that
        # has since grown -- a folded `(a) ...` line -- so a wrong line is never placed).
        crows = n.pop("_caption_rows", None)
        if crows and n.get("caption") and n.get("caption_box"):
            cg = _line_geom(crows, n["caption"])
            if cg:
                n["caption_line_geom"] = cg
        rows = n.pop("_print_rows", None)
        if (rows and n.get("kind") in ("para", "box", "list") and len(n.get("boxes") or []) == 1
                and not n.get("char_ranges")):
            geom = _line_geom(rows, n.get("body") or "")
            if geom:
                n["line_geom"] = geom
        # A PARAGRAPH ACROSS A PAGE BREAK, placed line by line on BOTH pages. Only its first
        # page used to be measured; the continuation was reflowed in the substitute font and
        # on BIO11L ch02 p012 wrapped one line longer than the book, over the next paragraph.
        # `frag_line_geom[i]` indexes the slice `body[char_ranges[i]]`, as the render cuts it.
        frows = n.pop("_frag_rows", None)
        rngs = n.get("char_ranges") or []
        if frows and len(frows) == len(rngs) == len(n.get("boxes") or []):
            body = n.get("body") or ""
            fg = [(_line_geom(fr, body[r["from"]:min(r["to"], len(body))]) if fr else None)
                  for fr, r in zip(frows, rngs)]
            # A FRAGMENT OF ONE PRINTED LINE is that line, at its measured box. `the following
            # key events:` opens BIO11L ch10 p124; with no geometry (one row is not enough for
            # `_line_geom`) it was flowed justified in its short box, wrapped to two lines and
            # printed over the bullet below.
            # (`_print_rows` keeps no rows for a one-line block, so the line is its box: a box one
            # line deep holding a short piece of text.)
            for k, r in enumerate(rngs):
                bx = (n["boxes"][k] or {}).get("bbox")
                if (fg[k] is None and bx and 0 < r["to"] - r["from"] <= 90
                        and bx[3] - bx[1] < 0.025):
                    fg[k] = [{"from": 0, "row": 0, "solo": True, "hyphen": False,
                              "bbox": list(bx)}]
            if any(fg):
                n["frag_line_geom"] = fg


_BULLET_ONLY = re.compile(r"[\s•●▪■◦]+")


def _typography(el, body):
    """The ink, face and size the book printed this block in, and where its lines break.

    All three are measured per run by the text layer and were dropped here, so the exact
    renderer guessed them from the block's KIND: every title came out blue and every block in
    Bookman. Measured on BIO11L ch01 p001, the unit opener prints `Unit 1` in AvantGarde-Book
    40pt and `DIVERSITY IN THE LIVING WORLD` in AvantGarde-Book 16pt, both in near-black
    #231f20 -- the guess made them blue serif, and at the box-fitted size `Unit 1` wrapped and
    printed its `1` on top of the subtitle. The most-printed value wins (by characters).

    `line_starts` -- where each printed line begins in `body` -- is recorded for SHORT blocks
    (titles, headings, captions, rail entries), so a renderer breaks them where the book does:
    the opener rail prints `Chapter 1` / `The Living World` on two lines, and run together and
    justified it spread across the rail. Long paragraphs are left to flow inside their measured
    box. A line start that cannot be found in the body records nothing rather than a guess.
    """
    fonts, inks, sizes = collections.Counter(), collections.Counter(), collections.Counter()
    emph = collections.Counter()
    for r in el.get("runs") or []:
        n = len((r.get("t") or "").strip())
        if not n:
            continue
        # A BULLET IS NOT THE BLOCK'S TYPE. BIO11L ch12 p161 prints its `•` markers in Bookman
        # 14pt beside 10.5pt items; when the bullet column was the measured run, the whole list
        # rendered at 14pt and its lines piled onto each other.
        if not _BULLET_ONLY.sub("", r.get("t") or ""):
            continue
        # THE BLOCK'S FACE IS ITS UNEMPHASISED TEXT'S. Bold and italic are carried by `marks`;
        # counting them here made `Examples: Pleurobrachia and Ctenoplana.` an italic block
        # (23 italic characters to 15 plain) and the renderer set the whole line italic. A
        # block with no plain text at all (a bold heading) falls back to its emphasised face.
        if r.get("font"):
            (emph if any(r.get(k) for k in ("b", "i", "sc", "script")) else fonts)[r["font"]] += n
        if r.get("color"):
            inks[r["color"]] += n
        if r.get("size"):
            sizes[round(float(r["size"]), 1)] += n
    out = {}
    if inks:
        out["ink"] = inks.most_common(1)[0][0]
    if fonts or emph:
        out["print_font"] = (fonts or emph).most_common(1)[0][0]
    # FAKE BOLD. NCERT thickens `4.2.11.1 Class -- Cyclostomata` by drawing its LightItalic text
    # five times over (`_drop_overprint` flags the kept copy bold). The face name says Light,
    # the page prints bold; with only the name, the render set every such heading light grey.
    bold = sum(len((r.get("t") or "").strip()) for r in el.get("runs") or [] if r.get("b"))
    total = sum(len((r.get("t") or "").strip()) for r in el.get("runs") or [])
    if (total and bold == total and out.get("print_font")
            and not re.search(r"Demi|Bold|Heavy|Black", out["print_font"])):
        out["print_bold"] = True
    if sizes:
        out["print_size_pt"] = sizes.most_common(1)[0][0]
    # THE FIRST-LINE INDENT, where the book set one: NCERT indents every paragraph but the first
    # after a heading (measured 18.5pt on BIO11L ch01 p004). The first line starting right of
    # every other line of the block is the indent; nothing is inferred for a one-line block.
    lb = sorted(el.get("line_boxes_pt") or [], key=lambda ln: ln["bbox_pt"][3])
    if len(lb) >= 2:
        indent = lb[0]["bbox_pt"][0] - min(ln["bbox_pt"][0] for ln in lb[1:])
        if 4.0 <= indent <= 40.0:
            out["first_indent_pt"] = round(indent, 1)
    rows = _printed_lines(el)
    if 2 <= len(rows) <= 4 and len(body) <= 200:
        # Matched on LETTERS ONLY, ignoring case and spacing: a small-caps title reaches the
        # text layer as `B IOLOGICAL  C LASSIFICATION` (the capital and the small capitals are
        # separate runs), which a plain substring search never finds in `Biological
        # Classification` -- so chapters 2 and 3 got no breaks and their titles wrapped over
        # the opening paragraph.
        letters = [(i, ch.lower()) for i, ch in enumerate(body) if ch.isalnum()]
        flat = "".join(ch for _i, ch in letters)
        starts, cursor = [], 0
        for text in rows[1:]:
            probe = "".join(ch.lower() for ch in text if ch.isalnum())[:10]
            at = flat.find(probe, cursor + 1) if probe else -1
            if at < 0:
                starts = []
                break
            # An opening bracket or quote glued to the line's first word starts the line with it:
            # matching on letters put the break after `(`, and `6.2.5 Dorsiventral (` /
            # `Dicotyledonous) Leaf` printed where the book sets `Dorsiventral` /
            # `(Dicotyledonous) Leaf` (BIO11L ch06 p076).
            s = letters[at][0]
            while s > 0 and body[s - 1] in "([{‘“\"'":
                s -= 1
            starts.append(s)
            cursor = at
        if starts:
            out["line_starts"] = starts
    return out


def build_tree(blocks, book_base, chapter_num):
    """Nest the flat block list under its numbered headings."""
    root = []
    # stack[d] = the children list to append to at heading depth d
    stack = {0: root}
    sections = {}          # depth -> the open section node

    pending_figures = []

    for b in blocks:
        el = b["el"]
        # `EXERCISES` AT TITLE SIZE IS STILL THE EXERCISES HEADING. Class 12 sets it in 30pt
        # orange AvantGarde, the chapter title's face, so it is classified `chapter_title` --
        # and BIO12L ch01 and ch02 then had no Exercises section at all: the heading sat
        # inside the last section (or the Summary), and no question was ever split out of the
        # 21 exercises under it. Only once a section has opened, so the opener's own
        # titles are never taken.
        as_heading = (el["role"] == "section_heading"
                      or (el["role"] == "chapter_title" and sections
                          and (ct.classify_heading(el.get("text") or "") or (1,))[0] is None))
        if as_heading:
            info = ct.classify_heading(el.get("text") or "")
            if info:
                number, title, depth = info
                parent = stack.get(depth, root)
                kind = "section"
                low = re.sub(r"[^a-z]", "", title.lower())
                if low in ct._UNNUMBERED:
                    kind = ct._UNNUMBERED[low]
                    depth = 0
                    parent = root
                node = {"kind": kind, "children": []}
                if number:
                    node["number"] = number
                node["title"] = title
                # THE TITLE'S OWN ITALIC. `5.8.1 The Lac operon` sets `Lac` italic inside the bold
                # heading (BIO12L ch05 p100); the title carried no marks, so it printed upright
                # in every output. Bold is the heading's face, so only italic is kept.
                _tb, _tm = ct.runs_to_body_marks(el.get("runs") or [])
                _at = _tb.find(title) if title else -1
                if _at >= 0:
                    _ti = [{"from": m["from"] - _at, "to": m["to"] - _at, "i": True}
                           for m in _tm if m.get("i") and m["from"] >= _at
                           and m["to"] <= _at + len(title)]
                    if _ti and sum(m["to"] - m["from"] for m in _ti) < 0.9 * len(title):
                        node["title_marks"] = _ti
                # The book sets this heading in SMALL CAPS (`1.1 Diversity in the Living World`,
                # `Summary`). The title carries no marks, so the face is said here -- without it
                # the render set the true-case title in ordinary capitals and lower case.
                _sc = sum(len((r.get("t") or "").strip()) for r in el.get("runs") or []
                          if r.get("sc"))
                if _sc and _sc >= 0.5 * len(re.sub(r"\s", "", title)):
                    node["small_caps"] = True
                # The title is normalised (`Exercises`); Class 12 prints `EXERCISES` and
                # `SUMMARY` in plain capitals, not small caps. What it printed is kept for
                # the page render.
                _printed = re.sub(r"\s+", " ", el.get("text") or "").strip()
                if (not number and not node.get("small_caps") and _printed
                        and _printed != title):
                    node["printed_title"] = _printed
                node["boxes"] = [{"page": b["page"], "page_file": b.get("page_file"),
                                  "src": el.get("layout_source")
                                         or ("agent" if el.get("from_a2l") else "measured"),
                                  "bbox": [round(v, 4)
                                           for v in (el.get("bbox_sheet") or el["bbox"])]}]
                # A SECTION HEADING IS ON A PAGE TOO. Section nodes are built here rather
                # than through `node_from`, so they were the one kind that never received a
                # `page_file` -- and on a chapter whose pages print no folio (every textless
                # scan) that left them with no page key at all. The renderer buckets by page,
                # so all 13 headings of Class 12 ch01 fell into one bucket and the chapter
                # rendered as a single sheet with every section piled on top of the next.
                node["pages"] = [b["page"]] if b["page"] is not None else []
                node["page_file"] = b.get("page_file")
                node["source"] = ("page_image" if b.get("source") in ("a2-agent", "a2s-agent")
                                  else "text_layer")
                node["qa"] = "auto"
                if el.get("line_count"):
                    node["line_count"] = el["line_count"]
                node.update(_typography(el, " ".join(x for x in (number, title) if x)))
                parent.append(node)
                sections[depth] = node
                stack[depth + 1] = node["children"]
                for d in list(stack):
                    if d > depth + 1:
                        del stack[d]
                continue
        target = stack[max(stack)] if stack else root
        # the deepest OPEN container
        depth = max(d for d in stack)
        target = stack[depth]
        node = node_from(b, book_base, chapter_num, f"tmp{len(target)}")
        if node["kind"] in ("figure", "table"):
            pending_figures.append((node, target))
        target.append(node)

    _move_figures_to_first_mention(root)
    _assign_paths(root, book_base, chapter_num)
    return root


def _walk_nodes(nodes):
    for n in nodes:
        yield n
        if n.get("children"):
            yield from _walk_nodes(n["children"])


def _tagged(unit_nodes, tree):
    """One tree over the whole file, every node saying which part of the book it belongs to.

    Tagged HERE rather than where the nodes are built because the figure/caption merge and the
    section-promotion passes create nodes after the build: tagging earlier left 5 of 87 nodes
    with no `belongs` at all, and an untagged node is one the export cannot route.
    """
    _walk(unit_nodes, lambda n, _p: n.update(belongs="unit"))
    _walk(tree, lambda n, _p: n.update(belongs=n.get("belongs") or "chapter"))
    return unit_nodes + tree


def _walk(nodes, fn, parents=()):
    for n in nodes:
        fn(n, parents)
        if n.get("children"):
            _walk(n["children"], fn, parents + (n,))


# Split on the AGENT'S OWN line breaks first -- it put each question on its own line, so no
# guessing is needed. The sentence-boundary form below is the fallback for a block that
# reached us already flattened.
_Q_LINE = re.compile(r"(?:^|\n)\s*(\d{1,2})\.\s+")
_Q_SPLIT = re.compile(r"(?:(?<=^)|(?<=[.?!]\s))\s*(\d{1,2})\.\s+(?=[A-Z(])")


_TYPO_KEYS = ("ink", "print_font", "print_size_pt", "line_pitch_pt", "print_lines")


def _typography_of(n):
    """The measured type of the block a question was cut from. A question built as a new node
    lost it, fell back to the stylesheet's 10.5pt at 1.27 leading, and the exercises then ran
    taller than the book and over the imprint at the foot of BIO11L ch01 p009."""
    return {k: n[k] for k in _TYPO_KEYS if n.get(k) is not None}


def _question_text(it):
    """(body, marks, parts) of a list item that opens `N. `, with the number cut off.

    THE MARKS MOVE WITH THE TEXT. Cutting `5. ` off the front shifted the body three characters
    left and left the marks where they were, so BIO11L ch01's question 5 carried an italic mark
    three characters late and running past the end of its body -- and `body_md` was built from
    the plain text, so it printed no italics at all.

    THE BOOK'S OWN SUB-LINES ARE PARTS. Question 5 prints `Mangifera Indica` and `Mangifera
    indica` on lines of their own, each wholly italic -- two names to choose between, not the
    end of a sentence. A2 keeps each printed line, so trailing lines that are wholly emphasised
    become `parts`, the way question 7's (a)(b)(c) do.
    """
    lines = it.get("_lines") or [(it.get("body") or "", it.get("marks") or [])]
    lines = [(b, mk) for b, mk in lines if b.strip()]

    def whole(b, mk):
        s, e = len(b) - len(b.lstrip()), len(b.rstrip())
        return any(x["from"] <= s and x["to"] >= e and (x.get("i") or x.get("b")) for x in mk)

    parts = []
    while len(lines) > 1 and whole(*lines[-1]):
        b, mk = lines.pop()
        parts.insert(0, {"body": b.strip(), "marks": mk, "body_md": ct.to_body_md(b.strip(), mk)})
    if parts:
        body, marks = "", []
        for b, mk in lines:
            off = len(body) + (1 if body else 0)
            body = f"{body} {b}" if body else b
            marks += [dict(x, **{"from": x["from"] + off, "to": x["to"] + off}) for x in mk]
    else:
        body, marks = it.get("body") or "", it.get("marks") or []
    m = re.match(r"^\s*\d{1,2}\s*[.)]\s+", body)
    cut = m.end() if m else 0
    text = body[cut:].rstrip()
    marks = [dict(x, **{"from": max(0, x["from"] - cut), "to": min(len(text), x["to"] - cut)})
             for x in marks if x["to"] - cut > 0 and x["from"] - cut < len(text)]
    return text, [x for x in marks if x["to"] > x["from"]], parts


def _drop_item_lines(n, _p):
    for it in n.get("items") or []:
        it.pop("_lines", None)


def _split_exercise_questions(root, book_base, chapter_num):
    """Ten exercise questions are TEN nodes, not one paragraph.

    NCERT prints `Exercises` as a numbered list and the text layer returns the whole run as one
    block, so the chapter ended with a single 1,400-character paragraph reading
    `1. Why are living organisms classified? 2. Why are the classification systems changing
    every now and then? 3. ...` -- unquotable, unlinkable, and wrong: the schema gives each
    question its own node (`N#005.001` ... `N#005.010`) precisely so a PYQ can cite one.

    Split on a number followed by a full stop at a sentence boundary, which is what the book
    prints and what distinguishes `10.` starting a question from `1.7-1.8 million` inside one.
    """
    # The highest question number emitted so far in the Exercises section being walked, so a
    # later block that continues the run (6, 7, 8 ...) is recognised instead of rejected.
    _q_seen = [0]

    def rec(nodes, parents):
        for n in list(nodes):
            if n.get("children"):
                rec(n["children"], parents + (n,))
        if not parents or parents[-1].get("kind") != "exercises":
            return
        _q_seen[0] = 0
        out = []
        for n in nodes:
            body = n.get("body") or ""
            # PHYSICS NUMBERS ITS EXERCISES `1.1` ... `1.17` (chapter.question), one block each
            # (`extract_page_layout._split_numbered_exercises`). The question keeps the printed
            # number and everything the node measured; its marks move with the text.
            phys = re.match(r"^\s*(%d\.\d{1,2})\s+(.*\S)\s*$" % chapter_num, body, re.S)
            num_re = re.compile(r"^\s*(%d\.\d{1,2})\s+(.*\S)\s*$" % chapter_num, re.S)
            if phys and n["kind"] == "list" and n.get("items"):
                # A run of exercises collapsed into one list (`collapse_lists`): a question at
                # every item that opens with `C.k`, its (a), (b) ... items joining it.
                own = (n.get("boxes") if len(n.get("boxes") or []) == len(n["items"]) else None)
                # ...or one box per QUESTION: each exercise was cut as its own block
                # (`_split_numbered_exercises`), so p011's 11 boxes are its 11 exercises.
                heads = [k for k, it in enumerate(n["items"])
                         if num_re.match((it.get("body") or "").strip())]
                per_q = (n.get("boxes") if not own and len(n.get("boxes") or []) == len(heads)
                         else None)
                cur = None
                for k_it, it in enumerate(n["items"]):
                    raw_t = it.get("body") or ""
                    t = raw_t.strip()
                    lead_ws = len(raw_t) - len(raw_t.lstrip())
                    m = num_re.match(t)
                    # the item's marks (m², s⁻², italic α) move with its text
                    cut = m.start(2) if m else 0
                    it_marks = [dict(mk, **{"from": mk["from"] - lead_ws - cut,
                                            "to": mk["to"] - lead_ws - cut})
                                for mk in it.get("marks") or [] if mk["from"] - lead_ws >= cut]
                    if not m and cur is not None:
                        off = len(cur["body"]) + 1
                        cur["marks"] += [dict(mk, **{"from": mk["from"] + off, "to": mk["to"] + off})
                                         for mk in it_marks]
                    if m or cur is None:
                        cur = {"kind": "question", "number": m.group(1) if m else None,
                               "body": m.group(2) if m else t,
                               "pages": n.get("pages"), "page_file": n.get("page_file"),
                               "boxes": ([own[k_it]] if own else
                                         [per_q[heads.index(k_it)]] if per_q and k_it in heads
                                         else n.get("boxes")),
                               "belongs": n.get("belongs"), "source": n.get("source"),
                               "qa": n.get("qa", "auto"), "marks": it_marks,
                               "id": ct.stable_id("question", book_base, chapter_num,
                                                  f"{n.get('path', 'x')}.{k_it}"),
                               **_typography_of(n)}
                        out.append(cur)
                    else:
                        cur["body"] = cur["body"] + "\n" + t
                        if own:
                            cur["boxes"] = cur["boxes"] + [own[k_it]]
                for q in out:
                    if q.get("kind") == "question" and "body_md" not in q:
                        q["body_md"] = ct.to_body_md(q["body"], q["marks"])
                        q["sentences"] = ct.split_sentences(q["body"])
                continue
            if phys and n["kind"] in ("para", "box", "list"):
                at = phys.start(2)
                q = {k: v for k, v in n.items() if k not in ("items", "line_geom")}
                q.update(kind="question", number=phys.group(1), body=phys.group(2),
                         marks=[dict(mk, **{"from": mk["from"] - at, "to": mk["to"] - at})
                                for mk in n.get("marks") or [] if mk["from"] >= at],
                         id=ct.stable_id("question", book_base, chapter_num,
                                         f"{n.get('path', 'x')}.{phys.group(1)}"))
                q["body_md"] = ct.to_body_md(q["body"], q["marks"])
                q["sentences"] = ct.split_sentences(q["body"])
                out.append(q)
                continue
            # ONE BLOCK CAN BE EXACTLY ONE QUESTION.
            #
            # The text layer can return each exercise as its own block, and the paths below only
            # accept a block holding two or more. Measured on BIO11L ch03: questions 2, 3 and 4
            # arrived one per block and were each flagged NEEDS_AGENT_SPLIT, the count of
            # questions seen stayed at 0, and the block carrying 5-9 was then rejected for not
            # starting at 1 -- so five questions printed as one run-on paragraph. A block that
            # opens with the next expected number and holds no further number in sequence is
            # one whole question; its marks are re-based onto the question's own text.
            # The full stop may be missing on the NEXT expected number only: BIO12L ch05 prints
            # `1 Group the following ...`, and question 1 stayed a paragraph.
            one = (re.match(r"^\s*(\d{1,2})\.\s+(.*\S)\s*$", body, re.S)
                   or re.match(r"^\s*(%d)\s+([A-Z].*\S)\s*$" % (_q_seen[0] + 1), body, re.S))
            if (one and n["kind"] in ("para", "box", "list")
                    and int(one.group(1)) in (1, _q_seen[0] + 1)
                    and not re.search(r"(?<![\d.])%d\.\s+" % (int(one.group(1)) + 1),
                                      one.group(2))):
                num, text, at = one.group(1), one.group(2), one.start(2)
                marks = [dict(mk, **{"from": mk["from"] - at, "to": mk["to"] - at})
                         for mk in n.get("marks") or []
                         if mk["from"] >= at and mk["to"] <= at + len(text)]
                out.append({"kind": "question", "number": num, "body": text,
                            "body_md": ct.to_body_md(text, marks), "marks": marks,
                            "sentences": ct.split_sentences(text),
                            "pages": n.get("pages"), "boxes": n.get("boxes"),
                            "page_file": n.get("page_file"),
                            "id": ct.stable_id("question", book_base, chapter_num,
                                               f"{n.get('path','x')}.{num}"),
                            "belongs": n.get("belongs"),
                            "source": n.get("source"), "qa": n.get("qa", "auto"),
                            **_typography_of(n)})
                _q_seen[0] = int(num)
                continue
            # The run of questions can arrive typed as a `box` or a `list` as well as a
            # `para` -- what matters is that it is a block of text inside `Exercises`, not
            # which role the size-and-position heuristic happened to give it.
            # A NUMBERED LIST INSIDE EXERCISES *IS* THE QUESTIONS.
            # Its `body` is empty -- the text lives in `items` -- so the length guard below
            # rejected it before the items were ever looked at, and six of eleven exercises
            # stayed a bulleted list with no numbers. Each item that opens with "N." is one
            # question; items that do not are sub-parts of the question above them, which is
            # exactly how the book sets (a)(b)(c) under question 7 and (i)-(v) under 9.
            if n["kind"] == "list" and n.get("items"):
                made, last = [], None
                # Each item's OWN measured box when the list has one per item -- a question cut
                # from a list must be placed where it printed, not at the list's first box.
                own = (n.get("boxes") if len(n.get("boxes") or []) == len(n["items"]) else None)
                for k_it, it in enumerate(n["items"]):
                    t = (it.get("body") or "").strip()
                    m = re.match(r"^(\d{1,2})\s*[.)]\s+(.*)$", t, re.S)
                    if m and (last is None or int(m.group(1)) == int(last["number"]) + 1):
                        q_body, q_marks, q_parts = _question_text(it)
                        last = {"kind": "question", "number": m.group(1),
                                "body": q_body, "body_md": ct.to_body_md(q_body, q_marks),
                                "marks": q_marks,
                                "sentences": ct.split_sentences(q_body),
                                "parts": q_parts,
                                "pages": n.get("pages"),
                                "boxes": [own[k_it]] if own else n.get("boxes"),
                                "page_file": n.get("page_file"),
                                "id": ct.stable_id("question", book_base, chapter_num,
                                                   f"{n.get('path','x')}.{m.group(1)}"),
                                "belongs": n.get("belongs"),
                                "source": n.get("source"), "qa": n.get("qa", "auto"),
                            **_typography_of(n)}
                        made.append(last)
                    elif last is not None and t:
                        last["parts"].append({"body": t, "marks": it.get("marks") or []})
                    # A LIST THAT OPENS ON A SUB-PART CONTINUES THE QUESTION BEFORE IT.
                    # BIO12L ch02's question 1 prints (a)-(e) on p039 and (f)-(k) on p040;
                    # the second page's list starts `(f)`, so with no question open yet its
                    # six parts became loose paragraphs and questions 2-21 were rejected.
                    elif (t and not made and out and out[-1].get("kind") == "question"
                          and re.match(r"^\s*\((?:[a-z]|[ivx]{1,5})\)", t)):
                        # The question's own (a)-(e) may still sit in its body, waiting for
                        # `_split_parts` -- which skips a question that already has parts. Split
                        # them out first, so (f) follows (e) instead of (a)-(e) staying inline.
                        if not out[-1].get("parts"):
                            _split_parts(out[-1], None)
                        # The part printed on THIS list's page, not the question's: the render
                        # draws it there (p040's (f)-(k) under p039's question 1).
                        part = {"body": t, "marks": it.get("marks") or []}
                        if n.get("page_file") != out[-1].get("page_file"):
                            part["page_file"] = n.get("page_file")
                            part["region"] = ((own[k_it] if own else (n.get("boxes") or [{}])[0])
                                              .get("bbox"))
                        out[-1].setdefault("parts", []).append(part)
                    elif t:
                        made.append({**n, "kind": "para", "items": None, "body": t})
                # ONE question is enough when it continues the run: BIO11L ch03's exercise 11 is
                # the only numbered item left in its list once the match table above it is
                # recognised, and requiring two left it a bulleted list item.
                qs = [x for x in made if x.get("kind") == "question"]
                # ...but only a GENUINELY single question: one item holding `1. ...\n2. ...`
                # is a whole run still to be split below.
                if len(qs) >= 2 or (len(qs) == 1 and not re.search(
                        r"(?<![\d.])%d\.\s" % (int(qs[0]["number"]) + 1), qs[0]["body"])):
                    nums_l = [int(x["number"]) for x in made if x.get("kind") == "question"]
                    if nums_l[0] in (1, _q_seen[0] + 1):
                        out.extend(made)
                        _q_seen[0] = nums_l[-1]
                        continue
            if n["kind"] not in ("para", "box", "list") or len(body) < 80:
                out.append(n)
                continue
            if not body and n.get("items"):
                body = " ".join(i.get("body", "") for i in n["items"])
            parts = _Q_LINE.split(body)
            if len(parts) < 5:
                parts = _Q_SPLIT.split(body)
            # SCAN FOR THE NEXT EXPECTED NUMBER, rather than for "a number at a boundary".
            #
            # Both regexes above need a sentence boundary before the numeral, and three of
            # BIO11L ch01's ten exercises do not have one: question 6 follows "Mangifera
            # indica", 8 follows "(c) Species Genus Order Phylum", 10 follows "(v) Genus".
            # They were silently dropped, leaving the split [1,2,3,4,5,7,9] -- and because
            # that has gaps the whole block was then left unsplit, so the page rendered as one
            # run-on paragraph with no question numbers at all.
            #
            # Exercises are numbered 1..N consecutively, which is a far stronger constraint
            # than any boundary rule: look for "6." only once 5 has been found, and the
            # ambiguity disappears. "1.7-1.8 million" cannot match, because by then the scan
            # is looking for a different number entirely.
            # The scan starts at the NEXT EXPECTED number, not at 1, and runs EVERY time. BIO11L
            # ch03's 5-10 continue a run whose 1-4 arrived as blocks of their own; the boundary
            # split found 5, 6, 7, 8 and stopped, because "(vi) isogamy 9." has no full stop
            # before the numeral -- and 5-8 is contiguous, so it passed the gap check and 9 and
            # 10 were left inside question 8. A boundary split can be contiguous AND short; the
            # sequential scan cannot be fooled by a missing full stop, so the longer run wins.
            first = _q_seen[0] + 1
            found = (len(parts) - 1) // 2
            scan, pos, want_n = [], 0, first
            while True:
                m = re.compile(r"(?<![\d.])" + str(want_n) + r"\.\s+").search(body, pos)
                if not m:
                    break
                scan.append((want_n, m.start(), m.end()))
                pos, want_n = m.end(), want_n + 1
            if len(scan) >= 3 and len(scan) > found:
                rebuilt = [body[:scan[0][1]]]
                for i, (num_i, _st, en) in enumerate(scan):
                    nxt = scan[i + 1][1] if i + 1 < len(scan) else len(body)
                    rebuilt += [str(num_i), body[en:nxt].strip()]
                parts = rebuilt
            # A SPLIT THAT SKIPS A NUMBER IS A WRONG SPLIT. Measured on BIO11L ch01, the page
            # prints ten exercises and the regex found 1,2,3,4,5,7,9 -- because question 5
            # carries two italic sub-lines, 7 carries options (a)(b)(c) and 9 carries (i)-(v),
            # and no rule about digits and full stops can tell a question number from a
            # sub-part. Seven questions with three silently missing is worse than one
            # unsplit block: the block is obviously unfinished, the seven look complete.
            # So the split only stands when the numbers run 1..N with no gaps; otherwise the
            # block is left whole and flagged for the agent, whose brief now asks it to return
            # one block per question.
            nums = [int(parts[i]) for i in range(1, len(parts) - 1, 2)]
            # A RUN MAY CONTINUE AN EARLIER BLOCK. The guard below used to demand the numbers
            # start at 1, which is right for the first block of an Exercises section and wrong
            # for every later one: BIO11O ch01 prints questions 1-11, the agent returned 1-5
            # as their own blocks and 6-11 as one more, and that second block was rejected for
            # starting at 6. Six of eleven exercises then stayed inside a list node and lost
            # their numbers. What matters is that the run is CONTIGUOUS and continues where
            # the section left off, not that it begins at one.
            want = _q_seen[0] + 1
            if not nums or nums != list(range(nums[0], nums[0] + len(nums))) \
                    or nums[0] not in (1, want):
                n["needs_agent_split"] = True
                n["split_attempt"] = nums
                out.append(n)
                continue
            if len(parts) < 5:                      # fewer than two questions -- leave it
                out.append(n)
                continue
            lead = parts[0].strip()
            if lead:
                out.append({**n, "body": lead, "body_md": lead,
                            "sentences": ct.split_sentences(lead)})
            for i in range(1, len(parts) - 1, 2):
                num, text = parts[i], parts[i + 1].strip()
                if not text:
                    continue
                out.append({"kind": "question", "number": num, "body": text,
                            "body_md": text, "marks": [],
                            "sentences": ct.split_sentences(text),
                            "pages": n.get("pages"), "boxes": n.get("boxes"),
                            "page_file": n.get("page_file"),
                            "id": ct.stable_id("question", book_base, chapter_num,
                                               f"{n.get('path','x')}.{num}"),
                            "source": n.get("source"), "qa": n.get("qa", "auto"),
                            **_typography_of(n)})
                _q_seen[0] = int(num)
        nodes[:] = out

    rec(root, ())


_PART_LEAD = re.compile(r"^\s*\((?:[a-h]|i{1,3}|iv|v|vi{0,3}|ix|x)\)\s*")


def _mark_inline_parts(nn, _p):
    """`parts_inline` when the book printed two or more of a question's sub-parts on ONE line.

    Measured on BIO11L ch01 p009: question 9 prints `(i) Phylum (ii) Class (iii) Family
    (iv) Order (v) Genus` on a single line, while question 7 sets (a), (b), (c) one per line.
    Drawn one per line, question 9 alone took five lines for the book's one and pushed
    question 10 off the foot of the sheet, over the imprint. A part is matched to a printed
    line by its own opening words, so a label merely repeated elsewhere cannot decide it.
    Then `print_lines` is dropped: it existed only to make this decision.
    """
    lines = nn.pop("print_lines", None)
    if nn.get("kind") != "question" or not nn.get("parts") or not lines:
        return
    # Matched WITH ITS LABEL: question 7's options repeat the same words, so `Species Or` alone
    # was found inside option (b)'s line `(b) Genus Species Order Kingdom` and set three
    # one-per-line options on a single line. `(a) Species` cannot match a line that is (b).
    def norm(s):
        return re.sub(r"\s+", " ", s or "").strip()
    heads = [norm(sp.get("body"))[:12] for sp in nn["parts"]]
    heads = [h for h in heads if _PART_LEAD.match(h) and len(h) >= 6]
    if any(sum(1 for h in heads if h in norm(line)) >= 2 for line in lines):
        nn["parts_inline"] = True


# One row of a match-the-following question: `(a) Operculum` in column I, `(i) Ctenophora` in II.
_MATCH_ROW = re.compile(
    r"^\s*(\(\s?[a-h]\s?\)\s*\S.*?)\s+(\((?:i{1,3}|iv|vi{0,3}|ix|x)\)\s*\S.*)$")


def _match_columns(nn, _p):
    """A match-the-following question's parts are ROWS OF TWO COLUMNS, and say so.

    `(a) Operculum (i) Ctenophora` is one part, which is right -- the (i) is the second column,
    not a new part -- but as one string every consumer printed the two columns run together:
    question 14 (BIO11L ch04 p054) came out as eight lines of `(a) Operculum (i) Ctenophora`
    where the book sets two aligned columns. Each such part now carries `columns`
    [column I, column II] with each column's own marks, and the renderers lay them out as such.
    """
    if (nn.get("kind") != "question" or not nn.get("parts")
            or not re.search(r"\bmatch\b", nn.get("body") or "", re.I)):
        return
    hits = [(sp, _MATCH_ROW.match(sp.get("body") or "")) for sp in nn["parts"]]
    if sum(1 for _sp, m in hits if m) < 3:
        return
    for sp, m in hits:
        if not m:
            continue
        marks = sp.get("marks") or []
        cols, cmarks = [], []
        for g in (1, 2):
            a, z = m.start(g), m.end(g)
            text = m.group(g)
            cut = len(text) - len(text.rstrip())
            cols.append(text.rstrip())
            cmarks.append([{**mk, "from": max(mk["from"], a) - a,
                            "to": min(mk["to"], z - cut) - a}
                           for mk in marks if min(mk["to"], z - cut) > max(mk["from"], a)])
        sp["columns"] = cols
        sp["column_marks"] = cmarks


def _absorb_table_cells(tree):
    """Cells the table did not claim are part of the table, not paragraphs of their own.

    The extractor builds a table's region from its caption down, and stops at a gap. Measured on
    BIO11L ch02 p011, Table 2.1 claimed its header and first rows and left 22 cells -- `Present
    with chitin`, `Tissue/ organ`, `Mode of nutrition`, ... -- as loose nodes. A2S had
    transcribed the whole table correctly, so every one of them was printed twice: once in the
    grid and once as a stray block drawn over it, and the loose copies reached the Markdown and
    search as sentences NCERT never wrote.

    Only a table whose grid came from A2S does this, because only then is the full cell text
    known. A node is a cell when every word of it occurs in the grid's text, it is short, and it
    sits on the table's page inside its columns and below its caption. It is removed and its box
    joins the table's, so the table occupies the region the book printed it in.
    """
    def flat(s):
        return re.sub(r"[^a-z0-9]", "", (s or "").lower())

    tables = [n for n in _walk_nodes(tree) if n.get("kind") == "table"
              and (n.get("table_grid") or {}).get("source") == "a2s-agent" and n.get("boxes")]
    # TO A FIXPOINT. The table's box only reaches its last column once cells are absorbed: Table
    # 2.1's whole Animalia column (BIO11L ch02 p011) sat just past the box's first right edge and
    # survived one pass as four loose `box` nodes -- printed over the grid and repeated in the
    # Markdown under the table. Each pass widens the box; stop when one absorbs nothing.
    for t in tables:
        while _absorb_into(t, tree, flat):
            pass


def _absorb_into(t, tree, flat):
    """One pass of `_absorb_table_cells` for table `t`; True when it absorbed a cell."""
    soup = flat(" ".join(c for row in t["table_grid"]["cells"] for c in row if c))
    first_col = {flat(row[0]) for row in t["table_grid"]["cells"] if row and row[0]}
    tb = t["boxes"][0]
    # A box may record only the printed folio (`page: 11`), so the page is resolved from
    # the box's file, else the node's file, else the folio -- for both sides of the test.
    def page_of(node, box):
        return box.get("page_file") or node.get("page_file") or box.get("page")
    pf, (x0, y0, x1, y1) = page_of(t, tb), tb["bbox"]
    absorbed = []

    def is_cell(n):
        if n is t or n.get("kind") not in ("para", "box") or n.get("children"):
            return False
        b = (n.get("boxes") or [{}])[0]
        bb = b.get("bbox")
        if not bb or page_of(n, b) != pf:
            return False
        # A block that starts INSIDE the table's measured rows may run past its measured
        # right edge: that edge is the text layer's, and is short of the printed one. Table
        # 4.1's row 2 (BIO11L ch04 p010) reached x 0.861 against a table box ending at 0.757,
        # missed the 0.08 allowance, and printed a second time across the grid. Below the
        # rows the allowance stays tight, where the next column's prose can sit.
        reach = 0.95 if bb[1] <= y1 else x1 + 0.08
        # The LEFT edge is short too. Table 4.2 (BIO11L ch04 p051) measured from its second
        # column, so its whole `Phylum` column -- Porifera ... Chordata -- stood beside the grid
        # as eleven loose paragraphs. A block left of the box is a cell only when it IS one of
        # the grid's first-column cells and sits within the rows.
        left_ok = (bb[1] <= y1 and bb[2] <= x0 + 0.02
                   and flat(n.get("body")) in first_col)
        # A table taller than half a page has rows below `y0 + 0.5`: Table 4.2's last row
        # (`Notochord, dorsal hollow nerve cord, ...`) started at 0.848 against a 0.846 limit.
        if (bb[1] < y0 or bb[1] > max(y0 + 0.5, y1 + 0.02)
                or (bb[0] < x0 - 0.02 and not left_ok) or bb[2] > reach):
            return False
        words = [flat(w) for w in (n.get("body") or "").split()]
        words = [w for w in words if w]
        return 0 < len(words) <= 25 and all(w in soup for w in words)

    def prune(nodes):
        out = []
        for n in nodes:
            if n.get("children"):
                n["children"] = prune(n["children"])
            if is_cell(n):
                absorbed.append(n)
                continue
            out.append(n)
        return out

    tree[:] = prune(tree)
    if absorbed:
        boxes = [tb["bbox"]] + [n["boxes"][0]["bbox"] for n in absorbed]
        tb["bbox"] = [round(min(b[0] for b in boxes), 4), round(min(b[1] for b in boxes), 4),
                      round(max(b[2] for b in boxes), 4), round(max(b[3] for b in boxes), 4)]
        t["cells_absorbed"] = t.get("cells_absorbed", 0) + len(absorbed)
    return bool(absorbed)


def _merge_figure_captions(root):
    """A figure's ARTWORK and its CAPTION are one piece, not two.

    The page prints `Figure 2.1 Bacteria of different shapes` under the drawing, and the two
    arrive as separate blocks: the artwork is an image with no text, the caption is text with
    no image. Both map to kind `figure`, so the tree ended up with a caption node carrying no
    picture and a picture node carrying no caption -- measured on BIO11O ch02, six of its
    thirteen figures came out that way, and the HTML rendered the caption as a stray bold line
    with the drawing somewhere else entirely.

    Merged on PAGE and proximity: a caption is matched to the nearest image-only figure on the
    same printed page. A caption with no artwork on its page keeps its own node rather than
    being attached to something further away -- a caption under the wrong picture is worse
    than a caption on its own.
    """
    captioned, artwork = [], []

    def collect(n, parents):
        if n.get("kind") not in ("figure", "table"):
            return
        has_img = bool(n.get("image_local"))
        has_cap = bool((n.get("caption") or "").strip())
        if has_cap and not has_img:
            captioned.append((n, parents))
        elif has_img and not has_cap:
            artwork.append((n, parents))
    _walk(root, collect)

    used = set()
    for cap_node, cap_parents in captioned:
        page = (cap_node.get("pages") or [None])[0]
        best, best_gap = None, None
        for art_node, art_parents in artwork:
            if id(art_node) in used:
                continue
            if page is None or page not in (art_node.get("pages") or []):
                continue
            a = (art_node.get("boxes") or [{}])[0].get("bbox", [0, 0, 0, 0])
            c = (cap_node.get("boxes") or [{}])[0].get("bbox", [0, 0, 0, 0])
            # THE EDGE-TO-EDGE GAP, AND ON THE SIDE THE BOOK PRINTS IT. NCERT sets a figure's
            # caption UNDER or BESIDE its artwork and a table's caption ABOVE it. Matching top
            # to top paired `Figure 4.1 (a) Radial symmetry` with the crab printed under it
            # (BIO11L ch04 p002), and every caption on the page then took the next picture
            # down. Artwork on the wrong side is only taken when nothing else is on the page.
            dx = max(0.0, max(a[0], c[0]) - min(a[2], c[2]))
            dy = max(0.0, max(a[1], c[1]) - min(a[3], c[3]))
            wrong_side = (a[1] >= c[3] - 0.005 if cap_node.get("kind") == "figure"
                          else a[3] <= c[1] + 0.005)
            gap = (dx * dx + dy * dy) ** 0.5 + (1.0 if wrong_side else 0.0)
            if best_gap is None or gap < best_gap:
                best, best_gap, best_parents = art_node, gap, art_parents
        if best is None:
            continue
        used.add(id(best))
        best["caption"] = cap_node["caption"]
        if cap_node.get("caption_marks"):
            best["caption_marks"] = cap_node["caption_marks"]
        if cap_node.get("number"):
            best["number"] = cap_node["number"]
        best["boxes"] = (best.get("boxes") or []) + (cap_node.get("boxes") or [])
        # The caption's own measured box, named, so a renderer can set the caption where
        # the book prints it -- `boxes` is a list of where the node printed, not what printed.
        if cap_node.get("boxes"):
            best["caption_box"] = cap_node["boxes"][0]
            for k in ("ink", "print_font", "print_size_pt", "line_starts", "line_count",
                      "line_pitch_pt", "marks"):
                if cap_node.get(k) is not None:
                    best[f"caption_{k}"] = cap_node[k]
            if cap_node.get("_caption_rows"):
                best["_caption_rows"] = cap_node["_caption_rows"]
        best["pages"] = sorted({b["page"] for b in best["boxes"] if b.get("page")})
        owner = cap_parents[-1]["children"] if cap_parents else root
        if cap_node in owner:
            owner.remove(cap_node)


def _opener_figures_to_art(doc, layout):
    """The opener's captionless picture is the page's artwork, not a figure of the chapter.

    Class 12 sets a picture in the opener's green panel -- an embryo in the uterus (BIO12L
    ch02), fallopian tubes (ch03) -- with no number and no caption. As a figure it opened
    chapter.json's tree and chapter.md as an unlabelled image, and the render drew it as a
    figure box. It is drawn with the page's art instead, at its own paint order `z` (the
    extractor measured it: z 15, over the panel's z 1). A figure with no crop stays a node.
    """
    tree = doc.get("tree") or []
    opener = next((n.get("page_file") for n in tree
                   if n.get("kind") == "chapter_title" and n.get("belongs") != "unit"), None)
    if not opener:
        return
    z_of = {e.get("figure_file"): e.get("z")
            for p in layout["pages"] if p.get("page_file") == opener
            for e in p["elements_in_reading_order"]
            if e["role"] == "figure" and e.get("figure_file")}
    page = next((p for p in doc.get("pages") or [] if p.get("page_file") == opener), None)
    if page is None:
        return
    keep = []
    for n in tree:
        box = ((n.get("boxes") or [{}])[0]).get("bbox")
        if (n.get("kind") == "figure" and n.get("page_file") == opener and box
                and n.get("image_local") and not n.get("number")
                and not (n.get("caption") or "").strip()):
            page.setdefault("art", None)
            page["art"] = (page["art"] or []) + [{
                "kind": "opener art",
                "z": z_of.get(os.path.basename(n["image_local"])),
                "file": n["image_local"], "bbox": box}]
            continue
        keep.append(n)
    tree[:] = keep


def _late_opener_art(doc):
    """An opener picture found only by `crop_vector_figures` is the page's art too.

    The Unit 3 opener's cell illustration (BIO11L ch08 p001) is measured by A2L and cut there,
    after `_opener_figures_to_art` ran, so it stayed a captionless figure appended to the END
    of the tree: chapter.md showed it after the Exercises and A4 filed it under the nucleus.
    A captionless, unnumbered figure with a crop on a page that holds a chapter or unit title
    moves to that page's `art`, as the earlier pass does.
    """
    titles = {n.get("page_file") for n in _walk_nodes(doc["tree"]) if n.get("kind") == "chapter_title"}
    pages = {p.get("page_file"): p for p in doc.get("pages") or []}
    moved = set()
    for n in _walk_nodes(doc["tree"]):
        box = ((n.get("boxes") or [{}])[0]).get("bbox")
        src = n.get("image_local") or n.get("image")
        pf = n.get("page_file")
        if (n.get("kind") == "figure" and pf in titles and pf in pages and box and src
                and not n.get("number") and not n.get("panels")
                and not (n.get("caption") or "").strip()):
            page = pages[pf]
            page["art"] = (page.get("art") or []) + [
                {"kind": "opener art", "z": None, "file": src, "bbox": box}]
            moved.add(id(n))
    if not moved:
        return

    def prune(nodes):
        out = []
        for n in nodes:
            if n.get("children"):
                n["children"] = prune(n["children"])
            if id(n) not in moved:
                out.append(n)
        return out
    doc["tree"] = prune(doc["tree"])


def _borrow_furniture_decor(doc):
    """A page too heavy to measure takes its FURNITURE from the nearest page on its side.

    `page_decor` gives up on a page over 8 MB of drawing (Figure 2.9 and 2.11, BIO12L ch02
    p034/p036: 29 and 26 MB), so the page had no decor and the render fell back to Class 11's
    rounded folio tab. The tab and edge bands are the same on every verso (and every recto);
    only shapes touching the trim are borrowed, never a page's own boxes or tints, and each
    says where it came from.
    """
    pages = doc.get("pages") or []

    def edge(b):
        return b[0] <= 0.005 or b[1] <= 0.005 or b[2] >= 0.995 or b[3] >= 0.995

    measured = [j for j, q in enumerate(pages) if q.get("decor") and q.get("printed") is not None]
    for i, p in enumerate(pages):
        if p.get("decor") is not None or p.get("printed") is None:
            continue
        donors = sorted((abs(j - i), j) for j in measured
                        if pages[j].get("page_side") == p.get("page_side"))
        if not donors:
            continue
        src = pages[donors[0][1]]
        p["decor"] = [dict(d, borrowed_from=src["page_file"])
                      for d in src["decor"] if d.get("bbox") and edge(d["bbox"])]
        # ...and the CAPTION TINT, the one tint the design sets the same way everywhere: Class
        # 12 prints every figure caption on a #fff1e2 strip. Taken only when a measured page
        # shows a caption on one, with that page's own padding round the caption.
        tint = _caption_tint(doc, measured)
        if tint:
            fill, pad = tint
            for n in _walk_nodes(doc.get("tree") or []):
                cb = (n.get("caption_box") or {})
                if (n.get("kind") == "figure" and cb.get("bbox")
                        and (cb.get("page_file") or n.get("page_file")) == p["page_file"]):
                    b = cb["bbox"]
                    p["decor"].insert(0, {"z": 0, "kind": "panel", "fill": fill, "stroke": None,
                                          "width": None, "opacity": None, "radius": None,
                                          "bbox": [round(b[i] + pad[i], 4) for i in range(4)],
                                          "borrowed_from": "caption tint"})


def _caption_tint(doc, measured):
    """(fill, [dx0, dy0, dx1, dy1]) of the tint the book prints under figure captions, or None.

    Measured: a decor panel on a measured page that encloses a figure's caption box, closely.
    """
    pages = doc.get("pages") or []
    by_pf = {pages[j]["page_file"]: pages[j] for j in measured}
    for n in _walk_nodes(doc.get("tree") or []):
        cb = n.get("caption_box") or {}
        pg = by_pf.get(cb.get("page_file") or n.get("page_file"))
        if n.get("kind") != "figure" or not cb.get("bbox") or not pg:
            continue
        b = cb["bbox"]
        for d in pg.get("decor") or []:
            q = d.get("bbox")
            if (d.get("fill") and q and q[0] <= b[0] and q[1] <= b[1] and q[2] >= b[2]
                    and q[3] >= b[3] and (q[3] - q[1]) < 3 * (b[3] - b[1])):
                return d["fill"], [round(q[i] - b[i], 4) for i in range(4)]
    return None


def _drop_decor_inside_figures(doc):
    """Decor lying wholly inside a figure's artwork box belongs to the figure, not the page.

    The figure's crop already shows whatever printed there. `page_decor` reads shapes without
    their clip, so BIO12L ch02 p010 carried two peach rounded panels that Figure 2.10 draws
    and clips away -- the book shows nothing there, the render drew both over the ovum.
    """
    arts = {}
    for n in _walk_nodes(doc.get("tree") or []):
        if n.get("kind") != "figure":
            continue
        cap = (n.get("caption_box") or {}).get("bbox")
        for b in n.get("boxes") or []:
            if b.get("bbox") and b["bbox"] != cap:
                arts.setdefault(b.get("page_file") or n.get("page_file"), []).append(b["bbox"])

    def inside(a, f, tol=0.004):
        # Never page furniture: BIO12L ch03 p045's folio tab bleeds off the trim (x 1.038), and
        # a figure box reaching the page's empty corner took it, so the page printed no tab.
        if a[0] <= 0.005 or a[1] <= 0.005 or a[2] >= 0.995 or a[3] >= 0.995:
            return False
        return (a[0] >= f[0] - tol and a[1] >= f[1] - tol
                and a[2] <= f[2] + tol and a[3] <= f[3] + tol)

    for p in doc.get("pages") or []:
        figs = arts.get(p.get("page_file")) or []
        if p.get("decor") and figs:
            p["decor"] = [d for d in p["decor"]
                          if not (d.get("bbox") and any(inside(d["bbox"], f) for f in figs))]


def _drop_furniture_figures(doc):
    """A captionless "figure" standing exactly on the page's QR code or banner is that furniture.

    The opener's QR code is an embedded image, so the extractor made a figure of it AS WELL AS
    the `qr code` furniture the page record carries (BIO11L ch02 p010). It printed twice in the
    exact render, reached the Markdown as an unlabelled picture at the top of the chapter, and
    was filed into a passage about viruses. Furniture is drawn from `pages[].art`; the figure is
    the duplicate.
    """
    furn = {}
    for p in doc.get("pages") or []:
        for f in (p.get("furniture") or []) + (p.get("art") or []):
            if f.get("kind") in ("qr code", "header art", "page ground") and f.get("bbox"):
                furn.setdefault(p.get("page_file"), []).append(f["bbox"])

    def iou(a, b):
        ix = max(0.0, min(a[2], b[2]) - max(a[0], b[0]))
        iy = max(0.0, min(a[3], b[3]) - max(a[1], b[1]))
        inter = ix * iy
        union = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter
        return inter / union if union > 0 else 0.0

    def prune(nodes):
        out = []
        for n in nodes:
            if n.get("children"):
                n["children"] = prune(n["children"])
            b0 = (n.get("boxes") or [{}])[0]
            if (n.get("kind") == "figure" and not (n.get("caption") or "").strip()
                    and b0.get("bbox") and any(
                        iou(b0["bbox"], fb) > 0.7
                        for fb in furn.get(b0.get("page_file") or n.get("page_file"), []))):
                continue
            out.append(n)
        return out

    doc["tree"] = prune(doc["tree"])


def _inherit_table_fill(tree):
    """A table whose tint was never measured takes the tint the book gives its other tables.

    Table 9.5 (BIO11L ch09 p109) was cut as a picture, so its element carried no `table_fill`;
    A2S's grid then made it a table, and the render set it plain -- no peach ground, no rules --
    beside Table 9.4's tinted grid. Every NCERT table in a book shares one tint.
    """
    tables = [n for n in _walk_nodes(tree) if n.get("kind") == "table"]
    fills = collections.Counter(n["table_fill"] for n in tables if n.get("table_fill"))
    if not fills:
        return
    fill = fills.most_common(1)[0][0]
    for n in tables:
        if not n.get("table_fill") and (n.get("table_grid") or {}).get("cells"):
            n["table_fill"] = fill
            n["table_fill_source"] = "inherited"


def _stack_bullet_boxes(tree):
    """A bulleted list whose items were separate blocks prints in ONE box, one row per item.

    BIO11L ch10 p121's `G1 phase` / `S phase` / `G2 phase` arrived as three one-line blocks; the
    list kept three boxes, and the render squeezed all three rows into the first one-line box.
    Boxes stacked one under the next on one page (gap under a line) become their union.
    """
    for n in _walk_nodes(tree):
        bx = n.get("boxes") or []
        if n.get("kind") != "list" or not n.get("marker") or len(bx) < 2:
            continue
        if len({b.get("page_file") for b in bx}) != 1 or n.get("char_ranges"):
            continue
        bb = sorted((b["bbox"] for b in bx), key=lambda b: b[1])
        line = min(b[3] - b[1] for b in bb)
        if any(bb[i + 1][1] - bb[i][3] > line for i in range(len(bb) - 1)):
            continue
        n["boxes"] = [dict(bx[0], bbox=[round(min(b[0] for b in bb), 4), round(bb[0][1], 4),
                                        round(max(b[2] for b in bb), 4), round(bb[-1][3], 4)])]
        n["line_count"] = max(n.get("line_count") or 0, len(n.get("items") or []))
        n.pop("line_geom", None)


def _nest_unnumbered_subheads(tree):
    """An unnumbered heading inside a numbered section HEADS the content printed under it.

    5.9 Solanaceae (BIO11L ch05 p068-069) prints `Vegetative Characters`, `Floral Characters` and
    `Economic Importance` over their own lines, but the tree held each heading as a childless
    sibling of those lines -- so A3 saw three sections holding only a heading, and every
    consumer that reads a section's children found nothing under them. Following siblings up to
    the next heading move under it. A one-letter "heading" (a stray symbol, BIO11L ch09 `P`, `t`)
    is not a title and takes nothing.
    """
    def is_title(n):
        t = (n.get("title") or n.get("body") or "").strip()
        return len(re.findall(r"[A-Za-z]", t)) >= 6 or len(t.split()) >= 2

    def rec(nodes, numbered_parent):
        i = 0
        while i < len(nodes):
            n = nodes[i]
            if n.get("children"):
                rec(n["children"], bool(n.get("number")) and n.get("kind") == "section")
            if (numbered_parent and n.get("kind") == "section" and not n.get("number")
                    and not n.get("children") and is_title(n)):
                j = i + 1
                while j < len(nodes) and nodes[j].get("kind") not in (
                        "section", "summary", "exercises", "chapter_title"):
                    j += 1
                if j > i + 1:
                    n["children"] = nodes[i + 1:j]
                    del nodes[i + 1:j]
            i += 1
    rec(tree, False)


def _drop_layer_duplicates(doc):
    """A text-layer leftover whose words an agent-read paragraph on its page already holds.

    BIO11L ch08 p098 printed `composed of ribonucleic acid (RNA) and proteins and are not
    surrounded by any membrane.` twice -- once as the end of the agent's Ribosomes paragraph and
    again as a loose text-layer block: the layer had split the paragraph at an inset figure and
    the join absorbed only the first piece. A `text_layer` para or box of >= 25 letters, all of
    which occur in order inside another node's body on the same page, is that copy and goes.
    """
    # Compared through NFKC: the agent's caption holds `CO₂`, the layer's copy `CO2`.
    def flat(s):
        return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKC", s or "").lower())
    # A CAPTION KEEPS ITS OWN TAIL TOO. Figure 11.8's caption (BIO11L ch11 p144) runs five lines;
    # its measured box held the first, the layer left lines 2-5 as a loose paragraph, and the
    # page printed them twice -- once crammed into the caption's one-line box, once below it.
    def text(k):
        return k.get("body") if k.get("source") == "page_image" and k.get("body") else k.get("caption")
    nodes = list(_walk_nodes(doc["tree"]))
    by_page = collections.defaultdict(list)
    for n in nodes:
        if text(n):
            for pf in {b.get("page_file") for b in n.get("boxes") or []} | {n.get("page_file")}:
                by_page[pf].append(n)
    gone = set()
    for n in nodes:
        if n.get("kind") not in ("para", "box") or n.get("source") != "text_layer":
            continue
        t = flat(n.get("body"))
        # A LEFTOVER WITH NO WORD IN IT IS A STRAY GLYPH. BIO11L ch14 p190 set the minus of
        # `forms HCO3- and H+` on a line of its own in the layer; the agent's paragraph holds
        # it, and the lone `–` became a box node of its own in all three files.
        if not t:
            gone.add(id(n))
            continue
        keep = next((k for k in by_page.get(n.get("page_file"), []) if k is not n
                     and t in flat(text(k))), None)
        # A caption's tail may be short -- `between C3 and C4 Plants`, Table 11.1's second
        # line -- and is still that caption's: the 25-letter floor guards running prose only.
        if keep is None or len(t) < (12 if text(keep) == keep.get("caption") else 25):
            continue
        gone.add(id(n))
        if not (keep.get("source") == "page_image" and keep.get("body")):
            cb, b0 = keep.get("caption_box"), (n.get("boxes") or [None])[0]
            if cb and b0 and b0.get("page_file") == cb.get("page_file"):
                a, c = cb["bbox"], b0["bbox"]
                merged = [min(a[0], c[0]), min(a[1], c[1]), max(a[2], c[2]), max(a[3], c[3])]
                for bx in keep.get("boxes") or []:
                    if bx.get("bbox") == a:
                        bx["bbox"] = merged
                cb["bbox"] = merged
                keep["caption_line_count"] = ((keep.get("caption_line_count") or 1)
                                              + (n.get("line_count") or 1))
                for k in ("caption_line_starts", "caption_line_geom"):
                    keep.pop(k, None)
            continue
        # ITS BOX IS WHERE THE KEEPER'S TAIL PRINTS. The Ribosomes paragraph's measured box
        # holds its first two lines; the last two are set beside Figure 8.9, in the copy's box.
        # Dropped with the copy, the render squeezed four lines into two. When the copy is the
        # keeper's END and the keeper has one box, the copy's box becomes its second fragment.
        tail = (n.get("body") or "").strip()
        body = (keep.get("body") or "").rstrip()
        b0 = (n.get("boxes") or [None])[0]
        if (tail and body.endswith(tail) and len(keep.get("boxes") or []) == 1
                and not keep.get("char_ranges") and b0):
            cut = len(body) - len(tail)
            keep["boxes"] = keep["boxes"] + [dict(b0)]
            keep["char_ranges"] = [
                {"page": keep["boxes"][0].get("page"), "page_file": keep["boxes"][0].get("page_file"),
                 "from": 0, "to": cut},
                {"page": b0.get("page"), "page_file": b0.get("page_file"),
                 "from": cut, "to": len(keep["body"])}]
            keep.pop("line_geom", None)
    if not gone:
        return

    def prune(ns):
        out = []
        for n in ns:
            if n.get("children"):
                n["children"] = prune(n["children"])
            if id(n) not in gone:
                out.append(n)
        return out
    doc["tree"] = prune(doc["tree"])


def _table_own_text(doc):
    """A captionless table's own rows are not its caption, nor its header row a paragraph.

    BIO11L ch11 p145 prints a small `In | Out` table with no number and no caption. The text
    layer read its body as one bold block, which became the table's `caption` -- `Six CO2 One
    glucose 18 ATP ...` printed in a bar above the grid -- and its header row, measured just
    above the table's box, stayed a loose `In Out` paragraph, so the page showed the header
    three times. A caption that does not open `Table` and whose words all lie in the table's
    own cells is dropped; a text-layer paragraph that is exactly the header row, set on the
    table's page directly above it, is folded into the table's box.
    """
    import unicodedata

    def words(s):
        return re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKC", s or "").lower())
    nodes = list(_walk_nodes(doc["tree"]))
    gone = set()
    for t in nodes:
        cells = ((t.get("table_grid") or {}).get("cells") or []) if t.get("kind") == "table" else []
        if not cells or not t.get("boxes"):
            continue
        own = collections.Counter(w for row in cells for c in row for w in words(c))
        cap = t.get("caption") or ""
        if cap and not re.match(r"\s*Table\b", cap, re.I):
            cw = collections.Counter(words(cap))
            if cw and all(own[w] >= k for w, k in cw.items()):
                for k in [k for k in t if k == "caption" or k.startswith("caption_")]:
                    t.pop(k)
        head = words(" ".join(cells[0]))
        tb = t["boxes"][0]
        for p in nodes:
            pb = (p.get("boxes") or [None])[0]
            if (p.get("kind") != "para" or p.get("source") != "text_layer" or not pb
                    or pb.get("page_file") != tb.get("page_file") or words(p.get("body")) != head):
                continue
            a, b = pb["bbox"], tb["bbox"]
            if -0.005 <= b[1] - a[3] <= 0.04 and min(a[2], b[2]) > max(a[0], b[0]):
                gone.add(id(p))
                tb["bbox"] = [min(a[0], b[0]), a[1], max(a[2], b[2]), b[3]]
    if not gone:
        return

    def prune(ns):
        out = []
        for n in ns:
            if n.get("children"):
                n["children"] = prune(n["children"])
            if id(n) not in gone:
                out.append(n)
        return out
    doc["tree"] = prune(doc["tree"])


def _drop_shadow_figures(doc):
    """One picture, one figure node: a captionless figure on a captioned one's box is that figure.

    The Unit 2 opener's portrait of Katherine Esau (BIO11L ch05 p002) arrived twice -- once as
    the embedded image (captionless) and once as A2L's measured figure carrying `Katherine Esau
    (1898 - 1997)` -- so chapter.json, the Markdown and the CDN each carried the portrait two
    times. A captionless figure whose box is >= 80% the same as a captioned figure's on the same
    page is dropped; the captioned one keeps the picture.
    """
    def iou(a, b):
        ix = max(0.0, min(a[2], b[2]) - max(a[0], b[0]))
        iy = max(0.0, min(a[3], b[3]) - max(a[1], b[1]))
        inter = ix * iy
        union = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter
        return inter / union if union > 0 else 0.0

    def box(n):
        b0 = (n.get("boxes") or [{}])[0]
        return b0.get("page_file") or n.get("page_file"), b0.get("bbox")
    named = [box(n) for n in _walk_nodes(doc["tree"])
             if n.get("kind") == "figure" and (n.get("caption") or "").strip()]
    shadow = set()
    # A TABLE'S CAPTION IS NOT A FIGURE OF ITS OWN. Table 11.1's caption (BIO11L ch11 p148) is
    # set above an A2S-read grid; the table took the caption, and the caption's own element
    # stayed behind as an unnumbered figure -- with a vector crop of the caption's ink as its
    # picture -- so the caption printed twice and a picture of text went to the CDN.
    def fold(s):
        return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKC", s or "").lower())
    tcaps = {(box(t)[0], fold(t.get("caption"))) for t in _walk_nodes(doc["tree"])
             if t.get("kind") == "table" and (t.get("caption") or "").strip()}
    for n in _walk_nodes(doc["tree"]):
        if (n.get("kind") == "figure" and not n.get("number") and (n.get("caption") or "").strip()
                and any(pf == box(n)[0] and fc.startswith(fold(n["caption"])[:40])
                        for pf, fc in tcaps)):
            shadow.add(id(n))
    for n in _walk_nodes(doc["tree"]):
        if n.get("kind") != "figure" or (n.get("caption") or "").strip() or n.get("panels"):
            continue
        pf, bb = box(n)
        if bb and any(p == pf and q and iou(bb, q) >= 0.8 for p, q in named):
            shadow.add(id(n))
    if not shadow:
        return

    def prune(nodes):
        out = []
        for n in nodes:
            if n.get("children"):
                n["children"] = prune(n["children"])
            if id(n) not in shadow:
                out.append(n)
        return out
    doc["tree"] = prune(doc["tree"])


def _running_head_titles(doc):
    """`Animal Kingdom` at the head of a body page is its RUNNING HEAD, not a chapter title.

    BIO11L ch04 p051 opens on Table 4.2, and the extractor filed the page's running head as a
    third `chapter_title` node: the page record kept no `header`, chapter.json carried a title
    NCERT never prints there, and the render drew it in title type over the head band. A title
    off the chapter's opening page, in the head band, whose text is the head the other pages
    print, goes back to its page record -- in the type those pages measured.
    """
    titles = [n for n in _walk_nodes(doc["tree"]) if n.get("kind") == "chapter_title"]
    if not titles:
        return
    opener = titles[0].get("page_file")

    def letters(s):
        return re.sub(r"[^a-z0-9]", "", (s or "").lower())
    pages = {p.get("page_file"): p for p in doc.get("pages") or []}
    heads = {}
    for p in pages.values():
        if p.get("header") and p.get("header_style"):
            heads.setdefault((letters(p["header"]), p.get("page_side")), p)
    moved = set()
    for n in titles:
        pf, b0 = n.get("page_file"), (n.get("boxes") or [{}])[0]
        pg, bb = pages.get(pf), b0.get("bbox")
        if pf == opener or not pg or pg.get("header") or not bb or bb[1] > 0.11:
            continue
        like = heads.get((letters(n.get("body")), pg.get("page_side")))
        if like is None:
            continue
        pg["header"] = like["header"]
        pg["header_bbox"] = bb
        pg["header_style"] = like["header_style"]
        moved.add(id(n))
    if not moved:
        return

    def prune(nodes):
        out = []
        for n in nodes:
            if n.get("children"):
                n["children"] = prune(n["children"])
            if id(n) not in moved:
                out.append(n)
        return out
    doc["tree"] = prune(doc["tree"])


def _absorb_caption_tails(tree):
    """A caption's second line, set under it and starting with a panel letter, is the caption.

    `Figure 2.5 Fungi: (a) Mucor` / `(b) Aspergillus (c) Agaricus` (BIO11L ch02 p017): the
    second line opens with `(b)`, so it was typed a LIST and filed into 2.3.2 Ascomycetes,
    splitting that section's paragraph in the Markdown while the figure's caption stopped at
    `Mucor`. A short label-led block whose top sits on the caption's last line, under the
    caption's own column, is folded into the caption with its marks.
    """
    figs = [n for n in _walk_nodes(tree) if n.get("kind") == "figure" and n.get("caption_box")
            and (n.get("caption") or "").strip()]
    if not figs:
        return
    claimed = {}
    for n in _walk_nodes(tree):
        if n.get("kind") not in ("list", "para") or n.get("children"):
            continue
        body = (n.get("body") or "").strip()
        b0 = (n.get("boxes") or [{}])[0]
        bb = b0.get("bbox")
        if not bb or len(n.get("boxes") or []) != 1 or len(body) > 120:
            continue
        if not re.match(r"^\(\s?[a-h]\s?\)", body):
            continue
        for f in figs:
            cb = f["caption_box"]["bbox"]
            if (cb and (b0.get("page_file") or n.get("page_file"))
                    == (f["caption_box"].get("page_file") or f.get("page_file"))
                    and cb[3] - 0.004 <= bb[1] <= cb[3] + 0.012
                    and bb[0] < cb[2] and bb[2] > cb[0]):
                claimed[id(n)] = (n, f)
                break
    if not claimed:
        return
    for n, f in claimed.values():
        cap = f["caption"].rstrip()
        body = (n.get("body") or "").strip()
        base = len(cap) + 1
        f["caption"] = f"{cap} {body}"
        # A list's marks still live on its items at this point in the build.
        items = n.get("items") or []
        marks = n.get("marks") or (items[0].get("marks") if len(items) == 1
                                   and (items[0].get("body") or "").strip() == body else []) or []
        f["caption_marks"] = (f.get("caption_marks") or []) + [
            {**m, "from": m["from"] + base, "to": m["to"] + base}
            for m in marks if m["to"] <= len(body)]
        cb, bb = f["caption_box"]["bbox"], n["boxes"][0]["bbox"]
        f["caption_box"] = {**f["caption_box"], "bbox": [
            round(min(cb[0], bb[0]), 4), round(min(cb[1], bb[1]), 4),
            round(max(cb[2], bb[2]), 4), round(max(cb[3], bb[3]), 4)]}
        f["caption_line_count"] = (f.get("caption_line_count") or 1) + (n.get("line_count") or 1)
        # the folded line starts a printed line of its own, as the book sets it
        f["caption_line_starts"] = list(f.get("caption_line_starts") or []) + [base]
        f["boxes"] = [b for b in f.get("boxes") or [] if b.get("bbox") != cb] + [f["caption_box"]]

    def prune(nodes):
        out = []
        for n in nodes:
            if n.get("children"):
                n["children"] = prune(n["children"])
            if id(n) not in claimed:
                out.append(n)
        return out

    tree[:] = prune(tree)


def _order_lettered_siblings(tree):
    """Figure 3.4 (a) before Figure 3.4 (b): same-numbered figures side by side, in letter order.

    BIO12L ch03 p045 prints Vasectomy (a) and Tubectomy (b) on one row, each with its own
    caption; the tubectomy drawing starts a few points higher, so reading order (top, then left)
    put (b) first in the JSON and the Markdown. Only a run of ADJACENT figures sharing a number
    and each captioned with a single letter is reordered.
    """
    def letter(n):
        m = re.match(r"^\s*(?:Figure|Fig\.)\s*\d+\.\d+\.?\s*\(([a-z])\)", n.get("caption") or "")
        return m.group(1) if m else None

    def fix(nodes):
        i = 0
        while i < len(nodes):
            j = i
            while (j < len(nodes) and nodes[j].get("kind") == "figure" and nodes[j].get("number")
                   and nodes[j].get("number") == nodes[i].get("number") and letter(nodes[j])):
                j += 1
            if j - i >= 2:
                nodes[i:j] = sorted(nodes[i:j], key=letter)
            i = max(j, i + 1)
        for n in nodes:
            if n.get("children"):
                fix(n["children"])

    fix(tree)


def _title_unnumbered_sections(tree):
    """`Vegetative Characters`, `Floral Characters`, `Economic Importance` are headings.

    An unnumbered bold heading reached the tree as a `section` with its words in `body` and no
    `title` (BIO11L ch05 p068-069). Every consumer reads a section's title, so the heading was
    missing from the Markdown and the page. The body becomes the title.
    """
    for n in _walk_nodes(tree):
        if n.get("kind") != "section" or (n.get("title") or "").strip():
            continue
        body = re.sub(r"\s+", " ", n.get("body") or "").strip()
        if not body or len(body) > 80 or body.endswith("."):
            continue
        n["title"] = body
        for k in ("body", "body_md", "marks", "sentences", "terms"):
            n.pop(k, None)


def _split_label_lines(tree):
    """`Stem: ...` / `Leaves: ...` -- each printed line that opens with a bold label is its own.

    A family's description prints one character per line: `Plants mostly herbs ...`, then
    `Stem: herbaceous ...`, `Leaves: alternate ...`; `Inflorescence :`, `Flower:`, `Calyx:` ...
    (BIO11L ch05 p068-069). A2 kept the lines, but its block became one list item and the line
    breaks were unwrapped, so each description printed as one run-on paragraph in the JSON,
    the Markdown and the page. The bold labels survive as marks: the block is cut before every
    bold `Label:` after its start, and each piece becomes a paragraph sharing the block's box.
    """
    def labels(body, marks):
        cuts = []
        for m in marks:
            if not m.get("b") or m["from"] == 0:
                continue
            word = body[m["from"]:m["to"]].strip()
            after = body[m["to"]:m["to"] + 3]
            # A label right after the item's marker is the item's own term, not a new line:
            # `(iv) Commensalism: This is ...` (BIO12L ch11 p201) was cut into a bare `(iv)`
            # paragraph and the item without its marker, on the page and in the Markdown.
            lead = body[:m["from"]]
            m0 = _MARK_AT_START.match(lead)
            if m0 and not lead[m0.end():].strip():
                continue
            if (word and len(word) <= 30 and (word.endswith(":") or after.lstrip().startswith(":"))
                    and body[m["from"] - 1].isspace()):
                cuts.append(m["from"])
        return cuts

    def split(n):
        if n.get("kind") == "list" and len(n.get("items") or []) == 1:
            body, marks = n["items"][0].get("body") or "", n["items"][0].get("marks") or []
        elif n.get("kind") == "para":
            body, marks = n.get("body") or "", n.get("marks") or []
        else:
            return None
        cuts = labels(body, marks)
        if len(cuts) < 2 and not (cuts and n.get("kind") == "list"):
            return None
        out, pos = [], 0
        for c in cuts + [len(body)]:
            seg = body[pos:c]
            lead = len(seg) - len(seg.lstrip())
            seg = seg.strip()
            if seg:
                a = pos + lead
                pm = [{**m, "from": max(m["from"], a) - a, "to": min(m["to"], a + len(seg)) - a}
                      for m in marks if min(m["to"], a + len(seg)) > max(m["from"], a)]
                piece = {k: v for k, v in n.items()
                         if k not in ("items", "ordered", "body", "body_md", "marks",
                                      "sentences", "terms", "line_geom", "line_starts",
                                      "line_count", "id", "path")}
                piece.update(kind="para", body=seg, marks=pm, body_md=ct.to_body_md(seg, pm),
                             sentences=ct.split_sentences(seg), label_line=True)
                out.append(piece)
            pos = c
        return out if len(out) >= 2 else None

    def walk(nodes):
        i = 0
        while i < len(nodes):
            n = nodes[i]
            if n.get("children"):
                walk(n["children"])
            parts = split(n)
            if parts:
                nodes[i:i + 1] = parts
                i += len(parts)
            else:
                i += 1

    walk(tree)


def _squeeze_caption_spaces(tree):
    """`Figure 2.6  (a) Tobacco...` -> one space, with every caption mark moved to match."""
    for n in _walk_nodes(tree):
        cap = n.get("caption")
        if not isinstance(cap, str) or not re.search(r"\s{2,}", cap.strip()):
            continue
        shifts, out, pos = [], [], 0
        for m in re.finditer(r"\s{2,}", cap):
            out.append(cap[pos:m.start()] + " ")
            shifts.append((m.start(), m.end() - m.start() - 1))
            pos = m.end()
        out.append(cap[pos:])
        new = "".join(out)

        def move(i):
            for at, d in shifts:
                if i > at:
                    i -= min(d, i - at)
            return i
        n["caption"] = new
        n["caption_marks"] = [{**m, "from": move(m["from"]), "to": move(m["to"])}
                              for m in n.get("caption_marks") or []
                              if move(m["to"]) > move(m["from"])]


def _move_figures_to_first_mention(root):
    """A figure sits after the paragraph that first names it, not where it is printed.

    Figure 1.1 is printed beside the end of 1.2.6 but belongs to 1.2.7 -- the section that
    discusses it. The printed position is untouched; only the reading order moves.
    """
    # Keyed by KIND and number: `Figure 1.1` and `Table 1.1` are different things, and keying by
    # the number alone let Table 1.1 overwrite Figure 1.1, so the figure never moved.
    figures = {}

    def collect(n, parents):
        if n.get("kind") in ("figure", "table") and n.get("number"):
            figures[(n["kind"], n["number"])] = (n, parents)
    _walk(root, collect)
    if not figures:
        return

    mentions = {}

    def find(n, parents):
        if n.get("kind") != "para":
            return
        for kind, rx in (("figure", _FIG_REF), ("table", _TAB_REF)):
            for num in rx.findall(n.get("body", "")):
                mentions.setdefault((kind, num), (n, parents))
    _walk(root, find)

    for num, (fig, fig_parents) in figures.items():
        tgt = mentions.get(num)
        if not tgt:
            continue
        para, para_parents = tgt
        src_list = fig_parents[-1]["children"] if fig_parents else root
        dst_list = para_parents[-1]["children"] if para_parents else root
        if src_list is dst_list:
            continue
        if fig in src_list:
            src_list.remove(fig)
            dst_list.insert(dst_list.index(para) + 1, fig)
            fig["moved_from_printed_position"] = True


def _assign_paths(root, book_base, chapter_num):
    """Number each piece's children 001, 002, … ; the path becomes the SK."""
    def rec(nodes, prefix):
        for i, n in enumerate(nodes, 1):
            path = f"{prefix}{i:03d}"
            n["path"] = path
            n["id"] = ct.stable_id(n["kind"], book_base, chapter_num, path)
            if n.get("children"):
                rec(n["children"], path + ".")
    rec(root, "")


def _drop_opener_contents(chapter_pages):
    """Re-label the opener's section-contents rail as furniture, not content.

    The chapter's own title page prints the chapter's section list in a narrow rail beside the
    opening prose. Those entries are the SAME strings as the section headings further in, so
    left as content the chapter begins with two stray lines that duplicate its own headings --
    and they reach search and read-along as though NCERT had written them twice. The schema is
    explicit that the opener's contents list belongs on the chapter row only.

    Matched against the chapter's real headings rather than by position, so a genuine marginal
    note on the opening page survives.
    """
    if not chapter_pages:
        return
    headings = set()
    for p in chapter_pages:
        for e in p["elements_in_reading_order"]:
            if e["role"] == "section_heading":
                headings.add(re.sub(r"[^a-z0-9]", "", (e.get("text") or "").lower()))
    # The rail is not always the headings verbatim. BIO11L ch05's rail wraps `5.8 Semi-technical
    # Description of a` / `Typical Flowering Plant`, and names 5.9 `Description of Some Important
    # Families` where the body heading is `5.9 Solanaceae`; all four lines matched no heading
    # and became content. So a numbered `n.m Title` entry in the rail is contents too, and so is
    # an unnumbered line hanging directly under one (its wrapped continuation).
    prev = None
    rail = sorted((e for e in chapter_pages[0]["elements_in_reading_order"]
                   if e["role"] in ("side_note", "contents_entry")),
                  key=lambda e: e["bbox_pt"][1])
    for e in rail:
        text = (e.get("text") or "").strip()
        key = re.sub(r"[^a-z0-9]", "", text.lower())
        hangs = (prev is not None and e["bbox_pt"][1] - prev["bbox_pt"][3] < 12
                 and e["bbox_pt"][0] >= prev["bbox_pt"][0] - 1)
        if (key and key in headings) or re.match(r"^\d+\.\d+\s+\S", text) or hangs:
            e["role"] = "contents_entry"      # in ct._FURNITURE -> never a node
            prev = e
        else:
            prev = None


def _title_lines_snapshot(layout):
    """The text layer's chapter titles, taken BEFORE the agent join rewrites them."""
    snap = {}
    for p in layout["pages"]:
        for e in p["elements_in_reading_order"]:
            if e["role"] == "chapter_title" and e.get("bbox_pt"):
                snap.setdefault(p["page_file"], []).append(
                    {k: e.get(k) for k in ("text", "runs", "line_boxes_pt", "bbox_pt",
                                           "bbox_sheet", "size_rel", "line_pitch_pt")})
    return snap


def _restore_title_lines(layout, snap):
    """`Chapter 2` and `Biological Classification` are two printed lines, in their own case.

    Two shapes of the same defect, both restored from the layer -- one element per printed
    title line, in the layer's case, small caps only where the layer measured them:
      * Class 11: the layer reads the opener's title as ONE two-line element, true-cased from
        its small capitals (`Chapter 2 Biological Classification`); A2 reads two blocks and the
        join paired the element with the second, so `CHAPTER 2` vanished and the title went out
        in plain capitals (BIO11L ch02 p010).
      * Class 12: the layer has two elements, `CHAPTER 3` and `REPRODUCTIVE HEALTH`; A2 reads one
        heading `CHAPTER 3 / REPRODUCTIVE HEALTH`, the join merged the elements, and the chapter
        number and title became ONE node (BIO12L ch03 p001).
    """
    def letters(s):
        return re.sub(r"[^a-z0-9]", "", (s or "").lower())

    for p in layout["pages"]:
        pieces = []                      # (text, bbox_pt, bbox_sheet, run, own measures)
        for s in snap.get(p["page_file"]) or []:
            bp, bs = s["bbox_pt"], s["bbox_sheet"] or s["bbox_pt"]
            sx = (bs[2] - bs[0]) / max(1e-6, bp[2] - bp[0])
            sy = (bs[3] - bs[1]) / max(1e-6, bp[3] - bp[1])

            def sheet(b, bp=bp, bs=bs, sx=sx, sy=sy):
                return [round(bs[0] + (b[0] - bp[0]) * sx, 4), round(bs[1] + (b[1] - bp[1]) * sy, 4),
                        round(bs[0] + (b[2] - bp[0]) * sx, 4), round(bs[1] + (b[3] - bp[1]) * sy, 4)]
            run0 = dict((s.get("runs") or [{}])[0])
            lbs = s.get("line_boxes_pt") or []
            m = re.match(r"(?is)^\s*(chapter\s*\d+)\s+(.+?)\s*$", s["text"] or "")
            if m and len(lbs) == 2:
                for text, lb in ((re.sub(r"\s+", " ", m.group(1)), lbs[0]), (m.group(2), lbs[1])):
                    pieces.append((text, list(lb["bbox_pt"]), sheet(lb["bbox_pt"]), run0, {}))
            else:
                # A separate layer element keeps ITS OWN size: `CHAPTER 1` is set at 26pt under a
                # 30pt title (BIO12L ch01), and copying the merged element's size_rel gave the
                # chapter number the title's.
                own = {k: s[k] for k in ("size_rel", "line_pitch_pt") if s.get(k) is not None}
                # ...and ITS OWN LINES. `STRUCTURAL ORGANISATION IN / ANIMALS` is one element
                # printed on two lines (BIO11L ch07 p079); stamping it `line_count: 1` made the
                # renderer hold it to one line and shrink it to fit.
                if len(lbs) > 1:
                    own["line_count"] = len(lbs)
                    own["line_boxes_pt"] = lbs
                pieces.append((re.sub(r"\s+", " ", s["text"] or "").strip(), list(bp),
                               list(bs), run0, own))
        if len(pieces) < 2:
            continue
        whole = letters("".join(t for t, *_ in pieces))
        tail = letters("".join(t for t, *_ in pieces[1:]))
        els = p["elements_in_reading_order"]
        hit = next((i for i, e in enumerate(els) if e["role"] == "chapter_title"
                    and letters(e.get("text")) in (whole, tail)), None)
        if hit is None:
            continue
        e = els[hit]
        new = []
        for text, bp_, bs_, run0, own in pieces:
            # The title's face is the heading's own, not a mark inside it.
            new.append({**e, "text": text,
                        "runs": [{**run0, "t": text, "sc": bool(run0.get("sc")),
                                  "b": False, "i": False}],
                        "bbox_pt": bp_, "bbox": bs_, "bbox_sheet": bs_,
                        "line_count": 1, "line_boxes_pt": [{"bbox_pt": bp_, "text": text}],
                        **own})
        # any other title element on the page that one of the pieces now carries goes
        keep = [x for i, x in enumerate(els) if i != hit and not (
            x["role"] == "chapter_title" and letters(x.get("text"))
            and any(letters(x.get("text")) == letters(t) for t, *_ in pieces))]
        at = sum(1 for i in range(hit) if els[i] in keep)
        p["elements_in_reading_order"] = keep[:at] + new + keep[at:]


def _titles_before_opener_art(tree):
    """The chapter's titles open the tree, ahead of the opener's picture.

    The opener prints its artwork level with `CHAPTER 2`, so a reading order may list the
    picture first -- BIO12L ch02's A2 read does -- and chapter.json and chapter.md then opened
    on a captionless image, with the rail and `## CHAPTER 2` after it.
    """
    i = 0
    while i < len(tree) and tree[i].get("kind") == "figure":
        i += 1
    j = i
    while j < len(tree) and tree[j].get("kind") == "chapter_title":
        j += 1
    if i and j > i and len({n.get("page_file") for n in tree[:j]}) == 1:
        tree[:j] = tree[i:j] + tree[:i]


def _strip_repeated_heading(tree):
    """`SUMMARY Humans are ...` -> `Humans are ...` under a Summary heading.

    A2 reads a boxed summary as one block, heading included, while the text layer keeps the
    heading as its own element -- so BIO12L ch02's summary printed `SUMMARY` twice, once as
    the heading and once opening the paragraph.
    """
    for n in tree:
        if n.get("kind") not in ("summary", "exercises") or not n.get("children"):
            continue
        c = n["children"][0]
        if c.get("kind") not in ("para", "box"):
            continue
        body = c.get("body") or ""
        m = re.match(r"^\s*%s\b[\s:.]*" % re.escape(n.get("title") or "~"), body, re.I)
        if not m or m.end() >= len(body):
            continue
        cut = m.end()
        body = body[cut:]
        marks = [dict(x, **{"from": x["from"] - cut, "to": x["to"] - cut})
                 for x in c.get("marks") or [] if x["from"] >= cut]
        c["body"] = body
        if c.get("marks") is not None:
            c["marks"] = marks
        c["body_md"] = ct.to_body_md(body, marks)
        c["sentences"] = ct.split_sentences(body)
        if c.get("terms"):
            c["terms"] = ct.terms_in(body, marks)


def chapter_title_of(pages):
    for p in pages:
        titles = [e["text"].strip() for e in p["elements_in_reading_order"]
                  if e["role"] == "chapter_title"]
        for t in titles:
            if not re.match(r"^\s*chapter\s+\d+\s*$", t, re.I):
                return re.sub(r"(?i)^chapter\s*\d+\s*", "", t).strip()
    return ""


def build(book_id, chapter_num, use_agent=True, lang="EN"):
    layout = extract_mod.extract(book_id, chapter_num)
    chapter = f"{book_id}-ch{chapter_num:02d}"
    join_stats = layout_stats = special_stats = None
    title_snap = _title_lines_snapshot(layout)
    if use_agent:
        steps = os.path.join(ROOT, "steps")
        # Figures BEFORE words: the text join would otherwise claim a figure's panel letters as
        # followers of its caption (see `apply_agent_figures`).
        src = layout.get("source_pdf")
        split_stats = join_agent_text.repair_cross_column_blocks(layout)
        fig_stats = join_agent_text.apply_agent_figures(
            layout, chapter, steps_dir=steps,
            pdf_path=src if not src or os.path.isabs(src) else os.path.join(ROOT, src))
        join_stats = join_agent_text.apply_agent_text(layout, chapter, steps_dir=steps)
        join_stats["figures"] = fig_stats
        join_stats["cross_column"] = split_stats
        # The layout join runs AFTER the text join, because it matches numbered elements on
        # `a2_block_n` -- which the text join is what writes.
        layout_stats = (join_agent_layout.apply_agent_layout(layout, chapter, steps_dir=steps)
                        if design_lib.a2l_join(book_id) else
                        {"pages": len(layout["pages"]), "skipped": "a2l_join off for this book"})
        # A2S last: it needs `a2_block_n`, which the text join writes, and it overrides the
        # geometry-derived table grid with the agent's transcription where one exists.
        special_stats = join_agent_special.apply_agent_special(layout, chapter, steps_dir=steps)
        _restore_title_lines(layout, title_snap)

    subject, klass, edition = design_lib.parse_book_id(book_id)
    book_base = f"{subject}{klass}"
    title = chapter_title_of(layout["pages"])

    unit_pages, chapter_pages = split_unit_pages(layout)
    _drop_opener_contents(chapter_pages)
    # The title is read from the CHAPTER's own pages, never the whole file. The unit opener
    # carries `Unit 1` as a `chapter_title` at 4x body size, so scanning every page made the
    # chapter's title come out as "Unit 1" -- the unit's name filed as the chapter's.
    title = chapter_title_of(chapter_pages) or title
    if not title:
        # A textless page carries no `chapter_title` element. The agent read the page, so its
        # first real heading is the chapter's name -- measured on BIO12L ch01, a pure A4 scan
        # whose title came out empty and whose folder was therefore named `ch01_chapter`.
        for _pg in chapter_pages[:2]:
            for _e in _pg["elements_in_reading_order"]:
                _t = (_e.get("text") or "").strip()
                if (_e.get("text_source") == "a2-agent"
                        and _e["role"] in ("section_heading", "chapter_title")
                        and _t and not re.match(r"^\s*\d+\.\d", _t) and len(_t) < 70):
                    title = re.sub(r"(?i)^chapter\s*\d+\s*", "", _t).strip()
                    break
            if title:
                break
    if not title:
        # No `chapter_title` element exists on a textless page. The agent read the page, so its
        # first heading block is the chapter's name -- measured on BIO12L ch01, which is a pure
        # A4 scan and whose title is otherwise empty.
        for pg in chapter_pages[:2]:
            for e in pg["elements_in_reading_order"]:
                if e.get("text_source") != "a2-agent":
                    continue
                t = (e.get("text") or "").strip()
                if (e["role"] in ("section_heading", "chapter_title")
                        and t and not re.match(r"^\s*\d+\.\d", t) and len(t) < 70):
                    title = re.sub(r"(?i)^chapter\s*\d+\s*", "", t).strip()
                    break
            if title:
                break
    blocks = collapse_lists(stitch_across_pages(collect_blocks(
        chapter_pages, two_col=not design_lib.is_measured(book_id))))
    tree = build_tree(blocks, book_base, chapter_num)
    _titles_before_opener_art(tree)
    _strip_repeated_heading(tree)

    folios = [p["printed_page_number"] for p in chapter_pages
              if isinstance(p.get("printed_page_number"), int)]
    reprint = next((p.get("imprint") for p in layout["pages"] if p.get("imprint")), None)
    if reprint:
        reprint = re.sub(r"(?i)^reprint\s+", "", reprint).strip()
    else:
        # AN IMAGE-ONLY CHAPTER PRINTS ITS IMPRINT TOO -- we just cannot read it, because there
        # is no text layer to read it from. The book's own imprint for this edition is known
        # from the measured design, so it is used and MARKED as inferred rather than left null
        # and silently stamped onto a row as if it had been read off the page.
        # `Design.imprint` is shadowed by the furniture dict of the same name in the
        # design table, so the mapping is read directly rather than through the method.
        reprint = (design_lib.design_for(book_id)
                   .imprint_by_edition.get(edition))
        reprint_inferred = True

    # ONE TREE FOR THE WHOLE FILE. The unit's nodes are built on their own paths (so their
    # ids never collide with the chapter's) and marked `belongs: "unit"`, then placed ahead of
    # the chapter's in binding order. A consumer walks one tree; the export routes by the tag.
    unit_nodes = (build_tree(collapse_lists(stitch_across_pages(collect_blocks(unit_pages))),
                             book_base, 0) if unit_pages else [])
    _walk(unit_nodes, lambda n, _p: n.update(belongs="unit"))

    doc = {
        "book": book_base,
        "book_id": book_id,
        "edition": {"L": "latest", "O": "older"}[edition],
        "grade": int(klass),
        "subject": SUBJECT_WORD[subject],
        "lang": lang,
        "reprint": reprint,
        "reprint_inferred": bool(locals().get("reprint_inferred")),
        "ncert_file": None,
        "design_key": layout.get("design_key"),
        "sheet_pt": layout.get("sheet_pt"),
        "source_pdf": layout["source_pdf"],
        "chapter": {
            "id": ct.stable_id("chapter", book_base, chapter_num, "META"),
            "number": chapter_num,
            "title": title,
            "unit": unit_number(unit_pages),
            "pages": [min(folios), max(folios)] if folios else None,
        },
        "pages": [{
            "page_file": p["page_file"],
            "printed": p.get("printed_page_number"),
            "page_side": p.get("page_side"),
            "size_pt": p.get("sheet_pt"),
            "header": next((e["text"] for e in p["elements_in_reading_order"]
                            if e["role"] == "running_header"), None),
            # Where the running head printed. Its box runs from the folio to the far end of
            # the line, so the head sits at the box's OUTER end: the right on a verso
            # (`Biology` ends at x 550.6 on p004), the left on a recto. Without it the head was
            # placed at a fixed 34% across every verso, mid-page.
            "header_bbox": next(([round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"])]
                                 for e in p["elements_in_reading_order"]
                                 if e["role"] == "running_header"), None),
            "footer": p.get("imprint"),
            # ...where and in what type the imprint prints: Class 12 sets `Reprint 2026-27` in
            # Arial 8pt at y 0.971, centred; the render set it in Bookman 12mm off the foot.
            "imprint": next(({"bbox": [round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"])],
                              "style": _run_style(e)}
                             for e in p["elements_in_reading_order"]
                             if e["role"] == "reprint_line" and (e.get("bbox_sheet") or e.get("bbox"))),
                            None),
            "has_text_layer": p.get("has_text_layer"),
            "sheet_pt": p.get("sheet_pt"),
            "sheet_aspect": p.get("sheet_aspect"),
            "geometry_source": p.get("geometry_source"),
            "text_source": p.get("text_source"),
            # The page's OWN artwork -- the chapter-opening page's green panel and its QR code
            # are cut like any other asset, and the renderer needs them from chapter.json alone.
            # The opener's section-contents rail: rendered in the margin, never part of the
            # readable content stream. Kept on the PAGE record for exactly that reason -- the
            # schema says the opener's contents list belongs to the chapter/page rows, and a
            # renderer still has to draw it where the book prints it.
            # FURNITURE A2L MEASURED, carried through so a renderer can draw a page it has
            # no hand-measured design for.
            #
            # `book_design.py` holds the six designs that were measured page by page, and the
            # renderer draws Class 11's header band, folio tab and foot band from it. Books
            # outside that set -- every scan, and every subject not yet measured -- got NO
            # furniture at all: Class 12 ch01 rendered 23 sheets with no running head and no
            # page number, because nothing in the pipeline knew what they looked like.
            #
            # A2L measures exactly that, per page, off the image: the band's rectangle and
            # fill, the folio block and its ink, where the running head sits and what it
            # says. Carrying it here means a measured page can be drawn correctly even when
            # its book has no design entry -- which is the whole point of having the agent.
            "furniture": [
                {"kind": e.get("furniture") or e.get("layout_role"),
                 "bbox": [round(v, 4) for v in (e.get("bbox_sheet") or e.get("bbox") or [])],
                 "fill": e.get("fill") or e.get("layout_fill"),
                 "text": (e.get("text") or "").strip() or None,
                 "color": e.get("text_color") or e.get("layout_text_color"),
                 "size_rel": e.get("size_rel")}
                for e in p["elements_in_reading_order"]
                if e.get("role") == "page_furniture" and (e.get("bbox_sheet") or e.get("bbox"))
            ] or None,
            "contents_rail": _merge_split_rail([
                {"text": e.get("text", ""),
                 "bbox": [round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"])],
                 # As printed: each entry its number and title, the title hung at its measured
                 # indent, in the rail's own type (Class 12: black Bookman italic 10pt in a
                 # peach box, not Class 11's blue 8.6pt).
                 "items": _rail_items(e.get("text", "")),
                 "indent_pt": _rail_indent(e),
                 "style": _run_style(e),
                 # the entry's NUMBER weight when it differs from its title's (PHY11: bold `1.1`)
                 **({"num_b": e["num_b"]} if e.get("num_b") is not None else {})}
                for e in p["elements_in_reading_order"]
                if e["role"] == "contents_entry"],
                keep_closers=not design_lib.is_measured(book_id)) or None,
            # THE BOOK'S OWN DECORATION AND TYPE, measured off the page (see
            # `extract_page_layout.page_decor`): panels, bands, boxes, tints and rules in paint
            # order, and the running head's and folio's face, size and colour.
            "decor": p.get("decor"),
            "header_style": next((_run_style(e, words=True) for e in p["elements_in_reading_order"]
                                  if e["role"] == "running_header"), None),
            "folio": next(({"bbox": [round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"])],
                            "style": _run_style(e)}
                           for e in p["elements_in_reading_order"]
                           if e["role"] == "page_number"), None),
            # FURNITURE IS A BAND, A TAB OR A MOTIF -- NEVER MOST OF THE PAGE.
            #
            # Every page of the Class 12 scan carried an "i00N_header2.png" covering 88.4% of
            # the sheet, classified as `header art`. It is not art: it is a scan of nearly the
            # whole page, text and all. Drawn as a background with the live text rendered on
            # top, every page showed its own prose TWICE, offset and overlapping -- which is
            # unreadable and also hides that the real text is correct underneath.
            #
            # An external review predicted this exactly: "almost full-page areas are
            # classified as header art ... if those crops include original text, restoring the
            # missing assets could place scanned text underneath newly rendered text."
            #
            # A header band is a strip; a folio is a tab; a motif is a corner. None of them
            # covers a third of the page. Anything that does is a page scan, and on a page
            # that also sets live text it must not be drawn.
            "art": [{"kind": e.get("furniture"),
                     "z": e.get("z"),
                     "file": f"figures/{e['furniture_file']}",
                     "bbox": [round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"])]}
                    for e in p["elements_in_reading_order"]
                    if e["role"] == "page_furniture" and e.get("furniture_file")
                    and (e.get("furniture") == "page ground"
                         or (e.get("furniture") in ("header art", "qr code", "ornament")
                             and _is_furniture_sized(e, p)))] or None,
            # WHICH PART OF THE BOOK THIS PAGE BELONGS TO.
            # The source file holds both: Class 11 ch01's PDF is the Unit 1 opener, the Ernst
            # Mayr biography, then the 7 chapter pages. All 9 are pages of this file and all 9
            # get rendered; the tag is what routes them to UNIT# rows rather than CH# rows on
            # export. Listing only the chapter's 7 made the render 2 sheets short and
            # renumbered every folio after them.
            "belongs": "unit" if p in unit_pages else "chapter",
            # WHAT KIND OF PAGE THIS IS -- stated as data, so the renderer never has to guess.
            #
            # It used to infer "is this an opener?" from whether a header-art crop existed.
            # That is a fact about OUR PIPELINE, not about the book: the Unit 1 opener has no
            # such crop so it was drawn as an ordinary page, with a header band and a running
            # head the book does not print; and on the Class 12 scan every page had art
            # detected, so all 22 sheets were drawn as chapter openers.
            #
            # The three designs are genuinely different pages:
            #   unit_opener     a full-bleed panel, the unit number set ~4x body, the chapter
            #                   list in a side panel. NO running head, NO folio.
            #   chapter_opener  the chapter banner, number and title, the contents rail.
            #                   NO running head.
            #   ordinary        header band, running head, folio tab, foot bar.
            "page_kind": (
                "unit_opener" if p in unit_pages and p is unit_pages[0]
                else "unit_page" if p in unit_pages
                else "chapter_opener" if p is chapter_pages[0]
                else "ordinary"),
        } for p in (unit_pages + chapter_pages)],
        "unit_pages": [p["page_file"] for p in unit_pages],
        # THE UNIT PAGES ARE CONTENT, THEY JUST BELONG TO THE BOOK AND NOT THIS CHAPTER.
        # Dropping them entirely cost 95 words -- the whole Unit 1 opener and the whole Ernst
        # Mayr biography box, which is exam material ("the Darwin of the 20th century"). They
        # are kept as their own small tree so they can be rendered and stored under
        # BOOK#<book>#<lang> / UNIT#<n>, which is where the schema puts them.
        # `unit_tree` is kept as a VIEW for consumers that want the unit alone; the real
        # tree below holds every node of the file so one walk covers the whole source.
        "unit_tree": build_tree(
            collapse_lists(stitch_across_pages(collect_blocks(unit_pages))),
            book_base, 0) if unit_pages else [],
        "unit_page_records": [{
            "page_file": p["page_file"],
            "printed": p.get("printed_page_number"),
            "page_side": p.get("page_side"),
            "footer": p.get("imprint"),
            # FURNITURE IS A BAND, A TAB OR A MOTIF -- NEVER MOST OF THE PAGE.
            #
            # Every page of the Class 12 scan carried an "i00N_header2.png" covering 88.4% of
            # the sheet, classified as `header art`. It is not art: it is a scan of nearly the
            # whole page, text and all. Drawn as a background with the live text rendered on
            # top, every page showed its own prose TWICE, offset and overlapping -- which is
            # unreadable and also hides that the real text is correct underneath.
            #
            # An external review predicted this exactly: "almost full-page areas are
            # classified as header art ... if those crops include original text, restoring the
            # missing assets could place scanned text underneath newly rendered text."
            #
            # A header band is a strip; a folio is a tab; a motif is a corner. None of them
            # covers a third of the page. Anything that does is a page scan, and on a page
            # that also sets live text it must not be drawn.
            "art": [{"kind": e.get("furniture"),
                     "z": e.get("z"),
                     "file": f"figures/{e['furniture_file']}",
                     "bbox": [round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"])]}
                    for e in p["elements_in_reading_order"]
                    if e["role"] == "page_furniture" and e.get("furniture_file")
                    and (e.get("furniture") == "page ground"
                         or (e.get("furniture") in ("header art", "qr code", "ornament")
                             and _is_furniture_sized(e, p)))] or None,
        } for p in unit_pages],
        "tree": _tagged(unit_nodes, tree),
        "text_join": join_stats,
        "layout_join": layout_stats,
        "special_join": special_stats,
    }
    if use_agent:
        join_agent_structure.apply_agent_structure(
            doc, layout, chapter, steps_dir=os.path.join(ROOT, "steps"))
    return doc, layout


# A QUESTION'S OPTIONS ARE ALTERNATIVES, NOT A SENTENCE.
#
# Question 7 prints three sequences to compare, one per row; question 9 prints five terms
# to define. Run together on one line -- "(a) Species Order Phylum Kingdom (b) Genus
# Species Order Kingdom (c) ..." -- they stop being alternatives a reader can compare,
# which is the entire point of the question. The book sets them on separate lines and so
# does the Markdown.
_PART = re.compile(r"\s*(\((?:[a-h]|i{1,3}|iv|v|vi{0,3}|ix|x)\))\s*")

def _split_parts(nn, _p):
    if nn.get("kind") != "question" or nn.get("parts"):
        return
    body = nn.get("body") or ""
    bits = _PART.split(body)
    if len(bits) < 5:                       # fewer than two labelled options
        return
    labels = [bits[i] for i in range(1, len(bits) - 1, 2)]
    # Only split a genuine run: (a)(b)(c) or (i)(ii)(iii), in order, starting at the first.
    if labels[0] not in ("(a)", "(i)"):
        return
    stem = bits[0].strip()
    # A part starts only at the NEXT label of the first label's own series. In a match-the-
    # following question `(a) Operculum (i) Ctenophora` is ONE row -- the (i) is the second
    # column -- and splitting on every label printed the two columns as sixteen parts.
    parts, cur = [], None
    for i in range(1, len(bits) - 1, 2):
        txt = (bits[i + 1] or "").strip()
        mk = bits[i].strip("()")
        if parts and cur is not None and mk not in _next_markers(cur):
            parts[-1]["body"] += f" {bits[i]} {txt}".rstrip()
            parts[-1]["body_md"] = parts[-1]["body"]
            continue
        if txt:
            cur = mk
            parts.append({"body": f"{bits[i]} {txt}", "body_md": f"{bits[i]} {txt}",
                          "marks": []})
    if len(parts) < 2 or not stem:
        return
    nn["body"] = stem
    nn["body_md"] = stem
    nn["sentences"] = ct.split_sentences(stem)
    nn["marks"] = [m for m in (nn.get("marks") or []) if m["to"] <= len(stem)]
    nn["parts"] = parts



def _imprint(v):
    """`2026-27`, never `Reprint Reprint 2026-27`.

    Some books print the bare year range in their imprint line and others print
    `Reprint 2026-27`; the Markdown header adds the word itself, so a book of the second
    kind came out saying it twice.
    """
    return re.sub(r"^\s*Reprint\s+", "", str(v or "")).strip() or "?"


_RUN_IN = re.compile(r"(?<![\d.])(\d{1,2})\.\s+")


def _fix_numbered_list(nn, _p):
    """A numbered list must hold each rule ONCE, as its own item.

    The four universal rules of nomenclature came out as four items where the FIRST held
    rules 1, 2 and 3 run together -- and then 2 and 3 appeared again as items of their own.
    A reader sees rule 2 twice and rule 3 twice, which is a content defect no stylesheet can
    repair: the extractor had the run-on block AND the split blocks and kept both.

    The numbers are consecutive, so the same sequential scan the exercises use applies here:
    split any item that contains a run, then drop any later item that merely repeats one.
    """
    if nn.get("kind") != "list" or not nn.get("items"):
        return
    out, seen, want = [], set(), 1
    for it in nn["items"]:
        t = (it.get("body") or "").strip()
        if not t:
            continue
        marks = _RUN_IN.findall(t)
        if len(marks) >= 2 and int(marks[0]) == want:
            # one item carrying several rules -- cut it at each expected number
            pos, cur = 0, want
            cuts = []
            while True:
                m = re.compile(r"(?<![\d.])" + str(cur) + r"\.\s+").search(t, pos)
                if not m:
                    break
                cuts.append((cur, m.end()))
                pos, cur = m.end(), cur + 1
            for i, (num, st) in enumerate(cuts):
                en = cuts[i + 1][1] - len(f"{cuts[i + 1][0]}. ") if i + 1 < len(cuts) else len(t)
                piece = t[st:en].strip()
                key = re.sub(r"\W+", "", piece.lower())[:60]
                if piece and key not in seen:
                    seen.add(key)
                    # RE-BASE THE MARKS, do not try to recover the markdown string.
                    # `body_md` is DERIVED from (body, marks); cutting a piece out of the
                    # body leaves the mark offsets pointing into the old string, so the
                    # emphasis silently disappears -- rule 4 kept its italic mark but
                    # printed `Mangifera indica` upright. Clip each mark to the piece,
                    # shift it, and regenerate the markdown from the two together.
                    off = st
                    pm = []
                    for m in (it.get("marks") or []):
                        f0, t0 = max(m["from"], off), min(m["to"], off + len(piece))
                        if t0 > f0:
                            pm.append({**m, "from": f0 - off, "to": t0 - off})
                    out.append({**it, "body": piece, "marks": pm,
                                "body_md": ct.to_body_md(piece, pm),
                                "sentences": ct.split_sentences(piece),
                                "number": str(num)})
                    want = num + 1
            continue
        m = _RUN_IN.match(t)
        num, piece = (m.group(1), t[m.end():].strip()) if m else (None, t)
        key = re.sub(r"\W+", "", piece.lower())[:60]
        if key in seen:
            continue                       # already emitted -- this is the duplicate
        seen.add(key)
        # Same re-basing as above: stripping the leading "4. " shifts every mark in the item
        # by three characters, and `body_md` must be regenerated from the shifted marks --
        # not copied from the plain text, which drops the emphasis entirely.
        off = len(t) - len(piece)
        pm = [{**m, "from": max(0, m["from"] - off), "to": m["to"] - off}
              for m in (it.get("marks") or []) if m["to"] - off > 0]
        out.append({**it, "body": piece, "marks": pm,
                    "body_md": ct.to_body_md(piece, pm),
                    "sentences": ct.split_sentences(piece), "number": num})
        if num:
            want = int(num) + 1
    if out:
        nn["items"] = out
        nn["ordered"] = any(i.get("number") for i in out)


# Letter-spaced text: single spaces BETWEEN LETTERS, wider gaps between words. The word gap
# is what tells them apart, so the collapse must keep it: `c a t e g o r i e s   s h o w i n g`
# is two words, and collapsing every space produced `categoriesshowing` -- trading one defect
# for a worse one, because a fused word is invisible to a reader skimming and to any search.
_SPACED = re.compile(r"(?:\b\w(?: |(?=\s{2,})|$)){4,}")


def _run_style(el, words=False):
    """{font, size, color, b, i} of an element's first printed run, or None.

    `words`: the first run holding a LETTER. A verso's running head opens with its folio --
    `12` in Bookman-Demi, then `B`+`IOLOGY` in Bookman-Light -- so the first run made every
    verso head of BIO11L ch02 bold.
    """
    r = next((r for r in el.get("runs") or [] if (r.get("t") or "").strip()
              and (not words or re.search(r"[A-Za-z]", r.get("t") or ""))), None)
    if not r:
        return None
    return {"font": r.get("font"), "size": r.get("size"), "color": r.get("color"),
            "b": bool(r.get("b")), "i": bool(r.get("i"))}


# The title is optional on the number's line: BIO12L ch02 sets each number in its own column,
# so the rail reads `2.1\nThe Male Reproductive\nSystem\n2.2\n...` -- one line per number.
_RAIL_NUM = re.compile(r"^\s*(\d+(?:\.\d+)+)(?:\s+(.*))?$")


def _rail_items(text):
    """`1.1 Flower ...\n1.2 Pre-fertilisation ...` -> [{num, title}] in printed order."""
    out = []
    for ln in (text or "").split("\n"):
        m = _RAIL_NUM.match(ln)
        if m:
            out.append({"num": m.group(1), "title": (m.group(2) or "").strip()})
        elif ln.strip() and out:
            out[-1]["title"] = (out[-1]["title"] + " " + ln.strip()).strip()
        elif ln.strip():
            out.append({"num": None, "title": ln.strip()})
    return out


def _merge_split_rail(entries, keep_closers=False):
    """Rejoin a rail entry the text layer cut in two: number + last title line, and the rest.

    BIO12L ch05's rail came back as `The Search for Genetic` (no number) and `5.2 Material`,
    `5.4` and `Replication` -- the number's block took the title's turnover line, so the MD
    listed a numberless entry and the page printed `Material` over `The Search for Genetic`.
    An unnumbered entry whose first line sits on the same printed row as a numbered entry to
    its left opens that entry's title.
    """
    if not entries:
        return entries
    indents = [e["indent_pt"] for e in entries if e.get("indent_pt")]
    out = list(entries)
    for e in entries:
        its = e.get("items") or []
        if len(its) != 1 or its[0].get("num") or e not in out:
            continue
        host = next((h for h in out if h is not e and len(h.get("items") or []) == 1
                     and h["items"][0].get("num") and h["bbox"][0] < e["bbox"][0]
                     and abs(h["bbox"][1] - e["bbox"][1]) < 0.006), None)
        if host is None:
            continue
        num = host["items"][0]["num"]
        title = " ".join(x for x in (its[0]["title"], host["items"][0]["title"]) if x)
        host.update(items=[{"num": num, "title": title}], text=f"{num} {title}",
                    bbox=[round(min(host["bbox"][0], e["bbox"][0]), 4),
                          round(min(host["bbox"][1], e["bbox"][1]), 4),
                          round(max(host["bbox"][2], e["bbox"][2]), 4),
                          round(max(host["bbox"][3], e["bbox"][3]), 4)],
                    indent_pt=host.get("indent_pt") or (max(set(indents), key=indents.count)
                                                         if indents else None))
        out.remove(e)
    # ...and a TURNOVER LINE BELOW its entry ends that entry's title. BIO11L ch05 p003 prints
    # `5.8 Semi-technical Description of a` / `Typical Flowering Plant`: the second line came back
    # as an entry with no number, and the JSON and the MD listed it as a section of its own. An
    # unnumbered entry set just under a numbered one and indented past its number joins it.
    for e in list(out):
        its = e.get("items") or []
        if len(its) != 1 or its[0].get("num"):
            continue
        k = out.index(e)
        host = out[k - 1] if k else None
        if not host or len(host.get("items") or []) != 1 or not host["items"][0].get("num"):
            continue
        # The rail's closing `Summary` / `Exercises` lines are entries of their own, not the
        # last section's turnover (PHY11L ch01: `1.6 ... applications Summary Exercises`).
        if keep_closers and re.fullmatch(r"(?:Summary|Exercises|Points to Ponder|Appendix)(?:\s+\S.*)?",
                                         (its[0].get("title") or "").strip()):
            continue
        hb, eb = host["bbox"], e["bbox"]
        line = max(eb[3] - eb[1], 0.012)
        if not (eb[0] > hb[0] + 0.005 and -0.004 <= eb[1] - hb[3] <= 1.5 * line):
            continue
        num = host["items"][0]["num"]
        title = " ".join(x for x in (host["items"][0]["title"], its[0]["title"]) if x)
        host.update(items=[{"num": num, "title": title}], text=f"{num} {title}",
                    bbox=[round(min(hb[0], eb[0]), 4), round(min(hb[1], eb[1]), 4),
                          round(max(hb[2], eb[2]), 4), round(max(hb[3], eb[3]), 4)])
        out.remove(e)
    return out


def _rail_indent(el):
    """Points from an entry's number to its title, measured on the rail's own lines."""
    lines = el.get("line_boxes_pt") or []
    # A line that STARTS with the number counts as the number's: the layer joins `6.4` and
    # `What is Adaptive` into one line (BIO12L ch06 p001), and only a bare `6.4` was taken, so
    # 6.4-6.9 had no indent and printed inline. The title's x is then its turnover line's.
    num = re.compile(r"\d+(\.\d+)+(\s|$)")
    nums = [ln["bbox_pt"][0] for ln in lines if num.match((ln.get("text") or "").strip())]
    rest = [ln["bbox_pt"][0] for ln in lines if not num.match((ln.get("text") or "").strip())]
    if nums and rest and min(rest) > min(nums):
        return round(min(rest) - min(nums), 1)
    return None


def _is_furniture_sized(el, page):
    """False for a crop big enough to be a scan of the page rather than a piece of furniture.

    See the note on `art` in the page record. The threshold is deliberately generous -- the
    tallest genuine furniture in this corpus is a chapter opener's banner at roughly a third
    of the sheet -- so only a crop that is plainly a whole-page scan is rejected, and only
    when the page also carries live text that the scan would duplicate.
    """
    bb = el.get("bbox_sheet") or el.get("bbox") or []
    if len(bb) != 4:
        return True
    area = (bb[2] - bb[0]) * (bb[3] - bb[1])
    if area < 0.34:
        return True
    has_text = any((e.get("text") or "").strip()
                   for e in page.get("elements_in_reading_order") or []
                   if e.get("role") not in ("page_furniture",))
    return not has_text


def _merge_split_captions(tree):
    """One figure, one caption. Rejoin a caption the text layer cut in half.

    NCERT sets its figure captions in a narrow rail under the artwork, so a long one breaks
    into several text blocks. Each block became its OWN figure node: Class 11 ch01 ended up
    with two "figures" that were really the two halves of Figure 1.1's caption --
    `Figure 1.1 Taxonomic` and `categories showing hierarchial arrangement in ascending
    order` -- and neither had any artwork, because the diagram itself is vector and left no
    block at all. The chapter's most-cited diagram was therefore absent while two fragments
    of its caption sat in the tree pretending to be figures.

    A fragment is a continuation when it follows a numbered caption on the same page and does
    not start a caption of its own. It is folded into the one above it and its node removed.
    """
    def prune(nodes):
        out = []
        for n in nodes:
            if n.get("children"):
                n["children"] = prune(n["children"])
            if n.get("kind") == "figure" and out:
                prev = out[-1]
                same_page = (n.get("page_file") or "") == (prev.get("page_file") or "")
                cap = (n.get("caption") or "").strip()
                prev_cap = (prev.get("caption") or "").strip()
                starts_own = re.match(r"^(?:Figure|Fig\.|Table)\s*\d", cap)
                if (prev.get("kind") == "figure" and same_page and cap and prev_cap
                        and not starts_own
                        and re.match(r"^(?:Figure|Fig\.|Table)\s*\d", prev_cap)):
                    # Two spaces when either half is letter-spaced: that is the word gap
                    # `_despace` keeps, so the seam does not fuse two words.
                    joiner = ("" if prev_cap.endswith("-") else
                              "  " if _SPACED.search(cap) or _SPACED.search(prev_cap) else " ")
                    # The second half's marks shift by the first half's length plus the joiner.
                    base = len(prev_cap.rstrip("-") + joiner)
                    prev["caption_marks"] = (prev.get("caption_marks") or []) + [
                        {**m, "from": m["from"] + base, "to": m["to"] + base}
                        for m in (n.get("caption_marks") or [])]
                    prev["caption"] = (prev_cap.rstrip("-") + joiner + cap).strip()
                    continue
            out.append(n)
        return out

    tree[:] = prune(tree)


def _despace(t):
    """`c a t e g o r i e s   s h o w i n g` -> `categories showing`.

    Each run of letter-spaced characters is closed up on its own; the two-or-more-space gaps
    that separate WORDS are preserved as single spaces. Collapsing those too is how
    `categoriesshowing` happened.
    """
    if not t or not _SPACED.search(t):
        return t

    def close(m):
        return re.sub(r" (?= )|(?<= ) ", "", m.group(0))

    out = []
    for chunk in re.split(r"(\s{2,})", t):
        if chunk.strip() and _SPACED.search(chunk):
            chunk = _SPACED.sub(lambda m: m.group(0).replace(" ", ""), chunk)
        out.append(chunk)
    return re.sub(r"\s{2,}", " ", "".join(out)).strip()


def _clean_text(nn, _p):
    """Repair text defects that are wrong in EVERY renderer, not just in HTML.

    Three kinds, all found by review rather than by any check:
      * LETTER-SPACED CAPTIONS. A caption set with tracking comes out of the text layer as
        `c a t e g o r i e s   s h o w i n g`, which is not a word in any search index.
      * A SUPERSCRIPT ZERO USED AS A DEGREE SIGN -- `-196\u2070C` is not a temperature.
      * A MISSING SENTENCE SPACE -- `pollinators.You'll` is two sentences welded together.

    EVERY OFFSET INTO A REPAIRED STRING MOVES WITH IT. The marks were left where they were, so
    each inserted sentence space pushed every later bold one character off its word: BIO11L
    ch06 p073 shipped `**vascular cambiu**m`, ` **close**d`, ` **radia**l` in the JSON, the
    Markdown and the page. Marks, sentences, per-page `char_ranges` and caption marks are now
    carried through the edit (caption marks used to be dropped outright).
    """
    def fix(t):
        t = _despace(t)
        t = t.replace("\u2070C", "\u00b0C").replace("\u2070 C", "\u00b0C")
        return re.sub(r"(?<=[a-z]{2})\.(?=[A-Z][a-z])", ". ", t)

    for key in ("body", "body_md", "caption", "title"):
        t = nn.get(key)
        if not isinstance(t, str) or not t:
            continue
        new = fix(t)
        if new == t:
            continue
        nn[key] = new
        if key == "body":
            f = _offset_map(t, new)
            if nn.get("marks"):
                nn["marks"] = _remap_marks(nn["marks"], f)
            if nn.get("char_ranges"):
                nn["char_ranges"] = [{**r, "from": f(r["from"]), "to": f(r["to"])}
                                     for r in nn["char_ranges"]]
            if nn.get("sentences"):
                nn["sentences"] = ct.split_sentences(new)
        elif key == "caption" and nn.get("caption_marks"):
            nn["caption_marks"] = _remap_marks(nn["caption_marks"], _offset_map(t, new))
    for it in nn.get("items") or []:
        for key in ("body", "body_md"):
            t = it.get(key)
            if isinstance(t, str) and t:
                new = fix(t)
                if key == "body" and new != t and it.get("marks"):
                    it["marks"] = _remap_marks(it["marks"], _offset_map(t, new))
                it[key] = new


def _offset_map(old, new):
    """o -> its position in `new`, for a string edited from `old` (insertions and deletions)."""
    import difflib
    ops = difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes()

    def f(o):
        for tag, i1, i2, j1, j2 in ops:
            if i1 <= o < i2:
                return j1 + (o - i1) if tag == "equal" else min(j2, j1 + (o - i1))
        return len(new)
    return f


def _remap_marks(marks, f):
    out = []
    for m in marks:
        # The end through its LAST character, so a space inserted right after a mark stays out.
        a, z = f(m["from"]), (f(m["to"] - 1) + 1 if m["to"] > m["from"] else f(m["to"]))
        if z > a:
            out.append({**m, "from": a, "to": z})
    return out


def to_markdown(doc):
    """The chapter as CommonMark -- any renderer shows it correctly.

    Built from `body_md`, which already carries the bold and italic as `**`/`*`, so the
    Markdown needs no formatting logic of its own and cannot drift from the JSON.
    """
    ch = doc["chapter"]
    out = [f"# {ch['title'].strip()}", "",
           f"*{doc['subject'].title()} · Class {doc['grade']} · "
           f"{'new' if doc['edition']=='latest' else 'old'} NCERT · chapter {ch['number']} · "
           f"reprint {_imprint(doc.get('reprint'))}*", ""]
    if ch.get("pages"):
        out.append(f"*Printed pages {ch['pages'][0]}–{ch['pages'][1]}*")
        out.append("")

    def rec(nodes, depth):
        for n in nodes:
            k = n["kind"]
            # The opener's contents rail is printed beside the title: the chapter's own list of
            # sections, set in the margin (`pages[].contents_rail`). It follows the titles.
            if k != "chapter_title" and rails.get(n.get("page_file")):
                for rail in rails.pop(n.get("page_file")):
                    # One bullet per ENTRY, not per printed line: a multi-line entry inside
                    # one `*...*` broke the emphasis at the first line end, and BIO12L ch02's
                    # rail, which sets each number on its own line, came out as 18 bullets.
                    for it in rail:
                        entry = " ".join(x for x in (it.get("num"), it.get("title")) if x)
                        if entry.strip():
                            out.append(f"- *{entry.strip()}*")
                out.append("")
            if k in ("section", "summary", "exercises"):
                title = (ct.to_body_md(n.get("title") or "", n["title_marks"])
                         if n.get("title_marks") else n.get("title"))
                head = " ".join(x for x in (n.get("number"), title) if x)
                out.append(f"{'#' * min(6, depth + 2)} {head}")
                out.append("")
                rec(n.get("children") or [], depth + 1)
            elif k == "table" and n.get("table_grid"):
                # A TABLE IS A TABLE, NOT A PICTURE OF ONE.
                # It was emitted as an image, so every cell -- the thing a flashcard or a PYQ
                # actually cites -- was unreadable, unsearchable and untranslatable in the
                # Markdown. The grid is measured and stored; it is written out as a grid.
                g = n["table_grid"]
                rows = [[(c or "").replace("|", "\\|").replace("\n", " ").strip()
                         for c in r] for r in g["cells"]]
                if rows:
                    cap = (n.get("caption") or "").strip()
                    if cap:
                        out.append(_md_caption(n))
                        out.append("")
                    # The cells' italics as the exact render sets them (`cell_italics`); a cell
                    # with superscripts or subscripts (`I<sup>A</sup>`) is written from its marks.
                    ital = n.get("cell_italics") or []
                    rows = [[(ct.to_body_md(g["cells"][ri][ci], mk)
                              if (mk := join_agent_special.cell_marks(
                                g, ri, ci, ital)) else _md_cell(c, ital))
                             for ci, c in enumerate(r)] for ri, r in enumerate(rows)]
                    width = max(len(r) for r in rows)
                    rows = [r + [""] * (width - len(r)) for r in rows]
                    out.append("| " + " | ".join(rows[0]) + " |")
                    out.append("|" + "|".join([" --- "] * width) + "|")
                    for r in rows[1:]:
                        out.append("| " + " | ".join(r) + " |")
                    out.append("")
            elif k in ("figure", "table"):
                # Our checked drawing where there is one (`_attach_drawn_figures`), else the crop.
                src = n.get("image_drawn") or n.get("image") or n.get("image_local")
                cap = (n.get("caption") or "").strip()
                panels = [q for q in n.get("panels") or [] if q.get("image") or q.get("image_local")]
                if panels:
                    # One image per printed panel, each named for its letter, so `Figure 2.5
                    # (b)` is its own picture with its own link -- not three in one crop.
                    num = f"Figure {n['number']}" if n.get("number") else "Figure"
                    for q in panels:
                        out.append(f"![{num} {q['label']}]({q.get('image') or q['image_local']})")
                        out.append("")
                elif src:
                    # An uncaptioned picture says what it shows (`alt`, e.g. BIO11L ch04 p047's
                    # Vertebrata classification chart) rather than `![]`.
                    out.append(f"![{cap or (n.get('alt') or '').strip()}]({src})")
                    out.append("")
                if cap:
                    # The caption as printed: its label bold, the rest with its own marks --
                    # not the whole caption in italics, which the book never sets.
                    out.append(_md_caption(n))
                    out.append("")
            elif k == "question":
                # THE NUMBER IS PART OF THE QUESTION, in Markdown as much as in HTML.
                # Ten exercises came out as ten anonymous paragraphs, which no question bank
                # can cite and no reader can match to the book.
                num = (n.get("number") or "").strip()
                body = n.get("body_md") or n.get("body", "")
                # `1.3` (Physics, chapter.question) prints bold with no stop, as the book does.
                out.append((f"**{num}** {body}" if "." in num else f"{num}. {body}")
                           if num else body)
                # Sub-parts as the book sets them. One printed line (`parts_inline`, e.g. the
                # (i)-(v) terms) stays one line; otherwise each part is its own paragraph inside
                # the list item -- consecutive indented lines with no blank between them are
                # ONE paragraph to a Markdown renderer, which ran question 7's three sequences
                # together.
                subs = [s.get("body_md") or s.get("body", "") for s in n.get("parts") or []
                        if (s.get("body") or "").strip()]
                sps = [s for s in n.get("parts") or [] if (s.get("body") or "").strip()]
                first = next((i for i, s in enumerate(sps) if s.get("columns")), None)
                if first is not None:
                    # A match-the-following question: its two columns as a table, as printed.
                    # The header is the book's own `Column I` / `Column II` parts when it prints
                    # them (BIO11L ch08), else empty -- never words the book does not print.
                    def cell(text, mk):
                        return ct.to_body_md(text, mk).replace("|", "\\|")
                    head = sps[first - 2:first] if first >= 2 and not any(
                        s.get("columns") for s in sps[first - 2:first]) else []
                    cells = [cell(s.get("body", ""), s.get("marks") or []) for s in head]
                    # ...or ONE part holding both, as the agent reads the header line (BIO11L
                    # ch15-ch19): it was printed under the table as `**Column I Column II**`
                    # and the table's header row came out empty.
                    hm = (re.match(r"^\s*(Column\s+I)\s+(Column\s+II)\s*$",
                                   sps[first - 1].get("body", ""), re.I)
                          if not head and first >= 1 and not sps[first - 1].get("columns")
                          else None)
                    if hm:
                        head = [sps[first - 1]]
                        bold = any(mk.get("b") for mk in sps[first - 1].get("marks") or [])
                        cells = [f"**{g}**" if bold else g for g in hm.groups()]
                    out.append("")
                    out.append("   | " + " | ".join(cells) + " |" if cells else "   |  |  |")
                    out.append("   |---|---|")
                    for s in sps[first:]:
                        if s.get("columns"):
                            cm = s.get("column_marks") or [[], []]
                            out.append(f"   | {cell(s['columns'][0], cm[0])} "
                                       f"| {cell(s['columns'][1], cm[1])} |")
                    taken = {id(s) for s in head} | {id(s) for s in sps if s.get("columns")}
                    subs = [s.get("body_md") or s.get("body", "") for s in sps
                            if id(s) not in taken]
                if subs and n.get("parts_inline"):
                    out.append("")
                    out.append("   " + "  ".join(subs))
                else:
                    for sub in subs:
                        out.append("")
                        out.append(f"   {sub}")
                out.append("")
            elif k == "list":
                # An ORDERED list where the book numbers its items. `- 1.` gives a bullet in
                # front of a numeral, which is neither what the book prints nor valid
                # structure -- the number is the list marker, not part of the text.
                items = n.get("items") or []
                if n.get("ordered"):
                    for it in items:
                        num = it.get("number")
                        out.append(f"{num}. {it['body_md']}" if num
                                   else f"   {it['body_md']}")
                else:
                    for it in items:
                        out.append(f"- {it['body_md']}")
                out.append("")
            elif k == "chapter_title":
                # `Unit 1`, `CHAPTER 1`, `THE LIVING WORLD` are titles on the page, not prose.
                # The chapter's own name is already the `#` heading; repeating it as `##`
                # opened BIO11L ch02 with the title twice.
                if (re.sub(r"[^a-z0-9]", "", (n.get("body") or "").lower())
                        != re.sub(r"[^a-z0-9]", "", (ch.get("title") or "").lower())):
                    out.append(f"## {n.get('body_md') or n.get('body', '')}")
                    out.append("")
            else:
                out.append(n.get("body_md") or n.get("body", ""))
                out.append("")
    rails = {p.get("page_file"): [r.get("items") or _rail_items(r.get("text"))
                                  for r in p.get("contents_rail") or [] if r.get("text")]
             for p in doc.get("pages") or [] if p.get("contents_rail")}
    rec(doc["tree"], 0)
    return "\n".join(out).rstrip() + "\n"


def _md_caption(n):
    """A figure or table caption with its own marks, as Markdown."""
    cap = (n.get("caption") or "").strip()
    # A printed asterisk (Table 9.1's footnote mark, `... Living Matter*`) is escaped, or the bold
    # caption ends `Matter***` and a Markdown renderer misreads the emphasis. A same-length
    # placeholder keeps every mark offset valid.
    md = ct.to_body_md(cap.replace("*", "\x00"), n.get("caption_marks") or [])
    return md.replace("\x00", "\\*")


def _md_cell(text, italics):
    """A table cell with the fragments the page printed in italic, as `_cell` in the render."""
    out = text
    for frag in sorted(italics, key=len, reverse=True):
        if frag in out and f"*{frag}" not in out:
            out = out.replace(frag, f"*{frag}*")
    return out


# ---------------------------------------------------------------------------------------------
# THE JSON MUST STAND ON ITS OWN
# ---------------------------------------------------------------------------------------------
#
# chapter.json is what is stored (DynamoDB rows are cut from it), and a consumer renders ONE
# node from it with no access to the PDF, the layout or the exact renderer's workarounds. The
# exact render looked right while the JSON under it was wrong in ways the renderer quietly
# compensated for -- measured on BIO11L ch01:
#
#   * all ten exercise questions carried ONE box, the whole Exercises region; the renderer
#     stacked them in a shared container, but a consumer placing question 5 had nowhere to put it;
#   * boxes named their page by printed folio only, and the opener pages print none, so the
#     chapter title, the opening paragraph and the 1.1 heading had `pages: []`;
#   * the Ernst Mayr caption was printed in the photograph's crop as PIXELS and existed nowhere as
#     text -- not in the JSON, not in the Markdown, not searchable;
#   * Table 1.1's italics existed only as glyphs in the PDF (`cell_italics` was empty), and its
#     `table_text` stopped after Housefly while the grid held all four organisms;
#   * the unit pages were stored twice (`unit_tree` and `belongs: unit` in `tree`) under
#     different ids, so any traversal indexed them twice.
#
# This runs LAST, after every pass that creates or moves a node, so nothing can out-step it.

_CAPTION_LABEL = re.compile(r"^((?:Figure|Fig\.|TABLE|Table)\s*\d+(?:\.\d+)*)")


def _box_px(bb, rect):
    return [bb[0] * rect.width, bb[1] * rect.height, bb[2] * rect.width, bb[3] * rect.height]


def _norm_box(r, rect):
    return [round(max(0.0, r[0] / rect.width), 4), round(max(0.0, r[1] / rect.height), 4),
            round(min(1.0, r[2] / rect.width), 4), round(min(1.0, r[3] / rect.height), 4)]


def _pdf_lines(page, area):
    """Text lines of `page` whose centre lies in `area` (points), top to bottom."""
    import pymupdf
    out = []
    for b in page.get_text("dict", clip=pymupdf.Rect(*area))["blocks"]:
        for ln in b.get("lines", []):
            x0, y0, x1, y1 = ln["bbox"]
            cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
            t = "".join(s["text"] for s in ln["spans"]).strip()
            if t and area[0] <= cx <= area[2] and area[1] <= cy <= area[3]:
                out.append({"bbox": [x0, y0, x1, y1], "text": t, "spans": ln["spans"]})
    out.sort(key=lambda l: (round(l["bbox"][1]), l["bbox"][0]))
    # one printed line per baseline: spans on the same baseline are one line
    merged = []
    for ln in out:
        if merged and abs(merged[-1]["bbox"][3] - ln["bbox"][3]) <= 2.5:
            m = merged[-1]
            m["bbox"] = [min(m["bbox"][0], ln["bbox"][0]), min(m["bbox"][1], ln["bbox"][1]),
                         max(m["bbox"][2], ln["bbox"][2]), max(m["bbox"][3], ln["bbox"][3])]
            m["text"] = (m["text"] + " " + ln["text"]).strip()
            m["spans"] = m["spans"] + ln["spans"]
        else:
            merged.append(dict(ln))
    return merged


def _is_bold(span):
    f = span.get("font") or ""
    return bool(span.get("flags", 0) & 16) or any(k in f for k in ("Bold", "Demi", "Black"))


def _is_italic(span):
    f = span.get("font") or ""
    return bool(span.get("flags", 0) & 2) or "Italic" in f or "Oblique" in f


def _caption_under_photo(n, page, pf, folio, cdir):
    """A photograph with its name printed under it, inside the photo's measured box, has that
    name as its caption -- as TEXT, with the picture re-cut to the photograph alone."""
    if (n.get("caption") or "").strip() or n.get("number") or not n.get("boxes"):
        return False
    box = n["boxes"][0]
    if not box.get("bbox"):
        return False
    rect = page.rect
    area = _box_px(box["bbox"], rect)
    photos = []
    for info in page.get_image_info():
        r = info["bbox"]
        ix = min(r[2], area[2]) - max(r[0], area[0])
        iy = min(r[3], area[3]) - max(r[1], area[1])
        a = max(1e-6, (r[2] - r[0]) * (r[3] - r[1]))
        if ix > 0 and iy > 0 and ix * iy / a >= 0.5 and (r[2] - r[0]) * (r[3] - r[1]) > 2000:
            photos.append([max(r[0], area[0]), max(r[1], area[1]),
                           min(r[2], area[2]), min(r[3], area[3])])
    if not photos:
        return False
    ph = [min(p[0] for p in photos), min(p[1] for p in photos),
          max(p[2] for p in photos), max(p[3] for p in photos)]
    lines = [l for l in _pdf_lines(page, area) if l["bbox"][1] >= ph[3] - 2]
    if not lines or len(lines) > 3 or sum(len(l["text"]) for l in lines) > 80:
        return False
    if all(re.fullmatch(r"\(?[a-z]{1,3}\)?", l["text"]) for l in lines):
        return False                                # panel letters, not a caption
    cap, marks, starts = "", [], []
    for l in lines:
        if cap:
            cap += " "
        starts.append(len(cap))
        for s in l["spans"]:
            t = s["text"]
            if not t:
                continue
            a = len(cap)
            cap += t
            if _is_bold(s) and t.strip():
                marks.append({"from": a + (len(t) - len(t.lstrip())), "to": a + len(t.rstrip()),
                              "b": True})
        cap = cap.rstrip()
    cap = re.sub(r"\s+", " ", cap).strip()
    lb = [min(l["bbox"][0] for l in lines), min(l["bbox"][1] for l in lines),
          max(l["bbox"][2] for l in lines), max(l["bbox"][3] for l in lines)]
    n["caption"] = cap
    n["caption_marks"] = [m for m in marks if m["to"] <= len(cap)]
    n["caption_line_starts"] = starts
    n["caption_line_count"] = len(lines)
    n["caption_print_size_pt"] = round(lines[0]["spans"][0]["size"], 2)
    n["caption_box"] = {"page": folio, "page_file": pf, "src": "measured",
                        "bbox": _norm_box(lb, rect)}
    n["caption_source"] = "pdf-text-layer"
    # The artwork is the photograph alone, re-cut, so the caption is not printed twice.
    n["boxes"] = [{**box, "bbox": _norm_box(ph, rect), "src": "measured",
                   "page_file": pf, "page": folio}] + n["boxes"][1:]
    local = n.get("image_local")
    if local:
        import pymupdf
        pad = 2.0
        clip = pymupdf.Rect(max(0, ph[0] - pad), max(0, ph[1] - pad),
                            min(rect.width, ph[2] + pad), min(rect.height, ph[3] + pad))
        page.get_pixmap(dpi=200, clip=clip).save(os.path.join(cdir, local))
        n.pop("image", None)
        n.pop("image_sha256", None)
        # The crop's rect is now THIS clip. Left at the first cut's rect (which took in the
        # caption), the render stretched the photo over its own caption (BIO11L ch05 p002,
        # Katherine Esau).
        n["image_bbox"] = _norm_box([clip.x0, clip.y0, clip.x1, clip.y1], rect)
    return True


def _question_boxes(questions, page, pf, folio):
    """Each exercise question's OWN measured box, from the PDF lines in their shared region."""
    rect = page.rect
    area = _box_px(questions[0]["boxes"][0]["bbox"], rect)
    area = [area[0] - 2, area[1] - 2, area[2] + 2, area[3] + 2]
    lines = _pdf_lines(page, area)
    starts = {}
    for i, l in enumerate(lines):
        m = re.match(r"^(\d{1,2})\.(?:\s|$)", l["text"])
        if m and m.group(1) not in starts:
            starts[m.group(1)] = i
    nums = [str(q.get("number")) for q in questions]
    if not all(k in starts for k in nums):
        return False
    order = sorted(nums, key=lambda k: starts[k])
    for k, q in zip(nums, questions):
        a = starts[k]
        nxt = [starts[o] for o in order if starts[o] > a]
        b = min(nxt) if nxt else len(lines)
        own = lines[a:b]
        bb = [min(l["bbox"][0] for l in own), min(l["bbox"][1] for l in own),
              max(l["bbox"][2] for l in own), max(l["bbox"][3] for l in own)]
        q["boxes"] = [{"page": folio, "page_file": pf, "src": "measured",
                       "bbox": _norm_box(bb, rect)}]
        q["line_count"] = len(own)
        if len(own) > 1:
            gaps = sorted(own[j + 1]["bbox"][3] - own[j]["bbox"][3] for j in range(len(own) - 1))
            q["line_pitch_pt"] = round(gaps[len(gaps) // 2], 2)
        # WHERE THE TEXT HANGS: from the number to the text on its own baseline. It differs by
        # chapter -- 18pt in BIO11L ch07, 20.9pt in ch13 -- and the stylesheet's one 6.5mm
        # (18.4pt) set ch13's turnover lines 2.5pt left of the book's and wrapped Q4 a word early.
        # `_pdf_lines` joins a baseline's spans, so the number is found among the spans.
        sps = sorted((s for s in lines[a].get("spans") or [] if s["text"].strip()),
                     key=lambda s: s["bbox"][0])
        if sps and re.fullmatch(r"\d{1,2}\.", sps[0]["text"].strip()) and len(sps) > 1:
            hang = sps[1]["bbox"][0] - sps[0]["bbox"][0]
            if 10.0 <= hang <= 40.0:
                q["hang_pt"] = round(hang, 1)
        q.pop("char_ranges", None)
    return True


def _distribute_question_boxes(questions):
    """Each exercise question takes ITS OWN measured lines, not the whole list's.

    BIO12L ch03 p050: the twelve questions came out of the exercise split each carrying all
    sixteen boxes of the list they were cut from, so the render set every question at once in
    the first and the page's questions stacked into its top half. In the book a question opens
    at the question indent and its sub-parts sit further in; walking the boxes top to bottom, a
    box at the question indent starts the next question and an indented box joins the current
    one. Applied only when every question shares the same box list and the question-indent
    boxes are exactly as many as the questions. Each question gets the union of its boxes.
    Returns the number of questions given boxes.
    """
    if len(questions) < 2 or not all(len(q.get("boxes") or []) > 1 for q in questions):
        return 0
    key = json.dumps([b.get("bbox") for b in questions[0]["boxes"]])
    if any(json.dumps([b.get("bbox") for b in q["boxes"]]) != key for q in questions[1:]):
        return 0
    boxes = sorted(questions[0]["boxes"], key=lambda b: b["bbox"][1])
    indent = min(b["bbox"][0] for b in boxes)
    starts = [i for i, b in enumerate(boxes) if b["bbox"][0] <= indent + 0.015]
    if len(starts) != len(questions):
        return 0
    for k, q in enumerate(questions):
        mine = boxes[starts[k]:(starts[k + 1] if k + 1 < len(starts) else len(boxes))]
        bb = [round(min(b["bbox"][0] for b in mine), 4), round(min(b["bbox"][1] for b in mine), 4),
              round(max(b["bbox"][2] for b in mine), 4), round(max(b["bbox"][3] for b in mine), 4)]
        q["boxes"] = [{**mine[0], "bbox": bb}]
    return len(questions)


def _distribute_after_continued_part(questions):
    """The questions on the page a continued question's parts spill onto get their own boxes.

    BIO12L ch10 p187: question 4's options (b)-(d) print at the head of the page (parts with
    `page_file` and `region`), then questions 5-13. The exercises span two pages, so the
    questions carry two different box lists and `_distribute_question_boxes` declined them all;
    5-13 kept every box on p187, the continuation strip included, and the render set them over
    (b)-(d). Per page's box list, the box a continued part claims is dropped and the rest are
    distributed as usual. Only pages holding such a part are touched. Returns questions given boxes.
    """
    claimed = {json.dumps([round(v, 4) for v in sp["region"]])
               for q in questions for sp in q.get("parts") or []
               if sp.get("page_file") and sp.get("region")}
    if not claimed:
        return 0
    groups = collections.defaultdict(list)
    for q in questions:
        if len(q.get("boxes") or []) > 1:
            groups[json.dumps([b.get("bbox") for b in q["boxes"]])].append(q)
    done = 0
    for grp in groups.values():
        boxes = grp[0]["boxes"]
        keep = [b for b in boxes
                if json.dumps([round(v, 4) for v in b.get("bbox") or []]) not in claimed]
        if len(keep) == len(boxes) or len(grp) < 2:
            continue
        for q in grp:
            q["boxes"] = keep
        got = _distribute_question_boxes(grp)
        if not got:
            for q in grp:
                q["boxes"] = boxes
        done += got
    return done


def _list_marks_from_pdf(n, page):
    """Bold and italic the PDF prints inside a list's box, onto items that lack them.

    A2 read the three steps of the fungal sexual cycle as one list block and the layer's runs
    covered only item (i), so `karyogamy` in item (ii) printed bold in the book and plain in
    every output (BIO11L ch02 p017). Returns the number of marks added.

    ONLY THE COPIES THE BOOK STYLES. A styled run used to mark its first unmarked occurrence
    even when the item already carried it: BIO12L ch05 p095 bolds `In capping` and `In
    tailing`, the join had both right, and this added bold to the earlier `called as capping
    and tailing` too. So a word gets a mark only while the box prints more styled copies of it
    than the items already carry, and the copy chosen is the one preceded by the word the book
    prints before the run.
    """
    runs = collections.defaultdict(list)          # (style, text) -> [word printed before it]
    for l in _pdf_lines(page, _box_px(n["boxes"][0]["bbox"], page.rect)):
        before = ""
        for s in l["spans"]:
            st = "b" if _is_bold(s) else "i" if _is_italic(s) else None
            t = re.sub(r"\s+", " ", s["text"]).strip(" ,;:.()")
            if st and len(re.sub(r"[^A-Za-z]", "", t)) >= 3:
                runs[(st, t)].append((re.findall(r"[A-Za-z0-9]+", before) or [""])[-1].lower())
            before += s["text"]
    added = 0
    for (st, t), prevs in runs.items():
        rx = re.compile(r"(?<![A-Za-z0-9])" + r"\s+".join(map(re.escape, t.split()))
                        + r"(?![A-Za-z0-9])")
        free, have = [], 0
        for it in n["items"]:
            body = it.get("body") or ""
            for m in rx.finditer(body):
                if any(x.get(st) and x["from"] < m.end() and x["to"] > m.start()
                       for x in it.get("marks") or []):
                    have += 1
                else:
                    word = (re.findall(r"[A-Za-z0-9]+", body[:m.start()]) or [""])[-1].lower()
                    free.append((it, m, word))
        for prev in prevs[have:]:
            if not free:
                break
            pick = next((f for f in free if f[2] == prev), free[0])
            free.remove(pick)
            it, m, _w = pick
            body = it.get("body") or ""
            marks = it.setdefault("marks", [])
            marks.append({"from": m.start(), "to": m.end(), st: True})
            marks.sort(key=lambda x: x["from"])
            it["body_md"] = ct.to_body_md(body, marks)
            added += 1
    return added


def _table_italics(n, page):
    """Italic fragments printed inside the table's box (genus and binomial names)."""
    area = _box_px(n["boxes"][0]["bbox"], page.rect)
    out = []
    for l in _pdf_lines(page, area):
        for s in l["spans"]:
            t = re.sub(r"\s+", " ", s["text"]).strip(" ,;:.")
            if _is_italic(s) and len(t) >= 2 and t not in out:
                out.append(t)
    return out


_SUB_FORM = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def _table_scripts(n, page):
    """The subscripts the book printed inside a table, put back into its agent-read cells.

    A2S reads a table's cells off the picture and writes `CO2` and `C3 Plants`; Table 11.1
    (BIO11L ch11 p148) prints `CO₂` and `C₃ Plants` in every row, and the JSON, the Markdown
    and the page all showed plain digits. The text layer sets each such digit as a small span
    right after the word it belongs to: every `word + small digits` pair printed inside the
    table's box is rewritten wherever that exact token stands in the cells. Returns the
    number of cells changed.
    """
    area = _box_px(n["boxes"][0]["bbox"], page.rect)
    toks = set()
    for l in _pdf_lines(page, area):
        sp = [s for s in l["spans"] if s["text"].strip()]
        for prev, s in zip(sp, sp[1:]):
            m = re.search(r"([A-Za-z]{1,4})\s*$", prev["text"])
            if (m and re.fullmatch(r"\s*\d{1,2}\s*", s["text"]) and s["size"] <= 0.8 * prev["size"]
                    and s["bbox"][0] - prev["bbox"][2] < 1.5):
                toks.add((m.group(1), s["text"].strip()))
    if not toks:
        return 0
    pat = re.compile(r"(?<![A-Za-z0-9])(" + "|".join(
        re.escape(w) + re.escape(d) for w, d in sorted(toks, key=lambda t: -len(t[0] + t[1])))
        + r")(?![0-9])")

    def fix(s):
        return pat.sub(lambda m: re.sub(r"\d+$", lambda d: d.group().translate(_SUB_FORM),
                                        m.group(1)), s) if isinstance(s, str) else s
    changed = 0
    grid = n.get("table_grid") or {}
    for row in grid.get("cells") or []:
        for k, c in enumerate(row):
            if fix(c) != c:
                row[k] = fix(c)
                changed += 1
    # The caption too (`between C₃ and C₄ Plants`): same length, so its marks stand.
    for k in ("table_text", "body", "body_md", "caption") if changed else ("caption",):
        if n.get(k):
            n[k] = fix(n[k])
    return changed


def _finalise_for_consumers(doc, cdir):
    import pymupdf
    src = doc.get("source_pdf") or ""
    src = src if os.path.isabs(src) else os.path.join(ROOT, src)
    pdf = pymupdf.open(src) if os.path.exists(src) else None
    if pdf is not None:
        import pdf_watermark
        pdf_watermark.strip(pdf)              # a re-cut photo never carries the watermark
    pages = doc.get("pages") or []
    pf_index = {p.get("page_file"): i for i, p in enumerate(pages)}
    folio_to_pf = {p.get("printed"): p.get("page_file") for p in pages
                   if p.get("printed") is not None}
    pf_to_folio = {p.get("page_file"): p.get("printed") for p in pages}
    stats = collections.Counter()

    # the figure follows the paragraph that first names it -- re-run now that the artwork and
    # its caption are one node (in `build_tree` only the caption node could move)
    _move_figures_to_first_mention(doc["tree"])

    def pf_of(b, n):
        return (b.get("page_file") or folio_to_pf.get(b.get("page"))
                or n.get("page_file"))

    # 1. every box names its page both ways; every node lists the page FILES it prints on
    for n in _walk_nodes(doc["tree"]):
        for b in (n.get("boxes") or []) + ([n["caption_box"]] if n.get("caption_box") else []):
            pf = pf_of(b, n)
            if pf:
                b["page_file"] = pf
                b["page"] = pf_to_folio.get(pf)
        for r in n.get("char_ranges") or []:
            if not r.get("page_file"):
                r["page_file"] = folio_to_pf.get(r.get("page")) or n.get("page_file")
        files = []
        for b in n.get("boxes") or []:
            if b.get("page_file") and b["page_file"] not in files:
                files.append(b["page_file"])
        if files:
            n["page_files"] = files
            n["page_file"] = files[0]
            n["pages"] = [pf_to_folio[f] for f in files if pf_to_folio.get(f) is not None]
        elif n.get("page_file"):
            n["page_files"] = [n["page_file"]]
    doc["chapter"]["page_files"] = [p["page_file"] for p in pages
                                    if p.get("belongs", "chapter") == "chapter"]

    # 2. per-node fixes that need the PDF
    if pdf is not None:
        def page_of(n):
            pf = n.get("page_file")
            return (pdf[pf_index[pf]], pf, pf_to_folio.get(pf)) if pf in pf_index else (None,) * 3

        for n in _walk_nodes(doc["tree"]):
            if n.get("kind") == "figure":
                page, pf, folio = page_of(n)
                if page is not None and _caption_under_photo(n, page, pf, folio, cdir):
                    stats["photo_captions"] += 1
            if n.get("kind") == "list" and n.get("items") and len(n.get("boxes") or []) == 1:
                page, pf, folio = page_of(n)
                if page is not None:
                    stats["list_item_marks"] += _list_marks_from_pdf(n, page)
            if n.get("kind") == "table" and n.get("table_grid") and n.get("boxes"):
                page, pf, folio = page_of(n)
                if page is not None and not n.get("cell_italics"):
                    ital = _table_italics(n, page)
                    if ital:
                        n["cell_italics"] = ital
                        stats["table_italics"] += len(ital)
                if page is not None:
                    stats["table_scripts"] += _table_scripts(n, page)
        # exercise questions sharing one box get their own
        for n in _walk_nodes(doc["tree"]):
            qs = [c for c in n.get("children") or [] if c.get("kind") == "question"
                  and c.get("boxes") and len(c["boxes"]) == 1]
            groups = collections.defaultdict(list)
            for q in qs:
                groups[json.dumps(q["boxes"][0]["bbox"])].append(q)
            for grp in groups.values():
                if len(grp) < 2:
                    continue
                page, pf, folio = page_of(grp[0])
                if page is not None and _question_boxes(grp, page, pf, folio):
                    stats["question_boxes"] += len(grp)
        pdf.close()
    # exercise questions all carrying the whole list's boxes get their own
    for n in _walk_nodes(doc["tree"]):
        qs = [c for c in n.get("children") or [] if c.get("kind") == "question"]
        stats["question_boxes_split"] += (_distribute_question_boxes(qs)
                                          or _distribute_after_continued_part(qs))

    # 2b. ONE LINK PER PICTURE. A figure the book prints as lettered panels is carried by its
    #     panels alone -- each its own crop, JSON entry, image and CDN link. The whole-figure
    #     crop beside them was a second, combined picture of the same artwork, linked from the
    #     JSON as `image` (BIO11L ch02 Figures 2.4-2.6).
    for n in _walk_nodes(doc["tree"]):
        if n.get("kind") == "figure" and len([q for q in n.get("panels") or []
                                               if q.get("image_local") or q.get("image")]) >= 2:
            for k in ("image_local", "image", "image_sha256"):
                n.pop(k, None)
            stats["panel_figures"] += 1

    # 3. tables: ONE text representation, derived from the grid the render draws
    for n in _walk_nodes(doc["tree"]):
        if n.get("kind") == "table" and (n.get("table_grid") or {}).get("cells"):
            rows = [[re.sub(r"\s+", " ", c or "").strip() for c in r]
                    for r in n["table_grid"]["cells"]]
            text = "\n".join(" | ".join(r) for r in rows)
            n["table_text"] = text
            n["body"] = text
            n["body_md"] = text
            for k in ("marks", "sentences", "terms", "line_starts", "line_geom"):
                n.pop(k, None)

    # 4. a caption's printed label is bold, in the data as on the page. A TABLE's caption is
    #    printed bold throughout (`TABLE 1.1 Organisms with their Taxonomic Categories`), which
    #    is how the exact render sets it.
    # ...unless that "title" is prose the page already prints outside the picture: A2S gave the
    # Vertebrata chart (BIO11L ch04 p047) the sentence above it, `The subphylum Vertebrata is
    # further divided as follows:`, which then printed twice in the Markdown and the page.
    def _flat(s):
        return re.sub(r"[^a-z0-9]", "", (s or "").lower())
    _prose = {(x.get("page_file"), _flat(x.get("body"))) for x in _walk_nodes(doc["tree"])
              if x.get("kind") in ("para", "box", "list") and x.get("body")}
    for n in _walk_nodes(doc["tree"]):
        art_cap = n.pop("_art_caption", None)
        if art_cap and (n.get("page_file"), _flat(art_cap)) in _prose:
            art_cap = None
        if n.get("kind") == "figure" and art_cap and not (n.get("caption") or "").strip():
            n["caption"] = art_cap
            n["caption_in_art"] = True
        cap = (n.get("caption") or "").strip()
        m = _CAPTION_LABEL.match(cap)
        if n.get("kind") == "table" and cap and n.get("table_grid"):
            n["caption_marks"] = [{"from": 0, "to": len(cap), "b": True}]
            continue
        if n.get("kind") in ("figure", "table") and m:
            cm = n.get("caption_marks") or []
            if not any(x.get("b") and x.get("from") == 0 for x in cm):
                n["caption_marks"] = [{"from": 0, "to": m.end(), "b": True}] + cm

    # 5. a list's own marks are its items' marks, at the items' offsets in the list body
    for n in _walk_nodes(doc["tree"]):
        if n.get("kind") != "list" or not n.get("items"):
            continue
        body, pos, marks = n.get("body") or "", 0, []
        for it in n["items"]:
            ib = it.get("body") or ""
            at = body.find(ib, pos) if ib else -1
            if at < 0:
                marks = None
                break
            marks += [{**m, "from": m["from"] + at, "to": m["to"] + at}
                      for m in it.get("marks") or []]
            pos = at + len(ib)
        if marks is not None and marks != (n.get("marks") or []):
            n["marks"] = sorted(marks, key=lambda m: m["from"])
            n["body_md"] = ct.to_body_md(body, n["marks"])
            stats["list_marks"] += 1

    # 6. one representation of the unit pages: `tree`, tagged `belongs: unit`
    doc.pop("unit_tree", None)

    # 7. ids/paths last, after anything moved
    _assign_paths(doc["tree"], doc["book"], doc["chapter"]["number"])
    _walk(doc["tree"], lambda n, _p: n.update(belongs=n.get("belongs") or "chapter"))

    # 8. passages and subtopics address the FINAL ids (see `structure_inputs.py`)
    _st = join_agent_structure.apply_tree_structure(
        doc, f"{doc['book_id']}-ch{doc['chapter']['number']:02d}",
        steps_dir=os.path.join(ROOT, "steps"))
    if _st:
        stats["passages"] = _st["passages"]
        stats["subtopics"] = _st["subtopics"]
    # A mark past the end of its text breaks every consumer that slices by offset. It is a bug
    # upstream, so it is counted and reported -- never silently kept.
    for n in _walk_nodes(doc["tree"]):
        for k in ("marks", "caption_marks"):
            body = n.get("body" if k == "marks" else "caption") or ""
            if n.get(k):
                ok = [m for m in n[k] if 0 <= m.get("from", 0) < m.get("to", 0) <= len(body)]
                if len(ok) != len(n[k]):
                    stats["bad_marks_dropped"] += len(n[k]) - len(ok)
                    print(f"  WARNING   {len(n[k]) - len(ok)} mark(s) outside the text of "
                          f"{n.get('kind')} {n.get('number') or ''} {body[:40]!r}")
                    n[k] = ok
    doc["consumer_finalise"] = dict(stats)
    return stats


def slugify(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", (s or "").strip().lower()).strip("-")
    return s or "chapter"


def _drop_equation_twins(doc):
    """A text-layer scrap inside an equation A2S transcribed is that equation, printed again.

    MathType equations reach the text layer as scattered pieces -- `-3` and `2.51 cm` beside
    `Density = 4.237g/2.51 cm^3`, `m = 0 − m 2 1/2 .` and `1 v` under exercise 1.13 (PHY11L
    ch01) -- and each piece the text join could not pair stayed a paragraph of its own, drawn
    over the typeset equation and listed as prose in the JSON and the Markdown. A short
    text-layer paragraph lying mostly inside (or within a line of) a transcribed equation's box
    is dropped. Physics only: its display maths is all transcribed (A2S)."""
    if doc.get("subject") != "physics":
        return 0
    eq = {}

    def boxes(n):
        return [(b.get("page_file"), b["bbox"]) for b in n.get("boxes") or [] if b.get("bbox")]

    def walk(ns):
        for n in ns or []:
            if n.get("latex"):
                for pf, bb in boxes(n):
                    eq.setdefault(pf, []).append(bb)
            walk(n.get("children"))
    walk(doc["tree"])

    def inside(pf, bb):
        a = max((bb[2] - bb[0]) * (bb[3] - bb[1]), 1e-9)
        g = 0.012                                      # about a line of slack
        for e in eq.get(pf, []):
            ix = min(bb[2], e[2] + g) - max(bb[0], e[0] - g)
            iy = min(bb[3], e[3] + g) - max(bb[1], e[1] - g)
            if ix > 0 and iy > 0 and ix * iy >= 0.5 * a:
                return True
        return False
    dropped = [0]

    def prune(ns):
        keep = []
        for n in ns:
            body = (n.get("body") or "").strip()
            if (n.get("kind") == "para" and n.get("source") == "text_layer" and not n.get("latex")
                    and len(body) < 60 and not n.get("children") and boxes(n)
                    and all(inside(pf, bb) for pf, bb in boxes(n))):
                dropped[0] += 1
                continue
            if n.get("children"):
                n["children"] = prune(n["children"])
            keep.append(n)
        return keep
    doc["tree"] = prune(doc["tree"])
    return dropped[0]


def _attach_drawn_figures(doc, cdir, cid):
    """A figure we drew ourselves (step FIGP) replaces its crop in what the reader sees.

    The agent writes a spec, code checks it against the PDF's own vector drawing and draws it
    (`chapter_steps.py check FIGP` -> steps/FIGP/drawn/<item>.svg). Only a drawing whose check
    PASSED is attached: `image_drawn` is the SVG (a CDN link after publishing), and the JSON keeps
    the crop beside it (`image_local`/`image`) and the checked spec (`image_drawn_spec`). The
    exact HTML and the Markdown show the drawing; a figure without a passing drawing keeps its
    crop. Same field names as the PHY11L-ch01 build shared by the team (2026-10-28)."""
    import shutil
    figures = []

    def rec(ns):
        for x in ns or []:
            if x.get("kind") == "figure":
                figures.append(x)
            rec(x.get("children"))
    rec(doc["tree"])
    for n in figures:
        if not n.get("image_local"):
            continue
        item = f"{cid}-{os.path.splitext(os.path.basename(n['image_local']))[0]}"
        st_path = os.path.join(ROOT, "steps", "FIGP", "status", f"{item}.json")
        if not os.path.exists(st_path):
            continue
        with open(st_path, encoding="utf-8") as fh:
            st = json.load(fh)
        svg = st.get("svg")
        if st.get("status") != "pass" or not svg or not os.path.exists(os.path.join(ROOT, svg)):
            continue
        name = f"{item}.svg"
        shutil.copyfile(os.path.join(ROOT, svg), os.path.join(cdir, "figures", name))
        n["image_drawn"] = f"figures/{name}"
        n["image_drawn_spec"] = f"steps/FIGP/out/{item}.{st.get('run') or 'runA'}.json"
        n["image_drawn_layout"] = st.get("layout")


def write_chapter(book_id, chapter_num, use_agent=True, lang="EN"):
    """Build one chapter and write chapter.json, chapter.md and figures/ into its folder."""
    doc, layout = build(book_id, chapter_num, use_agent=use_agent, lang=lang)
    # A CROP THAT CONTAINS THE PAGE'S OWN TEXT IS NOT A FIGURE.
    #
    # The Ernst Mayr page is a photograph with the biography set beside it. The extractor cut
    # a single block spanning the full page width from y 0.383 to the foot -- 61.7% of the
    # sheet -- which contains the portrait, the caption AND every word of the biography. The
    # renderer then drew that crop AND the live text it had already extracted, so the page
    # showed the same biography twice: once as selectable text, once baked into pixels
    # underneath it.
    #
    # A real figure does not contain the running prose around it. So a crop that covers two or
    # more of its own page's text nodes is a scan of a page REGION, not artwork, and is
    # dropped -- the text is already in the tree, which is where it belongs and where it can
    # be searched, marked up and translated.
    def _drop_page_region_crops(doc_tree, pages_list):
        text_boxes = {}
        for nn in _iter_nodes(doc_tree):
            if nn.get("kind") in ("para", "list", "section", "question", "box"):
                for bb in nn.get("boxes") or []:
                    if bb.get("bbox"):
                        text_boxes.setdefault(bb.get("page_file"), []).append(bb["bbox"])

        def covers(fig_bb, t):
            return (fig_bb[0] <= t[0] + 0.02 and fig_bb[2] >= t[2] - 0.02
                    and fig_bb[1] <= t[1] + 0.02 and fig_bb[3] >= t[3] - 0.02)

        dropped = []

        def prune(nodes):
            keep = []
            for nn in nodes:
                if nn.get("children"):
                    nn["children"] = prune(nn["children"])
                if nn.get("kind") == "figure":
                    bb0 = (nn.get("boxes") or [{}])[0]
                    bb = bb0.get("bbox")
                    pf_ = bb0.get("page_file") or nn.get("page_file")
                    if bb and len(bb) == 4:
                        inside = sum(1 for t in text_boxes.get(pf_, []) if covers(bb, t))
                        # A FULL-BLEED CROP ON A PAGE THAT ALSO SETS TEXT is a scan of the
                        # page, not a figure. On the Ernst Mayr page the embedded image is a
                        # picture of the whole page -- portrait, biography, caption, imprint
                        # and all -- sitting below the same biography rendered as live text,
                        # so the page showed its own content twice. Opener artwork IS
                        # full-bleed and is drawn from the page record's `art`, never from a
                        # figure node, so excluding it here costs nothing.
                        full_bleed = (bb[0] <= 0.02 and bb[2] >= 0.98
                                      and (bb[3] - bb[1]) >= 0.40)
                        if inside >= 2 or (full_bleed and text_boxes.get(pf_)):
                            dropped.append((pf_, round(
                                (bb[2] - bb[0]) * (bb[3] - bb[1]), 3), inside))
                            continue
                keep.append(nn)
            return keep

        out_tree = prune(doc_tree)
        return out_tree, dropped

    def _iter_nodes(ns):
        for nn in ns:
            yield nn
            if nn.get("children"):
                yield from _iter_nodes(nn["children"])

    doc["tree"], _dropped_crops = _drop_page_region_crops(doc["tree"], doc.get("pages") or [])
    if _dropped_crops:
        doc["dropped_page_region_crops"] = [
            {"page_file": a, "area": b, "text_nodes_covered": c}
            for a, b, c in _dropped_crops]

    # PDF LINE WRAPPING IS NOT PART OF THE TEXT.
    #
    # A2's text keeps newlines, and that is deliberate -- the Exercises block needs them to be
    # split into questions, and collapsing them once destroyed ten exercises into one run-on
    # paragraph. But once the questions ARE split, the newlines left inside ordinary prose are
    # just where the BOOK's column happened to wrap, and they are not content: 16 of 28
    # paragraphs in Class 11 ch01 carried them into `body`, `body_md` and the Markdown, where
    # they are wrong in every renderer and wrong for anyone diffing or translating the text.
    #
    # Sentence offsets are recomputed afterwards, because they index into this string.
    def _unwrap(nn, _p):
        if nn.get("kind") not in ("para", "box", "question", "summary", "list"):
            return

        def rewrap(text, marks):
            """Collapse the wrap AND carry every mark with it.

            `re.sub` shortens the string, so a mark recorded at character 412 of the wrapped
            text points somewhere else entirely in the unwrapped one. Rewriting the body
            without moving the marks is what produced `example <i>of Mangifera ind</i>ica` --
            the italic three characters early, eating the wrong words. `body_md` is derived
            from (body, marks), so a stale offset corrupts the Markdown too.

            Every edit is applied as a (position, delta) so the offsets move with the text
            instead of being recomputed from a string that no longer exists.
            """
            if not text or "\n" not in text:
                return text, marks
            shifts, out, pos = [], [], 0
            for m in re.finditer(r"[ \t]*\n[ \t]*", text):
                out.append(text[pos:m.start()])
                out.append(" ")
                shifts.append((m.start(), (m.end() - m.start()) - 1))
                pos = m.end()
            out.append(text[pos:])
            new_text = "".join(out)

            def move(i):
                for at, delta in shifts:
                    if i > at:
                        i -= delta
                return max(0, min(i, len(new_text)))

            new_marks = []
            for m in marks or []:
                f, t_ = move(m["from"]), move(m["to"])
                if t_ > f:
                    new_marks.append({**m, "from": f, "to": t_})
            return new_text.strip(), new_marks

        body, marks = rewrap(nn.get("body"), nn.get("marks") or [])
        if body is not None and body != nn.get("body"):
            nn["body"] = body
            nn["marks"] = marks
            nn["body_md"] = ct.to_body_md(body, marks)
            nn["sentences"] = ct.split_sentences(body)
        for it in nn.get("items") or []:
            ib, im = rewrap(it.get("body"), it.get("marks") or [])
            if ib is not None and ib != it.get("body"):
                it["body"] = ib
                it["marks"] = im
                it["body_md"] = ct.to_body_md(ib, im)

    _walk(doc["tree"], _unwrap)


    # LAST WORD ON PROVENANCE. The question-split pass runs after the tree is assembled, so
    # its 5 question nodes reached the file with no `belongs` at all. Re-tagging here, after
    # every pass that can create a node, is the only place that cannot be out-stepped.
    subject, klass, edition = design_lib.parse_book_id(book_id)
    cdir = os.path.join(ROOT, "data", f"{EDITION_WORD[edition]}_ncert", f"class_{klass}",
                        SUBJECT_WORD[subject],
                        f"ch{chapter_num:02d}_{slugify(doc['chapter']['title'])}")
    os.makedirs(cdir, exist_ok=True)

    # Crops are cut from the SAME layout the tree was built from, so a node's `figure_file`
    # and the file on disk cannot disagree.
    n_figs = len(cut_figures.cut(layout["source_pdf"], layout,
                                 os.path.join(cdir, "figures")))
    # re-walk the tree and attach the crop filenames the cutter just assigned
    by_box, el_by_box = {}, {}
    for p in layout["pages"]:
        for e in p["elements_in_reading_order"]:
            if e.get("figure_file"):
                key = tuple(round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"]))
                by_box[key] = e["figure_file"]
                el_by_box[key] = e

    def attach(n, _parents):
        if n["kind"] in ("figure", "table") and not n.get("image_local"):
            for b in n.get("boxes") or []:
                f = by_box.get(tuple(b["bbox"]))
                if f:
                    n["image_local"] = f"figures/{f}"
                    # The crop's own rect on the sheet (`cut_figures`), by the element's own
                    # pt -> sheet mapping: the render places the picture there, not in the box.
                    e = el_by_box[tuple(b["bbox"])]
                    cp, bp, bs = e.get("crop_bbox_pt"), e.get("bbox_pt"), e.get("bbox_sheet")
                    if cp and bp and bs and bp[2] > bp[0] and bp[3] > bp[1]:
                        sx = (bs[2] - bs[0]) / (bp[2] - bp[0])
                        sy = (bs[3] - bs[1]) / (bp[3] - bp[1])
                        n["image_bbox"] = [round(bs[0] + (cp[0] - bp[0]) * sx, 4),
                                           round(bs[1] + (cp[1] - bp[1]) * sy, 4),
                                           round(bs[2] + (cp[2] - bp[2]) * sx, 4),
                                           round(bs[3] + (cp[3] - bp[3]) * sy, 4)]
                    # The figure's lettered panels, each its own crop (see `cut_figures`): the
                    # node stays ONE figure under one caption, and carries its pictures.
                    panels = [{"label": q["label"],
                               "bbox": [round(v, 4) for v in q["bbox_sheet"]],
                               "image_local": f"figures/{q['figure_file']}"}
                              for q in el_by_box[tuple(b["bbox"])].get("panels") or []
                              if q.get("figure_file") and q.get("bbox_sheet")]
                    if len(panels) >= 2:
                        n["panels"] = panels
                    break
    _walk(doc["tree"], attach)
    # ONLY NOW can artwork and caption be merged: `image_local` is attached by the loop above,
    # and the merge needs to know which node has the picture. Running it inside build_tree --
    # where it was first put -- saw no images at all, so `artwork` was empty and every caption
    # stayed a node of its own with the drawing somewhere else.
    # THE PAGE'S ARTWORK IS ATTACHED HERE, NOT IN `build()`. `cut_figures` runs after the tree
    # is constructed, so at the time `doc["pages"]` was assembled no element carried a
    # `furniture_file` yet and every page recorded `art: null` -- the same ordering mistake that
    # left figure captions detached from their pictures. Anything that depends on a crop
    # existing has to run after the crops are cut.
    _by_file = {}
    for _p in layout["pages"]:
        _arts = [{"kind": e.get("furniture"),
                  "z": e.get("z"),
                  "file": f"figures/{e['furniture_file']}",
                  "bbox": [round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"])]}
                 for e in _p["elements_in_reading_order"]
                 if e["role"] == "page_furniture" and e.get("furniture_file")
                 and e.get("furniture") in ("page ground", "header art", "qr code", "ornament")]
        if _arts:
            _by_file[_p["page_file"]] = _arts
    for _pg in doc["pages"]:
        if _by_file.get(_pg["page_file"]):
            _pg["art"] = _by_file[_pg["page_file"]]
        # A one-line contents entry (`6.5 Biological Evolution`) has no turnover to measure
        # its title's x from; it hangs at its rail's indent, measured on a sibling at its x.
        _rail = _pg.get("contents_rail") or []
        _ind = [r["indent_pt"] for r in _rail if r.get("indent_pt")]
        for r in _rail:
            if not r.get("indent_pt") and _ind and any(
                    abs(s["bbox"][0] - r["bbox"][0]) < 0.004 for s in _rail if s.get("indent_pt")):
                r["indent_pt"] = max(set(_ind), key=_ind.count)
    _opener_figures_to_art(doc, layout)
    _attach_drawn_figures(doc, cdir, f"{book_id}-ch{chapter_num:02d}")
    doc.setdefault("text_join", {})["equation_scraps_dropped"] = _drop_equation_twins(doc)

    _split_exercise_questions(doc["tree"], doc["book"], doc["chapter"]["number"])
    _walk(doc["tree"], _drop_item_lines)
    # EVERYTHING THAT READS A QUESTION NODE MUST RUN AFTER THE PASS THAT CREATES ONE.
    # Both of these were placed earlier in the function and silently did nothing: the
    # `belongs` tag left five questions untagged, and the sub-part split saw zero questions
    # to split. Neither failed loudly, because walking a tree that does not yet contain the
    # nodes you are looking for is not an error -- it is just a no-op.
    _walk(doc["tree"], lambda n, _p: n.update(belongs=n.get("belongs") or "chapter"))
    _walk(doc["tree"], _split_parts)
    _walk(doc["tree"], _mark_inline_parts)
    _walk(doc["tree"], _match_columns)
    _merge_split_captions(doc["tree"])
    _walk(doc["tree"], _fix_numbered_list)
    _walk(doc["tree"], _clean_text)
    _merge_figure_captions(doc["tree"])
    _drop_shadow_figures(doc)
    _drop_layer_duplicates(doc)
    _table_own_text(doc)
    _nest_unnumbered_subheads(doc["tree"])
    _stack_bullet_boxes(doc["tree"])
    _absorb_caption_tails(doc["tree"])
    _squeeze_caption_spaces(doc["tree"])
    _order_lettered_siblings(doc["tree"])
    _title_unnumbered_sections(doc["tree"])
    _split_label_lines(doc["tree"])
    _drop_furniture_figures(doc)
    _running_head_titles(doc)
    _drop_decor_inside_figures(doc)
    _borrow_furniture_decor(doc)
    _absorb_table_cells(doc["tree"])
    _inherit_table_fill(doc["tree"])
    _apply_line_geom(doc["tree"])
    _apply_line_geom(doc.get("unit_tree") or [])
    _assign_paths(doc["tree"], doc["book"], doc["chapter"]["number"])

    # VECTOR ARTWORK, CROPPED BEFORE ANYTHING IS WRITTEN.
    # `cut_figures` can only crop embedded image blocks, so every diagram NCERT draws as
    # vector paths -- which is most of its flowcharts and labelled cross-sections -- reached
    # this point with a caption and no artwork. Running the crop afterwards as a separate
    # command left chapter.md and chapter.html stale: the JSON gained `image_local` and the
    # two files a reader actually opens still showed no figure at all.
    try:
        import crop_vector_figures
        made, _err = crop_vector_figures.crop_chapter(cdir, doc)
        if made:
            print(f"  vectors   {made} vector figure(s) cropped from measured boxes")
            # THE THIRD TIME THIS EXACT BUG HAS APPEARED: a pass that CREATES nodes running
            # after the pass that gives nodes their identity. These figure nodes are built
            # from A2L's measurements, so they arrive after `_assign_paths` has already
            # walked the tree -- and a node with no `path` has no sort key, so the DynamoDB
            # export dies on `KeyError: 'path'`. Re-assigning is cheap and idempotent.
            _assign_paths(doc["tree"], doc["book"], doc["chapter"]["number"])
            _walk(doc["tree"],
                  lambda n, _p: n.update(belongs=n.get("belongs") or "chapter"))
    except Exception as exc:                                  # noqa: BLE001
        print(f"  vectors   SKIPPED ({type(exc).__name__}: {exc})")
    # Again here: the CAPTIONED copy of a picture can be made only now, by `crop_vector_figures`
    # (the Unit 2 portrait of Katherine Esau, BIO11L ch05 p002), after the first pass ran.
    _drop_shadow_figures(doc)
    _late_opener_art(doc)

    # Last, after every pass that creates or moves a node: the JSON a consumer stores must be
    # complete on its own (see `_finalise_for_consumers`).
    _fin = _finalise_for_consumers(doc, cdir)
    if _fin:
        print(f"  final     {dict(_fin)}")

    # A REBUILD MUST NOT DESTROY THE CDN URLS.
    #
    # `upload_assets.py` writes the live URL onto each figure node and each page-art entry of
    # chapter.json. A rebuild regenerates those nodes from the PDF, so every URL vanished --
    # 98 of them on Class 12 ch01, silently, in a run whose output said nothing was wrong.
    # The assets are still on the CDN; only the pointers were lost, and re-uploading identical
    # bytes to get them back is pure waste.
    #
    # So the URLs are carried forward by the SHA of the file they point at: if the crop on
    # disk is byte-identical to the one that was uploaded, its URL is still correct. A crop
    # whose bytes changed keeps no URL and will be re-uploaded, which is right.
    _prev_path = os.path.join(cdir, "chapter.json")
    if os.path.exists(_prev_path):
        try:
            with open(_prev_path, encoding="utf-8") as fh:
                _prev = json.load(fh)
        except Exception:                                     # noqa: BLE001
            _prev = None
        if _prev:
            _by_local = {}
            for _n in _walk_nodes(_prev.get("tree") or []):
                if _n.get("image_local") and _n.get("image"):
                    _by_local[_n["image_local"]] = (_n["image"], _n.get("image_sha256"))
            _art_by_file = {a["file"]: a for pg in (_prev.get("pages") or [])
                            for a in (pg.get("art") or []) if a.get("url") and a.get("file")}

            def _sha_of(rel):
                fp = os.path.join(cdir, rel or "")
                if not os.path.exists(fp):
                    return None
                h = hashlib.sha256()
                with open(fp, "rb") as fh2:
                    for chunk in iter(lambda: fh2.read(1 << 16), b""):
                        h.update(chunk)
                return h.hexdigest()

            _kept = 0
            for _n in _walk_nodes(doc["tree"]):
                hit = _by_local.get(_n.get("image_local"))
                if hit and hit[1] and hit[1] == _sha_of(_n.get("image_local")):
                    _n["image"], _n["image_sha256"] = hit
                    _kept += 1
            for _pg in doc.get("pages") or []:
                for _a in (_pg.get("art") or []):
                    old = _art_by_file.get(_a.get("file"))
                    if old and old.get("sha256") and old["sha256"] == _sha_of(_a.get("file")):
                        _a["url"], _a["sha256"] = old["url"], old["sha256"]
                        _kept += 1
            if _kept:
                print(f"  cdn       {_kept} url(s) carried forward from the previous build")

    with open(os.path.join(cdir, "chapter.json"), "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False)
    with open(os.path.join(cdir, "chapter.md"), "w", encoding="utf-8") as fh:
        fh.write(to_markdown(doc))
    return cdir, doc, n_figs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("--no-agent-text", action="store_true")
    ap.add_argument("--lang", default="EN")
    a = ap.parse_args()
    m = re.fullmatch(r"([A-Z]{3}\d{2}[LO])-ch(\d+)", a.chapter)
    if not m:
        raise SystemExit("chapter must look like BIO11L-ch01")
    book, num = m.group(1), int(m.group(2))
    cdir, doc, n_figs = write_chapter(book, num, use_agent=not a.no_agent_text, lang=a.lang)
    n = [0]

    def count(x, _p):
        n[0] += 1
    _walk(doc["tree"], count)
    print(f"{a.chapter}: {n[0]} nodes, {len(doc['pages'])} pages, {n_figs} figures, "
          f"reprint={doc['reprint']}, title={doc['chapter']['title']!r}")
    print(f"   -> {os.path.relpath(cdir, ROOT)}")
    if doc["text_join"]:
        s = doc["text_join"]
        print(f"   agent text: {s['pages_with_agent']}/{s['pages']} pages, "
              f"{s['blocks_replaced']} blocks replaced, {s['blocks_kept_pdf']} kept from layer")


if __name__ == "__main__":
    main()
