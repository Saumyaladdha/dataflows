"""Step-specific check for A2S (spec Section 9/A2S 'Checks'): table rows have consistent column
counts; LaTeX parses; caption non-empty for figures.

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring.
"""
import re

_BALANCED_PAIRS = {"{": "}", "(": ")", "[": "]"}
_CLOSERS = {v: k for k, v in _BALANCED_PAIRS.items()}


def _latex_braces_balanced(s):
    """A cheap, dependency-free 'does this parse' proxy: braces/brackets/parens balance and every
    backslash command is a letter sequence (no stray trailing backslash). Not a real LaTeX parser
    (none is available in this project), but it catches the common break (an unclosed \\frac{,
    mismatched $, a truncated command) without pulling in a new dependency for one soft check."""
    stack = []
    for ch in s:
        if ch in _BALANCED_PAIRS:
            stack.append(ch)
        elif ch in _CLOSERS:
            if not stack or stack[-1] != _CLOSERS[ch]:
                return False
            stack.pop()
    if stack:
        return False
    if s.rstrip().endswith("\\"):
        return False
    if s.count("$") % 2 != 0:
        return False
    return True


def check(data, context):
    if not isinstance(data, dict):
        return False, "A2S output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    kind = data.get("kind")
    segments = []

    if kind == "table":
        rows = data.get("rows") or []
        header = data.get("header") or []
        widths = {len(header)} if header else set()
        for i, row in enumerate(rows):
            widths.add(len(row))
        if len(widths) > 1:
            segments.append(f"A2_SPECIAL_UNREAD: inconsistent column counts across table rows: {sorted(widths)}")

    elif kind == "figure":
        # An empty caption is NOT evidence of a bad transcription. The crop handed to the
        # transcriber is cut to the page reader's bbox, which encloses the artwork only -- NCERT
        # prints the "Fig. 8.x ..." line OUTSIDE it. Measured on real output: 16 of 20 figures came
        # back with no caption, and ALL 16 carried labels, i.e. the agent genuinely read the figure
        # and then correctly refused to invent a caption it could not see (Universal rule 5).
        # Failing those was the check punishing the right behaviour, and on retry it pressures an
        # agent into fabricating a caption -- the same perverse incentive that made agents flatten
        # 10^11 to "1011" elsewhere in this pipeline.
        #
        # So: a figure must carry SOMETHING real -- labels or a caption. Both empty still fails,
        # because then nothing was transcribed at all. The proper fix is upstream (extend the bbox
        # to include the caption line, or crop with padding); until then this stops rejecting
        # correct work without ever accepting an empty transcription.
        caption = (data.get("caption") or "").strip()
        labels = data.get("labels") or []
        note = (data.get("note") or "").strip()
        if not caption and not labels:
            # A figure CAN genuinely carry neither. Real case: PHY12O-ch01-p011-b6, whose
            # target_box_in_crop encloses only a portrait photograph of Coulomb -- not one glyph
            # of text inside it, confirmed independently by two workers at high zoom. Failing
            # that unconditionally made the brief's own documented safe default ("keep the crop
            # image; text left empty") structurally unpassable: the item could never terminate,
            # and the only escapes were to fabricate a caption or to loop forever. Fabrication is
            # the worst outcome this pipeline can produce, and this check's own comment above
            # warns against exactly that perverse incentive -- so an attested empty read is
            # accepted, while a silent one is still rejected.
            #
            # The bar: the note must open with the step's "unsure:" marker (so it is a deliberate
            # declaration, not an omission) and actually explain itself. A bare "unsure:" does
            # not pass.
            attested = note.lower().startswith("unsure:") and len(note) >= 40
            if not attested:
                segments.append(
                    "A2_SPECIAL_UNREAD: figure has neither a caption nor any labels -- nothing "
                    "was transcribed. If the box genuinely contains no text, say so: begin `note` "
                    "with 'unsure:' and explain what is in the box and where the caption actually "
                    "sits. Never invent a caption to satisfy this check."
                )
        # A label is one line of text, never a raw line break. Found on real data: 37 labels
        # corpus-wide like "Urinary\nbladder" and "CHROMOSOME\nNUMBER\nPER CELL" -- a printed
        # label wrapped across physical lines and the agent kept the line break instead of
        # joining with a space. The words are all present, so this is not an A2_SPECIAL_UNREAD
        # case; it is a formatting defect every downstream reader of `labels` would trip on.
        bad_labels = [lab for lab in labels if isinstance(lab, str) and "\n" in lab]
        if bad_labels:
            segments.append(
                f"A2_LABEL_LINEBREAK: {len(bad_labels)} label(s) contain a raw newline "
                f"(e.g. {bad_labels[0]!r}) -- join wrapped label text with a space, never a "
                f"literal line break"
            )

    elif kind == "equation":
        latex = data.get("latex") or ""
        if not latex.strip():
            segments.append("A2_SPECIAL_UNREAD: equation latex is empty")
        elif not _latex_braces_balanced(latex):
            segments.append(f"A2_SPECIAL_UNREAD: latex does not appear to parse (unbalanced braces/$): {latex!r}")

    elif kind == "box":
        # A box is a worked example ("Example 1.4" / "Solution"): running prose wrapped around one
        # or more display equations. What it must deliver is TEXT, because prose is the only thing
        # quote_verify.find can match a citation against -- a box transcribed as latex alone looks
        # complete and is still uncitable. The display equations are welcome in `latex` as well,
        # and are the reason A2 marked the block special in the first place, but they are optional:
        # PHY11L ch6 p017 b22 is a small box with no display equation at all.
        text = (data.get("text") or "").strip()
        latex = data.get("latex") or ""
        if not text:
            segments.append("A2_SPECIAL_UNREAD: box has no text -- the prose is what makes it "
                            "quotable, so latex alone is not a transcription")
        if latex.strip() and not _latex_braces_balanced(latex):
            segments.append(f"A2_SPECIAL_UNREAD: box latex does not appear to parse "
                            f"(unbalanced braces/$): {latex!r}")

    else:
        segments.append(f"A2_SPECIAL_UNREAD: unknown kind {kind!r}")

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
