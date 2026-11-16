#!/usr/bin/env python3
"""Build D4 (latest-edition NCERT line) packets from D1's chapter and D2's subtopic.

WHAT D4 NEEDS AND WHERE IT COMES FROM
-------------------------------------
The brief asks for `passages` ("5-15 latest-edition passages, id + full text -- a RANKED
STARTING POINT") and `chapter_index` ("every passage in this chapter, as id + section heading
+ page"). Both are assembled from `ncert_content`: a passage row carries `nodes`, a list of
block keys, and the prose lives on the blocks, so the text is joined back together in
`maps/passage_text_<paper>.json` rather than read from a book file on disk. `search_this_file`
is therefore omitted and `how_to_search` says so -- promising a file the agent cannot open
would invite it to claim a search it never ran.

RANKING IS BY THE SUBTOPIC D2 ALREADY CHOSE
-------------------------------------------
Passages whose `section_heading` matches a D2 subtopic come first; the rest of the chapter
follows, capped. The cap is real and is reported: a chapter like BIO12L-CH04 has 112 passages
and sending all of them would bury the ranked ones.

THE HONEST GAP
--------------
Several class-12 chapters have NO passage text at all (BIO12L-CH06 and CH11 return 0; CH01,
CH05, CH12, CH13 return 4, 16, 3, 5). That is the unfinished A3 passage split recorded in the
storage design, not a loader fault. A question in one of those chapters cannot be quoted, so it
is SKIPPED and counted -- never handed an empty `passages` list, which would read to the agent
as "NCERT does not say this".

Usage:
    python3 code/build_d4_packets.py --paper 2024_S1
    python3 code/build_d4_packets.py --paper 2024_S1 --apply
"""

import argparse
import collections
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_RANKED = 15
MAX_INDEX = 140

HOW = ("`passages` are the ranked candidates, assembled from the stored chapter -- the ones whose "
       "section heading matches the subtopic chosen for this question come first. `chapter_index` "
       "lists every stored passage of the chapter so you can go outside the ranked set. There is "
       "no book file to open in this run: if the line you need is in neither list, say so in "
       "`note` rather than quoting from memory.")


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()


#: Words too common in biology prose to carry any ranking signal.
STOP = set(("the a an of in to and or is are was were be been for on with that this these those "
            "it its as at by from which what not but can also more than then them their there "
            "has have had do does did will would may might one two both each other such into "
            "following given above shown figure cell cells body plant plants animal animals").split())


def keywords(*parts):
    ws = re.findall(r"[a-z]{4,}", norm(" ".join(str(p or "") for p in parts)))
    return set(w for w in ws if w not in STOP)


def heading_of(index, subtopic_id):
    """Turn a D2 id like `BIO11L-CH06#6.2.6` back into the heading it names.

    D2 answers with the id this pipeline minted, whose tail is the PRINTED NUMBER ("6.2.6"),
    not the heading text. The first version of this ranker compared that number against each
    passage's `section_heading` and so matched nothing: 0 of 92 packets got a ranked passage,
    and every one silently fell back to chapter order. Resolve the number to its heading first.
    """
    ch, _, tail = str(subtopic_id or "").partition("#")
    for sec in ((index.get(ch) or {}).get("sections") or []):
        if tail and (sec.get("n") == tail or norm(sec.get("heading")) == norm(tail)):
            return sec.get("heading")
    return tail or None


def q_stem_for_rank(q):
    """Everything in the question that names content: stem, statements, both match lists."""
    bits = [q.get("stem")]
    bits += [str(x) for x in (q.get("statements") or [])]
    bits += [str(x) for x in (q.get("list_i") or [])]
    bits += [str(x) for x in (q.get("list_ii") or [])]
    return " ".join(b for b in bits if b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    text = json.load(open(os.path.join(HERE, "maps",
                                       "passage_text_%s.json" % a.paper), encoding="utf-8"))
    index = json.load(open(os.path.join(HERE, "maps", "ncert_heading_index.json"),
                           encoding="utf-8"))
    report = collections.Counter()
    built = []

    for d1_path in sorted(glob.glob(os.path.join(HERE, "steps", "D1", "out",
                                                 "%s.*.runA.json" % a.paper))):
        qid = os.path.basename(d1_path).split(".")[1]
        pick = json.load(open(d1_path, encoding="utf-8"))
        chapters = [c for c in (pick.get("chapter_ids") or []) if c and c != "unsure"]
        if not chapters:
            report["d1 unsure -- no chapter"] += 1
            continue

        pool = []
        for ch in chapters:
            pool += text.get(ch) or []
        if not pool:
            report["chapter has no passage text stored (A3 incomplete)"] += 1
            continue

        q = json.load(open(os.path.join(HERE, "steps", "D1", "work",
                                        "%s.%s.runA.input.json" % (a.paper, qid)),
                           encoding="utf-8"))

        # D2's subtopic names, if D2 has run for this question
        wanted = set()
        heads = []
        d2_path = os.path.join(HERE, "steps", "D2", "out", "%s.%s.runA.json" % (a.paper, qid))
        d2 = {}
        if os.path.exists(d2_path):
            try:
                d2 = json.load(open(d2_path, encoding="utf-8"))
            except Exception:
                report["d2 output unreadable"] += 1
            for sid in (d2.get("subtopic_ids") or []):
                if sid and sid != "unsure":
                    h = heading_of(index, sid)
                    if h:
                        heads.append(h)
                        wanted.add(norm(h))

        # TWO SIGNALS, BECAUSE ONE IS NOT ENOUGH. Only 361 of the 1,593 stored passages carry a
        # `section_heading` at all (23%), so heading matching alone leaves three quarters of the
        # book unrankable. Word overlap with the stem, the answer and the chosen heading covers
        # the rest; the heading match, where it exists, is worth more and is added to the score.
        kw = keywords(q_stem_for_rank(q), (q.get("correct_answer") or {}).get("text"), *heads)

        def score(p):
            s_ = 3 if norm(p["section_heading"]) in wanted else 0
            return s_ + len(kw & keywords(p["text"]))

        scored = sorted(pool, key=score, reverse=True)
        ranked = [p for p in scored if score(p) > 0]
        passages = scored[:MAX_RANKED]
        if not ranked:
            report["nothing in the chapter overlapped the question"] += 1
        if wanted and not any(norm(p["section_heading"]) in wanted for p in pool):
            report["D2 heading not present on any stored passage"] += 1

        ca = q.get("correct_answer") or {}
        built.append({
            "question_id": q.get("question_id"),
            "stem": q.get("stem"),
            "statements": q.get("statements") or [],
            "list_i": q.get("list_i") or [],
            "list_ii": q.get("list_ii") or [],
            "options": q.get("options") or [],
            "answer_to_support": {"option": ca.get("option"), "text": ca.get("text"),
                                  "accepted_options": ca.get("accepted_options") or [],
                                  "agreement": ca.get("agreement")},
            "d1_chapter_ids": chapters,
            "d2_subtopic_ids": d2.get("subtopic_ids") or [],
            "passages": [{"passage_id": p["passage_id"], "section_heading": p["section_heading"],
                          "text": p["text"]} for p in passages],
            "chapter_index": [{"passage_id": p["passage_id"],
                               "section_heading": p["section_heading"],
                               "pages": p.get("pages") or []} for p in pool[:MAX_INDEX]],
            "how_to_search": HOW,
            "ranked_by_subtopic": len(ranked),
            "chapter_passages_total": len(pool),
        })
        report["ready"] += 1

    print("%s: %d D4 packet(s) ready" % (a.paper, len(built)))
    for k, v in sorted(report.items()):
        if k != "ready":
            print("   %-48s %3d" % (k, v))
    if built:
        print("   ranked-by-subtopic hits: %d of %d packets have at least one"
              % (sum(1 for b in built if b["ranked_by_subtopic"]), len(built)))
    if not a.apply:
        print("(nothing written -- pass --apply)")
        return
    work = os.path.join(HERE, "steps", "D4", "work")
    os.makedirs(work, exist_ok=True)
    for b in built:
        qid = b["question_id"].split("__")[-1]
        json.dump(b, open(os.path.join(work, "%s.%s.runA.input.json" % (a.paper, qid)),
                          "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote %d packet(s) to steps/D4/work" % len(built))


if __name__ == "__main__":
    main()
