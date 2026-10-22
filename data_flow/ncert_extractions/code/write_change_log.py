#!/usr/bin/env python3
"""A9 - write the change log for one chapter (spec docs/SPEC.md Section 9/A9, 6.4,
schemas/A9.json).

Pure SCRIPT step, no agent (spec 9/A9, config/steps.yaml A9: agent "script", input_fields []).
Procedure: one row per non-identical pair, using A8's RESOLVED judgement; every A6 'removed'
passage -> a deleted_topics.csv row. A8 itself is an AGENT step this build does not include --
in the real pipeline A9 runs after A8 has judged every non-identical pair from A7. Here A8's
output is supplied as an input file (--judgements): a JSON array of A8-shaped objects
(schemas/A8.json's fields, with change_type already resolved to one of
fact_changed/fact_removed/fact_added/wording_only -- never 'unsure', per schemas/A9.json's note
that an unresolved 'unsure' must not reach this log).

ncert/change_log.csv and ncert/deleted_topics.csv are SHARED, project-wide files (spec 5.8),
not one per chapter -- unlike ncert/pairs/<CHAPTER>.json and ncert/diffs/<CHAPTER>.jsonl. So this
script only ever replaces the rows that belong to --chapter-id on each run, leaving every other
chapter's previously-written rows untouched, and reuses each pair's existing change_id (never
minting a new one for a pair already logged) so reruns are idempotent and register/counters.json
is never burned through on a no-op rerun.

Per scripts/CONVENTIONS.md, run_step.py --auto invokes every script-only step as
`python3 scripts/<script>.py --chapter-id <ID>` with no other required flags. A8 (not built in
this project yet -- it is an AGENT step) has no fixed per-chapter aggregate output path in the
spec, so this script defines one as its own default input: steps/A8/out/<CHAPTER_ID>.judgements.json
-- a JSON array of A8-shaped objects, one per non-identical A7 pair, with change_type already
resolved. --judgements overrides this default (useful for testing against a hand-built fixture
file living elsewhere). If a chapter has non-identical diffs but no judgements file at all (at
the default path or the override), that is treated as a genuine missing-upstream-input failure
(non-zero exit), per CONVENTIONS.md rule 2 -- not silently skipped.

Usage:
    python3 scripts/write_change_log.py --chapter-id BIO12-CH06
    python3 scripts/write_change_log.py --chapter-id BIO12-CH06 --judgements <path>
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import ids
from lib import io as lib_io

CHANGE_LOG_FIELDS = [
    "change_id", "chapter_id", "subtopic_id", "old_passage_id", "new_passage_id",
    "change_type", "old_fact", "new_fact", "could_flip_an_answer",
    "old_text", "new_text", "affected_questions", "approval",
]
DELETED_TOPICS_FIELDS = ["old_passage_id", "chapter_id", "old_pages", "heading", "subtopic_hint"]

RESOLVED_CHANGE_TYPES = {"fact_changed", "fact_removed", "fact_added", "wording_only"}


def _change_log_path(override=None):
    return override or lib_io.project_path("ncert", "change_log.csv")


def _deleted_topics_path(override=None):
    return override or lib_io.project_path("ncert", "deleted_topics.csv")


def load_pairs(chapter_id, pairs_path=None):
    path = pairs_path or lib_io.project_path("ncert", "pairs", f"{chapter_id}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"A9 needs A6's output first: {path} does not exist")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_diffs(chapter_id, diffs_path=None):
    path = diffs_path or lib_io.project_path("ncert", "diffs", f"{chapter_id}.jsonl")
    return list(lib_io.read_jsonl(path))


def default_judgements_path(chapter_id):
    """This script's own convention for A8's per-chapter aggregate (see module docstring):
    steps/A8/out/<CHAPTER_ID>.judgements.json."""
    return lib_io.project_path("steps", "A8", "out", f"{chapter_id}.judgements.json")


def load_judgements(path):
    """--judgements file (or its default path): JSON array of A8-shaped objects
    (schemas/A8.json), keyed here by (old_passage_id, new_passage_id). Rejects any entry whose
    change_type is 'unsure' or missing -- A9 must only ever receive A8 results already resolved
    by A8's own fallback chain (retry/second-run/adjudication), per schemas/A9.json's change_type
    note. A missing file is treated as "no judgements supplied" (empty dict); the caller decides
    whether that's actually fine (no diffs needing one) or a genuine missing-input failure."""
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        rows = json.load(f)
    by_pair = {}
    for row in rows:
        key = (row["old_passage_id"], row["new_passage_id"])
        change_type = row.get("change_type")
        if change_type not in RESOLVED_CHANGE_TYPES:
            raise ValueError(
                f"A9: judgement for pair {key} has change_type={change_type!r}, not one of "
                f"{sorted(RESOLVED_CHANGE_TYPES)}. A8's 'unsure' must be resolved (retry / second "
                f"run / adjudicator) before it can reach the change log -- this script will not "
                f"guess."
            )
        by_pair[key] = row
    return by_pair


def load_links(book_id, links_dir=None):
    path = os.path.join(links_dir or lib_io.project_path("ncert", "links"), f"{book_id}.jsonl")
    return {row["passage_id"]: row.get("subtopic_id", "none") for row in lib_io.read_jsonl(path)}


def load_passages(book_id, passages_dir=None):
    path = os.path.join(passages_dir or lib_io.project_path("ncert", "passages"), f"{book_id}.jsonl")
    return {p["passage_id"]: p for p in lib_io.read_jsonl(path)}


def _page_range(passage):
    ps, pe = passage.get("page_start"), passage.get("page_end")
    if ps is None:
        return ""
    return str(ps) if ps == pe else f"{ps}-{pe}"


def build_change_log_rows(chapter_id, pairs, diffs, judgements, old_links, new_links, existing_change_ids):
    """One row per non-identical pair in `diffs`, in A7's order. subtopic_id prefers the new
    (latest-edition) passage's own link, since subtopics are defined on the latest edition only
    (spec 3 'Subtopic'); falls back to the old passage's link, then 'none'. Reuses an existing
    change_id for a pair already in the log (keyed by old_passage_id+new_passage_id) so reruns
    never mint duplicate CL- ids for the same change."""
    rows = []
    for diff_entry in diffs:
        old_id, new_id = diff_entry["pair"]
        key = (old_id, new_id)
        if key not in judgements:
            raise KeyError(
                f"A9: no A8 judgement supplied for non-identical pair {key} in chapter {chapter_id} "
                f"-- every diff from A7 needs a resolved A8 result before A9 can log it."
            )
        j = judgements[key]
        subtopic_id = new_links.get(new_id) or old_links.get(old_id) or "none"
        pair_entry = next(
            (e for e in pairs if e.get("old_passage_id") == old_id and e.get("new_passage_id") == new_id
             and e.get("result") == "pair"),
            None,
        )
        if pair_entry is None:
            raise KeyError(f"A9: pair {key} appears in A7's diffs but not as a 'pair' result in A6's output")

        change_id = existing_change_ids.get(key) or ids.next_change_id()
        rows.append({
            "change_id": change_id,
            "chapter_id": chapter_id,
            "subtopic_id": subtopic_id,
            "old_passage_id": old_id,
            "new_passage_id": new_id,
            "change_type": j["change_type"],
            "old_fact": j.get("old_fact", ""),
            "new_fact": j.get("new_fact", ""),
            "could_flip_an_answer": bool(j.get("could_flip_an_answer", False)),
            "old_text": "", "new_text": "",  # filled in by the caller, which has the passage text
            "affected_questions": [],  # spec 9/A9: empty at write time, filled after Stage D
            "approval": "pending",
        })
    return rows


def build_deleted_topics_rows(chapter_id, pairs, old_passages, old_links):
    """One row per A6 'removed' passage (genuinely removed, not merely non-identical -- spec 9/A9:
    'every removed passage from A6's output ... becomes a row in deleted_topics.csv')."""
    rows = []
    for entry in pairs:
        if entry.get("result") != "removed":
            continue
        old_id = entry["old_passage_id"]
        passage = old_passages.get(old_id)
        if passage is None:
            raise KeyError(f"A9: removed passage {old_id!r} not found in old-edition passages")
        subtopic_id = old_links.get(old_id, "none")
        subtopic_hint = passage.get("section_heading") or subtopic_id
        rows.append({
            "old_passage_id": old_id,
            "chapter_id": chapter_id,
            "old_pages": _page_range(passage),
            "heading": passage.get("section_heading", ""),
            "subtopic_hint": subtopic_hint,
        })
    return rows


def _serialise_row(row, fieldnames):
    # affected_questions is pipe-delimited ("Q-000123|Q-000456"), not JSON -- this matches
    # scripts/step_plugins.py's A9Plugin.check(), which reads the CSV back with
    # `(row.get("affected_questions") or "").split("|")`. A JSON-array string here would break
    # that reader (e.g. "[]".split("|") -> ["[]"], a non-empty, non-Q-id "question").
    out = {}
    for k in fieldnames:
        v = row[k]
        if isinstance(v, bool):
            out[k] = "true" if v else "false"
        elif isinstance(v, list):
            out[k] = "|".join(v)
        elif v is None:
            out[k] = ""
        else:
            out[k] = v
    return out


def _deserialise_change_log_row(row):
    row = dict(row)
    row["could_flip_an_answer"] = row.get("could_flip_an_answer") == "true"
    row["affected_questions"] = [v for v in (row.get("affected_questions") or "").split("|") if v]
    return row


def write_change_log(chapter_id, judgements_path=None, old_book=None, new_book=None,
                      pairs_path=None, diffs_path=None, passages_dir=None, links_dir=None,
                      change_log_path=None, deleted_topics_path=None):
    """Run A9 for one chapter: merge its rows into the shared ncert/change_log.csv and
    ncert/deleted_topics.csv, leaving every other chapter's rows untouched. Returns
    (change_log_rows, deleted_topics_rows) for just this chapter (the schemas/A9.json shape).
    judgements_path defaults to default_judgements_path(chapter_id) -- see module docstring."""
    if old_book is None or new_book is None:
        from pair_passages import derive_book_ids
        default_old, default_new = derive_book_ids(chapter_id)
        old_book = old_book or default_old
        new_book = new_book or default_new

    judgements_path = judgements_path or default_judgements_path(chapter_id)
    pairs = load_pairs(chapter_id, pairs_path)
    diffs = load_diffs(chapter_id, diffs_path)
    judgements = load_judgements(judgements_path)
    if diffs and not judgements:
        raise FileNotFoundError(
            f"A9: chapter {chapter_id} has {len(diffs)} non-identical pair(s) from A7 needing a "
            f"judgement, but no judgements file was found at {judgements_path!r} (and none was "
            f"given via --judgements). A8 must resolve every non-identical pair before A9 can "
            f"log it."
        )
    old_links = load_links(old_book, links_dir)
    new_links = load_links(new_book, links_dir)
    old_passages = load_passages(old_book, passages_dir)
    new_passages = load_passages(new_book, passages_dir)

    change_log_path = _change_log_path(change_log_path)
    deleted_topics_path = _deleted_topics_path(deleted_topics_path)

    existing_change_log = [_deserialise_change_log_row(r) for r in lib_io.read_csv(change_log_path)]
    existing_change_ids = {
        (r["old_passage_id"], r["new_passage_id"]): r["change_id"]
        for r in existing_change_log if r["chapter_id"] == chapter_id
    }
    other_chapters_change_log = [r for r in existing_change_log if r["chapter_id"] != chapter_id]

    this_chapter_rows = build_change_log_rows(
        chapter_id, pairs, diffs, judgements, old_links, new_links, existing_change_ids
    )
    for row in this_chapter_rows:
        row["old_text"] = old_passages[row["old_passage_id"]]["text"]
        row["new_text"] = new_passages[row["new_passage_id"]]["text"]

    all_change_log_rows = other_chapters_change_log + this_chapter_rows
    all_change_log_rows.sort(key=lambda r: r["change_id"])
    lib_io.write_csv(
        change_log_path,
        [_serialise_row(r, CHANGE_LOG_FIELDS) for r in all_change_log_rows],
        CHANGE_LOG_FIELDS,
    )

    existing_deleted = lib_io.read_csv(deleted_topics_path)
    other_chapters_deleted = [r for r in existing_deleted if r["chapter_id"] != chapter_id]
    this_chapter_deleted = build_deleted_topics_rows(chapter_id, pairs, old_passages, old_links)
    all_deleted_rows = other_chapters_deleted + this_chapter_deleted
    all_deleted_rows.sort(key=lambda r: r["old_passage_id"])
    lib_io.write_csv(
        deleted_topics_path,
        [_serialise_row(r, DELETED_TOPICS_FIELDS) for r in all_deleted_rows],
        DELETED_TOPICS_FIELDS,
    )

    print(
        f"A9 write_change_log: chapter={chapter_id} change_log_rows={len(this_chapter_rows)} "
        f"deleted_topics_rows={len(this_chapter_deleted)} -> {change_log_path}, {deleted_topics_path}"
    )
    return this_chapter_rows, this_chapter_deleted


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--chapter-id", required=True, help="e.g. BIO12-CH06")
    parser.add_argument("--judgements",
                         help="JSON array of A8-shaped judgements (schemas/A8.json), one per "
                              "non-identical pair from A7's diffs; change_type must already be "
                              "resolved (never 'unsure'). Default: "
                              "steps/A8/out/<CHAPTER_ID>.judgements.json (see module docstring)")
    parser.add_argument("--old-book", help="default: derived as {SUBJ}{CLASS}O from --chapter-id")
    parser.add_argument("--new-book", help="default: derived as {SUBJ}{CLASS}L from --chapter-id")
    parser.add_argument("--pairs-file", help="override ncert/pairs/<CHAPTER>.json")
    parser.add_argument("--diffs-file", help="override ncert/diffs/<CHAPTER>.jsonl")
    parser.add_argument("--passages-dir", help="override ncert/passages (testing)")
    parser.add_argument("--links-dir", help="override ncert/links (testing)")
    parser.add_argument("--change-log", help="override ncert/change_log.csv (testing)")
    parser.add_argument("--deleted-topics", help="override ncert/deleted_topics.csv (testing)")
    args = parser.parse_args()

    try:
        write_change_log(
            chapter_id=args.chapter_id,
            judgements_path=args.judgements,
            old_book=args.old_book,
            new_book=args.new_book,
            pairs_path=args.pairs_file,
            diffs_path=args.diffs_file,
            passages_dir=args.passages_dir,
            links_dir=args.links_dir,
            change_log_path=args.change_log,
            deleted_topics_path=args.deleted_topics,
        )
    except (FileNotFoundError, ValueError, KeyError) as exc:
        print(f"A9 write_change_log FAILED for chapter {args.chapter_id}: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
