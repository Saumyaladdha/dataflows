#!/usr/bin/env python3
"""Decide a question's NEET-syllabus status from the OFFICIAL syllabus, not from NCERT.

WHY THIS IS NOT AN NCERT QUESTION
---------------------------------
The two genuinely disagree, in both directions, and the 2024_S1 data shows each:

  * p-Block is Unit 10 of the NEET syllabus and was dropped from the rationalised NCERT. The
    paper's own reviewer caught this -- "p-Block rationalised NCERT me nahi; NMC-2024 Unit 10
    me hai".
  * "Animal tissues" is printed in Biology Unit 2 of the official syllabus, while the
    rationalised NCERT chapter no longer carries the epithelium material q193 tests.

An earlier version of this decided syllabus status from whether an NCERT line had been found,
and so labelled q193 out of syllabus when the NMC lists it. A verdict about the SYLLABUS has to
be read off the syllabus.

THE SOURCE
----------
`maps/neet_syllabus_2026.json`, parsed from the NMC/UGMEB letter of 22-12-2025 published at
nta.ac.in -- 18 pages, 50 units (Physics 20, Chemistry 20, Biology 10), fetched 2026-11-13.
Not an aggregator: three aggregator unit lists were checked against it and agree, but the file
is built from the PDF. (The PDF has its own quirks, preserved rather than corrected: it prints
"UNITS 15" for chemistry unit 15, and describes the frog as "an insect".)

MATCHING, AND WHY IT REPORTS ITS OWN CONFIDENCE
-----------------------------------------------
A question carries an exam-taxonomy chapter name; the syllabus is organised in units. The match
is word overlap between the question's chapter and subtopic names and each unit's name and
printed topic text. A weak match is reported as weak rather than rounded up: a syllabus verdict
a reader cannot check is worse than none, because a student acts on it.
"""

import json
import os
import re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPS = os.path.join(os.path.dirname(HERE), "ncert_to_paper_maps", "maps")

#: `chemistry`, `physics` and `biology` are in here deliberately. Without them "Surface
#: Chemistry" -- a chapter the 2023 rationalisation DELETED -- matched "Principles Related to
#: Practical Chemistry" on the bare word "chemistry" and would have been labelled in-syllabus.
#: A subject name carries no information inside its own subject's unit list.
STOP = set(("the a an of in to and or is are be for on with that this these those it its as at "
            "by from which what not but can also more than then their there has have had do "
            "does did will would may might one two both each other such into general brief "
            "account only introduction elementary idea ideas chemistry physics biology "
            "chemical physical biological").split())


def words(*parts):
    ws = re.findall(r"[a-z]{4,}", " ".join(str(p or "") for p in parts).lower())
    return set(w for w in ws if w not in STOP)


class Syllabus(object):
    def __init__(self, path=None):
        path = path or os.path.join(MAPS, "neet_syllabus_2026.json")
        d = json.load(open(path, encoding="utf-8"))
        self.source = d.get("source")
        self.source_url = d.get("source_url")
        self.fetched = d.get("fetched")
        self.units = d.get("units") or []
        for u in self.units:
            u["_name_words"] = words(u.get("unit_name"))
            u["_topic_words"] = words(u.get("topics"))
        self._all_text = " ".join((u.get("unit_name") or "") + " " + (u.get("topics") or "")
                                  for u in self.units)

    def match(self, subject, chapter_names, subtopic_names):
        """(unit, score, matched_words) for the best-fitting unit of that subject, or (None,0,[])."""
        want = words(*(list(chapter_names) + list(subtopic_names)))
        if not want:
            return None, 0.0, []
        best, best_score, best_hits = None, 0.0, []
        for u in self.units:
            if (u.get("subject") or "").lower() != (subject or "").lower():
                continue
            # the unit NAME is worth more than its topic prose: a chapter called "Electrostatics"
            # matching the unit called "Electrostatics" is a stronger fact than sharing three
            # common words with a long topic list.
            nhit = want & u["_name_words"]
            thit = want & u["_topic_words"]
            score = 3.0 * len(nhit) + len(thit)
            if score > best_score:
                best, best_score, best_hits = u, score, sorted(nhit | thit)
        return best, best_score, best_hits

    #: Words that name a KIND OF TREATMENT rather than a subject. "Morphology of Cockroach"
    #: is on the syllabus or not because of `cockroach`, never because of `morphology` -- and
    #: `morphology` is printed in Unit 2 regardless, so leaving it in would have called the
    #: deleted cockroach topics in-syllabus.
    PROCESS = set(("morphology anatomy structure structural function functions type types kinds "
                   "classification introduction general basic principle principles property "
                   "properties study concept concepts organisation organization system systems "
                   "about their").split())

    def specific_terms(self, names):
        """The words in these names that actually name a subject, longest first."""
        out = []
        for n in names or []:
            for w in re.findall(r"[A-Za-z][A-Za-z-]{4,}", str(n)):
                lw = w.lower()
                if lw in self.PROCESS or lw in STOP or lw in out:
                    continue
                out.append(w)
        return sorted(set(out), key=lambda w: -len(w))

    def covers(self, chapter_names, unit):
        """Does this chapter's name clearly belong to that unit's name?

        A ratio, not a score. "Thermodynamics" is one word and matches the unit called
        THERMODYNAMICS completely, but scored only 4 on the absolute scale and was being sent
        to `needs_review` -- 87 questions were, including exact-name matches.
        """
        want = words(*chapter_names)
        if not want:
            return False
        return len(want & unit["_name_words"]) / float(len(want)) >= 0.45

    #: THE SYLLABUS NAMES A GROUP WHERE A QUESTION NAMES ITS MEMBERS.
    #: q107 asks which fungus is the bread mould and which is the smut. Neither
    #: "Phycomycetes" nor "Basidiomycetes" is printed anywhere in the official text, so the
    #: word-by-word test sent it to `needs_review` -- yet Unit 1 reads "classification of
    #: Monera; Protista and Fungi into major groups", and the major groups of Fungi ARE those
    #: classes. The umbrella is only honoured when the group word itself is printed in the
    #: matched unit, so this widens nothing on its own; it just stops a correct question being
    #: flagged because the syllabus chose the collective noun.
    GROUPS = {
        "Fungi": ("phycomycetes", "ascomycetes", "basidiomycetes", "deuteromycetes"),
        "Monera": ("archaebacteria", "eubacteria", "cyanobacteria", "mycoplasma"),
        "Protista": ("chrysophytes", "dinoflagellates", "euglenoids", "protozoans"),
        "Algae": ("chlorophyceae", "phaeophyceae", "rhodophyceae"),
        "nonchordate": ("porifera", "coelenterata", "ctenophora", "platyhelminthes",
                        "aschelminthes", "annelida", "arthropoda", "mollusca",
                        "echinodermata", "hemichordata"),
        "chordate": ("urochordata", "cephalochordata", "cyclostomata", "chondrichthyes",
                     "osteichthyes", "amphibia", "reptilia", "aves", "mammalia"),
    }

    def group_cover(self, terms, unit):
        """(official group word, the member terms it covers) if this unit names the group."""
        for head, members in self.GROUPS.items():
            if not self.topic_present(unit, head):
                continue
            hit = [t for t in terms or [] if str(t).lower() in members]
            if hit:
                return head, hit
        return None, []

    def in_official_text(self, term):
        """Is this word printed ANYWHERE in the official syllabus? The decisive test.

        Word-overlap scoring cannot tell "s-Block Elements" from "P- BLOCK ELEMENTS" -- they
        share "block" and "elements" and score 7. Searching the official text settles it:
        "s-block" returns nothing, "p- block" is present. Same for "cockroach" (absent) against
        "animal tissues" (present), which is the pair that decides three of this paper's
        questions. The term is matched loosely on hyphens and spaces because the PDF prints
        "P- BLOCK" with a space the chapter name does not have.
        """
        return self._present(term, self._all_text)

    @staticmethod
    def _present(term, haystack):
        """Word-boundary match, hyphen- and space-tolerant.

        It was a bare substring search, and that is how "Production" came back PRESENT: it sits
        inside "Reproduction". Two questions on the deleted chapter "Strategies for Enhancement
        in Food Production" were labelled in-syllabus on that false hit. The boundaries are
        required; the hyphen slack is also required, because the PDF prints "P- BLOCK" where
        the chapter name is "p-Block".
        """
        t = str(term or "").strip()
        if not t:
            return False
        t = re.escape(t).replace(r"\-", r"[\s-]*").replace(r"\ ", r"\s+")
        return bool(re.search(r"\b%s\b" % t, haystack, re.I))

    def topic_present(self, unit, term):
        """Is a specific word printed in that unit's own topic text?"""
        return bool(unit) and self._present(term, unit.get("topics") or "")
