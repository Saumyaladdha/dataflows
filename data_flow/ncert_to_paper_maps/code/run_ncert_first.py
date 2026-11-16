#!/usr/bin/env python3
"""The NCERT-first chain for Biology: say what is done, build the next step, name what to run.

THE ORDER THIS ENFORCES
-----------------------
    D1   which NCERT chapter          (no exam-taxonomy hint in the packet)
    D2   which printed subtopic        from NCERT's own section headings
    D4   the exact lines + passages    these become the solution's vocabulary
    D5   the older edition's line      reported separately, never inside the solution
    D12  the student-facing solution   written in NCERT's words

Each step's packet is built from the step before it, so the order is not a convention anyone
has to remember -- D2 cannot be built before D1 has answered, and D12 cannot be built before D4
has supplied the words. Running this after each dispatch prints exactly what is still missing.

WHY IT DOES NOT DISPATCH THE AGENTS ITSELF
------------------------------------------
`run_step_api.py` would, but the API path answers "Your credit balance is too low", so agents go
through Claude Code subagents, which only the orchestrator can start. This prints the exact
instruction line for each one instead, in the form the RUNBOOK specifies.

Usage:
    python3 code/run_ncert_first.py --paper 2024_S1 --questions q101,q106,q107,q153,q157
    python3 code/run_ncert_first.py --paper 2024_S1 --questions ... --build   # build next packets
"""

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAIN = [
    ("D1",  "d1-chapter-picker",         "which NCERT chapter"),
    ("D2",  "d2-subtopic-picker",        "which printed subtopic"),
    ("D4",  "d4-evidence-quoter",        "the exact NCERT lines"),
    ("D5",  "d5-older-line-finder",      "the older edition's line"),
    ("D12", "d12-ncert-solution-writer", "the student-facing solution"),
]


def done(paper, step, qid):
    return os.path.exists(os.path.join(HERE, "steps", step, "out",
                                       "%s.%s.runA.json" % (paper, qid)))


def has_packet(paper, step, qid):
    return os.path.exists(os.path.join(HERE, "steps", step, "work",
                                       "%s.%s.runA.input.json" % (paper, qid)))


def build(step, paper, qids):
    """Build the packets for one step, using that step's own builder."""
    cmd = {
        "D1":  ["python3", "code/build_ncert_map_packets.py", "--paper", paper, "--apply"],
        "D2":  ["python3", "code/build_d2_packets.py", "--paper", paper, "--apply"],
        "D4":  ["python3", "code/build_d4_packets.py", "--paper", paper, "--apply"],
        "D5":  ["python3", "code/build_d5_packets.py", "--paper", paper, "--apply"],
        "D12": ["python3", "code/build_d12_packets.py", "--paper", paper,
                "--questions", ",".join(qids), "--apply"],
    }.get(step)
    if not cmd:
        return
    r = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True)
    tail = [l for l in (r.stdout or "").strip().splitlines() if l.strip()][-1:]
    print("      build %-4s -> %s" % (step, tail[0] if tail else (r.stderr or "").strip()[:90]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--questions", required=True)
    ap.add_argument("--build", action="store_true",
                    help="build the packets for the first step that is not finished")
    a = ap.parse_args()
    qids = [x.strip() for x in a.questions.split(",") if x.strip()]

    print("NCERT-first chain · %s · %d question(s)\n" % (a.paper, len(qids)))
    print("%-5s %-28s %s" % ("step", "what it answers", "done"))
    first_open = None
    for step, agent, what in CHAIN:
        fin = [q for q in qids if done(a.paper, step, q)]
        print("%-5s %-28s %d/%d%s" % (step, what, len(fin), len(qids),
                                      "" if len(fin) == len(qids) else "   <-- next"))
        if first_open is None and len(fin) < len(qids):
            first_open = (step, agent, [q for q in qids if q not in fin])

    if first_open is None:
        print("\nevery step finished. Render with:")
        print("  python3 ../paper_extraction/code/build_ncert_first_page.py "
              "--paper %s --questions %s --apply" % (a.paper, ",".join(qids)))
        return 0

    step, agent, todo = first_open
    print("\nnext: %s (%s) for %s" % (step, agent, " ".join(todo)))
    if a.build:
        build(step, a.paper, qids)
    missing = [q for q in todo if not has_packet(a.paper, step, q)]
    if missing:
        print("   packets missing for %s -- re-run with --build" % " ".join(missing))
        return 1
    print("\n   dispatch one subagent per line:")
    for q in todo:
        print("     Use the %s subagent. Input: steps/%s/work/%s.%s.runA.input.json  "
              "Output: steps/%s/out/%s.%s.runA.json" % (agent, step, a.paper, q, step, a.paper, q))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
