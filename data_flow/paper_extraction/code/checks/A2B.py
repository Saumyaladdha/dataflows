"""Step-specific check for A2B "Bold-term marker" (.claude/agents/a2b-bold-marker.md).

Same scope boundary as every other scripts/checks/<STEP>.py: what ONE agent output can be judged
on, given the input it was handed. Deciding where the file goes and merging it with A2's original
output (never mutating that original) lives in step_plugins.A2BPlugin.

What IS checkable from one output plus its own input file:
  - every block the input asked for must get exactly one entry in the output, keyed by the same
    `n`. A2B's whole point is to cover the given blocks; silently dropping one would make the
    backfill incomplete without anyone noticing, since there is no separate coverage metric for
    this step the way A2 has text-layer recall.
  - no entry may name an `n` the input did not ask for -- that would be reporting on a block
    (a heading, a figure) this step was never given.
  - every bold_terms string must actually be a substring of that block's own `text`, copied
    character for character. This is the one property that matters most: the agent's whole job is
    to point INTO text that already exists, not to retype it. A term that is close-but-not-exact
    (different punctuation, a typo, re-cased) is not pointing at the same text and must be
    rejected rather than silently accepted as approximately right.
  - no bold_terms list may contain the same string twice -- the brief says a repeated bold term
    is reported once, so a duplicate means the agent counted occurrences instead of distinct terms.
  - `note` must be non-empty and say something, even when the finding is "nothing was bold".

Convention: def check(data, context) -> (bool, str).
"""

_NOTHING_NOTES = {
    "", "none", "n/a", "na", "ok", "done", "nothing", "no bold terms", "no bold", "-",
    "no note", "not applicable", "complete",
}


def check(data, context):
    if not isinstance(data, dict):
        return False, "A2B output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    blocks = data.get("blocks")
    note = data.get("note")

    if not isinstance(blocks, list):
        return False, "A2B_BAD_OUTPUT: blocks is not an array"
    if not isinstance(note, str) or note.strip().lower().rstrip(".") in _NOTHING_NOTES:
        return False, (
            f"A2B_BAD_OUTPUT: note is empty or says nothing reviewable ({note!r}); say what was "
            f"found, or confirm there was nothing bold on this page"
        )

    input_data = (context or {}).get("input_data") or {}
    asked = {b.get("n"): (b.get("text") or "") for b in (input_data.get("blocks") or [])}

    if not asked:
        return False, "A2B_BAD_OUTPUT: this item's input names no blocks to cover"

    seen_n = set()
    for i, entry in enumerate(blocks, 1):
        if not isinstance(entry, dict):
            return False, f"A2B_BAD_OUTPUT: block entry {i} is not an object"
        n = entry.get("n")
        terms = entry.get("bold_terms")

        if n not in asked:
            return False, (f"A2B_BAD_OUTPUT: block entry {i} names n={n!r}, which this item's "
                           f"input did not ask for (asked for: {sorted(asked)})")
        if n in seen_n:
            return False, f"A2B_BAD_OUTPUT: block n={n} is covered twice"
        seen_n.add(n)

        if not isinstance(terms, list):
            return False, f"A2B_BAD_OUTPUT: block n={n}'s bold_terms is not an array"

        source_text = asked[n]
        lowered_source = source_text.lower()
        dupe_check = set()
        for term in terms:
            if not isinstance(term, str) or not term.strip():
                return False, f"A2B_BAD_OUTPUT: block n={n} has an empty or non-string bold term"
            if term in dupe_check:
                return False, (f"A2B_BAD_OUTPUT: block n={n} lists {term!r} more than once; a "
                               f"repeated bold term is reported once, not per occurrence")
            dupe_check.add(term)
            if term.lower() not in lowered_source:
                return False, (
                    f"A2B_BAD_OUTPUT: block n={n} claims {term!r} is bold, but that exact text "
                    f"does not appear in the block's own source text ({source_text[:160]!r}...). "
                    f"bold_terms must copy the text that is already there, not retype it."
                )

    missing = sorted(set(asked) - seen_n)
    if missing:
        return False, (f"A2B_BAD_OUTPUT: {len(missing)} block(s) this item was asked to cover "
                       f"were not reported on: n={missing}")

    total_terms = sum(len(e.get("bold_terms") or []) for e in blocks)
    return True, f"{len(blocks)} block(s) covered, {total_terms} bold term(s) found"
