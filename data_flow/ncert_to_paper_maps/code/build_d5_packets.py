#!/usr/bin/env python3
"""Build D5 (older-edition NCERT line) packets from D4's latest-edition evidence.

THE OLDER BOOK HAS BLOCKS, NOT PASSAGES
---------------------------------------
Measured in `ncert_content`: BIO11L carries 1,105 passage rows and BIO12L 527, but BIO11O
carries 84 and BIO12O **zero** -- while those same older books hold 1,190 and 920 `para` rows.
The prose is there; the A3 passage split was never run on the older editions (the storage
design records this as `blocks_resolved: false`). So D5's `older_passages` are assembled from
the text-bearing BLOCKS, and their ids say so: `BIO11O-CH13#PG#004#BL#0021`, not a passage id.
Calling them passage ids would invite a later join against passages that do not exist.

THE EDITION PAIR IS MATCHED ON CONTENT, NOT ON CHAPTER NUMBER
-------------------------------------------------------------
`PAIR#` rows in the table: zero. A6-A9 outputs on disk: zero files. And the numbers genuinely
move -- BIO11L-CH11 is BIO11O-CH13, BIO11L-CH14 is BIO11O-CH17, BIO12L-CH08 is BIO12O-CH10.
Pairing by number would have filed those three chapters' worth of questions against unrelated
older chapters. `maps/edition_pairs.json` is built from keyword overlap instead and every pair
used here scored Jaccard 0.42-0.997 with a clear margin over the runner-up.

WHAT "NONE" MEANS HERE, AND WHY IT IS THE POINT
-----------------------------------------------
A question whose answer has a latest line but no older line is a topic NCERT ADDED; one with an
older line and no latest line is a topic it REMOVED -- which is what feeds the syllabus status.
So D5 returning `none_for` is a finding, and the builder never withholds the older chapter to
make that outcome tidier.

Usage:
    python3 code/build_d5_packets.py --paper 2024_S1
    python3 code/build_d5_packets.py --paper 2024_S1 --apply
"""

import argparse
import collections
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_OLDER = 18

STOP = set(("the a an of in to and or is are was were be been for on with that this these those it "
            "its as at by from which what not but can also more than then them their there has have "
            "had do does did will would may might one two both each other such into following given "
            "above shown figure").split())


def keywords(*parts):
    ws = re.findall(r"[a-z]{4,}", " ".join(str(p or "") for p in parts).lower())
    return set(w for w in ws if w not in STOP)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    older = json.load(open(os.path.join(HERE, "maps", "older_blocks.json"), encoding="utf-8"))
    pairs = json.load(open(os.path.join(HERE, "maps", "edition_pairs.json"), encoding="utf-8"))
    report = collections.Counter()
    built = []

    for d4_path in sorted(glob.glob(os.path.join(HERE, "steps", "D4", "out",
                                                 "%s.*.runA.json" % a.paper))):
        qid = os.path.basename(d4_path).split(".")[1]
        try:
            d4 = json.load(open(d4_path, encoding="utf-8"))
        except Exception:
            report["d4 output unreadable"] += 1
            continue
        if d4.get("error"):
            report["d4 reported an error"] += 1
            continue

        q = json.load(open(os.path.join(HERE, "steps", "D4", "work",
                                        "%s.%s.runA.input.json" % (a.paper, qid)),
                           encoding="utf-8"))
        chapters = q.get("d1_chapter_ids") or []
        pool = []
        for ch in chapters:
            pair = pairs.get(ch) or {}
            if not pair.get("older"):
                report["no confident older partner for %s" % ch] += 1
                continue
            pool += older.get(pair["older"]) or []
        if not pool:
            report["older edition has no text for this chapter"] += 1
            continue

        # Rank the older blocks the same way D4's were: overlap with the question and with the
        # lines D4 actually settled on, so the older partner of the SAME fact comes first.
        kw = keywords(q.get("stem"), *[str(x) for x in (q.get("statements") or [])],
                      (q.get("answer_to_support") or {}).get("text"),
                      *[e.get("exact_line") for e in (d4.get("evidence") or [])])
        ranked = sorted(pool, key=lambda b: len(kw & keywords(b["text"])), reverse=True)
        chosen = ranked[:MAX_OLDER]
        if not (kw & keywords(chosen[0]["text"])) if chosen else True:
            report["nothing in the older chapter overlapped"] += 1

        ca = q.get("answer_to_support") or {}
        built.append({
            "question_id": q.get("question_id"),
            "stem": q.get("stem"),
            "statements": q.get("statements") or [],
            "list_i": q.get("list_i") or [],
            "list_ii": q.get("list_ii") or [],
            "options": q.get("options") or [],
            "answer_to_support": ca,
            "latest_evidence": d4.get("evidence") or [],
            "latest_link_type": d4.get("link_type"),
            "latest_supports_answer": d4.get("supports_answer"),
            "older_passages": [{"passage_id": b["block_id"], "heading": b.get("heading", ""),
                                "text": b["text"]} for b in chosen],
            "edition_pair": {ch: (pairs.get(ch) or {}) for ch in chapters},
            "note_from_runner": ("`older_passages` ids are BLOCK ids of the older edition "
                                 "(`BIO11O-CH13#PG#004#BL#0021`), because the older books have "
                                 "no passage rows. Quote only from this list; if the older book "
                                 "has no line for a part of the answer, name it in `none_for`."),
        })
        report["ready"] += 1

    print("%s: %d D5 packet(s) ready" % (a.paper, len(built)))
    for k, v in sorted(report.items()):
        if k != "ready":
            print("   %-52s %3d" % (k, v))
    if not a.apply:
        print("(nothing written -- pass --apply)")
        return
    work = os.path.join(HERE, "steps", "D5", "work")
    os.makedirs(work, exist_ok=True)
    for b in built:
        qid = b["question_id"].split("__")[-1]
        json.dump(b, open(os.path.join(work, "%s.%s.runA.input.json" % (a.paper, qid)),
                          "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote %d packet(s) to steps/D5/work" % len(built))


if __name__ == "__main__":
    main()
