"""Step-specific check for D8 (spec Section 12/D8 'Style' + d8-fact-line-writer.md's own rules).

spec 12/D8 names no "Checks" list of its own — only a Style block and one failure mode ("low
confidence -> D8_LOW_CONFIDENCE (low)"). schemas/D8.json already pins the {fact_line, facts,
confidence} shape and the confidence enum. This file checks the parts of that Style block a
script can honestly verify, and says plainly which parts it cannot.

CHECKED:
  (1) "no option numbers" -- an explicit reference to an option by number ("option 3",
      "Option (2)") or a bare leading "(3)". A fact line is a statement about the world; it must
      survive being read with no options in front of you.
  (2) "no 'which of the following'" -- the exact phrase, case-insensitive. This is the single
      most common way a fact line degenerates back into the question it came from.
  (3) Statement questions: spec 12/D8 Style, verbatim: "Statement questions: the fact of each
      TRUE statement joined by ' | '". So when the record's `structure` is "statements"
      (context["input_data"]["structure"]), `facts` must be non-empty and fact_line must be
      exactly " | ".join(facts). This is a real content check, not cosmetics -- D9 reads `facts`
      item by item to find a statement-question repeat ("Include a statement question if any one
      of its facts matches"), so a fact_line that disagrees with `facts` quietly breaks D9.
  (4) Numericals: spec 12/D8 Style, verbatim: "Numericals: 'Problem: <setup in general terms>.
      Rule: <formula>.'". A question is treated as a numerical here when D4 produced derivation
      steps for it (context["input_data"]["d4_has_derivation"]) -- the only mechanical signal in
      the record that real arithmetic was needed. Then fact_line must start with "Problem:" and
      contain "Rule:".

DELIBERATELY NOT CHECKED, and why:
  - "Present tense, subject first, NCERT's own term." Grammatical/stylistic judgements; a regex
    that tried would produce false failures on legitimate lines and teach the agent nothing.
  - "Never include ... specific numbers of a numerical." Cannot be done by looking for digits:
    real NCERT formulas contain them (`v = u + at`, `E = mc^2`, `1/2 mv^2`, "R is proportional to
    l squared"). A digit test would fail correct output more often than wrong output.
  - "Never include year." Also not a digit test, and not even a year test: a legitimate fact can
    BE about a year. Spec's own real `outside_ncert` example is 2015#180, the venue of the 2012
    UN climate conference -- whose fact line must name 2012 to be a fact at all.
  Both of the last two are left to the reviewer via Stage F, which is where spec puts style
  approval anyway.

Convention: def check(data, context) -> (bool, str). Segments are ';'-joined, each prefixed with
one of this step's own config/steps.yaml flag codes: D8_STYLE (low) for the cosmetic breaches --
the line is still a usable fact line, it just reads like the question -- and D8_FACTS_MISMATCH
(normal) for (3), which is not cosmetic at all. Spec 12/D8's own catalogued flag
(D8_LOW_CONFIDENCE, low) is about confidence rather than any of these rules, and is raised
unconditionally by step_plugins.D8Plugin on the resolved value.
"""
import re

_WHICH_OF_THE_FOLLOWING_RE = re.compile(r"which\s+of\s+the\s+following", re.IGNORECASE)
_OPTION_NUMBER_RE = re.compile(r"\boptions?\s*\(?\s*[1-4]\s*\)?", re.IGNORECASE)
_LEADING_OPTION_RE = re.compile(r"^\s*\(?\s*[1-4]\s*\)\s*")


def check(data, context):
    if not isinstance(data, dict):
        return False, "D8 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    fact_line = data.get("fact_line")
    facts = data.get("facts")
    if not isinstance(fact_line, str) or not fact_line.strip():
        return False, "fact_line is empty"
    if not isinstance(facts, list):
        return False, "facts is not a list"

    input_data = context.get("input_data") or {}
    structure = input_data.get("structure")
    d4_has_derivation = bool(input_data.get("d4_has_derivation"))

    segments = []

    if _WHICH_OF_THE_FOLLOWING_RE.search(fact_line):
        segments.append(
            "D8_STYLE: fact_line contains 'which of the following'; a fact line states the fact, "
            "it does not re-ask the question"
        )

    m = _OPTION_NUMBER_RE.search(fact_line)
    if m:
        segments.append(
            f"D8_STYLE: fact_line refers to an option by number ({m.group(0)!r}); it must not"
        )
    elif _LEADING_OPTION_RE.match(fact_line):
        segments.append("D8_STYLE: fact_line starts with a bare option number; it must not")

    if structure == "statements":
        if not facts:
            segments.append(
                "D8_FACTS_MISMATCH: this is a statement question, so `facts` must list the fact "
                "of each TRUE statement (spec 12/D8 Style); it is empty"
            )
        else:
            expected = " | ".join(f.strip() for f in facts)
            if " | ".join(p.strip() for p in fact_line.split("|")) != expected:
                segments.append(
                    "D8_FACTS_MISMATCH: fact_line is not the ' | '-join of `facts` -- D9 matches "
                    "a statement question fact by fact, so the two must agree exactly"
                )

    if d4_has_derivation:
        if not fact_line.strip().startswith("Problem:"):
            segments.append(
                "D8_STYLE: D4 produced derivation steps for this question (it is a numerical), "
                "so fact_line must start with 'Problem:' (spec 12/D8 Style)"
            )
        if "Rule:" not in fact_line:
            segments.append(
                "D8_STYLE: D4 produced derivation steps for this question (it is a numerical), "
                "so fact_line must name the rule after 'Rule:' (spec 12/D8 Style)"
            )

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
