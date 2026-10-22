"""Step-specific check for D5 (spec Section 12/D5 'Checks' + d5-older-line-finder.md's own rules).

schemas/D5.json already constrains the {older:[{for,passage_id,exact_line}], none_for, note} shape.
This file adds every rule that needs the per-item `context["input_data"]`
step_plugins.D5Plugin passes alongside the agent output (same pattern as scripts/checks/D4.py):

  (1) THE non-negotiable one (spec 12/D5 Checks, verbatim: "every older line found word for word
      in the **older** edition"): each exact_line must survive lib.quote_verify.find against the
      text of the older passage it names. `context["input_data"]["older_passages"]` is
      {passage_id: full_text}, read by the plugin FROM DISK (ncert/passages/<BOOK>O.jsonl via
      D3's own `older` list) — never from whatever the agent echoed back — so a verified quote is
      verified against the real older book, exactly as D4 does for the latest.
  (2) passage_id is one of those older passage ids.
  (3) the agent file's own "Never quote the latest edition here": a passage_id whose book-id
      letter is 'L' (or that appears in the latest passage list the plugin also passes) is a hard
      failure with its own message, distinct from "not found" — the two have different causes and
      a retry needs to be told which it was.
  (4) no ellipses (quote_verify.find already rejects them, but silently returning None would
      report this as "not found", which sends a retry chasing the wrong problem).
  (5) `for` labels: no duplicate (for, passage_id, exact_line) triple; a label must not appear in
      BOTH `older` and `none_for` (saying "here is the older line for statement B" and "the older
      book has no line for statement B" at once is self-contradictory).

What is DELIBERATELY NOT checked here:
  - That every `for` label D4 used appears in `older` ∪ `none_for`. Spec 12/D5 says "one older
    line per part that D4 covered ... plus lines for parts D4 could not cover if the older book
    has them" — the second half means the label set is legitimately NOT a function of D4's, so
    requiring an exact cover would fail honest output. The plugin records the D4 labels D5 left
    unaddressed on the record instead of failing the item (see D5Plugin._post_assembly).
  - Whether the older line states the SAME FACT as the latest one. That is a judgement, and it is
    D6's (written_differently) and D7's (answer_changed) to make, not a script's.

Convention: def check(data, context) -> (bool, str). A failing check returns a ';'-joined set of
segments (runner_core.parse_check_message), each optionally prefixed "<FLAG_CODE>: ..." using one
of this step's own config/steps.yaml flag codes.
"""
import re

from lib import quote_verify

_ELLIPSES = ("...", "…")
# A book id is {SUBJ}{CLASS}{EDITION-LETTER} (spec 6.1), and a passage id starts with it:
# "BIO11O-CH10-P05" -> edition letter "O". "L" = latest, "O" = older, "M" = lab manual.
_PASSAGE_ID_RE = re.compile(r"^([A-Z]{3})(\d{2})([LOM])-")


def _edition_letter(passage_id):
    m = _PASSAGE_ID_RE.match(passage_id or "")
    return m.group(3) if m else None


def check(data, context):
    if not isinstance(data, dict):
        return False, "D5 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    older = data.get("older")
    none_for = data.get("none_for")
    if not isinstance(older, list):
        return False, "older is not a list"
    if not isinstance(none_for, list):
        return False, "none_for is not a list"

    input_data = context.get("input_data") or {}
    older_passages = input_data.get("older_passages") or {}
    latest_passage_ids = set(input_data.get("latest_passage_ids") or [])
    allowed_ids = set(older_passages.keys())

    segments = []
    seen_triples = set()

    for i, item in enumerate(older):
        if not isinstance(item, dict):
            segments.append(f"D5_BAD_SHAPE: older[{i}] is not an object")
            continue
        label = item.get("for")
        pid = item.get("passage_id")
        quote = item.get("exact_line")

        triple = (label, pid, quote)
        if triple in seen_triples:
            segments.append(f"D5_BAD_SHAPE: older[{i}] repeats an earlier entry exactly ({label!r}, {pid!r})")
            continue
        seen_triples.add(triple)

        if quote and any(e in quote for e in _ELLIPSES):
            segments.append(
                f"D5_QUOTE_NOT_FOUND: older[{i}] exact_line contains an ellipsis; a quote must be "
                f"ONE continuous span with no '...' (use two entries for two separated spans)"
            )
            continue

        letter = _edition_letter(pid)
        if letter == "L" or pid in latest_passage_ids:
            segments.append(
                f"D5_LATEST_EDITION_QUOTE: older[{i}] passage_id {pid!r} is a LATEST-edition "
                f"passage; D5 must quote only the older edition"
            )
            continue
        if pid not in allowed_ids:
            segments.append(
                f"D5_QUOTE_NOT_FOUND: older[{i}] passage_id {pid!r} is not one of the older "
                f"passages given"
            )
            continue
        if quote_verify.find(quote, older_passages.get(pid) or "") is None:
            segments.append(
                f"D5_QUOTE_NOT_FOUND: older[{i}] exact_line not found word-for-word in older "
                f"passage {pid!r}"
            )

    labels_with_line = {item.get("for") for item in older if isinstance(item, dict)}
    contradictory = sorted(l for l in labels_with_line if l in set(none_for))
    if contradictory:
        segments.append(
            f"D5_BAD_SHAPE: label(s) {contradictory} appear in BOTH older and none_for -- a part "
            f"either has an older line or it does not"
        )

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
