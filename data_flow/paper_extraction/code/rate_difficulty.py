#!/usr/bin/env python3
"""E7: score each question's SOLUTION LOAD and band it easy / medium / hard.

    python3 scripts/rate_difficulty.py --self-test
    python3 scripts/rate_difficulty.py --dry-run
    python3 scripts/rate_difficulty.py --apply

WHAT THIS IS, AND WHAT IT IS HONESTLY NOT
-----------------------------------------
"Difficulty" normally means "what fraction of students got it right". We hold NO response data, and
SPEC Rule 22 forbids asserting student behaviour -- it is the rule that retired `obviously_wrong`
("no student who read the stem would be drawn to it"). So this step does not predict difficulty and
must not be read as doing so.

What it measures is SOLUTION LOAD: how much work the printed question demands, counted from features
anyone can check on the page. Every driver below is a fact about the question, and the band is the
sum. `difficulty_basis` records which drivers fired, so a band can be argued with rather than taken
on faith -- a band with no basis is a number nobody can check.

The honest limitation, stated here because it belongs with the number: load and difficulty are not
the same thing. A one-step question on an obscure fact is low load and may well be answered badly;
a four-step calculation on a familiar formula is high load and may be answered well. Nothing here
can distinguish those, and only item-analysis data could. If response data ever arrives, this
rubric is the thing to validate against it -- that is why the basis is stored per question.

WHY A SCRIPT AND NOT AN AGENT
-----------------------------
Every driver is already decided by an earlier step: `cognitive_demand` and `solution_structure` come
from ECAT, the items-to-adjudicate count from E1's printed shape, the figure overlay from the
record. Asking an agent to re-judge them would replace deterministic inputs with a guess and make
two runs disagree for no reason. The agent's job was the judgement; this is arithmetic over it.
"""

import argparse
import collections
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

SHEET = ("docs", "question_categories", "SHEET_V2.csv")

#: Each driver is (points, why). The weights are deliberately small integers and deliberately few:
#: a finer scale would imply a precision the inputs do not have.
DEMAND_LOAD = {
    "recall": 0,
    "concept_discrimination": 1,
    "application": 1,
    "condition_based_reasoning": 2,
    "representation_translation": 2,
    "explanatory_reasoning": 2,
    "dimensional_reasoning": 2,
    "calculation": 2,
}
STRUCTURE_LOAD = {
    "single_step": 0,
    "several_independent_checks": 1,
    "multi_step_dependent": 2,
}
#: How many things the PRINTED SHAPE forces the student to adjudicate before answering. Counted from
#: the shape rather than guessed: a four-row match list is four decisions whatever its subject.
SHAPE_ITEMS = {
    "plain_mcq": 1, "statement_options": 1, "pair_options": 1, "fill_in_blank": 1,
    "diagram_labelled": 1, "graph_options": 1, "structure_options": 1, "reaction_options": 1,
    "reaction_scheme": 1, "figure_to_read": 1,
    "statement_i_ii": 2, "assertion_reason": 3,
    "multi_part_respectively": 2,
    "arrange_in_order": 4, "match_the_lists": 4, "list_of_statements": 4,
    "list_of_structures": 5,
}
#: Traps that can only be seen through by completing the work -- they remove the chance of landing on
#: the answer part-way. Each adds load because the question cannot be short-circuited.
NO_SHORTCUT_TRAPS = {
    "intermediate_value", "complementary_grid", "no_elimination_route", "no_derivation_route",
    "partial_combination", "sequence_endpoint_or_adjacency", "parallel_order_decoy",
    "wrong_power_of_dependence", "omitted_contribution", "condition_ignored",
}

BANDS = [(0, 2, "easy"), (3, 5, "medium"), (6, 99, "hard")]


def primary_shape(raw):
    """The printed shape, overlays dropped -- overlays are scored separately."""
    overlays = {"figure_to_read", "fill_in_blank", "experiment_based", "table_based"}
    parts = [p.strip() for p in str(raw or "").split(";") if p.strip()]
    primary = [p for p in parts if p not in overlays]
    return (primary or parts or [""])[0]


def score(row):
    """Return (points, band, [basis lines]) for one sheet row.

    Returns band None when the row has not been rated yet: a band computed from empty inputs would
    be indistinguishable from a real one, and SPEC Rule 19 requires those two states to look
    different.
    """
    basis, points = [], 0

    if str(row.get("review_status") or "") == "source_incomplete":
        return None, None, ["source_incomplete: the question is not all there, so its load cannot "
                            "be counted (rulebook rule 5)"]

    demand = str(row.get("E4a_cognitive_demand") or "").strip()
    structure = str(row.get("E4b_solution_structure") or "").strip()
    if not demand or not structure:
        return None, None, ["not yet rated by ECAT: cognitive_demand=%r solution_structure=%r"
                            % (demand, structure)]

    if demand in DEMAND_LOAD:
        points += DEMAND_LOAD[demand]
        basis.append("demand %s +%d" % (demand, DEMAND_LOAD[demand]))
    if structure in STRUCTURE_LOAD:
        points += STRUCTURE_LOAD[structure]
        basis.append("structure %s +%d" % (structure, STRUCTURE_LOAD[structure]))

    shape = primary_shape(row.get("E1_question_type"))
    items = SHAPE_ITEMS.get(shape, 1)
    if items >= 4:
        points += 2
        basis.append("shape %s adjudicates %d items +2" % (shape, items))
    elif items >= 2:
        points += 1
        basis.append("shape %s adjudicates %d items +1" % (shape, items))

    overlays = [p.strip() for p in str(row.get("E1_question_type") or "").split(";")
                if p.strip() in ("figure_to_read", "table_based", "experiment_based")]
    overlays += [p.strip() for p in str(row.get("E1_secondary_type") or "").split(";")
                 if p.strip() in ("figure_to_read", "table_based", "experiment_based")]
    if overlays:
        points += 1
        basis.append("must read a %s before starting +1" % sorted(set(overlays))[0])

    polarity = str(row.get("task_polarity") or "direct")
    if polarity in ("not", "except"):
        points += 1
        basis.append("negated task (%s) +1" % polarity)

    traps = [t.strip() for t in str(row.get("E5_traps") or "").split(";") if t.strip()]
    blocking = sorted(set(traps) & NO_SHORTCUT_TRAPS)
    if blocking:
        points += 1
        basis.append("no part-way shortcut (%s) +1" % ", ".join(blocking))

    band = next(name for lo, hi, name in BANDS if lo <= points <= hi)
    return points, band, basis


SELF_TEST = [
    ({"review_status": "verified", "E4a_cognitive_demand": "recall",
      "E4b_solution_structure": "single_step", "E1_question_type": "plain_mcq",
      "task_polarity": "direct"}, 0, "easy"),
    ({"review_status": "verified", "E4a_cognitive_demand": "recall",
      "E4b_solution_structure": "several_independent_checks",
      "E1_question_type": "match_the_lists", "task_polarity": "direct"}, 3, "medium"),
    ({"review_status": "verified", "E4a_cognitive_demand": "calculation",
      "E4b_solution_structure": "multi_step_dependent", "E1_question_type": "plain_mcq",
      "task_polarity": "direct", "E5_traps": "intermediate_value"}, 5, "medium"),
    ({"review_status": "verified", "E4a_cognitive_demand": "calculation",
      "E4b_solution_structure": "multi_step_dependent",
      "E1_question_type": "plain_mcq;figure_to_read", "task_polarity": "not",
      "E5_traps": "intermediate_value"}, 7, "hard"),
    ({"review_status": "source_incomplete"}, None, None),
    ({"review_status": "verified", "E4a_cognitive_demand": "",
      "E4b_solution_structure": ""}, None, None),
]


def self_test():
    bad = 0
    for row, want_points, want_band in SELF_TEST:
        points, band, basis = score(row)
        ok = (points == want_points and band == want_band)
        bad += 0 if ok else 1
        print("%s  %-9s points=%-5s band=%-7s  %s"
              % ("ok  " if ok else "FAIL", row.get("E4a_cognitive_demand") or "-",
                 points, band, "; ".join(basis)[:88]))
    print("\n%d of %d self-tests pass" % (len(SELF_TEST) - bad, len(SELF_TEST)))
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run, --apply or --self-test")

    path = rc.pp(*SHEET)
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    fields = list(rows[0].keys())
    for column in ("E7_load_points", "E7_difficulty_band", "E7_difficulty_basis"):
        if column not in fields:
            fields.append(column)

    bands = collections.Counter()
    for row in rows:
        points, band, basis = score(row)
        row["E7_load_points"] = "" if points is None else points
        row["E7_difficulty_band"] = band or ""
        row["E7_difficulty_basis"] = "; ".join(basis)
        bands[band or "not yet scorable"] += 1

    print("%d questions" % len(rows))
    for band in ("easy", "medium", "hard", "not yet scorable"):
        if bands[band]:
            print("   %5d  %s" % (bands[band], band))
    print("\n   A band is SOLUTION LOAD counted from the page, not a prediction of how students"
          "\n   perform -- we hold no response data (SPEC Rule 22). `E7_difficulty_basis` records"
          "\n   which drivers fired so a band can be argued with.")
    if bands["not yet scorable"]:
        print("\n   %d not scorable yet: ECAT must rate cognitive_demand and solution_structure"
              " first,\n   and a source_incomplete question is never scored."
              % bands["not yet scorable"])

    if args.dry_run:
        print("\n(dry run -- nothing written)")
        return 0
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print("\nwrote %s" % os.path.join(*SHEET))
    return 0


if __name__ == "__main__":
    sys.exit(main())
