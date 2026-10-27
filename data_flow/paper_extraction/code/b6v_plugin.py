"""B6V's step plugin: solve ONE v2 question WITHOUT seeing any answer key.

WHY AN INDEPENDENT SOLVE IS THE THIRD COLUMN
---------------------------------------------
Three things can tell us a question's answer and they fail differently:

  booklet   the publisher's `Solution: (3)`. Publishers get questions wrong.
  official  NTA's own final key, per booklet code. The authority -- but it is joined in from a
            separate file, and a wrong join is SILENT.
  solved    this step. Having seen neither, it catches a bad join AND the case where the first two
            agree and are both wrong.

Kept in three columns rather than collapsed: agreement is evidence, and a disagreement is a question
worth a person's time. The v1 corpus had only the publisher's answer and could not tell a
publisher's error from a scrape error.

THE KEY IS WITHHELD BY CONSTRUCTION. CLAUDE.md: "Never pass ... answer keys to agents that must not
see them (B6 never sees the key)." The input built here carries the stem, the options and the figure
and nothing else -- no `official_answer`, no `answer_booklet`, no solution text. A solver that has
seen the answer is not evidence about the answer.
"""

import collections
import glob
import json
import os
import sys

import runner_core as rc

ListLine = collections.namedtuple(
    "ListLine", ["item_id", "agent", "input_path", "output_path", "run_label"])

CORPUS = rc.corpus()
B3V_OUT = ("steps", "B3V", "out")
WORK = ("steps", "B6V", "work")
OUT = ("steps", "B6V", "out")


class B6VPlugin:
    step = "B6V"
    agent = "b6-blind-solver"

    def _questions(self, filters=None):
        """{item_id: (paper_id, question, agent_read)} for questions B3V has already read.

        Only questions B3V has read are offered. Solving from the text draft would mean solving a
        question whose fractions are mangled -- the solver would be answering a different question
        from the one printed, and its disagreement would say nothing about the key.
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
                read_path = rc.pp(*B3V_OUT, "%s__q%03d.runA.json"
                                  % (paper_id, question["qno"]))
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

    def _out_path(self, item_id):
        return rc.pp(*OUT, "%s.runA.json" % item_id.replace("#", "__"))

    def _input_path(self, item_id, run_label="runA"):
        return rc.pp(*WORK, "%s.%s.input.json" % (item_id.replace("#", "__"), run_label))

    def list_items(self, filters):
        lines = []
        for item_id, (paper_id, question, read) in self._questions(filters).items():
            if os.path.exists(self._out_path(item_id)):
                continue
            # The geometric crop is a fallback ONLY where the image read says there IS a figure. On
            # 2017 Code-A it handed the solver of q58, q67 and q81 a drawing from a neighbouring
            # question, because B3V had found no figure and the geometric pass had guessed one.
            figure = (question.get("agent_figure_images")
                      or (question.get("figure_images") if read.get("has_figure") else None)
                      or [None])[0]
            # EXACTLY the fields b6-blind-solver's own Input block names, and nothing else. Adding a
            # field here is how a key leaks to a solver that must not see one.
            payload = {
                "stem_en": read.get("stem_en"),
                "statements": read.get("statements") or [],
                "list_i": read.get("list_i") or [],
                "list_ii": read.get("list_ii") or [],
                "options_en": read.get("options_en") or {},
                "figure_image": (os.path.relpath(rc.pp(*CORPUS, figure), rc.pp())
                                 if figure else None),
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
            return ("B6V has nothing to solve: it only offers questions B3V has already read, and "
                    "none have been. Run B3V first -- solving a mangled text draft would answer a "
                    "different question from the one printed.")
        done = sum(1 for i in questions if os.path.exists(self._out_path(i)))
        return "B6V: all %d solvable question(s) already answered." % done

    def check(self, filters):
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
        import jsonschema

        schema_path = rc.pp("schemas", "B6.json")
        schema = json.load(open(schema_path, encoding="utf-8")) if os.path.exists(schema_path) else None
        tally = collections.Counter()
        failed, passed = [], 0
        for item_id, (paper_id, question, _read) in self._questions(filters).items():
            out_path = self._out_path(item_id)
            if not os.path.exists(out_path):
                continue
            try:
                data = json.load(open(out_path, encoding="utf-8"))
            except ValueError as exc:
                failed.append((item_id, "output is not valid JSON: %s" % exc))
                continue
            if schema:
                try:
                    jsonschema.validate(data, schema)
                except jsonschema.ValidationError as exc:
                    failed.append((item_id, "schema: %s" % exc.message))
                    continue
            passed += 1
            solved = data.get("answer")
            booklet = (question.get("text_layer_draft") or {}).get("official_answer")
            tally["solved"] += 1
            if solved == "unsure":
                tally["unsure"] += 1
            elif booklet and solved and solved != booklet:
                tally["DISAGREES WITH BOOKLET"] += 1
                print("B6V %-22s solved %s, booklet says %s -- %s"
                      % (item_id, solved, booklet, (data.get("why") or "")[:70]), file=sys.stderr)
            elif booklet and solved == booklet:
                tally["agrees with booklet"] += 1

        for item_id, message in failed:
            print("B6V %-22s FAIL  %s" % (item_id, message), file=sys.stderr)
        total = len(self._questions(filters))
        print("B6V --check: %d solved, %d failed, %d unsolved (of %d solvable)"
              % (passed, len(failed), total - passed - len(failed), total), file=sys.stderr)
        if tally:
            print("B6V %s" % dict(tally), file=sys.stderr)
        print("A disagreement is a FINDING, not a failure: it is a question where the publisher, "
              "NTA and an independent solve do not all say the same thing.", file=sys.stderr)

        lines = []
        for item_id, message in failed:
            payload = json.load(open(self._input_path(item_id), encoding="utf-8"))
            payload["PREVIOUS ATTEMPT FAILED"] = message
            path = self._input_path(item_id, "retry1")
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, ensure_ascii=False, indent=1)
            lines.append(ListLine(item_id, self.agent, os.path.relpath(path, rc.pp()),
                                  os.path.relpath(self._out_path(item_id), rc.pp()), "retry1"))
        return lines
