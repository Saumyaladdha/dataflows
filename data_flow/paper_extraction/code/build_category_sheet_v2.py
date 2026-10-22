#!/usr/bin/env python3
"""Build the finalised category sheet (v2) from the v1 showcase and `docs/question_categories/RULEBOOK.md`.

    python3 scripts/build_category_sheet_v2.py --dry-run
    python3 scripts/build_category_sheet_v2.py --apply

v1 was reviewed from outside and four faults were confirmed against our own definitions:

  * `application` was defined as "a student who memorised nothing can still reach the answer", which
    is untenable -- applying a rule requires knowing the rule.
  * `direct_fact` was defined to include "no elimination route among the options", which contradicts
    `elimination` existing as a sibling label on the same axis.
  * `explanation_based` said "the facts are granted", but an Assertion-Reason question usually
    requires checking them first.
  * `obviously_wrong` said "no student who read the stem would be drawn to it" -- an empirical claim
    about students that reading the paper cannot support. We hold no response data.

The axis E4 also conflated three different questions (what thinking is needed, how many dependent
steps, what shortcut exists), which is why one question was tagged `check_each_statement` while
having a one-pair shortcut.

What this script does and does not do
-------------------------------------
It does the MECHANICAL part: carries E1-E3 across, re-expresses E4 on the three new axes, drops the
retired E5 labels, and derives `task_polarity`, `review_status` and `key_checked_against` from the
record and the printed sources. Those three are derivable and were missing, which is why the sheet
could carry confident trap tags for questions whose figure or options are absent.

It does NOT re-judge. `concept` and the per-option trap routes are judgements and are left empty and
marked, because a script inventing them is exactly the failure the review found. The agent step
reads this sheet and fills them.
"""

import argparse
import collections
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

#: The full tagged corpus. This was QUESTIONS_SHOWCASE.xlsx (55 rows) and so every figure the sheet
#: reported described 9% of the data -- including a trap total of 13 that looked saturated only
#: because the showcase was the subset where tags had been evidenced.
SRC = ("exports", "discovery", "QUESTIONS.xlsx")
OUT = ("docs", "question_categories", "SHEET_V2.csv")

#: The showcase and the full workbook name the same columns differently; accept either so the sheet
#: can be rebuilt from whichever is current.
COLUMN_ALIASES = {
    "question": ("question", "question_text"),
    "E1": ("E1 value", "E1 question type"),
    "E2": ("E2 value", "E2 format"),
    "E3": ("E3 value", "E3 content shape"),
    "E4": ("E4 value", "E4 thinking"),
    "E5": ("E5 value", "E5 trap"),
    "E5_why": ("E5 why this question", "E5 why"),
}

#: E4 was one axis doing three jobs. Each old label maps to a demand, a structure, or elsewhere.
E4_DEMAND = {
    "direct_fact": "recall",
    "confusing_options": "concept_discrimination",
    "application": "application",
    "explanation_based": "explanatory_reasoning",
    "numerical": "calculation",
    "ratio_based": "calculation",
    "sequence_based": "application",
}
E4_STRUCTURE = {
    "multi_step": "multi_step_dependent",
    "check_each_statement": "several_independent_checks",
}
#: these described a DISTRACTOR, not the thinking, and belong on E5 or E1
E4_MOVED = {"changed_word": "E5", "exception_based": "E5", "diagram_graph": "E1 figure_to_read"}

#: Retired with no inspectable replacement: no numeric device was ever shown behind these tags.
E5_RETIRED = {"number_near_miss"}
#: Each of these needs re-judging rather than a blind rename, because one old label stood for several
#: distinct devices. `obviously_wrong` and `extreme_word` were first retired outright on the grounds
#: that they asserted student behaviour -- but the per-subject analyses show the DEVICES are real
#: (an option with no derivation route behind it; an option wrong only for its quantifier). SPEC
#: Rule 22: redefine against the printed page, do not delete.
E5_NEEDS_REJUDGE = {
    "obviously_wrong": "no_derivation_route | source_damage_artifact",
    "extreme_word": "overclaiming_quantifier",
    "sign_or_direction": "sign_reversed_magnitude_right | inverted_ratio | reversed_order | semantic_reversal",
}
E5_RENAME = {
    "wrong_order": "reversed_order",
    "unit_conversion_slip": "unit_or_conversion",
    "reversed_cause_effect": "semantic_reversal",
    "opposite_answer": "semantic_reversal",
    "changed_word": "single_word_substitution",
}

POLARITY = [
    ("not", re.compile(r"\b(?:is|are|does|do|which)\s+NOT\b|\bNOT\b(?=[^a-z]*(?:correct|true|a |an |the ))")),
    ("except", re.compile(r"\bEXCEPT\b", re.I)),
    ("increasing", re.compile(r"increasing order|ascending order", re.I)),
    ("decreasing", re.compile(r"decreasing order|descending order", re.I)),
    ("maximum", re.compile(r"\b(?:maximum|highest|largest|most stable|fastest|greatest)\b", re.I)),
    ("minimum", re.compile(r"\b(?:minimum|lowest|smallest|least|slowest)\b", re.I)),
    ("respectively", re.compile(r"\brespectively\b", re.I)),
]

PLACEHOLDER = re.compile(r"imageoption|willbeadded|optionimage")


def _norm(t):
    return re.sub(r"[^a-z0-9]", "", re.sub(r"\\[a-zA-Z]+", " ", str(t or "")).lower())


def task_polarity(stem, options):
    """What the task actually asks for.

    `not` is taken from the TASK only. A biological premise containing "does not" ("cellulose does
    not form blue colour") is not a negative task, and neither is the "NOT" inside the standard
    Assertion-Reason option wording -- both were conflated in v1, which is why the field is derived
    here from the stem's question clause rather than from a bare word search.
    """
    text = str(stem or "")
    # the standard A/R and Statement wordings carry NOT inside the OPTIONS, never the task
    opts = " ".join(str(v) for v in (options or []))
    if re.search(r"\bNOT the correct explanation\b", opts, re.I):
        text = text  # unchanged; the option NOT must not count
    for label, pat in POLARITY:
        if pat.search(text):
            return label
    return "direct"


def review_status(rec):
    """Whether this question is complete enough to carry mechanism and trap labels."""
    if rec is None:
        return "provisional", "no record found for this id"
    opts = [(rec.get("options_en") or {}).get(k) or "" for k in "1234"]
    norm = [_norm(o) for o in opts]
    real = [n for n in norm if len(n) >= 3]
    if any(PLACEHOLDER.search(n) for n in norm if n):
        return "source_incomplete", "options are placeholders"
    if len(real) < 4:
        return "source_incomplete", "fewer than four readable options"
    if len(set(real)) < len(real):
        return "source_incomplete", "two options are indistinguishable"
    if rec.get("has_figure") and not (rec.get("figure_path") or rec.get("figure_path_source")):
        return "source_incomplete", "the question needs a figure and none is attached"
    if "unreadable" in " ".join(norm) or "unreadable" in _norm(rec.get("stem_en")):
        return "source_incomplete", "the stem or an option is marked unreadable"
    if rec.get("figure_verified") is True or rec.get("option_order_by_code"):
        return "verified", "checked against a printed paper"
    return "provisional", "complete, but not yet checked against a printed paper"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    import openpyxl
    wb = openpyxl.load_workbook(rc.pp(*SRC), read_only=True)
    rows = list(wb["Questions"].iter_rows(values_only=True))
    head = {h: i for i, h in enumerate(rows[0]) if h}

    recs = {}
    for p in sorted(os.listdir(rc.pp("papers", "records"))):
        if p.endswith(".json"):
            with open(rc.pp("papers", "records", p), encoding="utf-8") as fh:
                r = json.load(fh)
            recs[r.get("question_id")] = r

    out, stats = [], collections.Counter()
    for raw in rows[1:]:
        if not raw or not raw[head["question_id"]]:
            continue
        g = lambda k: (raw[head[k]] if k in head else None)  # noqa: E731

        def ga(alias):
            """Read a column by its logical name, accepting either workbook's spelling."""
            for name in COLUMN_ALIASES[alias]:
                if name in head:
                    return raw[head[name]]
            return None

        qid = g("question_id")
        rec = recs.get(qid)
        opts = [o for o in str(g("options") or "").split("\n") if o.strip()]

        e4_old = [x.strip() for x in str(ga("E4") or "").split(";") if x.strip()]
        demand = next((E4_DEMAND[x] for x in e4_old if x in E4_DEMAND), "")
        structure = next((E4_STRUCTURE[x] for x in e4_old if x in E4_STRUCTURE), "")
        strategy = "elimination" if "elimination" in e4_old else ""
        moved = [E4_MOVED[x] for x in e4_old if x in E4_MOVED]

        e5_old = [x.strip() for x in str(ga("E5") or "").split(";") if x.strip()]
        dropped = [x for x in e5_old if x in E5_RETIRED]
        rejudge = ["%s -> %s" % (x, E5_NEEDS_REJUDGE[x]) for x in e5_old if x in E5_NEEDS_REJUDGE]
        kept = [E5_RENAME.get(x, x) for x in e5_old
                if x not in E5_RETIRED and x not in E5_NEEDS_REJUDGE]
        kept = list(dict.fromkeys(kept))                      # de-duplicate after renaming
        stats["e5_tags_before"] += len(e5_old)
        stats["e5_tags_after"] += len(kept)
        if dropped:
            stats["rows_with_a_retired_tag"] += 1
        if len(e5_old) >= 4:
            stats["rows_overtagged_4_or_more"] += 1

        status, why = review_status(rec)
        stats[status] += 1

        out.append({
            "question_id": qid,
            "subject": g("subject"),
            "year": g("year"),
            "paper_codes": " ".join(str(c) for c in ((rec or {}).get("paper_codes") or [])),
            "question": ga("question"),
            "options": g("options"),
            "official_answer": (rec or {}).get("official_answer"),
            # --- E1 / E2 / E3 carry across unchanged; `secondary_type` and `concept` are new
            "E1_question_type": ga("E1"),
            "E1_secondary_type": "",
            "E2_answer_form": ga("E2"),
            "E3_content_shape": ga("E3"),
            "E3_concept": "",                                  # AGENT fills: specific and revisable
            # --- E4 split into the three questions it was conflating
            "E4a_cognitive_demand": demand,
            "E4b_solution_structure": structure,
            "E4c_strategy_available": strategy,
            "E4_needs_rejudge": "yes" if not (demand and structure) else "",
            "E4_moved_to": "; ".join(moved),
            # --- E5, with the retired and unevidenced labels taken out
            "E5_traps": "; ".join(kept),
            "E5_trap_routes": "",                              # AGENT fills: option + mistake, each
            "E5_dropped_retired": "; ".join(dropped),
            "E5_needs_rejudge": "; ".join(rejudge),
            # --- the supporting fields v1 lacked
            "task_polarity": task_polarity(ga("question"), opts),
            "review_status": status,
            "review_status_why": why,
            "key_checked_against": ("printed paper" if status == "verified" else "none"),
            "reason_v1_carried_over": ga("E5_why"),
        })

    print("%d questions" % len(out))
    for k, v in stats.most_common():
        print("   %5d  %s" % (v, k))
    if stats["e5_tags_before"]:
        print("\n   E5 tags: %d -> %d (%.0f%% removed as retired or unevidenced)"
              % (stats["e5_tags_before"], stats["e5_tags_after"],
                 100.0 * (stats["e5_tags_before"] - stats["e5_tags_after"]) / stats["e5_tags_before"]))
    print("\n   Fields left for the agent: E3_concept, E5_trap_routes, and any row marked "
          "E4_needs_rejudge or E5_needs_rejudge.")

    if args.dry_run:
        print("\n(dry run -- nothing written)")
        return 0
    path = rc.pp(*OUT)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    print("\nwrote %s" % os.path.relpath(path, rc.pp()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
