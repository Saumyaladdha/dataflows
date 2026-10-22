#!/usr/bin/env python3
"""Confirms every scripts/checks/<STEP>.py (S0, A1-A9 -- 11 files) imports cleanly and its
check(data, context) function runs without crashing against a hand-built fixture matching that
step's schema, per the M2/M3 task's testing requirement. This does NOT prove each check is
exhaustively correct (several steps have no real upstream data yet -- see the build report) --
it proves the convention holds: every file loads, every check() returns a (bool, str) pair for
both a passing-shaped and a failing-shaped fixture, and none of them raises.

Run: .venv/bin/python3 tests/test_checks_fixtures.py
"""
import os
import sys

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_TESTS_DIR)
_SCRIPTS_DIR = os.path.join(_PROJECT_ROOT, "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402

# Each entry: (step, data_pass, context_pass, data_fail, context_fail). Fixtures are minimal and
# match that step's schemas/<STEP>.json required fields (checked separately by
# rc.validate_schema in run_step.py; here only check() itself is exercised).
FIXTURES = {}

FIXTURES["S0"] = (
    {"item_type": "ncert_book", "subject": "Biology", "class": 12, "edition": "latest",
     "year": None, "sitting": None, "booklet_code": None, "file": None, "in_scope": None,
     "status": "present", "note": "found"},
    {"item_id": "ncert-Biology-12-latest", "step": "S0", "open_flags": []},
    {"item_type": "paper", "subject": None, "class": None, "edition": None, "year": 2024,
     "sitting": "MAIN", "booklet_code": None, "file": None, "in_scope": True,
     "status": "missing", "note": "not found"},
    {"item_id": "paper-2024-MAIN", "step": "S0", "open_flags": []},  # no matching flag -> fails
)

FIXTURES["A1"] = (
    {"subject": "Chemistry", "class": 12, "language": "English", "part": None,
     "edition_seen": "latest", "reprint_text_exact": "Reprint 2026-27", "reprint_page": 1,
     "is_lab_manual": False, "note": ""},
    {"item_id": "x", "step": "A1",
     "input_data": {"folder_edition_hint": "latest", "text_layer": ["intro Reprint 2026-27 end"]}},
    {"subject": "Chemistry", "class": 12, "language": "English", "part": None,
     "edition_seen": "older", "reprint_text_exact": "Reprint 2026-27", "reprint_page": 1,
     "is_lab_manual": False, "note": ""},
    {"item_id": "x", "step": "A1",
     "input_data": {"folder_edition_hint": "latest", "text_layer": ["intro Reprint 2026-27 end"]}},
)

FIXTURES["A2"] = (
    {"blocks": [{"n": 1, "kind": "paragraph", "text": "Hello world."}],
     "first_block_continues_from_previous": False, "last_block_continues_on_next": False,
     "running_header_footer_removed": [], "note": ""},
    {"item_id": "x", "step": "A2", "input_data": {"text_layer": "Hello world."}},
    {"blocks": [{"n": 1, "kind": "paragraph", "text": "Totally different text here."}],
     "first_block_continues_from_previous": False, "last_block_continues_on_next": False,
     "running_header_footer_removed": [], "note": ""},
    {"item_id": "x", "step": "A2", "input_data": {"text_layer": "Hello world, nothing alike at all really."}},
)

FIXTURES["A2S"] = (
    {"kind": "figure", "caption": "Figure 1.1: a diagram", "labels": ["A", "B"], "note": ""},
    {"item_id": "x", "step": "A2S"},
    {"kind": "figure", "caption": "", "labels": [], "note": ""},
    {"item_id": "x", "step": "A2S"},
)

FIXTURES["A3"] = (
    {"passages": [[1], [2, 4], [3], [5]], "note": ""},
    {"item_id": "x", "step": "A3", "input_data": {"blocks": [{"n": i} for i in range(1, 6)]}},
    {"passages": [[1], [2]], "note": ""},  # blocks 3,4,5 missing
    {"item_id": "x", "step": "A3", "input_data": {"blocks": [{"n": i} for i in range(1, 6)]}},
)

FIXTURES["A4"] = (
    {"chapter": "BIO12-CH06", "subtopics": [
        {"n": 1, "name": "Origin of life", "from_heading": "7.1", "passages": ["P01"]},
        {"n": 2, "name": "Evidence", "from_heading": "7.2", "passages": ["P02"]},
        {"n": 3, "name": "Natural selection", "from_heading": "7.3", "passages": ["P03"]},
        {"n": 4, "name": "Hardy-Weinberg", "from_heading": "7.4", "passages": ["P04"]},
    ], "note": ""},
    {"item_id": "BIO12-CH06", "step": "A4", "input_data": {}},
    {"chapter": "BIO12-CH06", "subtopics": [
        {"n": 1, "name": "Same name", "from_heading": "7.1", "passages": ["P01"]},
        {"n": 2, "name": "Same name", "from_heading": "7.2", "passages": ["P02"]},
    ], "note": ""},
    {"item_id": "BIO12-CH06", "step": "A4", "input_data": {}},
)

FIXTURES["A5"] = (
    {"passage_id": "BIO12O-CH06-P01", "subtopic_id": "BIO12-CH06-ST01", "confidence": "high", "note": ""},
    {"item_id": "x", "step": "A5", "input_data": {"subtopics": [{"id": "BIO12-CH06-ST01"}]}},
    {"passage_id": "BIO12O-CH06-P01", "subtopic_id": "BIO12-CH06-ST99", "confidence": "high", "note": ""},
    {"item_id": "x", "step": "A5", "input_data": {"subtopics": [{"id": "BIO12-CH06-ST01"}]}},
)

FIXTURES["A6"] = (
    [
        {"old_passage_id": "O1", "new_passage_id": "L1", "similarity": 1.0, "result": "pair", "adjudicated": False},
        {"old_passage_id": "O2", "new_passage_id": None, "similarity": 0.0, "result": "removed", "adjudicated": False},
        {"old_passage_id": None, "new_passage_id": "L2", "similarity": 0.0, "result": "added", "adjudicated": False},
    ],
    {"item_id": "BIO12-CH06", "step": "A6"},
    [
        {"old_passage_id": "O1", "new_passage_id": "L1", "similarity": 1.0, "result": "removed", "adjudicated": False},
    ],
    {"item_id": "BIO12-CH06", "step": "A6"},
)

FIXTURES["A7"] = (
    {"pair": ["O1", "L1"], "identical": False, "diff": [{"old": "20", "new": "13.8"}]},
    {"item_id": "BIO12-CH06", "step": "A7"},
    {"pair": ["O1", "L1"], "identical": False, "diff": []},
    {"item_id": "BIO12-CH06", "step": "A7"},
)

FIXTURES["A8"] = (
    {"change_type": "fact_changed", "old_fact": "20 billion years", "new_fact": "13.8 billion years",
     "could_flip_an_answer": True, "why": "the number changed", "confidence": "high"},
    {"item_id": "x", "step": "A8"},
    {"change_type": "fact_changed", "old_fact": "20 billion years", "new_fact": "20 billion years",
     "could_flip_an_answer": True, "why": "the number changed", "confidence": "high"},
    {"item_id": "x", "step": "A8"},
)

FIXTURES["A9"] = (
    {"change_log_rows": [
        {"change_id": "CL-0001", "chapter_id": "BIO12-CH06", "old_passage_id": "O1", "new_passage_id": "L1",
         "change_type": "fact_changed", "old_fact": "a", "new_fact": "b", "could_flip_an_answer": True,
         "old_text": "a", "new_text": "b", "affected_questions": [], "approval": "pending"},
    ], "deleted_topics_rows": []},
    {"item_id": "BIO12-CH06", "step": "A9", "expected_diff_count": None, "expected_removed_passage_ids": None},
    {"change_log_rows": [
        {"change_id": "CL-0001", "chapter_id": "BIO12-CH06", "old_passage_id": "O1", "new_passage_id": "L1",
         "change_type": "fact_changed", "old_fact": "a", "new_fact": "b", "could_flip_an_answer": True,
         "old_text": "a", "new_text": "b", "affected_questions": [], "approval": "pending"},
        {"change_id": "CL-0001", "chapter_id": "BIO12-CH06", "old_passage_id": "O2", "new_passage_id": "L2",
         "change_type": "fact_changed", "old_fact": "c", "new_fact": "d", "could_flip_an_answer": True,
         "old_text": "c", "new_text": "d", "affected_questions": [], "approval": "pending"},
    ], "deleted_topics_rows": []},  # duplicate change_id
    {"item_id": "BIO12-CH06", "step": "A9", "expected_diff_count": None, "expected_removed_passage_ids": None},
)


def main():
    steps = ["S0"] + [f"A{i}" for i in range(1, 10)]
    steps[steps.index("A2") + 1:steps.index("A2") + 1] = []  # no-op, A2S inserted explicitly below
    steps = ["S0", "A1", "A2", "A2S", "A3", "A4", "A5", "A6", "A7", "A8", "A9"]
    assert len(steps) == 11, steps

    for step in steps:
        module = rc.load_check_module(step)
        assert hasattr(module, "check"), f"{step}: no check() function"
        assert step in FIXTURES, f"{step}: no fixture registered in this test"

        data_pass, ctx_pass, data_fail, ctx_fail = FIXTURES[step]

        ok, msg = module.check(data_pass, ctx_pass)
        assert isinstance(ok, bool) and isinstance(msg, str), f"{step}: check() must return (bool, str), got {(ok, msg)!r}"
        assert ok is True, f"{step}: expected the PASS fixture to pass, got ({ok}, {msg!r})"

        ok2, msg2 = module.check(data_fail, ctx_fail)
        assert isinstance(ok2, bool) and isinstance(msg2, str)
        assert ok2 is False, f"{step}: expected the FAIL fixture to fail, got ({ok2}, {msg2!r})"

        print(f"{step}: OK (pass-fixture -> {ok}, fail-fixture -> {ok2} {msg2!r})")

    print("tests/test_checks_fixtures.py: ALL OK (11/11 check modules)")


if __name__ == "__main__":
    main()
