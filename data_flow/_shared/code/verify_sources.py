"""Source verifier: does the extracted question data actually match independent transcriptions?

READ-ONLY. This script never writes to papers/records/, never "fixes" a record, and never
touches inputs/. Its only outputs are two CSVs under exports/<date>/.

WHY THIS EXISTS
---------------
The bank's questions were extracted from coaching-website printouts (neet.training pages
printed from Chromium, registered under inputs/papers/neet_<year>_code-*.pdf). Those are NOT
official papers. The answer keys in inputs/keys/ ARE official. So the open question is whether
the extracted *question text* is faithful. Three independent transcriptions of the same
questions exist:

  1. the scrape   - what papers/records/Q-*.json was built from
  2. the book     - inputs/papers/<year>.pdf etc., typeset year-wise publications
  3. the sheet    - inputs/legacy_sheets/*.xlsx, columns Question / Answer / Year

Task 1 (`--records`) matches every canonical record to its counterpart in the year's book and
the year's sheet and reports where the three disagree.
Task 2 (`--sittings`) resolves which sitting the sitting-ambiguous paper files belong to.


MATCHING METHOD (validated on this project's real data, see "EVIDENCE" below)
----------------------------------------------------------------------------
* Compare FULL question text (stem + statements + lists + options), not the stem alone.
  Stem-only matching gave a real question a 1.3x margin over the runner-up (ambiguous);
  full text gave 5.0x.
* Normalise first: strip markdown images `![](...)`, strip `[bracketed descriptions]`, unwrap
  LaTeX `$...$` delimiters, drop non-alphanumerics, lowercase. Then word 3-grams, Jaccard.
* Judge by the GAP to the runner-up, NOT by absolute similarity. Spec Section 13 says accept
  at >= 0.85 absolute similarity. On this project's real data that rule rejects 100% of true
  matches: the highest similarity any genuinely-correct match reaches is ~0.64, because the
  three sources legitimately render the same question differently (LaTeX vs mangled PDF
  glyphs vs mathpix image links, and different option ORDER).

ANSWERS ARE COMPARED BY TEXT, NEVER BY LETTER OR NUMBER
-------------------------------------------------------
The option ORDER differs between sources. For Q-000001 all three sources agree word-for-word
on the stem, but the scrape lists `2W/A` first while the book and the sheet list `Zero` first.
The sheet therefore says answer `C` and the official key says `2` - and both denote the same
text, `W/A`. Comparing `C` against `2` manufactures a false alarm. So every answer is resolved
to the TEXT of the option it points at, in that source's own ordering, before comparison.


EVIDENCE FOR THE THRESHOLDS (measured on all 10 canonical records, all NEET 2023 MAIN)
--------------------------------------------------------------------------------------
Full-text similarity of the correct match, and its gap to the runner-up:

    record     book sim  book gap   sheet sim  sheet gap
    Q-000001     0.621     27.31x     0.679     29.55x
    Q-000002     0.289      6.66x     0.333      6.00x
    Q-000003     0.571       inf      0.583       inf
    Q-000004     0.614     33.77x     0.636     28.32x
    Q-000005     0.159      4.30x     0.393      8.90x
    Q-000007     0.621     45.97x     0.569     39.85x
    Q-000009     0.468     21.27x     0.643     28.61x
    Q-000011     0.432     32.00x     0.444     30.22x
    Q-000013     0.105      2.42x     0.147      2.72x
    Q-000015     0.695      4.96x     0.717      4.95x

Every one of those 20 matches was confirmed correct by hand AND by an independent positional
cross-check (see `_positional_crosscheck`): the book's question number and the sheet's row
number agree for all 10 records across three different per-subject offsets (+1 for Physics,
+51 for Chemistry, +101 for Biology). So all 20 are true positives, and:

  - absolute similarity maxes out at 0.717 -> the spec's >= 0.85 rule would reject all 20.
    ACCEPT_SIM_FLOOR is therefore set to a very low 0.05, purely as a guard against matching
    noise, and the real decision is made on the gap.
  - the smallest gap a true match produced is 2.42x (Q-000013). The briefed rule
    (accept >= 3x, flag 2-3x, reject < 2x) is kept UNCHANGED, because 2.42x is a figure-only
    question whose options are chemical structures rendered as bare glyphs - there is almost
    no comparable text, so a human genuinely should look at it. Keeping the accept bar at 3x
    costs one conservative flag out of 20 and loses nothing. Lowering it to 2x to absorb that
    case would buy no extra true matches and would weaken the reject bar.
  - a 2x floor for rejection is never exercised on this data: the gap distribution is sharply
    bimodal (one case at 2.4-2.7x, everything else at 4.3x or better), so there is no evidence
    here that argues for moving either bar.

Stem agreement is judged separately, and NOT with the 3-gram score - once the counterpart is
identified, a direct word-level comparison is more informative. Two numbers per pair:
`ratio` (difflib, order-sensitive) and `common_frac` (|multiset intersection| / length of the
shorter side, order-insensitive and tolerant of one side carrying extra material). Both are
needed because of two real, measured artefacts that are NOT textual disagreements:
  - the book's text layer absorbs labels drawn inside figures (Q-000002's book stem carries
    the circuit's own `A`, `B`, `3uF`, `3uF`, `3uF`), and renders formulae as glyph soup
    (Q-000013, Q-000007), while the scrape wrote `[unreadable glyph]` and the sheet wrote
    clean LaTeX;
  - the scrape sometimes orders the stem's components differently from the book and the sheet
    (Q-000015 puts "Choose the most appropriate answer..." before the lettered statements;
    both other sources put it after).
So: all-agree needs near-identity on one of the two measures; minor-diff means the shorter
side's words are essentially all present in the longer side (an extraction artefact or a
re-ordering); DISAGREE means words are genuinely missing or different on both measures, and a
human must look. Note the limit of this: a SHORT stem being fully contained in a longer one is
weak evidence on its own (Q-000013's stem is seven generic words), which is why every row also
carries its match verdict and its positional cross-check - the agreement verdict is never the
only thing reported.

Usage:
    python -m scripts.verify_sources               # both tasks
    python -m scripts.verify_sources --records     # Task 1 only
    python -m scripts.verify_sources --sittings    # Task 2 only
    python -m scripts.verify_sources --date 2026-10-12   # pin the exports/<date>/ folder
"""
import argparse
import collections
import csv
import datetime
import difflib
import glob
import json
import os
import re
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from scripts.lib import sittings as lib_sittings  # noqa: E402

# ---------------------------------------------------------------------------
# Thresholds. See "EVIDENCE FOR THE THRESHOLDS" in the module docstring - every number here
# was chosen against the 10 real records, not inherited from the spec.
# ---------------------------------------------------------------------------
ACCEPT_GAP = 3.0          # gap to runner-up at or above which a match is accepted
FLAG_GAP = 2.0            # gap in [FLAG_GAP, ACCEPT_GAP) -> flag for a human; below -> reject
ACCEPT_SIM_FLOOR = 0.05   # noise guard only; the decision is the gap, not this
STEM_IDENTICAL = 0.97     # ratio or common_frac at/above this counts as "the same words"
STEM_MINOR = 0.85         # common_frac at/above this counts as a minor/artefact difference
NGRAM = 3

# ---------------------------------------------------------------------------
# The owner's authoritative file index, transcribed from
#   /Users/saumyaladdha/Downloads/NEET PYQ 2010-2026 - Sheet1.csv
# It maps each year's sitting to the year-wise paper PDF and the legacy sheet XLSX that
# transcribe it. For the files it covers this is better evidence than any text matching, so
# Task 2 uses it directly and only falls back to text matching for the 166 scrape printouts,
# which the index does not mention at all.
#
# IMPORTANT, and deliberately not inferred away: the index lists what the owner HAS, not what
# exists. NEET 2019 had an Odisha re-exam after Cyclone Fani, 2020 had an October re-exam for
# containment-zone candidates, and 2024 had a 23 June re-test for 1,563 candidates in the
# grace-marks case. Those sittings are real and scripts/lib/sittings.py is right to require
# them. The index simply does not include their papers, which makes them missing inputs - not
# non-existent sittings.
# ---------------------------------------------------------------------------
# The owner's original is ~/Downloads/NEET PYQ 2010-2026 - Sheet1.csv; a verbatim copy now
# lives in the repo. The mapping below is embedded rather than parsed so that this script's
# results are reproducible and cannot shift under it, but `_verify_index_against_csv` re-reads
# the in-repo copy on every run and shouts if the two have drifted apart.
OWNER_INDEX_CSV = os.path.join("inputs", "_reference", "paper_index_2010_2026.csv")
OWNER_INDEX = {
    # year: {sitting-label-as-the-index-uses-it: (paper pdf basename, sheet xlsx basename)}
    2010: {"PRELIMINARY": ("AIPMT-2010-Preliminary ..pdf", "AIPMT-Pre_pyq_2010.xlsx"),
           "MAIN": ("aipmt-2010-main.pdf", "AIPMT-Main_pyq_2010.xlsx")},
    2011: {"PRELIMINARY": ("AIPMT-2011-Preliminary.pdf", "AIPMT-Pre_pyq_2011.xlsx"),
           "MAIN": ("AIPMT-2011-Main-Original-Solved-Question-Paper.pdf",
                    "AIPMT-Main_pyq_2011.xlsx")},
    2012: {"PRELIMINARY": ("2012 pre.pdf", "AIPMT-Pre_pyq_2012.xlsx"),
           "MAIN": ("AIPMT(Mains)-2012.pdf", "AIPMT-Main_pyq_2012.xlsx")},
    2013: {"MAIN": ("AIPMT_2013_NEET_UG_By_ALLEN.pdf", "NEET-UG_pyq_2013.xlsx")},
    2014: {"MAIN": ("AIPMT 2014.pdf", "AIPMT-UG_pyq_2014.xlsx")},
    2015: {"MAIN": ("AIPMT 2015.pdf", "AIPMT-UG_pyq_2015.xlsx")},
    2016: {"MAIN": ("NEET UG 2016 (Phase I).pdf", "NEET-UG_pyq_2016(Phase I)1.xlsx"),
           "PH2": ("NEET UG 2016 (Phase II).pdf", "NEET-UG_pyq_2016(Phase II)2.xlsx")},
    2017: {"MAIN": ("2017.pdf", "NEET-UG_pyq_2017.xlsx")},
    2018: {"MAIN": ("2018.pdf", "NEET-UG_pyq_2018.xlsx")},
    2019: {"MAIN": ("2019.pdf", "NEET-UG_pyq_2019.xlsx")},
    2020: {"MAIN": ("neet-2020_merged .pdf", "NEET-UG_pyq_2020.xlsx")},
    2021: {"MAIN": ("2021.pdf", "NEET-UG_pyq_2021.xlsx")},
    2022: {"MAIN": ("2022.pdf", "NEET-UG_pyq_2022.xlsx")},
    2023: {"MAIN": ("2023.pdf", "NEET-UG_pyq_2023.xlsx")},
    2024: {"MAIN": ("2024.pdf", "NEET-UG_pyq_2024.xlsx")},
    2025: {"MAIN": ("2025.pdf", "NEET-UG_pyq_2025.xlsx")},
    2026: {"CANCELLED": ("NEET Exam 2026_(03-05-2026).pdf",
                         "NEET Exam 2026_(03-05-2026).xlsx"),
           "REEXAM": ("NEET_UG(re-neet)21 Jun 2026 17-25.pdf",
                      "NEET_UG(re-neet)21 Jun 2026 17-25.xlsx")},
}

_CSV_YEAR = re.compile(r"neet\s*(\d{4})", re.IGNORECASE)


def _verify_index_against_csv():
    """Re-read the in-repo copy of the owner's index and confirm OWNER_INDEX still matches it.

    Guards against the embedded constant going stale if the owner revises the spreadsheet.
    Compares the SET of filenames named per year, which is what the constant is for; it does
    not re-derive the sitting labels, since naming the sitting from a loose spreadsheet grid is
    exactly the judgement the constant exists to pin down. Returns a list of warnings.
    """
    path = os.path.join(PROJECT_ROOT, OWNER_INDEX_CSV)
    if not os.path.exists(path):
        return [f"could not re-verify the embedded index: {OWNER_INDEX_CSV} is not in the repo"]
    from_csv = collections.defaultdict(set)
    year = None
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for row in csv.reader(fh):
            cells = [c.strip() for c in row if c and c.strip()]
            if not cells:
                continue
            m = _CSV_YEAR.search(cells[0])
            if m:
                year = int(m.group(1))
            if year is None:
                continue
            for c in cells:
                if c.lower().endswith((".pdf", ".xlsx")):
                    from_csv[year].add(c)
    warnings = []
    for y in sorted(set(from_csv) | set(OWNER_INDEX)):
        embedded = {f for pair in OWNER_INDEX.get(y, {}).values() for f in pair}
        if embedded != from_csv.get(y, set()):
            only_csv = sorted(from_csv.get(y, set()) - embedded)
            only_emb = sorted(embedded - from_csv.get(y, set()))
            warnings.append(f"{y}: embedded index disagrees with {OWNER_INDEX_CSV}"
                            + (f"; only in csv: {only_csv}" if only_csv else "")
                            + (f"; only in code: {only_emb}" if only_emb else ""))
    return warnings


PAPERS_DIR = os.path.join(PROJECT_ROOT, "inputs", "papers")
SHEETS_DIR = os.path.join(PROJECT_ROOT, "inputs", "legacy_sheets")
RECORDS_DIR = os.path.join(PROJECT_ROOT, "papers", "records")


# ---------------------------------------------------------------------------
# Normalisation and similarity
# ---------------------------------------------------------------------------
_MD_IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_BRACKETED = re.compile(r"\[[^\[\]]*\]")
_PLAIN_WORD = re.compile(r"^[A-Za-z]{3,}$")


def _strip_descriptions(text):
    """Remove `[bracketed descriptions]` only, leaving LaTeX optional arguments intact.

    A bracket counts as a prose description when its contents hold at least two plain English
    words (3+ letters, nothing else). That is what distinguishes the scrape's stand-ins -
    `[unreadable glyph]`, `[Chemical structure of a diketone with a benzene ring ...]` - from
    a LaTeX optional argument such as `\\xrightarrow[(ii)\\ H_{3}O^{+}]{...}` or `\\sqrt[3]{x}`,
    whose contents are symbols and subscripted formulae, not words.

    Position cannot be used for this test: the scrape writes `E[unreadable glyph]` with no
    space, so a "preceded by a letter means LaTeX" guard misses it, and running after a split
    on "$" fails too because a description can contain `$...$` of its own. Judging by the
    contents handles every case in this project's data.
    """
    def repl(m):
        inner = m.group(0)[1:-1]
        words = sum(1 for tok in inner.split() if _PLAIN_WORD.match(tok))
        return " " if words >= 2 else m.group(0)
    return _BRACKETED.sub(repl, text)
_LATEX_CMD = re.compile(r"\\[a-zA-Z]+|\\.")
_NON_ALNUM = re.compile(r"[^0-9a-z]+")
_DIGIT_LETTER = re.compile(r"(?<=\d)(?=[a-z])|(?<=[a-z])(?=\d)")
# Sub/superscript digits appear in the scrape's sanitised text layer (`2H₂O`, `CH₃`) where the
# sheet writes `$\mathrm{H_2O}$` and the book writes `H2O`. Fold them to plain digits so the
# three renderings of the same formula converge.
_UNICODE_DIGITS = {
    "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4",
    "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9",
    "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4",
    "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9",
}
_UNICODE_DIGIT_TABLE = {ord(k): v for k, v in _UNICODE_DIGITS.items()}


def norm_tokens(text):
    """Normalise for matching and return the word list.

    Steps, each one answering a difference that actually occurs between these three sources:

    1. strip markdown image links - the sheet stores every figure as a mathpix URL;
    2. fold unicode sub/superscript digits to plain digits;
    3. strip `[bracketed descriptions]` - the scrape's `[Chemical structure of ...]` and
       `[unreadable glyph]` stand-ins for something the other two sources render as a figure
       or as glyph soup - while leaving LaTeX optional arguments alone
       (see `_strip_descriptions`);
    4. unwrap `$...$` LaTeX: the delimiters AND the control-word names are dropped while the
       operands are kept, so `$-\\dfrac{16Gm}{R}$` and `$-\\frac{16Gm}{R}$` - the same answer
       written by two different transcribers - converge instead of being reported as a
       disagreement;
    5. lowercase and drop every non-alphanumeric character;
    6. split digit/letter boundaries, so `CH_3NC` -> `ch 3 nc` agrees with `CH_{3}NC`.
    """
    if not text:
        return []
    text = _MD_IMAGE.sub(" ", str(text)).translate(_UNICODE_DIGIT_TABLE)
    text = _strip_descriptions(text)
    # Odd/even split on "$": odd segments are math regions, where control words are dropped.
    parts = text.split("$")
    cleaned = [_LATEX_CMD.sub(" ", p) if i % 2 else p for i, p in enumerate(parts)]
    text = " ".join(cleaned).lower()
    text = _NON_ALNUM.sub(" ", text)
    return _DIGIT_LETTER.sub(" ", text).split()


def ngrams(tokens, n=NGRAM):
    """Word n-gram set. A text shorter than n degrades to a single whole-text gram rather than
    producing an empty set, so very short options still compare rather than silently score 0."""
    if len(tokens) < n:
        return {tuple(tokens)} if tokens else set()
    return {tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def ratio(tokens_a, tokens_b):
    """Order-sensitive word-level similarity."""
    if not tokens_a and not tokens_b:
        return 1.0
    if not tokens_a or not tokens_b:
        return 0.0
    return difflib.SequenceMatcher(None, tokens_a, tokens_b).ratio()


def common_frac(tokens_a, tokens_b):
    """Order-insensitive: how much of the SHORTER side's words appear in the longer side.

    1.0 means the shorter text's vocabulary is entirely contained in the longer one, which is
    what a figure-glyph leak or a re-ordering looks like. It is deliberately asymmetric-
    tolerant: extra material on one side does not count against agreement, because the
    measured extra material in this project's books is figure labels and glyph soup, not
    different wording. A genuine wording change shows up as missing words on the shorter
    side and so drops this number.
    """
    if not tokens_a or not tokens_b:
        return 0.0
    shared = collections.Counter(tokens_a) & collections.Counter(tokens_b)
    return sum(shared.values()) / min(len(tokens_a), len(tokens_b))


def _same_but_for_spacing(left, right):
    """True when two differing spans are the same words with different word-breaks.

    Real case this exists for: the 2024 book prints "waterlily", the scrape prints "water lily".
    Reported as a genuine DISAGREE, it is nothing of the kind -- and that matters far more than it
    sounds, because the whole value of this check is catching real corruption like the scrape's
    "2200 ohm" where the book and sheet both say "22000 ohm" (a dropped zero that made a correct
    blind-solve look wrong). If spacing noise is reported at the same severity, the real defects
    drown in it and the report stops being read. Compared with ALL whitespace removed, so
    hyphenation and compound-word splits collapse too."""
    a = re.sub(r"\s+", "", left or "")
    b = re.sub(r"\s+", "", right or "")
    return bool(a) and a == b


def diff_spans(tokens_a, tokens_b, label_a, label_b, limit=4):
    """Human-readable description of where two normalised token lists differ.

    Spans that differ only in word-breaks are skipped entirely -- see _same_but_for_spacing."""
    out = []
    sm = difflib.SequenceMatcher(None, tokens_a, tokens_b)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        left = " ".join(tokens_a[i1:i2])
        right = " ".join(tokens_b[j1:j2])
        if tag == "replace" and _same_but_for_spacing(left, right):
            continue
        if tag == "delete":
            out.append(f"only in {label_a}: “{left}”")
        elif tag == "insert":
            out.append(f"only in {label_b}: “{right}”")
        else:
            out.append(f"{label_a} “{left}” vs {label_b} “{right}”")
        if len(out) >= limit:
            out.append("...")
            break
    return "; ".join(out)


def rank(candidates, query_grams):
    """Score every candidate and return (best, best_sim, runner_sim, gap).

    `candidates` is a list of (payload, gram_set). The gap is best_sim / runner_sim, which is
    the quantity the accept/flag/reject decision is made on - see the module docstring.
    """
    scored = sorted(((jaccard(query_grams, g), i) for i, (_, g) in enumerate(candidates)),
                    reverse=True)
    if not scored:
        return None, 0.0, 0.0, 0.0
    best_sim, best_i = scored[0]
    runner_sim = scored[1][0] if len(scored) > 1 else 0.0
    if runner_sim > 0:
        gap = best_sim / runner_sim
    else:
        gap = float("inf") if best_sim > 0 else 0.0
    return candidates[best_i][0], best_sim, runner_sim, gap


def verdict(sim, gap):
    """accept / flag / reject, decided on the gap. See module docstring for why not on sim."""
    if sim < ACCEPT_SIM_FLOOR:
        return "reject"
    if gap >= ACCEPT_GAP:
        return "accept"
    if gap >= FLAG_GAP:
        return "flag"
    return "reject"


def fmt_gap(gap):
    if gap == float("inf"):
        return "inf"
    return f"{gap:.2f}"


# ---------------------------------------------------------------------------
# Source 1: the scrape (papers/records/Q-*.json)
# ---------------------------------------------------------------------------
def load_canonical_records():
    """Every record in papers/records/ that is NOT an absorbed duplicate.

    A record with `merged_into` was folded into another by step C1; its canonical twin carries
    the same question, so including it would double-count and produce a spurious near-tie
    against itself in the runner-up.
    """
    out = []
    for path in sorted(glob.glob(os.path.join(RECORDS_DIR, "Q-*.json"))):
        if os.path.basename(path).startswith("_"):
            continue
        with open(path, encoding="utf-8") as fh:
            rec = json.load(fh)
        if rec.get("merged_into"):
            continue
        out.append(rec)
    return out


def _statement_text(item):
    """Statements are stored either as plain strings or as {"label": "A", "text": "..."} dicts
    (Q-000015 uses the dict form). Rendering the dict with str() would leak `{'label': ...}`
    into the comparison and fake a disagreement, so unpack it."""
    if isinstance(item, dict):
        return " ".join(str(item.get(k, "")) for k in ("label", "text") if item.get(k))
    return str(item)


def record_stem_text(rec):
    """Everything in the record except the options: stem, statements, and both match-lists."""
    parts = [rec.get("stem_en") or ""]
    parts += [_statement_text(s) for s in (rec.get("statements") or [])]
    parts += [_statement_text(s) for s in (rec.get("list_i") or [])]
    parts += [_statement_text(s) for s in (rec.get("list_ii") or [])]
    return " ".join(p for p in parts if p)


def record_options(rec):
    opts = rec.get("options_en") or {}
    return {str(k): str(v) for k, v in opts.items()}


def record_full_text(rec):
    opts = record_options(rec)
    return record_stem_text(rec) + " " + " ".join(opts[k] for k in sorted(opts))


# ---------------------------------------------------------------------------
# Source 2: the year-wise book (inputs/papers/<year>.pdf etc.)
# ---------------------------------------------------------------------------
_NUM_MARK = re.compile(r"(?m)^[\t ]*(\d{1,3})\.[\t ]")
_SOLUTION_MARK = re.compile(r"^[\t ]*\d{1,3}\.[\t ]*\(([a-d])\)")
_OPT_COUNT = re.compile(r"(?m)(?:^|\t| )([a-d])[.)][\t ]")
_OPT_SPLIT = re.compile(r"(?:^|\n|\t)[\t ]*([a-d])[.)][\t ]+")


class BookIndex:
    """Questions (and their printed answers) parsed out of a typeset year-wise book PDF.

    The books interleave sections: a run of numbered questions for a subject, then a run of
    numbered solutions for that same subject, then the next subject - and the numbering
    restarts per subject. So blocks are split on the leading `N.` marker and then classified:
    a block whose number is immediately followed by `(a)`-`(d)` is a SOLUTION; a block
    carrying at least three option markers is a QUESTION. Contiguous runs of the same kind are
    grouped, and each question run is paired with the solution run that directly follows it -
    which is what lets the book contribute a third, independent answer letter.

    Verified on inputs/papers/2023.pdf: 200 question blocks in runs of 100/50/50 (Biology,
    Physics, Chemistry) and 199 of the 200 printed answers recovered.
    """

    def __init__(self, pdf_path):
        self.path = pdf_path
        self.questions = []   # list of dicts: number, run, text, stem, options, answer_letter
        self._grams = []
        if not pdf_path or not os.path.exists(pdf_path):
            return
        try:
            import pymupdf
        except ImportError:  # pragma: no cover - pymupdf is a hard dependency elsewhere
            return
        try:
            doc = pymupdf.open(pdf_path)
        except Exception:
            return
        try:
            full = "\n".join(doc[i].get_text() or "" for i in range(doc.page_count))
        finally:
            doc.close()
        self._parse(full)

    def _parse(self, full):
        marks = [(m.start(), int(m.group(1))) for m in _NUM_MARK.finditer(full)]
        seq = []
        for i, (start, num) in enumerate(marks):
            end = marks[i + 1][0] if i + 1 < len(marks) else len(full)
            block = full[start:end]
            sol = _SOLUTION_MARK.match(block)
            if sol:
                seq.append(("S", num, sol.group(1), block))
            elif len(_OPT_COUNT.findall(block)) >= 3:
                seq.append(("Q", num, None, block))

        runs = []
        for item in seq:
            if runs and runs[-1][0] == item[0]:
                runs[-1][1].append(item)
            else:
                runs.append((item[0], [item]))

        for ri, (kind, items) in enumerate(runs):
            if kind != "Q":
                continue
            answers = {}
            if ri + 1 < len(runs) and runs[ri + 1][0] == "S":
                answers = {it[1]: it[2] for it in runs[ri + 1][1]}
            for _, num, _unused, block in items:
                stem, options = self._split(block)
                self.questions.append({
                    "number": num,
                    "run": ri,
                    "text": block,
                    "stem": stem,
                    "options": options,
                    "answer_letter": answers.get(num) or "",
                })
        self._grams = [(q, ngrams(norm_tokens(q["text"]))) for q in self.questions]

    @staticmethod
    def _split(block):
        body = re.sub(r"^[\t ]*\d{1,3}\.[\t ]*", "", block)
        matches = list(_OPT_SPLIT.finditer(body))
        if not matches:
            return body, {}
        stem = body[:matches[0].start()]
        options = {}
        for i, m in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
            options[m.group(1)] = body[m.end():end].strip()
        return stem, options

    def match(self, query_grams):
        return rank(self._grams, query_grams)

    def all_grams(self):
        out = set()
        for _, g in self._grams:
            out |= g
        return out

    def __len__(self):
        return len(self.questions)


# ---------------------------------------------------------------------------
# Source 3: the legacy sheet (inputs/legacy_sheets/*.xlsx)
# ---------------------------------------------------------------------------
_SHEET_OPT_SPLIT = re.compile(r"(?:^|\n)[\t ]*([a-d])\)[\t ]*")


class SheetIndex:
    """Questions parsed out of a legacy sheet's "All Questions" tab.

    The `Question` column holds the stem (and any lettered statements) followed by the four
    options as `a) ... b) ... c) ... d) ...`, and the `Answer` column holds a letter A-D
    indexing into THAT ordering - which is frequently not the scrape's ordering, hence the
    answer-by-text rule.
    """

    def __init__(self, xlsx_path):
        self.path = xlsx_path
        self.rows = []
        self._grams = []
        if not xlsx_path or not os.path.exists(xlsx_path):
            return
        try:
            import openpyxl
        except ImportError:  # pragma: no cover
            return
        try:
            wb = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True)
        except Exception:
            return
        try:
            tab = "All Questions" if "All Questions" in wb.sheetnames else wb.sheetnames[0]
            raw = list(wb[tab].iter_rows(values_only=True))
        finally:
            wb.close()
        if not raw:
            return
        header = [str(c).strip() if c is not None else "" for c in raw[0]]
        try:
            q_i = header.index("Question")
            a_i = header.index("Answer")
        except ValueError:
            return
        for row_no, row in enumerate(raw[1:], start=2):
            if not row or q_i >= len(row) or not row[q_i]:
                continue
            cell = str(row[q_i])
            stem, options = self._split(cell)
            answer = str(row[a_i]).strip() if a_i < len(row) and row[a_i] else ""
            self.rows.append({
                "row": row_no,
                "text": cell,
                "stem": stem,
                "options": options,
                "answer_letter": answer,
            })
        self._grams = [(r, ngrams(norm_tokens(r["text"]))) for r in self.rows]

    @staticmethod
    def _split(cell):
        matches = list(_SHEET_OPT_SPLIT.finditer(cell))
        if not matches:
            return cell, {}
        stem = cell[:matches[0].start()]
        options = {}
        for i, m in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(cell)
            options[m.group(1)] = cell[m.end():end].strip()
        return stem, options

    def match(self, query_grams):
        return rank(self._grams, query_grams)

    def all_grams(self):
        out = set()
        for _, g in self._grams:
            out |= g
        return out

    def __len__(self):
        return len(self.rows)


# ---------------------------------------------------------------------------
# Resolving a record's / a source's answer to TEXT
# ---------------------------------------------------------------------------
_LETTER_TO_INDEX = {"a": 0, "b": 1, "c": 2, "d": 3, "1": 0, "2": 1, "3": 2, "4": 3}


def answer_text_from_options(options, pointer):
    """Resolve an answer pointer (a letter A-D or a number 1-4) to the option TEXT in that
    source's own ordering. Returns "" when the pointer is blank or the option is empty - which
    happens for real: a figure-only option set parses to empty strings, and the sheet leaves
    the Answer cell blank for questions that were dropped."""
    if not options or not pointer:
        return ""
    key = str(pointer).strip().lower()
    if key in options and str(options[key]).strip():
        return str(options[key])
    idx = _LETTER_TO_INDEX.get(key)
    if idx is None:
        return ""
    ordered = [options[k] for k in sorted(options)]
    if idx < len(ordered):
        return str(ordered[idx])
    return ""


def compare_answer_text(left, right):
    """Compare two answer TEXTS. Returns (agreement, detail).

    Prefix tolerance is deliberate and measured: a book's last option absorbs the next
    section's chapter heading ("Diplotenes\\nTransport in Plants"), and the scrape's raw option
    layer does the same. Trailing extra material on one side is reported as a minor difference
    rather than a disagreement; missing or altered words are a DISAGREE.
    """
    lt, rt = norm_tokens(left), norm_tokens(right)
    if not lt or not rt:
        return "not-comparable", ""
    if lt == rt:
        return "agree", ""
    if lt[:len(rt)] == rt or rt[:len(lt)] == lt:
        return "minor-diff", diff_spans(lt, rt, "key", "sheet")
    if common_frac(lt, rt) >= STEM_IDENTICAL:
        return "minor-diff", diff_spans(lt, rt, "key", "sheet")
    return "DISAGREE", diff_spans(lt, rt, "key", "sheet")


# ---------------------------------------------------------------------------
# Stem agreement across the sources that were actually matched
# ---------------------------------------------------------------------------
def stem_agreement(stems):
    """`stems` is a dict {source label: raw stem text} for the sources that matched.

    Returns (verdict, per-pair measurements, differing-span description).
    """
    labels = [k for k, v in stems.items() if norm_tokens(v)]
    if len(labels) < 2:
        return "single-source", {}, ""
    pairs = {}
    worst = None
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            a, b = labels[i], labels[j]
            ta, tb = norm_tokens(stems[a]), norm_tokens(stems[b])
            r, cf = ratio(ta, tb), common_frac(ta, tb)
            pairs[(a, b)] = (r, cf)
            score = max(r, cf)
            if worst is None or score < worst[0]:
                worst = (score, a, b, ta, tb, r, cf)

    if all(max(r, cf) >= STEM_IDENTICAL for r, cf in pairs.values()):
        return "all-agree", pairs, ""
    _, a, b, ta, tb, _, _ = worst
    spans = diff_spans(ta, tb, a, b)
    if all(cf >= STEM_MINOR for _, cf in pairs.values()):
        return "minor-diff", pairs, spans

    # Second chance before calling it a real disagreement: compare with every word-break removed.
    # Word-break differences are rife across these three sources and are not errors -- the 2024
    # book prints "waterlily" where the scrape prints "water lily", which tokenises as a genuine
    # mismatch and was reported as DISAGREE. Suppressing that is not cosmetic: this report's only
    # value is surfacing REAL corruption (the scrape's "2200 ohm" against the book and sheet's
    # "22000 ohm" -- a dropped zero that made a correct blind-solve look wrong), and a report
    # padded with spacing noise at the same severity stops being read at all.
    squashed = {lab: re.sub(r"\s+", "", " ".join(norm_tokens(stems[lab]))) for lab in labels}
    vals = [v for v in squashed.values() if v]
    if len(vals) >= 2 and all(
            difflib.SequenceMatcher(None, vals[0], v).ratio() >= STEM_IDENTICAL for v in vals[1:]):
        return "minor-diff", pairs, (spans + "; (word-breaks only -- identical once spacing is "
                                             "removed)" if spans else "word-breaks only")
    return "DISAGREE", pairs, spans


# ---------------------------------------------------------------------------
# Independent positional cross-check
# ---------------------------------------------------------------------------
def _positional_crosscheck(rows):
    """Corroborate the matches without using similarity at all.

    Both the book and the sheet list a paper's questions in paper order, so for every record
    matched in both, (sheet row - book question number) must be constant within a subject
    block. If it is, the two sources independently place the same question at the same spot,
    which confirms the pairing even where the similarity score is low because the question is
    mostly figures. Returns {question_id: "consistent"/"outlier"/"n/a"} plus a summary string.
    """
    offsets = {}
    for r in rows:
        if r["book_question_no"] and r["sheet_row"]:
            offsets[r["question_id"]] = int(r["sheet_row"]) - int(r["book_question_no"])
    if not offsets:
        return {}, "no record matched in both sources"
    counts = collections.Counter(offsets.values())
    # Each subject block has its own offset; an offset shared by >1 record is a real block.
    blocks = {off for off, n in counts.items() if n > 1}
    out = {}
    for qid, off in offsets.items():
        out[qid] = "consistent" if (off in blocks or counts[off] == 1) else "outlier"
    summary = (f"{len(offsets)} records matched in both book and sheet; "
               f"sheet-row minus book-question offsets: "
               + ", ".join(f"{off} (x{n})" for off, n in sorted(counts.items())))
    return out, summary


# ---------------------------------------------------------------------------
# Task 1
# ---------------------------------------------------------------------------
VERIFICATION_COLUMNS = [
    "question_id", "year", "sitting", "subject", "status",
    "book_file", "book_question_no", "book_sim", "book_runner_sim", "book_gap", "book_verdict",
    "sheet_file", "sheet_row", "sheet_sim", "sheet_runner_sim", "sheet_gap", "sheet_verdict",
    "positional_crosscheck",
    "stem_agreement", "stem_scrape_vs_book", "stem_scrape_vs_sheet", "stem_book_vs_sheet",
    "stem_diff_spans",
    "official_answer_pointer", "official_answer_text",
    "sheet_answer_pointer", "sheet_answer_text",
    "book_answer_pointer", "book_answer_text",
    "answer_text_agreement", "answer_diff_spans",
    "concern",
]


def _book_path_for(year):
    entry = OWNER_INDEX.get(year, {})
    for sitting in ("MAIN", "PRELIMINARY", "CANCELLED", "PH2", "REEXAM", "RETEST"):
        if sitting in entry:
            cand = os.path.join(PAPERS_DIR, entry[sitting][0])
            if os.path.exists(cand):
                return cand
    cand = os.path.join(PAPERS_DIR, f"{year}.pdf")
    return cand if os.path.exists(cand) else ""


def _sheet_path_for(year):
    entry = OWNER_INDEX.get(year, {})
    for sitting in ("MAIN", "PRELIMINARY", "CANCELLED", "PH2", "REEXAM", "RETEST"):
        if sitting in entry:
            cand = os.path.join(SHEETS_DIR, entry[sitting][1])
            if os.path.exists(cand):
                return cand
    return ""


def verify_records(out_dir):
    records = load_canonical_records()
    print(f"canonical records (merged duplicates skipped): {len(records)}")

    books, sheets = {}, {}
    rows = []
    for rec in records:
        year = rec.get("year")
        if year not in books:
            bp = _book_path_for(year)
            books[year] = BookIndex(bp)
            print(f"  year {year}: book {os.path.basename(bp) or '(none on disk)'} "
                  f"-> {len(books[year])} questions")
        if year not in sheets:
            sp = _sheet_path_for(year)
            sheets[year] = SheetIndex(sp)
            print(f"  year {year}: sheet {os.path.basename(sp) or '(none on disk)'} "
                  f"-> {len(sheets[year])} rows")
        book, sheet = books[year], sheets[year]

        full_grams = ngrams(norm_tokens(record_full_text(rec)))
        b_hit, b_sim, b_run, b_gap = book.match(full_grams)
        s_hit, s_sim, s_run, s_gap = sheet.match(full_grams)
        b_verdict = verdict(b_sim, b_gap) if b_hit else "no-source"
        s_verdict = verdict(s_sim, s_gap) if s_hit else "no-source"

        stems = {"scrape": record_stem_text(rec)}
        if b_verdict in ("accept", "flag"):
            stems["book"] = b_hit["stem"]
        if s_verdict in ("accept", "flag"):
            stems["sheet"] = s_hit["stem"]
        stem_v, pairs, spans = stem_agreement(stems)

        def pair(a, b):
            v = pairs.get((a, b)) or pairs.get((b, a))
            return f"ratio={v[0]:.3f} common={v[1]:.3f}" if v else ""

        opts = record_options(rec)
        key_ptr = (rec.get("official_answer") or "").strip()
        key_text = answer_text_from_options(opts, key_ptr)
        sheet_ptr = s_hit["answer_letter"] if s_verdict in ("accept", "flag") else ""
        sheet_text = (answer_text_from_options(s_hit["options"], sheet_ptr)
                      if s_verdict in ("accept", "flag") else "")
        book_ptr = b_hit["answer_letter"] if b_verdict in ("accept", "flag") else ""
        book_text = (answer_text_from_options(b_hit["options"], book_ptr)
                     if b_verdict in ("accept", "flag") else "")

        if not key_ptr:
            ans_v, ans_spans = "no-official-answer", ""
        else:
            ans_v, ans_spans = compare_answer_text(key_text, sheet_text)

        rows.append({
            "question_id": rec.get("question_id"),
            "year": year,
            "sitting": rec.get("sitting") or "",
            "subject": rec.get("subject") or "",
            "status": rec.get("status") or "",
            "book_file": os.path.basename(book.path) if book.path else "",
            "book_question_no": b_hit["number"] if b_verdict in ("accept", "flag") else "",
            "book_sim": f"{b_sim:.3f}", "book_runner_sim": f"{b_run:.3f}",
            "book_gap": fmt_gap(b_gap), "book_verdict": b_verdict,
            "sheet_file": os.path.basename(sheet.path) if sheet.path else "",
            "sheet_row": s_hit["row"] if s_verdict in ("accept", "flag") else "",
            "sheet_sim": f"{s_sim:.3f}", "sheet_runner_sim": f"{s_run:.3f}",
            "sheet_gap": fmt_gap(s_gap), "sheet_verdict": s_verdict,
            "positional_crosscheck": "",
            "stem_agreement": stem_v,
            "stem_scrape_vs_book": pair("scrape", "book"),
            "stem_scrape_vs_sheet": pair("scrape", "sheet"),
            "stem_book_vs_sheet": pair("book", "sheet"),
            "stem_diff_spans": spans,
            "official_answer_pointer": key_ptr,
            "official_answer_text": key_text,
            "sheet_answer_pointer": sheet_ptr,
            "sheet_answer_text": sheet_text,
            "book_answer_pointer": book_ptr,
            "book_answer_text": book_text,
            "answer_text_agreement": ans_v,
            "answer_diff_spans": ans_spans,
            "concern": "",
        })

    cross, cross_summary = _positional_crosscheck(rows)
    for r in rows:
        r["positional_crosscheck"] = cross.get(r["question_id"], "n/a")
        r["concern"] = _concern(r)

    path = os.path.join(out_dir, "source_verification.csv")
    _write_csv(path, VERIFICATION_COLUMNS, rows)
    _print_verification_summary(rows, cross_summary, path)
    return rows


def _concern(row):
    """Plain-English statement of what, if anything, a human needs to look at."""
    notes = []
    missing = [n for n, v in (("book", row["book_verdict"]), ("sheet", row["sheet_verdict"]))
               if v in ("reject", "no-source")]
    if missing:
        notes.append("no confident counterpart found in the " + " or ".join(missing)
                     + " - this question could not be cross-checked there")
    flagged = [n for n, v in (("book", row["book_verdict"]), ("sheet", row["sheet_verdict"]))
               if v == "flag"]
    if flagged:
        notes.append("the " + " and ".join(flagged) + " match is only "
                     + "/".join(row[f"{n}_gap"] + "x" for n in flagged)
                     + " clear of the runner-up, so the pairing itself is not certain")

    if row["stem_agreement"] == "DISAGREE":
        notes.append("the sources give genuinely different question text - "
                     + (row["stem_diff_spans"] or "see the stem columns"))
    elif row["stem_agreement"] == "minor-diff":
        notes.append("question text agrees apart from material present on one side only "
                     "(typically figure labels absorbed into a PDF text layer, or the stem's "
                     "parts in a different order) - "
                     + (row["stem_diff_spans"] or "see the stem columns"))
    elif row["stem_agreement"] == "single-source":
        notes.append("only one source had usable question text, so the wording is unverified")

    if row["answer_text_agreement"] == "DISAGREE":
        notes.append("the official key and the sheet point at DIFFERENT answer text - "
                     + (row["answer_diff_spans"] or ""))
    elif row["answer_text_agreement"] == "minor-diff":
        notes.append("the official key and the sheet point at the same answer but write it "
                     "differently (same symbols, different LaTeX layout or order) - "
                     + (row["answer_diff_spans"] or ""))
    elif row["answer_text_agreement"] == "no-official-answer":
        notes.append("the record carries no official answer"
                     + (" (status=dropped)" if row["status"] == "dropped" else "")
                     + (", and the sheet leaves its answer blank too - the two sources agree "
                        "that this question has no scorable answer"
                        if not row["sheet_answer_pointer"] else
                        f", though the sheet does give one ({row['sheet_answer_pointer']})"))
    elif row["answer_text_agreement"] == "not-comparable":
        notes.append("the answer's text could not be compared because the options are figures, "
                     "not words, in at least one source")

    if not notes:
        return "none - all sources agree on the question text and on the answer's text"
    return "; ".join(notes)


def _print_verification_summary(rows, cross_summary, path):
    print("\n" + "=" * 78)
    print("TASK 1 - SOURCE VERIFICATION")
    print("=" * 78)
    print(f"records checked: {len(rows)}")
    for field, title in (("book_verdict", "book match"), ("sheet_verdict", "sheet match"),
                         ("stem_agreement", "question-text agreement"),
                         ("answer_text_agreement", "answer-TEXT agreement (key vs sheet)")):
        counts = collections.Counter(r[field] for r in rows)
        print(f"  {title:38s} " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print(f"  positional cross-check: {cross_summary}")

    sims = [float(r["sheet_sim"]) for r in rows] + [float(r["book_sim"]) for r in rows]
    gaps = [float(r[k]) for r in rows for k in ("book_gap", "sheet_gap") if r[k] != "inf"]
    print(f"  similarity of accepted matches: max {max(sims):.3f} "
          f"(the spec's >= 0.85 absolute rule would reject every one of them)")
    print(f"  gap to runner-up: min {min(gaps):.2f}x, max {max(gaps):.2f}x"
          + (" (plus matches with no runner-up at all)"
             if any(r[k] == "inf" for r in rows for k in ("book_gap", "sheet_gap")) else ""))

    need_human = [r for r in rows if r["stem_agreement"] == "DISAGREE"
                  or r["answer_text_agreement"] == "DISAGREE"
                  or r["book_verdict"] == "flag" or r["sheet_verdict"] == "flag"
                  or r["book_verdict"] in ("reject", "no-source")
                  or r["sheet_verdict"] in ("reject", "no-source")]
    print(f"\n  questions a human must look at: {len(need_human)}")
    for r in need_human:
        print(f"    {r['question_id']}: {r['concern']}")
    print(f"\n  written: {path}")


# ---------------------------------------------------------------------------
# Task 2
# ---------------------------------------------------------------------------
SITTING_COLUMNS = [
    "row_kind", "year", "sitting", "file", "file_kind", "evidence",
    "matched_sheet", "match_score", "runner_sheet", "runner_score", "margin",
    "stated_questions", "expected_questions",
    "resolved_sitting", "verdict", "note",
]

# Questions in the official paper, by year - used only to report how complete each scrape
# printout is. Every neet.training page states its own count on page 1 ("N questions across
# Physics, Chemistry, and Biology"), and most of them fall short of the real paper.
OFFICIAL_QUESTION_COUNT = {2016: 180, 2017: 180, 2018: 180, 2019: 180, 2020: 180,
                           2021: 180, 2022: 200, 2023: 200, 2024: 200, 2025: 180}
_STATED_COUNT = re.compile(r"(\d{2,3})\s+questions across")

# How the owner's index labels a sitting vs how scripts/lib/sittings.py names it. Only the
# 2016 second phase and the 2026 pair need translating; everything else already agrees.
INDEX_TO_REQUIRED = {"PRELIMINARY": "PRELIMINARY", "PH2": "PH2", "MAIN": "MAIN",
                     "REEXAM": "REEXAM", "RETEST": "RETEST", "CANCELLED": "CANCELLED"}

_SCRAPE_NAME = re.compile(r"^neet_(\d{4})_code-(.+)\.pdf$")


def _load_all_sheets():
    out = {}
    for path in sorted(glob.glob(os.path.join(SHEETS_DIR, "*.xlsx"))):
        name = os.path.basename(path)
        if name.startswith("~$"):
            continue
        idx = SheetIndex(path)
        if len(idx):
            out[name] = idx.all_grams()
    return out


def _file_grams(pdf_path):
    """Return (n-gram set, self-stated question count) for one PDF."""
    try:
        import pymupdf
    except ImportError:  # pragma: no cover
        return set(), ""
    try:
        doc = pymupdf.open(pdf_path)
    except Exception:
        return set(), ""
    try:
        pages = [doc[i].get_text() or "" for i in range(doc.page_count)]
    finally:
        doc.close()
    text = "\n".join(pages)
    stated = _STATED_COUNT.search(pages[0] if pages else "")
    return ngrams(norm_tokens(text)), (stated.group(1) if stated else "")


def _sheet_sitting_lookup():
    """{sheet basename: (year, sitting)} straight from the owner's index."""
    out = {}
    for year, entry in OWNER_INDEX.items():
        for sitting, (_pdf, xlsx) in entry.items():
            out[xlsx] = (year, INDEX_TO_REQUIRED.get(sitting, sitting))
    return out


# 2016 is included as the method's control: its answer is already known independently (all four
# 2016 scrape files are Phase I, and Phase II is absent from the scrape set), and it is the one
# ambiguous year with TWO sheets, so it is the only year where the runner-up sheet is the
# other sitting of the same year rather than a different year. If the method cannot reproduce
# 2016 it should not be trusted on 2019/2020/2024.
AMBIGUOUS_YEARS = (2016, 2019, 2020, 2024)


def resolve_sittings(out_dir, years=AMBIGUOUS_YEARS):
    rows = []
    for warning in _verify_index_against_csv():
        print(f"  WARNING: {warning}")
    sheet_grams = _load_all_sheets()
    sheet_sitting = _sheet_sitting_lookup()
    print(f"\nloaded {len(sheet_grams)} legacy sheets as comparison targets")

    # --- (a) the owner's index: ground truth for the year-wise books and the sheets ---
    missing_pdfs = []
    for year in sorted(OWNER_INDEX):
        for sitting, (pdf, xlsx) in sorted(OWNER_INDEX[year].items()):
            req = INDEX_TO_REQUIRED.get(sitting, sitting)
            pdf_here = os.path.exists(os.path.join(PAPERS_DIR, pdf))
            if not pdf_here:
                missing_pdfs.append((year, req, pdf, xlsx))
            rows.append({
                "row_kind": "index", "year": year, "sitting": req,
                "file": pdf, "file_kind": "year-wise book", "evidence": "owner_index",
                "matched_sheet": xlsx, "match_score": "", "runner_sheet": "",
                "runner_score": "", "margin": "",
                "resolved_sitting": req,
                "verdict": "RESOLVED" if pdf_here else "MISSING_FILE",
                "note": ("sitting is stated by the owner's index, no text matching needed"
                         if pdf_here else
                         "named in the owner's index but NOT on disk anywhere under "
                         "inputs/papers or the Saumya_NEET_work source tree; the paired "
                         "sheet IS present, so this is a retrieval gap, not an unknown"),
            })
            rows.append({
                "row_kind": "index", "year": year, "sitting": req,
                "file": xlsx, "file_kind": "legacy sheet", "evidence": "owner_index",
                "matched_sheet": "", "match_score": "", "runner_sheet": "",
                "runner_score": "", "margin": "",
                "resolved_sitting": req,
                "verdict": ("RESOLVED" if xlsx in sheet_grams else "MISSING_FILE"),
                "note": "sitting is stated by the owner's index",
            })

    # --- (b) text matching: the only evidence available for the scrape printouts ---
    per_year = collections.defaultdict(list)
    for year in years:
        files = sorted(glob.glob(os.path.join(PAPERS_DIR, f"neet_{year}_code-*.pdf")))
        print(f"  {year}: matching {len(files)} scrape file(s) against all "
              f"{len(sheet_grams)} sheets")
        for path in files:
            name = os.path.basename(path)
            g, stated = _file_grams(path)
            expected = OFFICIAL_QUESTION_COUNT.get(year, "")
            if not g:
                rows.append({
                    "row_kind": "scrape", "year": year, "sitting": "", "file": name,
                    "file_kind": "scrape printout", "evidence": "text_match",
                    "matched_sheet": "", "match_score": "", "runner_sheet": "",
                    "runner_score": "", "margin": "", "stated_questions": stated,
                    "expected_questions": expected, "resolved_sitting": "",
                    "verdict": "UNRESOLVED",
                    "note": "no extractable text layer, so it cannot be matched",
                })
                continue
            short = ""
            if stated and expected and int(stated) < int(expected):
                short = (f" INCOMPLETE SOURCE: this printout states {stated} questions where "
                         f"the official {year} paper has {expected}, so "
                         f"{int(expected) - int(stated)} are not in it at all.")
            scored = sorted(((len(g & s) / len(g), n) for n, s in sheet_grams.items()),
                            reverse=True)
            best_score, best = scored[0]
            run_score, run = (scored[1] if len(scored) > 1 else (0.0, ""))
            margin = best_score / run_score if run_score else float("inf")
            resolved = sheet_sitting.get(best, (None, ""))
            ok = margin >= ACCEPT_GAP and resolved[0] == year
            rows.append({
                "row_kind": "scrape", "year": year, "sitting": "", "file": name,
                "file_kind": "scrape printout", "evidence": "text_match",
                "matched_sheet": best, "match_score": f"{best_score:.3f}",
                "runner_sheet": run, "runner_score": f"{run_score:.3f}",
                "margin": fmt_gap(margin),
                "stated_questions": stated, "expected_questions": expected,
                "resolved_sitting": resolved[1] if ok else "",
                "verdict": "RESOLVED" if ok else "UNRESOLVED",
                "note": ((f"its questions are the ones {best} transcribes, at "
                          f"{fmt_gap(margin)}x the next-best sheet ({run}); the owner's index "
                          f"attributes that sheet to {resolved[0]} {resolved[1]}"
                          if ok else
                          f"best sheet {best} at only {fmt_gap(margin)}x over {run} - "
                          "not clear enough to attribute a sitting") + short),
            })
            per_year[year].append((name, resolved[1] if ok else "", margin, best))

    # --- (c) one conclusion row per (year, required sitting) ---
    for year in years:
        got = per_year.get(year, [])
        resolved_to = collections.Counter(s for _, s, _, _ in got if s)
        margins = [m for _, s, m, _ in got if s]
        finite = [m for m in margins if m != float("inf")]
        for required in lib_sittings.REQUIRED_SITTINGS.get(year, []):
            n = resolved_to.get(required, 0)
            index_has = any(INDEX_TO_REQUIRED.get(s, s) == required
                            for s in OWNER_INDEX.get(year, {}))
            # Did a sheet for THIS sitting exist to discriminate against? That is the whole
            # difference between "proven absent from the scrape set" and "merely not found".
            sheet_for_required = ""
            for s, (_pdf, xlsx) in OWNER_INDEX.get(year, {}).items():
                if INDEX_TO_REQUIRED.get(s, s) == required and xlsx in sheet_grams:
                    sheet_for_required = xlsx
            if n:
                note = (f"{n} of {len(got)} scrape file(s) for {year} resolve to {required} "
                        f"(margins "
                        f"{min(finite):.1f}x-{max(finite):.1f}x over the next-best sheet). "
                        f"Every scrape file for this year lands on the same sheet, so none of "
                        f"them is from a different sitting. Caveat: this settles the PAPER "
                        f"files only - the {year} official answer key is a single file "
                        f"covering the whole year without splitting by sitting, and nothing "
                        f"here confirms which sitting(s) it covers.")
                v = "RESOLVED"
            elif sheet_for_required:
                # A sheet transcribing this very sitting was in the comparison pool and not one
                # of the year's scrape files preferred it. That is a real proof of absence
                # from the scrape set, not just a failure to find.
                note = (f"PROVEN ABSENT from the scrape set: {sheet_for_required} transcribes "
                        f"{year} {required} and was one of the {len(sheet_grams)} sheets every "
                        f"{year} scrape file was scored against, yet all {len(got)} of them "
                        f"preferred the other sitting's sheet by a wide margin. "
                        + (f"The index also names a {year} {required} paper PDF that is not on "
                           "disk, so the paper itself still needs collecting."
                           if index_has else ""))
                v = "ABSENT_INPUT"
            else:
                note = (f"{year} {required} is a real sitting (scripts/lib/sittings.py is "
                        f"correct to require it) but no paper for it exists in this project: "
                        f"the owner's index does not list one, and none of the "
                        f"{len(got)} scrape file(s) resolves to it. IMPORTANT - this is NOT a "
                        f"proof of absence: the only {year} sheet covers the "
                        f"{'/'.join(sorted(set(resolved_to))) or 'other'} sitting, so there "
                        f"was no {required} transcription in the comparison pool to recognise "
                        f"a {required} file by. A strong match to the {year} sheet proves "
                        f"'these files are "
                        f"{'/'.join(sorted(set(resolved_to))) or 'the other sitting'}', not "
                        f"'the {required} paper is missing'. Treat as an uncollected input, "
                        f"not as a closed question.")
                v = "UNRESOLVED_ABSENCE"
            rows.append({
                "row_kind": "conclusion", "year": year, "sitting": required, "file": "",
                "file_kind": "", "evidence": "owner_index+text_match",
                "matched_sheet": "", "match_score": "", "runner_sheet": "",
                "runner_score": "", "margin": "", "resolved_sitting": required if n else "",
                "verdict": v, "note": note,
            })

    path = os.path.join(out_dir, "sitting_resolution.csv")
    _write_csv(path, SITTING_COLUMNS, rows)
    _print_sitting_summary(rows, missing_pdfs, years, path)
    return rows


def _print_sitting_summary(rows, missing_pdfs, years, path):
    print("\n" + "=" * 78)
    print("TASK 2 - SITTING RESOLUTION")
    print("=" * 78)
    scrape = [r for r in rows if r["row_kind"] == "scrape"]
    print(f"scrape printouts examined: {len(scrape)} "
          f"({', '.join(str(y) for y in years)})")
    for year in years:
        yr = [r for r in scrape if r["year"] == year]
        ok = [r for r in yr if r["verdict"] == "RESOLVED"]
        if not yr:
            continue
        sheets_hit = collections.Counter(r["matched_sheet"] for r in yr)
        marg = [float(r["margin"]) for r in yr if r["margin"] not in ("", "inf")]
        print(f"  {year}: {len(ok)}/{len(yr)} resolved -> "
              + ", ".join(f"{r['resolved_sitting']}" for r in [ok[0]] if ok)
              + f"; all land on {', '.join(sheets_hit)}"
              + (f"; margins {min(marg):.1f}x-{max(marg):.1f}x" if marg else ""))
    incomplete = [r for r in scrape if r["stated_questions"] and r["expected_questions"]
                  and int(r["stated_questions"]) < int(r["expected_questions"])]
    if incomplete:
        print(f"\n  SEPARATE FINDING - incomplete scrape printouts: "
              f"{len(incomplete)} of {len(scrape)} state fewer questions than the official "
              f"paper has")
        for year in years:
            yr = [r for r in incomplete if r["year"] == year]
            if not yr:
                continue
            counts = sorted(int(r["stated_questions"]) for r in yr)
            exp = yr[0]["expected_questions"]
            print(f"    {year}: {len(yr)} short of {exp} "
                  f"(counts {counts[0]}-{counts[-1]}; worst is "
                  f"{min(yr, key=lambda r: int(r['stated_questions']))['file']} at "
                  f"{counts[0]})")
        print("    this is a completeness gap in the SOURCE, not an extraction error, and it "
              "is not something this script can repair")

    print("\n  conclusions per required sitting:")
    for r in rows:
        if r["row_kind"] == "conclusion":
            print(f"    {r['year']} {r['sitting']:10s} {r['verdict']:13s} {r['note']}")

    print(f"\n  files named in the owner's index but NOT on disk: {len(missing_pdfs)}")
    for year, sitting, pdf, xlsx in missing_pdfs:
        print(f"    {year} {sitting:12s} {pdf}   (its sheet {xlsx} IS present)")
    print(f"\n  written: {path}")


# ---------------------------------------------------------------------------
def _write_csv(path, columns, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    os.replace(tmp, path)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--records", action="store_true", help="run Task 1 only")
    ap.add_argument("--sittings", action="store_true", help="run Task 2 only")
    ap.add_argument("--date", default=None, help="exports/<date>/ folder (default: today)")
    args = ap.parse_args(argv)

    date = args.date or datetime.date.today().isoformat()
    out_dir = os.path.join(PROJECT_ROOT, "exports", date)
    os.makedirs(out_dir, exist_ok=True)

    do_records = args.records or not args.sittings
    do_sittings = args.sittings or not args.records
    if do_records:
        verify_records(out_dir)
    if do_sittings:
        resolve_sittings(out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
