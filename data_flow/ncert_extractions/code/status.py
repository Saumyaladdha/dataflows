#!/usr/bin/env python3
"""scripts/status.py: the status-reporting CLI (spec Section 19's report format), run as
`python3 scripts/status.py [--step STEP]`.

Naming note (M2 build): this file is named status.py to match .claude/commands/status.md's
`python scripts/status.py $ARGUMENTS` and spec Appendix C, even though scripts/lib/status.py
(the item-status constants/writer module) also exists. These never actually collide in Python:
this file is always executed as __main__ (`python3 scripts/status.py ...`) and, when imported by
anything else, is reached only via its full path/qualified import, never a bare `import status`;
every reference to the lib module below is the qualified `from lib import status as lib_status`.
If this ever needs to be imported as a module (e.g. by a test) rather than exec'd as a script, do
`import importlib.util; ...` from its file path (see tests/test_run_step.py) rather than a bare
`import status`, to keep that guarantee.
"""
import argparse
import collections
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402
from lib import io as lib_io  # noqa: E402
from lib import status as lib_status  # noqa: E402

_SEVERITY_ORDER = {"blocker": 0, "high": 1, "normal": 2, "low": 3}


def _steps_present():
    steps_dir = rc.pp("steps")
    if not os.path.isdir(steps_dir):
        return []
    return sorted(d for d in os.listdir(steps_dir) if os.path.isdir(os.path.join(steps_dir, d)))


def collect_status_counts(step_filter=None):
    """Returns (counts: {status: n}, blocked: [(step, item_id, message), ...])."""
    counts = collections.Counter()
    blocked = []
    for step in _steps_present():
        if step_filter and step != step_filter:
            continue
        status_dir = rc.pp("steps", step, "status")
        if not os.path.isdir(status_dir):
            continue
        # Recognise a status file by its CONTENT, not by its name.
        #
        # This used to blacklist `.pending.json` and `.last_block.json` and index `rec["status"]`
        # directly, which made the whole report crash with KeyError the moment a step introduced a
        # side-car shape the list did not name. Two had: B2 writes `<ITEM>.last_q.json` (413 of
        # them) and B6 writes an aggregate `_paper_stats.json`, so `status.py` could not run at
        # all. f_common.iter_step_statuses already settled the rule -- a side-car is anything with
        # no `status` key -- and this now matches it, so the next side-car costs nothing here.
        for fn in sorted(os.listdir(status_dir)):
            if not fn.endswith(".json"):
                continue
            item_id = fn[: -len(".json")]
            rec = lib_status.read_status(step, item_id)
            if not isinstance(rec, dict) or "status" not in rec:
                continue
            counts[rec["status"]] += 1
            if rec["status"] == lib_status.BLOCKED:
                blocked.append((step, item_id, rec.get("check_message", "")))
    return counts, blocked


def collect_open_flags(step_filter=None):
    flags_path = rc.pp("flags", "flags.jsonl")
    by_sev_code = collections.Counter()
    for flag in lib_io.read_jsonl(flags_path):
        if flag.get("status") != "open":
            continue
        if step_filter and flag.get("step") != step_filter:
            continue
        by_sev_code[(flag.get("severity", "normal"), flag.get("code", "UNKNOWN"))] += 1
    return by_sev_code


def main(argv=None):
    parser = argparse.ArgumentParser(description="Pipeline status summary (spec Section 19).")
    parser.add_argument("--step", help="Restrict to one step code.")
    args = parser.parse_args(argv)

    counts, blocked = collect_status_counts(args.step)
    by_sev_code = collect_open_flags(args.step)

    scope = f"--step {args.step}" if args.step else "all steps"
    print(f"# Status ({scope})")
    print()
    print("## Counts by status")
    for status in (lib_status.PASS, lib_status.FLAGGED, lib_status.BLOCKED, lib_status.SKIPPED, lib_status.STALE):
        print(f"  {status}: {counts.get(status, 0)}")
    total = sum(counts.values())
    print(f"  total: {total}")
    print()

    print("## New flags by severity and code (top 10)")
    ranked = sorted(by_sev_code.items(), key=lambda kv: (_SEVERITY_ORDER.get(kv[0][0], 9), -kv[1]))
    if not ranked:
        print("  (none open)")
    for (severity, code), n in ranked[:10]:
        print(f"  {severity:8s} {code}: {n}")
    if len(ranked) > 10:
        print(f"  ...and {len(ranked) - 10} more (severity, code) pairs")
    print()

    print(f"## Blocked items ({len(blocked)})")
    for step, item_id, msg in blocked[:20]:
        print(f"  {step} {item_id}: {msg}")
    if len(blocked) > 20:
        print(f"  ...and {len(blocked) - 20} more")


if __name__ == "__main__":
    main()
