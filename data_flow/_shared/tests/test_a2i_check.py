#!/usr/bin/env python3
"""Self-tests for scripts/checks/A2I.py (step A2I, the italic-term backfill).

scripts/checks/A2B.py -- the step A2I was cloned from -- has no test harness of its own, so this
file is written fresh for A2I. It covers every property the check promises, each as one case that
must FAIL (plus a good record that must PASS), so a future change that quietly drops one of them
fails here instead of passing in silence:

  1. a good record passes
  2. a term that is not present in the block's `text` fails
  3. a duplicate term within one block fails
  4. a term that is also in that block's `bold_terms` fails
  5. a block the input asked for but the output omits fails
  6. an empty (or nothing-saying) `note` fails

Plus the surrounding guards: an `error` payload, a non-object payload, a block `n` the input never
asked for, the same `n` covered twice, an empty-string term, an input naming no blocks at all,
and the case-only-difference message (A2I compares verbatim where A2B lowercases).

The fixture is the real page the step exists because of: PHY12O-ch01 page 1, whose italic
definition sentence and italic etymology were seen by the bold-term marker, judged correctly, and
then lost to a free-text note because there was nowhere to record them.

Run: .venv/bin/python3 tests/test_a2i_check.py   (or via pytest tests/)
"""
import os
import sys

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_TESTS_DIR)
_SCRIPTS_DIR = os.path.join(_PROJECT_ROOT, "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from checks import A2I as a2i_check  # noqa: E402

# Verbatim from steps/A2/out/PHY12O-ch01-p001.runA.json, blocks n=4 and n=6 (truncated for n=4 at
# a sentence boundary; the italic sentence itself is complete).
_N4 = ("This is precisely the topic we are going to discuss in this and the next chapter. Static "
       "means anything that does not move or change with time. Electrostatics deals with the "
       "study of forces, fields and potentials arising from static charges.")
_N6 = ("Historically the credit of discovery of the fact that amber rubbed with wool or silk "
       "cloth attracts light objects goes to Thales of Miletus, Greece, around 600 BC. The name "
       "electricity is coined from the Greek word elektron meaning amber. Many such pairs of "
       "materials were known which")
_ITALIC_N4 = ("Electrostatics deals with the study of forces, fields and potentials arising from "
              "static charges")


def _context(blocks=None):
    """A2I's check reads only context['input_data']['blocks'] -- the read-only view of the A2
    page that step_plugins.A2IPlugin hands the agent."""
    if blocks is None:
        blocks = [
            {"n": 4, "kind": "paragraph", "text": _N4, "bold_terms": []},
            {"n": 6, "kind": "paragraph", "text": _N6, "bold_terms": []},
        ]
    return {"item_id": "PHY12O-ch01-p001", "step": "A2I", "input_data": {"blocks": blocks}}


_GOOD_NOTE = ("n=4 closes with the chapter's own italic definition of electrostatics; n=6 "
              "italicises the Greek etymology elektron and the word amber it names.")

CASES = []


def case(name, data, context, want_pass, want_in_message=None):
    CASES.append((name, data, context, want_pass, want_in_message))


# --- 1. a good record passes -------------------------------------------------------------
case(
    "good record passes",
    {"blocks": [{"n": 4, "italic_terms": [_ITALIC_N4]},
                {"n": 6, "italic_terms": ["elektron", "amber"]}],
     "note": _GOOD_NOTE},
    _context(), True, "2 block(s) covered, 3 italic term(s) found",
)
case(
    "nothing italic anywhere still passes, with a real note",
    {"blocks": [{"n": 4, "italic_terms": []}, {"n": 6, "italic_terms": []}],
     "note": "Both paragraphs are plain roman throughout; no italic prose on this page."},
    _context(), True, "0 italic term(s) found",
)

# --- 2. a term not present in `text` fails -----------------------------------------------
case(
    "term absent from the block's text fails",
    {"blocks": [{"n": 4, "italic_terms": ["Electrodynamics deals with the study of forces"]},
                {"n": 6, "italic_terms": []}],
     "note": _GOOD_NOTE},
    _context(), False, "does not appear in the block's own source text",
)
case(
    "term retyped with different punctuation fails",
    {"blocks": [{"n": 6, "italic_terms": ["elektron,"]}, {"n": 4, "italic_terms": []}],
     "note": _GOOD_NOTE},
    _context(), False, "does not appear in the block's own source text",
)
case(
    "term differing only in capitalisation fails, and says so",
    {"blocks": [{"n": 6, "italic_terms": ["Elektron"]}, {"n": 4, "italic_terms": []}],
     "note": _GOOD_NOTE},
    _context(), False, "different capitalisation",
)

# --- 3. a duplicate term fails -----------------------------------------------------------
case(
    "same term listed twice in one block fails",
    {"blocks": [{"n": 6, "italic_terms": ["elektron", "amber", "elektron"]},
                {"n": 4, "italic_terms": []}],
     "note": _GOOD_NOTE},
    _context(), False, "more than once",
)

# --- 4. a term that is also in bold_terms fails ------------------------------------------
case(
    "term already recorded as bold fails",
    {"blocks": [{"n": 6, "italic_terms": ["elektron"]}, {"n": 4, "italic_terms": []}],
     "note": _GOOD_NOTE},
    _context([{"n": 4, "kind": "paragraph", "text": _N4, "bold_terms": []},
              {"n": 6, "kind": "paragraph", "text": _N6, "bold_terms": ["elektron"]}]),
    False, "already records it as BOLD",
)
case(
    "a DIFFERENT bold term on the same block does not block a real italic term",
    {"blocks": [{"n": 6, "italic_terms": ["elektron"]}, {"n": 4, "italic_terms": []}],
     "note": _GOOD_NOTE},
    _context([{"n": 4, "kind": "paragraph", "text": _N4, "bold_terms": []},
              {"n": 6, "kind": "paragraph", "text": _N6, "bold_terms": ["electricity"]}]),
    True, "1 italic term(s) found",
)

# --- 5. a missing block fails ------------------------------------------------------------
case(
    "block asked for but not reported on fails",
    {"blocks": [{"n": 4, "italic_terms": [_ITALIC_N4]}], "note": _GOOD_NOTE},
    _context(), False, "were not reported on: n=[6]",
)

# --- 6. an empty note fails --------------------------------------------------------------
case(
    "empty note fails",
    {"blocks": [{"n": 4, "italic_terms": [_ITALIC_N4]},
                {"n": 6, "italic_terms": ["elektron", "amber"]}],
     "note": ""},
    _context(), False, "note is empty or says nothing reviewable",
)
case(
    "nothing-saying note fails",
    {"blocks": [{"n": 4, "italic_terms": []}, {"n": 6, "italic_terms": []}],
     "note": "none."},
    _context(), False, "note is empty or says nothing reviewable",
)
case(
    "missing note fails",
    {"blocks": [{"n": 4, "italic_terms": []}, {"n": 6, "italic_terms": []}]},
    _context(), False, "note is empty or says nothing reviewable",
)

# --- surrounding guards ------------------------------------------------------------------
case("agent error payload fails", {"error": "input file not found"}, _context(), False,
     "agent reported error")
case("non-object payload fails", ["blocks"], _context(), False, "is not an object")
case("blocks not an array fails", {"blocks": {"n": 4}, "note": _GOOD_NOTE}, _context(), False,
     "blocks is not an array")
case(
    "an n the input never asked for fails",
    {"blocks": [{"n": 4, "italic_terms": []}, {"n": 6, "italic_terms": []},
                {"n": 9, "italic_terms": ["something"]}],
     "note": _GOOD_NOTE},
    _context(), False, "which this item's input did not ask for",
)
case(
    "the same n covered twice fails",
    {"blocks": [{"n": 4, "italic_terms": []}, {"n": 4, "italic_terms": []},
                {"n": 6, "italic_terms": []}],
     "note": _GOOD_NOTE},
    _context(), False, "is covered twice",
)
case(
    "italic_terms not an array fails",
    {"blocks": [{"n": 4, "italic_terms": "elektron"}, {"n": 6, "italic_terms": []}],
     "note": _GOOD_NOTE},
    _context(), False, "is not an array",
)
case(
    "empty-string term fails",
    {"blocks": [{"n": 4, "italic_terms": ["   "]}, {"n": 6, "italic_terms": []}],
     "note": _GOOD_NOTE},
    _context(), False, "empty or non-string italic term",
)
case(
    "an input naming no blocks at all fails",
    {"blocks": [], "note": _GOOD_NOTE},
    _context([]), False, "names no blocks to cover",
)


def main():
    failures = []
    for name, data, context, want_pass, want_in_message in CASES:
        try:
            ok, msg = a2i_check.check(data, context)
        except Exception as exc:  # a check must never raise -- that is itself a failure
            failures.append(f"{name}: check() raised {type(exc).__name__}: {exc}")
            continue
        if not isinstance(ok, bool) or not isinstance(msg, str):
            failures.append(f"{name}: check() returned {(ok, msg)!r}, not (bool, str)")
            continue
        if ok != want_pass:
            failures.append(f"{name}: expected pass={want_pass}, got pass={ok} ({msg})")
            continue
        if want_in_message and want_in_message not in msg:
            failures.append(f"{name}: message {msg!r} does not contain {want_in_message!r}")
            continue
        print(f"  ok   {name}  ->  {'PASS' if ok else 'FAIL'}: {msg[:100]}")

    print()
    if failures:
        print(f"{len(failures)} of {len(CASES)} A2I check cases WRONG:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"all {len(CASES)} A2I check cases behave as specified")
    return 0


def test_a2i_check():
    """pytest entry point."""
    assert main() == 0


if __name__ == "__main__":
    sys.exit(main())
