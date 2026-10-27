#!/usr/bin/env python3
"""Cut figure crops from the boxes B3V's agent reported, not from inferred vector geometry.

    python3 scripts/cut_agent_figures.py --paper-id 2015_A --dry-run
    python3 scripts/cut_agent_figures.py --paper-id 2015_A --apply

WHY THIS REPLACES THE GEOMETRIC FIGURE PASS
-------------------------------------------
`extract_paper_v2.py` finds figures by clustering vector paths and embedded images and then testing
the clusters by size, path count and text coverage. That pass is how the watermark, the page border
and the page background each had to be excluded in turn, and it still UNDER-COUNTS: 2015 Code-A
reports 17 figure questions where the booklet plainly has far more, because a diagram drawn as a
handful of thin strokes does not survive thresholds that were tightened to keep furniture out.

Stage A does not have this problem, and the reason is structural: `a2-page-reader` READS THE PAGE and
marks each figure with `needs_special: true` and a bbox, and a script then crops the recorded
rectangle. Deciding what is a figure is a judgement about content; cropping a recorded rectangle is
arithmetic. The geometric pass tried to make a script do the judgement.

So this script does the Stage A thing for papers: it takes the `figure_bbox` that `b3-question-reader`
reported while reading the question's own crop, and cuts it. One source of truth, no thresholds.

WHAT IT KEEPS FROM THE GEOMETRIC PASS: nothing. The two are not merged. A figure the agent did not
report is not cut, because a box nobody vouched for is exactly what produced watermark crops.
"""

import argparse
import collections
import re
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
from lib import pdf as lib_pdf  # noqa: E402

CORPUS = rc.corpus()
B3V_OUT = ("steps", "B3V", "out")


def agent_reads(paper_id):
    """{qno: the agent's B3 output} for one booklet."""
    out = {}
    for path in sorted(glob.glob(rc.pp(*B3V_OUT, "%s__q*.runA.json" % paper_id))):
        qno = int(os.path.basename(path).split("__q")[1].split(".")[0])
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except ValueError:
            continue
        if "error" not in data:
            out[qno] = data
    return out


#: Below this, a reported box is not a measurement. Four pixels is already far smaller than any
#: printed structure, so the threshold only ever catches a failure to measure.
MIN_BOX_PX = 4.0
#: A drawing beside the `Sol.` label can begin a few points above it -- measured on 2024 Code-Q2
#: q50, whose solution figure starts at y=515 while `Sol.` sits at y=529.5. The slack keeps that
#: case on the solution side of the line.
SOLUTION_SLACK_PX = 45.0
#: An agent's box is an estimate made by eye, and it errs TIGHT: 2017 Code-A q11 lost the `T2` label
#: at its right edge and q55 cut `NO2` to `NC`. Growing every box this far outward (clipped to the
#: page by crop_boxes) keeps the labels a figure is printed with, as Stage A's grown crops do.
FIGURE_PAD_PX = 16.0


def within(box, part_box):
    """`box` clipped to the question part it was measured in. The padding must never reach past the
    question's own crop, which stops at the printed answer line: unclipped, 2017 Code-A q55's padded
    figure pulled in "Answer (4)" -- an answer shown to b6-blind-solver inside its figure."""
    return [max(box[0], part_box[0]), max(box[1], part_box[1]),
            min(box[2], part_box[2]), min(box[3], part_box[3])]


#: The publisher's answer line. `Answer (N)` and `Sol.` both appear; whichever comes FIRST on the
#: page marks where the question stops and the worked solution begins.
SOLUTION_LINE = re.compile(r"^\s*(Answer\s*[:(]|Sol\b|Solution\s*[:(])", re.I)


def anchor(parts, box_top):
    """(part, offset_y) for the stitched part a crop-space y falls in.

    A question crop can be STITCHED from two parts -- 55 of 2015_A's 177 questions span a page break.
    Part 1 is only the top of that image, so a y below its height belongs to part 2 on the NEXT
    page, at y minus part 1's height.

    Factored out because EVERY box needs its own anchor, not just the question's figure. 2016_X q042
    prints options 1-2 on page 15 and options 3-4 on page 16; re-using the figure's page-15 offset
    for all four pushed options 3 and 4 several hundred pixels past the bottom of page 15, where
    they intersected nothing and were dropped -- while the counter still claimed four crops.
    """
    part, offset_y = parts[0], 0.0
    for candidate in parts:
        height = candidate["bbox"][3] - candidate["bbox"][1]
        if box_top < offset_y + height or candidate is parts[-1]:
            return candidate, offset_y
        offset_y += height + STITCH_GAP_PX
    return part, offset_y


#: The white gap extract_paper_v2.stitch_vertical() leaves between stitched parts. anchor() once
#: ignored it, so a box on a second part landed 10px too low for each break above it.
STITCH_GAP_PX = 10


def to_page(parts, box):
    """(part, page_box) -- a box measured in a STITCHED crop, moved onto the page it was cut from.

    Exact for multi-part crops: the stitcher puts a 10px gap between parts AND centres each part on
    the width of the widest, so a narrower part sits shifted right in the stitched image. Both shifts
    are undone here; the old arithmetic undid neither.
    """
    part, offset_y = anchor(parts, box[1])
    widest = max(p["bbox"][2] - p["bbox"][0] for p in parts)
    shift_x = (int(round(widest)) - int(round(part["bbox"][2] - part["bbox"][0]))) // 2
    dx = part["bbox"][0] - shift_x
    dy = part["bbox"][1] - offset_y
    return part, [box[0] + dx, box[1] + dy, box[2] + dx, box[3] + dy]


def solution_tops(pdf_path, dpi):
    """{page_index: [y of every `Answer`/`Sol.` line]}, in the same pixel space as the crops.

    WHY THIS IS NEEDED. The question crop deliberately runs from one question to the start of the
    next, so it CONTAINS the publisher's worked solution -- that is how these booklets print. A
    reader of the image therefore sees the solution's diagram, and `b3-question-reader` sometimes
    reports it as the question's own figure. 2015_A q008 is the clear case: "Caprolactum is used for
    the manufacture of:" has four word options and NO figure, but the read boxed the caprolactam ->
    Nylon-6 scheme that the solution draws underneath, and the export then presented the answer's
    own working as part of the question.

    A note in the brief cannot fix this, because the agent is looking at an image where the two sit
    one above the other. A measurement can: anything at or below the answer line is the solution.
    """
    import pymupdf
    scale = dpi / 72.0
    tops = {}
    with pymupdf.open(pdf_path) as doc:
        for index, page in enumerate(doc):
            for block in page.get_text("dict").get("blocks", []):
                for line in block.get("lines", []):
                    text = "".join(span["text"] for span in line.get("spans", []))
                    if SOLUTION_LINE.match(text):
                        x0, y0, x1, _y1 = line["bbox"]
                        tops.setdefault(index, []).append((y0 * scale, x0 * scale, x1 * scale))
    for index in tops:
        tops[index].sort()
    return tops


def solution_after(tops, page_index, question_top, columns=None):
    """The first `Answer`/`Sol.` line BELOW where this question starts, or None.

    Per-question, not per-page, and the difference is not cosmetic. A page carries several
    questions, each with its own solution underneath it. Taking the first answer line on the page
    takes the FIRST question's solution, and then every figure belonging to a later question on that
    page sits below it and is wrongly rejected -- measured at 27 of 35 on 2015_A before this was
    split out, against 8 after.

    And per COLUMN. `columns` is the question part's [x0, x1]; an answer line counts only if its
    midpoint falls inside it. On a two-column page the OTHER column's answer lines sit at every
    height, so 2017 Code-A q4, q11, q55 and q61 -- real question figures well inside their own
    crops -- were rejected as "below the Answer line" because of an answer printed in the
    neighbouring column.
    """
    for y, x0, x1 in tops.get(page_index, []):
        if columns is not None and not columns[0] <= (x0 + x1) / 2.0 <= columns[1]:
            continue
        if y >= question_top:
            return y
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper-id", help="one booklet; omit to do every booklet in the corpus")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    if not args.paper_id:
        # Every booklet, so a run needs no per-paper bookkeeping. Each is independent: a booklet the
        # agent has not reached yet simply reports 0 read and changes nothing.
        ids = [os.path.basename(x)[:-5]
               for x in sorted(glob.glob(rc.pp(*CORPUS, "papers", "*.json")))]
        failures = 0
        for paper_id in ids:
            sys.argv = [sys.argv[0], "--paper-id", paper_id] + (
                ["--apply"] if args.apply else ["--dry-run"])
            failures += main()
        return 1 if failures else 0

    paper_path = rc.pp(*CORPUS, "papers", "%s.json" % args.paper_id)
    with open(paper_path, encoding="utf-8") as fh:
        paper = json.load(fh)
    reads = agent_reads(args.paper_id)
    if not reads:
        print("%s: no agent reads yet -- nothing to cut" % args.paper_id)
        return 0

    counts = collections.Counter()
    # The source PDF is resolved up front now, because the solution line has to be MEASURED before
    # any box is accepted -- it was previously only needed at the end, to render.
    import extract_paper_v2 as extractor
    source = os.path.join(os.path.dirname(extractor.SOURCE_ROOT), paper["meta"]["source_pdf"])
    if not os.path.exists(source):
        print("source PDF not found: %s" % source)
        return 1
    solution_y = solution_tops(source, paper["meta"]["dpi"])
    jobs = []
    for question in paper["questions"]:
        read = reads.get(question["qno"])
        if read is None:
            counts["unread"] += 1
            continue
        counts["read"] += 1
        question["agent_has_figure"] = bool(read.get("has_figure"))
        bbox = read.get("figure_bbox")
        if not read.get("has_figure"):
            question["agent_figure_images"] = []
            continue
        counts["agent_says_figure"] += 1
        if bbox and len(bbox) == 4:
            # A DEGENERATE BOX is treated as no box. An agent that reports [x, y, x, y] -- or any
            # box narrower or shorter than a few pixels -- has seen a figure and failed to measure
            # it, which is the same situation as reporting no box at all. Cutting it anyway raised
            # `FzErrorArgument: Invalid bandwriter header dimensions` out of PyMuPDF and ABORTED THE
            # WHOLE RUN, which is why 2015_A was missing figures for q014, q033 and q041 while the
            # reads for all three say `has_figure: true`. One unmeasurable box must cost one figure,
            # not every figure after it.
            width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            if width < MIN_BOX_PX or height < MIN_BOX_PX:
                counts["degenerate_box"] += 1
                question["agent_figure_images"] = []
                question["agent_figure_note"] = (
                    "agent reported a figure but its box measures %gx%g px, too small to cut; "
                    "the question crop still holds the picture" % (width, height))
                continue
        if not bbox or len(bbox) != 4:
            # The agent saw a figure and could not box it. Recorded, not guessed: the question crop
            # itself still holds the picture, so nothing is lost, but no rectangle is invented.
            counts["figure_without_a_box"] += 1
            question["agent_figure_images"] = []
            question["agent_figure_note"] = "agent reported a figure with no usable bbox"
            continue
        # The box is in the QUESTION CROP's pixel space. The crop was cut from the page at a known
        # offset, so the box has to be moved back onto the page before it can be re-cut.
        # WHICH PART THE BOX FALLS IN. The agent measured the box against the question crop it was
        # shown, and that crop may be STITCHED from two parts -- 55 of 2015_A's 177 questions span a
        # page break. Part 1 is only the top of the stitched image; a box below its height belongs to
        # part 2, on the NEXT page, at y minus part 1's height. Always anchoring to part 1 pushed 7
        # of 2015_A's boxes several hundred pixels past the bottom of their page, where they
        # intersected nothing and were silently lost.
        parts = question["parts"] or []
        if not parts:
            counts["no_part_to_anchor_to"] += 1
            continue
        part, raw_box = to_page(parts, bbox)
        page_box = within([raw_box[0] - FIGURE_PAD_PX, raw_box[1] - FIGURE_PAD_PX,
                           raw_box[2] + FIGURE_PAD_PX, raw_box[3] + FIGURE_PAD_PX], part["bbox"])
        # IS THIS THE QUESTION'S FIGURE, OR THE SOLUTION'S? Measured, not assumed. A box whose top
        # sits at or below the `Answer`/`Sol.` line on the same page belongs to the worked solution,
        # and presenting it as the question's figure shows a reader the answer's own working.
        # WHICH PART DID THE SOLUTION START IN? A question can straddle a page break -- 55 of
        # 2015_A's 177 do -- and when `Solution: (n)` sits on the FIRST page, every drawing on the
        # second page is part of that solution, however high up the page it appears. Testing only
        # the figure's own page let 2015_A q037 through: its `Solution: (1)` is on page 11 and the
        # cis/trans isomer drawing it belongs to is near the top of page 12, above that page's own
        # next answer line.
        solution_part = None
        for index, candidate in enumerate(parts):
            if solution_after(solution_y, candidate["page"], candidate["bbox"][1],
                              (candidate["bbox"][0], candidate["bbox"][2])) is not None:
                solution_part = index
                break
        here = parts.index(part)
        cut = solution_after(solution_y, part["page"], part["bbox"][1],
                             (part["bbox"][0], part["bbox"][2]))
        if solution_part is not None and here > solution_part:
            counts["solution_figure_rejected"] += 1
            question["agent_figure_images"] = []
            question["agent_figure_note"] = (
                "the agent boxed a drawing on a later part of the question, after the printed "
                "Answer/Sol. line on an earlier part, so it belongs to the worked solution")
            continue
        if cut is not None and page_box[1] >= cut - SOLUTION_SLACK_PX:
            counts["solution_figure_rejected"] += 1
            question["agent_figure_images"] = []
            question["agent_figure_note"] = (
                "the agent boxed a drawing that sits below the printed Answer/Sol. line, so it is "
                "the publisher's worked solution, not this question's figure")
            continue
        rel = os.path.join("figures_agent", args.paper_id, "q%03d.png" % question["qno"])
        jobs.append((part["page"] + 1, page_box, os.path.join(rc.pp(*CORPUS), rel)))
        question["agent_figure_images"] = [rel]
        # The PAGE box is recorded beside the picture, so vector_figures.py lifts exactly the same
        # region out of the PDF as vector art. Without it the vector copy would need its own guess.
        question["agent_figure_boxes"] = [{"page": part["page"], "bbox": page_box}]
        counts["cut"] += 1

        # PER-OPTION CROPS, where the options are themselves drawings. One box around all four gives
        # a tall strip and four `[structure diagram]` lines, and the reader has to count down the
        # strip to find option 3. Cut separately, each drawing prints beside its own number.
        boxes = read.get("option_boxes") or {}
        cut_options, option_boxes = {}, {}
        for key in sorted(boxes):
            box = boxes[key]
            if len(box) != 4 or box[2] - box[0] < MIN_BOX_PX or box[3] - box[1] < MIN_BOX_PX:
                continue
            # EACH OPTION GETS ITS OWN ANCHOR. See anchor(): a four-option panel can straddle the
            # page break, and the figure's offset is only right for the options on the figure's page.
            option_part, raw_option = to_page(parts, box)
            option_page = within([raw_option[0] - FIGURE_PAD_PX, raw_option[1] - FIGURE_PAD_PX,
                                  raw_option[2] + FIGURE_PAD_PX, raw_option[3] + FIGURE_PAD_PX],
                                 option_part["bbox"])
            option_cut = solution_after(solution_y, option_part["page"], option_part["bbox"][1],
                                        (option_part["bbox"][0], option_part["bbox"][2]))
            if option_cut is not None and option_page[1] >= option_cut - SOLUTION_SLACK_PX:
                continue                     # below the answer line: the solution's own drawing
            option_rel = os.path.join("figures_agent", args.paper_id,
                                      "q%03d_option_%s.png" % (question["qno"], key))
            jobs.append((option_part["page"] + 1, option_page,
                         os.path.join(rc.pp(*CORPUS), option_rel)))
            cut_options[key] = option_rel
            option_boxes[key] = {"page": option_part["page"], "bbox": option_page}
        if cut_options:
            question["agent_option_images"] = cut_options
            question["agent_option_boxes"] = option_boxes
            counts["option_crops"] += len(cut_options)

    # THE SOLUTION'S OWN FIGURES, each at the step it belongs to. b3s-solution-reader boxes every
    # drawing in the printed working against the SOLUTION crop, with `after_step`; each is cut from
    # the page the same way a question figure is, and recorded so the export can show it under its
    # step instead of dumping the whole printed block below the answer.
    for question in paper["questions"]:
        question["solution_figures"] = []
        sol_path = rc.pp("steps", "B3S", "out", "%s__q%03d.runA.json" % (args.paper_id, question["qno"]))
        parts = question.get("solution_parts") or []
        if not parts or not os.path.exists(sol_path):
            continue
        with open(sol_path, encoding="utf-8") as fh:
            sol = json.load(fh)
        figures = sol.get("figures")
        if figures is None and sol.get("figure_bbox"):
            figures = [{"bbox": sol["figure_bbox"], "after_step": 0}]   # written before `figures`
        for n, figure in enumerate(figures or [], 1):
            box = figure.get("bbox") or []
            if len(box) != 4 or box[2] - box[0] < MIN_BOX_PX or box[3] - box[1] < MIN_BOX_PX:
                counts["solution_figure_degenerate"] += 1
                continue
            sol_part, raw_sol = to_page(parts, box)
            sol_page = within([raw_sol[0] - FIGURE_PAD_PX, raw_sol[1] - FIGURE_PAD_PX,
                               raw_sol[2] + FIGURE_PAD_PX, raw_sol[3] + FIGURE_PAD_PX],
                              sol_part["bbox"])
            rel = os.path.join("figures_agent", args.paper_id,
                               "q%03d_sol_%d.png" % (question["qno"], n))
            jobs.append((sol_part["page"] + 1, sol_page, os.path.join(rc.pp(*CORPUS), rel)))
            question["solution_figures"].append({
                "image": rel, "after_step": int(figure.get("after_step") or 0),
                "kind": figure.get("kind") or "", "page": sol_part["page"], "bbox": sol_page})
            counts["solution_figures"] += 1

    print("%s: %d question(s) read by the agent, %d unread" % (args.paper_id, counts["read"],
                                                               counts["unread"]))
    print("   agent reports a figure : %d" % counts["agent_says_figure"])
    print("   with a usable bbox     : %d  -> cut" % counts["cut"])
    if counts["option_crops"]:
        print("   per-option crops       : %d" % counts["option_crops"])
    if counts["solution_figures"]:
        print("   solution figures       : %d  (each placed at its step)" % counts["solution_figures"])
    if counts["solution_figure_rejected"]:
        print("   was the SOLUTION's figure : %d  -> rejected, not the question's"
              % counts["solution_figure_rejected"])
    if counts["degenerate_box"]:
        print("   box too small to cut   : %d  -> recorded, run continues"
              % counts["degenerate_box"])
    if counts["figure_without_a_box"]:
        print("   figure but no bbox     : %d  -> recorded, nothing invented"
              % counts["figure_without_a_box"])
    geometric = sum(1 for q in paper["questions"] if q.get("figures"))
    print("   for comparison, the geometric pass found %d" % geometric)

    if args.dry_run:
        print("(dry run -- nothing written)")
        return 0

    if jobs:
        for job in jobs:
            os.makedirs(os.path.dirname(job[2]), exist_ok=True)
        import pymupdf
        import extract_paper_v2 as extractor
        with pymupdf.open(source) as doc:
            furniture = extractor.document_furniture(doc)   # watermark and logos: never in a crop
        lib_pdf.crop_boxes(source, jobs, dpi=paper["meta"]["dpi"], unit="px", hide_xrefs=furniture)
        print("cut %d figure crop(s) into papers_v2/figures_agent/%s/" % (len(jobs), args.paper_id))
    with open(paper_path, "w", encoding="utf-8") as fh:
        json.dump(paper, fh, ensure_ascii=False, indent=1)
    print("updated %s" % os.path.relpath(paper_path, rc.pp()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
