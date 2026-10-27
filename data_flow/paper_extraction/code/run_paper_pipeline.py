#!/usr/bin/env python3
"""Run the whole v2 paper pipeline for one year or booklet, end to end.

    python3 code/run_paper_pipeline.py --year 2024
    python3 code/run_paper_pipeline.py --year 2022 2023 2024 --dry-run
    python3 code/run_paper_pipeline.py --paper-id 2015_A --from figures

ONE COMMAND, SO THE FLOW SURVIVES A HANDOVER
--------------------------------------------
The whole flow, in order. Before this file it was remembered commands, which is a flow that works
only for whoever remembered them. To run it with NO manual steps, use the saved workflow
`neet-paper-pipeline` (.claude/workflows/), which runs the scripts and dispatches every agent below.

    1  extract   code/extract_paper_v2.py      source, question crops, SOLUTION crops, figure crops
    2  subject   code/assign_subject.py        read the printed section headings
    3  READ      agent b3-question-reader  B3V <- every question read from its IMAGE
               agent b3s-solution-reader B3S <- every printed solution, figures boxed at their steps
    4  figures   code/cut_agent_figures.py     cut every figure the agents boxed (question, options,
                                               solution steps), with exact page boxes recorded
    5  vector    code/vector_figures.py        each figure lifted from the PDF as EXACT vector SVG
    6  AGENTS    b6-blind-solver   B6V  solve, answer withheld
               q-subject-confirmer QSUBJ  -> q-chapter-picker QCHAP -> q-subtopic-picker QTOPIC
               (taxonomy gaps: collect_taxonomy_gaps.py, extend_taxonomy.py,
                requeue_taxonomy_gaps.py, then QTOPIC again)
               e7-difficulty-rater E7V
               figc-structure-reader FIGC  chemistry drawings -> SMILES cards (RDKit + OPSIN)
               figp-figure-redrawer  FIGP  physics figures -> checked primitive specs
    7  cards     code/render_figure_cards.py   draw every CHECKED card beside its printed figure
    8  upload    code/upload_paper_assets.py   every image and SVG -> CDN link
    9  export    code/export_paper_v2.py       data/<year>/<paper_code>/ (LaTeX gate first)

EVERY RUN IS FRESH. Step 1 deletes what the previous run's SCRIPTS produced for each booklet it
re-extracts -- its JSON, crops, figures, solution crops and exports -- before cutting new ones, and
step 7 replaces the export folders and each data/<year>/<paper_code>/ folder whole. Nothing from an
earlier run survives beside the new output. Agent answers are kept, because a read costs a dispatch
and re-extracting does not change the question it read; `--clear-agent-reads` removes them too.
`--keep-previous` turns the clearing off. Resuming with `--from figures` (or any later step) never
clears: it continues the same run, after the agents have answered.

EVERY IMAGE IS A CDN LINK. Step 5 needs ARIVIHAN_TOKEN / ARIVIHAN_USER_ID (see lib/cdn.py), and the
pipeline STOPS there without them rather than exporting pages that point at local files.

THERE IS NO SEPARATE ANSWER-KEY STEP, and adding one back would be a mistake. The booklet prints its
own answer under every question, and THAT is the official answer this corpus uses. The separately
published NTA key PDFs were joined in until 2026-10-21 and were removed: NEET rotates the same
questions through ~24 booklet codes with the options reordered, so a key only means anything against
the code it was published for, and the 2016, 2017 and 2022 PDFs carry no code heading to join on.
Joined anyway, they contradicted the booklet's own printed answer on 71%, 74% and 78% of questions.
A wrong join is silent and looks authoritative, which is worse than having no second source at all.
The check that replaces it is step 5: an agent that solves the question having seen no answer.

Steps 3 and 5 are AGENTS and this script does not run them -- a script must never call a subagent
(_shared/code/CONVENTIONS.md rule 7). It prints the exact `run_step.py` commands instead and carries on, which
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

STEPS = ["extract", "subject", "read", "figures", "vector", "solve", "cards", "upload", "export"]
PY = sys.executable
HERE = os.path.dirname(os.path.abspath(__file__))


def script(name):
    """The absolute path of one of this folder's scripts. They used to be spelled `scripts/<name>`,
    relative to the project root, and the folder is now `code/` -- so the first step of every run
    failed to start."""
    return os.path.join(HERE, name)


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
    for path in sorted(glob.glob(rc.pp(*rc.corpus(), "papers", "*.json"))):
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
    ap.add_argument("--keep-previous", action="store_true",
                    help="do not clear a booklet's earlier output before re-extracting it")
    ap.add_argument("--clear-agent-reads", action="store_true",
                    help="also delete each re-extracted booklet's agent answers")
    args = ap.parse_args()
    if not (args.year or args.paper_id):
        ap.error("pass --year or --paper-id")

    begin = STEPS.index(args.start)
    def wanted(step):
        return STEPS.index(step) >= begin

    if wanted("extract") and args.year:
        argv = [PY, script("extract_paper_v2.py"), "--year"] + args.year + ["--apply"]
        if args.keep_previous:
            argv.append("--keep-previous")
        if args.clear_agent_reads:
            argv.append("--clear-agent-reads")
        if run("1 extract (fresh: clears each booklet's previous output first)"
               if not args.keep_previous else "1 extract", argv, args.dry_run):
            return 1

    if wanted("subject"):
        argv = [PY, script("assign_subject.py"), "--apply"]
        if args.paper_id:
            argv += ["--paper-id", args.paper_id]
        if run("2 subject", argv, args.dry_run):
            return 1


    ids = [args.paper_id] if args.paper_id else paper_ids(args.year)

    if wanted("read"):
        print("\n=== 3 READ each question from its image  [AGENT -- run these yourself]")
        print("    A script must never call a subagent (_shared/code/CONVENTIONS.md rule 7), so this")
        print("    step stops here. The text layer cannot represent a stacked fraction, so this")
        print("    read is what makes the corpus correct, not an optional extra.\n")
        print("      python3 code/run_step.py B3V --list     # one line per unread question")
        print("      # invoke b3-question-reader once per line, then:")
        print("      python3 code/run_step.py B3V --check")
        print("\n    ...then each printed worked solution, from its own crop (needs B3V first):\n")
        print("      python3 code/run_step.py B3S --list     # one line per unread solution")
        print("      # invoke b3s-solution-reader once per line, then:")
        print("      python3 code/run_step.py B3S --check")

    if wanted("figures"):
        argv = [PY, script("cut_agent_figures.py"), "--apply"]
        if args.paper_id:
            argv += ["--paper-id", args.paper_id]
        if run("4 figures from the agent's boxes", argv, args.dry_run):
            return 1

    if wanted("vector"):
        for paper_id in ids:
            if run("5 exact vector copy of every figure (%s)" % paper_id,
                   [PY, script("vector_figures.py"), "--paper-id", paper_id, "--apply"], args.dry_run):
                return 1

    if wanted("upload"):
        argv = [PY, script("upload_paper_assets.py")]
        if args.paper_id:
            argv += ["--paper-id", args.paper_id]
        if args.dry_run:
            argv.append("--dry-run")
        # Run even under --dry-run: upload_paper_assets has its own dry run, which lists what would go up.
        if run("8 upload every image and SVG to the CDN", argv, False):
            return 1

    if wanted("solve"):
        print("\n=== 6 AGENT STEPS, in this order  [the neet-paper-pipeline workflow dispatches them]")
        for line in ("B6V, QSUBJ, FIGC, FIGP   (independent of each other -- run together)",
                     "QCHAP                    (needs QSUBJ)",
                     "QTOPIC                   (needs QCHAP)",
                     "  then: collect_taxonomy_gaps.py --apply; extend_taxonomy.py --apply;",
                     "        requeue_taxonomy_gaps.py --paper-id <id> --apply; QTOPIC again",
                     "E7V                      (needs QSUBJ)"):
            print("      " + line)
        print("      each: python3 code/run_step.py <STEP> --list | one agent per line | --check")

    if wanted("cards"):
        for paper_id in ids:
            if run("7 draw every checked figure card (%s)" % paper_id,
                   [PY, script("render_figure_cards.py"), "--paper-id", paper_id, "--apply"],
                   args.dry_run):
                return 1

    if wanted("export"):
        if run("9 export", [PY, script("export_paper_v2.py"), "--csv", "--html", "--json", "--data"],
               args.dry_run):
            return 1

    corpus = "/".join(rc.corpus())
    print("\n" + "=" * 72)
    print("booklets in the corpus: %s" % (", ".join(ids) if ids else "none"))
    print("  DATA  data/<year>/<paper_code>/questions.json + question_paper.html   <- the deliverable")
    print("  CSV   %s/exports/csv/<booklet>.csv   (plus questions_v2_all.csv)" % corpus)
    print("  JSON  %s/exports/json/questions_v2_all.json" % corpus)
    print("  CDN   every image URL is on its question in %s/papers/<booklet>.json" % corpus)
    print("  HTML  %s/exports/html/index.html" % corpus)
    print("\nRe-running this command is safe: every script skips what is already done, so an")
    print("interrupted run is resumed by repeating it.")
    if args.dry_run:
        print("(dry run -- nothing was executed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
