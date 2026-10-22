#!/usr/bin/env python3
"""Generate the production category vocabulary from the rulebook, and record every predecessor.

    python3 scripts/build_allowed_values.py --dry-run
    python3 scripts/build_allowed_values.py --apply

THE PROBLEM THIS SOLVES
-----------------------
Three generations of category vocabulary existed at once, and only the oldest was executable:

  v0.2  config/allowed_values.yaml + schemas/E1-E5.json   <- what a live step may emit
  v1    exports/discovery/CATEGORIES.xlsx                 <- merged and renamed; 580 questions tagged
  v2    docs/question_categories/RULEBOOK.md              <- every definition, tie-break, evidence rule

Measured by `scripts/checks/category_label_census.py`, the gap was 59 rulebook labels that NO live
step could emit (30 of the 39 traps among them), 9 labels the rulebook had retired that a step could
still emit and have pass its check, and 45 allowed values the rulebook did not define.

So the trap taxonomy was unreachable from the pipeline that was supposed to apply it.

HOW THE MAPPING IS DERIVED, NOT TYPED
-------------------------------------
Nothing here is hand-written. Two documents already record the two hops:

  v0.2 -> v1   CATEGORIES.xlsx's `Status` column: "Renamed - was single_statement",
               "Merged - was formula, derived_result", "Kept as it was", "NEW".
  v1   -> v2   the rulebook's own retirement tables, read by the census module.

Composing them gives each v0.2 value its current name. Two compositions are genuinely AMBIGUOUS in
the source and are reported rather than guessed -- see `AMBIGUOUS` below.

SAFE TO RUN: no E1-E6 step has ever produced output (`run_log.csv` has one E0 row and
`steps/E*/out/` are empty), so no stored value is invalidated by renaming the enum.
"""

import argparse
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
import runner_core as rc  # noqa: E402
import category_label_census as census  # noqa: E402

CATEGORIES = ("exports", "discovery", "CATEGORIES.xlsx")
ALLOWED = ("config", "allowed_values.yaml")

#: axis -> (CATEGORIES.xlsx sheet, the allowed_values key it feeds, the schema field)
AXIS = [
    ("E1", "E1 Question type", "question_type", [("schemas/E1.json", "question_type")]),
    ("E2", "E2 Format", "format", [("schemas/E2.json", "format")]),
    ("E3", "E3 Content shape", "content_shape", [("schemas/E3.json", "content_shape")]),
    ("E4", "E4 Thinking", "thinking", [("schemas/E4.json", "primary"),
                                       ("schemas/E4.json", "secondary")]),
    ("E5", "E5 Trap", "trap", [("schemas/E5.json", "trap")]),
]

#: v0.2 values that v1 dropped WITHOUT recording a successor anywhere -- no Status row mentions
#: them. Unlike every other mapping here, these are hand-authored, because there is no record to
#: derive them from. Each cites the v2 definition that already covers the case, so the claim can be
#: checked against the rulebook rather than taken on trust. Printed as hand-authored every run.
DROPPED_IN_V1 = {
    "count_correct": ("count_qualifying_items",
                      "v2 E2 added this label for exactly this task"),
    "identify_reactant": ("predict_product",
                          "v2 predict_product covers 'the starting material'"),
    "identify_reagent_or_condition": ("predict_product",
                                      "v2 predict_product covers 'the reagent set that effects a "
                                      "conversion'"),
    "pick_scientist_or_date": ("name_or_identify",
                               "v2 name_or_identify covers 'a name, term, colour, organism, "
                               "scientist'"),
    "expand_abbreviation": ("name_or_identify",
                            "the v1 codebook's own name_or_identify text lists 'expanded "
                            "abbreviation'"),
    "pick_proportionality": ("derive_expression",
                             "v2 derive_expression covers 'which power of a variable the quantity "
                             "follows'"),
    "odd_one_out": ("pick_correct_statement",
                    "the task is grading each option and picking the one that fails; no v2 label "
                    "describes it more closely, so this is the weakest of these mappings"),
    "classify_into_group": ("name_or_identify",
                            "the answer is the group's name; E3 classification_hierarchy carries "
                            "the content side"),
    "one_line": ("definition_term",
                 "E3: a one-line taught fact about what a term means"),
    "applied_context": ("formula_or_law",
                        "E3: a relation applied to a described situation"),
    # NOT retired: `current_affairs` is live. scripts/checks/E3.py uses it to enforce an invariant
    # no other label carries -- a current-affairs fact is in NO NCERT edition, so a question tagged
    # with it whose D6 `syllabus_status` says otherwise is a contradiction worth failing. Mendel is
    # in NCERT, so `scientist_history` cannot stand in for it, and folding the two together would
    # have silently deleted that check.
}

#: v0.2 names whose v1 successor cannot be determined from CATEGORIES.xlsx, because two different v1
#: rows both claim to have been that name. Reported every run; never silently resolved.
AMBIGUOUS = {
    "elimination": ("check_each_statement claims 'Renamed - was elimination' while a row named "
                    "`elimination` claims 'Kept as it was' -- the same v0.2 name is both renamed "
                    "away and kept"),
    "process": ("both `multi_step` and `sequence_based` claim 'Renamed - was process', and E3 has "
                "its own live `process`"),
}


def v02_to_v1(sheet_rows):
    """Read one axis sheet's Status column into {old v0.2 name: current v1 name}."""
    head = next(i for i, r in enumerate(sheet_rows) if r and r[0] == "Category")
    cols = {h: i for i, h in enumerate(sheet_rows[head]) if h}
    mapping, live = {}, []
    for row in sheet_rows[head + 1:]:
        if not row or not row[0].strip():
            continue
        name = row[0].strip()
        live.append(name)
        status = row[cols["Status"]].strip() if "Status" in cols else ""
        m = re.search(r"\bwas\s+(.+)$", status)
        if not m:
            continue                       # "NEW" or "Kept as it was" with no predecessor listed
        for old in re.split(r",\s*", m.group(1)):
            old = old.strip().rstrip(".")
            if old and old != name:
                mapping[old] = name
    return mapping, live


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    import openpyxl
    import yaml

    wb = openpyxl.load_workbook(rc.pp(*CATEGORIES), read_only=True)
    secs = census.rulebook_sections()
    allowed = yaml.safe_load(open(rc.pp(*ALLOWED), encoding="utf-8"))
    old_version = allowed.get("version")

    # every live label on every axis, so a retirement that points at ANOTHER axis is recognised as
    # a move rather than reported as an unresolved target (diagram_graph -> E1 figure_to_read)
    all_live = set()
    for axis, _, _, _ in AXIS:
        live, _ = census.split_retired(secs.get(census.SECTION[axis], ""))
        all_live |= set(live) | set(census.PROSE_LABELS.get(axis, ()))

    lineage, vocab, report = {}, {}, collections.Counter()
    for axis, sheet, key, _ in AXIS:
        rows = [[("" if c is None else str(c)) for c in r]
                for r in wb[sheet].iter_rows(values_only=True)]
        hop1, v1_live = v02_to_v1(rows)

        section = secs.get(census.SECTION[axis], "")
        # Section 5a holds verdicts that are explicitly NOT traps (`source_damage_artifact` is our
        # own extraction damage; `arguable_key` is a review flag). They must not sit in the `trap`
        # enum, or an agent can satisfy "name the trap" by naming our data quality.
        # Read only the 5a..5b span: the retirement table sits BETWEEN 5a and 5b, so splitting the
        # section at 5a would hide it and the whole E5 lineage would come back empty.
        verdicts = []
        span = re.search(r"### 5a\b(.*?)(?=\*\*Retired|### 5b|\Z)", section, re.S)
        if span:
            verdicts = sorted(set(census.table_labels(span.group(1))))
        v2_live, v2_retired = census.split_retired(section)
        v2_live = sorted(set(v2_live) | set(census.PROSE_LABELS.get(axis, ())))
        hop2 = census.replacement_map(section)
        if verdicts:
            vocab["trap_verdict"] = verdicts
            v2_live = [l for l in v2_live if l not in verdicts]
            print("      5a verdicts held OUT of the trap enum: %s" % ", ".join(verdicts))

        # compose: a v0.2 name -> its v1 name -> its v2 name, as far as each hop goes
        chain = {}
        for old, mid in hop1.items():
            chain[old] = hop2.get(mid, mid)
        for name in v1_live:
            if name in hop2:
                chain[name] = hop2[name]
        # anything the rulebook retired, pointed at its replacement
        for name in v2_retired:
            if name in hop2:
                chain.setdefault(name, hop2[name])

        # the hand-authored hop for values v1 dropped with no record
        hand = {}
        for old, (new, _why) in DROPPED_IN_V1.items():
            if new in v2_live and old not in chain:
                chain[old] = new
                hand[old] = new

        moved = sorted(t for t in chain.values() if t not in v2_live and t in all_live)
        unresolved = sorted(t for t in chain.values() if t not in all_live)
        vocab[key] = v2_live
        lineage[key] = {k: v for k, v in sorted(chain.items()) if k not in v2_live}
        report["retired_recorded"] += len(lineage[key])
        report["hand_authored"] += len(hand)
        print("%s  %-14s v2 live %2d   predecessors %2d (derived %d + hand-authored %d)"
              % (axis, key, len(v2_live), len(lineage[key]), len(lineage[key]) - len(hand),
                 len(hand)))
        if moved:
            print("      retired ACROSS axes (not a fault): %s" % ", ".join(sorted(set(moved))))
        if unresolved:
            print("      UNRESOLVED -- target is no axis's live label: %s"
                  % ", ".join(sorted(set(unresolved))))
            report["unresolved"] += len(set(unresolved))

    print("\n%d mappings are HAND-AUTHORED because v1 dropped the value with no record:"
          % report["hand_authored"])
    for old, (new, why) in sorted(DROPPED_IN_V1.items()):
        print("   %-30s -> %-24s %s" % (old, new, why))

    print("\nambiguous in the source, reported not guessed:")
    for name, why in AMBIGUOUS.items():
        print("   %-12s %s" % (name, why))

    # ---- E4 is three sub-axes in v2, so one key cannot carry it
    section4 = secs.get("4.", "")
    demand = census.table_labels(re.split(r"\*\*4b", section4)[0])
    structure = census.table_labels(
        re.split(r"\*\*4c", re.split(r"\*\*4b", section4)[-1])[0])
    strategy = list(census.PROSE_LABELS.get("E4", ()))
    vocab.pop("thinking", None)
    vocab["cognitive_demand"] = sorted(set(demand))
    vocab["solution_structure"] = sorted(set(structure))
    vocab["strategy_available"] = sorted(set(strategy))
    print("\nE4 split into three keys: cognitive_demand %d, solution_structure %d, "
          "strategy_available %d"
          % (len(vocab["cognitive_demand"]), len(vocab["solution_structure"]),
             len(vocab["strategy_available"])))

    total = sum(len(v) for v in vocab.values())
    print("\n%d live values across %d keys; %d predecessors recorded as retired"
          % (total, len(vocab), report["retired_recorded"]))

    if args.dry_run:
        print("\n(dry run -- nothing written)")
        return 0

    # ---- write allowed_values.yaml, preserving every key this script does not own
    allowed["version"] = "v0.3"
    for key in ("thinking_draft", "thinking_candidates_for_owner", "thinking"):
        allowed.pop(key, None)
    allowed.update(vocab)
    allowed["category_retired"] = {k: v for k, v in sorted(lineage.items()) if v}
    allowed["category_ambiguous"] = {k: v for k, v in sorted(AMBIGUOUS.items())}
    header = (
        "# GENERATED by scripts/build_allowed_values.py -- do not hand-edit the category keys.\n"
        "# The category vocabulary is authored in docs/question_categories/RULEBOOK.md; this file\n"
        "# is what the live steps validate against, so the two must agree. SPEC Rules 21 and 23.\n"
        "# `category_retired` maps every superseded v0.2/v1 name to its current label, derived from\n"
        "# CATEGORIES.xlsx's Status column and the rulebook's retirement tables.\n"
        "# Checked by scripts/checks/category_label_census.py.\n")
    with open(rc.pp(*ALLOWED), "w", encoding="utf-8") as fh:
        fh.write(header)
        yaml.safe_dump(allowed, fh, sort_keys=True, default_flow_style=False, allow_unicode=True)
    print("\nwrote config/allowed_values.yaml  %s -> v0.3" % old_version)

    # ---- rewrite the schema enums in place, field by field
    for axis, _, key, targets in AXIS:
        values = (vocab.get("cognitive_demand", []) + vocab.get("solution_structure", [])
                  + vocab.get("strategy_available", [])) if axis == "E4" else vocab.get(key, [])
        for path, field in targets:
            full = rc.pp(path)
            blob = open(full, encoding="utf-8").read()
            pattern = re.compile(
                r'("%s"\s*:\s*\{[^{}]*?"enum"\s*:\s*)(\[[^\]]*\])' % re.escape(field), re.S)

            def _replace(m):
                # A NULLABLE enum must keep its null. schemas/E4.json's `secondary` is
                # "type": ["string", "null"] with null listed in the enum, because "no secondary
                # kind of thinking" is the normal case. Dropping it made every valid E4 answer
                # fail its own schema, and the failure surfaced as a bogus two-run disagreement
                # rather than as a schema error, which is why it is preserved explicitly here.
                try:
                    keep_null = None in json.loads(m.group(2))
                except ValueError:
                    keep_null = False
                out = sorted(values) + ([None] if keep_null else [])
                return m.group(1) + json.dumps(out, indent=0).replace("\n", " ")

            new, n = pattern.subn(_replace, blob, count=1)
            if not n:
                print("   COULD NOT PATCH %s field %s -- left unchanged" % (path, field))
                continue
            # A schema description that still cites the old version is a lie that survives the
            # patch -- the enum changes and the sentence explaining it does not.
            new = re.sub(
                r"config/allowed_values\.yaml(?:'s)?\s+(?:trap,\s*)?v0\.2(?:'s)?\s+\d+\s+values"
                r"(?:\s+verbatim)?",
                "config/allowed_values.yaml v0.3, generated from "
                "docs/question_categories/RULEBOOK.md by scripts/build_allowed_values.py", new)
            new = re.sub(r"config/allowed_values\.yaml\s+(\w+),\s*v0\.2",
                         r"config/allowed_values.yaml \1, v0.3", new)
            json.loads(new)                                   # refuse to write invalid JSON
            open(full, "w", encoding="utf-8").write(new)
            print("   patched %-16s %-14s -> %d values" % (path, field, len(values)))

    stale = []
    for path in sorted(set(p for _, _, _, ts in AXIS for p, _ in ts)):
        if "v0.2" in open(rc.pp(path), encoding="utf-8").read():
            stale.append(path)
    if stale:
        print("\n   STILL MENTION v0.2, fix by hand: %s" % ", ".join(stale))
    return 0


if __name__ == "__main__":
    sys.exit(main())
