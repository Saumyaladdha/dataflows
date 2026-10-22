#!/usr/bin/env python3
"""F6 · Gold set and scoring (spec Section 14/F6, targets from Section 1.1).

    python3 scripts/score_gold.py
    python3 scripts/score_gold.py --gold gold/gold_set.csv --out gold/scores.md
    python3 scripts/score_gold.py --fail-under-target   # non-zero exit if any target is missed

Compares each step's output — as it stands in `papers/records/<QID>.json`, attributed to the step
that produced it via `field_sources` — against the reviewer-confirmed values in
`gold/gold_set.csv`, and writes `gold/scores.md`: one table per Section 1.1 criterion against its
target, one table per step, and the actual list of mismatches so M7 ("fix and re-score") has
something to act on.

gold_set.csv is accepted in either shape, because the spec fixes its contents (90 questions, 30
per subject, every field reviewer-confirmed) but not its columns:

  LONG  question_id,field,gold_value[,subject,year,note]      one row per field
  WIDE  question_id[,subject,year],<field>,<field>,...         one row per question

Values are compared after a light normalisation (see `values_match`): JSON is parsed so
`["BIO11-CH10"]` matches `BIO11-CH10`; lists compare as sets when order carries no meaning;
LaTeX and whitespace go through the project's own normalisers for text fields. Nothing else is
coerced — a different answer is a different answer.

This script never writes to the records, never closes a flag and never releases anything. It only
reads and scores.
"""
import argparse
import collections
import json
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import f_common as fc  # noqa: E402
from lib import io as lib_io  # noqa: E402
from lib import latex_normalise  # noqa: E402
from lib import quote_verify  # noqa: E402
from lib import text_normalise  # noqa: E402

GOLD_PATH = fc.pp("gold", "gold_set.csv")
SCORES_PATH = fc.pp("gold", "scores.md")

EXPECTED_GOLD_SIZE = 90
EXPECTED_PER_SUBJECT = 30

META_COLUMNS = {"question_id", "qid", "subject", "year", "sitting", "note", "notes",
                "reviewer", "confirmed_at", "field", "gold_value", "value"}

# Spec Section 1.1's criteria, each mapped to the record fields that carry it and its target.
# `kind` selects the comparison: "text" normalises LaTeX/whitespace, "set" compares id lists
# order-blind, "exact" is literal, "quote" re-verifies the quote against the named edition, and
# "repeat" scores "no known repeat missed" (a gold repeat group must still be present).
CRITERIA = [
    {"id": "text_exact", "name": "Text exact after double reading", "target": 0.99,
     "fields": ["stem_en", "options_en", "statements", "list_i", "list_ii"], "kind": "text"},
    {"id": "answer_joined", "name": "Every answer joined to the right key", "target": 1.00,
     "fields": ["official_answer"], "kind": "exact"},
    {"id": "chapter", "name": "Chapter correct", "target": 0.98,
     "fields": ["chapter_ids"], "kind": "set"},
    {"id": "subtopic", "name": "Subtopic correct", "target": 0.95,
     "fields": ["subtopic_ids"], "kind": "set"},
    {"id": "quotes_found", "name": "Every NCERT quote found word for word in the named edition",
     "target": 1.00, "fields": ["evidence", "older_evidence"], "kind": "quote"},
    {"id": "evidence_passage", "name": "Right evidence passage", "target": 0.95,
     "fields": ["evidence"], "kind": "evidence_passage"},
    {"id": "repeats", "name": "No known repeat missed", "target": 1.00,
     "fields": ["repeat_group_id", "related_ids"], "kind": "repeat"},
    {"id": "thinking", "name": "Thinking tag agreement with faculty (per subject)",
     "target": 0.85, "fields": ["category_primary"], "kind": "exact", "per_subject": True},
]

FIELD_ALIASES = {
    "chapter_ids": ("chapter_ids", "d1_chapter_ids"),
    "subtopic_ids": ("subtopic_ids", "d2_subtopic_ids"),
}


class GoldSetProblem(Exception):
    pass


# --------------------------------------------------------------------------------------------
# Loading the gold set
# --------------------------------------------------------------------------------------------

def load_gold(path=None):
    """Return ({qid: {field: gold_value}}, {qid: {subject, year}}, shape)."""
    path = path or GOLD_PATH
    if not os.path.exists(path):
        raise GoldSetProblem(
            f"{os.path.relpath(path, fc.PROJECT_ROOT)} does not exist. F6 scores against a gold "
            f"set a reviewer confirmed field by field (spec 14/F6 steps 1-3); there is nothing to "
            f"score without one, and inventing rows would produce a meaningless score.")
    rows = lib_io.read_csv(path)
    if not rows:
        raise GoldSetProblem(f"{os.path.relpath(path, fc.PROJECT_ROOT)} has a header but no rows.")

    columns = set(rows[0].keys())
    qid_col = "question_id" if "question_id" in columns else ("qid" if "qid" in columns else None)
    if qid_col is None:
        raise GoldSetProblem(
            f"{os.path.relpath(path, fc.PROJECT_ROOT)} has no `question_id` column; its columns "
            f"are {sorted(columns)}.")

    gold = collections.defaultdict(dict)
    meta = {}
    value_col = next((c for c in ("gold_value", "value") if c in columns), None)
    if "field" in columns and value_col:
        shape = "long"
        for row in rows:
            qid = (row.get(qid_col) or "").strip()
            field = (row.get("field") or "").strip()
            if not qid or not field:
                continue
            gold[qid][field] = row.get(value_col)
            meta.setdefault(qid, {})
            if row.get("subject"):
                meta[qid]["subject"] = row["subject"].strip()
            if row.get("year"):
                meta[qid]["year"] = row["year"].strip()
    else:
        shape = "wide"
        field_cols = [c for c in rows[0] if c not in META_COLUMNS]
        for row in rows:
            qid = (row.get(qid_col) or "").strip()
            if not qid:
                continue
            meta.setdefault(qid, {})
            if row.get("subject"):
                meta[qid]["subject"] = row["subject"].strip()
            if row.get("year"):
                meta[qid]["year"] = row["year"].strip()
            for c in field_cols:
                v = row.get(c)
                if v is None or str(v).strip() == "":
                    continue
                gold[qid][c] = v
    return dict(gold), meta, shape


def gold_shape_warnings(gold, meta, records):
    """Everything about the gold set a reader of scores.md must know before trusting a number."""
    warnings = []
    if len(gold) != EXPECTED_GOLD_SIZE:
        warnings.append(f"The gold set has {len(gold)} question(s); spec 14/F6 calls for "
                        f"{EXPECTED_GOLD_SIZE} (30 per subject). Every percentage below is over "
                        f"this smaller set and is correspondingly less reliable.")
    by_subject = collections.Counter()
    for qid in gold:
        subject = (meta.get(qid, {}).get("subject")
                   or (records.get(qid) or {}).get("subject") or "unknown")
        by_subject[subject] += 1
    for subject, n in sorted(by_subject.items()):
        if n != EXPECTED_PER_SUBJECT:
            warnings.append(f"Subject {subject!r} has {n} gold question(s); spec 14/F6 calls for "
                            f"{EXPECTED_PER_SUBJECT}.")
    missing = sorted(q for q in gold if q not in records)
    if missing:
        warnings.append(f"{len(missing)} gold question(s) have no record in papers/records/ and "
                        f"were scored as missing, not skipped: {', '.join(missing[:12])}"
                        + ("..." if len(missing) > 12 else ""))
    return warnings, dict(by_subject)


# --------------------------------------------------------------------------------------------
# Comparison
# --------------------------------------------------------------------------------------------

def _coerce(value):
    """Parse a gold cell into a Python value. A spreadsheet cell is always a string, so
    `["A","B"]` and `4` arrive as text; JSON first, then the raw string."""
    if value is None:
        return None
    if not isinstance(value, str):
        return value
    s = value.strip()
    if s == "":
        return None
    if s[0] in "[{" or s in ("true", "false", "null") or _looks_numeric(s):
        try:
            return json.loads(s)
        except json.JSONDecodeError:
            return s
    return s


def _looks_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def _as_set(value):
    if value is None:
        return set()
    if isinstance(value, (list, tuple, set)):
        return {str(v).strip() for v in value if str(v).strip()}
    if isinstance(value, dict):
        return {f"{k}={v}" for k, v in value.items()}
    text = str(value).strip()
    if not text:
        return set()
    if any(sep in text for sep in (",", ";")):
        return {p.strip() for p in text.replace(";", ",").split(",") if p.strip()}
    return {text}


def _norm_text(value):
    if isinstance(value, dict):
        return {str(k): _norm_text(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_norm_text(v) for v in value]
    if value is None:
        return None
    s = text_normalise.normalise_quote(str(value))
    return latex_normalise.normalise(s)


def values_match(kind, gold_value, actual):
    """(matched: bool, detail: str) for one field."""
    g = _coerce(gold_value)
    if kind == "set":
        gs, as_ = _as_set(g), _as_set(actual)
        return gs == as_, f"gold={sorted(gs)} actual={sorted(as_)}"
    if kind == "text":
        return _norm_text(g) == _norm_text(actual), f"gold={g!r} actual={actual!r}"
    if kind == "evidence_passage":
        gp = {(e or {}).get("passage_id") for e in g} if isinstance(g, list) else _as_set(g)
        ap = {(e or {}).get("passage_id") for e in (actual or [])} if isinstance(actual, list) \
            else _as_set(actual)
        gp.discard(None)
        ap.discard(None)
        return gp == ap, f"gold passages={sorted(gp)} actual={sorted(ap)}"
    if kind == "repeat":
        gs, as_ = _as_set(g), _as_set(actual)
        # "No known repeat missed": every repeat the gold set knows about must still be there.
        # Extra repeats the pipeline found are not scored as misses here — a false positive is a
        # different defect and D11's own check owns it.
        return gs.issubset(as_), f"gold={sorted(gs)} actual={sorted(as_)}"
    return str(g) == str(actual) if not isinstance(g, (list, dict)) else g == actual, \
        f"gold={g!r} actual={actual!r}"


def record_value(rec, field):
    for alias in FIELD_ALIASES.get(field, (field,)):
        if alias in rec and rec[alias] not in (None, [], {}):
            return rec[alias]
    return rec.get(field)


def field_step(rec, field):
    """Which step produced the field, from the record's own field_sources (spec 5.8)."""
    sources = rec.get("field_sources") or {}
    for alias in FIELD_ALIASES.get(field, (field,)):
        if alias in sources:
            return (sources[alias] or {}).get("step")
    return None


# --------------------------------------------------------------------------------------------
# Quote re-verification (criterion: every NCERT quote found word for word, 100%, by script)
# --------------------------------------------------------------------------------------------

def verify_quotes(rec):
    """Re-verify every quote in a record's evidence against the passage it names.

    This criterion is a SCRIPT check in spec 1.1, not a comparison with the gold set: the quote
    either occurs word for word in the named edition or it does not. Returns
    (checked, found, failures)."""
    checked = found = 0
    failures = []
    for key in ("evidence", "older_evidence"):
        for ev in rec.get(key) or []:
            quote = (ev or {}).get("exact_line")
            passage_id = (ev or {}).get("passage_id")
            if not quote or not passage_id:
                continue
            checked += 1
            text = _passage_text(passage_id)
            if text is None:
                failures.append(f"{key}: passage {passage_id} not found in ncert/passages/")
                continue
            if quote_verify.find(quote, text) is None:
                failures.append(f"{key}: quote not found in {passage_id}: {quote[:70]!r}")
            else:
                found += 1
    return checked, found, failures


_PASSAGE_CACHE = None


def _passage_text(passage_id):
    global _PASSAGE_CACHE
    if _PASSAGE_CACHE is None:
        _PASSAGE_CACHE = {}
        import glob
        for path in sorted(glob.glob(fc.pp("ncert", "passages", "*.jsonl"))):
            for row in lib_io.read_jsonl(path):
                pid = row.get("passage_id")
                if pid:
                    _PASSAGE_CACHE[pid] = row.get("text") or ""
    return _PASSAGE_CACHE.get(passage_id)


# --------------------------------------------------------------------------------------------
# Scoring
# --------------------------------------------------------------------------------------------

def score(gold, meta, records):
    per_criterion = []
    per_step = collections.defaultdict(lambda: {"checked": 0, "matched": 0, "failures": []})
    all_failures = []

    for crit in CRITERIA:
        if crit["kind"] == "quote":
            checked = matched = 0
            failures = []
            for qid in sorted(gold):
                rec = records.get(qid)
                if not rec:
                    continue
                c, f, fails = verify_quotes(rec)
                checked += c
                matched += f
                for msg in fails:
                    failures.append({"question_id": qid, "field": "evidence", "step": "D4/D5",
                                     "detail": msg})
            per_criterion.append(_criterion_row(crit, checked, matched, failures))
            for f in failures:
                per_step[f["step"]]["failures"].append(f)
            all_failures.extend(failures)
            continue

        checked = matched = 0
        failures = []
        by_subject = collections.defaultdict(lambda: [0, 0])
        for qid in sorted(gold):
            rec = records.get(qid)
            subject = (meta.get(qid, {}).get("subject")
                       or (rec or {}).get("subject") or "unknown")
            for field in crit["fields"]:
                if field not in gold[qid]:
                    continue
                checked += 1
                by_subject[subject][1] += 1
                if rec is None:
                    failures.append({"question_id": qid, "field": field, "step": None,
                                     "detail": "no record in papers/records/"})
                    continue
                actual = record_value(rec, field)
                ok, detail = values_match(crit["kind"], gold[qid][field], actual)
                step = field_step(rec, field) or "(unattributed)"
                per_step[step]["checked"] += 1
                if ok:
                    matched += 1
                    by_subject[subject][0] += 1
                    per_step[step]["matched"] += 1
                else:
                    f = {"question_id": qid, "field": field, "step": step, "detail": detail}
                    failures.append(f)
                    per_step[step]["failures"].append(f)
        row = _criterion_row(crit, checked, matched, failures)
        if crit.get("per_subject"):
            row["per_subject"] = {
                s: {"checked": v[1], "matched": v[0],
                    "rate": (v[0] / v[1]) if v[1] else None,
                    "meets_target": (v[0] / v[1]) >= crit["target"] if v[1] else None}
                for s, v in sorted(by_subject.items())}
            row["meets_target"] = all(x["meets_target"] for x in row["per_subject"].values()
                                      if x["meets_target"] is not None) \
                if row["per_subject"] else None
        per_criterion.append(row)
        all_failures.extend(failures)

    return {
        "per_criterion": per_criterion,
        "per_step": {k: v for k, v in sorted(per_step.items(), key=lambda kv: fc.step_index(kv[0]))},
        "failures": all_failures,
    }


def _criterion_row(crit, checked, matched, failures):
    rate = (matched / checked) if checked else None
    return {
        "id": crit["id"], "name": crit["name"], "target": crit["target"],
        "fields": crit["fields"], "checked": checked, "matched": matched, "rate": rate,
        "meets_target": (rate >= crit["target"]) if rate is not None else None,
        "failures": failures,
    }


# --------------------------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------------------------

def _pct(rate):
    return "n/a" if rate is None else f"{rate * 100:.1f}%"


def render_markdown(result, gold, meta, warnings, by_subject, shape, gold_path):
    lines = []
    lines.append("# Gold set scores")
    lines.append("")
    lines.append(f"Generated {fc.now_iso()} by `scripts/score_gold.py` (spec Section 14/F6) "
                 f"against targets in SPEC Section 1.1.")
    lines.append("")
    lines.append(f"- gold set: `{os.path.relpath(gold_path, fc.PROJECT_ROOT)}` "
                 f"({shape} shape), {len(gold)} question(s)")
    lines.append("- subjects: " + ", ".join(f"{s} {n}" for s, n in sorted(by_subject.items())))
    lines.append(f"- field comparisons made: "
                 f"{sum(c['checked'] for c in result['per_criterion'])}")
    lines.append("")

    if warnings:
        lines.append("## Read this before trusting the numbers")
        lines.append("")
        for w in warnings:
            lines.append(f"- {w}")
        lines.append("")

    lines.append("## Against Section 1.1's targets")
    lines.append("")
    lines.append("| Criterion | Target | Checked | Matched | Rate | Meets target |")
    lines.append("|---|---|---|---|---|---|")
    for c in result["per_criterion"]:
        verdict = ("n/a — nothing to score" if c["meets_target"] is None
                   else ("yes" if c["meets_target"] else "**NO**"))
        lines.append(f"| {c['name']} | {_pct(c['target'])} | {c['checked']} | {c['matched']} | "
                     f"{_pct(c['rate'])} | {verdict} |")
    lines.append("")

    for c in result["per_criterion"]:
        if not c.get("per_subject"):
            continue
        lines.append(f"### {c['name']} — per subject")
        lines.append("")
        lines.append("| Subject | Checked | Matched | Rate | Meets target |")
        lines.append("|---|---|---|---|---|")
        for s, v in c["per_subject"].items():
            verdict = ("n/a" if v["meets_target"] is None
                       else ("yes" if v["meets_target"] else "**NO**"))
            lines.append(f"| {s} | {v['checked']} | {v['matched']} | {_pct(v['rate'])} | "
                         f"{verdict} |")
        lines.append("")

    lines.append("## Per step")
    lines.append("")
    if not result["per_step"]:
        lines.append("No field in the gold set could be attributed to a step "
                     "(`field_sources` is empty for every gold question).")
    else:
        lines.append("| Step | Checked | Matched | Rate | Failures |")
        lines.append("|---|---|---|---|---|")
        for step, v in result["per_step"].items():
            rate = (v["matched"] / v["checked"]) if v["checked"] else None
            lines.append(f"| {step} | {v['checked']} | {v['matched']} | {_pct(rate)} | "
                         f"{len(v['failures'])} |")
    lines.append("")

    lines.append("## Every mismatch")
    lines.append("")
    if not result["failures"]:
        lines.append("None.")
    else:
        lines.append("| Question | Field | Step | Gold vs actual |")
        lines.append("|---|---|---|---|")
        for f in result["failures"]:
            detail = str(f["detail"]).replace("|", "\\|")
            if len(detail) > 300:
                detail = detail[:300] + " …"
            lines.append(f"| {f['question_id']} | {f['field']} | {f.get('step')} | {detail} |")
    lines.append("")
    lines.append("## What to do with a missed target")
    lines.append("")
    lines.append("Spec 18.3 (M7): for each step under target, read its failures above, improve "
                 "the agent file (**never relax a check**), bump its prompt version, re-run that "
                 "step for the pilot chapters, let the cascade re-run what depends on it, and "
                 "score again. Record each change in `docs/OPEN_QUESTIONS.md`.")
    lines.append("")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description="F6 · score the pipeline against the gold set (spec 14/F6).")
    ap.add_argument("--gold", default=GOLD_PATH, help="Path to gold/gold_set.csv.")
    ap.add_argument("--out", default=SCORES_PATH, help="Path to write gold/scores.md.")
    ap.add_argument("--fail-under-target", action="store_true",
                    help="Exit non-zero if any Section 1.1 target is missed.")
    ap.add_argument("--dry-run", action="store_true", help="Score and print; write no file.")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    try:
        gold, meta, shape = load_gold(args.gold)
    except GoldSetProblem as e:
        print(f"F6 cannot score: {e}", file=sys.stderr)
        return 2

    records = fc.load_records()
    warnings, by_subject = gold_shape_warnings(gold, meta, records)
    result = score(gold, meta, records)
    markdown = render_markdown(result, gold, meta, warnings, by_subject, shape, args.gold)

    if not args.dry_run:
        lib_io.atomic_write_text(args.out, markdown)

    if args.json:
        print(json.dumps({"per_criterion": [{k: v for k, v in c.items() if k != "failures"}
                                            for c in result["per_criterion"]],
                          "failures": len(result["failures"]),
                          "warnings": warnings}, indent=2))
    else:
        print(f"F6 score_gold · {len(gold)} gold question(s), {shape} shape")
        for w in warnings:
            print(f"  WARNING: {w}")
        for c in result["per_criterion"]:
            verdict = "n/a" if c["meets_target"] is None else ("ok" if c["meets_target"] else "UNDER TARGET")
            print(f"  {c['name']:<58s} {_pct(c['rate']):>7s} / {_pct(c['target']):>6s}  {verdict}")
        print(f"  mismatches: {len(result['failures'])}")
        if not args.dry_run:
            print(f"  written   : {os.path.relpath(args.out, fc.PROJECT_ROOT)}")

    missed = [c for c in result["per_criterion"] if c["meets_target"] is False]
    if args.fail_under_target and missed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
