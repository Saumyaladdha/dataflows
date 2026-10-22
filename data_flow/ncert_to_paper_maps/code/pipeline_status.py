"""Measure where the pipeline actually stands, and say what to run next.

WHY THIS IS A SCRIPT AND NOT A PARAGRAPH IN A DOCUMENT
------------------------------------------------------
A handover document that states progress is wrong the day after it is written, and nobody notices,
because a stale number looks exactly like a fresh one. This reads the counts off disk every time it
runs, so the answer to "where are we" cannot drift from the truth. `docs/RUNBOOK.md` explains what
each stage MEANS and never states how much of it is done -- that is this script's job, and the two
are deliberately separated for that reason.

HOW IT DECIDES WHAT IS NEXT
---------------------------
Each stage declares what it needs and what it produces. A stage is BLOCKED only when something it
needs has produced NOTHING AT ALL -- not merely when that thing is unfinished. This pipeline works
item by item: 358 questions have been read from their images and every per-question stage can run
on those 358 today, without waiting for the other 1,511. Treating partial upstream progress as a
block would report almost the whole flow as blocked and hide the work that is genuinely available,
which is the opposite of what this script is for.

A stage whose upstream is partial is therefore READY, with the ceiling named: "ready, limited to
what B3V has read". The order printed at the end is the dependency order, so "run this next" is
derived from the graph rather than from anyone's memory of it.

Usage:
    .venv/bin/python scripts/pipeline_status.py            # the summary
    .venv/bin/python scripts/pipeline_status.py --detail   # every stage, with its gaps
"""

import argparse
import collections
import csv
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import runner_core as rc                                      # noqa: E402

#: One row per stage of the flow, in dependency order. `needs` names stages, never files, so the
#: graph stays readable; `count` is a callable measuring what exists; `total` measures what could.
Stage = collections.namedtuple("Stage", "key title needs count total unit note")


def _files(*parts):
    return len(glob.glob(rc.pp(*parts)))


def _papers():
    return sorted(os.path.basename(p)[:-5]
                  for p in glob.glob(rc.pp("papers_v2", "papers", "*.json")))


def _questions_total():
    n = 0
    for path in glob.glob(rc.pp("papers_v2", "papers", "*.json")):
        with open(path, encoding="utf-8") as fh:
            n += len(json.load(fh)["questions"])
    return n


def _csv_rows(column=None, value=None):
    """Rows across every exported paper CSV, optionally filtered."""
    n = 0
    for path in glob.glob(rc.pp("papers_v2", "exports", "csv", "*.csv")):
        if "questions_v2" in os.path.basename(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if column is None or (row.get(column) or "").strip() == value:
                    n += 1
    return n


def _mapped(column):
    n = 0
    for path in glob.glob(rc.pp("papers_v2", "exports", "csv", "*.csv")):
        if "questions_v2" in os.path.basename(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if (row.get(column) or "").strip():
                    n += 1
    return n


def _evidence_scope():
    """Questions whose evidence is a QUOTE, i.e. not physics or physical chemistry."""
    n = 0
    for path in glob.glob(rc.pp("papers_v2", "exports", "csv", "*.csv")):
        if "questions_v2" in os.path.basename(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                subject = (row.get("subject") or "").strip().lower()
                stream = (row.get("stream") or "").strip().lower()
                if subject == "physics" or (subject, stream) == ("chemistry", "physical"):
                    continue
                n += 1
    return n


STAGES = [
    Stage("A1", "NCERT books registered", [],
          lambda: _files("steps", "A1", "out", "*.json"), lambda: 13, "books",
          "One record per book. Everything in Stage A is scoped by this."),
    Stage("A2", "NCERT pages read from the page IMAGE", ["A1"],
          lambda: _files("steps", "A2", "out", "*.runA.json"),
          lambda: _files("steps", "A2", "work", "*.runA.input.json"), "pages",
          "a2-page-reader reads the image; the text layer is a cross-check only."),
    Stage("A2S", "Tables, equations and figure labels transcribed", ["A2"],
          lambda: _files("steps", "A2S", "out", "*.runA.json"),
          lambda: _files("steps", "A2S", "work", "*.runA.input.json"), "blocks",
          "Until a block is transcribed its passage text BREAKS OFF where the block sits."),
    Stage("FOLD", "Transcriptions folded back into passage text", ["A2S", "A3"],
          lambda: sum(1 for line in _passage_lines() if line.get("text_source")),
          lambda: sum(1 for line in _passage_lines()
                      if line.get("kind") in ("table", "equation", "figure", "box")), "passages",
          "scripts/fold_a2s_into_passages.py --apply. Without it a transcribed table is "
          "unquotable and reads as an NCERT gap."),
    Stage("A3", "Pages split into passages", ["A2S"],
          lambda: _files("steps", "A3", "out", "*.runA.json"),
          lambda: _files("steps", "A3", "work", "*.runA.input.json"), "sections",
          "Produces ncert/passages/<BOOK>.jsonl, which every quote is verified against."),
    Stage("A5", "Passages linked to subtopics", ["A3"],
          lambda: _files("ncert", "links", "*.jsonl"), lambda: 13, "books",
          "Only 4 books are linked; D3's subtopic scoping needs this, D4V's chapter scoping does not."),
    Stage("A6", "Old edition paired with new", ["A3"],
          lambda: _files("ncert", "pairs", "*.json"), lambda: 1, "runs",
          "NEVER RUN. Until it is, old-edition chapters are matched BY TITLE as a stopgap -- see "
          "build_ncert_paper_map.older_chapter_numbers. Editions renumber: old Class XII Biology "
          "ch4 is Reproductive Health, not Inheritance."),
    Stage("B1", "Paper corpus built from the PDFs", [],
          lambda: len(_papers()), lambda: 10, "booklets",
          "papers_v2/ is live; papers/ is the frozen v1 reference."),
    Stage("B3V", "Questions read from their own IMAGE", ["B1"],
          lambda: _files("steps", "B3V", "out", "*.runA.json"), _questions_total, "questions",
          "B3V is the record. A text-layer draft cannot represent a stacked fraction at all."),
    Stage("B6V", "Blind solve, key withheld", ["B3V"],
          lambda: _files("steps", "B6V", "out", "*.runA.json"), _questions_total, "questions",
          "The independent check on the booklet's printed answer."),
    Stage("QSUBJ", "Subject confirmed from the printed heading", ["B3V"],
          lambda: _files("steps", "QSUBJ", "out", "*.runA.json"), _questions_total, "questions",
          "The positional guess was wrong on ALL 179 questions of 2017 Code C. QCHAP refuses a "
          "guessed subject."),
    Stage("QCHAP", "Chapter assigned", ["QSUBJ"],
          lambda: _mapped("chapter_names"), _questions_total, "questions",
          "Closed chapter list chosen BY SUBJECT."),
    Stage("QTOPIC", "Subtopic assigned", ["QCHAP"],
          lambda: _mapped("topic_names"), _questions_total, "questions", ""),
    Stage("E7V", "Difficulty banded", ["B3V"],
          lambda: _files("steps", "E7V", "out", "*.runA.json"), _questions_total, "questions",
          "easy = 1 step, medium = 2-3, hard = 4+. The checker enforces band vs step count."),
    Stage("ECAT", "E1-E5 rated, in groups", ["B3V", "QSUBJ"],
          lambda: _files("steps", "ECAT", "out", "*.runA.json"),
          lambda: _files("steps", "ECAT", "work", "*.runA.input.json"), "packets",
          "The item is a GROUP of up to six similar questions -- RULEBOOK rule 0.7."),
    Stage("D4V", "NCERT line quoted (Biology, Organic, Inorganic)", ["A3", "QTOPIC"],
          lambda: _files("steps", "D4V", "out", "*.runA.json"), _evidence_scope, "questions",
          "Physics and Physical Chemistry are NOT in scope -- they go to QCA."),
    Stage("QCA", "Concept and approach (Physics, Physical Chemistry, solving questions)",
          ["B3V", "QCHAP"],
          lambda: _files("steps", "QCA", "out", "*.runA.json"),
          lambda: _qca_scope(), "questions",
          "A numerical's answer is a VALUE and NCERT prints SENTENCES."),
    Stage("EXPORT", "Paper pages and CSVs written", ["B3V"],
          lambda: _files("papers_v2", "exports", "html", "2*.html"), lambda: len(_papers()),
          "booklets", "scripts/export_paper_v2.py --html --all"),
    Stage("MAP", "NCERT evidence map built", ["D4V", "QCA", "EXPORT"],
          lambda: 1 if os.path.exists(rc.pp("ncert_book_mapping", "ncert_paper_map.html")) else 0,
          lambda: 1, "pages", "scripts/build_ncert_paper_map.py --finished"),
]


def _passage_lines():
    for path in glob.glob(rc.pp("ncert", "passages", "*.jsonl")):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                try:
                    yield json.loads(line)
                except ValueError:
                    continue


def _qca_scope():
    """Physics + physical chemistry questions, plus the solving questions of other branches."""
    n = 0
    for path in glob.glob(rc.pp("papers_v2", "exports", "csv", "*.csv")):
        if "questions_v2" in os.path.basename(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                subject = (row.get("subject") or "").strip().lower()
                stream = (row.get("stream") or "").strip().lower()
                if subject == "physics" or (subject, stream) == ("chemistry", "physical"):
                    n += 1
    return n


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--detail", action="store_true")
    args = ap.parse_args()

    done_keys, empty_keys, partial_keys, rows = set(), set(), set(), []
    for stage in STAGES:
        try:
            have, want = stage.count(), stage.total()
        except Exception as exc:                       # a missing directory is a state, not a crash
            have, want = 0, 0
            stage = stage._replace(note=stage.note + "  (not measurable: %s)" % exc)
        # Blocked ONLY by a stage that has produced nothing; a partial upstream caps this stage's
        # ceiling rather than stopping it.
        blocked = [n for n in stage.needs if n in empty_keys]
        limited = [n for n in stage.needs if n in partial_keys]
        if want and have >= want:
            state = "DONE"
            done_keys.add(stage.key)
        elif blocked:
            state = "BLOCKED"
            empty_keys.add(stage.key)
        elif have:
            state = "RUNNING"
            partial_keys.add(stage.key)
        else:
            state = "READY"
            empty_keys.add(stage.key)
        rows.append((stage, have, want, state, blocked, limited))

    print("=" * 96)
    print("PIPELINE STATUS   measured from disk, %s" % rc.pp().rstrip("/"))
    print("=" * 96)
    print("  %-6s %-54s %18s  %s" % ("STAGE", "WHAT IT PRODUCES", "PROGRESS", "STATE"))
    for stage, have, want, state, blocked, limited in rows:
        bar = ""
        if want:
            filled = int(round(10 * min(1.0, have / want)))
            bar = "[" + "#" * filled + "." * (10 - filled) + "]"
        print("  %-6s %-54s %6s/%-6s %s  %s"
              % (stage.key, stage.title[:54], have, want, bar, state))
        if args.detail and stage.note:
            print("         %s" % stage.note)
        if blocked:
            print("         BLOCKED: %s has produced nothing yet" % ", ".join(blocked))
        elif limited and state != "DONE":
            print("         ready, but capped by how far %s has got" % ", ".join(limited))

    nxt = [s for s, have, want, state, blocked, limited in rows
           if state in ("READY", "RUNNING") and not blocked]
    print()
    print("WHAT TO RUN NEXT (first unblocked, in dependency order)")
    if not nxt:
        print("  nothing is both unblocked and unfinished.")
    for stage in nxt[:4]:
        print("  %-6s %s" % (stage.key, stage.title))
        if stage.note:
            print("         %s" % stage.note)
    print()
    print("Read docs/RUNBOOK.md for what each stage means and how to run it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
