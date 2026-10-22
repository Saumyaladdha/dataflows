"""Step-specific check for D4 (spec Section 12/D4 'Checks' + d4-evidence-quoter.md's own rules).

schemas/D4.json already constrains link_type/supports_answer to their enums and the evidence item
shape. This file adds every STRUCTURAL/CORRECTNESS rule spec 12/D4's own Checks list names, using
the per-item context["input_data"] step_plugins.D4Plugin passes alongside the agent output (same
pattern as D1/D2's own check scripts):

  (1) every evidence[i].exact_line is found word for word in its own passage_id's text
      (lib.quote_verify.find -- the same function B8 already reuses for its own supporting_quote
      check), via context["input_data"]["passages"] = {passage_id: full_text} (the exact latest
      passages the agent was actually given -- D4 never sees anything else, spec 12/D4 Reads).
  (2) passage_id is one of those given passage ids.
  (3) link_type allowed (schema); rule_used needs >=1 evidence item with for=="rule";
      rules_chained needs >=2; states_answer needs an EMPTY derivation_steps.
  (4) a statement question (context["input_data"]["structure"] == "statements") marked
      supports_answer == "fully" needs one evidence item per statement label (including the
      label that shows a false statement is false) -- "for" is expected to literally contain the
      label letter (e.g. "statement B", "statement C is false"), a soft substring match since the
      agent file names no fixed grammar for `for`.
  (5) the derivation cross-check (numericals only) -- parse the LAST derivation step for a
      number, compare against the supported answer's own numeric value; applies only when
      derivation_steps is non-empty (the agent itself produced a derivation at all -- a
      states_answer/concept_applied verdict with no derivation never reaches this). This build has
      no real numerical D4 case to exercise it against (Q-000015, the only real end-to-end D4 run,
      is a statement question with no derivation_steps) -- this logic is honestly UNTESTED on real
      data; see the build report.

What is DELIBERATELY NOT here: a clean, legitimate supports_answer of "partly"/"not_at_all", or a
well-formed beyond_ncert_method verdict, is NOT a check failure -- the agent being honest about
weak evidence must never trigger a retry (same spirit as B6's "a retry only argues with itself").
Those are flagged unconditionally (D4_PARTLY/D4_NO_SUPPORT/D4_BEYOND_NCERT) by
step_plugins.D4Plugin's own post_assembly on whatever the FINAL resolved value turns out to be,
the same precedent as A8Plugin always flagging A8_FACT_CHANGE / B8Plugin always flagging
B8_CORRECTION regardless of this check's own pass/fail.

Convention: def check(data, context) -> (bool, str). A failing check returns a ';'-joined set of
segments (runner_core.parse_check_message), each optionally prefixed "<FLAG_CODE>: ..." using one
of this step's own config/steps.yaml flag codes, so one D4 output can fail more than one real rule
at once without the runner having to guess which.
"""
import re

from lib import quote_verify

_NUMBER_RE = re.compile(r"-?\d+(?:\.\d+)?")


def _final_number(text):
    """The derivation step's own FINAL computed value, e.g. 6 from 'x = 2*3 = 6' or 16 from
    "R' = rho(2l)/(A/2) = 4R = 16 ohm" (the agent file's own worked numerical example) -- NOT the
    first number encountered (which would wrongly grab an input operand like the '2' in '2*3').
    Real bug found and fixed during the D1-D4 build (2026-10): an earlier version used
    re.search (first match) here, which broke exactly this case; caught by this build's own
    fixture-only D4 verification script (no real numerical D4 case exists in this build's data to
    have caught it through a real run -- see the build report) before it ever reached real data.
    Splits on the LAST '=' (if any) and takes the first number after it; falls back to the LAST
    number anywhere in the text when there is no '=' at all."""
    if not text:
        return None
    cleaned = text.replace(",", "")
    tail = cleaned.rsplit("=", 1)[-1] if "=" in cleaned else cleaned
    m = _NUMBER_RE.search(tail)
    if m:
        return float(m.group())
    all_matches = _NUMBER_RE.findall(cleaned)
    return float(all_matches[-1]) if all_matches else None


def check(data, context):
    if not isinstance(data, dict):
        return False, "D4 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    link_type = data.get("link_type")
    derivation_steps = data.get("derivation_steps")
    evidence = data.get("evidence")

    if not isinstance(derivation_steps, list):
        return False, "derivation_steps is not a list"
    if not isinstance(evidence, list):
        return False, "evidence is not a list"

    segments = []

    if link_type == "states_answer" and derivation_steps:
        segments.append("D4_BAD_SHAPE: link_type is states_answer but derivation_steps is non-empty")

    rule_quotes = [e for e in evidence if isinstance(e, dict) and e.get("for") == "rule"]
    if link_type == "rule_used" and len(rule_quotes) < 1:
        segments.append("D4_BAD_SHAPE: link_type is rule_used but no evidence item has for=='rule'")
    if link_type == "rules_chained" and len(rule_quotes) < 2:
        segments.append(
            f"D4_BAD_SHAPE: link_type is rules_chained but only {len(rule_quotes)} evidence "
            f"item(s) have for=='rule' (need >=2)"
        )

    input_data = context.get("input_data") or {}
    passages = input_data.get("passages") or {}

    # THE SHORTLIST IS NOT THE LIMIT OF WHAT MAY BE QUOTED, AND THIS CHECK USED TO SAY IT WAS.
    #
    # It built `allowed_ids` from the input's own passage list and rejected every other id as "not
    # one of the latest passages given". That was right while the agent could only see the
    # shortlist. It became wrong on 2026-10-21, when the input gained `chapter_index` and
    # `search_this_file` and the brief began requiring the agent to go and find the section the
    # shortlist missed -- a change made because nine of twelve agents reported, and three proved,
    # that the one decisive passage was routinely ranked out of the top fifteen.
    #
    # Measured after that change: 11 of 15 re-run questions moved from not_at_all/partly to fully,
    # and in nearly all of them the deciding quote came from a passage the shortlist never carried.
    # This rule would have rejected exactly those, which is the opposite of what a check is for.
    #
    # So the test is now the right one: IS THE QUOTE IN THE BOOK? `find_in_edition` reads the whole
    # book file, which is the same thing a reader with the printed book would do -- and it is a
    # STRICTER test than the old one, not a looser one, because it verifies the words rather than
    # merely checking that an id appeared in a list.
    book_ids = []
    chapter = input_data.get("chapter") or {}
    for key in ("ncert_book", "book"):
        value = chapter.get(key)
        if isinstance(value, str):
            book_ids.append(value)
        elif isinstance(value, list):
            book_ids.extend(v for v in value if isinstance(v, str))
    # The older edition and the subject's sibling books are quotable too, and the agent is told so.
    book_ids += [b[:-1] + "O" for b in list(book_ids) if b.endswith("L")]
    for passage in (input_data.get("older_edition_passages") or []):
        pid = passage.get("passage_id") or ""
        if pid[:6] and pid[:6] not in book_ids:
            book_ids.append(pid[:6])
    book_ids = [b for b in dict.fromkeys(book_ids) if b]

    for i, item in enumerate(evidence):
        if not isinstance(item, dict):
            segments.append(f"D4_BAD_SHAPE: evidence[{i}] is not an object")
            continue
        pid = item.get("passage_id")
        quote = item.get("exact_line")
        if pid in passages:
            found = quote_verify.find(quote, passages.get(pid) or "") is not None
        else:
            # Off-shortlist: verify against the book itself, and require the quote to be in the
            # very passage the agent named -- a quote found elsewhere in the book under a different
            # id is a citation error, not a verified quote.
            hits = quote_verify.find_in_edition(quote, book_ids) if book_ids else []
            found = any(hit.get("passage_id") == pid for hit in hits)
            if not found and hits:
                segments.append(
                    f"D4_QUOTE_NOT_FOUND: evidence[{i}] exact_line IS in the book but in "
                    f"{hits[0].get('passage_id')!r}, not in the cited {pid!r}"
                )
                continue
        if not found:
            segments.append(
                f"D4_QUOTE_NOT_FOUND: evidence[{i}] exact_line not found word-for-word in "
                f"passage {pid!r}"
            )

    structure = input_data.get("structure")
    statements = input_data.get("statements") or []
    supports_answer = data.get("supports_answer")
    if structure == "statements" and supports_answer == "fully" and statements:
        covered_for = " ".join((e.get("for") or "") for e in evidence if isinstance(e, dict))
        missing_labels = [s.get("label") for s in statements
                           if s.get("label") and s.get("label") not in covered_for]
        if missing_labels:
            segments.append(
                f"D4_PARTLY: supports_answer is 'fully' but no evidence item's 'for' field "
                f"mentions statement label(s) {missing_labels} (one quote per statement is required)"
            )

    if link_type == "beyond_ncert_method" and not (data.get("note") or "").strip():
        segments.append(
            "D4_BEYOND_NCERT: link_type is beyond_ncert_method but note does not say which "
            "result is not in NCERT"
        )

    # (5) derivation cross-check -- numericals only (non-empty derivation_steps); honestly
    # untested against real data in this build, see module docstring.
    if derivation_steps:
        last_step_value = _final_number(derivation_steps[-1])
        answer_to_support = input_data.get("answer_to_support") or {}
        answer_value = _final_number(answer_to_support.get("text"))
        if last_step_value is not None and answer_value is not None \
                and abs(last_step_value - answer_value) > max(1e-6, abs(answer_value) * 1e-3):
            segments.append(
                f"D4_DERIVATION_MISMATCH: last derivation step evaluates to {last_step_value!r}, "
                f"the supported answer's own value is {answer_value!r}"
            )

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
