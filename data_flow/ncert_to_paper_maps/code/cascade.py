#!/usr/bin/env python3
"""F3's cascade engine (spec Section 14/F3 step 5 and Section 15).

When a field changes — a Stage F correction, a prompt-version bump, a new codebook file — the
steps that READ that field become `stale` for the affected items, then whatever reads THEIR
outputs, transitively; the stale (item, step) pairs are then re-run in stage order with the
normal runner.

    python3 scripts/cascade.py --field subtopic --item BIO12-CH01-ST03 --plan
    python3 scripts/cascade.py --field official_answer --item Q-000015 --apply
    python3 scripts/cascade.py --field question_text --item Q-000015 --apply --run
    python3 scripts/cascade.py --verify-map

`--plan` prints the stale set and changes nothing (the default).
`--apply` writes status `stale` for each (item, step) pair.
`--run`   additionally drives the runner for the script-only steps among them, in stage order,
          and reports which agent-driven steps a person must dispatch by hand (this script never
          calls a subagent and never shells out to `claude` — scripts/CONVENTIONS.md rule 7).
`--verify-map` compares config/cascade.yaml against what steps.yaml's `input_fields` imply
          (spec Section 15's closing note / test T25) and prints the disagreements.

Also importable: `apply_review.py` calls `plan_for_change()` / `apply_plan()` / `run_plan()`.
"""
import argparse
import json
import os
import re
import subprocess
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import f_common as fc  # noqa: E402
from lib import io as lib_io  # noqa: E402
from lib import status as lib_status  # noqa: E402

CASCADE_PATH = fc.pp("config", "cascade.yaml")


# ---------------------------------------------------------------------------
# config/cascade.yaml
# ---------------------------------------------------------------------------

_CASCADE_CACHE = None


def load_cascade_map(path=None):
    """config/cascade.yaml as {changed_key: {scope: [steps] | bool, ...}} (spec Section 15)."""
    global _CASCADE_CACHE
    if path is None and _CASCADE_CACHE is not None:
        return _CASCADE_CACHE
    import yaml
    with open(path or CASCADE_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if path is None:
        _CASCADE_CACHE = data
    return data


# Concrete field names a reviewer can correct -> the cascade.yaml key that governs them.
#
# cascade.yaml's keys are CONCEPTS ("question_text", "official_answer"), but review/decisions.csv
# carries a real record field name ("stem_en", "options_en", "status"). This table is the join.
# Record field names are spec 6.3's; the `d1_`/`d2_` aliases are the names D1/D2 actually write
# today (see f_common.record_chapter_ids for why both exist).
FIELD_TO_KEY = {
    # Book register (spec 6.2 register/books.csv)
    "book_register": "book_register",
    "edition": "book_register", "edition_seen": "book_register",
    "reprint_text_exact": "book_register", "reprint_page": "book_register",
    "part_ranges": "book_register", "language": "book_register",
    # NCERT passages / subtopics
    "passage_cuts": "passage_cuts", "passage_text": "passage_cuts", "text": "passage_cuts",
    "blocks": "passage_cuts", "section_heading": "passage_cuts",
    "subtopic_list": "subtopic_list", "subtopics": "subtopic_list",
    "passage_link": "passage_link", "link": "passage_link",
    "pair": "pair", "pairs": "pair",
    "change_log_row": "change_log_row", "change_type": "change_log_row",
    "old_fact": "change_log_row", "new_fact": "change_log_row",
    "could_flip_an_answer": "change_log_row",
    # Paper register (spec 6.2 register/papers.csv)
    "paper_register": "paper_register", "booklet_code": "paper_register",
    "sitting": "paper_register", "year": "paper_register", "exam": "paper_register",
    "trust": "paper_register", "in_scope": "paper_register",
    # Stage B question fields
    "question_boundaries": "question_boundaries", "boundaries": "question_boundaries",
    "qno": "question_boundaries",
    "question_text": "question_text", "stem_en": "question_text", "options_en": "question_text",
    "statements": "question_text", "list_i": "question_text", "list_ii": "question_text",
    "option_images": "question_text", "structure": "question_text",
    "negative_words": "question_text", "has_figure": "question_text",
    "figure_file": "question_text",
    "official_answer": "official_answer", "answer_source": "official_answer",
    "status": "official_answer", "issue_reason": "official_answer",
    "b8_correction": "b8_correction", "corrected_answer": "b8_correction",
    "corrected_stem": "b8_correction",
    "subject_branch": "subject_branch", "subject": "subject_branch", "branch": "subject_branch",
    # Stage D
    "chapter": "chapter", "chapter_ids": "chapter", "d1_chapter_ids": "chapter",
    "subtopic": "subtopic", "subtopic_ids": "subtopic", "d2_subtopic_ids": "subtopic",
    "evidence": "evidence", "link_type": "evidence", "derivation_steps": "evidence",
    "covers": "evidence",
    "older_line": "older_line", "older_evidence": "older_line",
    "status_note": "status_note", "syllabus_status": "status_note", "note_type": "status_note",
    "reason_note": "status_note", "change_ids": "status_note",
    "latest_answer": "latest_answer", "answer_changed": "latest_answer",
    "change_note": "latest_answer",
    "fact_line": "fact_line",
    "repeat_groups": "repeat_groups", "repeat_group_id": "repeat_groups",
    "repeat_label": "repeat_groups", "related_ids": "repeat_groups",
    # Stage E tags
    "any_e_tag": "any_e_tag", "question_type": "any_e_tag", "format": "any_e_tag",
    "content_shape": "any_e_tag", "category_primary": "any_e_tag",
    "category_secondary": "any_e_tag", "category_why": "any_e_tag",
    "option_traps": "any_e_tag", "stem_context": "any_e_tag", "answer_form": "any_e_tag",
    "negation": "any_e_tag", "item_count": "any_e_tag", "constants_given": "any_e_tag",
    "figure_role": "any_e_tag", "descriptive_tags": "any_e_tag",
    # Infrastructure changes
    "codebook_file": "codebook_file", "allowed_value_change": "allowed_value_change",
}


def cascade_key_for_field(field):
    """The cascade.yaml key that governs a concrete field name, or None if nothing reads it.

    None is a real answer, not a failure: `comment`, `reviewer` and `review_status` are fields a
    reviewer may set that no step reads, so correcting them cascades to nothing."""
    if not field:
        return None
    f = str(field).strip()
    if f in FIELD_TO_KEY:
        return FIELD_TO_KEY[f]
    if f in load_cascade_map():
        return f
    return None


def unmapped_fields_note(field):
    return (f"no cascade entry for field {field!r} — nothing re-runs. If a step does read it, add "
            f"it to cascade.py::FIELD_TO_KEY and config/cascade.yaml (spec Section 15).")


# ---------------------------------------------------------------------------
# steps.yaml `needs` graph, for the transitive half of the cascade
# ---------------------------------------------------------------------------

_STEP_CODE_RE = re.compile(r"\b([A-E]\d{1,2}S?|S0|F\d)\b")


def needs_of(step):
    """The steps a step depends on, parsed out of steps.yaml's free-text `needs` field
    (e.g. "D8 (all questions of the subtopic)" -> ["D8"], "C1, A9" -> ["C1", "A9"])."""
    raw = (fc.load_steps().get(step) or {}).get("needs") or ""
    if raw.strip() in ("", "-"):
        return []
    known = set(fc.step_order())
    return [c for c in _STEP_CODE_RE.findall(str(raw)) if c in known]


def downstream_steps(step):
    """Every step that transitively depends on `step`, in stage order."""
    reverse = {}
    for s in fc.step_order():
        for dep in needs_of(s):
            reverse.setdefault(dep, []).append(s)
    seen, stack = set(), list(reverse.get(step, []))
    while stack:
        s = stack.pop()
        if s in seen:
            continue
        seen.add(s)
        stack.extend(reverse.get(s, []))
    return sorted(seen, key=fc.step_index)


# ---------------------------------------------------------------------------
# Scope resolution: a cascade.yaml scope + an anchor item -> real (step, item) pairs
# ---------------------------------------------------------------------------

QUESTION_ITEM_KINDS = {"question", "faulty question", "question needing a figure",
                       "question × answer", "wrong option", "decision", "item"}


def _step_items(step):
    """Every item id the step already has a status for. The cascade can only make something stale
    that actually ran; a step with no status files has nothing to invalidate."""
    return [item_id for item_id, _ in fc.iter_step_statuses(step)]


def _book_matches(part, book_id):
    m = (fc._RE_PASSAGE.match(part) or fc._RE_BOOK_PAGE.match(part) or fc._RE_BOOK.match(part))
    if m:
        return f"{m.group(1)}{m.group(2)}{m.group(3)}" == book_id
    m = fc._RE_SUBTOPIC.match(part) or fc._RE_CHAPTER.match(part)
    if m:
        return f"{m.group(1)}{m.group(2)}" == book_id[:-1]
    return False


def _records_citing_book(book_id, records):
    """Questions whose evidence (latest or older) quotes a passage of this book."""
    out = []
    for qid, rec in records.items():
        cited = False
        for key in ("evidence", "older_evidence"):
            for ev in rec.get(key) or []:
                pid = (ev or {}).get("passage_id") or ""
                if pid.startswith(book_id + "-"):
                    cited = True
        if cited:
            out.append(qid)
    return sorted(out)


def _records_citing_passages(passage_ids, records):
    wanted = set(passage_ids)
    out = []
    for qid, rec in records.items():
        for key in ("evidence", "older_evidence"):
            for ev in rec.get(key) or []:
                if (ev or {}).get("passage_id") in wanted:
                    out.append(qid)
                    break
            else:
                continue
            break
    return sorted(set(out))


def _questions_in_chapter(chapter_id, records):
    return sorted(q for q, r in records.items() if chapter_id in fc.record_chapter_ids(r))


def _questions_in_subtopic(subtopic_id, records):
    return sorted(q for q, r in records.items() if subtopic_id in fc.record_subtopic_ids(r))


def _question_aliases(qid, records, index):
    """Every item id by which a step might know this question: the QID itself, plus the
    `<PAPER>-q<NNNN>` ids Stage B used before the QID was minted, plus the C1 pair ids."""
    aliases = {qid}
    for key, value in index.items():
        if value == qid and "#" in key:
            paper, qno = key.rsplit("#", 1)
            aliases.add(f"{paper}-q{int(qno):04d}")
    rec = records.get(qid) or {}
    merged_into = rec.get("merged_into")
    merged_from = rec.get("merged_from")
    for other in (merged_into, merged_from):
        if other:
            aliases.add(f"{qid}|{other}")
            aliases.add(f"{other}|{qid}")
    return aliases


def _paper_scope_items(step, paper_id, records, index):
    items = []
    for item_id in _step_items(step):
        parts = fc.item_parts(item_id)
        if any(p == paper_id or p.startswith(paper_id + "-") for p in parts):
            items.append(item_id)
            continue
        for p in parts:
            if fc._RE_QID.match(p):
                rec = records.get(p) or {}
                codes = rec.get("paper_codes") or []
                stem = paper_id.rsplit("-", 1)
                code = stem[1] if len(stem) == 2 else None
                if code and any(str(c).split(":")[0] == code for c in codes):
                    items.append(item_id)
                    break
    return sorted(set(items))


def resolve_scope(step, scope, anchor, records, index, change=None):
    """Which items of `step` a scope makes stale, given the anchor item that changed.

    Returns a sorted list of item ids. An empty list is a legitimate outcome — it means nothing
    of that step has run for anything in scope yet, so there is nothing to invalidate."""
    item_kind = fc.step_item_kind(step)
    question_scoped = item_kind in QUESTION_ITEM_KINDS

    if scope == "rerun_book":
        return sorted(i for i in _step_items(step)
                      if any(_book_matches(p, anchor) for p in fc.item_parts(i)))

    if scope == "rerun_questions_citing":
        if anchor and fc._RE_BOOK.match(anchor):
            qids = _records_citing_book(anchor, records)
        elif anchor and fc._RE_PASSAGE.match(anchor):
            qids = _records_citing_passages([anchor], records)
        elif change and change.get("passage_ids"):
            qids = _records_citing_passages(change["passage_ids"], records)
        else:
            qids = []
        return _map_qids_to_step_items(step, qids, records, index, question_scoped)

    if scope in ("rerun_chapter",):
        chapters = fc.item_chapter_ids(anchor, records, index) or ([anchor] if fc._RE_CHAPTER.match(anchor or "") else [])
        out = []
        for i in _step_items(step):
            if set(fc.item_chapter_ids(i, records, index)) & set(chapters):
                out.append(i)
        if item_kind == "chapter":
            out.extend(c for c in chapters)
        return sorted(set(out))

    if scope == "rerun_questions_in_chapter":
        chapters = fc.item_chapter_ids(anchor, records, index) or ([anchor] if fc._RE_CHAPTER.match(anchor or "") else [])
        qids = sorted({q for c in chapters for q in _questions_in_chapter(c, records)})
        if item_kind == "subtopic":
            return sorted({st for q in qids for st in fc.record_subtopic_ids(records[q])})
        return _map_qids_to_step_items(step, qids, records, index, question_scoped)

    if scope == "rerun_questions_in_subtopic":
        sts = [anchor] if fc._RE_SUBTOPIC.match(anchor or "") else fc.record_subtopic_ids(records.get(anchor) or {})
        qids = sorted({q for st in sts for q in _questions_in_subtopic(st, records)})
        if item_kind == "subtopic":
            return sorted(set(sts))
        return _map_qids_to_step_items(step, qids, records, index, question_scoped)

    if scope == "rerun_pair":
        pair_ids = (change or {}).get("pair_item_ids")
        if pair_ids:
            return sorted(set(pair_ids))
        # A pair's own item id shape is not fixed by the spec; fall back to the chapter, which is
        # a superset and therefore safe (it re-runs more than strictly needed, never less).
        return resolve_scope(step, "rerun_chapter", anchor, records, index, change)

    if scope == "rerun_affected_questions":
        qids = (change or {}).get("affected_questions") or []
        if not qids and anchor:
            for row in fc.change_log_rows():
                if row.get("change_id") == anchor:
                    qids = [q.strip() for q in (row.get("affected_questions") or "").replace(";", ",").split(",") if q.strip()]
        if item_kind == "subtopic":
            return sorted({st for q in qids for st in fc.record_subtopic_ids(records.get(q) or {})})
        return _map_qids_to_step_items(step, qids, records, index, question_scoped)

    if scope == "rerun_paper":
        return _paper_scope_items(step, anchor, records, index)

    if scope == "rerun_question":
        if item_kind == "subtopic":
            return sorted(fc.record_subtopic_ids(records.get(anchor) or {}))
        if item_kind == "chapter":
            return sorted(fc.item_chapter_ids(anchor, records, index))
        return _map_qids_to_step_items(step, [anchor], records, index, True)

    if scope == "rerun_subtopic":
        sts = [anchor] if fc._RE_SUBTOPIC.match(anchor or "") else fc.record_subtopic_ids(records.get(anchor) or {})
        if item_kind == "subtopic":
            return sorted(set(sts))
        qids = sorted({q for st in sts for q in _questions_in_subtopic(st, records)})
        return _map_qids_to_step_items(step, qids, records, index, question_scoped)

    if scope == "rerun_old_and_new_subtopic":
        sts = set((change or {}).get("old_subtopic_ids") or [])
        sts |= set((change or {}).get("new_subtopic_ids") or [])
        if not sts:
            sts = set(fc.record_subtopic_ids(records.get(anchor) or {}))
            if fc._RE_SUBTOPIC.match(anchor or ""):
                sts.add(anchor)
        if item_kind == "subtopic":
            return sorted(sts)
        qids = sorted({q for st in sts for q in _questions_in_subtopic(st, records)})
        return _map_qids_to_step_items(step, qids, records, index, question_scoped)

    if scope in ("rerun_all_questions_of_step_that_reads_it",
                 "rerun_affected_questions_of_that_tag_step"):
        qids = (change or {}).get("affected_questions") or sorted(records)
        if item_kind == "subtopic":
            return sorted({st for q in qids for st in fc.record_subtopic_ids(records[q])})
        return _map_qids_to_step_items(step, qids, records, index, question_scoped)

    if scope == "then":
        qids = (change or {}).get("affected_questions") or sorted(records)
        if item_kind == "subtopic":
            return sorted({st for q in qids for st in fc.record_subtopic_ids(records[q])})
        return _map_qids_to_step_items(step, qids, records, index, question_scoped)

    raise ValueError(f"unknown cascade scope {scope!r} in config/cascade.yaml")


def _map_qids_to_step_items(step, qids, records, index, question_scoped):
    """Turn a list of QIDs into the item ids this step actually uses.

    A question-scoped step may know a question by its QID (Stage D/E) or by its pre-QID
    `<PAPER>-q<NNNN>` id (Stage B). Both are returned when both exist as real status files, plus
    the QID itself so a step that has never run for it still gets a stale marker."""
    if not question_scoped:
        existing = set(_step_items(step))
        out = set()
        for qid in qids:
            for c in fc.item_chapter_ids(qid, records, index):
                if c in existing:
                    out.add(c)
        return sorted(out)
    existing = set(_step_items(step))
    out = set()
    for qid in qids:
        aliases = _question_aliases(qid, records, index)
        hit = aliases & existing
        out |= hit if hit else {qid}
    return sorted(out)


# ---------------------------------------------------------------------------
# Planning
# ---------------------------------------------------------------------------

class StalePair(dict):
    """One (step, item_id) pair the cascade invalidates, plus why."""


def plan_for_change(field, anchor, change=None, transitive=True, records=None, index=None):
    """The stale set for one change.

    `field`  a record field name or a cascade.yaml key (see FIELD_TO_KEY).
    `anchor` the item whose field changed (QID, chapter id, subtopic id, book id, paper id,
             change id ...).
    `change` optional extras a scope may need: affected_questions, old/new_subtopic_ids,
             passage_ids, pair_item_ids.

    Returns {"key": ..., "direct": [StalePair], "transitive": [StalePair], "notes": [...]}.
    """
    records = fc.canonical_records() if records is None else records
    index = fc.qid_index() if index is None else index
    notes = []
    key = cascade_key_for_field(field)
    if key is None:
        return {"key": None, "direct": [], "transitive": [], "notes": [unmapped_fields_note(field)]}

    entry = load_cascade_map().get(key) or {}
    direct, seen = [], set()
    for scope, value in entry.items():
        if value is True:
            # `rerun_all_questions_of_step_that_reads_it: true` names no step list of its own;
            # the step is "whichever reads the codebook / the renamed value", which steps.yaml
            # records as `codebook_file`. Resolve it from there rather than guessing.
            steps = _steps_reading_codebook() if key == "codebook_file" else _tag_steps()
            notes.append(f"scope {scope}=true resolved to steps {','.join(steps) or '(none)'} "
                         f"from config/steps.yaml")
        elif isinstance(value, list):
            steps = value
        else:
            notes.append(f"ignoring non-list scope value for {key}.{scope}: {value!r}")
            continue
        for step in steps:
            if step not in fc.load_steps():
                notes.append(f"config/cascade.yaml names step {step!r} which is not in config/steps.yaml")
                continue
            for item_id in resolve_scope(step, scope, anchor, records, index, change):
                pair = (step, item_id)
                if pair in seen:
                    continue
                seen.add(pair)
                direct.append(StalePair(step=step, item_id=item_id, scope=scope, key=key,
                                        reason=f"{key} changed on {anchor} ({scope})"))

    trans = []
    if transitive:
        for pair in direct:
            for down in downstream_steps(pair["step"]):
                # Stage F is the review process itself, not a derived value: F1 builds the pack,
                # F2 is people, F3 is this script, F5 is the release gate. Marking them "stale"
                # would be meaningless churn. F4 (the counts) IS a derived value and cascade.yaml
                # names it explicitly wherever it should re-run, so it arrives via `direct`.
                if fc.stage_of(down) == "F":
                    continue
                for item_id in _downstream_items(down, pair["item_id"], records, index):
                    k = (down, item_id)
                    if k in seen:
                        continue
                    seen.add(k)
                    trans.append(StalePair(step=down, item_id=item_id, scope="transitive",
                                           key=key,
                                           reason=f"reads {pair['step']}'s output for {pair['item_id']}"))
    direct.sort(key=lambda p: (fc.step_index(p["step"]), p["item_id"]))
    trans.sort(key=lambda p: (fc.step_index(p["step"]), p["item_id"]))
    return {"key": key, "direct": direct, "transitive": trans, "notes": notes}


def _downstream_items(step, item_id, records, index):
    """Which items of a downstream step read `item_id`'s output.

    Deliberately conservative-by-over-inclusion: a question's downstream steps get that question;
    a subtopic-scoped step gets the question's subtopics; a chapter-scoped step gets its chapters.
    Only items that ALREADY have a status are returned for non-question steps, so this cannot
    invent work for things that never ran."""
    kind = fc.step_item_kind(step)
    parts = fc.item_parts(item_id)
    qids = [p for p in parts if fc._RE_QID.match(p)]
    if not qids:
        m = next((fc._RE_PAPER_Q.match(p) for p in parts if fc._RE_PAPER_Q.match(p)), None)
        if m:
            qid = index.get(f"{m.group(1)}#{int(m.group(3))}")
            if qid:
                qids = [qid]
    if kind in QUESTION_ITEM_KINDS and qids:
        return _map_qids_to_step_items(step, qids, records, index, True)
    if kind == "subtopic":
        return sorted({st for q in qids for st in fc.record_subtopic_ids(records.get(q) or {})})
    existing = set(_step_items(step))
    chapters = set(fc.item_chapter_ids(item_id, records, index))
    if kind == "chapter":
        return sorted(chapters)
    return sorted(i for i in existing if set(fc.item_chapter_ids(i, records, index)) & chapters)


def _steps_reading_codebook():
    return [s for s, cfg in fc.load_steps().items() if (cfg or {}).get("codebook_file")]


def _tag_steps():
    return [s for s, cfg in fc.load_steps().items() if str((cfg or {}).get("stage")) == "E"
            and s != "E0"]


# ---------------------------------------------------------------------------
# Applying and running
# ---------------------------------------------------------------------------

def apply_plan(plan, dry_run=False):
    """Write status `stale` for every pair in the plan (spec 14/F3 step 5), remembering each
    pair's previous status and output digests so `run_plan` can tell an unchanged re-run from a
    changed one. Returns the list of applied pairs with that snapshot attached."""
    applied = []
    for pair in list(plan["direct"]) + list(plan["transitive"]):
        step, item_id = pair["step"], pair["item_id"]
        prev = lib_status.read_status(step, item_id) or {}
        snapshot = {
            "step": step, "item_id": item_id, "scope": pair["scope"], "key": pair["key"],
            "reason": pair["reason"],
            "previous_status": prev.get("status"),
            "previous_prompt_version": prev.get("prompt_version"),
            "previous_out_digests": fc.step_out_digests(step, item_id),
        }
        if not dry_run:
            lib_status.write_status(step, item_id, lib_status.STALE, extra={
                "prompt_version": prev.get("prompt_version"),
                "check_message": f"stale: {pair['reason']}",
                "stale_reason": pair["reason"],
                "stale_from_field": pair["key"],
                "previous_status": prev.get("status"),
                "stale_at": fc.now_iso(),
            })
        applied.append(snapshot)
    if not dry_run and applied:
        lib_io.append_jsonl(fc.CASCADE_LOG_PATH, {
            "at": fc.now_iso(), "action": "mark_stale", "pairs": [
                {"step": p["step"], "item_id": p["item_id"], "reason": p["reason"]} for p in applied
            ],
        })
    return applied


def _is_script_only(step):
    return str((fc.load_steps().get(step) or {}).get("agent") or "").strip() == "script"


def run_plan(applied, dry_run=False, runner="scripts/run_step.py"):
    """Re-run the stale (item, step) pairs in stage order (spec 14/F3 step 5).

    Script-only steps are driven through the normal runner (`run_step.py <STEP> --auto --items
    ...`). Agent-driven steps are NOT dispatched here: a script must never call a subagent
    (scripts/CONVENTIONS.md rule 7), so they are returned as `needs_dispatch` for the operator to
    run through the usual `--list` / invoke / `--check` loop.

    A re-run whose output is byte-identical to the previous output raises no flag and has its
    previous status restored; open flags on a pair that came back `pass` are set `auto_closed`.
    """
    report = {"ran": [], "needs_dispatch": [], "unchanged": [], "changed": [], "auto_closed": []}
    by_step = {}
    for pair in applied:
        by_step.setdefault(pair["step"], []).append(pair)

    for step in sorted(by_step, key=fc.step_index):
        pairs = by_step[step]
        items = sorted({p["item_id"] for p in pairs})
        if not _is_script_only(step):
            report["needs_dispatch"].append({"step": step, "items": items})
            continue
        cmd = [sys.executable, runner, step, "--auto", "--items", ",".join(items)]
        if dry_run:
            report["ran"].append({"step": step, "items": items, "cmd": " ".join(cmd),
                                  "dry_run": True})
            continue
        proc = subprocess.run(cmd, cwd=fc.PROJECT_ROOT, capture_output=True, text=True)
        report["ran"].append({"step": step, "items": items, "cmd": " ".join(cmd),
                              "returncode": proc.returncode,
                              "stdout_tail": (proc.stdout or "")[-2000:],
                              "stderr_tail": (proc.stderr or "")[-2000:]})
        for pair in pairs:
            after = fc.step_out_digests(step, pair["item_id"])
            if after and after == pair["previous_out_digests"]:
                report["unchanged"].append({"step": step, "item_id": pair["item_id"]})
                if pair["previous_status"] in lib_status.ALL_STATUSES:
                    lib_status.write_status(step, pair["item_id"], pair["previous_status"], extra={
                        "prompt_version": pair.get("previous_prompt_version"),
                        "check_message": "cascade re-run produced identical output; no flag raised",
                    })
            else:
                report["changed"].append({"step": step, "item_id": pair["item_id"]})

    if not dry_run:
        report["auto_closed"] = auto_close_flags(applied)
        lib_io.append_jsonl(fc.CASCADE_LOG_PATH, {"at": fc.now_iso(), "action": "rerun",
                                                  "report": report})
    return report


def auto_close_flags(applied):
    """Flags that no longer apply are set `auto_closed` (spec 14/F3 step 5).

    The rule implemented: an OPEN flag on a (step, item) pair the cascade just re-ran is
    auto-closed when that pair's new status is `pass` — i.e. the step ran again, every check
    passed, and no replacement flag of that code was raised. Anything else (still flagged, now
    blocked, never re-run) is left open for a person, because the cascade cannot know whether the
    reviewer's concern survived."""
    pairs = {(p["step"], p["item_id"]) for p in applied}
    if not pairs:
        return []
    flags = fc.load_flags()
    closed = []
    for flag in flags:
        if flag.get("status") != "open":
            continue
        key = (flag.get("step"), flag.get("item_id"))
        if key not in pairs:
            continue
        st = (lib_status.read_status(key[0], key[1]) or {}).get("status")
        if st == lib_status.PASS:
            flag["status"] = "auto_closed"
            flag["decision"] = "auto_closed"
            flag["decided_at"] = fc.now_iso()
            flag["auto_closed_reason"] = "cascade re-run passed every check; flag no longer applies"
            closed.append(flag["flag_id"])
    if closed:
        fc.save_flags(flags)
    return closed


def what_reruns_text(field, anchor=None, records=None, index=None, max_items=6):
    """A one-paragraph, human-readable "editing this re-runs ..." for F1's pack pages.

    Shows the cascade.yaml rule (which steps, under which scope) rather than a resolved item
    list, because a reviewer needs to know the blast radius, and the resolved list depends on how
    much of the pipeline has run."""
    key = cascade_key_for_field(field)
    if key is None:
        return "Nothing re-runs: no step in config/cascade.yaml reads this field."
    entry = load_cascade_map().get(key) or {}
    bits = []
    for scope, value in entry.items():
        label = scope.replace("rerun_", "").replace("_", " ")
        if value is True:
            steps = _steps_reading_codebook() if key == "codebook_file" else _tag_steps()
            bits.append(f"{label}: {', '.join(steps) or '(none)'}")
        elif isinstance(value, list):
            bits.append(f"{label}: {', '.join(value)}")
    return f"cascade key `{key}` → " + "; ".join(bits) if bits else f"cascade key `{key}` → (nothing)"


# ---------------------------------------------------------------------------
# --verify-map: cascade.yaml vs what steps.yaml's input_fields imply (spec 15 / test T25)
# ---------------------------------------------------------------------------

def derive_from_input_fields():
    """Derive "which steps read this cascade key" from each step's `input_fields` in steps.yaml.

    Spec Section 15 asks cascade.py to derive the same answer from `input_fields` as
    config/cascade.yaml states, with a test (T25) checking the two agree. That agreement is NOT
    achievable from the data as it stands: many steps have no `input_fields` at all, deliberately
    so in several cases (steps.yaml's own comments say `input_fields` lists what an AGENT call may
    see, and a script-only step has none). `input_fields` also does not distinguish a field a
    step READS from one it PRODUCES — A3 lists `blocks` because it cuts them, not because it
    consumes someone else's cuts — so a derived map over-claims as well as under-claims. So this
    returns what the data supports and `--verify-map` reports the gap instead of asserting
    equality; config/cascade.yaml stays authoritative."""
    derived = {}
    for step, cfg in fc.load_steps().items():
        for field in (cfg or {}).get("input_fields") or []:
            key = cascade_key_for_field(field)
            if key:
                derived.setdefault(key, set()).add(step)
    return {k: sorted(v, key=fc.step_index) for k, v in derived.items()}


def verify_map():
    """Compare config/cascade.yaml with derive_from_input_fields(). Returns a report dict."""
    stated = {}
    for key, entry in load_cascade_map().items():
        steps = set()
        for value in entry.values():
            if isinstance(value, list):
                steps |= set(value)
        stated[key] = sorted(steps, key=fc.step_index)
    derived = derive_from_input_fields()
    empty_input_fields = [s for s, cfg in fc.load_steps().items()
                          if not ((cfg or {}).get("input_fields") or [])]
    rows = []
    for key in sorted(set(stated) | set(derived)):
        s, d = set(stated.get(key, [])), set(derived.get(key, []))
        rows.append({"key": key, "stated_only": sorted(s - d, key=fc.step_index),
                     "derived_only": sorted(d - s, key=fc.step_index),
                     "agree": sorted(s & d, key=fc.step_index)})
    return {"rows": rows, "steps_with_empty_input_fields": empty_input_fields,
            "agrees": all(not r["stated_only"] and not r["derived_only"] for r in rows)}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description="F3 cascade (spec 14/F3, Section 15).")
    ap.add_argument("--field", help="Record field name or config/cascade.yaml key that changed.")
    ap.add_argument("--item", help="Item whose field changed (QID / chapter / subtopic / book / paper / change id).")
    ap.add_argument("--change-json", help="Optional JSON with scope extras: affected_questions, old_subtopic_ids, new_subtopic_ids, passage_ids, pair_item_ids.")
    ap.add_argument("--plan", action="store_true", help="Print the stale set; change nothing (default).")
    ap.add_argument("--apply", action="store_true", help="Write status `stale` for each pair.")
    ap.add_argument("--run", action="store_true", help="After --apply, drive the runner for script-only steps in stage order.")
    ap.add_argument("--no-transitive", action="store_true", help="Explicit cascade.yaml lists only; skip the `needs`-graph closure.")
    ap.add_argument("--verify-map", action="store_true", help="Compare config/cascade.yaml with steps.yaml's input_fields (spec 15 / T25).")
    ap.add_argument("--json", action="store_true", help="Machine-readable output.")
    args = ap.parse_args(argv)

    if args.verify_map:
        rep = verify_map()
        if args.json:
            print(json.dumps(rep, indent=2))
            return 0
        print("cascade.yaml vs steps.yaml input_fields (spec Section 15 / test T25)")
        print(f"  agree overall: {rep['agrees']}")
        print(f"  steps with EMPTY input_fields ({len(rep['steps_with_empty_input_fields'])}): "
              f"{','.join(rep['steps_with_empty_input_fields'])}")
        for row in rep["rows"]:
            if row["stated_only"] or row["derived_only"]:
                print(f"  {row['key']}:")
                if row["stated_only"]:
                    print(f"      stated in cascade.yaml only: {','.join(row['stated_only'])}")
                if row["derived_only"]:
                    print(f"      implied by input_fields only: {','.join(row['derived_only'])}")
        print(f"\nThe two cannot agree while {len(rep['steps_with_empty_input_fields'])} steps "
              f"have no input_fields at all (nothing can be derived for them) and input_fields "
              f"does not separate 'reads' from 'produces'. cascade.yaml stays authoritative; "
              f"this report is the gap, and the `implied by input_fields only` lines are the "
              f"candidate omissions in cascade.yaml worth a human look.")
        return 0

    if not args.field or not args.item:
        ap.error("--field and --item are required unless --verify-map is given")

    change = json.loads(args.change_json) if args.change_json else None
    plan = plan_for_change(args.field, args.item, change=change,
                           transitive=not args.no_transitive)

    if args.json and not (args.apply or args.run):
        print(json.dumps(plan, indent=2))
        return 0

    print(f"cascade: field {args.field!r} on {args.item!r} -> key {plan['key']!r}")
    for note in plan["notes"]:
        print(f"  note: {note}")
    print(f"  direct     ({len(plan['direct'])} pairs): "
          f"{', '.join(sorted({p['step'] for p in plan['direct']}, key=fc.step_index)) or '(none)'}")
    print(f"  transitive ({len(plan['transitive'])} pairs): "
          f"{', '.join(sorted({p['step'] for p in plan['transitive']}, key=fc.step_index)) or '(none)'}")
    for p in plan["direct"] + plan["transitive"]:
        print(f"    {p['step']:4s} {p['item_id']:38s} {p['scope']}")

    if not (args.apply or args.run):
        print("\n(plan only; nothing changed. Use --apply to mark these stale.)")
        return 0

    applied = apply_plan(plan)
    print(f"\nmarked {len(applied)} (item, step) pairs stale")
    if args.run:
        rep = run_plan(applied)
        for r in rep["ran"]:
            print(f"  ran {r['step']}: rc={r.get('returncode')} items={len(r['items'])}")
        for d in rep["needs_dispatch"]:
            print(f"  NEEDS A PERSON: {d['step']} is agent-driven — run "
                  f"`python3 scripts/run_step.py {d['step']} --list --items {','.join(d['items'])}`, "
                  f"invoke the named subagent per line, then `--check`.")
        print(f"  unchanged re-runs (no flag): {len(rep['unchanged'])}")
        print(f"  changed re-runs: {len(rep['changed'])}")
        print(f"  flags auto_closed: {len(rep['auto_closed'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
