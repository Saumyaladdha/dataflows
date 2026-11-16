#!/usr/bin/env python3
"""Rename the E7 hardness row from "the catch" to "what makes it harder" in a finished export.

WHY A PATCHER AND NOT A RE-EXPORT
---------------------------------
The generators are already fixed (`export_paper_v2.py`, `join_difficulty_into_export.py`), so
every export built from here on carries the new label. But most papers in `data/` cannot be
rebuilt: `export_paper_v2.py --data --paper-id 2024_S1` answers "no v2 papers found", because
these are finished exports whose v2 CORPUS record no longer exists -- the same reason the
`join_*_into_export.py` patchers exist at all. So the label is corrected in place.

WHY THE LABEL MOVED
-------------------
Two different fields wanted the name "the catch":

  * E7's `what_makes_it_hard` -- the factor BESIDES step count. OPTIONAL, so the row is simply
    absent whenever E7 leaves it empty: 83 of 200 questions on 2024_S1.
  * the ECAT trap -- the thing that actually catches a student. Present on all 200.

The 2024_S1 review recorded "the catch is not in the report" on exactly those 83 questions. The
reviewer was looking at the E7 row, which legitimately was not there, while the real catch sat
lower on the same card headed "The trap". Renaming the ECAT header to "The catch" (done in
`join_ecat_into_export.py`) fixes the 83 -- but it also puts two catch-named things on the 117
cards where E7 DID fill its field, so this row has to give up the name.

The replacement is exact markup, not a word: `<th>the catch</th>` is only ever the E7 row. The
ECAT header is `<span class="ecat-ohead">The catch</span>` and is untouched by this.

Usage:
    python3 code/relabel_e7_catch_row.py --paper 2024_S1
    python3 code/relabel_e7_catch_row.py --paper 2024_S1 --apply
    python3 code/relabel_e7_catch_row.py --all --apply
"""

import argparse
import glob
import os
import sys

OLD = "<th>the catch</th>"
NEW = "<th>what makes it harder</th>"
OLD_MD = "**the catch**"
NEW_MD = "**what makes it harder**"


def targets(paper):
    pat = "data/*/%s/question_paper.*" % (paper or "*")
    return [p for p in sorted(glob.glob(pat)) if p.endswith((".html", ".md"))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    if not a.paper and not a.all:
        sys.exit("give --paper <code> or --all")

    total = 0
    for path in targets(None if a.all else a.paper):
        s = open(path, encoding="utf-8").read()
        old, new = (OLD_MD, NEW_MD) if path.endswith(".md") else (OLD, NEW)
        n = s.count(old)
        if not n:
            continue
        total += n
        print("  %-44s %4d row(s)" % (os.path.relpath(path, "data"), n))
        if a.apply:
            open(path, "w", encoding="utf-8").write(s.replace(old, new))
    print("%s %d row(s)%s" % ("relabelled" if a.apply else "would relabel",
                              total, "" if a.apply else "  (pass --apply)"))


if __name__ == "__main__":
    main()
