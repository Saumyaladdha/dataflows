#!/usr/bin/env python3
"""The physics-figure machinery of paper_extraction, run for an NCERT chapter figure.

    python code/figp_bridge.py probe <pdf> <page_index> '<bbox_frac json>'
    python code/figp_bridge.py check <input.json> <output.json> <svg_out>

We draw physics figures ourselves the same way for NEET papers and NCERT chapters: an agent
writes a SPEC of primitives (agents/figp-figure-redrawer.md), and code -- never the agent --
checks and draws it. That code lives in `paper_extraction/code/lib`:

  physics_figure  the renderer, and check_spec (renders; claimed angles recompute; netlist matches)
  figure_text     every word printed inside the figure box is drawn or excluded with a reason
  print_trace     the PDF's own vector drawing of the figure, glyphs and strokes
  spec_trace      the spec's labels are printed there and its lines lie on the printed ink

It is imported read-only from there, never copied: one renderer, one set of checks. Both
pipelines call their package `lib`, so this runs as its own process with paper_extraction/code
first on the path and the NCERT code dir removed. Prints one JSON object on its last line.

The NCERT watermark is stripped first (pdf_watermark.strip): its glyphs would otherwise enter
the trace as printed words the spec "dropped".
"""

import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER_CODE = os.path.join(os.path.dirname(os.path.dirname(HERE)), "paper_extraction", "code")
sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != HERE]
sys.path.insert(0, PAPER_CODE)

_spec = importlib.util.spec_from_file_location("ncert_pdf_watermark", os.path.join(HERE, "pdf_watermark.py"))
pdf_watermark = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pdf_watermark)

ROOT = os.path.dirname(HERE)


def _page(pdf, page_index):
    import pymupdf
    doc = pymupdf.open(pdf if os.path.isabs(pdf) else os.path.join(ROOT, pdf))
    pdf_watermark.strip(doc)
    return doc, doc[int(page_index)]


def _rect(page, bbox_frac):
    w, h = page.rect.width, page.rect.height
    x0, y0, x1, y1 = bbox_frac
    return [x0 * w, y0 * h, x1 * w, y1 * h]


def probe(pdf, page_index, bbox_frac):
    """How many vector strokes the figure box holds, and the words printed inside it."""
    import pymupdf
    from lib import figure_text
    doc, page = _page(pdf, page_index)
    rect = pymupdf.Rect(_rect(page, bbox_frac))
    strokes = sum(1 for d in page.get_drawings() if pymupdf.Rect(d["rect"]).intersects(rect))
    text = figure_text.printed_text(doc, page.number, list(rect), 72)
    return {"strokes": strokes, "printed_text": text}


def check(input_path, output_path, svg_out):
    """{ok, msg, drawn, layout}. The paper step's own check (checks/FIGP.py) runs unchanged; then
    the spec is laid on the PDF's vector drawing. A passing spec is drawn on the print's own
    geometry (it then looks like the book); one that only fails to trace is drawn from the spec."""
    with open(input_path, encoding="utf-8") as fh:
        item = json.load(fh)
    with open(output_path, encoding="utf-8") as fh:
        output = json.load(fh)
    spec = importlib.util.spec_from_file_location("paper_check_figp",
                                                  os.path.join(PAPER_CODE, "checks", "FIGP.py"))
    figp_check = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(figp_check)
    from lib import physics_figure, print_trace, spec_trace
    import figure_plugins

    # source_pdf is left out on purpose: the paper check would resolve it against the NEET
    # booklet folder. The trace against the chapter PDF is done here instead.
    ok, msg = figp_check.check(output, item={"printed_text": item.get("printed_text")})
    if not ok:
        return {"ok": False, "msg": msg}
    if output.get("out_of_scope") or "error" in output:
        return {"ok": True, "msg": msg, "drawn": False}
    _doc, page = _page(item["source_pdf"], item["page_index"])
    trace = print_trace.read(page, _rect(page, item["bbox_frac"]),
                             figure_plugins.spec_words(output["spec"]))
    if trace is not None and len(trace.subpaths) >= 3:
        wrong = spec_trace.problems(output["spec"], trace)
        if wrong:
            return {"ok": False, "msg": "; ".join("not the printed figure: %s" % w for w in wrong)}
        svg = print_trace.svg(trace, styles=spec_trace.font_styles(output["spec"], trace))
        layout = "booklet"
    else:
        svg = physics_figure.render(output["spec"])
        layout = "spec"
    os.makedirs(os.path.dirname(svg_out), exist_ok=True)
    with open(svg_out, "w", encoding="utf-8") as fh:
        fh.write(svg)
    return {"ok": True, "msg": "ok", "drawn": True, "layout": layout}


def main():
    verb = sys.argv[1]
    if verb == "probe":
        res = probe(sys.argv[2], sys.argv[3], json.loads(sys.argv[4]))
    elif verb == "check":
        res = check(*sys.argv[2:5])
    else:
        raise SystemExit(f"unknown verb {verb}")
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()
