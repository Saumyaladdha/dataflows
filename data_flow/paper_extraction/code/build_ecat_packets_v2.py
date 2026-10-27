"""Build ECAT packets for the papers_v2 corpus: groups of similar questions, judged together.

WHY GROUPS AND NOT QUESTIONS
----------------------------
`RULEBOOK.md` rule 0.7 requires similar questions to be judged AGAINST EACH OTHER. v1 was tagged in
paper order and so gave one match-list question `check_each_statement` and another `elimination`,
with no stated reason anywhere for the difference. An agent that never sees the two together has no
way to be consistent, and no way to say why a member of a group differs. Hence the item is a group,
`ratings` is an array, and `group_note` is required -- the note is where the agent records how the
group was kept consistent, which is the thing v1 had no place to write down.

WHAT THE GROUPS ARE GROUPED BY, AND THE ONE COMPROMISE
-----------------------------------------------------
v1 grouped by (subject x E1 question_type). For this corpus E1 has not been assigned yet -- that is
what ECAT is for -- so grouping by it would be circular. Instead the groups are (subject x
`structure`), where `structure` is what `b3-question-reader` recorded about the SHAPE OF THE PAGE:
plain / match / statements / table / list / assertion_reason.

That is a near-miss for E1 rather than a substitute, and deliberately so. E1 is defined as "what the
question LOOKS like, decided from layout alone", which is exactly what `structure` measures, so the
two are close enough that a group is genuinely comparable. Where they differ -- `plain` covers
several E1 types -- the cost is only that a `plain` group is broader than ideal, not that unlike
questions are compared. The agent is told what the group was formed on, so it can say in
`group_note` when a member does not belong.

ONLY QUESTIONS B3V HAS READ
---------------------------
Same rule as B6V and E7V. Tagging a text-layer draft tags the extraction's damage: a question whose
options arrived blank would be labelled with whatever shape the damage left behind, and RULEBOOK
Section 7 ("fix the question before tagging it") exists precisely to stop that.
"""

import argparse
import collections
import glob
import json
import os

import runner_core as rc

CORPUS = rc.corpus()
B3V_OUT = ("steps", "B3V", "out")
WORK = ("steps", "ECAT", "work")
#: Rule 0.7's limit: more than six and the agent cannot hold the group in view while judging it.
PACKET_SIZE = 6
#: v2 packets are prefixed so they can never be confused with the v1 sheet's packets, which the
#: same plugin lists from the same directory.
PREFIX = "v2"


def read_questions(papers=None):
    """[(item_id, paper_id, question, read)] for every v2 question B3V has read."""
    out = []
    for path in sorted(glob.glob(rc.pp(*CORPUS, "papers", "*.json"))):
        with open(path, encoding="utf-8") as fh:
            paper = json.load(fh)
        meta = paper["meta"]
        paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
        if papers and paper_id not in papers:
            continue
        for question in paper["questions"]:
            read_path = rc.pp(*B3V_OUT, "%s__q%03d.runA.json" % (paper_id, question["qno"]))
            if not os.path.exists(read_path):
                continue
            try:
                with open(read_path, encoding="utf-8") as fh:
                    read = json.load(fh)
            except ValueError:
                continue
            if "error" in read:
                continue
            out.append(("%s#q%03d" % (paper_id, question["qno"]), paper_id, question, read))
    return out


def subject_of(question, item_id):
    """The confirmed subject, preferring QSUBJ's reading over the paper's positional guess."""
    path = rc.pp("steps", "QSUBJ", "out", "%s.runA.json" % item_id.replace("#", "__"))
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
            if data.get("subject") and data["subject"] != "unsure":
                return data["subject"]
        except ValueError:
            pass
    return question.get("subject") or "unknown"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--papers", nargs="*", help="limit to these paper ids")
    args = ap.parse_args()

    questions = read_questions(set(args.papers or []))
    groups = collections.defaultdict(list)
    for item_id, paper_id, question, read in questions:
        # THE PAPER IS PART OF THE GROUP KEY. Without it the packet names -- built from subject and
        # structure alone -- are identical across booklets, so a second paper's run finds every name
        # already taken and writes nothing. 2016_X produced 2 packets instead of 35 that way, and the
        # 179 questions it left out looked like a rating gap rather than a naming collision.
        key = (paper_id, subject_of(question, item_id).lower(), read.get("structure") or "unknown")
        groups[key].append((item_id, paper_id, question, read))

    packets, oversize = [], 0
    for (paper_id, subject, structure), members in sorted(groups.items()):
        for index in range(0, len(members), PACKET_SIZE):
            chunk = members[index:index + PACKET_SIZE]
            name = "%s__%s__%s__%s.part%d" % (PREFIX, paper_id, subject, structure,
                                              index // PACKET_SIZE + 1)
            packets.append((name, subject, structure, chunk))
        oversize += 1 if len(members) > PACKET_SIZE else 0

    print("questions read by B3V: %d" % len(questions))
    print("groups (subject x structure): %d  ->  packets of at most %d: %d"
          % (len(groups), PACKET_SIZE, len(packets)))
    for (paper_id, subject, structure), members in sorted(groups.items()):
        print("  %-8s %-10s %-16s %4d" % (paper_id, subject, structure, len(members)))

    if not args.apply:
        print("(nothing written -- pass --apply)")
        return 0

    os.makedirs(rc.pp(*WORK), exist_ok=True)
    written = 0
    for name, subject, structure, chunk in packets:
        path = rc.pp(*WORK, "%s.runA.input.json" % name)
        if os.path.exists(path):
            continue
        payload = {
            "group": name,
            "subject": subject,
            "grouped_on": ("`structure` as read from the page by b3-question-reader -- the nearest "
                           "measured stand-in for E1, which this step is what assigns. Say so in "
                           "group_note if a member does not belong with the rest."),
            "structure": structure,
            "questions": [{
                "question_id": item_id,
                "stem_en": read.get("stem_en"),
                "statements": read.get("statements") or [],
                "list_i": read.get("list_i") or [],
                "list_ii": read.get("list_ii") or [],
                "options_en": read.get("options_en") or {},
                "correct_answer": (question.get("text_layer_draft") or {}).get("official_answer"),
                "negative_words_seen": read.get("negative_words_seen") or [],
                "has_figure": read.get("has_figure"),
                "figure_image": (question.get("agent_figure_images")
                                 or question.get("figure_images") or [None])[0],
            } for item_id, _paper_id, question, read in chunk],
        }
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=1)
        written += 1
    print("wrote %d new packet(s) to %s" % (written, os.path.relpath(rc.pp(*WORK), rc.pp())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
