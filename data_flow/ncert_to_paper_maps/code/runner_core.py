"""Shared machinery for scripts/run_step.py, scripts/run_stage.py and scripts/status_cmd.py:
config loading, schema validation, status/flag/run_log writers, the "needs this step" rule
(spec 5.9), and small path/filename helpers used by more than one step plugin.

Deliberately NOT part of scripts/lib/ (that package is owned by a different, already-complete
build pass) — this is the M2/M3 runner's own internals, importable by run_step.py, run_stage.py,
status_cmd.py, scripts/step_plugins.py and scripts/checks/*.py alike.
"""
import csv
import datetime
import functools
import importlib.util
import json
import os
import re
import sys
import uuid

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from lib import flags as lib_flags  # noqa: E402
from lib import io as lib_io  # noqa: E402
from lib import status as lib_status  # noqa: E402

try:
    import yaml
except ImportError as e:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required (pip install pyyaml into the project venv: "
        ".venv/bin/pip install pyyaml). Original error: " + str(e)
    )

try:
    import jsonschema
except ImportError as e:  # pragma: no cover
    raise SystemExit(
        "jsonschema is required (pip install jsonschema into the project venv: "
        ".venv/bin/pip install jsonschema). Original error: " + str(e)
    )


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

def pp(*parts):
    """project_path, re-exported for convenience (always reads lib_io.PROJECT_ROOT fresh, so
    tests that monkeypatch lib_io.PROJECT_ROOT work transparently)."""
    return lib_io.project_path(*parts)


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


# ---------------------------------------------------------------------------
# config/steps.yaml
# ---------------------------------------------------------------------------

_CONFIG_CACHE = None


def load_steps_config(force_reload=False):
    global _CONFIG_CACHE
    if _CONFIG_CACHE is None or force_reload:
        path = pp("config", "steps.yaml")
        with open(path, "r", encoding="utf-8") as f:
            _CONFIG_CACHE = yaml.safe_load(f) or {}
    return _CONFIG_CACHE


def get_step_cfg(step):
    cfg = load_steps_config()
    if step not in cfg:
        raise SystemExit(
            f"unknown step {step!r}. Known steps: {', '.join(cfg.keys())}"
        )
    return cfg[step]


def step_kind(cfg):
    """Classify a step's steps.yaml `agent` field: 'script' (pure script, --auto only),
    'people' (Stage F, out of scope for this runner), 'hybrid' (script + agent, e.g. 'script |
    a5-passage-linker' or 'script + x-adjudicator'), or the single agent name (agent-driven)."""
    agent = (cfg.get("agent") or "").strip()
    if agent == "script":
        return "script"
    if agent == "PEOPLE":
        return "people"
    if "|" in agent or "+" in agent:
        return "hybrid"
    return agent  # a single agent name, e.g. "a1-book-registrar"


# ---------------------------------------------------------------------------
# prompt_version.txt
# ---------------------------------------------------------------------------

def get_prompt_version(step):
    path = pp("steps", step, "prompt_version.txt")
    if not os.path.exists(path):
        ensure_dir(os.path.dirname(path))
        with open(path, "w", encoding="utf-8") as f:
            f.write("v1\n")
        return "v1"
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip() or "v1"


# ---------------------------------------------------------------------------
# schemas/<STEP>.json
# ---------------------------------------------------------------------------

_SCHEMA_CACHE = {}


def load_schema(step):
    if step not in _SCHEMA_CACHE:
        path = pp("schemas", f"{step}.json")
        with open(path, "r", encoding="utf-8") as f:
            _SCHEMA_CACHE[step] = json.load(f)
    return _SCHEMA_CACHE[step]


def validate_schema(step, data):
    """Returns (ok: bool, message: str). message is 'ok' on success, else the first
    jsonschema error formatted for a human (and for run_log.csv's check_message column)."""
    schema = load_schema(step)
    validator = jsonschema.Draft7Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if not errors:
        return True, "ok"
    e = errors[0]
    loc = "/".join(str(p) for p in e.path) or "<root>"
    return False, f"schema: at {loc}: {e.message}"


# ---------------------------------------------------------------------------
# scripts/checks/<STEP>.py — dynamic import
# ---------------------------------------------------------------------------

_CHECK_MODULE_CACHE = {}


def load_check_module(step):
    if step in _CHECK_MODULE_CACHE:
        return _CHECK_MODULE_CACHE[step]
    path = pp("scripts", "checks", f"{step}.py")
    spec = importlib.util.spec_from_file_location(f"pyq_checks_{step}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _CHECK_MODULE_CACHE[step] = module
    return module


def run_step_check(step, data, context):
    """Call scripts/checks/<STEP>.py::check(data, context) -> (bool, str). Any exception from
    the check module is caught and turned into a failing (False, message) result rather than
    crashing the runner — a broken check script must not take down --check for every other item."""
    try:
        module = load_check_module(step)
        return module.check(data, context)
    except Exception as e:  # noqa: BLE001
        return False, f"check script raised {type(e).__name__}: {e}"


# ---------------------------------------------------------------------------
# Flag-code parsing convention (see scripts/checks/*.py docstrings): a failing check's message
# is a "; "-joined list of segments, each optionally "<FLAG_CODE>: <detail>" using one of the
# step's own flags.yaml codes. Segments with no recognised code are generic failures.
# ---------------------------------------------------------------------------

_SEGMENT_RE = re.compile(r"^([A-Z][A-Z0-9_]*):\s*(.*)$")


def parse_check_message(step_cfg, message):
    """Split a failing check's message into segments, tagging each with a known flag code from
    step_cfg['flags'] when its prefix matches one. Returns a list of (code_or_None, detail)."""
    known_codes = set((step_cfg.get("flags") or {}).keys())
    segments = []
    for part in (message or "").split("; "):
        part = part.strip()
        if not part:
            continue
        m = _SEGMENT_RE.match(part)
        if m and m.group(1) in known_codes:
            segments.append((m.group(1), m.group(2)))
        else:
            segments.append((None, part))
    return segments or [(None, message or "check failed")]


# ---------------------------------------------------------------------------
# status / flags / run_log writers
# ---------------------------------------------------------------------------

def status_dir(step):
    return pp("steps", step, "status")


def pending_marker_path(step, item_id):
    return os.path.join(status_dir(step), f"{item_id}.pending.json")


def write_pending(step, item_id, info):
    ensure_dir(status_dir(step))
    lib_io.atomic_write_json(pending_marker_path(step, item_id), info)


def read_pending(step, item_id):
    path = pending_marker_path(step, item_id)
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def clear_pending(step, item_id):
    path = pending_marker_path(step, item_id)
    if os.path.exists(path):
        os.remove(path)


def write_item_status(step, item_id, status, prompt_version, extra=None):
    payload = {"prompt_version": prompt_version}
    if extra:
        payload.update(extra)
    lib_status.write_status(step, item_id, status, extra=payload)
    clear_pending(step, item_id)


def read_item_status(step, item_id):
    return lib_status.read_status(step, item_id)


def raise_flag(item_type, item_id, step, code, severity, message, provisional_value=None,
               evidence=None, prompt_version=None):
    return lib_flags.raise_flag(
        item_type=item_type, item_id=item_id, step=step, code=code, severity=severity,
        message=message, provisional_value=provisional_value, evidence=evidence,
        prompt_version=prompt_version,
    )


_RUN_LOG_FIELDS = [
    "run_id", "item_id", "step", "run", "agent", "prompt_version", "started_at", "ended_at",
    "check", "check_message", "retry_of", "status_after",
]


def append_run_log(item_id, step, run, agent, prompt_version, started_at, ended_at, check,
                    check_message, retry_of, status_after):
    row = {
        "run_id": f"RL-{uuid.uuid4().hex[:12]}",
        "item_id": item_id, "step": step, "run": run, "agent": agent or "",
        "prompt_version": prompt_version or "", "started_at": started_at, "ended_at": ended_at,
        "check": check, "check_message": check_message or "", "retry_of": retry_of or "",
        "status_after": status_after,
    }
    lib_io.append_csv_row(pp("run_log.csv"), row, _RUN_LOG_FIELDS)
    return row


def now_iso():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


# ---------------------------------------------------------------------------
# NCERT input-file path parsing, shared by several Stage A plugins
# ---------------------------------------------------------------------------

_CHAPTER_NUM_PATTERNS = [
    re.compile(r"Chapter_(\d+)", re.IGNORECASE),
    re.compile(r"CH-(\d+)", re.IGNORECASE),
    # Class-11 older edition, both shapes seen in the real drop (2026-10-12):
    #   "10 9. Biomolecules.pdf"            -> sort-order prefix 10, chapter 9
    #   "11. Thermal Properties Of Matter.pdf" -> no prefix, chapter 11
    # The chapter number is the digit run followed by a DOT, which is what separates it from
    # both the sort-order prefix (digits + space, no dot) and from the front/back matter, whose
    # names carry a bare prefix number and no chapter number at all:
    #   "1 Prelims.pdf", "10 Appendices.pdf", "11 Answers.pdf"  -> no match, correctly None.
    # Requiring the dot is what stops those three being mis-registered as chapters 1, 10 and 11.
    re.compile(r"^(?:\d+\s+)?(\d+)\.\s"),
]

# Class-11 older Chemistry is published as two part volumes and copied that way (P1/, P2/).
# Each volume's filenames re-number its chapters from 1, so the filename number is an
# IN-VOLUME number, not the book's chapter number. Verified directly against the PDFs' own
# text: P2's "2 1. Redox Reactions.pdf" is UNIT 8, "3 2. Hydrogen.pdf" is UNIT 9,
# "5 4. The p-Block Elements.pdf" is UNIT 11, "7 6. Hydrocarbons.pdf" is UNIT 13,
# "8 7. Environmental Chemistry.pdf" is UNIT 14, and P2's own Answers.pdf indexes UNIT 8 and
# UNIT 12 — i.e. P2 continues from P1's last chapter (7), it does not restart the book.
# Taking the filename number at face value would register chapters 1-7 TWICE for Chemistry
# Class 11 older and silently lose seven real chapters, so the offset below is applied.
_PART_VOLUME_RE = re.compile(r"^P(\d+)$", re.IGNORECASE)

_EDITION_FOLDER_TO_CODE = {"latest": "latest", "older": "older", "lab_manuals": "lab_manual"}


def _filename_chapter_num(filename):
    """The chapter number written in the filename itself, with no part-volume correction."""
    stem = os.path.splitext(filename)[0]
    for pat in _CHAPTER_NUM_PATTERNS:
        m = pat.search(stem)
        if m:
            return int(m.group(1))
    return None


@functools.lru_cache(maxsize=None)
def _part_volume_offset(subject_abspath, part_dir):
    """How many chapters precede part volume `part_dir` of the book at `subject_abspath`.

    Derived from the real files on disk — the number of chapter PDFs in every lower-numbered
    part volume — never a hardcoded constant, so a drop with different volume splits stays
    correct. Returns 0 for the first volume, or if the sibling volumes can't be read.
    """
    m = _PART_VOLUME_RE.match(part_dir)
    if not m or not os.path.isdir(subject_abspath):
        return 0
    this_part = int(m.group(1))
    offset = 0
    for sibling in sorted(os.listdir(subject_abspath)):
        sm = _PART_VOLUME_RE.match(sibling)
        sib_path = os.path.join(subject_abspath, sibling)
        if not sm or not os.path.isdir(sib_path) or int(sm.group(1)) >= this_part:
            continue
        offset += sum(1 for fn in os.listdir(sib_path)
                      if fn.lower().endswith(".pdf")
                      and _filename_chapter_num(fn) is not None)
    return offset


def extract_chapter_num(filename, relpath=None):
    """Pull a chapter number out of any of this project's real older/latest filename patterns
    (Chapter_N.pdf, CH-N.pdf, Old_ncert_<Subj>_Chapter_N.pdf — docs/OPEN_QUESTIONS.md,
    2026-10-09 'older-edition filename inconsistency'; plus the Class-11 older
    "<sort order> <chapter>. <Title>.pdf" shape — 2026-10-12). Returns None when the file
    carries no chapter number at all, which for real front/back matter (Prelims, Appendices,
    Answers) is the correct answer, not a failure.

    `relpath` is the file's path relative to inputs/ncert/. Pass it whenever it is available:
    it is what lets a part-volume book (Class-11 older Chemistry, P1/P2) be numbered across the
    whole book rather than restarting at 1 in each volume. Without it, a part-volume file's
    in-volume number is returned as-is.
    """
    num = _filename_chapter_num(filename)
    if num is None or not relpath:
        return num
    parts = relpath.replace(os.sep, "/").split("/")
    # .../<edition>/<Class_Nth>/<Subject>/[<part volume>/]<filename>
    if len(parts) >= 5 and _PART_VOLUME_RE.match(parts[-2]):
        subject_abspath = pp("inputs", "ncert", *parts[:-2])
        num += _part_volume_offset(subject_abspath, parts[-2])
    return num


def parse_ncert_relpath(relpath):
    """relpath is a path like 'latest/Class_12th/Chemistry/Chapter_1.pdf', relative to
    inputs/ncert/. Returns a dict with edition_folder, edition_code, class_num, subject,
    filename, chapter_num (any of which may be None if the path doesn't match the expected
    shape) — never raises, so a stray file in inputs/ncert/ can't crash enumeration."""
    parts = relpath.replace(os.sep, "/").split("/")
    out = {
        "edition_folder": None, "edition_code": None, "class_num": None, "subject": None,
        "filename": parts[-1] if parts else relpath, "chapter_num": None,
    }
    if len(parts) >= 1:
        out["edition_folder"] = parts[0]
        out["edition_code"] = _EDITION_FOLDER_TO_CODE.get(parts[0])
    if len(parts) >= 2:
        m = re.match(r"Class_(\d+)", parts[1])
        if m:
            out["class_num"] = int(m.group(1))
    if len(parts) >= 3:
        out["subject"] = parts[2]
    out["chapter_num"] = extract_chapter_num(out["filename"], relpath)
    return out


def ncert_item_id(relpath):
    """Deterministic item_id for an inputs/ncert/... file, used by A1/A2 as the pre-registration
    item identity (before a book_id exists): the path relative to inputs/ncert/, '/' -> '__',
    extension stripped."""
    stem = os.path.splitext(relpath.replace(os.sep, "/"))[0]
    return stem.replace("/", "__")


def iter_ncert_files():
    """Yield every PDF under inputs/ncert/{latest,older,lab_manuals}/, sorted, as
    (relpath_from_inputs_ncert, absolute_path)."""
    root = pp("inputs", "ncert")
    for edition_dir in ("latest", "older", "lab_manuals"):
        base = os.path.join(root, edition_dir)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames.sort()
            for fn in sorted(filenames):
                if fn.lower().endswith(".pdf"):
                    abspath = os.path.join(dirpath, fn)
                    relpath = os.path.relpath(abspath, root)
                    yield relpath, abspath


# ---------------------------------------------------------------------------
# Readiness gates between steps that don't share one item-id space (documented judgment calls;
# see docs/OPEN_QUESTIONS.md). Steps I own both ends of (A1..A9) use real per-item status files
# instead (see step_plugins.py); this is only for crossing into a step I don't own the producer
# of (S0 -> A1).
# ---------------------------------------------------------------------------

def s0_has_run():
    """S0's spec-mandated Writes artifact (register/intake_report.md) is the one thing every
    downstream step can rely on regardless of intake_check.py's internal item/status scheme
    (which this build does not own — see docs/OPEN_QUESTIONS.md)."""
    return os.path.exists(pp("register", "intake_report.md"))


# ---------------------------------------------------------------------------
# Filters (--chapters / --papers / --items)
# ---------------------------------------------------------------------------

def parse_filter_list(value):
    if not value:
        return None
    return {v.strip() for v in value.split(",") if v.strip()}


def item_passes_filters(item_id, filters):
    """filters: dict with optional 'items' (exact-or-substring match against item_id),
    'chapters', 'papers' sets. A step plugin decides which of chapters/papers/items apply to its
    own item space; this helper only implements the matching rule itself."""
    items = filters.get("items")
    if items and not any(token in item_id for token in items):
        return False
    chapters = filters.get("chapters")
    if chapters and not any(token in item_id for token in chapters):
        return False
    papers = filters.get("papers")
    if papers and not any(token in item_id for token in papers):
        return False
    return True
