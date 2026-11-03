#!/usr/bin/env python3
"""What one paper's ratings say -- coverage, value spread, proposals, flags.

    python3 code/ecat_paper_report.py --paper 2017_A

WHY A REPORT AND NOT A GLANCE AT THE PAGE
-----------------------------------------
The point of rating a whole paper is to see which traps RECUR, and that is invisible one card
at a time. It also answers the question the vocabulary cut raised: a value kept because it felt
useful, but used once in 180 questions, is not a family -- it is a card with a long name. Only
a whole-paper count can tell those apart.

WHAT IT REFUSES TO COUNT
------------------------
Flagged questions. A misprinted stem, a disputed key and a deleted topic each produce a
perfectly valid-looking rating, and counting them means the pattern describes the fault rather
than the students. They are listed, with their flag, and left out of every distribution.
"""

import argparse
import collections
import glob
import json
import os

import yaml


def load(paper_id):
    rows = {}
    for p in sorted(glob.glob(os.path.join("steps", "ECAT", "out", "ex__%s__*.json" % paper_id))):
        try:
            doc = json.load(open(p, encoding="utf-8"))
        except ValueError:
            print("  UNREADABLE: %s" % p)
            continue
        for r in doc.get("ratings") or []:
            rows[r["question_id"]] = r
    return rows


def bar(n, total, width=28):
    return "#" * max(0, round(width * n / total)) if total else ""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", required=True)
    a = ap.parse_args()

    av = yaml.safe_load(open("config/allowed_values.yaml", encoding="utf-8"))
    names = {}
    for axis in (av.get("display") or {}).values():
        names.update(axis)

    export = json.load(open(os.path.join("data", a.paper.split("_")[0], a.paper,
                                         "questions.json"), encoding="utf-8"))
    total = len(export["questions"])
    subj = {r["question_id"]: ((r.get("classification") or {}).get("subject") or "?").lower()
            for r in export["questions"]}

    rows = load(a.paper)
    flagged = {q: r for q, r in rows.items() if r.get("flags")}
    counted = {q: r for q, r in rows.items() if not r.get("flags")}

    print("=" * 74)
    print("%s -- %d of %d questions rated" % (a.paper, len(rows), total))
    print("   counted: %d     flagged and left out: %d" % (len(counted), len(flagged)))
    by_sub = collections.Counter(subj.get(q, "?") for q in rows)
    print("   by subject: %s" % dict(by_sub.most_common()))
    print("=" * 74)

    for axis, getter in (("qtype", lambda r: r.get("qtype")),
                         ("asks", lambda r: r.get("asks")),
                         ("trap", lambda r: (r.get("trap") or {}).get("label"))):
        c = collections.Counter(getter(r) for r in counted.values())
        print("\n%s -- %d values in use of %d defined" %
              (axis.upper(), len(c), len(av[axis if axis != "trap" else "trap_v2"])))
        for v, n in c.most_common():
            print("   %-26s %3d  %-28s %s" % (names.get(v, v), n, bar(n, len(counted)), v))
        unused = [v for v in av[axis if axis != "trap" else "trap_v2"] if v not in c]
        if unused:
            print("   never used: %s" % ", ".join(unused))
        once = [v for v, n in c.items() if n == 1]
        if once:
            print("   used ONCE (cannot form a family): %s" % ", ".join(once))

    # the point of the run
    print("\n" + "=" * 74)
    print("NEW VALUES THE PAPER ASKED FOR")
    print("=" * 74)
    props = []
    for q, r in sorted(rows.items()):
        for where, obj in [("trap", r.get("trap") or {})] + \
                          [("also", x) for x in (r.get("also") or [])]:
            p = obj.get("proposed") or {}
            if p.get("name"):
                props.append((q, where, obj.get("label"), p["name"], p.get("why", "")))
        for field in ("asks", "qtype"):
            if str(r.get(field, "")).startswith("new_"):
                p = r.get("%s_proposed" % field) or r.get("proposed") or {}
                props.append((q, field, r[field], p.get("name", "(unnamed)"), p.get("why", "")))
    if not props:
        print("  none -- every question fitted the current lists")
    for q, where, label, name, why in props:
        print("\n  %s  %s -> %s" % (q, where, name))
        print("      %s" % " ".join(why.split())[:300])

    print("\n" + "=" * 74)
    print("LEFT OUT OF THE COUNTS (%d)" % len(flagged))
    print("=" * 74)
    for q, r in sorted(flagged.items()):
        print("  %-18s %-18s %s" % (q, ",".join(r["flags"]),
                                    " ".join((r.get("flag_why") or "").split())[:90]))

    nc = [r for r in rows.values() if (r.get("ncert") or {}).get("found") is False]
    print("\nNCERT-checked and NOT in the current edition: %d" % len(nc))
    no_trap = sum(1 for r in counted.values() if (r.get("trap") or {}).get("label") == "no_trap")
    print("no_trap: %d of %d counted questions (%.0f%%)"
          % (no_trap, len(counted), 100.0 * no_trap / max(1, len(counted))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
