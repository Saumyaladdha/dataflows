#!/usr/bin/env python3
"""D3 - fetch the passages for one question (spec docs/SPEC.md Section 12/D3, schemas/D3.json).

SCRIPT-only (no agent at all, spec 12/D3 Worker line). Given one question's D2-resolved
subtopic(s) (papers/records/<QID>.json's `d2_subtopic_ids`, written by step_plugins.D2Plugin),
builds the three lists spec 12/D3 names:

  (a) latest-edition passages linked (ncert/links/<CHAPTER>L.jsonl) to those subtopics; if more
      than 15, ranked by word-trigram Jaccard overlap against stem+answer (reusing
      scripts/pair_passages.py's own word_trigrams/jaccard -- no new similarity logic written for
      this, per the build's own instruction) and truncated to the top 15.
  (b) their older-edition partners, from A6's ncert/pairs/<CHAPTER>.json (new_passage_id -> this
      latest passage; old_passage_id is the partner) -- empty when A6 never ran for this chapter
      (a real, honest gap: A6 has only ever run against hand-built fixture chapters in this
      project, never BIO12-CH01/CH03 for real; see the build report).
  (c) every OTHER older-edition passage of the same chapter(s) not paired to any latest passage at
      all (possible deleted content) -- also empty under the same real gap as (b).
  (d) for Physics/Chemistry only, lab-manual passages (book id ending "M") whose words overlap the
      question at all, ranked the same way as (a) and capped at 15.

(b) and (c) both feed the single "older" list per spec 12/D3's three-list Writes shape.

What this script deliberately does NOT do (see its own module docstring precedent, A6/
pair_passages.py's "script half" split, and scripts/CONVENTIONS.md rule 7 -- "never call a
subagent... where a step's text describes an agent in the loop, that is handled by the hybrid
path, not by the script shelling out itself"): spec 12/D3's own "On failure: zero latest passages
-> re-run D2 once... still zero -> blocked, D3_NO_PASSAGES" is a cross-step, STATEFUL decision
(has a D2 retry already happened for this item?) that only step_plugins.D3Plugin.check() can make
-- this script is a pure, idempotent, re-runnable function of "whatever papers/records/<QID>.json's
d2_subtopic_ids currently says" and never raises D3_NO_PASSAGES itself, even when latest comes back
empty on this call; D3Plugin decides what empty latest actually means this round.

Usage:
    python3 scripts/fetch_passages.py --item-id Q-000015

Per scripts/CONVENTIONS.md's own escape hatch ("if your script's natural shape doesn't fit
--chapter-id, add the extra flag and send a note back so this file gets updated to match"): D3's
item is a QUESTION, not a chapter, so this script takes --item-id (a question id) instead of
--chapter-id. Documented in scripts/CONVENTIONS.md's own table.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pair_passages  # word_trigrams, jaccard -- no new similarity logic written for D3
from scripts.lib import io as lib_io
from scripts.lib import records as lib_records

_SUBJECT_PREFIX = {"Physics": "PHY", "Chemistry": "CHE", "Biology": "BIO"}
_CHAPTER_ID_RE = re.compile(r"^([A-Z]{3})(1[12])-CH(\d{2})$")
_SUBTOPIC_TO_CHAPTER_RE = re.compile(r"^(.*)-ST\d+$")
_LATEST_CAP = 15


def _chapter_id_of(subtopic_id):
    m = _SUBTOPIC_TO_CHAPTER_RE.match(subtopic_id or "")
    return m.group(1) if m else None


def _book_prefix(chapter_id):
    """BIO12-CH03 -> 'BIO12' (the ncert/{passages,links}/<prefix><edition-letter>.jsonl stem)."""
    m = _CHAPTER_ID_RE.match(chapter_id or "")
    return f"{m.group(1)}{m.group(2)}" if m else None


def _read_jsonl_dict(path, key):
    out = {}
    if os.path.exists(path):
        for row in lib_io.read_jsonl(path):
            k = row.get(key)
            if k:
                out[k] = row
    return out


def _links_by_subtopic(book_id):
    out = {}
    path = lib_io.project_path("ncert", "links", f"{book_id}.jsonl")
    if os.path.exists(path):
        for link in lib_io.read_jsonl(path):
            sid, pid = link.get("subtopic_id"), link.get("passage_id")
            if sid and pid:
                out.setdefault(sid, []).append(pid)
    return out


def _question_query_text(record):
    answer = record.get("corrected_answer") or record.get("official_answer")
    options = record.get("corrected_options") or record.get("options_en") or {}
    answer_text = options.get(str(answer)) if answer is not None else None
    parts = [record.get("stem_en") or ""]
    parts += [s.get("text", "") for s in (record.get("statements") or [])]
    parts += [s.get("text", "") for s in (record.get("list_i") or [])]
    parts += [s.get("text", "") for s in (record.get("list_ii") or [])]
    if answer_text:
        parts.append(answer_text)
    return " ".join(parts)


def _rank_and_cap(query_text, items, cap, require_overlap=False):
    """items: [(passage_id, text), ...]. Returns the same shape, ranked by word-trigram Jaccard
    against query_text, capped at `cap`. When require_overlap, items scoring exactly 0 are
    dropped first (used for lab-manual matching, spec 12/D3(d): 'whose words match the
    question')."""
    if len(items) <= cap and not require_overlap:
        return items
    q_grams = pair_passages.word_trigrams(query_text)
    scored = [(pid, text, pair_passages.jaccard(q_grams, pair_passages.word_trigrams(text)))
              for pid, text in items]
    if require_overlap:
        scored = [t for t in scored if t[2] > 0]
    scored.sort(key=lambda t: -t[2])
    return [(pid, text) for pid, text, _score in scored[:cap]]


def _latest_passages(record, subtopic_ids):
    by_chapter = {}
    for sid in subtopic_ids:
        chapter_id = _chapter_id_of(sid)
        by_chapter.setdefault(chapter_id, []).append(sid)

    collected = {}  # passage_id -> text, dedup across subtopics/chapters
    for chapter_id, sids in by_chapter.items():
        prefix = _book_prefix(chapter_id)
        if not prefix:
            continue
        book_id = f"{prefix}L"
        links = _links_by_subtopic(book_id)
        passages = _read_jsonl_dict(lib_io.project_path("ncert", "passages", f"{book_id}.jsonl"), "passage_id")
        for sid in sids:
            for pid in links.get(sid, []):
                p = passages.get(pid)
                if not p or pid in collected:
                    continue
                text = p.get("text") or ""
                if not text.strip():
                    # Figure/table/equation passages legitimately carry NO text -- their content
                    # lives in the A2S crop, not in `text`. They must not enter `latest`: D4 can
                    # only quote text, and scripts/checks/D3.py correctly refuses a text-less
                    # passage, which BLOCKS the whole question. Real case: Q-000002 blocked on
                    # "latest passage 'PHY12L-CH02-P170' has empty text" while Q-000001 survived
                    # only because ranking happened to push its empty passages past the cap.
                    # This is not an edge case -- empty-text passages are ~12% of the corpus
                    # (PHY12L 69/514, PHY11L 65/552, BIO12L 65/456, CHE12L 30/312), all of kind
                    # figure/table/equation/box. The lab-manual path already filtered them via
                    # require_overlap=True; the latest path did not, which is the whole bug.
                    continue
                collected[pid] = text

    items = list(collected.items())
    ranked = _rank_and_cap(_question_query_text(record), items, _LATEST_CAP)
    return ranked, by_chapter


def _older_passages(by_chapter, latest_ids):
    """(b) A6-paired older partners of the kept latest passages, PLUS (c) every other
    older-edition passage of the same chapter(s) never paired to any latest passage at all
    (possible deleted content) -- both into one combined list, per spec 12/D3's three-list shape.
    """
    out = {}
    for chapter_id in by_chapter:
        prefix = _book_prefix(chapter_id)
        if not prefix:
            continue
        older_book = f"{prefix}O"
        older_passages = _read_jsonl_dict(
            lib_io.project_path("ncert", "passages", f"{older_book}.jsonl"), "passage_id")
        if not older_passages:
            continue  # no older edition indexed for this chapter at all (real gap, see docstring)

        pairs_path = lib_io.project_path("ncert", "pairs", f"{chapter_id}.json")
        pairs = []
        if os.path.exists(pairs_path):
            with open(pairs_path, "r", encoding="utf-8") as f:
                pairs = json.load(f) or []

        paired_old_ids = set()
        for row in pairs:
            if not isinstance(row, dict):
                continue
            old_pid, new_pid = row.get("old_passage_id"), row.get("new_passage_id")
            if new_pid in latest_ids and old_pid and old_pid in older_passages:
                out[old_pid] = older_passages[old_pid].get("text") or ""  # (b)
            if old_pid:
                paired_old_ids.add(old_pid)

        for pid, p in older_passages.items():
            if p.get("chapter_id") == chapter_id and pid not in paired_old_ids and pid not in out:
                out[pid] = p.get("text") or ""  # (c) "none"-tagged / unpaired -> possible deletion

    return [{"passage_id": pid, "text": text} for pid, text in out.items()]


def _lab_manual_passages(record, query_text):
    subject = record.get("subject")
    if subject not in ("Physics", "Chemistry"):
        return []
    prefix = _SUBJECT_PREFIX[subject]
    passages_dir = lib_io.project_path("ncert", "passages")
    if not os.path.isdir(passages_dir):
        return []
    items = []
    for fn in sorted(os.listdir(passages_dir)):
        if fn.endswith("M.jsonl") and fn.startswith(prefix):
            for p in lib_io.read_jsonl(os.path.join(passages_dir, fn)):
                pid = p.get("passage_id")
                if pid:
                    items.append((pid, p.get("text") or ""))
    ranked = _rank_and_cap(query_text, items, _LATEST_CAP, require_overlap=True)
    return [{"passage_id": pid, "text": text} for pid, text in ranked]


def fetch_for_item(item_id):
    record = lib_records.read_record(item_id)
    subtopic_ids = record.get("d2_subtopic_ids") or []
    subtopic_ids = [s for s in subtopic_ids if s and s != "unsure"]

    latest_items, by_chapter = _latest_passages(record, subtopic_ids) if subtopic_ids else ([], {})
    latest = [{"passage_id": pid, "text": text} for pid, text in latest_items]
    older = _older_passages(by_chapter, {pid for pid, _t in latest_items}) if by_chapter else []
    lab_manual = _lab_manual_passages(record, _question_query_text(record))

    out = {"latest": latest, "older": older, "lab_manual": lab_manual}
    out_path = lib_io.project_path("steps", "D3", "out", f"{item_id}.json")
    lib_io.ensure_parent(out_path)
    lib_io.atomic_write_json(out_path, out)
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description="D3: fetch NCERT passages for one question.")
    parser.add_argument("--item-id", required=True, help="Question id, e.g. Q-000015.")
    args = parser.parse_args(argv)

    out = fetch_for_item(args.item_id)
    print(f"fetch_passages.py {args.item_id}: latest={len(out['latest'])} "
          f"older={len(out['older'])} lab_manual={len(out['lab_manual'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
