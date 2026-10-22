#!/usr/bin/env python3
"""Find each figure-needing question in the printed papers, crop it, and write a B9S work item.

    python3 scripts/find_figures_in_papers.py --year 2023 --dry-run
    python3 scripts/find_figures_in_papers.py --year 2023 --apply

The script half of step B9S. It locates and cuts; it decides nothing. Whether a crop is the right
figure, whole, and in the right panel order is step B9S's agent judgement
(.claude/agents/b9s-source-figure-confirmer.md), and only a `belongs_complete` verdict publishes.

How a question is found
-----------------------
By its own words, searched across EVERY printed paper in inputs/papers/, not just its own year.
Two measured facts shape that:

  * The 170 scraped booklet-code PDFs contain ZERO embedded images between them. They are the best
    source of TEXT -- the same 200 questions per year in a different order -- but no search of them
    can return a diagram. They are excluded as figure sources (`figure_sources`).
  * The printed volumes hold 871 images between them, and the compilations reprint across years
    ("AV NEET 35 Years", "NEET 34 Years"), so a question missing from its own year's volume is
    often printed in another. The question's own year is tried first; the rest follow.

What gets cropped
-----------------
Up to two images per question, because they answer different questions for the reader:

  * the DIAGRAM that belongs to the stem -- the circuit, the graph, the pedigree;
  * the OPTION BLOCK, for a question whose options are themselves pictures. Those arrive in the
    records as "image option will be added soon" or as four indistinguishable strings, and without
    the block the question cannot be answered at all.

The option block is captured whole and never split into four. Which panel is option 3 is a
judgement about the page, and splitting here would bake a guess into an image file where nothing
downstream could tell it was a guess. It is also precisely what lets a crop from a DIFFERENT
booklet code be used: the codes rotate the options, so the agent checks the mapping against the
record's own option text rather than assuming it.
"""

import argparse
import collections
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
from paper_source_match import (figure_sources, match, option_block, page_furniture,  # noqa: E402
                                parse_booklet, record_text, _graphics, _norm)

PLACEHOLDER = re.compile(r"imageoption|willbeadded|optionimage")


def needs_figure(rec):
    """(True, why) when this question cannot be read without a picture.

    Two populations, both of which the quality checks already flag: questions the reader marked
    `has_figure`, and questions whose OPTIONS did not survive extraction -- placeholders, or four
    strings that cannot be told apart. The second is the more serious: such a question has a keyed
    answer pointing at an option a reader cannot distinguish, so it is unanswerable as published.
    """
    opts = [(rec.get("options_en") or {}).get(k) or "" for k in "1234"]
    norm = [_norm(o) for o in opts]
    if any(PLACEHOLDER.search(n) for n in norm if n):
        return True, "options are placeholders"
    real = [n for n in norm if len(n) >= 3]
    if len(real) >= 2 and len(set(real)) == 1:
        return True, "options are indistinguishable from one another"
    if not real and rec.get("stem_en"):
        return True, "options are empty"
    if rec.get("has_figure"):
        return True, "marked has_figure by the reader"
    return False, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--limit-sources", type=int, help="only search this many papers (quick look)")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    import fitz  # noqa: F401  (imported for its side effect of being available to helpers)

    recs = {}
    published = []
    for path in sorted(glob.glob(rc.pp("papers", "records", "Q-*.json"))):
        with open(path, encoding="utf-8") as fh:
            r = json.load(fh)
        if str(r.get("year")) != str(args.year) or r.get("merged_into"):
            continue
        want, why = needs_figure(r)
        if want:
            recs[r["question_id"]] = (path, r, why)
        # Everything already carrying a figure, INDEPENDENT of whether `needs_figure` fires. Some
        # records hold a figure while `has_figure` is false, and those are published to readers
        # just the same, so they belong in the verification pass too.
        if r.get("figure_path"):
            published.append((r["question_id"], r, why or "has_figure not set on this record"))
    print(f"{len(recs)} live {args.year} questions need a picture")
    for why, n in collections.Counter(w for _p, _r, w in recs.values()).most_common():
        print(f"   {n:4d}  {why}")
    if not recs:
        return 0

    sources = figure_sources(prefer=args.year)
    if args.limit_sources:
        sources = sources[:args.limit_sources]
    print(f"\nsearching {len(sources)} printed papers (the booklet-code scrapes hold no images "
          f"and are excluded)")

    # best match per question across every source
    best = {}
    for src in sources:
        try:
            doc, chunks = parse_booklet(src)
        except Exception as exc:
            print(f"   {os.path.basename(src)}: unreadable ({exc})")
            continue
        if not chunks:
            continue
        pending = [r for qid, (_p, r, _w) in recs.items()
                   if best.get(qid, (0,))[0] < 0.999]
        if not pending:
            break
        hits = 0
        for rec, chunk, score in match(pending, chunks):
            qid = rec["question_id"]
            if chunk and score > best.get(qid, (0, None, None, None))[0]:
                best[qid] = (score, src, chunk, doc)
                hits += 1
        print(f"   {os.path.basename(src):<36} matched {hits}")

    print(f"\n{len(best)} of {len(recs)} questions located in a printed paper")

    tally = collections.Counter()
    items = []
    for qid, (path, rec, why) in sorted(recs.items()):
        if qid not in best:
            tally["not_found_in_any_paper"] += 1
            continue
        score, src, chunk, doc = best[qid]
        furniture = page_furniture(doc)
        year_tag = os.path.splitext(os.path.basename(src))[0]
        out_dir = rc.pp("papers", "figures", str(args.year), "source")
        made = {}

        # Find the option block FIRST, so the stem's diagram can be looked for above it. Without
        # that boundary the diagram search picks the largest drawing anywhere in the question, and
        # for a question whose options are four graphs the options ARE the largest drawing: the
        # crop came back holding the four option panels while the stem's own v-t plot was never
        # captured. An agent reading the crop caught it ("the stem says its figure is the velocity-
        # time plot, but no v-t plot appears in the crop at all").
        ob = option_block(doc, chunk["rects"], furniture)
        limit = {ob[0]: ob[1].y0} if ob else {}

        boxes = []
        for pi, r in chunk["rects"]:
            region = +r
            if pi in limit and limit[pi] > region.y0:
                region.y1 = min(region.y1, limit[pi])
            if region.height < 10:
                continue
            boxes += [(pi, b) for b in _graphics(doc[pi], region, furniture)]
        if boxes:
            pi, box = max(boxes, key=lambda b: b[1].get_area())
            rel = os.path.join("papers", "figures", str(args.year), "source", f"{qid}.png")
            if args.apply:
                os.makedirs(out_dir, exist_ok=True)
                doc[pi].get_pixmap(clip=(box + (-4, -4, 4, 4)) & doc[pi].rect,
                                   dpi=args.dpi).save(rc.pp(rel))
            made["diagram"] = rel
            tally["diagram_cropped"] += 1

        if why != "marked has_figure by the reader":
            if ob:
                pi, box = ob
                rel = os.path.join("papers", "figures", str(args.year), "source",
                                   f"{qid}_options.png")
                if args.apply:
                    os.makedirs(out_dir, exist_ok=True)
                    doc[pi].get_pixmap(clip=box & doc[pi].rect, dpi=args.dpi).save(rc.pp(rel))
                made["options"] = rel
                tally["option_block_cropped"] += 1

        if not made:
            tally["found_but_nothing_to_crop"] += 1
            continue

        items.append({
            "question_id": qid,
            "stem_en": (rec.get("stem_en") or "").strip(),
            "options_en": rec.get("options_en") or {},
            "figure_file": made.get("diagram") or made.get("options"),
            "option_block_file": made.get("options", ""),
            # Where this image came from. It is a LABEL, not a verdict: a crop from the printed
            # page can still be the wrong region, and a legacy figure can still be perfectly
            # correct. The agent judges the picture either way, and that is the point -- 54 legacy
            # figures are published in this bank today with no verdict of any kind against them.
            "figure_origin": "cropped_from_printed_paper",
            "source_pdf": os.path.relpath(src, rc.pp()),
            "source_page": chunk["rects"][0][0] + 1,
            "source_booklet_code": year_tag,
            "our_booklet_code": " ".join(str(c) for c in (rec.get("paper_codes") or [])),
            "match_score": score,
            "why_needed": why,
        })

    # Every figure ALREADY published gets a work item too, whatever its origin. Those came from
    # cdn.mathpix.com snips matched by wording against legacy spreadsheets, and two outside audits
    # found several whose option panels contradict the options printed beside them -- but only a
    # handful were ever looked at. An unverified figure that happens to be right and one that is
    # wrong are indistinguishable from the data, so each is put to the same judgement as a fresh
    # crop. A legacy figure the agent confirms is kept; this step is not a campaign against them.
    for qid, rec, why in sorted(published):
        existing = rec.get("figure_path")
        if not existing:
            continue
        full = existing if os.path.isabs(existing) else rc.pp(existing)
        if not os.path.exists(full):
            tally["published_figure_file_is_missing"] += 1
            continue
        items.append({
            "question_id": qid,
            "stem_en": (rec.get("stem_en") or "").strip(),
            "options_en": rec.get("options_en") or {},
            "figure_file": existing,
            "option_block_file": "",
            "figure_origin": "legacy_match_from_another_question_bank",
            "source_pdf": str(rec.get("figure_source_url") or "legacy sheet"),
            "source_page": 0,
            "source_booklet_code": "unknown -- matched by wording, not by code",
            "our_booklet_code": " ".join(str(c) for c in (rec.get("paper_codes") or [])),
            "match_score": 0.0,
            "why_needed": f"already published, never verified ({why})",
        })
        tally["published_figure_queued_for_verification"] += 1

    print()
    for k, v in tally.most_common():
        print(f"   {v:4d}  {k}")

    if args.apply and items:
        work = rc.pp("steps", "B9S", "work")
        os.makedirs(work, exist_ok=True)
        for it in items:
            # One work item per CANDIDATE IMAGE, not per question: a question can have both a
            # fresh crop and an already-published figure, and each needs its own verdict. The
            # origin goes in the file name so the two never overwrite each other.
            tag = "paper" if it["figure_origin"].startswith("cropped") else "legacy"
            with open(os.path.join(work, f"{it['question_id']}__{tag}.runA.input.json"),
                      "w", encoding="utf-8") as fh:
                json.dump(it, fh, ensure_ascii=False, indent=1)
                fh.write("\n")
        print(f"\nwrote {len(items)} work items to steps/B9S/work/ for the "
              f"b9s-source-figure-confirmer agent to rule on")
    elif args.dry_run:
        print("\n(dry run -- nothing written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
