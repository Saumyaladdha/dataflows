#!/usr/bin/env python3
"""Build ECAT packets from an EXPORTED paper (`data/<year>/<paper>/questions.json`).

    python3 code/build_ecat_packets_export.py --paper 2017_A
    python3 code/build_ecat_packets_export.py --paper 2017_A --apply

WHY A THIRD BUILDER, AND WHY IT IS NOT A FOURTH COPY OF THE RULES
-----------------------------------------------------------------
`build_ecat_packets.py` reads the v1 sheet and `build_ecat_packets_v2.py` reads the papers_v2
records that `b3v-question-verifier` has passed. A FINISHED EXPORT is neither: it is the paper
after every stage has run -- stem, options, official answer, subject, chapter, subtopic and
difficulty all `done` -- and the only thing left `excluded` is `categories`. That is exactly the
state 2017_A is in, and neither existing builder can see it (v2 reports "questions read by B3V: 0"
because B3V ran on the Code C booklet, not Code A).

So this builder exists to rate a paper that is otherwise complete. It deliberately shares the v2
PAYLOAD SHAPE, so the same brief, the same schema and the same check apply unchanged -- a packet
from here is indistinguishable to the agent from a packet from v2, except that it can carry MORE
context, because an export has the answer and the solution the raw record does not.

THE FIELD THE BRIEF PROMISES
----------------------------
`e-category-rater`'s brief opens "the question type has already been worked out for you". The v2
builder never sent it, which the ECAT audit names as the root cause of the v1 inaccuracy: a
missing field is not an error to an agent, it is a gap filled with something equally confident.
Here E1 is decided by `type_patterns.classify` -- E1's own script half, which spec 13/E1 makes the
PRIMARY classifier, the agent running only where no pattern fires -- and put through
`allowed_values.category_retired.question_type` so it speaks the current vocabulary
(`single_statement` is `plain_mcq`). Where no pattern fires the field is an explicit `null` with
the reason beside it, so "decide this yourself" is said out loud rather than implied by absence.

WHAT IS DELIBERATELY NOT SENT
-----------------------------
The publisher's SOLUTION. The agent is rating what the question demands of a student, and a
worked solution tells it what the setter did instead; rule 0.4 of the rulebook keeps the two
apart. The official ANSWER is sent, because rule 3 ("there is no trap on the answer") cannot be
applied without it.
"""

# NOTE FOR WHOEVER BUILDS PACKETS BY HAND
# ---------------------------------------
# The ANSWER does not live on the corpus record (`papers/papers/<id>.json`) -- its question
# objects carry no key at all. It lives on the EXPORT, at `answer.publisher` /
# `answer.publisher_accepted`. Reading it from the corpus record yields `null` silently, and a
# packet with `correct_answer: null` disables rulebook rule 3 ("there is no trap on the answer")
# without anything failing: the rater still produces a full, plausible sheet, having never been
# able to check that its trap was not sitting on the key. That happened on 2026_11's first
# biology run -- 43 questions rated blind -- and is why this note exists.


import argparse
import collections
import json
import os

import yaml

import runner_core as rc
import type_patterns

WORK = ("steps", "ECAT", "work")
PACKET_SIZE = 6
PREFIX = "ex"          # never collides with the v1 or `v2__` packet names


def _renames():
    allowed = yaml.safe_load(open(rc.pp("config", "allowed_values.yaml"), encoding="utf-8"))
    return (allowed.get("category_retired") or {}).get("question_type") or {}


def _e1_for(q, renames):
    """(label or None, why) -- E1 decided by script, in the current vocabulary."""
    opts = {o.get("key"): o.get("text") for o in (q.get("options") or [])}
    rec = {
        # Rule 8 (`statements` + combination options -> list_of_statements) tests `structure`,
        # which b3-question-reader records and the export calls `format`. Not passing it meant
        # rule 8 could never fire from here and every statements question defaulted to plain_mcq.
        "structure": q.get("format"),
        "stem": q.get("stem"),
        "stem_en": q.get("stem"),
        "options": opts,
        "options_en": opts,
        "statements": q.get("statements") or [],
        "list_i": q.get("list_i") or [],
        "list_ii": q.get("list_ii") or [],
    }
    try:
        hit = type_patterns.classify(rec)
    except Exception as exc:                       # reported, never guessed around
        return None, ("the pattern classifier errored (%s); decide question_type from the "
                      "layout yourself" % type(exc).__name__)
    if not hit:
        return None, "no E1 pattern fired; decide question_type from the layout yourself"
    label, rule = (hit if isinstance(hit, (list, tuple)) else (hit, "unnamed rule"))
    return renames.get(label, label), "decided by type_patterns, %s" % rule


def build(paper_id, apply_=False):
    year = paper_id.split("_")[0]
    path = rc.pp("data", year, paper_id, "questions.json")
    if not os.path.exists(path):
        raise SystemExit("no export at %s" % path)
    doc = json.load(open(path, encoding="utf-8"))
    renames = _renames()
    rulebook = rc.pp("..", "_shared", "docs", "question_categories", "RULEBOOK.md")
    if not os.path.exists(rulebook):
        raise SystemExit("rulebook not found at %s -- ECAT cannot be rated without it" % rulebook)
    codebook = open(rulebook, encoding="utf-8").read()

    groups = collections.defaultdict(list)
    skipped = collections.Counter()
    for row in doc.get("questions") or []:
        q = row.get("question") or {}
        cls = row.get("classification") or {}
        subject = (cls.get("subject") or "unknown").lower()
        # ONLY A QUESTION THE PIPELINE CALLS READ. Rating a damaged stem rates the damage
        # (RULEBOOK section 7); the export records that state per question.
        if (row.get("status") or {}).get("question") != "done":
            skipped["question not done"] += 1
            continue
        if not (q.get("stem") or "").strip() or not (q.get("options") or []):
            skipped["no stem or options"] += 1
            continue
        groups[(subject, q.get("format") or "unknown")].append((row, q, cls))

    packets = []
    for (subject, structure), rows in sorted(groups.items()):
        for i in range(0, len(rows), PACKET_SIZE):
            chunk = rows[i:i + PACKET_SIZE]
            name = "%s__%s__%s__%s.part%d" % (PREFIX, paper_id, subject, structure,
                                              i // PACKET_SIZE + 1)
            packets.append((name, subject, structure, chunk))

    print("questions: %d  skipped: %s" % (sum(len(v) for v in groups.values()),
                                          dict(skipped) or "none"))
    print("groups (subject x format): %d  ->  packets of at most %d: %d"
          % (len(groups), PACKET_SIZE, len(packets)))
    if not apply_:
        print("(nothing written -- pass --apply)")
        return packets

    os.makedirs(rc.pp(*WORK), exist_ok=True)
    written = 0
    for name, subject, structure, chunk in packets:
        out = rc.pp(*WORK, "%s.runA.input.json" % name)
        questions = []
        for row, q, cls in chunk:
            e1, why = _e1_for(q, renames)
            ans = row.get("answer") or {}
            questions.append({
                "question_id": row.get("question_id"),
                "E1_question_type": e1,
                "E1_question_type_why": why,
                "stem_en": q.get("stem"),
                "statements": q.get("statements") or [],
                "list_i": q.get("list_i") or [],
                "list_ii": q.get("list_ii") or [],
                "options_en": {o.get("key"): o.get("text") for o in (q.get("options") or [])},
                # A PAPER THAT AWARDED TWO OPTIONS STILL HAS A KEY. `publisher` holds one
                # option and is null when the booklet printed "Answer (1 & 4)", so sending it
                # alone told the rater the key was missing -- and a missing key reads as a
                # damaged record, which rule 3 says must not be given a trap at all. The
                # accepted list is the real key in that case, and rule 3 ("no trap on the
                # answer") then has to clear EVERY accepted option, not just the first.
                "correct_answer": ans.get("publisher") or (ans.get("publisher_accepted") or [None])[0],
                "accepted_answers": ans.get("publisher_accepted") or (
                    [ans["publisher"]] if ans.get("publisher") else []),
                "answer_line_as_printed": ans.get("publisher_line"),
                "negative_words_seen": q.get("negative_words") or [],
                "has_figure": bool(q.get("figures")),
                "figure_image": (q.get("figures") or [None])[0],
                # Context the raw record does not have. Named, so the agent knows these were
                # decided by earlier steps and are not its to re-open.
                "subject": cls.get("subject"),
                "chapter": (cls.get("chapter") or {}).get("name"),
                # The export records `subtopics` as a LIST, not a `subtopic` object; the
                # singular key is always absent, so reading it sent null on every question.
                "subtopics": [s.get("name") for s in (cls.get("subtopics") or [])
                              if isinstance(s, dict) and s.get("name")],
                "difficulty_level": (row.get("difficulty") or {}).get("level"),
            })
        payload = {
            "group": name,
            "subject": subject,
            # THE CODEBOOK TRAVELS WITH THE PACKET.
            #
            # `steps.yaml` lists `codebook` among ECAT's input_fields and sets `codebook_file`,
            # but no packet ever carried the text -- and the rater's own tools are Read and
            # Write, with no way to search for a file. Pointed at a path that did not resolve
            # from its working directory, the agent correctly refused to rate rather than guess
            # among 37 trap labels it could not see (brief rule 5). Of the five axes only the
            # trap list lives solely in the rulebook, so a missing codebook does not degrade the
            # rating, it blocks it. Sent inline, it cannot go missing.
            "codebook": codebook,
            "grouped_on": ("`format` as the export records it -- the nearest measured stand-in "
                           "for E1. Each question also carries `E1_question_type` where a "
                           "pattern decided it and null where none did; read "
                           "`E1_question_type_why`. Say so in group_note if a member does not "
                           "belong with the rest."),
            "structure": structure,
            "questions": questions,
        }
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=1)
        written += 1
    print("wrote %d packet(s) to %s" % (written, os.path.relpath(rc.pp(*WORK), rc.pp())))
    return packets


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", required=True, help="e.g. 2017_A")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    build(a.paper, a.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
