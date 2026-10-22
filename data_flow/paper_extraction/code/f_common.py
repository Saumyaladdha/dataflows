#!/usr/bin/env python3
"""Shared helpers for Stage F (spec Section 14): review pack, decisions, cascade, counts,
release, scoring.

This module is read-only with respect to agent output. It owns no pipeline decisions; it only
locates and parses state that earlier stages already wrote, plus the Stage-F-owned tables under
`review/` (spec 6.5).

Why this file exists: F1-F6 are six scripts that all need the same few things — the flag file,
the question records, the chapter/subject/year of an arbitrary item id, the step order from
`config/steps.yaml`, and the Stage-F approval ledger. Duplicating that six times would let the
six drift apart, and the release gate (F5) must agree exactly with the queue (F1) about what
"this chapter's queue is empty" means.

Nothing here writes to `data/` (only `export_tables.py` may, spec 6.6) and nothing here edits an
agent's output file (CLAUDE.md "Never edit an agent's output"). Stage F approvals are recorded in
`review/approvals.jsonl`, NOT by rewriting the `approval` field inside `ncert/subtopics/*.json`
or `ncert/change_log.csv` — see `load_approvals()` for the reasoning.
"""
import datetime
import fcntl
import glob
import hashlib
import json
import os
import re
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from lib import io as lib_io  # noqa: E402

PROJECT_ROOT = lib_io.PROJECT_ROOT


def pp(*parts):
    """Join path components onto the project root."""
    return os.path.join(PROJECT_ROOT, *parts)


def now_iso():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def today_iso():
    return datetime.date.today().isoformat()


# ---------------------------------------------------------------------------
# config/steps.yaml — step order (= stage order, since steps.yaml is written in stage order)
# ---------------------------------------------------------------------------

_STEPS_CACHE = None


def load_steps():
    """Return config/steps.yaml as an ordered dict {STEP: cfg}. Python dicts preserve insertion
    order and PyYAML preserves document order, so iteration order IS stage order (S0, A1..A9,
    B1..B9, C1, D1..D11, E0..E6, F1..F5) — which is exactly what F3's "run the stale (item, step)
    pairs in stage order" needs."""
    global _STEPS_CACHE
    if _STEPS_CACHE is None:
        import yaml  # imported lazily so a caller that never needs steps.yaml needs no PyYAML
        with open(pp("config", "steps.yaml"), "r", encoding="utf-8") as f:
            _STEPS_CACHE = yaml.safe_load(f) or {}
    return _STEPS_CACHE


def step_order():
    """Every step code in stage order."""
    return list(load_steps().keys())


def step_index(step):
    """Position of `step` in stage order; unknown steps sort after every known one."""
    order = step_order()
    try:
        return order.index(step)
    except ValueError:
        return len(order) + 1


def step_item_kind(step):
    """The `item:` field of a step ("question", "chapter", "subtopic", "page", ...)."""
    return (load_steps().get(step) or {}).get("item")


def stage_of(step):
    return str((load_steps().get(step) or {}).get("stage", ""))


# ---------------------------------------------------------------------------
# flags/flags.jsonl
# ---------------------------------------------------------------------------

FLAGS_PATH = pp("flags", "flags.jsonl")
OPEN_STATUSES = ("open",)
CLOSED_STATUSES = ("closed", "auto_closed", "blocked_by_reviewer")


def load_flags(path=None):
    """Every flag in flags/flags.jsonl, in file order."""
    return list(lib_io.read_jsonl(path or FLAGS_PATH))


def open_flags(path=None):
    return [f for f in load_flags(path) if f.get("status") == "open"]


def save_flags(flags, path=None):
    """Rewrite flags.jsonl atomically, holding an exclusive lock on <path>.lock for the duration.

    Rewriting (rather than appending) is correct here and is not "editing an agent's output":
    spec 5.6 gives every flag mutable `status` / `decision` / `reviewer` / `decided_at` fields
    precisely so Stage F can close it. The lock exists because other stages append flags
    concurrently; without it a concurrent append between our read and our write would be lost."""
    path = path or FLAGS_PATH
    lib_io.ensure_parent(path)
    lock_path = path + ".lock"
    with open(lock_path, "a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        try:
            body = "".join(json.dumps(f, ensure_ascii=False) + "\n" for f in flags)
            lib_io.atomic_write_text(path, body)
        finally:
            fcntl.flock(lock.fileno(), fcntl.LOCK_UN)


SEVERITY_RANK = {"blocker": 0, "high": 1, "normal": 2, "low": 3}


# Flag codes that F1's ordering treats specially (spec 14/F1 "Order"):
#   (2) book and paper registers
REGISTER_CODES = {
    "A1_REGISTER_DRAFT", "A1_REPRINT_NOT_FOUND", "A1_EDITION_MISMATCH",
    "B1_REGISTER_DRAFT", "B1_MANIFEST_MISMATCH",
}
#   (3) subtopic lists and change-log rows
SUBTOPIC_CHANGELOG_CODES = {"A4_SUBTOPICS_DRAFT", "A8_FACT_CHANGE", "A8_WORDING_RISK", "A9_CHANGE_LOG_ROW"}
#   (6) E0 findings and new categories
E0_CODES = {"E0_FINDINGS_READY", "E_NEW_CATEGORY"}
#   (7) the audit sample
AUDIT_CODE = "AUDIT_SAMPLE"


def priority_of(flag):
    """F1's strict ordering, spec 14/F1: (1) blocker; (2) registers; (3) subtopic lists and
    change-log rows; (4) high; (5) normal; (6) E0 findings and new categories; (7) low and the
    audit sample.

    The order of these tests is load-bearing. A4_SUBTOPICS_DRAFT and E_NEW_CATEGORY are both
    severity `normal`, but one belongs in band 3 (ahead of every `high`) and the other in band 6
    (behind every `normal`), so the code-specific tests must run before the severity tests — and
    `blocker` must run before everything, because a blocker on a register row is still a blocker.
    """
    code = flag.get("code") or ""
    severity = flag.get("severity") or "normal"
    if severity == "blocker":
        return 1
    if code in REGISTER_CODES:
        return 2
    if code in SUBTOPIC_CHANGELOG_CODES or flag.get("item_type") in ("subtopic_list", "change_log_row"):
        return 3
    if code in E0_CODES:
        return 6
    if code == AUDIT_CODE:
        return 7
    if severity == "high":
        return 4
    if severity == "normal":
        return 5
    return 7


PRIORITY_LABELS = {
    1: "1 · blocker",
    2: "2 · book and paper registers",
    3: "3 · subtopic lists and change-log rows",
    4: "4 · high (answers, keys, misreads, evidence, changed answers, corrections)",
    5: "5 · normal",
    6: "6 · E0 findings and new categories",
    7: "7 · low and audit sample",
}


# ---------------------------------------------------------------------------
# papers/records/<QID>.json
# ---------------------------------------------------------------------------

RECORDS_DIR = pp("papers", "records")


def load_records():
    """Every question record as {qid: record}, including records absorbed by a C1 merge."""
    out = {}
    if not os.path.isdir(RECORDS_DIR):
        return out
    for path in sorted(glob.glob(os.path.join(RECORDS_DIR, "Q-*.json"))):
        try:
            with open(path, "r", encoding="utf-8") as f:
                rec = json.load(f)
        except (OSError, json.JSONDecodeError):
            continue
        qid = rec.get("question_id") or os.path.splitext(os.path.basename(path))[0]
        out[qid] = rec
    return out


def is_canonical(rec):
    """A record absorbed into another by a C1 booklet merge carries `merged_into` and must not be
    counted twice (that is how `exports/.../questions.csv` gets the real unique count)."""
    return not rec.get("merged_into")


def canonical_records(records=None):
    records = load_records() if records is None else records
    return {q: r for q, r in records.items() if is_canonical(r)}


def qid_index():
    """papers/records/_qid_index.json: "{PAPER}#{QNO}" -> QID."""
    path = os.path.join(RECORDS_DIR, "_qid_index.json")
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}


def record_chapter_ids(rec):
    """A record's chapter ids.

    Spec 6.3 names the field `chapter_ids`; the D1 plugin as actually built writes
    `d1_chapter_ids` (verified on the real records, 2026-10-12). Read both, spec name first, so
    Stage F works either way and keeps working when D1 is reconciled with the spec."""
    for key in ("chapter_ids", "d1_chapter_ids"):
        v = rec.get(key)
        if v:
            return list(v)
    return []


def record_subtopic_ids(rec):
    """A record's subtopic ids — spec 6.3's `subtopic_ids`, or D1/D2-as-built's
    `d2_subtopic_ids`. Same reasoning as record_chapter_ids()."""
    for key in ("subtopic_ids", "d2_subtopic_ids"):
        v = rec.get(key)
        if v:
            return list(v)
    return []


# ---------------------------------------------------------------------------
# Item id -> chapter / subject / year
#
# Every step names its items differently (spec 5.8 only fixes the folder, not the id shape).
# These are the shapes that exist in the real pipeline today, confirmed by reading
# steps/*/status/ and flags/flags.jsonl on 2026-10-12:
#
#   Q-000015                              a question
#   Q-000001|Q-000006                     a C1 cross-code pair
#   SKIP:NEET|2023|MAIN                   a C1 sitting with nothing to merge
#   NEET-2023-MAIN-E1-q0003               a paper question before it has a QID
#   NEET-2023-MAIN-E1-p001                a paper page
#   NEET-2023-MAIN-E1                     a paper
#   BIO12L-ch01-p001                      a book page   (A2)
#   BIO12L-ch01-p001|BIO12L-ch01-p002     a page pair   (A2 join)
#   BIO12L-ch01-s01                       a book section (A3)
#   BIO12L-CH01-P89                       a passage
#   BIO12-CH01-ST03                       a subtopic
#   BIO12-CH01                            a chapter     (A4)
#   BIO12L                                a book
#   latest__Class_11th__Biology__Chapter_1   an A1 book-registration item
#   inputs__papers__neet_2023_code-E1        a B1 paper-registration item
#   paper-2024-MAIN / key-2016-PH2 / labmanual-Physics / inputs   S0 intake items
# ---------------------------------------------------------------------------

SUBJECT_BY_PREFIX = {"BIO": "Biology", "CHE": "Chemistry", "PHY": "Physics"}

_RE_QID = re.compile(r"^Q-\d{6}$")
_RE_PAPER_Q = re.compile(r"^(NEET-(\d{4})-[A-Z0-9]+-[A-Za-z0-9]+)-q0*(\d+)$")
_RE_PAPER_P = re.compile(r"^(NEET-(\d{4})-[A-Z0-9]+-[A-Za-z0-9]+)-p\d+$")
_RE_PAPER = re.compile(r"^NEET-(\d{4})-[A-Z0-9]+(?:-[A-Za-z0-9]+)?$")
_RE_BOOK_PAGE = re.compile(r"^([A-Z]{3})(\d{2})([LOM])-ch(\d+)-(?:p|s)\d+$")
_RE_PASSAGE = re.compile(r"^([A-Z]{3})(\d{2})([LOM])-CH(\d+)-P\d+$")
_RE_SUBTOPIC = re.compile(r"^([A-Z]{3})(\d{2})-CH(\d+)-ST\d+$")
_RE_CHAPTER = re.compile(r"^([A-Z]{3})(\d{2})-CH(\d+)$")
_RE_BOOK = re.compile(r"^([A-Z]{3})(\d{2})([LOM])$")
_RE_A1_ITEM = re.compile(r"^(latest|older|lab_?manual)__Class_(\d+)(?:th|st|nd|rd)__([A-Za-z]+)__", re.I)
_RE_S0_YEAR = re.compile(r"^(?:paper|key)-(\d{4})-")
_RE_ANY_YEAR = re.compile(r"(?:^|[^0-9])((?:19|20)\d{2})(?:[^0-9]|$)")

NO_CHAPTER = "_no_chapter"


def _chapter_from_subj_class_num(subj3, klass, num):
    subject_prefix = subj3.upper()
    if subject_prefix not in SUBJECT_BY_PREFIX:
        return None
    return f"{subject_prefix}{int(klass):02d}-CH{int(num):02d}"


def item_parts(item_id):
    """Split a composite item id (`A|B`) into its parts; a plain id yields one part."""
    if item_id is None:
        return []
    raw = str(item_id)
    if raw.startswith("SKIP:"):
        raw = raw[len("SKIP:"):]
    return [p for p in raw.split("|") if p]


def item_chapter_ids(item_id, records=None, index=None):
    """Best-effort chapter ids for an arbitrary item id, for F1's "Group by chapter" and F5's
    per-chapter release gate. Returns [] when the item genuinely has no chapter (an intake item,
    a paper register row, a whole-inputs item) — F1 groups those under NO_CHAPTER rather than
    guessing."""
    records = load_records() if records is None else records
    index = qid_index() if index is None else index
    out = []
    for part in item_parts(item_id):
        if _RE_QID.match(part):
            rec = records.get(part)
            if rec:
                out.extend(record_chapter_ids(rec))
            continue
        m = _RE_PAPER_Q.match(part)
        if m:
            qid = index.get(f"{m.group(1)}#{int(m.group(3))}")
            rec = records.get(qid) if qid else None
            if rec:
                out.extend(record_chapter_ids(rec))
            continue
        for rx in (_RE_PASSAGE, _RE_BOOK_PAGE):
            m = rx.match(part)
            if m:
                ch = _chapter_from_subj_class_num(m.group(1), m.group(2), m.group(4))
                if ch:
                    out.append(ch)
                break
        else:
            m = _RE_SUBTOPIC.match(part) or _RE_CHAPTER.match(part)
            if m:
                ch = _chapter_from_subj_class_num(m.group(1), m.group(2), m.group(3))
                if ch:
                    out.append(ch)
                continue
            m = _RE_A1_ITEM.match(part)
            if m:
                subject = m.group(3).title()
                prefix = {v: k for k, v in SUBJECT_BY_PREFIX.items()}.get(subject)
                chno = re.search(r"Chapter[_ ]?(\d+)", part, re.I)
                if prefix and chno:
                    out.append(f"{prefix}{int(m.group(2)):02d}-CH{int(chno.group(1)):02d}")
                continue
    seen, uniq = set(), []
    for c in out:
        if c not in seen:
            seen.add(c)
            uniq.append(c)
    return uniq


def item_subject_year(item_id, records=None, index=None):
    """(subject, year) for an arbitrary item id, used only to stratify F1's audit sample.
    Either half may be None — a book page has a subject but no exam year, an intake item for a
    whole paper has a year but no subject. `None` is a stratum of its own, never a guess."""
    records = load_records() if records is None else records
    index = qid_index() if index is None else index
    subject = None
    year = None
    for part in item_parts(item_id):
        rec = None
        if _RE_QID.match(part):
            rec = records.get(part)
        else:
            m = _RE_PAPER_Q.match(part)
            if m:
                year = year or int(m.group(2))
                qid = index.get(f"{m.group(1)}#{int(m.group(3))}")
                rec = records.get(qid) if qid else None
        if rec:
            subject = subject or rec.get("subject")
            year = year or rec.get("year")
            continue
        for rx in (_RE_PAPER_P, _RE_PAPER):
            m = rx.match(part)
            if m:
                year = year or int(m.group(2) if rx is _RE_PAPER_P else m.group(1))
                break
        for rx in (_RE_PASSAGE, _RE_BOOK_PAGE, _RE_BOOK):
            m = rx.match(part)
            if m:
                subject = subject or SUBJECT_BY_PREFIX.get(m.group(1))
                break
        for rx in (_RE_SUBTOPIC, _RE_CHAPTER):
            m = rx.match(part)
            if m:
                subject = subject or SUBJECT_BY_PREFIX.get(m.group(1))
                break
        m = _RE_A1_ITEM.match(part)
        if m:
            subject = subject or m.group(3).title()
        m = _RE_S0_YEAR.match(part)
        if m:
            year = year or int(m.group(1))
        if subject is None:
            for name in SUBJECT_BY_PREFIX.values():
                if name.lower() in part.lower():
                    subject = name
                    break
        if year is None:
            m = _RE_ANY_YEAR.search(part)
            if m:
                year = int(m.group(1))
    return subject, year


# ---------------------------------------------------------------------------
# Step status files
# ---------------------------------------------------------------------------

def iter_step_statuses(step):
    """Yield (item_id, status_dict) for every real status file of a step.

    Several steps keep side-car files next to their statuses (`<ITEM>.last_block.json` for A2,
    `<ITEM>.last_q.json` for B2) that are carry-over state, not statuses. They are recognised by
    having no `status` key, not by their filename, so a new side-car shape cannot be miscounted
    as a passing item."""
    d = pp("steps", step, "status")
    if not os.path.isdir(d):
        return
    for path in sorted(glob.glob(os.path.join(d, "*.json"))):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(data, dict) or "status" not in data:
            continue
        item_id = data.get("item_id") or os.path.splitext(os.path.basename(path))[0]
        yield item_id, data


def steps_with_status():
    """Every step that has at least one status file, in stage order."""
    present = []
    for step in step_order():
        if os.path.isdir(pp("steps", step, "status")):
            if any(True for _ in iter_step_statuses(step)):
                present.append(step)
    return present


# ---------------------------------------------------------------------------
# Drafts that need approval but are not flags
# ---------------------------------------------------------------------------

def subtopic_list_drafts():
    """Every ncert/subtopics/<CHAPTER>.json and its own `approval` value (spec 6.4).

    A4 also raises A4_SUBTOPICS_DRAFT per chapter, so in a healthy pipeline these two agree. They
    are collected separately anyway because F5's gate is phrased over the subtopic LIST ("its
    subtopic list ... approved"), and a chapter whose A4 flag was closed without an approval
    decision must still fail that gate."""
    out = []
    for path in sorted(glob.glob(pp("ncert", "subtopics", "*.json"))):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError):
            continue
        chapter_id = data.get("chapter_id") or os.path.splitext(os.path.basename(path))[0]
        out.append({
            "chapter_id": chapter_id,
            "path": os.path.relpath(path, PROJECT_ROOT),
            "approval_in_file": data.get("approval"),
            "version": data.get("version"),
            "subtopics": data.get("subtopics") or [],
        })
    return out


def change_log_rows():
    """Every row of ncert/change_log.csv (spec 6.4). Header-only file -> []."""
    return lib_io.read_csv(pp("ncert", "change_log.csv"))


# ---------------------------------------------------------------------------
# review/ tables (spec 6.5) — Stage F owns these outright
# ---------------------------------------------------------------------------

REVIEW_DIR = pp("review")
QUEUE_PATH = os.path.join(REVIEW_DIR, "queue.csv")
PACK_DIR = os.path.join(REVIEW_DIR, "review_pack")
DECISIONS_PATH = os.path.join(REVIEW_DIR, "decisions.csv")
CORRECTIONS_PATH = os.path.join(REVIEW_DIR, "corrections.jsonl")
RELEASES_PATH = os.path.join(REVIEW_DIR, "releases.csv")
APPROVALS_PATH = os.path.join(REVIEW_DIR, "approvals.jsonl")
APPLIED_PATH = os.path.join(REVIEW_DIR, "applied_decisions.jsonl")
BLOCKS_PATH = os.path.join(REVIEW_DIR, "blocks.jsonl")
CASCADE_LOG_PATH = os.path.join(REVIEW_DIR, "cascade_log.jsonl")

QUEUE_FIELDS = ["priority", "chapter_id", "flag_id", "item_id", "step", "code", "severity",
                "message", "evidence_page"]
DECISION_FIELDS = ["flag_id_or_item", "field", "decision", "corrected_value_json", "reviewer",
                   "comment", "decided_at"]
RELEASE_FIELDS = ["chapter_id", "released_at", "signed_by", "gold_score_snapshot", "open_flags"]

DECISION_VALUES = ("approve", "correct", "edit", "block")


def read_decisions(path=None):
    return lib_io.read_csv(path or DECISIONS_PATH)


def ensure_decisions_file(path=None):
    """Create review/decisions.csv with just a header if it does not exist, so a reviewer can
    open it in a spreadsheet straight away. Never touches an existing file."""
    path = path or DECISIONS_PATH
    if not os.path.exists(path):
        lib_io.write_csv(path, [], DECISION_FIELDS)
    return path


def decision_digest(row):
    """A stable fingerprint of one decisions.csv row, so `apply_review.py` can tell a NEW row
    from one it has already applied (spec 14/F3 step 1: "read NEW rows"). Deliberately covers
    every column: re-deciding the same flag differently later is a genuinely new decision."""
    payload = json.dumps([str(row.get(k, "") or "") for k in DECISION_FIELDS], ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def applied_digests(path=None):
    return {r.get("digest") for r in lib_io.read_jsonl(path or APPLIED_PATH)}


def load_approvals(path=None):
    """review/approvals.jsonl — the Stage F approval ledger.

    JUDGEMENT CALL, recorded here because it is the kind of thing a later reader will question:
    spec 6.4 puts an `approval` field inside `ncert/subtopics/<CHAPTER>.json` (an A4 AGENT output)
    and an `approval` column in `ncert/change_log.csv` (an A9 script output). Writing a reviewer's
    approval into those files would mean Stage F editing an agent's output, which CLAUDE.md
    forbids without qualification. So approvals are recorded only here, and this ledger — not the
    `approval` field in the agent's file — is what F5's release gate reads. Consequence to be
    aware of: `ncert/subtopics/*.json` will keep saying `"approval": "pending"` forever; that
    field is now informational only."""
    return list(lib_io.read_jsonl(path or APPROVALS_PATH))


def approval_index(path=None):
    """{target_key: latest approval record} from review/approvals.jsonl. Later rows win, so a
    re-approval after a correction supersedes the earlier one."""
    idx = {}
    for row in load_approvals(path):
        key = row.get("target")
        if key:
            idx[key] = row
    return idx


def subtopic_list_target(chapter_id):
    return f"subtopic_list:{chapter_id}"


def change_log_target(change_id):
    return f"change_log_row:{change_id}"


def flag_target(flag_id, field=None):
    return f"flag:{flag_id}" + (f":{field}" if field else "")


def load_blocks(path=None):
    """review/blocks.jsonl — non-question items a reviewer blocked (a question's block lives in
    its own record as `release_status = blocked_by_reviewer`, spec 14/F3 step 4, but a chapter or
    a register row has no record to write it into)."""
    return list(lib_io.read_jsonl(path or BLOCKS_PATH))


def blocked_chapters(path=None):
    out = set()
    for row in load_blocks(path):
        for ch in row.get("chapter_ids") or []:
            out.add(ch)
    return out


def read_releases(path=None):
    return lib_io.read_csv(path or RELEASES_PATH)


def signoff_for(chapter_id, path=None):
    """The newest valid sign-off row for a chapter, or None.

    A row counts only if it names this chapter AND has a non-empty `signed_by` AND a non-empty
    `released_at`. An empty `signed_by` is the single most likely way a chapter could be released
    with nobody having actually signed for it, so it is rejected rather than defaulted."""
    best = None
    for row in read_releases(path):
        if (row.get("chapter_id") or "").strip() != chapter_id:
            continue
        if not (row.get("signed_by") or "").strip():
            continue
        if not (row.get("released_at") or "").strip():
            continue
        if best is None or (row.get("released_at") or "") >= (best.get("released_at") or ""):
            best = row
    return best


# ---------------------------------------------------------------------------
# misc
# ---------------------------------------------------------------------------

def parse_list_arg(value):
    if not value:
        return None
    return [p.strip() for p in str(value).split(",") if p.strip()]


def file_digest(path):
    """sha256 of a file's bytes, or None if it does not exist. Used by the cascade to tell
    "re-ran and produced the same output" (no flag) from "re-ran and changed" (flag)."""
    if not os.path.exists(path):
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def step_out_digests(step, item_id):
    """{relpath: sha256} for every output file a step has for an item."""
    out = {}
    pattern = pp("steps", step, "out", f"{item_id}*")
    for path in sorted(glob.glob(pattern)):
        if os.path.isfile(path):
            out[os.path.relpath(path, PROJECT_ROOT)] = file_digest(path)
    return out


def html_escape(s):
    if s is None:
        return ""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;").replace("'", "&#39;"))


if __name__ == "__main__":
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("steps in stage order:", ",".join(step_order()))
    flags = load_flags()
    print(f"flags: {len(flags)} total, {sum(1 for f in flags if f.get('status') == 'open')} open")
    recs = load_records()
    print(f"records: {len(recs)} total, {len(canonical_records(recs))} canonical")
    print("steps with status:", ",".join(steps_with_status()))
    for f in flags[:3]:
        print(" sample:", f["flag_id"], f["code"], "prio", priority_of(f),
              "chapters", item_chapter_ids(f["item_id"], recs),
              "subj/year", item_subject_year(f["item_id"], recs))
