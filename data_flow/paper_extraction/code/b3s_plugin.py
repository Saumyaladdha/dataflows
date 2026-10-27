"""B3S's step plugin: read ONE question's printed worked solution from its IMAGE, over the v2 corpus.

WHY THIS STEP EXISTS
--------------------
The booklets print a worked solution under most questions, and until this step every line of it was
thrown away by the extractor. Keeping the lines is not enough: a worked solution is nothing but
fractions, radicals and exponents, the content a text layer cannot represent -- 2015 Code-A q170's
options 4/9, 9/4, 121/49, 49/121 come out of the text layer as "9 9", "4 121", "49 49", "121", and a
solution is that problem on every line. So `text_layer_draft.solution_lines` is a draft and a
cross-check, exactly as `text_layer_draft.stem` is for B3V, and this step reads the solution crop.

It mirrors B3V in shape: ITEM = ONE QUESTION, input written by --list, output checked by --check,
a failed check re-listed as `retry1` with the message.

WHAT IT CATCHES THAT NOTHING ELSE DOES
--------------------------------------
`concludes` is the option the WORKING lands on. Compared with the booklet's printed `Answer (N)`, it
finds a defect class nothing in the pipeline could see before: a booklet printing `Answer (3)` above
a solution that works out to 1. Raised as B3S_CONTRADICTS_PRINTED_ANSWER (high) -- a FINDING, never a
check failure, because the agent is right to report what the working says.

ONLY QUESTIONS B3V HAS READ ARE OFFERED (`needs: B3V`). The question text handed to the agent is the
one it uses to say which option the working lands on; handing it a mangled text-layer stem would make
`concludes` an answer about a different question.
"""

import collections
import glob
import json
import os
import sys

import runner_core as rc
from lib import flags as lib_flags

ListLine = collections.namedtuple(
    "ListLine", ["item_id", "agent", "input_path", "output_path", "run_label"])

CORPUS = rc.corpus()
B3V_OUT = ("steps", "B3V", "out")
WORK = ("steps", "B3S", "work")
OUT = ("steps", "B3S", "out")


class B3SPlugin:
    step = "B3S"
    agent = "b3s-solution-reader"

    def _questions(self, filters=None):
        """{item_id: (paper_id, question, b3v_read)} for every question with a solution crop on
        disk and a B3V read."""
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
                image = question.get("solution_image")
                if not image or not os.path.exists(rc.pp(*CORPUS, image)):
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

    def _out_path(self, item_id):
        return rc.pp(*OUT, "%s.runA.json" % item_id.replace("#", "__"))

    def _input_path(self, item_id, run_label="runA"):
        return rc.pp(*WORK, "%s.%s.input.json" % (item_id.replace("#", "__"), run_label))

    def _payload(self, paper_id, question, read):
        draft = question.get("text_layer_draft") or {}
        # The printed answer is deliberately NOT here. The agent reports what the working arrives
        # at; told the printed answer, it would read the working toward it, and the one disagreement
        # this step exists to find would stop being found.
        return {
            "paper_id": paper_id,
            "qno": question["qno"],
            "solution_image": os.path.relpath(rc.pp(*CORPUS, question["solution_image"]), rc.pp()),
            "solution_lines_draft": draft.get("solution_lines") or [],
            "question_text": read.get("stem_en") or "",
            # The question's statements and match lists ARE part of its text. Without them the agent
            # cannot say which option a working lands on for "which of (a)-(d) are correct" or a
            # Column I/II match: on 2017 Code-A q98, q109, q137 and q152 it had to answer `unclear`
            # because the stem it was handed ended at "Select the correct option".
            "statements": read.get("statements") or [],
            "list_i": read.get("list_i") or [],
            "list_ii": read.get("list_ii") or [],
            "options": read.get("options_en") or {},
        }

    def list_items(self, filters):
        lines = []
        for item_id, (paper_id, question, read) in self._questions(filters).items():
            if os.path.exists(self._out_path(item_id)):
                continue
            path = self._input_path(item_id)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(self._payload(paper_id, question, read), fh, ensure_ascii=False, indent=1)
            lines.append(ListLine(item_id, self.agent, os.path.relpath(path, rc.pp()),
                                  os.path.relpath(self._out_path(item_id), rc.pp()), "runA"))
        return lines

    def list_reason(self):
        questions = self._questions()
        if not questions:
            return ("B3S has nothing to read: it needs a solution crop (code/extract_paper_v2.py "
                    "--apply cuts them) AND a B3V read of the question (run_step.py B3V first).")
        done = sum(1 for i in questions if os.path.exists(self._out_path(i)))
        return "B3S: all %d solution(s) already read. Run `run_step.py B3S --check`." % done

    def check(self, filters):
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
        import jsonschema
        import B3S as b3s_check

        schema = json.load(open(rc.pp("schemas", "B3S.json"), encoding="utf-8"))
        failed, passed = [], 0
        tally = collections.Counter()
        for item_id, (paper_id, question, read) in self._questions(filters).items():
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
            ok, message = b3s_check.check(data, item=self._payload(paper_id, question, read))
            if not ok:
                failed.append((item_id, message))
                continue
            passed += 1
            if "error" not in data:
                for code in self._raise_flags(item_id, data, question):
                    tally[code] += 1
            print("B3S %-22s PASS  %s" % (item_id, message), file=sys.stderr)

        for item_id, message in failed:
            print("B3S %-22s FAIL  %s" % (item_id, message), file=sys.stderr)
        total = len(self._questions(filters))
        print("B3S --check: %d read, %d failed, %d still unread (of %d)"
              % (passed, len(failed), total - passed - len(failed), total), file=sys.stderr)
        if tally:
            print("B3S flags %s" % dict(tally), file=sys.stderr)

        lines = []
        for item_id, message in failed:
            source = self._input_path(item_id)
            if os.path.exists(source):
                with open(source, encoding="utf-8") as fh:
                    payload = json.load(fh)
            else:
                paper_id, question, read = self._questions({"items": [item_id]})[item_id]
                payload = self._payload(paper_id, question, read)
            payload["PREVIOUS ATTEMPT FAILED"] = message
            path = self._input_path(item_id, "retry1")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, ensure_ascii=False, indent=1)
            lines.append(ListLine(item_id, self.agent, os.path.relpath(path, rc.pp()),
                                  os.path.relpath(self._out_path(item_id), rc.pp()), "retry1"))
        return lines

    def _raise_flags(self, item_id, data, question):
        """The three findings steps.yaml declares for B3S. Idempotent: lib.flags never re-raises an
        open flag for the same (item, step, code)."""
        raised = []
        printed = (question.get("text_layer_draft") or {}).get("official_answer")
        concludes = data.get("concludes")
        if data.get("complete") is False:
            lib_flags.raise_flag("question", item_id, self.step, "B3S_SOLUTION_CLIPPED", "normal",
                                 "the printed solution is cut off in its crop: %s"
                                 % (data.get("note") or "no note"))
            raised.append("B3S_SOLUTION_CLIPPED")
        if concludes == "unclear":
            lib_flags.raise_flag("question", item_id, self.step, "B3S_CONCLUDES_UNCLEAR", "low",
                                 "the printed working does not clearly land on an option: %s"
                                 % (data.get("note") or "no note"))
            raised.append("B3S_CONCLUDES_UNCLEAR")
        elif printed and concludes and concludes != printed:
            lib_flags.raise_flag("question", item_id, self.step, "B3S_CONTRADICTS_PRINTED_ANSWER",
                                 "high",
                                 "the booklet prints Answer (%s) but its own worked solution "
                                 "arrives at option %s" % (printed, concludes),
                                 provisional_value=printed,
                                 evidence={"printed_answer": printed, "working_concludes": concludes})
            raised.append("B3S_CONTRADICTS_PRINTED_ANSWER")
        return raised
