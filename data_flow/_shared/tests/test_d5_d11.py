#!/usr/bin/env python3
"""Tests for Stage D's D5-D11 (spec Section 12/D5-D11).

READ THIS FIRST, BECAUSE IT IS THE POINT OF THE FILE:

D5-D11 all sit downstream of D4, and **D4 has never run for real in this project**. Every real
question is blocked earlier in Stage D (`Q-000015` at D3 with `D3_NO_PASSAGES`; `Q-000001`-
`Q-000005` at D1 with `D1_NO_CHAPTERS`), `ncert/change_log.csv` and `ncert/deleted_topics.csv`
are header-only, no older-edition or lab-manual book is indexed, and the bank's 10 questions all
come from ONE sitting of ONE year -- so D9 can never find an other-year candidate and no repeat
group exists to confirm. There is therefore **no real D5-D11 output to test against**, and none
was manufactured to pretend otherwise.

So this file does the two honest things available:

  1. Where REAL data exists, it uses it. Every latest-edition quote verified below is real NCERT
     text, read READ-ONLY out of the project's own `ncert/passages/BIO12L.jsonl` (the two real
     passages Stage A actually indexed from Biology Class 12 Chapter 1) and copied into an
     isolated fixture root. A paraphrase of real NCERT prose really is rejected by
     `quote_verify.find`; that is tested, not assumed.

  2. Where real data does NOT exist (older edition, lab manual, change log, deleted topics,
     multi-year questions, repeat groups), it builds CLEARLY-LABELLED FIXTURES -- every fixture
     id below carries an obvious marker (`BIO12O-CH01-P0x` for a fabricated older passage,
     `CL-FIXTURE-0001` for a fabricated change-log row, `Q-FIX0001` for a fabricated question) so
     no fixture value can ever be mistaken for real pipeline data.

ISOLATION IS NOT OPTIONAL HERE. Every test below runs in a temp project root with
`lib_io.PROJECT_ROOT`, `lib_flags.FLAGS_PATH` and `lib_ids.COUNTERS_PATH` all redirected, exactly
as tests/test_run_step.py does and for exactly the reason docs/OPEN_QUESTIONS.md records on
2026-10-10: an earlier fixture pass in this project wrote test data straight into the real
`ncert/`, `steps/`, `flags/flags.jsonl` and `run_log.csv`, and cost a real cleanup. Nothing in
this file writes anywhere but its own temp directory.

Run: .venv/bin/python3 tests/test_d5_d11.py   (or via pytest)
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

import build_groups  # noqa: E402
import runner_core as rc  # noqa: E402
import step_plugins as sp  # noqa: E402
from lib import flags as lib_flags  # noqa: E402
from lib import ids as lib_ids  # noqa: E402
from lib import io as lib_io  # noqa: E402

_REAL_PASSAGES = os.path.join(_PROJECT_ROOT, "ncert", "passages", "BIO12L.jsonl")

# Two REAL passage ids from the real indexed Biology Class 12 Chapter 1 (read-only).
REAL_LATEST_A = "BIO12L-CH01-P117"   # "...is termed pollination."
REAL_LATEST_B = "BIO12L-CH01-P111"   # "...a mass of cells called the nucellus."

# Fixture ids. Every one of these is fabricated and marked as such.
FIX_OLDER_A = "BIO12O-CH01-P01"
FIX_OLDER_DELETED = "BIO12O-CH01-P02"
FIX_LAB = "PHY11M-CH01-P01"
FIX_CHANGE_ID = "CL-FIXTURE-0001"


# ---------------------------------------------------------------------------
# Isolation helpers (same pattern and same reasons as tests/test_run_step.py)
# ---------------------------------------------------------------------------

def _real_passage(passage_id):
    """One real NCERT passage row, read READ-ONLY from the live project. Fails loudly rather than
    silently substituting invented prose, because the whole value of using it is that it is real."""
    if not os.path.exists(_REAL_PASSAGES):
        raise SystemExit(f"{_REAL_PASSAGES} is missing; this test reads (never writes) the real "
                           f"Stage A passage index.")
    for row in lib_io.read_jsonl(_REAL_PASSAGES):
        if row.get("passage_id") == passage_id:
            return row
    raise SystemExit(f"real passage {passage_id} not found in {_REAL_PASSAGES}")


def _build_isolated_root():
    tmp = tempfile.mkdtemp(prefix="d5_d11_fixture_")
    copy = ["config/steps.yaml", "config/allowed_values.yaml", "scripts/checks/__init__.py"]
    copy += [f"schemas/D{i}.json" for i in range(1, 12)]
    copy += [f"scripts/checks/D{i}.py" for i in range(1, 12)]
    copy += ["codebook/D11.md"]
    for rel in copy:
        src, dst = os.path.join(_PROJECT_ROOT, rel), os.path.join(tmp, rel)
        if not os.path.exists(src):
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(src, dst)
    for sub in ("ncert/passages", "papers/records", "steps", "flags"):
        os.makedirs(os.path.join(tmp, sub), exist_ok=True)
    # Header-only tables, matching the REAL current state of the project exactly: no fabricated
    # change-log or deleted-topics row exists on disk unless a test explicitly writes one.
    lib_io.write_csv(os.path.join(tmp, "ncert", "change_log.csv"), [], [
        "change_id", "chapter_id", "subtopic_id", "old_passage_id", "new_passage_id",
        "change_type", "old_fact", "new_fact", "could_flip_an_answer", "old_text", "new_text",
        "affected_questions", "approval"])
    lib_io.write_csv(os.path.join(tmp, "ncert", "deleted_topics.csv"), [], [
        "old_passage_id", "chapter_id", "old_pages", "heading", "subtopic_hint"])
    return tmp


@contextlib.contextmanager
def _isolated_project(tmp):
    """Redirect every path the real project would otherwise be written to.

    Note the SECOND set of patches below. scripts/build_groups.py does `from scripts.lib import
    io as lib_io` while this file (and step_plugins.py) do `from lib import io` -- two import
    paths to the same file, which Python loads as two SEPARATE module objects. Patching only this
    file's `lib_io.PROJECT_ROOT` leaves build_groups still reading and writing the REAL project,
    which is exactly the accident docs/OPEN_QUESTIONS.md records on 2026-10-10. In production the
    duplication is harmless (both resolve to the same real root, and `--auto` runs build_groups
    as a subprocess anyway), but under test it has to be patched explicitly on both.
    """
    orig = (lib_io.PROJECT_ROOT, lib_flags.FLAGS_PATH, lib_ids.COUNTERS_PATH)
    bg_orig = (build_groups.lib_io.PROJECT_ROOT, build_groups.lib_ids.COUNTERS_PATH)
    lib_io.PROJECT_ROOT = tmp
    lib_flags.FLAGS_PATH = os.path.join(tmp, "flags", "flags.jsonl")
    lib_ids.COUNTERS_PATH = os.path.join(tmp, "register", "counters.json")
    build_groups.lib_io.PROJECT_ROOT = tmp
    build_groups.lib_ids.COUNTERS_PATH = os.path.join(tmp, "register", "counters.json")
    rc.load_steps_config(force_reload=True)
    rc._SCHEMA_CACHE.clear()
    rc._CHECK_MODULE_CACHE.clear()
    try:
        yield
    finally:
        lib_io.PROJECT_ROOT, lib_flags.FLAGS_PATH, lib_ids.COUNTERS_PATH = orig
        build_groups.lib_io.PROJECT_ROOT, build_groups.lib_ids.COUNTERS_PATH = bg_orig
        rc.load_steps_config(force_reload=True)
        rc._SCHEMA_CACHE.clear()
        rc._CHECK_MODULE_CACHE.clear()


def _write_passages(tmp, book_id, rows):
    path = os.path.join(tmp, "ncert", "passages", f"{book_id}.jsonl")
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")


def _seed_latest_and_older(tmp):
    """Real latest passages (read-only copies) + clearly-labelled fixture older/lab-manual ones."""
    pa, pb = _real_passage(REAL_LATEST_A), _real_passage(REAL_LATEST_B)
    _write_passages(tmp, "BIO12L", [pa, pb])
    _write_passages(tmp, "BIO12O", [
        {"passage_id": FIX_OLDER_A, "chapter_id": "BIO12-CH01", "kind": "paragraph",
         "text": "FIXTURE older-edition text, not real NCERT. Pollen transfer from anther to "
                 "stigma is called pollination."},
        {"passage_id": FIX_OLDER_DELETED, "chapter_id": "BIO12-CH01", "kind": "paragraph",
         "text": "FIXTURE older-edition text for a deleted topic, not real NCERT. The nucellus "
                 "stores reserve food."},
    ])
    _write_passages(tmp, "PHY11M", [
        {"passage_id": FIX_LAB, "chapter_id": "PHY11-CH01", "kind": "paragraph",
         "text": "FIXTURE lab-manual text, not real NCERT. Balance the metre bridge by moving "
                 "the jockey until the galvanometer reads zero."},
    ])
    return pa, pb


def _d3_out(tmp, qid, latest=(), older=(), lab=()):
    lib_io.atomic_write_json(os.path.join(tmp, "steps", "D3", "out", f"{qid}.json"),
                               {"latest": list(latest), "older": list(older),
                                "lab_manual": list(lab)})


def _status(tmp, step, item_id, status="pass", prompt_version="v1", **extra):
    payload = {"item_id": item_id, "step": step, "status": status,
               "prompt_version": prompt_version}
    payload.update(extra)
    lib_io.atomic_write_json(os.path.join(tmp, "steps", step, "status", f"{item_id}.json"), payload)


def _record(tmp, qid, **fields):
    data = {"question_id": qid, "field_sources": {}}
    data.update(fields)
    lib_io.atomic_write_json(os.path.join(tmp, "papers", "records", f"{qid}.json"), data)
    return data


# ===========================================================================
# 1. Every check module loads and returns (bool, str) for a pass and a fail fixture.
# ===========================================================================

def test_check_modules_pass_and_fail_fixtures():
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        pa, _pb = _seed_latest_and_older(tmp)
        real_line = "Transfer of pollen grains (shed from the anther) to the stigma of a pistil is termed pollination."
        older_line = "Pollen transfer from anther to stigma is called pollination."

        fixtures = {}

        # --- D5: real latest text in the `latest_passage_ids` guard, fixture older text quoted.
        d5_ctx = {"item_id": "Q-FIX0001", "step": "D5", "input_data": {
            "older_passages": {FIX_OLDER_A: "FIXTURE older-edition text, not real NCERT. "
                                             + older_line},
            "latest_passage_ids": [REAL_LATEST_A],
        }}
        fixtures["D5"] = (
            {"older": [{"for": "answer", "passage_id": FIX_OLDER_A, "exact_line": older_line}],
             "none_for": [], "note": ""}, d5_ctx,
            # FAIL: a paraphrase of the fixture older line -- not found word for word.
            {"older": [{"for": "answer", "passage_id": FIX_OLDER_A,
                         "exact_line": "Pollen moves from anther to stigma, which is pollination."}],
             "none_for": [], "note": ""}, d5_ctx,
        )

        # --- D6: quoted line is REAL NCERT text, verified against the real passage.
        d6_ctx = {"item_id": "Q-FIX0001", "step": "D6", "input_data": {
            "syllabus_status": "latest_ncert", "allowed_note_types": ["same_both"],
            "editions": {"L": {REAL_LATEST_A: pa["text"]}},
        }}
        fixtures["D6"] = (
            {"syllabus_status": "latest_ncert", "note_type": "same_both",
             "reason_note": f'Answer from the latest NCERT: "{real_line}".',
             "quoted_lines": [{"edition": "L", "passage_id": REAL_LATEST_A, "text": real_line}]},
            d6_ctx,
            # FAIL: the agent changed the status the SCRIPT decided.
            {"syllabus_status": "outside_ncert", "note_type": "same_both",
             "reason_note": f'Answer from the latest NCERT: "{real_line}".',
             "quoted_lines": [{"edition": "L", "passage_id": REAL_LATEST_A, "text": real_line}]},
            d6_ctx,
        )

        # --- D7
        d7_ctx = {"item_id": "Q-FIX0001", "step": "D7", "input_data": {
            "latest_passages": {REAL_LATEST_A: pa["text"]},
            "change_log_entries": {FIX_CHANGE_ID: {"change_id": FIX_CHANGE_ID,
                                                     "old_passage_id": FIX_OLDER_A,
                                                     "new_passage_id": REAL_LATEST_A}},
            "evidence_passage_ids": [REAL_LATEST_A, FIX_OLDER_A],
            "official_answer": "2",
        }}
        fixtures["D7"] = (
            {"latest_answer": "3", "same_as_official": False, "quote": real_line,
             "change_id": FIX_CHANGE_ID,
             "sentence_for_note": "By the older NCERT the answer was (2); by the latest NCERT it is (3).",
             "note": ""}, d7_ctx,
            # FAIL: same_as_official contradicts latest_answer vs the official answer.
            {"latest_answer": "3", "same_as_official": True, "quote": real_line,
             "change_id": FIX_CHANGE_ID, "sentence_for_note": "", "note": ""}, d7_ctx,
        )

        # --- D8
        d8_ctx = {"item_id": "Q-FIX0001", "step": "D8",
                   "input_data": {"structure": "statements", "d4_has_derivation": False}}
        fixtures["D8"] = (
            {"fact_line": "A is true. | B is true.", "facts": ["A is true.", "B is true."],
             "confidence": "high"}, d8_ctx,
            # FAIL: fact_line is not the ' | '-join of facts -> D9 would match the wrong facts.
            {"fact_line": "A is true.", "facts": ["A is true.", "B is true."],
             "confidence": "high"}, d8_ctx,
        )

        # --- D9
        d9_ctx = {"item_id": "Q-FIX0001", "step": "D9", "input_data": {
            "this_id": "Q-FIX0001", "this_year": 2023, "this_subtopics": ["BIO12-CH01-ST01"],
            "others": {"Q-FIX0002": {"year": 2019, "sitting": "MAIN",
                                       "subtopics": ["BIO12-CH01-ST01"]}},
        }}
        fixtures["D9"] = (
            {"possible_repeats": ["Q-FIX0002"], "none": False}, d9_ctx,
            # FAIL: an id that was never in the candidate table.
            {"possible_repeats": ["Q-FIX9999"], "none": False}, d9_ctx,
        )

        # --- D10
        d10_ctx = {"item_id": "BIO12-CH01-ST01", "step": "D10"}
        fixtures["D10"] = (
            {"subtopic_id": "BIO12-CH01-ST01",
             "groups": [{"group_id": "RG-0001", "members": ["Q-FIX0001", "Q-FIX0002"]}],
             "singletons": ["Q-FIX0003"],
             "links_used": [["Q-FIX0001", "Q-FIX0002"]]}, d10_ctx,
            # FAIL: a link crossing two groups -- the classic un-merged-component bug.
            {"subtopic_id": "BIO12-CH01-ST01",
             "groups": [{"group_id": "RG-0001", "members": ["Q-FIX0001", "Q-FIX0002"]},
                         {"group_id": "RG-0002", "members": ["Q-FIX0003", "Q-FIX0004"]}],
             "singletons": [],
             "links_used": [["Q-FIX0001", "Q-FIX0002"], ["Q-FIX0003", "Q-FIX0004"],
                             ["Q-FIX0002", "Q-FIX0003"]]}, d10_ctx,
        )

        # --- D11
        d11_ctx = {"item_id": "RG-0001", "step": "D11", "input_data": {"members": {
            "Q-FIX0001": {"year": 2019, "sitting": "MAIN"},
            "Q-FIX0002": {"year": 2023, "sitting": "MAIN"},
            "Q-FIX0003": {"year": 2025, "sitting": "MAIN"},
        }}}
        fixtures["D11"] = (
            {"groups": [{"fact_line": "F.", "first": "Q-FIX0001",
                          "members": [{"id": "Q-FIX0001", "label": "first"},
                                       {"id": "Q-FIX0002", "label": "reworded"}]}],
             "related": [{"id": "Q-FIX0003", "related_to": "Q-FIX0001"}], "removed": []},
            d11_ctx,
            # FAIL: `first` is not the earliest member (2023 named instead of 2019).
            {"groups": [{"fact_line": "F.", "first": "Q-FIX0002",
                          "members": [{"id": "Q-FIX0002", "label": "first"},
                                       {"id": "Q-FIX0001", "label": "reworded"}]}],
             "related": [{"id": "Q-FIX0003", "related_to": "Q-FIX0002"}], "removed": []},
            d11_ctx,
        )

        for step in ("D5", "D6", "D7", "D8", "D9", "D10", "D11"):
            module = rc.load_check_module(step)
            assert hasattr(module, "check"), f"{step}: no check()"
            data_pass, ctx_pass, data_fail, ctx_fail = fixtures[step]

            # The pass fixture must ALSO be schema-valid -- a check fixture that the schema would
            # have rejected proves nothing about the real pipeline.
            ok_schema, schema_msg = rc.validate_schema(step, data_pass)
            assert ok_schema, f"{step}: pass fixture is not schema-valid: {schema_msg}"

            ok, msg = module.check(data_pass, ctx_pass)
            assert isinstance(ok, bool) and isinstance(msg, str)
            assert ok is True, f"{step}: expected the pass fixture to pass, got {msg!r}"
            ok2, msg2 = module.check(data_fail, ctx_fail)
            assert ok2 is False, f"{step}: expected the fail fixture to fail, got {msg2!r}"
            assert isinstance(msg2, str) and msg2
            print(f"  {step}: pass-fixture ok; fail-fixture rejected -> {msg2[:110]}")
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_check_modules_pass_and_fail_fixtures: OK")


# ===========================================================================
# 2. D5 verifies against the OLDER edition, drops what it cannot find, and refuses a latest quote.
# ===========================================================================

def test_d5_quote_verification_and_latest_edition_refusal():
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        pa, _pb = _seed_latest_and_older(tmp)
        real_line = "Transfer of pollen grains (shed from the anther) to the stigma of a pistil is termed pollination."
        qid = "Q-FIX0001"
        _record(tmp, qid, official_answer="2", status="normal", year=2023, sitting="MAIN",
                 subject="Biology", stem_en="Fixture question.",
                 options_en={"1": "a", "2": "b", "3": "c", "4": "d"},
                 structure="plain", d1_chapter_ids=["BIO12-CH01"],
                 d2_subtopic_ids=["BIO12-CH01-ST01"], d4_link_type="states_answer",
                 d4_evidence=[{"for": "answer", "passage_id": REAL_LATEST_A,
                                "exact_line": real_line}],
                 d4_supports_answer="fully", d4_derivation_steps=[])
        _d3_out(tmp, qid,
                 latest=[{"passage_id": REAL_LATEST_A, "text": pa["text"]}],
                 older=[{"passage_id": FIX_OLDER_A,
                          "text": "FIXTURE older-edition text, not real NCERT. Pollen transfer "
                                   "from anther to stigma is called pollination."}])
        _status(tmp, "D3", qid, "pass")
        _status(tmp, "D4", qid, "pass")

        plugin = sp.D5Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        lines = plugin.list_items(filters)
        assert len(lines) == 1 and lines[0].agent == "d5-older-line-finder", lines

        # The dispatched work input must be the AGENT's shape, not the check context.
        with open(rc.pp("steps", "D5", "work", f"{qid}.runA.input.json")) as f:
            agent_input = json.load(f)
        assert set(agent_input) == {"question", "answer_to_support", "latest_evidence",
                                     "older_passages"}, sorted(agent_input)
        assert agent_input["older_passages"][0]["id"] == FIX_OLDER_A

        # Agent output: one quote that IS in the older passage, one that is a paraphrase of it,
        # and one that quotes the LATEST edition (the agent file's own Never rule).
        lib_io.atomic_write_json(rc.pp("steps", "D5", "out", f"{qid}.runA.json"), {
            "older": [
                {"for": "answer", "passage_id": FIX_OLDER_A,
                 "exact_line": "Pollen transfer from anther to stigma is called pollination."},
                {"for": "rule", "passage_id": FIX_OLDER_A,
                 "exact_line": "Pollen moves from the anther to the stigma."},   # paraphrase
                {"for": "extra", "passage_id": REAL_LATEST_A, "exact_line": real_line},  # latest!
            ], "none_for": [], "note": ""})

        retry_lines = plugin.check(filters)
        assert len(retry_lines) == 1 and retry_lines[0].run_label == "retry1", retry_lines
        with open(rc.pp("steps", "D5", "work", f"{qid}.retry1.input.json")) as f:
            retry_input = json.load(f)
        # The retry must get the AGENT's input shape plus the failure note (the bug the
        # `agent_inputs` parameter of resolve_single_run_items fixes).
        assert "question" in retry_input and "older_passages" in retry_input, sorted(retry_input)
        assert "D5_LATEST_EDITION_QUOTE" in retry_input["previous_attempt_failed"]
        assert "D5_QUOTE_NOT_FOUND" in retry_input["previous_attempt_failed"]

        # The retry repeats the same mistakes -> the two bad quotes are DROPPED, the good one kept.
        lib_io.atomic_write_json(rc.pp("steps", "D5", "out", f"{qid}.retry1.json"),
                                   _read(rc.pp("steps", "D5", "out", f"{qid}.runA.json")))
        assert plugin.check(filters) == []
        record = _read(rc.pp("papers", "records", f"{qid}.json"))
        kept = record["d5_older"]
        assert len(kept) == 1 and kept[0]["passage_id"] == FIX_OLDER_A, kept
        assert any("not found" in s for s in record["d5_none_for"]), record["d5_none_for"]
        codes = {f["code"] for f in lib_io.read_jsonl(rc.pp("flags", "flags.jsonl"))}
        assert "D5_QUOTE_NOT_FOUND" in codes, codes
        assert rc.read_item_status("D5", qid)["status"] == "flagged"
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d5_quote_verification_and_latest_edition_refusal: OK")


def test_d5_skips_when_no_older_passages_exist():
    """The REAL state of every question in the bank today: D3's `older` list is empty because no
    older-edition book is indexed. D5 must resolve `skipped` with no agent call and flag the gap."""
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        pa, _ = _seed_latest_and_older(tmp)
        qid = "Q-FIX0010"
        _record(tmp, qid, official_answer="2", status="normal", year=2023, sitting="MAIN",
                 subject="Biology", stem_en="Fixture question.", options_en={"2": "b"},
                 d4_evidence=[{"for": "answer", "passage_id": REAL_LATEST_A, "exact_line": "x"}])
        _d3_out(tmp, qid, latest=[{"passage_id": REAL_LATEST_A, "text": pa["text"]}], older=[])
        _status(tmp, "D3", qid, "pass")
        _status(tmp, "D4", qid, "pass")

        plugin = sp.D5Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        assert plugin.list_items(filters) == [], "a question with no older passages must not be dispatched"
        assert plugin.check(filters) == []
        assert rc.read_item_status("D5", qid)["status"] == "skipped"
        codes = {f["code"] for f in lib_io.read_jsonl(rc.pp("flags", "flags.jsonl"))}
        assert codes == {"D5_NO_OLDER_PASSAGES"}, codes
        assert _read(rc.pp("papers", "records", f"{qid}.json"))["d5_older"] == []
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d5_skips_when_no_older_passages_exist: OK")


# ===========================================================================
# 3. D6: the rule ladder's ORDER is the rule. All six rungs, and first-match-wins between them.
# ===========================================================================

def test_d6_rule_ladder_order_is_first_match_wins():
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        _seed_latest_and_older(tmp)
        rule_quote = {"for": "rule", "passage_id": REAL_LATEST_A, "exact_line": "x"}
        answer_quote = {"for": "answer", "passage_id": REAL_LATEST_A, "exact_line": "x"}
        older_quote = {"for": "answer", "passage_id": FIX_OLDER_A, "exact_line": "x"}
        deleted_quote = {"for": "answer", "passage_id": FIX_OLDER_DELETED, "exact_line": "x"}
        lab_quote = {"for": "answer", "passage_id": FIX_LAB, "exact_line": "x"}
        decide = sp.D6Plugin._decide_status

        # rule 0: a rule-type link with a verified rule quote.
        assert decide({"d4_link_type": "rule_used"}, [rule_quote], [], []) \
            == ("latest_ncert", "0", "link_type 'rule_used' with 1 verified rule quote(s)")
        # rule 0 for concept_applied and rules_chained too.
        for lt in ("rules_chained", "concept_applied"):
            assert decide({"d4_link_type": lt}, [rule_quote], [], [])[1] == "0"
        # rule 1: verified latest lines, but no rule quote / not a rule-type link.
        assert decide({"d4_link_type": "states_answer"}, [answer_quote], [], [])[:2] \
            == ("latest_ncert", "1")
        # rule 1 also catches a rule-type link whose quotes are NOT labelled `for: "rule"`.
        assert decide({"d4_link_type": "rule_used"}, [answer_quote], [], [])[1] == "1"
        # rule 2: no latest line at all, but a verified lab-manual line.
        assert decide({"d4_link_type": "states_answer"}, [], [], [lab_quote])[:2] \
            == ("lab_manual", "2")
        # rule 4: nothing anywhere.
        assert decide({"d4_link_type": "states_answer"}, [], [], [])[:2] == ("outside_ncert", "4")
        # rule 4 with beyond_ncert_method still gives outside_ncert (the NOTE TYPE is what changes).
        assert decide({"d4_link_type": "beyond_ncert_method"}, [], [], [])[:2] \
            == ("outside_ncert", "4")
        assert sp.D6Plugin._allowed_note_types("outside_ncert", "4", "beyond_ncert_method", []) \
            == ["outside_rules"]
        assert sp.D6Plugin._allowed_note_types("outside_ncert", "4", "states_answer", []) \
            == ["outside"]

        # rules 3 and 3b need rows that do not exist in real data. Write them into the ISOLATED
        # root only, clearly marked as fixtures.
        lib_io.write_csv(rc.pp("ncert", "deleted_topics.csv"),
                           [{"old_passage_id": FIX_OLDER_DELETED, "chapter_id": "BIO12-CH01",
                              "old_pages": "1", "heading": "FIXTURE deleted topic",
                              "subtopic_hint": "fixture"}],
                           ["old_passage_id", "chapter_id", "old_pages", "heading", "subtopic_hint"])
        lib_io.write_csv(rc.pp("ncert", "change_log.csv"),
                           [{"change_id": FIX_CHANGE_ID, "chapter_id": "BIO12-CH01",
                              "subtopic_id": "BIO12-CH01-ST01", "old_passage_id": FIX_OLDER_A,
                              "new_passage_id": REAL_LATEST_A, "change_type": "fact_changed",
                              "old_fact": "FIXTURE old", "new_fact": "FIXTURE new",
                              "could_flip_an_answer": "True", "old_text": "f", "new_text": "f",
                              "affected_questions": "", "approval": "pending"}],
                           ["change_id", "chapter_id", "subtopic_id", "old_passage_id",
                            "new_passage_id", "change_type", "old_fact", "new_fact",
                            "could_flip_an_answer", "old_text", "new_text", "affected_questions",
                            "approval"])

        # rule 3: an older line in a passage on deleted_topics.csv.
        assert decide({"d4_link_type": "states_answer"}, [], [deleted_quote], [])[:2] \
            == ("deleted_content", "3")
        # rule 3b: an older line in a passage with a change-log entry.
        assert decide({"d4_link_type": "states_answer"}, [], [older_quote], [])[:2] \
            == ("latest_ncert", "3b")
        # ORDER, the part that matters: rule 3 wins over 3b when BOTH apply...
        assert decide({"d4_link_type": "states_answer"}, [], [deleted_quote, older_quote], [])[1] == "3"
        # ...rule 2 wins over 3 and 3b...
        assert decide({"d4_link_type": "states_answer"}, [], [deleted_quote], [lab_quote])[1] == "2"
        # ...rule 1 wins over 2/3/3b...
        assert decide({"d4_link_type": "states_answer"}, [answer_quote], [deleted_quote],
                        [lab_quote])[1] == "1"
        # ...and rule 0 wins over everything, which is what keeps Physics on-syllabus.
        assert decide({"d4_link_type": "rule_used"}, [rule_quote], [deleted_quote], [lab_quote])[1] == "0"
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d6_rule_ladder_order_is_first_match_wins: OK")


def test_d6_templates_round_trip_against_spec_3_1():
    """Every one of spec 3.1's seven templates: the SCRIPT's filler output must satisfy the
    CHECK's own template regex. If the two ever drift apart, the script-fill fallback would
    produce a note its own check rejects."""
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        d6 = rc.load_check_module("D6")
        fill = sp.D6Plugin._fill_template
        cases = {
            "same_both": fill("same_both", latest_line="Water is a solvent."),
            "written_differently": fill("written_differently", latest_line="Water is a solvent.",
                                          older_line="Water dissolves things."),
            "answer_changed": ('By the latest NCERT the answer is (3): "Water is a solvent". '
                                'The older NCERT said "Water dissolves things", which gave (2). '
                                'Follow the latest.'),
            "deleted": fill("deleted", older_line="Water dissolves things."),
            "outside": fill("outside"),
            "outside_rules": fill("outside_rules", rule_lines=["F = ma", "v = u + at"]),
            "lab_manual": fill("lab_manual", latest_line="Read the vernier scale."),
        }
        assert set(cases) == set(d6._TEMPLATES), (sorted(cases), sorted(d6._TEMPLATES))
        for note_type, note in cases.items():
            assert note, f"{note_type}: filler returned nothing"
            assert d6._TEMPLATES[note_type].match(d6._norm(note)), \
                f"{note_type}: filled template does not match its own regex: {note!r}"
        # A note with extra prose outside the template must FAIL (spec 12/D6: "note matches its
        # template"; the agent file's own Never: "never add explanations outside the template").
        bad = cases["same_both"] + " This is because water is polar."
        assert not d6._TEMPLATES["same_both"].match(d6._norm(bad))
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d6_templates_round_trip_against_spec_3_1: OK")


def test_d6_end_to_end_flags_unverifiable_outside_ncert():
    """A question with no verified evidence of any kind AND no older edition available must not
    simply be declared off-syllabus: rules 3/3b were never evaluable, so D6_STATUS_UNVERIFIABLE
    must be raised alongside the D6_NOTE_APPROVAL the `outside` note type already needs."""
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        pa, _ = _seed_latest_and_older(tmp)
        qid = "Q-FIX0020"
        _record(tmp, qid, official_answer="2", status="normal", year=2023, sitting="MAIN",
                 subject="Biology", stem_en="Fixture question with no NCERT support.",
                 options_en={"2": "b"}, d4_link_type="states_answer", d4_evidence=[],
                 d4_supports_answer="not_at_all", d5_older=[], d5_older_passages_available=0)
        _d3_out(tmp, qid, latest=[{"passage_id": REAL_LATEST_A, "text": pa["text"]}], older=[])
        for step in ("D3", "D4"):
            _status(tmp, step, qid, "pass")
        _status(tmp, "D5", qid, "skipped")

        plugin = sp.D6Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        lines = plugin.list_items(filters)
        assert len(lines) == 1 and lines[0].agent == "d6-status-note-writer", lines
        with open(rc.pp("steps", "D6", "work", f"{qid}.runA.input.json")) as f:
            agent_input = json.load(f)
        assert agent_input["syllabus_status"] == "outside_ncert"
        assert agent_input["allowed_note_types"] == ["outside"]

        lib_io.atomic_write_json(rc.pp("steps", "D6", "out", f"{qid}.runA.json"), {
            "syllabus_status": "outside_ncert", "note_type": "outside",
            "reason_note": "This fact is not in any NCERT edition. The answer is from the "
                            "official key.",
            "quoted_lines": []})
        assert plugin.check(filters) == []
        assert rc.read_item_status("D6", qid)["status"] == "pass"
        record = _read(rc.pp("papers", "records", f"{qid}.json"))
        assert record["syllabus_status"] == "outside_ncert" and record["note_type"] == "outside"
        assert record["d6_rule_fired"] == "4"
        codes = {f["code"] for f in lib_io.read_jsonl(rc.pp("flags", "flags.jsonl"))}
        assert "D6_NOTE_APPROVAL" in codes and "D6_STATUS_UNVERIFIABLE" in codes, codes
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d6_end_to_end_flags_unverifiable_outside_ncert: OK")


def test_d6_leaves_the_note_empty_when_no_verified_line_can_fill_the_template():
    """Rule 3b resolves to `latest_ncert` on the strength of an OLDER line in a changed passage,
    with no verified LATEST line at all. If the agent's note is then unusable, the script must NOT
    fill `Answer from the latest NCERT: "..."` with a placeholder -- a student would read that as
    NCERT's own wording. The note is left empty and the flag escalates to `normal`."""
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        pa, _ = _seed_latest_and_older(tmp)
        lib_io.write_csv(rc.pp("ncert", "change_log.csv"),
                           [{"change_id": FIX_CHANGE_ID, "chapter_id": "BIO12-CH01",
                              "subtopic_id": "", "old_passage_id": FIX_OLDER_A,
                              "new_passage_id": REAL_LATEST_A, "change_type": "fact_changed",
                              "old_fact": "FIXTURE", "new_fact": "FIXTURE",
                              "could_flip_an_answer": "True", "old_text": "", "new_text": "",
                              "affected_questions": "", "approval": "pending"}],
                           ["change_id", "chapter_id", "subtopic_id", "old_passage_id",
                            "new_passage_id", "change_type", "old_fact", "new_fact",
                            "could_flip_an_answer", "old_text", "new_text", "affected_questions",
                            "approval"])
        older_line = "Pollen transfer from anther to stigma is called pollination."
        qid = "Q-FIX0022"
        _record(tmp, qid, official_answer="2", status="normal", year=2023, sitting="MAIN",
                 subject="Biology", stem_en="Fixture.", options_en={"2": "b"},
                 d4_link_type="states_answer", d4_evidence=[],   # no latest line at all
                 d5_older=[{"for": "answer", "passage_id": FIX_OLDER_A,
                             "exact_line": older_line}],
                 d5_older_passages_available=1)
        _d3_out(tmp, qid, latest=[{"passage_id": REAL_LATEST_A, "text": pa["text"]}],
                 older=[{"passage_id": FIX_OLDER_A,
                          "text": "FIXTURE older-edition text, not real NCERT. " + older_line}])
        for step in ("D3", "D4"):
            _status(tmp, step, qid, "pass")
        _status(tmp, "D5", qid, "pass")

        plugin = sp.D6Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        lines = plugin.list_items(filters)
        assert len(lines) == 1
        with open(rc.pp("steps", "D6", "work", f"{qid}.runA.input.json")) as f:
            agent_input = json.load(f)
        assert agent_input["syllabus_status"] == "latest_ncert", "rule 3b"
        assert agent_input["change_log_entries"][0]["change_id"] == FIX_CHANGE_ID

        bad = {"syllabus_status": "latest_ncert", "note_type": "same_both",
               "reason_note": "Freeform prose that is not any template.", "quoted_lines": []}
        lib_io.atomic_write_json(rc.pp("steps", "D6", "out", f"{qid}.runA.json"), bad)
        assert len(plugin.check(filters)) == 1
        lib_io.atomic_write_json(rc.pp("steps", "D6", "out", f"{qid}.retry1.json"), bad)
        assert plugin.check(filters) == []

        record = _read(rc.pp("papers", "records", f"{qid}.json"))
        assert record["d6_rule_fired"] == "3b", record["d6_rule_fired"]
        assert record["reason_note"] == "", repr(record["reason_note"])
        assert "None" not in str(record["reason_note"])
        flags = list(lib_io.read_jsonl(rc.pp("flags", "flags.jsonl")))
        tmpl = [f for f in flags if f["code"] == "D6_TEMPLATE_NOTE"]
        assert tmpl and tmpl[0]["severity"] == "normal", tmpl
        assert "left EMPTY for Stage F" in tmpl[0]["message"]
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d6_leaves_the_note_empty_when_no_verified_line_can_fill_the_template: OK")


def test_d6_script_fills_template_after_a_failed_retry():
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        pa, _ = _seed_latest_and_older(tmp)
        real_line = "Transfer of pollen grains (shed from the anther) to the stigma of a pistil is termed pollination."
        qid = "Q-FIX0021"
        _record(tmp, qid, official_answer="2", status="normal", year=2023, sitting="MAIN",
                 subject="Biology", stem_en="Fixture.", options_en={"2": "b"},
                 d4_link_type="states_answer",
                 d4_evidence=[{"for": "answer", "passage_id": REAL_LATEST_A,
                                "exact_line": real_line}],
                 d5_older=[], d5_older_passages_available=3)
        _d3_out(tmp, qid, latest=[{"passage_id": REAL_LATEST_A, "text": pa["text"]}], older=[])
        for step in ("D3", "D4"):
            _status(tmp, step, qid, "pass")
        _status(tmp, "D5", qid, "pass")

        plugin = sp.D6Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        plugin.list_items(filters)
        bad = {"syllabus_status": "latest_ncert", "note_type": "same_both",
               "reason_note": "The answer comes from NCERT because pollination happens.",
               "quoted_lines": []}
        lib_io.atomic_write_json(rc.pp("steps", "D6", "out", f"{qid}.runA.json"), bad)
        retry = plugin.check(filters)
        assert len(retry) == 1 and retry[0].run_label == "retry1", retry
        lib_io.atomic_write_json(rc.pp("steps", "D6", "out", f"{qid}.retry1.json"), bad)
        assert plugin.check(filters) == []

        record = _read(rc.pp("papers", "records", f"{qid}.json"))
        assert record["note_type"] == "same_both"
        assert record["reason_note"] == f'Answer from the latest NCERT: "{real_line}".'
        assert record["d6_quoted_lines"][0]["passage_id"] == REAL_LATEST_A
        codes = {f["code"] for f in lib_io.read_jsonl(rc.pp("flags", "flags.jsonl"))}
        assert "D6_TEMPLATE_NOTE" in codes, codes
        assert rc.read_item_status("D6", qid)["status"] == "flagged"
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d6_script_fills_template_after_a_failed_retry: OK")


# ===========================================================================
# 4. D7: the input restriction (spec Rule 10) is enforced in code, and the run gate is the spec's.
# ===========================================================================

def test_d7_input_guard_refuses_forbidden_material():
    clean = {"question": {"stem": "s"}, "options": {"1": "a"}, "official_answer": "2",
             "latest_evidence": [], "older_evidence": [], "change_log_entries": []}
    assert sp._guard_d7_input(dict(clean)) is not None

    for bad, why in [
        ({**clean, "b6_answer": "3"}, "B6's answer at the top level"),
        ({**clean, "coaching_notes": "x"}, "a coaching field at the top level"),
        ({**clean, "question": {"stem": "s", "b6_reason": "because"}}, "B6's reason nested"),
        ({**clean, "latest_evidence": [{"passage_id": "P", "b6_working": "x"}]},
         "a B6 field nested inside a list"),
        ({**clean, "legacy_row": {"Chapter Name": "x"}}, "a legacy-sheet row"),
        ({**clean, "solution": "worked explanation"}, "a worked solution"),
    ]:
        try:
            sp._guard_d7_input(bad)
        except sp.D7InputGuardError:
            pass
        else:
            raise AssertionError(f"D7 input guard let through {why}: {sorted(bad)}")

    # A coaching/legacy PATH anywhere also fails, via lib/coaching_guard.py.
    try:
        sp._guard_d7_input({**clean, "question": {"stem": "inputs/coaching/allen.pdf"}})
    except Exception as e:  # CoachingGuardError
        assert "coaching" in str(e).lower(), e
    else:
        raise AssertionError("D7 input guard let through an inputs/coaching/ path")

    # The official answer IS allowed for D7 (unlike B6) -- it has to compare against it.
    assert sp._guard_d7_input(dict(clean))["official_answer"] == "2"
    print("test_d7_input_guard_refuses_forbidden_material: OK")


def test_d7_run_gate_and_skip_path():
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        pa, _ = _seed_latest_and_older(tmp)
        real_line = "Transfer of pollen grains (shed from the anther) to the stigma of a pistil is termed pollination."
        base = dict(official_answer="2", status="normal", year=2023, sitting="MAIN",
                     subject="Biology", stem_en="Fixture.", options_en={"1": "a", "2": "b",
                                                                          "3": "c", "4": "d"},
                     d4_link_type="states_answer",
                     d4_evidence=[{"for": "answer", "passage_id": REAL_LATEST_A,
                                    "exact_line": real_line}])

        # (a) Neither limb true -> skipped, latest_answer = the official answer, no flag.
        qid = "Q-FIX0030"
        _record(tmp, qid, **base, d5_older=[])
        _d3_out(tmp, qid, latest=[{"passage_id": REAL_LATEST_A, "text": pa["text"]}])
        for step in ("D3", "D4", "D5", "D6"):
            _status(tmp, step, qid, "pass")
        plugin = sp.D7Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        assert plugin.list_items(filters) == [], "a question neither limb selects must not be dispatched"
        assert plugin.check(filters) == []
        assert rc.read_item_status("D7", qid)["status"] == "skipped"
        rec = _read(rc.pp("papers", "records", f"{qid}.json"))
        assert rec["latest_answer"] == "2" and rec["d7_same_as_official"] is True
        assert not os.path.exists(rc.pp("flags", "flags.jsonl")) or \
            not list(lib_io.read_jsonl(rc.pp("flags", "flags.jsonl"))), "the skip path raises no flag"

        # (b) Limb 2: the older line differs from the latest line -> D7 runs.
        qid2 = "Q-FIX0031"
        _record(tmp, qid2, **base,
                 d5_older=[{"for": "answer", "passage_id": FIX_OLDER_A,
                             "exact_line": "Pollen transfer from anther to stigma is called "
                                            "pollination."}])
        _d3_out(tmp, qid2, latest=[{"passage_id": REAL_LATEST_A, "text": pa["text"]}],
                 older=[{"passage_id": FIX_OLDER_A, "text": "FIXTURE older text."}])
        for step in ("D3", "D4", "D5", "D6"):
            _status(tmp, step, qid2, "pass")
        should, why = sp.D7Plugin._should_run(_read(rc.pp("papers", "records", f"{qid2}.json")))
        assert should and "differs" in why, why

        # ...but an older line that differs only by whitespace/LaTeX spacing does NOT trigger it
        # (spec 5.7's two normalisations are applied before comparing).
        _record(tmp, "Q-FIX0032", **base,
                 d5_older=[{"for": "answer", "passage_id": FIX_OLDER_A,
                             "exact_line": "Transfer  of pollen grains (shed from the anther)\n"
                                            "to the stigma of a pistil is termed pollination."}])
        should2, why2 = sp.D7Plugin._should_run(
            _read(rc.pp("papers", "records", "Q-FIX0032.json")))
        assert not should2, f"whitespace-only difference must not count as differing: {why2}"

        # (c) Limb 1: a change-log entry on an evidence passage -> D7 runs even with no older line.
        lib_io.write_csv(rc.pp("ncert", "change_log.csv"),
                           [{"change_id": FIX_CHANGE_ID, "chapter_id": "BIO12-CH01",
                              "subtopic_id": "", "old_passage_id": FIX_OLDER_A,
                              "new_passage_id": REAL_LATEST_A, "change_type": "fact_changed",
                              "old_fact": "FIXTURE", "new_fact": "FIXTURE",
                              "could_flip_an_answer": "True", "old_text": "", "new_text": "",
                              "affected_questions": "", "approval": "pending"}],
                           ["change_id", "chapter_id", "subtopic_id", "old_passage_id",
                            "new_passage_id", "change_type", "old_fact", "new_fact",
                            "could_flip_an_answer", "old_text", "new_text", "affected_questions",
                            "approval"])
        should3, why3 = sp.D7Plugin._should_run(_read(rc.pp("papers", "records", f"{qid}.json")))
        assert should3 and FIX_CHANGE_ID in why3, why3

        # And the built input is allowlisted + guarded.
        agent_input = sp.D7Plugin._build_input(_read(rc.pp("papers", "records", f"{qid}.json")))
        assert set(agent_input) <= sp._D7_ALLOWED_TOP_LEVEL, sorted(agent_input)
        assert agent_input["change_log_entries"][0]["change_id"] == FIX_CHANGE_ID
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d7_run_gate_and_skip_path: OK")


def test_d7_answer_changed_triggers_flags_note_rewrite_and_d4_rerun():
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        pa, _ = _seed_latest_and_older(tmp)
        real_line = "Transfer of pollen grains (shed from the anther) to the stigma of a pistil is termed pollination."
        qid = "Q-FIX0040"
        _record(tmp, qid, official_answer="2", status="normal", year=2023, sitting="MAIN",
                 subject="Biology", stem_en="Fixture.",
                 options_en={"1": "a", "2": "b", "3": "c", "4": "d"},
                 d4_link_type="states_answer",
                 d4_evidence=[{"for": "answer", "passage_id": REAL_LATEST_A,
                                "exact_line": real_line}],
                 d5_older=[{"for": "answer", "passage_id": FIX_OLDER_A,
                             "exact_line": "Pollen transfer from anther to stigma is called "
                                            "pollination."}],
                 syllabus_status="latest_ncert", note_type="same_both",
                 reason_note=f'Answer from the latest NCERT: "{real_line}".')
        _d3_out(tmp, qid, latest=[{"passage_id": REAL_LATEST_A, "text": pa["text"]}],
                 older=[{"passage_id": FIX_OLDER_A, "text": "FIXTURE older text."}])
        for step in ("D3", "D4", "D5", "D6"):
            _status(tmp, step, qid, "pass")

        plugin = sp.D7Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        lines = plugin.list_items(filters)
        assert len(lines) == 1 and lines[0].agent == "d7-latest-answer-checker", lines

        lib_io.atomic_write_json(rc.pp("steps", "D7", "out", f"{qid}.runA.json"), {
            "latest_answer": "3", "same_as_official": False, "quote": real_line,
            "change_id": None,
            "sentence_for_note": "By the older NCERT the answer was (2); by the latest NCERT it is (3).",
            "note": "FIXTURE: no change-log row covers this passage."})

        new_lines = plugin.check(filters)
        # spec 12/D7: D4 re-runs for latest_answer.
        assert len(new_lines) == 1 and new_lines[0].agent == "d4-evidence-quoter", new_lines
        assert new_lines[0].run_label == "d4_latest"
        with open(rc.pp("steps", "D7", "work", f"{qid}.d4_latest.input.json")) as f:
            rerun_input = json.load(f)
        assert rerun_input["answer_to_support"]["number"] == "3"
        assert rerun_input["answer_to_support"]["text"] == "c"
        assert "question" in rerun_input and "passages" in rerun_input

        record = _read(rc.pp("papers", "records", f"{qid}.json"))
        assert record["latest_answer"] == "3"
        assert record["note_type"] == "answer_changed", record["note_type"]
        assert record["reason_note"].endswith("by the latest NCERT it is (3)."), record["reason_note"]
        codes = {f["code"] for f in lib_io.read_jsonl(rc.pp("flags", "flags.jsonl"))}
        assert "D7_ANSWER_CHANGED" in codes and "D7_UNEXPLAINED_CHANGE" in codes, codes

        # Answer the D4 re-run; its quotes are verified independently and stored SEPARATELY.
        lib_io.atomic_write_json(rc.pp("steps", "D7", "out", f"{qid}.d4_latest.json"), {
            "link_type": "states_answer", "derivation_steps": [],
            "evidence": [{"for": "answer", "passage_id": REAL_LATEST_A, "exact_line": real_line},
                          {"for": "extra", "passage_id": REAL_LATEST_A,
                           "exact_line": "a paraphrase that is not in the passage"}],
            "supports_answer": "fully", "missing": [], "note": ""})
        assert plugin.check(filters) == []
        record = _read(rc.pp("papers", "records", f"{qid}.json"))
        assert len(record["d4_latest_answer_evidence"]) == 1, record["d4_latest_answer_evidence"]
        assert record["d4_evidence"][0]["exact_line"] == real_line, \
            "the OFFICIAL answer's evidence must survive untouched (spec 3: both are stored)"
        assert rc.read_item_status("D7", qid)["status"] == "flagged"
        codes = {f["code"] for f in lib_io.read_jsonl(rc.pp("flags", "flags.jsonl"))}
        assert "D7_QUOTE_NOT_FOUND" in codes, codes
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d7_answer_changed_triggers_flags_note_rewrite_and_d4_rerun: OK")


# ===========================================================================
# 5. D8 / D9
# ===========================================================================

def test_d8_uses_latest_answer_and_flags_low_confidence():
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        pa, _ = _seed_latest_and_older(tmp)
        qid = "Q-FIX0050"
        _record(tmp, qid, official_answer="2", status="normal", year=2023, sitting="MAIN",
                 subject="Biology", stem_en="Fixture.",
                 options_en={"1": "a", "2": "b", "3": "c", "4": "d"},
                 structure="plain", d1_chapter_ids=["BIO12-CH01"],
                 d2_subtopic_ids=["BIO12-CH01-ST01"], d4_link_type="states_answer",
                 d4_evidence=[], d4_derivation_steps=[],
                 latest_answer="3")  # D7 changed the taught answer
        _d3_out(tmp, qid, latest=[{"passage_id": REAL_LATEST_A, "text": pa["text"]}])
        for step in ("D3", "D4", "D5", "D6", "D7"):
            _status(tmp, step, qid, "pass")

        plugin = sp.D8Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        lines = plugin.list_items(filters)
        assert len(lines) == 1
        with open(rc.pp("steps", "D8", "work", f"{qid}.runA.input.json")) as f:
            agent_input = json.load(f)
        # spec 12 preamble: D8-E5 use latest_answer, not the official answer.
        assert agent_input["answer_taught"] == {"number": "3", "text": "c"}, agent_input["answer_taught"]

        lib_io.atomic_write_json(rc.pp("steps", "D8", "out", f"{qid}.runA.json"), {
            "fact_line": "Pollen is transferred from the anther to the stigma.",
            "facts": [], "confidence": "low"})
        assert plugin.check(filters) == []
        record = _read(rc.pp("papers", "records", f"{qid}.json"))
        assert record["fact_line"] == "Pollen is transferred from the anther to the stigma."
        assert record["d8_fact_line"] == record["fact_line"]
        codes = {f["code"] for f in lib_io.read_jsonl(rc.pp("flags", "flags.jsonl"))}
        assert codes == {"D8_LOW_CONFIDENCE"}, codes
        assert rc.read_item_status("D8", qid)["status"] == "pass", \
            "a low-confidence fact line is flagged, never failed"
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d8_uses_latest_answer_and_flags_low_confidence: OK")


def test_d9_scopes_to_other_years_and_skips_an_empty_table():
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        _seed_latest_and_older(tmp)
        common = dict(official_answer="2", status="normal", sitting="MAIN", subject="Biology",
                       stem_en="Fixture.", options_en={"2": "b"},
                       d2_subtopic_ids=["BIO12-CH01-ST01"])
        # Same subtopic, three different years, plus one same-year sibling and one other subtopic.
        _record(tmp, "Q-FIX0060", year=2019, fact_line="Pollination transfers pollen.", **common)
        _record(tmp, "Q-FIX0061", year=2023, fact_line="Pollen moves to the stigma.", **common)
        _record(tmp, "Q-FIX0062", year=2023, sitting="PH2", official_answer="2", status="normal",
                 subject="Biology", stem_en="Fixture same year, other sitting.",
                 options_en={"2": "b"}, d2_subtopic_ids=["BIO12-CH01-ST01"],
                 fact_line="Pollen moves to the stigma, re-asked.")
        _record(tmp, "Q-FIX0063", year=2021, fact_line="Nucellus stores food.", **{
            **common, "d2_subtopic_ids": ["BIO12-CH01-ST09"]})
        for qid in ("Q-FIX0060", "Q-FIX0061", "Q-FIX0062", "Q-FIX0063"):
            for step in ("D3", "D4", "D5", "D6", "D7", "D8"):
                _status(tmp, step, qid, "pass")

        pool = sp.D9Plugin._candidates()
        assert set(pool) == {"Q-FIX0060", "Q-FIX0061", "Q-FIX0062", "Q-FIX0063"}, sorted(pool)

        others_61 = sp.D9Plugin._others_table("Q-FIX0061", pool["Q-FIX0061"], pool)
        # 2019 sibling in the same subtopic: in. 2023/PH2 sibling: OUT (same year) -- the real
        # spec limitation this build reports rather than widens. Other subtopic: out.
        assert set(others_61) == {"Q-FIX0060"}, sorted(others_61)
        assert "Q-FIX0062" not in others_61, (
            "spec 12/D9 scopes to OTHER YEARS, so a same-year second sitting is structurally "
            "unfindable -- asserted here deliberately, and reported as a question for the owner")

        # A question whose table is empty resolves `skipped`, with no agent call and no flag.
        plugin = sp.D9Plugin()
        filters = {"chapters": None, "papers": None, "items": ["Q-FIX0063"]}
        assert plugin.list_items(filters) == []
        assert plugin.check(filters) == []
        assert rc.read_item_status("D9", "Q-FIX0063")["status"] == "skipped"
        assert not os.path.exists(rc.pp("flags", "flags.jsonl")) or \
            not list(lib_io.read_jsonl(rc.pp("flags", "flags.jsonl"))), \
            "an empty candidate table is a plain fact, not a doubt -- no flag"

        # The three that DO have a table get dispatched, and the agent never sees subtopic ids.
        # Note Q-FIX0062 (2023/PH2) IS dispatched -- it has a 2019 candidate; what it can never be
        # offered is its own same-year sibling Q-FIX0061, which is the limitation above.
        filters_all = {"chapters": None, "papers": None, "items": None}
        lines = plugin.list_items(filters_all)
        assert {l.item_id for l in lines} == {"Q-FIX0060", "Q-FIX0061", "Q-FIX0062"}, lines
        with open(rc.pp("steps", "D9", "work", "Q-FIX0061.runA.input.json")) as f:
            agent_input = json.load(f)
        assert set(agent_input) == {"this", "others"}
        assert "subtopic" not in json.dumps(agent_input), \
            "the agent must not be shown subtopic ids (it would group by subtopic name)"
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d9_scopes_to_other_years_and_skips_an_empty_table: OK")


# ===========================================================================
# 6. D10: union-find, and its idempotence (RG ids are never reused)
# ===========================================================================

def test_d10_union_find_components_and_idempotence():
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        _seed_latest_and_older(tmp)
        st = "BIO12-CH01-ST01"
        other_st = "BIO12-CH01-ST09"
        common = dict(official_answer="2", status="normal", sitting="MAIN", subject="Biology",
                       stem_en="Fixture.", options_en={"2": "b"}, fact_line="F.")
        # A-B-C chain (one component of 3, from a one-sided link each), D-E pair, F alone,
        # G linked only across subtopics (so, for THIS subtopic, a singleton).
        _record(tmp, "Q-FIXA", year=2013, d2_subtopic_ids=[st],
                 d9_possible_repeats=["Q-FIXB"], **common)
        _record(tmp, "Q-FIXB", year=2016, d2_subtopic_ids=[st],
                 d9_possible_repeats=["Q-FIXC"], **common)
        _record(tmp, "Q-FIXC", year=2019, d2_subtopic_ids=[st], d9_possible_repeats=[], **common)
        _record(tmp, "Q-FIXD", year=2021, d2_subtopic_ids=[st],
                 d9_possible_repeats=["Q-FIXE"], **common)
        _record(tmp, "Q-FIXE", year=2023, d2_subtopic_ids=[st], d9_possible_repeats=[], **common)
        _record(tmp, "Q-FIXF", year=2025, d2_subtopic_ids=[st], d9_possible_repeats=[], **common)
        _record(tmp, "Q-FIXG", year=2024, d2_subtopic_ids=[st],
                 d9_possible_repeats=["Q-FIXH"], **common)
        _record(tmp, "Q-FIXH", year=2022, d2_subtopic_ids=[other_st],
                 d9_possible_repeats=["Q-FIXG"], **common)
        # An absorbed C1 record must be ignored entirely.
        _record(tmp, "Q-FIXZ", year=2018, d2_subtopic_ids=[st], d9_possible_repeats=["Q-FIXA"],
                 merged_into="Q-FIXA", **common)

        assert build_groups.subtopics_with_work() == sorted([st, other_st])
        out = build_groups.build_for_subtopic(st)
        groups = {g["group_id"]: g["members"] for g in out["groups"]}
        members_sets = sorted(groups.values())
        assert members_sets == [["Q-FIXA", "Q-FIXB", "Q-FIXC"], ["Q-FIXD", "Q-FIXE"]], members_sets
        assert out["singletons"] == ["Q-FIXF", "Q-FIXG"], out["singletons"]
        assert "Q-FIXZ" not in json.dumps(out), "a C1-absorbed record must never enter a group"
        assert ["Q-FIXG", "Q-FIXH"] not in out["links_used"], \
            "a cross-subtopic link belongs to the other subtopic's own file"

        ok, msg = rc.load_check_module("D10").check(out, {"item_id": st, "step": "D10"})
        assert ok, msg
        ok_s, msg_s = rc.validate_schema("D10", out)
        assert ok_s, msg_s

        # Idempotence (spec 5.9): a rerun must be byte-identical and must MINT NO NEW RG ID.
        counters_before = json.load(open(lib_ids.COUNTERS_PATH))
        first = json.dumps(out, sort_keys=True)
        out2 = build_groups.build_for_subtopic(st)
        assert json.dumps(out2, sort_keys=True) == first, "a rerun changed the output"
        assert json.load(open(lib_ids.COUNTERS_PATH)) == counters_before, \
            "a no-op rerun minted a new repeat-group id"
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d10_union_find_components_and_idempotence: OK")


# ===========================================================================
# 7. D11: earliest-first ordering (from the real sitting calendar), agreement, splits
# ===========================================================================

def test_d11_sitting_order_comes_from_the_real_calendar():
    d11 = rc.load_check_module("D11")
    # lib/sittings.py's per-year lists are chronological: 2026 CANCELLED (3 May) precedes
    # REEXAM (21 Jun), and 2016 MAIN precedes PH2. The check must agree.
    assert d11.sitting_sort_key(2026, "CANCELLED") < d11.sitting_sort_key(2026, "REEXAM")
    assert d11.sitting_sort_key(2016, "MAIN") < d11.sitting_sort_key(2016, "PH2")
    assert d11.sitting_sort_key(2016, "PH2") < d11.sitting_sort_key(2017, "MAIN")
    # An off-calendar sitting is ordered deterministically (alphabetically) rather than randomly.
    assert d11.sitting_sort_key(2023, "MYSTERY") == (2023, 99, "MYSTERY")
    # The plugin and the check must use the SAME function -- otherwise the runner and its own
    # check could disagree about which member is earliest.
    assert d11.sitting_sort_key is rc.load_check_module("D11").sitting_sort_key
    print("test_d11_sitting_order_comes_from_the_real_calendar: OK")


def test_d11_two_runs_agree_disagree_and_split():
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        _seed_latest_and_older(tmp)
        st = "BIO12-CH01-ST01"
        common = dict(official_answer="2", status="normal", sitting="MAIN", subject="Biology",
                       stem_en="Fixture stem.", options_en={"2": "b"}, fact_line="F.")
        for qid, year in (("Q-FIXA", 2013), ("Q-FIXB", 2016), ("Q-FIXC", 2019)):
            _record(tmp, qid, year=year, d2_subtopic_ids=[st], d9_possible_repeats=[], **common)
        group_id = "RG-0001"
        lib_io.atomic_write_json(rc.pp("steps", "D10", "out", f"{st}.json"), {
            "subtopic_id": st,
            "groups": [{"group_id": group_id, "members": ["Q-FIXA", "Q-FIXB", "Q-FIXC"]}],
            "singletons": [], "links_used": [["Q-FIXA", "Q-FIXB"], ["Q-FIXB", "Q-FIXC"]]})
        _status(tmp, "D10", st, "pass")

        plugin = sp.D11Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        lines = plugin.list_items(filters)
        assert {l.run_label for l in lines} == {"runA", "runB"}, lines
        assert all(l.item_id == group_id for l in lines)
        with open(rc.pp("steps", "D11", "work", f"{group_id}.runA.input.json")) as f:
            agent_input = json.load(f)
        assert "codebook" in agent_input, "codebook/D11.md exists, so spec 13.0 says pass it"
        assert len(agent_input["members"]) == 3
        assert set(agent_input["members"][0]) == {"id", "year", "sitting", "stem", "answer_text",
                                                    "fact_line"}

        verdict_a = {"groups": [{"fact_line": "F.", "first": "Q-FIXA",
                                   "members": [{"id": "Q-FIXA", "label": "first"},
                                                {"id": "Q-FIXB", "label": "reworded"}]}],
                      "related": [{"id": "Q-FIXC", "related_to": "Q-FIXA"}], "removed": []}
        verdict_b = json.loads(json.dumps(verdict_a))
        lib_io.atomic_write_json(rc.pp("steps", "D11", "out", f"{group_id}.runA.json"), verdict_a)
        lib_io.atomic_write_json(rc.pp("steps", "D11", "out", f"{group_id}.runB.json"), verdict_b)
        assert plugin.check(filters) == []
        assert rc.read_item_status("D11", group_id)["status"] == "pass"

        rec_a = _read(rc.pp("papers", "records", "Q-FIXA.json"))
        rec_b = _read(rc.pp("papers", "records", "Q-FIXB.json"))
        rec_c = _read(rc.pp("papers", "records", "Q-FIXC.json"))
        assert rec_a["repeat_group_id"] == group_id and rec_a["repeat_label"] == "first"
        assert rec_b["repeat_label"] == "reworded"
        assert rec_c["repeat_group_id"] is None and rec_c["related_ids"] == ["Q-FIXA"]
        assert rec_a["related_ids"] == ["Q-FIXC"], "related_ids is written symmetrically"
        assert rec_a["d11_codebook_version"] not in (None, "none"), \
            "codebook_version must be the real content hash of codebook/D11.md"
    shutil.rmtree(tmp, ignore_errors=True)

    # --- Disagreement -> adjudicator; adjudicator 'combined' splits the group into two. ---
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        _seed_latest_and_older(tmp)
        st = "BIO12-CH01-ST01"
        common = dict(official_answer="2", status="normal", sitting="MAIN", subject="Biology",
                       stem_en="Fixture stem.", options_en={"2": "b"}, fact_line="F.")
        for qid, year in (("Q-FIXA", 2013), ("Q-FIXB", 2016), ("Q-FIXC", 2019), ("Q-FIXD", 2021)):
            _record(tmp, qid, year=year, d2_subtopic_ids=[st], d9_possible_repeats=[], **common)
        group_id = "RG-0001"
        lib_io.atomic_write_json(rc.pp("steps", "D10", "out", f"{st}.json"), {
            "subtopic_id": st,
            "groups": [{"group_id": group_id,
                         "members": ["Q-FIXA", "Q-FIXB", "Q-FIXC", "Q-FIXD"]}],
            "singletons": [], "links_used": [["Q-FIXA", "Q-FIXB"], ["Q-FIXB", "Q-FIXC"],
                                               ["Q-FIXC", "Q-FIXD"]]})
        _status(tmp, "D10", st, "pass")
        plugin = sp.D11Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        plugin.list_items(filters)

        four_in_one = {"groups": [{"fact_line": "F.", "first": "Q-FIXA", "members": [
            {"id": "Q-FIXA", "label": "first"}, {"id": "Q-FIXB", "label": "reworded"},
            {"id": "Q-FIXC", "label": "reworded"}, {"id": "Q-FIXD", "label": "reworded"}]}],
            "related": [], "removed": []}
        two_plus_removed = {"groups": [{"fact_line": "F.", "first": "Q-FIXA", "members": [
            {"id": "Q-FIXA", "label": "first"}, {"id": "Q-FIXB", "label": "exact_same"}]}],
            "related": [{"id": "Q-FIXC", "related_to": "Q-FIXA"}], "removed": ["Q-FIXD"]}
        lib_io.atomic_write_json(rc.pp("steps", "D11", "out", f"{group_id}.runA.json"), four_in_one)
        lib_io.atomic_write_json(rc.pp("steps", "D11", "out", f"{group_id}.runB.json"),
                                   two_plus_removed)
        adj_lines = plugin.check(filters)
        assert len(adj_lines) == 1 and adj_lines[0].agent == "x-adjudicator", adj_lines

        split = {"groups": [
            {"fact_line": "Fact one.", "first": "Q-FIXA",
             "members": [{"id": "Q-FIXA", "label": "first"},
                          {"id": "Q-FIXB", "label": "exact_same"}]},
            {"fact_line": "Fact two.", "first": "Q-FIXC",
             "members": [{"id": "Q-FIXC", "label": "first"},
                          {"id": "Q-FIXD", "label": "same_fact_new_format"}]}],
            "related": [], "removed": []}
        lib_io.atomic_write_json(rc.pp("steps", "D11", "out", f"{group_id}.adjudicated.json"),
                                   {"choice": "combined", "value": split, "why": "two facts"})
        assert plugin.check(filters) == []
        assert rc.read_item_status("D11", group_id)["status"] == "flagged"
        codes = {f["code"] for f in lib_io.read_jsonl(rc.pp("flags", "flags.jsonl"))}
        assert "D11_ADJUDICATED" in codes, codes

        resolved = _read(rc.pp("steps", "D11", "out", f"{group_id}.resolved.json"))
        ids = [g["group_id"] for g in resolved["groups"]]
        assert ids[0] == group_id, "the first split group keeps the candidate's own RG id"
        assert len(set(ids)) == 2 and ids[1].startswith("RG-"), ids
        assert _read(rc.pp("papers", "records", "Q-FIXC.json"))["repeat_group_id"] == ids[1]
        assert _read(rc.pp("papers", "records", "Q-FIXA.json"))["repeat_group_id"] == group_id
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d11_two_runs_agree_disagree_and_split: OK")


def test_d11_blocks_when_neither_run_is_usable():
    """Spec 5.5 rung 4: no safe default -> blocked + blocker flag. A repeat group is never
    guessed at."""
    tmp = _build_isolated_root()
    with _isolated_project(tmp):
        _seed_latest_and_older(tmp)
        st = "BIO12-CH01-ST01"
        common = dict(official_answer="2", status="normal", sitting="MAIN", subject="Biology",
                       stem_en="Fixture stem.", options_en={"2": "b"}, fact_line="F.")
        for qid, year in (("Q-FIXA", 2013), ("Q-FIXB", 2016)):
            _record(tmp, qid, year=year, d2_subtopic_ids=[st], d9_possible_repeats=[], **common)
        group_id = "RG-0001"
        lib_io.atomic_write_json(rc.pp("steps", "D10", "out", f"{st}.json"), {
            "subtopic_id": st, "groups": [{"group_id": group_id, "members": ["Q-FIXA", "Q-FIXB"]}],
            "singletons": [], "links_used": [["Q-FIXA", "Q-FIXB"]]})
        _status(tmp, "D10", st, "pass")
        plugin = sp.D11Plugin()
        filters = {"chapters": None, "papers": None, "items": None}
        plugin.list_items(filters)
        for run in ("runA", "runB"):
            lib_io.atomic_write_json(rc.pp("steps", "D11", "out", f"{group_id}.{run}.json"),
                                       {"error": "FIXTURE: input unreadable"})
        assert plugin.check(filters) == []
        assert rc.read_item_status("D11", group_id)["status"] == "blocked"
        codes = {f["code"] for f in lib_io.read_jsonl(rc.pp("flags", "flags.jsonl"))}
        assert codes == {"D11_UNRESOLVED"}, codes
    shutil.rmtree(tmp, ignore_errors=True)
    print("test_d11_blocks_when_neither_run_is_usable: OK")


def _read(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


_TESTS = [
    test_check_modules_pass_and_fail_fixtures,
    test_d5_quote_verification_and_latest_edition_refusal,
    test_d5_skips_when_no_older_passages_exist,
    test_d6_rule_ladder_order_is_first_match_wins,
    test_d6_templates_round_trip_against_spec_3_1,
    test_d6_end_to_end_flags_unverifiable_outside_ncert,
    test_d6_script_fills_template_after_a_failed_retry,
    test_d6_leaves_the_note_empty_when_no_verified_line_can_fill_the_template,
    test_d7_input_guard_refuses_forbidden_material,
    test_d7_run_gate_and_skip_path,
    test_d7_answer_changed_triggers_flags_note_rewrite_and_d4_rerun,
    test_d8_uses_latest_answer_and_flags_low_confidence,
    test_d9_scopes_to_other_years_and_skips_an_empty_table,
    test_d10_union_find_components_and_idempotence,
    test_d11_sitting_order_comes_from_the_real_calendar,
    test_d11_two_runs_agree_disagree_and_split,
    test_d11_blocks_when_neither_run_is_usable,
]


if __name__ == "__main__":
    for fn in _TESTS:
        fn()
    print(f"tests/test_d5_d11.py: ALL OK ({len(_TESTS)} tests)")
