"""Step-specific check for D6 (spec Section 12/D6 'Checks' + d6-status-note-writer.md's rules).

D6 is a three-part step (spec 12/D6 Worker line, verbatim): "SCRIPT decides status; AGENT
`d6-status-note-writer` writes the note; SCRIPT verifies." The rule ladder (0, 1, 2, 3, 3b, 4,
first match wins) is NOT here — it is the script's own decision, made BEFORE the agent is
dispatched, in step_plugins.D6Plugin._decide_status(). This file is the third part: it verifies
what the agent wrote, using the per-item `context["input_data"]` the plugin passes alongside the
output.

  (1) `syllabus_status` echoes the script's decision unchanged. The agent does not get to change
      the status — if it does, that is a hard failure, not a disagreement to adjudicate, because
      the status was never the agent's judgement to make.
  (2) `note_type` is one of the types legal for that status
      (`context["input_data"]["allowed_note_types"]`, computed by the plugin from the status and
      D4's link_type — spec 12/D6 rule 4: "if link_type = beyond_ncert_method, note type
      outside_rules").
  (3) spec 12/D6 Checks, first half: "every quoted line exists in the edition it names."
      `context["input_data"]["editions"]` is {"L"|"O"|"M": {passage_id: full_text}}, built by the
      plugin FROM DISK (ncert/passages/<BOOK><LETTER>.jsonl via D3's own three lists), never from
      what the agent echoed. A line whose `edition` is "O" but which only exists in the latest
      book fails with its own message — mislabelling which edition a line came from is the whole
      defect the `written_differently` / `deleted` note types exist to describe, so it must not
      pass quietly.
  (4) spec 12/D6 Checks, second half: "note matches its template." The seven templates are spec
      3.1's, verbatim; _TEMPLATES below holds one regex per note_type. Matching is done after a
      light normalisation (curly quotes -> straight, whitespace collapsed) and the sentence-final
      period after a closing quote is optional, because an NCERT line often ends in its own
      period and agents reasonably write `..."` rather than `...".`. Nothing else is relaxed: the
      fixed scaffolding words of the template must be present exactly.
  (5) every quoted_lines[i].text actually appears inside reason_note (for every note_type whose
      template quotes a line at all). A `quoted_lines` entry that is not in the note is either a
      stray or a sign the note quoted something else; both need a human, and the retry message
      can say which.

What is DELIBERATELY NOT checked here:
  - Whether `written_differently` was the RIGHT choice (i.e. whether the older line really states
    the same fact in different words). That is the agent's judgement — spec 12/D6 gives it to the
    agent and routes it to a reviewer via D6_NOTE_APPROVAL (normal), not to a script.
  - Present tense / "no explanations outside the template" beyond what the template regex already
    pins down.

Convention: def check(data, context) -> (bool, str). Segments are ';'-joined. These segments
deliberately carry NO flag-code prefix: spec 12/D6's own "On failure" is "retry; then SCRIPT fills
the template from verified lines, D6_TEMPLATE_NOTE (low)" — the outcome flag depends on how the
chain ends, not on which rule failed, so step_plugins.D6Plugin owns the flag decision and this
file only reports what is wrong.
"""
import re

from lib import quote_verify
from lib import text_normalise

_PASSAGE_ID_RE = re.compile(r"^([A-Z]{3})(\d{2})([LOM])-")

# spec 3.1, "The five reason-note templates (D6/D7)" -- seven rows. `_Q` is one quoted line:
# greedy, because an NCERT line can itself contain a straight quote character. `_P` is the
# optional sentence-final period after a closing quote (see module docstring (4)).
_Q = r'"(.+)"'
_P = r"\.?"

_TEMPLATES = {
    "same_both": re.compile(rf'^Answer from the latest NCERT: {_Q}{_P}$'),
    "written_differently": re.compile(
        rf'^Answer from the latest NCERT: {_Q}\. Remember: the older NCERT wrote it as {_Q}\. '
        rf'Same fact; follow the latest wording\.$'
    ),
    "answer_changed": re.compile(
        rf'^By the latest NCERT the answer is \(([^)]+)\): {_Q}\. The older NCERT said {_Q}, '
        rf'which gave \(([^)]+)\)\. Follow the latest\.$'
    ),
    "deleted": re.compile(
        rf'^This question is from content deleted from the latest NCERT\. The answer is according '
        rf'to the older NCERT: {_Q}{_P}$'
    ),
    "outside": re.compile(
        r'^This fact is not in any NCERT edition\. The answer is from the official key\.$'
    ),
    "outside_rules": re.compile(
        rf'^This question uses a result that is not given in NCERT\. The NCERT rules involved '
        rf'are: {_Q}\. The answer is from the official key\.$'
    ),
    "lab_manual": re.compile(rf'^Answer from the NCERT lab manual: {_Q}{_P}$'),
}

# note_type `outside` quotes nothing; every other template quotes at least one line.
_NOTE_TYPES_WITHOUT_QUOTES = {"outside"}

_EDITION_NAME = {"L": "latest", "O": "older", "M": "lab manual"}


def _norm(s):
    """Curly quotes -> straight, ligatures -> letters, whitespace collapsed -- lib's own
    normalise_quote, reused rather than reimplemented (spec 5.7)."""
    return text_normalise.normalise_quote(s or "")


def _edition_letter(passage_id):
    m = _PASSAGE_ID_RE.match(passage_id or "")
    return m.group(3) if m else None


def check(data, context):
    if not isinstance(data, dict):
        return False, "D6 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    input_data = context.get("input_data") or {}
    decided_status = input_data.get("syllabus_status")
    allowed_note_types = input_data.get("allowed_note_types") or []
    editions = input_data.get("editions") or {}

    segments = []

    status = data.get("syllabus_status")
    if decided_status and status != decided_status:
        segments.append(
            f"syllabus_status is {status!r} but the SCRIPT already decided {decided_status!r}; "
            f"D6's agent writes the note only, it never changes the status"
        )

    note_type = data.get("note_type")
    if allowed_note_types and note_type not in allowed_note_types:
        segments.append(
            f"note_type {note_type!r} is not legal for syllabus_status {decided_status!r} "
            f"(allowed: {sorted(allowed_note_types)})"
        )

    quoted_lines = data.get("quoted_lines")
    if not isinstance(quoted_lines, list):
        return False, "quoted_lines is not a list"

    reason_note = data.get("reason_note") or ""
    note_norm = _norm(reason_note)

    for i, q in enumerate(quoted_lines):
        if not isinstance(q, dict):
            segments.append(f"quoted_lines[{i}] is not an object")
            continue
        edition = q.get("edition")
        pid = q.get("passage_id")
        text = q.get("text")

        if edition not in editions:
            segments.append(
                f"quoted_lines[{i}] names edition {edition!r}, for which this question has no "
                f"passages at all (available: {sorted(editions.keys())})"
            )
            continue

        letter = _edition_letter(pid)
        if letter and letter != edition:
            segments.append(
                f"quoted_lines[{i}] says edition {edition!r} ({_EDITION_NAME.get(edition, '?')}) "
                f"but passage_id {pid!r} belongs to edition {letter!r} "
                f"({_EDITION_NAME.get(letter, '?')})"
            )
            continue

        passages = editions.get(edition) or {}
        if pid not in passages:
            segments.append(
                f"quoted_lines[{i}] passage_id {pid!r} is not one of the {edition!r}-edition "
                f"passages given for this question"
            )
            continue
        if quote_verify.find(text, passages.get(pid) or "") is None:
            segments.append(
                f"quoted_lines[{i}] text not found word-for-word in {edition!r}-edition passage "
                f"{pid!r}"
            )
            continue
        if note_type not in _NOTE_TYPES_WITHOUT_QUOTES and _norm(text) not in note_norm:
            segments.append(
                f"quoted_lines[{i}] text is verified against {pid!r} but does not appear inside "
                f"reason_note itself"
            )

    if note_type in _TEMPLATES:
        if not _TEMPLATES[note_type].match(note_norm):
            segments.append(
                f"reason_note does not match the {note_type!r} template from spec 3.1; got "
                f"{reason_note[:160]!r}"
            )
    elif note_type is not None:
        segments.append(f"note_type {note_type!r} has no template in spec 3.1")

    if note_type not in _NOTE_TYPES_WITHOUT_QUOTES and note_type in _TEMPLATES and not quoted_lines:
        segments.append(
            f"note_type {note_type!r} quotes at least one line in its template, but quoted_lines "
            f"is empty"
        )

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
