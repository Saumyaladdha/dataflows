#!/usr/bin/env python3
"""E6's SCRIPT half (spec Section 13/E6): the descriptive tags that need no judgement.

    python3 scripts/describe_tags.py --item-id Q-000015
    python3 scripts/describe_tags.py --all
    python3 scripts/describe_tags.py --self-test

Spec 13/E6 splits this step cleanly: the SCRIPT fills `answer_form`, `negation`, `item_count`,
`constants_given` and `figure_role`, and also `stem_context` **by patterns** -- with the
`e6-context-tagger` AGENT called only for `stem_context` when the patterns don't decide. So
`stem_context: None` here is the designed trigger for a real agent call, never a failure.

Deliberate restraint, per CLAUDE.md ("Scripts are plain Python and make no judgements"): the five
script-owned fields are all mechanically derivable from the record, and `stem_context` is only
claimed where the spec names an explicit pattern. Where two contexts could apply, the spec gives a
tie-break rule that needs real judgement ("choose the one the question cannot be answered
without" -- its own example: a stem quoting natality/mortality figures is `data_given`, not
`case_scenario`), so this module resolves only the unambiguous cases and hands the rest over
rather than guessing with a priority order the spec never states.
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

# Spec 13/E2's negative-word guard names six; B3's own allowed set omits MISMATCH (a real
# 5-vs-6 discrepancy already logged in docs/OPEN_QUESTIONS.md, 2026-10-11 config entry).
# E6 only COUNTS negatives, so it reads the full six and does not depend on that discrepancy.
_NEGATIVE_WORDS = ("NOT", "EXCEPT", "INCORRECT", "FALSE", "WRONG", "MISMATCH")


def _options(rec):
    opts = rec.get("options_en") or {}
    return [str(opts.get(k) or "") for k in ("1", "2", "3", "4") if opts.get(k)]


def _stem_and_statements(rec):
    parts = [rec.get("stem_en") or ""]
    for s in rec.get("statements") or []:
        parts.append(f"{s.get('label', '')} {s.get('text', '')}" if isinstance(s, dict) else str(s))
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# answer_form -- from the parsed options (spec: "from parsed options")
# ---------------------------------------------------------------------------

_LETTER_COMBO_RE = re.compile(r"\b[A-E]\b(?:\s*(?:,|and|&)\s*\b[A-E]\b)+|\b[A-E]\s+and\s+[A-E]\b",
                              re.IGNORECASE)
_MATCH_CODE_RE = re.compile(r"\(?[A-Da-d]\)?\s*[-–—:]\s*\(?(?:[ivx]+|\d)\)?", re.IGNORECASE)
# A ratio is `a : b`. A LaTeX FRACTION is not a ratio -- including \frac/\dfrac here mislabelled
# real Q-000009's gravitational-potential options (`$-\dfrac{16Gm}{R}$`) as `ratio` when they are
# plainly expressions, while real Q-000004 (`3 : 5`) is the genuine ratio shape. Confirmed against
# both real records.
_RATIO_RE = re.compile(r"(?<![\d.])\d+(?:\.\d+)?\s*:\s*\d+(?:\.\d+)?(?![\d.])")

# Units arrive BOTH as literal glyphs (μF, Ω, °C) and as LaTeX macros (\mu F, \Omega, \circ C) in
# this corpus -- real Q-000002's options are `$2\,\mu F$`, which the glyph-only pattern missed
# entirely and so fell through to `expression`. Both spellings are matched deliberately.
_LATEX_UNIT = r"\\mu\s*[FHAWV]|\\Omega|\\circ\s*C|\\text\{[^}]*\}"
_NUM_UNIT_RE = re.compile(
    r"\d[^A-Za-z]{0,12}(?:"
    r"m|cm|mm|km|nm|s|ms|kg|g|mg|N|J|W|V|A|C|K|Pa|atm|mol|L|ml|Hz|kHz|MHz|eV|MeV|"
    r"Ω|ohm|μF|uF|pF|nF|μm|T|Wb|rad|°C|°"
    r")\b|\d[^A-Za-z]{0,12}(?:" + _LATEX_UNIT + r")")

_EXPR_RE = re.compile(r"[a-zA-Z]\s*[\^_]|\\sqrt|\\frac|\\dfrac|[+\-*/]\s*[a-zA-Z]|\$")

# `order` means a SEQUENCE (A < B < C, or a multi-step pathway "zygote → morula → blastula"), not
# a chemical transformation. A single arrow is a reaction ("CH3CN → product"); a genuine ordering
# chains two or more. Real Q-000005 (four one-arrow reactions) was mislabelled `order` before this
# distinction was drawn -- confirmed against the real record.
_ORDER_CMP_RE = re.compile(r"[<>]")
_ARROW_RE = re.compile(r"→|->|\\rightarrow|\\xrightarrow")


def _looks_like_order(option_text):
    if _ORDER_CMP_RE.search(option_text):
        return True
    return len(_ARROW_RE.findall(option_text)) >= 2


def answer_form(rec):
    """Which KIND of thing the options are. Order matters: a combination code like "A and D only"
    also contains words, and a ratio like "3 : 5" also contains digits, so the most specific
    shapes are tested first."""
    opts = _options(rec)
    if not opts:
        return None
    option_images = rec.get("option_images") or {}
    if option_images:
        kinds = " ".join(str(v) for v in option_images.values()).lower()
        return "graph_image" if "graph" in kinds else "structure_image"

    def most(pred):
        return sum(1 for o in opts if pred(o)) >= max(2, len(opts) - 1)

    if most(lambda o: _LETTER_COMBO_RE.search(o)):
        return "combination_code"
    if most(lambda o: _MATCH_CODE_RE.search(o)):
        return "match_code"
    if most(_looks_like_order):
        return "order"
    if most(lambda o: _RATIO_RE.search(o)):
        return "ratio"
    if most(lambda o: _NUM_UNIT_RE.search(o)):
        return "number_with_unit"
    if most(lambda o: _EXPR_RE.search(o)):
        return "expression"
    # A full clause is a statement; a short noun phrase is a term.
    if most(lambda o: len(o.split()) >= 5):
        return "statement"
    return "term"


# ---------------------------------------------------------------------------
# negation -- from B3's negative_words (spec: "none/single/double")
# ---------------------------------------------------------------------------


def negation(rec):
    """Counts DISTINCT negative words, not occurrences. "double" means the question carries two
    different negatives (the genuinely trap-prone shape, e.g. "which is NOT incorrect"); the same
    word repeated is still one negation."""
    seen = rec.get("negative_words")
    if seen is None:
        seen = rec.get("negative_words_seen")
    if seen:
        distinct = {str(w).strip().upper() for w in seen if str(w).strip()}
    else:
        # B3 may not have populated the field; fall back to reading the real stem.
        text = _stem_and_statements(rec).upper()
        distinct = {w for w in _NEGATIVE_WORDS if re.search(rf"\b{w}\b", text)}
    n = len(distinct)
    return "none" if n == 0 else ("single" if n == 1 else "double")


# ---------------------------------------------------------------------------
# item_count -- spec: "lettered statements or list rows only; items inside one sentence count as 0"
# ---------------------------------------------------------------------------


def item_count(rec):
    """Only *structurally* separate items count. The spec is explicit that items listed inside a
    single sentence count as 0 -- which is why real "How many plants among the following are
    monocots?" (a sentence listing items inline) is 0, not 4. So this counts B3's parsed
    `statements` / `list_i` / `list_ii` arrays and never re-parses prose."""
    statements = rec.get("statements") or []
    list_i = rec.get("list_i") or []
    list_ii = rec.get("list_ii") or []
    if statements:
        return len(statements)
    if list_i or list_ii:
        return max(len(list_i), len(list_ii))
    return 0


# ---------------------------------------------------------------------------
# constants_given -- spec: '"Given:", "[Take …]", "(At. no. …)"'
# ---------------------------------------------------------------------------

_CONSTANTS_RES = (
    re.compile(r"\bGiven\s*:", re.IGNORECASE),
    re.compile(r"\[\s*Take\b", re.IGNORECASE),
    re.compile(r"\(\s*At\.?\s*no\.?", re.IGNORECASE),
    re.compile(r"\(\s*Atomic\s+(?:number|mass)", re.IGNORECASE),
    re.compile(r"\bTake\s+g\s*=", re.IGNORECASE),
    re.compile(r"\bUse\s+[a-zA-Z]\s*=", re.IGNORECASE),
)


def constants_given(rec):
    text = _stem_and_statements(rec)
    return any(r.search(text) for r in _CONSTANTS_RES)


# ---------------------------------------------------------------------------
# figure_role -- spec: none / needed / decorative / options_are_figures
# ---------------------------------------------------------------------------

_FIG_REFERENCED_RE = re.compile(
    r"\bfigure\b|\bfig\.|\bshown\b|\bdiagram\b|\bgraph\b|\bcircuit\b|\bgiven\s+below\b|"
    r"\bfollowing\s+reaction\b|\bstructure\b", re.IGNORECASE)


def figure_role(rec):
    """`decorative` is deliberately never returned by the script. Deciding a figure is decorative
    means asserting the question is answerable without it -- a judgement, and a consequential one
    (B6 refuses any `has_figure` question as image-unsafe, so calling a figure decorative would
    silently widen what the blind solver is asked to do). The script reports `needed` whenever a
    figure exists, leaving any downgrade to a person in Stage F."""
    if rec.get("option_images"):
        return "options_are_figures"
    if not rec.get("has_figure"):
        return "none"
    return "needed"


# ---------------------------------------------------------------------------
# stem_context -- spec names the patterns; ambiguous cases go to the agent
# ---------------------------------------------------------------------------

_CTX_TABLE_RE = re.compile(r"\btable\b|\bcolumn\b", re.IGNORECASE)
# `reactions?` not `reaction`: real Q-000005's stem says "Which of the following reactionS will
# NOT give primary amine" and the singular-only pattern missed it entirely. Confirmed against the
# real record, not hypothesised.
_CTX_REACTION_RE = re.compile(r"→|->|\\rightarrow|\\xrightarrow|\breactions?\b", re.IGNORECASE)
_CTX_EQUATION_RE = re.compile(r"=\s*0\b|\bequation\b|\busing\s+the\s+(?:formula|equation)\b",
                              re.IGNORECASE)
_CTX_STUDENT_RE = re.compile(r"\ba\s+student\b|\bexperiment\b|\bobserved\b|\bapparatus\b|"
                             r"\bmeasure[sd]?\b|\bset\s*-?\s*up\b", re.IGNORECASE)
_CTX_HISTORICAL_RE = re.compile(r"\b(?:18|19|20)\d{2}\b|\bdescribed\s+for\s+the\s+first\s+time\b|"
                                r"\bdiscovered\s+by\b|\bproposed\s+by\b", re.IGNORECASE)
_CTX_DATA_RE = re.compile(r"\bnatality\b|\bmortality\b|\bthe\s+following\s+data\b|\bdata\s*:",
                          re.IGNORECASE)


def stem_context(rec):
    """Return (value, why) or (None, why) -- None means the `e6-context-tagger` agent must decide.

    Only the spec's own unambiguous patterns are claimed here. The spec's tie-break ("if two
    apply, choose the one the question cannot be answered without") is a real judgement, so when
    two patterns both fire this returns None instead of imposing an invented priority.

    The reaction test also reads the OPTIONS, not just the stem: real Q-000005 keeps its reaction
    arrows entirely in its four options ("$\\mathrm{CH_3CN} \\rightarrow$ ..."), so a stem-only
    span could never see them and the question came out `plain`. Every other pattern stays
    stem-scoped on purpose -- a figure or a date mentioned only in an option does not make the
    stem's context."""
    text = _stem_and_statements(rec)
    options_text = " ".join(str(v) for v in (rec.get("options_en") or {}).values())

    hits = []
    if _CTX_DATA_RE.search(text):
        hits.append(("data_given", "explicit data in the stem"))
    if _CTX_TABLE_RE.search(text) and (rec.get("list_i") or rec.get("list_ii")):
        hits.append(("table_given", "table/column wording with parsed list rows"))
    if _CTX_REACTION_RE.search(text) or _CTX_REACTION_RE.search(options_text):
        hits.append(("reaction_given", "reaction arrow or wording"))
    if _CTX_EQUATION_RE.search(text):
        hits.append(("equation_given", "an equation to use"))
    if _CTX_STUDENT_RE.search(text):
        hits.append(("experiment_setup", "a student/experiment/observation setup"))
    if _CTX_HISTORICAL_RE.search(text):
        hits.append(("historical", "a scientist or date"))
    if rec.get("has_figure"):
        hits.append(("figure_given", "a figure accompanies the stem"))

    if not hits:
        return "plain", "no context pattern matched"
    if len(hits) == 1:
        return hits[0][0], hits[0][1]
    return None, ("several contexts apply (" + ", ".join(h[0] for h in hits) +
                  ") -- spec's tie-break needs judgement, agent decides")


# ---------------------------------------------------------------------------
# assemble
# ---------------------------------------------------------------------------


def describe(rec):
    ctx, ctx_why = stem_context(rec)
    return {
        "answer_form": answer_form(rec),
        "negation": negation(rec),
        "item_count": item_count(rec),
        "constants_given": constants_given(rec),
        "figure_role": figure_role(rec),
        "stem_context": ctx,
        "stem_context_why": ctx_why,
        "needs_agent_for_stem_context": ctx is None,
    }


# ---------------------------------------------------------------------------
# self-test: spec-named cases + real records
# ---------------------------------------------------------------------------

_CASES = [
    ("spec 13/E6 example: natality/mortality figures -> data_given, not case_scenario",
     {"stem_en": "A biologist studied a population of rats. The natality is 250 and mortality 240.",
      "options_en": {"1": "+10", "2": "-10", "3": "0", "4": "250"}},
     {"stem_context": "data_given"}),

    ("spec 13/E6: items inside one sentence count as 0",
     {"stem_en": "How many plants among the following are monocots: wheat, rice, maize, pea?",
      "options_en": {"1": "2", "2": "3", "3": "4", "4": "5"}},
     {"item_count": 0}),

    ("REAL Q-000015: 4 lettered statements, combination options",
     {"stem_en": "Which of the following statements are correct regarding female reproductive cycle?",
      "structure": "statements", "has_figure": False, "negative_words": [],
      "statements": [{"label": "A", "text": "oestrus cycle"}, {"label": "B", "text": "menopause"},
                     {"label": "C", "text": "pregnancy"}, {"label": "D", "text": "menarche"}],
      "options_en": {"1": "A and D only", "2": "A and B only", "3": "A, B and C only",
                     "4": "A, C and D only"}},
     {"item_count": 4, "answer_form": "combination_code", "negation": "none",
      "figure_role": "none"}),

    ("REAL Q-000005: a NOT question whose options are reactions",
     {"stem_en": "Which of the following reactions will NOT give primary amine as the product?",
      "has_figure": False,
      "options_en": {"1": r"$\mathrm{CH_3CONH_2} \rightarrow \mathrm{Br_2}$ Product",
                     "2": r"$\mathrm{CH_3CN} \rightarrow$ (i) $\mathrm{LiAlH_4}$ Product",
                     "3": r"$\mathrm{CH_3NC} \rightarrow$ (i) $\mathrm{LiAlH_4}$ Product",
                     "4": r"$\mathrm{CH_3CONH_2} \rightarrow$ (i) $\mathrm{LiAlH_4}$ Product"}},
     {"negation": "single", "figure_role": "none"}),

    ("a figure question -> figure_role needed, never decorative from a script",
     {"stem_en": "The equivalent capacitance of the system shown in the following figure is",
      "has_figure": True,
      "options_en": {"1": r"$2\,\mu F$", "2": r"$3\,\mu F$", "3": r"$6\,\mu F$",
                     "4": r"$9\,\mu F$"}},
     {"figure_role": "needed", "answer_form": "number_with_unit"}),

    ("constants given in brackets",
     {"stem_en": "Find the escape velocity. [Take g = 9.8 m/s^2]",
      "options_en": {"1": "11.2 km/s", "2": "7.9 km/s", "3": "2.4 km/s", "4": "1.0 km/s"}},
     {"constants_given": True}),

    ("REAL Q-000004: `3 : 5` really is a ratio",
     {"stem_en": "The ratio of radius of gyration of a solid sphere of mass M and radius R is",
      "has_figure": False,
      "options_en": {"1": "3 : 5", "2": "5 : 3", "3": "2 : 5", "4": "5 : 2"}},
     {"answer_form": "ratio"}),

    ("REAL Q-000009: a LaTeX FRACTION is an expression, not a ratio",
     {"stem_en": r"Two bodies of mass $m$ and $9m$ are placed at a distance $R$. "
                 r"The gravitational potential is",
      "has_figure": False,
      "options_en": {"1": r"$-\dfrac{8Gm}{R}$", "2": r"$-\dfrac{12Gm}{R}$",
                     "3": r"$-\dfrac{16Gm}{R}$", "4": r"$-\dfrac{20Gm}{R}$"}},
     {"answer_form": "expression"}),

    ("REAL Q-000002: LaTeX-encoded unit `$2\\,\\mu F$` is number_with_unit, not expression",
     {"stem_en": "The equivalent capacitance of the system shown in the following figure is",
      "has_figure": True,
      "options_en": {"1": r"$2\,\mu F$", "2": r"$3\,\mu F$", "3": r"$6\,\mu F$",
                     "4": r"$9\,\mu F$"}},
     {"answer_form": "number_with_unit"}),

    ("two distinct negatives -> double",
     {"stem_en": "Which of the following is NOT an INCORRECT statement about enzymes?",
      "options_en": {"1": "They are proteins and speed up reactions markedly",
                     "2": "They are consumed entirely during the reaction they catalyse",
                     "3": "They work best outside their optimum temperature range",
                     "4": "They change the equilibrium constant of the reaction"}},
     {"negation": "double"}),
]


def _self_test():
    failures = []
    for name, rec, expected in _CASES:
        got = describe(rec)
        bad = {k: (v, got.get(k)) for k, v in expected.items() if got.get(k) != v}
        print(f"{'ok  ' if not bad else 'FAIL'}  {name}")
        if bad:
            for k, (exp, actual) in bad.items():
                print(f"        {k}: expected {exp!r}, got {actual!r}")
            failures.append(name)
    print()
    if failures:
        print(f"{len(failures)} of {len(_CASES)} FAILED")
        return 1
    print(f"all {len(_CASES)} cases pass")
    return 0


def _load(qid):
    path = rc.pp("papers", "records", f"{qid}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main(argv=None):
    ap = argparse.ArgumentParser(description="E6 descriptive tags, SCRIPT half (spec 13/E6).")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--item-id")
    g.add_argument("--all", action="store_true")
    g.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return _self_test()

    if args.item_id:
        rec = _load(args.item_id)
        if not rec:
            print(f"no record for {args.item_id}", file=sys.stderr)
            return 2
        print(json.dumps({"question_id": args.item_id, **describe(rec)}, indent=2))
        return 0

    records_dir = rc.pp("papers", "records")
    need_agent = 0
    rows = 0
    print(f"{'QID':<10} {'answer_form':<17} {'neg':<7} {'items':>5}  {'const':<5} "
          f"{'figure_role':<19} stem_context")
    for fn in sorted(os.listdir(records_dir)):
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        rec = _load(fn[: -len(".json")])
        if not isinstance(rec, dict) or rec.get("merged_into"):
            continue
        d = describe(rec)
        rows += 1
        if d["needs_agent_for_stem_context"]:
            need_agent += 1
        print(f"{rec.get('question_id'):<10} {str(d['answer_form']):<17} {d['negation']:<7} "
              f"{d['item_count']:>5}  {str(d['constants_given']):<5} "
              f"{d['figure_role']:<19} {d['stem_context'] or 'NEEDS-AGENT'}")
    print(f"\n{rows} canonical questions; {need_agent} need a real agent call for stem_context.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
