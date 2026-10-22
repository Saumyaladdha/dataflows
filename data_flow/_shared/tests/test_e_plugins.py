#!/usr/bin/env python3
"""Unit tests for the SEVEN Stage E runner plugins in scripts/step_plugins.py (E0Plugin ..
E6Plugin): which items they dispatch, what goes into an agent's input, how the retry /
second-run / adjudicator / safe-default chains resolve, and that every step's codebook reaches
its agent with its hash recorded.

    .venv/bin/python -m pytest tests/test_e_plugins.py -q

HONEST SCOPE, because it is the thing most worth knowing about these tests.

  * Stage E CANNOT run end to end on real data. E1 needs a resolved D7, D7 needs D6, and D6 is
    agent-driven (`d6-status-note-writer`) and has never been dispatched in this project, so no
    real question has reached any E step. `run_step.py E1 --list` says exactly that.
  * Every AGENT OUTPUT below is invented. No E agent has ever run here, so there is no real E
    output to test against. A test showing a plugin dispatches, merges and falls back correctly
    proves the WIRING; it proves nothing about whether any tag is right.
  * The records are hand-built fixtures under tests/fixtures/stage_e_plugins/ (see its README).
    The real codebook/E*.md files and the real config/allowed_values.yaml ARE used, so the
    codebook-wiring assertions are about the real files.

NOTHING HERE WRITES INTO A REAL PIPELINE PATH. Every test runs in a temporary copy of the fixture
tree with PROJECT_ROOT, lib/flags.py's FLAGS_PATH and lib/ids.py's COUNTERS_PATH all repointed at
it -- the three module-level paths tests/test_run_step.py documents having to patch together.
(docs/OPEN_QUESTIONS.md 2026-10-10 records what happened the one time fixtures were written into
real paths.)
"""
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

import codebook_version  # noqa: E402
import runner_core as rc  # noqa: E402
import step_plugins as sp  # noqa: E402
from lib import flags as lib_flags  # noqa: E402
from lib import ids as lib_ids  # noqa: E402
from lib import io as lib_io  # noqa: E402
from lib import records as lib_records  # noqa: E402

FIXTURE_SRC = os.path.join(_TESTS_DIR, "fixtures", "stage_e_plugins")

NO_FILTER = {"chapters": None, "papers": None, "items": None}

#: The one fixture question whose shape no spec E1 pattern covers (the real Q-000005 shape), so
#: scripts/type_patterns.py hands it to the agent.
E1_HANDOVER = "Q-991002"
#: The one fixture question where two describe_tags context patterns fire at once, so spec 13/E6's
#: tie-break needs judgement and the agent is called.
E6_HANDOVER = "Q-991003"
SCRIPT_DECIDED = "Q-991001"


class Sandbox:
    """A throwaway project root holding a copy of the fixture tree."""

    def __init__(self, tmpdir):
        self.root = tmpdir
        shutil.copytree(FIXTURE_SRC, self.root, dirs_exist_ok=True)
        # config/ is read-only input here; copy the REAL one so the step entries, the cascade map
        # and the allowed values under test are the project's actual ones.
        shutil.copytree(os.path.join(_PROJECT_ROOT, "config"),
                        os.path.join(self.root, "config"), dirs_exist_ok=True)
        # schemas/ and scripts/ are the code under test, so they are symlinked rather than
        # copied -- a stale second copy would be testing something other than the real plugins.
        for name in ("schemas", "scripts"):
            link = os.path.join(self.root, name)
            if not os.path.exists(link):
                os.symlink(os.path.join(_PROJECT_ROOT, name), link)
        # codebook/ is COPIED, not symlinked: the real files are what the wiring assertions check,
        # but one test has to delete codebook/E4.md to exercise the E4_NO_CODEBOOK path, and that
        # must never reach the real directory.
        shutil.copytree(os.path.join(_PROJECT_ROOT, "codebook"),
                        os.path.join(self.root, "codebook"), dirs_exist_ok=True)

    def __enter__(self):
        self._saved = (lib_io.PROJECT_ROOT, lib_flags.FLAGS_PATH, lib_ids.COUNTERS_PATH)
        lib_io.PROJECT_ROOT = self.root
        lib_flags.FLAGS_PATH = os.path.join(self.root, "flags", "flags.jsonl")
        lib_ids.COUNTERS_PATH = os.path.join(self.root, "register", "counters.json")
        rc.load_steps_config(force_reload=True)
        rc._SCHEMA_CACHE.clear()
        rc._CHECK_MODULE_CACHE.clear()
        sp._E_PASSAGE_KINDS.clear()
        return self

    def __exit__(self, *exc):
        lib_io.PROJECT_ROOT, lib_flags.FLAGS_PATH, lib_ids.COUNTERS_PATH = self._saved
        rc.load_steps_config(force_reload=True)
        rc._SCHEMA_CACHE.clear()
        rc._CHECK_MODULE_CACHE.clear()
        sp._E_PASSAGE_KINDS.clear()
        return False

    # --- helpers -----------------------------------------------------------
    def path(self, *parts):
        return os.path.join(self.root, *parts)

    def fresh(self, step):
        """Clear one step's OWN status files so it has work to do.

        The fixture tree ships a hand-written `pass` status for D7, D8 and E1-E4 purely so each E
        step's `needs` gate opens (E2 needs E1, E3 needs E2, ...). That means the step UNDER TEST
        would otherwise look already resolved, so a test for step X clears X's own statuses and
        leaves its upstream gate alone. This is also the realistic state: in a real run E1 has not
        run yet when E1 is being run."""
        status_dir = self.path("steps", step, "status")
        if os.path.isdir(status_dir):
            for fn in os.listdir(status_dir):
                os.remove(os.path.join(status_dir, fn))

    def gate(self, step):
        """(Re-)write the hand-written `pass` status that opens the NEXT step's gate, for every
        fixture question. Needed when a test freshens one E step and still needs the others'
        statuses -- E1 is both a step under test and E2's and E6's gate."""
        for fn in sorted(os.listdir(self.path("papers", "records"))):
            if not fn.endswith(".json") or fn.startswith("_"):
                continue
            rc.write_item_status(step, fn[: -len(".json")], "pass", "v1",
                                  extra={"check_message": "FIXTURE gate status; nothing was run"})

    def work_input(self, step, item_id, run_label):
        with open(self.path("steps", step, "work", f"{item_id}.{run_label}.input.json"),
                  encoding="utf-8") as f:
            return json.load(f)

    def write_out(self, step, item_id, run_label, data):
        path = self.path("steps", step, "out", f"{item_id}.{run_label}.json")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return path

    def record(self, qid):
        return lib_records.read_record(qid)

    def status(self, step, item_id):
        return rc.read_item_status(step, item_id)

    def flags(self, code=None, item_id=None):
        path = self.path("flags", "flags.jsonl")
        if not os.path.exists(path):
            return []
        rows = list(lib_io.read_jsonl(path))
        if code:
            rows = [r for r in rows if r.get("code") == code]
        if item_id:
            rows = [r for r in rows if r.get("item_id") == item_id]
        return rows


@pytest.fixture()
def sb():
    tmp = tempfile.mkdtemp(prefix="stage_e_plugins_")
    try:
        with Sandbox(tmp) as box:
            yield box
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ============================================================================================
# Codebook wiring (spec 13.0) -- the requirement that is invisible if it is wrong
# ============================================================================================

def test_every_e_step_but_e0_declares_a_codebook_and_e0s_null_is_load_bearing(sb):
    """E0's `codebook_file` MUST stay null: spec 13/E0 step 1 runs e0-open-look with no
    categories shown, and a codebook would turn the discovery into a matching exercise."""
    assert rc.get_step_cfg("E0").get("codebook_file") is None
    text, version = sp._e_codebook("E0")
    assert (text, version) == (None, "none")

    for step in ("E1", "E2", "E3", "E4", "E5", "E6"):
        declared = rc.get_step_cfg(step).get("codebook_file")
        assert declared, f"{step} declares no codebook_file"
        text, version = sp._e_codebook(step)
        assert text, f"{step}'s declared codebook {declared} is not on disk"
        # The one formula in the repo: scripts/codebook_version.py.
        assert version == codebook_version.for_step(step)[1]
        assert version != "none"


def test_the_codebook_text_itself_reaches_the_agent_input(sb):
    """Not just a hash: the agent input must carry the codebook's FULL TEXT (spec 13.0)."""
    cases = [("E1", sp.E1Plugin(), E1_HANDOVER, "runA"),
             ("E2", sp.E2Plugin(), SCRIPT_DECIDED, "runA"),
             ("E3", sp.E3Plugin(), SCRIPT_DECIDED, "runA"),
             ("E4", sp.E4Plugin(), SCRIPT_DECIDED, "runA"),
             ("E6", sp.E6Plugin(), E6_HANDOVER, "runA")]
    for step, plugin, item_id, run_label in cases:
        sb.fresh(step)
        for other in ("E1", "E2", "E3", "E4"):
            if other != step:
                sb.gate(other)
        plugin.list_items(NO_FILTER)
        payload = sb.work_input(step, item_id, run_label)
        real_text, real_version = sp._e_codebook(step)
        assert payload["codebook"] == real_text, f"{step} did not pass its codebook"
        if step == "E4":
            # E4 is the one step whose agent must echo the version back (spec 13/E4's own output
            # shape), so it is the one step whose INPUT carries it.
            assert payload["codebook_version"] == real_version


def test_e5_passes_its_codebook_to_each_wrong_option(sb):
    plugin = sp.E5Plugin()
    lines = plugin.list_items({"chapters": None, "papers": None, "items": {SCRIPT_DECIDED}})
    assert lines
    payload = sb.work_input("E5", f"{SCRIPT_DECIDED}#opt2", "runA")
    assert payload["codebook"] == sp._e_codebook("E5")[0]


def test_no_legacy_field_ever_reaches_an_agent_input(sb):
    """Spec Section 13: `legacy_chapter` / `legacy_topic` / `legacy_question_type` are never
    inputs to any agent. Q-991001 carries all three precisely so this can be proved."""
    assert sb.record(SCRIPT_DECIDED)["legacy_chapter"].startswith("FIXTURE")
    for step, plugin in (("E2", sp.E2Plugin()), ("E3", sp.E3Plugin()), ("E4", sp.E4Plugin())):
        sb.fresh(step)
        for other in ("E1", "E2", "E3", "E4"):
            if other != step:
                sb.gate(other)
        plugin.list_items(NO_FILTER)
        blob = json.dumps(sb.work_input(step, SCRIPT_DECIDED, "runA"))
        assert "legacy_" not in blob and "FIXTURE legacy" not in blob


def test_assert_no_legacy_actually_fires_if_a_plugin_ever_leaked_one(sb):
    with pytest.raises(ValueError):
        sp._e_write_agent_input("E1", "Q-991001", "runA",
                                 {"question": {}, "legacy_question_type": "Assertion-Reason"})


# ============================================================================================
# E1 -- script first, agent only when no pattern decides, then one retry
# ============================================================================================

def test_e1_dispatches_only_the_question_no_pattern_decides(sb):
    sb.fresh("E1")
    lines = sp.E1Plugin().list_items(NO_FILTER)
    assert [l.item_id for l in lines] == [E1_HANDOVER]
    assert lines[0].agent == "e1-type-tagger"
    assert lines[0].run_label == "runA"


def test_e1_resolves_the_pattern_decided_questions_with_no_agent_at_all(sb):
    sb.fresh("E1")
    plugin = sp.E1Plugin()
    plugin.check(NO_FILTER)
    status = sb.status("E1", SCRIPT_DECIDED)
    assert status["status"] == "pass"
    assert status["run"] == "script"
    record = sb.record(SCRIPT_DECIDED)
    assert record["question_type"] == "single_statement"
    assert record["e1_decided_by"].startswith("script pattern")
    # Spec 13.0: the hash is recorded on every tag the step produced -- script-decided included.
    assert record["codebook_version"]["E1"] == sp._e_codebook("E1")[1]
    assert record["e1_codebook_version"] == sp._e_codebook("E1")[1]
    # ... and the handover question is NOT resolved by the script.
    assert sb.status("E1", E1_HANDOVER) is None


def test_e1_check_is_idempotent(sb):
    sb.fresh("E1")
    plugin = sp.E1Plugin()
    plugin.check(NO_FILTER)
    rows_after_first = len(lib_io.read_csv(sb.path("run_log.csv")))
    before = sb.record(SCRIPT_DECIDED)
    plugin.check(NO_FILTER)
    assert len(lib_io.read_csv(sb.path("run_log.csv"))) == rows_after_first
    assert sb.record(SCRIPT_DECIDED) == before


def test_e1_retry_input_is_the_AGENT_input_not_the_check_context(sb):
    """The real bug resolve_single_run_items' `agent_inputs=` parameter exists for: E1's check
    context is {record: ...} (it re-runs type_patterns on the real record) while the agent's own
    input is {question, codebook, allowed}. Without agent_inputs the retry would hand the agent a
    question record instead of a question."""
    sb.fresh("E1")
    plugin = sp.E1Plugin()
    plugin.list_items(NO_FILTER)
    # A low confidence on a real value is a check failure in scripts/checks/E1.py.
    sb.write_out("E1", E1_HANDOVER, "runA",
                 {"question_type": "single_statement", "new_description": "", "confidence": "low"})
    lines = plugin.check(NO_FILTER)
    assert [(l.item_id, l.run_label) for l in lines] == [(E1_HANDOVER, "retry1")]
    retry = sb.work_input("E1", E1_HANDOVER, "retry1")
    assert set(retry) == {"question", "codebook", "allowed", "previous_attempt_failed"}
    assert "record" not in retry
    assert retry["question"]["stem"].startswith("Which of the following reactions")
    assert retry["previous_attempt_failed"]


def test_e1_safe_default_is_new_type_with_the_failing_message_once(sb):
    """config/steps.yaml E1 safe_default, verbatim: retry exhausted -> new_type with the failing
    check's message as new_description, E_NEW_CATEGORY (normal)."""
    sb.fresh("E1")
    plugin = sp.E1Plugin()
    plugin.list_items(NO_FILTER)
    bad = {"question_type": "statement_options", "new_description": "", "confidence": "high"}
    sb.write_out("E1", E1_HANDOVER, "runA", bad)
    plugin.check(NO_FILTER)
    sb.write_out("E1", E1_HANDOVER, "retry1", bad)
    assert plugin.check(NO_FILTER) == []

    record = sb.record(E1_HANDOVER)
    assert record["question_type"] == "new_type"
    assert "reaction" in record["e1_new_description"].lower()
    assert sb.status("E1", E1_HANDOVER)["status"] == "flagged"
    # Exactly one E_NEW_CATEGORY: lib/flags.py appends and never dedupes, so a plugin raising one
    # that resolve_single_run_items already raised would queue the same item twice in Stage F.
    assert len(sb.flags("E_NEW_CATEGORY", E1_HANDOVER)) == 1


# ============================================================================================
# E2 -- the one E step whose chain is retry THEN adjudicator
# ============================================================================================

def _e2_answer(fmt, confidence="high", description=""):
    return {"format": fmt, "new_description": description, "confidence": confidence}


#: A format that FAILS E2's negative guard for E1_HANDOVER: a letter-code format where the options
#: are single items. The old failing value was `pick_correct`, which merged into
#: `pick_correct_statement` in allowed_values v0.3 -- and that is now the value the guard REQUIRES,
#: so it can no longer stand for "wrong answer" in these tests.
GUARD_FAILS = "pick_match_code"
#: ...and the value the guard requires, read from the check so this cannot drift from it.
GUARD_REQUIRES = sp.E2Plugin._negative_format()


def test_e2_guard_failure_retries_with_specs_own_sentence(sb):
    """Spec 13/E2 On failure: "retry with 'The stem contains <word>'". scripts/checks/E2.py puts
    that sentence at the head of every E2_NEGATIVE_GUARD segment so the plugin can forward it
    unchanged instead of re-wording it."""
    sb.fresh("E2")
    plugin = sp.E2Plugin()
    plugin.list_items(NO_FILTER)
    sb.write_out("E2", E1_HANDOVER, "runA", _e2_answer(GUARD_FAILS))
    lines = plugin.check({"chapters": None, "papers": None, "items": {E1_HANDOVER}})
    assert [(l.item_id, l.run_label) for l in lines] == [(E1_HANDOVER, "retry1")]
    retry = sb.work_input("E2", E1_HANDOVER, "retry1")
    assert retry["previous_attempt_failed"].startswith("The stem contains NOT.")
    assert retry["negative_words_seen"] == ["NOT"]


def test_e2_second_failure_goes_to_the_adjudicator_not_straight_to_the_safe_default(sb):
    sb.fresh("E2")
    plugin = sp.E2Plugin()
    scope = {"chapters": None, "papers": None, "items": {E1_HANDOVER}}
    plugin.list_items(NO_FILTER)
    sb.write_out("E2", E1_HANDOVER, "runA", _e2_answer(GUARD_FAILS))
    plugin.check(scope)
    sb.write_out("E2", E1_HANDOVER, "retry1", _e2_answer(GUARD_FAILS))
    lines = plugin.check(scope)
    assert [(l.item_id, l.agent, l.run_label) for l in lines] == \
        [(E1_HANDOVER, "x-adjudicator", "adjudicated")]
    # Nothing is resolved yet: the adjudicator rung spec names has not answered.
    assert sb.status("E2", E1_HANDOVER) is None
    payload = sb.work_input("E2", E1_HANDOVER, "adjudicated")
    assert payload["evidence"]["guard_requires"] == GUARD_REQUIRES
    assert payload["run_a"]["format"] == GUARD_FAILS
    assert payload["codebook"] == sp._e_codebook("E2")[0]


def test_e2_adjudicator_unsure_takes_the_guards_own_required_value(sb):
    sb.fresh("E2")
    plugin = sp.E2Plugin()
    scope = {"chapters": None, "papers": None, "items": {E1_HANDOVER}}
    plugin.list_items(NO_FILTER)
    sb.write_out("E2", E1_HANDOVER, "runA", _e2_answer(GUARD_FAILS))
    plugin.check(scope)
    sb.write_out("E2", E1_HANDOVER, "retry1", _e2_answer(GUARD_FAILS))
    plugin.check(scope)
    sb.write_out("E2", E1_HANDOVER, "adjudicated", {"choice": "unsure"})
    assert plugin.check(scope) == []

    record = sb.record(E1_HANDOVER)
    assert record["format"] == GUARD_REQUIRES
    assert sb.status("E2", E1_HANDOVER)["status"] == "flagged"
    guard = sb.flags("E2_NEGATIVE_GUARD", E1_HANDOVER)
    assert len(guard) == 1 and guard[0]["severity"] == "high"
    # The agent's own value is kept as the provisional one so Stage F sees both.
    assert guard[0]["provisional_value"]["agent_answer"]["format"] == GUARD_FAILS


def test_e2_adjudicator_cannot_bypass_the_guard(sb):
    """A verdict that still fails the guard is NOT stored: the adjudicator is re-checked."""
    sb.fresh("E2")
    plugin = sp.E2Plugin()
    scope = {"chapters": None, "papers": None, "items": {E1_HANDOVER}}
    plugin.list_items(NO_FILTER)
    sb.write_out("E2", E1_HANDOVER, "runA", _e2_answer(GUARD_FAILS))
    plugin.check(scope)
    sb.write_out("E2", E1_HANDOVER, "retry1", _e2_answer(GUARD_FAILS))
    plugin.check(scope)
    sb.write_out("E2", E1_HANDOVER, "adjudicated", {"choice": "A"})
    plugin.check(scope)
    assert sb.record(E1_HANDOVER)["format"] == GUARD_REQUIRES
    assert "still fails the guard" in sb.status("E2", E1_HANDOVER)["check_message"]


def test_e2_a_clean_answer_passes_without_a_flag(sb):
    sb.fresh("E2")
    plugin = sp.E2Plugin()
    scope = {"chapters": None, "papers": None, "items": {E1_HANDOVER}}
    plugin.list_items(NO_FILTER)
    sb.write_out("E2", E1_HANDOVER, "runA", _e2_answer("pick_correct_statement"))
    assert plugin.check(scope) == []
    assert sb.status("E2", E1_HANDOVER)["status"] == "pass"
    assert sb.record(E1_HANDOVER)["format"] == "pick_correct_statement"
    assert sb.flags("E2_NEGATIVE_GUARD", E1_HANDOVER) == []


# ============================================================================================
# E3 -- medium confidence is a FLAG, never a retry
# ============================================================================================

def test_e3_medium_confidence_passes_and_raises_e3_medium(sb):
    sb.fresh("E3")
    plugin = sp.E3Plugin()
    scope = {"chapters": None, "papers": None, "items": {SCRIPT_DECIDED}}
    plugin.list_items(NO_FILTER)
    sb.write_out("E3", SCRIPT_DECIDED, "runA", {
        "content_shape": "definition_term", "why": "Evidence is the weber line in the SI units box",
        "new_description": "", "confidence": "medium"})
    assert plugin.check(scope) == []
    assert sb.status("E3", SCRIPT_DECIDED)["status"] == "pass"
    assert sb.record(SCRIPT_DECIDED)["content_shape"] == "definition_term"
    medium = sb.flags("E3_MEDIUM", SCRIPT_DECIDED)
    assert len(medium) == 1 and medium[0]["severity"] == "low"


def test_e3_evidence_carries_the_passage_kind_from_the_real_book(sb):
    """e3-shape-tagger asks for the evidence lines WITH their passage kinds, and D3's output
    carries only passage_id + text, so the plugin looks the kind up in ncert/passages/."""
    sb.fresh("E3")
    sp.E3Plugin().list_items(NO_FILTER)
    evidence = sb.work_input("E3", SCRIPT_DECIDED, "runA")["evidence"]
    assert evidence and evidence[0]["kind"] == "paragraph"
    assert evidence[0]["passage_id"] == "PHY11L-CH99-P01"
    # An empty list is passed as [] rather than omitted -- checks/E3.py's current_affairs rule
    # depends on the key existing.
    sp.E3Plugin().list_items({"chapters": None, "papers": None, "items": {E1_HANDOVER}})
    assert sb.work_input("E3", E1_HANDOVER, "runA")["evidence"] == []


# ============================================================================================
# E4 -- 2 runs + adjudicator, and the branch rule
# ============================================================================================

def _e4_answer(primary, secondary=None, why="Must convert the unit before comparing the two",
                confidence="high", branch_used="none", version=None):
    return {"primary": primary, "secondary": secondary, "why": why, "confidence": confidence,
            "codebook_version": version or sp._e_codebook("E4")[1], "branch_used": branch_used}


def test_e4_agent_input_always_carries_the_branch_even_when_it_is_null(sb):
    """codebook/E4.md section 1's rule, made impossible to break: scripts/checks/E4.py FAILS any
    item whose input_data has no `branch` key, so both the agent input and the check context must
    carry it -- present even when the value is None (every Physics record)."""
    sb.fresh("E4")
    lines = sp.E4Plugin().list_items({"chapters": None, "papers": None, "items": {SCRIPT_DECIDED}})
    assert [l.run_label for l in lines] == ["runA", "runB"]
    for run_label in ("runA", "runB"):
        payload = sb.work_input("E4", SCRIPT_DECIDED, run_label)
        assert "branch" in payload and payload["branch"] is None
        assert payload["subject"] == "Physics"
    assert "branch" in sp.E4Plugin()._check_context(sb.record(SCRIPT_DECIDED))


def test_e4_two_agreeing_runs_resolve_pass(sb):
    sb.fresh("E4")
    plugin = sp.E4Plugin()
    scope = {"chapters": None, "papers": None, "items": {SCRIPT_DECIDED}}
    plugin.list_items(scope)
    for run_label in ("runA", "runB"):
        sb.write_out("E4", SCRIPT_DECIDED, run_label, _e4_answer("recall"))
    assert plugin.check(scope) == []
    assert sb.status("E4", SCRIPT_DECIDED)["status"] == "pass"
    record = sb.record(SCRIPT_DECIDED)
    assert record["category_primary"] == "recall" and record["category_secondary"] is None
    assert record["codebook_version"]["E4"] == sp._e_codebook("E4")[1]
    # codebook/E4.md exists, so E4_NO_CODEBOOK must NOT appear. Its reappearance is the signal
    # that the codebook stopped reaching the agent.
    assert sb.flags("E4_NO_CODEBOOK", SCRIPT_DECIDED) == []
    assert sb.flags("E4_ADJUDICATED", SCRIPT_DECIDED) == []


def test_e4_agreement_is_on_the_primary_and_on_whether_a_secondary_exists(sb):
    """Spec 13/E4 Checks, and the asymmetry that is the rule rather than a simplification:
    {numerical, diagram_graph} and {numerical, reasoning} AGREE (both have a secondary);
    {numerical, null} and {numerical, reasoning} DISAGREE."""
    sb.fresh("E4")
    plugin = sp.E4Plugin()
    assert plugin._canonical(_e4_answer("numerical", "diagram_graph")) == \
        plugin._canonical(_e4_answer("numerical", "reasoning"))
    assert plugin._canonical(_e4_answer("numerical", None)) != \
        plugin._canonical(_e4_answer("numerical", "reasoning"))

    scope = {"chapters": None, "papers": None, "items": {SCRIPT_DECIDED}}
    plugin.list_items(scope)
    sb.write_out("E4", SCRIPT_DECIDED, "runA", _e4_answer("recall", None))
    sb.write_out("E4", SCRIPT_DECIDED, "runB", _e4_answer("recall", "reasoning"))
    lines = plugin.check(scope)
    assert [(l.agent, l.run_label) for l in lines] == [("x-adjudicator", "adjudicated")]
    payload = sb.work_input("E4", SCRIPT_DECIDED, "adjudicated")
    assert "whether a secondary exists" in payload["failed_check"].lower()
    assert payload["evidence"]["branch"] is None
    assert "never promote a secondary" in payload["never"]


def test_e4_adjudicator_unsure_uses_run_a_primary_with_secondary_null(sb):
    """config/steps.yaml E4 safe_default: never merge two primaries, never promote a secondary."""
    sb.fresh("E4")
    plugin = sp.E4Plugin()
    scope = {"chapters": None, "papers": None, "items": {SCRIPT_DECIDED}}
    plugin.list_items(scope)
    sb.write_out("E4", SCRIPT_DECIDED, "runA", _e4_answer("recall", None))
    sb.write_out("E4", SCRIPT_DECIDED, "runB", _e4_answer("application", "reasoning"))
    plugin.check(scope)
    sb.write_out("E4", SCRIPT_DECIDED, "adjudicated", {"choice": "unsure"})
    assert plugin.check(scope) == []

    record = sb.record(SCRIPT_DECIDED)
    assert record["category_primary"] == "recall"
    assert record["category_secondary"] is None
    assert sb.status("E4", SCRIPT_DECIDED)["status"] == "flagged"
    adjudicated = sb.flags("E4_ADJUDICATED", SCRIPT_DECIDED)
    assert len(adjudicated) == 1
    provisional = adjudicated[0]["provisional_value"]
    assert provisional["run_a"]["primary"] == "recall"
    assert provisional["run_b"]["primary"] == "application"


def test_e4_a_low_confidence_run_is_the_designed_escalation(sb):
    """scripts/checks/E4.py fails `confidence: low`; that failure routes the item to the
    adjudicator rather than into the bank."""
    sb.fresh("E4")
    plugin = sp.E4Plugin()
    scope = {"chapters": None, "papers": None, "items": {SCRIPT_DECIDED}}
    plugin.list_items(scope)
    sb.write_out("E4", SCRIPT_DECIDED, "runA", _e4_answer("recall", confidence="low"))
    sb.write_out("E4", SCRIPT_DECIDED, "runB", _e4_answer("recall"))
    lines = plugin.check(scope)
    assert [l.run_label for l in lines] == ["adjudicated"]


def test_e4_flags_a_missing_codebook_from_the_real_hash_not_a_message(sb):
    """Spec 13.0 / 16: E4_NO_CODEBOOK (low) is raised on EVERY E4 output while codebook/E4.md
    does not exist, from the real hash. Simulated by pointing the step at a file that is absent,
    which is exactly what config/steps.yaml said before the E entries were merged. The sandbox's
    OWN COPY of codebook/E4.md is removed here -- never the real file -- so the plugin and
    scripts/checks/E4.py both see it absent, which is the only way the two can agree."""
    sb.fresh("E4")
    os.remove(sb.path("codebook", "E4.md"))
    assert sp._e_codebook("E4") == (None, "none")

    plugin = sp.E4Plugin()
    scope = {"chapters": None, "papers": None, "items": {SCRIPT_DECIDED}}
    plugin.list_items(scope)
    # With no codebook the input carries no `codebook` key and codebook_version is spec 13.0's
    # literal "none", which is what the agent then echoes.
    assert "codebook" not in sb.work_input("E4", SCRIPT_DECIDED, "runA")
    assert sb.work_input("E4", SCRIPT_DECIDED, "runA")["codebook_version"] == "none"
    for run_label in ("runA", "runB"):
        sb.write_out("E4", SCRIPT_DECIDED, run_label, _e4_answer("recall", version="none"))
    assert plugin.check(scope) == []
    assert len(sb.flags("E4_NO_CODEBOOK", SCRIPT_DECIDED)) == 1
    assert sb.flags("E4_NO_CODEBOOK", SCRIPT_DECIDED)[0]["severity"] == "low"
    assert sb.record(SCRIPT_DECIDED)["e4_codebook_version"] == "none"


# ============================================================================================
# E5 -- the item is ONE WRONG OPTION, and three is the normal case, not a quota
# ============================================================================================

def _e5_answer(option, trap="look_alike_term",
                why="The option names the neighbouring unit on the same page", description=""):
    return {"option": str(option), "trap": trap, "why": why, "new_description": description,
            "confidence": "high"}


def test_e5_creates_one_item_per_genuinely_wrong_option(sb):
    plugin = sp.E5Plugin()
    by_question = {}
    for item_id, qid, _record, number, _text in plugin._items(NO_FILTER):
        by_question.setdefault(qid, []).append((item_id, number))

    # normal, answer 1 -> three wrong options
    assert [n for _i, n in by_question["Q-991001"]] == ["2", "3", "4"]
    assert by_question["Q-991001"][0][0] == "Q-991001#opt2"
    # multiple_accepted, official key "1,3" -> TWO wrong options, not three
    assert [n for _i, n in by_question["Q-991004"]] == ["2", "4"]
    # dropped with a B8 corrected_answer of 1 -> the correction is the answer, three items
    assert [n for _i, n in by_question["Q-991005"]] == ["2", "3", "4"]
    # dropped with no corrected_answer -> NO item at all, nothing invented
    assert "Q-991006" not in by_question


def test_e5_records_a_question_with_no_wrong_option_as_skipped(sb):
    plugin = sp.E5Plugin()
    plugin.check({"chapters": None, "papers": None, "items": {"Q-991006"}})
    status = sb.status("E5", "Q-991006")
    assert status["status"] == "skipped"
    assert "no identifiable wrong option" in status["check_message"]
    assert sb.record("Q-991006")["option_traps"] == []


def test_e5_two_agreeing_runs_merge_into_option_traps_per_option(sb):
    plugin = sp.E5Plugin()
    scope = {"chapters": None, "papers": None, "items": {SCRIPT_DECIDED}}
    plugin.list_items(scope)
    traps = {"2": "look_alike_term", "3": "wrong_quantity", "4": "half_true"}
    for number, trap in traps.items():
        for run_label in ("runA", "runB"):
            sb.write_out("E5", f"{SCRIPT_DECIDED}#opt{number}", run_label,
                         _e5_answer(number, trap))
    assert plugin.check(scope) == []
    rows = sb.record(SCRIPT_DECIDED)["option_traps"]
    assert [r["option"] for r in rows] == ["2", "3", "4"]
    assert {r["option"]: r["trap"] for r in rows} == traps
    for number in traps:
        assert sb.status("E5", f"{SCRIPT_DECIDED}#opt{number}")["status"] == "pass"


def test_e5_disagreement_adjudicates_and_unsure_takes_run_a(sb):
    plugin = sp.E5Plugin()
    item_id = f"{SCRIPT_DECIDED}#opt2"
    scope = {"chapters": None, "papers": None, "items": {item_id}}
    plugin.list_items(scope)
    sb.write_out("E5", item_id, "runA", _e5_answer(2, "look_alike_term"))
    sb.write_out("E5", item_id, "runB", _e5_answer(2, "name_variant"))
    lines = plugin.check(scope)
    assert [(l.item_id, l.agent) for l in lines] == [(item_id, "x-adjudicator")]
    assert "runs disagree on the trap" in sb.work_input("E5", item_id, "adjudicated")["failed_check"]

    sb.write_out("E5", item_id, "adjudicated", {"choice": "unsure"})
    assert plugin.check(scope) == []
    rows = sb.record(SCRIPT_DECIDED)["option_traps"]
    assert [r["trap"] for r in rows] == ["look_alike_term"]
    assert sb.status("E5", item_id)["status"] == "flagged"
    assert len(sb.flags("E5_ADJUDICATED", item_id)) == 1


def test_e5_filter_by_question_id_reaches_its_option_items(sb):
    lines = sp.E5Plugin().list_items({"chapters": None, "papers": None, "items": {SCRIPT_DECIDED}})
    assert {l.item_id for l in lines} == {f"{SCRIPT_DECIDED}#opt{n}" for n in (2, 3, 4)}


# ============================================================================================
# E6 -- five script fields plus one agent question
# ============================================================================================

def test_e6_dispatches_only_the_tie_break_and_stores_the_five_script_fields(sb):
    plugin = sp.E6Plugin()
    lines = plugin.list_items(NO_FILTER)
    assert [l.item_id for l in lines] == [E6_HANDOVER]

    plugin.check(NO_FILTER)
    decided = sb.record(SCRIPT_DECIDED)
    assert decided["stem_context"] == "plain"          # the script decided it, legitimately
    assert decided["answer_form"] == "term"
    assert decided["negation"] == "none"
    assert decided["figure_role"] == "none"
    assert decided["descriptive_tags"]["stem_context"] == "plain"
    assert sb.status("E6", SCRIPT_DECIDED)["status"] == "pass"

    # The handover question gets its five script fields now and NO stem_context at all: writing
    # None there would look like a decided value.
    waiting = sb.record(E6_HANDOVER)
    assert waiting["answer_form"] == "statement"
    assert "stem_context" not in waiting
    assert sb.status("E6", E6_HANDOVER) is None


def test_e6_safe_default_is_unsure_and_never_plain(sb):
    """config/steps.yaml E6 safe_default: `unsure` + E6_CONTEXT_UNSURE (low). codebook/E6.md
    section 2 is that `plain` can never win a tie-break, and this agent only runs when two or
    more contexts already applied."""
    plugin = sp.E6Plugin()
    plugin.list_items(NO_FILTER)
    bad = {"stem_context": "plain", "why": "nothing much applies here really", "confidence": "high"}
    sb.write_out("E6", E6_HANDOVER, "runA", bad)
    lines = plugin.check(NO_FILTER)
    assert [(l.item_id, l.run_label) for l in lines] == [(E6_HANDOVER, "retry1")]
    sb.write_out("E6", E6_HANDOVER, "retry1", bad)
    assert plugin.check(NO_FILTER) == []

    record = sb.record(E6_HANDOVER)
    assert record["stem_context"] == "unsure"
    assert record["stem_context"] != "plain"
    unsure = sb.flags("E6_CONTEXT_UNSURE", E6_HANDOVER)
    assert len(unsure) == 1 and unsure[0]["severity"] == "low"


def test_e6_a_good_agent_answer_resolves_pass(sb):
    plugin = sp.E6Plugin()
    plugin.list_items(NO_FILTER)
    sb.write_out("E6", E6_HANDOVER, "runA", {
        "stem_context": "reaction_given",
        "why": "Both reaction_given and figure_given fired; the reaction is the thing the "
               "question cannot be answered without, the drawing only shows it",
        "confidence": "high"})
    assert plugin.check(NO_FILTER) == []
    assert sb.record(E6_HANDOVER)["stem_context"] == "reaction_given"
    assert sb.status("E6", E6_HANDOVER)["status"] == "pass"
    assert sb.flags("E6_CONTEXT_UNSURE", E6_HANDOVER) == []


# ============================================================================================
# E0 -- discovery, and the sample gate
# ============================================================================================

def test_e0_refuses_to_dispatch_below_specs_sample_size(sb):
    plugin = sp.E0Plugin()
    assert plugin.list_items(NO_FILTER) == []
    reason = plugin.list_reason()
    assert "NOT dispatching" in reason and "~300" in reason


def test_e0_open_look_is_shown_no_categories_and_no_codebook(sb, monkeypatch):
    """Spec 13/E0 step 1: e0-open-look answers "with NO categories shown". The sample floor is
    lowered HERE ONLY so the dispatch path can be exercised at all -- the real bank has 10
    canonical questions against spec's ~300."""
    import e0_category_sheet
    monkeypatch.setattr(e0_category_sheet, "SAMPLE_FLOOR", 1)
    monkeypatch.setattr(e0_category_sheet, "PER_SUBJECT_FLOOR", 0)
    plugin = sp.E0Plugin()
    lines = plugin.list_items(NO_FILTER)
    assert lines and all(l.agent == "e0-open-look" for l in lines)

    payload = sb.work_input("E0", SCRIPT_DECIDED, "runA")
    assert set(payload) == {"question", "answer_taught", "evidence", "subject"}
    assert "codebook" not in payload and "allowed" not in payload


def test_e0_groups_per_tag_only_once_every_free_answer_exists(sb, monkeypatch):
    import e0_category_sheet
    monkeypatch.setattr(e0_category_sheet, "SAMPLE_FLOOR", 1)
    monkeypatch.setattr(e0_category_sheet, "PER_SUBJECT_FLOOR", 0)
    plugin = sp.E0Plugin()
    sample = sorted(plugin._sample())
    plugin.list_items(NO_FILTER)

    open_look = {"student_must": "remember which unit goes with which quantity",
                 "built_as": "a short question with four one-word answers",
                 "asks_to_pick": "the right unit",
                 "ncert_material": "a line in the units box",
                 "wrong_options": {"2": "a near-by unit", "3": "another near-by unit",
                                   "4": "a unit from a different quantity"}}
    for qid in sample:
        answer = plugin._build_open_look_input(sb.record(qid))["answer_taught"]["number"]
        payload = dict(open_look)
        payload["wrong_options"] = {k: v for k, v in open_look["wrong_options"].items()
                                     if k != str(answer)} or {"2": "a near-by unit"}
        sb.write_out("E0", qid, "runA", payload)
    plugin.check(NO_FILTER)

    # Q-991006 is the dropped question with no answer at all, so "the answer is not one of the
    # wrong options" cannot be checked and its own free answer is BLOCKED -- it must not block the
    # grouping forever, and it must not be grouped either.
    assert sb.status("E0", "Q-991006")["status"] == "blocked"

    lines = plugin.list_items(NO_FILTER)
    assert {l.item_id for l in lines} == {f"tag__{t}" for t in plugin.TAG_SOURCE_FIELD}
    assert all(l.agent == "e0-category-grouper" for l in lines)
    grouper_input = sb.work_input("E0", "tag__thinking", "runA")
    assert grouper_input["tag"] == "thinking"
    assert len(grouper_input["answers"]) == len(sample) - 1
    assert "Q-991006" not in {a["question_id"] for a in grouper_input["answers"]}
    assert grouper_input["answers"][0]["text"].startswith("remember which unit")
    assert "recall" in grouper_input["starting_list"]


# ============================================================================================
# Shared helpers
# ============================================================================================

def test_e_candidates_gate_on_the_steps_own_needs_entry(sb):
    """Each E step opens only when the step its config/steps.yaml `needs` line names is resolved
    -- the same gate D5-D9 hard-code one at a time."""
    assert set(sp._e_candidates("E1")) == set(sp._e_candidates("E0"))
    assert SCRIPT_DECIDED in sp._e_candidates("E1")
    os.remove(sb.path("steps", "D7", "status", f"{SCRIPT_DECIDED}.json"))
    assert SCRIPT_DECIDED not in sp._e_candidates("E1")
    assert SCRIPT_DECIDED in sp._e_candidates("E0")  # E0 needs D8, which is untouched


def test_e_set_tags_keeps_a_codebook_version_map_across_steps(sb):
    sp._e_set_tags("E1", SCRIPT_DECIDED, {"question_type": "single_statement"}, "v1", "pass",
                    cb_version="aaaaaaaaaaaa")
    sp._e_set_tags("E4", SCRIPT_DECIDED, {"category_primary": "recall"}, "v1", "pass",
                    cb_version="bbbbbbbbbbbb")
    record = sb.record(SCRIPT_DECIDED)
    assert record["codebook_version"] == {"E1": "aaaaaaaaaaaa", "E4": "bbbbbbbbbbbb"}
    assert record["e1_codebook_version"] == "aaaaaaaaaaaa"
    assert record["field_sources"]["category_primary"]["step"] == "E4"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
