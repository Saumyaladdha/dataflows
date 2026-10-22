#!/usr/bin/env python3
"""The heart of the pipeline (spec 5.1). Usage:

    python3 scripts/run_step.py <STEP> --list   [--chapters X,Y] [--papers X,Y] [--items X,Y]
    python3 scripts/run_step.py <STEP> --check  [--chapters X,Y] [--papers X,Y] [--items X,Y]
    python3 scripts/run_step.py <STEP> --auto   [--chapters X,Y] [--papers X,Y] [--items X,Y]

--list   prints one line per item needing this step (agent-driven/hybrid steps only), in the
         exact format spec 5.1 requires: "item_id | agent | input_path | output_path | run_label".
         For a script-only step it prints an explanatory message instead of erroring.
--check  validates every new agent output against schemas/<STEP>.json, runs
         scripts/checks/<STEP>.py, applies the fallback chain (config/steps.yaml), writes
         status/flags/run_log rows, and either prints a NEW --list-style output (work still
         needed: retries, second runs, adjudications, or items dispatched but not yet answered)
         or prints DONE.
--auto   for script-only/hybrid steps, invokes the step's real script per
         scripts/CONVENTIONS.md, then runs the same --check logic.

This file is deliberately thin: all per-step logic lives in scripts/step_plugins.py; this file is
just argument parsing + the three generic verbs.
"""
import argparse
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402
import step_plugins as sp  # noqa: E402


def build_filters(args):
    return {
        "chapters": rc.parse_filter_list(args.chapters),
        "papers": rc.parse_filter_list(args.papers),
        "items": rc.parse_filter_list(args.items),
    }


def print_lines(lines):
    for ll in lines:
        print(sp.format_list_line(ll))


def cmd_list(step, plugin, cfg, filters):
    kind = rc.step_kind(cfg)
    # "people" joins script/hybrid here so F2's explanation goes to STDOUT like any other
    # "nothing for the runner to list" message, rather than to stderr as if nothing had happened.
    if kind in ("script", "hybrid", "people"):
        lines = plugin.list_items(filters) if hasattr(plugin, "list_items") else []
        if lines:
            print_lines(lines)
        else:
            reason = plugin.list_reason() if hasattr(plugin, "list_reason") else \
                f"{step} is a script-only step; nothing to list. Run `run_step.py {step} --auto`."
            print(f"# {reason}")
        return
    # pure agent-driven step
    lines = plugin.list_items(filters)
    if lines:
        print_lines(lines)
    else:
        reason = plugin.list_reason() if hasattr(plugin, "list_reason") else "nothing needs this step right now."
        print(f"# {reason}", file=sys.stderr)


def cmd_check(step, plugin, cfg, filters):
    new_lines = plugin.check(filters)
    if not new_lines and hasattr(plugin, "list_items"):
        # Nothing newly resolved this round; items dispatched-but-not-yet-answered (or never
        # dispatched at all) still count as "work still needed" per spec 5.1's --check contract.
        new_lines = plugin.list_items(filters)
    if new_lines:
        print_lines(new_lines)
    else:
        print("DONE")


def cmd_auto(step, plugin, cfg, filters):
    kind = rc.step_kind(cfg)
    if kind == "people":
        # Spec 14/F2: this step is done by PEOPLE. There is no agent and no script, so --auto has
        # nothing truthful to do; say what actually happens instead of reporting a missing
        # headless-subagent facility that was never going to be used here.
        reason = plugin.list_reason() if hasattr(plugin, "list_reason") else \
            f"{step} is done by people (steps.yaml agent={cfg.get('agent')!r}); there is nothing to run."
        print(f"run_step.py {step} --auto: {reason}", file=sys.stderr)
        sys.exit(2)
    if not hasattr(plugin, "auto"):
        print(
            f"run_step.py {step} --auto: this is an agent-driven step with no script-only half "
            f"(steps.yaml agent={cfg.get('agent')!r}). Headless subagent invocation (spec 5.2) "
            f"is not implemented in this build environment (scripts/lib/agents.py::call_headless "
            f"raises NotImplementedError — the `claude` CLI isn't on PATH here; see "
            f"docs/OPEN_QUESTIONS.md). Use the interactive flow instead: `--list`, invoke the "
            f"named subagent for each line, then `--check`.",
            file=sys.stderr,
        )
        sys.exit(2)
    plugin.auto(filters)
    cmd_check(step, plugin, cfg, filters)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run one pipeline step (spec 5.1).")
    parser.add_argument("step", help="Step code, e.g. A1, A2S, S0.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--list", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--auto", action="store_true")
    parser.add_argument("--chapters", help="Comma-separated chapter ids to scope to.")
    parser.add_argument("--papers", help="Comma-separated paper ids to scope to.")
    parser.add_argument("--items", help="Comma-separated item ids (substring match) to scope to.")
    args = parser.parse_args(argv)

    step = args.step
    cfg = rc.get_step_cfg(step)
    plugins = sp.get_plugins()
    if step not in plugins:
        print(
            f"run_step.py: step {step!r} is recognised in config/steps.yaml but "
            f"scripts/step_plugins.py has no plugin for it. Every step the config declares "
            f"(S0, A1-A9, B1-B9, C1, D1-D11, E0-E6, F1-F6) has one, so this means a step entry "
            f"was added to the YAML without its plugin: add one to step_plugins.get_plugins().",
            file=sys.stderr,
        )
        sys.exit(2)
    plugin = plugins[step]
    filters = build_filters(args)

    if args.list:
        cmd_list(step, plugin, cfg, filters)
    elif args.check:
        cmd_check(step, plugin, cfg, filters)
    elif args.auto:
        cmd_auto(step, plugin, cfg, filters)


if __name__ == "__main__":
    main()
