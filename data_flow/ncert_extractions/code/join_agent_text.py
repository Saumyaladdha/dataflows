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
    "table": "table",
}


def _norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


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
    return pairs


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

        pairs = _align([b.get("text", "") for b in blocks], [e.get("text", "") for e in els])
        matched_pdf = set()
        for ai, bj in pairs:
            if ai is None or bj is None:
                if ai is not None:
                    stats["blocks_unmatched_agent"] += 1
                continue
            el, blk = els[bj], blocks[ai]
            text = (blk.get("text") or "").strip()
            if not text:
                continue
            # THE AGENT'S TEXT WINS; THE LAYER'S FORMATTING IS RE-LOCATED INTO IT.
            #
            # The naive version took the agent's string and gave it the FIRST run's flags. On
            # the Genus paragraph the first run is the bold term `Genus`, so the whole
            # 479-character paragraph came back bold -- 1 mark where the book prints 7, and
            # `terms` empty because no single word was bold any more.
            #
            # The layer is wrong about the CHARACTERS of a formula and right about WHICH WORDS
            # are bold or italic, so the formatted substrings are carried over by searching for
            # them in the agent's text. A substring that cannot be found is dropped rather than
            # guessed at: a mark in the wrong place is worse than a missing one, because it
            # renders as emphasis the book does not print.
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
            base = (el.get("runs") or [{}])[0]
            spans = []
            for r in el.get("runs") or []:
                frag = re.sub(r"\s+", " ", r.get("t", "")).strip()
                flags = {k: True for k in ("b", "i", "sc") if r.get(k)}
                if r.get("script"):
                    flags["script"] = r["script"]
                if frag and flags and len(frag) <= 120:
                    spans.append((frag, flags))
            el["text"] = text
            runs, cursor = [], 0
            for frag, flags in spans:
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
                at, probe = -1, cursor
                while True:
                    at = text.find(frag, probe)
                    if at < 0:
                        break
                    tail = at + len(frag)
                    if len(frag) > 3 or not (tail < len(text) and text[tail].isalpha()):
                        break
                    probe = at + 1
                if at < 0:
                    continue
                if at > cursor:
                    runs.append({"t": text[cursor:at]})
                runs.append({"t": frag, **flags})
                cursor = at + len(frag)
            if cursor < len(text):
                runs.append({"t": text[cursor:]})
            for r in runs:
                r.setdefault("b", False); r.setdefault("i", False)
                r.setdefault("sc", False); r.setdefault("script", None)
                r["color"] = base.get("color", "#231f20")
                r["size"] = base.get("size"); r["font"] = base.get("font")
            el["runs"] = runs or [{"t": text, "b": False, "i": False, "sc": False,
                                   "script": None, "color": base.get("color", "#231f20"),
                                   "size": base.get("size"), "font": base.get("font")}]
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
            matched_pdf.add(bj)
            stats["blocks_replaced"] += 1
        for j, e in enumerate(els):
            if j not in matched_pdf:
                e["text_source"] = "pdf-text-layer"
                stats["blocks_kept_pdf"] += 1
    layout["text_join"] = stats
    return stats
