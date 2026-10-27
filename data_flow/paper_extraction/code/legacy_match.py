#!/usr/bin/env python3
"""Spec Section 13 "Legacy fields": match each bank question to the legacy sheets and store
`legacy_chapter`, `legacy_topic`, `legacy_question_type`.

    python3 scripts/legacy_match.py --all                 # dry run over every canonical question
    python3 scripts/legacy_match.py --item-id Q-000015    # one question, with the runner-up
    python3 scripts/legacy_match.py --all --write         # actually store the fields
    python3 scripts/legacy_match.py --self-test           # the metric's own behaviour

Spec, verbatim: "`legacy_match.py` matches each bank question to the legacy sheets by text
similarity (>= 0.85 on word 3-grams after normalisation, same year) and stores `legacy_chapter`,
`legacy_topic`, `legacy_question_type`. These are never inputs to any agent. Stage F shows them
beside the pipeline's values."

=== THE RULE THAT MATTERS MOST: THESE FIELDS NEVER REACH AN AGENT ===

Spec 2.2's finding is that the legacy tags ARE NOT USABLE -- the sheets contain confirmed
"Assertion-Reason" rows with no assertion in them at all, and free-form `Question Type` strings
like "Numerical + Application" and "Statement-Based + Conceptual" that are not the pipeline's
taxonomy and were never validated against it. Their entire purpose is to sit NEXT TO the
pipeline's own tags in Stage F so a human can see where the two disagree. If one ever leaked into
an E-step's agent input, the tag it is supposed to be compared against would be anchored to it,
and the comparison would be measuring the leak.

So this module exports the mechanism, not just the warning: `LEGACY_FIELDS` names the three
fields, and `assert_no_legacy(payload, where)` raises if any of them (or any other `legacy_`
key) appears anywhere in a nested agent-input payload. Every E-step input builder should call it,
the same belt-and-braces B6's coaching guard already uses for the answer key. The call site is
specified in config/_pending_E_entries.yaml because scripts/step_plugins.py is owned elsewhere.

=== WHAT IS MATCHED, AND HOW ===

The sheets' own columns are `Chapter Name`, `Topic` and `Question Type`, confirmed present and
identically named in all 22 real sheets (2010-2026). The `Question` column holds the stem followed
by the four options as `a) ... b) ... c) ... d) ...`, which is the text the similarity runs on --
the whole cell against the record's whole text (stem + statements + options), because a stem alone
is often one short line and two different questions on the same NCERT line can share it.

Normalisation and the 3-gram set are reused from `scripts/verify_sources.py`
(`norm_tokens`/`ngrams`/`jaccard`), not reimplemented. That module's normalisation already answers
the differences that really occur between these sources -- markdown image links (the sheet stores
every figure as a mathpix URL), unicode sub/superscript digits, the scrape's `[bracketed
description]` stand-ins, and LaTeX written two ways (`\\dfrac` vs `\\frac`) -- and it was built and
verified against these exact files. A second copy of that logic here would drift from it, and the
drift would show up as silent non-matches.

`jaccard` on 3-gram SETS is the metric spec names ("0.85 on word 3-grams"). Note what that
threshold means in practice: it is strict. Jaccard punishes extra material on either side, and the
sheet cell and the scrape record genuinely differ in how much they carry -- so a real pair of
transcriptions of the same question typically scores well below 0.85. This is reported honestly
rather than quietly loosened: `--all` prints every question's best score so the real distribution
is visible, and a score below the threshold stores NOTHING. Loosening spec's number, or swapping
in a more forgiving metric, would be a decision about data quality and is the owner's to make, not
this script's. `scripts/verify_sources.py` -- which exists to decide whether two sources describe
the same question -- deliberately decides on the GAP to the runner-up rather than on an absolute
similarity, for exactly this reason; that is the alternative to propose if spec's 0.85 proves
unusable.

=== SAME YEAR ===

A record carries `year` and `sitting`. Sheets are resolved from `verify_sources.OWNER_INDEX`, the
owner's authoritative year -> sitting -> file index (2026-10-12), so a multi-sitting year picks the
right sheet instead of guessing from the filename: 2010-2012 have Preliminary + Main, 2016 has
Phase I + Phase II, 2026 has the 3 May sitting plus the 21 Jun re-NEET. When the record's sitting
is not in the index, every sheet of that year is searched and the best match wins -- never a sheet
from another year, which is what "same year" in spec means.
"""
import argparse
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402
try:
    import verify_sources as vs  # noqa: E402
except ImportError:
    # verify_sources.py lives in _shared/code, not here. Only the legacy-SHEET matching below needs
    # it; `assert_no_legacy`, which step_plugins calls on every E-stage input, does not. A hard
    # import stopped step_plugins loading at all, so no paper step could even be listed.
    class _VerifySourcesElsewhere:
        def __getattr__(self, attr):
            raise SystemExit("verify_sources.py is not part of paper_extraction -- it lives in "
                             "_shared/code. Legacy-sheet matching (vs.%s) cannot run here." % attr)
    vs = _VerifySourcesElsewhere()
from lib import records as lib_records  # noqa: E402

#: Spec Section 13's three legacy fields. Never an input to any agent.
LEGACY_FIELDS = ("legacy_chapter", "legacy_topic", "legacy_question_type")

#: Spec's own threshold: >= 0.85 jaccard on word 3-grams after normalisation.
MATCH_THRESHOLD = 0.85

#: The sheet columns the three fields come from.
SHEET_COLUMNS = {
    "legacy_chapter": "Chapter Name",
    "legacy_topic": "Topic",
    "legacy_question_type": "Question Type",
}

#: The step name recorded in the record's `field_sources` for these fields. Not a step in
#: config/steps.yaml: spec Section 13 puts legacy matching under "Legacy fields", after E6 and
#: outside the E0-E6 sequence, with no agent, no runs and no checks of its own.
STEP_NAME = "LEGACY"


# ---------------------------------------------------------------------------
# The guard: these fields never reach an agent
# ---------------------------------------------------------------------------


def assert_no_legacy(payload, where="agent input"):
    """Raise ValueError if any `legacy_` key appears anywhere in a nested payload.

    Call this on every agent input before it is written. Spec Section 13: the legacy fields "are
    never inputs to any agent" -- and spec 2.2 is that the legacy tags are not usable, so a leak
    would anchor the very tag it is meant to be compared against."""
    def walk(node, path):
        if isinstance(node, dict):
            for k, v in node.items():
                if str(k).startswith("legacy_"):
                    raise ValueError(
                        f"{where} contains {path + '.' + str(k) if path else str(k)!r}: the legacy "
                        f"fields are never inputs to any agent (spec Section 13). They exist only "
                        f"so Stage F can show them beside the pipeline's own values.")
                walk(v, f"{path}.{k}" if path else str(k))
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]")
    walk(payload, "")
    return payload


# ---------------------------------------------------------------------------
# The sheets
# ---------------------------------------------------------------------------


class TaggedSheet:
    """One legacy sheet's rows, keeping the three tag columns alongside the question text.

    `verify_sources.SheetIndex` already reads these files but keeps only the question text and the
    answer letter, because that is all source verification needs. This class exists for the three
    extra columns, and reuses that module's normalisation so the two cannot disagree about what
    two texts being "the same" means."""

    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.rows = []
        self._grams = []
        if not os.path.exists(path):
            return
        try:
            import openpyxl
        except ImportError:  # pragma: no cover
            return
        try:
            wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        except Exception:  # noqa: BLE001
            return
        try:
            tab = "All Questions" if "All Questions" in wb.sheetnames else wb.sheetnames[0]
            raw = list(wb[tab].iter_rows(values_only=True))
        finally:
            wb.close()
        if not raw:
            return
        header = [str(c).strip() if c is not None else "" for c in raw[0]]

        def col(name):
            return header.index(name) if name in header else None

        q_i = col("Question")
        if q_i is None:
            return
        idx = {field: col(column) for field, column in SHEET_COLUMNS.items()}
        for row_no, row in enumerate(raw[1:], start=2):
            if not row or q_i >= len(row) or not row[q_i]:
                continue

            def cell(i):
                if i is None or i >= len(row) or row[i] is None:
                    return ""
                value = row[i]
                # The sheets store Chapter No as a float; a chapter NAME is always text, but be
                # defensive -- a numeric cell must not become "4.0" in a reviewer's column.
                if isinstance(value, float) and value.is_integer():
                    return str(int(value))
                return str(value).strip()

            self.rows.append({
                "sheet": self.name,
                "row": row_no,
                "text": str(row[q_i]),
                **{field: cell(i) for field, i in idx.items()},
            })
        self._grams = [(r, vs.ngrams(vs.norm_tokens(r["text"]))) for r in self.rows]

    def best(self, query_grams):
        """(row, similarity, runner_up_similarity) for the closest row, or (None, 0.0, 0.0)."""
        scored = sorted(((vs.jaccard(query_grams, g), i) for i, (_, g) in enumerate(self._grams)),
                         reverse=True)
        if not scored:
            return None, 0.0, 0.0
        best_sim, best_i = scored[0]
        runner = scored[1][0] if len(scored) > 1 else 0.0
        return self._grams[best_i][0], best_sim, runner

    def __len__(self):
        return len(self.rows)


_SHEET_CACHE = {}


def sheet_paths_for(year, sitting=None):
    """Every legacy sheet for one year, the record's own sitting first when the index knows it.

    `verify_sources._sheet_sitting_lookup()` is the owner's authoritative index (2026-10-12),
    which is better evidence than inferring a sitting from a filename."""
    lookup = vs._sheet_sitting_lookup()  # {xlsx basename: (year, sitting)}
    exact, same_year = [], []
    for basename, (sheet_year, sheet_sitting) in sorted(lookup.items()):
        if sheet_year != year:
            continue
        path = os.path.join(vs.SHEETS_DIR, basename)
        if not os.path.exists(path):
            continue
        if sitting and sheet_sitting == sitting:
            exact.append(path)
        else:
            same_year.append(path)
    return exact + same_year


def load_sheet(path):
    if path not in _SHEET_CACHE:
        _SHEET_CACHE[path] = TaggedSheet(path)
    return _SHEET_CACHE[path]


# ---------------------------------------------------------------------------
# Matching
# ---------------------------------------------------------------------------


def record_text(record):
    """The record's whole comparable text: stem + lettered statements + list rows + options.

    The sheet's `Question` cell holds all of it in one string, so comparing the whole against the
    whole is the only like-for-like comparison. verify_sources.record_full_text already builds
    exactly this, and is reused so the two cannot drift."""
    return vs.record_full_text(record)


def match_one(record):
    """Match one record against its year's sheets.

    Returns a dict describing the attempt, always -- including when nothing met the threshold,
    because "the best available row scored 0.41" is the finding spec's 0.85 threshold produces on
    this data and hiding it behind a None would be the one unhelpful outcome."""
    year = record.get("year")
    sitting = record.get("sitting")
    result = {
        "question_id": record.get("question_id"),
        "year": year,
        "sitting": sitting,
        "sheets_searched": [],
        "best": None,
        "similarity": 0.0,
        "runner_up": 0.0,
        "matched": False,
        "fields": {},
        "why": "",
    }
    if not year:
        result["why"] = "record has no year, so 'same year' cannot be satisfied"
        return result

    paths = sheet_paths_for(year, sitting)
    if not paths:
        result["why"] = f"no legacy sheet on disk for year {year}"
        return result

    query = vs.ngrams(vs.norm_tokens(record_text(record)))
    best_row, best_sim, runner = None, 0.0, 0.0
    for path in paths:
        sheet = load_sheet(path)
        result["sheets_searched"].append(f"{sheet.name} ({len(sheet)} rows)")
        row, sim, run_up = sheet.best(query)
        if row is not None and sim > best_sim:
            best_row, best_sim, runner = row, sim, max(run_up, best_sim)

    result["best"] = best_row
    result["similarity"] = best_sim
    result["runner_up"] = runner

    if best_row is None:
        result["why"] = "no readable rows in the year's sheet(s)"
        return result
    if best_sim < MATCH_THRESHOLD:
        result["why"] = (f"best row scored {best_sim:.3f} on word 3-grams, below spec's "
                           f"{MATCH_THRESHOLD} threshold, so nothing is stored")
        return result

    result["matched"] = True
    result["fields"] = {field: best_row.get(field) or "" for field in LEGACY_FIELDS}
    result["why"] = (f"{best_row['sheet']} row {best_row['row']} scored {best_sim:.3f} "
                       f"(>= {MATCH_THRESHOLD})")
    return result


def canonical_records():
    """Every record in papers/records/ that is not the absorbed half of a C1 merge."""
    import json
    records_dir = rc.pp("papers", "records")
    out = []
    for fn in sorted(os.listdir(records_dir)):
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        with open(os.path.join(records_dir, fn), "r", encoding="utf-8") as f:
            try:
                rec = json.load(f)
            except Exception:  # noqa: BLE001
                continue
        if isinstance(rec, dict) and not rec.get("merged_into"):
            out.append(rec)
    return out


def store(result, prompt_version="v1"):
    """Write the three fields onto the record. Only ever called for a real match."""
    lib_records.set_fields(result["question_id"], result["fields"],
                            step=STEP_NAME, prompt_version=prompt_version, status="pass")


# ---------------------------------------------------------------------------
# Self-test: the metric's own behaviour, on the real normalisation
# ---------------------------------------------------------------------------

_SELF_TEST_CASES = [
    ("identical text scores 1.0", "The dimensions of mu0 epsilon0 are",
     "The dimensions of mu0 epsilon0 are", 1.0, 1.0),
    ("the same question with a figure URL stripped still scores 1.0",
     "Find the current in the circuit shown",
     "Find the current in the circuit shown ![](https://cdn.mathpix.com/snip/images/x.jpg)",
     1.0, 1.0),
    ("two different questions on the same topic score low",
     "The dimensions of mu0 epsilon0 are",
     "A galvanometer of resistance G is shunted by a resistance S ohm",
     0.0, 0.2),
    ("LaTeX written two ways converges",
     r"the potential is $-\dfrac{16Gm}{R}$",
     r"the potential is $-\frac{16Gm}{R}$",
     1.0, 1.0),
]


def _self_test():
    failures = []
    for name, a, b, lo, hi in _SELF_TEST_CASES:
        sim = vs.jaccard(vs.ngrams(vs.norm_tokens(a)), vs.ngrams(vs.norm_tokens(b)))
        ok = lo <= sim <= hi
        print(f"{'ok  ' if ok else 'FAIL'}  {sim:.3f}  (expected {lo}..{hi})  {name}")
        if not ok:
            failures.append(name)

    # The guard must actually raise, nested.
    try:
        assert_no_legacy({"question": {"stem_en": "x"}, "meta": [{"legacy_topic": "Dimensions"}]})
        print("FAIL  assert_no_legacy did not raise on a nested legacy_ key")
        failures.append("assert_no_legacy nested")
    except ValueError as e:
        print(f"ok    assert_no_legacy raised: {str(e)[:70]}...")
    try:
        assert_no_legacy({"question": {"stem_en": "x"}, "allowed": ["a", "b"]})
        print("ok    assert_no_legacy passes a clean payload")
    except ValueError as e:  # pragma: no cover
        print(f"FAIL  assert_no_legacy raised on a clean payload: {e}")
        failures.append("assert_no_legacy clean")

    print()
    if failures:
        print(f"{len(failures)} FAILED")
        return 1
    print("all self-tests pass")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _print_one(result, verbose=True):
    qid = result["question_id"]
    best = result["best"]
    mark = "MATCH" if result["matched"] else "  -  "
    # The gap to the runner-up is printed beside the similarity because on real data it is the
    # number that actually separates a right row from a wrong one -- see the module docstring.
    runner = result["runner_up"]
    gap = f"{result['similarity'] / runner:.1f}x" if runner > 0 else "inf"
    print(f"{mark} {qid}  sim={result['similarity']:.3f}  gap={gap:>6}  {result['why']}")
    if verbose and best:
        print(f"        sheets: {', '.join(result['sheets_searched'])}")
        print(f"        best row: {best['sheet']} row {best['row']}")
        for field in LEGACY_FIELDS:
            print(f"          {field:<22} {best.get(field) or '(blank)'!r}")
        print(f"        runner-up similarity in that sheet: {result['runner_up']:.3f}")


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Spec 13 'Legacy fields': match bank questions to the legacy sheets.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--item-id", help="One question id, e.g. Q-000015.")
    g.add_argument("--all", action="store_true", help="Every canonical record.")
    g.add_argument("--self-test", action="store_true", help="The metric and the guard.")
    ap.add_argument("--write", action="store_true",
                    help="Store the three fields on matched records. Without this it is a dry run.")
    args = ap.parse_args(argv)

    if args.self_test:
        return _self_test()

    if args.item_id:
        record = lib_records.read_record(args.item_id)
        if not record:
            print(f"no record for {args.item_id}", file=sys.stderr)
            return 2
        records = [record]
    else:
        records = canonical_records()

    matched, stored = 0, 0
    print(f"threshold: jaccard >= {MATCH_THRESHOLD} on word 3-grams, same year "
          f"(spec Section 13)\n")
    for record in records:
        result = match_one(record)
        _print_one(result, verbose=bool(args.item_id))
        if result["matched"]:
            matched += 1
            if args.write:
                store(result)
                stored += 1

    print(f"\n{len(records)} question(s); {matched} met spec's {MATCH_THRESHOLD} threshold; "
          f"{stored} written"
          + ("" if args.write else " (dry run -- pass --write to store)"))
    if matched == 0 and records:
        print("\nNOTE: zero matches at spec's 0.85 jaccard-on-3-grams threshold is a real "
              "finding about the metric, not about whether the questions are in the sheets -- "
              "scripts/verify_sources.py separately matched all 10 canonical records in both the "
              "year-wise book and the legacy sheet, deciding on the GAP to the runner-up rather "
              "than on an absolute similarity. See this module's docstring; loosening spec's "
              "number is the owner's call.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
