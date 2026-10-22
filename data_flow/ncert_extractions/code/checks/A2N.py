"""Step-specific check for A2N "Notation fixer" (.claude/agents/a2n-notation-fixer.md).

Same scope boundary as every other scripts/checks/<STEP>.py: what ONE agent output can be judged
on, given the input it was handed. Merging a correction into whatever reads A2's text downstream
(never mutating the original A2 output) lives in step_plugins.A2NPlugin.

What IS checkable from one output plus its own input file:
  - every block the input asked for must get exactly one entry, keyed by the same `n` -- this
    step's whole point is covering the given blocks, and a silently skipped block means a known
    defect (a flattened exponent, a dropped radical) is left unfixed with nobody told.
  - no entry may name an `n` the input did not ask for.
  - `no_change` and `corrected_text` are mutually exclusive, and exactly one must be given.
  - **the one property that matters most: `corrected_text` must carry the SAME prose words, in
    the SAME order, as the original `text`.** This agent's job is to repair notation, not
    re-transcribe the page -- a correction that also changed a word, dropped a sentence, or
    reordered prose is not a notation fix, it is an uncontrolled rewrite of checked passage text,
    and must be rejected outright rather than trusted. Reuses `scripts/checks/A2._prose_words`,
    the same word-extraction A2's own check uses, so "what counts as a word" is one definition
    across both steps.
  - when `corrected_text` is given, `fixes` must be present and non-empty, and every `fixes[i].wrong`
    string must actually appear in the ORIGINAL text (not inventing what was "wrong") while every
    `fixes[i].right` string must appear in `corrected_text` (the claimed fix must actually be
    present in the output, not merely described).
  - `note` must be non-empty and say something.

Convention: def check(data, context) -> (bool, str).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from A2 import _prose_words  # noqa: E402  (reuse A2's own word-extraction; one definition, two steps)

_NOTHING_NOTES = {
    "", "none", "n/a", "na", "ok", "done", "nothing", "no change", "no changes", "-",
    "no note", "not applicable", "complete",
}


def check(data, context):
    if not isinstance(data, dict):
        return False, "A2N output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    blocks = data.get("blocks")
    note = data.get("note")

    if not isinstance(blocks, list):
        return False, "A2N_BAD_OUTPUT: blocks is not an array"
    if not isinstance(note, str) or note.strip().lower().rstrip(".") in _NOTHING_NOTES:
        return False, (
            f"A2N_BAD_OUTPUT: note is empty or says nothing reviewable ({note!r}); say what was "
            f"corrected, or confirm nothing needed fixing"
        )

    input_data = (context or {}).get("input_data") or {}
    asked = {b.get("n"): (b.get("text") or "") for b in (input_data.get("blocks") or [])}

    if not asked:
        return False, "A2N_BAD_OUTPUT: this item's input names no blocks to cover"

    seen_n = set()
    n_corrected = 0
    for i, entry in enumerate(blocks, 1):
        if not isinstance(entry, dict):
            return False, f"A2N_BAD_OUTPUT: block entry {i} is not an object"
        n = entry.get("n")

        if n not in asked:
            return False, (f"A2N_BAD_OUTPUT: block entry {i} names n={n!r}, which this item's "
                           f"input did not ask for (asked for: {sorted(asked)})")
        if n in seen_n:
            return False, f"A2N_BAD_OUTPUT: block n={n} is covered twice"
        seen_n.add(n)

        no_change = entry.get("no_change")
        corrected = entry.get("corrected_text")
        fixes = entry.get("fixes")

        if no_change and corrected is not None:
            return False, (f"A2N_BAD_OUTPUT: block n={n} sets both no_change and corrected_text; "
                           f"they are mutually exclusive")
        if not no_change and corrected is None:
            return False, (f"A2N_BAD_OUTPUT: block n={n} gives neither no_change nor "
                           f"corrected_text")

        if corrected is not None:
            n_corrected += 1
            original = asked[n]

            orig_words = _prose_words(original)
            new_words = _prose_words(corrected)
            if new_words != orig_words:
                return False, (
                    f"A2N_BAD_OUTPUT: block n={n}'s corrected_text changes the prose itself -- "
                    f"this step may only fix notation (digits/symbols), never reword, drop or "
                    f"reorder words. Original words: {orig_words[:12]}... "
                    f"corrected words: {new_words[:12]}..."
                )

            if not isinstance(fixes, list) or not fixes:
                return False, (f"A2N_BAD_OUTPUT: block n={n} has corrected_text but no non-empty "
                               f"fixes list explaining what changed")
            for j, fx in enumerate(fixes, 1):
                if not isinstance(fx, dict) or "wrong" not in fx or "right" not in fx:
                    return False, f"A2N_BAD_OUTPUT: block n={n} fixes[{j}] is malformed"
                wrong, right = fx["wrong"], fx["right"]
                if wrong not in original:
                    return False, (
                        f"A2N_BAD_OUTPUT: block n={n} fixes[{j}] claims {wrong!r} was wrong, but "
                        f"that text does not appear in the ORIGINAL -- it cannot be what was "
                        f"corrected"
                    )
                if right not in corrected:
                    return False, (
                        f"A2N_BAD_OUTPUT: block n={n} fixes[{j}] claims the fix is {right!r}, but "
                        f"that text does not appear in corrected_text -- the claimed fix was not "
                        f"actually applied"
                    )

    missing = sorted(set(asked) - seen_n)
    if missing:
        return False, (f"A2N_BAD_OUTPUT: {len(missing)} block(s) this item was asked to cover "
                       f"were not reported on: n={missing}")

    return True, f"{len(blocks)} block(s) covered, {n_corrected} corrected"
