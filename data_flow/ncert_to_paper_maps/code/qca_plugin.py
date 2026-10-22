"""QCA: the concept a question tests, and the approach that answers it.

WHY THIS STEP EXISTS, AND WHY ONLY FOR PHYSICS AND PHYSICAL CHEMISTRY
--------------------------------------------------------------------
Stage D quotes the exact NCERT line an answer rests on. For Biology that IS the evidence: the answer
is a sentence NCERT prints, and highlighting that sentence settles the question. For Physics and
Physical Chemistry it is the wrong instrument, and the measurements said so before anyone decided
it. Across twelve evidence agents on these two subjects the verdict came back `partly` again and
again -- not because the physics was missing from NCERT, but because what the solution needed was a
display equation (carried as an image, so absent from the passage text), a constant in a table row,
or a relation taught in a different chapter. The honest record for a numerical is not a quotation.

So for these subjects the record is two short lines: the CONCEPT -- the relation itself, `F = ma`,
`V = IR`, Raoult's law -- and the APPROACH, one line on how it is applied to this question. A
reader with those two knows what the question is for. A reader with a half-matched NCERT paragraph
knows less than nothing, because the paragraph looks like evidence and is not.

THREE KINDS OF QUESTION, NOT TWO
--------------------------------
The first version of this step split the corpus in two -- quote for Biology and Organic, concept for
Physics and Physical Chemistry -- and that split was wrong at one edge, which the owner caught:

    quote only        a fact stated in a sentence. Most of Biology, Inorganic.
    concept only      a value NCERT never prints. Physics, Physical Chemistry.
    QUOTE AND CONCEPT a question that is BOTH -- the rule is printed in NCERT and the answer is
                      still a number you have to compute from it.

That third kind is real and not rare. Heredity is the clear case: `Principles of Inheritance and
Variation` and `Molecular Basis of Inheritance` carry monohybrid and dihybrid ratios, probabilities
of an affected child, and base-pair arithmetic -- and NCERT states the law of segregation, the 3:1
and 9:3:3:1 ratios and the 0.34 nm rise per base pair outright. So the quote is genuine evidence AND
the student still needs the route. Organic Chemistry is the same shape: its reactions are printed as
equations, so the equation is quotable, and the approach -- which reagent, in which order, and why
that regiochemistry -- is still the thing a reader needs said.

For those, this step runs ALONGSIDE D4V rather than instead of it, and the page shows both.

A question is treated as the third kind when its own record says it computes something: ECAT's E2
`format` is `calculate_value`, or its E4 `cognitive_demand` is `calculation`, or D4 recorded
`derivation_steps` for it. That is the question's own measured shape, not a guess from its chapter
name -- a Heredity question asking which disorder is X-linked is still quote-only.

WHAT THE INPUT OMITS, AND WHY
-----------------------------
The answer, in every form -- the booklet's printed answer, any key, and `b6-blind-solver`'s answer.
An agent that can see which option is correct writes the approach backwards from it, and a route
built backwards from a known answer always reads shorter and cleaner than the route a candidate
has to find. Same omission, and same reason, as B6V and E7V.
"""

import collections
import glob
import json
import os
import sys

import runner_core as rc

ListLine = collections.namedtuple(
    "ListLine", ["item_id", "agent", "input_path", "output_path", "run_label"])

CORPUS = ("papers_v2",)
B3V_OUT = ("steps", "B3V", "out")
QSUBJ_OUT = ("steps", "QSUBJ", "out")
QCHAP_OUT = ("steps", "QCHAP", "out")
WORK = ("steps", "QCA", "work")
OUT = ("steps", "QCA", "out")

D4V_OUT = ("steps", "D4V", "out")
#: Branches whose record is a concept INSTEAD of a quotation. Everything else that is in scope gets
#: both -- the quoted line AND the approach.
CONCEPT_ONLY = {("chemistry", "physical")}


class QCAPlugin:
    step = "QCA"
    agent = "q-concept-approach"

    def _questions(self, filters=None):
        """{item_id: (paper_id, question, read)} for in-scope questions B3V has read.

        Only read questions, for the reason B6V and E7V give: a question whose fractions arrived
        mangled is not a question yet, and naming the concept of a fragment names the concept of
        something the candidate never saw.
        """
        wanted = set((filters or {}).get("items") or [])
        papers = set((filters or {}).get("papers") or [])
        out = {}
        for path in sorted(glob.glob(rc.pp(*CORPUS, "papers", "*.json"))):
            with open(path, encoding="utf-8") as fh:
                paper = json.load(fh)
            meta = paper["meta"]
            paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
            if papers and paper_id not in papers:
                continue
            for question in paper["questions"]:
                item_id = "%s#q%03d" % (paper_id, question["qno"])
                if wanted and item_id not in wanted:
                    continue
                read_path = rc.pp(*B3V_OUT, "%s__q%03d.runA.json" % (paper_id, question["qno"]))
                if not os.path.exists(read_path):
                    continue
                try:
                    with open(read_path, encoding="utf-8") as fh:
                        read = json.load(fh)
                except ValueError:
                    continue
                if "error" in read:
                    continue
                if not self._in_scope(item_id, question):
                    continue
                out[item_id] = (paper_id, question, read)
        return out

    @staticmethod
    def _confirmed_subject(item_id, question):
        """The CONFIRMED subject, never the paper's positional guess.

        A guess from the question number was wrong on all 43 checked questions of 2015 Code A and
        all 179 of 2017 Code C. Scoping this step by a guess would hand physics briefs to chemistry
        questions, which is worse than leaving them unscoped.
        """
        path = rc.pp(*QSUBJ_OUT, "%s.runA.json" % item_id.replace("#", "__"))
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as fh:
                    data = json.load(fh)
                if data.get("subject") and data["subject"] != "unsure":
                    return data["subject"].lower()
            except ValueError:
                pass
        if "printed heading" in (question.get("subject_from") or ""):
            return (question.get("subject") or "").lower()
        return None

    def _stream(self, item_id):
        """Chemistry's branch (physical / organic / inorganic), from the chapter mapping."""
        path = rc.pp(*QCHAP_OUT, "%s.runA.json" % item_id.replace("#", "__"))
        if not os.path.exists(path):
            return None
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except ValueError:
            return None
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import export_paper_v2 as export
        names = data.get("chapter_names") or ([data["chapter_name"]]
                                              if data.get("chapter_name") else [])
        codes = data.get("chapter_ids") or data.get("chapter_codes") or []
        stream, _branch = export.stream_and_branch("chemistry", None, codes, names)
        return (stream or "").lower() or None

    @staticmethod
    def _computes(item_id):
        """True when the question's OWN record says an answer has to be computed.

        Three independent witnesses, any one of which settles it: ECAT's E2 `format`, ECAT's E4
        `cognitive_demand`, and whether D4 recorded `derivation_steps`. Read off the record rather
        than inferred from the chapter, because the distinction is per question and not per chapter:
        a Heredity question asking which disorder is X-linked is a stated fact, and a Heredity
        question asking the probability of an affected grandson is a calculation, and they sit on
        facing pages of the same chapter.
        """
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import export_paper_v2 as export
        paper_id, qno = item_id.split("#q")
        rating = export.categories_of(paper_id, int(qno))[0] or {}
        if rating.get("format") == "calculate_value":
            return True
        if rating.get("cognitive_demand") == "calculation":
            return True
        path = rc.pp(*D4V_OUT, "%s.runA.json" % item_id.replace("#", "__"))
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as fh:
                    data = json.load(fh)
            except ValueError:
                return False
            # `derivation_steps` ALONE is too loose, and an agent caught it: D4 fills steps for
            # `concept_applied` elimination chains as well, so three recall questions -- "which
            # character did Mendel NOT use", "put these four terms in order" -- were offered as
            # calculations. The steps only count as evidence of computing when the link is a RULE,
            # which is the shape a numerical has.
            return (bool(data.get("derivation_steps"))
                    and data.get("link_type") in ("rule_used", "rules_chained"))
        return False

    def _in_scope(self, item_id, question):
        """Which questions get a concept and an approach at all.

            Physics, Physical Chemistry      ALWAYS -- and with no NCERT quotation beside it,
                                             because the answer is a value the book never prints.
            Biology, Organic, Inorganic      ONLY where the question solves or computes something.
                                             Their content IS in NCERT, so the formula or constant
                                             can be pointed at in the book -- and then the route
                                             still needs saying. A stated-fact question in those
                                             subjects needs no route: the quoted sentence IS the
                                             whole answer, and an "approach" under it would be
                                             padding dressed as method.

        That last line is the correction the owner made twice, and it is the one that keeps this
        step honest. Scoping these three subjects by subject alone would put a concept box under
        every "which of the following is a hormone", where there is no concept to state.
        """
        subject = self._confirmed_subject(item_id, question)
        if subject == "physics":
            return True
        if subject == "chemistry":
            if (subject, self._stream(item_id)) in CONCEPT_ONLY:
                return True
            return self._computes(item_id)       # organic and inorganic: solving questions only
        if subject == "biology":
            return self._computes(item_id)
        return False

    def _out_path(self, item_id):
        return rc.pp(*OUT, "%s.runA.json" % item_id.replace("#", "__"))

    def _input_path(self, item_id, run_label="runA"):
        return rc.pp(*WORK, "%s.%s.input.json" % (item_id.replace("#", "__"), run_label))

    def list_items(self, filters):
        # The agent writes here, so the directory has to exist before the first one runs. Reported
        # by shard ab, whose first write failed with FileNotFoundError until it made the directory
        # itself -- which is work no agent should be doing.
        os.makedirs(rc.pp(*OUT), exist_ok=True)
        lines = []
        for item_id, (_paper_id, question, read) in self._questions(filters).items():
            if os.path.exists(self._out_path(item_id)):
                continue
            figure = (question.get("agent_figure_images")
                      or question.get("figure_images") or [None])[0]
            crop = question.get("question_image")
            # NO ANSWER FIELD OF ANY KIND -- see the module docstring.
            payload = {
                "question_id": item_id,
                "stem_en": read.get("stem_en"),
                "statements": read.get("statements") or [],
                "list_i": read.get("list_i") or [],
                "list_ii": read.get("list_ii") or [],
                "options_en": read.get("options_en") or {},
                "structure": read.get("structure"),
                "figure_image": (os.path.relpath(rc.pp(*CORPUS, figure), rc.pp())
                                 if figure else None),
                "question_image": (os.path.relpath(rc.pp(*CORPUS, crop), rc.pp())
                                   if crop else None),
            }
            path = self._input_path(item_id)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, ensure_ascii=False, indent=1)
            lines.append(ListLine(item_id, self.agent, os.path.relpath(path, rc.pp()),
                                  os.path.relpath(self._out_path(item_id), rc.pp()), "runA"))
        return lines

    def list_reason(self):
        questions = self._questions()
        if not questions:
            return ("QCA has nothing to do: it offers only Physics and physical-Chemistry questions "
                    "that B3V has read AND whose subject is confirmed, never guessed from the "
                    "question number.")
        done = sum(1 for i in questions if os.path.exists(self._out_path(i)))
        return "QCA: all %d in-scope question(s) already have a concept and approach." % done

    def check(self, filters):
        """Report, and return the retry lines -- NOT a summary dict.

        Every plugin's `check` returns a list of ListLines for the runner to re-dispatch; returning
        a dict made `run_step.py --check` fall into its list formatter and die on a string. The
        report itself goes to stderr, the way E7V's does.
        """
        try:
            import jsonschema
        except ImportError:
            jsonschema = None

        schema = json.load(open(rc.pp("schemas", "QCA.json"), encoding="utf-8"))
        failed, passed, tally = [], 0, collections.Counter()
        for item_id in self._questions(filters):
            out_path = self._out_path(item_id)
            if not os.path.exists(out_path):
                continue
            try:
                data = json.load(open(out_path, encoding="utf-8"))
            except ValueError as exc:
                failed.append((item_id, "output is not valid JSON: %s" % exc))
                continue
            if "error" in data:
                tally["declared unreadable"] += 1
                continue
            if jsonschema is not None:
                try:
                    jsonschema.validate(data, schema)
                except jsonschema.ValidationError as exc:
                    failed.append((item_id, "QCA_SHAPE: %s" % exc.message))
                    continue
            else:
                # The library is absent in this interpreter, so the two bounds that actually bite
                # are enforced by hand rather than skipped. Agents reported hitting the 90 exactly.
                if not 2 <= len(data.get("concept", "")) <= 90:
                    failed.append((item_id, "QCA_SHAPE: concept is %d characters, limit is 90"
                                   % len(data.get("concept", ""))))
                    continue
                if not 10 <= len(data.get("approach", "")) <= 240:
                    failed.append((item_id, "QCA_SHAPE: approach is %d characters, limit is 240"
                                   % len(data.get("approach", ""))))
                    continue
            if data.get("question_id") != item_id:
                failed.append((item_id, "QCA_WRONG_ID: output says %r" % data.get("question_id")))
                continue
            # A concept that is a sentence about the question is the failure this step was written
            # to prevent, and it has one reliable tell: it talks ABOUT the question.
            concept = data["concept"].lower()
            if any(phrase in concept for phrase in
                   ("this question", "the question", "tests the", "asks ", "candidate")):
                failed.append((item_id, "QCA_CONCEPT_IS_A_SENTENCE: %r describes the question "
                                        "instead of stating the relation" % data["concept"]))
                continue
            tally["concept and approach written"] += 1
            passed += 1
        for item_id, message in failed:
            print("QCA %-22s FAIL  %s" % (item_id, message), file=sys.stderr)
        total = len(self._questions(filters))
        print("QCA --check: %d passed, %d failed, %d without output (of %d)"
              % (passed, len(failed), total - passed - len(failed), total), file=sys.stderr)
        if tally:
            print("QCA %s" % dict(tally), file=sys.stderr)
        return []


def get_plugin():
    return QCAPlugin()
