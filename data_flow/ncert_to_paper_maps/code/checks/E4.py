"""Step-specific check for E4 (spec Section 13/E4 + codebook/E4.md) -- including the rule that
makes a BRANCH-BLIND Chemistry tagging impossible to pass silently.

schemas/E4.json already constrains `primary`/`secondary` to config/allowed_values.yaml's EIGHT
`thinking_draft` categories (the nine `thinking_candidates_for_owner` beside them are deliberately
excluded -- spec 17.5: "for E0 and the owner, not for E4 until a codebook includes them"), and
requires `codebook_version` and `branch_used`. This file adds everything else spec 13/E4's Checks
line and codebook/E4.md call for.

=== 1. THE BRANCH RULE (codebook/E4.md §1, the most-confirmed rule in Stage E) ===

Confirmed on 10 of 10 real papers with no exceptions: a Chemistry expectation must be conditioned
on B7's `branch`, NEVER on the word "Chemistry". Physical chemistry (kinetics, equilibrium,
electrochemistry, solutions, thermodynamics, atomic structure) behaves like Physics --
numerical/application. Organic and inorganic behave like Biology -- recall/elimination. The split
runs roughly 40-60% each way and varies by paper, so treating "Chemistry" as one bucket mis-tags a
large share of Chemistry questions in BOTH directions.

Nothing in spec 13/E4's five-field output records whether the agent ever looked at the branch, so
a branch-blind tagging would satisfy every enum and every structural rule in total silence. Three
checks close that, at the two places it can go wrong:

  (1a) THE WIRING. `context["input_data"]` must contain a `branch` key -- present even when its
       value is None. If the plugin never put the branch in the agent's input, the agent could not
       possibly have conditioned on it, and no amount of checking the OUTPUT would reveal that.
       This is the check that makes branch-blindness impossible rather than merely discouraged.
  (1b) THE AGENT. `branch_used` must equal the record's own `branch` verbatim ("none" when the
       record has no branch, as every Physics record has none). An agent that did not read the
       field cannot restate it.
  (1c) THE REASONING, as far as a script can reach it. For a Chemistry question whose tag
       CONTRADICTS its branch's prior, `why` must carry real substance -- codebook/E4.md §1: "If
       your tag contradicts the prior, that is normal -- say why in one clause and keep your tag."
       And for a Chemistry question whose branch is `unsure` or absent, `why` must say so --
       codebook/E4.md §1: "take no prior at all. Read the question cold. ... Say in `why` that the
       branch was unavailable." Both are the codebook's own instructions made mechanical.

A script cannot verify that a judgement was actually conditioned on the branch. It can verify that
the branch reached the agent, that the agent restated it, and that a contradiction was accounted
for. That is the whole of what is checkable, and it is implemented here in full.

NOTE: `branch` is NEVER used here to constrain the tag itself. The second rule in codebook/E4.md
§1 is that thinking can never be shortcut from question_type, format or subject -- confirmed in
both directions on real 2024 data (a Physics Assertion-Reason item needed a real calculation; a
Biology item that looked numerical was pure recall). A prior is a sanity check on a tag already
decided by reading, never evidence for one. So a Chemistry/organic question tagged `numerical`
passes -- it just has to say why.

=== 2. codebook_version (spec 13.0, and the E4_NO_CODEBOOK flag) ===

Spec 13.0: the runner records the codebook's file hash as `codebook_version` on every tag, or
"none" when the file is missing; spec 13/E4 additionally puts it in the agent's own output. So:

  * claimed "none" while `codebook/E4.md` EXISTS -> FAIL. The codebook never reached the agent.
    That is a wiring failure, it mis-tags at volume, and it is otherwise completely invisible. It
    is the real state of this build today: `config/steps.yaml` has `codebook_file: null` for E4
    even though the file exists (the YAML to fix it is in config/_pending_E_entries.yaml).
  * a claimed hash that is not the real one -> FAIL. The agent was given a different text than
    the file now holds, so the tag cannot be attributed to a codebook version.
  * real version "none" (file genuinely absent) and claimed "none" -> PASS, reported, so the
    plugin can raise E4_NO_CODEBOOK (low) straight from this message. Spec is explicit that E4
    runs on the eight draft categories in that case; it is not an error.

=== 3. The rest of spec 13/E4's Checks ===

  * `confidence: low` -> FAIL. Spec 13/E4 Checks says "confidence not low", and its On-failure
    line routes failures to the adjudicator (E4_ADJUDICATED, normal). The failure IS the designed
    escalation, not a complaint about the agent.
  * `secondary` must differ from `primary`, and must never be the OTHER HALF of the recall/
    elimination pair (codebook/E4.md §4: "Do not pair `recall` with `elimination`. Those are two
    points on one scale (how many facts), not two kinds of thinking.").
  * `why` must be a real sentence naming the specific hard step.

"Runs agree on primary and on whether a secondary exists" is cross-run, needs both outputs at
once, and therefore belongs in the plugin's own check() -- the same split as D1/D2/D11/A4. It is
specified in config/_pending_E_entries.yaml, not here.

Convention: def check(data, context) -> (bool, str), ';'-joined segments.
"""
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import codebook_version  # noqa: E402
from lib import records as lib_records  # noqa: E402

#: codebook/E4.md §1's confirmed table: which thinking the branch's own prior expects.
#: Chemistry ONLY -- the rule is about Chemistry never being one bucket. Physics and Biology have
#: their own subject-level priors in the codebook, but spec gives no branch for Physics and no
#: step assigns Biology's botany/zoology (see BIOLOGY_BRANCH_GAP below), so neither is keyed here.
CHEM_BRANCH_PRIOR = {
    "physical": ("calculation", "application"),     # behaves like Physics
    "organic": ("recall", "elimination"),          # behaves like Biology
    "inorganic": ("recall", "elimination"),        # behaves like Biology
}

#: Two points on one scale (how many facts), not two kinds of thinking -- codebook/E4.md §4.
FORBIDDEN_PAIR = frozenset({"recall", "elimination"})

#: `why` floors. The second applies when the tag contradicts its branch's prior, where the
#: codebook requires an explicit clause explaining the contradiction.
MIN_WHY_WORDS = 5
MIN_WHY_WORDS_AGAINST_PRIOR = 9

#: REAL TAXONOMY GAP, recorded not worked around (docs/OPEN_QUESTIONS.md 2026-10-12):
#: config/allowed_values.yaml defines Biology branches (botany/zoology) but the ONLY step that
#: assigns a branch is B7, the CHEM branch sorter, whose own allowed set is
#: physical/organic/inorganic/unsure. So every Biology record reads `unsure`, which means "no step
#: ever tried" rather than "a step tried and failed" -- real Q-000015 (the female reproductive
#: cycle) should be `zoology`. E4's branch rule is Chemistry-specific, so E4 is correct either
#: way; this check says so out loud rather than letting the silence pass for a correct state.
BIOLOGY_BRANCH_GAP = (
    "note: the record's subject is Biology and its branch is {branch!r}; no step in the pipeline "
    "assigns Biology's botany/zoology (B7 is the chem-branch sorter), so this is a known taxonomy "
    "gap and not an E4 problem -- E4's branch rule is Chemistry-only"
)


def question_record(context):
    """The real question record. Prefers context["input_data"]["record"]; falls back to
    papers/records/<QID>.json so this check is testable against real data before the E plugins
    exist. {} when neither is available -- rules needing it degrade to a reported skip."""
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


def record_branch_token(record):
    """The record's branch as `branch_used` must spell it: the value verbatim, or "none" when the
    record carries no branch at all (every Physics record)."""
    branch = record.get("branch")
    if branch is None or str(branch).strip() == "":
        return "none"
    return str(branch).strip()


def check(data, context):
    if not isinstance(data, dict):
        return False, "E4 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    primary = data.get("primary")
    secondary = data.get("secondary")
    why = (data.get("why") or "").strip()
    claimed_version = data.get("codebook_version")
    branch_used = data.get("branch_used")
    input_data = context.get("input_data") or {}
    segments = []
    notes = []

    # --- 3. spec 13/E4's own Checks -------------------------------------------------------
    if data.get("confidence") == "low":
        segments.append(
            "E4_ADJUDICATED: confidence is low; spec 13/E4's Checks require 'confidence not low', "
            "and a low-confidence run goes to the adjudicator rather than into the bank")

    if secondary is not None:
        if secondary == primary:
            segments.append(
                f"secondary {secondary!r} is the same as primary; a secondary is a second, "
                f"genuinely DIFFERENT kind of thinking, and null is the normal case")
        elif {primary, secondary} == FORBIDDEN_PAIR:
            segments.append(
                f"primary {primary!r} + secondary {secondary!r}: recall and elimination are two "
                f"points on one scale (how many facts must be settled), not two kinds of "
                f"thinking, and must never be paired (codebook/E4.md §4)")

    # --- 2. codebook_version --------------------------------------------------------------
    real_text, real_version = codebook_version.for_step("E4")
    if real_version != codebook_version.NONE and claimed_version == codebook_version.NONE:
        segments.append(
            f"codebook_version is \"none\" but codebook/E4.md exists on disk (real version "
            f"{real_version}, {len(real_text)} chars), so the codebook never reached the agent -- "
            f"a wiring failure, not an agent error: config/steps.yaml still has "
            f"codebook_file: null for E4 (see config/_pending_E_entries.yaml)")
    elif claimed_version not in (codebook_version.NONE, real_version):
        segments.append(
            f"codebook_version {claimed_version!r} is neither \"none\" nor codebook/E4.md's real "
            f"content hash ({real_version}); the tag cannot be attributed to a codebook version")
    elif real_version == codebook_version.NONE:
        # Informational only. The flag itself is raised unconditionally by the plugin from
        # codebook_version.for_step("E4"), the same way D4Plugin raises its own outcome flags --
        # a flag must never depend on a passing check's message being parsed.
        notes.append("note: codebook/E4.md is absent, so this tag was made from the eight draft "
                     "categories only -> E4_NO_CODEBOOK (low)")

    # --- 1. the branch rule ---------------------------------------------------------------
    # (1a) the wiring: the branch must have been IN the agent's input at all.
    if "branch" not in input_data:
        segments.append(
            "the agent input carried no `branch` field at all, so this tag cannot have been "
            "conditioned on B7's branch -- codebook/E4.md §1 is that a Chemistry expectation must "
            "never be keyed off the word 'Chemistry' (confirmed on 10 of 10 real papers). The "
            "input must include `branch` even when its value is null")

    record = question_record(context)
    if not record:
        segments.append(
            "no question record available (neither context['input_data']['record'] nor "
            "papers/records/<QID>.json), so branch_used could not be verified against the real "
            "branch -- the branch rule must never be skipped silently")
    else:
        subject = record.get("subject")
        expected_token = record_branch_token(record)

        # (1b) the agent restated the real branch.
        if branch_used != expected_token:
            segments.append(
                f"branch_used is {branch_used!r} but the record's own branch is {expected_token!r}; "
                f"it must be copied verbatim (\"none\" when the record has no branch), because it "
                f"is the only evidence that the branch was read at all")

        # (1c) the reasoning, as far as a script reaches it. Chemistry only.
        if subject == "Chemistry":
            prior = CHEM_BRANCH_PRIOR.get(expected_token)
            if prior is None:
                # branch unsure/none on a Chemistry question: take no prior, and say so.
                if "branch" not in why.lower():
                    segments.append(
                        f"the record is Chemistry with branch {expected_token!r}, so no prior "
                        f"applies and codebook/E4.md §1 requires `why` to say the branch was "
                        f"unavailable; `why` does not mention it ({why!r})")
            elif primary not in prior:
                if len(why.split()) < MIN_WHY_WORDS_AGAINST_PRIOR:
                    segments.append(
                        f"primary {primary!r} contradicts the {expected_token} prior "
                        f"({' / '.join(prior)}), which is legitimate but codebook/E4.md §1 "
                        f"requires the contradiction to be accounted for in one clause; `why` is "
                        f"only {len(why.split())} word(s) ({why!r})")
                else:
                    notes.append(
                        f"primary {primary!r} contradicts the {expected_token} prior "
                        f"({' / '.join(prior)}) and says why -- normal, not an error")
        elif subject == "Biology" and expected_token in ("unsure", "none"):
            notes.append(BIOLOGY_BRANCH_GAP.format(branch=record.get("branch")))

    # --- `why` substance -------------------------------------------------------------------
    if len(why.split()) < MIN_WHY_WORDS:
        segments.append(
            f"why is {len(why.split())} word(s) ({why!r}); it must name the specific hard step in "
            f"a sentence a reviewer can check in seconds -- 'must judge four statements' is "
            f"checkable, 'requires conceptual understanding' is not")

    if segments:
        return False, "; ".join(segments)
    return True, "; ".join(["ok"] + notes)
