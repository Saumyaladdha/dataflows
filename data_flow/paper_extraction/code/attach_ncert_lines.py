#!/usr/bin/env python3
"""Attach judged NCERT lines to the ratings, re-checking every quote first.

    python3 code/attach_ncert_lines.py --paper 2017_A --subject biology --apply

WHY EVERY QUOTE IS RE-CHECKED HERE
----------------------------------
The judging step says it verified its quotes. This does not take that on trust. A citation that
is not actually in the book is the exact failure the NCERT row exists to prevent, and it is the
most damaging kind of error on the card, because a quote with a chapter and a page READS as
evidence -- a reader stops checking once they see one. So each quote is matched as a substring
of the chapter it is attributed to, and one that fails is dropped with a line saying so rather
than attached with a caveat.

A REJECT IS A RESULT, NOT A GAP
-------------------------------
Where the judge found NCERT does not carry the question at all, that is written onto the rating
as `ncert.found: false` with the reason, and the question is flagged `out_of_syllabus` so it
stays on the page and out of every count. This corpus is the rationalised NCERT, and whole
chapters are gone from it; a 2017 question on deleted material is a fact worth recording.
"""

import argparse
import glob
import json
import os

NCERT = ("/Users/saumyaladdha/DATAFLOWS/data_flow/ncert_extractions/data/new_ncert/"
         "class_*/%s/%s/chapter.json")


def chapter_text(subject, chapter):
    for p in glob.glob(NCERT % (subject, chapter)):
        doc = json.load(open(p, encoding="utf-8"))

        def walk(ns):
            for n in ns:
                yield n
                for c in n.get("children") or []:
                    yield from walk([c])
        return " ".join(" ".join((n.get("body") or "").split())
                        for n in walk(doc.get("tree") or []))
    return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", required=True)
    ap.add_argument("--subject", default="biology")
    ap.add_argument("--glob", default="steps/ECAT/work/ncert2__%s__%s.part*.judged.json")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    judged = {}
    files = sorted(glob.glob(a.glob % (a.paper, a.subject)))
    for p in files:
        for q in json.load(open(p, encoding="utf-8"))["questions"]:
            judged[q["question_id"]] = q
    print("judged files: %d   questions: %d" % (len(files), len(judged)))
    if not judged:
        raise SystemExit("nothing judged yet")

    cache = {}
    attached = rejected = refused = 0
    for path in sorted(glob.glob("steps/ECAT/out/ex__%s__%s__*.json" % (a.paper, a.subject))):
        doc = json.load(open(path, encoding="utf-8"))
        touched = False
        for r in doc["ratings"]:
            j = judged.get(r["question_id"])
            if not j or r.get("ncert"):          # already carries one -- leave it
                continue
            if j["decision"] == "reject" or not (j.get("quote") or "").strip():
                r["ncert"] = {"quote": "", "found": False,
                              "why_not": j.get("why", ""),
                              "searched": "all 32 %s chapters of the rationalised NCERT" % a.subject,
                              "found_by": "find_ncert_lines.py cascade, agent-judged"}
                flags = set(r.get("flags") or []) | {"out_of_syllabus"}
                r["flags"] = sorted(flags)
                r.setdefault("flag_why",
                             "The NCERT check found this topic is not in the current edition.")
                rejected += 1
                touched = True
                continue
            ch = j["chapter"]
            if ch not in cache:
                cache[ch] = chapter_text(a.subject, ch)
            if " ".join(j["quote"].split()) not in cache[ch]:
                print("  NOT VERBATIM in %s, refusing: q%s" % (ch, j.get("qno")))
                refused += 1
                continue
            r["ncert"] = {"quote": j["quote"], "chapter": ch, "page": j.get("page"),
                          "supports": j.get("supports"), "found": True,
                          "why": j.get("why", ""),
                          "found_by": "find_ncert_lines.py cascade (subtopic -> chapter -> all), "
                                      "agent-judged, quote re-checked verbatim"}
            attached += 1
            touched = True
        if touched and a.apply:
            json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("attached %d   recorded not-in-NCERT %d   refused as not verbatim %d"
          % (attached, rejected, refused))
    if not a.apply:
        print("(nothing written -- pass --apply)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
