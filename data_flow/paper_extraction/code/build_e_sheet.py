#!/usr/bin/env python3
"""Builds the E1-E5 question analysis sheet.

    python3 scripts/build_e_sheet.py --batches 8     # write agent inputs
    python3 scripts/build_e_sheet.py --merge         # merge agent outputs -> xlsx

One row per question, twelve columns:

    question_id | question_text | E1 question type | E1 why | E2 format | E2 why
                | E3 content shape | E3 why | E4 thinking | E4 why | E5 traps | E5 why

E1, E2 and E3 are derived here from printed features, so they are consistent across the sheet.
The seven "why"/judgement columns -- E1 why, E2 why, E3 why, E4 thinking, E4 why, E5 traps,
E5 why -- are about the individual question and are written by an agent that reads that question.
This script never writes them; a regex cannot say why a particular question's trap bites.

The sample is chosen to cover every category, so all 15 question types appear across the rows.
"""

import argparse
import collections
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
from build_category_sheet import (CATEGORIES, categories_of, load_questions,  # noqa: E402
                                  options_text, question_text, _norm_opts, _PERM_RE)

WORK = rc.pp("docs", "question_categories", "work")
OUTD = os.path.join(WORK, "out")

# The judgement columns an agent must supply, in sheet order.
AGENT_FIELDS = ["e1_why", "e2_why", "e3_why", "e4_thinking", "e4_why", "e5_traps", "e5_why"]

_CAT_NAME = {c[0]: c[2] for c in CATEGORIES}


def e1_type(cats):
    """The question type: its primary category name, plus any secondary ones."""
    names = [_CAT_NAME[c] for c in cats]
    return names[0] if len(names) == 1 else f"{names[0]} (also: {', '.join(names[1:])})"


def e2_format(rec):
    """How the options are PRESENTED -- the surface format a reader meets."""
    opts = _norm_opts(rec)
    vals = list(opts.values())
    if not vals:
        return "no options captured"
    if all(re.search(r"image option|will be added soon", v, re.I) for v in vals):
        return "image options (pictures, not captured in our source)"
    if all(_PERM_RE.match(v) for v in vals):
        return "permutation options (A-I, B-II, ...)"
    if any(re.search(r"both\s+a\s+and\s+r", v, re.I) for v in vals):
        return "fixed assertion-reason ladder (4 rungs)"
    if any(re.search(r"\bonly\b", v, re.I) for v in vals):
        return "combination options ('A and C only')"
    if all(re.search(r"^[\(\sA-D]*[A-D]\s*[><=]", v) for v in vals):
        return "ordering options (A > B > C)"
    if all("$" in v for v in vals) and not all(re.search(r"\d", v) for v in vals):
        return "symbolic / formula options"
    if all(re.search(r"\d", v) for v in vals):
        return "numeric options"
    return "prose options (4 text statements)"


def e3_shape(rec):
    """What this question actually CARRIES -- counted, not assumed."""
    bits = []
    if (rec.get("stem_en") or "").strip():
        bits.append("stem")
    for field, label in (("statements", "statements"), ("list_i", "list_i"), ("list_ii", "list_ii")):
        n = len([e for e in (rec.get(field) or []) if isinstance(e, dict)])
        if n:
            bits.append(f"{label}[{n}]")
    bits.append(f"options[{len(_norm_opts(rec))}]")
    if rec.get("has_figure"):
        bits.append("figure")
    if rec.get("negative_words_seen"):
        bits.append("negation:" + "/".join(rec["negative_words_seen"]))
    return " + ".join(bits)


def pick(records, per_cat):
    by_cat = collections.defaultdict(list)
    for qid, rec in records.items():
        for cat in categories_of(rec):
            by_cat[cat].append(qid)
    chosen, used = [], set()
    for cat in (c[0] for c in CATEGORIES):
        pool, picked = by_cat[cat], []
        for qid in pool:
            if len(picked) >= per_cat:
                break
            if qid in used and len(pool) > per_cat * 3:
                continue
            picked.append(qid)
            used.add(qid)
        chosen.extend(picked)
    # de-duplicate while keeping order; a question covering two categories appears once
    seen, out = set(), []
    for qid in chosen:
        if qid not in seen:
            seen.add(qid)
            out.append(qid)
    return out, by_cat


def rows_for(records, qids):
    rows = []
    for qid in qids:
        rec = records[qid]
        cats = categories_of(rec)
        rows.append({
            "question_id": qid,
            "cat_ids": cats,
            "question_text": question_text(rec),
            "options": options_text(rec),
            "e1_type": e1_type(cats),
            "e2_format": e2_format(rec),
            "e3_shape": e3_shape(rec),
        })
    return rows


def cmd_batches(args):
    records = load_questions()
    qids, _ = pick(records, args.per_cat)
    rows = rows_for(records, qids)
    os.makedirs(OUTD, exist_ok=True)
    n = args.batches
    for i in range(n):
        chunk = rows[i::n]
        path = os.path.join(WORK, f"batch_{i + 1:02d}.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(chunk, fh, ensure_ascii=False, indent=1)
        print(f"batch_{i + 1:02d}.json  {len(chunk)} questions")
    with open(os.path.join(WORK, "all_rows.json"), "w", encoding="utf-8") as fh:
        json.dump(rows, fh, ensure_ascii=False, indent=1)
    print(f"\n{len(rows)} questions total, covering "
          f"{len({c for r in rows for c in r['cat_ids']})} categories")
    print(f"agent outputs go to {os.path.relpath(OUTD, rc.pp())}/<question_id>.json")
    print(f"each must contain: {AGENT_FIELDS}")
    return 0


def cmd_merge(args):
    with open(os.path.join(WORK, "all_rows.json"), encoding="utf-8") as fh:
        rows = json.load(fh)
    filled, missing = [], []
    for row in rows:
        path = os.path.join(OUTD, f"{row['question_id']}.json")
        if not os.path.exists(path):
            missing.append(row["question_id"])
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                got = json.load(fh)
        except (OSError, json.JSONDecodeError):
            missing.append(row["question_id"])
            continue
        absent = [f for f in AGENT_FIELDS if not str(got.get(f) or "").strip()]
        if absent:
            missing.append(f"{row['question_id']} (empty: {','.join(absent)})")
            continue
        merged = dict(row)
        merged.update({f: got[f] for f in AGENT_FIELDS})
        filled.append(merged)

    out_csv = rc.pp("docs", "question_categories", "e_sheet.csv")
    header = ["question_id", "question_text", "options",
              "E1 question type", "E1 why", "E2 format", "E2 why",
              "E3 content shape", "E3 why", "E4 thinking", "E4 why", "E5 traps", "E5 why",
              "categories"]
    with open(out_csv, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        for r in filled:
            w.writerow([r["question_id"], r["question_text"], r["options"],
                        r["e1_type"], r["e1_why"], r["e2_format"], r["e2_why"],
                        r["e3_shape"], r["e3_why"], r["e4_thinking"], r["e4_why"],
                        r["e5_traps"], r["e5_why"], ";".join(r["cat_ids"])])
    print(f"wrote {os.path.relpath(out_csv, rc.pp())}  ({len(filled)} rows)")
    if missing:
        print(f"\nNOT YET WRITTEN ({len(missing)}):")
        for m in missing:
            print(f"  {m}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batches", type=int, default=8)
    ap.add_argument("--per-cat", type=int, default=4)
    ap.add_argument("--merge", action="store_true")
    args = ap.parse_args()
    os.makedirs(WORK, exist_ok=True)
    return cmd_merge(args) if args.merge else cmd_batches(args)


if __name__ == "__main__":
    sys.exit(main())
