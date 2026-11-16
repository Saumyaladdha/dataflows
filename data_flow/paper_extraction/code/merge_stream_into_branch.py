#!/usr/bin/env python3
"""Merge the `stream` and `branch` columns into ONE `branch` field, in a finished export.

WHY THEY WERE ALWAYS ONE FIELD
------------------------------
Measured across all 200 questions of 2024_S1, the two are never both filled:

    Biology      branch = botany (50) / zoology (50)      stream empty
    Chemistry    stream = physical (19) / organic (15) /  branch empty
                          inorganic (16)
    Physics      neither

So one mutually exclusive fact was being carried under two names, and the page then printed
300 "not applicable" rows on a 200-question paper to explain the halves that did not apply.
That is exactly the reviewer's point -- "Branch aur Stream ko alag fields tabhi rakhein jab
dono ka clear aur different purpose ho. Duplicate ya confusing classification remove karein."

WHAT THE MERGED FIELD HOLDS
---------------------------
    Biology      Botany | Zoology
    Chemistry    Physical | Organic | Inorganic
    Physics      nothing -- the row is not emitted at all

Physics gets no row rather than an empty one. It has no standard division, so the honest page
says nothing instead of saying "not applicable" fifty times. The chemistry division is kept
(not dropped as the reviewer suggested for non-Biology) because it is load-bearing elsewhere:
`b7-chem-branch-sorter` produces it, Stage D routes organic/inorganic to an NCERT quote and
physical chemistry to QCA on the strength of it, and Stage E conditions its chemistry prior on
it. Dropping the column would throw away a real signal to tidy a display.

The data keeps both original keys as well, so the 19 readers that index `stream` or `branch`
by name keep working; the merged value is added as `classification.branch_merged`.

Usage:
    python3 code/merge_stream_into_branch.py --paper 2024_S1
    python3 code/merge_stream_into_branch.py --paper 2024_S1 --apply
"""

import argparse
import collections
import html
import json
import os
import re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#: Matches one classify-table row for either column, whatever its `class` attribute says.
ROW = re.compile(r'<tr[^>]*><th>(stream|branch)</th><td[^>]*>.*?</td></tr>', re.S)


def division(subject, stream, branch):
    """The one value this question's subject actually divides on."""
    v = (branch or stream or "").strip()
    if (subject or "").lower() not in ("biology", "chemistry"):
        return None                      # physics: no standard division, so no row
    return v.title() if v else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    year = a.paper.split("_")[0]
    base = os.path.join(HERE, "data", year, a.paper)
    doc = json.load(open(os.path.join(base, "questions.json"), encoding="utf-8"))
    src = open(os.path.join(base, "question_paper.html"), encoding="utf-8").read()

    want = {}
    report = collections.Counter()
    for q in doc["questions"]:
        cls = q.get("classification") or {}
        d = division(cls.get("subject"), cls.get("stream"), cls.get("branch"))
        want[q["question_id"].split("__")[-1]] = d
        cls["branch_merged"] = d
        report["%s -> %s" % (cls.get("subject"), d or "(no row)")] += 1

    # rebuild the document in one pass, per question card
    starts = [(m.group(1), m.start()) for m in re.finditer(r'<div class="q" id="(q\d+)"', src)]
    out, last, replaced, dropped = [], 0, 0, 0
    for i, (qid, at) in enumerate(starts):
        end = starts[i + 1][1] if i + 1 < len(starts) else len(src)
        out.append(src[last:at])
        card = src[at:end]
        # REMOVE FIRST, THEN INSERT -- and never the other way round. The first version put the
        # merged row in place of the old one and then swept up the remaining matches, but the
        # row it had just inserted IS a `<th>branch</th>` row, so the sweep deleted it too and
        # the column vanished from all 200 cards. Removing everything first and anchoring the
        # new row on `subject` also makes this safe to run twice.
        n_before = len(ROW.findall(card))
        if n_before:
            for m in reversed(list(ROW.finditer(card))):
                card = card[:m.start()] + card[m.end():]
            dropped += n_before
        d = want.get(qid)
        if d:
            anchor = re.search(r'<tr[^>]*><th>subject</th><td[^>]*>.*?</td></tr>', card, re.S)
            if anchor:
                card = (card[:anchor.end()]
                        + '<tr class=""><th>branch</th><td>%s</td></tr>' % html.escape(d)
                        + card[anchor.end():])
                replaced += 1
            else:
                report["no subject row to anchor the branch on"] += 1
        out.append(card)
        last = end
    out.append(src[last:])
    merged = "".join(out)

    print("%s: %d question cards" % (a.paper, len(starts)))
    for k, v in sorted(report.items()):
        print("   %-34s %3d" % (k, v))
    print("   cards rewritten: %d, duplicate rows removed: %d" % (replaced, dropped))
    print("   html %.1f MB -> %.1f MB" % (len(src) / 1e6, len(merged) / 1e6))
    if not a.apply:
        print("(nothing written -- pass --apply)")
        return
    json.dump(doc, open(os.path.join(base, "questions.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    open(os.path.join(base, "question_paper.html"), "w", encoding="utf-8").write(merged)
    print("wrote questions.json and question_paper.html")


if __name__ == "__main__":
    main()
