"""Step-specific check for B1 (spec Section 10/B1 'Checks' + b1-paper-registrar.md's own rules):
register-level checks (1) one row per file, (2) paper/key codes match, (3) every official sitting
has both are cross-item/register-level and enforced where the row is actually written
(step_plugins.B1Plugin._post_assembly, which dedupes on (paper_id, file_kind) -- mirrors how
A1's "exactly one latest/older book" check lives in A1Plugin._post_assembly, not here).

This file enforces what a SINGLE B1 output can verify on its own:
  - 'On failure' (10/B1): cover text disagreeing with the manifest is B1_MANIFEST_MISMATCH
    (normal) -- not a hard failure in the sense of blocking, but per config/steps.yaml's
    B1 fallback ([], no retry chain) a failing check() here is how that flag gets raised and the
    item resolves to status "flagged" rather than silently "pass" (see step_plugins.py's
    resolve_single_run_items, called with B1's fallback=[]).
  - the agent file's own rule: trust must never be "official" when booklet_code is empty (an
    unconfirmed code must be trust: "unsure", never silently promoted) -- this is the concrete,
    checkable form of "never promote a folder/filename-implied code" (b1-paper-registrar.md
    Never section).

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring for the
full convention this build uses, including how a failing message's "<FLAG_CODE>: <detail>"
segments map onto config/steps.yaml's flags.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "B1 output is not an object"

    required = ["file_kind", "exam", "year", "sitting", "booklet_code", "language",
                "trust", "cover_text_exact", "agrees_with_manifest", "note"]
    missing = [f for f in required if f not in data]
    if missing:
        return False, f"missing required field(s): {missing}"

    if data.get("agrees_with_manifest") is False:
        return False, (
            f"B1_MANIFEST_MISMATCH: cover text disagrees with the manifest row -- "
            f"{data.get('note', '')}"
        )

    if data.get("trust") == "official" and not (data.get("booklet_code") or "").strip():
        return False, (
            "B1_MANIFEST_MISMATCH: trust=official but booklet_code is empty -- the agent's own "
            "rule requires trust=unsure whenever the page content doesn't independently confirm "
            "a code; an empty confirmed code is a contradiction, not a pass"
        )

    return True, "ok"
