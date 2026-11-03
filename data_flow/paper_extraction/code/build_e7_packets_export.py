#!/usr/bin/env python3
"""Build difficulty packets from an EXPORTED paper, for a re-rate.

    python3 code/build_e7_packets_export.py --paper 2017_A --apply

WHY FROM THE EXPORT
-------------------
`E7V` needs `B3V`, which ran on a different booklet, so it can see nothing of 2017_A. The export
is the paper after every stage has run, and it holds the stem, the options and the figure -- all
a difficulty rater needs, and more than it is allowed.

WHAT IS WITHHELD, AND WHY IT MATTERS MORE HERE THAN ANYWHERE ELSE
-----------------------------------------------------------------
THE ANSWER. Not the printed key, not the accepted list, not the publisher's solution, not the
AI's solution, and not the difficulty the last run recorded.

A rater that sees the key reasons backwards from it, and the route to a known answer is always
shorter than the route a candidate has to find. Worse for this step: the whole second spine is
"how many options would a candidate actually consider", and nobody can judge that honestly while
knowing which one is right -- every other option looks obviously wrong once you know. So the key
is withheld, and the packet says so, rather than being trusted to ignore it.

The previous difficulty is withheld for the same reason in reverse: it would be anchored to.
"""

import argparse
import collections
import json
import os

import runner_core as rc

WORK = ("steps", "E7V", "work")
PACKET = 10
PREFIX = "ex7"


def build(paper_id, apply_=False):
    year = paper_id.split("_")[0]
    path = rc.pp("data", year, paper_id, "questions.json")
    if not os.path.exists(path):
        raise SystemExit("no export at %s" % path)
    doc = json.load(open(path, encoding="utf-8"))

    groups = collections.defaultdict(list)
    skipped = collections.Counter()
    for row in doc.get("questions") or []:
        q = row.get("question") or {}
        if (row.get("status") or {}).get("question") != "done":
            skipped["question not done"] += 1
            continue
        if not (q.get("stem") or "").strip() or not (q.get("options") or []):
            skipped["no stem or options"] += 1
            continue
        subject = ((row.get("classification") or {}).get("subject") or "unknown").lower()
        groups[subject].append((row, q))

    packets = []
    for subject, rows in sorted(groups.items()):
        rows.sort(key=lambda r: r[0].get("qno") or 0)
        for i in range(0, len(rows), PACKET):
            packets.append(("%s__%s__%s.part%d" % (PREFIX, paper_id, subject, i // PACKET + 1),
                            subject, rows[i:i + PACKET]))

    print("questions: %d  skipped: %s" % (sum(len(v) for v in groups.values()),
                                          dict(skipped) or "none"))
    print("packets of at most %d: %d" % (PACKET, len(packets)))
    if not apply_:
        print("(nothing written -- pass --apply)")
        return packets

    os.makedirs(rc.pp(*WORK), exist_ok=True)
    for name, subject, chunk in packets:
        questions = []
        for row, q in chunk:
            questions.append({
                "question_id": row.get("question_id"),
                "qno": row.get("qno"),
                "stem_en": q.get("stem"),
                "statements": q.get("statements") or [],
                "list_i": q.get("list_i") or [],
                "list_ii": q.get("list_ii") or [],
                "options_en": {o.get("key"): o.get("text") for o in (q.get("options") or [])},
                "structure": q.get("format"),
                "subject": (row.get("classification") or {}).get("subject"),
                "chapter": ((row.get("classification") or {}).get("chapter") or {}).get("name"),
                "has_figure": bool(q.get("figures")),
                "figure_image": (q.get("figures") or [None])[0],
                "negative_words_seen": q.get("negative_words") or [],
            })
        payload = {
            "group": name,
            "subject": subject,
            "answer_withheld": ("Deliberate. You are judging how many options a candidate would "
                                "consider, and nobody can judge that while knowing which one is "
                                "right. Do not guess the key from the option set and then rate "
                                "around it -- rate the question as a candidate meets it."),
            "questions": questions,
        }
        with open(rc.pp(*WORK, "%s.runA.input.json" % name), "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=1)
    print("wrote %d packet(s) to %s" % (len(packets), os.path.relpath(rc.pp(*WORK), rc.pp())))
    return packets


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    build(a.paper, a.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
