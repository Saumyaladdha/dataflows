"""Step-specific check for B6 (spec Section 10/B6 'Checks'): compare B6's independent answer
against the official answer already joined onto the record by B5 (any accepted option counts --
e.g. a multiple_accepted question's comma-separated official_answer). This IS B6's whole check --
B6 has no retry (config/steps.yaml fallback: [], spec "a retry only argues with itself; the
disagreement is the signal"), so a failing check here is exactly how the required
B6_DISAGREES_WITH_KEY flag gets raised; it is not a hard failure in the block/retry sense, and the
question always continues downstream with the official answer regardless of this result
(step_plugins.B6Plugin.check() never substitutes B6's answer in for it).

Convention: def check(data, context) -> (bool, str). `context["official_answer"]` and
`context["status"]` are the record's own already-joined B5 values.
"""


def _accepted_options(official_answer):
    if not official_answer:
        return set()
    return {a.strip() for a in str(official_answer).split(",") if a.strip()}


def check(data, context):
    if not isinstance(data, dict):
        return False, "B6 output is not an object"

    required = ["answer", "reason", "working", "confidence", "note"]
    missing = [f for f in required if f not in data]
    if missing:
        return False, f"missing required field(s): {missing}"

    official_answer = context.get("official_answer")
    status = context.get("status")
    accepted = _accepted_options(official_answer)
    answer = data.get("answer")

    if not accepted:
        if status == "dropped":
            # A dropped question has no official answer by definition -- nothing to disagree
            # with; B6's independent answer is still recorded (see step_plugins.py) but this is
            # not a B6_DISAGREES_WITH_KEY case.
            return True, "ok (dropped question, no official answer to compare against)"
        return False, (
            f"B6_DISAGREES_WITH_KEY: no official answer recorded yet to compare against "
            f"(status={status!r})"
        )

    if answer == "unsure":
        return False, (
            f"B6_DISAGREES_WITH_KEY: B6 could not choose an option (unsure); official answer is "
            f"{official_answer!r}"
        )

    if answer not in accepted:
        return False, (
            f"B6_DISAGREES_WITH_KEY: B6 chose {answer!r}, official answer is {official_answer!r} "
            f"(B6 reason: {data.get('reason', '')!r})"
        )

    return True, "ok"
