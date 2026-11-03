#!/usr/bin/env python3
"""Move any figure crop that contains the printed ANSWER out of the corpus.

    python3 code/quarantine_leaky_figures.py --paper-id 2026_11 --apply

WHY
---
B6V is the blind solve: it answers the question without the key so that a later step can
compare the two independently. On a question whose OPTIONS are drawings, the solver has to open
a figure file to read them -- and on 2026_11 two of those files carry the booklet's own
`Answer (4)` / `Answer (3 or 4)` line inside the crop. The step is then not blind, and its
agreement with the key stops being evidence of anything.

This finds crops whose pixels include an answer line and moves them to `figures_quarantine/`.
It does not delete them: a figure is also a record of what was cut, and a wrong cut is worth
keeping where it can be looked at but not read by a step.

NOTHING IS LOST BY MOVING THEM. `cut_agent_figures.py` already cuts a clean, per-option crop
from the box the question-reader reported, clipped above the solution by `solution_after()`.
Those are the figures the pipeline is meant to use -- its own docstring says of the geometric
pass: "WHAT IT KEEPS FROM THE GEOMETRIC PASS: nothing."
"""

import argparse
import glob
import json
import os
import re
import shutil

import pymupdf

import runner_core as rc

ANSWER = re.compile(r"\bAnswer\s*\(", re.I)


def leaky(paper_id):
    """[(path, the answer text found)] for every figure crop whose area holds an answer line."""
    rec = json.load(open(rc.pp("papers", "papers", "%s.json" % paper_id), encoding="utf-8"))
    pdf = rc.pp("source_pdfs", "papers", os.path.basename(rec["meta"]["source_pdf"]))
    doc = pymupdf.open(pdf)
    dpi = rec["meta"]["dpi"]
    k = 72.0 / dpi
    out = []
    for q in rec["questions"]:
        for fig in q.get("figures") or []:
            box, page = fig.get("crop_bbox"), fig.get("page")
            img = fig.get("image")
            if not (box and page and img):
                continue
            path = rc.pp("papers", img)
            if not os.path.exists(path):
                continue
            rect = pymupdf.Rect(box[0] * k, box[1] * k, box[2] * k, box[3] * k)
            text = doc[page - 1].get_textbox(rect) or ""
            m = ANSWER.search(text)
            if m:
                line = " ".join(text[m.start():m.start() + 40].split())
                out.append((path, line, q["qno"]))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper-id", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    found = leaky(a.paper_id)
    if not found:
        print("%s: no figure crop contains an answer line" % a.paper_id)
        return 0
    dest = rc.pp("papers", "figures_quarantine", a.paper_id)
    for path, line, qno in found:
        print("  q%03d  %-46s holds %r" % (qno, os.path.basename(path), line))
        if a.apply:
            os.makedirs(dest, exist_ok=True)
            shutil.move(path, os.path.join(dest, os.path.basename(path)))
    print("%d crop(s) %s" % (len(found), "quarantined" if a.apply else "would be quarantined"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
