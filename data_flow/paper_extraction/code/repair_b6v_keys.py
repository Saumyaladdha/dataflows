#!/usr/bin/env python3
"""Rename `why` to `reason` in B6V outputs written against the wrong key name.

    python3 scripts/repair_b6v_keys.py --dry-run
    python3 scripts/repair_b6v_keys.py --apply

WHOSE MISTAKE THIS REPAIRS
--------------------------
`schemas/B6.json` requires `answer`, `reason`, `working`, `confidence`, `note`. The dispatch prompt
asked the solver for `why` instead, so 82 otherwise-correct answers failed their own schema on a key
name. The content is sound -- the fault was in the instruction, not the answer -- so the right repair
is a rename, not a re-solve.

`working` is set from `reason` only when the reason actually contains arithmetic, because the schema
says `working` is "shown for a numerical; empty string when not applicable" and copying prose into it
would make every answer look like a calculation. The split is recorded in `note` so the rename is
auditable rather than invisible.
"""

import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

OUT = ("steps", "B6V", "out")
#: A reason that shows a calculation: an equals sign or an arithmetic operator between digits.
ARITHMETIC = re.compile(r"\d\s*[=+\-*/×÷^]\s*\d|=\s*\d|\d\s*/\s*\d")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    renamed = numeric = already = broken = 0
    for path in sorted(glob.glob(rc.pp(*OUT, "*.json"))):
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except ValueError:
            broken += 1
            continue
        if "error" in data:
            continue
        if "reason" in data and "why" not in data:
            already += 1
            continue
        if "why" not in data:
            continue
        reason = data.pop("why")
        data["reason"] = reason
        if "working" not in data:
            shows_working = bool(ARITHMETIC.search(reason))
            data["working"] = reason if shows_working else ""
            if shows_working:
                numeric += 1
        data.setdefault("note", "")
        marker = ("key renamed from `why` to `reason` to match schemas/B6.json; the dispatch "
                  "prompt asked for the wrong name")
        if marker not in (data["note"] or ""):
            data["note"] = (data["note"] + "; " if data["note"] else "") + marker
        renamed += 1
        if args.apply:
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(data, fh, ensure_ascii=False, indent=1)

    print("%d renamed (%d of them carried arithmetic and kept it in `working`)" % (renamed, numeric))
    print("%d already correct, %d unreadable" % (already, broken))
    if args.dry_run:
        print("(dry run -- nothing written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
