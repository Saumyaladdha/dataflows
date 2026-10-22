"""Raises flags for a person to look at in Stage F, in the exact JSON shape of spec 5.6."""
import datetime

from . import ids
from . import io as lib_io

SEVERITIES = {"blocker", "high", "normal", "low"}

FLAGS_PATH = lib_io.project_path("flags", "flags.jsonl")


def _now_iso():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def _open_flag_for(flags_path, item_type, item_id, step, code):
    """An already-OPEN flag for the same condition, or None.

    A flag identifies a CONDITION on an item, not an occurrence of noticing it. Re-running a step
    whose condition still holds must not mint a second flag for the same thing.
    """
    path = flags_path or FLAGS_PATH
    try:
        rows = lib_io.read_jsonl(path)
    except (OSError, ValueError):
        return None
    for row in rows:
        if (row.get("status") == "open"
                and row.get("item_type") == item_type
                and row.get("item_id") == item_id
                and row.get("step") == step
                and row.get("code") == code):
            return row
    return None


def raise_flag(item_type, item_id, step, code, severity, message,
                provisional_value=None, evidence=None, prompt_version=None,
                flags_path=None):
    """Build one flag record in the exact shape of spec 5.6 (minting its flag_id via ids.py) and
    append it to flags/flags.jsonl. Returns the flag dict that was written.

    IDEMPOTENT per condition. If an OPEN flag already exists for the same
    (item_type, item_id, step, code), that flag is returned unchanged and nothing is appended.

    Why this matters, measured on the real flag store before the fix: 2,371 rows represented only
    1,114 distinct conditions -- 1,257 rows were exact duplicates, identical apart from `flag_id`
    and `created_at`. One condition had been re-raised ELEVEN times (every B5 run re-flagged
    `NEET-2017-MAIN-W-key` for the same missing booklet code). Two concrete harms: spec 14/F1
    builds the reviewer's queue from open flags, so a person would have been handed 2,371 items for
    1,114 real decisions; and `open_flags` is a column of `review/releases.csv`, so the release
    gate was counting noise. Neither is a judgement call, which is why this is fixed in code rather
    than left for a reviewer.

    Deliberately NOT done here: updating the existing flag's message or severity. The condition is
    the same, the first observation is the one with the earliest `created_at`, and silently
    rewriting a flag a reviewer may already be looking at would be worse than leaving it. A step
    whose finding genuinely changed should use a different code.
    """
    if severity not in SEVERITIES:
        raise ValueError(f"invalid severity {severity!r}; must be one of {sorted(SEVERITIES)}")

    existing = _open_flag_for(flags_path, item_type, item_id, step, code)
    if existing is not None:
        return existing

    flag = {
        "flag_id": ids.next_flag_id(),
        "item_type": item_type,
        "item_id": item_id,
        "step": step,
        "code": code,
        "severity": severity,
        "message": message,
        "provisional_value": provisional_value,
        "evidence": evidence or [],
        "prompt_version": prompt_version,
        "created_at": _now_iso(),
        "status": "open",
        "decision": None,
        "reviewer": None,
        "decided_at": None,
    }
    lib_io.append_jsonl(flags_path or FLAGS_PATH, flag)
    return flag


if __name__ == "__main__":
    import json
    import os
    import shutil
    import tempfile

    tmp_dir = tempfile.mkdtemp(prefix="flags_selfcheck_")
    orig_counters_path = ids.COUNTERS_PATH
    ids.COUNTERS_PATH = os.path.join(tmp_dir, "counters.json")  # isolate from real register/
    try:
        path = os.path.join(tmp_dir, "flags.jsonl")
        flag = raise_flag(
            item_type="question", item_id="Q-000123", step="D1",
            code="D1_ADJUDICATED", severity="normal",
            message="Run A: BIO11-CH10; run B: unsure; adjudicator chose BIO11-CH10.",
            provisional_value={"chapter_ids": ["BIO11-CH10"]},
            evidence=["steps/D1/out/Q-000123.runA.json"],
            prompt_version="v1", flags_path=path,
        )
        assert flag["status"] == "open"
        assert flag["decision"] is None and flag["reviewer"] is None and flag["decided_at"] is None
        assert flag["flag_id"].startswith("FL-")

        lines = [json.loads(l) for l in open(path)]
        assert len(lines) == 1 and lines[0]["flag_id"] == flag["flag_id"]

        try:
            raise_flag("question", "Q-1", "D1", "X", "catastrophic", "bad severity", flags_path=path)
            raise AssertionError("expected ValueError for invalid severity")
        except ValueError:
            pass

        print("flags.py self-check OK:", flag["flag_id"], flag["created_at"])
    finally:
        ids.COUNTERS_PATH = orig_counters_path
        shutil.rmtree(tmp_dir)
