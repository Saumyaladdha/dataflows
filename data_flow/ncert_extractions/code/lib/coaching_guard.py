"""Enforces spec Rule 10: B6 (the blind solver) and D7 (the latest-answer checker) never see
coaching material, and B6 never sees the key. A simple path-prefix and field-name check, run on
an agent's input JSON/file list before it is handed to the agent.
"""

FORBIDDEN_PATH_PREFIXES = ("inputs/coaching/", "inputs/legacy_sheets/")

ANSWER_KEY_FIELD_NAMES = {
    "official_answer", "answer", "answer_key", "final_answer", "key_answer",
    "correct_option", "correct_answer", "answer_source",
}


class CoachingGuardError(ValueError):
    """Raised when an agent input contains coaching/legacy material, or an answer-key field it
    must not see."""


def _collect_strings(data):
    out = []

    def walk(x):
        if isinstance(x, str):
            out.append(x)
        elif isinstance(x, dict):
            for v in x.values():
                walk(v)
        elif isinstance(x, (list, tuple)):
            for v in x:
                walk(v)

    walk(data)
    return out


def _collect_field_names(data):
    names = set()

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                names.add(k)
                walk(v)
        elif isinstance(x, (list, tuple)):
            for v in x:
                walk(v)

    walk(data)
    return names


def check_input(data, agent_name=None, forbid_answer_fields=False):
    """Raise CoachingGuardError if `data` (an agent input dict, or a list of file paths)
    contains any string path under inputs/coaching/ or inputs/legacy_sheets/, or, when
    `forbid_answer_fields` is True, any field name that looks like an answer key. Does nothing
    and returns None if the input is clean."""
    for s in _collect_strings(data):
        normalised = s.replace("\\", "/")
        for bad in FORBIDDEN_PATH_PREFIXES:
            if bad in normalised:
                raise CoachingGuardError(
                    f"forbidden input for {agent_name or 'this agent'}: path under {bad!r} "
                    f"found ({s!r}) — B6 and D7 must never see coaching/legacy material"
                )
    if forbid_answer_fields:
        bad_fields = _collect_field_names(data) & ANSWER_KEY_FIELD_NAMES
        if bad_fields:
            raise CoachingGuardError(
                f"forbidden answer-key field(s) for {agent_name or 'this agent'}: "
                f"{sorted(bad_fields)} — B6 must never see the key"
            )


def guard_b6_input(data):
    """Guard B6 (the blind solver): must see neither coaching/legacy material nor the answer key."""
    check_input(data, agent_name="b6-blind-solver", forbid_answer_fields=True)


def guard_d7_input(data):
    """Guard D7 (the latest-answer checker): must never see coaching/legacy material."""
    check_input(data, agent_name="d7-latest-answer-checker", forbid_answer_fields=False)


if __name__ == "__main__":
    clean = {"question_id": "Q-1", "stem_en": "What is X?", "options_en": {"1": "a", "2": "b"}}
    check_input(clean)  # must not raise
    guard_b6_input(clean)
    guard_d7_input(clean)

    dirty_path = {"question_id": "Q-1", "source_files": ["inputs/coaching/allen_notes.pdf"]}
    try:
        guard_b6_input(dirty_path)
        raise AssertionError("expected CoachingGuardError for coaching path")
    except CoachingGuardError:
        pass

    dirty_legacy = ["inputs/legacy_sheets/2019_biology.csv"]
    try:
        guard_d7_input(dirty_legacy)
        raise AssertionError("expected CoachingGuardError for legacy path")
    except CoachingGuardError:
        pass

    dirty_answer = {"question_id": "Q-1", "stem_en": "What is X?", "official_answer": "2"}
    try:
        guard_b6_input(dirty_answer)
        raise AssertionError("expected CoachingGuardError for answer field")
    except CoachingGuardError:
        pass
    guard_d7_input(dirty_answer)  # D7 is allowed to see the answer field; only B6 is not

    print("coaching_guard.py self-check OK")
