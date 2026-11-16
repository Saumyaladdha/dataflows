#!/usr/bin/env python3
"""Write the NCERT mapping (D1/D2/D4/D5) and the physics concept+approach (QCA) into a paper.

WHY THIS IS A SEPARATE STEP FROM ECAT
-------------------------------------
The owner asked for it directly: NCERT mapping is not part of ECAT. ECAT answers "what does
this question do to a student" from the question alone; this answers "where in the book does
the answer live", which needs the book. Keeping them apart is what let the 2024_S1 ECAT
re-rate touch 7 packets without disturbing a single mapping, and it is why `--redo` on one does
not invalidate the other.

WHAT IT WRITES
--------------
On each question record, one `ncert_mapping` block:

    chapter            D1's NCERT chapter (NOT the exam taxonomy's chapter)
    ncert_subtopics    D2's choice, from the headings NCERT PRINTS -- "6.2.6 Isobilateral
                       (Monocotyledonous) Leaf", not a name of ours
    latest             D4: link_type, supports_answer, and each exact line with its passage id
    older              D5: the older edition's line for the same fact, or what it had none for
    concept_approach   QCA, for physics -- there is no quote to give, by measurement

and renames the existing `classification.subtopics` to `examtopicmapping_subtopics`, because
that is what they are: picks from `chapter_subtopics_mappings/ExamChapterTopicMappings.raw.json`,
an exam taxonomy, with ids like `neet_physics_electric_charges_and_fields_..._practice`. The
2024_S1 review flagged 23 questions for exactly this confusion -- "Not an NCERT heading. Should
be 'Inheritance of One Gene'" -- which is a complaint about the NAME of the field as much as its
value. The old key is kept as an alias so the 19 readers that still look for `subtopics` do not
break; nothing is deleted.

Usage:
    python3 code/join_ncert_map_into_export.py --paper 2024_S1
    python3 code/join_ncert_map_into_export.py --paper 2024_S1 --apply
"""

import argparse
import collections
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPS = os.path.join(os.path.dirname(HERE), "ncert_to_paper_maps")
sys.path.insert(0, os.path.join(HERE, "code"))
from neet_syllabus import Syllabus   # noqa: E402


#: Chapters whose text is not extracted at all, so nothing can be said from NCERT about a
#: question filed under them. Measured, not assumed: these return zero passages with text.
UNEXTRACTED = {"BIO12L-CH06", "BIO12L-CH11"}

#: WHICH SYLLABUS THE LABEL IS JUDGED AGAINST, carried on every label.
#:
#: A syllabus verdict with no year on it rots silently. NMC released the NEET 2026 syllabus on
#: 23 Dec 2025 unchanged from 2025, which is itself the 2023 rationalisation first applied to
#: NEET 2024 -- so one list currently serves 2024 through 2026. The moment 2027 differs, every
#: label written now becomes a claim about a syllabus that no longer exists, and the only way
#: to find them is for them to say which one they meant.
#: Checked 2026-11-13: NMC has published NOTHING for NEET 2027. The newest official syllabus is
#: still the 2026 one it notified on 22 Dec 2025, itself unchanged from 2025 and resting on the
#: 2023 rationalisation first applied to NEET 2024. The 2027 bulletin is expected around Feb
#: 2027, so every label written now is PROVISIONAL for the 2027 paper and must be re-checked
#: when that lands -- which is the whole reason this string is stored on each label.
SYLLABUS_AGAINST = ("NEET 2026 syllabus (NMC, notified 22 Dec 2025; unchanged from 2025, base "
                    "is the 2023 rationalisation first applied to NEET 2024). No NEET 2027 "
                    "syllabus has been published as of 2026-11-13, so this is provisional for "
                    "the 2027 paper.")


def syllabus_label(q, m, syl):
    """Is this question on the NEET syllabus? Read off the SYLLABUS, not off NCERT.

    An earlier version decided this from whether an NCERT line had been found, and the owner
    was right to reject it: the two sources genuinely disagree, in both directions, and
    2024_S1 contains an example of each.

      * p-Block is Unit 10 of the official syllabus and was dropped from the rationalised
        NCERT. The paper's reviewer caught it: "p-Block rationalised NCERT me nahi; NMC-2024
        Unit 10 me hai."
      * "Animal tissues" is printed in Biology Unit 2 of the official syllabus, while the
        rationalised NCERT chapter no longer carries the epithelium material q193 tests. The
        NCERT-driven version labelled q193 OUT OF SYLLABUS. That was wrong, and it was wrong
        in the direction that matters -- telling a student to skip something the exam lists.

    So the verdict comes from `maps/neet_syllabus_2026.json`, parsed from the NMC/UGMEB letter
    of 22-12-2025 published at nta.ac.in. NCERT evidence is reported alongside as a separate
    fact, never as the verdict.

    The strongest signal is a DISTINCTIVE TERM of the chapter appearing in the official text:
    searching it for "cockroach" and "s-block" returns nothing, while "p- block" and "animal
    tissues" are both present. Word-overlap matching alone cannot do this -- "s-Block Elements"
    scores 7 against "P- BLOCK ELEMENTS" on the shared words "block" and "elements".
    """
    cls = q.get("classification") or {}
    subject = str(cls.get("subject") or "")
    chapter_names = [c for c in [(cls.get("chapter") or {}).get("name")] if c]
    sub_names = [s.get("name") for s in (m.get("ncert_subtopics") or []) if s.get("name")]
    sub_names += [s.get("name") for s in (cls.get("examtopicmapping_subtopics") or [])
                  if s.get("name")]

    unit, score, hits = syl.match(subject, chapter_names, sub_names)
    where = ("%s Unit %s: %s" % (subject, unit["unit"], unit["unit_name"])) if unit else None

    # THE TEST IS RUN TWICE, AT TWO GRAINS, because a topic can be deleted without its chapter
    # being deleted. "Structural Organisation in Animals" is Biology Unit 2 of the official
    # syllabus and the unit is intact -- but the cockroach inside it is gone, and the unit's
    # printed topics now say "an insect (Frog)". A chapter-level test alone calls q153 in
    # syllabus; a subtopic-level test alone has no chapter to fall back on for q120, whose
    # whole chapter ("Strategies for Enhancement in Food Production") is absent.
    chap_terms = syl.specific_terms(chapter_names)
    sub_terms = syl.specific_terms(sub_names)
    chap_seen = [w for w in chap_terms if syl.in_official_text(w)]
    sub_seen = [w for w in sub_terms if syl.in_official_text(w)]

    # A SUBTOPIC MISSING FROM THE OFFICIAL TEXT IS NOT EVIDENCE ON ITS OWN. The syllabus is
    # written far coarser than our subtopics -- it says "Fungi", never "Basidiomycetes"; it
    # says "Classification of animals", never "Phylum Chordata". Testing subtopic terms alone
    # marked 16 questions out of syllabus and at least 12 of them were plainly wrong
    # (Androecium, Forebrain, Osmosis, Haloalkanes...). So a subtopic-level removal is only
    # declared when the two INDEPENDENT sources agree: our own latest-vs-older NCERT comparison
    # found the content gone, AND the term is absent from the official syllabus text.
    ncert_removed = m.get("syllabus_signal") == "removed_from_latest_ncert"

    # A CHAPTER NAME MISSING FROM THE OFFICIAL TEXT IS ALSO NOT EVIDENCE ON ITS OWN, for the
    # same reason one grain down: the syllabus uses its own vocabulary. "Haloalkanes and
    # Haloarenes" appears nowhere in it because it is called "Organic Compounds Containing
    # Halogens" -- and the bare-absence rule marked three such questions out of syllabus. So
    # the chapter-level verdict needs corroboration too, and the corroboration available here
    # is NCERT's own chapter list: q120 and q143 are out because `d1-chapter-picker` searched
    # all 32 rationalised biology chapters and found none that covers them.
    #
    # `chap_seen` is checked for a term that is MISSING, not for all of them being missing.
    # Chapter names contain generic nouns that turn up in unrelated topics: "Strategies for
    # Enhancement in Food Production" has "Production", which the syllabus prints in "industrial
    # production" and "vaccine production". Requiring every term to be absent let that one
    # generic word keep a deleted chapter in-syllabus. The pairing that matters is a missing
    # DISTINCTIVE term plus NCERT's own exhaustive search coming up empty.
    # ONLY BIOLOGY. "No NCERT chapter was found" is evidence only where a search actually ran,
    # and D1 runs on biology alone -- physics and physical chemistry are routed to QCA, which
    # produces a concept and no chapter at all. Without this guard every physics question looked
    # like a question whose chapter NCERT does not have, and three Semiconductor Electronics
    # questions were marked out of syllabus while sitting squarely in Unit 19, Electronic Devices.
    no_ncert_chapter = (subject == "Biology" and bool(m)
                        and not ((m.get("chapter") or {}).get("ncert_chapter_ids")))
    chap_missing = [w for w in chap_terms if w not in chap_seen]
    if chap_missing and no_ncert_chapter:
        return ("out_of_syllabus",
                "Two sources agree: %s appear%s nowhere in the official NEET 2026 syllabus, "
                "and d1-chapter-picker searched all 32 chapters of the rationalised NCERT and "
                "found none that covers this question."
                % (", ".join('"%s"' % w for w in chap_missing[:3]),
                   "s" if len(chap_missing) == 1 else ""))
    if chap_terms and not chap_seen:
        return ("needs_review",
                "This chapter's own words (%s) appear nowhere in the official NEET 2026 "
                "syllabus, but the syllabus often uses different wording for the same "
                "chapter — check by hand rather than treating it as off-syllabus."
                % ", ".join('"%s"' % w for w in chap_terms[:3]))
    if ncert_removed and sub_terms and not sub_seen:
        return ("out_of_syllabus",
                "Two sources agree: %s appear%s nowhere in the official NEET 2026 syllabus "
                "text, and the latest NCERT no longer carries this content while the older "
                "edition does. Its chapter (%s) is still on the syllabus."
                % (", ".join('"%s"' % w for w in sub_terms[:3]),
                   "s" if len(sub_terms) == 1 else "", where or subject))
    if unit and (syl.covers(chapter_names, unit)
                 or any(syl.topic_present(unit, w) for w in chap_terms)
                 or any(syl.topic_present(unit, w) for w in sub_terms)):
        got = [w for w in (sub_terms + chap_terms) if syl.topic_present(unit, w)][:2]
        return ("in_syllabus",
                "Listed in the official NEET 2026 syllabus — %s%s." %
                (where, ("; that unit's own topics name %s"
                         % ", ".join('"%s"' % w for w in got)) if got else ""))
    # THE SYLLABUS SOMETIMES NAMES THE GROUP, NOT ITS MEMBERS. Unit 1 lists "Fungi into major
    # groups" and never prints "Phycomycetes", so a question on the fungal classes failed the
    # word-by-word test and was sent to review though it is plainly examinable.
    if unit:
        head, hit = syl.group_cover(sub_terms + chap_terms, unit)
        if head:
            return ("in_syllabus",
                    "Listed in the official NEET 2026 syllabus — %s. The syllabus names the "
                    "group rather than its members: it lists \"%s\", and %s %s one of its major "
                    "groups." % (where, head, ", ".join('"%s"' % w for w in hit[:3]),
                                 "is" if len(hit) == 1 else "are"))
    if ncert_removed:
        return ("needs_review",
                "The latest NCERT no longer carries this content (the older edition does), but "
                "the official syllabus text neither lists nor excludes it at this level of "
                "detail — decide by hand.")
    if unit:
        return ("needs_review",
                "Closest official unit is %s, but neither this chapter's name nor its topic "
                "words appear in that unit — check by hand before relying on it." % where)
    return ("needs_review",
            "No unit of the official NEET 2026 %s syllabus matched this chapter." % subject)


def with_paragraph(lines, paragraphs, report):
    """Attach to each quoted line the whole NCERT paragraph it was cut from.

    A quoted sentence alone cannot be checked: a reader cannot see whether the next sentence
    qualifies it, nor where in the chapter it sits. The owner asked for the paragraph to be in
    the JSON as well as on the page, so the two always agree -- the card renders this same text
    with the quote marked inside it.

    `paragraph_found` is recorded rather than assumed: the older edition's ids are BLOCK ids and
    the latest edition's are passage ids, and a line whose paragraph is missing is a signal that
    the lookup and the evidence disagree about what exists.
    """
    out = []
    for e in lines:
        e = dict(e)
        para = paragraphs.get(e.get("passage_id"))
        line = str(e.get("exact_line") or "")
        if para:
            found = line in para
            e["quote_is_in_paragraph"] = found
            if found:
                # THE WINDOW, NOT THE WHOLE PASSAGE. Storing the full stored text would put a
                # 15,000-character blob on each of several lines of the same question --
                # BIO12L-CH05 holds the whole of Molecular Basis of Inheritance in 16 passages.
                # About 300 characters each way, snapped outward to sentence boundaries, is
                # enough to see whether the next sentence qualifies the quote, which is the
                # only reason the surrounding text is here at all. `passage_id` still points
                # at the full text for anyone who needs it.
                at = para.find(line)
                lo, hi = max(0, at - 300), min(len(para), at + len(line) + 300)
                if lo > 0:
                    dot = para.rfind(". ", lo, at)
                    lo = dot + 2 if dot != -1 else lo
                if hi < len(para):
                    dot = para.find(". ", at + len(line), hi)
                    hi = dot + 1 if dot != -1 else hi
                e["context"] = ("… " if lo > 0 else "") + para[lo:hi] + (" …" if hi < len(para) else "")
                report["context window attached"] += 1
            else:
                report["QUOTE NOT FOUND in its own paragraph"] += 1
        else:
            report["no paragraph stored for this id"] += 1
        out.append(e)
    return out


def read_step(paper, step, qid):
    p = os.path.join(MAPS, "steps", step, "out", "%s.%s.runA.json" % (paper, qid))
    if not os.path.exists(p):
        return None
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception:
        return None
    return None if d.get("error") else d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    year = a.paper.split("_")[0]
    path = os.path.join(HERE, "data", year, a.paper, "questions.json")
    doc = json.load(open(path, encoding="utf-8"))
    report = collections.Counter()

    index_path = os.path.join(MAPS, "maps", "ncert_heading_index.json")
    index = json.load(open(index_path, encoding="utf-8"))
    paragraphs = json.load(open(os.path.join(MAPS, "maps", "paragraphs.json"), encoding="utf-8"))
    syl = Syllabus()

    def heading(sid):
        """`BIO11L-CH06#6.2.6` -> ('6.2.6', 'Isobilateral (Monocotyledonous) Leaf')."""
        ch, _, tail = str(sid or "").partition("#")
        for sec in ((index.get(ch) or {}).get("sections") or []):
            if sec.get("n") == tail:
                return tail, sec.get("heading")
        return tail, None

    for q in doc["questions"]:
        qid = q["question_id"].split("__")[-1]
        cls = q.setdefault("classification", {})

        # THE RENAME, as an addition. `subtopics` stays as an alias: record_v3, paper_md,
        # compute_counts, apply_review, step_plugins and 14 other readers index it by that
        # name, and renaming the key alone would have broken all of them silently.
        if "subtopics" in cls and "examtopicmapping_subtopics" not in cls:
            cls["examtopicmapping_subtopics"] = cls["subtopics"]
            report["examtopicmapping_subtopics named"] += 1
        st = q.setdefault("status", {})
        if "subtopic" in st and "examtopicmapping_subtopic" not in st:
            st["examtopicmapping_subtopic"] = st["subtopic"]

        d1, d2 = read_step(a.paper, "D1", qid), read_step(a.paper, "D2", qid)
        d4, d5 = read_step(a.paper, "D4", qid), read_step(a.paper, "D5", qid)
        qca = read_step(a.paper, "QCA", qid)
        if not any((d1, d2, d4, d5, qca)):
            # STILL LABELLED. These are the chemistry questions held back until their NCERT is
            # extracted; a question with no mapping is exactly the case where a blank column
            # would be read as "fine" rather than "unchecked".
            label, why = syllabus_label(q, {}, syl)
            q["syllabus"] = {"label": label, "basis": why, "against": SYLLABUS_AGAINST,
                         "source_url": syl.source_url}
            report["syllabus: %s" % label] += 1
            report["no mapping produced"] += 1
            continue

        m = {}
        if d1:
            chs = [c for c in (d1.get("chapter_ids") or []) if c and c != "unsure"]
            m["chapter"] = {"ncert_chapter_ids": chs, "why": d1.get("why"),
                            "confidence": d1.get("confidence")}
            report["chapter mapped" if chs else "chapter unsure"] += 1
        if d2:
            subs = []
            for sid in (d2.get("subtopic_ids") or []):
                if not sid or sid == "unsure":
                    continue
                n, name = heading(sid)
                subs.append({"id": sid, "printed_number": n, "name": name})
            m["ncert_subtopics"] = subs
            m["ncert_subtopics_why"] = d2.get("why")
            cls["ncert_subtopics"] = subs
            report["ncert_subtopic named" if subs else "ncert_subtopic unsure"] += 1
        if d4:
            m["latest"] = {"link_type": d4.get("link_type"),
                           "supports_answer": d4.get("supports_answer"),
                           "lines": with_paragraph(d4.get("evidence") or [], paragraphs, report),
                           "missing": d4.get("missing") or [],
                           "note": d4.get("note")}
            report["latest NCERT line quoted"] += 1 if (d4.get("evidence") or []) else 0
        if d5:
            m["older"] = {"lines": with_paragraph(d5.get("older") or [], paragraphs, report),
                          "none_for": d5.get("none_for") or [],
                          "note": d5.get("note")}
            report["older NCERT line quoted"] += 1 if (d5.get("older") or []) else 0
        # THE SYLLABUS SIGNAL, AND WHY IT IS NOT "latest found nothing + older found something".
        # That rule flags four questions on 2024_S1 and one of them, q111, is a FALSE positive:
        # D4 returned `states_answer / not_at_all` there after searching only its 15 ranked
        # passages, and the D5 agent said so unprompted -- "more likely a D4 gap than deleted
        # content, so D6 doesn't mis-classify it as a removal". The honest discriminator is
        # D4's own `link_type`: `beyond_ncert_method` is the value it uses when it has checked
        # the whole stored chapter and the material is not there ("Confirmed absent, not
        # unfound"), while `states_answer` with no lines means it simply did not find one.
        lat = m.get("latest") or {}
        old_ = m.get("older") or {}
        if lat.get("supports_answer") == "not_at_all" and (old_.get("lines") or []):
            if lat.get("link_type") == "beyond_ncert_method":
                m["syllabus_signal"] = "removed_from_latest_ncert"
                report["REMOVED from latest NCERT (older has it)"] += 1
            else:
                m["syllabus_signal"] = "latest_line_not_found_needs_recheck"
                report["latest line not found -- recheck, not a removal"] += 1
        if qca:
            m["concept_approach"] = {"concept": qca.get("concept"),
                                     "approach": qca.get("approach"),
                                     "also_uses": qca.get("also_uses") or [],
                                     "note": qca.get("note")}
            report["physics concept + approach"] += 1
        q["ncert_mapping"] = m
        label, why = syllabus_label(q, m, syl)
        q["syllabus"] = {"label": label, "basis": why, "against": SYLLABUS_AGAINST,
                         "source_url": syl.source_url}
        report["syllabus: %s" % label] += 1

    print("%s: %d questions" % (a.paper, len(doc["questions"])))
    for k, v in sorted(report.items()):
        print("   %-34s %3d" % (k, v))
    if not a.apply:
        print("(nothing written -- pass --apply)")
        return
    json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote %s" % os.path.relpath(path, HERE))


if __name__ == "__main__":
    main()
