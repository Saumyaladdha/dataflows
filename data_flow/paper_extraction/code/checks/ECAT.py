"""Step check for ECAT (schemas/ECAT.json + config/allowed_values.yaml).

The schema enforces the SHAPE. This file enforces what a schema cannot, and every rule below is
a way the v1 category sheet went wrong.

WHAT CHANGED FROM v1, AND WHY
-----------------------------
v1 rated five axes and allowed one trap per wrong option. Measured on 2017_A's first 124
ratings: 8 `cognitive_demand` values against 33 trap labels, 2.9 traps a question. The two axes
were not independent -- `recall` drew `other_one_fact` 48 times, `neighbouring_fact` 35,
`wrong_site_or_stage` 17 and `look_alike_term` 11, four names for one idea, while `calculation`
drew `calculation_slip`, which is that demand having failed. So thinking and trap are one field,
`format` and `content_shape` are one field, and a question has ONE trap.

  (0) NOT BLOCKED. A rule judged against a field the packet never sent must say BLOCKED, not
      pass. "Could not be checked" looked exactly like "checked and clean" in v1, which is how
      the whole sheet came back green.
  (1) EVERY QUESTION RATED, EXACTLY ONCE. The item is a group so the members are judged against
      each other; a missing member was not judged as a group, a duplicated one is two verdicts
      with no adjudication.
  (2) ONE TRAP, AND NOT ON THE ANSWER. There is no trap on the key: an option that attracts has
      to be a wrong one.
  (3) NO TRAP ON A DAMAGED RECORD. A trap inferred from a question whose figure or option is
      missing is a guess dressed as a finding.
  (4) EVERY LABEL IS A CURRENT ONE, read from config/allowed_values.yaml rather than restated
      here. The v0.2/v1/v2 drift happened because four files each held their own copy.
  (5) NO CLAIMS ABOUT STUDENTS. A route names the half-remembered rule or the dropped step. It
      never says how many students fall for it -- that is unfalsifiable, and §6 of the audit is
      about fields that drift toward whatever reads well.
"""

import os
import re

import yaml

#: Phrasings that assert what students in general do. A route is about the ROUTE.
BEHAVIOUR = [re.compile(p, re.I) for p in (
    r"\bstudents\s+(?:will|would|often|usually|commonly|typically|tend)\b",
    r"\b(?:most|many|some|few)\s+students\b",
    r"\ba\s+common\s+(?:error|mistake|trap|choice)\b",
    r"\bno\s+student\b",
    r"\b(?:very\s+)?tempting\b",
    r"\bthe\s+majority\b",
)]


def _allowed(root="."):
    path = os.path.join(root, "config", "allowed_values.yaml")
    with open(path, encoding="utf-8") as fh:
        av = yaml.safe_load(fh)
    return (set(av.get("trap_v2") or []), set(av.get("asks") or []),
            set(av.get("qtype") or []))


def check(output, item=None, record=None, root=".", **_kwargs):
    """Return (ok, message). `item` is the packet dict the agent was given."""
    if not isinstance(output, dict):
        return False, "output is not a JSON object"
    if "error" in output:
        return True, "agent reported an error: %s" % output["error"]

    traps_allowed, asks_allowed, types_allowed = _allowed(root)
    packet = item or {}
    supplied = {q.get("question_id"): q for q in (packet.get("questions") or [])}
    ratings = output.get("ratings") or []
    problems = []

    # (0) a check that cannot run must not report PASS
    if not supplied:
        return False, ("BLOCKED: the packet carried no `questions`, so coverage, the "
                       "official-answer rule and the damaged-record rule cannot be judged")

    # (1) coverage, exactly once
    rated = [r.get("question_id") for r in ratings]
    missing = [q for q in supplied if q not in rated]
    extra = [q for q in rated if q not in supplied]
    dupes = {q for q in rated if rated.count(q) > 1}
    if missing:
        problems.append("%d question(s) in the packet were not rated (e.g. %s)"
                        % (len(missing), missing[0]))
    if extra:
        problems.append("rated a question the packet did not supply: %s" % extra[0])
    if dupes:
        problems.append("rated twice: %s" % sorted(dupes)[0])

    for r in ratings:
        qid = r.get("question_id")
        q = supplied.get(qid) or {}
        where = qid or "<no id>"

        # (6) A `new_*` VALUE MUST COME WITH A PROPOSAL.
        # The vocabulary is open deliberately -- it was built from real questions and more keep
        # arriving. But v1 reached for a bare `new_trap` 15 times on this paper alone, and the
        # mechanism survived only because raters happened to describe it in prose. Named, it can
        # be promoted into allowed_values.yaml when it recurs; unnamed, it is just a hole.
        for field, prop_key in (("qtype", "qtype_proposed"), ("asks", "asks_proposed")):
            if str(r.get(field) or "").startswith("new_") and not r.get(prop_key):
                problems.append("%s: %s is %r but no `%s` {name, why} was given -- name what "
                                "you met so it can be added" % (where, field, r.get(field), prop_key))
        _t = r.get("trap") or {}
        if str(_t.get("label") or "").startswith("new_") and not _t.get("proposed"):
            problems.append("%s: trap is `new_trap` but carries no `proposed` {name, why}"
                            % where)

        # (4) current labels only
        if r.get("qtype") not in types_allowed:
            problems.append("%s: qtype %r is not in allowed_values.qtype_v2"
                            % (where, r.get("qtype")))
        if r.get("asks") not in asks_allowed:
            problems.append("%s: asks %r is not in allowed_values.asks"
                            % (where, r.get("asks")))

        trap = r.get("trap")
        if not isinstance(trap, dict):
            problems.append("%s: `trap` must be ONE object, not %s"
                            % (where, type(trap).__name__))
            continue
        label, opt = trap.get("label"), trap.get("option")
        if label not in traps_allowed:
            problems.append("%s: trap %r is not in allowed_values.trap_v2" % (where, label))

        # (2) no trap on the key
        key = str(q.get("correct_answer") or "")
        if opt and key and str(opt) == key:
            problems.append("%s: the trap sits on option %s, which is the official answer"
                            % (where, opt))
        if label == "no_trap" and opt:
            problems.append("%s: `no_trap` must not name an option" % where)

        # (3) a damaged record carries no trap
        if q.get("review_status") == "source_incomplete" and label != "no_trap":
            problems.append("%s: the record is source_incomplete, so the trap %r is inferred "
                            "from damage" % (where, label))

        # (5) no claims about students
        for field in ("reason", "note"):
            text = r.get(field) or ""
            for pat in BEHAVIOUR:
                if pat.search(text):
                    problems.append("%s: `%s` claims what students do (%r) -- say what the "
                                    "ROUTE is instead" % (where, field, pat.pattern))
                    break
        for pat in BEHAVIOUR:
            if pat.search(trap.get("route") or ""):
                problems.append("%s: the trap route claims what students do (%r)"
                                % (where, pat.pattern))
                break

    if problems:
        return False, "; ".join(problems[:6])
    n_real = sum(1 for r in ratings if (r.get("trap") or {}).get("label") != "no_trap")
    return True, ("%d questions rated, one trap each, %d naming a real trap and %d filler-only"
                  % (len(ratings), n_real, len(ratings) - n_real))
