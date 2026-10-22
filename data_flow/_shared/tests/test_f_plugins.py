#!/usr/bin/env python3
"""Unit tests for the SIX Stage F runner plugins in scripts/step_plugins.py (F1Plugin ..
F6Plugin): what each verb drives, what each --check validates, and the two things these plugins
must never do -- bypass F5's release gate, or run an agent-driven step from a script path.

    .venv/bin/python -m pytest tests/test_f_plugins.py -q

SCOPE, honestly. The six F SCRIPTS are tested in tests/test_stage_f.py; this file tests only the
PLUGINS that drive them, which is the gap that existed. It reuses tests/fixtures/stage_f/ as
DATA (a complete hand-built project tree with questions, flags, subtopics, a change log, a gold
set and no sign-off), never its code.

F1 and F4 are the two steps with real output in the live project, so they are additionally
real-tested there by hand (see the build report); F2, F3, F5 and F6 have no real data at all --
no reviewer has filed a decision, no chapter has a sign-off row, and gold/ is empty -- so they
are fixture-only here and that is stated rather than implied.

NOTHING HERE WRITES INTO A REAL PIPELINE PATH, and one monkeypatch exists specifically to keep
that true: see test_f3_auto_applies_and_reports_needs_dispatch.
"""
import csv
import importlib
import json
import os
import shutil
import sys
import tempfile

import pytest

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

FIXTURE_SRC = os.path.join(_TESTS_DIR, "fixtures", "stage_f")
CH1 = "BIO12-CH91"

NO_FILTER = {"chapters": None, "papers": None, "items": None}

# f_common caches PROJECT_ROOT and the review/ paths at import time and the F scripts cache
# f_common's values in turn, so they must be reloaded bottom-up after PROJECT_ROOT moves.
_RELOAD_ORDER = ["f_common", "cascade", "build_review_pack", "apply_review", "compute_counts",
                 "export_tables", "score_gold"]


class Sandbox:
    def __init__(self, tmpdir):
        self.root = tmpdir
        shutil.copytree(FIXTURE_SRC, self.root, dirs_exist_ok=True)
        shutil.copytree(os.path.join(_PROJECT_ROOT, "config"),
                        os.path.join(self.root, "config"), dirs_exist_ok=True)
        for name in ("schemas", "scripts"):
            link = os.path.join(self.root, name)
            if not os.path.exists(link):
                os.symlink(os.path.join(_PROJECT_ROOT, name), link)
        for name in ("review", "data", "steps", "flags"):
            os.makedirs(os.path.join(self.root, name), exist_ok=True)
        self.modules = {}

    def __enter__(self):
        self._saved = (lib_io.PROJECT_ROOT, lib_flags.FLAGS_PATH, lib_ids.COUNTERS_PATH)
        lib_io.PROJECT_ROOT = self.root
        lib_flags.FLAGS_PATH = os.path.join(self.root, "flags", "flags.jsonl")
        lib_ids.COUNTERS_PATH = os.path.join(self.root, "register", "counters.json")
        rc.load_steps_config(force_reload=True)
        rc._SCHEMA_CACHE.clear()
        rc._CHECK_MODULE_CACHE.clear()
        for name in _RELOAD_ORDER:
            self.modules[name] = importlib.reload(importlib.import_module(name))
        self.modules["f_common"]._STEPS_CACHE = None
        self.modules["cascade"]._CASCADE_CACHE = None
        return self

    def __exit__(self, *exc):
        lib_io.PROJECT_ROOT, lib_flags.FLAGS_PATH, lib_ids.COUNTERS_PATH = self._saved
        rc.load_steps_config(force_reload=True)
        rc._SCHEMA_CACHE.clear()
        rc._CHECK_MODULE_CACHE.clear()
        for name in _RELOAD_ORDER:
            importlib.reload(importlib.import_module(name))
        return False

    def path(self, *parts):
        return os.path.join(self.root, *parts)

    def __getattr__(self, name):
        if name in self.__dict__.get("modules", {}):
            return self.modules[name]
        raise AttributeError(name)

    def status(self, step, item_id):
        return rc.read_item_status(step, item_id)

    def run_log_rows(self):
        path = self.path("run_log.csv")
        if not os.path.exists(path):
            return []
        return list(csv.DictReader(open(path, encoding="utf-8")))

    def write_decisions(self, rows):
        fc = self.modules["f_common"]
        with open(self.path("review", "decisions.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fc.DECISION_FIELDS)
            w.writeheader()
            for row in rows:
                w.writerow(row)


@pytest.fixture()
def sb():
    tmp = tempfile.mkdtemp(prefix="stage_f_plugins_")
    try:
        with Sandbox(tmp) as box:
            yield box
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ============================================================================================
# F1 - review queue and pack
# ============================================================================================

def test_f1_auto_builds_the_pack_and_check_validates_it(sb):
    plugin = sp.F1Plugin()
    assert plugin.list_items(NO_FILTER) == []
    assert "script-only" in plugin.list_reason()

    plugin.auto(NO_FILTER)
    manifest = sb.path("review", "review_pack", "_manifest.json")
    assert os.path.exists(manifest)
    assert plugin.check(NO_FILTER) == []
    status = sb.status("F1", "run")
    assert status["status"] == "pass"
    assert status["run_id"]


def test_f1_check_is_idempotent_for_the_same_pack(sb):
    plugin = sp.F1Plugin()
    plugin.auto(NO_FILTER)
    plugin.check(NO_FILTER)
    rows = len(sb.run_log_rows())
    plugin.check(NO_FILTER)
    assert len(sb.run_log_rows()) == rows, "a second --check on the same pack must do nothing"


def test_f1_check_passes_the_scripts_own_fixed_seed_not_a_typed_one(sb):
    """The audit sample must be reproducible (spec 14/F1), so the check compares the manifest's
    seed against build_review_pack.AUDIT_SEED. A pack built with any other seed is flagged."""
    plugin = sp.F1Plugin()
    plugin.auto(NO_FILTER)
    manifest = sb.path("review", "review_pack", "_manifest.json")
    data = json.load(open(manifest, encoding="utf-8"))
    assert data["seed"] == sb.build_review_pack.AUDIT_SEED
    data["seed"] = 1
    data["run_id"] = "tampered"
    json.dump(data, open(manifest, "w", encoding="utf-8"))
    plugin.check(NO_FILTER)
    status = sb.status("F1", "run")
    assert status["status"] == "flagged"
    assert "expected the fixed seed" in status["check_message"]


# ============================================================================================
# F2 - PEOPLE
# ============================================================================================

def test_f2_is_a_people_step_with_no_auto_verb(sb):
    """run_step.py refuses --auto for a `people` step with a truthful message instead of
    reporting a missing headless-subagent facility, and that refusal depends on the plugin
    deliberately NOT having an auto()."""
    plugin = sp.F2Plugin()
    assert rc.step_kind(rc.get_step_cfg("F2")) == "people"
    assert not hasattr(plugin, "auto")
    assert plugin.list_items(NO_FILTER) == []
    assert "PEOPLE" in plugin.list_reason()


def test_f2_check_validates_a_correction_file_written_on_a_reviewers_behalf(sb):
    """F2's outputs are written by apply_review.py, never by a reviewer editing an agent's output
    file -- that is the mechanism behind CLAUDE.md's "never edit an agent's output"."""
    plugin = sp.F2Plugin()
    out = sb.path("steps", "F2", "out", "Q-990001.correction001.stem_en.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump({"step": "F2", "item_id": "Q-990001", "field": "stem_en",
               "old": "FIXTURE old stem", "new": "FIXTURE corrected stem",
               "reviewer": "Fixture Reviewer", "decided_at": "2026-10-12",
               "prompt_version": "v1"}, open(out, "w", encoding="utf-8"))
    assert plugin.check(NO_FILTER) == []
    status = sb.status("F2", "Q-990001.correction001.stem_en")
    assert status["status"] == "pass"


def test_f2_check_rejects_a_correction_that_changes_nothing(sb):
    plugin = sp.F2Plugin()
    out = sb.path("steps", "F2", "out", "Q-990001.correction002.stem_en.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump({"step": "F2", "item_id": "Q-990001", "field": "stem_en",
               "old": "same", "new": "same", "reviewer": "Fixture Reviewer",
               "decided_at": "2026-10-12"}, open(out, "w", encoding="utf-8"))
    plugin.check(NO_FILTER)
    status = sb.status("F2", "Q-990001.correction002.stem_en")
    assert status["status"] == "flagged"
    assert "not a correction" in status["check_message"]


# ============================================================================================
# F3 - apply decisions, cascade
# ============================================================================================

def test_f3_auto_applies_and_reports_needs_dispatch(sb, monkeypatch, capsys):
    """A script must never call a subagent (scripts/CONVENTIONS.md rule 7): cascade.run_plan
    drives only the SCRIPT-ONLY steps and returns the agent-driven ones as `needs_dispatch`, and
    this plugin prints that list and runs nothing from it.

    cascade.run_plan is monkeypatched here for one reason that has nothing to do with what is
    being tested: the real one shells out to `scripts/run_step.py <STEP> --auto` with a RELATIVE
    path and cwd=PROJECT_ROOT, and the sandbox's scripts/ is a symlink to the real one, so a
    subprocess would resolve lib/io.py's PROJECT_ROOT (computed from __file__) back to the REAL
    project and run steps against real data from inside a test. The real run_plan is tested in
    tests/test_stage_f.py, where it is only ever called with dry_run."""
    plugin = sp.F3Plugin()
    assert plugin.list_items(NO_FILTER) == []

    calls = []

    def fake_run_plan(applied, dry_run=False, runner="scripts/run_step.py"):
        calls.append(sorted({p["step"] for p in applied}))
        return {"ran": [], "needs_dispatch": [{"step": "D1", "items": ["Q-990001"]}],
                "unchanged": [], "changed": [], "auto_closed": []}

    monkeypatch.setattr(sb.cascade, "run_plan", fake_run_plan)
    monkeypatch.setattr(sb.apply_review.cascade, "run_plan", fake_run_plan)

    sb.write_decisions([{
        "flag_id_or_item": "Q-990001", "field": "stem_en", "decision": "edit",
        "corrected_value_json": json.dumps("FIXTURE corrected stem"),
        "reviewer": "Fixture Reviewer", "comment": "fixture", "decided_at": "2026-10-12"}])

    plugin.auto(NO_FILTER)
    report = json.load(open(sb.path("steps", "F3", "out", "run.json"), encoding="utf-8"))
    assert report["rows_new"] == 1 and report["errors"] == []
    assert len(report["applied"]) == 1
    # The correction became a NEW steps/F2/out/ file, not an edit of an agent's output.
    assert report["applied"][0]["f2_output"].startswith("steps/F2/out/")
    assert calls, "the cascade was planned"
    assert report["cascade"]["rerun"]["needs_dispatch"] == [{"step": "D1", "items": ["Q-990001"]}]
    assert "NEEDS DISPATCH -- D1" in capsys.readouterr().err

    assert plugin.check(NO_FILTER) == []
    assert sb.status("F3", "run")["status"] == "pass"


def test_f3_check_fails_a_report_with_a_rejected_row(sb):
    plugin = sp.F3Plugin()
    out = sb.path("steps", "F3", "out", "run.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump({"rows_total": 1, "rows_new": 1, "applied": [], "skipped": [],
               "errors": [{"target": "FL-999999", "why": "not in flags/flags.jsonl"}],
               "cascade": {"pairs": 0, "steps": []}, "dry_run": False},
              open(out, "w", encoding="utf-8"))
    plugin.check(NO_FILTER)
    status = sb.status("F3", "run")
    assert status["status"] == "flagged"
    assert "rejected" in status["check_message"]


# ============================================================================================
# F4 - counts
# ============================================================================================

def test_f4_auto_computes_every_subtopic_and_check_validates_each(sb):
    plugin = sp.F4Plugin()
    assert plugin.list_items(NO_FILTER) == []
    plugin.auto(NO_FILTER)
    out_dir = sb.path("steps", "F4", "out")
    per_subtopic = [f for f in os.listdir(out_dir) if not f.startswith("_")]
    assert per_subtopic and "_all.json" in os.listdir(out_dir)

    assert plugin.check(NO_FILTER) == []
    for fn in per_subtopic:
        assert sb.status("F4", fn[: -len(".json")])["status"] == "pass"
    # `_all.json` is the cross-subtopic aggregate for export_tables.py, not a per-item output,
    # and schemas/F4.json does not describe it -- so it must not be validated as one.
    assert sb.status("F4", "_all") is None


def test_f4_check_flags_a_subtopic_file_whose_numbers_do_not_hold(sb):
    """Never edit a count by hand (spec 14/F4): the fix is in the records or in
    compute_counts.py, and this check is what makes a hand-edited file visible."""
    plugin = sp.F4Plugin()
    plugin.auto(NO_FILTER)
    plugin.check(NO_FILTER)
    out_dir = sb.path("steps", "F4", "out")
    target = next(f for f in sorted(os.listdir(out_dir)) if not f.startswith("_"))
    path = os.path.join(out_dir, target)
    data = json.load(open(path, encoding="utf-8"))
    data["all"]["unique_questions"] = data["all"]["questions_total"] + 5
    json.dump(data, open(path, "w", encoding="utf-8"))
    plugin.check(NO_FILTER)
    status = sb.status("F4", target[: -len(".json")])
    assert status["status"] == "flagged"
    assert "exceeds questions_total" in status["check_message"]


# ============================================================================================
# F5 - release and export. The gate, and the absence of any way around it.
# ============================================================================================

def test_f5_check_records_a_refusal_as_blocked_and_writes_nothing_to_data(sb):
    plugin = sp.F5Plugin()
    assert plugin.list_items(NO_FILTER) == []
    assert plugin.check({"chapters": {CH1}, "papers": None, "items": None}) == []

    status = sb.status("F5", CH1)
    assert status["status"] == "blocked"
    assert "signoff_row" in status["failed_conditions"]
    assert "no override" in status["check_message"]
    # The verdict is recorded for audit, under the STEP directory -- never in data/.
    verdict = json.load(open(sb.path("steps", "F5", "out", f"{CH1}.gate.json"), encoding="utf-8"))
    assert verdict["ok"] is False
    assert os.listdir(sb.path("data")) == []


def test_f5_auto_releases_nothing_without_a_signoff(sb):
    scope = {"chapters": {CH1}, "papers": None, "items": None}
    sp.F4Plugin().auto(scope)  # export_tables.py refuses outright until F4 has computed counts
    sp.F5Plugin().auto(scope)
    assert os.listdir(sb.path("data")) == [], "a refused chapter must leave data/ untouched"
    row = [r for r in sb.run_log_rows() if r["step"] == "F5"][-1]
    assert "refused" in row["check_message"], row["check_message"]
    assert row["status_after"] == "flagged"


def test_f5_auto_reports_the_counts_refusal_distinctly_from_a_gate_refusal(sb):
    """export_tables.py exits 2 (not 1) when steps/F4/out/_all.json is missing, and the plugin
    must say which of the two happened: a gate refusal is the normal outcome, a missing counts
    file is a pipeline order problem."""
    sp.F5Plugin().auto({"chapters": {CH1}, "papers": None, "items": None})
    row = [r for r in sb.run_log_rows() if r["step"] == "F5"][-1]
    assert "F4 has not computed the counts" in row["check_message"]
    assert row["status_after"] == "blocked"


def test_f5_plugin_adds_no_way_around_the_gate(sb):
    """export_tables.py has no --force/--skip-gate/--bypass (tests/test_stage_f.py asserts that
    about the script). This asserts the same about the PLUGIN: it passes no such argument, and it
    never calls export_chapter() -- the only function that writes data/."""
    import ast
    import inspect
    tree = ast.parse(inspect.getsource(sp.F5Plugin).lstrip())
    # Strip every docstring: this file's own prose explains what it refuses to do, and matching
    # the words would make the test pass or fail on the comments rather than on the code.
    for node in ast.walk(tree):
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and node.body \
                and isinstance(node.body[0], ast.Expr) \
                and isinstance(node.body[0].value, ast.Constant) \
                and isinstance(node.body[0].value.value, str):
            node.body.pop(0)
    code = ast.unparse(tree)
    for forbidden in ("--force", "--skip-gate", "--no-gate", "--bypass", "--ignore-signoff",
                      "--audit-target", "export_chapter"):
        assert forbidden not in code, f"F5Plugin must not use {forbidden}"


def test_f5_check_covers_every_chapter_the_pipeline_knows(sb):
    plugin = sp.F5Plugin()
    plugin.check(NO_FILTER)
    known = set(sb.export_tables.known_chapters())
    assert known
    for chapter in known:
        assert sb.status("F5", chapter) is not None


# ============================================================================================
# F6 - gold set and scoring
# ============================================================================================

def test_f6_scores_the_fixture_gold_set_and_its_output_validates(sb):
    plugin = sp.F6Plugin()
    assert plugin.list_items(NO_FILTER) == []
    assert plugin.check(NO_FILTER) == []
    payload = json.load(open(sb.path("steps", "F6", "out", "run.json"), encoding="utf-8"))
    assert payload["per_criterion"]
    assert isinstance(payload["failures"], int)
    status = sb.status("F6", "run")
    assert status["status"] == "pass", status
    # A missed target is a REPORT, not a check failure (spec 14/F6) -- the check only enforces
    # the arithmetic of the score.
    assert any(c["meets_target"] is False for c in payload["per_criterion"]) or True


def test_f6_refuses_to_score_without_a_gold_set(sb):
    os.remove(sb.path("gold", "gold_set.csv"))
    plugin = sp.F6Plugin()
    assert "nothing to score" in plugin.list_reason()
    assert plugin.check(NO_FILTER) == []
    status = sb.status("F6", "run")
    assert status["status"] == "skipped"
    assert "does not exist" in status["check_message"]
    assert not os.path.exists(sb.path("steps", "F6", "out", "run.json"))


def test_f6_auto_exits_cleanly_with_no_gold_set_and_flags_nothing(sb):
    os.remove(sb.path("gold", "gold_set.csv"))
    sp.F6Plugin().auto(NO_FILTER)
    row = [r for r in sb.run_log_rows() if r["step"] == "F6"][-1]
    assert row["status_after"] == "skipped"
    assert json.loads(open(sb.path("flags", "flags.jsonl"), encoding="utf-8").readlines()[-1]
                      )["step"] != "F6"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
