"""B3F's step plugin: one item per FIGURE crop in the v2 paper corpus.

Kept in its own module and wired in from `get_plugins()`, like ECAT, because it shares none of the
B1-B10 helpers: its items are not derived per question from `papers/records/` but read from the v2
corpus that `scripts/extract_paper_v2.py` writes.

WHY THE ITEM IS A FIGURE AND NOT A QUESTION. A question can carry a stem diagram and a block of
option panels at once, and they are different objects with different downstream jobs -- the stem
diagram is content the question cannot be read without, the option panels are the options themselves
and their order is booklet-code specific (SPEC Rule 16). One item per question would force one
verdict over both.
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
WORK = ("steps", "B3F", "work")
OUT = ("steps", "B3F", "out")


class B3FPlugin:
    step = "B3F"
    agent = "b3f-figure-transcriber"

    def _figures(self, filters=None):
        """{item_id: (paper_id, qno, figure dict)} for every figure crop in the v2 corpus."""
        wanted = set((filters or {}).get("items") or [])
        papers = (filters or {}).get("papers") or None
        out = {}
        for path in sorted(glob.glob(rc.pp(*CORPUS, "papers", "*.json"))):
            with open(path, encoding="utf-8") as fh:
                paper = json.load(fh)
            meta = paper["meta"]
            paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
            if papers and paper_id not in papers:
                continue
            for question in paper["questions"]:
                for n, figure in enumerate(question["figures"], 1):
                    if not figure.get("image"):
                        continue
                    item_id = "%s#q%03d_%s_%d" % (paper_id, question["qno"], figure["role"], n)
                    if wanted and item_id not in wanted:
                        continue
                    out[item_id] = (paper_id, question["qno"], figure)
        return out

    def _out_path(self, item_id):
        return rc.pp(*OUT, "%s.runA.json" % item_id.replace("#", "__"))

    def _input_path(self, item_id, run_label="runA"):
        return rc.pp(*WORK, "%s.%s.input.json" % (item_id.replace("#", "__"), run_label))

    def list_items(self, filters):
        lines = []
        for item_id, (paper_id, qno, figure) in self._figures(filters).items():
            if os.path.exists(self._out_path(item_id)):
                continue
            image = rc.pp(*CORPUS, figure["image"])
            payload = {
                "paper_id": paper_id,
                "qno": qno,
                "role": figure["role"],
                "image": os.path.relpath(image, rc.pp()),
                "target_box_in_crop": figure["target_box_in_crop"],
                # The text the PDF holds inside the crop. Exact for prose and unreliable for exactly
                # the characters a figure label is made of, which is why the agent is told the image
                # wins where the two differ (SPEC Rule 28).
                "text_layer": None,
            }
            path = self._input_path(item_id)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, ensure_ascii=False, indent=1)
            lines.append(ListLine(item_id, self.agent, os.path.relpath(path, rc.pp()),
                                  os.path.relpath(self._out_path(item_id), rc.pp()), "runA"))
        return lines

    def list_reason(self):
        figures = self._figures()
        if not figures:
            return ("B3F has no figures to transcribe. Build the v2 corpus first: "
                    "`python3 scripts/extract_paper_v2.py --year 2024 --apply`.")
        done = sum(1 for i in figures if os.path.exists(self._out_path(i)))
        return ("B3F: all %d figure crop(s) already have output. Run `run_step.py B3F --check`."
                % done)

    def check(self, filters):
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
        import B3F as b3f_check
        import jsonschema

        schema = json.load(open(rc.pp("schemas", "B3F.json"), encoding="utf-8"))
        failed, passed = [], 0
        tally = collections.Counter()
        for item_id, (paper_id, qno, _figure) in self._figures(filters).items():
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
            ok, message = b3f_check.check(data, item={"paper_id": paper_id, "qno": qno})
            if ok:
                passed += 1
                tally[data.get("kind")] += 1
                if data.get("complete") is False:
                    tally["CLIPPED"] += 1
                print("B3F %-34s PASS  %s" % (item_id, message), file=sys.stderr)
            else:
                failed.append((item_id, message))

        for item_id, message in failed:
            print("B3F %-34s FAIL  %s" % (item_id, message), file=sys.stderr)
        total = len(self._figures(filters))
        print("B3F --check: %d passed, %d failed, %d crop(s) without output (of %d)"
              % (passed, len(failed), total - passed - len(failed), total), file=sys.stderr)
        if tally:
            print("B3F kinds: %s" % dict(tally), file=sys.stderr)
        if tally.get("CLIPPED"):
            print("B3F: %d crop(s) reported CLIPPED -- the geometry in "
                  "scripts/extract_paper_v2.py wants widening for those, which is the finding, not "
                  "a failure of the agent." % tally["CLIPPED"], file=sys.stderr)
        if tally.get("not_a_figure"):
            print("B3F: %d crop(s) are NOT figures -- the band detector emitted text, a watermark "
                  "or furniture. Fix the detector rather than transcribing around it."
                  % tally["not_a_figure"], file=sys.stderr)

        lines = []
        for item_id, message in failed:
            path = self._input_path(item_id, "retry1")
            payload = json.load(open(self._input_path(item_id), encoding="utf-8"))
            payload["PREVIOUS ATTEMPT FAILED"] = message
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, ensure_ascii=False, indent=1)
            lines.append(ListLine(item_id, self.agent, os.path.relpath(path, rc.pp()),
                                  os.path.relpath(self._out_path(item_id), rc.pp()), "retry1"))
        return lines
