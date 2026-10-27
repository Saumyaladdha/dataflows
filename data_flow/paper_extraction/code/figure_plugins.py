"""FIGC and FIGP: the agent steps that turn a printed figure into a CHECKED card a renderer draws.

    FIGC   one CHEMISTRY question  -> SMILES cards for its question, option and solution drawings
    FIGP   one PHYSICS figure      -> a figure spec of primitives (render_figure's vocabulary)

The agent never draws; it writes a card, code checks the card, and the renderer draws it
(docs FIGURE_RENDERING_PLAN.md). The exact vector copy of the printed figure (vector_figures.py) stays
beside every drawing, because a self-consistent card can still be the wrong figure and only a reader
comparing the two catches that.

WHICH FIGURES. Every figure the pipeline has CUT for a question -- the agent's question figure,
per-option drawings, and the solution's drawings at their steps -- is offered, scoped by the
CONFIRMED subject (QSUBJ or a printed heading), never by a positional guess. A figure is identified
by a stable `figure_id`: `question`, `option_<k>`, `solution_<n>`.
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


def confirmed_subject(paper_id, question):
    """QSUBJ's subject, else a printed heading's; None when only a positional guess exists."""
    path = rc.pp("steps", "QSUBJ", "out", "%s__q%03d.runA.json" % (paper_id, question["qno"]))
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            subject = json.load(fh).get("subject")
        if subject and subject != "unsure":
            return subject
    if "printed heading" in (question.get("subject_from") or ""):
        return question.get("subject")
    return None


def figures_of(question):
    """[{figure_id, image, role, page, bbox}] for every figure cut for this question, PNG paths
    corpus-relative, `page`/`bbox` the region on the booklet page it was cut from (pixels)."""
    out = []
    boxes = question.get("agent_figure_boxes") or []
    for n, image in enumerate(question.get("agent_figure_images") or []):
        box = boxes[n] if n < len(boxes) else {}
        out.append({"figure_id": "question", "image": image, "role": "the question's figure",
                    "page": box.get("page"), "bbox": box.get("bbox")})
    option_boxes = question.get("agent_option_boxes") or {}
    for key, image in sorted((question.get("agent_option_images") or {}).items()):
        box = option_boxes.get(key) or {}
        out.append({"figure_id": "option_%s" % key, "image": image,
                    "role": "the drawing printed as option (%s)" % key,
                    "page": box.get("page"), "bbox": box.get("bbox")})
    for n, figure in enumerate(question.get("solution_figures") or [], 1):
        out.append({"figure_id": "solution_%d" % n, "image": figure["image"],
                    "role": "a drawing in the printed solution, after step %d"
                            % figure.get("after_step", 0),
                    "page": figure.get("page"), "bbox": figure.get("bbox")})
    return out


_SOURCES = {}
_TRACES = {}


def _source(source_pdf):
    import pymupdf
    import extract_paper_v2 as extractor
    source = os.path.join(os.path.dirname(extractor.SOURCE_ROOT), source_pdf)
    if source not in _SOURCES:
        _SOURCES[source] = pymupdf.open(source)
    return _SOURCES[source]


def trace_of(source_pdf, dpi, page, bbox, keep_words=()):
    """The figure as the booklet's vector drawing has it (lib/print_trace), or None without a box.

    Every FIGC card is checked against it (each SMILES must BE a printed molecule, atom for atom)
    and drawn on it, so our drawing has the booklet's layout instead of RDKit's."""
    if page is None or not bbox:
        return None
    key = (source_pdf, page, tuple(bbox), frozenset(keep_words))
    if key not in _TRACES:
        from lib import print_trace
        scale = 72.0 / dpi
        _TRACES[key] = print_trace.read(_source(source_pdf)[page], [v * scale for v in bbox],
                                        keep_words)
    return _TRACES[key]


def spec_words(spec):
    """The words a physics spec's labels print, for trace_of(keep_words=...)."""
    out = set()
    for item in (spec or {}).get("draw") or []:
        if item.get("kind") == "label":
            out |= set(((item.get("text") or "") + (item.get("sub") or "")
                        + (item.get("sup") or "")).split())
    return frozenset(out)


def physics_trace(item_or_paper, figure, spec):
    """(trace, problems) for a physics figure that is a vector drawing, else (None, [])."""
    from lib import print_trace, spec_trace
    source = item_or_paper.get("source_pdf") or item_or_paper["meta"]["source_pdf"]
    dpi = item_or_paper.get("dpi") or item_or_paper["meta"]["dpi"]
    trace = trace_of(source, dpi, figure.get("page"), figure.get("bbox"), spec_words(spec))
    if trace is None or len(trace.subpaths) < 3:
        return None, []
    return trace, spec_trace.problems(spec, trace)


def printed_text(paper, figure):
    """The words printed inside this figure on the booklet page (lib/figure_text), or None when
    the figure has no page box. Given to the agent as `printed_text`, and to the check, which fails
    a card that neither draws nor excludes one of them."""
    if figure.get("page") is None or not figure.get("bbox"):
        return None
    from lib import figure_text
    return figure_text.printed_text(_source(paper["meta"]["source_pdf"]), figure["page"],
                                    figure["bbox"], paper["meta"]["dpi"])


def _root(path):
    return os.path.relpath(rc.pp(*CORPUS, path), rc.pp())


def _papers(filters):
    papers = set((filters or {}).get("papers") or [])
    for path in sorted(glob.glob(rc.pp(*CORPUS, "papers", "*.json"))):
        with open(path, encoding="utf-8") as fh:
            paper = json.load(fh)
        meta = paper["meta"]
        paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
        if papers and paper_id not in papers:
            continue
        yield paper_id, paper


def _b3v(paper_id, qno):
    path = rc.pp("steps", "B3V", "out", "%s__q%03d.runA.json" % (paper_id, qno))
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        read = json.load(fh)
    return None if "error" in read else read


class _FigureStep:
    """Shared list/check machinery; subclasses say which items exist and what each input holds."""
    step = agent = check_module = None

    def items(self, filters=None):
        raise NotImplementedError

    def _out(self, item_id):
        return rc.pp("steps", self.step, "out", "%s.runA.json" % item_id.replace("#", "__"))

    def _in(self, item_id, run_label="runA"):
        return rc.pp("steps", self.step, "work",
                     "%s.%s.input.json" % (item_id.replace("#", "__"), run_label))

    def list_items(self, filters):
        wanted = set((filters or {}).get("items") or [])
        lines = []
        for item_id, payload in self.items(filters).items():
            if (wanted and item_id not in wanted) or os.path.exists(self._out(item_id)):
                continue
            path = self._in(item_id)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, ensure_ascii=False, indent=1)
            lines.append(ListLine(item_id, self.agent, os.path.relpath(path, rc.pp()),
                                  os.path.relpath(self._out(item_id), rc.pp()), "runA"))
        return lines

    def list_reason(self):
        items = self.items()
        if not items:
            return ("%s has nothing to do: it needs cut figures (cut_agent_figures.py) and a "
                    "confirmed subject (QSUBJ)." % self.step)
        done = sum(1 for i in items if os.path.exists(self._out(i)))
        return "%s: %d of %d done. Run `run_step.py %s --check`." % (self.step, done, len(items),
                                                                     self.step)

    def check(self, filters):
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
        import importlib
        import jsonschema
        module = importlib.import_module(self.check_module)
        schema = json.load(open(rc.pp("schemas", "%s.json" % self.step), encoding="utf-8"))
        failed, passed = [], 0
        items = self.items(filters)
        for item_id, payload in items.items():
            out = self._out(item_id)
            if not os.path.exists(out):
                continue
            try:
                data = json.load(open(out, encoding="utf-8"))
                jsonschema.validate(data, schema)
            except (ValueError, jsonschema.ValidationError) as exc:
                failed.append((item_id, payload, "schema: %s" % getattr(exc, "message", exc)))
                continue
            ok, message = module.check(data, item=payload)
            if not ok:
                failed.append((item_id, payload, message))
                continue
            passed += 1
            print("%s %-30s PASS  %s" % (self.step, item_id, message), file=sys.stderr)
        for item_id, _payload, message in failed:
            print("%s %-30s FAIL  %s" % (self.step, item_id, message), file=sys.stderr)
        print("%s --check: %d passed, %d failed, %d not yet run (of %d)"
              % (self.step, passed, len(failed), len(items) - passed - len(failed), len(items)),
              file=sys.stderr)
        lines = []
        for item_id, payload, message in failed:
            # The earlier answer travels with the failure, so a retry FIXES it (adds a missing
            # `text`, corrects one name) instead of re-reading every structure from scratch.
            retry = dict(payload, **{"PREVIOUS ATTEMPT FAILED": message})
            try:
                with open(self._out(item_id), encoding="utf-8") as fh:
                    retry["PREVIOUS OUTPUT"] = json.load(fh)
            except (OSError, ValueError):
                pass
            path = self._in(item_id, "retry1")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(retry, fh, ensure_ascii=False, indent=1)
            lines.append(ListLine(item_id, self.agent, os.path.relpath(path, rc.pp()),
                                  os.path.relpath(self._out(item_id), rc.pp()), "retry1"))
        return lines


class FIGCPlugin(_FigureStep):
    """One CHEMISTRY question with at least one cut figure -> SMILES cards for all its drawings."""
    step, agent, check_module = "FIGC", "figc-structure-reader", "FIGC"

    def items(self, filters=None):
        out = {}
        for paper_id, paper in _papers(filters):
            for question in paper["questions"]:
                figures = figures_of(question)
                read = _b3v(paper_id, question["qno"])
                if not figures or read is None:
                    continue
                if confirmed_subject(paper_id, question) != "Chemistry":
                    continue
                out["%s#q%03d" % (paper_id, question["qno"])] = {
                    "paper_id": paper_id, "qno": question["qno"], "subject": "Chemistry",
                    "question_text": read.get("stem_en") or "", "options": read.get("options_en") or {},
                    "figures": [{"figure_id": f["figure_id"], "image": _root(f["image"]),
                                 "role": f["role"], "printed_text": printed_text(paper, f),
                                 # where it sits on the page, for the check against the print
                                 "page": f.get("page"), "bbox": f.get("bbox")}
                                for f in figures],
                    "source_pdf": paper["meta"]["source_pdf"], "dpi": paper["meta"]["dpi"]}
        return out


class FIGPPlugin(_FigureStep):
    """One PHYSICS figure -> a figure spec. Item = one figure, because a spec is one drawing."""
    step, agent, check_module = "FIGP", "figp-figure-redrawer", "FIGP"

    def items(self, filters=None):
        out = {}
        for paper_id, paper in _papers(filters):
            for question in paper["questions"]:
                read = _b3v(paper_id, question["qno"])
                if read is None or confirmed_subject(paper_id, question) != "Physics":
                    continue
                for figure in figures_of(question):
                    item_id = "%s#q%03d_%s" % (paper_id, question["qno"], figure["figure_id"])
                    out[item_id] = {"paper_id": paper_id, "qno": question["qno"],
                                    "figure_id": figure["figure_id"], "role": figure["role"],
                                    "image": _root(figure["image"]),
                                    "printed_text": printed_text(paper, figure),
                                    # where it sits on the page, for the check against the print
                                    "page": figure.get("page"), "bbox": figure.get("bbox"),
                                    "source_pdf": paper["meta"]["source_pdf"],
                                    "dpi": paper["meta"]["dpi"],
                                    "question_text": read.get("stem_en") or "",
                                    "options": read.get("options_en") or {}}
        return out
