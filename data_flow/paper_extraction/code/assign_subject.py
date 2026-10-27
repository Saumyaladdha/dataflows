#!/usr/bin/env python3
"""Assign subject (and Biology branch) to every v2 question, from the paper's own printed headings.

    python3 scripts/assign_subject.py --paper-id 2015_A --dry-run
    python3 scripts/assign_subject.py --apply            # every booklet

WHY THE PRINTED HEADING, NOT THE QUESTION NUMBER
-------------------------------------------------
NEET looks positional -- Physics first, then Chemistry, then Biology -- and assigning by question
number is the obvious shortcut. It is also wrong, and wrong CONFIDENTLY, which is worse.

Measured on this corpus:

    2024 Code-Q2   PHYSICS -> q1   CHEMISTRY -> q51   BOTANY -> q101   ZOOLOGY -> q151
    2015 Code-A    BIOLOGY -> q46  PHYSICS  -> q136
    2017 Code-C    no headings printed at all

2015 Code-A does not start with Physics. Its headings put Chemistry at 1-45, Biology at 46-135 and
Physics at 136-180. A positional rule would have labelled all 177 of its questions, every one of
them with full confidence, and most of them wrong. That is exactly the failure SPEC Rule 20 was
written for: a derivation validated against rows that already carried the answer.

So: the heading is read off the page where it exists, position is a FALLBACK that is recorded as
one, and `subject_from` always says which happened. A reviewer can then check the fallbacks and
ignore the rest.

THE BOTANY/ZOOLOGY SPLIT COMES FROM HERE AND NOWHERE ELSE. The product's own
`ExamChapterTopicMappings` table has subject physics/chemistry/biology with no branch, while NEET
prints Botany and Zoology as separate sections. The paper is the only source that knows which.
"""

import argparse
import collections
import glob
import json
import os
import re
import sys
import warnings

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

CORPUS = rc.corpus()

#: A section heading is a short line that is ONLY the subject's name. The length cap is what keeps
#: "PHYSICS" apart from a stem that happens to contain the word physics.
HEADING = re.compile(r"^(PHYSICS|CHEMISTRY|BIOLOGY|BOTANY|ZOOLOGY)$", re.I)
HEADING_MAX_CHARS = 14

#: heading -> (subject, branch). Botany and Zoology are Biology with a branch, which is how
#: config/allowed_values.yaml models them.
SUBJECT_OF = {
    "PHYSICS": ("Physics", None),
    "CHEMISTRY": ("Chemistry", None),
    "BIOLOGY": ("Biology", None),
    "BOTANY": ("Biology", "botany"),
    "ZOOLOGY": ("Biology", "zoology"),
}

#: The positional layout NEET normally uses, by how many questions the paper holds. Used ONLY where
#: no heading is printed, and always recorded as a fallback.
POSITIONAL = {
    200: [(1, 50, "Physics", None), (51, 100, "Chemistry", None),
          (101, 150, "Biology", "botany"), (151, 200, "Biology", "zoology")],
    180: [(1, 45, "Physics", None), (46, 90, "Chemistry", None),
          (91, 180, "Biology", None)],
}


def headings(doc, pages):
    """[(page, y, heading)] for every printed section heading, in reading order."""
    found = []
    for index, page in enumerate(pages):
        for line in page["lines"]:
            text = line["text"].strip().replace(":", "").strip()
            if len(text) <= HEADING_MAX_CHARS and HEADING.match(text):
                found.append((index, line["y0"], text.upper()))
    found.sort()
    return found


def positional_rule(count):
    """The nearest standard layout for a paper of this size, or None."""
    if count in POSITIONAL:
        return POSITIONAL[count]
    # a paper a few questions short of a standard size still follows that layout
    for size in sorted(POSITIONAL, reverse=True):
        if abs(count - size) <= 10:
            return POSITIONAL[size]
    return None


def assign(paper_id, write=False):
    import pymupdf
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import extract_paper_v2 as extractor

    path = rc.pp(*CORPUS, "papers", "%s.json" % paper_id)
    with open(path, encoding="utf-8") as fh:
        paper = json.load(fh)
    source = os.path.join(os.path.dirname(extractor.SOURCE_ROOT), paper["meta"]["source_pdf"])
    if not os.path.exists(source):
        print("%s: source PDF missing (%s)" % (paper_id, source))
        return None

    doc = pymupdf.open(source)
    pages, _spans = extractor.analyse(doc)
    marks = headings(doc, pages)
    doc.close()

    questions = paper["questions"]
    order = {(q["page"] - 1, q["parts"][0]["bbox"][1] * 72.0 / extractor.DPI if q["parts"] else 0.0)
             : q for q in questions}

    counts = collections.Counter()
    # A heading governs every question from where it sits until the next heading.
    bounds = []
    for n, (page_index, y, text) in enumerate(marks):
        subject, branch = SUBJECT_OF[text]
        start = (page_index, y)
        end = (marks[n + 1][0], marks[n + 1][1]) if n + 1 < len(marks) else (10 ** 6, 0.0)
        bounds.append((start, end, subject, branch, text))

    fallback = positional_rule(len(questions))
    for question in questions:
        part = (question["parts"] or [None])[0]
        here = (question["page"] - 1,
                (part["bbox"][1] * 72.0 / extractor.DPI) if part else 0.0)
        hit = next((b for b in bounds if b[0] <= here < b[1]), None)
        if hit:
            question["subject"] = hit[2]
            question["branch"] = hit[3]
            question["subject_from"] = "printed heading %r" % hit[4]
            counts["from_heading"] += 1
        elif fallback:
            band = next((b for b in fallback if b[0] <= question["qno"] <= b[1]), None)
            if band:
                question["subject"] = band[2]
                question["branch"] = band[3]
                question["subject_from"] = ("position (no heading governs this question; the "
                                            "%d-question layout was assumed)" % len(questions))
                counts["from_position"] += 1
            else:
                question["subject"] = None
                question["branch"] = None
                question["subject_from"] = "unassigned"
                counts["unassigned"] += 1
        else:
            question["subject"] = None
            question["branch"] = None
            question["subject_from"] = "unassigned (no heading and no standard layout for %d "
            counts["unassigned"] += 1

    # Boundary questions are the ones worth a person's eye: the first and last of each run.
    runs, previous = [], None
    for question in sorted(questions, key=lambda q: q["qno"]):
        tag = (question.get("subject"), question.get("branch"))
        if tag != previous:
            runs.append([question["qno"], question["qno"], tag])
            previous = tag
        else:
            runs[-1][1] = question["qno"]

    print("%-9s %3d questions  %s" % (paper_id, len(questions),
                                      "  ".join("%s=%d" % (k, v) for k, v in counts.most_common())))
    for first, last, (subject, branch) in runs:
        print("        q%-3d-%-3d  %s%s" % (first, last, subject or "UNASSIGNED",
                                            "/" + branch if branch else ""))
    if marks:
        print("        headings printed: %s" % ", ".join(t for _p, _y, t in marks))
    else:
        print("        NO headings printed -- every row above is a positional fallback")

    if write:
        paper["meta"]["subject_assignment"] = {
            "headings_found": [t for _p, _y, t in marks],
            "from_heading": counts["from_heading"],
            "from_position": counts["from_position"],
            "unassigned": counts["unassigned"],
        }
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(paper, fh, ensure_ascii=False, indent=1)
    return counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper-id")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    ids = ([args.paper_id] if args.paper_id else
           [os.path.basename(p)[:-5]
            for p in sorted(glob.glob(rc.pp(*CORPUS, "papers", "*.json")))])
    total = collections.Counter()
    for paper_id in ids:
        counts = assign(paper_id, write=args.apply)
        if counts:
            total.update(counts)
    print("\n%d from a printed heading, %d from position, %d unassigned"
          % (total["from_heading"], total["from_position"], total["unassigned"]))
    print("   `subject_from` on every question says which, so the fallbacks can be reviewed and "
          "the rest trusted.")
    if args.dry_run:
        print("(dry run -- nothing written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
