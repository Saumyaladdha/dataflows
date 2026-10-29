#!/usr/bin/env python3
"""After extend_taxonomy.py, re-queue the QTOPIC answers whose missing topic now exists.

    python3 code/requeue_taxonomy_gaps.py --paper-id 2017_A --dry-run
    python3 code/requeue_taxonomy_gaps.py --paper-id 2017_A --apply

The gap loop is: QTOPIC answers `unsure` and names the topic in `proposed_topic` (or picks the
`Unspecified Topic` placeholder and names it); collect_taxonomy_gaps.py and extend_taxonomy.py mint
the topic as a local addition; and the question has to be asked AGAIN, now that its chapter's list
holds the topic it wanted. This script does that last part: it moves exactly those QTOPIC outputs
whose proposed topic is now in the chapter's list to steps/QTOPIC/superseded/, so
`run_step.py QTOPIC --list` offers them again.
Done by hand on 2017 Code-A (9 questions); a script, so the next booklet does not depend on memory.
An answer whose wanted topic is still absent is left alone -- removing it would only re-ask a
question the taxonomy still cannot answer.
"""

import argparse
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
import extend_taxonomy  # noqa: E402
import qmap_plugins  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper-id", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    index = qmap_plugins.chapter_index()
    topics_by_chapter = {}
    for chapters in index.values():
        for chapter in chapters:
            names = {extend_taxonomy.canonical(t["topic"]) for t in chapter.get("topics") or []}
            topics_by_chapter.setdefault(chapter.get("chapter_code") or chapter["chapter"], set()).update(names)
    requeued = []
    for path in sorted(glob.glob(rc.pp("steps", "QTOPIC", "out", "%s__q*.runA.json" % args.paper_id))):
        with open(path, encoding="utf-8") as fh:
            out = json.load(fh)
        wanted = (out.get("proposed_topic") or "").strip()
        unplaced = out.get("topic_ids") == ["unsure"] or any(
            "unspecified" in (n or "").lower() for n in out.get("topic_names") or [])
        if not (wanted and unplaced):
            continue
        item = os.path.basename(path).split(".")[0]
        chap_path = rc.pp("steps", "QCHAP", "out", "%s.runA.json" % item)
        if not os.path.exists(chap_path):
            continue
        with open(chap_path, encoding="utf-8") as fh:
            codes = json.load(fh).get("chapter_codes") or []
        if any(extend_taxonomy.canonical(wanted) in topics_by_chapter.get(code, set()) for code in codes):
            requeued.append((item, wanted))
            if args.apply:
                # KEPT, not deleted: an agent's answer is evidence (the topic it asked for), and
                # steps/<STEP>/superseded/ is where every replaced answer goes
                keep = rc.pp("steps", "QTOPIC", "superseded")
                os.makedirs(keep, exist_ok=True)
                os.replace(path, os.path.join(keep, os.path.basename(path).replace(
                    ".runA.json", ".runA.before_taxonomy.json")))
    for item, wanted in requeued:
        print("  re-queue %-16s now offered: %s" % (item, wanted))
    print("%d QTOPIC answer(s) %s" % (len(requeued), "re-queued" if args.apply else "would be re-queued"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
