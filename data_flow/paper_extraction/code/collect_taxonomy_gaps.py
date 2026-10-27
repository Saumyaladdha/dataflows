"""Gather every chapter and topic the mapping agents asked for and could not find.

WHY THIS EXISTS
---------------
The chapter and topic lists handed to `q-chapter-picker` and `q-subtopic-picker` are CLOSED: the
agents may only answer with a code the list already contains. That is deliberate -- a chapter an
agent composes is a chapter the product cannot show. But the list comes from the
`ExamChapterTopicMappings` table, and a full scan of it (1,606 rows, `Count == ScannedCount`, no
pagination key, so not a truncated read) holds only 26 Chemistry, 32 Biology and 31 Physics
chapters. Whole NCERT chapters are simply absent from it.

So the agents were given somewhere to put the answer they wanted instead of quietly settling for a
near neighbour: `proposed_chapter` and `proposed_topic`. This script collects those, together with
every `unsure` and every `Unspecified Topic` fallback, into one reviewable list -- with the
questions that wanted each, so a person can see how much rides on a gap before deciding to fill it.

IT DOES NOT EDIT THE TAXONOMY. Nothing here is written back into `chapter_index.json`. That index
is the product's own vocabulary and extending it is a decision about the product, taken once,
upstream. What this produces is the evidence for that decision in one file, instead of scattered
across 1,869 output notes where nobody will read it.
"""

import argparse
import collections
import glob
import json
import os

import runner_core as rc

OUT = rc.mappings() + ("taxonomy_gaps.json",)


def _outputs(step):
    """Every agent output for a step, as (item_id, data). Unreadable files are skipped, not fatal."""
    for path in sorted(glob.glob(rc.pp("steps", step, "out", "*.runA.json"))):
        item = os.path.basename(path).replace(".runA.json", "").replace("__", "#")
        try:
            with open(path, encoding="utf-8") as fh:
                yield item, json.load(fh)
        except ValueError:
            continue


def collect():
    """({chapter wanted: evidence}, {topic wanted: evidence})."""
    chapters = collections.defaultdict(lambda: {"questions": [], "notes": []})
    topics = collections.defaultdict(lambda: {"questions": [], "notes": [], "chapters": set()})

    for item, data in _outputs("QCHAP"):
        if "error" in data:
            continue
        wanted = (data.get("proposed_chapter") or "").strip()
        unsure = data.get("chapter_codes") == ["unsure"]
        if not (wanted or unsure):
            continue
        # An unsure with no name is still a gap, only an unnamed one. Outputs written before
        # `proposed_chapter` existed named the wanted chapter in prose instead, so those are grouped
        # by their own note rather than collapsed into one meaningless bucket of 139.
        key = wanted or ("unnamed: %s" % (data.get("note") or "no note given").strip()[:110])
        chapters[key]["questions"].append(item)
        if data.get("note"):
            chapters[key]["notes"].append(data["note"])

    chosen = dict(_outputs("QCHAP"))
    for item, data in _outputs("QTOPIC"):
        if "error" in data:
            continue
        wanted = (data.get("proposed_topic") or "").strip()
        placeholder = any("unspecified" in str(name).lower()
                          for name in (data.get("topic_names") or []))
        unsure = data.get("topic_ids") == ["unsure"]
        if not (wanted or placeholder or unsure):
            continue
        key = wanted or ("(placeholder used, no topic named)" if placeholder
                         else "(unsure, no topic named)")
        topics[key]["questions"].append(item)
        if data.get("note"):
            topics[key]["notes"].append(data["note"])
        # Which chapter the topic was wanted IN: the same topic name missing from two chapters is
        # two different pieces of work, so they are not merged.
        for name in (chosen.get(item, {}).get("chapter_names") or []):
            topics[key]["chapters"].add(name)

    return chapters, topics


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write the JSON as well as printing it")
    args = ap.parse_args()

    chapters, topics = collect()
    payload = {
        "source": "steps/QCHAP/out and steps/QTOPIC/out",
        "chapters_wanted": sorted(
            ({"chapter": name, "questions": sorted(v["questions"]),
              "question_count": len(v["questions"]), "notes": v["notes"][:6]}
             for name, v in chapters.items()),
            key=lambda row: -row["question_count"]),
        "topics_wanted": sorted(
            ({"topic": name, "in_chapters": sorted(v["chapters"]),
              "questions": sorted(v["questions"]),
              "question_count": len(v["questions"]), "notes": v["notes"][:6]}
             for name, v in topics.items()),
            key=lambda row: -row["question_count"]),
    }

    print("chapters the taxonomy is missing: %d  (%d questions affected)"
          % (len(chapters), sum(len(v["questions"]) for v in chapters.values())))
    for row in payload["chapters_wanted"][:25]:
        print("  %4d  %s" % (row["question_count"], row["chapter"]))
    print("topics the taxonomy is missing: %d  (%d questions affected)"
          % (len(topics), sum(len(v["questions"]) for v in topics.values())))
    for row in payload["topics_wanted"][:25]:
        print("  %4d  %-44s in %s" % (row["question_count"], row["topic"],
                                      ", ".join(row["in_chapters"]) or "-"))

    if args.apply:
        path = rc.pp(*OUT)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=1)
        print("wrote %s" % os.path.relpath(path, rc.pp()))
    else:
        print("(nothing written -- pass --apply)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
