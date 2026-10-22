"""Step-specific check for B10 "Split the recovered figure" (.claude/agents/b10-figure-splitter.md).

Same scope boundary as every other scripts/checks/<STEP>.py: what ONE agent output can be judged
on, given the input it was handed. The cropping itself, naming the files, and deciding what the
sheet shows live in scripts/split_figures.py and step_plugins.B10Plugin.

What IS checkable from one output plus its own input file:
  - every named `slot` must be a slot this item ACTUALLY asked for. schemas/B10.json can only
    constrain the shape (`opt3`, `list_i:A`, `unknown`); it cannot know that this question's slots
    were `list_i:A..D`, so `opt3` on a match-list item is shape-valid and wrong.
  - **no `opt` slot may be claimed.** This is the whole correctness rule of the step. Our option
    text is empty -- that is why the question is here -- so a printed "(1)" has nothing in our
    record to agree with: it is the SOURCE paper's option order, and booklet codes shuffle option
    order. Q-000343 is the proof: the official key for our booklet says 4 while the physically
    correct plot in the recovered picture is printed (2). An agent that fills opt1..opt4 is making
    a claim it cannot support, and the first four runs of this step all did exactly that, so this
    is enforced in code rather than trusted to the brief.
  - `labels_match_our_slots` must be false whenever any slot is "unknown", and must be false for a
    question whose slots are all options -- the two statements have to agree.
  - boxes must be ordered (x0 < x1, y0 < y1) and not degenerate. A reversed or zero-area box
    silently crops nothing, so the slot would look handled while no picture exists.
  - boxes must not overlap. Two overlapping boxes mean at least one crop contains a neighbouring
    picture, which sends a reader to the wrong option.
  - `note` must be non-empty and say something. It is the only reviewable artifact besides the
    crops themselves, and an empty panel list is only trustworthy if it explains itself.

Convention: def check(data, context) -> (bool, str).
"""

_NOTHING_NOTES = {
    "", "none", "n/a", "na", "ok", "done", "no panels", "nothing", "split", "unsure", "-",
    "no note", "not applicable", "panels found",
}

_OVERLAP_TOLERANCE = 0.01  # boxes may share an edge; a real overlap is bigger than this


def _overlap(a, b):
    """Area of intersection between two [x0,y0,x1,y1] boxes."""
    dx = min(a[2], b[2]) - max(a[0], b[0])
    dy = min(a[3], b[3]) - max(a[1], b[1])
    return dx * dy if dx > 0 and dy > 0 else 0.0


def check(data, context):
    if not isinstance(data, dict):
        return False, "B10 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    panels = data.get("panels")
    matched = data.get("labels_match_our_slots")
    note = data.get("note")

    if not isinstance(panels, list):
        return False, "B10_BAD_OUTPUT: panels is not an array"
    if not isinstance(matched, bool):
        return False, f"B10_BAD_OUTPUT: labels_match_our_slots {matched!r} is not a boolean"
    if not isinstance(note, str) or note.strip().lower().rstrip(".") in _NOTHING_NOTES:
        return False, (
            f"B10_BAD_OUTPUT: note is empty or says nothing reviewable ({note!r}); say how the "
            f"pictures are arranged, what separates them, or why none could be cut"
        )

    input_data = (context or {}).get("input_data") or {}
    asked = list(input_data.get("slots") or [])
    all_options = bool(asked) and all(s.startswith("opt") for s in asked)

    if not panels:
        # The spec'd "unsure" form. Legitimate, but it must not claim a mapping.
        if matched:
            return False, ("B10_BAD_OUTPUT: no panels were returned, so labels_match_our_slots "
                           "cannot be true")
        return True, f"no panels cut: {note.strip()[:120]}"

    if len(panels) > len(asked):
        return False, (f"B10_BAD_OUTPUT: {len(panels)} panels returned but this question has only "
                       f"{len(asked)} slot(s) needing a picture")

    boxes, claimed = [], []
    for i, panel in enumerate(panels, 1):
        slot = panel.get("slot")
        box = panel.get("box")

        if slot != "unknown":
            if slot not in asked:
                return False, (f"B10_BAD_OUTPUT: panel {i} names slot {slot!r}, which this item "
                               f"did not ask for (slots: {asked})")
            if slot.startswith("opt"):
                return False, (
                    f"B10_BAD_OUTPUT: panel {i} claims option slot {slot!r}. An option slot may "
                    f"never be claimed: this question's option text is empty, so a printed label "
                    f"is the source paper's option order and booklet codes shuffle it. Use "
                    f"\"unknown\" and let the printed_label carry what you saw."
                )
            claimed.append(slot)

        if not (isinstance(box, list) and len(box) == 4):
            return False, f"B10_BAD_OUTPUT: panel {i} has no usable box"
        x0, y0, x1, y1 = box
        if not (x1 - x0 > 0 and y1 - y0 > 0):
            return False, (f"B10_BAD_OUTPUT: panel {i}'s box {box} is reversed or zero-area, so it "
                           f"would crop nothing")
        boxes.append((box, i))

    if len(set(claimed)) != len(claimed):
        return False, f"B10_BAD_OUTPUT: the same slot is claimed by two panels ({claimed})"

    for idx, (box_a, i) in enumerate(boxes):
        for box_b, j in boxes[idx + 1:]:
            if _overlap(box_a, box_b) > _OVERLAP_TOLERANCE:
                return False, (f"B10_BAD_OUTPUT: panels {i} and {j} overlap; at least one crop "
                               f"would contain a neighbouring picture")

    if all_options and matched:
        return False, ("B10_BAD_OUTPUT: every slot on this item is an option slot, so "
                       "labels_match_our_slots must be false")
    if matched and any(p.get("slot") == "unknown" for p in panels):
        return False, ("B10_BAD_OUTPUT: labels_match_our_slots is true but some panel has slot "
                       "\"unknown\"")

    mapped = len(claimed)
    return True, (f"{len(panels)} panel(s) cut, {mapped} tied to a slot"
                  + (f" ({claimed})" if claimed else " (none claimed, as options require)"))
