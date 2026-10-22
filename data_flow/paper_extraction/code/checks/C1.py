"""Step-specific check for C1 (spec Section 11/C1 'Checks' + c1-booklet-matcher.md's own rules).

This file validates what a SINGLE c1-booklet-matcher output can check on its own, exactly the
same scope boundary as scripts/checks/B5.py's precedent: shape/internal-consistency checks live
here; the cross-record checks named in spec 11/C1 ("one-to-one; both codes' keys point to the
same option through the map") need visibility into the whole sitting's other shortlisted pairs
and both codes' official_answer rows, so -- like B5's "every question exactly one row" and "key
text layer agrees" -- those are enforced at the register/merge level in step_plugins.C1Plugin,
not here.

What IS checkable from one output alone:
  - exact_same -> option_map must be a real bijection: all four A1-A4 keys present, values a
    permutation of B1-B4 (no key missing, no value reused). schemas/C1.json only constrains each
    individual key/value's STRING PATTERN (propertyNames/additionalProperties regex), not that
    all four keys are present or that the four values are distinct -- this check adds exactly
    that, the same split responsibility schemas/B3.json's own description documents between
    draft-07 shape and a script-side completeness check.
  - not_exact -> option_map must be null (schema already allows null OR a well-formed map for
    EITHER verdict, since the agent file's two examples are the only hard pairing, and JSON
    Schema's oneOf-based nullable union can't itself express "null iff verdict==not_exact"
    without an allOf/if-then the project's other schemas don't use for this kind of pairing --
    same reasoning as schemas/A6.json's allOf being used only for its OWN three-way branch).
  - not_exact -> differences should be non-empty (agent file: "If not exact, list what differs").
    A not_exact verdict with an empty differences list is shape-valid per schemas/C1.json but is
    a real content inconsistency worth catching here, the same spirit as B3.py's overlay-marker
    check: cheap, real, and specific to a known-bad shape this agent could emit.

Convention: def check(data, context) -> (bool, str).
"""

_A_KEYS = ["A1", "A2", "A3", "A4"]
_B_VALUES = {"B1", "B2", "B3", "B4"}


def check(data, context):
    if not isinstance(data, dict):
        return False, "C1 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    verdict = data.get("verdict")
    if verdict not in ("exact_same", "not_exact"):
        return False, f"C1_BAD_VERDICT: verdict {verdict!r} is not exact_same/not_exact"

    option_map = data.get("option_map")
    differences = data.get("differences")
    if not isinstance(differences, list):
        return False, "differences is not a list"

    if verdict == "exact_same":
        if not isinstance(option_map, dict):
            return False, "C1_OPTION_MAP_INVALID: verdict is exact_same but option_map is not an object"
        missing = [k for k in _A_KEYS if k not in option_map]
        if missing:
            return False, f"C1_OPTION_MAP_INVALID: option_map missing key(s) {missing}"
        values = [option_map[k] for k in _A_KEYS]
        if set(values) != _B_VALUES or len(set(values)) != 4:
            return False, (
                f"C1_OPTION_MAP_INVALID: option_map values {values} are not a bijection onto "
                f"{sorted(_B_VALUES)} (each B option must be used exactly once)"
            )
    else:  # not_exact
        if option_map is not None:
            return False, "C1_OPTION_MAP_INVALID: verdict is not_exact but option_map is not null"
        if not differences:
            return False, "C1_NO_DIFFERENCES: verdict is not_exact but differences is empty"

    return True, "ok"
