"""Step-specific check for B8 (spec Section 10/B8 'Checks' + b8-faulty-fixer.md's own rules):
'reason allowed' is already schema-enforced (schemas/B8.json's issue_reason enum). This file
validates what a single B8 output can check on its own beyond the schema: that a `note` isn't
used to smuggle a non-empty 'issue_reason: other' without saying why, matching the agent file's
own spirit even though it isn't a separate numbered rule.

'Supporting quote verified in the latest edition' (spec 10/B8 Checks) is a cross-file lookup
against ncert/passages/<BOOK>.jsonl, so it lives in step_plugins.B8Plugin._verify_quote() instead
of here, same precedent as B8's sibling quote-verifying step D4 and B4's own field comparison.

Convention: def check(data, context) -> (bool, str).
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "B8 output is not an object"

    required = [
        "issue_reason", "notice_says", "proposed_answer", "supporting_quote",
        "corrected_stem", "corrected_options", "confidence", "note",
    ]
    missing = [f for f in required if f not in data]
    if missing:
        return False, f"missing required field(s): {missing}"

    if data.get("issue_reason") == "other" and not (data.get("note") or "").strip():
        return False, (
            "issue_reason is 'other' with an empty note -- the agent file's own rule is that "
            "'other' must still say what the issue is somewhere in its output"
        )

    return True, "ok"
