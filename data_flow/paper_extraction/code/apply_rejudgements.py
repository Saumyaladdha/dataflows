#!/usr/bin/env python3
"""Applies the agents' re-judgements onto the corrected lists, producing exports/discovery/applied/.

Pipeline position: final/ (as discovered) -> corrected/ (wrong assignments removed or moved)
-> applied/ (holes refilled by agents) -> the workbook.

Three safety properties this script enforces, because the inputs are agent output:

1. **Only values that already exist may be assigned.** The taxonomy is settled; re-judging is a
   membership fix. An `assign` naming a value not in the list is refused and reported, never
   silently created.
2. **Only questions that actually have a hole are refilled.** The re-judging agents were handed
   larger queues than survived my later rule fixes -- 32 of my strips turned out to be wrong and
   were restored, so an agent may offer a verdict on a question that no longer needs one. Applying
   it anyway would re-break what the fix repaired, so those are skipped and counted.
3. **Every count is recomputed from the resulting ids**, never carried over.

`trap` differs from the other two by design: a question can carry several traps (the step runs
once per wrong option), so its assignments are additive and it does not partition the corpus.
`thinking` and `content_shape` are single-pick, so a second assignment to the same question is a
conflict and is refused.
"""

import json
import os
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISC = os.path.join(ROOT, "exports", "discovery")
CORR = os.path.join(DISC, "corrected")
REJ = os.path.join(DISC, "rejudged")
OUT = os.path.join(DISC, "applied")
RECORDS = os.path.join(ROOT, "papers", "records")
TAGS = ["question_type", "format", "content_shape", "thinking", "trap"]
MULTI = {"trap"}


def _read(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    records = {}
    for fn in sorted(os.listdir(RECORDS)):
        if fn.startswith("Q-") and fn.endswith(".json"):
            try:
                r = _read(os.path.join(RECORDS, fn))
            except Exception:
                continue
            if isinstance(r, dict) and r.get("question_id"):
                records[r["question_id"]] = r

    data = {t: _read(os.path.join(CORR, f"{t}.json")) for t in TAGS}
    report = {"applied": [], "refused": [], "skipped_no_longer_needed": [], "new_values": []}

    # --- merge the one new category the splitting pass established ---
    #
    # The five splitting agents proposed exactly one new value between them: `copied_from_stem`.
    # It is merged here rather than hand-edited into final/ so the originals stay untouched and
    # the provenance is visible in one place.
    #
    # Why this one is trusted: the agent did not argue from the mechanism being distinct (which is
    # arguable) but showed that the merge it was supposed to live under had never actually
    # happened -- only 6 of its 22 questions were inside `number_near_miss`, 4 carried no trap at
    # all, and the rest sat in values naming a slip the student performed, when the point of these
    # options is that they performed none. It then re-derived the set mechanically (wrong options
    # whose numbers are a subset of the stem's), which corroborated 6, surfaced 3 it had missed,
    # and eliminated 4 it had wrongly included. I verified one independently: Q-000266's stem
    # prints "(BB/Bb)" and option 4 is "BB/Bb", with no number anywhere for a near-miss to mean.
    SPLITS = os.path.join(DISC, "splits")
    for tag in TAGS:
        p = os.path.join(SPLITS, f"{tag}.json")
        if not os.path.exists(p):
            continue
        sp = _read(p)
        for key, val in sp.items():
            if not (isinstance(val, dict) and str(val.get("verdict", "")).startswith("give it its own")):
                continue
            ids = [q for q in (val.get("question_ids") or []) if q in records]
            if not ids:
                continue
            cats = data[tag].setdefault("categories", [])
            if any(c["name"] == key for c in cats):
                continue
            cats.append({
                "name": key,
                "definition": val.get("definition")
                or "A value or label printed in the stem, offered back as a wrong option; the "
                   "student pattern-matches the stem instead of solving.",
                "decision": "new",
                "was": None,
                "why_this_name": "how a student describes it: they picked the number already given",
                "question_ids": ids,
                "examples": val.get("examples") or [],
                "evidence": (val.get("why") or "")[:400],
                "not_to_be_confused_with":
                    "number_near_miss, which requires the option to be CLOSE to the correct "
                    "value; a stem echo generally is not (Q-000459 echoes 10 N against a key of 6 N)",
            })
            report["new_values"].append({"tag": tag, "name": key, "count": len(ids)})

    for tag in TAGS:
        path = os.path.join(REJ, f"{tag}.json")
        if not os.path.exists(path):
            continue
        rj = _read(path)
        cats = {c["name"]: c for c in data[tag].get("categories") or []}
        needs = set(data[tag].get("corrected", {}).get("questions_needing_rejudgement") or [])
        placed = defaultdict(set)
        for c in data[tag].get("categories") or []:
            for q in c.get("question_ids") or []:
                placed[q].add(c["name"])

        for entry in rj.get("rejudged") or []:
            qid = entry.get("question_id")
            if not qid:
                continue
            if qid not in needs:
                report["skipped_no_longer_needed"].append(
                    {"question": qid, "tag": tag,
                     "why": "my own strip rule was later found wrong and this tag was restored; "
                            "applying the re-judgement would re-break it"})
                continue
            assigns = entry.get("assign")
            assigns = assigns if isinstance(assigns, list) else ([assigns] if assigns else [])
            for name in assigns:
                if name not in cats:
                    report["refused"].append(
                        {"question": qid, "tag": tag, "assign": name,
                         "why": "value does not exist in the settled list; not creating it"})
                    continue
                if tag not in MULTI and placed[qid]:
                    report["refused"].append(
                        {"question": qid, "tag": tag, "assign": name,
                         "why": f"{tag} is single-pick and this question already sits in "
                                f"{sorted(placed[qid])}"})
                    continue
                if qid in (cats[name].get("question_ids") or []):
                    continue
                cats[name].setdefault("question_ids", []).append(qid)
                placed[qid].add(name)
                report["applied"].append({"question": qid, "tag": tag, "assign": name,
                                          "why": (entry.get("why") or "")[:200]})

    # recompute every count and subject split from the resulting ids
    for tag in TAGS:
        for c in data[tag].get("categories") or []:
            ids = sorted(set(c.get("question_ids") or []))
            c["question_ids"] = ids
            c["count"] = len(ids)
            by = defaultdict(int)
            for q in ids:
                by[(records.get(q) or {}).get("subject") or "(unset)"] += 1
            c["count_by_subject"] = {k: by[k] for k in sorted(by)}
            c["examples"] = [e for e in (c.get("examples") or [])
                             if not isinstance(e, dict) or e.get("question_id") in set(ids)]
        data[tag]["applied"] = {
            "rejudgements_applied": sum(1 for r in report["applied"] if r["tag"] == tag),
            "refused": sum(1 for r in report["refused"] if r["tag"] == tag),
            "still_untagged": sorted(
                set(data[tag].get("corrected", {}).get("questions_needing_rejudgement") or [])
                - {q for c in data[tag].get("categories") or []
                   for q in (c.get("question_ids") or [])}),
        }

    os.makedirs(OUT, exist_ok=True)
    for tag in TAGS:
        with open(os.path.join(OUT, f"{tag}.json"), "w", encoding="utf-8") as fh:
            json.dump(data[tag], fh, indent=1, ensure_ascii=False)
    with open(os.path.join(OUT, "_apply_report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=1, ensure_ascii=False)

    print(f"applied   : {len(report['applied'])}")
    print(f"refused   : {len(report['refused'])}")
    print(f"skipped   : {len(report['skipped_no_longer_needed'])} (tag restored by a later rule fix)")
    for tag in TAGS:
        a = data[tag]["applied"]
        if a["rejudgements_applied"] or a["refused"] or a["still_untagged"]:
            print(f"  {tag:15s} applied {a['rejudgements_applied']:3d}  refused {a['refused']:2d}  "
                  f"still untagged {len(a['still_untagged'])}")
    for r in report["refused"][:8]:
        print(f"    REFUSED {r['question']} [{r['tag']}] -> {r['assign']}: {r['why'][:70]}")
    print(f"\nwrote {os.path.relpath(OUT, ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
