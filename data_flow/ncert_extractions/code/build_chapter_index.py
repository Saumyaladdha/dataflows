#!/usr/bin/env python3
"""Turn the DynamoDB ExamChapterTopicMappings scan into a clean chapter/subtopic index.

    python3 scripts/build_chapter_index.py --apply

WHAT THE TABLE IS
-----------------
`ExamChapterTopicMappings` in ap-south-1 is the product's own chapter and topic taxonomy: 1,606 rows
keyed by `topic_id` + `exam`, each carrying a `subject`, a `chapter`, a `topic`, display names, a
chapter code and per-level question counts. It is the list a question must be mapped INTO, so it is
the authority on what a chapter is allowed to be called -- a chapter this pipeline invents is a
chapter the product cannot show.

WHAT IT DOES NOT HAVE, AND WHY THAT MATTERS HERE
------------------------------------------------
Its `subject` is physics / chemistry / biology. There is **no botany/zoology split**, while NEET
itself prints Botany and Zoology as separate sections and this pipeline records them as a `branch`
(config/allowed_values.yaml). So a Biology question can be mapped to a chapter from this table, and
the botany/zoology distinction has to come from the paper's own printed section heading, not from
here. Recorded rather than papered over: the two taxonomies genuinely differ at that level.

DATA PROBLEMS IN THE TABLE, REPORTED NOT SILENTLY CLEANED
---------------------------------------------------------
Found by this script and printed every run, because an index that quietly fixes its source hides a
problem the source still has:

  * 364 of 1,606 rows carry NO `subject` at all, and 1 row spells it `Physics` with a capital P
    against 503 lower-case `physics`. Those 365 rows cannot be routed by subject.
  * Some `topic` strings carry mojibake from a bad encode round-trip -- `wave\\udce2\\udc80\\udc93particle`
    is "wave–particle" with the en dash broken. The display name is affected too.
  * A chapter can carry an `unspecified topic` row whose `topicNumber` is a sentinel like 1999320.
"""

import argparse
import collections
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

RAW = ("papers_v2", "mappings", "ExamChapterTopicMappings.raw.json")
OUT = ("papers_v2", "mappings", "chapter_index.json")


def flatten(item):
    """DynamoDB's typed JSON -> plain values."""
    out = {}
    for key, wrapper in item.items():
        value = list(wrapper.values())[0]
        out[key] = value
    return out


def repair(text):
    """Undo the surrogate-escape mojibake in `topic`/`topic_display_name`.

    `wave\\udce2\\udc80\\udc93particle` is UTF-8 bytes for an en dash that were decoded as latin-1 and
    re-encoded. Recovering it is a round trip back through those bytes; where that fails the string
    is left exactly as stored, because a guess at a title is worse than a visible defect.
    """
    if not isinstance(text, str):
        return text
    try:
        return text.encode("utf-8", "surrogateescape").decode("utf-8")
    except (UnicodeDecodeError, UnicodeEncodeError):
        return text


def normalise(name):
    """A chapter name reduced to what identifies it, for matching shadow rows to real ones.

    Case, punctuation and the dash family all vary between the two spellings of the same chapter --
    `P Block` against `The p-Block Elements`, `Magnetic Effect of Current` against `Magnetic Effect
    of Electric Current` -- so matching is done on letters alone, with a leading article dropped.
    """
    text = unicodedata.normalize("NFKD", name or "").lower()
    text = re.sub(r"^(the|a|an)\s+", "", text)
    return re.sub(r"[^a-z0-9]", "", text)


def deduplicate(chapters):
    """Merge the taxonomy's duplicate chapters, and report what was merged.

    TWO DISTINCT DEFECTS, both measured in the live table:

      * 30 chapters carry NO `chapter_code` and exactly one topic, which is an
        `Unspecified Topic` placeholder. They are shadow rows of real chapters, written in raw
        lower case -- `plant kingdom` beside `Plant Kingdom`. Left in, an agent is offered the same
        chapter twice and its answer is unstable between two spellings of one thing.
      * 2 `chapter_code` values are used by two differently-titled chapters -- `CHENEETENGPBB` for
        both `P Block` and `The p-Block Elements`. The code is what downstream stores, so these are
        one chapter wearing two names.

    A shadow row is merged into its coded twin when their normalised names agree. One that matches
    nothing is KEPT and reported, because a chapter with no code that is also not a duplicate is a
    real gap in the taxonomy, not noise to drop.
    """
    coded, uncoded = {}, []
    for chapter in chapters:
        code = chapter.get("chapter_code")
        if code:
            key = (chapter["subject"], code)
            if key in coded:
                kept = coded[key]
                # the longer title is the fuller one: "The p-Block Elements" over "P Block"
                if len(chapter["chapter"]) > len(kept["chapter"]):
                    kept["chapter"], chapter["chapter"] = chapter["chapter"], kept["chapter"]
                kept.setdefault("merged_titles", []).append(chapter["chapter"])
                kept["topics"] += chapter["topics"]
            else:
                coded[key] = chapter
        else:
            uncoded.append(chapter)

    by_name = {}
    for chapter in coded.values():
        by_name.setdefault((chapter["subject"], normalise(chapter["chapter"])), chapter)

    merged_shadows, orphans = 0, []
    for chapter in uncoded:
        twin = by_name.get((chapter["subject"], normalise(chapter["chapter"])))
        if twin is None:
            orphans.append(chapter)
            continue
        twin.setdefault("merged_titles", []).append(chapter["chapter"])
        # a shadow's only topic is the placeholder; keep it only if the twin has none
        real = [t for t in chapter["topics"]
                if (t["topic"] or "").lower() != "unspecified topic"]
        twin["topics"] += real
        merged_shadows += 1

    # a topic can arrive twice once chapters are merged
    for chapter in coded.values():
        seen, unique = set(), []
        for topic in chapter["topics"]:
            if topic["topic_id"] in seen:
                continue
            seen.add(topic["topic_id"])
            unique.append(topic)
        chapter["topics"] = unique

    return list(coded.values()) + orphans, merged_shadows, len(orphans)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    with open(rc.pp(*RAW), encoding="utf-8") as fh:
        raw = json.load(fh)
    rows = [flatten(i) for i in raw["Items"]]

    problems = collections.Counter()
    chapters = {}
    for row in rows:
        subject = (row.get("subject") or "").strip()
        if not subject:
            problems["rows_with_no_subject"] += 1
            continue
        if subject != subject.lower():
            problems["subject_not_lower_case"] += 1
        subject = subject.lower()
        chapter = (row.get("chapter_display_name") or row.get("chapter") or "").strip()
        if not chapter:
            problems["rows_with_no_chapter"] += 1
            continue
        topic = repair(row.get("topic_display_name") or row.get("topic") or "").strip()
        if topic != (row.get("topic_display_name") or row.get("topic") or "").strip():
            problems["topic_name_repaired"] += 1
        if any(0xDC00 <= ord(ch) <= 0xDFFF for ch in topic):
            problems["topic_name_still_broken"] += 1
        key = (subject, chapter)
        entry = chapters.setdefault(key, {
            "subject": subject,
            "chapter": chapter,
            "chapter_code": row.get("chapter_code"),
            "chapter_trend_text": row.get("chapter_trend_text"),
            "topics": [],
        })
        if (topic or "").lower() == "unspecified topic":
            problems["unspecified_topic_rows"] += 1
        entry["topics"].append({
            "topic": topic,
            "topic_id": row.get("topic_id"),
            "topic_number": row.get("topicNumber"),
            "questions": row.get("numberOfQuestions"),
            "priority": row.get("topic_priority") or row.get("priority"),
            "trend": row.get("topic_trend_text"),
        })

    merged, shadows, orphans = deduplicate(list(chapters.values()))
    index = {
        "source": "dynamodb ap-south-1 ExamChapterTopicMappings",
        "rows_scanned": len(rows),
        "chapters": sorted(merged, key=lambda c: (c["subject"], c["chapter"])),
    }
    problems["shadow_chapters_merged"] = shadows
    problems["uncoded_chapters_kept"] = orphans
    for chapter in index["chapters"]:
        chapter["topics"].sort(key=lambda t: (t["topic"] or ""))

    bysub = collections.Counter(c["subject"] for c in index["chapters"])
    topics = sum(len(c["topics"]) for c in index["chapters"])
    print("%d rows -> %d chapters, %d topics" % (len(rows), len(index["chapters"]), topics))
    for subject, count in sorted(bysub.items()):
        n = sum(len(c["topics"]) for c in index["chapters"] if c["subject"] == subject)
        print("   %-10s %2d chapters, %4d topics" % (subject, count, n))
    print("\nproblems in the source table, reported not cleaned:")
    for name, count in problems.most_common():
        print("   %-26s %d" % (name, count))
    print("\n   NOTE: the table's `subject` is physics/chemistry/biology with NO botany/zoology\n"
          "   split, while NEET prints Botany and Zoology as separate sections. The branch must\n"
          "   come from the paper's own section heading, not from this table.")

    if args.dry_run:
        print("\n(dry run -- nothing written)")
        return 0
    path = rc.pp(*OUT)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1)
    print("\nwrote %s" % os.path.relpath(path, rc.pp()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
