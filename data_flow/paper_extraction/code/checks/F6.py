"""Step-specific check for F6 (spec 14/F6, targets from Section 1.1).

`data` is one gold-set score summary (schemas/F6.json shape).

What this enforces: the arithmetic of the score itself, so a report cannot overstate the
pipeline. `matched` can never exceed `checked`, `rate` must be exactly matched/checked, and
`meets_target` must follow from `rate` and `target` rather than being asserted. A criterion that
scored nothing (`checked == 0`) must report `rate: null` and `meets_target: null` — never a
passing verdict, because "we checked nothing" is not "we met the target". A missed target is NOT
a check failure: scores.md exists precisely to report misses so M7 can fix them.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "F6 output is not an object"
    criteria = data.get("per_criterion")
    if not isinstance(criteria, list) or not criteria:
        return False, "per_criterion is missing or empty"

    notes = []
    for c in criteria:
        if not isinstance(c, dict):
            return False, f"criterion is not an object: {c!r}"
        name = c.get("id") or c.get("name")
        checked, matched = c.get("checked"), c.get("matched")
        if not isinstance(checked, int) or not isinstance(matched, int):
            return False, f"{name}: checked/matched are not integers"
        if matched > checked:
            return False, f"{name}: matched ({matched}) exceeds checked ({checked})"
        target, rate, meets = c.get("target"), c.get("rate"), c.get("meets_target")
        if not isinstance(target, (int, float)) or not 0 <= target <= 1:
            return False, f"{name}: target {target!r} is not a fraction between 0 and 1"
        if checked == 0:
            if rate is not None or meets is not None:
                return False, (f"{name}: nothing was checked, so rate and meets_target must both "
                               f"be null (got {rate!r}, {meets!r}); 'we checked nothing' is not "
                               f"'we met the target'")
            notes.append(f"{name}: nothing to score")
            continue
        expected_rate = matched / checked
        if rate is None or abs(float(rate) - expected_rate) > 1e-9:
            return False, (f"{name}: rate is {rate!r} but matched/checked is {expected_rate:.6f}")
        if c.get("per_subject"):
            per = c["per_subject"]
            if not isinstance(per, dict):
                return False, f"{name}: per_subject is not an object"
            expected_meets = all(v.get("meets_target") for v in per.values()
                                 if isinstance(v, dict) and v.get("meets_target") is not None) \
                if per else None
            if meets is not None and expected_meets is not None and bool(meets) != bool(expected_meets):
                return False, (f"{name}: meets_target is {meets!r} but the per-subject verdicts "
                               f"imply {expected_meets!r} (the target is per subject)")
        else:
            expected_meets = expected_rate >= target
            if meets is None or bool(meets) != expected_meets:
                return False, (f"{name}: meets_target is {meets!r} but rate {expected_rate:.4f} "
                               f"vs target {target} implies {expected_meets}")
        if not expected_meets:
            notes.append(f"{name}: UNDER TARGET ({expected_rate:.1%} < {target:.0%})")

    if notes:
        return True, "note: " + "; ".join(notes)
    return True, "ok"
