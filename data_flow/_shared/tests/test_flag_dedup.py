#!/usr/bin/env python3
"""Pins that `lib.flags.raise_flag` is idempotent per CONDITION, added 2026-10-13.

A flag identifies a condition on an item, not an occurrence of noticing it. Re-running a step
whose condition still holds must not mint a second flag for the same thing.

Measured on the real flag store before the fix: **2,371 rows represented only 1,114 distinct
conditions** -- 1,253 rows were exact duplicates, identical apart from `flag_id` and `created_at`.
One condition had been raised ELEVEN times: every B5 run re-flagged `NEET-2017-MAIN-W-key` for the
same missing booklet code.

Two concrete harms, which is why this is code and not a reviewer's problem:
  * spec 14/F1 builds the reviewer's queue from open flags, so a person would have been handed
    2,371 items for 1,114 real decisions;
  * `open_flags` is a column of `review/releases.csv`, so the release gate was counting noise.

Run: .venv/bin/python3 -m pytest tests/test_flag_dedup.py -q
"""
import json
import os
import sys
import tempfile

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_TESTS_DIR)
_SCRIPTS_DIR = os.path.join(_PROJECT_ROOT, "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from lib import flags as lib_flags  # noqa: E402
from lib import ids as lib_ids  # noqa: E402


def _isolated():
    """A temp flag file and counter, so the real register/ and flags/ are never touched."""
    d = tempfile.mkdtemp(prefix="flag_dedup_")
    lib_ids.COUNTERS_PATH = os.path.join(d, "counters.json")
    return os.path.join(d, "flags.jsonl")


def _rows(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(ln) for ln in fh if ln.strip()]


def test_same_condition_raised_twice_writes_one_row():
    p = _isolated()
    a = lib_flags.raise_flag("item", "NEET-2017-MAIN-W-key", "B5", "B5_KEY_ROW_MISSING",
                             "blocker", "booklet_code is empty", flags_path=p)
    b = lib_flags.raise_flag("item", "NEET-2017-MAIN-W-key", "B5", "B5_KEY_ROW_MISSING",
                             "blocker", "booklet_code is empty (seen again)", flags_path=p)
    assert len(_rows(p)) == 1
    assert a["flag_id"] == b["flag_id"], "the existing flag must be returned, not a new one"


def test_first_observation_is_the_one_kept():
    """Deliberately NOT updating the message: a reviewer may already be reading it, and the
    earliest observation is the one with the honest `created_at`."""
    p = _isolated()
    lib_flags.raise_flag("item", "X-1", "B5", "B5_KEY_ROW_MISSING", "blocker", "first",
                         flags_path=p)
    lib_flags.raise_flag("item", "X-1", "B5", "B5_KEY_ROW_MISSING", "blocker", "second",
                         flags_path=p)
    assert _rows(p)[0]["message"] == "first"


def test_a_different_code_on_the_same_item_is_a_different_condition():
    p = _isolated()
    lib_flags.raise_flag("item", "X-1", "B5", "B5_KEY_ROW_MISSING", "blocker", "m", flags_path=p)
    lib_flags.raise_flag("item", "X-1", "B5", "B5_UNRECOGNISED_MARK", "high", "m", flags_path=p)
    assert len(_rows(p)) == 2


def test_the_same_code_on_a_different_item_is_a_different_condition():
    p = _isolated()
    lib_flags.raise_flag("item", "X-1", "B5", "B5_KEY_ROW_MISSING", "blocker", "m", flags_path=p)
    lib_flags.raise_flag("item", "X-2", "B5", "B5_KEY_ROW_MISSING", "blocker", "m", flags_path=p)
    assert len(_rows(p)) == 2


def test_the_same_code_from_a_different_step_is_a_different_condition():
    p = _isolated()
    lib_flags.raise_flag("item", "X-1", "B5", "SHARED_CODE", "normal", "m", flags_path=p)
    lib_flags.raise_flag("item", "X-1", "B6", "SHARED_CODE", "normal", "m", flags_path=p)
    assert len(_rows(p)) == 2


def test_a_closed_flag_does_not_suppress_a_new_one():
    """Dedup keys on OPEN flags only. If a reviewer closed a flag and the condition recurs, that
    is new information and must be raised again -- otherwise a resolved-then-regressed defect
    would go unreported forever."""
    p = _isolated()
    first = lib_flags.raise_flag("item", "X-1", "B5", "B5_KEY_ROW_MISSING", "blocker", "m",
                                 flags_path=p)
    rows = _rows(p)
    rows[0]["status"] = "closed"
    with open(p, "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")
    second = lib_flags.raise_flag("item", "X-1", "B5", "B5_KEY_ROW_MISSING", "blocker", "again",
                                  flags_path=p)
    assert len(_rows(p)) == 2
    assert second["flag_id"] != first["flag_id"]


def test_real_store_has_no_duplicate_open_conditions():
    """The live store was compacted alongside this fix; guard against it drifting back.

    Four conditions legitimately keep two rows each: `review/queue.csv` already pointed at both
    siblings, and breaking a queue reference would be worse than the duplicate.
    """
    path = os.path.join(_PROJECT_ROOT, "flags", "flags.jsonl")
    if not os.path.exists(path):
        return
    import collections
    rows = _rows(path)
    counts = collections.Counter(
        (r.get("item_type"), r.get("item_id"), r.get("step"), r.get("code"))
        for r in rows if r.get("status") == "open")
    extra = sum(v - 1 for v in counts.values() if v > 1)
    assert extra <= 4, (
        f"{extra} redundant open flag rows in the real store (allowance is the 4 "
        f"queue-referenced siblings); raise_flag's dedup may have regressed")
