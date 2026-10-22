"""Build D4 evidence inputs for papers_v2 questions, scoped to their NCERT chapter.

WHY THIS EXISTS INSTEAD OF REUSING fetch_passages.py
----------------------------------------------------
`fetch_passages.py` (step D3) scopes a question's candidate passages by the NCERT SUBTOPIC that
step D2 chose for it, reading `d2_subtopic_ids` off the v1 record. The papers_v2 questions have no
such field: QCHAP and QTOPIC mapped them against the product's own `ExamChapterTopicMappings`
taxonomy, whose ids (`neet_physics_current_electricity_potentiometer`) are a different vocabulary
from NCERT's (`PHY12-CH03-ST04`). Running D2 over 358 questions purely to translate between the two
would spend 358 agent calls to re-answer a question that is already answered.

So this scopes by CHAPTER instead, resolved through `ncert_book_mapping/coverage.json`, and leaves
the finer choice to D4 -- which is the step whose whole job is finding the exact line. The passages
of one chapter are ranked against the question by word-trigram overlap and capped at 15, reusing
`pair_passages.jaccard` exactly as fetch_passages.py does; no new similarity logic is invented here.

WHAT IS LOST, AND WHY IT IS ACCEPTABLE
--------------------------------------
Subtopic scoping would hand D4 a tighter shortlist. Chapter scoping hands it a broader one, so a
wrong line is likelier to be *available*. What protects against taking it is unchanged: a script
re-finds every quoted line in the book word for word, and `supports_answer` is graded fully /
partly / not_at_all with the gaps named. Breadth costs the agent reading time, not correctness.

WHAT IT DELIBERATELY WILL NOT DO
--------------------------------
**It writes no input for a Physics or Physical Chemistry question at all.** Those two branches are
routed to step QCA (concept and approach) instead, and the routing is in code here rather than left
to whoever dispatches the step, because the first wave proved the decision cannot be made per-run:
twelve evidence agents on these subjects returned "partly supported" over and over, and the reason
was never that NCERT lacked the physics. It was that a numerical's answer is a VALUE, and NCERT
prints sentences. What the solution needed was a display equation (carried as an image, so absent
from the passage text), a constant in a table row, or a relation taught in another chapter. A
half-matched NCERT paragraph on such a question is worse than none, because it reads as evidence.

Organic and Inorganic Chemistry stay in scope: their content IS stated in sentences and printed
reactions, so quoting works there exactly as it does for Biology.

It also writes no input for a chapter whose pages are not extracted. A question whose chapter has no
passages cannot have evidence quoted for it, and an empty `passages` list would invite the agent to
answer from memory -- which is the one failure this whole stage exists to prevent.
"""

import argparse
import collections
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pair_passages                                        # noqa: E402
import runner_core as rc                                     # noqa: E402

COVERAGE = ("ncert_book_mapping", "coverage.json")
#: Subject/branch pairs whose record is a CONCEPT, not a quotation -- handled by step QCA. Keyed on
#: the export's own `subject` and `stream` columns; physics has no finer split, so any stream counts.
CONCEPT_BRANCHES = {("chemistry", "physical")}
PASSAGES = ("ncert", "passages")
WORK = ("steps", "D4V", "work")
OUT = ("steps", "D4V", "out")
B3V_OUT = ("steps", "B3V", "out")
#: Rule from spec 12/D3: more than 15 passages and the agent cannot hold them in view at once.
PASSAGE_CAP = 15


def coverage_index():
    """{(subject, chapter name): row} from the coverage map."""
    with open(rc.pp(*COVERAGE), encoding="utf-8") as fh:
        data = json.load(fh)
    out = {}
    for row in data.get("chapters", []):
        out[(row["subject"].lower(), row["chapter"].strip().lower())] = row
    return out


def passages_for(book_id, chapter_numbers, include_empty=False):
    """Every passage of the named chapters of one book, as [{passage_id, heading, pages, text}].

    `include_empty` keeps the passages whose text is blank. Those are not noise: a blank passage is
    where NCERT prints a TABLE OR FIGURE, and the chapter's prose flows around it. They are useless
    as quotations and they matter as landmarks -- see `chapter_index`.
    """
    path = rc.pp(*PASSAGES, "%s.jsonl" % book_id)
    if not os.path.exists(path):
        return []
    wanted = {int(n) for n in chapter_numbers}
    found = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            try:
                row = json.loads(line)
            except ValueError:
                continue
            if row.get("chapter_num") not in wanted:
                continue
            if (row.get("text") or "").strip() or include_empty:
                found.append({
                    "passage_id": row["passage_id"],
                    "section_heading": row.get("section_heading") or "",
                    "page_start": row.get("page_start"),
                    "page_end": row.get("page_end"),
                    "text": row["text"],
                })
    return found


#: Headings that are not teaching text. An NCERT chapter ends with exercises, a summary and
#: "Points to Ponder", and the exercises are full of the same numbers and units as the questions --
#: so on raw trigram overlap they outrank the section that actually states the physics. Measured:
#: for 2015_A q141 (potentiometer) the top three were two EXERCISES passages and the chapter title.
NOT_TEACHING = re.compile(r"^\s*(exercises?|summary|points to ponder|additional exercises?|"
                          r"chapter \w+|appendix)", re.I)


def rank(passages, query, subtopics=(), cap=PASSAGE_CAP):
    """The `cap` passages most likely to hold the line this question turns on.

    Three signals, in order of trust:

    1. THE SUBTOPIC'S OWN WORDS against the section heading. QTOPIC already decided what this
       question tests -- "Potentiometer", "Meter Bridge", "Drift Velocity" -- and NCERT prints its
       section headings in the same language. A heading that contains the subtopic's words is the
       strongest evidence available that the line is in that section, and it costs nothing, because
       the subtopic is already on the record.
    2. Trigram overlap with the question, the same measure `pair_passages` uses to match an older
       passage to its latest counterpart.
    3. A penalty for exercises, summaries and chapter fronts. They are not where a fact is stated,
       and their numbers and units make them score highly on overlap alone.
    """
    grams = pair_passages.word_trigrams(query)
    words = {w for t in subtopics for w in re.findall(r"[a-z]{4,}", t.lower())}
    scored = []
    for passage in passages:
        heading = passage.get("section_heading") or ""
        score = pair_passages.jaccard(grams, pair_passages.word_trigrams(passage["text"]))
        if words:
            hit = sum(1 for w in words if w in heading.lower())
            score += 0.5 * hit                      # dominates overlap, as intended
        if NOT_TEACHING.match(heading):
            score -= 0.25
        scored.append((score, passage))
    scored.sort(key=lambda pair: -pair[0])
    return [p for _score, p in scored[:cap]]


def sibling_books(book):
    """The other extracted books of the same subject, newest and older edition alike.

    WHY A CHAPTER IS SOMETIMES THE WRONG BOUNDARY
    ---------------------------------------------
    Chapter scoping is right most of the time and wrong in a way that is easy to mistake for an
    NCERT gap. Three measured cases from the first wave:

      polysome            asked in a Molecular Basis question; NCERT describes it in Class XI
                          "Cell: The Unit of Life", a different book entirely
      polyploidy          the mechanism is in Cell Cycle (Class XI); the word is defined in
                          Principles of Inheritance (Class XII)
      F = ma, p = h rho g needed by Work-Energy questions; printed in Laws of Motion and in
                          Mechanical Properties of Fluids

    In each the fact IS in NCERT and the chapter-scoped shortlist could never contain it, so the
    honest verdict was `partly` with a gap named -- which reads as an NCERT deficiency when it is a
    scoping artefact. Listing the subject's other books lets the agent go and look, and record the
    passage it actually used, from whatever chapter that turns out to be.
    """
    prefix = book[:3] if book else ""
    found = []
    for path in sorted(glob.glob(rc.pp(*PASSAGES, "%s*.jsonl" % prefix))):
        name = os.path.basename(path)[:-len(".jsonl")]
        if name != book and "." not in name:
            found.append(os.path.relpath(path, rc.pp()))
    return found


def older_edition_passages(book, chapter_numbers, cap=4):
    """A few passages of the OLDER edition of the same chapter, where that edition is extracted.

    The 2023 rationalisation cut whole sections -- Meter Bridge and Potentiometer out of Current
    Electricity among them -- so for a 2015 or 2016 paper the line a question rests on can exist
    ONLY in the older book. Without these the agent has nothing to quote and must answer
    `beyond_ncert_method`, which says "NCERT does not teach this" about something NCERT taught
    until 2023.
    """
    older = book[:-1] + "O" if book and book.endswith("L") else None
    if not older:
        return []
    found = passages_for(older, chapter_numbers)
    return found[:cap]


def chapter_index(passages):
    """Every passage of the chapter as (id, heading, page) -- the chapter's table of contents.

    WHY THIS IS IN THE INPUT ALONGSIDE A RANKED SHORTLIST
    ----------------------------------------------------
    The shortlist is 15 passages chosen by word overlap, and nine evidence agents independently
    reported the same failure: the ONE decisive passage was not among them, while sibling questions
    in the same run were handed it. Measured cases -- `BIO12L-CH04-P39` carries the ABO gene I
    sentence verbatim and was shortlisted for q135 but not for q048; `PHY12L-CH03-P66` carries the
    negative-temperature-coefficient sentence and was shortlisted for neither of the two questions
    that turn on it; the Colour Blindness paragraph of 4.8.2 reached q104 but not q059.

    A ranked list cannot fix this, because the ranking signal is the question's own words and the
    book states a fact in its own. What fixes it is letting the agent SEE WHAT THE CHAPTER
    CONTAINS and go fetch the section it expects: the index is small (a heading and a page per
    passage), and an agent that knows §4.8.2 Mendelian Disorders exists can read it even when
    overlap never put it in the top 15.
    """
    index = []
    for passage in passages:
        entry = {"passage_id": passage["passage_id"],
                 "section_heading": (passage.get("section_heading") or "").strip(),
                 "page": passage.get("page_start")}
        if not (passage.get("text") or "").strip():
            # A LANDMARK, NOT A QUOTATION. NCERT prints a table or figure here and the extracted
            # text is empty, so nothing can be quoted from it -- but the agent needs to know the art
            # exists. Measured: "which character did Mendel NOT use" is settled only by Table 4.1,
            # whose placeholder is `BIO12L-CH04-P11` with empty text; an agent searched the whole
            # book for the words, found nothing, and could not tell whether NCERT omits the fact or
            # prints it as art. Those are completely different findings.
            entry["printed_as_art"] = ("a table or figure is printed here and its text was not "
                                       "extracted -- nothing can be quoted from it. If the answer "
                                       "depends on this art, say so rather than reporting the fact "
                                       "as absent from NCERT.")
        index.append(entry)
    return index


def question_text(read, row):
    """Stem plus options plus the answer's own text -- what the evidence has to support."""
    parts = [read.get("stem_en") or row.get("stem") or ""]
    for item in (read.get("statements") or []):
        parts.append("%s %s" % (item.get("label") or "", item.get("text") or ""))
    options = read.get("options_en") or {}
    for key in sorted(options):
        parts.append("%s %s" % (key, options[key]))
    return "\n".join(p for p in parts if p)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--chapter", action="append",
                    help="limit to this product chapter name; repeatable")
    ap.add_argument("--papers", nargs="*", help="limit to these paper ids")
    args = ap.parse_args()

    import csv
    index = coverage_index()
    cache, counts, written = {}, collections.Counter(), 0
    os.makedirs(rc.pp(*WORK), exist_ok=True)

    for path in sorted(glob.glob(rc.pp("papers_v2", "exports", "csv", "*.csv"))):
        if "questions_v2" in os.path.basename(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if args.papers and row["paper_id"] not in args.papers:
                    continue
                names = [n.strip() for n in (row["chapter_names"] or "").split(";") if n.strip()]
                if not names:
                    counts["no chapter mapped"] += 1
                    continue
                if args.chapter and not any(n in args.chapter for n in names):
                    continue
                subject = (row.get("subject") or "").strip().lower()
                stream = (row.get("stream") or "").strip().lower()
                if subject == "physics" or (subject, stream) in CONCEPT_BRANCHES:
                    counts["routed to QCA (concept and approach), not NCERT"] += 1
                    continue
                entry = index.get((row["subject"].lower(), names[0].lower()))
                if not entry:
                    counts["chapter not in the coverage map"] += 1
                    continue
                ncert = entry.get("ncert") or {}
                book = ncert.get("book")
                # FLATTENED, because a product chapter can map to several NCERT chapters and the
                # coverage map records that either as [3, 4] or as [[3], [4]] depending on which
                # pass wrote the row. An unflattened list is unhashable, so the cache key below
                # raises -- which only showed when the script was first run across every chapter.
                def _flatten(value):
                    if isinstance(value, list):
                        for item in value:
                            for inner in _flatten(item):
                                yield inner
                    elif value is not None:
                        yield value

                numbers = [int(n) for n in _flatten(ncert.get("chapter_number"))]
                # A product chapter can span TWO BOOKS -- "The p-Block Elements" is chapter 11 of
                # CHE11O and chapter 7 of CHE12O -- and the coverage map then records `book` as a
                # list. The paired form under `chapters` is the one that says which number belongs
                # to which book; reading `book` and `chapter_number` as parallel lists would pair
                # them by position and silently fetch the wrong chapter.
                pairs = [(c["book"], int(c["chapter_number"]))
                         for c in (ncert.get("chapters") or [])
                         if c.get("book") and c.get("chapter_number") is not None]
                if not pairs:
                    books = [b for b in _flatten(book)]
                    pairs = [(b, n) for b in books for n in numbers]
                if not pairs:
                    counts["chapter unresolved to an NCERT chapter"] += 1
                    continue
                book = pairs[0][0]
                numbers = sorted({n for _b, n in pairs})
                key = tuple(pairs)
                if key not in cache:
                    found = []
                    for one_book, one_number in pairs:
                        found.extend(passages_for(one_book, [one_number]))
                    cache[key] = found
                if not cache[key]:
                    counts["NCERT chapter not extracted yet"] += 1
                    continue

                item = "%s#q%03d" % (row["paper_id"], int(row["qno"]))
                read_path = rc.pp(*B3V_OUT, "%s.runA.json" % item.replace("#", "__"))
                read = {}
                if os.path.exists(read_path):
                    try:
                        with open(read_path, encoding="utf-8") as fh2:
                            read = json.load(fh2)
                    except ValueError:
                        read = {}
                if "error" in read:
                    read = {}

                answer = row.get("answer_official") or ""
                payload = {
                    "question": {
                        "stem_en": read.get("stem_en") or row.get("stem"),
                        "statements": read.get("statements") or [],
                        "list_i": read.get("list_i") or [],
                        "list_ii": read.get("list_ii") or [],
                        "options_en": read.get("options_en") or {
                            k: row.get("option_%s" % k) for k in "1234" if row.get("option_%s" % k)},
                    },
                    "answer_to_support": {
                        "option": answer,
                        "text": (read.get("options_en") or {}).get(answer)
                                 or row.get("option_%s" % answer) or "",
                    },
                    "chapter": {"product_chapter": names[0], "ncert_book": book,
                                "ncert_chapter_number": numbers,
                                "ncert_chapter_title": ncert.get("chapter_title")},
                    "product_subtopics": [t.strip() for t in (row["topic_names"] or "").split(";")
                                          if t.strip()],
                    "scoped_by": ("CHAPTER, not subtopic -- see build_evidence_inputs.py. "
                                  "`passages` is a RANKED STARTING POINT of %d, not a boundary. "
                                  "If the line you expect is not in it, find the section in "
                                  "`chapter_index` and read that passage out of `search_this_file` "
                                  "yourself. A measured 9 of 12 agents in the first wave hit "
                                  "exactly this: the decisive passage existed in the book and was "
                                  "not in their shortlist." % PASSAGE_CAP),
                    "chapter_index": chapter_index(
                        passages_for(book, numbers, include_empty=True)),
                    "older_edition_passages": older_edition_passages(book, numbers),
                    "other_books_you_may_search": sibling_books(book),
                    "search_this_file": os.path.relpath(
                        rc.pp(*PASSAGES, "%s.jsonl" % book), rc.pp()),
                    "how_to_search": [
                        "Read `chapter_index` first and name the section you EXPECT to carry the "
                        "line -- the subtopic in `product_subtopics` is usually printed as an "
                        "NCERT heading almost word for word.",
                        "If that section is in `passages`, quote from it.",
                        "If it is not, grep `search_this_file` for its passage_id, or for a "
                        "distinctive word of the fact, and quote the line you find there. Record "
                        "the passage_id you actually used.",
                        "If the chapter genuinely does not carry the fact, search the subject's "
                        "OTHER books listed in `other_books_you_may_search`. A quote from another "
                        "chapter or another class's book is valid evidence -- record the real "
                        "passage_id and say in `note` where it came from. Measured cases: polysome "
                        "is described in Class XI Cell: The Unit of Life, not in Molecular Basis; "
                        "F = ma is in Laws of Motion, not in Work, Energy and Power.",
                        "Where the latest edition cut the section, quote the OLDER edition from "
                        "`older_edition_passages` and say so. Meter Bridge and Potentiometer were "
                        "removed from Current Electricity in 2023 and a 2015 paper still asks them.",
                        "Only after all of that may you answer not_at_all -- and then say which "
                        "sections and which books you looked in, and what you searched for.",
                    ],
                    "passages": rank(cache[key], question_text(read, row),
                                     subtopics=[t.strip() for t in
                                                (row["topic_names"] or "").split(";") if t.strip()]),
                }
                counts["input built"] += 1
                if args.apply:
                    target = rc.pp(*WORK, "%s.runA.input.json" % item.replace("#", "__"))
                    with open(target, "w", encoding="utf-8") as fh2:
                        json.dump(payload, fh2, ensure_ascii=False, indent=1)
                    written += 1

    for reason, number in counts.most_common():
        print("  %-42s %d" % (reason, number))
    print("wrote %d input(s) to %s" % (written, os.path.relpath(rc.pp(*WORK), rc.pp()))
          if args.apply else "(nothing written -- pass --apply)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
