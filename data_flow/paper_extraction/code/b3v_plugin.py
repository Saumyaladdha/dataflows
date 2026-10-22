"""B3V's step plugin: read ONE question from its IMAGE, over the v2 paper corpus.

WHY THIS STEP EXISTS, AND WHY IT IS THE MAIN ONE
------------------------------------------------
Stage A reads NCERT by rendering each page and having `a2-page-reader` read the IMAGE, with the text
layer as a cross-check only. That extraction is sound. The v2 paper extractor was built the other way
round -- the text layer as the product, the image as an afterthought -- and the result is wrong on
every question whose content is not linear text:

    printed   (1) 4/9   (2) 9/4   (3) 121/49   (4) 49/121        (2015 Code-A q170)
    text      (1) 9 9   (2) 4 121 (3) 49 49    (4) 121

    printed   300 cos(15t + 4pi/3)                                (2015 Code-A q173)
    text      pi 300 cos (15t + 3)

A stacked fraction is three unrelated objects -- numerator, drawn bar, denominator -- on different
rows. There is no parse that recovers it, and the same is true of a radical, a matrix, a drawn
structure and a two-line subscript. Measured across the corpus, 30-45% of questions per booklet carry
at least one of these (`needs_image_read`).

So this step does what Stage A does: the agent reads the question's own crop. The text draft is
passed alongside ONLY as a cross-check, exactly as `a2-page-reader` receives `text_layer`, and the
agent is told the image wins where they differ.

ITEM = ONE QUESTION, matching config/steps.yaml B3's own `item: question`.
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
WORK = ("steps", "B3V", "work")
OUT = ("steps", "B3V", "out")


class B3VPlugin:
    step = "B3V"
    agent = "b3-question-reader"

    def _questions(self, filters=None):
        """{item_id: (paper, question)} for every question in the v2 corpus."""
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
                out[item_id] = (meta, question)
        return out

    def _out_path(self, item_id):
        return rc.pp(*OUT, "%s.runA.json" % item_id.replace("#", "__"))

    def _input_path(self, item_id, run_label="runA"):
        return rc.pp(*WORK, "%s.%s.input.json" % (item_id.replace("#", "__"), run_label))

    def list_items(self, filters):
        lines = []
        for item_id, (meta, question) in self._questions(filters).items():
            if os.path.exists(self._out_path(item_id)):
                continue
            image = rc.pp(*CORPUS, question["question_image"])
            if not os.path.exists(image):
                continue
            draft = question["text_layer_draft"]
            payload = {
                "paper_id": question["paper_id"],
                "qno": question["qno"],
                "question_image": os.path.relpath(image, rc.pp()),
                # Cross-check only, never the answer -- the same role `text_layer` plays for
                # a2-page-reader. Where the two differ the IMAGE is right, and these fields say so.
                "text_layer_draft": {
                    "stem": draft.get("stem"),
                    "options": draft.get("options"),
                    "official_answer": draft.get("official_answer"),
                },
                "text_layer_reliable": question.get("text_layer_reliable", True),
                "needs_image_read": question.get("needs_image_read", False),
                "needs_image_read_why": question.get("needs_image_read_why", []),
                "figure_images": [os.path.relpath(rc.pp(*CORPUS, f), rc.pp())
                                  for f in (question.get("figure_images") or [])],
                "source_pdf": question.get("source_pdf"),
                "page": question.get("page"),
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
            return ("B3V has nothing to read. Build the v2 corpus first: "
                    "`python3 scripts/extract_paper_v2.py --year 2024 --apply`.")
        done = sum(1 for i in questions if os.path.exists(self._out_path(i)))
        return ("B3V: all %d question(s) already read. Run `run_step.py B3V --check`." % done)

    def check(self, filters):
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
        import jsonschema

        schema = json.load(open(rc.pp("schemas", "B3.json"), encoding="utf-8"))
        failed, passed = [], 0
        tally = collections.Counter()
        for item_id, (_meta, question) in self._questions(filters).items():
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
            problems = self._agree(data, question)
            if problems:
                tally["differs_from_draft"] += 1
            if data.get("has_figure"):
                tally["has_figure"] += 1
            passed += 1
            print("B3V %-22s PASS  %s" % (item_id, "; ".join(problems) or "agrees with the draft"),
                  file=sys.stderr)

        for item_id, message in failed:
            print("B3V %-22s FAIL  %s" % (item_id, message), file=sys.stderr)
        total = len(self._questions(filters))
        print("B3V --check: %d read, %d failed, %d still unread (of %d)"
              % (passed, len(failed), total - passed - len(failed), total), file=sys.stderr)
        if tally:
            print("B3V %s" % dict(tally), file=sys.stderr)

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

    @staticmethod
    def _agree(data, question):
        """Where the agent's read differs from the text draft -- REPORTED, never failed.

        A difference is the expected outcome on any question the draft could not represent, and on
        those the agent is right by construction. Reporting it is how a reader sees which questions
        the text layer was wrong about; failing it would be failing the agent for doing its job.
        """
        draft = question["text_layer_draft"]
        notes = []
        agent_options = data.get("options_en") or {}
        draft_options = draft.get("options") or {}
        differing = [k for k in "1234"
                     if (agent_options.get(k) or "").strip() != (draft_options.get(k) or "").strip()]
        if differing:
            notes.append("options %s differ from the draft" % ",".join(differing))
        filled = sum(1 for k in "1234" if (agent_options.get(k) or "").strip())
        if filled == 4 and sum(1 for v in draft_options.values() if v.strip()) < 4:
            notes.append("agent recovered a complete option set the draft could not")
        return notes
