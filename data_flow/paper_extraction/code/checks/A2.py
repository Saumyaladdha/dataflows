"""Step-specific check for A2 (spec Section 9/A2 'Checks'):
  (1) pages read = PDF pages -- a whole-book aggregate, not a single page's concern; enforced at
      the plugin level (every page 1..N gets an A2 item) rather than here.
  (2) page N's last_block_continues_on_next == page N+1's first_block_continues_from_previous --
      a cross-item (pair-of-pages) check; this build raises A2_JOIN_ADJUDICATED for a mismatch at
      the plugin level once both pages have output, not in this single-page check.
  (3) with a text layer, the blocks' text matches it -- implemented below, see
      "Comparing blocks against the text layer".
  (4) no header/footer text inside blocks -- implemented below, see "Header/footer limb".

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring.
context["input_data"] is the A2 work input: book_id, page, image, text_layer (whole-page text, or
None/empty for an image-only page), previous_page_last_block.


Comparing blocks against the text layer
---------------------------------------
Spec 9/A2 asks for ">= 99% of characters after whitespace normalisation". Implemented literally
(paragraph-only block text vs. the whole raw page text layer, difflib `quick_ratio`) that bar is
not a fidelity check at all -- measured on all 104 real A2 outputs in steps/A2/out it failed 89
of them (86%), including pages independently confirmed correct against the page image, while
failing deliberately corrupted block sets at 82-93%. A test that fires on 86% of correct output
and 90% of wrong output carries almost no information (Youden's J ~= 0-7 points per error class).

Three real PDF-extraction artifacts, all verified directly against real NCERT pages and page
images, are why a naive comparison cannot work. None is an agent error:

  (a) NON-PARAGRAPH TEXT IS REAL PAGE TEXT. Comparing paragraph-only block text against the
      whole page's layer structurally penalises every page that mixes paragraphs with
      headings/boxes/lists -- the heading and list characters are in the layer but can never be
      credited. Physics/Chemistry pages are far more heading/box/list dense than Biology prose.
      Fix: compare ALL block kinds' text.

  (b) OUTLINE/SHADOW-FONT SIDE-HEADINGS ARE EXTRACTED 5x DUPLICATED AND OUT OF READING ORDER.
      NCERT draws section side-headings in a layered outline font; each layer is a separate
      text run. Real example, CHE12L-ch09-p017's layer, verbatim, at the very END of the stream
      (after every body paragraph) and interleaved with the running header/footer:
          9.8 / 9.8 / 9.8 / 9.8 / 9.8 / Physical / Physical / Physical / Physical / Physical /
          Properties / Properties / Properties / Properties / Properties / 9.9 / 9.9 / ...
      A faithful, correctly-ordered transcription therefore cannot score high ORDERED similarity
      against the raw layer. Fix: collapse runs of identical consecutive lines, and do not
      require the agent's block ORDER to match the layer's (see "order" below).

  (c) SUB/SUPERSCRIPT FORMULAE ARE EXTRACTED CHARACTER-SCRAMBLED. Every subscript/superscript in
      a chemical formula or equation becomes its own line, hoisted out of position. Real example,
      CHE12L-ch09-p016's layer for the formula "RN2+X-":
          "The diazonium salts have the general formula " / "-" / "2" / "R N X" / " where R stands"
      and for "C6H5N2+Cl-":  "-" / "2" / "6" / "5" / "C H" / "N" / "Cl".
      The layer is not merely reordered here, it is scrambled below the word level, so no
      character-level comparison against it can be trusted on formula-dense content.
      Fix: compare a PROSE-WORD stream -- purely alphabetic tokens of >= 3 characters, which is
      exactly the material a PDF text layer renders reliably and exactly what sub/superscript
      debris (single letters, digits, signs) is excluded from. Formula fidelity is not abandoned:
      it is covered by the separate numeric-token limb below and by A2S for special blocks.

The resulting four limbs, with thresholds chosen by measuring all 104 real A2 outputs against
seven families of deliberately corrupted block sets (see tests/test_a2_check.py):

  prose precision   Per block, the fraction of that block's prose words lying in matching runs
   (>= 0.95)        of >= 3 words shared with the layer, length-weighted across blocks. Order is
                    enforced WITHIN a block (difflib's matching runs are monotonic) but a block
                    may sit anywhere in the layer, because artifact (b) proves the layer's block
                    order is not reading order. This is strictly STRONGER than the old check,
                    which used `quick_ratio` -- a bag-of-characters measure that ignored order
                    entirely. Real floor 0.956; catches paraphrase 100%, word-scramble 96%.

  numeric precision Every multi-digit number appearing in block text must appear somewhere in
   (== 1.0)         the layer. Order-free, because artifact (c) scrambles where digits land, but
                    not which digits exist. Real value: exactly 1.000 on all 104 real outputs;
                    catches corrupted numbers/quantities 100%. This is the limb that protects
                    numerical fidelity (NEET answers turn on these digits).

  worst unit        The weakest sentence-ish unit (>= 10 prose words) must still score >= 0.75
   (>= 0.75)        prose-word coverage. Localises an error that a page-wide average dilutes.

  coverage limbs    When the page defers NOTHING to A2S (no needs_special block, no empty-text
   (conditional)    block), the layer must be fully explained: prose-word recall >= 0.99 and no
                    unexplained contiguous run of > 10 layer prose words. When the page DOES
                    defer content, those limbs are not computable -- the deferred table/figure
                    text is in the layer with no block text to match it (real example:
                    PHY11L-ch08-p007 defers Table 8.3 and Table 8.4, leaving a legitimate
                    120-prose-word unexplained run) -- so only a loose wholesale-failure bar
                    (recall >= 0.50) applies, and A2S's own check covers that content instead.

Honest limits, deliberately recorded rather than papered over: this check catches whole-block
paraphrase and word-scrambling essentially always, and corrupted digits always, but a SINGLE
substituted word inside one paragraph of a 400-word page is only caught ~9-13% of the time --
one word is 0.25% of the page, below any page-level bar. The old check did not catch those
either (its 85% "catch" came with an 86% false-positive rate, i.e. no signal). Cross-checking
individual words needs a second independent reading of the page, not a tighter threshold.


Header/footer limb
------------------
The old limb asked `if stamp in block_text` -- a bare substring test. Two real false-positive
families, both confirmed on real data:
  - a numeric stamp that is also a number in prose: page "50" vs "the past 50 years";
  - a title-word stamp that is also a content word: CHE12L-ch09's running header is "275 Amines",
    so the stamp "Amines" fired on every block discussing amines -- really happened on
    CHE12L-ch09-p007 (n=14), -p009 (n=4, n=8) and -p019 (n=5), all inspected and all correct
    transcriptions.
A running header/footer that an agent failed to strip survives as its OWN line, never as a word
inside a sentence. So the limb now flags a stamp only when it occupies a whole line of a block's
text (or a whole run of consecutive lines, for a stamp the agent split across lines), which is
precisely the defect the check exists to catch and never fires on prose usage.
"""
import difflib
import re

from lib.text_normalise import normalise_quote
from lib.latex_normalise import normalise as latex_normalise

# --- thresholds (see the module docstring for how each was measured) ---
MIN_PROSE_WORD_LEN = 3      # shorter tokens are sub/superscript debris in the layer
MIN_MATCH_RUN = 3           # prose words; a shared run must be at least this long to count
UNIT_MIN_WORDS = 10         # smallest sentence-ish unit scored on its own
BLOCK_MIN_WORDS = 4         # smallest whole block scored on its own
PROSE_PRECISION_MIN = 0.95
WORST_UNIT_MIN = 0.75
WORST_BLOCK_MIN = 0.70      # real floor measured at 0.778 (hyphenated chemical names in boxes)
RECALL_MIN_STRICT = 0.99    # page defers nothing to A2S
RECALL_MIN_DEFERRED = 0.50  # page defers a table/figure/equation to A2S
MAX_UNEXPLAINED_RUN = 10    # layer prose words, strict pages only


def _prose_words(s):
    """The tokens a PDF text layer renders reliably: purely alphabetic, >= 3 characters.
    Excludes digits, single letters and symbols -- i.e. exactly the material NCERT's
    sub/superscript formulae get scrambled into (artifact (c))."""
    cleaned = normalise_quote(latex_normalise(s or ""))
    return [w.lower() for w in re.findall(r"[A-Za-z]+", cleaned)
            if len(w) >= MIN_PROSE_WORD_LEN]


# PDF text extraction flattens superscripts: NCERT's "2.0 × 10¹¹ Pa" comes out of the text layer
# as "2.0 × 1011 Pa". Before this mapping, a CORRECT transcription that kept the superscript
# yielded the token "10" while the layer yielded "1011", so the two could never match and the
# faithful transcription FAILED A2_TEXT_MISMATCH. Agents then did the rational thing under the
# step's "copy the text layer exactly" rule and flattened the exponent to satisfy the checker --
# writing semantically wrong numbers into passage text that D4 later quotes as verified NCERT.
# Found corpus-wide: 60 instances across Biology, Chemistry and Physics, including Young's modulus
# of steel rendered as "2.0 × 1011 Pa".
#
# Folding the Unicode sub/superscript digits to ASCII makes the correct transcription and the
# flattened layer compare EQUAL, which removes the pressure to corrupt. It deliberately does not
# try to distinguish them: this is a fidelity heuristic, and the right behaviour when the layer
# cannot represent a distinction is to stop penalising it, not to invent a stricter test.
# CRITICAL: fold ONLY a script-digit run that directly follows an ASCII digit, i.e. a true
# exponent like 10¹¹. Folding unconditionally is wrong and was caught on real data: Raoult's-law
# notation `p₂⁰` (pure vapour pressure of component 2) collapsed to `p20`, manufacturing a number
# "20" that exists nowhere on the page and failing three otherwise-correct Chemistry pages. The
# same would happen to every `H₂SO₄`. A script attached to a LETTER is part of a symbol's name,
# not a quantity, so it must be left alone.
_SCRIPT_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉"
_SCRIPT_TO_ASCII = str.maketrans(_SCRIPT_DIGITS, "01234567890123456789")
_EXPONENT_RE = re.compile(rf"(?<=\d)([{_SCRIPT_DIGITS}]+)")

# LaTeX exponents reach the same flattened shape, with the same letter-vs-number distinction:
# 10^{11} -> 1011, but p_2^0 must stay untouched.
_LATEX_EXPONENT_RE = re.compile(r"(?<=\d)[\^_]\s*\{?\s*(\d+)\s*\}?")


def _numbers(s):
    """Multi-digit numbers. Single digits are skipped: they are both the commonest
    sub/superscript debris and too weak to carry a fidelity signal.

    Unicode sub/superscript digits and LaTeX ^{n}/_{n} are folded into the adjacent number first,
    so a superscripted exponent compares equal to the text layer's flattened form -- see the
    comment above `_DIGIT_FOLD` for why that matters."""
    raw = _EXPONENT_RE.sub(lambda m: m.group(1).translate(_SCRIPT_TO_ASCII), s or "")
    raw = _LATEX_EXPONENT_RE.sub(r"\1", raw)
    cleaned = normalise_quote(latex_normalise(raw))
    return [t for t in re.findall(r"\d+", cleaned) if len(t) >= 2]


def _stamp_variants(stamps):
    """A running stamp and its whitespace-separated parts. NCERT headers are composites like
    '275 Amines' or 'Chemistry 274', and the layer splits them onto separate lines, so both the
    whole stamp and each part must be recognisable as a running-stamp line."""
    out = set()
    for stamp in stamps or []:
        s = normalise_quote(stamp or "").strip()
        if not s:
            continue
        out.add(s)
        for part in s.split(" "):
            if part:
                out.add(part)
    return out


def _layer_lines(text_layer, stamps):
    """Normalise the page's text layer into comparable lines:
    drop blank lines, drop running header/footer lines, and collapse runs of identical
    consecutive lines (artifact (b): outline-font headings extract 5x duplicated)."""
    variants = _stamp_variants(stamps)
    lines = []
    for raw in (text_layer or "").splitlines():
        s = normalise_quote(raw).strip()
        if not s or s in variants:
            continue
        if lines and lines[-1] == s:
            continue
        lines.append(s)
    return lines


def _min_run_for(seq):
    """The run length to demand of `seq`. Never more than `seq` itself is long: a 2-word heading
    block like "9.8 Physical Properties" can only ever produce a 2-word run, and demanding 3
    would score every such block 0 and drag the page average down for no reason."""
    return max(1, min(MIN_MATCH_RUN, len(seq)))


def _run_coverage(seq, ref):
    """Fraction of `seq` lying in matching runs of >= _min_run_for(seq) elements shared with
    `ref`. difflib's matching runs are monotonic in both sequences, so the ORDER of `seq` is
    enforced; `seq` may however be found anywhere in `ref`."""
    if not seq:
        return 1.0
    need = _min_run_for(seq)
    matcher = difflib.SequenceMatcher(None, seq, ref, autojunk=False)
    hit = sum(size for _, _, size in matcher.get_matching_blocks() if size >= need)
    return min(1.0, hit / len(seq))


def _units(text):
    """Split a block's text into sentence-ish units, merging fragments forward until each holds
    at least UNIT_MIN_WORDS prose words (a trailing short remainder joins the previous unit)."""
    units, buf = [], ""
    for part in re.split(r"(?<=[.:;!?])\s+|\n", text or ""):
        buf = (buf + " " + part).strip() if buf else part
        if len(_prose_words(buf)) >= UNIT_MIN_WORDS:
            units.append(buf)
            buf = ""
    if buf:
        if units:
            units[-1] = units[-1] + " " + buf
        else:
            units.append(buf)
    return units


def _block_text(blocks):
    return [b.get("text") or "" for b in blocks if (b.get("text") or "").strip()]


def _defers_to_a2s(blocks):
    """True when some block's content is deliberately left for A2S -- a needs_special block, or
    any block carrying no text. Such a page's layer contains text no block can match, so the
    strict coverage limbs are not computable on it."""
    return any(b.get("needs_special") or not (b.get("text") or "").strip() for b in blocks)


def _text_layer_segments(blocks, text_layer, stamps):
    """The limbs of check (3). Returns a list of human-readable failure strings."""
    lines = _layer_lines(text_layer, stamps)
    layer_words = _prose_words("\n".join(lines))
    if not layer_words:
        return []  # nothing comparable (image-only or formula-only page)

    segments = []

    # --- prose precision, per block (immune to block reordering, strict within a block) ---
    weighted, total = 0.0, 0
    covered = [False] * len(layer_words)
    worst_block, worst_block_at = 1.0, None
    for b in blocks:
        bw = _prose_words(b.get("text") or "")
        if not bw:
            continue
        need = _min_run_for(bw)
        matcher = difflib.SequenceMatcher(None, layer_words, bw, autojunk=False)
        hit = 0
        for i, _j, size in matcher.get_matching_blocks():
            if size >= need:
                hit += size
                for k in range(i, i + size):
                    covered[k] = True
        score = min(1.0, hit / len(bw))
        weighted += score * len(bw)
        total += len(bw)
        if len(bw) >= BLOCK_MIN_WORDS and score < worst_block:
            worst_block, worst_block_at = score, (b.get("n"), b.get("text") or "")
    precision = (weighted / total) if total else 1.0
    if precision < PROSE_PRECISION_MIN:
        segments.append(
            f"A2_TEXT_MISMATCH: only {precision:.1%} of the blocks' prose words are found, in "
            f"order, in the page's text layer (want >= {PROSE_PRECISION_MIN:.0%})"
        )

    # A page-wide average dilutes one bad block among many, so score the weakest block too.
    # This is the limb that catches a short block being reworded or re-ordered.
    if worst_block < WORST_BLOCK_MIN and worst_block_at:
        n, text = worst_block_at
        excerpt = re.sub(r"\s+", " ", text).strip()[:80]
        segments.append(
            f"A2_TEXT_MISMATCH: block n={n} is only {worst_block:.1%} matched to the page's "
            f"text layer (want >= {WORST_BLOCK_MIN:.0%}): {excerpt!r}"
        )

    # --- numeric precision: every multi-digit number written must exist in the layer ---
    layer_numbers = set(_numbers("\n".join(lines)))
    block_numbers = _numbers(" ".join(_block_text(blocks)))
    if block_numbers:
        missing = [t for t in block_numbers if t not in layer_numbers]
        if missing:
            shown = ", ".join(sorted(set(missing))[:6])
            segments.append(
                f"A2_TEXT_MISMATCH: {len(missing)} number(s) in block text do not appear "
                f"anywhere in the page's text layer: {shown}"
            )

    # --- worst sentence-ish unit ---
    worst, worst_at = 1.0, None
    for b in blocks:
        if not (b.get("text") or "").strip():
            continue
        for unit in _units(b["text"]):
            uw = _prose_words(unit)
            if len(uw) < UNIT_MIN_WORDS:
                continue
            score = _run_coverage(uw, layer_words)
            if score < worst:
                worst, worst_at = score, (b.get("n"), unit)
    if worst < WORST_UNIT_MIN and worst_at:
        n, unit = worst_at
        excerpt = re.sub(r"\s+", " ", unit).strip()[:80]
        segments.append(
            f"A2_TEXT_MISMATCH: block n={n} contains a sentence only {worst:.1%} matched to the "
            f"page's text layer (want >= {WORST_UNIT_MIN:.0%}): {excerpt!r}"
        )

    # --- coverage limbs ---
    deferred = _defers_to_a2s(blocks)
    block_words = _prose_words(" ".join(_block_text(blocks)))
    from collections import Counter
    have, want = Counter(block_words), Counter(layer_words)

    # Discount what the agent DECLARED it removed as furniture, before measuring recall.
    #
    # Without this the check punishes the agent for doing its job. A chapter-opening page carries a
    # section-contents panel ("7.2 Kepler's laws", "12.1 Do Plants ...") which is navigational
    # apparatus -- furniture by this step's own definition -- and it is present in the text layer.
    # The agent correctly keeps it out of `blocks`, and the old denominator then counted every one
    # of those words as prose the blocks had failed to account for. Measured: PHY11L-ch07-p001
    # listed ALL sixteen panel lines in `running_header_footer_removed`, excluded them exactly as
    # instructed, and was failed at 90.7% recall for it. Fourteen chapter-opener pages failed this
    # way across one Stage A wave, which I first mis-read as the agents under-capturing openers.
    #
    # Line-by-line matching is not enough and was the second half of the bug: the agent declares
    # "7.2 Kepler's laws" while the text layer breaks it as "7.2" / "Kepler's laws" on separate
    # lines, so any exact-string comparison misses. Matching on the word multiset sidesteps the
    # layout entirely.
    #
    # The discount cannot be used to hide a bad transcription: it only ever removes words the agent
    # explicitly listed, those words must genuinely occur in the text layer to be subtracted at
    # all, and a declared string that ALSO appears inside a block is already a separate failure
    # (see the stamps check below), so furniture cannot be both discounted here and kept there.
    if stamps:
        want = want - Counter(_prose_words(" ".join(str(s) for s in stamps)))

    recall = sum((have & want).values()) / max(1, sum(want.values()))
    recall_min = RECALL_MIN_DEFERRED if deferred else RECALL_MIN_STRICT
    if recall < recall_min:
        # Report enough digits to show the shortfall is real. At one decimal place a recall of
        # 0.9897 prints as "only 99.0% ... (want >= 99%)", which reads as a contradiction and
        # invites someone to "fix" a threshold that is behaving correctly -- the comparison is
        # `<`, so an exact 99% passes. Widen the precision only when rounding would hide the gap.
        gap = recall_min - recall
        shown = f"{recall:.1%}" if gap >= 0.001 else f"{recall:.3%}"
        segments.append(
            f"A2_TEXT_MISMATCH: blocks account for only {shown} of the page's text-layer "
            f"prose (want >= {recall_min:.0%}"
            + (" -- page defers content to A2S, so only the wholesale-failure bar applies)"
               if deferred else ")")
        )
    if not deferred:
        # Declared furniture counts as ACCOUNTED FOR here too, for the same reason it is
        # discounted from recall above. `covered` is built only from block matches, so a
        # chapter-opener's section-contents panel -- correctly excluded from blocks and correctly
        # listed in `running_header_footer_removed` -- left a long uncovered stretch and tripped
        # this limb instead. PHY11L-ch07-p001 is the worked example: fixing recall alone moved its
        # failure from "accounts for only 90.7%" to "28 consecutive prose words in no block", the
        # same sixteen declared panel lines counted a second way.
        #
        # Consumed from a multiset so a single declared word cannot explain away many occurrences
        # of itself in the layer.
        if stamps:
            budget = Counter(_prose_words(" ".join(str(s) for s in stamps)))
            for k, word in enumerate(layer_words):
                if not covered[k] and budget.get(word, 0):
                    budget[word] -= 1
                    covered[k] = True
        longest = run = 0
        for flag in covered:
            run = 0 if flag else run + 1
            longest = max(longest, run)
        if longest > MAX_UNEXPLAINED_RUN:
            segments.append(
                f"A2_TEXT_MISMATCH: {longest} consecutive prose words of the page's text layer "
                f"are in no block (want <= {MAX_UNEXPLAINED_RUN}); the page defers nothing to "
                "A2S, so every line should be accounted for"
            )
    return segments


def _header_footer_segments(blocks, stamps):
    """Check (4). A running header/footer the agent failed to strip survives as its own line,
    never as a word inside a sentence -- so only whole-line occurrences are flagged. See the
    module docstring's "Header/footer limb" for the two real false-positive families this
    replaces."""
    variants = _stamp_variants(stamps)
    # Ignore declared strings too generic to be furniture. A running header is a distinctive
    # phrase; a bare common word is not, and flagging it produces a true-but-useless failure.
    # Real cases that made this necessary: agents declared `'of'` (PHY12L-ch11-p005),
    # `'radiation.'` (p006), `'GROWTH'` (BIO11L-ch13-p002) and `'Polymers'` (CHE12O-ch15-p005)
    # as removed, and the check then reported each as "still present inside a block" because of
    # course a one-word string recurs in prose. Four of six new failures in one wave were this.
    #
    # The guard is on the DECLARED string's own specificity, not on where it was found: keep
    # anything with a digit (page numbers like "275" are genuine stamps and must stay checkable),
    # anything of two or more words, and any single word longer than three characters.
    #
    # The length bar is deliberately LOW, and that is a correction. I first set it at 8 characters,
    # which silenced the useless `'of'` finding but also silenced `'Amines'` -- and this file's own
    # sensitivity test injects exactly that as a running header, so it failed and told me the
    # check had gone blinder. A chapter-name header is often short (`Amines`, `GROWTH`,
    # `Polymers`), so length cannot separate a real header from a stray word. Only two rules here
    # are actually principled: a function word of three characters or fewer is not furniture, and
    # a string ending in sentence punctuation is not furniture.
    #
    # The other half of the fix belongs upstream: the agent should declare the whole header line,
    # not a fragment of it. That is now stated in .claude/agents/a2-page-reader.md.
    # A second, sharper discriminator on top of specificity: a running header or footer never
    # ends in sentence punctuation. `'radiation.'` passed the length test but that trailing full
    # stop says plainly it is the tail of a sentence the agent mis-declared, not page furniture.
    # This is a typographic fact about headers rather than a tuned threshold, so it is the rule I
    # trust more of the two. Note it correctly KEEPS `'Polymers'` (CHE12O ch15's own chapter-name
    # header, where the contradiction is real) while dropping the prose fragment.
    def _specific(v):
        if v.endswith((".", "!", "?", ";", ":", ",")):
            return False
        return bool(re.search(r"\d", v)) or len(v.split()) > 1 or len(v.strip()) > 3
    variants = {v for v in variants if _specific(v)}
    if not variants:
        return []
    segments = []
    for b in blocks:
        raw_lines = [normalise_quote(ln).strip() for ln in (b.get("text") or "").splitlines()]
        lines = [ln for ln in raw_lines if ln]
        if not lines:
            continue
        hits = set()
        # a stamp sitting on its own line
        for ln in lines:
            if ln in variants:
                hits.add(ln)
        # a stamp the agent split across consecutive lines (e.g. "275" / "Amines")
        for i in range(len(lines) - 1):
            for j in (2, 3):
                if i + j <= len(lines):
                    joined = " ".join(lines[i:i + j])
                    if joined in variants:
                        hits.add(joined)
        for stamp in sorted(hits):
            segments.append(
                f"A2_TEXT_MISMATCH: header/footer string {stamp!r} (listed as removed) is still "
                f"present as its own line inside block n={b.get('n')}"
            )
    return segments


def check(data, context):
    if not isinstance(data, dict):
        return False, "A2 output is not an object"

    input_data = context.get("input_data") or {}
    blocks = data.get("blocks") or []
    stamps = data.get("running_header_footer_removed") or []
    segments = []

    seen_n = set()
    for b in blocks:
        n = b.get("n")
        if n in seen_n:
            segments.append(f"A2_TEXT_MISMATCH: duplicate block n={n}")
        seen_n.add(n)

    text_layer = (input_data.get("text_layer") or "").strip()
    if text_layer:
        segments.extend(_text_layer_segments(blocks, text_layer, stamps))

    segments.extend(_header_footer_segments(blocks, stamps))

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
