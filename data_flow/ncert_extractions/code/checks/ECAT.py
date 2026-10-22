"""Step-specific check for ECAT (docs/question_categories/RULEBOOK.md + schemas/ECAT.json).

schemas/ECAT.json enforces the SHAPE. This file enforces the rules that a JSON schema cannot
express, each of which corresponds to a way v1's category sheet went wrong:

  (1) EVERY QUESTION IN THE PACKET IS RATED, EXACTLY ONCE. The item is a group precisely so the
      members are judged against each other (rulebook rule 0.7). A packet that comes back missing a
      member was not judged as a group, and a duplicated member means two verdicts with no
      adjudication.

  (2) NO TRAP ON A `source_incomplete` QUESTION. Rulebook rule 5. 113 of the 580 questions are
      `source_incomplete`, and the per-subject analyses in exports/discovery/clusters_pass_b/
      recorded roughly 98 devices that were actually our own extraction damage. A trap mechanism
      inferred from a question whose figure or option is missing is a guess dressed as a finding.

  (3) NO TRAP ON THE OFFICIAL ANSWER. There is no trap on the answer; an option that attracts has
      to be a wrong one.

  (4) EVERY TRAP LABEL IS A CURRENT ONE, read from config/allowed_values.yaml rather than restated.
      The whole v0.2/v1/v2 drift happened because four files each held their own copy of the trap
      list. This check owns no list.

  (5) `elimination` CARRIES ITS EVIDENCE. Rulebook section 4c: name the pair or fact and the options
      it strikes out. v1 applied `elimination` with no shortcut shown, which is what made it
      contradict `direct_fact` on the same axis.

  (6) NO REASON MAY ASSERT STUDENT BEHAVIOUR. SPEC Rule 22; this project holds no response data.
      `obviously_wrong` was retired for exactly this ("no student who read the stem would be drawn
      to it"), and a reason that reintroduces the claim in prose is the same unfalsifiable move.

  (7) `new_demand` AND `new_trap` MUST BE DESCRIBED. An escape hatch with no description makes the
      vocabulary look complete while hiding what did not fit -- the opposite of its purpose.

WHAT IS DELIBERATELY NOT HERE: any judgement about whether a label is the RIGHT one. That is the
agent's job and a script re-deriving it would either be wrong or be the agent. What a script can do
is refuse an answer that breaks a rule the rulebook states outright, and that is all this does.
"""

import json
import os
import re

#: phrasings that assert how students behave. Checked case-insensitively on `reason` and `route`.
BEHAVIOUR = [
    r"\ba common (?:error|mistake)\b",
    r"\bmost students\b",
    r"\bno student\b",
    r"\bstudents (?:will|would|tend|often|usually|typically)\b",
    r"\bobviously wrong\b",
    r"\blikely to (?:be )?(?:pick|choose|select)",
    r"\beasily fooled\b",
    r"\btempting to (?:a |the )?student\b",
]


def _allowed(root):
    """The current vocabulary, read from config rather than restated here (rule 4 above)."""
    import yaml
    with open(os.path.join(root, "config", "allowed_values.yaml"), encoding="utf-8") as fh:
        values = yaml.safe_load(fh)
    return set(values.get("trap") or []), set(values.get("trap_verdict") or [])


def check(output, item=None, record=None, root=".", **_kwargs):
    """Return (ok, message). `item` is the packet dict the agent was given."""
    if not isinstance(output, dict):
        return False, "output is not a JSON object"
    if "error" in output:
        return True, "agent reported an error: %s" % output["error"]

    traps_allowed, verdicts_allowed = _allowed(root)
    packet = item or {}
    supplied = {q.get("question_id"): q for q in (packet.get("questions") or [])}
    ratings = output.get("ratings") or []
    problems = []

    # (1) coverage, exactly once
    rated = [r.get("question_id") for r in ratings]
    missing = sorted(set(supplied) - set(rated))
    extra = sorted(set(rated) - set(supplied))
    dupes = sorted({q for q in rated if rated.count(q) > 1})
    if supplied and missing:
        problems.append("not rated: %s -- the group must be judged together, so every member is "
                        "rated or the comparison did not happen" % ", ".join(missing))
    if extra:
        problems.append("rated but not in this packet: %s" % ", ".join(extra))
    if dupes:
        problems.append("rated twice: %s" % ", ".join(dupes))

    if packet.get("group") and output.get("group") != packet["group"]:
        problems.append("group is %r but the packet is %r -- output written against another packet"
                        % (output.get("group"), packet["group"]))

    for r in ratings:
        qid = r.get("question_id") or "?"
        q = supplied.get(qid, {})
        traps = r.get("traps") or []

        # (2) no trap where the source is incomplete
        if q.get("review_status") == "source_incomplete" and traps:
            problems.append("%s is source_incomplete (%s) yet carries %d trap(s); rulebook rule 5 "
                            "says E4/E5 stay empty and the verdict is source_damage_artifact"
                            % (qid, q.get("review_status_why") or "reason not recorded", len(traps)))

        # THE KEY, UNDER EITHER NAME. v1 packets call it `official_answer`; the papers_v2 packets
        # built by build_ecat_packets_v2.py call it `correct_answer`. Reading only the v1 spelling
        # left check (3) -- "there is no trap on the answer" -- silently never firing for any v2
        # packet: it did not fail, it simply had no answer to compare against, which is the worst
        # kind of broken check. Found by a rater who enforced the rule by hand and said so.
        answer = str(q.get("official_answer") or q.get("correct_answer") or "").strip()
        seen_options = set()
        for t in traps:
            label, option = t.get("label"), str(t.get("option") or "")
            # (4) current vocabulary only
            if label not in traps_allowed:
                problems.append("%s: trap %r is not in config/allowed_values.yaml `trap` -- if "
                                "nothing fits, use new_trap and describe it" % (qid, label))
            # (3) never the answer
            if answer and option == answer:
                problems.append("%s: trap on option %s, which is the official answer; there is no "
                                "trap on the answer" % (qid, option))
            if option in seen_options:
                problems.append("%s: two traps on option %s" % (qid, option))
            seen_options.add(option)
            # (7) escape hatch must be described
            if label == "new_trap" and len(str(t.get("route") or "").split()) < 5:
                problems.append("%s: new_trap needs a full description of the device in `route`"
                                % qid)
            for pattern in BEHAVIOUR:
                if re.search(pattern, str(t.get("route") or ""), re.I):
                    problems.append("%s: trap route asserts student behaviour (%r); describe the "
                                    "arithmetic or the fact instead (SPEC Rule 22)"
                                    % (qid, re.search(pattern, t["route"], re.I).group(0)))

        for v in (r.get("verdicts") or []):
            if v not in verdicts_allowed:
                problems.append("%s: verdict %r is not in `trap_verdict`" % (qid, v))

        # (5) elimination carries its evidence
        if "elimination" in (r.get("strategy_available") or []):
            if len(str(r.get("strategy_evidence") or "").split()) < 5:
                problems.append("%s: `elimination` requires strategy_evidence naming the pair or "
                                "fact and the options it strikes out" % qid)

        # (7) the other escape hatch
        if r.get("cognitive_demand") == "new_demand" and not str(r.get("note") or "").strip():
            problems.append("%s: new_demand needs a description in `note`" % qid)

        # unsure forms must say why, so "could not decide" stays distinct from "never judged"
        for field in ("concept", "cognitive_demand", "solution_structure"):
            if r.get(field) == "" and not str(r.get("note") or "").strip():
                problems.append("%s: %s was left blank with no reason in `note`; 'judged and could "
                                "not be decided' and 'never judged' must look different "
                                "(SPEC Rule 19)" % (qid, field))

        # (6) reasons about the question, not about students
        for pattern in BEHAVIOUR:
            m = re.search(pattern, str(r.get("reason") or ""), re.I)
            if m:
                problems.append("%s: reason asserts student behaviour (%r); we hold no response "
                                "data (SPEC Rule 22)" % (qid, m.group(0)))

    if problems:
        return False, "; ".join(problems[:8]) + (
            " (+%d more)" % (len(problems) - 8) if len(problems) > 8 else "")

    n_traps = sum(len(r.get("traps") or []) for r in ratings)
    n_incomplete = sum(1 for q in supplied.values()
                       if q.get("review_status") == "source_incomplete")

    # REPORTED, NOT FAILED: the agent found damage on a question the sheet calls `verified`. The
    # agent read the options; `review_status` was DERIVED by scripts/build_category_sheet_v2.py from
    # patterns (placeholder text, duplicate options, a missing figure). Prose glosses standing in
    # for drawn structures pass every one of those patterns while still being unusable, so the
    # agent is the better witness here and the derivation is what needs revisiting. Failing the
    # agent for being right would teach it to stop reporting.
    contested = [r.get("question_id") for r in ratings
                 if "source_damage_artifact" in (r.get("verdicts") or [])
                 and supplied.get(r.get("question_id"), {}).get("review_status") != "source_incomplete"]
    extra = ""
    if contested:
        extra = ("; DERIVATION DISAGREEMENT -- %s carry source_damage_artifact but the sheet "
                 "derived review_status=verified. Raise ECAT_SOURCE_INCOMPLETE and re-derive: the "
                 "agent read the options, review_status was pattern-derived"
                 % ", ".join(contested))
    return True, ("%d questions rated, %d traps with an option and a route, %d source_incomplete "
                  "correctly carrying none%s"
                  % (len(ratings), n_traps, n_incomplete, extra))


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("output")
    ap.add_argument("--item")
    ap.add_argument("--root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                   "..", ".."))
    args = ap.parse_args(argv)
    with open(args.output, encoding="utf-8") as fh:
        out = json.load(fh)
    item = None
    if args.item:
        with open(args.item, encoding="utf-8") as fh:
            item = json.load(fh)
    ok, message = check(out, item=item, root=args.root)
    print(("PASS  " if ok else "FAIL  ") + message)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
