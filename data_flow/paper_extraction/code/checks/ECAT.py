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
    # "the majority" ALONE IS NOT A HEADCOUNT. It is a semiconductor term (majority carriers) and
    # an ordinary quantifier in biology (cortical nephrons, the majority, have short loops), and
    # as a bare pattern it rejected three correct routes before it caught a single real claim.
    # What the rule is actually about is a claim that most PEOPLE do something, so the pattern
    # now needs either a word for the people or a verb of choosing.
    r"\bthe\s+majority\s+(?:of\s+(?:students|candidates|them|test[\s-]?takers)"
    r"|(?:pick|choose|select|mark|go\s+for|fall\s+for)s?)\b",
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

        # (2) no trap on the key -- and "the key" is EVERY ACCEPTED OPTION, not just the first.
        # A paper that awards two options prints both in `accepted_answers` while
        # `correct_answer` holds only one of them. Reading the single field made this file
        # contradict itself: rule 2 forbade covering an awarded option and rule 8 then demanded
        # coverage of that same option, so six ratings across four papers failed for doing
        # exactly what the rulebook asks ("where it holds more than one option, rule 3 must
        # clear EVERY accepted option"). The agents were right; the check was reading one field.
        key = str(q.get("correct_answer") or "")
        accepted = {str(a) for a in (q.get("accepted_answers") or []) if a}
        if key:
            accepted.add(key)
        if opt and str(opt) in accepted:
            problems.append("%s: the trap sits on option %s, which is an official answer"
                            % (where, opt))
        if label == "no_trap" and opt:
            problems.append("%s: `no_trap` must not name an option" % where)

        # (3) a damaged record carries no trap
        if q.get("review_status") == "source_incomplete" and label != "no_trap":
            problems.append("%s: the record is source_incomplete, so the trap %r is inferred "
                            "from damage" % (where, label))

        # (6) A REAL TRAP IS CARRIED AT THE DEPTH THE REVIEWED ARTIFACTS USE. The label and a
        #     single route sentence were never the teaching -- the 60 questions the subject
        #     experts signed off name who falls, why the option feels right, and the student's
        #     own steps with the breaking one marked. A tag without those is a classification,
        #     and a classification is what the SMEs asked us to stop shipping.
        others = r.get("other_options") or []
        if label != "no_trap":
            for field in ("who", "feels"):
                if not (trap.get(field) or "").strip():
                    problems.append("%s: the trap names no `%s`" % (where, field))
            if not (trap.get("ways") or []):
                problems.append("%s: the trap walks no route -- give the student's steps with "
                                "the breaking one marked `bad`" % where)

        # (7) EVERY BAD STEP CARRIES ITS FIX, and every route breaks somewhere. A route whose
        #     steps are all `ok` has described a correct solution, not a trap.
        for holder, tag in [(trap, "trap")] + [(o, "option %s" % o.get("option")) for o in others]:
            for way in (holder.get("ways") or []):
                marks = [s.get("mark") for s in (way.get("steps") or [])]
                if "bad" not in marks:
                    problems.append("%s: %s has a route with no `bad` step -- it never breaks"
                                    % (where, tag))
                for step in (way.get("steps") or []):
                    if step.get("mark") == "bad" and not (step.get("fix") or "").strip():
                        problems.append("%s: %s has a `bad` step with no `fix`" % (where, tag))

        # (8) EVERY WRONG OPTION IS ACCOUNTED FOR. The artifacts explain all of them; a page that
        #     explains one and leaves two blank is the gap the SMEs read as missing work. A
        #     `filler` is a finding, but rule 5.3 of the shared rules requires it be proved.
        # A DISPUTED KEY SUSPENDS THE COVERAGE RULE, and only when the rater says so out loud.
        # Four ratings across two papers hit the contradiction this resolves: the stored key was
        # contradicted by the paper's own printed answer line (2021_O1 q170 stores "1" while the
        # line reads "Answer: (a) or (d)") or by the source the question is built on (2018_NN
        # q110 ferrous/ferric, q120 pachytene/diplotene, q175 alpha/beta 1->6). In each the rater
        # left the possibly-awarded option unassigned -- which is what rule 2 demands -- and rule
        # 8 then failed them for it. Forcing coverage there would put a trap on an option that
        # may be an answer, so the exception is allowed; it costs nothing, because it only opens
        # when `verdict` is `arguable_key` or `disputed_key` is flagged, both of which a reviewer
        # sees. An uncovered option with no such declaration still fails.
        disputed = (r.get("verdict") == "arguable_key"
                    or "disputed_key" in (r.get("flags") or []))
        if label != "no_trap" and accepted and not disputed \
                and q.get("review_status") != "source_incomplete":
            wrong = {str(n) for n in "1234"} - accepted
            covered = ({str(opt)} if opt else set()) | {str(o.get("option")) for o in others}
            missing = sorted(wrong - covered)
            if missing:
                problems.append("%s: wrong option(s) %s carry no trap and no filler finding"
                                % (where, ", ".join(missing)))
        for o in others:
            if o.get("role") == "filler" and not (o.get("proof") or "").strip():
                problems.append("%s: option %s is called filler with no `proof` of what was "
                                "checked" % (where, o.get("option")))
            if o.get("role") == "trap" and not (o.get("ways") or []):
                problems.append("%s: option %s is called a trap but walks no route"
                                % (where, o.get("option")))
            if str(o.get("option")) in accepted:
                problems.append("%s: option %s is an official answer and cannot be a trap or a "
                                "filler" % (where, o.get("option")))

        # (5) no claims about students -- over every field a reader sees, not only the two the
        #     first cut of this rule covered. 150 of 179 routes on 2026_11 opened with a
        #     headcount, so the surface this scans is the surface that drifts.
        for field in ("reason", "note"):
            text = r.get(field) or ""
            for pat in BEHAVIOUR:
                if pat.search(text):
                    problems.append("%s: `%s` claims what students do (%r) -- say what the "
                                    "ROUTE is instead" % (where, field, pat.pattern))
                    break
        prose = [("trap route", trap.get("route")), ("trap who", trap.get("who")),
                 ("trap feels", trap.get("feels"))]
        for holder, tag in [(trap, "trap")] + [(o, "option %s" % o.get("option")) for o in others]:
            if holder is not trap:
                prose += [("%s who" % tag, holder.get("who")),
                          ("%s feels" % tag, holder.get("feels")),
                          ("%s proof" % tag, holder.get("proof"))]
            for way in (holder.get("ways") or []):
                prose.append(("%s way name" % tag, way.get("name")))
                for step in (way.get("steps") or []):
                    prose.append(("%s step" % tag, step.get("text")))
                    prose.append(("%s fix" % tag, step.get("fix")))
        for tag, text in prose:
            if not text:
                continue
            for pat in BEHAVIOUR:
                if pat.search(text):
                    problems.append("%s: the %s claims what students do (%r)"
                                    % (where, tag, pat.pattern))
                    break

    if problems:
        return False, "; ".join(problems[:6])
    n_real = sum(1 for r in ratings if (r.get("trap") or {}).get("label") != "no_trap")
    return True, ("%d questions rated, one trap each, %d naming a real trap and %d filler-only"
                  % (len(ratings), n_real, len(ratings) - n_real))
