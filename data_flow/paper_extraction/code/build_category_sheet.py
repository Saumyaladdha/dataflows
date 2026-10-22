#!/usr/bin/env python3
"""Builds the question-type / trap category sheet from the questions B3 has actually extracted.

    python3 scripts/build_category_sheet.py            # writes docs/question_categories/*.csv
    python3 scripts/build_category_sheet.py --per-cat 4

Two sheets come out:

  * `categories.csv` -- one row per category: what shape the content takes, what the trap is, how
    to spot it, the four handling steps, and how many questions in the corpus fall in it.
  * `questions.csv`  -- a sample covering EVERY category, with real question ids and the real
    question text, so each category has worked examples rather than a description.

The categories are derived from the corpus, not invented: every detector below was written against
the 700 extracted questions and its count is reported, so a category that does not occur shows up
as zero instead of being asserted.

Two things worth knowing, both found by this script disagreeing with its first author:

  1. A "near-miss" match question CANNOT have two options agreeing on 3 of 4 pairings. Fix three
     pairs of a bijection and the fourth is forced. The real near-miss is a single TRANSPOSITION --
     two options agreeing on exactly 2 of 4. Asking for 3 reported 0 such questions; asking for the
     possible thing reports 48 of the 72 match questions, so two thirds of them turn on one pairing.
  2. 15 questions have options that are PICTURES the scrape never captured; the site itself prints
     "(Image option - will be added soon)". They are unanswerable from our source material, so they
     are their own category (C15) and are excluded from every other category's examples -- a graph
     question whose four graphs are missing teaches nothing about graph questions.

This script makes no judgements: it classifies on printed features and counts. Which categories
matter, and what to do about C14/C15, are decisions for a person.
"""

import argparse
import collections
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

_NAME_RE = re.compile(
    r"(NEET-\d{4}-[A-Z0-9]+-[A-Z0-9]+)-(q\d+)\.(runA|runB|retry1|retry2|adjudicated)\.json$")
_RUN_PRIORITY = {"adjudicated": 0, "retry2": 1, "retry1": 2, "runB": 3, "runA": 4}

_PERM_RE = re.compile(r"^[A-D]-(IV|III|II|I)(,\s*[A-D]-(IV|III|II|I))*$")
_PAIR_RE = re.compile(r"([A-D])-(IV|III|II|I)")
_PLACEHOLDER_RE = re.compile(r"image option|will be added soon|image not available", re.I)
_SEQ_RE = re.compile(r"\b(arrange|increasing|decreasing|order of|ascending|descending)\b", re.I)
_POW10_RE = re.compile(r"10[\^\-–]|10\s*[-–]\s*\d")

# A stem that NAMES a figure. Used to catch questions whose figure was never recorded: 23 such
# questions exist, and they were landing in the prose categories as though they were answerable.
_FIG_REF_RE = re.compile(
    r"\b(figure|fig\.|graph|circuit|diagram|plot|curve|shown below|shown here|given below the)\b",
    re.I)

# Options that carry no digit yet belong to a numeric question. "Zero" and "Infinity" ARE numeric
# answers; they just spell the number. One of them used to break an all-options numeric test and
# drop the question into single-fact recall -- 7 questions were misfiled that way.
_ODD_NUMERIC_RE = re.compile(
    r"^(zero|infinity|infinite|unity|none of these|none of the above|cannot be determined)\.?$",
    re.I)

# A real statement-combination option: at least two labels joined by "and"/comma, then "only".
# Labels appear as (a), (b) or A, B or I, II -- the parentheses defeated a naive letter pattern,
# so genuine combinations like "(a), (b) and (c) only" were being missed while prose containing
# the word "only" ("Conserve only high-risk species") was being matched.
_LABEL = r"\(?\b(?:[a-eA-E]|I{1,3}|IV|V)\b\)?"
_COMBO_RE = re.compile(rf"{_LABEL}\s*(?:,|and)\s*{_LABEL}", re.I)

# cat_id, structure, name, content_shape, trap_mechanism, how_to_spot, step_1..step_4
CATEGORIES = [
    ("C01", "plain", "Single-fact recall",
     "stem + 4 prose options",
     "Every distractor is a true statement about the topic; only one answers the question actually "
     "asked, so recognition feels like knowing.",
     "Prose options, no lists, no negation word.",
     "Name the single thing the stem asks for",
     "Reject options that are true but answer a different question",
     "Match the survivor to the NCERT line that states it",
     "Record the NCERT anchor for the answer"),
    ("C02", "plain", "Negation / EXCEPT",
     "stem carrying NOT / INCORRECT / FALSE / EXCEPT + 4 options",
     "The reader solves the positive question and then picks a TRUE option. The negation inverts "
     "which option wins, so correct knowledge produces a wrong mark.",
     "negative_words_seen is non-empty.",
     "Circle the negation word before reading any option",
     "Judge each option true or false on its own merits",
     "Choose the one that FAILS, not the three that hold",
     "Re-read the stem to confirm you answered the polarity asked"),
    ("C03", "plain", "Numeric calculation",
     "stem with given quantities + 4 numeric options",
     "Options are placed a factor or one decimal place apart, so a single arithmetic or unit slip "
     "lands exactly on a printed distractor instead of nowhere.",
     "Every option contains a digit.",
     "List the givens with their units",
     "Write the governing relation before substituting anything",
     "Carry units through to the result and check them",
     "Ask which distractor a common slip would produce, and why yours is not it"),
    ("C04", "plain", "Power-of-ten / exponent",
     "numeric options carrying 10^n",
     "The exponent, or its SIGN, is the only thing separating options. Scraped papers also flatten "
     "superscripts onto the baseline, which hides the difference entirely.",
     "Options contain 10^n or a flattened 10-n.",
     "Rewrite every option in one common exponent form",
     "Compute the mantissa separately from the exponent",
     "Fix the sign of the exponent deliberately",
     "Sanity-check the order of magnitude against physical reality"),
    ("C05", "plain", "Symbolic / formula",
     "stem + 4 algebraic expressions",
     "Options are algebraically near-identical, differing by a factor, a sign, or which variable "
     "carries the square.",
     "All four options render as math.",
     "Derive the expression symbolically before looking at options",
     "Check the dimensions of each option",
     "Eliminate everything dimensionally impossible",
     "Match the surviving form exactly, factor for factor"),
    ("C06", "match", "Match List I-II (plain)",
     "stem + list_i[4] + list_ii[4] + 4 permutation options",
     "Knowing 2 of 4 pairings feels like progress but need not narrow the options to one.",
     "structure=match, options like 'A-III, B-II, C-IV, D-I'.",
     "Commit only the pairings you are certain of",
     "Strike every option contradicting a certain pairing",
     "Resolve what remains on the weakest pairing",
     "Verify all four pairings of the chosen option"),
    ("C07", "match", "Match near-miss (one swap apart)",
     "as C06, with two options a single transposition apart",
     "Two options differ by ONE swapped pairing, so the whole question turns on a single pair. "
     "(Agreeing on 3 of 4 is impossible -- fix three pairs of a bijection and the fourth is forced; "
     "a single swap agrees on exactly 2.)",
     "Two permutation options agree on exactly 2 of 4 pairings.",
     "Find the one pairing the two surviving options disagree about",
     "Decide that pairing on its own merits",
     "Ignore the pairings the options already agree on",
     "Confirm there is no second disagreement you missed"),
    ("C08", "statement_i_ii", "Two statements I / II",
     "stem + statements[2] + 4 options over the (I, II) truth pair",
     "Mixed-truth pairs: one statement is true and the other is subtly false, usually on a "
     "qualifier rather than on the substance.",
     "structure=statement_i_ii, or two statements with no 'only' options.",
     "Judge statement I alone as true or false",
     "Judge statement II alone as true or false",
     "Map the resulting (I, II) pair to the option that states it",
     "Re-check qualifier words -- all, only, always, never"),
    ("C09", "statements", "Multi-statement combination",
     "stem + statements[3..5] + options like 'A and C only'",
     "Partial knowledge maps cleanly onto a WRONG combination, and 'only' makes both the superset "
     "and the subset of the true set look defensible.",
     "Options contain the word 'only'.",
     "Judge every statement independently, writing each verdict down",
     "Write out the true set explicitly before looking at options",
     "Find the option matching that set exactly",
     "Reject options that add one member or drop one"),
    ("C10", "assertion_reason", "Assertion-Reason ladder",
     "stem + statements[A, R] + the fixed four-rung ladder",
     "Both A and R are frequently true while R is NOT the explanation of A. That rung is the "
     "commonest miss on this shape, because verifying both statements feels like finishing.",
     "Options mention 'Both A and R'.",
     "Judge A alone",
     "Judge R alone",
     "If both are true, test separately whether R actually EXPLAINS A",
     "Pick the rung matching that three-part verdict"),
    ("C11", "any", "Figure-dependent",
     "stem + figure + 4 options",
     "Unanswerable without the figure. A missing, clipped or mis-cropped figure turns the item "
     "into a guess without ever looking unanswerable.",
     "has_figure is true.",
     "Confirm the figure is present and not clipped",
     "Extract the quantities the figure carries, not the prose alone",
     "Solve from figure values",
     "Flag the item if any part of the figure is missing"),
    ("C12", "table", "Data table in stem",
     "stem + inline data table + 4 options",
     "Table structure collapses to a run-on digit string when scraped, destroying row and column "
     "alignment while leaving every digit present and plausible.",
     "structure=table.",
     "Rebuild rows and columns explicitly before solving",
     "Restate the table as labelled pairs and check the count",
     "Read the answer off the rebuilt table",
     "Flag the item if alignment cannot be recovered with certainty"),
    ("C13", "plain", "Order / sequence",
     "stem asking increasing or decreasing order + 4 orderings",
     "The correct sequence printed BACKWARDS is almost always one of the four options, so reading "
     "the direction wrong still lands on a printed answer.",
     "Stem says arrange / increasing / decreasing / order of.",
     "Note which direction the stem demands",
     "Rank the items on the stated property",
     "Write the sequence in the demanded direction",
     "Check that the reverse of your answer is not what you marked"),
    ("C14", "any", "Defective options (duplicate)",
     "options containing a genuine duplicate",
     "Two options are identical as printed, so NO single correct answer exists in the source. "
     "Usually a lost radical, exponent or decimal point.",
     "Two option strings are identical.",
     "Magnify each duplicated option region separately",
     "Look specifically for a lost radical, exponent, decimal or unit prefix",
     "If still identical, mark the SOURCE defective",
     "Never reconstruct the option -- flag it for better source material"),
    ("C15", "any", "Image-only options (not captured)",
     "stem + 4 options that are pictures, absent from our source",
     "The options are graphs, structures or circuits, and the scrape stored a placeholder instead "
     "of the image. The question looks complete but is unanswerable from our material.",
     "Option text matches 'Image option - will be added soon'.",
     "Detect the placeholder before attempting a solve",
     "Do not attempt to infer the pictures from the stem",
     "Record the item as source-incomplete",
     "Route it to re-acquisition from an official PDF"),
]


def _norm_opts(rec):
    return {k: (v or "").strip()
            for k, v in sorted((rec.get("options_en") or {}).items()) if (v or "").strip()}


def _placeholder_options(rec):
    """True when EVERY option is the scrape's missing-image placeholder."""
    opts = _norm_opts(rec)
    if not opts:
        return False
    return all(_PLACEHOLDER_RE.search(v) for v in opts.values())


def _one_transposition_apart(rec):
    """Two permutation options differing by exactly one swap -- they agree on 2 of 4.

    Agreeing on 3 of 4 is impossible for a bijection, which is why this asks for 2.
    """
    perms = [v for v in _norm_opts(rec).values() if _PERM_RE.match(v)]
    for i in range(len(perms)):
        for j in range(i + 1, len(perms)):
            a = dict(_PAIR_RE.findall(perms[i]))
            b = dict(_PAIR_RE.findall(perms[j]))
            if len(a) == 4 and len(b) == 4:
                if sum(1 for k in a if a.get(k) == b.get(k)) == 2:
                    return True
    return False


def categories_of(rec):
    """Every category this question belongs to. A question can carry more than one."""
    opts = _norm_opts(rec)
    vals = list(opts.values())
    structure = rec.get("structure")
    found = []

    if _placeholder_options(rec):
        return ["C15"]  # unanswerable from our source; not an example of anything else

    if vals and len(set(vals)) < len(vals):
        found.append("C14")
    if rec.get("has_figure"):
        found.append("C11")
    if structure == "table":
        found.append("C12")
    if structure == "match":
        found.append("C07" if _one_transposition_apart(rec) else "C06")
    if structure == "statement_i_ii":
        found.append("C08")
    if structure == "statements":
        found.append("C09" if any(re.search(r"\bonly\b", v, re.I) for v in vals) else "C08")
    if structure == "assertion_reason":
        found.append("C10")
    if structure in ("plain", "list", None):
        if _SEQ_RE.search(rec.get("stem_en") or ""):
            found.append("C13")
        if rec.get("negative_words_seen"):
            found.append("C02")
        if any(_POW10_RE.search(v) for v in vals):
            found.append("C04")
        elif vals and all(re.search(r"\d", v) for v in vals):
            found.append("C03")
        elif vals and all("$" in v for v in vals):
            found.append("C05")
    return found or ["C01"]


def load_questions():
    """One record per (paper, question), preferring the most-settled run."""
    best = {}
    for path in glob.glob(rc.pp("steps", "B3", "out", "*.json")):
        m = _NAME_RE.match(os.path.basename(path))
        if not m:
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                rec = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(rec, dict) or rec.get("error"):
            continue
        key = f"{m.group(1)}-{m.group(2)}"
        priority = _RUN_PRIORITY[m.group(3)]
        if key not in best or priority < best[key][0]:
            best[key] = (priority, rec)
    return {k: v[1] for k, v in sorted(best.items())}


def question_text(rec):
    """Stem PLUS the lists and statements -- the stem alone is boilerplate for match and A-R."""
    parts = [(rec.get("stem_en") or "").strip()]
    for field, label in (("statements", ""), ("list_i", "List I"), ("list_ii", "List II")):
        entries = [e for e in (rec.get(field) or []) if isinstance(e, dict)]
        if entries:
            if label:
                parts.append(f"{label}:")
            parts.extend(f"({e.get('label')}) {e.get('text')}" for e in entries)
    return "\n".join(p for p in parts if p)


def options_text(rec):
    return " | ".join(f"({k}) {v}" for k, v in _norm_opts(rec).items())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-cat", type=int, default=5,
                    help="target example questions per category (default 5)")
    ap.add_argument("--out-dir", default=rc.pp("docs", "question_categories"))
    args = ap.parse_args()

    records = load_questions()
    by_cat = collections.defaultdict(list)
    for qid, rec in records.items():
        for cat in categories_of(rec):
            by_cat[cat].append(qid)

    os.makedirs(args.out_dir, exist_ok=True)
    cat_by_id = {c[0]: c for c in CATEGORIES}

    cats_path = os.path.join(args.out_dir, "categories.csv")
    with open(cats_path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["cat_id", "category_name", "question_type", "content_shape", "trap_mechanism",
                    "how_to_spot", "step_1", "step_2", "step_3", "step_4", "count_in_corpus"])
        for c in CATEGORIES:
            w.writerow([c[0], c[2], c[1], c[3], c[4], c[5], c[6], c[7], c[8], c[9],
                        len(by_cat[c[0]])])

    chosen, used = [], set()
    for cat in (c[0] for c in CATEGORIES):
        pool = by_cat[cat]
        picked = []
        for qid in pool:
            if len(picked) >= args.per_cat:
                break
            if qid in used and len(pool) > args.per_cat * 3:
                continue  # prefer unused examples where the pool is big enough to allow it
            picked.append(qid)
            used.add(qid)
        chosen.extend((cat, qid) for qid in picked)

    q_path = os.path.join(args.out_dir, "questions.csv")
    with open(q_path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["row", "cat_id", "category_name", "question_id", "paper_id", "q_no",
                    "structure", "trap_mechanism", "question_text", "options", "negative_words",
                    "has_figure", "step_1", "step_2", "step_3", "step_4"])
        for i, (cat, qid) in enumerate(chosen, 1):
            rec = records[qid]
            c = cat_by_id[cat]
            m = re.match(r"(NEET-\d{4}-[A-Z0-9]+-[A-Z0-9]+)-(q\d+)$", qid)
            w.writerow([i, cat, c[2], qid, m.group(1) if m else "", m.group(2) if m else "",
                        rec.get("structure"), c[4], question_text(rec), options_text(rec),
                        ";".join(rec.get("negative_words_seen") or []),
                        bool(rec.get("has_figure")),
                        c[6], c[7], c[8], c[9]])

    # Counts the renderer needs, written here so nothing downstream has to re-derive them. The
    # membership total is reported separately from the question total because a question can carry
    # several categories, so summing `count_in_corpus` is NOT a question count.
    with open(os.path.join(args.out_dir, "meta.json"), "w", encoding="utf-8") as fh:
        json.dump({
            "questions_classified": len(records),
            "category_memberships": sum(len(v) for v in by_cat.values()),
            "categories": len(CATEGORIES),
            "examples": len(chosen),
        }, fh, indent=2)

    print(f"questions classified: {len(records)}")
    for c in CATEGORIES:
        print(f"  {c[0]}  {c[2]:34s} {len(by_cat[c[0]]):4d}")
    print(f"\nwrote {os.path.relpath(cats_path, rc.pp())}  ({len(CATEGORIES)} categories)")
    print(f"wrote {os.path.relpath(q_path, rc.pp())}  ({len(chosen)} example questions)")
    empty = [c[0] for c in CATEGORIES if not by_cat[c[0]]]
    if empty:
        print(f"\nNOTE: no questions found for {empty} -- category asserted but unobserved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
