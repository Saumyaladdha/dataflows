#!/usr/bin/env python3
"""Corrects demonstrably-wrong category assignments in exports/discovery/final/.

Two kinds of correction, kept strictly apart because only one of them is safe for a script:

1. REMOVALS, applied mechanically. A rule here only fires when the assignment is *impossible*,
   not merely doubtful -- `trap: number_near_miss` on a question whose four options are
   "A-III, B-I, C-II, D-IV" cannot be right, because there is no number for anything to be near.
   Each rule below was verified by hand against named real questions before being written down.

2. REASSIGNMENTS, listed explicitly by question id. These came from reading all 580 questions'
   stems and options one at a time; each entry names the destination and the reason. They are
   enumerated rather than derived because choosing where a question *should* go is a judgement,
   and this script must not make judgements -- it only applies ones already made and recorded.

What this script will NOT do: invent a destination for a removal. A question whose impossible
trap is stripped is left with one fewer tag and listed in the re-judge queue, because the honest
next step is for an agent to look at it again, not for a script to guess.

Originals are never edited. Output goes to exports/discovery/corrected/ with a full log, so every
change is reviewable and reversible.
"""

import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FINAL = os.path.join(ROOT, "exports", "discovery", "final")
OUT = os.path.join(ROOT, "exports", "discovery", "corrected")
RECORDS = os.path.join(ROOT, "papers", "records")
TAGS = ["question_type", "format", "content_shape", "thinking", "trap"]

#: A number, digits OR spelled out. Q-000100's options are "increase by a factor of nine / six /
#: three" -- genuinely numeric options with no digit in them, and its `calculation_slip` was
#: stripped for "containing no number". Physics and Chemistry options spell small integers often
#: enough that a digit-only test is wrong.
_NUM = re.compile(
    r"\d|\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|half|"
    r"double|triple|twice|thrice)\b", re.I)
#: Units as they really appear, including LaTeX and greek prefixes. An earlier version of this
#: regex missed `\mu F` and `\AA` and produced two false positives (Q-000002, Q-000077) -- both
#: were correctly tagged and would have been stripped.
#: Units as they really appear in this corpus. This regex has now been wrong three times, each
#: time by being too narrow, and each miss caused a CORRECT tag to be stripped:
#:   round 1 missed \mu F and \AA          -> would have stripped Q-000002, Q-000077
#:   round 2 missed T, D, cal, m^3, u, mT, bp -> did strip Q-000126, Q-000358, Q-000477, Q-000574
#: The lesson is that a deny-by-default list of units is the wrong shape for this check: the cost
#: of a miss is destroying real data, while the cost of being generous is only leaving a doubtful
#: tag for a human. So it is deliberately permissive now -- any short token that looks like a unit
#: symbol counts, and anything genuinely unitless (bare integers, names, match codes) still fails.
_UNIT = re.compile(
    r"\\mu\s*[A-Za-z]|\\AA|\\circ|\\Omega|\\text|\\mathrm|"
    r"\b(?:m/s|ms|cm|mm|nm|km|kg|mg|g|J|kJ|cal|N|V|mV|A|mA|F|C|K|T|mT|D|W|Hz|kHz|MHz|Pa|atm|bar|"
    r"L|mL|mol|M|eV|Wb|H|S|bp|u|amu|rpm|rad|deg|ohm|s|min|hr|m)\b|%|°|Å",
    re.I)
#: Does the stem really point at a picture? `given below` must NOT be here: it is NEET boilerplate
#: ("Choose the correct answer from the options given below"), present in 161 of 617 questions, and
#: including it wrongly protected 12 figure-less items from the diagram/graph strip -- found only
#: because a re-judging agent noticed that Q-000563 had moved to `process` while Q-000419 and
#: Q-000446, the same C4-compartmentalisation material, were still sitting in `diagram`.
#: Plurals are spelled out rather than relying on \b, which does not match "circuits".
_FIGWORD = re.compile(
    r"\bfigures?\b|\bgraphs?\b|\bdiagrams?\b|\bcircuits?\b|\bcurves?\b|\bplots?\b"
    r"|as shown|shown (?:in|below|here|above)|given (?:figure|graph|diagram|circuit)"
    r"|graphical|following graph|in the figure", re.I)
#: Shapes whose PICTURE lives in the options rather than the stem. A content_shape of diagram or
#: graph is legitimate for these even with has_figure false and no figure word in the stem --
#: Q-000098 ("correct graphical representation of Boyle's Law") has four graphs as its options.
_PICTORIAL_SHAPES = {"graph_options", "structure_options", "diagram_labelled",
                     "figure_to_read", "list_of_structures", "reaction_scheme"}
#: A match code ("A-III, B-I, …") or a lettered subset ("B and D only"). These carry no numbers,
#: so every numeric trap is impossible on them.
_CODE = re.compile(r"^\s*\(?[A-Ea-e]\)?\s*[-–—]\s*\(?[IViv]+\)?|only\s*$|^\s*[A-E](,|\s+and\s+)", re.I)

#: Reassignments from reading every question. (qid, tag, from, to, why)
#: `to=None` means no existing value fits -- see NEEDS_NEW_VALUE.
REASSIGN = [
    # --- format: options are plainly words, no number anywhere ---
    ("Q-000011", "format", "calculate_value", "name_or_identify", "options are error types (Random errors)"),
    ("Q-000069", "format", "calculate_value", "name_or_identify", "options are named principles (Bernoulli's)"),
    ("Q-000082", "format", "calculate_value", "name_or_identify", "options are chemical species formulae"),
    ("Q-000120", "format", "calculate_value", "name_or_identify", "options are nuclides"),
    ("Q-000130", "format", "calculate_value", "name_or_identify", "options are physical quantities"),
    ("Q-000136", "format", "calculate_value", "name_or_identify", "options are transport mechanisms"),
    ("Q-000268", "format", "calculate_value", "name_or_identify", "options are population terms (Carrying capacity)"),
    ("Q-000445", "format", "calculate_value", "name_or_identify", "options are tissue-culture products"),
    ("Q-000523", "format", "calculate_value", "name_or_identify", "options are organisms"),
    ("Q-000524", "format", "calculate_value", "name_or_identify", "options are techniques"),
    ("Q-000593", "format", "calculate_value", "name_or_identify", "options are plant names"),
    # --- format: options are plainly numbers ---
    ("Q-000091", "format", "name_or_identify", "calculate_value", "answer is a mass in grams"),
    ("Q-000359", "format", "name_or_identify", "calculate_value", "answer is an energy in joules"),
    ("Q-000384", "format", "name_or_identify", "calculate_value", "answer is a cell potential in volts"),
    ("Q-000512", "format", "name_or_identify", "calculate_value", "answer is a degree of dissociation"),
    # --- format: the ratio confusion, both directions ---
    ("Q-000045", "format", "pick_ratio", "calculate_value", "answer is a sink temperature, not a ratio"),
    ("Q-000124", "format", "pick_ratio", "calculate_value", "answer is an angular value (2pi), not a ratio"),
    ("Q-000479", "format", "pick_ratio", "calculate_value", "answer is a value in terms of T, not a ratio"),
    ("Q-000494", "format", "pick_ratio", "calculate_value", "options are bare numbers, not ratios"),
    ("Q-000086", "format", "pick_ratio", "calculate_value", "answer is a value in terms of U, not a ratio"),
    ("Q-000122", "format", "derive_expression", "pick_ratio", "options are ratios (2:1, 4:1, 1:2)"),
    ("Q-000577", "format", "derive_expression", "pick_ratio", "options are ratios (1:2, 2:1, 1:4)"),
    # --- format: expression vs value ---
    ("Q-000188", "format", "name_or_identify", "derive_expression", "options are equations/identities"),
    ("Q-000076", "format", "derive_expression", "calculate_value", "answer is a numeric coefficient"),
    ("Q-000021", "format", "derive_expression", "name_or_identify", "answer is a colour band"),
    ("Q-000488", "format", "calculate_value", "derive_expression", "options are symbolic (t*alpha*beta)"),
    # --- format: coupled answers, settled consistently. Q-000033 already correct. ---
    ("Q-000107", "format", "name_or_identify", "pick_both_parts", "answer is an ordered triple of coefficients"),
    ("Q-000191", "format", "calculate_value", "pick_both_parts", "answer is three coupled counts, respectively"),
    ("Q-000370", "format", "name_or_identify", "pick_both_parts", "answer is a pair of oxidation states"),
    ("Q-000401", "format", "calculate_value", "pick_both_parts", "answer is a verdict plus its justifying number"),
    ("Q-000276", "format", "pick_order", "pick_both_parts", "answer is two current directions, not an order"),
    ("Q-000483", "format", "calculate_value", "pick_order", "options rank three pressures"),
]

#: Questions whose answer is a bare direction, sign or comparison. No value in the 15 fits; the
#: analysts' own `asked_for` says so ("A direction only ... No magnitude, no units, no number").
#: Left in place and listed, because adding a 16th value is the owner's call, not this script's.
NEEDS_NEW_VALUE = {
    "Q-000003": "a compass direction",
    "Q-000038": "a direction (along the axis of rotation)",
    "Q-000217": "a comparison (more on bigger sphere)",
    "Q-000177": "a sign/limit class (zero, positive, infinity, negative)",
    "Q-000100": "a direction plus a factor",
}


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_records():
    out = {}
    for fn in sorted(os.listdir(RECORDS)):
        if fn.startswith("Q-") and fn.endswith(".json"):
            try:
                r = _read(os.path.join(RECORDS, fn))
            except Exception:
                continue
            if isinstance(r, dict) and r.get("question_id"):
                out[r["question_id"]] = r
    return out


def impossible(qid, tag, value, rec, shape):
    """Why this assignment cannot be right -- or None if it can.

    Only hard impossibilities. "Unlikely" is not enough: a script that strips doubtful tags is
    just an unaccountable agent.
    """
    o = rec.get("options_en") or {}
    vals = [(o.get(k) or "") for k in sorted(o)]
    if not vals:
        return None
    stem = rec.get("stem_en") or ""
    # A match-list question keeps its real content in list_i/list_ii and its options are bare
    # pairing codes; a statement question keeps it in `statements`. Looking only at stem+options
    # therefore reports "there is no number here" for questions full of numbers. Q-000354 is the
    # case that caught this: its options are "A-II, B-IV, C-I, D-III" while list_i holds "1 mol"
    # and list_ii holds "3 F / 2 F / 1 F" -- genuine electron bookkeeping, and its `numerical`
    # tag was stripped on a false premise. This is the same blind spot that made B7 hand its agent
    # a content-free record for every match question.
    def _texts(key):
        v = rec.get(key) or []
        return [x.get("text", "") if isinstance(x, dict) else str(x) for x in v]

    content = vals + [stem] + _texts("list_i") + _texts("list_ii") + _texts("statements")
    has_num = any(_NUM.search(v) for v in content)
    has_unit = any(_UNIT.search(v) for v in content)
    is_code = sum(1 for v in vals if _CODE.search(v.strip())) >= 3
    fig = bool(rec.get("has_figure")) or bool(_FIGWORD.search(stem))

    if tag == "trap":
        # These two fail differently, so they need different rules.
        #
        # `number_near_miss` is a claim about the OPTION ITSELF: the printed wrong option is a
        # number close to the key. A pairing code like "A-II, B-IV" cannot be close to anything,
        # whatever the lists contain -- so match-code options rule it out outright.
        if value == "number_near_miss":
            if is_code:
                return "number_near_miss but the options are match/letter codes, which cannot be near a value"
            if not has_num:
                return "number_near_miss but there is no number anywhere in the question"
        # `calculation_slip` is a claim about the STUDENT'S WORKING, not about how the answer is
        # printed. A match question can demand a real calculation and then record the result as a
        # pairing: Q-000354 asks how many faradays each conversion needs (list_ii holds 3F/2F/1F/5F)
        # and a miscount lands on the wrong code. Stripping it for having code options was wrong --
        # so only strip when the question contains no number at all to miscalculate.
        if value == "calculation_slip" and not has_num:
            return "calculation_slip but there is no number anywhere in the question to miscalculate"
        if value == "unit_conversion_slip" and not has_unit:
            return "unit_conversion_slip but no option or list entry carries a unit"
    if tag == "thinking":
        if value in ("numerical", "ratio_based") and not has_num and not _NUM.search(stem):
            return f"{value} but there is no number in the stem or any option"
        if value == "diagram_graph" and not fig:
            return "diagram_graph but the record has no figure and the stem never mentions one"
        if value == "direct_fact" and shape in ("match_the_lists", "list_of_statements"):
            return (f"direct_fact means one stored fact decides it, but the printed shape is "
                    f"{shape}, which requires several")
    if tag == "content_shape":
        if value in ("diagram", "graph") and not fig and shape not in _PICTORIAL_SHAPES:
            return (f"{value} but the record has no figure, the stem never mentions one, and the "
                    f"printed shape ({shape or 'unknown'}) does not put a picture in the options")
    return None


def main():
    records = load_records()
    data = {t: _read(os.path.join(FINAL, f"{t}.json")) for t in TAGS}

    shape = {}
    for c in data["question_type"].get("categories") or []:
        for q in c.get("question_ids") or []:
            shape.setdefault(q, c["name"])

    log = []

    # --- 1. reassignments, from reading every question ---
    moved = 0
    for qid, tag, src, dst, why in REASSIGN:
        cats = data[tag].get("categories") or []
        frm = next((c for c in cats if c["name"] == src), None)
        to = next((c for c in cats if c["name"] == dst), None)
        if not frm or not to:
            log.append(("ERROR", qid, tag, f"{src}->{dst}", "value not found in list"))
            continue
        if qid not in (frm.get("question_ids") or []):
            log.append(("SKIP", qid, tag, f"{src}->{dst}", f"not currently in {src}"))
            continue
        frm["question_ids"].remove(qid)
        to.setdefault("question_ids", []).append(qid)
        log.append(("MOVED", qid, tag, f"{src} -> {dst}", why))
        moved += 1

    # --- 2. mechanical removals of impossible assignments ---
    removed = 0
    rejudge = defaultdict(list)
    for tag in TAGS:
        for c in data[tag].get("categories") or []:
            keep = []
            for qid in c.get("question_ids") or []:
                rec = records.get(qid)
                why = impossible(qid, tag, c["name"], rec, shape.get(qid)) if rec else None
                if why:
                    log.append(("REMOVED", qid, tag, c["name"], why))
                    rejudge[tag].append(qid)
                    removed += 1
                else:
                    keep.append(qid)
            c["question_ids"] = keep

    # --- 3. recompute every count and subject split from the corrected ids ---
    for tag in TAGS:
        for c in data[tag].get("categories") or []:
            ids = c.get("question_ids") or []
            c["count"] = len(ids)
            by = defaultdict(int)
            for q in ids:
                by[(records.get(q) or {}).get("subject") or "(unset)"] += 1
            c["count_by_subject"] = {k: by[k] for k in sorted(by)}
            # Drop examples that are no longer members -- an example outside its own category is
            # how a reader loses trust in the whole sheet.
            exs = [e for e in (c.get("examples") or [])
                   if not isinstance(e, dict) or e.get("question_id") in set(ids)]
            if exs != (c.get("examples") or []):
                log.append(("EXAMPLE_DROPPED", c["name"], tag, "", "example was no longer a member"))
            c["examples"] = exs

    os.makedirs(OUT, exist_ok=True)
    for tag in TAGS:
        data[tag]["corrected"] = {
            "note": "counts and subject splits recomputed from corrected question_ids",
            "reassignments_applied": sum(1 for r in log if r[0] == "MOVED" and r[2] == tag),
            "impossible_assignments_removed": sum(1 for r in log if r[0] == "REMOVED" and r[2] == tag),
            "questions_needing_rejudgement": sorted(set(rejudge[tag])),
        }
        with open(os.path.join(OUT, f"{tag}.json"), "w", encoding="utf-8") as fh:
            json.dump(data[tag], fh, indent=1, ensure_ascii=False)

    with open(os.path.join(OUT, "_corrections_log.json"), "w", encoding="utf-8") as fh:
        json.dump({"needs_new_format_value": NEEDS_NEW_VALUE,
                   "entries": [dict(zip(("action", "question", "tag", "value", "why"), r))
                               for r in log]}, fh, indent=1, ensure_ascii=False)

    print(f"reassigned (from reading each question) : {moved}")
    print(f"removed as impossible (mechanical rules): {removed}")
    print(f"questions needing re-judgement          : {len({q for v in rejudge.values() for q in v})}")
    for tag in TAGS:
        n = len(set(rejudge[tag]))
        if n:
            print(f"    {tag:15s} {n}")
    print(f"\nwrote {os.path.relpath(OUT, ROOT)}/ (originals untouched)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
