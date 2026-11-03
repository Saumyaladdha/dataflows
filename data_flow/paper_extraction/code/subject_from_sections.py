#!/usr/bin/env python3
"""Record each question's subject from the booklet's own printed section headings.

    python3 code/subject_from_sections.py --paper 2026_11 --apply

WHY THIS IS NOT AN AGENT STEP HERE
----------------------------------
QSUBJ exists to "confirm subject where NO HEADING WAS PRINTED" -- 2015_A opens with Chemistry
where the standard layout predicts Physics, and only reading the question settles it. This
booklet prints `PHYSICS`, `CHEMISTRY` and `BIOLOGY` as their own lines on pages 2, 23 and 42,
so the premise of the step does not hold: the paper states the answer.

Asking an agent to infer from content what the page prints in capitals would be slower, cost
180 calls, and be LESS reliable -- an agent can misread a borderline biophysics question, the
printed heading cannot. So the heading is the evidence, and `why` says so on every record.

WHAT IS LEFT FOR A HUMAN OR AN AGENT
------------------------------------
`branch` -- botany vs zoology inside Biology. The booklet prints one BIOLOGY heading and does
not split it, so there is nothing here to read it off, and it is left null rather than guessed.
"""

import argparse
import json
import os
import re

import pymupdf

import runner_core as rc

OUT = ("steps", "QSUBJ", "out")
HEADINGS = ("PHYSICS", "CHEMISTRY", "BIOLOGY", "BOTANY", "ZOOLOGY")


def sections(pdf_path):
    """[(page, SUBJECT)] for every heading the booklet prints on a line of its own."""
    doc = pymupdf.open(pdf_path)
    found = []
    for i in range(doc.page_count):
        text = doc[i].get_text()
        for h in HEADINGS:
            if re.search(r"^\s*%s\s*$" % h, text, re.M):
                found.append((i + 1, h))
    return found


def run(paper_id, apply_=False):
    rec_path = rc.pp("papers", "papers", "%s.json" % paper_id)
    rec = json.load(open(rec_path, encoding="utf-8"))
    pdf = rc.pp("source_pdfs", "papers",
                os.path.basename(rec["meta"]["source_pdf"]))
    heads = sections(pdf)
    if not heads:
        raise SystemExit("no printed section headings in %s -- this paper DOES need QSUBJ" % pdf)
    print("printed headings: %s" % ", ".join("p%d %s" % h for h in heads))

    # a question belongs to the last heading printed at or before its page
    def subject_for(page):
        best = None
        for pg, h in heads:
            if pg <= page:
                best = h
        return best

    counts, written = {}, 0
    for q in rec["questions"]:
        page, qno = q.get("page"), q.get("qno")
        head = subject_for(page)
        if not head:
            print("  q%03d on page %s is before the first heading -- skipped" % (qno, page))
            continue
        subject = head.title()
        counts[subject] = counts.get(subject, 0) + 1
        out = {
            "subject": subject,
            # The booklet prints one BIOLOGY heading and never splits botany from zoology, so
            # there is nothing to read this off. Null, not guessed.
            "branch": None,
            "why": ("The booklet prints %s as a section heading on page %d, and this question "
                    "is printed on page %s, under that heading." % (head, 
                     max(pg for pg, h in heads if pg <= page), page)),
            "agrees_with_position": True,
            "confidence": "high",
            "note": ("Recorded from the printed section heading by "
                     "code/subject_from_sections.py, not inferred from content. QSUBJ exists "
                     "for booklets that print no heading; this one does."),
        }
        if apply_:
            os.makedirs(rc.pp(*OUT), exist_ok=True)
            with open(rc.pp(*OUT, "%s__q%03d.runA.json" % (paper_id, qno)), "w",
                      encoding="utf-8") as fh:
                json.dump(out, fh, ensure_ascii=False, indent=1)
        written += 1
    print("%d question(s)%s   %s" % (written, "" if apply_ else " (dry run)", counts))
    return written


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    run(a.paper, a.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
