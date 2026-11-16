#!/usr/bin/env python3
"""Join the NCERT-first solution into `questions.json`, and retire what it replaces.

BIOLOGY ONLY. Every question this touches is selected by `classification.subject == "Biology"`.
Physics and Chemistry records are not read, not written and not counted -- their NCERT corpus
is not extracted yet, so the step that produces these solutions has never run for them.

WHAT IT ADDS
------------
`ncert_first`, assembled from the two agent steps the page already renders:

    D12  in_short, what_ncert_says (+ source), explanation, answer_is,
         why_other_options_fail, rests_on_ncert, terms_beyond_ncert, note
    D13  diagram: which picture was chosen and why

Until now those lived only under `ncert_to_paper_maps/steps/`, and the HTML read them straight
from there. That was fine for a five-question trial and wrong for everything after it: the
markdown is generated from `questions.json`, the DynamoDB rows are built from `questions.json`,
and neither could see a solution that was not in it.

WHAT IT RETIRES, AND WHY NOTHING IS DELETED
-------------------------------------------
The exam taxonomy and the superseded solution fields are MOVED to
`<paper>/archive/retired_fields.json`, keyed by question id, and removed from the record. They
are not deleted: the owner intends to map the exam taxonomy properly later, and a field that is
gone from a 1,722-question corpus cannot be recovered by rerunning anything.

    classification.chapter                  the coaching chapter (BIONEETENGBML "Biomolecules")
    classification.subtopics                \\ byte-identical duplicates of each other --
    classification.examtopicmapping_subtopics/  same id, same name, same why
    solution.full_text / .html / .steps     three more copies of the publisher's own working.
                                            `steps` is OUR numbering of prose the publisher
                                            never numbered, which is what the teacher review
                                            kept objecting to; `printed_lines` is what it
                                            actually printed, and that stays.
    categories.concept / .note              these carry the exact wording the review called
                                            out -- "phosphate-choline head", "phosphoglyceride"
                                            -- because they predate the NCERT-vocabulary rule
                                            and it never reached them.

KEPT: `solution.printed_lines`, `solution.screenshot`, `classification.ncert_subtopics`, the
whole of `ncert_mapping` (the page's quote windows are built from its `context` fields), the
whole of `categories` apart from the two fields above, `syllabus`, `difficulty`.

Usage:
    python3 code/join_ncert_first_into_export.py --paper 2024_S1
    python3 code/join_ncert_first_into_export.py --paper 2024_S1 --apply
"""

import argparse
import collections
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPS = os.path.join(os.path.dirname(HERE), "ncert_to_paper_maps")

#: (container, field) pairs lifted out of the record into the archive.
RETIRE = (("classification", "chapter"),
          ("classification", "subtopics"),
          ("classification", "examtopicmapping_subtopics"),
          ("solution", "full_text"),
          ("solution", "html"),
          ("solution", "steps"),
          ("categories", "concept"),
          ("categories", "note"))


def step_out(paper, step, qid):
    p = os.path.join(MAPS, "steps", step, "out", "%s.%s.runA.json" % (paper, qid))
    if not os.path.exists(p):
        return None
    try:
        d = json.load(open(p, encoding="utf-8"))
    except ValueError:
        return None
    return None if d.get("error") else d


def diagram_of(d13):
    """What D13 decided, in the few fields a reader or a renderer needs."""
    if not d13:
        return {"decision": "none", "why": "step D13 has not run for this question"}
    dec = d13.get("decision") or "none"
    out = {"decision": dec, "why": d13.get("why") or "", "caption": d13.get("caption") or ""}
    if dec == "annotate":
        a = d13.get("annotate") or {}
        out["image"] = a.get("image")
        out["marks"] = a.get("marks") or []
    elif dec == "ncert_figure":
        out["ncert_figure"] = d13.get("ncert_figure") or {}
    elif dec == "draw":
        out["drawn_spec"] = d13.get("draw") or {}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    year = a.paper.split("_")[0]
    base = os.path.join(HERE, "data", year, a.paper)
    doc = json.load(open(os.path.join(base, "questions.json"), encoding="utf-8"))

    report, archive = collections.Counter(), {}
    for q in doc["questions"]:
        if ((q.get("classification") or {}).get("subject") or "") != "Biology":
            report["not biology -- untouched"] += 1
            continue
        qid = q["question_id"].split("__")[-1]
        report["biology"] += 1

        d12, d13 = step_out(a.paper, "D12", qid), step_out(a.paper, "D13", qid)
        if not d12:
            report["no D12 solution yet -- left as it was"] += 1
            continue

        q["ncert_first"] = {
            "in_short": d12.get("in_short") or "",
            "what_ncert_says": d12.get("what_ncert_says") or "",
            "what_ncert_says_source": d12.get("what_ncert_says_source") or "",
            "explanation": d12.get("explanation") or "",
            "answer_is": d12.get("answer_is") or "",
            "why_other_options_fail": d12.get("why_other_options_fail") or [],
            "rests_on_ncert": d12.get("rests_on_ncert") or "",
            "terms_beyond_ncert": d12.get("terms_beyond_ncert") or [],
            "diagram": diagram_of(d13),
            "note": d12.get("note") or "",
        }
        report["ncert_first added"] += 1
        if not d12.get("in_short"):
            report["WARNING: D12 output predates in_short"] += 1
        if not d13:
            report["no D13 diagram decision yet"] += 1

        # THE PRINTED KEY IS NEVER OVERWRITTEN. Where NCERT contradicts it the record says so
        # and keeps both, because changing a booklet's answer in the data is a claim no
        # pipeline should make silently.
        printed = str((q.get("answer") or {}).get("publisher") or "")
        if printed and d12.get("answer_is") and printed != str(d12["answer_is"]):
            q["ncert_first"]["disagrees_with_printed_key"] = True
            report["marked for review: NCERT disagrees with the printed key"] += 1

        kept = {}
        for container, field in RETIRE:
            box = q.get(container)
            if isinstance(box, dict) and field in box:
                kept.setdefault(container, {})[field] = box.pop(field)
        if kept:
            archive[q["question_id"]] = kept
            report["records with fields retired"] += 1

    for k, v in sorted(report.items()):
        print("   %-48s %d" % (k, v))
    if not a.apply:
        print("(nothing written -- pass --apply)")
        return

    if archive:
        adir = os.path.join(base, "archive")
        os.makedirs(adir, exist_ok=True)
        path = os.path.join(adir, "retired_fields.json")
        if os.path.exists(path):                       # never lose an earlier run's archive
            old = json.load(open(path, encoding="utf-8"))
            old.update(archive)
            archive = old
        json.dump(archive, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("archived %d record(s) to archive/retired_fields.json" % len(archive))
    json.dump(doc, open(os.path.join(base, "questions.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("wrote questions.json")


if __name__ == "__main__":
    main()
