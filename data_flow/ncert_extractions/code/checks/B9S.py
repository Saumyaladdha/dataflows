"""Step-specific check for B9S "Confirm the figure cut from the official booklet"
(.claude/agents/b9s-source-figure-confirmer.md).

Same scope boundary as every other scripts/checks/<STEP>.py in this build: what ONE agent output
can be judged on, given the input it was handed. Everything needing the wider world -- publishing
the crop, superseding B9's figure, raising B9S's flags -- belongs in the step plugin, the split
scripts/checks/B9.py documents for B9.

What IS checkable from one output plus its own input file:
  - `question_id` must be the id this item was about. schemas/B9S.json can only check the shape
    Q-nnnnnn; a well-formed id for a DIFFERENT question is shape-valid, and is precisely the error
    that would publish a confirmed figure onto the wrong record.
  - `missing` must be filled when the verdict is `belongs_clipped` and empty otherwise; `junk`
    likewise for `belongs_with_junk`. Draft-07 cannot express that pairing without duplicating all
    six verdict branches, and the pairing is the whole content of those two verdicts: a
    `belongs_clipped` with nothing named in `missing` tells a reviewer that something is cut off
    but not what, which is unactionable.
  - `shows` must say something about the picture rather than restate the verdict. It is the only
    artifact besides the image itself that a person can review, and for `wrong_figure` it is the
    only record of what the cropper actually landed on.
  - a `wrong_figure` or `not_a_figure` verdict must not ALSO name missing parts or junk: those
    describe a figure that belongs, and filling them alongside a rejection is a sign the verdict
    and the description disagree.

Convention: def check(data, context) -> (bool, str). context carries `input_data` (the work item
the agent was given), so cross-field checks against the input are possible here and nowhere else.
"""

_VERDICTS = ("belongs_complete", "belongs_clipped", "belongs_with_junk",
             "panel_order_differs", "wrong_figure", "not_a_figure", "unsure")

#: A `shows` that only repeats the verdict carries no information for a reviewer. These are the
#: forms seen in practice when an agent fills the field to satisfy the schema.
_EMPTY_SHOWS = {
    "", "the figure", "a figure", "the diagram", "a diagram", "the image", "an image",
    "it belongs", "belongs", "correct figure", "the correct figure", "wrong figure",
    "the wrong figure", "not a figure", "n/a", "na", "none", "unknown", "unsure",
}


def check(data, context=None):
    if "error" in data:
        return True, "ok (agent reported a broken input)"

    verdict = data.get("verdict")
    if verdict not in _VERDICTS:
        return False, f"B9S_BAD_OUTPUT: verdict {verdict!r} is not one of {list(_VERDICTS)}"

    shows = data.get("shows")
    if not isinstance(shows, str) or shows.strip().lower().rstrip(".") in _EMPTY_SHOWS:
        return False, (
            f"B9S_BAD_OUTPUT: shows is empty or only restates the verdict ({shows!r}); name what "
            f"is actually drawn in the image -- it is the only part of this verdict a person can "
            f"review without reopening the paper"
        )

    missing = data.get("missing") or ""
    junk = data.get("junk") or ""

    if verdict == "belongs_clipped" and not missing.strip():
        return False, ("B9S_BAD_OUTPUT: verdict is belongs_clipped but missing is empty; name "
                       "exactly what was cut off, or the finding cannot be acted on")
    if verdict == "belongs_with_junk" and not junk.strip():
        return False, ("B9S_BAD_OUTPUT: verdict is belongs_with_junk but junk is empty; name "
                       "exactly what else is in the image, so the cropper can be fixed rather "
                       "than the crop redone by hand")
    if verdict != "belongs_clipped" and missing.strip():
        return False, (f"B9S_BAD_OUTPUT: missing is filled ({missing!r}) but the verdict is "
                       f"{verdict!r}; missing describes a figure that BELONGS and is cut short")
    if verdict != "belongs_with_junk" and junk.strip():
        return False, (f"B9S_BAD_OUTPUT: junk is filled ({junk!r}) but the verdict is {verdict!r}; "
                       f"junk describes a figure that BELONGS and is whole")

    pmap = data.get("panel_map") or {}
    if verdict == "panel_order_differs":
        if not isinstance(pmap, dict) or len(pmap) < 2:
            return False, ("B9S_BAD_OUTPUT: verdict is panel_order_differs but panel_map does not "
                           "give the mapping; without it the keyed answer still selects the wrong "
                           "picture, which is the whole defect this verdict reports")
        if len(set(pmap.values())) != len(pmap.values()):
            return False, (f"B9S_BAD_OUTPUT: panel_map {pmap} sends two panels to the same option; "
                           f"a rotation is one-to-one, so this mapping cannot be applied")
        bad = [v for v in pmap.values() if str(v) not in ("1", "2", "3", "4")]
        if bad:
            return False, (f"B9S_BAD_OUTPUT: panel_map points at option(s) {bad}, which are not "
                           f"option numbers 1-4")
    elif pmap:
        return False, (f"B9S_BAD_OUTPUT: panel_map is filled ({pmap}) but the verdict is "
                       f"{verdict!r}; it describes a rotation and belongs only to "
                       f"panel_order_differs")

    input_data = (context or {}).get("input_data") or {}
    want = input_data.get("question_id")
    got = data.get("question_id")
    if want and got != want:
        return False, (f"B9S_BAD_OUTPUT: question_id {got!r} is not the question this item was "
                       f"about ({want!r}); a verdict under the wrong id would attach this figure "
                       f"to another record")

    return True, f"ok ({verdict})"
