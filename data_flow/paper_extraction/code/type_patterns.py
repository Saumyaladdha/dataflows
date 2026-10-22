#!/usr/bin/env python3
"""E1's SCRIPT half (spec Section 13/E1): decide `question_type` from the question's own shape.

    python3 scripts/type_patterns.py --item-id Q-000015      # one question
    python3 scripts/type_patterns.py --all                   # every canonical record
    python3 scripts/type_patterns.py --self-test             # spec's own boundary cases

Spec 13/E1 is explicit that the AGENT (`e1-type-tagger`) runs ONLY when no pattern decides, so
this module is the primary classifier and `classify()` returning None is what triggers a real
agent call. The 16 patterns are applied in the spec's stated priority order, FIRST MATCH WINS --
that ordering is load-bearing, not incidental: an Assertion-Reason question also contains two
statements, and a match question also contains lists, so a different order silently reclassifies
whole families of real questions.

Every pattern below cites the spec rule it implements and, where the spec names a real question
that must NOT be caught by the obvious reading, that counter-example is in `--self-test` so a
future edit that breaks it fails loudly instead of quietly mis-tagging the bank.

This module makes no judgements beyond the spec's literal patterns (CLAUDE.md: "Scripts are plain
Python and make no judgements"); anything the patterns don't settle is handed to the agent.
"""
import argparse
import json
import os
import re
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402

# ---------------------------------------------------------------------------
# Helpers over the real record shape (papers/records/<QID>.json)
# ---------------------------------------------------------------------------


def _text_of(rec):
    """The stem plus any lettered statements -- the span the stem-shape patterns look at.

    Statements are included because several real patterns ("two statements", "Assertion") are
    worded in the statements themselves rather than the stem; options are deliberately NOT
    included here, since option-shape is a separate signal handled by `_options_look_like`."""
    parts = [rec.get("stem_en") or ""]
    for s in rec.get("statements") or []:
        if isinstance(s, dict):
            parts.append(f"{s.get('label', '')} {s.get('text', '')}")
        else:
            parts.append(str(s))
    return "\n".join(parts)


def _options(rec):
    opts = rec.get("options_en") or {}
    return [str(opts.get(k) or "") for k in ("1", "2", "3", "4") if opts.get(k)]


def _has_two_lists(rec):
    return bool(rec.get("list_i")) and bool(rec.get("list_ii"))


_PAIR_RE = re.compile(r"^\s*\(?[A-Za-z]\)?\s*[-–—:]\s*\(?[ivx\d]+\)?\s*$", re.IGNORECASE)


def _options_are_single_pairs(rec):
    """`pair_options` (pattern 5) needs options that are each ONE pairing, e.g. "A - ii", not a
    combination code like "A-ii, B-i, C-iv". Counting separators is what distinguishes them."""
    opts = _options(rec)
    if not opts:
        return False
    for o in opts:
        o = o.strip()
        # A combination option lists several pairs; a single pair has no comma/semicolon.
        if "," in o or ";" in o:
            return False
        if not _PAIR_RE.match(o) and not re.match(r"^\s*\(?[A-Za-z]\)?\s*[-–—:]\s*", o):
            return False
    return True


_COMBO_RE = re.compile(r"\b(?:only|and)\b", re.IGNORECASE)
_LETTER_LIST_RE = re.compile(r"\b[A-E]\b(?:\s*(?:,|and|&)\s*\b[A-E]\b)+")


def _options_are_combinations(rec):
    """Combination options name several lettered items: "A and D only", "A, B and C only"."""
    opts = _options(rec)
    if not opts:
        return False
    hits = sum(1 for o in opts if _LETTER_LIST_RE.search(o) or
               (_COMBO_RE.search(o) and re.search(r"\b[A-E]\b", o)))
    return hits >= max(2, len(opts) - 1)


_MATHY_RE = re.compile(r"\$|\\mathrm|\\rightarrow|\\dfrac|\\frac|_\{|\^\{")


def _options_are_reactions(rec):
    """Options that are each a chemical REACTION (a reagent/arrow transformation), e.g. real
    Q-000005: "$\\mathrm{CH_3CN} \\rightarrow$ (i) $\\mathrm{LiAlH_4}$ ... Product".

    This exists because of a real gap found in spec 13/E1's own pattern list (see classify()'s
    rule-9b comment): pattern 9 only covers a reaction in the STEM, and pattern 15 covers prose
    statements. Neither covers "the four options are four different reactions to evaluate", which
    is a common real Chemistry shape. Detecting it lets classify() hand the question to the agent
    instead of mislabelling it `statement_options`."""
    opts = _options(rec)
    if len(opts) < 2:
        return False
    hits = sum(1 for o in opts if _P_REACTION.search(o))
    return hits >= max(2, len(opts) - 1)


def _options_are_full_statements(rec):
    """Pattern 15: options that are themselves statements to judge. Heuristic the spec implies
    rather than states numerically -- every option is a prose clause of real length, none is a
    bare value/name/letter-combination, and none is dominated by formula/chemical notation.

    The notation guard is not cosmetic: without it, four LaTeX chemical reactions each read as a
    long "statement" and real Q-000005 was mislabelled `statement_options` (confirmed against the
    real record). A reaction equation is not a statement to judge.

    Kept deliberately conservative -- when this is unsure the step hands off rather than guessing,
    because a wrong `statement_options` tag propagates: E2's own format test keys off it."""
    opts = _options(rec)
    if len(opts) < 2:
        return False
    for o in opts:
        o = o.strip()
        if len(o.split()) < 4:
            return False
        if _LETTER_LIST_RE.search(o):
            return False
        # Formula/chemical-notation-dominated options are not prose statements.
        if _MATHY_RE.search(o) and len(re.findall(r"\b[a-z]{4,}\b", o)) < 3:
            return False
    return True


def _figure_role_needed(rec):
    return bool(rec.get("has_figure"))


# ---------------------------------------------------------------------------
# The 16 ordered patterns (spec 13/E1 "Patterns (apply in this priority order)")
# ---------------------------------------------------------------------------

_P_ASSERTION = re.compile(r"\bassertion\b", re.IGNORECASE)
_P_STATEMENT_I_II = re.compile(
    r"statement[\s\-–—]*(?:I\b|1\b)|two\s+statements", re.IGNORECASE)
_P_COLUMN_III = re.compile(r"column[\s\-–—]*(?:III\b|3\b)", re.IGNORECASE)
_P_TWO_LISTS = re.compile(
    r"list[\s\-–—]*(?:I\b|1\b)|column[\s\-–—]*(?:I\b|1\b)|\bmatch\b", re.IGNORECASE)
_P_MATCHED = re.compile(
    r"correctly\s+matched|wrongly\s+matched|mismatch|correct\s+match|incorrectly\s+paired",
    re.IGNORECASE)
_P_ARRANGE = re.compile(
    r"\barrange\b|\bsequence\b|correct\s+order\s+of\s+(?:events|steps|stages)", re.IGNORECASE)
_P_RANK = re.compile(
    r"(?:increasing|decreasing|correct)\s+order\s+of\s+\w+|largest\s+to\s+smallest|"
    r"smallest\s+to\s+largest", re.IGNORECASE)
_P_REACTION = re.compile(
    r"(?:→|->|\\rightarrow|\\xrightarrow)", re.IGNORECASE)
_P_REACTION_ASK = re.compile(
    r"\b(?:X|Y|Z)\b|\bproduct\b|\breagent\b|\bname\s+of\s+the\s+reaction\b", re.IGNORECASE)
_P_BLANK = re.compile(r"_{3,}|\.{4,}")
_P_LABELLED = re.compile(r"\blabel(?:led|ed)\b|marked\s+as\s+[A-D]\b", re.IGNORECASE)
_P_RESPECTIVELY = re.compile(r"\brespectively\b", re.IGNORECASE)


def _answer_has_multiple_parts(rec):
    """Pattern 14 hinges on the ANSWER having two or more parts, not merely on the word
    "respectively" appearing. Spec's own counter-example: "...two arms are 5 Ω and R Ω
    respectively" (2014#27) is NOT multi_part_respectively, because there the word describes the
    SETUP and each option is a single value. So: look at the options, not the stem."""
    opts = _options(rec)
    if not opts:
        return False
    multi = 0
    for o in opts:
        # Two or more comma/"and"-joined values, or an explicit pair like "2, 3".
        if re.search(r"\d\s*(?:,|;|and)\s*\d", o) or o.count(",") >= 1:
            multi += 1
    return multi >= max(2, len(opts) - 1)


def classify(rec):
    """Return (question_type, which_rule) or (None, reason) when no pattern decides.

    (None, ...) is a real, expected outcome -- it is exactly the signal that step E1 must call
    the `e1-type-tagger` agent for this question (spec 13/E1: "AGENT only when no pattern
    decides"). It is never a failure."""
    text = _text_of(rec)

    # 1. Assertion -> assertion_reason
    if _P_ASSERTION.search(text):
        return "assertion_reason", "1 assertion"

    # 2. "Statement I"/"two statements" WITHOUT Assertion -> statement_i_ii
    #    Spec boundary: "Two statements A and B" with no because-link (2026-May#25) is
    #    statement_i_ii even though a legacy sheet called it Assertion-Reason.
    if _P_STATEMENT_I_II.search(text):
        return "statement_i_ii", "2 statement I/II"

    # 3. Column III / three-column rows -> match_three_columns
    if _P_COLUMN_III.search(text):
        return "match_three_columns", "3 column III"

    # 4. List-I/Column-I/Match with two lists -> match_the_lists
    if _has_two_lists(rec) or _P_TWO_LISTS.search(text):
        if _options_are_single_pairs(rec):
            return "pair_options", "5 single-pair options (before 4)"
        return "match_the_lists", "4 two lists"

    # 5. correctly/wrongly matched AND options are single pairs -> pair_options
    if _P_MATCHED.search(text) and _options_are_single_pairs(rec):
        return "pair_options", "5 matched + pair options"

    # 6. arrange / sequence / correct order of events|steps|stages -> arrange_in_order
    if _P_ARRANGE.search(text):
        return "arrange_in_order", "6 arrange/sequence"

    # 7. (increasing|decreasing|correct) order of <property> -> rank_by_property
    #    Spec boundary: "correct order of organisation of genetic material from largest to
    #    smallest" (2015#161) is rank_by_property, NOT arrange_in_order -- which is why 6's
    #    regex is restricted to events|steps|stages and does not match a bare "order of".
    if _P_RANK.search(text):
        return "rank_by_property", "7 order of property"

    # 8. B3 structure == statements with combination options -> list_of_statements
    if rec.get("structure") == "statements" and _options_are_combinations(rec):
        return "list_of_statements", "8 statements + combination options"

    # 9. reaction arrow/scheme asking for X/Y/Z/product/reagent/name -> reaction_scheme
    if _P_REACTION.search(text) and _P_REACTION_ASK.search(text):
        return "reaction_scheme", "9 reaction scheme (text arrow)"

    # 9a. Spec's rule 9 is "reaction arrow OR SCHEME IMAGE in the stem" -- the image half matters
    #     and was missed on the first pass: real Q-000013 ("Identify product (A) in the following
    #     reaction: [Chemical structure of a diketone ... undergoing reduction]") has its scheme as
    #     an IMAGE, no text arrow, so the text-arrow test above cannot see it. Without this it fell
    #     through to rule 12 and was mislabelled `figure_to_read`, losing the fact that it is a
    #     reaction question at all. Must stay ahead of rules 11/12, which also match a figure.
    if _figure_role_needed(rec) and _P_REACTION_ASK.search(text) and \
            re.search(r"\breaction\b|\bscheme\b|\bsynthesis\b", text, re.IGNORECASE):
        return "reaction_scheme", "9a reaction scheme (image in stem)"

    # 9b. REAL GAP IN SPEC 13/E1's PATTERN LIST, found from real data -- recorded, not papered
    #     over. When the four OPTIONS are each a reaction (real Q-000005: "which of the following
    #     reactions will NOT give primary amine"), no spec pattern applies: rule 9 is scoped to the
    #     stem, rule 10 covers option IMAGES only, rule 15 covers prose statements. Returning None
    #     hands it to the `e1-type-tagger` agent, which is exactly what spec 13/E1 says to do when
    #     no pattern decides -- strictly better than the mislabel this produced before. The
    #     taxonomy's `list_of_structures` (added in v0.2 for option-structures) suggests a
    #     reaction analogue may be the real answer; that is the owner's call, logged in
    #     docs/OPEN_QUESTIONS.md, not something a script should decide.
    if _options_are_reactions(rec):
        return None, "9b options are reactions -- no spec pattern covers this"

    # 10. options are images: graphs -> graph_options; structures -> structure_options
    #     Needs real option-image data (B2 crops them to papers/questions/...). The current
    #     corpus has none, so this cannot fire yet -- left explicit rather than silently absent.
    option_images = rec.get("option_images") or {}
    if option_images:
        kinds = " ".join(str(v) for v in option_images.values()).lower()
        if "graph" in kinds:
            return "graph_options", "10 graph option images"
        if "structure" in kinds:
            return "structure_options", "10 structure option images"

    # 11. figure with letter labels A-D to identify -> diagram_labelled
    if _figure_role_needed(rec) and _P_LABELLED.search(text):
        return "diagram_labelled", "11 labelled figure"

    # 12. figure referred to and needed -> figure_to_read
    if _figure_role_needed(rec):
        return "figure_to_read", "12 figure needed"

    # 13. "____" -> fill_in_blank
    if _P_BLANK.search(text):
        return "fill_in_blank", "13 blank"

    # 14. "...are respectively" where the ANSWER has 2+ parts -> multi_part_respectively
    if _P_RESPECTIVELY.search(text) and _answer_has_multiple_parts(rec):
        return "multi_part_respectively", "14 respectively + multi-part answer"

    # 15. options are full statements to judge -> statement_options
    if _options_are_full_statements(rec):
        return "statement_options", "15 full-statement options"

    # 16. otherwise -> single_statement
    #     Spec boundary: "how many plants among ..." (2015#130) is single_statement -- those are
    #     items, not statements, so pattern 8/15 must not have caught it.
    return "single_statement", "16 default"


# ---------------------------------------------------------------------------
# Self-test: the spec's own named boundary cases (13/E1 "Boundaries seen in real data")
# ---------------------------------------------------------------------------

_CASES = [
    # (name, record, expected_type)
    ("2026-May#25 two statements, no because-link -> statement_i_ii (not assertion_reason)",
     {"stem_en": "Given below are two statements A and B. Choose the correct answer.",
      "statements": [{"label": "A", "text": "Water potential of pure water is zero."},
                     {"label": "B", "text": "Solutes lower water potential."}],
      "options_en": {"1": "Both A and B are correct", "2": "A correct, B incorrect",
                     "3": "A incorrect, B correct", "4": "Both incorrect"}},
     "statement_i_ii"),

    ("2015#161 order of ... largest to smallest -> rank_by_property (not arrange_in_order)",
     {"stem_en": "The correct order of organisation of genetic material from largest to smallest is",
      "options_en": {"1": "genome", "2": "chromosome", "3": "gene", "4": "nucleotide"}},
     "rank_by_property"),

    ("2014#27 'respectively' describing the SETUP -> not multi_part_respectively",
     {"stem_en": "In a metre bridge the two arms are 5 Ω and R Ω respectively. Find R.",
      "options_en": {"1": "2 Ω", "2": "5 Ω", "3": "10 Ω", "4": "15 Ω"}},
     "single_statement"),

    ("2015#130 'how many plants among' -> single_statement (items, not statements)",
     {"stem_en": "How many plants among the following are monocots?",
      "options_en": {"1": "2", "2": "3", "3": "4", "4": "5"}},
     "single_statement"),

    ("assertion wins over statement wording (priority 1 before 2)",
     {"stem_en": "Assertion: Water rises in a capillary. Reason: Surface tension acts. "
                 "Given below are two statements.",
      "options_en": {"1": "Both true", "2": "A true R false", "3": "A false", "4": "Both false"}},
     "assertion_reason"),

    ("real Q-000015 shape: statements + combination options -> list_of_statements",
     {"stem_en": "Which of the following statements are correct regarding female reproductive "
                 "cycle? Choose the most appropriate answer from the options given below:",
      "structure": "statements",
      "statements": [{"label": "A", "text": "oestrus cycle"}, {"label": "B", "text": "menopause"},
                     {"label": "C", "text": "pregnancy"}, {"label": "D", "text": "menarche"}],
      "options_en": {"1": "A and D only", "2": "A and B only", "3": "A, B and C only",
                     "4": "A, C and D only"}},
     "list_of_statements"),

    ("three columns -> match_three_columns (priority 3 before 4)",
     {"stem_en": "Match Column I with Column II and Column III.",
      "list_i": ["a"], "list_ii": ["b"],
      "options_en": {"1": "A-i-p", "2": "A-ii-q", "3": "A-iii-r", "4": "A-iv-s"}},
     "match_three_columns"),

    ("reaction arrow asking for the product -> reaction_scheme",
     {"stem_en": "CH3CH2Br + KCN → X. The product X is",
      "options_en": {"1": "nitrile", "2": "amine", "3": "alcohol", "4": "acid"}},
     "reaction_scheme"),

    # --- Regression cases from real records, added after both were caught mis-tagged. ---

    ("REAL Q-000013: scheme is an IMAGE, no text arrow -> reaction_scheme (not figure_to_read)",
     {"stem_en": "Identify product (A) in the following reaction: [Chemical structure of a "
                 "diketone with a benzene ring attached to a cyclohexane ring, undergoing "
                 "reduction]",
      "has_figure": True,
      "options_en": {
          "1": "Ethyl group attached to cyclohexane and ethyl group attached to benzene ring",
          "2": r"$\mathrm{OH}$ attached to cyclohexane and $\mathrm{OH}$ attached to benzene ring",
          "3": r"$\mathrm{CH_2OH}$ attached to cyclohexane and $\mathrm{CH_2OH}$ attached to benzene ring",
          "4": r"$\mathrm{CH_3}$ attached to cyclohexane and $\mathrm{CH_3}$ attached to benzene ring"}},
     "reaction_scheme"),

    ("REAL Q-000005: the OPTIONS are reactions -> no spec pattern covers it, hand to the agent",
     {"stem_en": "Which of the following reactions will NOT give primary amine as the product?",
      "has_figure": False,
      "options_en": {
          "1": r"$\mathrm{CH_3CONH_2} \rightarrow \mathrm{Br_2}\,/\,\mathrm{KOH}$ Product",
          "2": r"$\mathrm{CH_3CN} \rightarrow$ (i) $\mathrm{LiAlH_4}$, (ii) $\mathrm{H_3O^+}$ Product",
          "3": r"$\mathrm{CH_3NC} \rightarrow$ (i) $\mathrm{LiAlH_4}$, (ii) $\mathrm{H_3O^+}$ Product",
          "4": r"$\mathrm{CH_3CONH_2} \rightarrow$ (i) $\mathrm{LiAlH_4}$, (ii) $\mathrm{H_3O^+}$ Product"}},
     None),

    ("REAL Q-000007: options really are prose statements -> statement_options",
     {"stem_en": "If [unreadable glyph]_S E[unreadable glyph] [unreadable glyph] dS[unreadable "
                 "glyph] = 0 over a surface, then :",
      "options_en": {
          "1": "the number of flux lines entering the surface must be equal to the number of flux lines leaving",
          "2": "the magnitude of electric field on the surface is constant.",
          "3": "all the charges must necessarily be inside the surface.",
          "4": "the electric field inside the surface is necessarily uniform."}},
     "statement_options"),
]


def _self_test():
    failures = []
    for name, rec, expected in _CASES:
        got, rule = classify(rec)
        ok = got == expected
        # `got` is legitimately None for a case the patterns must hand to the agent, so render it
        # before formatting rather than formatting None.
        shown = got if got is not None else "NEEDS-AGENT"
        print(f"{'ok  ' if ok else 'FAIL'}  {shown:<24} (rule {rule:<34}) {name}")
        if not ok:
            failures.append((name, expected, got))
    print()
    if failures:
        print(f"{len(failures)} of {len(_CASES)} FAILED:")
        for name, exp, got in failures:
            print(f"  expected {exp}, got {got}  <- {name}")
        return 1
    print(f"all {len(_CASES)} spec boundary cases pass")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _load(qid):
    path = rc.pp("papers", "records", f"{qid}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main(argv=None):
    ap = argparse.ArgumentParser(description="E1 question_type pattern classifier (spec 13/E1).")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--item-id", help="One question id, e.g. Q-000015.")
    g.add_argument("--all", action="store_true", help="Every canonical record.")
    g.add_argument("--self-test", action="store_true", help="Run the spec's boundary cases.")
    args = ap.parse_args(argv)

    if args.self_test:
        return _self_test()

    if args.item_id:
        rec = _load(args.item_id)
        if not rec:
            print(f"no record for {args.item_id}", file=sys.stderr)
            return 2
        qt, rule = classify(rec)
        print(json.dumps({"question_id": args.item_id, "question_type": qt,
                          "decided_by": f"pattern {rule}" if qt else "no pattern -- needs agent"},
                         indent=2))
        return 0

    records_dir = rc.pp("papers", "records")
    rows = []
    for fn in sorted(os.listdir(records_dir)):
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        rec = _load(fn[: -len(".json")])
        if not isinstance(rec, dict) or rec.get("merged_into"):
            continue  # non-canonical half of a C1 merge; its twin carries the tags
        qt, rule = classify(rec)
        rows.append((rec.get("question_id"), rec.get("structure") or "", qt, rule,
                     (rec.get("stem_en") or "")[:58]))
    w = max((len(r[2] or "") for r in rows), default=10)
    for qid, struct, qt, rule, stem in rows:
        print(f"{qid}  {struct:<11}  {qt or 'NEEDS-AGENT':<{w}}  [{rule:<34}]  {stem}")
    print(f"\n{len(rows)} canonical questions; "
          f"{sum(1 for r in rows if r[2] is None)} need a real agent call.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
