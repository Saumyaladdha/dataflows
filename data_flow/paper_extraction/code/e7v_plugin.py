"""E7V: the difficulty band of one question of the papers_v2 corpus.

WHY A SEPARATE STEP FROM E7
---------------------------
`E7` is a SCRIPT over the 580-question v1 sheet: it derives a band from ECAT's already-filled
cognitive-demand and solution-structure columns. This one is the JUDGEMENT itself, per SPEC Section
E7 -- an agent counting the work a question takes. The two cannot share a step because they do not
share an item: E7's item is a run, E7V's is a question.

WHAT THE INPUT DELIBERATELY OMITS
---------------------------------
The answer. Not the booklet's printed answer, not any key, and not `b6-blind-solver`'s answer
either. Difficulty is a property of the question, not of which option is correct, and a rater who
can see the answer reasons backwards from it -- the route to a known answer always looks shorter
than the route a candidate has to find. This is the same omission B6V makes, for a related reason,
and it is the reason this plugin builds its own payload rather than reusing the export's row.

WHAT IT INCLUDES THAT B6V DOES NOT
----------------------------------
The question image. A rater has to be able to see a figure to know whether it supplies data or
merely decorates, and has to see the printed layout to judge whether the options are the kind that
are eliminated one at a time.
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
WORK = ("steps", "E7V", "work")
OUT = ("steps", "E7V", "out")
#: Step whose band must agree with the step count, checked below.
BAND_STEPS = {"easy": (1, 1), "medium": (2, 3), "hard": (4, 99)}


class E7VPlugin:
    step = "E7V"
    agent = "e7-difficulty-rater"

    def _questions(self, filters=None):
        """{item_id: (paper_id, question, read)} -- questions B3V has read.

        Only read questions are offered, and for the same reason B6V gives: counting the steps of a
        question whose fractions are mangled counts the steps of a different question. A damaged
        question is not hard, it is unanswerable, and a band on it is worse than no band.
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
                out[item_id] = (paper_id, question, read)
        return out

    @staticmethod
    def _subject(paper_id, item_id, question):
        """The CONFIRMED subject, never the paper's positional guess.

        Three booklets print no section heading, so their `subject` field is a guess from the
        question number -- and in 2015_A all 43 of those guesses were wrong, in 2017_C all 179. This
        plugin shipped reading that raw field, and a rater correctly reported being handed
        "Physics" for the chemistry block q004-q045. The subject does not change a difficulty band
        on its own, but it is shown to the rater as context, and context that is wrong is worse than
        context that is absent.
        """
        path = rc.pp("steps", "QSUBJ", "out", "%s.runA.json" % item_id.replace("#", "__"))
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as fh:
                    data = json.load(fh)
                if data.get("subject") and data["subject"] != "unsure":
                    return data["subject"]
            except ValueError:
                pass
        if "printed heading" in (question.get("subject_from") or ""):
            return question.get("subject")
        # A bare positional guess is not reported as a subject at all: saying nothing is honest,
        # saying "Physics" about a chemistry question is not.
        return None

    def _out_path(self, item_id):
        return rc.pp(*OUT, "%s.runA.json" % item_id.replace("#", "__"))

    def _input_path(self, item_id, run_label="runA"):
        return rc.pp(*WORK, "%s.%s.input.json" % (item_id.replace("#", "__"), run_label))

    def list_items(self, filters):
        lines = []
        for item_id, (paper_id, question, read) in self._questions(filters).items():
            if os.path.exists(self._out_path(item_id)):
                continue
            figure = (question.get("agent_figure_images")
                      or question.get("figure_images") or [None])[0]
            crop = question.get("question_image")
            # NO ANSWER FIELD OF ANY KIND. Adding one here is how a rater starts reasoning from the
            # answer instead of from the work -- see the module docstring.
            payload = {
                "stem_en": read.get("stem_en"),
                "statements": read.get("statements") or [],
                "list_i": read.get("list_i") or [],
                "list_ii": read.get("list_ii") or [],
                "options_en": read.get("options_en") or {},
                "structure": read.get("structure"),
                "subject": self._subject(paper_id, item_id, question),
                "stem_source": "b3v_image_read",
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
            return ("E7V has nothing to rate: it only offers questions B3V has already read, and "
                    "none have been. Counting the steps of a mangled draft counts the steps of a "
                    "different question.")
        done = sum(1 for i in questions if os.path.exists(self._out_path(i)))
        return "E7V: all %d readable question(s) already banded." % done

    def check(self, filters):
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
        import jsonschema

        schema = json.load(open(rc.pp("schemas", "E7V.json"), encoding="utf-8"))
        tally = collections.Counter()
        failed, passed = [], 0
        for item_id, (paper_id, _question, _read) in self._questions(filters).items():
            out_path = self._out_path(item_id)
            if not os.path.exists(out_path):
                continue
            try:
                data = json.load(open(out_path, encoding="utf-8"))
            except ValueError as exc:
                failed.append((item_id, "output is not valid JSON: %s" % exc))
                continue
            try:
                jsonschema.validate(data, schema)
            except jsonschema.ValidationError as exc:
                failed.append((item_id, "schema: %s" % exc.message))
                continue
            if "error" in data:
                failed.append((item_id, "agent reported: %s" % data["error"]))
                continue
            band = data.get("difficulty")
            tally[band] += 1
            steps = data.get("steps_to_solve") or 0
            if band != "unsure":
                low, high = BAND_STEPS[band]
                # The band and the step count must agree, OR the agent must have named the factor
                # that overrides the count and said so. Without this the step count becomes
                # decoration, and the band goes back to being a feeling with a number beside it.
                if not low <= steps <= high:
                    if not (data.get("what_makes_it_hard") and data.get("note")):
                        failed.append(
                            (item_id, "band %s with steps_to_solve=%d (expected %d-%d), and no "
                                      "what_makes_it_hard + note explaining the override"
                             % (band, steps, low, high)))
                        continue
                    tally["count overridden, explained"] += 1
                if not (data.get("steps") or []):
                    failed.append((item_id, "no `steps` listed: a band with no countable steps "
                                            "behind it cannot be reviewed"))
                    continue
            # SPEC E7: where the blind solve failed or hedged and the rater said easy, or the solve
            # was confident and the rater said hard, the question is contested -- flagged for a
            # person rather than either side being believed.
            solve = rc.pp("steps", "B6V", "out", "%s.runA.json" % item_id.replace("#", "__"))
            if os.path.exists(solve):
                try:
                    solved = json.load(open(solve, encoding="utf-8"))
                except ValueError:
                    solved = {}
                if solved.get("answer") == "unsure" and band == "easy":
                    tally["E7_DIFFICULTY_CONTESTED"] += 1
                elif solved.get("confidence") == "high" and band == "hard":
                    tally["E7_DIFFICULTY_CONTESTED"] += 1
            passed += 1
        for item_id, message in failed:
            print("E7V %-22s FAIL  %s" % (item_id, message), file=sys.stderr)
        total = len(self._questions(filters))
        print("E7V --check: %d passed, %d failed, %d without output (of %d)"
              % (passed, len(failed), total - passed - len(failed), total), file=sys.stderr)
        if tally:
            print("E7V %s" % dict(tally), file=sys.stderr)
        return []
