"""Step-specific check for E6 (spec Section 13/E6 + codebook/E6.md + scripts/describe_tags.py).

E6 is five script-owned fields plus ONE agent question. Spec 13/E6: the SCRIPT fills `answer_form`,
`negation`, `item_count`, `constants_given`, `figure_role` and `stem_context` BY PATTERNS, and
the `e6-context-tagger` AGENT is called for `stem_context` only, and only when the patterns do not
decide. schemas/E6.json covers that one agent output. This file adds:

  (1) THE AGENT MUST ONLY BE RUNNING WHEN THE SCRIPT HANDED OVER. `describe_tags.stem_context()`
      is re-run on the real record; if it returned a value, the item should never have been
      dispatched and a judgement would be silently replacing a deterministic classification.
      On the real bank today exactly ONE of the 10 canonical questions reaches the agent
      (Q-000013, where `reaction_given` and `figure_given` both fire), so this is the common case.

  (2) `plain` CAN NEVER WIN A TIE-BREAK. codebook/E6.md §2: "`plain` is never a tie-break winner.
      If anything genuinely applies, `plain` is wrong." The agent is only called when two or more
      context patterns fired, so by construction something applies. This is a real failure, not a
      style note.

  (3) `why` MUST ACCOUNT FOR THE TIE-BREAK. Spec 13/E6's rule is "if two apply, choose the one the
      question cannot be answered without", and that is the only reason this agent exists. So
      `why` must be a real sentence (>= 4 words). A script cannot verify that the right one was
      chosen; it can refuse a sentence that explains nothing.

  (4) A CHOICE OUTSIDE THE SCRIPT'S CANDIDATES IS REPORTED, NOT FAILED. The agent may legitimately
      see a framing no regex covers -- codebook/E6.md §4.2 records two real cases where the
      script's own patterns under-detect (`Q-000003`, a football player turning, arguably
      `case_scenario`; `Q-000001`, a wire suspended and loaded, arguably `experiment_setup`). So a
      value outside the fired set is carried in the passing message for Stage F to see, never
      failed. Only `plain` is failed, per (2).

  (5) `unsure` IS A LEGITIMATE OUTCOME, NOT A FAILURE. Spec 13/E6's "On failure" line is
      `E6_CONTEXT_UNSURE` (low) -- a flag. Retrying an agent that honestly could not apply the
      tie-break would just produce a confident guess, which is worse.

WHAT IS DELIBERATELY NOT HERE: any check on the five script-owned fields. They are produced by
scripts/describe_tags.py, not by an agent, so there is no agent output to validate -- and
re-deriving them here to compare against themselves would be circular. Their real values for all
10 canonical records are recorded in codebook/E6.md §3, and describe_tags.py's own `--self-test`
(10 cases, all passing) is where those rules are regression-tested.

ONE REAL DISCREPANCY FOUND BETWEEN codebook/E6.md AND scripts/describe_tags.py, reported not
silently reconciled: codebook/E6.md §4.2 states that `_CTX_REACTION_RE` "misses the plural" and
that a question whose four options are reactions is therefore tagged `plain`. The script does NOT
have that defect -- its pattern is `reactions?` and its reaction test deliberately reads the
OPTIONS as well as the stem, with a comment recording that exact real Q-000005 fix. So the
codebook's §4.2 describes a pre-fix state. Per codebook/E6.md's own STATUS rule ("A disagreement
between this file and that script is a bug -- report it, do not pick a side"), it is reported here
and in the build report. The script is the one that matches real data.

Convention: def check(data, context) -> (bool, str), ';'-joined segments.
"""
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import describe_tags  # noqa: E402
from lib import records as lib_records  # noqa: E402

MIN_WHY_WORDS = 4


def question_record(context):
    """The real question record. Prefers context["input_data"]["record"]; falls back to
    papers/records/<QID>.json so this check is testable against real data before the E plugins
    exist. {} when neither is available."""
    rec = (context.get("input_data") or {}).get("record")
    if isinstance(rec, dict) and rec:
        return rec
    qid = str(context.get("item_id") or "").split("#")[0]
    if not qid:
        return {}
    # lib_records.read_record() returns a SKELETON {"question_id", "field_sources"} when the
    # record does not exist, which would read here as a real-but-empty record and SILENTLY skip
    # every rule that needs real fields. Test the file itself instead. (Real gotcha found by
    # tests/test_e_checks.py, 2026-10-12.)
    if not os.path.exists(lib_records.record_path(qid)):
        return {}
    try:
        return lib_records.read_record(qid) or {}
    except Exception:  # noqa: BLE001 -- an unreadable record is a reported skip, never a crash
        return {}


def check(data, context):
    if not isinstance(data, dict):
        return False, "E6 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    stem_context = data.get("stem_context")
    why = (data.get("why") or "").strip()
    segments = []
    notes = []

    # (3) `why` substance.
    if len(why.split()) < MIN_WHY_WORDS:
        segments.append(
            f"why is {len(why.split())} word(s) ({why!r}); this agent only runs when two or more "
            f"contexts apply, so `why` must say which were in play and why the chosen one is the "
            f"one the question cannot be answered without")

    record = question_record(context)
    if not record:
        segments.append(
            "no question record available (neither context['input_data']['record'] nor "
            "papers/records/<QID>.json), so neither the script-handed-over check nor the "
            "tie-break check could run")
        return False, "; ".join(segments)

    script_value, script_why = describe_tags.stem_context(record)

    # (1) the agent must only run when the patterns did not decide.
    if script_value is not None:
        segments.append(
            f"scripts/describe_tags.py already decides this stem as {script_value!r} "
            f"({script_why}), so spec 13/E6 says the agent must not run for it at all; the agent "
            f"answered {stem_context!r}")
    else:
        # `script_why` lists the contexts that fired, e.g. "several contexts apply (a, b) -- ..."
        candidates = _candidates_from_why(script_why)

        # (2) plain can never win a tie-break.
        if stem_context == "plain":
            segments.append(
                f"stem_context is `plain` but {len(candidates) or 'several'} contexts actually "
                f"apply ({', '.join(candidates) or script_why}); `plain` is never a tie-break "
                f"winner -- if anything genuinely applies, `plain` is wrong (codebook/E6.md §2)")
        # (4) a value outside the fired set is legitimate but worth seeing.
        elif candidates and stem_context not in candidates and stem_context != "unsure":
            notes.append(
                f"note: {stem_context!r} is not one of the contexts the script's patterns found "
                f"({', '.join(candidates)}); legitimate -- the script is known to under-detect "
                f"(codebook/E6.md §4.2) -- but worth a Stage F look")
        # (5) unsure is an outcome, not a failure.
        if stem_context == "unsure":
            notes.append("note: stem_context is `unsure` -> E6_CONTEXT_UNSURE (low); an honest "
                         "unsure is better than a confident guess")

    if segments:
        return False, "; ".join(segments)
    return True, "; ".join(["ok"] + notes)


def _candidates_from_why(script_why):
    """The context values describe_tags.stem_context() reported as having fired.

    Its hand-over message is literally "several contexts apply (a, b, c) -- spec's tie-break needs
    judgement, agent decides", so the candidate list is read out of the parenthesis. Returns []
    when the message has no list, in which case the checks above degrade to reporting the raw
    message rather than asserting anything about a list they could not read."""
    if not script_why or "(" not in script_why or ")" not in script_why:
        return []
    inner = script_why[script_why.index("(") + 1:script_why.rindex(")")]
    return [part.strip() for part in inner.split(",") if part.strip()]
