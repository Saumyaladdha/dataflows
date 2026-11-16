#!/usr/bin/env python3
"""Build D2 (NCERT subtopic) packets from D1's chapter picks.

THE SUBTOPIC MENU IS THE PRINTED HEADINGS
-----------------------------------------
D2's brief asks for `subtopics`: "id, name, one-line description (this chapter only)". Two
candidate menus exist and they are not equivalent:

  * A4's drafted lists (`subtopic` rows) -- our own names, and only 9 of biology's 32
    latest-edition chapters have one.
  * NCERT's own `section` rows -- the headings the book prints, with their printed numbers,
    for every chapter that has been extracted.

The 2024_S1 review asked for the printed name by name: "Part of this chapter, but exact NCERT
heading is 'Isobilateral (Monocotyledonous) Leaf'", "Not an NCERT heading. Should be
'Inheritance of One Gene'". It flagged 23 questions that way. So the printed headings are the
answer set and the A4 names ride along as `drafted_subtopics` -- offered, clearly labelled, and
never the only choice.

Usage:
    python3 code/build_d2_packets.py --paper 2024_S1
    python3 code/build_d2_packets.py --paper 2024_S1 --apply
"""

import argparse
import collections
import glob
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(HERE, "maps", "ncert_heading_index.json")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    index = json.load(open(INDEX, encoding="utf-8"))
    report = collections.Counter()
    built = []

    for d1_path in sorted(glob.glob(os.path.join(HERE, "steps", "D1", "out",
                                                 "%s.*.runA.json" % a.paper))):
        qid = os.path.basename(d1_path).split(".")[1]
        try:
            pick = json.load(open(d1_path, encoding="utf-8"))
        except Exception:
            report["d1 output unreadable"] += 1
            continue
        if pick.get("error"):
            report["d1 reported an error"] += 1
            continue
        chapters = [c for c in (pick.get("chapter_ids") or []) if c and c != "unsure"]
        if not chapters:
            report["d1 was unsure -- no chapter to narrow"] += 1
            continue

        in_path = os.path.join(HERE, "steps", "D1", "work", "%s.%s.runA.input.json" % (a.paper, qid))
        question = json.load(open(in_path, encoding="utf-8"))

        subtopics, drafted = [], []
        for ch in chapters:
            entry = index.get(ch) or {}
            if not entry:
                report["chapter not in the heading index"] += 1
                continue
            for s in entry.get("sections") or []:
                # The printed number is part of the identity: two chapters can both print
                # "Introduction", and a bare heading would not say which book it came from.
                subtopics.append({"id": "%s#%s" % (ch, s.get("n") or s["heading"][:24]),
                                  "chapter_id": ch,
                                  "printed_number": s.get("n") or "",
                                  "name": s["heading"]})
            for s in entry.get("subtopics") or []:
                drafted.append({"id": s.get("id"), "chapter_id": ch, "name": s.get("name")})
        if not subtopics:
            report["chapter has no printed headings extracted"] += 1
            continue

        built.append({
            "question_id": question.get("question_id"),
            "stem": question.get("stem"),
            "statements": question.get("statements") or [],
            "list_i": question.get("list_i") or [],
            "list_ii": question.get("list_ii") or [],
            "options": question.get("options") or [],
            "correct_answer": question.get("correct_answer"),
            "d1_chapter_ids": chapters,
            "d1_why": pick.get("why"),
            "subtopics": subtopics,
            "drafted_subtopics": drafted,
            "note_from_runner": ("`subtopics` are the headings NCERT PRINTS in this chapter, with "
                                 "their printed numbers. `drafted_subtopics` are our own earlier "
                                 "draft names for the same chapter, offered only as context -- "
                                 "choose from `subtopics`."),
        }) if True else None
        report["ready"] += 1

    print("%s: %d D2 packet(s) ready" % (a.paper, len(built)))
    for k, v in sorted(report.items()):
        if k != "ready":
            print("   skipped: %-42s %3d" % (k, v))
    if built:
        n = [len(b["subtopics"]) for b in built]
        print("   printed headings offered per question: min %d, median %d, max %d"
              % (min(n), sorted(n)[len(n) // 2], max(n)))
    if not a.apply:
        print("(nothing written -- pass --apply)")
        return

    work = os.path.join(HERE, "steps", "D2", "work")
    os.makedirs(work, exist_ok=True)
    for b in built:
        qid = b["question_id"].split("__")[-1]
        p = os.path.join(work, "%s.%s.runA.input.json" % (a.paper, qid))
        json.dump(b, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote %d packet(s) to steps/D2/work" % len(built))


if __name__ == "__main__":
    main()
