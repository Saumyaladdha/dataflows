#!/usr/bin/env python3
"""Builds the semantic CHAPTER MODEL for an NCERT Inorganic Chemistry chapter.

This is the single source both the Markdown export and the HTML export are rendered from, which
is the whole reason it is its own module: in every earlier flow the Markdown exporter and the HTML
exporter each walked the raw A2 output separately and decided for themselves what a block meant,
so the two drifted -- a block the HTML set as a worked-example panel the Markdown set as an
ordinary paragraph. Here the meaning is decided once.

What the model joins together:

  * A2    - the blocks, their reading order, their kind and their text  (the CONTENT, unchanged)
  * A2S   - transcriptions of figures, tables, equations and boxes
  * A2N   - corrected inline notation
  * A2B   - which terms are set bold
  * the measurement (scripts/inorganic_chemistry_measure.py) - where each block is PRINTED, in
    what column, inside which panel, and -- the part no other flow has -- the sub/superscript
    structure of its formulae, recovered from the PDF's own span sizes and baselines.

Nothing here makes a content judgement. Classification is by the book's own printed evidence:
a heading numbered `5.2` is a margin heading because NCERT sets those in the margin; a box whose
first line reads `Example 5.4` is a worked example because that is what the book prints on it.
"""

import difflib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
# Reused rather than reimplemented: these are the same most-settled-run loaders every other
# export in this project reads its data through, so this flow cannot silently see a different
# version of a page than the Biology or Physics flow would.
from export_ncert_chapter_review import (  # noqa: E402
    _best_page_outputs,
    _load_sibling_json,
)

# A2 records a block's bbox in PIXELS on a page image rendered at lib_pdf.DEFAULT_DPI (200).
# The measurement records everything as a FRACTION of the sheet. This is the conversion between
# them, and it is derived from the measured trim rather than hardcoded, because the only reason
# 1600x2180 is right for this book is that its sheet is 576x784.8pt.
_A2_DPI = 200.0


# --------------------------------------------------------------------------------------------
# What a block IS, decided from what the book prints on it.
# --------------------------------------------------------------------------------------------
_RE_MARGIN_HEADING = re.compile(r"^\s*(\d+\.\d+)\s+(?!\d)(\S.*)$", re.S)
_RE_SUB_HEADING = re.compile(r"^\s*(\d+\.\d+\.\d+)\s+(\S.*)$", re.S)
_RE_LETTER_HEADING = re.compile(r"^\s*\(\s*([a-z])\s*\)\s*(\S.*)$", re.S | re.I)
_RE_UNIT_TITLE = re.compile(r"^\s*Unit\s+(\d+)\s*\n(.+)$", re.S | re.I)
_RE_EXAMPLE = re.compile(r"^\s*Example\s+([\d.]+)", re.I)
_RE_SOLUTION = re.compile(r"^\s*Solution\b", re.I)
_RE_OBJECTIVES = re.compile(r"^\s*Objectives\b", re.I)
_RE_SUMMARY = re.compile(r"^\s*Summary\b", re.I)
_RE_INTEXT = re.compile(r"^\s*Intext\s+Questions\b", re.I)
_RE_EXERCISES = re.compile(r"^\s*Exercises?\s*$", re.I)
_RE_ANSWERS = re.compile(r"^\s*Answers\s+to\s+Some\s+Intext\s+Questions\b", re.I)
_RE_FIG_CAPTION = re.compile(r"^\s*Fig\.?\s*\d", re.I)
_RE_TABLE_CAPTION = re.compile(r"^\s*Table\s+\d", re.I)
# A scientist panel opens with the subject's name and says they were born. NCERT sets exactly one
# of these per chapter and always in this shape ("Werner was born on December 12, 1866, in ...").
_RE_SCIENTIST = re.compile(r"^\s*([A-Z][\w'’-]+)\s+was\s+born\b")


def _first_line(text):
    return (text or "").strip().split("\n", 1)[0].strip()


def classify(block, panel_kind=None):
    """The semantic role of one A2 block. Returns (role, label).

    The worked-example labels are tested FIRST, before the block's A2 kind is consulted. NCERT
    prints "Example 9.3" and "Solution" as the headings of a box, and A2 reads them as whatever
    they look like on the page -- sometimes a `box`, sometimes a `heading`, sometimes the opening
    line of a `paragraph`. Keying off the kind therefore recognised them only when A2 happened to
    call them a box: on Amines that meant one worked example in five kept its blue script label
    and the rest came out as ordinary run-in headings, with the question and its solution running
    together and Example 9.3 split across three separate pieces.

    `panel_kind` is what the MEASUREMENT says this block sits inside, and it wins over the text
    for panel membership: the Summary runs across two sheets and only its first block carries the
    word "Summary", so classifying by text alone put the second half outside the panel.
    """
    kind = block.get("kind")
    text = (block.get("text") or "").strip()
    head = _first_line(text)

    # What the book PRINTS on the block, whatever A2 called it.
    m = _RE_EXAMPLE.match(head)
    if m:
        return "example", m.group(1)
    if _RE_SOLUTION.match(head):
        return "solution", ""
    if _RE_SUMMARY.match(head) and kind in ("box", "heading"):
        return "summary", ""
    if _RE_INTEXT.match(head):
        return "intext", ""
    if _RE_OBJECTIVES.match(head) and kind in ("box", "heading"):
        return "objectives", ""

    if kind == "heading":
        m = _RE_UNIT_TITLE.match(text)
        if m:
            return "chapter_title", m.group(1)
        if _RE_ANSWERS.match(head):
            return "answers_heading", ""
        if _RE_EXERCISES.match(head):
            return "exercises_heading", ""
        m = _RE_SUB_HEADING.match(text)
        if m:
            return "sub_heading", m.group(1)
        m = _RE_MARGIN_HEADING.match(text)
        if m:
            return "margin_heading", m.group(1)
        m = _RE_LETTER_HEADING.match(text)
        if m:
            return "letter_heading", m.group(1)
        if _RE_FIG_CAPTION.match(head):
            return "figure_caption", ""
        if _RE_TABLE_CAPTION.match(head):
            return "table_caption", ""
        return "run_in_heading", ""

    if kind == "box":
        if _RE_OBJECTIVES.match(head):
            return "objectives", ""
        m = _RE_EXAMPLE.match(head)
        if m:
            return "example", m.group(1)
        if _RE_SOLUTION.match(head):
            return "solution", ""
        if _RE_SUMMARY.match(head):
            return "summary", ""
        if _RE_INTEXT.match(head):
            return "intext", ""
        m = _RE_SCIENTIST.match(text)
        if m:
            return "scientist", m.group(1)
        if panel_kind == "summary":
            return "summary_body", ""
        if panel_kind == "feature":
            return "feature", ""
        if panel_kind == "example":
            return "example_body", ""
        return "note", ""

    if kind == "figure":
        return "figure", ""
    if kind == "table":
        return "table", ""
    if kind == "equation":
        return "equation", ""
    if kind == "list":
        return "list", ""
    return "paragraph", ""


# --------------------------------------------------------------------------------------------
# Joining A2's text to the measured print
# --------------------------------------------------------------------------------------------
def _norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


# Which MEASURED font roles an extracted block of each semantic role may match.
#
# Matching on text alone cannot place the display-face blocks. The opener sets its title in a face
# the text layer splits into one block per line plus a shadow copy of each, so no measured block
# equals "Unit 5 / Coordination Compounds"; every true fragment is too short to pass a length
# sanity check, and the only candidate left standing was the section heading further down the
# page -- which is how the chapter title ended up inheriting the heading's position and the
# heading ended up with none.
#
# The measurement already knows what KIND of type each printed block is, from its face and size.
# Constraining the candidates by that first is both cheaper and far more robust than trying to
# out-score a coincidence on shared words.
_ROLE_CANDIDATES = {
    "margin_heading": ("margin_heading",),
    "chapter_title": ("chapter_title", "display_script", "unit_numeral"),
    "letter_heading": ("caption_or_letter_heading", "demi"),
    "sub_heading": ("demi", "caption_or_letter_heading"),
    "figure_caption": ("caption_or_letter_heading", "demi"),
    "table_caption": ("demi", "caption_or_letter_heading"),
}


def match_blocks(a2_blocks, measured_blocks, roles_by_n=None):
    """{a2 block n: measured text block} -- which printed block each extracted block IS.

    A2 and the measurement see the same page through different instruments: A2 reports blocks in
    reading order with their text, the measurement reports them with their position, font and
    formula structure. They are joined on the text itself, normalised to letters and digits so
    that line-wrap whitespace, hyphenation and the measurement's fake-bold repeats cannot break
    the match. Measured on this chapter, every text-bearing block matches at 0.95 or better.
    """
    pool = [(i, _norm(b["text"]), b) for i, b in enumerate(measured_blocks)]
    out, taken = {}, set()
    for b in a2_blocks:
        n, target = b.get("n"), _norm(b.get("text"))
        if not isinstance(n, int) or not target:
            continue
        allowed = _ROLE_CANDIDATES.get((roles_by_n or {}).get(n))
        best, best_score, best_i = None, 0.0, None
        for i, norm_text, rec in pool:
            if i in taken or not norm_text:
                continue
            if allowed and rec.get("role") not in allowed:
                continue
            head = target[:60]
            if head and head in norm_text:
                score = 1.0
            elif (norm_text[:60] and norm_text[:60] in target
                  and len(norm_text) >= 0.6 * len(target)):
                # The measured block must cover MOST of the extracted block before being accepted
                # on reverse containment. Without the length test any short printed block whose
                # words appear anywhere in a long block scored 0.97: on p001 the banner's
                # "Coordination Compounds" out-scored the real match for the section heading
                # "5.1 Werner's Theory of Coordination Compounds", so the heading inherited the
                # banner's position and was laid out at the top of the page instead of beside the
                # paragraph it heads.
                score = 0.97
            else:
                score = difflib.SequenceMatcher(None, target[:300], norm_text[:300]).ratio()
                # Length sanity. The opener sets its title in a display face that the text layer
                # splits into one block per line plus a shadow copy of each, so no single measured
                # block equals "Unit 5 / Coordination Compounds". Left unchecked, the partial
                # blocks let an unrelated heading score on shared words alone and the title
                # inherited the heading's position. A candidate less than half or more than twice
                # the block's length is not that block.
                ratio_len = len(norm_text) / max(1, len(target))
                if ratio_len < 0.5 or ratio_len > 2.0:
                    score *= 0.5
            if score > best_score:
                best, best_score, best_i = rec, score, i
        if best is not None and best_score >= 0.55:
            taken.add(best_i)
            out[n] = {"measured": best, "score": round(best_score, 3)}

    # SECOND PASS: a printed block may hold SEVERAL extracted blocks.
    #
    # A2 reads a page more finely than the text layer segments it -- p001 has 12 A2 blocks against
    # 10 printed ones -- so once each printed block is claimed, the extra A2 blocks match nothing
    # and end up with no position at all. 35 of this chapter's 236 blocks were unplaced that way,
    # and a block with no position cannot be put in a column, inside a panel, or beside a figure.
    # That one fact is behind most of the layout damage in this chapter.
    #
    # Reuse is allowed only on CONTAINMENT: the extracted text must appear inside the printed
    # block, which means it really is part of it. The first pass still prefers an unclaimed block,
    # so nothing it got right is changed.
    for b in a2_blocks:
        n, target = b.get("n"), _norm(b.get("text"))
        if not isinstance(n, int) or not target or n in out:
            continue
        for i, norm_text, rec in pool:
            if not norm_text:
                continue
            head = target[:60]
            if head and head in norm_text:
                out[n] = {"measured": rec, "score": 0.9, "shared": True}
                break
    return out


def page_variant_stream(measured_blocks):
    """The whole page's printed characters in reading order, each carrying its own typing.

    Matching an A2 paragraph to ONE measured block is not enough, and the reason is specific:
    PyMuPDF splits a run of script-sized glyphs into a block of its own, so a paragraph that ends
    "[Fe(CN)6]4-, [Co(NH3)6]3+." is reported as the paragraph PLUS a separate little block holding
    its tail. Aligning against the single best-matching block therefore typed the body of the
    paragraph correctly and left its last clause flat -- visible on p004 as `[Co(NH3)6]3+` set in
    running text beside a properly typeset `[CoCl3(NH3)3]` two lines above.

    Aligning against the page instead makes block boundaries irrelevant, which is the right level:
    they are an artefact of how the text layer was segmented, not a fact about the chapter.

    Returns (compact_text, variant_per_char) over non-space characters only, because A2 and the
    text layer disagree about whitespace almost everywhere and about nothing else.
    """
    chars, variants, sizes, line_of, lines = [], [], [], [], []
    for block in measured_blocks:
        for line in block.get("lines", []):
            idx = len(lines)
            lines.append(line)
            for run in line["runs"]:
                for ch in run["t"]:
                    if ch.isspace():
                        continue
                    chars.append(ch)
                    # The full typed STYLE of this character, not only its variant: NCERT's
                    # italics carry meaning (n-, o-, p-, in situ, ortho) and its colour coding
                    # shows which group is reacting. Both were measured and then dropped here.
                    variants.append((run["v"], bool(run.get("i")), run.get("c")))
                    sizes.append(line.get("size"))
                    line_of.append(idx)
    return "".join(chars), variants, sizes, line_of, lines


# Characters the two instruments spell differently. A2S types a charge as an ASCII hyphen
# ("3Cl-") where the book sets an en dash ("3Cl–"); the same goes for the minus sign and for
# curly quotes. Folding them before matching is what lets a cell be found at all -- unfolded,
# Table 5.1's formula column missed on its very last character and no cell in the chapter's
# tables was ever typed.
_FOLD = {"\u2013": "-", "\u2014": "-", "\u2212": "-", "\u2010": "-", "\u2011": "-",
         "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"', "\u00a0": " "}


# Glyphs the text layer hands back under the wrong Latin codepoint. NCERT draws its reaction
# arrows from a symbol encoding, and PyMuPDF maps that slot to U+00AE -- so every reaction in the
# Answers section read "[Co(NH3)5Br]SO4 + Ba 2+ (R) BaSO4 (s)". A registered-trademark sign does
# not otherwise occur in an NCERT chemistry chapter, so the mapping is unambiguous.
# The same symbol encoding mis-maps the Greek letters NCERT uses for substituent positions, so
# "alpha-nitroso-beta-naphthol" came through as "a-nitroso-b-naphthol". Only repaired where the
# source span is set in a SYMBOL face -- a bare Latin "a" in prose must never become an alpha.
_GLYPH_REPAIR = {"\u00ae": "\u2192"}
_SYMBOL_REPAIR = {"a": "\u03b1", "b": "\u03b2", "g": "\u03b3", "d": "\u03b4",
                  "m": "\u03bc", "p": "\u03c0", "s": "\u03c3", "l": "\u03bb",
                  "D": "\u0394", "\u00ae": "\u2192", "\u00ad": "\u2190"}


# A2 reads the PRIME in a symbol font as a cent sign, and reads the display face's repeated draws
# as repeated characters. Together those turn "R-NHR' and tertiary amines by R3N, RNR'R\"" into
# "R-NHR\u00a2 and tertiary amines by R3N, RNR\u00a2R\u00a2\u00a2\u00a2\u00a2\u00a2\u00a2\u00a2\u00a2\u00a2", which is what the Summary
# of Amines was printing. Both are defects in the extracted text, not in the render -- the right
# fix is to re-read that page -- but leaving a chapter's Summary garbled while that happens serves
# nobody, and the mapping is unambiguous: a cent sign does not occur in an NCERT chemistry
# chapter, and no notation in this book takes more than a double prime.
_PRIME_RUN = re.compile("\u00a2(?:\\s*[.,]?\\s*\u00a2)*")


def _repair_primes(text):
    def one(mo):
        n = mo.group(0).count("\u00a2")
        return "\u2032" if n == 1 else "\u2033"
    return _PRIME_RUN.sub(one, text)


def repair_glyphs(text):
    for bad, good in _GLYPH_REPAIR.items():
        text = text.replace(bad, good)
    return _repair_primes(text)


def _fold(text):
    return "".join(_FOLD.get(ch, ch) for ch in text)


def transfer_variants(a2_text, stream):
    r"""A2's text, re-typed with the sub/superscripts the book actually prints.

    A2 transcribes `[Co(NH3)6]3+` as those literal characters -- correctly, because that is what a
    text layer flattened to a string contains. The measurement knows better: it kept each span's
    point size and baseline, so it knows the `3` is set as a subscript and the `3+` as a
    superscript. This carries that typing onto A2's own characters, which is what lets this book's
    chemistry be set as TEXT rather than shipped as a screenshot of the page.

    `stream` is the page's (compact_text, variants) from page_variant_stream. The content stays
    A2's; only the typography comes from the measurement.
    """
    compact_text, variants = stream[0], stream[1]
    if not compact_text or not a2_text:
        return [{"t": a2_text, "v": ""}]

    a_idx = [i for i, ch in enumerate(a2_text) if not ch.isspace()]
    a_compact = "".join(a2_text[i] for i in a_idx)
    if not a_compact:
        return [{"t": a2_text, "v": ""}]

    # Folding is per character, so indices stay 1:1 with the unfolded strings.
    a_fold, m_fold = _fold(a_compact), _fold(compact_text)

    out_variants = [("", False, None)] * len(a2_text)
    offset = m_fold.find(a_fold)
    if offset >= 0:
        # The common case: A2's characters appear verbatim in the stream.
        for k in range(len(a_compact)):
            out_variants[a_idx[k]] = variants[offset + k]
        return _collapse(a2_text, out_variants)

    # A2N may have rewritten notation, or A2 may have joined text the layer orders differently.
    # Locate roughly, then align inside a window -- a full SequenceMatcher per block is quadratic
    # and the answer is always local.
    #
    # The anchor is tried at SHRINKING lengths. A fixed 40-character anchor cannot match anything
    # shorter than itself, so every short string -- which is to say every table cell -- failed to
    # anchor, fell back to offset 0, and then searched a window at the START of the stream that
    # could not contain it. Table 5.1's cells sit 105 characters in; the window ended at 102.
    anchor = -1
    for n in (40, 24, 16, 10, 6):
        if len(a_fold) >= n:
            anchor = m_fold.find(a_fold[:n])
            if anchor >= 0:
                break
    if anchor < 0:
        match = difflib.SequenceMatcher(None, m_fold, a_fold, autojunk=False
                                        ).find_longest_match(0, len(m_fold), 0, len(a_fold))
        anchor = max(0, match.a - match.b) if match.size else 0
    window_end = anchor + int(len(a_compact) * 1.4) + 80
    window = m_fold[anchor:window_end]
    matcher = difflib.SequenceMatcher(None, a_fold, window, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag != "equal":
            continue
        for k in range(i2 - i1):
            out_variants[a_idx[i1 + k]] = variants[anchor + j1 + k]
    return _collapse(a2_text, out_variants)


def _collapse(a2_text, out_variants):
    """Per-character style back into runs."""
    out = []
    for ch, st in zip(a2_text, out_variants):
        v, ital, ink = st if isinstance(st, tuple) else (st, False, None)
        if out and out[-1]["v"] == v and out[-1].get("i", False) == ital \
                and out[-1].get("c") == ink:
            out[-1]["t"] += ch
        else:
            run = {"t": ch, "v": v}
            if ital:
                run["i"] = True
            if ink:
                run["c"] = ink
            out.append(run)
    # A space between two scripts belongs to neither; carrying the variant across it would set
    # the space in "NH3 (Yellow)" as a subscript.
    for run in out:
        if run["v"] and not run["t"].strip():
            run["v"] = ""
    return [r for r in out if r["t"]]


def _locate(a2_text, stream, exact_only=False):
    """(offset, length) of this block's characters inside the page stream, or None.

    `exact_only` refuses the shrinking-anchor fallback. The fallback is right for carrying
    sub/superscript typing across -- a partial alignment still types most of the block correctly
    and types nothing wrongly -- but it is wrong for deciding a block's POINT SIZE, where landing
    on the wrong run of text mis-sizes the whole block. Measured: p007's Example 5.2 and 5.3
    anchored onto the 8pt marginal note beside them and were set at 8pt, against the 10.5pt the
    book prints them at.
    """
    compact_text = stream[0]
    a_compact = "".join(ch for ch in (a2_text or "") if not ch.isspace())
    if not compact_text or not a_compact:
        return None
    a_fold, m_fold = _fold(a_compact), _fold(compact_text)
    offset = m_fold.find(a_fold)
    if offset < 0 and not exact_only:
        for n in (40, 24, 16, 10):
            if len(a_fold) >= n:
                offset = m_fold.find(a_fold[:n])
                if offset >= 0:
                    break
    return (offset, len(a_compact)) if offset >= 0 else None


def block_lines(a2_text, stream):
    """The measured PRINTED LINES this block occupies, in order.

    Located by the same text alignment the typing and the size use, NOT by the block's bounding
    box. The bbox route is wrong in both directions and both were observed: a long block matches
    one small printed block and sees a single line (p020's 1369-character Summary), while a short
    block's box encloses its neighbours' lines and sees far too many (p020's 95-character sentence
    enclosed 22). Locating by text cannot do either -- a block's own characters are its own.
    """
    found = _locate(a2_text, stream)
    if not found:
        return []
    offset, length = found
    line_of, lines = stream[3], stream[4]
    seen, out = set(), []
    for i in line_of[offset:offset + length]:
        if i not in seen:
            seen.add(i)
            out.append(lines[i])
    return out


def block_size_pt(a2_text, stream, body_pt):
    """The point size this block's RUNNING MATTER is set in, or None.

    Derived from the same text alignment the sub/superscript typing uses, NOT from the block's
    bounding box. The bbox route failed on exactly the blocks that matter: a long block matches
    one small printed block, so the lines "inside" it are a single line and the size is unknown.
    p020's Summary is 1369 characters and found one line that way, so it rendered at the body's
    10.5pt where the book sets it at 9.5 -- and that one page overran its sheet by 62% while the
    rest of the chapter overran by 10-25%.

    Sizes outside [0.7, 1.05] x body are excluded: above it are the block's own display labels
    ("Summary" at 16pt, "Example 5.4" at 13pt), below it are script-sized fragments.
    """
    sizes = stream[2]
    found = _locate(a2_text, stream, exact_only=True)
    if not found or not sizes:
        return None
    offset, length = found
    span = [z for z in sizes[offset:offset + length]
            if z and body_pt * 0.7 <= z <= body_pt * 1.05]
    if not span:
        return None
    span.sort()
    return span[len(span) // 2]


def apply_bold(runs, bold_terms):
    """Mark the runs covered by each A2B bold term, longest term first so a short term inside a
    long one cannot steal the match (the same rule the Markdown and HTML exporters already use).

    Returns runs each carrying a `b` flag alongside its `v` variant.
    """
    flat = "".join(r["t"] for r in runs)
    marks = [False] * len(flat)
    for term in sorted(bold_terms or [], key=len, reverse=True):
        term = (term or "").strip()
        if not term:
            continue
        start = flat.find(term)
        if start < 0:
            # The term may be wrapped across a line in A2's text; retry whitespace-insensitively.
            pattern = re.escape(term).replace(r"\ ", r"\s+")
            m = re.search(pattern, flat)
            if not m:
                continue
            start, end = m.start(), m.end()
        else:
            end = start + len(term)
        for i in range(start, end):
            marks[i] = True

    out, pos = [], 0
    for r in runs:
        for ch in r["t"]:
            bold = marks[pos]
            pos += 1
            same = (out and out[-1]["v"] == r["v"] and out[-1]["b"] == bold
                    and out[-1].get("i", False) == r.get("i", False)
                    and out[-1].get("c") == r.get("c"))
            if same:
                out[-1]["t"] += ch
            else:
                nr = {"t": ch, "v": r["v"], "b": bold}
                if r.get("i"):
                    nr["i"] = True
                if r.get("c"):
                    nr["c"] = r["c"]
                out.append(nr)
    return out


# --------------------------------------------------------------------------------------------
def _centre_in(bbox, outer, pad=0.02):
    """True when `bbox`'s centre lies inside `outer` grown by `pad`."""
    if not bbox or not outer:
        return False
    cx = (bbox[0] + bbox[2]) / 2.0
    cy = (bbox[1] + bbox[3]) / 2.0
    return (outer[0] - pad <= cx <= outer[2] + pad
            and outer[1] - pad <= cy <= outer[3] + pad)


def _inside(point_bbox, panel_bbox, pad=0.012):
    """True when a block's measured box sits inside a measured panel."""
    if not point_bbox or not panel_bbox:
        return False
    x0, y0, x1, y1 = point_bbox
    px0, py0, px1, py1 = panel_bbox
    cy = (y0 + y1) / 2.0
    return (px0 - pad <= x0 and x1 <= px1 + pad and py0 - pad <= cy <= py1 + pad)


# How far a neighbour may overlap this block's own column and still count as sitting BESIDE it.
# NCERT lets a margin figure run a little under the text column (p004's EDTA structure ends at
# 0.3125 against prose starting at 0.302), so an exact test calls that figure full-width and
# stacks the prose under it instead of beside it.
_SIDE_TOL = 0.02
# ... and how much of the shorter block's height the two must share before they are "level".
_SIDE_OVERLAP = 0.33


_RE_UNIT_ONLY = re.compile(r"^\s*Unit\s+(\d+)\s*$", re.I)


def _place_unpositioned_in_panels(items):
    """Put a block with no measured position into the panel it is surrounded by.

    Panel membership is decided by position, which cannot place a block that has none: a block
    that matched no printed block carries no bbox, so it falls outside every panel however
    obviously it belongs to one. On Amines p007 that block is the QUESTION of Example 9.3 -- so
    the box came out as an empty "Example 9.3", the question floating unboxed beneath it, and the
    "Solution" in a second box, which is three pieces of one thing.

    Reading order answers it without needing a position: a block sandwiched between two blocks of
    the same panel is inside that panel, because the book does not interleave a box with anything
    else. Only genuinely unplaced blocks are moved, and only when both neighbours agree.
    """
    for i, it in enumerate(items):
        if it.get("bbox") or it.get("panel"):
            continue
        before = next((items[j] for j in range(i - 1, -1, -1) if items[j].get("panel")), None)
        after = next((items[j] for j in range(i + 1, len(items)) if items[j].get("panel")), None)
        if not before or not after:
            continue
        pb, pa = before["panel"], after["panel"]
        if pb.get("bbox") == pa.get("bbox"):
            it["panel"] = pb
            it["role"] = classify(it, pb.get("kind"))[0] if it["role"] == "paragraph" \
                else it["role"]


def _merge_unit_title(items):
    """Join a chapter title that A2 read as two blocks into one.

    NCERT prints "Unit 9" and "Amines" as two lines of one banner, and A2 may read them as one
    block or as two -- Coordination Compounds came through as a single "Unit 5\nCoordination
    Compounds", Amines as a separate "Unit 9" and "Amines". Only the single-block form matched
    the opener pattern, so on Amines the chapter banner was never recognised at all: the page
    opened with two lines of ordinary small type where the book prints a lavender panel, a large
    numeral and the chapter name.

    The pair is unmistakable -- a heading whose entire text is "Unit <n>" followed immediately by
    another heading -- so merging them is safe and leaves the single-block form untouched.
    """
    for i, it in enumerate(items[:-1]):
        if it.get("a2_kind") != "heading":
            continue
        m = _RE_UNIT_ONLY.match(it.get("text") or "")
        if not m:
            continue
        nxt = items[i + 1]
        if nxt.get("a2_kind") != "heading" or not (nxt.get("text") or "").strip():
            continue
        it["role"], it["label"] = "chapter_title", m.group(1)
        it["text"] = "%s\n%s" % (it["text"].strip(), nxt["text"].strip())
        it["runs"] = [{"t": it["text"], "v": "", "b": False}]
        nxt["role"], nxt["text"], nxt["runs"] = "merged_into_title", "", []
        break
    items[:] = [i for i in items if i["role"] != "merged_into_title"]


def _assign_columns(items):
    """Mark each item left / right / full, from what is printed BESIDE it.

    NCERT Chemistry sets a narrow outer column (section headings in script, small structural
    diagrams, figure captions) with the body prose running alongside. Deciding that from an x
    threshold does not survive the real pages: the threshold has to be the body column's left
    edge, and that edge is in a different place on a single-measure page (0.27), on a page whose
    prose wraps around a float (0.453) and on a genuinely two-column page (0.589). The question
    the layout actually turns on is not "how far left is this" but "is something printed next to
    it", which is a fact about the page and needs no threshold at all.
    """
    boxed = [it for it in items if it.get("bbox")]
    for it in boxed:
        x0, y0, x1, y1 = it["bbox"]
        right = left = False
        for other in boxed:
            if other is it or not other.get("bbox"):
                continue
            ox0, oy0, ox1, oy1 = other["bbox"]
            overlap = min(y1, oy1) - max(y0, oy0)
            if overlap <= 0 or overlap < _SIDE_OVERLAP * min(y1 - y0, oy1 - oy0):
                continue
            if ox0 >= x1 - _SIDE_TOL:
                right = True
            elif ox1 <= x0 + _SIDE_TOL:
                left = True
        if right and not left:
            it["column"] = "left"
        elif left and not right:
            it["column"] = "right"
        else:
            it["column"] = "full"
    for it in items:
        if not it.get("bbox"):
            it["column"] = "full"



_WORDY = re.compile(r"[A-Za-z]{3,}")

# Only text containers may be filled from the measurement. Deliberately excludes:
#   figure   -- its measured line is the caption, and writing it into `text` would make the
#               renderer print the caption as prose instead of cropping the diagram (p002's
#               "Fig. 9.1 Pyramidal shape of trimethylamine").
#   table    -- the tables already render in full from A2S; filling them re-prints a subset of
#               the cells, and the dedup guard drops the header row, so the copy is worse.
#   equation -- a displayed scheme's measured lines are reagent labels in geometric order
#               ("NaOHBr", "NaCN", "Partialhydrolysis"), which read as words and so pass the
#               prose test while still being artwork.
_FILLABLE_ROLES = frozenset({
    "note", "example", "example_body", "solution", "summary", "intext", "answer", "objectives",
})


def _line_text(line):
    return "".join(r.get("t", "") for r in (line.get("runs") or []))


def _norm_fold(t):
    return re.sub(r"[^0-9a-z]+", "", (t or "").lower())


def _reads_as_prose(bodies):
    """True when measured lines read in sentence order, not diagram order.

    A displayed structure's lines come back in geometric order -- "K=", "3", "2", "R", "OH" --
    because the PDF draws a formula as scattered glyph runs. Running prose comes back as whole
    lines. The separator is how much of the block is real words: a scheme is mostly one- and
    two-character fragments, a sentence is not. Tried and rejected: line count (tables have many
    short cells and are still wanted) and punctuation (schemes carry commas too).
    """
    if not bodies:
        return False
    chars = sum(len(b) for b in bodies)
    if chars < 25:
        return False
    worded = sum(1 for b in bodies if len(_WORDY.findall(b)) >= 1)
    alpha = sum(1 for b in bodies for c in b if c.isalpha())
    return worded / len(bodies) >= 0.55 and alpha / max(1, chars) >= 0.5


def fill_empty_from_measured(model):
    """Give a block its printed text when A2/A2S left it empty but the page measured text there.

    75 of this chapter's A2S outputs carry no items. For artwork that is correct -- a diagram has
    no transcription. But some of those blocks are prose: the whole body of Example 9.1, the
    Answers lines, two basicity orders. That text is not lost, it is in the PDF's own text layer
    and `chemistry_measure` already read it, so the render can take it from there rather than
    leave a drawn-but-empty box.

    Two guards, both learned from getting it wrong:

    * Only prose. `_reads_as_prose` keeps scrambled structure labels out; they stay artwork.
    * Only text no other block already shows. A needs_special bbox routinely reaches into the
      paragraph above, so the measured lines often repeat a sentence that is already rendered in
      its own block. Filling those is what printed "For example:" and "Larger the value of Kb"
      twice. The page's own A2 text is the authority on what is already shown.
    """
    filled = 0
    for page in model.get("pages") or []:
        head = _norm_fold(page.get("running_header") or "")
        shown = _norm_fold(" ".join((i.get("text") or "") for i in page.get("items") or []))
        for item in page.get("items") or []:
            if item.get("role") not in _FILLABLE_ROLES:
                continue
            if (item.get("text") or "").strip() or (item.get("special") or []):
                continue
            # Reading order, not list order. The measurement lists lines as the PDF draws them,
            # which puts a box's label ("Example 9.2", set larger and further left) after the
            # body it labels. Sorting by baseline then left edge recovers the printed order.
            lines = sorted((item.get("lines") or []),
                           key=lambda L: (round(L["bbox"][1], 3), L["bbox"][0]))
            bodies = [t for t in (_line_text(L) for L in lines) if t.strip()]
            # The folio and running header sit outside the box but inside its measured bbox.
            bodies = [b for b in bodies
                      if not b.strip().isdigit() and _norm_fold(b) != head]
            fresh = [b for b in bodies if _norm_fold(b) and _norm_fold(b) not in shown]
            if len(fresh) < len(bodies):
                # Part of this block is already on the page: the bbox over-reached into a
                # neighbour. Keep only what is new, and require that remainder to stand alone.
                bodies = fresh
            if not _reads_as_prose(bodies):
                continue
            # The renderer sets `runs`, not `text` -- `text` alone left these boxes as empty as
            # before. Rebuilding runs from the same measured lines also keeps what the text layer
            # knows about each glyph: sub/superscript variant, italic and colour all survive,
            # which plain text would have flattened.
            runs, keep = [], set(id(b) for b in bodies)
            for line in lines:
                body = _line_text(line)
                if not body.strip() or body not in bodies:
                    continue
                for r in (line.get("runs") or []):
                    if not r.get("t"):
                        continue
                    runs.append({"t": r["t"], "v": r.get("v", ""), "b": False,
                                 "i": r.get("i", False), "c": r.get("c")})
                runs.append({"t": " ", "v": "", "b": False, "i": False, "c": None})
            if runs and runs[-1]["t"] == " ":
                runs.pop()
            if not runs:
                continue
            item["text"] = "\n".join(bodies)
            item["runs"] = runs
            item["text_from_measured"] = True
            filled += 1
    return filled


def _is_prose_line(text):
    """A full sentence of the body, as opposed to a glyph run belonging to a diagram.

    A figure's own labels come through as tiny runs -- "O", "Cl", "CH", "2", "5+HCl". The
    paragraph above it comes through as one long multi-word line. Length plus word count
    separates them; nothing subtler is needed, and anything subtler misfires on "+ HCl".
    """
    t = (text or "").strip()
    return len(t) >= 18 and len(t.split()) >= 3


def grow_art_to_block(model):
    """Widen each figure's art region out to its block, as far as no prose blocks the way.

    The art region is found by clustering vector ink, and clustering systematically loses the
    parts of a drawing that are *typeset* rather than stroked. A2R caught both failure modes in
    this chapter:

      p013  the two upper sulphonyl oxygens of the Hinsberg scheme sit 0.015 above the top of
            the ink cluster, so the crop sliced them off and the scheme showed S with no =O.
      p002  the trimethylamine annotation ("unshared electron pair", 108 degrees) sits to the
            right of the cluster, so Fig. 9.1 printed as a bare blue N and three lines.

    A2's own block box already says how far the figure extends. So the art region can be grown
    out to it, edge by edge, stopping at the first prose line in the way -- which is what keeps
    the neighbouring paragraph out of the crop. Where there is no prose between the ink and the
    block edge, as on p002, the whole block is the figure.
    """
    grown = 0
    for page in model.get("pages") or []:
        prose = []
        for item in page.get("items") or []:
            for line in item.get("lines") or []:
                if _is_prose_line(_line_text(line)):
                    prose.append(line["bbox"])
        for item in page.get("items") or []:
            art, box = item.get("art_bbox"), item.get("bbox")
            if not art or not box:
                continue
            new = list(art)
            # Top and bottom: a prose line only blocks if it overlaps the art horizontally.
            over = [b for b in prose if b[2] > art[0] and b[0] < art[2]]
            above = [b[3] for b in over if b[3] <= art[1] + 0.004]
            below = [b[1] for b in over if b[1] >= art[3] - 0.004]
            new[1] = max(box[1], max(above) + 0.004) if above else min(new[1], box[1])
            new[3] = min(box[3], min(below) - 0.004) if below else max(new[3], box[3])
            # Left and right: grow to the block unless prose shares those rows.
            rows = [b for b in prose if b[3] > new[1] and b[1] < new[3]]
            left = [b[2] for b in rows if b[2] <= art[0] + 0.004]
            right = [b[0] for b in rows if b[0] >= art[2] - 0.004]
            new[0] = max(box[0], max(left) + 0.004) if left else min(new[0], box[0])
            new[2] = min(box[2], min(right) - 0.004) if right else max(new[2], box[2])
            if new[2] - new[0] > 0.01 and new[3] - new[1] > 0.01 and new != list(art):
                item["art_bbox"] = [round(v, 4) for v in new]
                item["art_grown"] = True
                grown += 1
    return grown

def build(chapter, measurement):
    """The chapter model: {"chapter":..., "pages": [{"page":n, "items": [...]}, ...]}.

    Every item carries both what it SAYS (role, label, runs, caption, rows) and where it is
    PRINTED (column, panel, bbox), so the Markdown and the HTML can each take what they need from
    one agreed reading of the chapter.
    """
    pages_a2 = _best_page_outputs(chapter)
    by_page = {p["page"]: p for p in measurement["pages"]}
    trim_w, trim_h = measurement["trim_pt"]
    px_w, px_h = trim_w / 72.0 * _A2_DPI, trim_h / 72.0 * _A2_DPI
    body_col = measurement["text_measure"]["body_column"]

    model = {"chapter": chapter, "trim_pt": measurement["trim_pt"],
             "trim_mm": measurement["trim_mm"],
             "body_size_pt": measurement["body_size_pt"],
             "palette": measurement["palette"],
             "text_measure": measurement["text_measure"],
             "pages": []}

    for page_num, (run_label, rec) in pages_a2.items():
        meas = by_page.get(page_num, {})
        blocks = rec.get("blocks") or []
        item_id = "%s-p%03d" % (chapter, page_num)
        a2b = _load_sibling_json("A2B", item_id) or {}
        a2n = _load_sibling_json("A2N", item_id) or {}
        bold_by_n = {b["n"]: b.get("bold_terms") or [] for b in a2b.get("blocks", [])}
        corr_by_n = {b["n"]: b for b in a2n.get("blocks", []) if b.get("corrected_text")}

        pre_roles = {b["n"]: classify(b, None)[0] for b in blocks if isinstance(b.get("n"), int)}
        matched = match_blocks(blocks, meas.get("text_blocks", []), pre_roles)
        stream = page_variant_stream(meas.get("text_blocks", []))
        panels = meas.get("panels", [])
        art = meas.get("art_regions", [])

        items = []
        for b in blocks:
            n, kind = b.get("n"), b.get("kind")
            m = matched.get(n, {}).get("measured")
            bbox = m["bbox"] if m else None

            # A2's own bbox (figures, tables, equations) is in 200-dpi pixels; convert so that
            # everything downstream speaks one coordinate system.
            if not bbox and b.get("bbox"):
                x0, y0, x1, y1 = b["bbox"]
                bbox = [x0 / px_w, y0 / px_h, x1 / px_w, y1 / px_h]

            panel = next((p for p in panels if _inside(bbox, p["bbox"])), None)
            role, label = classify(b, panel["kind"] if panel else None)

            # A numbered EXERCISE STEM is not a section heading, however alike they look.
            #
            # "9.5 How will you convert:" and "9.5 Bonding in Coordination Compounds" match the
            # same pattern, so the exercises came out set in the margin in the book's display
            # face, detached from the list each one introduces. Text cannot separate them -- but
            # the measurement can: a section heading is printed in the script face, an exercise
            # stem in body type. Where the two disagree, the page wins.
            # The demotion must also fire when the block matched NOTHING. An exercise stem is
            # not printed in the script face, so it never matches a margin-heading block and `m`
            # is None -- which an "m and ..." test skips, leaving every stem in the margin. The
            # chapter's real section headings all match (p018's "9.10 Importance of Diazonium
            # Salts" scores 0.79); the four exercise stems score nothing at all.
            if role == "margin_heading" and (
                    m is None or m.get("role") not in
                    ("margin_heading", "display_script", "chapter_title")):
                role = "list" if "\n" in text else "paragraph"

            # The opener's strap line is set in the book's magenta italic, and nothing in its
            # TEXT says so -- it reads as an ordinary sentence, which is how every earlier render
            # set it. The measurement knows its ink, so the role is taken from the ink.
            if role == "paragraph" and m:
                inks = [ln.get("color") for ln in m.get("lines", []) if ln.get("color")]
                if inks and all(i == inks[0] for i in inks) and inks[0] == "#ec008c":
                    role = "strapline"

            fix = corr_by_n.get(n)
            text = repair_glyphs(
                (fix["corrected_text"] if fix else (b.get("text") or "")).strip())
            runs = apply_bold(transfer_variants(text, stream), bold_by_n.get(n))

            a2s = _load_sibling_json("A2S", "%s-b%s" % (item_id, n)) if b.get("needs_special") else None

            item = {
                "n": n, "a2_kind": kind, "role": role, "label": label,
                "text": text, "runs": runs,
                "bbox": [round(v, 4) for v in bbox] if bbox else None,
                "match_score": matched.get(n, {}).get("score"),
                "notation_corrected": bool(fix),
                "panel": ({"kind": panel["kind"], "tab_side": panel["tab_side"],
                           "bbox": panel["bbox"]} if panel else None),
                "column": None,
            }
            # Column is resolved after the whole page is read -- see _assign_columns.
            # Every printed LINE inside this block's own box, with its position and its typing.
            # Two things need it, and neither can be answered from A2's text alone:
            #   * a block the book sets in COLUMNS (p003's Solution runs "(i) ... (ii) ..." across
            #     the panel, not down it) -- the arrangement is in the line positions, and A2's
            #     text records only the reading order;
            #   * a special block A2S has not transcribed -- this book has its words in the text
            #     layer even when no agent has read the block, so there is no reason to print
            #     "not yet transcribed" over content we can read.
            # Where the panel's own label is printed. NCERT sets "Example 9.3", "Solution" and
            # "Summary" in a display script that cannot be licensed into this export, so the
            # renderer takes them as vector from the page itself -- these are decorative marks
            # nobody searches for, and they are where the book's character is most visible.
            if role in ("example", "solution", "summary", "objectives"):
                want = _norm(_first_line(text))
                for tb in meas.get("text_blocks", []):
                    for ln in tb.get("lines", []):
                        if ln.get("role") not in ("panel_label", "display_script",
                                                  "margin_heading"):
                            continue
                        if _norm("".join(r["t"] for r in ln["runs"])) == want:
                            item["label_bbox"] = ln["bbox"]
                            break
                    if item.get("label_bbox"):
                        break

            located = block_lines(text, stream)
            if not located and not text and bbox:
                # A needs_special block carries no text of its own, so there is nothing to locate
                # it by -- fall back to the lines printed inside its recorded box. This is what
                # lets p002's tabulated "1 mol CoCl3.6NH3 (Yellow) gave 3 mol AgCl" rows be set as
                # type: A2 marked them special and transcribed nothing, but the words are right
                # there in the layer.
                located = [ln for tb in meas.get("text_blocks", [])
                           for ln in tb.get("lines", [])
                           if _inside(ln["bbox"], bbox, pad=0.012)]
            item["lines"] = [
                {"bbox": ln["bbox"], "runs": ln["runs"], "size": ln.get("size")}
                for ln in located
            ]
            item["measured_lines"] = [
                {"bbox": ln["bbox"], "runs": ln["runs"], "size": ln.get("size"),
                 "role": ln.get("role")}
                for tb in meas.get("text_blocks", [])
                for ln in tb.get("lines", [])
                if _inside(ln["bbox"], bbox, pad=0.012)
            ] if bbox else []

            if a2s:
                item["caption"] = a2s.get("caption") or ""
                item["labels"] = a2s.get("labels") or []
                item["latex"] = a2s.get("latex") or ""
                item["header"] = a2s.get("header") or []
                item["rows"] = a2s.get("rows") or []
                item["box_text"] = a2s.get("text") or ""
                item["number"] = a2s.get("number") or ""
            elif b.get("needs_special"):
                item["untranscribed"] = True
                # ... but only REPORT it as missing if the page really has nothing to show. On
                # this book the text layer usually does, so an untranscribed equation is still
                # rendered as text rather than as an apology.
                if item["measured_lines"] and kind in ("equation", "box"):
                    item["recovered_from_text_layer"] = True
                    item["runs"] = [r for ln in item["measured_lines"] for r in
                                    (ln["runs"] + [{"t": "\n", "v": ""}])]

            # The size this block is actually SET in. NCERT does not set the whole chapter at one
            # size: body prose is 10.5pt, but the Summary, the Exercises, the Answers and every
            # table body are 9.5pt. Rendering all of them at the body size is what made those four
            # pages overrun their sheet by 38-62% while the rest of the chapter overran by 10-25%,
            # and "shrink the whole book until the worst page fits" is the wrong answer to a
            # problem only four pages have.
            #
            # Lines led by a script-sized span are excluded: a line that happens to begin with a
            # superscript reports the superscript's size, and on p023 that elected 5.5pt as the
            # size of the entire Answers section.
            # Bounded ABOVE as well as below. A block carries its own display furniture inside
            # it -- the 24pt script "Objectives", the 16pt "Summary", the 13pt "Example 5.4" --
            # and those lines are not the size the RUNNING MATTER is set in. Taking an unbounded
            # median elected them and made the worst page overrun 118% instead of 62%. Running
            # matter in this book is never set larger than the body size, so anything above it is
            # a label and anything far below it is a script-sized fragment.
            body_pt = measurement.get("body_size_pt") or 10.5
            item["size_pt"] = block_size_pt(text, stream, body_pt)
            if item["size_pt"] is None:
                real = sorted(ln["size"] for ln in item["measured_lines"]
                              if ln.get("size") and body_pt * 0.7 <= ln["size"] <= body_pt * 1.05)
                item["size_pt"] = real[len(real) // 2] if real else None

            # A table whose cells DESCRIBE a drawing instead of transcribing it cannot be set as
            # type. A2S returned "NH2 (on a drawn benzene ring)" for four rows of Table 9.1 --
            # that is a note to a human, not a cell value, and rendering it prints the description
            # where the book prints a structure. Such a table is shown as the book draws it.
            if role == "table":
                cells = [str(c) for r in (item.get("rows") or []) for c in r]
                item["describes_artwork"] = any(
                    re.search(r"\(\s*(?:on a |a )?drawn\b|\bnot transcribed\b", c, re.I)
                    for c in cells)

            if role == "table" and bbox:
                # Every printed line inside the table's own box, with its sub/superscript typing
                # intact. A2S transcribes a cell as a flat string ("[Co(NH3)6]3+3Cl-"), which is
                # right for a data table and wrong for a chemistry one: the book sets those
                # digits as subscripts and that charge as a superscript. Keeping the measured
                # lines here lets the renderer re-type each cell from the book's own glyphs.
                item["cell_runs"] = [
                    ln["runs"] for tb in meas.get("text_blocks", [])
                    for ln in tb.get("lines", [])
                    if _inside(ln["bbox"], bbox, pad=0.015)
                ]

            # Does this block's region contain any ARTWORK at all? A "table" or "figure" that
            # A2 marked special but whose region is pure type -- p002's four "1 mol CoCl3.6NH3
            # (Yellow) gave 3 mol AgCl" rows are a tabulated paragraph, not a drawing -- has
            # nothing to crop, and cropping it ships a picture of text.
            if bbox:
                item["has_artwork"] = any(_inside(a["bbox"], bbox, pad=0.02) for a in art)

            if role == "figure" and bbox and not (item.get("caption") or "").strip():
                # A2S did not transcribe this figure's caption, but the book prints one and the
                # text layer has it. Taking the caption-role lines printed directly beneath the
                # artwork recovers it -- Figs 5.13 and 5.14 lost their captions entirely this way.
                fx0, fy0, fx1, fy1 = bbox
                # Searched INSIDE the figure's box as well as under it. NCERT sets a caption in
                # the margin beside the artwork as often as beneath it, and A2's recorded bbox
                # encloses both -- "Fig. 5.13" sits at y 0.239 inside a figure spanning 0.080 to
                # 0.312. A below-only window found neither of this chapter's lost captions.
                # Filtered on the LINE's role, not the block's. A block's role is the role of
                # most of its lines, so a caption printed inside a block of prose is filed under
                # "body" and a block-level filter never sees it -- which is why neither lost
                # caption was found on the first attempt.
                below = [ln for tb in meas.get("text_blocks", [])
                         for ln in tb.get("lines", [])
                         if ln.get("role") in ("caption_or_letter_heading", "demi")
                         and fy0 - 0.01 <= ln["bbox"][1] <= fy1 + 0.075
                         and ln["bbox"][0] >= fx0 - 0.06 and ln["bbox"][2] <= fx1 + 0.12]
                text_below = " ".join(
                    "".join(r["t"] for r in ln["runs"]) for ln in
                    sorted(below, key=lambda l: (round(l["bbox"][1], 3), l["bbox"][0])))
                # Only a line that actually announces itself as a caption. Caption-role type also
                # carries lettered sub-headings and in-figure labels, and neither is a caption.
                if re.match(r"^\s*(Fig|Table)\s*\.?\s*\d", text_below):
                    item["caption"] = re.sub(r"\s+", " ", text_below).strip()
                    item["caption_lines"] = [{"bbox": ln["bbox"], "runs": ln["runs"]}
                                             for ln in below]
                    item["caption_recovered"] = True

            if role == "figure" and bbox and (item.get("caption") or ""):
                # The caption's printed lines: caption-role type sitting just under or beside the
                # artwork. Needed both to re-type the caption and to keep it OUT of the crop.
                cx0, cy0, cx1, cy1 = bbox
                item["caption_lines"] = [
                    {"bbox": ln["bbox"], "runs": ln["runs"]}
                    for tb in meas.get("text_blocks", [])
                    for ln in tb.get("lines", [])
                    if ln.get("role") in ("caption_or_letter_heading", "demi")
                    and ln["bbox"][1] >= cy0 - 0.02 and ln["bbox"][3] <= cy1 + 0.09
                    and ln["bbox"][0] >= cx0 - 0.05 and ln["bbox"][2] <= cx1 + 0.12
                ]

            if role == "figure" and bbox:
                # The artwork this figure block refers to: every measured ink region inside its
                # recorded box, unioned. Cropping the union rather than the recorded box is what
                # keeps a two-part figure (a mirror-image pair) whole without also sweeping in the
                # paragraph beside it.
                # Selected by the region's CENTRE, not by full containment.
                #
                # Containment was the defect behind every bad crop in this chapter. A measured
                # artwork region that pokes a few thousandths past A2's recorded box -- which they
                # routinely do, because A2 draws its box around what it reads and the ink does not
                # respect it -- was dropped entirely. The surviving regions then covered only part
                # of the figure, so the crop cut the drawing; and when too little survived, the
                # 35% rule fell back to A2's box, which on a page like p002 runs from x 0.368 to
                # 0.892 and takes the whole paragraph with it. Either way the crop was wrong, and
                # the two failures look opposite but share this one cause.
                #
                # A region's centre tells you whose figure it is without needing it to fit inside
                # anything, and a neighbouring figure's region is centred elsewhere.
                inside = [a for a in art if _centre_in(a["bbox"], bbox, pad=0.025)]
                union = None
                if inside:
                    union = [round(min(a["bbox"][0] for a in inside), 4),
                             round(min(a["bbox"][1] for a in inside), 4),
                             round(max(a["bbox"][2] for a in inside), 4),
                             round(max(a["bbox"][3] for a in inside), 4)]
                # Tightening to the measured ink is right when the ink IS the figure, and wrong
                # when the figure is drawn mostly with TYPE. Fig 5.13 sets Ni(CO)4, Fe(CO)5,
                # Cr(CO)6, Mn2(CO)10 and Co2(CO)8 almost entirely as lettering with a handful of
                # bonds, so only one 8-stroke cluster registered and the crop came out as a
                # fragment of the last structure with a hole where the figure should be. A2's
                # recorded bbox is the authority on a figure's extent; the ink union may only
                # tighten it, never shrink it to a corner of it.
                # The ink is only half of a figure. Its LABELS -- "CH3", "108 deg", "unshared
                # electron pair", "Phthalimide" -- are text, absent from the measured ink, and a
                # crop taken from ink alone cuts every one of them off.
                #
                # Which text is a label is NOT guessed from geometry. Ten attempts were made to
                # infer it from shape and position, and every one either cut the artwork or pulled
                # the last line of the paragraph above into the crop, because A2's figure box and
                # the measured ink disagree about where a figure begins and the stray line sits in
                # the gap between them. A2S has already answered the question directly: its
                # `labels` field lists the text printed inside this figure. Matching against that
                # list is exact, and it is the only source here that actually knows.
                # Matched on LONG labels only, and on whole lines.
                #
                # A2S lists every piece of text in a figure, including "N", "O", "CH3" and "R".
                # Matching those as substrings pulls in any line of prose that happens to contain
                # them -- which is every line -- and drags the crop back over the paragraph above.
                # The long labels ("unshared electron pair", "Phthalimide", "N-Alkylphthalimide")
                # identify a figure's text unambiguously; the short ones sit among the ink and are
                # already inside the box the strokes give.
                if union and (item.get("labels") or []):
                    wanted = {_norm(l) for l in item["labels"] if len(_norm(l)) >= 6}
                    for tb in meas.get("text_blocks", []):
                        for ln in tb.get("lines", []):
                            txt = _norm("".join(r["t"] for r in ln["runs"]))
                            if len(txt) < 6 or not any(txt == w for w in wanted):
                                continue
                            if not _centre_in(ln["bbox"], union, pad=0.05):
                                continue        # the same words elsewhere on the page
                            lb = ln["bbox"]
                            union = [min(union[0], lb[0]), min(union[1], lb[1]),
                                     max(union[2], lb[2]), max(union[3], lb[3])]

                def _area(b):
                    return max(0.0, b[2] - b[0]) * max(0.0, b[3] - b[1])
                if union and _area(union) >= 0.35 * _area(bbox):
                    item["art_bbox"], item["art_kinds"] = union, sorted(
                        set(a["kind"] for a in inside))
                else:
                    item["art_bbox"] = item["bbox"]
                    item["art_kinds"] = sorted(set(a["kind"] for a in inside)) if inside else []
            items.append(item)

        _place_unpositioned_in_panels(items)
        _merge_unit_title(items)
        _assign_columns(items)
        model["pages"].append({
            "page": page_num,
            "run": run_label,
            "folio": _folio_of(rec),
            "running_header": _running_header_of(rec),
            "imprint": _imprint_of(rec),
            "continues": bool(rec.get("first_block_continues_from_previous")),
            "furniture": meas.get("furniture", []),
            "panels": panels,
            "body_column": meas.get("body_column"),
            "margin_column": meas.get("margin_column"),
            "items": items,
        })
    # A folio the book prints but A2 did not record.
    #
    # The page number is read off the page as removed furniture, and on four pages of Amines A2
    # simply did not list it -- so those sheets printed with no footer at all, which A2R flagged
    # on p012, p016, p021 and p022. A chapter's folios run consecutively, so a gap can be filled
    # from its neighbours with certainty rather than guessed.
    known = [(i, int(p["folio"])) for i, p in enumerate(model["pages"])
             if (p["folio"] or "").isdigit()]
    if known:
        base_i, base_n = known[0]
        for i, page in enumerate(model["pages"]):
            if not (page["folio"] or "").isdigit():
                page["folio"] = str(base_n + (i - base_i))
                page["folio_inferred"] = True

    model["filled_from_measured"] = fill_empty_from_measured(model)
    model["art_grown"] = grow_art_to_block(model)
    return model


_RE_YEAR = re.compile(r"^\s*(?:Reprint\s+)?\d{4}\s*-\s*\d{2,4}\s*$", re.I)


def _folio_of(rec):
    for t in rec.get("running_header_footer_removed") or []:
        if t.strip().isdigit():
            return t.strip()
    return ""


def _running_header_of(rec):
    for t in rec.get("running_header_footer_removed") or []:
        s = t.strip()
        if s and not s.isdigit() and not _RE_YEAR.match(s):
            return s
    return ""


def _imprint_of(rec):
    for t in rec.get("running_header_footer_removed") or []:
        if _RE_YEAR.match(t.strip()):
            return t.strip()
    return ""


def load_measurement(chapter):
    path = rc.pp("exports", "review", "html_data", chapter + "_inorganic_layout.json")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)
