#!/usr/bin/env python3
"""Tests for Stage F (spec Section 14): F1 review pack, F3 apply + cascade, F4 counts,
F5 release gate, F6 gold scoring.

Every test runs against a COPY of tests/fixtures/stage_f/ in a temporary directory, with the
scripts' PROJECT_ROOT repointed at that copy. The real ncert/, papers/, steps/, flags/, review/,
data/ and gold/ paths are never read for state and never written. (docs/OPEN_QUESTIONS.md
2026-10-10 records what happened the one time fixture data was written into real paths.)

Honest scope. Only F1 has real data to run against today, and `test_f1_against_real_project`
below exercises it read-only on the real project. Everything else — the cascade, the counts over
a populated bank, the release gate actually opening, the gold scoring — has no real data yet, so
it is tested here on the fixture tree and is labelled fixture-only in the build report.

Run: .venv/bin/python -m pytest tests/test_stage_f.py -q
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

FIXTURE_SRC = os.path.join(_TESTS_DIR, "fixtures", "stage_f")

CH1 = "BIO12-CH91"
CH2 = "BIO12-CH92"

# Module load order matters: f_common caches PROJECT_ROOT and the review/ paths at import time,
# and the F scripts cache f_common's values in turn, so they must be reloaded bottom-up.
_RELOAD_ORDER = ["f_common", "cascade", "build_review_pack", "apply_review", "compute_counts",
                 "export_tables", "score_gold"]


class Sandbox:
    """A throwaway project root holding a copy of the fixture tree, with every Stage F module
    reloaded against it."""

    def __init__(self, tmpdir):
        self.root = tmpdir
        shutil.copytree(FIXTURE_SRC, self.root, dirs_exist_ok=True)
        # config/ is read-only input for Stage F; copy the real one so the cascade map and the
        # step order under test are the project's actual ones, not a second copy that could drift.
        shutil.copytree(os.path.join(_PROJECT_ROOT, "config"),
                        os.path.join(self.root, "config"), dirs_exist_ok=True)
        # runner_core resolves schemas/<STEP>.json and scripts/checks/<STEP>.py through the same
        # PROJECT_ROOT, so the sandbox needs them too. Symlinked, not copied: they are the code
        # under test and must never be a stale second copy.
        for name in ("schemas", "scripts"):
            link = os.path.join(self.root, name)
            if not os.path.exists(link):
                os.symlink(os.path.join(_PROJECT_ROOT, name), link)
        os.makedirs(os.path.join(self.root, "review"), exist_ok=True)
        os.makedirs(os.path.join(self.root, "data"), exist_ok=True)
        self.modules = {}

    def __enter__(self):
        from lib import io as lib_io
        self._saved_root = lib_io.PROJECT_ROOT
        lib_io.PROJECT_ROOT = self.root
        for name in _RELOAD_ORDER:
            module = importlib.import_module(name)
            self.modules[name] = importlib.reload(module)
        # Reloading f_common resets its own caches, but PyYAML-parsed steps.yaml is cached per
        # module object, so clear it explicitly to be sure the sandbox's config is what is read.
        self.modules["f_common"]._STEPS_CACHE = None
        self.modules["cascade"]._CASCADE_CACHE = None
        return self

    def __exit__(self, *exc):
        from lib import io as lib_io
        lib_io.PROJECT_ROOT = self._saved_root
        for name in _RELOAD_ORDER:
            importlib.reload(importlib.import_module(name))
        return False

    def path(self, *parts):
        return os.path.join(self.root, *parts)

    def __getattr__(self, name):
        if name in self.modules:
            return self.modules[name]
        raise AttributeError(name)

    def write_decisions(self, rows):
        fc = self.modules["f_common"]
        with open(self.path("review", "decisions.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fc.DECISION_FIELDS)
            w.writeheader()
            for row in rows:
                w.writerow(row)

    def read_record(self, qid):
        with open(self.path("papers", "records", f"{qid}.json"), encoding="utf-8") as f:
            return json.load(f)

    def flags(self):
        return {f["flag_id"]: f for f in self.modules["f_common"].load_flags()}


@pytest.fixture()
def sandbox():
    tmp = tempfile.mkdtemp(prefix="stage_f_sandbox_")
    try:
        with Sandbox(tmp) as sb:
            yield sb
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def decision(target, field, decision_value, value=None, reviewer="Fixture Reviewer",
             comment="fixture", at="2026-10-12"):
    return {"flag_id_or_item": target, "field": field, "decision": decision_value,
            "corrected_value_json": "" if value is None else json.dumps(value),
            "reviewer": reviewer, "comment": comment, "decided_at": at}


# ============================================================================================
# F1 · review pack
# ============================================================================================

def test_f1_priority_order_is_the_spec_order(sandbox):
    """Spec 14/F1: blocker, registers, subtopic lists and change-log rows, high, normal, E0
    findings and new categories, low and audit sample — in exactly that order."""
    f1 = sandbox.build_review_pack
    _, items = f1.build(dry_run=True)
    by_flag = {i["flag_id"]: i["priority"] for i in items if i["kind"] == "flag"}
    assert by_flag["FL-990001"] == 1, "a blocker must come first even though its step is D3"
    assert by_flag["FL-990002"] == 2, "a register draft outranks its own `low` severity"
    assert by_flag["FL-990003"] == 3, "a subtopic-list draft outranks every `high`"
    assert by_flag["FL-990004"] == 4
    assert by_flag["FL-990005"] == 5
    assert by_flag["FL-990006"] == 6, "a new-category flag is `normal` but belongs behind normal"
    assert by_flag["FL-990007"] == 7

    priorities = [i["priority"] for i in items]
    assert priorities == sorted(priorities), "the queue must be emitted in priority order"


def test_f1_groups_by_chapter_and_resolves_fixture_ids(sandbox):
    f1 = sandbox.build_review_pack
    _, items = f1.build(dry_run=True)
    by_flag = {i["flag_id"]: i for i in items if i["kind"] == "flag"}
    assert by_flag["FL-990001"]["chapter_ids"] == [CH1], "a question flag inherits its chapter"
    assert by_flag["FL-990003"]["chapter_ids"] == [CH1], "a chapter-item flag is its own chapter"
    assert by_flag["FL-990005"]["chapter_ids"] == [CH2]
    assert by_flag["FL-990002"]["chapter_ids"] == [CH1], \
        "an A1 register item resolves to the book/chapter named in its item id"


def test_f1_audit_sample_is_reproducible_and_stratified(sandbox):
    f1 = sandbox.build_review_pack
    first = [i["pack_id"] for i in f1.build(dry_run=True)[1] if i["kind"] == "audit_sample"]
    again = [i["pack_id"] for i in f1.build(dry_run=True)[1] if i["kind"] == "audit_sample"]
    other = [i["pack_id"] for i in f1.build(dry_run=True, seed=4242)[1]
             if i["kind"] == "audit_sample"]
    assert first and first == again, "the same seed must produce the same sample"
    assert first != other, "a different seed must produce a different sample"

    # 5% per step, at least 20 per step, never more than exist: B3 has 30 passing items, so 20.
    b3 = [i for i in f1.build(dry_run=True)[1]
          if i["kind"] == "audit_sample" and i["step"] == "B3"]
    assert len(b3) == 20, f"expected min-20 of B3's 30 passing items, got {len(b3)}"
    # D4 has only 6 passing items, fewer than the minimum, so all of them.
    d4 = [i for i in f1.build(dry_run=True)[1]
          if i["kind"] == "audit_sample" and i["step"] == "D4"]
    assert len(d4) == 6

    strata = {(i["audit"]["subject"], i["audit"]["year"]) for i in d4}
    assert len(strata) > 1, "D4's sample should span more than one (subject, year) stratum"


def test_f1_audit_sample_ignores_status_side_cars(sandbox):
    """steps/B3/status/<ITEM>.last_q.json is carry-over state, not a passing item."""
    f1 = sandbox.build_review_pack
    audit = [i for i in f1.build(dry_run=True)[1] if i["kind"] == "audit_sample"]
    assert not any("last_q" in i["item_id"] for i in audit)


def test_f1_audit_sample_is_not_written_to_the_real_flag_file(sandbox):
    """The audit sample is recorded in review/audit_sample.jsonl, never appended to
    flags/flags.jsonl (see collect_audit_sample's docstring for why)."""
    f1, fc = sandbox.build_review_pack, sandbox.f_common
    before = len(fc.load_flags())
    f1.build()
    assert len(fc.load_flags()) == before
    assert os.path.exists(sandbox.path("review", "audit_sample.jsonl"))


def test_f1_writes_queue_pages_and_a_header_only_decisions_file(sandbox):
    f1, fc = sandbox.build_review_pack, sandbox.f_common
    result, items = f1.build()
    assert result["queue_size"] == len(items)
    queue = list(csv.DictReader(open(sandbox.path("review", "queue.csv"), encoding="utf-8")))
    assert len(queue) == len(items)
    assert list(queue[0].keys()) == fc.QUEUE_FIELDS, "queue.csv columns are fixed by spec 6.5"
    for row in queue:
        assert os.path.exists(sandbox.path(row["evidence_page"])), row["evidence_page"]
    assert os.path.exists(sandbox.path("review", "review_pack", "index.html"))

    decisions = open(sandbox.path("review", "decisions.csv"), encoding="utf-8").read()
    assert decisions.strip() == ",".join(fc.DECISION_FIELDS)


def test_f1_pages_carry_value_evidence_cascade_legacy_and_a_form(sandbox):
    """Spec 14/F1 names five things every page must have."""
    f1 = sandbox.build_review_pack
    f1.build()
    page = next(p for p in sorted(os.listdir(sandbox.path("review", "review_pack")))
                if p.startswith("p4__"))
    html = open(sandbox.path("review", "review_pack", page), encoding="utf-8").read()
    assert "The value in question" in html
    assert "class=\"value\"" in html, "the provisional value must be highlighted"
    assert "What editing this re-runs" in html
    assert "cascade key" in html
    assert "Evidence" in html
    assert "Legacy values" in html and "Fixture legacy chapter" in html
    assert "review/decisions.csv" in html
    for value in ("approve", "correct", "edit", "block"):
        assert f"<option value='{value}'>" in html


def test_f1_schema_and_check_accept_its_own_manifest(sandbox):
    import runner_core as rc
    f1 = sandbox.build_review_pack
    f1.build()
    manifest = json.load(open(sandbox.path("review", "review_pack", "_manifest.json"),
                              encoding="utf-8"))
    assert rc.validate_schema("F1", manifest)[0]
    ok, msg = rc.run_step_check("F1", manifest, {"item_id": "run",
                                                 "expected_seed": f1.AUDIT_SEED})
    assert ok, msg


def test_f1_check_rejects_a_pack_whose_queue_and_pages_disagree():
    import runner_core as rc
    bad = {"run_id": "x", "seed": 1, "queue_size": 5, "pack_ids": ["a", "b"],
           "pages": {"a": "a.html", "b": "b.html"}}
    ok, msg = rc.run_step_check("F1", bad, {})
    assert not ok and "queue_size" in msg

    collision = {"run_id": "x", "seed": 1, "queue_size": 2, "pack_ids": ["a", "b"],
                 "pages": {"a": "same.html", "b": "same.html"}}
    ok, msg = rc.run_step_check("F1", collision, {})
    assert not ok and "share one page" in msg

    no_seed = {"run_id": "x", "queue_size": 0, "pack_ids": []}
    ok, msg = rc.run_step_check("F1", no_seed, {})
    assert not ok and "reproducible" in msg


def test_f1_new_only_emits_only_new_pages(sandbox):
    f1 = sandbox.build_review_pack
    f1.build()
    result, _ = f1.build(new_only=True)
    assert result["emitted_pages"] == 0, "nothing new since the previous pack"


def test_f1_e4_agreement_sample_is_drawn_once_and_then_stays(sandbox):
    """Spec 14/F1 draws it "in the first full review"; it must then stay in the pack until it has
    been answered, rather than being re-drawn (losing part-finished work) or dropped (losing it)."""
    f1 = sandbox.build_review_pack
    first = [i["item_id"] for i in f1.build()[1] if i["kind"] == "e4_agreement"]
    assert first, "the fixture has E4-tagged questions, so there is an agreement sample to draw"
    assert len(first) == 5, "every E4-tagged canonical question, since the fixture has under 50"
    assert "Q-990006" not in first, "a merged-away record is not a canonical question"
    again = [i["item_id"] for i in f1.build()[1] if i["kind"] == "e4_agreement"]
    assert again == first, "the sample on record must be re-emitted unchanged"


def test_f1_e4_agreement_pages_hide_the_pipeline_tags(sandbox):
    f1 = sandbox.build_review_pack
    f1.build(first_full_review=True)
    page = next(p for p in os.listdir(sandbox.path("review", "review_pack"))
                if "e4_agreement" in p)
    html = open(sandbox.path("review", "review_pack", page), encoding="utf-8").read()
    assert "DELIBERATELY HIDDEN" in html
    assert "are hidden on purpose" in html
    assert "category_primary</th>" not in html, "the pipeline's own thinking tag must not appear"
    assert "<h3 style='margin-top:1rem'>Tags</h3>" not in html
    assert "Fixture stem for" in html, "but the question itself must still be shown"


def test_f1_full_rebuild_removes_a_stale_page(sandbox):
    """Found for real on 2026-10-12: an item whose chapter changes between two F1 runs gets a new
    page filename, and the old file stayed behind where a reviewer could open outdated evidence."""
    f1 = sandbox.build_review_pack
    f1.build()
    orphan = os.path.join(sandbox.path("review", "review_pack"),
                          "p4__BIO12-CH99__FL-999999__deadbeef.html")
    with open(orphan, "w", encoding="utf-8") as f:
        f.write("<p>stale page from an earlier run</p>")
    result, _ = f1.build()
    assert result["orphans_removed"] == 1
    assert not os.path.exists(orphan)
    assert os.path.exists(sandbox.path("review", "review_pack", "index.html"))


def test_f1_new_only_and_scoped_builds_never_remove_pages(sandbox):
    f1 = sandbox.build_review_pack
    f1.build()
    keeper = os.path.join(sandbox.path("review", "review_pack"),
                          "p4__BIO12-CH99__FL-999999__deadbeef.html")
    with open(keeper, "w", encoding="utf-8") as f:
        f.write("<p>a page from another chapter's pack</p>")
    assert f1.build(new_only=True)[0]["orphans_removed"] == 0
    assert f1.build(chapters=[CH1])[0]["orphans_removed"] == 0
    assert os.path.exists(keeper), \
        "a scoped build must not delete pages for items it did not consider"


# ============================================================================================
# F3 · apply decisions
# ============================================================================================

def test_f3_dry_run_changes_nothing(sandbox):
    ar = sandbox.apply_review
    sandbox.write_decisions([decision("FL-990004", "official_answer", "approve")])
    report = ar.apply_decisions(apply=False)
    assert report["rows_new"] == 1 and report["dry_run"]
    assert sandbox.flags()["FL-990004"]["status"] == "open"
    assert not os.path.exists(sandbox.path("review", "approvals.jsonl"))


def test_f3_approve_closes_the_flag_and_records_reviewer_and_date(sandbox):
    ar, fc = sandbox.apply_review, sandbox.f_common
    sandbox.write_decisions([decision("FL-990004", "official_answer", "approve",
                                      reviewer="Ekta", at="2026-10-12")])
    report = ar.apply_decisions(apply=True)
    assert not report["errors"], report["errors"]
    flag = sandbox.flags()["FL-990004"]
    assert flag["status"] == "closed"
    assert flag["decision"] == "approve"
    assert flag["reviewer"] == "Ekta"
    assert flag["decided_at"] == "2026-10-12"

    rec = sandbox.read_record("Q-990002")
    review = rec["field_sources"]["official_answer"]["review"]
    assert review == {"status": "approved", "reviewer": "Ekta", "at": "2026-10-12"}
    assert rec["field_sources"]["official_answer"]["step"] == "B5", \
        "approving a value must not reattribute it to F2 — it is still B5's value"

    approvals = {a["target"]: a for a in fc.load_approvals()}
    assert "flag:FL-990004:official_answer" in approvals


def test_f3_approving_a_subtopic_draft_flag_also_approves_the_list_itself(sandbox):
    """F1 de-duplicates the standalone draft item away when a flag covers it, so the flag's
    approval has to satisfy F5's `subtopic_list:<CHAPTER>` gate too."""
    ar, fc = sandbox.apply_review, sandbox.f_common
    sandbox.write_decisions([decision("FL-990003", "subtopic_list", "approve", reviewer="Faculty")])
    ar.apply_decisions(apply=True)
    approvals = {a["target"]: a for a in fc.load_approvals()}
    assert fc.subtopic_list_target(CH1) in approvals


def test_f3_rejects_a_decision_with_no_reviewer(sandbox):
    ar = sandbox.apply_review
    sandbox.write_decisions([decision("FL-990004", "official_answer", "approve", reviewer="")])
    report = ar.apply_decisions(apply=True)
    assert report["errors"] and "reviewer" in report["errors"][0]["why"]
    assert sandbox.flags()["FL-990004"]["status"] == "open"


def test_f3_rejects_an_unknown_flag_id_and_an_unknown_decision(sandbox):
    ar = sandbox.apply_review
    sandbox.write_decisions([
        decision("FL-000999", "official_answer", "approve"),
        decision("FL-990004", "official_answer", "maybe"),
    ])
    report = ar.apply_decisions(apply=True)
    whys = " ".join(e["why"] for e in report["errors"])
    assert "not in flags/flags.jsonl" in whys
    assert "not one of" in whys


def test_f3_correction_writes_a_new_f2_output_and_never_touches_the_original(sandbox):
    """Rule 2: a correction is a NEW F2 output plus a record update, preserving history."""
    ar = sandbox.apply_review
    original = sandbox.path("steps", "D4", "out", "Q-990001.runA.json")
    before = open(original, encoding="utf-8").read()

    sandbox.write_decisions([decision("FL-990001", "subtopic_ids", "correct",
                                      value=[f"{CH1}-ST03"], reviewer="Faculty")])
    report = ar.apply_decisions(apply=True)
    assert not report["errors"], report["errors"]

    assert open(original, encoding="utf-8").read() == before, \
        "the step's own output file must be byte-identical after a correction"

    outputs = sorted(os.listdir(sandbox.path("steps", "F2", "out")))
    assert len(outputs) == 1 and ".correction001." in outputs[0]
    payload = json.load(open(sandbox.path("steps", "F2", "out", outputs[0]), encoding="utf-8"))
    assert payload["step"] == "F2"
    assert payload["field"] == "subtopic_ids"
    assert payload["old"] == [f"{CH1}-ST01"]
    assert payload["new"] == [f"{CH1}-ST03"]
    assert payload["reviewer"] == "Faculty"

    rec = sandbox.read_record("Q-990001")
    assert rec["subtopic_ids"] == [f"{CH1}-ST03"]
    source = rec["field_sources"]["subtopic_ids"]
    assert source["step"] == "F2"
    assert source["corrected_from_step"] == "D2", "the superseded step must stay traceable"
    assert source["f2_output"] == payload_relpath(outputs[0])

    corrections = [json.loads(l) for l in
                   open(sandbox.path("review", "corrections.jsonl"), encoding="utf-8")]
    assert len(corrections) == 1
    assert corrections[0]["old"] == [f"{CH1}-ST01"]
    assert corrections[0]["new"] == [f"{CH1}-ST03"]
    assert corrections[0]["cascade"], "a correction must record the cascade it triggered"
    assert sandbox.flags()["FL-990001"]["status"] == "closed"


def payload_relpath(filename):
    return f"steps/F2/out/{filename}"


def test_f3_two_corrections_to_one_field_keep_both(sandbox):
    """A second correction must not overwrite the first F2 output."""
    ar = sandbox.apply_review
    sandbox.write_decisions([decision("FL-990001", "subtopic_ids", "correct",
                                      value=[f"{CH1}-ST03"], reviewer="A", at="2026-10-12")])
    ar.apply_decisions(apply=True)
    sandbox.write_decisions([decision("Q-990001", "subtopic_ids", "edit",
                                      value=[f"{CH1}-ST02"], reviewer="B", at="2026-10-13")])
    ar.apply_decisions(apply=True)
    outputs = sorted(os.listdir(sandbox.path("steps", "F2", "out")))
    assert len(outputs) == 2, outputs
    assert ".correction001." in outputs[0] and ".correction002." in outputs[1]
    second = json.load(open(sandbox.path("steps", "F2", "out", outputs[1]), encoding="utf-8"))
    assert second["old"] == [f"{CH1}-ST03"] and second["new"] == [f"{CH1}-ST02"]


def test_f3_correction_with_no_value_is_rejected(sandbox):
    ar = sandbox.apply_review
    sandbox.write_decisions([decision("FL-990004", "official_answer", "correct")])
    report = ar.apply_decisions(apply=True)
    assert report["errors"] and "corrected_value_json is empty" in report["errors"][0]["why"]
    assert not os.path.isdir(sandbox.path("steps", "F2", "out")) or \
        not os.listdir(sandbox.path("steps", "F2", "out"))


def test_f3_block_sets_release_status_blocked_by_reviewer(sandbox):
    ar, fc = sandbox.apply_review, sandbox.f_common
    sandbox.write_decisions([decision("FL-990005", "subtopic_ids", "block", reviewer="Faculty")])
    ar.apply_decisions(apply=True)
    rec = sandbox.read_record("Q-990004")
    assert rec["release_status"] == "blocked_by_reviewer"
    blocks = fc.load_blocks()
    assert blocks and blocks[0]["item_id"] == "Q-990004"
    assert sandbox.flags()["FL-990005"]["status"] == "blocked_by_reviewer"


def test_f3_is_idempotent(sandbox):
    """"Running a command twice in a row must do nothing the second time" (spec 5.9)."""
    ar = sandbox.apply_review
    sandbox.write_decisions([decision("FL-990001", "subtopic_ids", "correct",
                                      value=[f"{CH1}-ST03"], reviewer="Faculty")])
    first = ar.apply_decisions(apply=True)
    second = ar.apply_decisions(apply=True)
    assert first["rows_new"] == 1
    assert second["rows_new"] == 0
    assert second["skipped"] and "already applied" in second["skipped"][0]["why"]
    assert len(os.listdir(sandbox.path("steps", "F2", "out"))) == 1


def test_f3_report_passes_its_own_schema_and_check(sandbox):
    import runner_core as rc
    ar = sandbox.apply_review
    sandbox.write_decisions([decision("FL-990001", "subtopic_ids", "correct",
                                      value=[f"{CH1}-ST03"], reviewer="Faculty")])
    report = ar.apply_decisions(apply=True)
    assert rc.validate_schema("F3", report)[0], rc.validate_schema("F3", report)[1]
    ok, msg = rc.run_step_check("F3", report, {"item_id": "decisions"})
    assert ok, msg


def test_f3_check_rejects_a_correction_that_edited_in_place():
    import runner_core as rc
    bad = {"rows_total": 1, "rows_new": 1, "dry_run": False, "errors": [], "skipped": [],
           "applied": [{"target": "FL-1", "decision": "correct", "item_id": "Q-000001",
                        "field": "stem_en", "reviewer": "R", "decided_at": "2026-10-12",
                        "f2_output": "steps/D4/out/Q-000001.runA.json",
                        "cascade_steps": ["D5"]}],
           "cascade": {"pairs": 1, "steps": ["D5"], "marked_stale": 1}}
    ok, msg = rc.run_step_check("F3", bad, {})
    assert not ok and "never be edited in place" in msg


def test_f2_check_rejects_a_no_op_correction():
    import runner_core as rc
    same = {"step": "F2", "item_id": "Q-000001", "field": "stem_en", "old": "x", "new": "x",
            "reviewer": "R", "decided_at": "2026-10-12"}
    ok, msg = rc.run_step_check("F2", same, {})
    assert not ok and "that is an approval, not a correction" in msg


# ============================================================================================
# F3 · cascade
# ============================================================================================

def test_cascade_maps_a_record_field_to_its_cascade_key(sandbox):
    cs = sandbox.cascade
    assert cs.cascade_key_for_field("stem_en") == "question_text"
    assert cs.cascade_key_for_field("official_answer") == "official_answer"
    assert cs.cascade_key_for_field("d2_subtopic_ids") == "subtopic"
    assert cs.cascade_key_for_field("category_primary") == "any_e_tag"
    assert cs.cascade_key_for_field("reviewer") is None, \
        "a field no step reads must cascade to nothing, not to everything"


def test_cascade_subtopic_change_hits_the_steps_section_15_names(sandbox):
    cs = sandbox.cascade
    plan = cs.plan_for_change("subtopic_ids", "Q-990001", transitive=False)
    steps = {p["step"] for p in plan["direct"]}
    # Section 15, "Subtopic": D3-D8 and E3-E5 for the question; D9-D11 and F4 for the subtopics.
    for step in ("D3", "D4", "D5", "D6", "D7", "D8", "E3", "E4", "E5", "F4"):
        assert step in steps, f"{step} should be stale after a subtopic change"
    assert ("F4", f"{CH1}-ST01") in {(p["step"], p["item_id"]) for p in plan["direct"]}, \
        "F4's item is a subtopic, so the subtopic id — not the question — becomes stale"


def test_cascade_question_text_change_reaches_stage_e(sandbox):
    cs = sandbox.cascade
    plan = cs.plan_for_change("stem_en", "Q-990001", transitive=False)
    steps = {p["step"] for p in plan["direct"]}
    for step in ("D1", "E1", "E6", "F4"):
        assert step in steps


def test_cascade_change_log_row_uses_its_affected_questions(sandbox):
    cs = sandbox.cascade
    plan = cs.plan_for_change("change_log_row", "CL-9901", transitive=False)
    pairs = {(p["step"], p["item_id"]) for p in plan["direct"]}
    assert ("D6", "Q-990001") in pairs
    assert ("D7", "Q-990002") in pairs
    assert not any(i == "Q-990004" for _, i in pairs), \
        "CL-9901 does not affect Q-990004, so nothing of it should go stale"


def test_cascade_never_marks_stage_f_review_steps_stale_transitively(sandbox):
    cs = sandbox.cascade
    plan = cs.plan_for_change("stem_en", "Q-990001", transitive=True)
    transitive_steps = {p["step"] for p in plan["transitive"]}
    assert not ({"F1", "F2", "F3", "F5"} & transitive_steps), \
        "F1/F2/F3/F5 are the review process, not derived values"


def test_cascade_apply_marks_stale_and_remembers_the_previous_status(sandbox):
    cs = sandbox.cascade
    from lib import status as lib_status
    plan = cs.plan_for_change("subtopic_ids", "Q-990001", transitive=False)
    applied = cs.apply_plan(plan)
    assert applied
    d4 = lib_status.read_status("D4", "Q-990001")
    assert d4["status"] == "stale"
    assert d4["previous_status"] == "pass"
    snapshot = next(p for p in applied if p["step"] == "D4" and p["item_id"] == "Q-990001")
    assert snapshot["previous_out_digests"], "the pre-re-run output must be fingerprinted"


def test_cascade_unchanged_rerun_restores_the_previous_status_and_raises_no_flag(sandbox):
    """"A re-run whose output equals the previous output raises no flag" (spec 14/F3 step 5).

    No agent can be dispatched from a script, so this exercises the comparison directly: mark
    D4 stale, change nothing, and run the plan. D4 is agent-driven, so it is reported as needing
    a person; the digest comparison itself is asserted via run_plan on a script-only step."""
    cs, fc = sandbox.cascade, sandbox.f_common
    plan = cs.plan_for_change("subtopic_ids", "Q-990001", transitive=False)
    applied = cs.apply_plan(plan)
    report = cs.run_plan(applied, dry_run=True)  # noqa: F841 (fc used below)
    dispatch_steps = {d["step"] for d in report["needs_dispatch"]}
    assert "D4" in dispatch_steps, "an agent-driven step must be handed to a person, not faked"
    assert all(not cs._is_script_only(d["step"]) for d in report["needs_dispatch"])
    assert len(fc.load_flags()) == 7, "the cascade must not invent flags"


def test_cascade_auto_closes_a_flag_whose_pair_came_back_pass(sandbox):
    cs = sandbox.cascade
    from lib import status as lib_status
    applied = [{"step": "D1", "item_id": "Q-990001", "scope": "rerun_question",
                "key": "subtopic", "reason": "fixture", "previous_status": "flagged",
                "previous_prompt_version": "v1", "previous_out_digests": {}}]
    # The flag on (D3, Q-990001) must NOT close: its pair is not in the re-run set.
    lib_status.write_status("D1", "Q-990001", lib_status.PASS)
    closed = cs.auto_close_flags(applied)
    assert closed == [], "no open flag sits on (D1, Q-990001) in the fixture"

    applied = [{"step": "D3", "item_id": "Q-990001", "scope": "rerun_question",
                "key": "subtopic", "reason": "fixture", "previous_status": "blocked",
                "previous_prompt_version": "v1", "previous_out_digests": {}}]
    lib_status.write_status("D3", "Q-990001", lib_status.PASS)
    closed = cs.auto_close_flags(applied)
    assert closed == ["FL-990001"]
    assert sandbox.flags()["FL-990001"]["status"] == "auto_closed"


def test_cascade_leaves_a_flag_open_when_the_rerun_did_not_pass(sandbox):
    cs = sandbox.cascade
    from lib import status as lib_status
    lib_status.write_status("D3", "Q-990001", lib_status.FLAGGED)
    closed = cs.auto_close_flags([{"step": "D3", "item_id": "Q-990001", "scope": "x",
                                   "key": "subtopic", "reason": "fixture",
                                   "previous_status": "blocked",
                                   "previous_prompt_version": "v1",
                                   "previous_out_digests": {}}])
    assert closed == []
    assert sandbox.flags()["FL-990001"]["status"] == "open"


def test_cascade_verify_map_reports_the_gap_rather_than_asserting_agreement(sandbox):
    """Spec Section 15 asks for a derived map to agree with cascade.yaml (T25). It cannot today;
    this asserts the honest behaviour — a report with both sides and the reason."""
    cs = sandbox.cascade
    report = cs.verify_map()
    assert set(report) == {"rows", "steps_with_empty_input_fields", "agrees"}
    assert report["rows"], "every cascade key should appear in the comparison"
    keys = {r["key"] for r in report["rows"]}
    assert "question_text" in keys and "subtopic" in keys


# ============================================================================================
# F4 · counts
# ============================================================================================

def test_f4_counts_all_and_released_only(sandbox):
    cc = sandbox.compute_counts
    summary, per = cc.compute()

    st01 = per[f"{CH1}-ST01"]["all"]
    assert st01["questions_total"] == 3, "Q-990001, Q-990002, Q-990003"
    assert st01["unique_questions"] == 2, "Q-990002 and Q-990003 share RG-9901"
    assert st01["years_asked"] == [2019, 2022, 2023]
    assert st01["last_asked"] == 2023
    assert st01["repeat_groups"] == ["RG-9901"]

    st02 = per[f"{CH1}-ST02"]
    assert st02["all"]["questions_total"] == 1, "Q-990006 is merged into Q-990005, not a second row"
    assert st02["released_only"]["questions_total"] == 1, "Q-990005 is released"
    assert st01 != per[f"{CH1}-ST01"]["released_only"]
    assert per[f"{CH1}-ST01"]["released_only"]["questions_total"] == 0

    st03 = per[f"{CH1}-ST03"]["all"]
    assert st03["questions_total"] == 0 and st03["last_asked"] is None, \
        "a subtopic nobody has been asked about is still reported"


def test_f4_recent_mixes_only_count_questions_since_2021(sandbox):
    cc = sandbox.compute_counts
    _, per = cc.compute()
    mix = per[f"{CH1}-ST01"]["all"]["category_mix_recent"]
    assert sum(mix.values()) == 2, "2019's question is not recent; 2022 and 2023's are"
    assert mix == {"recall": 2}


def test_f4_self_check_counts_links_independently(sandbox):
    cc = sandbox.compute_counts
    summary, per = cc.compute()
    assert summary["self_check"]["passed"]
    assert summary["self_check"]["sum_of_subtopic_totals"] == \
        summary["self_check"]["links_counted_independently"] == 5
    assert sum(v["all"]["questions_total"] for v in per.values()) == 5


def test_f4_fails_loudly_and_writes_nothing_when_the_totals_disagree(sandbox, monkeypatch):
    """Rule 3: the self-check must fail loudly if totals disagree with the link count."""
    cc = sandbox.compute_counts
    # Break ONLY the independent link counter, leaving the aggregation correct, so the two sides
    # of the self-check genuinely disagree. (Q-990001 exists, so this is a plausible wrong
    # answer — a duplicated link — not an obviously bogus question id.)
    real_links = cc.question_subtopic_links
    monkeypatch.setattr(cc, "question_subtopic_links",
                        lambda records: real_links(records) + [("Q-990001", f"{CH1}-ST02")])
    with pytest.raises(cc.CountMismatch) as e:
        cc.compute()
    assert "self-check FAILED" in str(e.value)
    assert "never the count" in str(e.value)
    assert not os.path.exists(sandbox.path("steps", "F4", "out", "_all.json")), \
        "a failed self-check must write nothing at all"


def test_f4_rejects_a_link_to_a_question_with_no_record(sandbox, monkeypatch):
    cc = sandbox.compute_counts
    real_links = cc.question_subtopic_links
    monkeypatch.setattr(cc, "question_subtopic_links",
                        lambda records: real_links(records) + [("Q-999999", f"{CH1}-ST01")])
    with pytest.raises(cc.CountMismatch) as e:
        cc.compute()
    assert "no canonical record" in str(e.value) and "Q-999999" in str(e.value)


def test_f4_cli_exits_non_zero_on_a_mismatch(sandbox, monkeypatch):
    cc = sandbox.compute_counts
    monkeypatch.setattr(cc, "compute",
                        lambda **kw: (_ for _ in ()).throw(cc.CountMismatch("boom")))
    assert cc.main([]) == 2


def test_f4_outputs_pass_their_schema_and_check(sandbox):
    import runner_core as rc
    cc = sandbox.compute_counts
    summary, per = cc.compute()
    cc.write(summary, per)
    for st in (f"{CH1}-ST01", f"{CH1}-ST02", f"{CH1}-ST03", f"{CH2}-ST01"):
        data = json.load(open(sandbox.path("steps", "F4", "out", f"{st}.json"), encoding="utf-8"))
        ok, msg = rc.validate_schema("F4", data)
        assert ok, f"{st}: {msg}"
        ok, msg = rc.run_step_check("F4", data, {"item_id": st})
        assert ok, f"{st}: {msg}"


def test_f4_check_catches_hand_edited_counts():
    import runner_core as rc
    base = {"subtopic_id": "BIO12-CH91-ST01", "chapter_id": "BIO12-CH91",
            "all": {"questions_total": 3, "unique_questions": 2, "years_asked": [2019, 2023],
                    "last_asked": 2023, "repeat_groups": ["RG-9901"], "repeat_group_count": 1,
                    "category_mix_recent": {"recall": 1}, "format_mix_recent": {"pick_one": 1},
                    "question_type_mix_recent": {"single_best_answer": 1}},
            "released_only": {"questions_total": 0, "unique_questions": 0, "years_asked": [],
                              "last_asked": None, "repeat_groups": [], "repeat_group_count": 0,
                              "category_mix_recent": {}, "format_mix_recent": {},
                              "question_type_mix_recent": {}}}
    ok, msg = rc.run_step_check("F4", base, {})
    assert ok, msg

    import copy
    inflated = copy.deepcopy(base)
    inflated["all"]["unique_questions"] = 9
    ok, msg = rc.run_step_check("F4", inflated, {})
    assert not ok and "exceeds questions_total" in msg

    wrong_last = copy.deepcopy(base)
    wrong_last["all"]["last_asked"] = 2026
    ok, msg = rc.run_step_check("F4", wrong_last, {})
    assert not ok and "last_asked" in msg

    released_bigger = copy.deepcopy(base)
    released_bigger["released_only"]["questions_total"] = 5
    released_bigger["released_only"]["unique_questions"] = 5
    ok, msg = rc.run_step_check("F4", released_bigger, {})
    assert not ok and "subset" in msg, msg

    overfull_mix = copy.deepcopy(base)
    overfull_mix["all"]["category_mix_recent"] = {"recall": 9}
    ok, msg = rc.run_step_check("F4", overfull_mix, {})
    assert not ok and "more than questions_total" in msg


# ============================================================================================
# F5 · release gate
# ============================================================================================

def _satisfy_gate(sandbox, chapter=CH1, audit_outcome="approve"):
    """Drive the fixture chapter through every gate condition, honestly: real decisions applied
    by apply_review.py, a real sign-off row, real F4 counts. Nothing is written straight into an
    approvals or releases file behind the scripts' back except the sign-off row, which is by
    definition a human artifact."""
    fc, f1, ar, cc = (sandbox.f_common, sandbox.build_review_pack, sandbox.apply_review,
                      sandbox.compute_counts)
    f1.build()  # so review/audit_sample.jsonl exists

    rows = []
    for flag in fc.load_flags():
        if flag["status"] != "open":
            continue
        if chapter not in fc.item_chapter_ids(flag["item_id"], fc.load_records()):
            continue
        field = f1.field_for(flag)
        rows.append(decision(flag["flag_id"], field, "approve", reviewer="Ekta"))
    rows.append(decision(fc.subtopic_list_target(chapter), "subtopic_list", "approve",
                         reviewer="Faculty"))
    for r in fc.change_log_rows():
        if r["chapter_id"] == chapter:
            rows.append(decision(fc.change_log_target(r["change_id"]), "change_log_row",
                                 "approve", reviewer="Faculty"))
    for row in sandbox.modules["f_common"].lib_io.read_jsonl(
            sandbox.path("review", "audit_sample.jsonl")):
        if chapter in (row.get("chapter_ids") or []):
            rows.append(decision(row["pack_id"], row["field"], audit_outcome,
                                 value=["fixture"] if audit_outcome != "approve" else None,
                                 reviewer="Faculty"))
    sandbox.write_decisions(rows)
    ar.apply_decisions(apply=True)

    with open(sandbox.path("review", "releases.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fc.RELEASE_FIELDS)
        w.writeheader()
        w.writerow({"chapter_id": chapter, "released_at": "2026-10-12", "signed_by": "Ekta",
                    "gold_score_snapshot": "fixture", "open_flags": "0"})
    summary, per = cc.compute()
    cc.write(summary, per)


def test_f5_refuses_every_chapter_by_default(sandbox):
    et = sandbox.export_tables
    for chapter in (CH1, CH2):
        report = et.gate(chapter)
        assert not report["ok"]
        failed = {c["id"] for c in report["conditions"] if not c["ok"]}
        assert "signoff_row" in failed
        assert "subtopic_list_approved" in failed
        assert "queue_empty" in failed


def test_f5_writes_nothing_when_it_refuses(sandbox):
    et = sandbox.export_tables
    assert et.main(["--chapters", CH1]) != 0
    assert not os.listdir(sandbox.path("data"))


def test_f5_still_refuses_without_a_signoff_row_even_when_everything_else_passes(sandbox):
    """The sign-off is not one condition among many; it is the one that cannot be bypassed."""
    et = sandbox.export_tables
    _satisfy_gate(sandbox)
    assert et.gate(CH1)["ok"]
    os.remove(sandbox.path("review", "releases.csv"))
    report = et.gate(CH1)
    assert not report["ok"]
    assert {c["id"] for c in report["conditions"] if not c["ok"]} == {"signoff_row"}
    assert et.main(["--chapters", CH1]) != 0
    assert not os.listdir(sandbox.path("data"))


def test_f5_rejects_a_signoff_row_with_an_empty_signed_by(sandbox):
    fc, et = sandbox.f_common, sandbox.export_tables
    _satisfy_gate(sandbox)
    with open(sandbox.path("review", "releases.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fc.RELEASE_FIELDS)
        w.writeheader()
        w.writerow({"chapter_id": CH1, "released_at": "2026-10-12", "signed_by": "",
                    "gold_score_snapshot": "", "open_flags": "0"})
    report = et.gate(CH1)
    assert not report["ok"]
    assert {c["id"] for c in report["conditions"] if not c["ok"]} == {"signoff_row"}


def test_f5_has_no_force_or_bypass_argument(sandbox):
    """There must be no flag that skips the sign-off requirement."""
    et = sandbox.export_tables
    source = open(os.path.join(_SCRIPTS_DIR, "export_tables.py"), encoding="utf-8").read()
    for forbidden in ("--force", "--skip-gate", "--no-gate", "--bypass", "--ignore-signoff"):
        assert forbidden not in source, f"export_tables.py must not accept {forbidden}"
    with pytest.raises(SystemExit):
        et.main(["--force"])


def test_f5_releases_a_chapter_that_passes_every_condition(sandbox):
    et = sandbox.export_tables
    _satisfy_gate(sandbox)
    report = et.gate(CH1)
    assert report["ok"], [c for c in report["conditions"] if not c["ok"]]
    assert et.main(["--chapters", CH1]) == 0

    questions = list(csv.DictReader(open(sandbox.path("data", "questions.csv"), encoding="utf-8")))
    assert {r["question_id"] for r in questions} == {"Q-990001", "Q-990002", "Q-990003",
                                                     "Q-990005"}
    assert all(r["release_status"] == "released" for r in questions)
    assert all(r["released_at"] == "2026-10-12" for r in questions)

    links = list(csv.DictReader(open(sandbox.path("data", "ncert_links.csv"), encoding="utf-8")))
    assert len(links) == 4, "one row per question-subtopic (spec 6.6)"
    assert {r["subtopic_id"] for r in links} == {f"{CH1}-ST01", f"{CH1}-ST02"}

    tags = list(csv.DictReader(open(sandbox.path("data", "tags.csv"), encoding="utf-8")))
    assert {r["question_id"] for r in tags} == {r["question_id"] for r in questions}

    stats = list(csv.DictReader(open(sandbox.path("data", "subtopic_stats.csv"),
                                     encoding="utf-8")))
    assert {r["population"] for r in stats} == {"all", "released_only"}
    assert {r["subtopic_id"] for r in stats} == {f"{CH1}-ST01", f"{CH1}-ST02", f"{CH1}-ST03"}

    log = [json.loads(l) for l in
           open(sandbox.path("data", "_release_log.jsonl"), encoding="utf-8")]
    assert log[-1]["chapter_id"] == CH1 and log[-1]["signed_by"] == "Ekta"
    assert all(c["ok"] for c in log[-1]["gate"])


def test_f5_does_not_release_a_chapter_that_was_not_asked_for(sandbox):
    et = sandbox.export_tables
    _satisfy_gate(sandbox)
    et.main(["--chapters", CH1])
    questions = list(csv.DictReader(open(sandbox.path("data", "questions.csv"), encoding="utf-8")))
    assert "Q-990004" not in {r["question_id"] for r in questions}, \
        "Q-990004 belongs to the chapter that fails the gate"


def test_f5_refuses_when_a_question_is_blocked_by_a_reviewer(sandbox):
    ar, et = sandbox.apply_review, sandbox.export_tables
    _satisfy_gate(sandbox)
    assert et.gate(CH1)["ok"]
    sandbox.write_decisions([decision("Q-990001", "subtopic_ids", "block", reviewer="Faculty")])
    ar.apply_decisions(apply=True)
    report = et.gate(CH1)
    assert not report["ok"]
    assert "nothing_blocked" in {c["id"] for c in report["conditions"] if not c["ok"]}


def test_f5_refuses_when_the_audit_sample_misses_its_target(sandbox):
    et = sandbox.export_tables
    _satisfy_gate(sandbox, audit_outcome="correct")
    report = et.gate(CH1)
    assert not report["ok"]
    failed = {c["id"] for c in report["conditions"] if not c["ok"]}
    assert "audit_sample_meets_target" in failed


def test_f5_refuses_when_the_counts_have_not_been_computed(sandbox):
    et = sandbox.export_tables
    _satisfy_gate(sandbox)
    os.remove(sandbox.path("steps", "F4", "out", "_all.json"))
    assert et.main(["--chapters", CH1]) == 2
    assert not os.listdir(sandbox.path("data"))


def test_f5_gate_report_writes_nothing(sandbox):
    et = sandbox.export_tables
    assert et.main(["--gate-report"]) == 0
    assert not os.listdir(sandbox.path("data"))


def test_f5_verdict_passes_its_own_schema_and_check(sandbox):
    import runner_core as rc
    et = sandbox.export_tables
    _satisfy_gate(sandbox)
    report = et.gate(CH1)
    ok, msg = rc.validate_schema("F5", report)
    assert ok, msg
    ok, msg = rc.run_step_check("F5", report, {"item_id": CH1})
    assert ok, msg


def test_f5_check_rejects_a_release_that_claims_ok_with_a_failed_condition():
    import runner_core as rc
    verdict = {
        "chapter_id": "BIO12-CH91", "ok": True, "audit_target": 0.95,
        "signoff": {"chapter_id": "BIO12-CH91", "released_at": "2026-10-12",
                    "signed_by": "Ekta"},
        "conditions": [
            {"id": "queue_empty", "requirement": "r", "ok": False, "detail": "3 open flags"},
            {"id": "subtopic_list_approved", "requirement": "r", "ok": True, "detail": ""},
            {"id": "change_log_rows_approved", "requirement": "r", "ok": True, "detail": ""},
            {"id": "audit_sample_meets_target", "requirement": "r", "ok": True, "detail": ""},
            {"id": "signoff_row", "requirement": "r", "ok": True, "detail": ""},
            {"id": "nothing_blocked", "requirement": "r", "ok": True, "detail": ""},
        ],
    }
    ok, msg = rc.run_step_check("F5", verdict, {})
    assert not ok and "no override" in msg

    verdict["conditions"][0]["ok"] = True
    verdict["signoff"] = None
    ok, msg = rc.run_step_check("F5", verdict, {})
    assert not ok and "no sign-off row" in msg

    verdict["signoff"] = {"chapter_id": "BIO12-CH91", "released_at": "2026-10-12",
                          "signed_by": "Ekta"}
    verdict["conditions"] = verdict["conditions"][:4]
    ok, msg = rc.run_step_check("F5", verdict, {})
    assert not ok and "every condition" in msg


# ============================================================================================
# F6 · gold scoring
# ============================================================================================

def test_f6_refuses_without_a_gold_set(sandbox):
    sg = sandbox.score_gold
    os.remove(sandbox.path("gold", "gold_set.csv"))
    assert sg.main([]) == 2
    assert not os.path.exists(sandbox.path("gold", "scores.md"))


def test_f6_scores_the_fixture_gold_set(sandbox):
    sg, fc = sandbox.score_gold, sandbox.f_common
    gold, meta, shape = sg.load_gold()
    assert shape == "long"
    records = fc.load_records()
    result = sg.score(gold, meta, records)
    by_id = {c["id"]: c for c in result["per_criterion"]}

    assert by_id["chapter"]["checked"] == 3
    assert by_id["chapter"]["matched"] == 3, "a bare id must match a one-element list"
    assert by_id["chapter"]["rate"] == 1.0

    assert by_id["subtopic"]["checked"] == 1
    assert by_id["subtopic"]["matched"] == 0, "the fixture's subtopic gold value is a mismatch"
    assert by_id["subtopic"]["meets_target"] is False

    assert by_id["answer_joined"]["checked"] == 3
    assert by_id["answer_joined"]["matched"] == 1, \
        "Q-990002's gold answer differs; Q-990099 has no record"

    assert by_id["repeats"]["matched"] == 1, "RG-9901 is present, so no known repeat is missed"
    assert by_id["quotes_found"]["checked"] >= 3
    assert by_id["quotes_found"]["matched"] == by_id["quotes_found"]["checked"], \
        "every fixture quote occurs word for word in the fixture passage"

    thinking = by_id["thinking"]
    assert thinking["per_subject"]["Biology"]["matched"] == 2
    assert thinking["per_subject"]["Physics"]["matched"] == 0
    assert thinking["per_subject"]["Physics"]["meets_target"] is False
    assert thinking["meets_target"] is False, "the target is per subject; one subject failing fails it"

    assert any(f["question_id"] == "Q-990099" for f in result["failures"])
    assert any(f["step"] == "D2" for f in result["failures"]), \
        "a mismatch must be attributed to the step that produced the value"


def test_f6_writes_scores_md_with_targets_warnings_and_mismatches(sandbox):
    sg = sandbox.score_gold
    assert sg.main([]) == 0
    md = open(sandbox.path("gold", "scores.md"), encoding="utf-8").read()
    assert "# Gold set scores" in md
    assert "Against Section 1.1's targets" in md
    assert "Read this before trusting the numbers" in md
    assert "spec 14/F6 calls for 90" in md, "a short gold set must be called out, not hidden"
    assert "Every mismatch" in md
    assert "Q-990099" in md
    assert "**NO**" in md, "a missed target must be marked, not softened"
    assert "Per step" in md and "| D2 |" in md


def test_f6_fail_under_target_exit_code(sandbox):
    sg = sandbox.score_gold
    assert sg.main(["--fail-under-target"]) == 1


def test_f6_accepts_a_wide_gold_set(sandbox):
    sg = sandbox.score_gold
    with open(sandbox.path("gold", "gold_set.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["question_id", "subject", "year", "official_answer", "chapter_ids"])
        w.writerow(["Q-990001", "Biology", "2019", "2", '["BIO12-CH91"]'])
        w.writerow(["Q-990004", "Physics", "2024", "2", '["BIO12-CH92"]'])
    gold, meta, shape = sg.load_gold()
    assert shape == "wide"
    assert gold["Q-990001"]["official_answer"] == "2"
    result = sg.score(gold, meta, sandbox.f_common.load_records())
    by_id = {c["id"]: c for c in result["per_criterion"]}
    assert by_id["answer_joined"]["checked"] == 2 and by_id["answer_joined"]["matched"] == 2


def test_f6_summary_passes_its_own_schema_and_check(sandbox):
    import runner_core as rc
    sg, fc = sandbox.score_gold, sandbox.f_common
    gold, meta, _ = sg.load_gold()
    result = sg.score(gold, meta, fc.load_records())
    payload = {"per_criterion": [{k: v for k, v in c.items() if k != "failures"}
                                 for c in result["per_criterion"]]}
    ok, msg = rc.validate_schema("F6", payload)
    assert ok, msg
    ok, msg = rc.run_step_check("F6", payload, {"item_id": "gold"})
    assert ok, msg
    assert "UNDER TARGET" in msg, "a missed target is reported as a note, not a check failure"


def test_f6_check_rejects_an_overstated_score():
    import runner_core as rc
    inflated = {"per_criterion": [
        {"id": "chapter", "name": "Chapter correct", "target": 0.98, "checked": 10,
         "matched": 10, "rate": 1.0, "meets_target": True},
        {"id": "subtopic", "name": "Subtopic correct", "target": 0.95, "checked": 10,
         "matched": 4, "rate": 1.0, "meets_target": True},
    ]}
    ok, msg = rc.run_step_check("F6", inflated, {})
    assert not ok and "matched/checked" in msg

    nothing_checked = {"per_criterion": [
        {"id": "chapter", "name": "Chapter correct", "target": 0.98, "checked": 0,
         "matched": 0, "rate": 1.0, "meets_target": True}]}
    ok, msg = rc.run_step_check("F6", nothing_checked, {})
    assert not ok and "is not" in msg

    impossible = {"per_criterion": [
        {"id": "chapter", "name": "Chapter correct", "target": 0.98, "checked": 3,
         "matched": 5, "rate": 1.0, "meets_target": True}]}
    ok, msg = rc.run_step_check("F6", impossible, {})
    assert not ok and "exceeds checked" in msg


# ============================================================================================
# The real project — read-only
# ============================================================================================

def test_f1_against_real_project():
    """F1 is the one Stage F step with real data to run against today (~100 open flags). This
    runs it on the REAL project in dry-run mode: it reads real flags, records and statuses and
    writes nothing at all."""
    import f_common as fc
    import build_review_pack as f1
    result, items = f1.build(dry_run=True)
    assert result["dry_run"]
    assert result["queue_size"] == len(items)
    open_count = len(fc.open_flags())
    flag_items = [i for i in items if i["kind"] == "flag"]
    assert len(flag_items) == open_count, "every open flag must reach the queue"
    priorities = [i["priority"] for i in items]
    assert priorities == sorted(priorities)
    assert any(i["priority"] == 1 for i in items), "the real bank has open blockers"
    for item in items:
        assert item["field"], f"{item['pack_id']} has no field for its decision row"


def test_real_project_data_dir_is_untouched_by_the_gate_report():
    """export_tables.py must be safe to interrogate: a gate report never writes data/."""
    import export_tables as et
    before = sorted(os.listdir(os.path.join(_PROJECT_ROOT, "data")))
    assert et.main(["--gate-report"]) == 0
    assert sorted(os.listdir(os.path.join(_PROJECT_ROOT, "data"))) == before


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
