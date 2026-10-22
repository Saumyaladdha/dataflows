#!/usr/bin/env python3
"""Reconcile every category sheet we have produced against the tagged corpus.

    python3 scripts/checks/category_sheet_reconcile.py

Seven artefacts describe "the categories", written at different times by different scripts:

    exports/discovery/CATEGORIES.xlsx            the v1 codebook -- definitions + per-axis counts
    exports/discovery/QUESTIONS.xlsx             the v1 applied tags, 580 questions   <- the corpus
    exports/discovery/QUESTIONS_SHOWCASE.xlsx    55 of those, plus a Coverage tab
    docs/question_categories/RULEBOOK.md         the v2 rulebook
    docs/question_categories/SHEET_V2.csv        the v2 sheet, all 580 questions
    docs/question_categories/categories.csv      15 composite categories with solving recipes
    exports/discovery/clusters_pass_b/*.json     per-subject discovered dimensions

A count printed in a codebook is a claim about the corpus, so it can be checked. Where the
codebook's `Total` disagrees with the tags actually present, one of the two was written against a
state the other never saw -- and a reader cannot tell which. This script finds those.
"""

import collections
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import runner_core as rc  # noqa: E402

AXES = [
    ("E1", "E1 Question type", "E1 question type"),
    ("E2", "E2 Format", "E2 format"),
    ("E3", "E3 Content shape", "E3 content shape"),
    ("E4", "E4 Thinking", "E4 thinking"),
    ("E5", "E5 Trap", "E5 trap"),
]
BLANK = ("", "none", "-")


def codebook():
    """Each axis sheet of CATEGORIES.xlsx: label -> (claimed total, definition, status)."""
    import openpyxl
    wb = openpyxl.load_workbook(rc.pp("exports", "discovery", "CATEGORIES.xlsx"), read_only=True)
    out = {}
    for axis, sheet, _ in AXES:
        rows = [[("" if c is None else str(c)) for c in r]
                for r in wb[sheet].iter_rows(values_only=True)]
        head = next((i for i, r in enumerate(rows) if r and r[0] == "Category"), None)
        if head is None:
            out[axis] = {}
            continue
        cols = {h: i for i, h in enumerate(rows[head]) if h}
        d = {}
        for r in rows[head + 1:]:
            if not r or not r[0].strip():
                continue
            total = r[cols["Total"]].strip() if "Total" in cols else ""
            d[r[0].strip()] = (
                int(total) if total.isdigit() else None,
                r[cols["What it means"]].strip() if "What it means" in cols else "",
                r[cols["Status"]].strip() if "Status" in cols else "",
            )
        out[axis] = d
    return out


def corpus():
    """Each axis of QUESTIONS.xlsx: label -> how many questions actually carry it."""
    import openpyxl
    wb = openpyxl.load_workbook(rc.pp("exports", "discovery", "QUESTIONS.xlsx"), read_only=True)
    rows = list(wb["Questions"].iter_rows(values_only=True))
    head = {h: i for i, h in enumerate(rows[0]) if h}
    out = {}
    for axis, _, col in AXES:
        counts = collections.Counter()
        for raw in rows[1:]:
            for label in str(raw[head[col]] or "").split(";"):
                label = label.strip()
                if label and label.lower() not in BLANK:
                    counts[label] += 1
        out[axis] = counts
    return out, len(rows) - 1


def rulebook_labels():
    """Labels the v2 rulebook accounts for, per axis -- live, retired and prose-stated alike.

    Imported from the census rather than re-parsed here. Two parsers over one document is how this
    check reported `opposite_answer` as undefined while the census correctly reported it retired:
    whichever one you read, the other disagreed.
    """
    import category_label_census as census
    secs = census.rulebook_sections()
    out = {}
    for axis, _, _ in AXES:
        section = secs.get(census.SECTION[axis], "")
        live, retired = census.split_retired(section)
        out[axis] = set(live) | set(retired) | set(census.PROSE_LABELS.get(axis, ()))
    return out


def main():
    book, (corp, total) = codebook(), corpus()
    rb = rulebook_labels()
    print("corpus: %d questions\n" % total)

    bad = 0
    for axis, _, _ in AXES:
        claims, actual = book[axis], corp[axis]
        mismatched = [(l, c, actual.get(l, 0)) for l, (c, _, _) in sorted(claims.items())
                      if c is not None and c != actual.get(l, 0)]
        orphan = sorted(l for l in actual if l not in claims)
        print("%s  codebook defines %2d  corpus uses %2d  rulebook defines %2d"
              % (axis, len(claims), len(actual), len(rb.get(axis, ()))))
        print("      codebook count != corpus count : %2d" % len(mismatched))
        for label, claimed, found in sorted(mismatched, key=lambda x: -abs(x[1] - x[2])):
            print("         %-32s codebook %3d   corpus %3d   (%+d)"
                  % (label, claimed, found, found - claimed))
        if orphan:
            print("      tagged but NOT in the codebook  : %s" % ", ".join(orphan))
        missing = sorted(l for l in claims if l not in rb.get(axis, ()))
        print("      in the codebook, absent from the v2 rulebook: %2d%s"
              % (len(missing), ("   " + ", ".join(missing)) if missing else ""))
        print()
        bad += len(mismatched)

    print("--- the other sheets ---")
    # categories.csv is a TEACHING taxonomy, not a classification one: 15 composite categories, each
    # with a four-step solving recipe. Its question_type / content_shape / trap_mechanism columns are
    # prose by design and must NOT be read as axis labels -- doing so reports ~70 phantom faults.
    # Its categories deliberately overlap (a figure-dependent question can also be a numeric one), so
    # count_in_corpus summing past 580 is expected. What cannot be checked is each individual count,
    # because no column records the rule that produced it.
    cats = rc.pp("docs", "question_categories", "categories.csv")
    rows = list(csv.DictReader(open(cats, encoding="utf-8")))
    claimed = sum(int(r["count_in_corpus"]) for r in rows if r["count_in_corpus"].strip().isdigit())
    print("categories.csv       %2d composite categories (overlapping by design)" % len(rows))
    print("   count_in_corpus sums to %d over %d questions (%.1f categories per question)"
          % (claimed, total, claimed / float(total)))
    print("   every count is hand-written with no derivation rule recorded -> SPEC Rule 23")
    recipes = sum(1 for r in rows if all((r.get("step_%d" % i) or "").strip() for i in (1, 2, 3, 4)))
    print("   %d of %d carry a complete four-step recipe" % (recipes, len(rows)))

    sheet2 = rc.pp("docs", "question_categories", "SHEET_V2.csv")
    v2 = list(csv.DictReader(open(sheet2, encoding="utf-8")))
    print("SHEET_V2.csv         %2d rows  (%.0f%% of the corpus)" % (len(v2), 100.0 * len(v2) / total))

    for path in sorted(glob.glob(rc.pp("exports", "discovery", "clusters_pass_b", "*.json"))):
        d = json.load(open(path, encoding="utf-8"))
        dims = d.get("dimensions") or {}
        names = list(dims) if isinstance(dims, dict) else ["%d dims" % len(dims)]
        n = d.get("n_questions_analysed") or d.get("questions_analysed")
        print("%-20s %s questions, dimensions: %s"
              % (os.path.basename(path).replace("_categories.json", ""), n, ", ".join(map(str, names))))

    # CATEGORIES.xlsx is frozen history (see the rulebook's authority map), so its hand-written
    # totals will disagree with the corpus for good. Report the drift; do not fail on it -- a check
    # that can never pass is a check everyone learns to ignore. What WOULD be a failure is a label
    # applied to a question with no definition governing it, and that is what the census gates.
    print("\n%d count disagreements between the codebook and the corpus" % bad)
    print("   expected: CATEGORIES.xlsx is frozen history and its Total column must not be cited.")
    print("   the gate that can fail is scripts/checks/category_label_census.py")
    undefined = sum(1 for axis, _, _ in AXES for l in corp[axis] if l not in rb.get(axis, ()))
    print("\n%d labels applied to a question with no definition governing them" % undefined)
    return 1 if undefined else 0


if __name__ == "__main__":
    sys.exit(main())
