#!/usr/bin/env python3
"""Apply the B9S agents' verdicts to the records.

    python3 scripts/apply_b9s_verdicts.py --dry-run
    python3 scripts/apply_b9s_verdicts.py --apply

Reads `steps/B9S/out/<question>__<origin>.runA.json` against the work item it answers, and writes
the outcome onto the record. The agent decided; this file only records what it decided, and refuses
anything that does not validate.

What publishes and what does not
--------------------------------
Only `belongs_complete` puts a figure in front of a reader. Everything else is recorded and
flagged, because the alternative is worse than a visible gap:

  belongs_complete      -> published. For a crop that means `figure_path_source`; for a figure the
                           bank already shows, it means the existing `figure_path` is CONFIRMED,
                           which is the first verdict any of them has ever carried.
  panel_order_differs   -> `option_panel_map` is stored and the figure is NOT published as it
                           stands. The panels are right and the order is wrong, so the mapping has
                           to be applied -- publishing without it is exactly the defect two audits
                           found, where the keyed answer selects the wrong picture.
  belongs_clipped       -> not published. A diagram missing an axis answers the question wrongly in
  belongs_with_junk        a way no reader can detect; a gap is at least reviewable.
  wrong_figure          -> not published, and for a figure the bank already shows this is a
  not_a_figure             RETRACTION: `figure_path` is cleared and the reason recorded.
  unsure                -> nothing changes.

A `wrong_figure` on an already-published image is the most consequential outcome here, so it is
the one place this script removes something. The image file is left on disk; only the record stops
pointing at it, so the decision is reversible and the evidence survives.
"""

import argparse
import collections
import datetime
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
import B9S as b9s_check  # noqa: E402

PUBLISHES = "belongs_complete"
RETRACTS = ("wrong_figure", "not_a_figure")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    recs = {}
    for path in sorted(glob.glob(rc.pp("papers", "records", "Q-*.json"))):
        with open(path, encoding="utf-8") as fh:
            r = json.load(fh)
        recs[r.get("question_id")] = (path, r)

    stamp = datetime.date.today().isoformat()
    tally = collections.Counter()
    touched = {}
    rejected = []

    for out_path in sorted(glob.glob(rc.pp("steps", "B9S", "out", "*.runA.json"))):
        name = os.path.basename(out_path)[:-len(".runA.json")]
        qid, _, origin = name.partition("__")
        work = rc.pp("steps", "B9S", "work", f"{name}.runA.input.json")
        if not os.path.exists(work) or qid not in recs:
            rejected.append((name, "no matching work item or record"))
            continue
        with open(out_path, encoding="utf-8") as fh:
            try:
                verdict = json.load(fh)
            except json.JSONDecodeError as exc:
                rejected.append((name, f"output is not valid JSON ({exc})"))
                continue
        with open(work, encoding="utf-8") as fh:
            item = json.load(fh)

        ok, why = b9s_check.check(verdict, {"input_data": item})
        if not ok:
            rejected.append((name, why))
            continue
        if "error" in verdict:
            tally["agent_reported_broken_input"] += 1
            continue

        v = verdict["verdict"]
        tally[f"{v} ({origin})"] += 1
        path, rec = recs[qid]
        notes = []

        if v == PUBLISHES:
            if origin == "paper":
                rec["figure_path_source"] = item["figure_file"]
                notes.append(f"figure cut from {item['source_pdf']} page {item['source_page']} and "
                             f"CONFIRMED by the B9S agent as this question's figure, whole and "
                             f"clean: {verdict['shows']}")
            else:
                rec["figure_verified"] = True
                notes.append(f"the figure this bank already publishes was CONFIRMED by the B9S "
                             f"agent as this question's figure, whole and clean: "
                             f"{verdict['shows']}. It came from a wording match against another "
                             f"question bank and had never been checked")
            tally["published"] += 1

        elif v == "panel_order_differs":
            rec["option_panel_map"] = verdict["panel_map"]
            rec["figure_verified"] = False
            notes.append(f"the four panels belong to this question but are printed in a different "
                         f"order from this record's options: {verdict['panel_map']}. The figure is "
                         f"NOT published as it stands -- the mapping must be applied first, "
                         f"otherwise the keyed answer selects the wrong picture. Agent saw: "
                         f"{verdict['shows']}")
            tally["panel_map_recorded"] += 1

        elif v in RETRACTS and origin == "legacy" and rec.get("figure_path"):
            notes.append(f"the figure this bank was publishing is WITHDRAWN: the B9S agent found "
                         f"it is {v.replace('_', ' ')}. It showed {verdict['shows']}. "
                         f"{verdict.get('note') or ''} The file is left on disk; only this record "
                         f"stops pointing at it, so the decision is reversible")
            rec["figure_path_withdrawn"] = rec.pop("figure_path")
            rec["figure_verified"] = False
            tally["withdrawn"] += 1

        elif v == "unsure":
            # Recorded, not skipped. "Judged and could not be decided" and "never judged" are
            # different states, and leaving unsure silent made them indistinguishable in the
            # record -- which is the exact confusion this step was added to remove, since an
            # unverified figure that happens to be right looks the same as one that is wrong.
            rec["figure_verified"] = False
            notes.append(f"the B9S agent could not decide whether this candidate is the right "
                         f"figure, and said so rather than guessing: {verdict['shows']}. "
                         f"{verdict.get('note') or ''} It is not published, and the question stays "
                         f"a visible gap for a person to settle")
            tally["undecided"] += 1

        elif v in ("belongs_clipped", "belongs_with_junk"):
            rec["figure_verified"] = False
            notes.append(f"the B9S agent found this candidate is {v.replace('_', ' ')} "
                         f"({verdict.get('missing') or verdict.get('junk')}), so it is not "
                         f"published: a figure missing part of itself, or carrying another "
                         f"question's text, answers the question wrongly in a way a reader cannot "
                         f"detect, while a gap is at least reviewable. Agent saw: "
                         f"{verdict['shows']}")
            tally["held_back"] += 1

        if notes:
            rec.setdefault("repairs", []).append(
                {"date": stamp, "by": "step B9S (b9s-source-figure-confirmer)",
                 "kind": f"figure_verdict_{v}", "notes": notes})
            touched[qid] = (path, rec)

    for k, v in tally.most_common():
        print(f"   {v:4d}  {k}")
    if rejected:
        print(f"\n{len(rejected)} verdicts REJECTED and not applied:")
        for name, why in rejected[:10]:
            print(f"   {name}: {why[:120]}")
    print(f"\n{len(touched)} records would change")

    if args.dry_run:
        print("\n(dry run -- nothing written)")
        return 0
    for qid, (path, rec) in touched.items():
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(rec, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    print(f"wrote {len(touched)} records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
