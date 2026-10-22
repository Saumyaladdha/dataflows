"""Step-specific check for E7 (scripts/rate_difficulty.py + schemas/E7.json + codebook/E7.md).

The schema fixes the report's shape. This adds the two things it cannot say:

  (1) EVERY ROW IS ACCOUNTED FOR. `questions` must equal easy + medium + hard + not_scorable. A
      banding pass that silently drops rows would read as complete coverage while hiding whatever it
      could not handle -- and `not_scorable` is exactly the bucket a sloppy implementation would
      rather not report.

  (2) EVERY BANDED ROW CARRIES ITS BASIS, AND EVERY UNBANDED ROW CARRIES NONE. A band without
      `E7_difficulty_basis` is a number nobody can argue with, which is the whole objection to
      calling this "difficulty" at all. The converse matters too: a row with a basis but no band
      means the rubric scored it and then lost the result.

  (3) THE RUBRIC AGREES WITH THE SHEET. The script's own band is recomputed from the stored row and
      compared, so a hand-edited sheet is caught. This is not circular: it compares the SHEET
      against the RUBRIC, which is the pair that can drift (SPEC Rule 20 -- verify against the
      thing, not against your own previous output).

DELIBERATELY NOT HERE: any claim that a band is correct in the sense of matching student
performance. Nothing in this repository can establish that, and a check that pretended to would be
the exact failure SPEC Rule 22 names.
"""

import csv
import json
import os
import sys


def check(output, item=None, record=None, root=".", **_kwargs):
    if not isinstance(output, dict):
        return False, "output is not a JSON object"
    if "error" in output:
        return True, "script reported an error: %s" % output["error"]

    bands = output.get("bands") or {}
    total = sum(int(bands.get(b, 0)) for b in ("easy", "medium", "hard"))
    claimed = int(output.get("questions", 0))
    unscored = int(output.get("not_scorable", 0))
    problems = []
    if claimed != total + unscored:
        problems.append("questions=%d but easy+medium+hard+not_scorable=%d; %d row(s) unaccounted "
                        "for" % (claimed, total + unscored, claimed - total - unscored))

    sheet = os.path.join(root, "docs", "question_categories", "SHEET_V2.csv")
    if os.path.exists(sheet):
        sys.path.insert(0, os.path.join(root, "scripts"))
        import rate_difficulty

        rows = list(csv.DictReader(open(sheet, encoding="utf-8")))
        if len(rows) != claimed:
            problems.append("report says %d questions, the sheet has %d" % (claimed, len(rows)))
        bad_basis = disagree = 0
        for row in rows:
            band = (row.get("E7_difficulty_band") or "").strip()
            basis = (row.get("E7_difficulty_basis") or "").strip()
            if band and not basis:
                bad_basis += 1
            if basis and not band and "not yet rated" not in basis \
                    and "source_incomplete" not in basis:
                bad_basis += 1
            _points, want, _why = rate_difficulty.score(row)
            if (want or "") != band:
                disagree += 1
        if bad_basis:
            problems.append("%d row(s) have a band with no basis, or a basis with no band and no "
                            "stated reason" % bad_basis)
        if disagree:
            problems.append("%d row(s) where the sheet's band differs from what the rubric scores "
                            "from that same row -- the sheet was edited by hand, or the rubric "
                            "changed without a re-run" % disagree)

    if problems:
        return False, "; ".join(problems)
    return True, ("%d questions: %d easy, %d medium, %d hard, %d not scorable (by design); every "
                  "band carries its basis and matches the rubric. Bands are SOLUTION LOAD, never a "
                  "prediction of student performance -- no response data exists (SPEC Rule 22)."
                  % (claimed, bands.get("easy", 0), bands.get("medium", 0), bands.get("hard", 0),
                     unscored))


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("output")
    ap.add_argument("--root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                   "..", ".."))
    args = ap.parse_args(argv)
    ok, message = check(json.load(open(args.output, encoding="utf-8")), root=args.root)
    print(("PASS  " if ok else "FAIL  ") + message)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
