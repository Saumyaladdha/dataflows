#!/usr/bin/env python3
"""Stage E's single reader for `config/allowed_values.yaml`.

    python3 scripts/tag_values.py --list                 # every E-relevant list and its size
    python3 scripts/tag_values.py --list question_type   # one list
    python3 scripts/tag_values.py --audit-schemas        # schemas/E*.json enums vs this file

WHY THIS FILE EXISTS. Spec 17 is explicit that `config/allowed_values.yaml` is the value list and
that "a new value is added only after Stage F names it". Stage E has six tags and seven check
modules; if each of them typed its own copy of a 20-to-29-value list, the lists would drift and a
value invented in a check would be indistinguishable from a real one. Everything in Stage E that
needs an allowed value reads it from here, and here reads it from the YAML.

NOTHING IN THIS FILE MAY ADD, RENAME OR REMOVE A VALUE. `config/allowed_values.yaml` is the
owner's file; this module only reads it. The two genuine taxonomy gaps found on real data
(`list_of_reactions` for E1, a reaction value for `answer_form` -- see codebook/E1.md §4 and
codebook/E6.md §5) are deliberately NOT patched in here: a check that quietly accepted a value the
owner never approved would hide the gap instead of surfacing it.

`--audit-schemas` is the mechanism that keeps the seven `schemas/E*.json` files honest: it reports
any enum in a schema that is not exactly its list in the YAML, in either direction. tests/
test_e_checks.py runs it, so an invented enum value fails the test suite rather than reaching data.
"""
import argparse
import json
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import yaml  # noqa: E402

import runner_core as rc  # noqa: E402

_CACHE = {}


def load(force_reload=False):
    """The whole parsed `config/allowed_values.yaml`."""
    if force_reload or "raw" not in _CACHE:
        with open(rc.pp("config", "allowed_values.yaml"), "r", encoding="utf-8") as f:
            _CACHE["raw"] = yaml.safe_load(f)
    return _CACHE["raw"]


def version():
    return str(load().get("version") or "unknown")


def _as_list(node):
    """A YAML list stays a list; a mapping of value -> one-line definition yields its keys.

    `allowed_values.yaml` stores some lists both ways on purpose -- `question_type` and `format`
    carry their one-line definitions as mapping values, `content_shape` and `trap` are bare
    lists -- so every consumer here would otherwise have to know which is which."""
    if isinstance(node, dict):
        return list(node.keys())
    if isinstance(node, list):
        return [str(v) for v in node]
    return []


#: E4's axis is THREE keys since allowed_values.yaml v0.3. Callers that still ask for one `thinking`
#: list get their union, in rulebook order: demand, then structure, then strategy.
THINKING_KEYS = ("cognitive_demand", "solution_structure", "strategy_available")


def values(name):
    """The allowed values for one list name, in the YAML's own order."""
    av = load()
    if name == "thinking":
        # WAS `thinking_draft` -- the eight draft categories of spec 13.0/17.5, which conflated
        # three questions: what thinking is needed, how many dependent steps, and what shortcut
        # exists. That is why one question could be `check_each_statement` while having a one-pair
        # shortcut. docs/question_categories/RULEBOOK.md section 4 split them, and
        # scripts/build_allowed_values.py writes the three keys. Callers asking for one list get the
        # union, which is what schemas/E4.json's `primary`/`secondary` enums hold.
        out = []
        for key in THINKING_KEYS:
            if key not in av:
                raise KeyError(
                    f"config/allowed_values.yaml has no list named {key!r}. E4's axis is three keys "
                    f"since v0.3 ({', '.join(THINKING_KEYS)}); regenerate with "
                    f"`python3 scripts/build_allowed_values.py --apply`.")
            out += _as_list(av[key])
        return out
    if name not in av:
        raise KeyError(f"config/allowed_values.yaml has no list named {name!r}")
    return _as_list(av[name])


def definitions(name):
    """{value: one-line definition} where the YAML carries definitions, else {} -- this is what
    spec 13.0 means by "the allowed values with their one-line definitions" in an agent input."""
    av = load()
    if name == "thinking":
        # the three v0.3 keys are bare lists, so E4 carries no inline definitions any more; its
        # guidance lives in codebook/E4.md and docs/question_categories/RULEBOOK.md section 4
        return {}
    node = av.get(name)
    return {str(k): str(v) for k, v in node.items()} if isinstance(node, dict) else {}


def branches(subject):
    """Allowed branches for one subject, or [] when the taxonomy defines none (Physics).

    REAL TAXONOMY GAP, reported not fixed (docs/OPEN_QUESTIONS.md 2026-10-12): the YAML defines
    Biology branches (botany/zoology) but no step ever assigns them -- B7 is the CHEM branch
    sorter and its own allowed set is physical/organic/inorganic/unsure -- so every Biology record
    reads `unsure`, meaning "no step ever tried" rather than "a step tried and failed". E4's
    branch rule (codebook/E4.md §1) only concerns Chemistry, so E4 is correct either way, but
    scripts/checks/E4.py says so out loud rather than letting the silence pass."""
    node = (load().get("branch") or {})
    return _as_list(node.get(subject)) if isinstance(node, dict) else []


# E-stage lists, by the field name each tag actually writes. The keys are what
# scripts/checks/E*.py and tests/test_e_checks.py ask for.
E_FIELD_LISTS = {
    "question_type": "question_type",      # E1
    "format": "format",                    # E2
    "content_shape": "content_shape",      # E3
    "thinking": "thinking",                # E4 (-> the three v0.3 sub-axis keys, unioned)
    "trap": "trap",                        # E5
    "stem_context": "stem_context",        # E6 (agent; `unsure` added -- see below)
    "answer_form": "answer_form",          # E6 (script)
    "negation": "negation",                # E6 (script)
    "figure_role": "figure_role",          # E6 (script)
    "confidence": "confidence",            # every E agent
}

# `unsure` is not in the YAML's `stem_context` list, but Universal rule 5 and
# .claude/agents/e6-context-tagger.md's own allowed list both name it, and spec 16 gives it a
# flag (E6_CONTEXT_UNSURE, low). It is an "I could not decide" marker, not a category, which is
# why it belongs in the agent's output schema and not in the owner's category list. Kept here,
# beside the reason, rather than hidden inside schemas/E6.json.
STEM_CONTEXT_UNSURE = "unsure"


# E4's `branch_used` (schemas/E4.json) is not a tag value -- it records which branch the agent
# actually conditioned on, so a branch-blind Chemistry tagging cannot pass silently
# (codebook/E4.md §1). Its enum is every branch config/allowed_values.yaml defines, for every
# subject, plus the two markers the real pipeline produces: B7's own "unsure" (schemas/B7.json)
# and "none" for a record whose `branch` is null, as every Physics record's is.
BRANCH_MARKERS = ["unsure", "none"]


def all_branches():
    node = (load().get("branch") or {})
    out = []
    for subject in sorted(node):
        for b in _as_list(node[subject]):
            if b not in out:
                out.append(b)
    return out


def schema_enum(field):
    """Exactly the enum `schemas/E*.json` must carry for one E field."""
    if field == "branch_used":
        return all_branches() + BRANCH_MARKERS
    vals = list(values(E_FIELD_LISTS[field]))
    if field == "stem_context":
        vals.append(STEM_CONTEXT_UNSURE)
    return vals


# ---------------------------------------------------------------------------
# schemas/E*.json audit -- the guard against an invented enum value
# ---------------------------------------------------------------------------

# {step: {json-pointer-ish path inside the schema: E field name}}
SCHEMA_ENUM_SITES = {
    "E1": {"question_type": "question_type", "confidence": "confidence"},
    "E2": {"format": "format", "confidence": "confidence"},
    "E3": {"content_shape": "content_shape", "confidence": "confidence"},
    "E4": {"primary": "thinking", "secondary": "thinking", "confidence": "confidence",
            "branch_used": "branch_used"},
    "E5": {"trap": "trap", "confidence": "confidence"},
    "E6": {"stem_context": "stem_context", "confidence": "confidence"},
}


def _collect_enums(node, out, key=None):
    """Every {"enum": [...]} in a schema, keyed by the property name it sits under."""
    if isinstance(node, dict):
        if "enum" in node and isinstance(node["enum"], list) and key:
            out.setdefault(key, []).append([v for v in node["enum"] if v is not None])
        for k, v in node.items():
            _collect_enums(v, out, k if k not in ("properties", "items", "oneOf", "anyOf") else key)
    elif isinstance(node, list):
        for v in node:
            _collect_enums(v, out, key)
    return out


def audit_schemas():
    """Returns a list of problem strings; empty means every E schema enum matches the YAML."""
    problems = []
    for step, sites in SCHEMA_ENUM_SITES.items():
        path = rc.pp("schemas", f"{step}.json")
        if not os.path.exists(path):
            problems.append(f"{step}: schemas/{step}.json does not exist")
            continue
        with open(path, "r", encoding="utf-8") as f:
            schema = json.load(f)
        found = _collect_enums(schema, {})
        for prop, field in sites.items():
            expected = schema_enum(field)
            list_name = E_FIELD_LISTS.get(field, field)
            if prop not in found:
                problems.append(f"{step}: no enum found for property {prop!r}")
                continue
            for actual in found[prop]:
                extra = [v for v in actual if v not in expected]
                missing = [v for v in expected if v not in actual]
                if extra:
                    problems.append(
                        f"{step}.{prop}: {extra} are NOT in config/allowed_values.yaml's "
                        f"{list_name} list -- never invent an allowed value")
                if missing:
                    problems.append(
                        f"{step}.{prop}: missing {missing} from config/allowed_values.yaml's "
                        f"{list_name} list")
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description="Stage E's reader for config/allowed_values.yaml.")
    ap.add_argument("--list", nargs="?", const="*", metavar="NAME",
                    help="Print one list, or every E-relevant list with its size.")
    ap.add_argument("--audit-schemas", action="store_true",
                    help="Check every schemas/E*.json enum against config/allowed_values.yaml.")
    args = ap.parse_args(argv)

    if args.audit_schemas:
        problems = audit_schemas()
        for p in problems:
            print(f"PROBLEM  {p}")
        print(f"\n{len(problems)} problem(s); allowed_values.yaml {version()}")
        return 1 if problems else 0

    if args.list:
        if args.list == "*":
            for field, name in E_FIELD_LISTS.items():
                vals = schema_enum(field) if field == "stem_context" else values(name)
                print(f"{field:<16} {len(vals):>3}  {', '.join(vals)}")
            print(f"\nconfig/allowed_values.yaml {version()}")
        else:
            for v in values(args.list):
                print(v)
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
