"""Step-specific check for A2I "Italic-term marker" (.claude/agents/a2i-italic-marker.md).

Cloned from scripts/checks/A2B.py, inverted to italics. Same scope boundary as every other
scripts/checks/<STEP>.py: what ONE agent output can be judged on, given the input it was handed.
Deciding where the file goes and merging it with A2's original output (never mutating that
original) lives in step_plugins.A2IPlugin.

What IS checkable from one output plus its own input file:
  - every block the input asked for must get exactly one entry in the output, keyed by the same
    `n`. A2I's whole point is to cover the given blocks; silently dropping one would make the
    backfill incomplete without anyone noticing, since there is no separate coverage metric for
    this step the way A2 has text-layer recall.
  - no entry may name an `n` the input did not ask for -- that would be reporting on a block
    (a heading, a figure) this step was never given.
  - every italic_terms string must actually be a substring of that block's own `text`, copied
    character for character. This is the one property that matters most: the agent's whole job is
    to point INTO text that already exists, not to retype it. A term that is close-but-not-exact
    (different punctuation, a typo, re-cased) is not pointing at the same text and must be
    rejected rather than silently accepted as approximately right.
  - no italic_terms list may contain the same string twice -- the brief says a repeated italic
    term is reported once, so a duplicate means the agent counted occurrences instead of
    distinct terms.
  - no italic_terms string may repeat a term the same block already records in `bold_terms`
    (handed to the agent read-only in its input). Bold and italic are mutually exclusive
    typesettings of the same characters: a term claimed as both means one of the two readings is
    wrong, and a consumer joining the two lists would double-count it. This check is A2I's only
    addition over A2B's list, and it exists because A2I runs on pages whose bold terms are
    already decided -- the inverse ask (bold must not duplicate italic) has no such input.
  - `note` must be non-empty and say something, even when the finding is "nothing was italic".

Deliberate divergence from A2B.py: the substring comparison here is EXACT, where A2B compares
case-insensitively. A2B's own docstring asks for "character for character" and its lowercasing
is laxer than the rule it states; A2I is specified as verbatim, so it is verbatim, and a term
that differs only in case gets a message naming that as the reason rather than a bare miss.

Convention: def check(data, context) -> (bool, str).
"""

_NOTHING_NOTES = {
    "", "none", "n/a", "na", "ok", "done", "nothing", "no italic terms", "no italics",
    "no italic", "-", "no note", "not applicable", "complete",
}


def check(data, context):
    if not isinstance(data, dict):
        return False, "A2I output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    blocks = data.get("blocks")
    note = data.get("note")

    if not isinstance(blocks, list):
        return False, "A2I_BAD_OUTPUT: blocks is not an array"
    if not isinstance(note, str) or note.strip().lower().rstrip(".") in _NOTHING_NOTES:
        return False, (
            f"A2I_BAD_OUTPUT: note is empty or says nothing reviewable ({note!r}); say what was "
            f"found, or confirm there was nothing italic on this page"
        )

    input_data = (context or {}).get("input_data") or {}
    asked, asked_bold = {}, {}
    for b in (input_data.get("blocks") or []):
        asked[b.get("n")] = b.get("text") or ""
        asked_bold[b.get("n")] = [t for t in (b.get("bold_terms") or []) if isinstance(t, str)]

    if not asked:
        return False, "A2I_BAD_OUTPUT: this item's input names no blocks to cover"

    seen_n = set()
    for i, entry in enumerate(blocks, 1):
        if not isinstance(entry, dict):
            return False, f"A2I_BAD_OUTPUT: block entry {i} is not an object"
        n = entry.get("n")
        terms = entry.get("italic_terms")

        if n not in asked:
            return False, (f"A2I_BAD_OUTPUT: block entry {i} names n={n!r}, which this item's "
                           f"input did not ask for (asked for: {sorted(asked)})")
        if n in seen_n:
            return False, f"A2I_BAD_OUTPUT: block n={n} is covered twice"
        seen_n.add(n)

        if not isinstance(terms, list):
            return False, f"A2I_BAD_OUTPUT: block n={n}'s italic_terms is not an array"

        source_text = asked[n]
        bold_here = asked_bold.get(n) or []
        dupe_check = set()
        for term in terms:
            if not isinstance(term, str) or not term.strip():
                return False, f"A2I_BAD_OUTPUT: block n={n} has an empty or non-string italic term"
            if term in dupe_check:
                return False, (f"A2I_BAD_OUTPUT: block n={n} lists {term!r} more than once; a "
                               f"repeated italic term is reported once, not per occurrence")
            dupe_check.add(term)
            if term not in source_text:
                if term.lower() in source_text.lower():
                    return False, (
                        f"A2I_BAD_OUTPUT: block n={n} claims {term!r} is italic, but the block's "
                        f"own source text spells it with different capitalisation. italic_terms "
                        f"must copy the text that is already there character for character."
                    )
                return False, (
                    f"A2I_BAD_OUTPUT: block n={n} claims {term!r} is italic, but that exact text "
                    f"does not appear in the block's own source text ({source_text[:160]!r}...). "
                    f"italic_terms must copy the text that is already there, not retype it."
                )
            if term in bold_here:
                return False, (
                    f"A2I_BAD_OUTPUT: block n={n} lists {term!r} as italic, but this block's "
                    f"input already records it as BOLD. A term is bold or italic, never both; "
                    f"italic_terms is for text that is italic AND NOT bold."
                )

    missing = sorted(set(asked) - seen_n)
    if missing:
        return False, (f"A2I_BAD_OUTPUT: {len(missing)} block(s) this item was asked to cover "
                       f"were not reported on: n={missing}")

    total_terms = sum(len(e.get("italic_terms") or []) for e in blocks)
    return True, f"{len(blocks)} block(s) covered, {total_terms} italic term(s) found"
