#!/usr/bin/env python3
"""Idempotence proof for run_step.py (spec 5.9: "Running a command twice in a row must do
nothing the second time"), run in an ISOLATED temp project root (not the real, shared one --
this project's real register/, steps/, ncert/ are being mutated concurrently by other build
passes in parallel, so a repeatable automated test needs its own sandbox copy).

Run: .venv/bin/python3 tests/test_run_step.py
(Needs pymupdf/jsonschema/pyyaml, i.e. the project venv -- see scripts/lib/pdf.py.)
"""
import contextlib
import json
import os
import shutil
import sys
import tempfile

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_TESTS_DIR)
_SCRIPTS_DIR = os.path.join(_PROJECT_ROOT, "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402
import step_plugins as sp  # noqa: E402
from lib import flags as lib_flags  # noqa: E402
from lib import ids as lib_ids  # noqa: E402
from lib import io as lib_io  # noqa: E402


def _build_isolated_root():
    """A minimal copy of the real project, just enough for A1 to run against one real PDF:
    config/steps.yaml, schemas/A1.json, scripts/checks/A1.py (+its own lib/ dependency via the
    checks module's `from lib import quote_verify` -- scripts/checks/A1.py reaches scripts/lib
    through runner_core's sys.path bootstrap, which inserts the REAL scripts/ dir, so lib/ itself
    does not need copying), register/intake_report.md (the S0-ready signal), and one real NCERT
    chapter PDF (confirmed to carry a findable 'Reprint 2026-27' stamp on page 1 -- the same file
    a1-book-registrar.md's own worked example uses)."""
    tmp = tempfile.mkdtemp(prefix="run_step_idempotence_")
    for rel in ("config/steps.yaml", "schemas/A1.json", "scripts/checks/A1.py", "scripts/checks/__init__.py"):
        src = os.path.join(_PROJECT_ROOT, rel)
        dst = os.path.join(tmp, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(src, dst)

    os.makedirs(os.path.join(tmp, "register"), exist_ok=True)
    with open(os.path.join(tmp, "register", "intake_report.md"), "w", encoding="utf-8") as f:
        f.write("# fixture intake report\npresent: everything needed for this test\n")

    src_pdf = os.path.join(_PROJECT_ROOT, "inputs", "ncert", "latest", "Class_12th", "Chemistry", "Chapter_1.pdf")
    dst_pdf = os.path.join(tmp, "inputs", "ncert", "latest", "Class_12th", "Chemistry", "Chapter_1.pdf")
    if not os.path.exists(src_pdf):
        raise SystemExit(f"fixture PDF missing: {src_pdf} -- this test needs the real project's "
                           "inputs/ncert/ tree present (it only READS from it, never modifies it).")
    os.makedirs(os.path.dirname(dst_pdf), exist_ok=True)
    shutil.copy(src_pdf, dst_pdf)
    return tmp


@contextlib.contextmanager
def _isolated_project(tmp):
    """Monkeypatch every module-level path this build's lib/ code fixes at IMPORT time, not just
    lib_io.PROJECT_ROOT -- lib/flags.py's FLAGS_PATH and lib/ids.py's COUNTERS_PATH are each
    computed ONCE at import (`FLAGS_PATH = lib_io.project_path(...)`), so patching PROJECT_ROOT
    alone does NOT redirect them; they keep pointing at the real project's flags/flags.jsonl and
    register/counters.json for the rest of the process. (Found by this test polluting the real
    project's flags.jsonl and counters.json on a first draft -- cleaned up by hand; see this
    file's test_a1_retry_chain_resolves_to_safe_default and the report for details.) This mirrors
    the pattern lib/ids.py's own self-check already uses: reassign the module attribute directly,
    not just the thing it was originally computed from."""
    orig_root = lib_io.PROJECT_ROOT
    orig_flags_path = lib_flags.FLAGS_PATH
    orig_counters_path = lib_ids.COUNTERS_PATH
    lib_io.PROJECT_ROOT = tmp
    lib_flags.FLAGS_PATH = os.path.join(tmp, "flags", "flags.jsonl")
    lib_ids.COUNTERS_PATH = os.path.join(tmp, "register", "counters.json")
    rc.load_steps_config(force_reload=True)
    rc._SCHEMA_CACHE.clear()
    rc._CHECK_MODULE_CACHE.clear()
    try:
        yield
    finally:
        lib_io.PROJECT_ROOT = orig_root
        lib_flags.FLAGS_PATH = orig_flags_path
        lib_ids.COUNTERS_PATH = orig_counters_path
        rc.load_steps_config(force_reload=True)
        rc._SCHEMA_CACHE.clear()
        rc._CHECK_MODULE_CACHE.clear()


def test_a1_list_check_idempotence():
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        plugin = sp.A1Plugin()
        filters = {"chapters": None, "papers": None, "items": None}

        # --- --list #1: fresh item, must render and list exactly one line. ---
        lines1 = plugin.list_items(filters)
        assert len(lines1) == 1, f"expected 1 fresh item, got {lines1}"
        item_id = "latest__Class_12th__Chemistry__Chapter_1"
        assert lines1[0].item_id == item_id
        assert lines1[0].agent == "a1-book-registrar"
        assert lines1[0].run_label == "runA"

        work_path = rc.pp("steps", "A1", "work", f"{item_id}.runA.input.json")
        png_path = rc.pp("steps", "A1", "work", f"{item_id}_p1.png")
        assert os.path.exists(work_path) and os.path.exists(png_path)
        work_mtime, png_mtime = os.path.getmtime(work_path), os.path.getmtime(png_path)

        # --- --list #2, same filters, no agent output written yet: MUST do nothing new. ---
        lines2 = plugin.list_items(filters)
        assert lines1 == lines2, "a second --list before any output exists must repeat the same line"
        assert os.path.getmtime(work_path) == work_mtime, "idempotence: must not re-render the work input"
        assert os.path.getmtime(png_path) == png_mtime, "idempotence: must not re-render the page image"

        # --- Simulate the agent writing a valid output (the real stamp on this file's page 1). ---
        agent_output = {
            "subject": "Chemistry", "class": 12, "language": "English", "part": None,
            "edition_seen": "latest", "reprint_text_exact": "Reprint 2026-27",
            "reprint_page": 1, "is_lab_manual": False, "note": "",
        }
        out_path = rc.pp("steps", "A1", "out", f"{item_id}.runA.json")
        lib_io.atomic_write_json(out_path, agent_output)

        # --- --check #1: resolves to pass, writes status/flags/run_log, books.csv row. ---
        new_lines = plugin.check(filters)
        assert new_lines == [], f"expected the check to resolve cleanly, got pending lines {new_lines}"
        status = rc.read_item_status("A1", item_id)
        assert status is not None and status["status"] == "pass", status
        books = lib_io.read_csv(rc.pp("register", "books.csv"))
        assert len(books) == 1 and books[0]["book_id"] == "CHE12L", books

        run_log_rows_after_first_check = lib_io.read_csv(rc.pp("run_log.csv"))
        assert len(run_log_rows_after_first_check) == 1

        # --- --list #3: item is resolved; must NOT be listed again. ---
        lines3 = plugin.list_items(filters)
        assert lines3 == [], f"a resolved item must not be re-listed, got {lines3}"

        # --- --check #2 (same prompt version, nothing changed): must do nothing new at all. ---
        new_lines_2 = plugin.check(filters)
        assert new_lines_2 == []
        run_log_rows_after_second_check = lib_io.read_csv(rc.pp("run_log.csv"))
        assert len(run_log_rows_after_second_check) == len(run_log_rows_after_first_check), (
            "a second --check with nothing new must not append a new run_log row (spec 5.9)"
        )
        books_after = lib_io.read_csv(rc.pp("register", "books.csv"))
        assert books_after == books, "a second --check must not touch register/books.csv again"

        print("test_a1_list_check_idempotence: OK")
    shutil.rmtree(tmp, ignore_errors=True)


def test_a1_retry_chain_resolves_to_safe_default():
    """A second, smaller isolated run proving the retry-once-then-safe-default chain (spec 5.5):
    a bad first output (edition mismatch) gets one retry; a bad retry output resolves via the
    field-level safe default + flag, status=flagged, not blocked (A1 always has a safe default)."""
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        plugin = sp.A1Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        item_id = "latest__Class_12th__Chemistry__Chapter_1"

        plugin.list_items(filters)
        bad_output = {
            "subject": "Chemistry", "class": 12, "language": "English", "part": None,
            "edition_seen": "older",  # wrong: folder hint is "latest"
            "reprint_text_exact": "Reprint 2026-27", "reprint_page": 1,
            "is_lab_manual": False, "note": "",
        }
        lib_io.atomic_write_json(rc.pp("steps", "A1", "out", f"{item_id}.runA.json"), bad_output)

        retry_lines = plugin.check(filters)
        assert len(retry_lines) == 1 and retry_lines[0].run_label == "retry1", retry_lines
        retry_input_path = rc.pp("steps", "A1", "work", f"{item_id}.retry1.input.json")
        assert os.path.exists(retry_input_path)
        with open(retry_input_path) as f:
            retry_input = json.load(f)
        assert "previous_attempt_failed" in retry_input and "A1_EDITION_MISMATCH" in retry_input["previous_attempt_failed"]

        # retry also comes back wrong -> resolves via safe default, status=flagged (not blocked).
        lib_io.atomic_write_json(rc.pp("steps", "A1", "out", f"{item_id}.retry1.json"), bad_output)
        final_lines = plugin.check(filters)
        assert final_lines == []
        status = rc.read_item_status("A1", item_id)
        assert status["status"] == "flagged", status

        flags = list(lib_io.read_jsonl(rc.pp("flags", "flags.jsonl")))
        codes = {f["code"] for f in flags}
        assert "A1_EDITION_MISMATCH" in codes, codes
        assert "A1_REGISTER_DRAFT" in codes, codes

        print("test_a1_retry_chain_resolves_to_safe_default: OK")
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    test_a1_list_check_idempotence()
    test_a1_retry_chain_resolves_to_safe_default()
    print("tests/test_run_step.py: ALL OK")
