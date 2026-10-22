#!/usr/bin/env python3
"""Write a human-inspectable snapshot of everything the pipeline currently holds, as plain CSVs.

    python3 scripts/export_snapshot.py              # writes exports/<today>/
    python3 scripts/export_snapshot.py --out DIR    # writes somewhere else

WHY THIS IS NOT `export_tables.py` (an important distinction, not a naming whim):

Spec Section 14/F5 reserves `export_tables.py` -> `data/` for the *gated release* export: it may
only run for a chapter whose review queue is empty, whose subtopic list and change-log rows are
approved, and which has a real sign-off row in `review/releases.csv`. CLAUDE.md states the rule
flatly -- "Never release a chapter; only export_tables.py does, after a sign-off row". That gate is
the whole point: released data carries an implicit promise that a person checked it.

This script makes no such promise and deliberately writes nowhere near `data/`. It is a read-only
snapshot of work-in-progress for inspection -- so the owner can open the real values in a
spreadsheet and judge them, instead of taking a progress report's word for it. Every row carries
its real `status`/flag context precisely so nothing here can be mistaken for approved output.
It reads the pipeline's files and writes CSVs; it never writes into the pipeline, never mutates a
record, and never closes a flag.

Tables written (one CSV each, plus a README.txt explaining them):
  questions.csv   one row per canonical question (merged duplicates folded in, not duplicated)
  merged_away.csv the non-canonical half of each C1 merge, so no question silently disappears
  passages.csv    every indexed NCERT passage (the unit D4 quotes from)
  subtopics.csv   every drafted subtopic, with how many passages actually link to it
  chapters.csv    every indexed chapter
  books.csv       registered books and their exact editions
  papers.csv      registered papers and keys
  flags.csv       every flag ever raised, with severity and current status
  run_log.csv     the full audit trail, copied verbatim
  coverage.csv    per-step counts: how many items reached pass / flagged / blocked
"""
import argparse
import collections
import csv
import datetime
import json
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402
from lib import io as lib_io  # noqa: E402


def _read_jsonl(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def _read_json(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_csv(out_dir, name, fieldnames, rows):
    path = os.path.join(out_dir, name)
    lib_io.ensure_parent(path)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return path, len(rows)


def _flat(value):
    """CSV cells hold one string. A list becomes ' | '-joined; a dict becomes compact JSON, so
    nothing is silently dropped from the snapshot just because it isn't scalar."""
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return " | ".join(_flat(v) for v in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


# ---------------------------------------------------------------------------
# questions
# ---------------------------------------------------------------------------

_Q_FIELDS = [
    "question_id", "exam", "year", "sitting", "paper_codes", "subject", "branch",
    "structure", "has_figure", "negative_words",
    "stem_en", "statements", "list_i", "list_ii",
    "option_1", "option_2", "option_3", "option_4",
    "official_answer", "answer_text", "answer_source", "status",
    "b6_answer", "b6_agrees_with_key", "b6_confidence",
    "d1_chapter_ids", "d2_subtopic_ids",
    "d4_link_type", "d4_supports_answer", "d4_quotes",
    "merged_from", "trust", "open_flags", "worst_flag_severity", "source_file",
]

_SEV_ORDER = {"blocker": 3, "high": 2, "normal": 1, "low": 0}


def _question_rows(flags_by_item):
    """One row per question record. A record whose `merged_into` is set is NOT canonical (C1
    folded it into another question); those go to merged_away.csv instead, so a reader counting
    rows in questions.csv gets the real unique-question count rather than a double count."""
    canonical, merged = [], []
    records_dir = rc.pp("papers", "records")
    if not os.path.isdir(records_dir):
        return canonical, merged

    for fn in sorted(os.listdir(records_dir)):
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        rec = _read_json(os.path.join(records_dir, fn))
        if not isinstance(rec, dict):
            continue
        qid = rec.get("question_id") or fn[: -len(".json")]
        opts = rec.get("options_en") or {}
        answer = rec.get("official_answer")
        # Statements arrive as [{"label","text"}, ...]; flatten to "A. text" so the CSV stays
        # readable in a spreadsheet instead of showing raw JSON for the commonest question shape.
        statements = rec.get("statements") or []
        if statements and isinstance(statements[0], dict):
            statements = [f"{s.get('label', '')}. {s.get('text', '')}".strip() for s in statements]

        item_flags = flags_by_item.get(qid, [])
        open_codes = [f["code"] for f in item_flags if f.get("status") == "open"]
        worst = ""
        if open_codes:
            worst = max((f.get("severity", "low") for f in item_flags if f.get("status") == "open"),
                        key=lambda s: _SEV_ORDER.get(s, 0))

        row = {
            "question_id": qid,
            "exam": _flat(rec.get("exam")),
            "year": _flat(rec.get("year")),
            "sitting": _flat(rec.get("sitting")),
            "paper_codes": _flat(rec.get("paper_codes")),
            "subject": _flat(rec.get("subject")),
            "branch": _flat(rec.get("branch")),
            "structure": _flat(rec.get("structure")),
            "has_figure": _flat(rec.get("has_figure")),
            "negative_words": _flat(rec.get("negative_words")),
            "stem_en": _flat(rec.get("stem_en")),
            "statements": _flat(statements),
            "list_i": _flat(rec.get("list_i")),
            "list_ii": _flat(rec.get("list_ii")),
            "option_1": _flat(opts.get("1")),
            "option_2": _flat(opts.get("2")),
            "option_3": _flat(opts.get("3")),
            "option_4": _flat(opts.get("4")),
            "official_answer": _flat(answer),
            # The answer's own TEXT, not just its number -- the number alone is useless when
            # reading a row by eye, and codes reorder options between booklets.
            "answer_text": _flat(opts.get(str(answer))) if answer else "",
            "answer_source": _flat(rec.get("answer_source")),
            "status": _flat(rec.get("status")),
            "b6_answer": _flat(rec.get("b6_answer")),
            "b6_agrees_with_key": _flat(rec.get("b6_agrees_with_key")),
            "b6_confidence": _flat(rec.get("b6_confidence")),
            "d1_chapter_ids": _flat(rec.get("d1_chapter_ids")),
            "d2_subtopic_ids": _flat(rec.get("d2_subtopic_ids")),
            "d4_link_type": _flat(rec.get("d4_link_type")),
            "d4_supports_answer": _flat(rec.get("d4_supports_answer")),
            "d4_quotes": _flat([e.get("exact_line") for e in (rec.get("d4_evidence") or [])
                                if isinstance(e, dict)]),
            "merged_from": _flat(rec.get("merged_from")),
            "trust": _flat(rec.get("trust")),
            "open_flags": _flat(open_codes),
            "worst_flag_severity": worst,
            "source_file": _flat(rec.get("source_file")),
        }
        if rec.get("merged_into"):
            row["merged_into"] = _flat(rec.get("merged_into"))
            merged.append(row)
        else:
            canonical.append(row)
    return canonical, merged


# ---------------------------------------------------------------------------
# ncert tables
# ---------------------------------------------------------------------------

def _passage_rows():
    rows = []
    d = rc.pp("ncert", "passages")
    if not os.path.isdir(d):
        return rows
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".jsonl"):
            continue
        for p in _read_jsonl(os.path.join(d, fn)):
            rows.append({
                "passage_id": _flat(p.get("passage_id")),
                "book_id": _flat(p.get("book_id")),
                "chapter_id": _flat(p.get("chapter_id")),
                "chapter_num": _flat(p.get("chapter_num")),
                "section_heading": _flat(p.get("section_heading")),
                "kind": _flat(p.get("kind")),
                "page_start": _flat(p.get("page_start")),
                "page_end": _flat(p.get("page_end")),
                "n_chars": len(p.get("text") or ""),
                "text": _flat(p.get("text")),
            })
    return rows


def _subtopic_rows():
    """Each drafted subtopic, plus how many passages A5 actually linked to it. The link count is
    the point: a subtopic with 0 links is a real defect (D3 can find no evidence for a question
    routed there, and will block), and that only shows up by joining the two files."""
    link_counts = collections.Counter()
    d_links = rc.pp("ncert", "links")
    if os.path.isdir(d_links):
        for fn in sorted(os.listdir(d_links)):
            if fn.endswith(".jsonl"):
                for l in _read_jsonl(os.path.join(d_links, fn)):
                    link_counts[l.get("subtopic_id")] += 1

    rows = []
    d = rc.pp("ncert", "subtopics")
    if not os.path.isdir(d):
        return rows
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".json"):
            continue
        data = _read_json(os.path.join(d, fn)) or {}
        chapter_id = data.get("chapter_id") or fn[: -len(".json")]
        for st in data.get("subtopics") or []:
            sid = st.get("subtopic_id")
            rows.append({
                "subtopic_id": _flat(sid),
                "chapter_id": _flat(chapter_id),
                "name": _flat(st.get("name")),
                "from_heading": _flat(st.get("from_heading")),
                "description": _flat(st.get("description")),
                "passages_listed_by_a4": len(st.get("passages") or []),
                "passages_linked_by_a5": link_counts.get(sid, 0),
                "approval": _flat(data.get("approval")),
            })
    return rows


def _chapter_rows():
    rows = []
    d = rc.pp("ncert", "chapters")
    if not os.path.isdir(d):
        return rows
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".json"):
            continue
        data = _read_json(os.path.join(d, fn))
        for ch in (data if isinstance(data, list) else [data]):
            if not isinstance(ch, dict):
                continue
            rows.append({
                "chapter_id": _flat(ch.get("chapter_id")),
                "title": _flat(ch.get("title")),
                "older_title": _flat(ch.get("older_title")),
                "n_headings": len(ch.get("headings") or []),
                "headings": _flat([f"{h.get('number', '')} {h.get('text', '')}".strip()
                                   for h in (ch.get("headings") or []) if isinstance(h, dict)]),
            })
    return rows


# ---------------------------------------------------------------------------
# flags, coverage
# ---------------------------------------------------------------------------

def _flag_rows_and_index():
    flags = _read_jsonl(rc.pp("flags", "flags.jsonl"))
    by_item = collections.defaultdict(list)
    rows = []
    for f in flags:
        by_item[f.get("item_id")].append(f)
        rows.append({
            "flag_id": _flat(f.get("flag_id")),
            "severity": _flat(f.get("severity")),
            "status": _flat(f.get("status")),
            "step": _flat(f.get("step")),
            "code": _flat(f.get("code")),
            "item_type": _flat(f.get("item_type")),
            "item_id": _flat(f.get("item_id")),
            "message": _flat(f.get("message")),
            "evidence": _flat(f.get("evidence")),
            "created_at": _flat(f.get("created_at")),
            "decision": _flat(f.get("decision")),
            "reviewer": _flat(f.get("reviewer")),
        })
    # Worst-first, so the rows that need attention sit at the top of the spreadsheet.
    rows.sort(key=lambda r: (-_SEV_ORDER.get(r["severity"], 0), r["step"], r["code"]))
    return rows, by_item


def _coverage_rows():
    """Per step: how many items actually reached each terminal status. This is the honest answer
    to "how much is done" -- it counts real status files on disk, not intentions."""
    steps_dir = rc.pp("steps")
    rows = []
    if not os.path.isdir(steps_dir):
        return rows
    for step in sorted(os.listdir(steps_dir)):
        status_dir = os.path.join(steps_dir, step, "status")
        if not os.path.isdir(status_dir):
            continue
        counts = collections.Counter()
        for fn in os.listdir(status_dir):
            if not fn.endswith(".json"):
                continue
            # Sidecar bookkeeping files (pending/last_block/_paper_stats) are not items.
            if ".pending." in fn or ".last_block." in fn or fn.startswith("_"):
                counts["pending_or_sidecar"] += 1
                continue
            data = _read_json(os.path.join(status_dir, fn)) or {}
            counts[data.get("status") or "unknown"] += 1
        n_out = 0
        out_dir = os.path.join(steps_dir, step, "out")
        if os.path.isdir(out_dir):
            n_out = len([f for f in os.listdir(out_dir) if f.endswith(".json")])
        rows.append({
            "step": step,
            "items_pass": counts.get("pass", 0),
            "items_flagged": counts.get("flagged", 0),
            "items_blocked": counts.get("blocked", 0),
            "items_skipped": counts.get("skipped", 0),
            "items_stale": counts.get("stale", 0),
            "pending_or_sidecar": counts.get("pending_or_sidecar", 0),
            "agent_output_files": n_out,
        })
    return rows


def _copy_csv_rows(rel_path):
    path = rc.pp(*rel_path.split("/"))
    if not os.path.exists(path):
        return [], []
    rows = lib_io.read_csv(path)
    fieldnames = list(rows[0].keys()) if rows else []
    return fieldnames, rows


_README = """SNAPSHOT OF WORK IN PROGRESS -- NOT RELEASED DATA
=================================================
Written by scripts/export_snapshot.py on {when}.

This is a read-only snapshot for inspection. It is NOT the released bank.
Nothing here has been through Stage F review, and no person has signed it off.
Spec Section 14/F5 reserves the released export (scripts/export_tables.py -> data/)
for chapters that have an approved subtopic list, an empty review queue, and a real
sign-off row in review/releases.csv. None of that has happened yet.

Read every row alongside its status and flag columns. A value with an open
high/blocker flag is the pipeline SAYING IT IS UNSURE, not an answer.

FILES
-----
questions.csv    One row per unique question. Duplicates that C1 merged across booklet
                 codes are folded in here (see paper_codes, merged_from), so the row
                 count is the real unique-question count.
merged_away.csv  The other half of each merge. Kept so no extracted question silently
                 vanishes from the snapshot; merged_into names its canonical twin.
passages.csv     Every indexed NCERT passage. This is the unit D4 quotes evidence from.
subtopics.csv    Every drafted subtopic. Compare passages_listed_by_a4 against
                 passages_linked_by_a5: a subtopic with 0 links is a real defect --
                 a question routed there has no evidence available and will block.
chapters.csv     Every indexed chapter and its heading tree.
books.csv        Registered books with the exact reprint text read off each cover.
papers.csv       Registered papers and answer keys.
flags.csv        Every flag ever raised, worst severity first.
run_log.csv      Full audit trail, copied verbatim: every step run, when, pass/fail.
coverage.csv     Per step, how many items reached pass / flagged / blocked. This is the
                 honest "how much is done" table -- counted from status files on disk.

COUNTS IN THIS SNAPSHOT
-----------------------
{counts}
"""


def main(argv=None):
    ap = argparse.ArgumentParser(description="Export an inspectable CSV snapshot (not a release).")
    ap.add_argument("--out", help="Output directory (default: exports/<YYYY-MM-DD>/).")
    args = ap.parse_args(argv)

    out_dir = args.out or rc.pp("exports", datetime.date.today().isoformat())
    rc.ensure_dir(out_dir)

    flag_rows, flags_by_item = _flag_rows_and_index()
    q_rows, merged_rows = _question_rows(flags_by_item)

    written = []
    written.append(_write_csv(out_dir, "questions.csv", _Q_FIELDS, q_rows))
    written.append(_write_csv(out_dir, "merged_away.csv", _Q_FIELDS + ["merged_into"], merged_rows))
    written.append(_write_csv(out_dir, "passages.csv",
                              ["passage_id", "book_id", "chapter_id", "chapter_num",
                               "section_heading", "kind", "page_start", "page_end", "n_chars",
                               "text"], _passage_rows()))
    written.append(_write_csv(out_dir, "subtopics.csv",
                              ["subtopic_id", "chapter_id", "name", "from_heading", "description",
                               "passages_listed_by_a4", "passages_linked_by_a5", "approval"],
                              _subtopic_rows()))
    written.append(_write_csv(out_dir, "chapters.csv",
                              ["chapter_id", "title", "older_title", "n_headings", "headings"],
                              _chapter_rows()))
    written.append(_write_csv(out_dir, "flags.csv",
                              ["flag_id", "severity", "status", "step", "code", "item_type",
                               "item_id", "message", "evidence", "created_at", "decision",
                               "reviewer"], flag_rows))
    written.append(_write_csv(out_dir, "coverage.csv",
                              ["step", "items_pass", "items_flagged", "items_blocked",
                               "items_skipped", "items_stale", "pending_or_sidecar",
                               "agent_output_files"], _coverage_rows()))

    for name, rel in (("books.csv", "register/books.csv"),
                      ("papers.csv", "register/papers.csv"),
                      ("run_log.csv", "run_log.csv")):
        fieldnames, rows = _copy_csv_rows(rel)
        if fieldnames:
            written.append(_write_csv(out_dir, name, fieldnames, rows))
        else:
            written.append((os.path.join(out_dir, name), 0))

    counts = "\n".join(f"  {os.path.basename(p):<18} {n:>6} rows" for p, n in written)
    lib_io.atomic_write_text(
        os.path.join(out_dir, "README.txt"),
        _README.format(when=rc.now_iso(), counts=counts),
    )

    print(f"Snapshot written to {out_dir}\n")
    for p, n in written:
        print(f"  {os.path.basename(p):<18} {n:>6} rows")
    print("\nREADME.txt explains each file. This is work in progress, not released data.")


if __name__ == "__main__":
    main()
