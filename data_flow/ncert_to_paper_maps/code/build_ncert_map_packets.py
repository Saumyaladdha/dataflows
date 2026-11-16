#!/usr/bin/env python3
"""Build NCERT-mapping packets (D1, D2, QCA) from a FINISHED PAPER EXPORT.

WHY A SEPARATE STEP, AND NOT PART OF ECAT
-----------------------------------------
ECAT answers "what does this question do to a student" and needs only the question. NCERT
mapping answers "where in the book does this answer live", which needs the book -- a different
input, a different failure mode, and a different agent. Keeping them apart is also what lets
one be re-run without the other: the 2024_S1 ECAT re-rate touched 7 packets and left the
mapping alone.

WHY IT READS THE EXPORT AND NOT THE PIPELINE
--------------------------------------------
`run_step.py D1 --list` reports "every ready question's subject has zero chapters indexed",
and `export_paper_v2.py --data --paper-id 2024_S1` answers "no v2 papers found": these papers
are finished exports whose v2 CORPUS record is gone. `build_ecat_packets_export.py` exists for
exactly this reason, and this builder is its twin on the NCERT side.

THE SUBTOPIC LIST IS THE PRINTED HEADINGS, NOT OUR OWN NAMES
------------------------------------------------------------
D2 is handed `maps/ncert_heading_index.json`, built from the `section` rows of `ncert_content`
-- the headings NCERT actually prints, with their printed numbers ("6.1 The Tissue System").
The A4 lists are carried alongside as `drafted_subtopics` but they are NOT the answer set: A4
covers 9 of biology's 32 latest-edition chapters, and the 2024_S1 review asked for the printed
name specifically -- "exact NCERT heading is 'Isobilateral (Monocotyledonous) Leaf'" -- which
is a `section` row and was never an A4 name.

ROUTING, WHICH IS THE SAME RULE STAGE D ALREADY USES
----------------------------------------------------
    Biology, Organic, Inorganic  ->  D1 -> D2 -> D4 (latest line) -> D5 (older line)
    Physics, Physical Chemistry  ->  QCA (concept + approach)
A numerical's answer is a value and NCERT prints sentences, so a quote step on physics returns
"partly supported" and means nothing. Only the LATEST editions are offered to D1/D2; D5 gets
the older book, because "what did the older edition say" is its whole question.

Usage:
    python3 code/build_ncert_map_packets.py --paper 2024_S1
    python3 code/build_ncert_map_packets.py --paper 2024_S1 --apply
"""

import argparse
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(HERE))
PAPERS = os.path.join(REPO, "data_flow", "paper_extraction", "data")
INDEX = os.path.join(HERE, "maps", "ncert_heading_index.json")

#: Latest-edition biology books. D1 chooses only from these; D5 is handed the `O` twins.
LATEST = ("BIO11L", "BIO12L")
#: Stage D quotes NCERT for these; QCA handles the rest.
QUOTED = {"biology", "organic", "inorganic"}


def load_paper(paper):
    year = paper.split("_")[0]
    path = os.path.join(PAPERS, year, paper, "questions.json")
    if not os.path.exists(path):
        sys.exit("no export at %s" % path)
    return json.load(open(path, encoding="utf-8"))


def route(cls):
    """Which evidence step this question goes to.

    CHEMISTRY IS HELD BACK, and not as a simplification. The owner deferred it, and the data
    agrees: `ncert_content` holds CHE11L and nothing else -- 9 chapters, no class 12 at all and
    no older edition of either. Offering a chemistry question the biology chapter menu would
    force a wrong pick from a closed list, and D5's whole question ("what did the older book
    say") has no book to ask. So chemistry is routed nowhere and counted, rather than guessed.
    Its `QUOTED` streams stay named above for when those books are extracted.
    """
    subject = str(cls.get("subject") or "").lower()
    if subject == "biology":
        return "quote"
    if subject == "chemistry":
        return "deferred"
    return "qca"          # physics


def chapter_menu(index):
    """The closed chapter list D1 picks from: id, title, and its printed top-level headings."""
    out = []
    for key in sorted(index):
        if not key.startswith(LATEST):
            continue
        entry = index[key]
        # Top-level only. A chapter with 20 headings would otherwise crowd out the other 31
        # chapters in the prompt, and D1's question is which CHAPTER, not which heading.
        tops = [s["heading"] for s in entry.get("sections") or [] if (s.get("n") or "").count(".") <= 1]
        out.append({"chapter_id": key, "title": entry.get("title") or "",
                    "headings": tops[:12]})
    return out


def question_payload(q):
    """The question as the agents' Input sections describe it: stem, lists, options, answer."""
    qq = q.get("question") or {}
    opts = []
    for o in (qq.get("options") or []):
        text = str(o.get("text") or "").strip()
        if not text:
            fig = (o.get("figure") or {}).get("text")
            text = "[drawn option] %s" % str(fig).strip() if str(fig or "").strip() else ""
        opts.append({"key": o.get("key"), "text": text})
    # THE ANSWER IS UNDER `publisher`, NOT `option`. The first version of this builder read
    # `answer.option` / `answer.text`, which do not exist in an export: all 200 questions of
    # 2024_S1 carry `publisher` / `publisher_text` / `publisher_accepted` / `ai` / `verdict`.
    # So every packet shipped `correct_answer: null`, and d1-chapter-picker said so in its own
    # note -- "the pick rests on the stem and options alone". Picking the chapter NCERT puts an
    # answer in, without being told the answer, is most of the task thrown away.
    #
    # `accepted` is carried separately because a paper can award TWO options, and a mapping
    # anchored on one of them would contradict the key it was built from. `ai` and `verdict`
    # ride along so a disputed key is visible to the agent rather than hidden behind one value.
    ans = q.get("answer") or {}
    accepted = [str(x) for x in (ans.get("publisher_accepted") or []) if str(x).strip()]
    official = str(ans.get("publisher") or "").strip()
    if official and official not in accepted:
        accepted.insert(0, official)
    return {
        "question_id": q.get("question_id"),
        "stem": qq.get("stem"),
        "statements": qq.get("statements") or [],
        "list_i": qq.get("list_i") or [],
        "list_ii": qq.get("list_ii") or [],
        "options": opts,
        "correct_answer": {"option": official or None,
                           "text": ans.get("publisher_text"),
                           "accepted_options": accepted,
                           "independently_solved": ans.get("ai"),
                           "independently_solved_text": ans.get("ai_text"),
                           "agreement": ans.get("verdict")},
        "subject": (q.get("classification") or {}).get("subject"),
        "stream": (q.get("classification") or {}).get("stream"),
        # THE EXAM TAXONOMY'S CHAPTER IS NOT PASSED. It used to be, as a hint, and the agents
        # were visibly steered by it -- "the input's own examtopicmapping_chapter names that
        # same missing chapter", "that one disagrees with the hint". In the NCERT-first order
        # NCERT decides on its own evidence; a coaching label arriving alongside the question
        # is exactly the contamination this reordering exists to remove. The taxonomy stays in
        # `questions.json`, it just does not travel into the decision.
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    doc = load_paper(a.paper)
    index = json.load(open(INDEX, encoding="utf-8"))
    menu = chapter_menu(index)

    counts = collections.Counter()
    d1, qca = [], []
    for q in doc["questions"]:
        cls = q.get("classification") or {}
        where = route(cls)
        counts["%s:%s" % (str(cls.get("subject") or "?").lower(), where)] += 1
        payload = question_payload(q)
        if where == "quote":
            d1.append(payload)
        elif where == "qca":
            qca.append(payload)

    print("%s: %d questions" % (a.paper, len(doc["questions"])))
    for k, v in sorted(counts.items()):
        print("   %-22s %3d" % (k, v))
    print("D1 (chapter, then subtopic): %d   QCA (concept + approach): %d" % (len(d1), len(qca)))
    print("chapter menu offered to D1: %d chapters from %s" % (len(menu), ", ".join(LATEST)))

    if not a.apply:
        print("(nothing written -- pass --apply)")
        return

    for step, rows, extra in (("D1", d1, {"chapters": menu}), ("QCA", qca, {})):
        work = os.path.join(HERE, "steps", step, "work")
        os.makedirs(work, exist_ok=True)
        for row in rows:
            name = "%s.%s.runA.input.json" % (a.paper, row["question_id"].split("__")[-1])
            body = dict(row)
            body.update(extra)
            with open(os.path.join(work, name), "w", encoding="utf-8") as fh:
                json.dump(body, fh, ensure_ascii=False, indent=1)
        print("wrote %d %s packet(s) to steps/%s/work" % (len(rows), step, step))


if __name__ == "__main__":
    main()
