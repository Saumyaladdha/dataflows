#!/usr/bin/env python3
"""Build D12 packets -- everything the NCERT solution writer needs, in NCERT's order.

THE ORDER IS THE POINT
----------------------
Until now the pipeline classified a question against an exam taxonomy, solved it, and mapped it
to NCERT last. The owner reversed that, and the reason is in the 2024_S1 review: solution after
solution was factually right and worded in vocabulary NCERT does not use -- "phosphoglyceride",
"phosphate-choline head", "circular, double-stranded". A teacher cannot tell such a line is
examinable, and a student revising from the book cannot place it.

So NCERT now comes FIRST and its text becomes the solution's dictionary:

    D1  which NCERT chapter        ->  D2  which printed subtopic
    D4  the exact lines + passages ->  D12 the student-facing explanation, in those words
    D5  the older edition          ->  reported BELOW the solution, never mixed into it

`ncert_passages` is carried as well as `ncert_lines` deliberately. The quoted line proves the
answer; the surrounding passage is what tells the writer which words the book uses on the way to
it -- which is the thing that was going wrong.

THE PUBLISHER TRAVELS AS A REVIEWER
-----------------------------------
`publisher_solution` is included, and the brief tells the agent to read it only AFTER writing
its own. The owner's instruction was explicit: refer to it while reviewing, but the final
explanation must be independently written. Carried as `printed_lines` (the publisher's own
printed wording) rather than `steps`, because `steps` is our numbered reshaping of prose the
publisher never numbered -- 198 of 200 questions on this paper.

Usage:
    python3 code/build_d12_packets.py --paper 2024_S1 --questions q101,q106,q107,q153,q157
    python3 code/build_d12_packets.py --paper 2024_S1 --questions q101,... --apply
"""

import argparse
import collections
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(HERE))
PAPERS = os.path.join(REPO, "data_flow", "paper_extraction", "data")
MAX_PASSAGES = 6


def step_out(paper, step, qid):
    p = os.path.join(HERE, "steps", step, "out", "%s.%s.runA.json" % (paper, qid))
    if not os.path.exists(p):
        return None
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception:
        return None
    return None if d.get("error") else d


def heading(index, sid):
    ch, _, tail = str(sid or "").partition("#")
    for sec in ((index.get(ch) or {}).get("sections") or []):
        if sec.get("n") == tail:
            return "%s %s" % (tail, sec.get("heading"))
    return tail or sid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--questions", required=True, help="comma-separated, e.g. q101,q106")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    year = a.paper.split("_")[0]
    doc = json.load(open(os.path.join(PAPERS, year, a.paper, "questions.json"), encoding="utf-8"))
    Q = {q["question_id"].split("__")[-1]: q for q in doc["questions"]}
    index = json.load(open(os.path.join(HERE, "maps", "ncert_heading_index.json"), encoding="utf-8"))
    paragraphs = json.load(open(os.path.join(HERE, "maps", "paragraphs.json"), encoding="utf-8"))

    report = collections.Counter()
    built = []
    for qid in [x.strip() for x in a.questions.split(",") if x.strip()]:
        q = Q.get(qid)
        if not q:
            report["no such question"] += 1
            continue
        d1, d2 = step_out(a.paper, "D1", qid), step_out(a.paper, "D2", qid)
        d4, d5 = step_out(a.paper, "D4", qid), step_out(a.paper, "D5", qid)
        if not d1:
            report["no NCERT chapter yet (run D1 first)"] += 1
            continue

        lines = [{"exact_line": e.get("exact_line"), "passage_id": e.get("passage_id"),
                  "for": e.get("for")}
                 for e in ((d4 or {}).get("evidence") or []) if e.get("exact_line")]
        # the passages those lines came from -- the writer's dictionary, deduped and capped
        seen, passages = set(), []
        for e in lines:
            pid = e["passage_id"]
            if pid in seen or pid not in paragraphs:
                continue
            seen.add(pid)
            passages.append({"passage_id": pid, "text": paragraphs[pid]})
            if len(passages) >= MAX_PASSAGES:
                break
        if not lines:
            report["NCERT carries nothing for this question"] += 1

        qq = q.get("question") or {}
        ans = q.get("answer") or {}
        sol = q.get("solution") or {}
        built.append({
            "question_id": q["question_id"],
            "question": {
                "stem": qq.get("stem"), "statements": qq.get("statements") or [],
                "list_i": qq.get("list_i") or [], "list_ii": qq.get("list_ii") or [],
                "options": [{"key": o.get("key"),
                             "text": (o.get("text") or "").strip()
                                     or ("[drawn option] %s" % ((o.get("figure") or {}).get("text") or "")).strip()}
                            for o in (qq.get("options") or [])],
            },
            "answer": {"printed_option": ans.get("publisher"), "printed_text": ans.get("publisher_text"),
                       "independently_solved": ans.get("ai"), "agreement": ans.get("verdict")},
            "ncert_chapter": (d1.get("chapter_ids") or []),
            "ncert_subtopics": [heading(index, s) for s in ((d2 or {}).get("subtopic_ids") or [])
                                if s and s != "unsure"],
            "ncert_lines": lines,
            "ncert_passages": passages,
            "older_ncert_lines": [{"exact_line": e.get("exact_line"), "passage_id": e.get("passage_id")}
                                  for e in ((d5 or {}).get("older") or []) if e.get("exact_line")],
            # THE WRITER MUST SEE WHAT THE STUDENT SEES. q157 prints three muscle-tissue
            # diagrams labelled a, b and c, and every option refers to them -- but the packet
            # carried only text, so the solution was written blind and the agent reported the
            # stem as having no figures. Local paths, because the agent reads files.
            "figures": [f["printed"]["png"]["path"]
                        for f in ((qq.get("figures") or [])
                                  + [o.get("figure") or {} for o in (qq.get("options") or [])]
                                  + (sol.get("figures") or []))
                        if ((f.get("printed") or {}).get("png") or {}).get("path")],
            "publisher_solution": sol.get("printed_lines") or [],
            "note_from_runner": ("`ncert_lines` and `ncert_passages` are your vocabulary. "
                                 "`publisher_solution` is the publisher's own printed wording -- "
                                 "read it only after writing your own. `older_ncert_lines` is "
                                 "reported separately and must not appear in the explanation. "
                                 "Write `in_short` as well: one or two plain sentences, "
                                 "30 words at most, answering the question outright. It is "
                                 "printed directly UNDER the quoted NCERT line, saying what THAT line means and "
                                 "settling the question. The card shows the "
                                 "fuller `explanation` only on request."),
        })
        report["ready"] += 1

    print("%s: %d D12 packet(s)" % (a.paper, len(built)))
    for k, v in sorted(report.items()):
        if k != "ready":
            print("   %-42s %d" % (k, v))
    for b in built:
        print("   %-18s chapter=%-14s subtopics=%-40s lines=%d passages=%d older=%d"
              % (b["question_id"].split("__")[-1], ";".join(b["ncert_chapter"]),
                 ("; ".join(b["ncert_subtopics"]) or "-")[:40],
                 len(b["ncert_lines"]), len(b["ncert_passages"]), len(b["older_ncert_lines"])))
    if not a.apply:
        print("(nothing written -- pass --apply)")
        return
    work = os.path.join(HERE, "steps", "D12", "work")
    os.makedirs(work, exist_ok=True)
    for b in built:
        qid = b["question_id"].split("__")[-1]
        json.dump(b, open(os.path.join(work, "%s.%s.runA.input.json" % (a.paper, qid)),
                          "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote %d packet(s) to steps/D12/work" % len(built))


if __name__ == "__main__":
    main()
