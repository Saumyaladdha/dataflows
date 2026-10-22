"""Item status constants and the rule for computing an item's overall status across its steps
(spec 5.4), plus reading/writing steps/<STEP>/status/<ITEM>.json.
"""
import json
import os

from . import io as lib_io

PASS = "pass"
FLAGGED = "flagged"
BLOCKED = "blocked"
SKIPPED = "skipped"
STALE = "stale"

ALL_STATUSES = {PASS, FLAGGED, BLOCKED, SKIPPED, STALE}

# "An item's overall status is the worst across its steps: blocked > flagged > pass" (5.4).
# stale and skipped aren't named in that ordering; 5.4/5.9 describe stale as "cleared by the
# cascade; must re-run" (a value is known-invalid until the step is redone) and skipped as
# "the step does not apply" (a neutral, not-bad outcome, same as a clean pass for gating
# purposes). So: blocked (nothing continues) outranks stale (known-invalid, pending a re-run)
# outranks flagged (usable but needs a human look) outranks pass/skipped (both fine to continue
# from). Between pass and skipped, pass ranks slightly above skipped only so that an item with a
# mix of passed and skipped steps reports "pass" rather than "skipped" — but an item whose steps
# are *all* skipped correctly reports "skipped" overall, since nothing applicable actually ran.
_RANK = {BLOCKED: 4, STALE: 3, FLAGGED: 2, PASS: 1, SKIPPED: 0}


def overall_status(statuses):
    """Compute one item's overall status as the worst across a list of per-step statuses, per
    spec 5.4: blocked > stale > flagged > pass > skipped. Returns SKIPPED if given no statuses."""
    if not statuses:
        return SKIPPED
    for s in statuses:
        if s not in ALL_STATUSES:
            raise ValueError(f"unknown status {s!r}; expected one of {sorted(ALL_STATUSES)}")
    return max(statuses, key=lambda s: _RANK[s])


def status_path(step, item_id, project_root=None):
    """Return the path for one item's status file under a step: steps/<STEP>/status/<ITEM>.json."""
    root = project_root or lib_io.PROJECT_ROOT
    return os.path.join(root, "steps", step, "status", f"{item_id}.json")


def write_status(step, item_id, status, extra=None, project_root=None):
    """Write one item's status JSON for a step, atomically. `extra` can carry additional fields
    (e.g. check message, run label) alongside the required status."""
    if status not in ALL_STATUSES:
        raise ValueError(f"unknown status {status!r}; expected one of {sorted(ALL_STATUSES)}")
    payload = {"item_id": item_id, "step": step, "status": status}
    if extra:
        payload.update(extra)
    lib_io.atomic_write_json(status_path(step, item_id, project_root), payload)
    return payload


def read_status(step, item_id, project_root=None):
    """Return one item's status JSON for a step as a dict, or None if it has no status yet."""
    path = status_path(step, item_id, project_root)
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    import shutil
    import tempfile

    assert overall_status([PASS, PASS]) == PASS
    assert overall_status([PASS, FLAGGED]) == FLAGGED
    assert overall_status([PASS, FLAGGED, BLOCKED]) == BLOCKED
    assert overall_status([PASS, SKIPPED]) == PASS
    assert overall_status([SKIPPED, SKIPPED]) == SKIPPED
    assert overall_status([STALE, PASS]) == STALE
    assert overall_status([STALE, BLOCKED]) == BLOCKED
    assert overall_status([STALE, FLAGGED]) == STALE
    assert overall_status([]) == SKIPPED

    tmp_root = tempfile.mkdtemp(prefix="status_selfcheck_")
    try:
        write_status("D1", "Q-000123", FLAGGED, extra={"check_message": "weak match"},
                     project_root=tmp_root)
        got = read_status("D1", "Q-000123", project_root=tmp_root)
        assert got["status"] == FLAGGED and got["check_message"] == "weak match"
        assert read_status("D1", "Q-999999", project_root=tmp_root) is None

        try:
            write_status("D1", "Q-1", "not_a_status", project_root=tmp_root)
            raise AssertionError("expected ValueError")
        except ValueError:
            pass

        print("status.py self-check OK:", got)
    finally:
        shutil.rmtree(tmp_root)
