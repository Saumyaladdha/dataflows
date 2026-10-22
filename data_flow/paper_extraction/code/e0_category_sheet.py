#!/usr/bin/env python3
"""E0's SCRIPT half (spec 13/E0 step 3): export `codebook/E0_findings/category_sheet.csv`.

    python3 scripts/e0_category_sheet.py --check        # can E0 meaningfully run yet?
    python3 scripts/e0_category_sheet.py                # build the real sheet
    python3 scripts/e0_category_sheet.py --inputs <dir> --out <path>   # test / inspect elsewhere

Spec 13/E0, step 3, verbatim: "SCRIPT: export `codebook/E0_findings/category_sheet.csv` with
columns `tag, category, definition, subjects, example_1, example_2, count_physics,
count_chemistry, count_biology, years_seen, decision`." Those eleven columns, in that order, and
no others -- a twelfth column would be this script deciding what the owner's sheet says.

THE ONE RULE THAT GOVERNS THIS FILE. Spec 13/E0: "**Never:** write `codebook/E*.md`. Those are the
owner's." E0 gives the owner data so the owner can write a codebook; it never writes one, and it
never edits `config/allowed_values.yaml` either. That is enforced by construction, not by
intention: `_assert_writable()` refuses any destination that is not a `category_sheet.csv`, and
refuses outright any path that looks like a codebook markdown file. tests/test_e_checks.py asserts
both refusals. The six `codebook/E*.md` files that now exist were drafted by the pipeline at the
owner's later request -- that lifted the prohibition for a human-directed drafting task, not for
this script, which runs unattended inside a step.

WHY THIS CANNOT MEANINGFULLY RUN TODAY, STATED UP FRONT. Spec 13/E0's sample is "~300 questions
from the most recent papers available ... ~100 per subject, across many chapters". The bank holds
TEN canonical questions, every one of them from a single paper (2023 MAIN, booklet codes E1/E2),
split 6 Physics / 2 Chemistry / 1 Biology / 1 with no subject assigned. Grouping ten free answers
would hand the owner a category sheet whose counts are 1s and 2s, against a taxonomy that ~500
real sampled questions already validated -- an invitation to decide a real question on noise. So
`--check` reports the shortfall, and a build below SAMPLE_FLOOR refuses unless
`--allow-small-sample` is passed, which stamps the reason into the run's own stdout. Nothing about
the shortfall is a flag: spec 16 gives E0 exactly one flag (E0_FINDINGS_READY, normal) and
inventing a second would be inventing a flag.

INPUT. One `e0-category-grouper` output per tag, as written by the runner, read from
`steps/E0/out/` by default: any `*.json` whose content matches the grouper branch of
`schemas/E0.json` (it has a `categories` key). Open-look outputs in the same directory are
skipped, not errors -- they are the grouper's input, not this script's.
"""
import argparse
import csv
import glob
import json
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402

#: Spec 13/E0's eleven columns, in spec's own order. Never add to this.
COLUMNS = [
    "tag", "category", "definition", "subjects", "example_1", "example_2",
    "count_physics", "count_chemistry", "count_biology", "years_seen", "decision",
]

SUBJECTS = ("Physics", "Chemistry", "Biology")

#: Spec 13/E0's sample is ~300 questions, ~100 per subject. The floor below which a category sheet
#: would mislead rather than inform. Not a spec number -- a judgement, stated so it can be argued
#: with, and overridable on the command line rather than silently.
SAMPLE_FLOOR = 300
PER_SUBJECT_FLOOR = 100

#: The one file this script may write.
SHEET_RELPATH = os.path.join("codebook", "E0_findings", "category_sheet.csv")


def _assert_writable(path):
    """Refuse any destination that is not a `category_sheet.csv`, and any codebook markdown file.

    Spec 13/E0's Never is absolute, so it is a precondition in code rather than a comment. The
    check is on the resolved basename and extension, so neither a relative path, a symlink target
    name, nor an `--out` pointing into `codebook/` can route a write to `codebook/E4.md`."""
    base = os.path.basename(os.path.abspath(path))
    if base.lower().endswith(".md"):
        raise ValueError(
            f"refusing to write {path!r}: E0 must NEVER write a codebook markdown file "
            f"(spec 13/E0: 'Never: write codebook/E*.md. Those are the owner's.')")
    if base != "category_sheet.csv":
        raise ValueError(
            f"refusing to write {path!r}: E0's only output is category_sheet.csv "
            f"(spec 13/E0 step 3)")
    return path


# ---------------------------------------------------------------------------
# Sample adequacy
# ---------------------------------------------------------------------------


def sample_state():
    """(rows, total, per_subject) describing the canonical questions E0 could draw on.

    Reads papers/records/ directly, skipping the absorbed half of every C1 merge (its twin carries
    the tags), so the count is the real number of distinct questions and not inflated by merges."""
    records_dir = rc.pp("papers", "records")
    rows, per_subject = [], {s: 0 for s in SUBJECTS}
    unassigned = 0
    if not os.path.isdir(records_dir):
        return rows, 0, per_subject, 0
    for fn in sorted(os.listdir(records_dir)):
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        with open(os.path.join(records_dir, fn), "r", encoding="utf-8") as f:
            try:
                rec = json.load(f)
            except Exception:  # noqa: BLE001
                continue
        if not isinstance(rec, dict) or rec.get("merged_into"):
            continue
        rows.append(rec)
        subject = rec.get("subject")
        if subject in per_subject:
            per_subject[subject] += 1
        else:
            unassigned += 1
    return rows, len(rows), per_subject, unassigned


def report_sample():
    """Print the honest state of E0's sample. Returns True when it meets spec 13/E0's size."""
    rows, total, per_subject, unassigned = sample_state()
    years = sorted({r.get("year") for r in rows if r.get("year")})
    papers = sorted({code.split(":")[0] for r in rows for code in (r.get("paper_codes") or [])})

    print(f"canonical questions in the bank: {total}  (spec 13/E0 asks for ~{SAMPLE_FLOOR})")
    for s in SUBJECTS:
        print(f"  {s:<10} {per_subject[s]:>4}   (spec asks for ~{PER_SUBJECT_FLOOR})")
    if unassigned:
        print(f"  {'(no subject)':<10} {unassigned:>4}   (B7 has not run on these)")
    print(f"  years represented : {years or '(none)'}")
    print(f"  booklet codes     : {papers or '(none)'}")

    ok = total >= SAMPLE_FLOOR and all(per_subject[s] >= PER_SUBJECT_FLOOR for s in SUBJECTS)
    print()
    if ok:
        print("sample meets spec 13/E0's size")
    else:
        print(f"E0 CANNOT MEANINGFULLY RUN YET. {total} question(s) from "
              f"{len(papers)} booklet code(s) and {len(years)} year(s) cannot support a category "
              f"decision: the counts would be 1s and 2s against a taxonomy that ~500 real sampled "
              f"questions already validated. Collect the sample first (spec 13/E0: ~300 questions "
              f"from the most recent papers, ~100 per subject, across many chapters).")
    return ok


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------


def load_grouper_outputs(inputs_dir):
    """Every e0-category-grouper output in `inputs_dir`, newest-name-last. Open-look outputs in
    the same directory are skipped (they are the grouper's input, not this script's)."""
    out = []
    for path in sorted(glob.glob(os.path.join(inputs_dir, "*.json"))):
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception as e:  # noqa: BLE001
                print(f"  skipped {os.path.basename(path)}: not valid JSON ({e})")
                continue
        if not isinstance(data, dict):
            continue
        if "error" in data:
            print(f"  skipped {os.path.basename(path)}: agent reported error "
                  f"({data['error']!r})")
            continue
        if "categories" not in data:
            continue  # an open-look output, or something else entirely
        out.append((path, data))
    return out


def rows_from(outputs):
    """The sheet's rows, one per category, in tag order then the agent's own category order.

    Nothing is computed, re-grouped, re-counted or re-decided here: every cell is the agent's own
    value, because `decision` is the owner's call to make from the agent's evidence and this
    script's job is to lay that evidence out, not to form an opinion about it."""
    rows = []
    for path, data in outputs:
        tag = data.get("tag") or ""
        for cat in data.get("categories") or []:
            if not isinstance(cat, dict):
                continue
            counts = cat.get("count") or {}
            examples = list(cat.get("examples") or [])
            rows.append({
                "tag": tag,
                "category": cat.get("name") or "",
                "definition": cat.get("definition") or "",
                "subjects": "; ".join(str(s) for s in (cat.get("subjects") or [])),
                "example_1": str(examples[0]) if len(examples) > 0 else "",
                "example_2": str(examples[1]) if len(examples) > 1 else "",
                "count_physics": int(counts.get("Physics") or 0),
                "count_chemistry": int(counts.get("Chemistry") or 0),
                "count_biology": int(counts.get("Biology") or 0),
                "years_seen": "; ".join(str(y) for y in (cat.get("years_seen") or [])),
                "decision": cat.get("decision") or "",
            })
    return rows


def write_sheet(rows, out_path):
    _assert_writable(out_path)
    rc.ensure_dir(os.path.dirname(os.path.abspath(out_path)))
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return out_path


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="E0's category sheet (spec 13/E0 step 3). Never writes codebook/E*.md.")
    ap.add_argument("--check", action="store_true",
                    help="Report whether E0's sample meets spec 13/E0's size, and stop.")
    ap.add_argument("--inputs", default=None,
                    help="Directory of e0-category-grouper outputs (default steps/E0/out).")
    ap.add_argument("--out", default=None,
                    help=f"Destination CSV (default {SHEET_RELPATH}). The basename must be "
                          f"category_sheet.csv.")
    ap.add_argument("--allow-small-sample", action="store_true",
                    help="Build the sheet even though the sample is below spec 13/E0's size. "
                          "The reason is printed into the run's own output.")
    args = ap.parse_args(argv)

    sample_ok = report_sample()
    if args.check:
        return 0 if sample_ok else 1

    if not sample_ok and not args.allow_small_sample:
        print("\nnot building a sheet. Re-run with --allow-small-sample to build one anyway "
              "(the shortfall above will still be printed).")
        return 1
    if not sample_ok:
        print("\n--allow-small-sample given: building a sheet from a sample that does NOT meet "
              "spec 13/E0's size. Treat every count in it as provisional.")

    inputs_dir = args.inputs or rc.pp("steps", "E0", "out")
    out_path = args.out or rc.pp(*SHEET_RELPATH.split(os.sep))

    print(f"\nreading e0-category-grouper outputs from {inputs_dir}")
    if not os.path.isdir(inputs_dir):
        print("  (directory does not exist -- E0 has never run)")
        outputs = []
    else:
        outputs = load_grouper_outputs(inputs_dir)
    print(f"  {len(outputs)} grouper output(s)")
    if not outputs:
        print("\nnothing to export: no e0-category-grouper output exists. Not writing an empty "
              "sheet, which would read as 'the discovery found nothing'.")
        return 1

    rows = rows_from(outputs)
    write_sheet(rows, out_path)
    tags = sorted({r["tag"] for r in rows})
    print(f"\nwrote {out_path}")
    print(f"  {len(rows)} category row(s) across tag(s): {', '.join(tags)}")
    print(f"  columns: {', '.join(COLUMNS)}")
    print("\nThis sheet is DATA FOR THE OWNER. E0 never writes codebook/E*.md and never edits "
          "config/allowed_values.yaml; a new value is added only after Stage F names it "
          "(spec 17).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
