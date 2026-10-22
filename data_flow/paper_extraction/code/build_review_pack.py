#!/usr/bin/env python3
"""F1 · Build the review queue and pack (spec Section 14/F1).

    python3 scripts/build_review_pack.py
    python3 scripts/build_review_pack.py --chapters BIO12-CH01,BIO12-CH03
    python3 scripts/build_review_pack.py --new-only          # F3 step 6, after applying decisions
    python3 scripts/build_review_pack.py --first-full-review # include the E4 agreement sample
    python3 scripts/build_review_pack.py --dry-run           # report the queue, write nothing

Collects (spec 14/F1):
  * every OPEN flag in flags/flags.jsonl;
  * an AUDIT SAMPLE of `pass` items — 5% per step, at least 20 per step per run, stratified by
    subject and year, with a FIXED random seed so the same run reproduces the same sample;
  * every draft needing approval — the register/subtopic-list/change-log flags, plus every
    `ncert/subtopics/<CHAPTER>.json` and `ncert/change_log.csv` row that Stage F has not yet
    approved (those have an `approval` field of their own in spec 6.4 and are not always
    represented by a live flag);
  * on the first full review, the E4 agreement sample — 50 questions per subject shown WITHOUT
    the pipeline's tags.

Orders them strictly: (1) blocker; (2) book and paper registers; (3) subtopic lists and
change-log rows; (4) high; (5) normal; (6) E0 findings and new categories; (7) low and the audit
sample — then groups by chapter (see f_common.priority_of).

Writes: review/queue.csv (spec 6.5), one HTML page per item under review/review_pack/, an
index.html, review/audit_sample.jsonl, review/e4_agreement.jsonl, and a header-only
review/decisions.csv if none exists. Writes nothing anywhere else; raises no flags.
"""
import argparse
import glob
import hashlib
import json
import math
import os
import random
import re
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import cascade  # noqa: E402
import f_common as fc  # noqa: E402
from lib import io as lib_io  # noqa: E402
from lib import status as lib_status  # noqa: E402

# --------------------------------------------------------------------------------------------
# The audit sample's seed.
#
# Spec 14/F1 requires a FIXED random seed so the sample is reproducible. This constant is that
# seed; `--seed` overrides it only for testing. The per-step generator is seeded from
# f"{seed}:{step}" rather than from the seed alone, so adding or removing a step changes only
# that step's sample instead of reshuffling every other step's — which is what makes the sample
# stable across a growing pipeline, not merely stable within one invocation.
# --------------------------------------------------------------------------------------------
AUDIT_SEED = 20261013
AUDIT_FRACTION = 0.05
AUDIT_MIN_PER_STEP = 20

E4_AGREEMENT_PER_SUBJECT = 50
E4_HIDDEN_FIELDS = (
    "question_type", "format", "content_shape", "category_primary", "category_secondary",
    "category_why", "option_traps", "stem_context", "answer_form", "negation", "item_count",
    "constants_given", "figure_role", "descriptive_tags",
)

AUDIT_SAMPLE_PATH = os.path.join(fc.REVIEW_DIR, "audit_sample.jsonl")
E4_AGREEMENT_PATH = os.path.join(fc.REVIEW_DIR, "e4_agreement.jsonl")
MANIFEST_PATH = os.path.join(fc.PACK_DIR, "_manifest.json")

# Which field of a record a flag's decision is about. A reviewer correcting a D1_GUESS is
# correcting the chapter; correcting a B5_KEY_ADJUDICATED is correcting the official answer.
# Anything not listed falls back to the flag's step, whose own primary field is looked up in
# STEP_PRIMARY_FIELD; anything still unknown becomes the literal string "provisional_value",
# which cascades to nothing and tells the reviewer to name the field themselves.
CODE_FIELD = {
    "A1_REGISTER_DRAFT": "book_register", "A1_REPRINT_NOT_FOUND": "reprint_text_exact",
    "A1_EDITION_MISMATCH": "edition_seen",
    "A2_JOIN_ADJUDICATED": "passage_cuts", "A2_TEXT_MISMATCH": "passage_text",
    "A2_UNREADABLE": "passage_text", "A2_CHECK_FAILED": "passage_text",
    "A2_SPECIAL_UNREAD": "passage_text", "A3_DEFAULT_CUTS": "passage_cuts",
    "A4_SUBTOPICS_DRAFT": "subtopic_list", "A5_UNSURE": "passage_link",
    "A6_WEAK_PAIR": "pair", "A8_ADJUDICATED": "change_log_row",
    "A8_FACT_CHANGE": "change_log_row", "A8_WORDING_RISK": "change_log_row",
    "B1_REGISTER_DRAFT": "paper_register", "B1_MANIFEST_MISMATCH": "paper_register",
    "B2_BOUNDARY_ADJUDICATED": "question_boundaries", "B2_MISSING_QNO": "question_boundaries",
    "B3_OPTION_COUNT": "options_en", "B3_UNREADABLE": "stem_en",
    "B3_DUPLICATE_OPTIONS": "options_en", "B4_MISMATCH_ADJUDICATED": "question_text",
    "B5_KEY_ROW_MISSING": "official_answer", "B5_KEY_ADJUDICATED": "official_answer",
    "B6_DISAGREES_WITH_KEY": "official_answer", "B6_IMAGE_INPUT_UNSAFE": "has_figure",
    "B7_BRANCH_GUESS": "branch", "B8_CORRECTION": "corrected_answer",
    "B9_FIGURE_RECOVERED": "figure_file", "B9_FIGURE_EXTRA_IMAGES": "figure_file",
    "C1_READING_FIXED": "question_text", "C1_UNMATCHED": "paper_codes",
    "C1_KEY_INCONSISTENT": "official_answer",
    "D1_ADJUDICATED": "chapter_ids", "D1_GUESS": "chapter_ids", "D1_NO_CHAPTERS": "chapter_ids",
    "D2_ADJUDICATED": "subtopic_ids", "D2_GUESS": "subtopic_ids",
    "D3_NO_PASSAGES": "subtopic_ids",
    "D4_QUOTE_NOT_FOUND": "evidence", "D4_PARTLY": "evidence", "D4_NO_SUPPORT": "evidence",
    "D4_DERIVATION_MISMATCH": "derivation_steps", "D4_BEYOND_NCERT": "evidence",
    "D5_QUOTE_NOT_FOUND": "older_evidence",
    "D6_TEMPLATE_NOTE": "reason_note", "D6_NOTE_APPROVAL": "reason_note",
    "D7_ANSWER_CHANGED": "latest_answer", "D7_UNEXPLAINED_CHANGE": "latest_answer",
    "D8_LOW_CONFIDENCE": "fact_line", "D11_ADJUDICATED": "repeat_group_id",
    "E0_FINDINGS_READY": "allowed_value_change", "E_NEW_CATEGORY": "allowed_value_change",
    "E1_ADJUDICATED": "question_type", "E2_NEGATIVE_GUARD": "format", "E3_MEDIUM": "content_shape",
    "E4_ADJUDICATED": "category_primary", "E4_NO_CODEBOOK": "category_primary",
    "E5_ADJUDICATED": "option_traps", "E6_CONTEXT_UNSURE": "stem_context",
    "S0_MISSING_INPUT": "paper_register",
}

STEP_PRIMARY_FIELD = {
    "A1": "book_register", "A2": "passage_text", "A2S": "passage_text", "A3": "passage_cuts",
    "A4": "subtopic_list", "A5": "passage_link", "A6": "pair", "A7": "pair",
    "A8": "change_log_row", "A9": "change_log_row",
    "B1": "paper_register", "B2": "question_boundaries", "B3": "question_text",
    "B4": "question_text", "B5": "official_answer", "B6": "official_answer",
    "B7": "subject_branch", "B8": "b8_correction", "B9": "figure_file",
    "C1": "question_text",
    "D1": "chapter_ids", "D2": "subtopic_ids", "D3": "subtopic_ids", "D4": "evidence",
    "D5": "older_evidence", "D6": "status_note", "D7": "latest_answer", "D8": "fact_line",
    "D9": "repeat_groups", "D10": "repeat_groups", "D11": "repeat_groups",
    "E1": "question_type", "E2": "format", "E3": "content_shape", "E4": "category_primary",
    "E5": "option_traps", "E6": "stem_context",
}

# Who reviews what (spec 14/F2). Shown on each page so the pack can be split up.
REVIEWER_FOR_PRIORITY = {
    2: "Ekta (registers and intake)",
    3: "faculty of that subject (subtopic lists, change log)",
}


def field_for(flag):
    code = flag.get("code") or ""
    if code in CODE_FIELD:
        return CODE_FIELD[code]
    step = flag.get("step") or ""
    if step in STEP_PRIMARY_FIELD:
        return STEP_PRIMARY_FIELD[step]
    return "provisional_value"


# --------------------------------------------------------------------------------------------
# Collecting
# --------------------------------------------------------------------------------------------

def collect_flag_items(records, index, chapters_filter):
    """One pack item per OPEN flag."""
    items = []
    for flag in fc.open_flags():
        chs = fc.item_chapter_ids(flag.get("item_id"), records, index)
        if chapters_filter is not None and not (set(chs) & set(chapters_filter)):
            continue
        field = field_for(flag)
        items.append({
            "pack_id": flag["flag_id"],
            "kind": "flag",
            "priority": fc.priority_of(flag),
            "chapter_ids": chs,
            "flag_id": flag["flag_id"],
            "item_id": flag.get("item_id"),
            "item_type": flag.get("item_type"),
            "step": flag.get("step"),
            "code": flag.get("code"),
            "severity": flag.get("severity"),
            "message": flag.get("message"),
            "field": field,
            "value": flag.get("provisional_value"),
            "evidence": list(flag.get("evidence") or []),
            "prompt_version": flag.get("prompt_version"),
            "created_at": flag.get("created_at"),
        })
    return items


def collect_subtopic_list_drafts(approvals, chapters_filter):
    """Subtopic lists Stage F has not approved yet (spec 6.4's `approval` field; F5 gates on it)."""
    items = []
    for draft in fc.subtopic_list_drafts():
        ch = draft["chapter_id"]
        if chapters_filter is not None and ch not in chapters_filter:
            continue
        target = fc.subtopic_list_target(ch)
        if (approvals.get(target) or {}).get("decision") == "approve":
            continue
        items.append({
            "pack_id": f"subtopic_list:{ch}",
            "kind": "subtopic_list_draft",
            "priority": 3,
            "chapter_ids": [ch],
            "flag_id": "",
            "item_id": ch,
            "item_type": "subtopic_list",
            "step": "A4",
            "code": "A4_SUBTOPICS_DRAFT",
            "severity": "normal",
            "message": (f"Subtopic list for {ch}: {len(draft['subtopics'])} subtopics, version "
                        f"{draft.get('version')}, approval in file = "
                        f"{draft.get('approval_in_file')!r}. Needs Stage F approval before the "
                        f"chapter can be released (spec 14/F5)."),
            "field": "subtopic_list",
            "value": draft["subtopics"],
            "evidence": [draft["path"]],
            "prompt_version": None,
            "created_at": None,
        })
    return items


def collect_change_log_drafts(approvals, chapters_filter):
    """Change-log rows Stage F has not approved yet (spec 6.4's `approval` column)."""
    items = []
    for row in fc.change_log_rows():
        ch = (row.get("chapter_id") or "").strip()
        if chapters_filter is not None and ch not in chapters_filter:
            continue
        change_id = (row.get("change_id") or "").strip()
        if not change_id:
            continue
        target = fc.change_log_target(change_id)
        if (approvals.get(target) or {}).get("decision") == "approve":
            continue
        items.append({
            "pack_id": f"change_log_row:{change_id}",
            "kind": "change_log_draft",
            "priority": 3,
            "chapter_ids": [ch] if ch else [],
            "flag_id": "",
            "item_id": change_id,
            "item_type": "change_log_row",
            "step": "A9",
            "code": "A9_CHANGE_LOG_ROW",
            "severity": "high" if str(row.get("could_flip_an_answer", "")).lower() in ("yes", "true", "1") else "normal",
            "message": (f"Change-log row {change_id} ({row.get('change_type')}) for {ch}: "
                        f"could_flip_an_answer={row.get('could_flip_an_answer')!r}, affects "
                        f"{row.get('affected_questions') or '(no questions recorded)'}."),
            "field": "change_log_row",
            "value": row,
            "evidence": ["ncert/change_log.csv"],
            "prompt_version": None,
            "created_at": None,
        })
    return items


def _audit_target(population_size):
    """5% per step, at least 20 per step per run — but never more than exist (spec 14/F1)."""
    return min(population_size, max(AUDIT_MIN_PER_STEP, math.ceil(AUDIT_FRACTION * population_size)))


def _stratify(pass_items, records, index):
    """Group a step's `pass` items by (subject, year). Either half may be None; `None` is a
    stratum, never a guess (see f_common.item_subject_year)."""
    strata = {}
    for item_id in pass_items:
        subject, year = fc.item_subject_year(item_id, records, index)
        strata.setdefault((subject, year), []).append(item_id)
    for v in strata.values():
        v.sort()
    return strata


def _allocate(strata, target):
    """Largest-remainder allocation of `target` draws across strata in proportion to their size.

    Deterministic: strata are visited in sorted key order and ties on the remainder are broken by
    that same order, so the allocation is a pure function of (strata sizes, target)."""
    keys = sorted(strata, key=lambda k: (str(k[0]), str(k[1])))
    total = sum(len(strata[k]) for k in keys)
    if total == 0 or target <= 0:
        return {k: 0 for k in keys}
    exact = {k: target * len(strata[k]) / total for k in keys}
    alloc = {k: min(len(strata[k]), int(exact[k])) for k in keys}
    remaining = target - sum(alloc.values())
    order = sorted(keys, key=lambda k: (-(exact[k] - int(exact[k])), str(k[0]), str(k[1])))
    i = 0
    while remaining > 0 and any(alloc[k] < len(strata[k]) for k in keys):
        k = order[i % len(order)]
        if alloc[k] < len(strata[k]):
            alloc[k] += 1
            remaining -= 1
        i += 1
        if i > 10000:
            break
    return alloc


def collect_audit_sample(records, index, chapters_filter, seed, steps_filter=None):
    """The audit sample: `pass` items per step, 5% / min 20, stratified by subject and year,
    reproducible from a fixed seed.

    Returned items are NOT written to flags/flags.jsonl. Spec Section 16 does list AUDIT_SAMPLE
    as a flag code, and this is a deliberate departure, recorded here:
      1. F1 is not the step that judged the item, so a flag attributed to step D4 but raised by
         F1 would misattribute it, and scripts/CONVENTIONS.md rule 5 reserves flag-raising for
         the step itself;
      2. "at least 20 per step per RUN" means a fresh sample every run — writing those into
         flags.jsonl would grow the one real flag file without bound, run after run;
      3. flags.jsonl is appended to concurrently by every other stage.
    They are recorded in review/audit_sample.jsonl instead, appear in queue.csv and the pack like
    any other item, and F5's release gate reads them from there.
    """
    out = []
    for step in fc.steps_with_status():
        if steps_filter and step not in steps_filter:
            continue
        pass_items = [i for i, st in fc.iter_step_statuses(step)
                      if st.get("status") == lib_status.PASS]
        if not pass_items:
            continue
        target = _audit_target(len(pass_items))
        strata = _stratify(pass_items, records, index)
        alloc = _allocate(strata, target)
        rng = random.Random(f"{seed}:{step}")
        picked = []
        for key in sorted(strata, key=lambda k: (str(k[0]), str(k[1]))):
            n = alloc[key]
            if n <= 0:
                continue
            picked.extend(rng.sample(strata[key], n))
        picked.sort()
        for item_id in picked:
            chs = fc.item_chapter_ids(item_id, records, index)
            if chapters_filter is not None and not (set(chs) & set(chapters_filter)):
                continue
            subject, year = fc.item_subject_year(item_id, records, index)
            out.append({
                "pack_id": f"audit:{step}:{item_id}",
                "kind": "audit_sample",
                "priority": 7,
                "chapter_ids": chs,
                "flag_id": "",
                "item_id": item_id,
                "item_type": fc.step_item_kind(step),
                "step": step,
                "code": fc.AUDIT_CODE,
                "severity": "low",
                "message": (f"Audit sample: {step} passed every check for this item. Confirm the "
                            f"value is actually right. Stratum (subject={subject!r}, "
                            f"year={year!r}); {target} of {len(pass_items)} passing {step} items "
                            f"sampled this run; seed {seed}."),
                "field": STEP_PRIMARY_FIELD.get(step, "provisional_value"),
                "value": _value_for_audit(step, item_id, records),
                "evidence": sorted(fc.step_out_digests(step, item_id).keys()),
                "prompt_version": None,
                "created_at": None,
                "audit": {"step": step, "population": len(pass_items), "target": target,
                          "subject": subject, "year": year, "seed": seed},
            })
    return out


def _value_for_audit(step, item_id, records):
    """The value an audit-sample page shows: the record field this step owns when the item is a
    question, otherwise the step's own output file contents."""
    field = STEP_PRIMARY_FIELD.get(step)
    if field and fc._RE_QID.match(item_id or ""):
        rec = records.get(item_id) or {}
        if field == "chapter_ids":
            return fc.record_chapter_ids(rec)
        if field == "subtopic_ids":
            return fc.record_subtopic_ids(rec)
        if field in rec:
            return rec[field]
    for path in sorted(glob.glob(fc.pp("steps", step, "out", f"{item_id}*.json"))):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError):
            continue
    return None


def _rehydrate_e4_agreement(records, chapters_filter):
    """Re-emit the E4 agreement sample already recorded in review/e4_agreement.jsonl, unchanged."""
    out = []
    for row in lib_io.read_jsonl(E4_AGREEMENT_PATH):
        qid = row.get("item_id")
        chs = row.get("chapter_ids") or fc.record_chapter_ids(records.get(qid) or {})
        if chapters_filter is not None and not (set(chs) & set(chapters_filter)):
            continue
        out.append({
            "pack_id": row.get("pack_id") or f"e4_agreement:{qid}",
            "kind": "e4_agreement", "priority": 7, "chapter_ids": chs,
            "flag_id": "", "item_id": qid, "item_type": "question", "step": "E4",
            "code": "E4_AGREEMENT_SAMPLE", "severity": "low",
            "message": (f"E4 agreement sample ({row.get('subject')}). The pipeline's thinking tag "
                        f"is DELIBERATELY HIDDEN on this page. Read the question and write the "
                        f"primary thinking category you would give it."),
            "field": "category_primary", "value": None,
            "evidence": [f"papers/records/{qid}.json"],
            "prompt_version": None, "created_at": None,
            "e4_agreement": {"subject": row.get("subject"), "seed": row.get("seed")},
        })
    return out


def collect_e4_agreement(records, index, chapters_filter, seed):
    """The E4 agreement sample: 50 questions per subject shown WITHOUT the pipeline's tags
    (spec 14/F1), so faculty agreement with E4 can be measured against an unprimed judgement
    (Section 1.1: thinking-tag agreement >= 85% per subject).

    Candidates are canonical questions E4 has actually tagged. If E4 has not run, this is empty —
    there is nothing to measure agreement against, and inventing candidates would produce a
    meaningless agreement number."""
    by_subject = {}
    for qid, rec in fc.canonical_records(records).items():
        if not rec.get("category_primary"):
            continue
        by_subject.setdefault(rec.get("subject") or "unknown", []).append(qid)
    out = []
    for subject in sorted(by_subject):
        pool = sorted(by_subject[subject])
        # Spread across years: round-robin the years so a 50-draw never lands in one year.
        by_year = {}
        for qid in pool:
            by_year.setdefault((records[qid].get("year")), []).append(qid)
        rng = random.Random(f"{seed}:E4:{subject}")
        for v in by_year.values():
            rng.shuffle(v)
        picked, years = [], sorted(by_year, key=lambda y: (y is None, y))
        while len(picked) < min(E4_AGREEMENT_PER_SUBJECT, len(pool)):
            progressed = False
            for y in years:
                if by_year[y]:
                    picked.append(by_year[y].pop())
                    progressed = True
                    if len(picked) >= min(E4_AGREEMENT_PER_SUBJECT, len(pool)):
                        break
            if not progressed:
                break
        for qid in sorted(picked):
            chs = fc.record_chapter_ids(records[qid])
            if chapters_filter is not None and not (set(chs) & set(chapters_filter)):
                continue
            out.append({
                "pack_id": f"e4_agreement:{qid}",
                "kind": "e4_agreement",
                "priority": 7,
                "chapter_ids": chs,
                "flag_id": "",
                "item_id": qid,
                "item_type": "question",
                "step": "E4",
                "code": "E4_AGREEMENT_SAMPLE",
                "severity": "low",
                "message": (f"E4 agreement sample ({subject}). The pipeline's thinking tag is "
                            f"DELIBERATELY HIDDEN on this page. Read the question and write the "
                            f"primary thinking category you would give it."),
                "field": "category_primary",
                "value": None,
                "evidence": [f"papers/records/{qid}.json"],
                "prompt_version": None,
                "created_at": None,
                "e4_agreement": {"subject": subject, "seed": seed},
            })
    return out


# --------------------------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------------------------

CSS = """
:root { --fg:#14171a; --bg:#fff; --muted:#5b6670; --line:#d8dee3; --hi:#fff3bf;
        --hi-line:#e0b400; --blocker:#b3261e; --high:#c75300; --normal:#2b6cb0; --low:#5b6670; }
* { box-sizing:border-box; }
body { margin:0; font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
       color:var(--fg); background:var(--bg); }
.wrap { max-width:62rem; margin:0 auto; padding:1.5rem 1.25rem 4rem; }
h1 { font-size:1.4rem; margin:0 0 .25rem; }
h2 { font-size:1.05rem; margin:2rem 0 .5rem; border-bottom:1px solid var(--line);
     padding-bottom:.3rem; }
a { color:#1a5fb4; }
.meta { color:var(--muted); font-size:.85rem; margin-bottom:1.25rem; }
.badge { display:inline-block; padding:.1rem .45rem; border-radius:.5rem; font-size:.75rem;
         font-weight:600; color:#fff; vertical-align:.08em; }
.badge.blocker{background:var(--blocker)} .badge.high{background:var(--high)}
.badge.normal{background:var(--normal)} .badge.low{background:var(--low)}
.card { border:1px solid var(--line); border-radius:.5rem; padding:.9rem 1rem; margin:0 0 1rem; }
.card h3 { margin:0 0 .5rem; font-size:1rem; }
.value { background:var(--hi); border:1px solid var(--hi-line); border-radius:.4rem;
         padding:.7rem .85rem; }
pre { margin:0; white-space:pre-wrap; word-break:break-word; font:13px/1.5 ui-monospace,
      SFMono-Regular,Menlo,monospace; }
table { border-collapse:collapse; width:100%; font-size:.86rem; }
th,td { border:1px solid var(--line); padding:.35rem .5rem; text-align:left;
        vertical-align:top; }
th { background:#f4f6f8; }
.scroll { overflow-x:auto; }
label { display:block; font-weight:600; font-size:.85rem; margin:.7rem 0 .2rem; }
select,input[type=text],textarea { width:100%; font:inherit; padding:.4rem .5rem;
  border:1px solid var(--line); border-radius:.35rem; background:#fff; color:var(--fg); }
textarea { font:13px/1.45 ui-monospace,SFMono-Regular,Menlo,monospace; }
button { font:inherit; font-weight:600; padding:.45rem .9rem; border:1px solid var(--line);
         border-radius:.35rem; background:#f4f6f8; color:var(--fg); cursor:pointer; }
.row { display:flex; gap:.5rem; flex-wrap:wrap; align-items:center; margin-top:.7rem; }
.hint { color:var(--muted); font-size:.82rem; }
.nav { display:flex; justify-content:space-between; gap:1rem; margin-bottom:1rem;
       font-size:.86rem; }
.hidden-note { border-left:3px solid var(--hi-line); background:#fffbe6; padding:.6rem .8rem;
               font-size:.88rem; }
"""

# The pack is static HTML opened from the filesystem; there is no server to POST to. So the form
# builds the exact review/decisions.csv row and the reviewer saves it: "Copy row" puts one CSV
# line on the clipboard to paste into the spreadsheet, and the index page collects every decision
# made in this browser into one downloadable decisions.csv. localStorage is per-page-origin and
# can be unavailable (private windows, file:// restrictions), so every write is wrapped and the
# copy-the-row path always works even when storage does not.
FORM_JS = """
const KEY = 'pyq_decisions_v1';
function store() { try { return window.localStorage; } catch (e) { return null; } }
function allDecisions() {
  const s = store(); if (!s) return {};
  try { return JSON.parse(s.getItem(KEY) || '{}'); } catch (e) { return {}; }
}
function csvField(v) {
  v = (v === null || v === undefined) ? '' : String(v);
  return /[",\\n\\r]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v;
}
function buildRow() {
  const g = id => (document.getElementById(id) || {}).value || '';
  return [g('f_target'), g('f_field'), g('f_decision'), g('f_value'), g('f_reviewer'),
          g('f_comment'), g('f_decided_at')].map(csvField).join(',');
}
function refresh() {
  const out = document.getElementById('f_row');
  if (out) out.value = buildRow();
}
function saveDecision() {
  refresh();
  const s = store();
  if (s) {
    const all = allDecisions();
    all[document.getElementById('f_target').value] = buildRow();
    try { s.setItem(KEY, JSON.stringify(all)); } catch (e) {}
  }
  const n = document.getElementById('f_saved');
  if (n) n.textContent = s ? 'Saved in this browser. Collect every saved decision from index.html.'
                           : 'This browser blocks local storage — use "Copy row" and paste into review/decisions.csv.';
}
function copyRow() {
  refresh();
  const t = document.getElementById('f_row');
  t.select();
  try { document.execCommand('copy'); } catch (e) {}
  if (navigator.clipboard) { navigator.clipboard.writeText(t.value).catch(() => {}); }
  const n = document.getElementById('f_saved');
  if (n) n.textContent = 'Row copied. Paste it as a new line in review/decisions.csv.';
}
document.addEventListener('DOMContentLoaded', () => {
  const d = document.getElementById('f_decided_at');
  if (d && !d.value) d.value = new Date().toISOString().slice(0, 10);
  ['f_decision', 'f_value', 'f_reviewer', 'f_comment', 'f_decided_at'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('input', refresh);
  });
  refresh();
});
"""

INDEX_JS = """
const KEY = 'pyq_decisions_v1';
const HEADER = 'flag_id_or_item,field,decision,corrected_value_json,reviewer,comment,decided_at';
function collect() {
  let all = {};
  try { all = JSON.parse(window.localStorage.getItem(KEY) || '{}'); } catch (e) {}
  const rows = Object.keys(all).sort().map(k => all[k]);
  const box = document.getElementById('collected');
  box.value = rows.length ? HEADER + '\\n' + rows.join('\\n') + '\\n'
                          : '(no decisions saved in this browser yet)';
  document.getElementById('collected_count').textContent = rows.length + ' decision(s)';
}
function copyAll() {
  const t = document.getElementById('collected');
  t.select();
  try { document.execCommand('copy'); } catch (e) {}
  if (navigator.clipboard) { navigator.clipboard.writeText(t.value).catch(() => {}); }
  document.getElementById('collected_note').textContent =
    'Copied. Save it as review/decisions.csv (replacing the header-only file), then run ' +
    'python3 scripts/apply_review.py --apply';
}
function clearAll() {
  if (!confirm('Delete every decision saved in this browser? The pack itself is untouched.')) return;
  try { window.localStorage.removeItem(KEY); } catch (e) {}
  collect();
}
document.addEventListener('DOMContentLoaded', collect);
"""


def _page_filename(item):
    """A stable, filesystem-safe page name: priority, chapter, then a digest of the pack id so
    two items can never collide and the same item keeps the same filename across runs."""
    ch = (item["chapter_ids"][0] if item["chapter_ids"] else fc.NO_CHAPTER)
    safe_ch = "".join(c if c.isalnum() or c in "-_" else "_" for c in ch)
    base = "".join(c if c.isalnum() or c in "-_" else "_" for c in item["pack_id"])[:60]
    digest = hashlib.sha256(item["pack_id"].encode("utf-8")).hexdigest()[:8]
    return f"p{item['priority']}__{safe_ch}__{base}__{digest}.html"


def _evidence_fallback(item):
    """When a flag recorded no evidence paths, show the step's own output files for that item
    instead. Observed on real data (D1_GUESS on Q-000015 carries `evidence: []` even though
    steps/D1/out/Q-000015.*.json exist), and spec 14/F1 asks the pack to show "agent runs side by
    side" — so the pack finds them rather than showing an empty Evidence section. This adds no
    information the pipeline did not already write; it only locates it."""
    found = sorted(fc.step_out_digests(item["step"] or "", item["item_id"] or "").keys())
    for part in fc.item_parts(item["item_id"] or ""):
        if fc._RE_QID.match(part):
            found.append(f"papers/records/{part}.json")
            for pattern in (f"papers/questions/*/{part}*.png",):
                found.extend(os.path.relpath(p, fc.PROJECT_ROOT)
                             for p in sorted(glob.glob(fc.pp(pattern))))
    seen, out = set(), []
    for f in found:
        if f not in seen and os.path.exists(fc.pp(f)):
            seen.add(f)
            out.append(f)
    return out


def _evidence_html(item):
    evidence = item["evidence"] or _evidence_fallback(item)
    note = ("" if item["evidence"] else
            "<p class='hint'>The flag itself recorded no evidence paths; these are this step's "
            "own output files for the item, found by the pack.</p>")
    if not evidence:
        return "<p class='hint'>No evidence files were recorded with this item, and this step has no output file for it.</p>"
    rows = []
    for ev in evidence:
        rel = str(ev)
        abspath = rel if os.path.isabs(rel) else fc.pp(rel)
        exists = os.path.exists(abspath)
        href = os.path.relpath(abspath, fc.PACK_DIR) if exists else None
        is_image = rel.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))
        cell = (f"<a href='{fc.html_escape(href)}'>{fc.html_escape(rel)}</a>" if href
                else f"{fc.html_escape(rel)} <em>(file not found)</em>")
        if href and is_image:
            cell += (f"<br><img src='{fc.html_escape(href)}' alt='' "
                     f"style='max-width:100%;border:1px solid #d8dee3;border-radius:.3rem;margin-top:.4rem'>")
        else:
            cell += _inline_evidence(abspath) if exists else ""
        rows.append(f"<tr><td>{cell}</td></tr>")
    return note + f"<div class='scroll'><table><tbody>{''.join(rows)}</tbody></table></div>"


def _inline_evidence(abspath, limit=4000):
    """Inline a small JSON/text evidence file so the reviewer does not have to open it.

    Each agent run's own output file is what spec 14/F1 means by "agent runs side by side" and
    "adjudicator choice" — the pack shows them in the order the flag listed them, which for an
    adjudicated step is runA, runB, adjudicated."""
    if not abspath.lower().endswith((".json", ".txt", ".md", ".csv", ".jsonl")):
        return ""
    try:
        with open(abspath, "r", encoding="utf-8") as f:
            text = f.read(limit + 1)
    except (OSError, UnicodeDecodeError):
        return ""
    truncated = len(text) > limit
    if abspath.endswith(".json"):
        try:
            text = json.dumps(json.loads(text), indent=2, ensure_ascii=False)
        except json.JSONDecodeError:
            pass
    body = fc.html_escape(text[:limit]) + ("\n… (truncated)" if truncated else "")
    return f"<pre style='margin-top:.5rem'>{body}</pre>"


def _record_context_html(item, records):
    """The question itself, when the item is (or resolves to) a question — the "page/question
    image, both readings, verified quotes with surrounding passage text" of spec 14/F1."""
    qids = [p for p in fc.item_parts(item["item_id"]) if fc._RE_QID.match(p)]
    if not qids:
        return ""
    blocks = []
    for qid in qids:
        rec = records.get(qid)
        if not rec:
            continue
        hide = item["kind"] == "e4_agreement"
        parts = [f"<h3>Question {fc.html_escape(qid)}</h3>"]
        parts.append("<table><tbody>")
        for label, key in (("exam/year/sitting", None), ("paper codes", "paper_codes"),
                           ("subject / branch", None), ("official answer", "official_answer"),
                           ("status", "status")):
            if key is None and label == "exam/year/sitting":
                val = f"{rec.get('exam')} {rec.get('year')} {rec.get('sitting')}"
            elif key is None:
                val = f"{rec.get('subject')} / {rec.get('branch')}"
            else:
                val = rec.get(key)
            parts.append(f"<tr><th style='width:12rem'>{fc.html_escape(label)}</th>"
                         f"<td>{fc.html_escape(val)}</td></tr>")
        parts.append("</tbody></table>")
        parts.append(f"<p style='margin-top:.7rem'><strong>Stem.</strong> "
                     f"{fc.html_escape(rec.get('stem_en'))}</p>")
        for st in rec.get("statements") or []:
            parts.append(f"<p style='margin:.2rem 0'><strong>{fc.html_escape(st.get('label'))}.</strong> "
                         f"{fc.html_escape(st.get('text'))}</p>")
        opts = rec.get("options_en") or {}
        if opts:
            rows = "".join(f"<tr><th style='width:3rem'>{fc.html_escape(k)}</th>"
                           f"<td>{fc.html_escape(v)}</td></tr>" for k, v in sorted(opts.items()))
            parts.append(f"<table style='margin-top:.5rem'><tbody>{rows}</tbody></table>")
        fig = rec.get("figure_file")
        if fig:
            abspath = fig if os.path.isabs(fig) else fc.pp(fig)
            if os.path.exists(abspath):
                href = os.path.relpath(abspath, fc.PACK_DIR)
                parts.append(f"<p><img src='{fc.html_escape(href)}' alt='figure' "
                             f"style='max-width:100%;border:1px solid #d8dee3;border-radius:.3rem'></p>")
        for ev in rec.get("evidence") or []:
            parts.append(f"<p class='hint'>evidence · {fc.html_escape((ev or {}).get('passage_id'))} "
                         f"for {fc.html_escape((ev or {}).get('for'))}: "
                         f"“{fc.html_escape((ev or {}).get('exact_line'))}”</p>")
        if hide:
            parts.append("<div class='hidden-note'>The pipeline's E1–E6 tags for this question "
                         "are hidden on purpose (spec 14/F1: the E4 agreement sample is shown "
                         "<strong>without</strong> the agent's tags). Do not look them up before "
                         "answering.</div>")
        else:
            tags = {k: rec.get(k) for k in E4_HIDDEN_FIELDS if rec.get(k) is not None}
            if tags:
                rows = "".join(f"<tr><th style='width:12rem'>{fc.html_escape(k)}</th>"
                               f"<td><pre>{fc.html_escape(json.dumps(v, ensure_ascii=False, indent=2) if not isinstance(v, str) else v)}</pre></td></tr>"
                               for k, v in tags.items())
                parts.append(f"<h3 style='margin-top:1rem'>Tags</h3>"
                             f"<div class='scroll'><table><tbody>{rows}</tbody></table></div>")
        blocks.append("".join(parts))
    if not blocks:
        return ""
    return "<div class='card'>" + "</div><div class='card'>".join(blocks) + "</div>"


def _legacy_html(item, records):
    """The legacy values if any (spec 14/F1). Legacy sheet fields live on the record; a register
    item has no legacy counterpart, which is said plainly rather than left blank."""
    qids = [p for p in fc.item_parts(item["item_id"]) if fc._RE_QID.match(p)]
    rows = []
    for qid in qids:
        rec = records.get(qid) or {}
        for key in ("legacy_chapter", "legacy_topic", "legacy_question_type"):
            if rec.get(key) is not None:
                rows.append(f"<tr><th style='width:14rem'>{fc.html_escape(qid)} · "
                            f"{fc.html_escape(key)}</th><td>{fc.html_escape(rec[key])}</td></tr>")
    if not rows:
        return ("<p class='hint'>No legacy values recorded for this item. (Spec 2.2: the legacy "
                "tags are not usable as truth — they are shown only as a cross-check when they "
                "exist.)</p>")
    return f"<div class='scroll'><table><tbody>{''.join(rows)}</tbody></table></div>"


def _form_html(item):
    target = item["flag_id"] or item["pack_id"]
    value_json = json.dumps(item["value"], ensure_ascii=False) if item["value"] is not None else ""
    options = "".join(f"<option value='{v}'>{v}</option>" for v in fc.DECISION_VALUES)
    return f"""
<h2>Decision</h2>
<div class="card">
  <p class="hint">This writes one row of <code>review/decisions.csv</code> (spec 6.5). Columns:
  <code>{', '.join(fc.DECISION_FIELDS)}</code>.</p>
  <input type="hidden" id="f_target" value="{fc.html_escape(target)}">
  <input type="hidden" id="f_field" value="{fc.html_escape(item['field'])}">
  <label for="f_decision">decision</label>
  <select id="f_decision">{options}</select>
  <label for="f_value">corrected_value_json <span class="hint">— leave as-is to approve the
    value below; replace it with the corrected value (valid JSON) to correct or edit</span></label>
  <textarea id="f_value" rows="4">{fc.html_escape(value_json)}</textarea>
  <label for="f_reviewer">reviewer</label>
  <input type="text" id="f_reviewer" placeholder="your name">
  <label for="f_comment">comment</label>
  <input type="text" id="f_comment" placeholder="why">
  <label for="f_decided_at">decided_at</label>
  <input type="text" id="f_decided_at">
  <label for="f_row">the decisions.csv row this makes</label>
  <textarea id="f_row" rows="3" readonly></textarea>
  <div class="row">
    <button type="button" onclick="saveDecision()">Save in this browser</button>
    <button type="button" onclick="copyRow()">Copy row</button>
    <span class="hint" id="f_saved"></span>
  </div>
  <p class="hint">The pack is plain files with no server behind it, so nothing here can write to
  disk by itself. Save decisions here and collect them all from <a href="index.html">index.html</a>,
  or copy a row and paste it straight into <code>review/decisions.csv</code>. Then run
  <code>python3 scripts/apply_review.py --apply</code>.</p>
</div>
"""


def render_item_page(item, records, prev_href, next_href, run_id):
    sev = item["severity"] or "normal"
    rerun = cascade.what_reruns_text(item["field"], item["item_id"], records)
    value_pretty = (json.dumps(item["value"], indent=2, ensure_ascii=False)
                    if item["value"] is not None else "(no provisional value — nothing to approve "
                                                      "as-is; this item needs a corrected value "
                                                      "or a block)")
    who = REVIEWER_FOR_PRIORITY.get(item["priority"], "faculty of that subject (spec 14/F2)")
    nav = (f"<div class='nav'><div>{'<a href=\"' + prev_href + '\">&larr; previous</a>' if prev_href else ''}</div>"
           f"<div><a href='index.html'>index</a></div>"
           f"<div>{'<a href=\"' + next_href + '\">next &rarr;</a>' if next_href else ''}</div></div>")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{fc.html_escape(item['pack_id'])} · {fc.html_escape(item['code'])}</title>
<style>{CSS}</style></head><body><div class="wrap">
{nav}
<h1>{fc.html_escape(item['code'])} <span class="badge {sev}">{fc.html_escape(sev)}</span></h1>
<p class="meta">
  priority {fc.html_escape(fc.PRIORITY_LABELS.get(item['priority'], item['priority']))} ·
  step {fc.html_escape(item['step'])} ·
  item <code>{fc.html_escape(item['item_id'])}</code> ·
  chapter {fc.html_escape(', '.join(item['chapter_ids']) or '(none)')} ·
  {fc.html_escape(item['flag_id'] or item['pack_id'])} ·
  reviewer: {fc.html_escape(who)} ·
  pack run {fc.html_escape(run_id)}
</p>

<h2>What is being asked</h2>
<div class="card"><p>{fc.html_escape(item['message'])}</p></div>

<h2>The value in question · field <code>{fc.html_escape(item['field'])}</code></h2>
<div class="value"><pre>{fc.html_escape(value_pretty)}</pre></div>

<h2>What editing this re-runs</h2>
<div class="card"><p>{fc.html_escape(rerun)}</p>
<p class="hint">From <code>config/cascade.yaml</code> (spec Section 15). Exact pairs:
<code>python3 scripts/cascade.py --field {fc.html_escape(item['field'])} --item {fc.html_escape(item['item_id'])} --plan</code></p></div>

<h2>Evidence</h2>
{_evidence_html(item)}
{_record_context_html(item, records)}

<h2>Legacy values</h2>
{_legacy_html(item, records)}

{_form_html(item)}
<script>{FORM_JS}</script>
</div></body></html>
"""


def render_index(items, pages, run_id, stats):
    """The pack index: grouped by chapter, in priority order (spec 14/F1 "Group by chapter")."""
    by_chapter = {}
    for item in items:
        key = item["chapter_ids"][0] if item["chapter_ids"] else fc.NO_CHAPTER
        by_chapter.setdefault(key, []).append(item)
    chapter_keys = sorted(by_chapter, key=lambda c: (c == fc.NO_CHAPTER, c))

    sections = []
    for ch in chapter_keys:
        rows = []
        for item in by_chapter[ch]:
            href = pages[item["pack_id"]]
            rows.append(
                f"<tr><td>{item['priority']}</td>"
                f"<td><span class='badge {fc.html_escape(item['severity'] or 'normal')}'>"
                f"{fc.html_escape(item['severity'])}</span></td>"
                f"<td>{fc.html_escape(item['step'])}</td>"
                f"<td><a href='{fc.html_escape(href)}'>{fc.html_escape(item['code'])}</a></td>"
                f"<td><code>{fc.html_escape(item['item_id'])}</code></td>"
                f"<td>{fc.html_escape((item['message'] or '')[:220])}</td></tr>")
        label = "no chapter (intake, registers, whole-paper items)" if ch == fc.NO_CHAPTER else ch
        sections.append(
            f"<h2>{fc.html_escape(label)} <span class='hint'>· {len(by_chapter[ch])} item(s)</span></h2>"
            f"<div class='scroll'><table><thead><tr><th>pri</th><th>sev</th><th>step</th>"
            f"<th>code</th><th>item</th><th>message</th></tr></thead>"
            f"<tbody>{''.join(rows)}</tbody></table></div>")

    prio_rows = "".join(
        f"<tr><td>{fc.html_escape(fc.PRIORITY_LABELS[p])}</td><td>{stats['by_priority'].get(p, 0)}</td></tr>"
        for p in sorted(fc.PRIORITY_LABELS))
    kind_rows = "".join(f"<tr><td>{fc.html_escape(k)}</td><td>{v}</td></tr>"
                        for k, v in sorted(stats["by_kind"].items()))

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Review pack · {fc.html_escape(run_id)}</title>
<style>{CSS}</style></head><body><div class="wrap">
<h1>Review pack</h1>
<p class="meta">run {fc.html_escape(run_id)} · {len(items)} item(s) · audit seed
{stats['seed']} · queue: <code>review/queue.csv</code></p>

<h2>How to use this pack</h2>
<div class="card">
<p>Work top to bottom: the order is the spec's (blockers first, then registers, then subtopic
lists and change-log rows, then high, normal, E0 findings, and last the low items and the audit
sample). Each page shows the value, the evidence, what editing it will re-run, and a form.</p>
<p>Record each decision with <strong>Save in this browser</strong>, come back here, press
<strong>Collect</strong>, and save the result as <code>review/decisions.csv</code>. Then run
<code>python3 scripts/apply_review.py --apply</code>. You can also edit
<code>review/decisions.csv</code> directly in a spreadsheet — the pack never writes to it.</p>
</div>

<h2>Counts</h2>
<div class="scroll"><table><thead><tr><th>priority band</th><th>items</th></tr></thead>
<tbody>{prio_rows}</tbody></table></div>
<div class="scroll" style="margin-top:.75rem"><table><thead><tr><th>kind</th><th>items</th></tr></thead>
<tbody>{kind_rows}</tbody></table></div>

<h2>Collect decisions</h2>
<div class="card">
  <div class="row"><button type="button" onclick="collect()">Collect</button>
  <button type="button" onclick="copyAll()">Copy all</button>
  <button type="button" onclick="clearAll()">Clear</button>
  <span class="hint" id="collected_count"></span></div>
  <textarea id="collected" rows="10" readonly style="margin-top:.6rem"></textarea>
  <p class="hint" id="collected_note"></p>
</div>

{''.join(sections)}
<script>{INDEX_JS}</script>
</div></body></html>
"""


# --------------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------------

def build(chapters=None, seed=AUDIT_SEED, new_only=False, first_full_review=False,
          include_audit=True, dry_run=False, steps_filter=None):
    records = fc.load_records()
    index = fc.qid_index()
    approvals = fc.approval_index()
    chapters_filter = set(chapters) if chapters else None

    items = []
    items += collect_flag_items(records, index, chapters_filter)
    items += collect_subtopic_list_drafts(approvals, chapters_filter)
    items += collect_change_log_drafts(approvals, chapters_filter)
    if include_audit:
        items += collect_audit_sample(records, index, chapters_filter, seed, steps_filter)

    # The E4 agreement sample is drawn ONCE ("in the first full review", spec 14/F1) and then
    # stays in the pack until it has been answered — re-drawing it every run would discard the
    # faculty's partly-finished work, and dropping it after the first run would lose it entirely.
    # So: draw it if it has never been drawn, otherwise re-emit exactly the sample on record.
    if os.path.exists(E4_AGREEMENT_PATH) and not first_full_review:
        e4_items = _rehydrate_e4_agreement(records, chapters_filter)
    else:
        e4_items = collect_e4_agreement(records, index, chapters_filter, seed)
    items += e4_items

    # De-duplicate: a flag and a draft item can describe the same subtopic list. The flag wins
    # (it carries the agent's own message and evidence), and the draft is dropped so the reviewer
    # does not answer the same question twice.
    flagged_subtopic_lists = {i["item_id"] for i in items
                              if i["kind"] == "flag" and i["code"] == "A4_SUBTOPICS_DRAFT"}
    items = [i for i in items if not (i["kind"] == "subtopic_list_draft"
                                      and i["item_id"] in flagged_subtopic_lists)]

    items.sort(key=lambda i: (
        i["priority"],
        (i["chapter_ids"][0] if i["chapter_ids"] else "zzz_" + fc.NO_CHAPTER),
        fc.SEVERITY_RANK.get(i["severity"] or "normal", 9),
        fc.step_index(i["step"] or ""),
        i["pack_id"],
    ))

    prev_manifest = {}
    if os.path.exists(MANIFEST_PATH):
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
                prev_manifest = json.load(f)
        except (OSError, json.JSONDecodeError):
            prev_manifest = {}
    previously_emitted = set(prev_manifest.get("pack_ids") or [])

    emit = items
    if new_only:
        emit = [i for i in items if i["pack_id"] not in previously_emitted]

    run_id = fc.now_iso()
    pages = {i["pack_id"]: _page_filename(i) for i in items}
    stats = {
        "seed": seed,
        "by_priority": {},
        "by_kind": {},
    }
    for i in items:
        stats["by_priority"][i["priority"]] = stats["by_priority"].get(i["priority"], 0) + 1
        stats["by_kind"][i["kind"]] = stats["by_kind"].get(i["kind"], 0) + 1

    queue_rows = [{
        "priority": i["priority"],
        "chapter_id": i["chapter_ids"][0] if i["chapter_ids"] else "",
        "flag_id": i["flag_id"] or i["pack_id"],
        "item_id": i["item_id"],
        "step": i["step"],
        "code": i["code"],
        "severity": i["severity"],
        "message": (i["message"] or "").replace("\n", " "),
        "evidence_page": os.path.join("review", "review_pack", pages[i["pack_id"]]),
    } for i in items]

    result = {
        "run_id": run_id, "seed": seed, "queue_size": len(items), "emitted_pages": len(emit),
        "new_only": new_only, "stats": stats, "chapters": sorted(chapters) if chapters else None,
        "queue_path": os.path.relpath(fc.QUEUE_PATH, fc.PROJECT_ROOT),
        "pack_dir": os.path.relpath(fc.PACK_DIR, fc.PROJECT_ROOT),
        "e4_agreement_items": len(e4_items),
        "audit_items": stats["by_kind"].get("audit_sample", 0),
    }
    if dry_run:
        result["dry_run"] = True
        return result, items

    os.makedirs(fc.PACK_DIR, exist_ok=True)
    lib_io.write_csv(fc.QUEUE_PATH, queue_rows, fc.QUEUE_FIELDS)
    fc.ensure_decisions_file()

    ordered = [i["pack_id"] for i in items]
    for n, item in enumerate(items):
        if item not in emit:
            continue
        prev_href = pages[ordered[n - 1]] if n > 0 else None
        next_href = pages[ordered[n + 1]] if n + 1 < len(ordered) else None
        html = render_item_page(item, records, prev_href, next_href, run_id)
        lib_io.atomic_write_text(os.path.join(fc.PACK_DIR, pages[item["pack_id"]]), html)

    lib_io.atomic_write_text(os.path.join(fc.PACK_DIR, "index.html"),
                             render_index(items, pages, run_id, stats))

    audit_items = [i for i in items if i["kind"] == "audit_sample"]
    if audit_items:
        lib_io.atomic_write_text(AUDIT_SAMPLE_PATH, "".join(
            json.dumps({"run_id": run_id, "seed": seed, "pack_id": i["pack_id"],
                        "step": i["step"], "item_id": i["item_id"],
                        "chapter_ids": i["chapter_ids"], "field": i["field"],
                        "audit": i["audit"]}, ensure_ascii=False) + "\n"
            for i in audit_items))
    if e4_items:
        lib_io.atomic_write_text(E4_AGREEMENT_PATH, "".join(
            json.dumps({"run_id": run_id, "seed": seed, "pack_id": i["pack_id"],
                        "item_id": i["item_id"], "subject": i["e4_agreement"]["subject"],
                        "chapter_ids": i["chapter_ids"]}, ensure_ascii=False) + "\n"
            for i in e4_items))

    lib_io.atomic_write_json(MANIFEST_PATH, {
        "run_id": run_id, "seed": seed, "queue_size": len(items),
        "pack_ids": ordered, "pages": pages,
        "chapters": sorted(chapters) if chapters else None,
    })
    result["orphans_removed"] = _prune_orphan_pages(pages, new_only, chapters_filter)
    return result, items


_PAGE_NAME_RE = re.compile(r"^p[1-7]__.+__[0-9a-f]{8}\.html$")


def _prune_orphan_pages(pages, new_only, chapters_filter):
    """Delete pack pages that are no longer in the pack.

    A page's filename embeds the item's priority and chapter, so when either changes the item
    gets a NEW filename and the old file is orphaned. Found for real on 2026-10-12: a sibling
    agent re-ran D1 between two F1 runs, Q-000015's chapter moved from BIO12-CH03 to BIO12-CH02,
    and the pack ended up with two pages for FL-000093 — the index linked the new one, but anyone
    browsing review/review_pack/ could have opened the stale one and reviewed outdated evidence.

    Only run on a FULL rebuild. On `--new-only` (or a `--chapters` build) the pages this run did
    not consider are legitimately still current, so nothing is removed."""
    if new_only or chapters_filter is not None:
        return 0
    keep = set(pages.values()) | {"index.html"}
    removed = 0
    for name in sorted(os.listdir(fc.PACK_DIR)):
        if name in keep or not _PAGE_NAME_RE.match(name):
            continue
        try:
            os.remove(os.path.join(fc.PACK_DIR, name))
            removed += 1
        except OSError:
            pass
    return removed


def main(argv=None):
    ap = argparse.ArgumentParser(description="F1 · build the review queue and pack (spec 14/F1).")
    ap.add_argument("--chapters", help="Comma-separated chapter ids to scope to.")
    ap.add_argument("--steps", help="Comma-separated steps to scope the AUDIT SAMPLE to.")
    ap.add_argument("--seed", type=int, default=AUDIT_SEED,
                    help=f"Audit-sample seed (default {AUDIT_SEED}; fixed so the sample is reproducible).")
    ap.add_argument("--new-only", action="store_true",
                    help="Only write pages for items not in the previous pack (spec 14/F3 step 6).")
    ap.add_argument("--first-full-review", action="store_true",
                    help="Include the E4 agreement sample (50 questions per subject, tags hidden).")
    ap.add_argument("--no-audit", action="store_true", help="Skip the audit sample.")
    ap.add_argument("--dry-run", action="store_true", help="Report the queue; write nothing.")
    ap.add_argument("--json", action="store_true", help="Machine-readable summary.")
    args = ap.parse_args(argv)

    result, items = build(
        chapters=fc.parse_list_arg(args.chapters),
        seed=args.seed,
        new_only=args.new_only,
        first_full_review=args.first_full_review,
        include_audit=not args.no_audit,
        dry_run=args.dry_run,
        steps_filter=set(fc.parse_list_arg(args.steps) or []) or None,
    )
    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"F1 review pack · run {result['run_id']}")
    print(f"  queue size        : {result['queue_size']}")
    print(f"  pages written     : {result['emitted_pages']}"
          f"{' (--new-only)' if result['new_only'] else ''}"
          f"{' (dry run: none)' if result.get('dry_run') else ''}")
    print(f"  audit sample      : {result['audit_items']} item(s), seed {result['seed']}")
    print(f"  E4 agreement      : {result['e4_agreement_items']} item(s)")
    print("  by priority:")
    for p in sorted(fc.PRIORITY_LABELS):
        print(f"    {fc.PRIORITY_LABELS[p]:<70s} {result['stats']['by_priority'].get(p, 0)}")
    print("  by kind:")
    for k, v in sorted(result["stats"]["by_kind"].items()):
        print(f"    {k:<70s} {v}")
    if not result.get("dry_run"):
        if result.get("orphans_removed"):
            print(f"  stale pages removed: {result['orphans_removed']} "
                  f"(an item's priority or chapter changed since the last pack)")
        print(f"  queue             : {result['queue_path']}")
        print(f"  pack              : {result['pack_dir']}/index.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
