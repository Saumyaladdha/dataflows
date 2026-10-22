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
import hashlib
import json
import os
import re
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
    first_chapter_page = 0
    for i, p in enumerate(layout["pages"]):
        titles = [e["text"] for e in p["elements_in_reading_order"]
                  if e["role"] == "chapter_title"]
        if any(re.match(r"^\s*chapter\s+\d+", t, re.I) for t in titles):
            first_chapter_page = i
            break
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


def collect_blocks(pages):
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
        elements = sorted(p["elements_in_reading_order"],
                          key=lambda e: ((e.get("bbox_sheet") or e["bbox"])[1],
                                         (e.get("bbox_sheet") or e["bbox"])[0]))
        for e in elements:
            if e["role"] in ct._FURNITURE:
                continue
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
        if (prev and b["continues_from_previous"]
                and prev["el"]["role"] == b["el"]["role"] == "paragraph"):
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
            return
        head = dict(run[0])
        head["items"] = [{"text": r["el"].get("text", ""),
                          "runs": r["el"].get("runs") or []} for r in run]
        head["extra_boxes"] = head.get("extra_boxes", []) + [
            {"page": r["page"], "bbox": r["el"].get("bbox_sheet") or r["el"]["bbox"]}
            for r in run[1:]]
        out.append(head)
        run.clear()

    for b in blocks:
        if b["el"]["role"] == "list":
            run.append(b)
            continue
        flush()
        out.append(b)
    flush()
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

    if kind in ("figure", "table"):
        caption = (el.get("text") or "").strip()
        m = (_FIG_NUM if kind == "figure" else _TAB_NUM).match(caption)
        if m:
            node["number"] = m.group(1)
        node["caption"] = caption
        if el.get("figure_file"):
            node["image_local"] = f"figures/{el['figure_file']}"
        if el.get("table_text"):
            node["table_text"] = el["table_text"]
        if el.get("table_grid"):
            node["table_grid"] = el["table_grid"]
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
        for it in block["items"]:
            body, marks = ct.runs_to_body_marks(it["runs"]) if it["runs"] else (it["text"], [])
            node["items"].append({"body": body, "marks": marks,
                                  "body_md": ct.to_body_md(body, marks)})
        node["body"] = " ".join(i["body"] for i in node["items"])
    else:
        body, marks = ct.runs_to_body_marks(el.get("runs") or [])
        if not body:
            body = (el.get("text") or "").strip()
        node["body"] = body
        if marks:
            node["marks"] = marks
        node["body_md"] = ct.to_body_md(body, marks)
        node["sentences"] = ct.split_sentences(body)
        terms = ct.terms_in(body, marks)
        if terms:
            node["terms"] = terms

    node["id"] = ct.stable_id(kind, book_base, chapter_num, path)
    node["source"] = "page_image" if block.get("source") == "a2-agent" else "text_layer"
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
    # A3 groups blocks into passages by the number A2 gave them, so the number has to survive
    # into the tree or the passage join has nothing to match on.
    if el.get("a2_block_n") is not None:
        node["a2_block_n"] = el["a2_block_n"]
    return node


def build_tree(blocks, book_base, chapter_num):
    """Nest the flat block list under its numbered headings."""
    root = []
    # stack[d] = the children list to append to at heading depth d
    stack = {0: root}
    sections = {}          # depth -> the open section node

    pending_figures = []

    for b in blocks:
        el = b["el"]
        if el["role"] == "section_heading":
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
                node["source"] = "page_image" if b.get("source") == "a2-agent" else "text_layer"
                node["qa"] = "auto"
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
                for it in n["items"]:
                    t = (it.get("body") or "").strip()
                    m = re.match(r"^(\d{1,2})\s*[.)]\s+(.*)$", t, re.S)
                    if m and (last is None or int(m.group(1)) == int(last["number"]) + 1):
                        last = {"kind": "question", "number": m.group(1),
                                "body": m.group(2).strip(), "body_md": m.group(2).strip(),
                                "marks": it.get("marks") or [],
                                "sentences": ct.split_sentences(m.group(2).strip()),
                                "parts": [],
                                "pages": n.get("pages"), "boxes": n.get("boxes"),
                                "page_file": n.get("page_file"),
                                "id": ct.stable_id("question", book_base, chapter_num,
                                                   f"{n.get('path','x')}.{m.group(1)}"),
                                "belongs": n.get("belongs"),
                                "source": n.get("source"), "qa": n.get("qa", "auto")}
                        made.append(last)
                    elif last is not None and t:
                        last["parts"].append({"body": t, "marks": it.get("marks") or []})
                    elif t:
                        made.append({**n, "kind": "para", "items": None, "body": t})
                if sum(1 for x in made if x.get("kind") == "question") >= 2:
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
            if len(parts) < 5 or [int(parts[i]) for i in range(1, len(parts) - 1, 2)] \
                    != list(range(1, (len(parts) - 1) // 2 + 1)):
                scan, pos, want_n = [], 0, 1
                while True:
                    m = re.compile(r"(?<![\d.])" + str(want_n) + r"\.\s+").search(body, pos)
                    if not m:
                        break
                    scan.append((want_n, m.start(), m.end()))
                    pos, want_n = m.end(), want_n + 1
                if len(scan) >= 3:
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
                            "source": n.get("source"), "qa": n.get("qa", "auto")})
                _q_seen[0] = int(num)
        nodes[:] = out

    rec(root, ())


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
            a_y = (art_node.get("boxes") or [{}])[0].get("bbox", [0, 0, 0, 0])[1]
            c_y = (cap_node.get("boxes") or [{}])[0].get("bbox", [0, 0, 0, 0])[1]
            gap = abs(c_y - a_y)
            if best_gap is None or gap < best_gap:
                best, best_gap, best_parents = art_node, gap, art_parents
        if best is None:
            continue
        used.add(id(best))
        best["caption"] = cap_node["caption"]
        if cap_node.get("number"):
            best["number"] = cap_node["number"]
        best["boxes"] = (best.get("boxes") or []) + (cap_node.get("boxes") or [])
        best["pages"] = sorted({b["page"] for b in best["boxes"] if b.get("page")})
        owner = cap_parents[-1]["children"] if cap_parents else root
        if cap_node in owner:
            owner.remove(cap_node)


def _move_figures_to_first_mention(root):
    """A figure sits after the paragraph that first names it, not where it is printed.

    Figure 1.1 is printed beside the end of 1.2.6 but belongs to 1.2.7 -- the section that
    discusses it. The printed position is untouched; only the reading order moves.
    """
    figures = {}

    def collect(n, parents):
        if n.get("kind") in ("figure", "table") and n.get("number"):
            figures[n["number"]] = (n, parents)
    _walk(root, collect)
    if not figures:
        return

    mentions = {}

    def find(n, parents):
        if n.get("kind") != "para":
            return
        for rx in (_FIG_REF, _TAB_REF):
            for num in rx.findall(n.get("body", "")):
                mentions.setdefault(num, (n, parents))
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
    for e in chapter_pages[0]["elements_in_reading_order"]:
        if e["role"] not in ("side_note", "contents_entry"):
            continue
        key = re.sub(r"[^a-z0-9]", "", (e.get("text") or "").lower())
        if key and key in headings:
            e["role"] = "contents_entry"      # in ct._FURNITURE -> never a node


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
    if use_agent:
        steps = os.path.join(ROOT, "steps")
        join_stats = join_agent_text.apply_agent_text(layout, chapter, steps_dir=steps)
        # The layout join runs AFTER the text join, because it matches numbered elements on
        # `a2_block_n` -- which the text join is what writes.
        layout_stats = join_agent_layout.apply_agent_layout(layout, chapter, steps_dir=steps)
        # A2S last: it needs `a2_block_n`, which the text join writes, and it overrides the
        # geometry-derived table grid with the agent's transcription where one exists.
        special_stats = join_agent_special.apply_agent_special(layout, chapter, steps_dir=steps)

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
    blocks = collapse_lists(stitch_across_pages(collect_blocks(chapter_pages)))
    tree = build_tree(blocks, book_base, chapter_num)

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
            "footer": p.get("imprint"),
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
            "contents_rail": [
                {"text": e.get("text", ""),
                 "bbox": [round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"])]}
                for e in p["elements_in_reading_order"]
                if e["role"] == "contents_entry"] or None,
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
                     "file": f"figures/{e['furniture_file']}",
                     "bbox": [round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"])]}
                    for e in p["elements_in_reading_order"]
                    if e["role"] == "page_furniture" and e.get("furniture_file")
                    and e.get("furniture") in ("header art", "qr code")
                    and _is_furniture_sized(e, p)] or None,
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
                     "file": f"figures/{e['furniture_file']}",
                     "bbox": [round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"])]}
                    for e in p["elements_in_reading_order"]
                    if e["role"] == "page_furniture" and e.get("furniture_file")
                    and e.get("furniture") in ("header art", "qr code")
                    and _is_furniture_sized(e, p)] or None,
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
    parts = []
    for i in range(1, len(bits) - 1, 2):
        txt = (bits[i + 1] or "").strip()
        if txt:
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
                    joiner = "" if prev_cap.endswith("-") else " "
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
    """
    for key in ("body", "body_md", "caption", "title"):
        t = nn.get(key)
        if not isinstance(t, str) or not t:
            continue
        t = _despace(t)
        t = t.replace("\u2070C", "\u00b0C").replace("\u2070 C", "\u00b0C")
        t = re.sub(r"(?<=[a-z]{2})\.(?=[A-Z][a-z])", ". ", t)
        if t != nn[key]:
            nn[key] = t
    for it in nn.get("items") or []:
        for key in ("body", "body_md"):
            t = it.get(key)
            if isinstance(t, str) and t:
                t = _despace(t)
                t = t.replace("\u2070C", "\u00b0C")
                t = re.sub(r"(?<=[a-z]{2})\.(?=[A-Z][a-z])", ". ", t)
                it[key] = t


def to_markdown(doc):
    """The chapter as CommonMark -- any renderer shows it correctly.

    Built from `body_md`, which already carries the bold and italic as `**`/`*`, so the
    Markdown needs no formatting logic of its own and cannot drift from the JSON.
    """
    ch = doc["chapter"]
    out = [f"# {ch['title']} ", "",
           f"*{doc['subject'].title()} · Class {doc['grade']} · "
           f"{'new' if doc['edition']=='latest' else 'old'} NCERT · chapter {ch['number']} · "
           f"reprint {_imprint(doc.get('reprint'))}*", ""]
    if ch.get("pages"):
        out.append(f"*Printed pages {ch['pages'][0]}–{ch['pages'][1]}*")
        out.append("")

    def rec(nodes, depth):
        for n in nodes:
            k = n["kind"]
            if k in ("section", "summary", "exercises"):
                head = " ".join(x for x in (n.get("number"), n.get("title")) if x)
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
                        out.append(f"**{cap}**")
                        out.append("")
                    width = max(len(r) for r in rows)
                    rows = [r + [""] * (width - len(r)) for r in rows]
                    out.append("| " + " | ".join(rows[0]) + " |")
                    out.append("|" + "|".join([" --- "] * width) + "|")
                    for r in rows[1:]:
                        out.append("| " + " | ".join(r) + " |")
                    out.append("")
            elif k in ("figure", "table"):
                src = n.get("image") or n.get("image_local")
                cap = (n.get("caption") or "").strip()
                if src:
                    out.append(f"![{cap}]({src})")
                    out.append("")
                if cap:
                    out.append(f"*{cap}*")
                    out.append("")
            elif k == "question":
                # THE NUMBER IS PART OF THE QUESTION, in Markdown as much as in HTML.
                # Ten exercises came out as ten anonymous paragraphs, which no question bank
                # can cite and no reader can match to the book.
                num = (n.get("number") or "").strip()
                body = n.get("body_md") or n.get("body", "")
                out.append(f"{num}. {body}" if num else body)
                # Sub-parts on their own lines, indented under the question: the (a)(b)(c)
                # options and the (i)-(v) terms are alternatives to compare, and run together
                # on one line they stop being that.
                for sub in n.get("parts") or []:
                    out.append(f"   {sub.get('body_md') or sub.get('body', '')}")
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
            else:
                out.append(n.get("body_md") or n.get("body", ""))
                out.append("")
    rec(doc["tree"], 0)
    return "\n".join(out).rstrip() + "\n"


def slugify(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", (s or "").strip().lower()).strip("-")
    return s or "chapter"


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
    by_box = {}
    for p in layout["pages"]:
        for e in p["elements_in_reading_order"]:
            if e.get("figure_file"):
                by_box[tuple(round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"]))] = \
                    e["figure_file"]

    def attach(n, _parents):
        if n["kind"] in ("figure", "table") and not n.get("image_local"):
            for b in n.get("boxes") or []:
                f = by_box.get(tuple(b["bbox"]))
                if f:
                    n["image_local"] = f"figures/{f}"
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
                  "file": f"figures/{e['furniture_file']}",
                  "bbox": [round(v, 4) for v in (e.get("bbox_sheet") or e["bbox"])]}
                 for e in _p["elements_in_reading_order"]
                 if e["role"] == "page_furniture" and e.get("furniture_file")
                 and e.get("furniture") in ("header art", "qr code")]
        if _arts:
            _by_file[_p["page_file"]] = _arts
    for _pg in doc["pages"]:
        if _by_file.get(_pg["page_file"]):
            _pg["art"] = _by_file[_pg["page_file"]]

    _split_exercise_questions(doc["tree"], doc["book"], doc["chapter"]["number"])
    # EVERYTHING THAT READS A QUESTION NODE MUST RUN AFTER THE PASS THAT CREATES ONE.
    # Both of these were placed earlier in the function and silently did nothing: the
    # `belongs` tag left five questions untagged, and the sub-part split saw zero questions
    # to split. Neither failed loudly, because walking a tree that does not yet contain the
    # nodes you are looking for is not an error -- it is just a no-op.
    _walk(doc["tree"], lambda n, _p: n.update(belongs=n.get("belongs") or "chapter"))
    _walk(doc["tree"], _split_parts)
    _merge_split_captions(doc["tree"])
    _walk(doc["tree"], _fix_numbered_list)
    _walk(doc["tree"], _clean_text)
    _merge_figure_captions(doc["tree"])
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
