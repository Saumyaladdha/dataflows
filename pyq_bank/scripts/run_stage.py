#!/usr/bin/env python3
"""scripts/run_stage.py <STAGE> --plan (spec 5.11): prints the ordered list of steps in a stage
and whether each is agent-driven, script-only, hybrid or people, so /run-stage can drive
/run-step once per line in order. Stage order itself is just config/steps.yaml's file order
(the spec writes out Sections 8-14 in dependency order already, e.g. Stage A = A1->A2->A2S->
A3->A4->A5->A6->A7->A8->A9 — see spec 9's opening line — and PyYAML/py3.7+ dicts preserve file
order on load, so no separate topological sort is needed).

Usage: python3 scripts/run_stage.py <0|A|B|C|D|E|F> --plan
"""
import argparse
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402

def _implemented_steps():
    """Which steps the runner can actually drive -- asked of the runner itself, never listed here.

    This was a hard-coded set of the eleven Stage-0/A steps that existed when the file was
    written. It then silently went stale three times over: B1-B9, C1, D1-D11 and finally all of
    E and F were built and registered, yet `--plan` kept printing "[not yet implemented by
    run_step.py]" against 34 working steps -- telling an operator the opposite of the truth.
    Deriving it from `get_plugins()` means the answer cannot drift from reality again."""
    import step_plugins as sp
    return set(sp.get_plugins())


def kind_label(cfg):
    kind = rc.step_kind(cfg)
    if kind == "script":
        return "script-only"
    if kind == "people":
        return "people (Stage F)"
    if kind == "hybrid":
        return "hybrid (script + agent)"
    return f"agent-driven ({kind})"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Print the ordered step plan for one stage (spec 5.11).")
    parser.add_argument("stage", help="Stage code: 0, A, B, C, D, E, F, or 'smoke'.")
    parser.add_argument("--plan", action="store_true", required=True)
    # Accepted for compatibility with /run-stage's $ARGUMENTS passthrough; the plan itself
    # doesn't change per filter (filters apply when /run-step is actually invoked per step).
    parser.add_argument("--chapters")
    parser.add_argument("--papers")
    parser.add_argument("--items")
    args = parser.parse_args(argv)

    if args.stage.lower() == "smoke":
        print("# 'smoke' is the M4 fixture test flow, not a config/steps.yaml stage; "
              "see spec Section 7 M4. No step plan to print.")
        return

    cfg = rc.load_steps_config()
    rows = [(step, entry) for step, entry in cfg.items() if str(entry.get("stage")) == args.stage]
    if not rows:
        print(f"# No steps found with stage={args.stage!r} in config/steps.yaml.", file=sys.stderr)
        sys.exit(2)

    for step, entry in rows:
        implemented = "" if step in _implemented_steps() else "  [not yet implemented by run_step.py]"
        print(f"{step} | {kind_label(entry)} | {entry.get('agent')}{implemented}")


if __name__ == "__main__":
    main()
