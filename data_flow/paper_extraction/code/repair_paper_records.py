#!/usr/bin/env python3
"""Mechanical, provenance-recorded repairs to question records.

    python3 scripts/repair_paper_records.py --dry-run     # show what would change
    python3 scripts/repair_paper_records.py --apply

Only repairs that need NO transcription judgement are done here. Anything that would require
reading the printed page -- restoring a lost leading digit, deciding the official option order,
choosing which figure panel is option 4 -- is deliberately left alone and stays flagged by
scripts/checks/paper_quality.py, because guessing would convert a detectable defect into an
undetectable one.

Every record this touches gets a `repairs` entry naming what changed, why, and that it was a
script rather than an agent read. The pipeline's own rule is that an agent's output is evidence;
a silent edit would make that evidence false, so the edit is recorded inside the record itself.

Repairs performed:

1. paper_codes normalisation. Most rows carry short codes ("E1:8"), but 200 carry the long form
   ("NEET-2023-MAIN-E1:8"). Any join or grouping keyed on this field silently splits one booklet
   into two, which is how a 2024 row came to look as though it came from code S3.

2. Figure inheritance between identical rows. A row can be flagged `has_figure` with no file while
   the SAME question, extracted from the other booklet code, has a perfectly good figure. The file
   already exists and is already linked to the identical question, so pointing the second row at
   it adds no new claim -- it only stops the question being unanswerable in one of its two rows.
"""

import argparse
import collections
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

LONG_CODE = re.compile(r"^NEET-\d{4}-[A-Z]+-")


def _norm_question(rec):
    blob = " ".join([(rec.get("stem_en") or "")]
                    + [(rec.get("options_en") or {}).get(k) or "" for k in "1234"])
    norm = re.sub(r"[^a-z0-9]", "", blob.lower())
    return norm[:200] if len(norm) >= 60 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    rec_dir = rc.pp("papers", "records")
    recs = {}
    for name in sorted(os.listdir(rec_dir)):
        if name.endswith(".json"):
            path = os.path.join(rec_dir, name)
            with open(path, encoding="utf-8") as fh:
                r = json.load(fh)
            recs[r.get("question_id")] = (path, r)

    by_q = collections.defaultdict(list)
    for qid, (_, r) in recs.items():
        k = _norm_question(r)
        if k:
            by_q[k].append(qid)

    changes = collections.Counter()
    touched = {}
    stamp = datetime.date.today().isoformat()

    for qid, (path, r) in recs.items():
        notes = []

        codes = r.get("paper_codes") or []
        fixed = [LONG_CODE.sub("", str(c)) for c in codes]
        if fixed != [str(c) for c in codes]:
            r["paper_codes"] = fixed
            notes.append(f"paper_codes normalised to the short form {fixed} -- the long form "
                         f"splits one booklet across two values in any join")
            changes["paper_codes_normalised"] += 1

        fp = r.get("figure_path")
        if r.get("has_figure") and (not fp or not os.path.exists(rc.pp(fp) if not
                                   os.path.isabs(fp) else fp)):
            k = _norm_question(r)
            for twin in by_q.get(k, []):
                if twin == qid:
                    continue
                tfp = recs[twin][1].get("figure_path")
                if tfp and os.path.exists(tfp if os.path.isabs(tfp) else rc.pp(tfp)):
                    r["figure_path"] = tfp
                    notes.append(f"figure_path taken from {twin}, which is the SAME question "
                                 f"extracted from the other booklet code and already links this "
                                 f"file; this row was flagged has_figure with no file, leaving the "
                                 f"question unanswerable in one of its two rows")
                    changes["figure_inherited_from_twin"] += 1
                    break

        if notes:
            rep = r.setdefault("repairs", [])
            rep.append({"date": stamp, "by": "scripts/repair_paper_records.py",
                        "kind": "mechanical", "notes": notes})
            touched[qid] = (path, r)

    print(f"{len(recs)} records examined, {len(touched)} would change")
    for k, v in changes.most_common():
        print(f"   {v:4d}  {k}")
    if args.dry_run:
        for qid, (_, r) in list(touched.items())[:5]:
            print(f"\n  {qid}: {r['repairs'][-1]['notes']}")
        print("\n(dry run -- nothing written)")
        return 0

    for qid, (path, r) in touched.items():
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(r, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    print(f"wrote {len(touched)} records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
