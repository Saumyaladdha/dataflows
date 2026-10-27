#!/usr/bin/env python3
"""Draw every CHECKED figure card: SMILES cards (FIGC) with RDKit, physics specs (FIGP) as SVG.

    python3 code/render_figure_cards.py --paper-id 2017_A --apply

The third leg of "the AI never draws; it writes a card, code checks the card, the renderer draws it".

WHERE THE BOOKLET'S FIGURE IS A VECTOR DRAWING (every 2017_A chemistry figure), a card is drawn ON
THAT GEOMETRY (lib/print_trace.py): the FIGC check has already laid every SMILES on a printed
molecule atom for atom, so the structures are drawn where and how the booklet drew them -- ring
circles, the aldehyde's H on the left, OCH3 written out -- with the arrows, curved mechanism arrows,
"<" signs and conditions around them. RDKit's own layout is the fallback for a scanned figure only:
it is what made q089's aldehyde come out mirrored and q064's rings lose their circles.
A card is drawn only if it passes its step's check right now -- a card that fails is recorded with
the reason and NOT drawn, because an unchecked drawing is exactly the valid-looking wrong picture the
split exists to prevent.

WHAT IT WRITES
    figures_drawn/<paper>/q###_<figure_id>.svg       one drawing per figure
    question["drawn"] = {<figure png path>: {figure_id, source, svg | status, ...}}

keyed by the SAME png path the figure is stored under, so the export puts each drawing beside the
exact vector copy of the printed figure it redraws -- never in place of it.
"""

import argparse
import collections
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
import runner_core as rc  # noqa: E402
import figure_plugins  # noqa: E402
from lib import chem_cards, physics_figure, print_trace  # noqa: E402
import FIGC as figc_check  # noqa: E402
import FIGP as figp_check  # noqa: E402

CORPUS = rc.corpus()
_SIZE = re.compile(r"<svg[^>]*?width=['\"]([\d.]+)(?:px)?['\"][^>]*?height=['\"]([\d.]+)(?:px)?['\"]")
LABEL_PX = 20
GAP_PX = 26


def _output(step, item_id):
    path = rc.pp("steps", step, "out", "%s.runA.json" % item_id.replace("#", "__"))
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def compose(cells, per_row):
    """One SVG holding several drawings in a grid, each with its printed label above it -- the
    booklet's 2x2 layout of four option structures."""
    sized = []
    for label, svg in cells:
        match = _SIZE.search(svg or "")
        if not match:
            continue
        sized.append((label, svg, float(match.group(1)), float(match.group(2))))
    if not sized:
        return None
    rows = [sized[i:i + per_row] for i in range(0, len(sized), per_row)]
    col_w = max(w for _l, _s, w, _h in sized)
    parts, y = [], 0.0
    for row in rows:
        row_h = max(h for _l, _s, _w, h in row) + LABEL_PX
        for n, (label, svg, w, h) in enumerate(row):
            x = n * (col_w + GAP_PX)
            if label:
                parts.append('<text x="%.1f" y="%.1f" font-family="Arial, Helvetica, sans-serif" '
                             'font-size="14" text-anchor="middle">%s</text>'
                             % (x + col_w / 2, y + 14, html.escape(chem_cards.formula_label(label))))
            parts.append(chem_cards.place(svg, x + (col_w - w) / 2, y + LABEL_PX))
        y += row_h + GAP_PX / 2
    width = len(rows[0]) * col_w + (len(rows[0]) - 1) * GAP_PX if rows else col_w
    width = max(width, max(len(r) for r in rows) * col_w + (max(len(r) for r in rows) - 1) * GAP_PX)
    return ('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            'viewBox="0 0 %.1f %.1f" width="%.1f" height="%.1f">%s</svg>'
            % (width, y, width, y, "".join(parts)))


def species_drawing(species):
    return chem_cards.species_svg(species["smiles"], species.get("orient"),
                                  species.get("abbreviate", True), species.get("explicit_h"),
                                  species.get("annotations"))


def chem_figure(card):
    """The drawing of one FIGC card, or None for not_a_structure.

    A card with a `scheme` is drawn from it -- every printed arrow, condition and letter. RDKit's
    reaction drawing is NOT a fallback for a reaction: it drops the arrow's printed conditions and
    lays the molecules out its own way, which is how 2017_A q052's aldol came out looking like a
    different compound."""
    if card.get("kind") == "not_a_structure":
        return None
    if card.get("scheme"):
        return chem_cards.scheme_svg(card)
    cells = [(s.get("label") or "", species_drawing(s)) for s in card.get("species") or []]
    per_row = 2 if len(cells) == 4 else min(len(cells), 3) or 1
    return compose(cells, per_row)


def traced(paper, card, figure):
    """(trace, per-species results) when this card's figure is drawn on the booklet's geometry."""
    if card.get("kind") == "not_a_structure" or not figure:
        return None
    trace = figure_plugins.trace_of(paper["meta"]["source_pdf"], paper["meta"]["dpi"],
                                    figure.get("page"), figure.get("bbox"))
    if trace is None or not print_trace.usable(trace):
        return None
    results, problems = print_trace.assign(trace, card.get("species") or [])
    return None if problems else (trace, results)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper-id", required=True)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    paper_path = rc.pp(*CORPUS, "papers", "%s.json" % args.paper_id)
    with open(paper_path, encoding="utf-8") as fh:
        paper = json.load(fh)
    figc_items = figure_plugins.FIGCPlugin().items({"papers": [args.paper_id]})
    figp_items = figure_plugins.FIGPPlugin().items({"papers": [args.paper_id]})
    counts = collections.Counter()

    def write(rel, svg):
        if args.apply:
            path = rc.pp(*CORPUS, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(svg)

    for question in paper["questions"]:
        drawn = {}
        figures = {f["figure_id"]: f for f in figure_plugins.figures_of(question)}
        png_of = {k: f["image"] for k, f in figures.items()}
        qid = "%s#q%03d" % (args.paper_id, question["qno"])
        # chemistry: one card per question, one entry per figure
        if qid in figc_items:
            output = _output("FIGC", qid)
            if output and "error" not in output:
                ok, message = figc_check.check(output, item=figc_items[qid])
                for card in output.get("figures") or []:
                    png = png_of.get(card.get("figure_id"))
                    if not png:
                        continue
                    entry = {"figure_id": card["figure_id"], "source": "smiles",
                             "card": chem_cards.enrich(card)}
                    if not ok:
                        entry.update(status="failed_check", message=message)
                        counts["chem_failed"] += 1
                    elif card.get("kind") == "not_a_structure":
                        entry.update(status="not_a_structure")
                        counts["chem_not_structure"] += 1
                    else:
                        on_print = traced(paper, card, figures.get(card["figure_id"]))
                        if on_print:
                            trace, results = on_print
                            svg = print_trace.svg(trace)
                            entry["layout"] = "booklet"
                            entry["print_match"] = [{"shown_as": r["shown_as"]} for r in results]
                            counts["chem_on_print"] += 1
                        else:
                            svg = chem_figure(card)
                            entry["layout"] = "rdkit"
                        rel = os.path.join("figures_drawn", args.paper_id,
                                           "q%03d_%s.svg" % (question["qno"], card["figure_id"]))
                        if svg:
                            write(rel, svg)
                            entry.update(status="drawn", svg=rel)
                            counts["chem_drawn"] += 1
                        # ...and EACH structure on its own, so an option carries its own drawing
                        # beside its SMILES instead of pointing into a four-panel picture.
                        singles = []
                        for n, species in enumerate(card.get("species") or [], 1):
                            one = None
                            if on_print and results[n - 1]["shown_as"] == "structure":
                                one = print_trace.component_svg(trace, results[n - 1]["component"])
                            if one is None:
                                one = species_drawing(species)
                            one_rel = os.path.join("figures_drawn", args.paper_id, "q%03d_%s_s%d.svg"
                                                   % (question["qno"], card["figure_id"], n))
                            if one:
                                write(one_rel, one)
                            singles.append(one_rel if one else None)
                        entry["species_svgs"] = singles
                    drawn[png] = entry
        # physics: one spec per figure
        for figure_id, png in png_of.items():
            item_id = "%s_%s" % (qid, figure_id)
            if item_id not in figp_items:
                continue
            output = _output("FIGP", item_id)
            if not output or "error" in output:
                continue
            ok, message = figp_check.check(output, item=figp_items[item_id])
            entry = {"figure_id": figure_id, "source": "spec", "spec": output.get("spec"),
                     "unreadable": output.get("unreadable") or []}
            if not ok:
                entry.update(status="failed_check", message=message)
                counts["phys_failed"] += 1
            elif output.get("out_of_scope"):
                entry.update(status="out_of_scope")
                counts["phys_out_of_scope"] += 1
            else:
                rel = os.path.join("figures_drawn", args.paper_id,
                                   "q%03d_%s.svg" % (question["qno"], figure_id))
                # On the booklet's own geometry where the figure is a vector drawing the spec was
                # checked against (lib/spec_trace.py): 2017_A q016's isotherms, open chevrons and
                # roman numerals as printed, not the renderer's approximation of them.
                trace, wrong = figure_plugins.physics_trace(paper, figures[figure_id], output["spec"])
                if trace is not None and not wrong:
                    from lib import spec_trace
                    found = spec_trace.agreement(output["spec"], trace)
                    write(rel, print_trace.svg(trace, styles=spec_trace.font_styles(output["spec"],
                                                                                    trace)))
                    entry["layout"] = "booklet"
                    entry["print_match"] = {"labels": len(spec_trace.spec_labels(output["spec"])),
                                            "precision": round(found["precision"], 2),
                                            "recall": round(found["recall"], 2)}
                    counts["phys_on_print"] += 1
                else:
                    write(rel, physics_figure.render(output["spec"]))
                    entry["layout"] = "spec"
                entry.update(status="drawn", svg=rel)
                counts["phys_drawn"] += 1
            drawn[png] = entry
        question["drawn"] = drawn

    print("%s: chemistry drawn %d (%d on the booklet's geometry), not a structure %d, FAILED check %d"
          " | physics drawn %d (%d on the booklet's geometry), out of scope %d, FAILED check %d"
          % (args.paper_id, counts["chem_drawn"], counts["chem_on_print"], counts["chem_not_structure"],
             counts["chem_failed"], counts["phys_drawn"], counts["phys_on_print"],
             counts["phys_out_of_scope"],
             counts["phys_failed"]))
    if args.apply:
        with open(paper_path, "w", encoding="utf-8") as fh:
            json.dump(paper, fh, ensure_ascii=False, indent=1)
    return 1 if (counts["chem_failed"] or counts["phys_failed"]) else 0


if __name__ == "__main__":
    sys.exit(main())
