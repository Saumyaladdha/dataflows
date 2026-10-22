"""Step-specific check for B9 "Recover the figure" (.claude/agents/b9-figure-matcher.md).

Same scope boundary as every other scripts/checks/<STEP>.py in this build: what ONE agent
output can be judged on, given the input it was handed. Everything that needs the wider world
-- downloading, copying the accepted image into papers/figures/, writing figure_path /
figure_source_url onto the record, raising B9's flags -- lives in step_plugins.B9Plugin, the
same split scripts/checks/C1.py documents for C1's cross-record merge checks.

What IS checkable from one output plus its own input file:
  - `match` must name a candidate that was ACTUALLY OFFERED on this item (or be "none").
    schemas/B9.json can only constrain the enum cand_1..cand_3|none; it cannot know that this
    particular item was shown two candidates, so "cand_3" on a two-candidate item is
    shape-valid and wrong. Catching it here is the point -- an out-of-range pick would
    otherwise index into nothing and silently attach no figure with no explanation.
  - `match` must not be a candidate whose image failed to download: the agent cannot have
    looked at an image that is not on disk, so such a pick is a hallucinated verdict, not a
    judgement.
  - `why` must be non-empty and must not be a bare restatement of the verdict. The reason a
    figure was or was not attached is the only reviewable artifact B9 leaves behind besides the
    image itself.
  - a "none" verdict must not carry confidence "high"/"medium" claims about a candidate it did
    not pick -- there is nothing to validate there, so "none" is accepted at any confidence
    (B9Plugin treats every "none" as unmatched regardless).

Convention: def check(data, context) -> (bool, str). context carries `input_data` (the work
file B9Plugin wrote) exactly as resolve_single_run_items/other plugins pass it.
"""

_CONFIDENCES = ("high", "medium", "low")

# A `why` that is only these words tells a reviewer nothing; the agent file asks for the
# concrete thing in the image that ties it to the question.
_EMPTY_WHYS = {
    "", "none", "no match", "n/a", "na", "match", "yes", "no", "unsure", "cand_1", "cand_2",
    "cand_3", "it matches", "does not match", "no figure", "not sure",
}


def check(data, context):
    if not isinstance(data, dict):
        return False, "B9 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    match = data.get("match")
    confidence = data.get("confidence")
    why = data.get("why")

    if confidence not in _CONFIDENCES:
        return False, f"B9_BAD_OUTPUT: confidence {confidence!r} is not one of {list(_CONFIDENCES)}"

    if not isinstance(why, str) or why.strip().lower().rstrip(".") in _EMPTY_WHYS:
        return False, (
            f"B9_BAD_OUTPUT: why is empty or says nothing reviewable ({why!r}); name the concrete "
            f"thing in the image that ties it to (or rules it out of) this question"
        )

    input_data = (context or {}).get("input_data") or {}
    candidates = input_data.get("candidates") or []
    offered = [c.get("candidate_id") for c in candidates]
    usable = [c.get("candidate_id") for c in candidates if c.get("figure_image")]

    if match == "none":
        return True, "ok (no candidate accepted)"

    if match not in offered:
        return False, (
            f"B9_BAD_OUTPUT: match {match!r} was not offered on this item; "
            f"candidates were {offered or '[]'} (plus \"none\")"
        )
    if match not in usable:
        return False, (
            f"B9_BAD_OUTPUT: match {match!r} has no image on disk (its download failed), so it "
            f"cannot have been looked at; usable candidates were {usable or '[]'}"
        )
    return True, "ok"
