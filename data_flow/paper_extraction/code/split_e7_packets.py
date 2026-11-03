#!/usr/bin/env python3
"""Split packet difficulty outputs into the per-question files the export reads.

    python3 code/split_e7_packets.py --paper 2017_A --apply

The re-rate ran in packets of ten so one agent could hold a subject together and band it
consistently. `export_paper_v2.difficulty_of` reads ONE FILE PER QUESTION, named
`<paper>__q<nnn>.runA.json`. This writes those, so the packet shape is a detail of how the
rating was produced and not something every reader has to know about.

Existing per-question files are OVERWRITTEN, which is the point: the previous pass banded 180
of 180 questions at exactly their step count, and this run exists to replace it.
"""

import argparse
import glob
import json
import os

import runner_core as rc

OUT = ("steps", "E7V", "out")


def split(paper_id, apply_=False):
    wrote, seen = 0, {}
    for p in sorted(glob.glob(rc.pp(*OUT, "ex7__%s__*.runA.json" % paper_id))):
        try:
            doc = json.load(open(p, encoding="utf-8"))
        except ValueError:
            print("  UNREADABLE %s" % os.path.basename(p))
            continue
        for r in doc.get("ratings") or []:
            qid = r.get("question_id") or ""
            if not qid.startswith(paper_id):
                continue
            qno = int(qid[-3:])
            if qno in seen:
                print("  duplicate rating for q%03d (%s and %s)"
                      % (qno, seen[qno], os.path.basename(p)))
            seen[qno] = os.path.basename(p)
            out = dict(r)
            out.pop("question_id", None)
            if apply_:
                with open(rc.pp(*OUT, "%s__q%03d.runA.json" % (paper_id, qno)), "w",
                          encoding="utf-8") as fh:
                    json.dump(out, fh, ensure_ascii=False, indent=1)
            wrote += 1
    print("%d per-question difficulty file(s)%s" % (wrote, "" if apply_ else " (dry run)"))
    # A packet that has been split and then archived (see steps/E7V/crosscheck) leaves its
    # per-question files in place. Reporting those as unrated would send someone off to
    # re-rate 30 questions that are already on the page.
    on_disk = {int(f[-13:-10]) for f in glob.glob(rc.pp(*OUT, "%s__q*.runA.json" % paper_id))}
    missing = [q for q in range(1, 181) if q not in seen and q not in on_disk]
    already = sorted(q for q in on_disk if q not in seen)
    if already:
        print("  %d question(s) already have a per-question file from an earlier split"
              % len(already))
    if missing:
        print("  NOT RATED: %s" % ", ".join("q%03d" % q for q in missing))
    return wrote


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    split(a.paper, a.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
