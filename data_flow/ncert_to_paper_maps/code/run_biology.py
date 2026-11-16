#!/usr/bin/env python3
"""The whole Biology NCERT-first flow for ONE paper: what is done, what to run next.

    python3 code/run_biology.py --paper 2024_S1              # status only
    python3 code/run_biology.py --paper 2024_S1 --build      # + build the next step's packets
    python3 code/run_biology.py --paper 2024_S1 --write      # + run the writers when ready

BIOLOGY ONLY. Questions are selected by `classification.subject == "Biology"`. Physics and
Chemistry are counted and skipped: their NCERT corpus is not extracted, so the steps that map
a question to a printed line cannot run for them, and nothing here touches their records.

THE ORDER IS ENFORCED BY THE DATA, NOT BY MEMORY
------------------------------------------------
Each step's packets are built from the step before it, so D2 cannot be built before D1 has
answered and D12 cannot be built before D4 has supplied the words. Run this after each batch
of agents; it prints the next thing to do and nothing else.

    D1   which NCERT chapter          d1-chapter-picker
    D2   which printed subtopic       d2-subtopic-picker
    D4   the exact NCERT lines        d4-evidence-quoter
    D5   the older edition's line     d5-older-line-finder
    D12  the student-facing solution  d12-ncert-solution-writer
    D13  the picture, if any          d13-solution-diagram

WHY IT PRINTS INSTRUCTIONS INSTEAD OF CALLING THE AGENTS
--------------------------------------------------------
These agents run as Claude Code subagents, which only the orchestrating session can start; the
API path answers "Your credit balance is too low". So this prints the exact dispatch line for
each question and the orchestrator sends them, in batches, in parallel.
"""

import argparse
import collections
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(HERE))
PAPERS = os.path.join(REPO, "data_flow", "paper_extraction", "data")
PAPER_CODE = os.path.join(REPO, "data_flow", "paper_extraction", "code")

CHAIN = [
    ("D1",  "d1-chapter-picker",         "which NCERT chapter",
     ["python3", "code/build_ncert_map_packets.py"]),
    ("D2",  "d2-subtopic-picker",        "which printed subtopic",
     ["python3", "code/build_d2_packets.py"]),
    ("D4",  "d4-evidence-quoter",        "the exact NCERT lines",
     ["python3", "code/build_d4_packets.py"]),
    ("D5",  "d5-older-line-finder",      "the older edition's line",
     ["python3", "code/build_d5_packets.py"]),
    ("D12", "d12-ncert-solution-writer", "the student-facing solution",
     ["python3", "code/build_d12_packets.py"]),
    ("D13", "d13-solution-diagram",      "the picture, if any",
     ["python3", "code/build_d13_packets.py"]),
]

#: Run in this order once every step above has answered. Each takes --paper and --apply.
WRITERS = [
    ("join_ncert_map_into_export.py", "NCERT mapping + syllabus label into questions.json"),
    ("join_ncert_card_into_html.py",  "the evidence card and page render into the HTML"),
    ("join_ncert_first_into_export.py", "the NCERT-first solution into questions.json"),
    ("make_biology_ncert_page.py",    "rewrite the Biology cards in question_paper.html"),
    ("make_biology_ncert_md.py",      "rewrite the Biology sections of question_paper.md"),
]


def biology_qids(paper):
    year = paper.split("_")[0]
    path = os.path.join(PAPERS, year, paper, "questions.json")
    doc = json.load(open(path, encoding="utf-8"))
    bio, other = [], 0
    for q in doc["questions"]:
        if ((q.get("classification") or {}).get("subject") or "") == "Biology":
            bio.append(q["question_id"].split("__")[-1])
        else:
            other += 1
    return sorted(bio), other


def done(paper, step, qid):
    return os.path.exists(os.path.join(HERE, "steps", step, "out",
                                       "%s.%s.runA.json" % (paper, qid)))


def has_packet(paper, step, qid):
    return os.path.exists(os.path.join(HERE, "steps", step, "work",
                                       "%s.%s.runA.input.json" % (paper, qid)))


def build(cmd, paper, qids, step):
    full = list(cmd) + ["--paper", paper]
    if step in ("D12", "D13"):                      # these take an explicit question list
        full += ["--questions", ",".join(qids)]
    full += ["--apply"]
    r = subprocess.run(full, cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tail = [l for l in (r.stdout or b"").decode("utf-8", "replace").strip().splitlines()
            if l.strip()][-1:]
    print("      build %-4s -> %s" % (step, tail[0] if tail
                                      else (r.stderr or b"").decode("utf-8", "replace")[:100]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--build", action="store_true", help="build the next step's packets")
    ap.add_argument("--write", action="store_true", help="run the writers once every step is in")
    ap.add_argument("--limit", type=int, default=40,
                    help="how many dispatch lines to print at once (default 40)")
    a = ap.parse_args()

    qids, other = biology_qids(a.paper)
    print("Biology NCERT-first . %s . %d biology question(s), %d left alone (not Biology)\n"
          % (a.paper, len(qids), other))
    print("%-5s %-28s %s" % ("step", "what it answers", "done"))

    first_open = None
    for step, agent, what, cmd in CHAIN:
        fin = [q for q in qids if done(a.paper, step, q)]
        flag = "" if len(fin) == len(qids) else "   <-- next"
        print("%-5s %-28s %d/%d%s" % (step, what, len(fin), len(qids), flag))
        if first_open is None and len(fin) < len(qids):
            first_open = (step, agent, cmd, [q for q in qids if q not in fin])

    if first_open is None:
        print("\nevery agent step is in. The writers, in order:")
        for name, what in WRITERS:
            print("   %-34s %s" % (name, what))
        if not a.write:
            print("\n(nothing run -- pass --write)")
            return 0
        for name, _ in WRITERS:
            extra = ["--into-paper"] if name == "make_biology_ncert_page.py" else []
            r = subprocess.run(["python3", os.path.join(PAPER_CODE, name),
                                "--paper", a.paper] + extra + ["--apply"],
                               cwd=os.path.dirname(PAPER_CODE),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = (r.stdout or b"").decode("utf-8", "replace").strip().splitlines()
            print("\n== %s ==" % name)
            for line in out[-8:]:
                print("   " + line)
            if r.returncode != 0:
                print("   FAILED: %s"
                      % (r.stderr or b"").decode("utf-8", "replace").strip()[:300])
                return 1
        print("\ndone: questions.json, question_paper.html and question_paper.md all carry "
              "the NCERT-first Biology solutions.")
        return 0

    step, agent, cmd, todo = first_open
    print("\nnext: %s (%s) for %d question(s)" % (step, agent, len(todo)))
    if a.build:
        build(cmd, a.paper, todo, step)
    missing = [q for q in todo if not has_packet(a.paper, step, q)]
    if missing:
        print("   packets missing for %d question(s) -- re-run with --build" % len(missing))
        return 1

    print("\n   dispatch one subagent per line (send them in parallel, in batches):")
    for q in todo[:a.limit]:
        print("     Use the %s subagent. Input: steps/%s/work/%s.%s.runA.input.json  "
              "Output: steps/%s/out/%s.%s.runA.json"
              % (agent, step, a.paper, q, step, a.paper, q))
    if len(todo) > a.limit:
        print("   ... and %d more; re-run this command after these finish."
              % (len(todo) - a.limit))
    return 0


if __name__ == "__main__":
    sys.exit(main())
