#!/usr/bin/env python3
"""Build the e-category-rater work packets from the finalised sheet.

    python3 scripts/build_ecat_packets.py --dry-run
    python3 scripts/build_ecat_packets.py --apply

The rulebook requires similar questions to be judged TOGETHER (rule 0.7), because v1 was tagged in
paper order and so gave one match-list question `check_each_statement` and another `elimination` with
no stated reason for the difference. So a packet is one (subject, E1 type) group, capped at
`--per-packet` questions.

Grouping by subject as well as type is deliberate: the same printed shape asks for different work in
different subjects -- a Chemistry `statement_options` item turns on reagent mappings, a Biology one
on textbook sentences -- and a rater comparing across subjects has no basis for "equal demands get
equal labels".

The earlier packets covered the 55-row showcase. This builds over all 580, which is the whole point
of the sheet having been rebuilt from `QUESTIONS.xlsx`.
"""

import argparse
import collections
import csv
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

SHEET = ("docs", "question_categories", "SHEET_V2.csv")
RULEBOOK = ("docs", "question_categories", "RULEBOOK.md")
WORK = ("steps", "ECAT", "work")

#: fields the rater is allowed to see. The official answer IS included -- unlike B6, this step is
#: not checking the key, and a trap route cannot be named without knowing which option is right.
CARRY = ["question_id", "subject", "year", "question", "options", "official_answer",
         "E1_question_type", "E1_secondary_type", "E2_answer_form", "E3_content_shape",
         "task_polarity", "review_status", "review_status_why"]


def primary_type(raw):
    """The PRIMARY E1 type, with overlays dropped.

    v1 wrote overlays into the same cell as the shape ("statement_options;figure_to_read"), but
    `figure_to_read` and `fill_in_blank` are overlays, not shapes -- rulebook section 1 puts them in
    `E1_secondary_type`. Grouping on the raw cell invented a one-member group whose name was two
    labels joined by a semicolon, which is neither a valid item id nor a real question type.
    """
    parts = [p.strip() for p in str(raw or "").split(";") if p.strip()]
    overlays = {"figure_to_read", "fill_in_blank", "experiment_based", "table_based"}
    primary = [p for p in parts if p not in overlays]
    return (primary or parts or ["untyped"])[0]


def slug(subject, qtype):
    name = "%s__%s" % (str(subject or "unknown").lower()[:12], qtype or "untyped")
    # an item id becomes a filename and a runner-table cell, so keep it to safe characters
    return re.sub(r"[^a-z0-9_.]+", "_", name.lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--per-packet", type=int, default=6,
                    help="max questions per packet; a rater must hold them all in view at once")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    codebook = open(rc.pp(*RULEBOOK), encoding="utf-8").read()
    rows = list(csv.DictReader(open(rc.pp(*SHEET), encoding="utf-8")))

    groups = collections.OrderedDict()
    for r in rows:
        groups.setdefault(slug(r.get("subject"), primary_type(r.get("E1_question_type"))),
                          []).append(r)

    packets, stats = [], collections.Counter()
    for name, members in groups.items():
        # keep each packet's members adjacent in id order, so a reader can follow the comparison
        members.sort(key=lambda r: r.get("question_id") or "")
        chunks = [members[i:i + args.per_packet]
                  for i in range(0, len(members), args.per_packet)]
        for n, chunk in enumerate(chunks, 1):
            label = name if len(chunks) == 1 else "%s.part%d" % (name, n)
            stats["incomplete"] += sum(1 for r in chunk
                                       if r.get("review_status") == "source_incomplete")
            packets.append((label, {
                "group": name,
                "part": "%d of %d" % (n, len(chunks)),
                "codebook": codebook,
                "questions": [
                    dict([(k, r.get(k)) for k in CARRY]
                         + [("v1_traps", r.get("E5_traps")),
                            ("v1_needs_rejudge", r.get("E5_needs_rejudge")),
                            ("v1_reason", r.get("reason_v1_carried_over"))])
                    for r in chunk],
            }))

    print("%d questions -> %d groups -> %d packets (<=%d each)"
          % (len(rows), len(groups), len(packets), args.per_packet))
    print("   %d questions are source_incomplete: the rater must leave their traps empty"
          % stats["incomplete"])
    print("   codebook carried into every packet: %d chars" % len(codebook))
    wide = [(n, len(p["questions"])) for n, p in packets if len(p["questions"]) > args.per_packet]
    if wide:
        print("   OVERSIZED: %s" % wide)
    for name, p in packets[:6]:
        print("      %-40s %d questions" % (name, len(p["questions"])))
    if len(packets) > 6:
        print("      ... and %d more" % (len(packets) - 6))

    if args.dry_run:
        print("\n(dry run -- nothing written)")
        return 0

    out = rc.pp(*WORK)
    # the previous packets covered the showcase only; keep them until the new set is written
    if os.path.isdir(out):
        old = out + "_showcase_55"
        if os.path.isdir(old):
            shutil.rmtree(old)
        os.rename(out, old)
        print("\nmoved the previous %s aside to %s" % (os.path.join(*WORK), os.path.basename(old)))
    os.makedirs(out, exist_ok=True)
    for name, payload in packets:
        with open(os.path.join(out, "%s.runA.input.json" % name), "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=1)
    print("wrote %d packets to %s" % (len(packets), os.path.join(*WORK)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
