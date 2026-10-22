"""Add the chapters and topics the mapping agents asked for into a LOCAL extension of the taxonomy.

WHY THIS IS SEPARATE FROM THE SOURCE
------------------------------------
`papers_v2/mappings/chapter_index.json` is built from a scan of the product's own
`ExamChapterTopicMappings` table. It is a copy of something owned elsewhere, and rewriting a copy of
someone else's table is how two systems quietly stop agreeing. So nothing here touches it.

Instead this writes `papers_v2/mappings/taxonomy_additions.json`, which `chapter_index()` merges on
top of the scan. Every added row carries `added_locally: true` and the questions that asked for it,
so at any point you can answer three questions that matter: what did we add, who wanted it, and what
would break if the upstream table added its own version tomorrow.

WHERE THE ADDITIONS COME FROM
-----------------------------
Only from `proposed_chapter` / `proposed_topic` on agent outputs, or from a chapter title the agent
quoted in its note. Nothing is invented here. The agents were working against a CLOSED list and were
required to say what they wanted rather than force a question into a near neighbour -- these are
those answers, collected.

The scan holds 26 Chemistry, 32 Biology and 31 Physics chapters against roughly 97 in the NEET
syllabus, so the gaps are real chapters, not exotica: Transport in Plants, Digestion and Absorption,
Environmental Issues, The s-Block Elements, The Solid State, Hydrogen, Surface Chemistry.

CODES
-----
A code is minted in the source's own shape -- `CHENEETENGPOL` -- so an added chapter is addressable
exactly like a scanned one, and the `added_locally` flag rather than a weird-looking code is what
marks it. Codes are derived from the title, so the same title always mints the same code and
re-running is idempotent.
"""

import argparse
import collections
import glob
import json
import os
import re

import runner_core as rc

INDEX = ("papers_v2", "mappings", "chapter_index.json")
OUT = ("papers_v2", "mappings", "taxonomy_additions.json")

SUBJECT_PREFIX = {"physics": "PHY", "chemistry": "CHE", "biology": "BIO"}
#: Words that carry no identity in a chapter title, so the code is built from the words that do.
STOPWORDS = {"the", "of", "and", "in", "its", "a", "an", "to", "for", "with", "on"}


def slug(text):
    return re.sub(r"[^a-z0-9]+", "_", (text or "").lower()).strip("_")


def mint_code(subject, chapter, taken):
    """`CHENEETENGSOL` -- the source's own shape, derived from the title so it is reproducible."""
    words = [w for w in re.findall(r"[A-Za-z]+", chapter) if w.lower() not in STOPWORDS]
    stem = "".join(w[0] for w in words).upper()[:4] or "XXX"
    if len(stem) < 3:
        stem = (words[0][:3] if words else "XXX").upper()
    base = "%sNEETENG%s" % (SUBJECT_PREFIX.get(subject, "GEN"), stem)
    code, n = base, 1
    while code in taken:
        n += 1
        code = "%s%d" % (base, n)
    return code


def _outputs(step):
    for path in sorted(glob.glob(rc.pp("steps", step, "out", "*.runA.json"))):
        item = os.path.basename(path).replace(".runA.json", "").replace("__", "#")
        try:
            with open(path, encoding="utf-8") as fh:
                yield item, json.load(fh)
        except ValueError:
            continue


NAMED_IN_NOTE = re.compile(r"['‘“]([A-Z][^'’”]{3,60})['’”]")


def named_in_note(note):
    """The chapter an agent quoted in prose. Outputs written before `proposed_chapter` existed named
    the wanted chapter this way, and there are hundreds of them -- worth reading, not re-running."""
    match = NAMED_IN_NOTE.search(note or "")
    return match.group(1) if match else ""


def normalise_title(title):
    """Trim the parenthetical gloss agents add, so 'The s-Block Elements (alkali metals)' and
    'The s-Block Elements' are ONE chapter rather than two near-identical additions."""
    title = re.sub(r"\s*\([^)]*\)\s*$", "", (title or "").strip())
    return re.sub(r"\s+", " ", title).strip(" .,:;")


def canonical(title):
    """The key two titles are compared on. Deliberately aggressive, because the cost of being wrong
    is asymmetric: a missed match ADDS A DUPLICATE CHAPTER to the taxonomy, which is the exact defect
    this file exists to stop, while an over-eager match merely merges two spellings of one chapter.

    It folds the four ways the same chapter was written across the scan and the agents' proposals:
      * an en-dash or em-dash where the other has a hyphen -- 'The p-Block Elements' is spelt
        'the p\u2013block elements' in the scan, which is why it was not recognised as existing;
      * a leading 'The';
      * the source's own ' - Practice' / ' Practice' suffix on topic and chapter rows;
      * case, punctuation and spacing.
    """
    text = normalise_title(title).lower()
    text = text.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")
    text = re.sub(r"\s*-\s*practice$", "", text)
    text = re.sub(r"\s+practice$", "", text)
    text = re.sub(r"^the\s+", "", text)
    return re.sub(r"[^a-z0-9]+", "", text)


def collect(subject_of):
    """({(subject, chapter): [items]}, {(subject, chapter, topic): [items]})."""
    chapters = collections.defaultdict(list)
    topics = collections.defaultdict(list)
    chosen = dict(_outputs("QCHAP"))

    for item, data in _outputs("QCHAP"):
        if "error" in data or data.get("chapter_codes") != ["unsure"]:
            continue
        title = normalise_title(data.get("proposed_chapter") or named_in_note(data.get("note")))
        subject = subject_of(item)
        if title and subject:
            chapters[(subject, title)].append(item)

    for item, data in _outputs("QTOPIC"):
        if "error" in data:
            continue
        title = normalise_title(data.get("proposed_topic") or "")
        if not title:
            continue
        # A topic belongs to the chapter the SAME question was filed under; a topic name alone is
        # not an identifier, because "Secondary Growth" is wanted inside one specific chapter.
        parent = (chosen.get(item, {}).get("chapter_names") or [None])[0]
        subject = subject_of(item)
        if parent and subject:
            topics[(subject, normalise_title(parent), title)].append(item)
    return chapters, topics


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write the additions file")
    ap.add_argument("--min-questions", type=int, default=1,
                    help="only add a chapter or topic at least this many questions asked for")
    args = ap.parse_args()

    with open(rc.pp(*INDEX), encoding="utf-8") as fh:
        index = json.load(fh)
    taken = {c["chapter_code"] for c in index["chapters"] if c.get("chapter_code")}
    existing = {(c["subject"], canonical(c["chapter"])) for c in index["chapters"]}
    existing_topics = {(c["subject"], canonical(c["chapter"]), canonical(t["topic"]))
                       for c in index["chapters"] for t in c["topics"]}

    # The subject a question was mapped under: read from the export's own CSV so this script and the
    # page can never disagree about which subject a question is.
    subject_by_item = {}
    import csv
    for path in glob.glob(rc.pp("papers_v2", "exports", "csv", "*.csv")):
        if "questions_v2" in os.path.basename(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                item = "%s#q%03d" % (row["paper_id"], int(row["qno"]))
                subject_by_item[item] = (row["subject"] or "").lower()

    chapters, topics = collect(lambda item: subject_by_item.get(item, ""))

    def merge(counter, key_at):
        """Fold proposals whose canonical form agrees, keeping the longest spelling as the label.
        Two agents asking for 'Solid State' and 'The Solid State' want ONE chapter."""
        folded = {}
        for key, items in counter.items():
            canon = tuple(canonical(part) if index_of == key_at else part
                          for index_of, part in enumerate(key))
            if canon in folded:
                label, existing_items = folded[canon]
                keep = label if len(label) >= len(key[key_at]) else key[key_at]
                folded[canon] = (keep, existing_items + items)
            else:
                folded[canon] = (key[key_at], list(items))
        out = collections.defaultdict(list)
        for canon, (label, items) in folded.items():
            key = tuple(label if i == key_at else part for i, part in enumerate(canon))
            out[key] = items
        return out

    chapters = merge(chapters, 1)
    topics = merge(topics, 2)

    added_chapters, added_topics, skipped = [], [], []
    for (subject, title), items in sorted(chapters.items(), key=lambda kv: -len(kv[1])):
        if len(items) < args.min_questions:
            continue
        if (subject, canonical(title)) in existing:
            skipped.append("chapter already in the scan: %s / %s" % (subject, title))
            continue
        code = mint_code(subject, title, taken)
        taken.add(code)
        added_chapters.append({"subject": subject, "chapter": title, "chapter_code": code,
                               "added_locally": True, "asked_for_by": sorted(items),
                               "question_count": len(items), "topics": []})
    for (subject, parent, title), items in sorted(topics.items(), key=lambda kv: -len(kv[1])):
        if len(items) < args.min_questions:
            continue
        if (subject, canonical(parent), canonical(title)) in existing_topics:
            skipped.append("topic already in the scan: %s / %s" % (parent, title))
            continue
        added_topics.append({"subject": subject, "chapter": parent, "topic": title,
                             "topic_id": "neet_%s_%s_%s" % (subject, slug(parent), slug(title)),
                             "added_locally": True, "asked_for_by": sorted(items),
                             "question_count": len(items)})

    # Every ADDED chapter needs at least one topic, or the chapter is unusable by QTOPIC the moment
    # a question is filed into it. "Unspecified Topic" is the source's own placeholder spelling.
    for chapter in added_chapters:
        own = [t for t in added_topics if t["chapter"].lower() == chapter["chapter"].lower()]
        chapter["topics"] = [{"topic_id": t["topic_id"], "topic": t["topic"],
                              "added_locally": True} for t in own] or [
            {"topic_id": "neet_%s_%s_unspecified_topic" % (chapter["subject"],
                                                           slug(chapter["chapter"])),
             "topic": "Unspecified Topic", "added_locally": True}]

    payload = {
        "source": "agent proposals in steps/QCHAP/out and steps/QTOPIC/out",
        "merged_on_top_of": "papers_v2/mappings/chapter_index.json",
        "warning": ("These rows are LOCAL. They are not in ExamChapterTopicMappings. If the upstream "
                    "table later adds its own version of one, the codes will differ and the local "
                    "row must be retired rather than kept alongside."),
        "chapters": added_chapters,
        "topics_in_existing_chapters": [t for t in added_topics
                                        if not any(c["chapter"].lower() == t["chapter"].lower()
                                                   for c in added_chapters)],
    }

    print("chapters to add: %d" % len(added_chapters))
    for c in added_chapters:
        print("  %-9s %-14s %-48s wanted by %d" % (c["subject"], c["chapter_code"],
                                                  c["chapter"], c["question_count"]))
    print("topics to add inside existing chapters: %d"
          % len(payload["topics_in_existing_chapters"]))
    for t in payload["topics_in_existing_chapters"]:
        print("  %-30s <- %-44s wanted by %d" % (t["chapter"][:30], t["topic"][:44],
                                                 t["question_count"]))
    for line in skipped:
        print("  skipped: %s" % line)

    if args.apply:
        path = rc.pp(*OUT)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=1)
        print("wrote %s" % os.path.relpath(path, rc.pp()))
    else:
        print("(nothing written -- pass --apply)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
