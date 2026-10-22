"""Step-specific check for D7 (spec Section 12/D7 'Checks' + d7-latest-answer-checker.md's rules).

spec 12/D7 Checks, verbatim: "quote verified in the latest edition; `change_id` exists and covers
an evidence passage." Both need the per-item `context["input_data"]` step_plugins.D7Plugin passes
alongside the output, which is built from an EXPLICIT ALLOWLIST (spec Rule 10: "B6 and D7 never
see coaching material") — see D7Plugin._build_input.

  (1) `quote` is found word for word in the LATEST edition, via
      `context["input_data"]["latest_passages"]` = {passage_id: full_text}, read by the plugin
      from disk (ncert/passages/<BOOK>L.jsonl via D3's `latest` list), never from what the agent
      echoed. Empty quote is allowed ONLY when latest_answer is "unsure" — the agent genuinely
      could not decide and has nothing to cite. A non-empty quote that is not in any latest
      passage is a hard failure: D7's whole authority is that the latest book really says this.
  (2) `change_id`, when not null, exists among the change-log entries given AND covers an
      evidence passage — i.e. its old_passage_id or new_passage_id is one of the D4/D5 evidence
      passages (`context["input_data"]["evidence_passage_ids"]`). An id that exists but points at
      some other passage does not explain THIS question's answer.
  (3) internal consistency: `same_as_official` must agree with latest_answer == official_answer.
      Both come from the same output; a contradiction between them means the agent misread its
      own conclusion, and downstream (D7_ANSWER_CHANGED, the D4 re-run for latest_answer, what a
      student is taught) keys off `same_as_official`, so this one must not slip through.
  (4) `sentence_for_note` is empty exactly when same_as_official is true, and otherwise matches
      the agent file's own template: "By the older NCERT the answer was (<official>); by the
      latest NCERT it is (<latest>)." with the two option numbers actually filled in correctly.
  (5) the agent file's own rule: "if none explains it, set change_id null and explain in note" —
      so a changed answer with change_id null must carry a non-empty note. (That outcome is NOT
      a failure of this check beyond the missing note: it is the real D7_UNEXPLAINED_CHANGE
      (high) case, raised by D7Plugin, and the honest answer when the change log has no row.)

What is DELIBERATELY NOT checked here:
  - Whether the latest book really implies that option. That is the agent's judgement.
  - Whether a change-log entry's `change_type` is consistent with an answer change. A
    `wording_only` row accompanying a changed answer is suspicious, but spec 12/D7's own worked
    example goes the other way ("Change log says wording_only and the latest line still supports
    the official option -> same_as_official true"), and nothing in the spec forbids the suspicious
    combination. step_plugins.D7Plugin records it in the flag message instead of failing it.

Convention: def check(data, context) -> (bool, str). Segments are ';'-joined, each optionally
prefixed "<FLAG_CODE>: ..." using one of this step's own config/steps.yaml flag codes.
"""
import re

from lib import quote_verify

_SENTENCE_RE = re.compile(
    r"^By the older NCERT the answer was \(([^)]*)\); by the latest NCERT it is \(([^)]*)\)\.$"
)


def check(data, context):
    if not isinstance(data, dict):
        return False, "D7 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    input_data = context.get("input_data") or {}
    latest_passages = input_data.get("latest_passages") or {}
    change_log_entries = input_data.get("change_log_entries") or {}
    evidence_passage_ids = set(input_data.get("evidence_passage_ids") or [])
    official_answer = input_data.get("official_answer")

    latest_answer = data.get("latest_answer")
    same_as_official = data.get("same_as_official")
    quote = data.get("quote") or ""
    change_id = data.get("change_id")
    sentence = data.get("sentence_for_note") or ""
    note = (data.get("note") or "").strip()

    segments = []

    # (1) quote verified in the latest edition.
    if not quote.strip():
        if latest_answer != "unsure":
            segments.append(
                "D7_QUOTE_NOT_FOUND: quote is empty but latest_answer is not 'unsure'; the latest "
                "line that decides the answer must be quoted"
            )
    else:
        found_in = [pid for pid, text in latest_passages.items()
                    if quote_verify.find(quote, text or "") is not None]
        if not found_in:
            segments.append(
                "D7_QUOTE_NOT_FOUND: quote not found word-for-word in any of the latest-edition "
                "passages given"
            )

    # (3) same_as_official vs latest_answer/official_answer.
    if latest_answer != "unsure" and official_answer is not None:
        expected_same = str(latest_answer) == str(official_answer)
        if isinstance(same_as_official, bool) and same_as_official != expected_same:
            segments.append(
                f"D7_INCONSISTENT: same_as_official is {same_as_official} but latest_answer "
                f"{latest_answer!r} vs official answer {str(official_answer)!r} says it should be "
                f"{expected_same}"
            )

    # (2) change_id exists and covers an evidence passage.
    if change_id is not None:
        entry = change_log_entries.get(change_id)
        if entry is None:
            segments.append(
                f"D7_INCONSISTENT: change_id {change_id!r} is not one of the change-log entries "
                f"given ({sorted(change_log_entries.keys())})"
            )
        else:
            covered = {entry.get("old_passage_id"), entry.get("new_passage_id")} - {None, ""}
            if evidence_passage_ids and not (covered & evidence_passage_ids):
                segments.append(
                    f"D7_INCONSISTENT: change_id {change_id!r} covers passages {sorted(covered)}, "
                    f"none of which is one of this question's evidence passages "
                    f"{sorted(evidence_passage_ids)}"
                )

    # (4)/(5) the appended sentence, and the "no entry explains it" note.
    if same_as_official is True:
        if sentence.strip():
            segments.append(
                "sentence_for_note must be empty when same_as_official is true (nothing changed, "
                "so nothing is appended to the reason note)"
            )
    elif same_as_official is False:
        if not sentence.strip():
            segments.append(
                "same_as_official is false but sentence_for_note is empty; the changed answer "
                "needs its sentence for the reason note"
            )
        else:
            m = _SENTENCE_RE.match(sentence.strip())
            if not m:
                segments.append(
                    f"sentence_for_note does not match the template 'By the older NCERT the "
                    f"answer was (<official>); by the latest NCERT it is (<latest>).'; got "
                    f"{sentence[:160]!r}"
                )
            else:
                said_official, said_latest = m.group(1).strip(), m.group(2).strip()
                if official_answer is not None and said_official != str(official_answer):
                    segments.append(
                        f"sentence_for_note names ({said_official}) as the older/official answer, "
                        f"but the official answer is ({official_answer})"
                    )
                if latest_answer is not None and said_latest != str(latest_answer):
                    segments.append(
                        f"sentence_for_note names ({said_latest}) as the latest answer, but "
                        f"latest_answer is ({latest_answer})"
                    )
        if change_id is None and not note:
            segments.append(
                "same_as_official is false with change_id null, but note is empty; the agent must "
                "say why no change-log entry explains the change"
            )

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
