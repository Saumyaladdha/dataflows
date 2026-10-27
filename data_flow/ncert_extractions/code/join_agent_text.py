#!/usr/bin/env python3
"""Put the A2 AGENT's page text onto the PDF's measured layout.

    from join_agent_text import apply_agent_text
    stats = apply_agent_text(layout, "BIO11L-ch03")

WHY THIS EXISTS -- THE DIVISION OF LABOUR, MEASURED
----------------------------------------------------
Two sources describe the same page and each is authoritative about different things.

`extract_page_layout.py` reads the PDF's text layer. For GEOMETRY it is exact and an agent
cannot compete: the bbox of every block to a tenth of a point, the font name, the colour, the
type size, the printed line pitch, which side of the spread the page is. For RUNNING PROSE it
is also excellent -- compared block for block against the agent's own reads on 23 pages of
BIO11L ch01 and ch03, the agent found zero words the text layer had missed.

But for NOTATION it is quietly wrong, and that is the whole problem:

    'C6H12O6 (Glucose)'    the subscripts of C(6)H(12)O(6) flattened to inline digits
    '(CH )'                the subscript digits dropped from the string ENTIRELY
    'CH OH'                the same
    'OCH2' 'HOCH2' 'HO'    a structural formula shattered into unordered fragments

and across the whole of BIO11L ch09 -- Biomolecules, a chapter of H2O and CO2 -- PyMuPDF
reported 9 superscript runs and ZERO subscript runs, because it does not flag subscripts at
all. The project had already measured the same defect in physics and written step A2N for it:
NCERT's `2.0 x 10^11 Pa` comes out of the text layer as `2.0 x 1011 Pa`. That is not a
typographic blemish, it is a materially wrong NUMBER stored as verified NCERT text, which D4
then quotes to a student as evidence.

So: the text layer owns the LAYOUT, the agent owns the WORDS. This module is the join.

HOW THE JOIN IS MADE, AND WHY NOT BY POSITION
----------------------------------------------
A2 blocks carry no coordinates -- the agent is asked for the page's content, in reading order,
not for pixel boxes. Both sides are therefore ordered sequences of blocks over the same page,
which makes this a sequence ALIGNMENT, not a lookup. `difflib` aligns them on normalised text
so a block the agent merged or split still lands against the right neighbours, and anything
that does not align is left carrying its text-layer text and counted, rather than being
silently matched to the nearest thing.

Every element records where its text came from (`text_source`), so no page can claim agent
provenance it does not have.
"""

import collections
import difflib
import glob
import json
import os
import re

# Most settled run wins, matching build_html_layout_data.py's own ordering.
_RUN_PRIORITY = {"adjudicated": 0, "retry2": 1, "retry1": 2, "runB": 3, "runA": 4}

# The roles that carry a page's readable text. Furniture is excluded deliberately: the folio and
# the running head are measured off the page and must not be replaced by a block the agent
# happened to emit, and A2's brief tells it to drop the running header/footer anyway.
_TEXT_ROLES = ("paragraph", "list", "section_heading", "figure_caption",
               "chapter_title", "side_note", "contents_entry")

_A2_KIND_TO_ROLE = {
    "heading": "section_heading",
    "paragraph": "paragraph",
    "list": "list",
    "caption": "figure_caption",
    # The kind the A2 brief actually asks for (rule 3). Unmapped, a caption the text layer had
    # guessed was a list stayed a list: Figure 4.3's caption (BIO11L ch04 p039) reached the
    # Markdown as a bullet point and its figure never got its number.
    "figure_caption": "figure_caption",
    "table": "table",
}


_SCRIPT_DIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉", "01234567890123456789")


def _norm(s):
    # A raised or lowered number is its digits, apart from what it hangs on: the agent writes
    # `10⁶ base pairs`, the layer prints `10` then `6 base pairs` as the next block's opening,
    # and the block went unclaimed -- its sentence printed twice (BIO12L ch05 p105).
    s = re.sub(r"[⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉]+",
               lambda m: " " + m.group().translate(_SCRIPT_DIGITS) + " ", s or "")
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def best_a2_path(chapter, page_num, steps_dir="steps"):
    """The most-settled A2 output for this page, or None."""
    cands = glob.glob(os.path.join(steps_dir, "A2", "out",
                                   f"{chapter}-p{page_num:03d}.*.json"))
    if not cands:
        return None
    def rank(p):
        label = os.path.basename(p).split(".")[-2]
        return _RUN_PRIORITY.get(label, 9)
    return sorted(cands, key=rank)[0]


def _align(agent_texts, pdf_texts):
    """[(agent_index | None, pdf_index | None)] aligning two block sequences.

    Alignment, not lookup: the agent legitimately merges a paragraph that the PDF splits across
    a column break, and splits one the PDF runs together. Matching by index would then shift
    every block after the first disagreement onto the wrong neighbour -- which is the failure
    that makes a join like this worse than no join at all.
    """
    a = [_norm(t)[:60] for t in agent_texts]
    b = [_norm(t)[:60] for t in pdf_texts]
    # A QUESTION IS KEYED BY ITS OWN FIRST LINE when its sub-parts follow on lines of their own.
    # `1. Define the following:` is 24 letters, so the 60-letter key ran on into `(a) Exocrine
    # gland ...`, while the layer set the stem and the sub-parts as separate blocks: no question
    # on BIO11L ch19 p251 matched, and the layer's sub-part rows printed over the agent's
    # questions. Only a block opening on a printed question number, and only when its full key
    # matches nothing.
    keys = set(b)
    for i, t in enumerate(agent_texts):
        if a[i] not in keys and "\n" in (t or "") and re.match(r"\s*\d+\.\s", t or ""):
            first = _norm(t.split("\n", 1)[0])[:60]
            if first in keys:
                a[i] = first
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    pairs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                pairs.append((i1 + k, j1 + k))
        elif tag == "replace":
            # A replace is usually the SAME block worded slightly differently (the agent fixed
            # notation). Pair them up positionally within the replaced span, and only where the
            # two are recognisably the same text.
            for k in range(max(i2 - i1, j2 - j1)):
                ai = i1 + k if i1 + k < i2 else None
                bj = j1 + k if j1 + k < j2 else None
                if ai is not None and bj is not None:
                    ratio = difflib.SequenceMatcher(None, a[ai], b[bj]).ratio()
                    pairs.append((ai, bj) if ratio >= 0.55 else (ai, None))
                    if ratio < 0.55 and bj is not None:
                        pairs.append((None, bj))
                else:
                    pairs.append((ai, bj))
        elif tag == "delete":
            pairs += [(i, None) for i in range(i1, i2)]
        elif tag == "insert":
            pairs += [(None, j) for j in range(j1, j2)]
    return _pair_out_of_order(pairs, agent_texts, pdf_texts)


def _pair_out_of_order(pairs, agent_texts, pdf_texts, min_ratio=0.6):
    """Pair blocks the in-order alignment left unmatched, by CONTENT, whatever their order.

    The two sides do not always list a page in the same order. Measured on BIO11L ch01 p009:
    the text layer returns the Summary paragraph BEFORE its `Summary` heading (the heading is
    centred, the paragraph sorts first by column), while A2 reads heading-then-paragraph. The
    alignment matched the two headings and left the paragraph AND the exercises unmatched --
    so both kept text-layer text, and the exercises lost the `Species -> Order -> Phylum`
    arrows that A2 had read (the book draws them; the text layer has nothing there).

    An agent block left over is paired with the left-over layer element its opening text most
    resembles, best match first, and only above `min_ratio`. Each pair takes the agent block's
    position in the list, so `_claim_followers` still sees the agent's own reading order.
    """
    lone_a = [ai for ai, bj in pairs if bj is None and ai is not None]
    lone_b = [bj for ai, bj in pairs if ai is None and bj is not None]
    if not lone_a or not lone_b:
        return pairs
    cands = []
    for ai in lone_a:
        a = _norm(agent_texts[ai])[:200]
        for bj in lone_b:
            b = _norm(pdf_texts[bj])[:200]
            if a and b:
                r = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
                if r >= min_ratio:
                    cands.append((r, ai, bj))
    match, used_b = {}, set()
    for r, ai, bj in sorted(cands, reverse=True):
        if ai not in match and bj not in used_b:
            match[ai] = bj
            used_b.add(bj)
    out = []
    for ai, bj in pairs:
        if ai is not None and bj is None and ai in match:
            out.append((ai, match[ai]))
        elif ai is None and bj in used_b:
            continue
        else:
            out.append((ai, bj))
    return out


def apply_agent_text(layout, chapter, steps_dir="steps"):
    """Replace measured-layout text with the A2 agent's text, in place.

    Returns {"pages": n, "pages_with_agent": n, "blocks_replaced": n, "blocks_unmatched": n,
             "pages_missing": [page numbers]} -- the numbers a report should print rather than
    a claim that the chapter "uses agent text".
    """
    stats = {"pages": 0, "pages_with_agent": 0, "blocks_replaced": 0,
             "blocks_unmatched_agent": 0, "blocks_kept_pdf": 0, "pages_missing": []}
    for pi, page in enumerate(layout["pages"], 1):
        stats["pages"] += 1
        path = best_a2_path(chapter, pi, steps_dir)
        els = [e for e in page["elements_in_reading_order"] if e["role"] in _TEXT_ROLES]
        if not path:
            stats["pages_missing"].append(page.get("printed_page_number") or pi)
            page["text_source"] = "pdf-text-layer (NO AGENT READ)"
            for e in els:
                e["text_source"] = "pdf-text-layer"
            stats["blocks_kept_pdf"] += len(els)
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                a2 = json.load(fh)
        except (OSError, json.JSONDecodeError):
            page["text_source"] = "pdf-text-layer (agent file unreadable)"
            continue
        blocks = [b for b in (a2.get("blocks") or []) if (b.get("text") or "").strip()]
        # A PAGE THE AGENT FOUND EMPTY keeps none of the layer's text it listed as furniture.
        # The blank notes page closing BIO11L ch19 prints only `NOTE`; it survived as a
        # `Note` chapter title inside the Exercises, in all three files.
        if not blocks and els:
            gone = {_norm(t) for t in a2.get("running_header_footer_removed") or [] if _norm(t)}
            drop = [e for e in els if _norm(e.get("text")) in gone]
            if drop:
                page["elements_in_reading_order"] = [
                    e for e in page["elements_in_reading_order"] if not any(e is d for d in drop)]
                els = [e for e in els if not any(e is d for d in drop)]
        stats["pages_with_agent"] += 1
        page["text_source"] = "a2-agent"
        page["a2_run"] = os.path.basename(path)

        # AN IMAGE-ONLY PAGE HAS NOTHING TO JOIN TO, SO THE AGENT'S BLOCKS BECOME THE PAGE.
        #
        # 12% of this corpus is pure scan -- `inputs/.../Class_12th/Biology/Chapter_1.pdf` is
        # A4 with zero extractable text on all 23 pages. The extractor therefore produces no
        # text elements, `els` is empty, and the alignment below has nothing to align: measured,
        # that chapter built with "23/23 pages read by a2-page-reader, 0 blocks replaced" and
        # came out as 26 figures and not one word. The agent had read every page; the join
        # discarded all of it.
        #
        # Where there is no text layer the agent IS the page, so its blocks are promoted to
        # elements directly. They carry no measured bbox -- there is nothing to measure -- so
        # they are laid out in reading order and marked `bbox_estimated`, which is honest and
        # is what A2L exists to improve on when it runs over these pages.
        if not els and blocks:
            top, step = 0.12, max(0.008, 0.76 / max(len(blocks), 1))
            for i, blk in enumerate(blocks):
                text = re.sub(r"\s+", " ", blk.get("text") or "").strip()
                if not text:
                    continue
                kind = (blk.get("kind") or "paragraph").lower()
                role = _A2_KIND_TO_ROLE.get(kind, "paragraph")
                y0 = top + i * step
                page["elements_in_reading_order"].append({
                    "role": role,
                    "text": text,
                    "runs": [{"t": text, "b": False, "i": False, "sc": False,
                              "script": None, "color": "#231f20",
                              "size": page.get("body_text_size_pt"), "font": None}],
                    "bbox": [0.10, round(y0, 4), 0.90, round(min(y0 + step, 0.97), 4)],
                    "bbox_sheet": [0.10, round(y0, 4), 0.90, round(min(y0 + step, 0.97), 4)],
                    "bbox_pt": [0.0, 0.0, 0.0, 0.0],
                    "bbox_estimated": True,
                    # WHERE THIS GEOMETRY CAME FROM, carried all the way into chapter.json.
                    # These boxes are INVENTED: 0.10-0.90 wide, evenly subdivided down the
                    # page. They are a reading-order guess and nothing more. An external
                    # review of Class 12 ch01 found all 127 of them sharing one x-range and
                    # could not tell them from measured boxes, because this key did not
                    # survive into the tree. A consumer that cannot see the difference will
                    # trust a guess as a measurement.
                    "layout_source": "estimated",
                    "column": "full",
                    "size_rel": 1.0,
                    "text_source": "a2-agent",
                    "a2_block_n": blk.get("n"),
                    **({"continues_from_previous": True}
                       if blk.get("continues_from_previous") else {}),
                })
                stats["blocks_replaced"] += 1
            page["built_from_agent_only"] = True
            continue

        if _split_leading_tails(blocks, els, page):
            els = [e for e in page["elements_in_reading_order"] if e["role"] in _TEXT_ROLES]
        pairs = _align([b.get("text", "") for b in blocks], [e.get("text", "") for e in els])
        followers = _claim_followers(pairs, blocks, els)
        claimed = {ai for tail in followers.values() for ai in tail}
        absorbed = _claim_absorbed(pairs, blocks, els)
        matched_pdf, inserts, dropped, heads_before = set(), [], [], []
        for ai, bj in pairs:
            if ai is None or bj is None:
                if ai is not None and ai not in claimed:
                    stats["blocks_unmatched_agent"] += 1
                continue
            el, blk = els[bj], blocks[ai]
            if not (blk.get("text") or "").strip():
                continue
            tail = [blocks[k] for k in followers.get(bj, [])]
            src = dict(el)
            _take_agent_block(el, blk)
            matched_pdf.add(bj)
            stats["blocks_replaced"] += 1
            # A HEADING THE AGENT'S BLOCK OPENS WITH STAYS A HEADING. A2 reads the boxed Summary
            # as one block, `SUMMARY` included; absorbed, the centred heading also failed the
            # indent test below, so BIO12L ch04's summary had no Summary section and its six
            # paragraphs were one. The heading keeps its own element; its words leave the text.
            for j in list(absorbed.get(bj) or []):
                head = (els[j].get("text") or "").strip()
                # A real heading has a word: a bare `(i)` the layer typed a heading is the
                # list item's marker (BIO12L ch01 `(i) Autogamy`), never kept apart.
                if els[j].get("role") == "section_heading" and re.search(
                        r"[A-Za-z]{4,}", head) and re.match(
                        r"\s*" + re.escape(head) + r"\b", el.get("text") or "", re.I):
                    el["text"] = re.sub(r"^\s*" + re.escape(head) + r"\b[\s:.]*", "",
                                        el["text"], count=1, flags=re.I)
                    absorbed[bj].remove(j)
                    matched_pdf.add(j)
                    heads_before.append((els[j], el))
                    _take_runs(el, src)
            if absorbed.get(bj):
                # SEVERAL LAYER BLOCKS, ONE AGENT BLOCK -- the agent's text already holds them,
                # so they leave the page and the element takes their measured boxes.
                members = [els[j] for j in absorbed[bj]]
                _set_union_geometry(el, [src] + members, page)
                # ...and their FORMATTING comes with them. The runs were taken from the first
                # layer block only, so `Marchantia` -- italic in exercise 4's own layer block,
                # absorbed into A2's block of exercises 1-4 -- printed upright (BIO11L ch03 p013).
                # A space between blocks: run together, the last word of one and the first of the
                # next made one "word", and a script glued to it was never placed (`normal` +
                # `14NH` + sub `4` on BIO12L ch05 p089 looked for `normal14NH`).
                runs = []
                for j in sorted([bj] + absorbed[bj]):
                    rs = (src if j == bj else els[j]).get("runs") or []
                    if runs and rs:
                        runs.append(dict(runs[-1], t=" ", b=False, i=False, sc=False, script=None))
                    runs += rs
                _take_runs(el, {**src, "runs": runs})
                matched_pdf.update(absorbed[bj])
                dropped += members
                paras = _split_absorbed_paragraphs(
                    el, [src if j == bj else els[j] for j in sorted([bj] + absorbed[bj])], page)
                if paras:
                    inserts.append((el, paras))
                    stats["paragraphs_kept_apart"] = (stats.get("paragraphs_kept_apart", 0)
                                                      + len(paras))
                stats["blocks_absorbed"] = stats.get("blocks_absorbed", 0) + len(members)
            if not tail:
                continue
            # ONE LAYER BLOCK, SEVERAL AGENT PARAGRAPHS -- split it on its measured lines.
            starts = _split_points(src, [blk] + tail)
            if starts is None:
                # The split cannot be placed on measured lines, so it is not guessed: the agent's
                # paragraphs stay together in the one measured box, every word kept.
                el["text"] = "\n".join([el["text"]] + [
                    re.sub(r"[ \t]+", " ", (b.get("text") or "").strip()) for b in tail])
                for b in tail:
                    _add_agent_terms(el, b)
                _take_runs(el, src)
                stats["blocks_joined_unsplit"] = stats.get("blocks_joined_unsplit", 0) + len(tail)
                continue
            lines = src["line_boxes_pt"]
            bounds = starts + [len(lines)]
            _set_part_geometry(el, src, lines[bounds[0]:bounds[1]], page)
            parts = []
            for k, b in enumerate(tail, 1):
                sub = dict(src)
                sub.pop("continues_from_previous", None)
                _take_agent_block(sub, b)
                _set_part_geometry(sub, src, lines[bounds[k]:bounds[k + 1]], page)
                parts.append(sub)
            inserts.append((el, parts))
            stats["blocks_split_from_layer"] = stats.get("blocks_split_from_layer", 0) + len(parts)
            stats["blocks_replaced"] += len(parts)
        for j, e in enumerate(els):
            if j not in matched_pdf:
                e["text_source"] = "pdf-text-layer"
                stats["blocks_kept_pdf"] += 1
        for el, parts in inserts:
            order = page["elements_in_reading_order"]
            at = next(i for i, e in enumerate(order) if e is el)
            order[at + 1:at + 1] = parts
        # ...and a heading kept out of an agent block is read before it.
        for head, el in heads_before:
            order = [e for e in page["elements_in_reading_order"] if e is not head]
            at = next(i for i, e in enumerate(order) if e is el)
            page["elements_in_reading_order"] = order[:at] + [head] + order[at:]
        if dropped:
            page["elements_in_reading_order"] = [
                e for e in page["elements_in_reading_order"]
                if not any(e is d for d in dropped)]
        # AN EQUATION'S OWN LINE, LEFT OVER. A2 gives an equation no text, so when its line was
        # part of a larger layer block (BIO12L ch13 p220: `log S = log C + Z log A` heading the
        # `where S= ...` block), the equation was rebuilt from the spans in A2's box while the
        # split left the same line behind as a layer paragraph -- printed twice, once across the
        # figure beside it. A layer leftover saying exactly what an equation on its line says
        # is that equation.
        order = page["elements_in_reading_order"]
        eqs = [e for e in order if e.get("a2_kind") == "equation" and e.get("bbox_pt")]
        twins = [e for e in order if e.get("text_source") == "pdf-text-layer"
                 and e.get("a2_block_n") is None and e.get("bbox_pt") and (e.get("text") or "").strip()
                 and any(_norm(e["text"]) == _norm(q.get("text"))
                         and min(e["bbox_pt"][3], q["bbox_pt"][3])
                         - max(e["bbox_pt"][1], q["bbox_pt"][1])
                         > 0.5 * (e["bbox_pt"][3] - e["bbox_pt"][1]) for q in eqs)]
        if twins:
            page["elements_in_reading_order"] = [e for e in order
                                                 if not any(e is t for t in twins)]
            stats["equation_twins_dropped"] = stats.get("equation_twins_dropped", 0) + len(twins)
    layout["text_join"] = stats
    return stats


def _split_leading_tails(blocks, els, page):
    """Cut a layer block where an agent block STARTS on one of its lines. True if any was cut.

    The layer can run the end of one printed block into the start of the next, and the
    alignment then pairs the mixed block with only one of the two:
      * BIO12L ch05 p096: `also act as initiator codon. (vi) UAA, UAG, UGA ... If following is
        the sequence ...` -- the genetic-code list's last two lines, then the italic prompt (the
        margin folio ended the list's own blocks). Paired with the prompt, the list never got
        those lines: `initiator` lost its bold and the list its last lines' box.
      * p082: `over the other in double helix ... (Figure 5.3). Compare the structure of purines
        ...` -- list item (v)'s end, then the italic prompt. The list absorbed it whole and the
        prompt was dropped from every output.
    A block is cut at a measured line (after its first) that opens with an agent block's first
    words; each piece keeps its own lines, runs and box, and the alignment pairs them apart.
    """
    starts = [_norm(b.get("text"))[:25] for b in blocks
              if (b.get("kind") or "paragraph").lower() in ("paragraph", "list", "box", "question")]
    starts = [s for s in starts if len(s) >= 15]
    cut_any = False
    for el in list(els):
        lines = sorted(el.get("line_boxes_pt") or [], key=lambda ln: ln["bbox_pt"][3])
        if len(lines) < 2 or not el.get("text"):
            continue
        norms = [_norm(ln.get("text")) for ln in lines]
        cuts = []                                     # (line index, char offset)
        for k in range(1, len(lines)):
            joined = " ".join(norms[k:k + 3])
            probe = next((s for s in starts if joined.startswith(s)), None)
            if not probe:
                continue
            words = (lines[k].get("text") or "").split()[:4]
            at, _ = _find_flex(el["text"], " ".join(words), cuts[-1][1] + 1 if cuts else 1,
                               boundary=True)
            if at > 0:
                cuts.append((k, at))
        if not cuts:
            continue
        src = dict(el)
        bounds = [(0, 0)] + cuts + [(len(lines), len(src["text"]))]
        pieces = []
        for (k0, a0), (k1, a1) in zip(bounds, bounds[1:]):
            part = el if not pieces else dict(src)
            part["text"] = src["text"][a0:a1].strip()
            part["runs"] = _slice_runs(src.get("runs") or [], a0, a1)
            if pieces:
                part.pop("continues_from_previous", None)
            _set_part_geometry(part, src, lines[k0:k1], page)
            pieces.append(part)
        order = page["elements_in_reading_order"]
        at_el = next(i for i, e in enumerate(order) if e is el)
        order[at_el + 1:at_el + 1] = pieces[1:]
        cut_any = True
    return cut_any


def _claim_absorbed(pairs, blocks, els):
    """{layer index: [layer indices]} -- layer blocks the alignment left unmatched whose text is
    already INSIDE the agent block matched to their neighbour.

    The mirror of `_claim_followers`. A2 can read as one block what the layer returns as several:
    measured on BIO11L ch03 p014, A2 returned exercises 5-9 as one list block while the layer had
    eight (each question, and each line of question 8's sub-parts). The alignment gave the agent
    block to question 5 and left the other seven on their layer text, so questions 6-9 printed
    twice -- and the duplicates then defeated the exercise split. A layer block is claimed only when
    its opening words are found in the agent block's text, scanning outward from the matched one
    in both directions and stopping at the first block that is not.
    """
    matched = {bj: ai for ai, bj in pairs if ai is not None and bj is not None}
    unmatched = {bj for ai, bj in pairs if ai is None and bj is not None}
    out = {}
    for bj, ai in matched.items():
        agent = _norm(blocks[ai].get("text"))
        if len(agent) <= len(_norm(els[bj].get("text"))):
            continue
        # Compared without spaces: the agent's `T₄` normalises to `t 4`, the layer's `T4` to
        # `t4`, and Q9's match rows (BIO11L ch19 p251) went unclaimed and printed twice.
        flat = agent.replace(" ", "")
        claim = []
        for step in (1, -1):
            j = bj + step
            blanks = []
            while j in unmatched and j not in claim:
                probe = _norm(els[j].get("text"))[:25]
                # A blank's own line (`_______.`, BIO11L ch16 p216) has no words to probe; it
                # joins the block only if a worded block past it does, so the scan goes on.
                if not probe:
                    blanks.append(j)
                    j += step
                    continue
                if probe.replace(" ", "") not in flat:
                    break
                claim += blanks + [j]
                blanks = []
                j += step
        if claim:
            out[bj] = sorted(claim)
            unmatched -= set(claim)
    return out


def _split_absorbed_paragraphs(el, group, page):
    """[parts] -- the paragraphs of a boxed passage A2 read as ONE block, split back apart.

    A2 reads a boxed Summary as a single block; the layer returns its paragraphs as blocks of
    their own, each opening on a paragraph indent. `_claim_absorbed` merged them, so BIO12L
    ch02's three-paragraph summary came out as one 40-line paragraph. Each later layer block
    must open on an INDENT (8-30pt in from the passage's left edge) -- a block that is merely
    the next column beside a figure starts on the edge or a figure's width away, and stays
    joined -- and its opening words must be found in the agent's text in order. Otherwise the
    passage stays whole. `el` keeps the first paragraph; the rest are returned.
    """
    if el.get("role") != "paragraph" or len(group) < 2:
        return None
    lines = [ln for g in group for ln in (g.get("line_boxes_pt") or [])]
    if not lines or any(not g.get("line_boxes_pt") for g in group):
        return None
    left = min(ln["bbox_pt"][0] for ln in lines)
    for g in group[1:]:
        first = min(g["line_boxes_pt"], key=lambda ln: ln["bbox_pt"][1])
        if not 8.0 <= first["bbox_pt"][0] - left <= 30.0:
            return None
    text, cuts = el["text"], [0]
    for g in group[1:]:
        words = (g.get("text") or "").split()[:5]
        if len(words) < 3:
            return None
        at, _ = _find_flex(text, " ".join(words), cuts[-1] + 1, boundary=True)
        if at <= cuts[-1]:
            return None
        cuts.append(at)
    cuts.append(len(text))
    whole = dict(el)
    parts = []
    for k, g in enumerate(group):
        tgt = el if k == 0 else dict(whole)
        if k:
            tgt.pop("continues_from_previous", None)
        tgt["text"] = text[cuts[k]:cuts[k + 1]].strip()
        _take_runs(tgt, {**g, "runs": g.get("runs") or []})
        _set_part_geometry(tgt, whole, sorted(g["line_boxes_pt"],
                                               key=lambda ln: ln["bbox_pt"][3]), page)
        if k:
            parts.append(tgt)
    return parts


def _set_union_geometry(el, members, page):
    """The box of several measured layer blocks merged into one element: their union."""
    boxes = [m["bbox_pt"] for m in members]
    x0, y0 = min(b[0] for b in boxes), min(b[1] for b in boxes)
    x1, y1 = max(b[2] for b in boxes), max(b[3] for b in boxes)
    pw, ph = page["page_width_pt"], page["page_height_pt"]
    sw, sh = page["sheet_pt"]
    dx, dy = page.get("sheet_offset_pt") or (0.0, 0.0)
    el["bbox_pt"] = [x0, y0, x1, y1]
    el["bbox"] = [round(x0 / pw, 4), round(y0 / ph, 4), round(x1 / pw, 4), round(y1 / ph, 4)]
    el["bbox_sheet"] = [round((x0 + dx) / sw, 4), round((y0 + dy) / sh, 4),
                        round((x1 + dx) / sw, 4), round((y1 + dy) / sh, 4)]
    el["line_count"] = sum(m.get("line_count") or 0 for m in members) or el.get("line_count")
    el["line_boxes_pt"] = sorted((ln for m in members for ln in (m.get("line_boxes_pt") or [])),
                                 key=lambda ln: ln["bbox_pt"][3])


def _claim_followers(pairs, blocks, els):
    """{layer index: [agent indices]} -- agent blocks the alignment left unmatched that sit
    INSIDE the layer block their predecessor matched.

    PyMuPDF can hand back several printed paragraphs as one block while A2 reads them apart.
    The alignment pairs the first paragraph with the block and leaves the rest unmatched, and an
    unmatched agent block used to be dropped -- losing text that was in both sources. A block is
    claimed only when its opening words are found in the layer block's own text, so a block the
    agent saw and the layer did not is still reported unmatched.
    """
    followers, host, nxt = {}, None, None
    for ai, bj in pairs:
        if ai is not None and bj is not None:
            host, nxt = bj, ai + 1
            followers[bj] = []
            continue
        if ai is None or host is None or ai != nxt:
            host = None
            continue
        probe = _norm(blocks[ai].get("text"))[:25]
        if probe and probe in _norm(els[host].get("text")):
            followers[host].append(ai)
            nxt = ai + 1
        else:
            host = None
    # A FIGURE BETWEEN THE TWO PARAGRAPHS breaks the chain above. On BIO12L ch03 p004 the layer
    # holds `In barrier methods ...` and `Another effective and popular method ... (IUDs)` as one
    # block, while A2 reads them as blocks 6 and 9 with Figure 3.2 and its caption (7, 8) in
    # between. The caption matched its own element, so the IUD paragraph -- the page's last,
    # running on to p005 -- was dropped from every output. A paragraph still unclaimed goes to the
    # nearest EARLIER matched layer block whose text holds its opening words.
    taken = {a for tail in followers.values() for a in tail}
    matched = [(ai, bj) for ai, bj in pairs if ai is not None and bj is not None]
    for ai, bj in pairs:
        if ai is None or bj is not None or ai in taken:
            continue
        if (blocks[ai].get("kind") or "paragraph").lower() not in ("paragraph", "list", "box"):
            continue
        probe = _norm(blocks[ai].get("text"))[:25]
        hosts = [h for a, h in matched if a < ai and probe and probe in _norm(els[h].get("text"))]
        if hosts:
            followers.setdefault(hosts[-1], []).append(ai)
            followers[hosts[-1]].sort()
            taken.add(ai)
    return {bj: tail for bj, tail in followers.items() if tail}


def _split_points(src, parts):
    """The index of the measured line each part starts on, or None if any start is not found."""
    lines = src.get("line_boxes_pt") or []
    if len(lines) < len(parts):
        return None
    norms = [_norm(ln["text"]) for ln in lines]
    starts = [0]
    for blk in parts[1:]:
        probe = _norm(blk.get("text"))[:25]
        hit = next((k for k in range(starts[-1] + 1, len(lines))
                    if probe and " ".join(norms[k:k + 3]).startswith(probe)), None)
        if hit is None:
            return None
        starts.append(hit)
    return starts


def _set_part_geometry(el, src, lines, page):
    """Give one part of a split block the box of its own measured lines.

    The x-extent stays the block's, which is measured; the y-extent is the part's own lines.
    `bbox_sheet` uses the chapter offset exactly as `extract_page_layout._apply_chapter_offset`.
    """
    x0, x1 = src["bbox_pt"][0], src["bbox_pt"][2]
    y0 = min(ln["bbox_pt"][1] for ln in lines)
    y1 = max(ln["bbox_pt"][3] for ln in lines)
    pw, ph = page["page_width_pt"], page["page_height_pt"]
    sw, sh = page["sheet_pt"]
    dx, dy = page.get("sheet_offset_pt") or (0.0, 0.0)
    el["bbox_pt"] = [x0, y0, x1, y1]
    el["bbox"] = [round(x0 / pw, 4), round(y0 / ph, 4), round(x1 / pw, 4), round(y1 / ph, 4)]
    el["bbox_sheet"] = [round((x0 + dx) / sw, 4), round((y0 + dy) / sh, 4),
                        round((x1 + dx) / sw, 4), round((y1 + dy) / sh, 4)]
    el["line_count"] = len({round(ln["bbox_pt"][3], 1) for ln in lines})
    el["line_boxes_pt"] = lines


def _take_agent_block(el, blk):
    """Put one A2 block's text onto one measured element, in place."""
    text = (blk.get("text") or "").strip()
    # DO NOT FLATTEN THE AGENT'S NEWLINES.
    #
    # A2 returns a numbered list as ONE block whose items are separated by `\n` --
    # `1. Why are living organisms classified?\n2. Why are the classification systems
    # changing...`. Collapsing all whitespace threw that structure away, and the
    # exercises then had to be re-split by guessing sentence boundaries, which gets 7
    # of 10 right because question 9 contains `(i) Phylum (ii) Class ...` sub-parts.
    # The agent already knew where the questions start; the join was deleting the
    # answer and then trying to reconstruct it.
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n", text).strip()
    el["text"] = text
    el.pop("agent_terms", None)
    _add_agent_terms(el, blk)
    _take_runs(el, dict(el))
    el["text_source"] = "a2-agent"
    el["a2_block_n"] = blk.get("n")
    # A2 is the ONLY thing that knows a paragraph runs on from the previous page --
    # it reads the two pages in sequence and says so. Without carrying the flag, a
    # paragraph broken by a page break stays two half-paragraphs, neither quotable:
    # measured on BIO11L ch01, "If you look around you will see..." ends page 3 mid
    # sentence and "types of organisms present on earth..." opens page 4.
    if blk.get("continues_from_previous"):
        el["continues_from_previous"] = True
    kind = _A2_KIND_TO_ROLE.get((blk.get("kind") or "").lower())
    # The agent's KIND is a judgement about what the block is, which is the thing an
    # agent is for; the text layer's role is inferred from size and position. Where the
    # agent says `heading` and the heuristic said `paragraph`, the agent is right.
    if kind and kind != el["role"] and el["role"] in ("paragraph", "list"):
        el["role"] = kind
    # A caption set in a narrow column extracts as `side_note`, and a side_note becomes a `box`
    # node: Figure 5.12's caption on BIO11L ch05 p011 did. The agent saw a caption.
    elif kind == "figure_caption" and el["role"] == "side_note":
        el["role"] = kind


def _add_agent_terms(el, blk):
    """Remember the bold and italic terms A2 read off the page image for this block."""
    terms = el.setdefault("agent_terms", {"b": [], "i": []})
    for key, field in (("b", "bold_terms"), ("i", "italic_terms")):
        terms[key] += [t for t in (blk.get(field) or []) if isinstance(t, str) and t.strip()]


# Separators the text layer folds into an emphasised run: `Examples ... insects – Apis` sets
# the dash in the italic face with the genus, so the run is `– Apis`. They are not emphasis.
# Nor is a comma: `Mucor (Figure 2.5a), Rhizopus` sets `, Rhizopus` as one italic run (BIO11L
# ch02 p017), which reached the Markdown as `(Figure 2.5a)*, Rhizopus*`.
_LEAD_JUNK = " \t\n–—-•·,;"


def _find_flex(text, frag, start, boundary):
    """Where `frag` occurs in `text` at or after `start`, whitespace matched loosely.

    The layer's run is one line's worth of characters with its line breaks collapsed;
    the agent's text keeps the book's `\\n`. `Ascidia, Salpa, Doliolum;` is one italic
    run in the layer and `Ascidia, Salpa,\\nDoliolum;` in the agent's text, so an exact
    search missed it and three genus names lost their italics (BIO11L ch04 p010).
    `boundary` demands the match not begin or end inside a word.
    """
    # A line broken after a slash or hyphen (`yellow/` | `green`, BIO12L ch04 p012) is one word
    # in the agent's text, so the space after such a word is optional.
    words = frag.split()
    pat = "".join(re.escape(w) + ((r"\s*" if w[-1] in "/-" else r"\s+") if k < len(words) - 1
                                  else "") for k, w in enumerate(words))
    if boundary:
        pat = r"(?<![A-Za-z0-9])" + pat + r"(?![A-Za-z0-9])"
    m = re.compile(pat).search(text, start)
    return (m.start(), m.end()) if m else (-1, -1)


_SUP_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
_SUB_DIGITS = "₀₁₂₃₄₅₆₇₈₉"


class _Shift:
    """A regex match on a slice, reporting offsets in the whole string."""

    def __init__(self, m, by):
        self._m, self._by = m, by

    def start(self, g=0):
        return self._m.start(g) + self._by

    def end(self, g=0):
        return self._m.end(g) + self._by


def _take_runs(el, src):
    """Rebuild `el["runs"]` over `el["text"]`, carrying `src`'s formatted runs into it.

    THE AGENT'S TEXT WINS; THE LAYER'S FORMATTING IS RE-LOCATED INTO IT.

    The naive version took the agent's string and gave it the FIRST run's flags. On
    the Genus paragraph the first run is the bold term `Genus`, so the whole
    479-character paragraph came back bold -- 1 mark where the book prints 7, and
    `terms` empty because no single word was bold any more.

    The layer is wrong about the CHARACTERS of a formula and right about WHICH WORDS
    are bold or italic, so the formatted substrings are carried over by searching for
    them in the agent's text. A substring that cannot be found is dropped rather than
    guessed at: a mark in the wrong place is worse than a missing one, because it
    renders as emphasis the book does not print.
    """
    text = el["text"]
    src_runs = src.get("runs") or [{}]
    base = src_runs[0]
    # THE PLAIN TEXT'S FACE IS THE ONE THE PLAIN TEXT WAS PRINTED IN, NOT THE FIRST RUN'S.
    # Every rebuilt run used to take `base`'s font, and on a paragraph that opens with a bold
    # term `base` is that term: the Genus paragraph's 474 plain characters all came back
    # `Bookman-Demi`, `print_font` (most-printed face) became the bold face, and the exact
    # render set the whole paragraph bold -- 25 paragraphs across BIO11L ch01-ch10. The flags
    # were right; only the face was wrong. Plain runs take the face of the source's unflagged
    # text (by characters); a formatted run keeps the face of the run it was found in.
    face = collections.Counter()
    for r in src_runs:
        if not any(r.get(k) for k in ("b", "i", "sc", "script")):
            face[(r.get("font"), r.get("size"), r.get("color"))] += len((r.get("t") or "").strip())
    plain = dict(zip(("font", "size", "color"),
                     face.most_common(1)[0][0] if face else
                     (base.get("font"), base.get("size"), base.get("color"))))
    spans = []
    for k, r in enumerate(src_runs):
        frag = re.sub(r"\s+", " ", r.get("t", "")).strip()
        flags = {k: True for k in ("b", "i", "sc") if r.get(k)}
        if r.get("script"):
            flags["script"] = r["script"]
        else:
            frag = frag.lstrip(_LEAD_JUNK)
        # Up to 800 characters, not 120: an italic activity prompt runs several lines as one
        # run -- `Take out some seeds of orange ... Can they be called clones?` (BIO12L ch01
        # p023, 260 characters) -- and the cap dropped it, so the prompt printed upright. A long
        # run is matched whitespace-flexibly and simply not placed if the agent's text differs.
        if frag and flags and len(frag) <= 800:
            flags["_face"] = (r.get("font"), r.get("size"), r.get("color"))
            # The two words printed just before it, for placing a short fragment (below).
            before = "".join(q.get("t", "") for q in src_runs[:k])
            ctx = before.split()[-2:] if before[-1:].isspace() else []
            # ...or the word it is GLUED to. `about 14th day` sets `th` as a superscript run
            # straight after `14`, with no space, so there were no words before it to place it
            # by -- and the boundary search below put it on the `th` ending `Both`, a line
            # earlier (BIO12L ch02 p010). `14` + `th` lands on the right one.
            glued = before.split()[-1] if before.strip() and not before[-1:].isspace() else None
            # ...and what is glued AFTER it. `(Hb<sup>S</sup>Hb<sup>S</sup>)` prints the next
            # `Hb` straight after the first `S`, so "no letter follows" refused the right `S`
            # and the mark went to the second (BIO12L ch04 p024: `HbSHb<sup>S</sup>`).
            after = "".join(q.get("t", "") for q in src_runs[k + 1:])
            # (A run that ends in its own space -- the layer's `1 ` of `F1 plants` -- has nothing
            # glued after it.)
            glued_after = (after.split()[0][:3] if after.strip() and not after[:1].isspace()
                           and not r.get("t", "")[-1:].isspace() else None)
            spans.append((frag, flags, ctx, (glued, glued_after)))
    found, cursor = [], 0      # (start, end, flags) of each formatted range in `text`
    for frag, flags, ctx, (glued, glued_after) in spans:
        if len(frag) <= 3 and glued:
            tail = (r"(?=" + re.escape(glued_after) + ")" if glued_after and glued_after[:1].isalpha()
                    else r"(?![A-Za-z])")
            # The word it is glued to may END the formatted run placed just before it --
            # `quiescent stage (G` italic, then `0` (BIO11L ch10 p003) -- so the search starts
            # far enough back to see that word again -- but the fragment itself lands at or after
            # the cursor, never on one already placed (`G1 ... G1` became `G11`, BIO11L ch10).
            # The glued word is matched with the agent's spacing round symbols: the layer prints
            # `4.6 ×10` + `6`, the agent `4.6 × 106` (BIO12L ch05 p090). And a word opening on
            # a LETTER may follow a digit -- `15NH4Cl` prints `15` (sup), `NH`, `4` (sub): the
            # `4` is glued to `NH`, which the isotope number touches.
            # A digit also matches its raised or lowered form: the layer's `10` + `9` is `10⁹`
            # in the agent's text (BIO12L ch05 p105), and ` bp` after it lost its italic.
            gpat = "".join((f"[{c}{_SUP_DIGITS[int(c)]}{_SUB_DIGITS[int(c)]}]" if c.isdigit()
                            else re.escape(c)) + (r"\s*" if (c.isalnum() != nx.isalnum()) else "")
                           for c, nx in zip(glued, glued[1:] + glued[-1]))
            lead = r"(?<![A-Za-z])" if glued[:1].isalpha() else r"(?<![A-Za-z0-9])"
            m = next((x for x in re.finditer(
                lead + gpat + r"\s*(" + re.escape(frag) + r")" + tail,
                text) if x.start(1) >= cursor
                and x.start() >= max(0, cursor - len(glued) - 1)), None)
            if m:
                found.append((m.start(1), m.end(1), flags))
                cursor = m.end(1)
                continue
            # A GLUED FRAGMENT NOT FOUND ON ITS WORD IS NOT PLACED. The searches below take any
            # free-standing letter: the `A` of `Hb<sup>A</sup>` landed on `A daughter` in the
            # paragraph before (BIO12L ch04 p023/p024), and where the agent wrote the allele as
            # `Iᴬ` the layer's `I` + `A` landed on `both A and B types of sugars` (p011) --
            # superscripts the book does not print. A missing mark is better than a wrong one.
            continue
        # A SHORT FRAGMENT IS PLACED BY THE WORDS BEFORE IT. `chlorophyll a, c` italicises the
        # letters `a` and `c`; a forward search for a free-standing `a` found the article in
        # `may reach a height` a line earlier (BIO11L ch03 p004), so the article was italic and
        # chlorophyll's `a` plain. Searching for `chlorophyll a` lands on the right `a`; if the
        # agent's text differs there, the plain search below still runs.
        # A NUMBER may sit against a letter -- the isotope `¹⁵N` (BIO12L ch05 p089) -- but never
        # inside a longer number. A letter fragment keeps the rule that it ends its word.
        numeric = frag.isdigit()
        after_frag = r"(?!\d)" if numeric else r"(?![A-Za-z])"
        # ...unless the layer itself prints letters straight after it: the red `B` inserted in
        # `RAM HAS BRE DCA P` (BIO12L ch05 p097) is its own run, glued to `RE`.
        if not numeric and glued_after and glued_after[:1].isalpha():
            after_frag = r"(?=" + re.escape(glued_after) + ")"
        # The context words may END the run placed just before (`RAM HAS` bold, then the red
        # `B`, BIO12L ch05 p097), so the search looks back over them; the fragment itself still
        # lands at or after the cursor.
        back = max(0, cursor - len(" ".join(ctx)) - 4) if ctx else cursor

        def _ctx_hit(pat):
            return next((x for x in re.finditer(pat, text[back:])
                         if x.start(1) + back >= cursor), None)
        if len(frag) <= 3 and ctx:
            m = _ctx_hit(r"\s+".join(re.escape(w) for w in ctx) + r"\s*("
                         + re.escape(frag) + r")" + after_frag)
            if m:
                m = _Shift(m, back)
                found.append((m.start(1), m.end(1), flags))
                cursor = m.end(1)
                continue
        # A SHORT FRAGMENT MUST NOT MATCH INSIDE A LONGER WORD.
        #
        # "ERNST MAYR ... was known as the Darwin of the 20th century" carries ONE
        # superscript run: the "th" of "20th". Scanning forward for "th" finds the
        # "th" of "the" first -- 76 characters earlier -- and the render came out as
        # "<sup>th</sup>e Harvard University", raising two letters of an ordinary
        # word. The run is real and its flags are right; only the position was wrong.
        #
        # So a fragment of three characters or fewer must land on a word boundary:
        # "th" may match "20th" (followed by a space) and never "the" (followed by a
        # letter). Longer fragments are distinctive enough not to need this.
        # A LONGER FRAGMENT IS ALSO PLACED BY THE WORDS BEFORE IT, when the layer has them. The
        # first copy after the cursor is not always the printed one: BIO12L ch05 p095 bolds
        # `In capping`, and `called as capping` a line earlier took the mark. A copy with no
        # sign of the printed context (not even its preceding word) is not marked at all: the
        # layer's block there ran in another block's runs, and `the process of splicing`
        # (plain in the book) came out bold.
        if len(frag) > 3 and ctx and not flags.get("sc"):
            m = _ctx_hit(r"\s+".join(re.escape(w) for w in ctx) + r"\s*("
                         + r"\s+".join(map(re.escape, frag.split())) + r")")
            if m:
                m = _Shift(m, back)
                found.append((m.start(1), m.end(1), flags))
                cursor = m.end(1)
                continue
            want = re.sub(r"[^a-z0-9]", "", ctx[-1].lower())

            def _ctx_ok(at):
                # one side may be a line-broken half (`pro-` / `process`)
                # the last token holding a letter or digit: a dash is not a word (`Aquarium
                # – Betta`, BIO11L ch04 p048, lost Betta's italic)
                pw = re.sub(r"[^a-z0-9]", "", next(
                    (w for w in reversed(text[:at].split()) if re.search(r"[A-Za-z0-9]", w)),
                    "").lower())
                if not want or pw == want:
                    return True
                return min(len(pw), len(want)) >= 3 and (
                    pw.startswith(want) or want.startswith(pw)
                    or pw.endswith(want) or want.endswith(pw))
            at, end = _find_flex(text, frag, cursor, boundary=False)
            while at >= 0 and not _ctx_ok(at):
                at, end = _find_flex(text, frag, at + 1, boundary=False)
            if at < 0:
                continue
            found.append((at, end, flags))
            cursor = end
            continue
        at, probe = -1, cursor
        while True:
            at, end = _find_flex(text, frag, probe, boundary=False)
            if at < 0:
                break
            if len(frag) > 3:
                break
            if numeric:
                if not (end < len(text) and text[end].isdigit()) and not (
                        at > 0 and text[at - 1].isdigit()):
                    break
            elif not (end < len(text) and text[end].isalpha()):
                break
            probe = at + 1
        if flags.get("sc"):
            # SMALL CAPS: THE LAYER KNOWS THE CASE, THE PICTURE DOES NOT. NCERT sets `1.1
            # Diversity in the Living World` with its lower-case letters as small capitals; the
            # agent reads the image and writes `DIVERSITY IN THE LIVING WORLD`, the layer's run
            # says `Diversity in the Living World` and flags it small caps. The exact search
            # missed on case, so the heading reached chapter.json and the Markdown in capitals
            # and the render set it as plain capitals. Matched case-blind, the layer's casing
            # is copied letter for letter (same length, so no offset moves) and the mark kept.
            # A digit matches its script forms too: the layer's `The C4 Pathway` is the agent's
            # `11.8 THE C₄ PATHWAY` (BIO11L ch11 p145), which stayed in plain capitals.
            def pat(w):
                return "".join(f"[{c}{_SUB_DIGITS[int(c)]}{'⁰¹²³⁴⁵⁶⁷⁸⁹'[int(c)]}]"
                               if c.isdigit() and c.isascii() else re.escape(c) for c in w)
            m = re.compile(r"\s+".join(pat(w) for w in frag.split()), re.I).search(text, cursor)
            # ...and an EARLIER case-blind match beats a later exact one: the Unit 2 biography
            # opens `KATHERINE ESAU was born` (small caps) and names `Katherine Esau` again in
            # plain text near its end. The exact search took the late one, the cursor jumped
            # past both italic book titles in between, and they lost their italic.
            if m and (at < 0 or m.start() < at):
                letters = iter(ch for ch in frag if not ch.isspace())
                # letter for letter; a digit consumes its partner but keeps the agent's `₄`
                seg = "".join(ch if ch.isspace() else (lambda lc: lc if ch.isalpha() else ch)(
                    next(letters, ch)) for ch in text[m.start():m.end()])
                text = text[:m.start()] + seg + text[m.end():]
                el["text"] = text
                at, end = m.start(), m.end()
        if at < 0:
            continue
        found.append((at, end, flags))
        cursor = end
    # THE AGENT'S OWN TERMS FILL WHAT THE LAYER COULD NOT PLACE.
    #
    # The layer's runs cover only the measured element the agent block was paired with. A2
    # read `(i) open type ...\n(ii) closed type ...` as one list block, but only line (i)'s
    # element came across, so `closed type` had no bold run and printed plain (BIO11L ch04
    # p002). A2 lists the bold and italic terms it saw in `bold_terms` / `italic_terms`, so a
    # term the layer left unmarked is placed from there -- on a word boundary, never over a
    # range already formatted, first unformatted occurrence only (a term recurs in prose
    # unemphasised, and A2 lists a term once however often the book bolds it).
    # A term the LAYER carried in that style is not filled: the layer knew where the book
    # printed it, and if its run could not be placed there, the first plain occurrence is a
    # guess -- BIO11L ch05 bolded `opposite and whorled` for the `whorled,` of `as in Alstonia`.
    layer_terms = {k: {re.sub(r"\W+", " ", f).strip().lower() for f, fl, _c, _g in spans
                       if fl.get(k)} for k in ("b", "i")}
    for key, terms in (el.get("agent_terms") or {}).items():
        for term in sorted(set(terms), key=len, reverse=True):
            term = term.strip()
            if any(f.get(key) and text[a:e].strip() == term for a, e, f in found):
                continue
            # ...nor a term INSIDE a run the layer carried in that style: the header run
            # `Column I Column II` holds both terms, and the fill bolded them in the plain
            # stem `Match Column I with Column II` above it (BIO11L ch15, ch17).
            tkey = re.sub(r"\W+", " ", term).strip().lower()
            if any(f" {tkey} " in f" {lt} " for lt in layer_terms.get(key, ())):
                continue
            probe = 0
            while True:
                at, end = _find_flex(text, term, probe, boundary=True)
                if at < 0:
                    break
                if not any(at < e and a < end for a, e, _ in found):
                    found.append((at, end, {key: True}))
                    break
                probe = at + 1
    found.sort(key=lambda x: x[0])
    runs, cursor = [], 0
    for at, end, flags in found:
        if at > cursor:
            runs.append({"t": text[cursor:at]})
        runs.append({"t": text[at:end], **flags})
        cursor = end
    if cursor < len(text):
        runs.append({"t": text[cursor:]})
    for r in runs:
        r.setdefault("b", False); r.setdefault("i", False)
        r.setdefault("sc", False); r.setdefault("script", None)
        font, size, color = r.pop("_face", None) or (plain["font"], plain["size"], plain["color"])
        r["color"] = color or "#231f20"
        r["size"] = size; r["font"] = font
    el["runs"] = runs or [{"t": text, "b": False, "i": False, "sc": False,
                           "script": None, "color": plain["color"] or "#231f20",
                           "size": plain["size"], "font": plain["font"]}]


# ---------------------------------------------------------------------------------------------
# A2's FIGURE boxes: one printed figure, one element, its labels inside it
# ---------------------------------------------------------------------------------------------

#: A2 renders the page at this resolution, so its `bbox` is in these pixels.
_A2_DPI = 200
#: Only short text is a label -- the same bar `extract_page_layout._absorb_figure_labels` uses.
_LABEL_MAX = 42
_NOT_LABEL = ("figure_caption", "section_heading", "page_number", "running_header",
              "reprint_line", "page_furniture", "contents_entry")


def _inside(box, area, frac):
    ix = max(0.0, min(box[2], area[2]) - max(box[0], area[0]))
    iy = max(0.0, min(box[3], area[3]) - max(box[1], area[1]))
    a = max(1e-6, (box[2] - box[0]) * (box[3] - box[1]))
    return ix * iy / a >= frac


def _centre_in(box, area):
    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    return area[0] <= cx <= area[2] and area[1] <= cy <= area[3]


_PANEL_LETTER = re.compile(r"^\(\s*([a-z])\s*\)$")


def _letters_of(labels):
    """The panel letters among a fragment's absorbed labels: `['(a)', 'Hypha']` -> ['a']."""
    out = []
    for t in labels or []:
        for tok in re.findall(r"\(\s*[a-z]\s*\)", t or ""):
            m = _PANEL_LETTER.match(tok)
            if m and m.group(1) not in out:
                out.append(m.group(1))
    return out


def _box_gap(a, b):
    dx = max(0.0, max(a[0], b[0]) - min(a[2], b[2]))
    dy = max(0.0, max(a[1], b[1]) - min(a[3], b[3]))
    return (dx * dx + dy * dy) ** 0.5


_PAGE_READS = {}


def _page_read(pg, what):
    """A page's words, text dict or image list, read ONCE per page and kept.

    The figure pass asked PyMuPDF for them again for every figure and panel, and each request
    rebuilds the page's text page: on BIO12L ch01 that was 81 rebuilds at ~1.15s on the dense
    pages -- 95s of a 157s pass. Keyed by the file's normalised path and page number."""
    import os
    key = (os.path.normcase(os.path.abspath(pg.parent.name)), pg.number, what)
    if key not in _PAGE_READS:
        _PAGE_READS[key] = (pg.get_text("words") if what == "words"
                            else pg.get_text("dict") if what == "dict"
                            else pg.get_image_info(xrefs=True) if what == "images_x"
                            else pg.get_image_info())
    return _PAGE_READS[key]


def _cluster_boxes(boxes, gap=8.0, min_pt=12.0):
    """Measured ink boxes grouped into the separate drawings they make up (touching = one).

    Grid occupancy, not pairwise: Figure 2.6 alone is 61,000 paths. Same routine the extractor
    clusters figure fragments with. Clusters smaller than `min_pt` either way are dropped."""
    if not boxes:
        return []
    from extract_page_layout import merge_image_blocks
    w = max(b[2] for b in boxes) + gap
    h = max(b[3] for b in boxes) + gap
    return [list(b) for b, _n in merge_image_blocks(boxes, w, h, gap_pt=gap, min_pt=min_pt)
            if (b[2] - b[0]) >= min_pt and (b[3] - b[1]) >= min_pt]


def _named_panels_from_pdf(pdf_page, area, pw, ph):
    """[{label, key, bbox_pt}] for a figure of separate drawings each NAMED beneath, or [].

    Figure 2.1 (BIO11L ch02 p012) prints four bacteria -- Cocci, Bacilli, Spirilla, Vibrio --
    each its own drawing with its name under it, and no `(a)` `(b)` letters, so the lettered
    search found nothing and the four shipped as one crop and one CDN link. Here the drawings
    are clustered from the page's own vector paths and images, and a cluster is a panel when
    the lowest short text line centred under it names it. Part labels set higher with leader
    lines (`Spore`, `Flagellum`) join the panel they sit on.

    A labelled single diagram must stay whole, so this refuses unless: at least two clusters,
    every cluster named, the names distinct, short, and printed near one baseline (a diagram's
    part labels are scattered), and no two panels overlap. `key` (a, b, c ...) names the crop
    file; `label` is the printed name.
    """
    import pymupdf
    import book_design
    from extract_page_layout import visible_drawings

    def usable(b):
        frac = (b[0] / pw, b[1] / ph, b[2] / pw, b[3] / ph)
        if book_design.is_watermark(frac) or (b[2] - b[0]) >= 0.9 * pw:
            return None
        if not _centre_in(b, area):
            return None
        return [max(b[0], area[0]), max(b[1], area[1]), min(b[2], area[2]), min(b[3], area[3])]

    ink = [c for info in _page_read(pdf_page, "images") for c in [usable(list(info["bbox"]))] if c]
    for d in visible_drawings(pdf_page):
        r = d["rect"]
        c = usable([r.x0, r.y0, r.x1, r.y1])
        if c:
            ink.append(c)
    clusters = [c for c in _cluster_boxes(ink, gap=5.0)
                if c[2] - c[0] >= 15 and c[3] - c[1] >= 15]
    if len(clusters) < 2:
        return []
    lines = []
    for blk in pdf_page.get_text("dict", clip=pymupdf.Rect(*area))["blocks"]:
        for ln in blk.get("lines", []):
            t = re.sub(r"\s+", " ", "".join(sp["text"] for sp in ln["spans"])).strip()
            if t and _centre_in(list(ln["bbox"]), area):
                lines.append((t, list(ln["bbox"])))
    names = {}
    for i, c in enumerate(clusters):
        mid = (c[1] + c[3]) / 2
        under = [(b[3], t, b) for t, b in lines
                 if c[0] - 10 <= (b[0] + b[2]) / 2 <= c[2] + 10 and (b[1] + b[3]) / 2 >= mid]
        if not under:
            return []
        _y, t, b = max(under)
        if len(t.split()) > 3 or len(t) > 30 or t.endswith("."):
            return []
        names[i] = (t, b)
    texts = [t for t, _b in names.values()]
    bases = [b[3] for _t, b in names.values()]
    if len(set(texts)) != len(texts) or max(bases) - min(bases) > 20:
        return []
    boxes = {i: list(c) for i, c in enumerate(clusters)}
    for i, (_t, b) in names.items():
        boxes[i] = _union(boxes[i], b)
    named = {id(b) for _t, b in names.values()}
    for t, b in lines:
        if id(b) in named:
            continue
        j = min(boxes, key=lambda i: _box_gap(boxes[i], b))
        boxes[j] = _union(boxes[j], b)
    # Reading order: rows by vertical overlap, left to right within a row -- Spirilla's flagella
    # reach higher than its neighbours, and rounding tops into bands sorted it first.
    rows = []
    for i in sorted(boxes, key=lambda i: boxes[i][1]):
        y0, y1 = boxes[i][1], boxes[i][3]
        row = next((r for r in rows if min(y1, r["y1"]) - max(y0, r["y0"]) > 0), None)
        if row is None:
            rows.append({"y0": y0, "y1": y1, "ids": [i]})
        else:
            row["ids"].append(i)
            row["y0"], row["y1"] = min(row["y0"], y0), max(row["y1"], y1)
    order = [i for r in rows for i in sorted(r["ids"], key=lambda i: boxes[i][0])]
    panels = [{"label": names[i][0], "key": "abcdefghijklmnop"[k],
               "bbox_pt": [round(v, 1) for v in boxes[i]]} for k, i in enumerate(order)]
    for k, a in enumerate(panels):
        for b in panels[k + 1:]:
            ix = min(a["bbox_pt"][2], b["bbox_pt"][2]) - max(a["bbox_pt"][0], b["bbox_pt"][0])
            iy = min(a["bbox_pt"][3], b["bbox_pt"][3]) - max(a["bbox_pt"][1], b["bbox_pt"][1])
            if ix > 3 and iy > 3:
                return []
    return panels


def _union(a, b):
    return [min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3])]


def _panels_from_pdf(pdf_page, box, pw, ph):
    """The lettered panels of the figure at `box`, measured off the PDF page itself.

    Pieces are the page's image blocks and visible vector paths inside the box, each clipped to
    it -- never the watermark (an image AND a mask path the size of a third of the page, which
    otherwise fused every panel of Figure 3.2 into one) and never a full-page ground.
    """
    import pymupdf
    import book_design
    from extract_page_layout import visible_drawings
    pad = 2.0
    area = [box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad]
    letters = []
    # The bottom row's letters are printed UNDER its pictures and can fall just past the measured
    # box: Figure 1.9's `(c)` (BIO12L ch01 p012) sits 4pt below it, so (b) took the Commelina
    # plant as well as the sunflower. Letters are looked for 14pt below the box.
    below = [area[0], area[1], area[2], area[3] + 14]
    # The page's words read once (`_page_read`), kept where they touch the search box -- the
    # same set a clipped read gave, so the one-word-line test below is unchanged.
    words = [w for w in _page_read(pdf_page, "words")
             if w[2] > below[0] and w[0] < below[2] and w[3] > below[1] and w[1] < below[3]]
    # A panel letter stands ALONE on its line. Figure 1.8's box (BIO12L ch01 p010) takes in its
    # caption, `(a) Parts of the ovule ... (b) 2, 4, and 8-nucleate ... (c) A diagrammatic`,
    # whose letters then competed with the ones printed under the pictures.
    per_line = collections.Counter((w[5], w[6]) for w in words)
    for w in words:
        m = _PANEL_LETTER.match(w[4].strip())
        if m and _centre_in(list(w[:4]), below) and per_line[(w[5], w[6])] == 1:
            letters.append((m.group(1), list(w[:4])))
    if len({l for l, _ in letters}) < 2:
        return _named_panels_from_pdf(pdf_page, area, pw, ph)

    def usable(b):
        frac = (b[0] / pw, b[1] / ph, b[2] / pw, b[3] / ph)
        if book_design.is_watermark(frac) or (b[2] - b[0]) >= 0.9 * pw:
            return None
        c = [max(b[0], area[0]), max(b[1], area[1]), min(b[2], area[2]), min(b[3], area[3])]
        if c[2] - c[0] <= 0 or c[3] - c[1] <= 0 or not _centre_in(b, area):
            return None
        return c

    pieces = [c for info in _page_read(pdf_page, "images") for c in [usable(list(info["bbox"]))] if c]
    for d in visible_drawings(pdf_page):
        r = d["rect"]
        c = usable([r.x0, r.y0, r.x1, r.y1])
        if c:
            pieces.append(c)
    # THE PANEL'S OWN TEXT LABELS ARE PART OF IT. `Sheath` beside the bacteriophage and `Main
    # axis` beside the moss are printed words, joined to their drawing by leader lines; without
    # them a panel crop cut each word in half at the drawing's edge. A label lying between two
    # panels then makes them overlap, and the figure stays whole -- the safe outcome.
    # Lines are read WHOLE, not clipped to the box, and a label lies mostly inside it: clipped,
    # the prose line `(ii) Geitonogamy - Transfer of pollen ...` beside Figure 1.9 (BIO12L ch01
    # p012) shrank to the `(ii)` inside the box's edge, passed as a label, and joined panel (c),
    # which then overlapped (b) and the split was refused.
    for blk in _page_read(pdf_page, "dict")["blocks"]:
        for ln in blk.get("lines", []):
            t = "".join(sp["text"] for sp in ln["spans"]).strip()
            b = list(ln["bbox"])
            if t and not _PANEL_LETTER.match(t) and _centre_in(b, area) and _inside(b, area, 0.6):
                pieces.append(b)
    # ONE EMBEDDED PICTURE PER PRINTED LETTER: each picture is its own panel. Clustering fused
    # Figure 2.4's (b) Euglena and (c) slime mould (BIO11L ch02 p015), whose image rectangles
    # overlap by 2pt of transparent margin, so three groups met four letters and the figure
    # shipped as one crop. The other pieces (labels, leader lines) still cluster and join the
    # nearest letter; a split that makes two panels overlap is still refused.
    images = [c for info in _page_read(pdf_page, "images") for c in [usable(list(info["bbox"]))] if c]
    n_letters = len({l for l, _ in letters})
    if len(images) == n_letters:
        rest = [b for b in pieces if b not in images]
        groups = [(g, []) for g in images] + [(g, []) for g in _cluster_boxes(rest, gap=3.0, min_pt=6.0)]
        panels = _find_panels(groups, letters)
        if panels:
            return panels
    # 6pt, not 12: a panel letter DRAWN as paths is ~9pt -- Figure 3.3's `(a)` (BIO11L ch03
    # p009) is three filled shapes, and at 12pt it was dropped as noise, so the Selaginella
    # panel was cut without its letter.
    groups = [(g, []) for g in _cluster_boxes(pieces, gap=3.0, min_pt=6.0)]
    return _find_panels(groups, letters)


def _find_panels(groups, letter_boxes):
    """[{label, bbox_pt}] -- one entry per lettered panel the book prints, or [].

    ONE FIGURE, SEVERAL PICTURES. Figure 2.5 prints (a) Mucor, (b) Aspergillus, (c) Agaricus
    as three pictures under one caption (BIO11L ch02 p017). The figure stays ONE node -- the
    caption names all three -- but each picture is its own panel with its own crop, so a
    product can show or cite `Figure 2.5 (b)` alone, and each gets its own CDN link.

    A panel is what the BOOK labels: the printed letters `(a)`, `(b)` ... decide how many there
    are. NCERT sets each letter UNDER its picture, so a letter first claims the piece it sits
    just beneath; nearest-edge alone gave Figure 2.5's `(b)` to panel (c), whose top is 1pt
    from it. Every other piece then joins the letter it is nearest to. Nothing is returned --
    the figure stays one picture -- unless at least two letters are printed, each claimed a
    piece, and no two panels overlap. A guessed split is worse than none.
    """
    letters = {}
    for letter, box in letter_boxes:
        letters.setdefault(letter, box)
    if len(letters) < 2 or len(groups) < len(letters):
        return []

    # "Just beneath" means within 40pt: Figure 3.3's `(d)` (BIO11L ch03 p009) lies 224pt under
    # the Equisetum and, scored as "beneath" it, took (b)'s picture before (b) could.
    def under(g, lb):
        cx = (lb[0] + lb[2]) / 2
        if g[0] - 10 <= cx <= g[2] + 10 and g[3] - 6 <= lb[1] <= g[3] + 40:
            return abs(lb[1] - g[3])
        return 1000 + _box_gap(g, lb)

    owner = {}
    cands = sorted((under(g, lb), i, l) for i, (g, _ls) in enumerate(groups)
                   for l, lb in letters.items())
    claimed = set()
    for score, i, l in cands:
        if l in claimed or i in owner:
            continue
        owner[i] = l
        claimed.add(l)
    if len(claimed) < len(letters):
        return []
    # ONE LETTER DRAWN INTO THE ARTWORK. Figure 3.3 (BIO11L ch03 p009) prints `(b)` `(c)` `(d)`
    # as text but its `(a)` is part of the Selaginella drawing, so four pictures met three
    # letters. When exactly one letter of the run a..last is absent and exactly one picture-
    # sized piece is left unclaimed, that piece is the absent panel; anything less certain
    # still leaves the figure whole.
    def area(b):
        return (b[2] - b[0]) * (b[3] - b[1])
    absent = [chr(c) for c in range(ord("a"), ord(max(letters)) + 1) if chr(c) not in letters]
    smallest = min(area(groups[i][0]) for i in owner)
    big = [i for i, (g, _ls) in enumerate(groups) if i not in owner and area(g) >= 0.25 * smallest]
    if len(absent) == 1 and len(big) == 1:
        owner[big[0]] = absent[0]
        letters[absent[0]] = groups[big[0]][0]
    # A leftover piece joins the PICTURE it lies against, or a letter if one is nearer.
    # Nearest-letter alone gave Figure 3.2's `Antheridial branch` (BIO11L ch03 p006), printed
    # on panel (d)'s moss, to the `(b)` 26pt above it; (b) then reached into (d) and the
    # overlap refusal kept the whole figure as one picture.
    seeds = dict(owner)
    for i, (g, _ls) in enumerate(groups):
        if i not in owner:
            near = [(_box_gap(g, groups[j][0]), seeds[j]) for j in seeds]
            near += [(_box_gap(g, letters[l]), l) for l in letters]
            owner[i] = min(near)[1]
    panels = []
    for l in sorted(letters):
        bs = [groups[i][0] for i in owner if owner[i] == l] + [letters[l]]
        panels.append({"label": f"({l})",
                       "bbox_pt": [round(min(b[0] for b in bs), 1), round(min(b[1] for b in bs), 1),
                                   round(max(b[2] for b in bs), 1), round(max(b[3] for b in bs), 1)]})
    # A THIN OVERLAP IS A SHARED MARGIN, NOT A SHARED PICTURE. Figure 4.22's chameleon image
    # runs to x 179 and the crocodile's starts at 173 (BIO11L ch04 p049): 6pt of transparent
    # margin, and refusing every overlap > 3pt shipped all four reptiles as ONE crop (also Figure
    # 4.20, 8pt). Side-by-side or stacked panels whose overlap is under a fifth of the narrower
    # one part at its middle, as `cut_figures` parts overlapping crops; a real overlap still
    # leaves the figure whole.
    for _ in range(2):
        for i, a in enumerate(panels):
            for b in panels[i + 1:]:
                A, B = a["bbox_pt"], b["bbox_pt"]
                ix = min(A[2], B[2]) - max(A[0], B[0])
                iy = min(A[3], B[3]) - max(A[1], B[1])
                if ix <= 3 or iy <= 3:
                    continue
                left, right = (A, B) if A[0] <= B[0] else (B, A)
                top, bot = (A, B) if A[1] <= B[1] else (B, A)
                if (right[0] > left[0] and right[2] > left[2]
                        and ix < 0.2 * min(A[2] - A[0], B[2] - B[0])):
                    mid = round((right[0] + left[2]) / 2, 1)
                    left[2], right[0] = mid, mid
                elif (bot[1] > top[1] and bot[3] > top[3]
                        and iy < 0.2 * min(A[3] - A[1], B[3] - B[1])):
                    mid = round((bot[1] + top[3]) / 2, 1)
                    top[3], bot[1] = mid, mid
    for i, a in enumerate(panels):
        for b in panels[i + 1:]:
            ix = min(a["bbox_pt"][2], b["bbox_pt"][2]) - max(a["bbox_pt"][0], b["bbox_pt"][0])
            iy = min(a["bbox_pt"][3], b["bbox_pt"][3]) - max(a["bbox_pt"][1], b["bbox_pt"][1])
            if ix > 3 and iy > 3:
                return []
    return panels


_CAPTION_MARK = re.compile(r"\(\s*([a-z]|[ivx]+)\s*\)")


def _caption_panel_rows(caption):
    """The panels a caption names, one row per letter: `(a) Green algae (i) Volvox (ii)
    Ulothrix (b) ...` -> [["a-i", "a-ii"], ["b-i", ...], ...]; a letter with no numerals is
    one panel, ["a"]. [] unless the letters run a, b, c ... from (a)."""
    rows = []
    for tok in _CAPTION_MARK.findall(caption or ""):
        if re.fullmatch(r"[ivx]+", tok) and rows:
            rows[-1][1].append(tok)
        elif re.fullmatch(r"[a-h]", tok):
            rows.append((tok, []))
    if [l for l, _ in rows] != [chr(ord("a") + k) for k in range(len(rows))]:
        return []
    return [[f"{l}-{r}" for r in subs] or [l] for l, subs in rows]


def _raster_ink_components(pix, dilate):
    """(labels, [(ink, [x0, y0, x1, y1])] per component) of a picture's ink, in pixels."""
    import numpy as np
    from scipy import ndimage
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    ink = a[:, :, :3].min(axis=2) < 215
    lab, n = ndimage.label(ndimage.binary_dilation(ink, iterations=dilate))
    sums = ndimage.sum(ink, lab, range(1, n + 1))
    return lab, [(float(sums[i]), [o[1].start, o[0].start, o[1].stop, o[0].stop])
                 for i, o in enumerate(ndimage.find_objects(lab))]


def _rgb_pixmap(doc, xref):
    import pymupdf
    pix = pymupdf.Pixmap(doc, xref)
    if pix.n - pix.alpha != 3:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    return pix


def _panels_from_raster(pdf_page, box, pw, ph, caption):
    """The panels of a figure printed as ONE scanned picture, split on its white space.

    Figure 3.1 (BIO11L ch03 p003) is a single 886x1189 image holding seven drawings, its
    `(a-i)` ... `(c-ii)` letters painted into the pixels: the text layer has nothing to split
    on. The caption says what the book prints -- (a) i, ii; (b) i, ii, iii; (c) i, ii -- so the
    picture's ink is split into separate drawings, and the split is taken ONLY when the drawings
    fall into exactly those rows: the same number of rows, the same count in each, read top to
    bottom and left to right. Anything else leaves the figure whole.

    Each panel records its drawing's pixel pieces (`raster`), because neighbouring drawings'
    boxes can overlap (Fucus's label reaches between Polysiphonia's branches): `cut_figures`
    cuts each from the picture itself, keeping only its own pieces.
    """
    import book_design
    rows_want = _caption_panel_rows(caption)
    if sum(len(r) for r in rows_want) < 2:
        return []
    area = (box[2] - box[0]) * (box[3] - box[1])
    pics = []
    for info in _page_read(pdf_page, "images_x"):
        b = list(info["bbox"])
        if book_design.is_watermark((b[0] / pw, b[1] / ph, b[2] / pw, b[3] / ph)) \
                or (b[2] - b[0]) >= 0.9 * pw or not _inside(b, box, 0.9):
            continue
        if (b[2] - b[0]) * (b[3] - b[1]) >= 0.6 * area:
            pics.append(info)
    if len(pics) != 1 or not pics[0].get("xref"):
        return []
    info = pics[0]
    t = info.get("transform") or (1, 0, 0, 1, 0, 0)
    if abs(t[1]) > 1e-6 or abs(t[2]) > 1e-6 or t[0] <= 0 or t[3] <= 0:
        return []                       # rotated or flipped: pixel and page axes differ
    pix = _rgb_pixmap(pdf_page.parent, info["xref"])
    bx = info["bbox"]
    sx, sy = (bx[2] - bx[0]) / pix.width, (bx[3] - bx[1]) / pix.height
    import numpy as np
    from scipy import ndimage
    for dilate in (6, 10, 14, 20, 28):
        lab, comps = _raster_ink_components(pix, dilate)
        total = sum(c[0] for c in comps) or 1
        big_ids = [i for i, c in enumerate(comps) if c[0] >= 0.02 * total]
        if len(big_ids) != sum(len(r) for r in rows_want):
            continue
        big = [comps[i][1] for i in big_ids]
        parts = {k: [b] for k, b in enumerate(big)}
        # A loose piece (a painted letter, a label) joins the drawing whose INK is nearest, not
        # whose box is: Figure 3.1's `(b-iii)` sits under Dictyota's stipe but inside the box
        # of Polysiphonia's spreading branches, and went to (c-ii) by box distance.
        dist = [ndimage.distance_transform_edt(lab != i + 1) for i in big_ids]
        for i, (ink, b) in enumerate(comps):
            if i not in big_ids:
                here = lab == i + 1
                parts[min(range(len(big)), key=lambda k: float(dist[k][here].min()))].append(b)
        boxes = {k: [min(p[0] for p in ps), min(p[1] for p in ps),
                     max(p[2] for p in ps), max(p[3] for p in ps)] for k, ps in parts.items()}
        order = sorted(boxes, key=lambda k: (boxes[k][1] + boxes[k][3]) / 2)
        rows, last = [], None
        for k in order:
            cy = (boxes[k][1] + boxes[k][3]) / 2
            if last is None or cy - last > 0.1 * pix.height:
                rows.append([])
            rows[-1].append(k)
            last = cy
        if [len(r) for r in rows] != [len(r) for r in rows_want]:
            continue
        panels = []
        for got, want in zip(rows, rows_want):
            for k, key in zip(sorted(got, key=lambda k: boxes[k][0]), want):
                x0, y0, x1, y1 = boxes[k]
                panels.append({"label": f"({key})", "key": key,
                               "bbox_pt": [round(bx[0] + x0 * sx, 1), round(bx[1] + y0 * sy, 1),
                                           round(bx[0] + x1 * sx, 1), round(bx[1] + y1 * sy, 1)],
                               "raster": {"xref": info["xref"], "dilate": dilate,
                                          "box_px": boxes[k], "parts_px": parts[k]}})
        return panels
    return []


def raster_panel_image(doc, raster):
    """One raster panel as an RGBA picture: its own drawing's pixels, everything else clear."""
    import numpy as np
    from PIL import Image
    pix = _rgb_pixmap(doc, raster["xref"])
    lab, comps = _raster_ink_components(pix, raster["dilate"])
    mine = [i + 1 for i, (_ink, b) in enumerate(comps) if b in raster["parts_px"]]
    rgb = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3]
    alpha = np.where(np.isin(lab, mine), 255, 0).astype(np.uint8)
    x0, y0, x1, y1 = raster["box_px"]
    return Image.fromarray(np.dstack([rgb, alpha])[y0:y1, x0:x1], "RGBA")


def _vector_ink(pdf_page, area, pw, ph):
    """Boxes of the PDF's own vector drawings standing inside `area` -- measured ink."""
    from extract_page_layout import path_rects
    out = []
    # The page's shared read (see `extract_page_layout.visible_drawings`): a second walk of
    # BIO12L ch01 p014's 1.83 million paths cost four more minutes.
    for r in path_rects(pdf_page):
        if r.width > 0.9 * pw or r.height > 0.9 * ph:
            continue
        b = [r.x0, r.y0, r.x1, r.y1]
        if _centre_in(b, area) and _inside(b, area, 0.6 if r.width * r.height > 1 else 0.0):
            out.append(b)
    return out


def _element_from_spans(pdf_page, area, page):
    """A text element built from the PDF spans inside `area`, or None."""
    if pdf_page is None:
        return None
    import pymupdf
    lines = []
    for b in pdf_page.get_text("dict", clip=pymupdf.Rect(*area))["blocks"]:
        for ln in b.get("lines", []):
            t = "".join(sp["text"] for sp in ln["spans"]).strip()
            if t and _centre_in(list(ln["bbox"]), area):
                lines.append({"bbox_pt": list(ln["bbox"]), "text": t,
                              "size": ln["spans"][0]["size"], "font": ln["spans"][0]["font"]})
    if not lines:
        return None
    text = " ".join(ln["text"] for ln in lines)
    el = {"role": "paragraph", "text": text, "column": "body", "size_rel": 1.0,
          "runs": [{"t": text, "b": False, "i": False, "sc": False, "script": None,
                    "color": "#231f20", "size": lines[0]["size"], "font": lines[0]["font"]}],
          "rebuilt_from": "pdf-spans"}
    _set_union_geometry(el, [{"bbox_pt": ln["bbox_pt"]} for ln in lines], page)
    el["line_count"] = len({round(ln["bbox_pt"][3]) for ln in lines})
    el["line_boxes_pt"] = [{"bbox_pt": ln["bbox_pt"], "text": ln["text"]} for ln in lines]
    return el


def _release_from_figures(els, eq, page):
    """Pull any figure's box back off `eq`, and drop `eq`'s text from its absorbed labels."""
    eb = eq["bbox_pt"]
    key = _norm(eq["text"])
    for f in els:
        if f is eq or f["role"] != "figure" or not _inside(eb, f["bbox_pt"], 0.3):
            continue
        fb = list(f["bbox_pt"])
        if (eb[1] + eb[3]) / 2 > (fb[1] + fb[3]) / 2:
            fb[3] = min(fb[3], eb[1] - 2)          # formula under the diagram
        else:
            fb[1] = max(fb[1], eb[3] + 2)
        if fb[3] - fb[1] > 24:
            _set_union_geometry(f, [{"bbox_pt": fb}], page)
            f.pop("line_count", None)
            f.pop("line_boxes_pt", None)
        f["absorbed_labels"] = [t for t in f.get("absorbed_labels") or [] if _norm(t) != key]


def _slice_runs(runs, a, b):
    """The runs covering characters [a, b) of their concatenated text."""
    out, pos = [], 0
    for r in runs or []:
        t = r.get("t") or ""
        lo, hi = max(a, pos), min(b, pos + len(t))
        if lo < hi:
            out.append(dict(r, t=t[lo - pos:hi - pos]))
        pos += len(t)
    return out


_NUM_LABEL = re.compile(r"^\(?\d{1,2}(?:\.\d{1,2})*[.)]?$")


def repair_cross_column_blocks(layout):
    """Split a PDF block whose lines stand in two different columns, and give each stray line
    back to the block it belongs to.

    PyMuPDF groups lines into blocks by proximity, and on a page with a narrow rail beside the
    measure a line of the rail can join a block of the body. Measured on BIO11L ch05:

      * p002 -- the portrait's name line `Katherine Esau` (x 119-199) sat INSIDE the
        biography's last paragraph (x 258-552), so the caption was lost and the paragraph's box
        was widened across the photograph;
      * p013 -- the last line of the floral-symbols paragraph (x 72-344) joined Figure 5.16's
        caption (x 356-518), so the caption's box ran across the paragraph and the caption's
        own second line, `floral formula`, was left behind as a stray box.

    Lines whose horizontal spans do not overlap are not one block. The block keeps the group
    holding most of its text; each other group becomes its own element, which then joins a
    block directly above or below it in ITS column, or stands alone. Text and runs are cut by
    character offset, so formatting stays on the words it belongs to.
    """
    stats = {"blocks_split": 0, "lines_moved": 0, "rejoined": 0}
    for page in layout["pages"]:
        els = page["elements_in_reading_order"]
        new = []
        for e in els:
            lines = e.get("line_boxes_pt") or []
            if e["role"] not in _TEXT_ROLES or len(lines) < 2:
                continue
            # One group = lines that overlap horizontally OR share a baseline. The second clause
            # matters: a heading's number and title (`5.1.1` | `Regions of the Root`), a
            # caption's bold label and its text, an exercise's `9.` and its question are
            # separate line records side by side, and splitting them made 25 stray boxes.
            # A bare number beside its line is held by ROW, not baseline: BIO11L ch10 p010's `4.`
            # ends at y 698.7 and `What is G0 (quiescent phase)...` at 701.3 -- the subscript
            # drops the line's bottom 2.6pt -- so the number was cut off, glued onto question 3,
            # and questions 4-16 lost their run.
            def together(a, b, ta="", tb=""):
                if (min(a[2], b[2]) - max(a[0], b[0]) > 0) or abs(a[3] - b[3]) <= 2.5:
                    return True
                if _NUM_LABEL.match(ta) or _NUM_LABEL.match(tb):
                    return min(a[3], b[3]) - max(a[1], b[1]) >= 0.5 * min(a[3] - a[1], b[3] - b[1])
                return False
            groups = []
            for ln in lines:
                hit = [g for g in groups if any(together(ln["bbox_pt"], o["bbox_pt"],
                                                         (ln.get("text") or "").strip(),
                                                         (o.get("text") or "").strip())
                                                for o in g)]
                merged = [ln] + [x for g in hit for x in g]
                groups = [g for g in groups if not any(g is h for h in hit)] + [merged]
            if len(groups) < 2:
                continue
            groups.sort(key=lambda g: -sum(len(ln.get("text") or "") for ln in g))
            text = e.get("text") or ""
            cut = []
            for g in groups[1:]:
                piece = " ".join((ln.get("text") or "").strip() for ln in g)
                at = text.find(piece)
                if not piece or at < 0:
                    cut = None
                    break
                cut.append((at, at + len(piece), g, piece))
            if not cut:
                continue
            for at, end, g, piece in sorted(cut, key=lambda c: -c[0]):
                stray = {"role": "side_note", "text": piece, "column": e.get("column"),
                         "size_rel": e.get("size_rel", 1.0),
                         "runs": _slice_runs(e.get("runs"), at, end) or [],
                         "split_from_block": True}
                _set_union_geometry(stray, [{"bbox_pt": ln["bbox_pt"]} for ln in g], page)
                stray["line_count"] = len(g)
                stray["line_boxes_pt"] = list(g)
                new.append(stray)
                e["runs"] = _slice_runs(e.get("runs"), 0, at) + _slice_runs(
                    e.get("runs"), end, len(text))
                text = (text[:at].rstrip() + " " + text[end:].lstrip()).strip()
                stats["lines_moved"] += len(g)
            e["text"] = text
            main = groups[0]
            _set_union_geometry(e, [{"bbox_pt": ln["bbox_pt"]} for ln in main], page)
            e["line_count"] = len({round(ln["bbox_pt"][3]) for ln in main})
            e["line_boxes_pt"] = sorted(main, key=lambda ln: ln["bbox_pt"][3])
            stats["blocks_split"] += 1
        # Each stray joins a neighbour in its own column: a block it continues (just below it)
        # or one it heads (just above it).
        for st in new:
            sb = st["bbox_pt"]
            best = None
            for o in els + [x for x in new if x is not st]:
                if o is st or o["role"] not in _TEXT_ROLES or o.get("_merged"):
                    continue
                ob = o["bbox_pt"]
                w = min(sb[2], ob[2]) - max(sb[0], ob[0])
                if w < 0.5 * (sb[2] - sb[0]):
                    continue
                gap = max(sb[1] - ob[3], ob[1] - sb[3])
                if -2 <= gap < 8 and (best is None or gap < best[0]):
                    best = (gap, o)
            if best is None:
                els.append(st)
                continue
            o = best[1]
            first, second = (o, st) if sb[1] >= o["bbox_pt"][1] else (st, o)
            joint = [dict((first.get("runs") or [{}])[-1], t=" ")] if first.get("runs") else []
            o["runs"] = (first.get("runs") or []) + joint + (second.get("runs") or [])
            o["text"] = ((first.get("text") or "") + " " + (second.get("text") or "")).strip()
            lines = (o.get("line_boxes_pt") or []) + st["line_boxes_pt"]
            _set_union_geometry(o, [{"bbox_pt": ln["bbox_pt"]} for ln in lines], page)
            o["line_count"] = len({round(ln["bbox_pt"][3]) for ln in lines})
            o["line_boxes_pt"] = sorted(lines, key=lambda ln: ln["bbox_pt"][3])
            st["_merged"] = True
            stats["rejoined"] += 1
        for st in new:
            st.pop("_merged", None)
    return stats


def _is_sliver(box):
    """An image strip in the bleed, a few points wide, is page edge art and never a figure.
    Measured on BIO11L ch05 p003: an image at x -9..1pt, clipped to a 1pt strip down the left
    edge, came out as a figure that `BOX_OUT_OF_PAGE` failed."""
    return box[2] - box[0] < 4.0 or box[3] - box[1] < 4.0


def _panels_from_hints(pdf_page, hints, pw, ph):
    """Panels where A2 boxed each one (see `_merge_panel_runs`): A2 decides MEMBERSHIP, the PDF
    the geometry. Each panel is the union of the measured ink -- pictures, drawn paths, label
    lines -- whose centre lies in its A2 box, cut to that box. A picture with a transparent
    margin (Figure 1.14 (b) is placed 226 -> 595pt, past the page edge) is cut to its panel.
    Lettered (a), (b) ... in A2's reading order; [] if any panel is empty or two overlap."""
    import pymupdf
    import book_design
    from extract_page_layout import visible_drawings

    def ok(b):
        return not (book_design.is_watermark((b[0] / pw, b[1] / ph, b[2] / pw, b[3] / ph))
                    or (b[2] - b[0]) >= 0.9 * pw)
    ink = [list(i["bbox"]) for i in _page_read(pdf_page, "images") if ok(list(i["bbox"]))]
    ink += [[d["rect"].x0, d["rect"].y0, d["rect"].x1, d["rect"].y1]
            for d in visible_drawings(pdf_page) if ok([d["rect"].x0, d["rect"].y0,
                                                       d["rect"].x1, d["rect"].y1])]
    ink += [list(ln["bbox"]) for blk in _page_read(pdf_page, "dict")["blocks"]
            for ln in blk.get("lines", []) if "".join(s["text"] for s in ln["spans"]).strip()]
    panels = []
    for k, h in enumerate(hints):
        area = [max(0, h[0] - 4), max(0, h[1] - 4), min(pw, h[2] + 4), min(ph, h[3] + 4)]
        bs = [[max(b[0], area[0]), max(b[1], area[1]), min(b[2], area[2]), min(b[3], area[3])]
              for b in ink if _centre_in(b, area)]
        bs = [b for b in bs if b[2] > b[0] and b[3] > b[1]]
        if not bs:
            return []
        panels.append({"label": f"({chr(ord('a') + k)})",
                       "bbox_pt": [round(min(b[0] for b in bs), 1), round(min(b[1] for b in bs), 1),
                                   round(max(b[2] for b in bs), 1), round(max(b[3] for b in bs), 1)]})
    for i, a in enumerate(panels):
        for b in panels[i + 1:]:
            ix = min(a["bbox_pt"][2], b["bbox_pt"][2]) - max(a["bbox_pt"][0], b["bbox_pt"][0])
            iy = min(a["bbox_pt"][3], b["bbox_pt"][3]) - max(a["bbox_pt"][1], b["bbox_pt"][1])
            if ix > 3 and iy > 3:
                return []
    return panels


def _grow_to_drawn(box, small, others, captions, page_size=None):
    """`box` grown over small drawn shapes within 6pt of it, repeatedly (see the call in
    `apply_agent_figures`). A shape inside another box in `others` is never taken, and the box
    never grows onto a caption it did not already touch: Figure 1.5's labels (BIO12L ch01 p007)
    widened its box onto the end of Figure 1.4's caption, and the captions of the two figures
    were then paired the wrong way round."""
    fb = list(box)
    touching = [c for c in captions if _box_gap(c, fb) <= 0]
    # Never page furniture: a folio tab or band bleeds to the trim, and growing over BIO12L
    # ch02 p010's tab put `35` into Figure 2.10's crop (the render printed `35 35`).
    pw_, ph_ = page_size if page_size else (1e9, 1e9)
    small = [r for r in small if r[0] > 2 and r[1] > 2 and r[2] < pw_ - 2 and r[3] < ph_ - 2]
    grown = True
    while grown:
        grown = False
        for r in small:
            if r[0] >= fb[0] and r[2] <= fb[2] and r[1] >= fb[1] and r[3] <= fb[3]:
                continue
            if _box_gap(r, fb) > 6 or any(_box_gap(r, o) <= 0 for o in others):
                continue
            nb = [min(fb[0], r[0]), min(fb[1], r[1]), max(fb[2], r[2]), max(fb[3], r[3])]
            if any(_box_gap(nb, c) <= 0 for c in captions if c not in touching):
                continue
            fb, grown = nb, True
    return fb


def _merge_panel_runs(blocks):
    """A2 blocks with each run of PANEL boxes of one figure made one figure box.

    A2 normally boxes a whole figure; on BIO12L ch01 p019 and p021 it boxed Figure 1.14 (a) and
    (b), and Figure 1.15 (a) and (b), separately -- two figure blocks, then the one caption. Each
    became a figure of its own, the caption paired with one of them, and the other shipped as
    an unnumbered figure whose crop overlapped its sibling's, so labels printed twice. A run of
    figure blocks is one figure only when the block right after it is a caption naming exactly
    as many lettered panels as the run has boxes; across every A2 read on disk only those two
    pages match. The merged box is split back into its panels by `_panels_from_pdf`.
    """
    out, i = [], 0
    while i < len(blocks):
        j = i
        while (blocks[i].get("kind") == "figure" and j + 1 < len(blocks)
               and blocks[j + 1].get("kind") == "figure"):
            j += 1
        nxt = blocks[j + 1] if j + 1 < len(blocks) else {}
        text = (nxt.get("text") or "").strip()
        letters = set(re.findall(r"\(([a-h])\)", text))
        run = blocks[i:j + 1]
        if (j > i and re.match(r"(Figure|Fig\.)\s*\d+\.\d+", text)
                and len(letters) == len(run) and all(len(b.get("bbox") or []) == 4 for b in run)):
            bs = [b["bbox"] for b in run]
            out.append({**run[0], "bbox": [min(b[0] for b in bs), min(b[1] for b in bs),
                                           max(b[2] for b in bs), max(b[3] for b in bs)],
                        "merged_blocks": [b.get("n") for b in run], "panel_boxes": bs})
        else:
            out.extend(run)
        i = j + 1
    return out


def apply_agent_figures(layout, chapter, steps_dir="steps", pdf_path=None):
    """Make each figure A2 measured ONE element, with its printed labels absorbed into it.

    The extractor finds figures by clustering image blocks and drawing paths, and that goes
    wrong three ways on a diagram-heavy chapter -- measured on BIO11L ch05:

      * a figure SPLITS. Figure 5.12's five placentation diagrams came out as six figures and
        Figure 5.17's six panels as seven; only one of each could pair with the caption, and
        the rest reached the tree as unnumbered figures.
      * a vector figure is MISSED. Figure 5.1 is drawn, not embedded, so no element existed
        and its eleven labels (`Flower`, `Node`, `Primary root` ...) became paragraphs; the
        labels of Figure 5.15 and the panel letters `(a)`..`(f)` sat just outside their
        fragments and became twenty `box` nodes.
      * a figure is INVENTED. Hidden images under the Gynoecium paragraph on p011 clustered
        into a "figure" the page does not print, with the prose drawn over it.

    A2 read the page image and drew one box round each whole figure, labels included. That box
    is an ESTIMATE off a picture, so it only decides MEMBERSHIP: which fragments are one figure
    and which short text is its labels. The element's box stays the union of PDF-measured
    pieces -- fragments, label lines and, for a vector figure, the drawing paths -- so no
    agent-estimated coordinate becomes geometry (LESSONS 0.1).

    It runs BEFORE the text join. Run after it, the join had already claimed Figure 5.12's panel
    letters `(a)`..`(e)` as followers of its caption (the caption says `(a) Marginal ...`), and
    the merged caption box spanned the whole right column. Text A2 kept as a block of its own
    is never absorbed: the agent decided that was running text, and a loose figure box must not
    delete it.

    Each figure and equation element is also stamped with A2's block number, which is what
    `join_agent_special` matches A2S on; without it a page with two figures matched none.
    """
    stats = {"figures_merged": 0, "fragments_absorbed": 0, "labels_absorbed": 0,
             "vector_figures_built": 0, "equations_gathered": 0, "figures_dropped": 0}
    pdf = None
    pdf_path = pdf_path or layout.get("source_pdf")
    for pi, page in enumerate(layout["pages"], 1):
        path = best_a2_path(chapter, pi, steps_dir)
        if not path:
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                a2 = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        k = 72.0 / _A2_DPI
        merged = _merge_panel_runs(a2.get("blocks") or [])
        specials = [(b.get("kind"), b.get("n"), [v * k for v in b["bbox"]])
                    for b in merged
                    if b.get("kind") in ("figure", "equation")
                    and len(b.get("bbox") or []) == 4]
        hints = {b.get("n"): [[v * k for v in bb] for bb in b["panel_boxes"]]
                 for b in merged if b.get("panel_boxes")}
        kept_text = {_norm(b.get("text")) for b in (a2.get("blocks") or [])
                     if (b.get("text") or "").strip()}
        pw, ph = page["page_width_pt"], page["page_height_pt"]
        els = page["elements_in_reading_order"]
        gone = set()

        def pdf_page(_pi=pi):
            nonlocal pdf
            if pdf is None and pdf_path:
                import pymupdf
                pdf = pymupdf.open(pdf_path)
            return pdf[_pi - 1] if pdf is not None else None

        kept_all = " ".join(kept_text)

        def short_text(i, area):
            e = els[i]
            t = (e.get("text") or "").strip()
            if not (i not in gone and e["role"] not in _NOT_LABEL and e["role"] != "figure"
                    and e.get("a2_block_n") is None and t
                    and _norm(t) not in kept_text and _centre_in(e["bbox_pt"], area)):
                return False
            # A LONGER BLOCK WHOLLY INSIDE A2'S FIGURE BOX, WORDS A2 NEVER READ AS TEXT, IS THE
            # FIGURE'S. Figure 4.9's column heads (`Possibility I ... One long orange and short
            # green chromosome ...`, BIO12L ch04 p016) are one 150-character layer block, so the
            # length limit kept them as a paragraph printed over the artwork. A block holding any
            # prose A2 transcribed is never taken.
            return len(t) <= _LABEL_MAX or (_inside(e["bbox_pt"], area, 0.95)
                                            and _norm(t) not in kept_all)

        for kind, n, raw in specials:
            area = [raw[0] - 4, raw[1] - 4, raw[2] + 4, raw[3] + 4]
            if kind == "equation":
                parts = [i for i in range(len(els)) if short_text(i, area)]
                # A STACKED FRACTION'S GLYPHS ARE BIG, NOT HEADINGS. `rate = δP/δt` (BIO11L ch09
                # p113) sets `P`, `t` and `δ` large, so the extractor typed them section headings
                # and `short_text` skipped them: they became three empty sections and a loose
                # `rate = δ`. A fragment of <= 3 characters inside the equation's box is a part.
                parts += [i for i, e in enumerate(els)
                          if i not in parts and i not in gone and e["role"] == "section_heading"
                          and e.get("a2_block_n") is None
                          and 0 < len((e.get("text") or "").strip()) <= 3
                          and _centre_in(e["bbox_pt"], area)]
                parts.sort(key=lambda i: (els[i]["bbox_pt"][1], els[i]["bbox_pt"][0]))
                if not parts:
                    # `_absorb_figure_labels` reaches 14pt round a figure, so a formula set
                    # under its diagram is taken as a label -- Figure 5.16's floral formula on
                    # BIO11L ch05 p013 was, and its A2S transcription then had nowhere to land.
                    # Rebuild it from the PDF's own spans and pull the figure back off it.
                    eq = _element_from_spans(pdf_page(), area, page)
                    if eq is None:
                        # A FORMULA DRAWN AS PATHS has no text at all: the Lyases reaction
                        # (BIO11L ch09 p117) is vector art, so nothing was found and A2S's
                        # transcription had nowhere to land -- JSON and MD lost it and the page
                        # showed an empty tint box. An element at A2's measured box takes it.
                        eq = {"role": "paragraph", "text": "", "runs": [], "column": "body",
                              "size_rel": 1.0, "rebuilt_from": "a2-box"}
                        _set_union_geometry(eq, [{"bbox_pt": list(raw)}], page)
                    els.append(eq)
                    _release_from_figures(els, eq, page)
                    parts = [len(els) - 1]
                eq = els[parts[0]]
                _set_union_geometry(eq, [els[i] for i in parts], page)
                eq["text"] = " ".join((els[i].get("text") or "").strip() for i in parts)
                # The RUNS too: the node's body is built from them, so joining only the text
                # kept the first line and dropped the rest -- BIO11L ch09 p114 printed
                # `Glucose → 2 Pyruvic acid` without the `C6H12O6 + O2 → ...` line under it.
                if len(parts) > 1 and all(els[i].get("runs") for i in parts):
                    runs = []
                    for i in parts:
                        if runs:
                            runs.append(dict(runs[-1], t=" "))
                        runs += els[i]["runs"]
                    eq["runs"] = runs
                eq["role"] = "paragraph"
                eq["a2_block_n"] = n
                eq["a2_kind"] = "equation"
                gone.update(parts[1:])
                stats["equations_gathered"] += 1
                continue
            members = [i for i, e in enumerate(els) if i not in gone and e["role"] == "figure"
                       and not _is_sliver(e["bbox_pt"]) and _inside(e["bbox_pt"], area, 0.5)]
            labels = [i for i in range(len(els)) if short_text(i, area)]
            # THE PDF'S OWN PICTURES INSIDE A2'S BOX ARE PART OF THE FIGURE. The extractor's
            # fragment for Figure 4.20 (BIO11L ch04 p012) stopped at the seahorse's middle, so
            # the union of fragments cropped half a seahorse and half a fish. The embedded
            # images are measured, so taking them keeps the box a measurement (LESSONS 0.1).
            # NEVER THE WATERMARK: it is an image too, a third of the page, and lies inside a
            # big figure's box -- taking it stretched Figure 3.2 (BIO11L ch03 p006) up over the
            # prose above it, so the crop printed two lines of body text.
            import book_design
            pg = pdf_page()
            images = []
            if pg is not None:
                for info in _page_read(pg, "images"):
                    b = list(info["bbox"])
                    if (b[2] - b[0]) < 0.9 * pw and (b[3] - b[1]) < 0.9 * ph \
                            and not book_design.is_watermark((b[0] / pw, b[1] / ph,
                                                              b[2] / pw, b[3] / ph)) \
                            and _inside(b, area, 0.8):
                        images.append(b)
            # With the pictures measured, a fragment only HALF inside A2's box is not artwork to
            # take geometry from: Figure 4.20's reached x 457pt, across the gutter into the
            # prose. It is still absorbed (it is this figure's debris, not another figure), it
            # just does not widen the box. When EVERY fragment is loose the figure is rebuilt
            # from the pictures -- that fragment had swallowed the heading `4.2.11.3 Class --
            # Osteichthyes` as a "label", which is where its width came from.
            loose = []
            if images:
                loose = [i for i in members if not _inside(els[i]["bbox_pt"], area, 0.8)]
                members = [i for i in members if i not in loose]
            pieces = [els[i]["bbox_pt"] for i in members + labels] + images
            # PRINTED WORDS IN A2'S BOX THAT NO TEXT BLOCK HOLDS ARE THIS FIGURE'S LABELS. The
            # extractor can file a label under another cluster: `Central dogma` (BIO12L ch05
            # p082) went into a page-wide cluster's absorbed labels, so no element was left to
            # take, and the rebuilt figure's crop cut the label in half.
            if pg is not None:
                import pymupdf
                held = [e["bbox_pt"] for j, e in enumerate(els) if j not in gone and j not in labels
                        and e["role"] != "figure" and (e.get("text") or "").strip()
                        and e.get("bbox_pt")]
                pieces += [list(w[:4]) for w in pg.get_text("words", clip=pymupdf.Rect(*raw))
                           if _inside(list(w[:4]), raw, 0.9)
                           and not any(_centre_in(list(w[:4]), t) for t in held)]
            if loose and pg is not None:
                # A loose fragment's DRAWN artwork goes with it unless taken back here: Figure
                # 1.14 (a) (BIO12L ch01 p019) is vector paths, the fragment holding it ran off the
                # page, and the figure rebuilt from images alone lost the whole of panel (a).
                pieces += [b for b in _vector_ink(pg, area, pw, ph)
                           if not book_design.is_watermark((b[0] / pw, b[1] / ph,
                                                            b[2] / pw, b[3] / ph))
                           # nor page furniture: a tab or band bleeds to the trim
                           and b[0] > 2 and b[1] > 2 and b[2] < pw - 2 and b[3] < ph - 2]
            gone.update(loose)
            loose_labels = [t for i in loose for t in (els[i].get("absorbed_labels") or [])]
            if members:
                fig = els[members[0]]
            elif loose and images:
                fig = {"role": "figure", "runs": [], "text": "", "column": "body",
                       "size_rel": 1.0, "figure_box_src": "a2-membership+pdf-images"}
                els.append(fig)
                # The loose fragment's labels go with it; their printed words, measured off the
                # page inside A2's box, keep `(a)` `(b)` under the pictures inside the crop.
                import pymupdf
                # A word inside a text block still on the page is that block's -- the caption
                # under Figure 4.20 also prints `(a)` and `(b)`.
                want = {w for t in loose_labels for w in t.split()}
                texts = [e["bbox_pt"] for j, e in enumerate(els) if j not in gone
                         and e["role"] in _TEXT_ROLES and e.get("bbox_pt")]
                pieces += [list(w[:4]) for w in pg.get_text("words", clip=pymupdf.Rect(*area))
                           if w[4] in want and _centre_in(list(w[:4]), area)
                           and not any(_centre_in(list(w[:4]), t) for t in texts)]
            else:
                # A FIGURE WITH NO FRAGMENT AND NO LABEL IS STILL A FIGURE. Figure 4.1(a)'s
                # starfish (BIO11L ch04 p002) is drawn, unlabelled, and the extractor made no
                # element for it; returning here on "no members, no labels" left its caption to
                # pair with the crab below it, and every caption on the page slid one down.
                ink = _vector_ink(pg, area, pw, ph) if pg is not None else []
                if not ink and not pieces:
                    continue            # nothing measured to build a box from
                pieces += ink
                fig = {"role": "figure", "runs": [], "text": "", "column": "body",
                       "size_rel": 1.0, "figure_box_src": "a2-membership+vector-ink"}
                els.append(fig)
                stats["vector_figures_built"] += 1
            _set_union_geometry(fig, [{"bbox_pt": b} for b in pieces], page)
            # THE FIGURE'S OWN INK INSIDE A2'S BOX: the PDF's paths, never one crossing a printed
            # text LINE (prose, a caption and its tint), never page furniture (watermark, a shape
            # touching the trim) or another figure's ink. Read lazily -- a dense page is 160,000
            # paths -- and only for a figure the measurement left short of A2's box.
            _ink = []

            def own_ink():
                if not _ink:
                    lines = [ln["bbox"] for blk in _page_read(pg, "dict")["blocks"]
                             for ln in blk.get("lines", [])
                             if "".join(s["text"] for s in ln["spans"]).strip()]
                    others = [e["bbox_pt"] for j, e in enumerate(els)
                              if e["role"] == "figure" and e is not fig and j not in gone
                              and j not in members]

                    import numpy as np
                    cand = [b for b in _vector_ink(pg, area, pw, ph)
                            if b[0] > 2 and b[1] > 2 and b[2] < pw - 2 and b[3] < ph - 2
                            and not book_design.is_watermark(
                                (b[0] / pw, b[1] / ph, b[2] / pw, b[3] / ph))]
                    if cand:
                        # Vectorised: a dense page holds 160,000 paths against ~60 text lines.
                        B = np.asarray(cand, float)
                        keep = np.ones(len(B), bool)
                        for o in lines:
                            keep &= ~((np.minimum(B[:, 2], o[2]) - np.maximum(B[:, 0], o[0]) > 0.5)
                                      & (np.minimum(B[:, 3], o[3]) - np.maximum(B[:, 1], o[1]) > 0.5))
                        cx, cy = (B[:, 0] + B[:, 2]) / 2, (B[:, 1] + B[:, 3]) / 2
                        for o in others:
                            keep &= ~((o[0] <= cx) & (cx <= o[2]) & (o[1] <= cy) & (cy <= o[3]))
                        cand = B[keep].tolist()
                    _ink.append(cand)
                return _ink[0]
            # A FIGURE MEASURED AT A FRACTION OF A2'S BOX IS RE-MEASURED FROM ITS INK. Both Figure
            # 4.13s of BIO12L ch04 are vector drawings with OUTLINED labels (no text layer), set
            # inside a paragraph that wraps round them; the paragraph's block box covers the
            # drawing, so the extractor's prose veto threw most of each cluster away -- the
            # honey-bee chart kept its right third (p021), the pedigree key its last two symbols
            # (p022). When the measured box covers under 60% of A2's, the figure is its own ink
            # inside A2's box, and the measured box is held inside A2's.
            fb = fig["bbox_pt"]
            a2_area = (raw[2] - raw[0]) * (raw[3] - raw[1])
            cover = (max(0.0, min(fb[2], raw[2]) - max(fb[0], raw[0]))
                     * max(0.0, min(fb[3], raw[3]) - max(fb[1], raw[1])))
            if pg is not None and a2_area > 0 and cover < 0.6 * a2_area and own_ink():
                held = [max(fb[0], area[0]), max(fb[1], area[1]),
                        min(fb[2], area[2]), min(fb[3], area[3])]
                keep = ([held] if held[2] > held[0] and held[3] > held[1] else []) + own_ink()
                _set_union_geometry(fig, [{"bbox_pt": b} for b in keep], page)
                stats["undersized_regrown"] = stats.get("undersized_regrown", 0) + 1
            # THE HEAD ZONE'S INK. The figure finder skips every drawing lying wholly in the head
            # zone (top 13%), so a figure starting there loses its top: Figure 2.9 (BIO12L ch02
            # p009, a coarse page read as a 4pt grid) its top rule and LH peak; Figure 4.1's
            # outlined column heads `Character  Dominant trait  Recessive trait` (ch04 p004) and
            # Figure 4.3's parental tier (p006), both path by path. When the box stops more than
            # 10pt below A2's top it is extended up to the ink inside A2's box -- the coarse grid
            # on a coarse page, the figure's own paths otherwise -- never past A2's top, so the
            # header band above is not taken.
            if pg is not None:
                from extract_page_layout import visible_drawings as _vd
                fb = fig["bbox_pt"]
                if fb[1] - area[1] > 10:
                    coarse = [[r.x0, r.y0, r.x1, r.y1] for d in _vd(pg) if d.get("coarse")
                              for r in (d["rect"],)]
                    top = [b[1] for b in (coarse or own_ink())
                           if area[0] <= (b[0] + b[2]) / 2 <= area[2]
                           and area[1] <= (b[1] + b[3]) / 2 < fb[1]]
                    if top:
                        _set_union_geometry(
                            fig, [{"bbox_pt": [fb[0], max(area[1], min(top)), fb[2], fb[3]]}],
                            page)
                        stats["tops_extended"] = stats.get("tops_extended", 0) + 1
            fig.pop("line_count", None)
            fig.pop("line_boxes_pt", None)
            # A label that A2 kept as a block of its own is running text, not a label -- the
            # same rule `short_text` applies to candidates, applied to what the extractor had
            # already absorbed before this pass ran.
            fig["absorbed_labels"] = [t for t in (fig.get("absorbed_labels") or []) + loose_labels + [
                " ".join(els[i].get("absorbed_labels") or []) for i in members[1:]] + [
                (els[i].get("text") or "").strip() for i in labels]
                if t and _norm(t) not in kept_text]
            fig.setdefault("figure_box_src", "a2-membership")
            fig["a2_block_n"] = n
            if hints.get(n):
                fig["panel_hints"] = hints[n]
            gone.update(members[1:])
            gone.update(labels)
            stats["figures_merged"] += 1 if len(members) > 1 else 0
            stats["fragments_absorbed"] += max(0, len(members) - 1)
            stats["labels_absorbed"] += len(labels)

        # A figure A2 did not see, that is a bleed sliver or lies under the page's prose, is not
        # artwork the page prints.
        fig_areas = [raw for kind, _, raw in specials if kind == "figure"]
        prose = [e["bbox_pt"] for e in els if e["role"] in _TEXT_ROLES
                 and len((e.get("text") or "").strip()) > _LABEL_MAX]
        for i, e in enumerate(els):
            if i in gone or e["role"] != "figure" or e.get("a2_block_n") is not None:
                continue
            b = e["bbox_pt"]
            # 0.5, not "any overlap": p011's invented figure reaches 26% into Figure 5.12's box.
            unseen = not any(_inside(b, a, 0.5) for a in fig_areas)
            # AN ORNAMENT IS NOT A FIGURE. The summary and exercises pages of BIO12L ch01 (p023,
            # p024) carry a narrow decorative strip beside the text, 0.085 of the page wide; A2
            # read both pages and boxed no figure, yet each shipped as an unnumbered figure.
            ornament = (unseen and (b[2] - b[0]) < 0.12 * pw
                        and not (e.get("absorbed_labels") or []))
            if _is_sliver(b) or ornament or (unseen and any(_inside(b, t, 0.3) for t in prose)):
                e["role"] = "page_furniture"
                e["furniture_reason"] = ("sliver" if _is_sliver(b) else "ornament" if ornament
                                         else "not-a-printed-figure")
                if ornament and not _is_sliver(b):
                    e["furniture"] = "ornament"      # still printed: cut and drawn as page art
                stats["figures_dropped"] += 1
                # ...AND AN ORNAMENT INSIDE A DROPPED CLUSTER IS STILL PRINTED. BIO12L ch06 p017's
                # leaf strip (an image 0.084 of the page wide) clustered with the Summary box's
                # frame into one 0.71-wide "figure"; A2 boxed no figure there, the cluster was
                # dropped as not-a-printed-figure, and the strip went with it. A narrow embedded
                # image mostly inside the dropped box is kept, at its own (page-clipped) rect.
                if not ornament and not _is_sliver(b) and pdf_page() is not None:
                    for xref, *_ in pdf_page().get_images(full=True):
                        for r in pdf_page().get_image_rects(xref):
                            c = [max(r.x0, 0.0), max(r.y0, 0.0), min(r.x1, pw), min(r.y1, ph)]
                            iw, ih = c[2] - c[0], c[3] - c[1]
                            if not (0 < iw < 0.12 * pw and ih > 3 * iw):
                                continue
                            ov = (max(0.0, min(c[2], b[2]) - max(c[0], b[0]))
                                  * max(0.0, min(c[3], b[3]) - max(c[1], b[1])))
                            if ov < 0.5 * iw * ih:
                                continue
                            orn = {"role": "page_furniture", "furniture": "ornament",
                                   "furniture_reason": "ornament",
                                   "bbox_pt": [round(v, 1) for v in c],
                                   "bbox": [round(c[0] / pw, 4), round(c[1] / ph, 4),
                                            round(c[2] / pw, 4), round(c[3] / ph, 4)]}
                            els.append(orn)
        # A TABLE THE BOOK DRAWS. Table 5.1 of BIO12L ch05 (the genetic code, p096) is vector
        # art -- rules, tints and OUTLINED glyphs, no text layer -- so the extractor measured
        # the caption alone: the crop held one line and the render squeezed A2S's 17-row grid
        # into it. A table whose box covers under 40% of A2's, with no layer text under its
        # caption inside A2's box, takes the drawn ink inside A2's box and the ink that
        # touches it (A2's box is an estimate and stopped 23pt above the last row), never
        # crossing a text line, the watermark or the trim. It is flagged `grid_drawn`; the
        # caption keeps its own measured box.
        for b in merged:
            if b.get("kind") != "table" or len(b.get("bbox") or []) != 4 or pdf_page() is None:
                continue
            raw = [v * k for v in b["bbox"]]
            area = [raw[0] - 4, raw[1] - 4, raw[2] + 4, raw[3] + 4]
            tbl = next((e for i, e in enumerate(els) if i not in gone and e["role"] == "table"
                        and _centre_in(e["bbox_pt"], area)), None)
            if tbl is None or tbl.get("grid_drawn"):
                continue
            tb = tbl["bbox_pt"]
            a2_area = (raw[2] - raw[0]) * (raw[3] - raw[1])
            if a2_area <= 0 or (tb[2] - tb[0]) * (tb[3] - tb[1]) >= 0.4 * a2_area:
                continue
            pg = pdf_page()
            tlines = [list(ln["bbox"]) for blk in _page_read(pg, "dict")["blocks"]
                      for ln in blk.get("lines", [])
                      if "".join(s["text"] for s in ln["spans"]).strip()]
            if any(_centre_in(ln, area) and ln[1] > tb[3] + 2 for ln in tlines):
                continue                                  # a text grid: the layer measures it
            import book_design
            from extract_page_layout import path_rects
            cand = [[r.x0, r.y0, r.x1, r.y1] for r in path_rects(pg)
                    if r.width < 0.9 * pw and r.height < 0.9 * ph]
            cand = [c for c in cand if c[0] > 2 and c[1] > 2 and c[2] < pw - 2 and c[3] < ph - 2
                    and not book_design.is_watermark((c[0] / pw, c[1] / ph, c[2] / pw, c[3] / ph))
                    and area[0] - 20 <= (c[0] + c[2]) / 2 <= area[2] + 20
                    and not any(min(c[2], ln[2]) - max(c[0], ln[0]) > 0.5
                                and min(c[3], ln[3]) - max(c[1], ln[1]) > 0.5 for ln in tlines)]
            box = None
            for c in cand:
                if _centre_in(c, area) and c[1] >= tb[1]:
                    box = list(c) if box is None else [min(box[0], c[0]), min(box[1], c[1]),
                                                       max(box[2], c[2]), max(box[3], c[3])]
            if box is None:
                continue
            grown = True
            while grown:
                grown = False
                for c in cand:
                    if (c[0] < box[0] or c[1] < box[1] or c[2] > box[2] or c[3] > box[3]) and \
                            c[0] <= box[2] + 4 and c[2] >= box[0] - 4 and \
                            c[1] <= box[3] + 4 and c[3] >= box[1] - 4 and c[1] >= tb[1]:
                        box = [min(box[0], c[0]), min(box[1], c[1]),
                               max(box[2], c[2]), max(box[3], c[3])]
                        grown = True
            pages_sheet = tbl.get("bbox_sheet") or tbl["bbox"]
            tbl["caption_bbox_sheet"] = list(pages_sheet)
            _set_union_geometry(tbl, [{"bbox_pt": tb}, {"bbox_pt": box}], page)
            tbl["grid_drawn"] = True
            tbl["a2_block_n"] = b.get("n")
            stats["tables_drawn"] = stats.get("tables_drawn", 0) + 1
        page["elements_in_reading_order"] = [e for i, e in enumerate(els) if i not in gone]
        # A FIGURE TAKES ITS DRAWN LABELS. Figure 1.5's `Vacuoles`, `Nucleus`, `Asymmetric
        # spindle` ... (BIO12L ch01 p007) are outlined glyphs, not text, joined to the cells by
        # leader lines and set left of A2's box -- so the box, the crops and the panels all cut
        # them off at `les`, `cus`. Small drawn shapes touching a figure (within 6pt) join it,
        # repeatedly, so a leader line brings its label letter by letter; growth never enters
        # another figure. Text is never a drawn shape, so no prose can be taken.
        pg = pdf_page()
        from extract_page_layout import visible_drawings
        figs_here = [e for e in page["elements_in_reading_order"] if e["role"] == "figure"]
        if pg is not None and figs_here:
            small = [list(d["rect"]) for d in visible_drawings(pg)
                     if not d.get("coarse") and d["rect"].width < 60 and d["rect"].height < 60
                     and max(d["rect"].width, d["rect"].height) > 0]   # a leader line is 0 high
            caps_all = [c["bbox_pt"] for c in page["elements_in_reading_order"]
                        if c["role"] == "figure_caption" and c.get("bbox_pt")]
            # THE FOLIO TAB IS NOT A LABEL. Its pieces need not bleed to the trim: on BIO12L ch03
            # p045 Figure 3.4 (b) grew over a piece ending at x 498pt, so the crop covered the
            # orange `45` tab and the render printed it cut in half. A shape touching the printed
            # page number's box (padded) is never taken.
            folios = [[o["bbox_pt"][0] - 8, o["bbox_pt"][1] - 8,
                       o["bbox_pt"][2] + 8, o["bbox_pt"][3] + 8]
                      for o in page["elements_in_reading_order"]
                      if o["role"] == "page_number" and o.get("bbox_pt")]
            for e in figs_here:
                others = [o["bbox_pt"] for o in figs_here if o is not e] + folios
                fb = _grow_to_drawn(e["bbox_pt"], small, others, caps_all, (pw, ph))
                if fb != e["bbox_pt"]:
                    _set_union_geometry(e, [{"bbox_pt": fb}], page)
                    e.pop("line_count", None)
                    e.pop("line_boxes_pt", None)
                    stats["figures_grown_to_drawn_labels"] = (
                        stats.get("figures_grown_to_drawn_labels", 0) + 1)
            # A FIGURE SET ON ITS OWN PANEL TAKES THE PANEL. Figure 6.8 (BIO12L ch06 p011) is
            # drawn on a cream rounded frame; the box was measured from the graphs inside it, so
            # the crop cut the frame on all four sides. A filled shape that holds the figure,
            # is at most twice its area, and holds no prose, caption or other figure is the
            # figure's own ground: the box grows to it (and to an outline on the same rect).
            words = [t["bbox_pt"] for t in page["elements_in_reading_order"]
                     if t.get("bbox_pt") and (t["role"] == "figure_caption" or (
                         t["role"] in _TEXT_ROLES
                         and len((t.get("text") or "").strip()) > _LABEL_MAX))]
            shapes = [d for d in visible_drawings(pg) if not d.get("coarse")]
            for e in figs_here:
                fb = e["bbox_pt"]
                area = (fb[2] - fb[0]) * (fb[3] - fb[1])
                best = None
                for d in shapes:
                    r = d["rect"]
                    pr = [r.x0, r.y0, r.x1, r.y1]
                    if not d.get("fill") or r.width >= 0.9 * pw or r.height >= 0.9 * ph:
                        continue
                    if not (pr[0] <= fb[0] + 2 and pr[1] <= fb[1] + 2
                            and pr[2] >= fb[2] - 2 and pr[3] >= fb[3] - 2):
                        continue
                    if r.width * r.height > 2.0 * area or pr == list(fb):
                        continue
                    if any(_centre_in(w, pr) and not _centre_in(w, fb) for w in words):
                        continue
                    if any(_box_gap(o["bbox_pt"], pr) < 0 for o in figs_here if o is not e):
                        continue
                    if best is None or r.width * r.height < best[4]:
                        best = pr + [r.width * r.height]
                if best:
                    nb = [min(fb[0], best[0]), min(fb[1], best[1]),
                          max(fb[2], best[2]), max(fb[3], best[3])]
                    # its keyline: an unfilled stroke on (about) the same rectangle
                    for d in shapes:
                        r = d["rect"]
                        if (not d.get("fill") and abs(r.x0 - best[0]) < 4 and abs(r.y0 - best[1]) < 4
                                and abs(r.x1 - best[2]) < 4 and abs(r.y1 - best[3]) < 4):
                            nb = [min(nb[0], r.x0), min(nb[1], r.y0),
                                  max(nb[2], r.x1), max(nb[3], r.y1)]
                    nb = [nb[0] - 0.5, nb[1] - 0.5, nb[2] + 0.5, nb[3] + 0.5]
                    _set_union_geometry(e, [{"bbox_pt": nb}], page)
                    e.pop("line_count", None)
                    e.pop("line_boxes_pt", None)
                    stats["figures_grown_to_panel"] = stats.get("figures_grown_to_panel", 0) + 1
        # A FIGURE STOPS AT ITS CAPTION. A2 boxes a figure with its caption (Figure 1.8, BIO12L
        # ch01 p010), so the box took in the caption's first line, the crop -- a render of the
        # box -- printed the caption in its pixels, and the live caption drawn under it overlapped
        # that copy. A figure box reaching into a caption is cut back to the caption's edge.
        caps_here = [c["bbox_pt"] for c in page["elements_in_reading_order"]
                     if c["role"] == "figure_caption" and c.get("bbox_pt")]
        for e in page["elements_in_reading_order"]:
            if e["role"] != "figure":
                continue
            fb = list(e["bbox_pt"])
            for cb in caps_here:
                ix = min(fb[2], cb[2]) - max(fb[0], cb[0])
                iy = min(fb[3], cb[3]) - max(fb[1], cb[1])
                # Only a caption the figure SITS ON: one it overlaps across most of the
                # caption's width. Figure 1.5's drawn labels reach past the end of Figure 1.4's
                # caption (BIO12L ch01 p007); cutting there took panel (a) off the figure.
                if ix <= 0 or iy <= 0 or ix < 0.5 * (cb[2] - cb[0]):
                    continue
                cuts = {3: cb[1] - 1 if cb[1] > fb[1] + 0.5 * (fb[3] - fb[1]) else None,
                        1: cb[3] + 1 if cb[3] < fb[1] + 0.5 * (fb[3] - fb[1]) else None,
                        2: cb[0] - 1 if cb[0] > fb[0] + 0.5 * (fb[2] - fb[0]) else None}
                k = next((k for k in (3, 1, 2) if cuts[k] is not None), None)
                if k is None:
                    # A CAPTION AT THE MIDDLE, between two figures. The extractor unioned Figure
                    # 12.4 (a), its caption and pyramid (b) into one box (BIO12L ch12 p212), with
                    # the caption at the box's middle, so neither half-test fired; the (a) crop
                    # printed caption (a) under the live one and (b) a second time. When another
                    # figure lies past the caption on ONE side, that side is not this figure's.
                    others = [o["bbox_pt"] for o in page["elements_in_reading_order"]
                              if o is not e and o["role"] == "figure" and o.get("bbox_pt")
                              and min(fb[2], o["bbox_pt"][2]) > max(fb[0], o["bbox_pt"][0])]
                    below = any(cb[3] - 2 <= o[1] < fb[3] for o in others)
                    above = any(fb[1] < o[3] <= cb[1] + 2 for o in others)
                    if below != above:
                        k = 3 if below else 1
                        cuts[k] = cb[1] - 1 if below else cb[3] + 1
                if k is not None:
                    fb[k] = cuts[k]
            if fb != e["bbox_pt"] and fb[2] > fb[0] and fb[3] > fb[1]:
                _set_union_geometry(e, [{"bbox_pt": fb}], page)
                e.pop("line_count", None)
                e.pop("line_boxes_pt", None)
                stats["figures_cut_at_caption"] = stats.get("figures_cut_at_caption", 0) + 1
        # PANELS, measured from the PDF inside each figure's final box (see `_find_panels`).
        # Done last and from the page itself, because by now the extractor and the merge above
        # have unioned a figure's pictures into one box and its letters into one label list.
        for e in page["elements_in_reading_order"]:
            if e["role"] != "figure":
                continue
            pg = pdf_page()
            panels = _panels_from_pdf(pg, e["bbox_pt"], pw, ph) if pg is not None else []
            if not panels and pg is not None:
                # No letters in the text layer: maybe ONE scanned picture whose letters are
                # pixels. Its caption -- the one printed nearest under it -- says the panels.
                fb = e["bbox_pt"]
                caps = [c for c in page["elements_in_reading_order"]
                        if c["role"] == "figure_caption" and c.get("bbox_pt")
                        and fb[3] - 6 <= c["bbox_pt"][1] <= fb[3] + 40
                        and min(fb[2], c["bbox_pt"][2]) > max(fb[0], c["bbox_pt"][0])]
                if caps:
                    cap = min(caps, key=lambda c: c["bbox_pt"][1])
                    panels = _panels_from_raster(pg, fb, pw, ph, cap.get("text") or "")
            if not panels and pg is not None and e.get("panel_hints"):
                panels = _panels_from_hints(pg, e["panel_hints"], pw, ph)
            # A SPLIT MUST GIVE EVERY PANEL THE CAPTION NAMES. A split into fewer pictures than
            # the caption letters has put two of them in one panel and labelled it as one.
            fb = e["bbox_pt"]
            caps = [c for c in page["elements_in_reading_order"]
                    if c["role"] == "figure_caption" and c.get("bbox_pt")
                    and fb[3] - 6 <= c["bbox_pt"][1] <= fb[3] + 60
                    and min(fb[2], c["bbox_pt"][2]) > max(fb[0], c["bbox_pt"][0])]
            named = set(re.findall(r"\(([a-h])\)", min(caps, key=lambda c: c["bbox_pt"][1])
                                   .get("text") or "")) if caps else set()
            got = {re.sub(r"[^a-z]", "", q.get("key") or q.get("label") or "")[:1] for q in panels}
            if panels and len(named) > len(panels) and not named <= got:
                panels = []
            # Each panel takes its own drawn labels, as a figure does (`_grow_to_drawn`): a
            # figure kept clear of a neighbour's caption can still leave its labels outside, and
            # Figure 1.5 (b)'s crop would cut `Vacuoles` to `les`.
            if panels and pg is not None:
                smallp = [list(d["rect"]) for d in visible_drawings(pg)
                          if not d.get("coarse") and d["rect"].width < 60 and d["rect"].height < 60
                          and max(d["rect"].width, d["rect"].height) > 0]
                capsp = [c["bbox_pt"] for c in page["elements_in_reading_order"]
                         if c["role"] == "figure_caption" and c.get("bbox_pt")]
                figo = [o["bbox_pt"] for o in page["elements_in_reading_order"]
                        if o["role"] == "figure" and o is not e]
                for p in panels:
                    if p.get("raster"):
                        continue
                    sib = [q["bbox_pt"] for q in panels if q is not p]
                    p["bbox_pt"] = [round(v, 1) for v in
                                    _grow_to_drawn(p["bbox_pt"], smallp, sib + figo, capsp,
                                                   (pw, ph))]
            for p in panels:
                tmp = {}
                _set_union_geometry(tmp, [{"bbox_pt": p["bbox_pt"]}], page)
                p["bbox_sheet"] = tmp["bbox_sheet"]
            if panels:
                e["panels"] = panels
                stats["panels"] = stats.get("panels", 0) + len(panels)
            else:
                e.pop("panels", None)
    return stats
