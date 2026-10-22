#!/usr/bin/env python3
"""Run the whole v2 paper pipeline for one year or booklet, end to end.

    python3 scripts/run_paper_pipeline.py --year 2024
    python3 scripts/run_paper_pipeline.py --year 2022 2023 2024 --dry-run
    python3 scripts/run_paper_pipeline.py --paper-id 2015_A --from export

ONE COMMAND, SO THE FLOW SURVIVES A HANDOVER
--------------------------------------------
Six things have to happen in order and four of them are scripts. Before this file they were six
remembered commands, which is a flow that works only for whoever remembered them.

    1  extract   scripts/extract_paper_v2.py     pick the source, cut question and figure crops
    2  subject   scripts/assign_subject.py       read the printed section headings
    3  READ      agent b3-question-reader        <- AGENT. Reads each question's IMAGE.
    4  figures   scripts/cut_agent_figures.py    cut the boxes the agent reported
    5  SOLVE     agent b6-blind-solver           <- AGENT. Answers with the printed answer withheld.
    6  export    scripts/export_paper_v2.py      CSV and paper-like HTML per booklet

THERE IS NO SEPARATE ANSWER-KEY STEP, and adding one back would be a mistake. The booklet prints its
own answer under every question, and THAT is the official answer this corpus uses. The separately
published NTA key PDFs were joined in until 2026-10-21 and were removed: NEET rotates the same
questions through ~24 booklet codes with the options reordered, so a key only means anything against
the code it was published for, and the 2016, 2017 and 2022 PDFs carry no code heading to join on.
Joined anyway, they contradicted the booklet's own printed answer on 71%, 74% and 78% of questions.
A wrong join is silent and looks authoritative, which is worse than having no second source at all.
The check that replaces it is step 5: an agent that solves the question having seen no answer.

Steps 3 and 5 are AGENTS and this script does not run them -- a script must never call a subagent
(scripts/CONVENTIONS.md rule 7). It prints the exact `run_step.py` commands instead and stops, which
is the same contract every other stage uses. Everything either side of them is automatic and
idempotent: re-running skips what is already done, so an interrupted run is resumed by repeating the
same command.

WHY THE AGENT STEPS ARE NOT OPTIONAL. The text layer cannot represent a stacked fraction -- its
numerator, bar and denominator are three unrelated objects on different rows. Measured on 2015
Code-A, 76 of 177 questions came out materially wrong from text alone, including every question with
a fraction. The crops are correct; the reading has to be done from them.
"""

import argparse
import glob
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

STEPS = ["extract", "subject", "read", "figures", "solve", "export"]
PY = sys.executable


def run(label, argv, dry):
    print("\n=== %s: %s" % (label, " ".join(os.path.basename(a) if a.endswith(".py") else a
                                            for a in argv[1:])))
    if dry:
        print("    (dry run)")
        return 0
    result = subprocess.run(argv, cwd=rc.pp())
    if result.returncode:
        print("    FAILED with exit code %d -- stopping, because every later step reads this "
              "one's output" % result.returncode)
    return result.returncode


def paper_ids(years):
    """Booklets in the corpus, optionally filtered to some years."""
    out = []
    for path in sorted(glob.glob(rc.pp("papers_v2", "papers", "*.json"))):
        stem = os.path.basename(path)[:-5]
        if not years or stem.split("_")[0] in years:
            out.append(stem)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", nargs="*", help="years to extract, e.g. 2022 2023 2024")
    ap.add_argument("--paper-id", help="skip extraction and work on one existing booklet")
    ap.add_argument("--from", dest="start", choices=STEPS, default="extract",
                    help="resume from a later step")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.year or args.paper_id):
        ap.error("pass --year or --paper-id")

    begin = STEPS.index(args.start)
    def wanted(step):
        return STEPS.index(step) >= begin

    if wanted("extract") and args.year:
        if run("1 extract", [PY, "scripts/extract_paper_v2.py", "--year"] + args.year + ["--apply"],
               args.dry_run):
            return 1

    if wanted("subject"):
        argv = [PY, "scripts/assign_subject.py", "--apply"]
        if args.paper_id:
            argv += ["--paper-id", args.paper_id]
        if run("2 subject", argv, args.dry_run):
            return 1


    ids = [args.paper_id] if args.paper_id else paper_ids(args.year)

    if wanted("read"):
        print("\n=== 3 READ each question from its image  [AGENT -- run these yourself]")
        print("    A script must never call a subagent (scripts/CONVENTIONS.md rule 7), so this")
        print("    step stops here. The text layer cannot represent a stacked fraction, so this")
        print("    read is what makes the corpus correct, not an optional extra.\n")
        print("      python3 scripts/run_step.py B3V --list     # one line per unread question")
        print("      # invoke b3-question-reader once per line, then:")
        print("      python3 scripts/run_step.py B3V --check")

    if wanted("figures"):
        argv = [PY, "scripts/cut_agent_figures.py", "--apply"]
        if args.paper_id:
            argv += ["--paper-id", args.paper_id]
        if run("4 figures from the agent's boxes", argv, args.dry_run):
            return 1

    if wanted("solve"):
        print("\n=== 5 SOLVE each question with the printed answer withheld  [AGENT -- run these yourself]")
        print("      python3 scripts/run_step.py B6V --list")
        print("      # invoke b6-blind-solver once per line, then:")
        print("      python3 scripts/run_step.py B6V --check")

    if wanted("export"):
        if run("6 export", [PY, "scripts/export_paper_v2.py", "--csv", "--html"], args.dry_run):
            return 1

    print("\n" + "=" * 72)
    print("booklets in the corpus: %s" % (", ".join(ids) if ids else "none"))
    print("  CSV   papers_v2/exports/csv/<booklet>.csv   (plus questions_v2_all.csv)")
    print("  HTML  papers_v2/exports/html/index.html")
    print("\nRe-running this command is safe: every script skips what is already done, so an")
    print("interrupted run is resumed by repeating it.")
    if args.dry_run:
        print("(dry run -- nothing was executed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
