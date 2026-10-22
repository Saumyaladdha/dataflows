#!/usr/bin/env python3
"""Match question records against an ORIGINAL paper PDF, verify them against it, and crop their
figures out of it.

    python3 scripts/paper_source_match.py --year 2024 --report
    python3 scripts/paper_source_match.py --year 2024 --crop --apply

Why this exists
---------------
Every figure in this bank today came from `cdn.mathpix.com` snip URLs that a script matched *by
wording* against an old question bank (step B9). SPEC.md Section 4 forbids exactly that: "Always
crop figures from the official PDFs; never depend on a URL." The reason is visible in the audits --
a near-wording match lands on the same question printed in a DIFFERENT booklet code, whose option
panels are in a different order, so the figure silently contradicts the options beside it.

`inputs/papers/` holds the original PDFs, so the figure can be cut from the page the question was
actually printed on. This file does that, and on the way it gets something the pipeline has never
had: an independent source to check the records against. Every other check so far compared the
scrape with itself.

What it can and cannot verify
-----------------------------
The booklet in `inputs/papers/` and the records are usually DIFFERENT booklet codes (2024: records
are code Q1, the booklet is code T3). NEET prints the same 200 questions per code in a different
order with the options rotated, so:

  CAN   -- confirm the stem wording, confirm the option VALUES as a set, and cut any diagram that
           belongs to the stem. All three are code-independent: a diagram of a circuit is the same
           circuit in every code.
  CANNOT -- confirm the option ORDER, or cut a figure for a question whose OPTIONS ARE PICTURES.
           For those the panel order is a property of the code, and taking it from another code is
           the very defect this file was written to stop. Such questions are reported as
           `option_image_wrong_code` and deliberately left without a figure.

Provenance is recorded per record in `repairs`, the same way scripts/repair_paper_records.py does,
because a figure with no recorded origin is indistinguishable from the B9 figures we are replacing.
"""

import argparse
import collections
import csv
import datetime
import difflib
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

# A question start, in the two forms the papers in inputs/papers/ actually use. The official
# booklets print the number ALONE on its own line with the stem indented beside it; the coaching
# compilations run the number into the stem. Both are anchored to the column's left margin, which
# is what keeps "(2) 10 V" and "1.32 kg" from being read as the start of question 2 or 1 -- those
# sit inside the text, never at the margin. An earlier version anchored to the start of a text
# BLOCK instead, and found 82 of 200 questions, because this layout packs the tail of one question
# and the head of the next into a single block.
INSTRUCTIONS = re.compile(r"GENERAL INSTRUCTION|Do not open this Test Booklet", re.I)
# "1. (4) 2. (1) 3. (3)" -- the key grid some booklets print on their last page.
KEY_PAIR = re.compile(r"(\d{1,3})\s*\.\s*\((\d)\)")
OPT_SPLIT = re.compile(r"\((\d)\)")
Q_ALONE = re.compile(r"^(\d{1,3})\s*\.\s*$")
Q_INLINE = re.compile(r"^(\d{1,3})\s*\.\s+(?=[A-Z(\[])")

# Printed pages carry a running header and a page number; both sit outside the type area and would
# otherwise be cropped into the top of any figure that starts high on the page.
HEADER_PT = 42
FOOTER_PT = 28


def _norm(text):
    """Letters and digits only -- the comparison key used throughout this repo.

    LaTeX control words are stripped FIRST. The records store maths as LaTeX while the print is
    plain text, so "$6\\,\\mathrm{bp}$" and "6 bp" must reduce to the same key; without the strip
    the first becomes "6mathrmbp" and every maths-bearing option looks like a mismatch. That alone
    accounted for most of a 91-question "disagreement" count on the first run.
    """
    t = re.sub(r"\\[a-zA-Z]+", " ", text or "")
    return re.sub(r"[^a-z0-9]", "", t.lower())


#: words that carry no discriminating power in a NEET stem -- every Assertion-Reason question and
#: every Match-the-List question shares them, so matching on them pairs questions at random.
STOP = set("""the a an of is are was were be to in on for with and or as at by from that this
these those which what given below two statements one labelled assertion reason correct incorrect
following match list i ii if then it its their his her they them has have had not no only also
but so than when where who whom whose will would can could may might must shall should do does
did done being been about into over under between among through during before after above
""".split())


def _tokens(text):
    """Discriminating words of a stem, for cheap candidate ranking."""
    t = re.sub(r"\\[a-zA-Z]+", " ", text or "").lower()
    return [w for w in re.findall(r"[a-z]{3,}", t) if w not in STOP]


def _columns(page):
    """(x_mid, n_columns) for one page.

    Derived from where the text actually sits rather than assumed, because the booklets in
    inputs/papers/ are not all the same: the 2024 booklet is two-column at 595pt wide, the coaching
    compilations are single-column at 671pt. Guessing two columns on a single-column page splits
    every question in half.
    """
    # Measured on LINES, not blocks. A text block can span both columns -- the running head does,
    # and so does any block the extractor merges across the gutter -- so counting block left edges
    # undercounts the right column. On page 17 of the 2024 booklet that misread a two-column page
    # as single-column, which set the margin at 71pt and silently rejected every question start in
    # the right column: questions 128-132 and 158-160 vanished from the parse.
    xs = [l["bbox"][0]
          for b in page.get_text("dict")["blocks"] if b["type"] == 0
          for l in b["lines"]
          if HEADER_PT < l["bbox"][1] < page.rect.height - FOOTER_PT
          and any(s["text"].strip() for s in l["spans"])]
    if not xs:
        return page.rect.width / 2, 1
    mid = page.rect.width / 2
    right = [x for x in xs if x > mid]
    return mid, 2 if len(right) >= max(5, len(xs) * 0.15) else 1


def parse_booklet(path):
    """[{qno, rects, text}] in printed reading order.

    A question's content is everything between its own number and the next one, which may continue
    into the next column or onto the next page -- so the region is a LIST of rectangles, not one
    box. Treating it as a single box is what makes a cropper miss a diagram that was pushed to the
    top of the following column.
    """
    import fitz
    doc = fitz.open(path)
    panes = []                                   # reading-order list of (page_index, rect)
    starts = []                                  # (pane_index, y, qno)
    for pi, page in enumerate(doc):
        # The booklet opens with a numbered instruction list ("6. The CODE for this Booklet is
        # T3."). Those items are formatted exactly like questions and parse as questions 1-10,
        # which then collide with the real 1-10 and give one of them the wrong page.
        # The last page of some booklets is the key grid for this code. Every "12. (3)" in it
        # parses as the start of question 12 and collides with the real one; it is picked up
        # separately by booklet_key() and is worth far more there.
        if INSTRUCTIONS.search(page.get_text() or "") or \
                len(KEY_PAIR.findall(" ".join((page.get_text() or "").split()))) >= 30:
            panes.append((pi, fitz.Rect(0, 0, page.rect.width, page.rect.height)))
            continue
        mid, ncol = _columns(page)
        top, bot = HEADER_PT, page.rect.height - FOOTER_PT
        bounds = ([(0, mid), (mid, page.rect.width)] if ncol == 2
                  else [(0, page.rect.width)])
        lines = [(fitz.Rect(l["bbox"]), " ".join(s["text"] for s in l["spans"]).strip())
                 for b in page.get_text("dict")["blocks"] if b["type"] == 0
                 for l in b["lines"]]
        lines = [(r, t) for r, t in lines if t and top <= r.y0 < bot]
        for x0, x1 in bounds:
            pane = fitz.Rect(x0, top, x1, bot)
            panes.append((pi, pane))
            col = [(r, t) for r, t in lines if x0 <= (r.x0 + r.x1) / 2 < x1]
            if not col:
                continue
            # The margin is a LOW PERCENTILE of the column's own line edges, plus a tolerance.
            # Two earlier rules each failed on a real file: the leftmost line in the column is
            # dragged left by a centred heading ("PHYSICS" overhangs by 27pt), which rejected every
            # question start in that column; and a fixed fraction of the column width is too tight
            # for a narrow column with a deep indent -- 12% of a 306pt column is 36.7pt, while the
            # Aakash solution booklets start their text at 50pt, so every start on their two-column
            # pages was rejected. The 10th percentile sits at the body's true left edge whichever
            # way the page is set.
            edges = sorted(r.x0 for r, _ in col)
            margin = edges[max(0, int(len(edges) * 0.10))] + 14.0
            for r, t in sorted(col, key=lambda rt: rt[0].y0):
                if r.x0 > margin:
                    continue
                m = Q_ALONE.match(t) or Q_INLINE.match(t)
                if m and 1 <= int(m.group(1)) <= 200:
                    starts.append((len(panes) - 1, r.y0, int(m.group(1))))

    out = []
    for idx, (pane_i, y, qno) in enumerate(starts):
        nxt = starts[idx + 1] if idx + 1 < len(starts) else None
        rects = []
        last = nxt[0] if nxt else len(panes) - 1
        for p in range(pane_i, min(last, len(panes) - 1) + 1):
            page_i, pane = panes[p]
            r = +pane
            if p == pane_i:
                r.y0 = y
            if nxt and p == nxt[0]:
                r.y1 = nxt[1]
            if r.height > 2:
                rects.append((page_i, r))
        # Cut the region at its worked SOLUTION, if it prints one. The Aakash booklets are
        # "Answers & Solutions" volumes: each question is followed by "Sol. ..." carrying the
        # working, its own numbers and often its own diagram. Left in, the solution's content reads
        # as material the record is missing (38 of 103 matched 2023 records came back
        # `content_dropped`, and the clean rate read 28% against a source that actually agrees with
        # them), and a figure cut from the region can be the SOLUTION's diagram rather than the
        # question's.
        rects = _cut_at_solution(doc, rects)
        text = " ".join(" ".join(doc[pi].get_text(clip=r).split()) for pi, r in rects)
        out.append({"qno": qno, "rects": rects, "text": text})

    # Drop chunks that plainly hold MORE THAN ONE question. This happens wherever the numbering is
    # not a single ascending run -- the chapter-wise compilations restart at 1 in every chapter and
    # interleave worked solutions, so a "next start" can be pages away and one chunk swallows
    # everything between. Such a chunk matches almost any record at containment 1.0, simply because
    # it contains several questions, and then reports a confident pairing under the wrong question
    # number. Dropping is right rather than splitting: this file's job is to CHECK records against
    # a paper, so a region it cannot segment with confidence is evidence it must not use.
    # Whether the guards below are needed at all depends on the document. An exam booklet numbers
    # its questions 1..200 in one ascending run, so a boundary is wherever the next number appears
    # and the segmentation can be trusted. The chapter-wise compilations restart at 1 in every
    # chapter and interleave worked solutions, so "the next start" can be pages away. Measuring
    # which kind this is, rather than applying the strict guard everywhere, matters both ways: the
    # strict guard drops the official paper's long Match-List questions (19 of 200), and dropping
    # it for a compilation lets one chunk swallow a whole chapter.
    # The test is whether question numbers are UNIQUE across the document, not whether they
    # ascend. A chapter-wise book ascends inside each chapter and so reads as 97% ascending, which
    # is indistinguishable from a booklet by that measure; but it reuses every number once per
    # chapter, so its distinct-to-total ratio is 0.35 against the booklet's 1.00.
    nos = [c["qno"] for c in out]
    sequential = len(out) > 10 and len(set(nos)) >= len(nos) * 0.95

    if sequential:
        # Numbers unique and ascending: every boundary is a real question boundary, so nothing is
        # dropped. A second "(1)" inside a region is a figure's own label or an option that
        # reflowed, not a second question, and discarding on it cost 11 of the official paper's
        # 200 questions.
        return doc, out

    clean = []
    for c in out:
        if len(re.findall(r"\(\s*1\s*\)", c["text"])) > 1:
            continue
        if len(c["text"]) > 1200 or len(re.findall(r"\ba\s*\.\s", c["text"])) > 1:
            continue
        clean.append(c)
    return doc, clean


#: The scraped booklet-code PDFs. Excluded as figure sources, and the exclusion is measured, not
#: assumed: all 170 of them contain ZERO embedded images between them, which is the gap step B9
#: exists to paper over. They remain the best source for TEXT -- the same questions in a different
#: order, which is what scripts/cross_code_match.py uses as evidence -- but a search for a diagram
#: in them can only ever come back empty.
CODE_SCRAPE = re.compile(r"^neet_\d{4}_code-", re.I)


def figure_sources(prefer=None):
    """Every PDF in inputs/papers/ that can actually supply a figure, best first.

    Deliberately NOT restricted to the question's own year. The compilations reprint questions
    across many years -- "AV NEET 35 Years", "NEET 34 Years" -- so a 2023 question is often printed
    in the 2022 or 2025 volume as well, and between them these files hold 871 images where the code
    scrapes hold none. `prefer` puts the question's own year first so a same-year printing wins
    when there is one.
    """
    out = []
    for path in sorted(glob.glob(rc.pp("inputs", "papers", "*.pdf"))):
        name = os.path.basename(path)
        if CODE_SCRAPE.match(name):
            continue
        # A scanned volume is used through its OCR'd copy in papers/ocr_cache/, which
        # scripts/ocr_paper.py builds. The OCR is what makes the question FINDABLE; the crop is
        # still pixels from the same scan, so the picture is unaffected by OCR quality.
        cached = rc.pp("papers", "ocr_cache", name)
        out.append(cached if os.path.exists(cached) else path)
    if prefer:
        out.sort(key=lambda p: (str(prefer) not in os.path.basename(p), p))
    return out


def booklet_key(doc):
    """{q_no: option} printed inside the booklet itself, or {} if it prints no key.

    A key grid found this way is a CANDIDATE answer source, never a trusted one -- see
    `key_is_trustworthy`. The grid inside inputs/papers/2024.pdf turned out to belong to neither
    the booklet's own question order nor ours, and taking it at face value produced 109 false
    "our answer disagrees with the official paper" findings on records that were in fact correct.
    """
    for page in doc:
        flat = " ".join((page.get_text() or "").split())
        pairs = KEY_PAIR.findall(flat)
        if len(pairs) >= 30:
            return {int(q): int(o) for q, o in pairs if 1 <= int(q) <= 200 and 1 <= int(o) <= 4}
    return {}


def key_is_trustworthy(key, pairs):
    """Does this key grid actually belong to the question order it was printed beside?

    Tested against the one thing already known: the records' own answers, which came from the
    official NTA key. The option NUMBERS cannot be compared across booklet codes, so the test
    compares the option TEXT each side selects. A key that belongs to the paper agrees on nearly
    every question; one that does not sits near 25%, which is what four options gives by chance.

    This gate exists because the alternative is worse than having no key at all: a stray grid
    silently rewrites every answer in the bank and every one of its findings looks like a defect in
    the data rather than in the grid.
    """
    agree = total = 0
    for rec, chunk, _score in pairs:
        if not chunk:
            continue
        ours = str(rec.get("official_answer") or "")
        theirs = key.get(chunk["qno"])
        opts = chunk_options(chunk["text"])
        if ours not in "1234" or not ours or not theirs or str(theirs) not in opts:
            continue
        a = _norm((rec.get("options_en") or {}).get(ours))[:30]
        b = _norm(opts[str(theirs)])[:30]
        if not a or not b:
            continue
        total += 1
        if a == b or a.startswith(b[:15]) or b.startswith(a[:15]):
            agree += 1
    rate = agree / total if total else 0.0
    return rate >= 0.60, agree, total, round(rate, 3)


def chunk_options(text):
    """{n: option text} read off the printed question.

    Needed because the answer check has to compare option TEXT, not option number: our records are
    one booklet code and the source is another, and the whole point of a code is that the options
    are rotated. Comparing numbers across codes would report a disagreement on nearly every
    question and hide the handful that are really wrong.
    """
    parts = OPT_SPLIT.split(text)
    out = {}
    for i in range(1, len(parts) - 1, 2):
        n = parts[i]
        if n in "1234" and n not in out:
            # The last option runs straight into whatever the page prints next -- in the Aakash
            # volumes an "Answer" marker, elsewhere the next question's number. Left attached it
            # makes option 4 differ from the record on 42 of 102 questions that otherwise agree
            # position for position, which reads as a rotated option order rather than a stray word.
            val = re.split(r"\b(?:Answer|Ans\b|Sol\b|Solution)\b", parts[i + 1], maxsplit=1)[0]
            out[n] = val.strip()
    return out


#: How a worked solution announces itself in the volumes held here.
SOLUTION_START = re.compile(r"^(?:Sol\s*[.:]|Solution\s*[.:]|Ans\s*[.:]|Hide\s+solution)", re.I)


def _cut_at_solution(doc, rects):
    """`rects` truncated at the first line that starts a worked solution.

    Returns the region unchanged when no solution marker appears, so question-only papers are
    untouched. Everything from the marker onward is dropped, including later panes: once the
    solution has begun, the rest of the region belongs to it.
    """
    out = []
    for pi, rect in rects:
        hit = None
        for block in doc[pi].get_text("dict")["blocks"]:
            if block["type"]:
                continue
            for line in block["lines"]:
                text = " ".join(s["text"] for s in line["spans"]).strip()
                y0 = line["bbox"][1]
                if SOLUTION_START.match(text) and rect.y0 <= y0 < rect.y1:
                    hit = y0 if hit is None else min(hit, y0)
        if hit is None:
            out.append((pi, rect))
            continue
        trimmed = +rect
        trimmed.y1 = max(rect.y0, hit - 1)
        if trimmed.height > 4:
            out.append((pi, trimmed))
        break                                    # the solution runs on; later panes are all it
    return out or rects


def page_furniture(doc):
    """Image xrefs that appear on most pages -- the publisher's watermark and logo.

    They sit inside the type area, so a question whose figure is near them crops the watermark in
    with the diagram. Identified by repetition rather than by appearance, which needs no list of
    known publishers.
    """
    seen = collections.Counter()
    for page in doc:
        for xref in {im[0] for im in page.get_images(full=True)}:
            seen[xref] += 1
    return {x for x, n in seen.items() if n > max(2, doc.page_count * 0.5)}


def _graphics(page, rect, furniture=frozenset()):
    """Diagram clusters inside `rect`, as rectangles.

    Vector diagrams are hundreds of separate primitives, and so are fraction bars, square-root
    hooks and table rules. The separation used here is CLUSTERING: a real diagram is many
    primitives packed together spanning a decent area, while a fraction bar is one hairline alone
    on its line. The 2023 compilation has 27 drawings on a page that contains no diagram at all --
    every one of them a maths rule -- which is what this has to reject.
    """
    import fitz
    prim = []
    for im in page.get_images(full=True):
        if im[0] in furniture:                       # the publisher's watermark, on every page
            continue
        for r in page.get_image_rects(im[0]):
            if fitz.Rect(r).intersects(rect):
                prim.append(("image", fitz.Rect(r)))
    for d in page.get_drawings():
        r = fitz.Rect(d["rect"]) & rect
        if r.is_empty:
            continue
        # Page furniture -- the column rule, the page border, the band under a running head -- is a
        # single primitive as tall or as wide as the type area. Clustered in with a diagram it
        # stretches the crop box over the options printed below, which is how the first run
        # produced figures with "(1) 50 pi^2 (2) 1280 pi^2" baked into the image.
        if r.height > rect.height * 0.6 or r.width > rect.width * 0.92:
            continue
        # A diagram is laid out INSIDE its column; the column rule, the page border and the
        # publisher's roundel all run up to or past the column edge. Clipping on that boundary
        # removes them without needing to know what they look like.
        if r.x0 <= rect.x0 + 2 or r.x1 >= rect.x1 - 2:
            continue
        prim.append(("draw", r))
    if not prim:
        return []

    prim.sort(key=lambda p: p[1].y0)
    clusters, cur = [], [prim[0]]
    for kind, r in prim[1:]:
        # 24pt, because the parts of one diagram are separated by real gaps -- the hatched ceiling
        # sits well above the pendulum hanging from it, and at 8pt they clustered separately, so
        # keeping only the largest cluster cut the support off the top of the figure.
        if r.y0 - max(x[1].y1 for x in cur) <= 24:
            cur.append((kind, r))
        else:
            clusters.append(cur)
            cur = [(kind, r)]
    clusters.append(cur)

    lines = [fitz.Rect(l["bbox"]) for b in page.get_text("dict")["blocks"]
             if b["type"] == 0 for l in b["lines"]]
    keep = []
    for c in clusters:
        box = fitz.Rect(c[0][1])
        for _, r in c[1:]:
            box |= r
        box &= rect
        if box.is_empty or box.height < 22 or box.width < 38:
            continue
        has_image = any(k == "image" for k, _ in c)
        if not has_image and len(c) < 4:
            continue
        # a band that is mostly text is a maths run or a table, not a diagram
        txt = sum((fitz.Rect(l) & box).get_area() for l in lines if l.intersects(box))
        if txt > box.get_area() * 0.55:
            continue
        keep.append(_trim_edge_text(box, lines))
    return keep


def option_block(page, rects, furniture=frozenset()):
    """The printed option block as ONE rectangle, or None.

    For a question whose options ARE pictures -- four structures, four graphs, four circuits -- the
    options cannot be transcribed and the record holds either placeholders ("image option will be
    added soon") or four indistinguishable strings. The whole block is therefore captured as a
    single screenshot of the page, which is what makes such a question answerable at all.

    It is NOT split into four. Deciding which panel is option 3 is a judgement about the printed
    page, and splitting here would bake a guess about panel order into an image file where nothing
    downstream could see it was a guess. The agent at step B9S rules on the mapping instead, and
    that ruling is what allows a crop taken from a DIFFERENT booklet code to be used safely: the
    codes print the same question with the options rotated, so the order has to be checked, not
    assumed.
    """
    import fitz
    found = None
    for pi, rect in rects:
        lines = [(fitz.Rect(l["bbox"]), " ".join(s["text"] for s in l["spans"]).strip())
                 for b in page[pi].get_text("dict")["blocks"] if b["type"] == 0
                 for l in b["lines"]]
        # The FIRST option fixes the top edge; EVERY option fixes the bottom. Using the first
        # option's line for both cut the block off below option (a), which for a question whose
        # options are pictures loses three of the four panels -- the exact content the crop exists
        # to capture.
        first = [r for r, t in lines
                 if r.intersects(rect) and re.match(r"^\(?\s*(?:1|a|A)\s*[\).]", t)]
        marks = [r for r, t in lines
                 if r.intersects(rect) and re.match(r"^\(?\s*[1-4a-dA-D]\s*[\).]", t)]
        if not first or not marks:
            continue
        top = min(m.y0 for m in first) - 2
        # A picture option is taller than the label beside it: the graph for option (1) rises well
        # above the "(1)" itself, so a top edge taken from the label alone decapitates the first
        # panel -- which then reads as `belongs_clipped` and never publishes. Any drawing that
        # straddles the label's own line pulls the edge up to its own top.
        for g in _graphics(page[pi], rect, furniture):
            if g.y0 < top and g.y1 > top:
                top = min(top, g.y0 - 2)
        # The block ends with its last option, not with the question region. A region runs to the
        # next question's number, so it can trail across a chapter heading ("Current Electricity")
        # or into the following question's first line; one line of slack past the last option
        # marker keeps a wrapped option without picking those up.
        last = max(m.y1 for m in marks)
        slack = max(m.height for m in marks) * 1.6
        box = fitz.Rect(rect.x0, max(rect.y0, top), rect.x1, min(rect.y1, last + slack))
        if box.height > 24 and (found is None or box.get_area() > found[1].get_area()):
            found = (pi, box)
    return found


def _trim_edge_text(box, lines):
    """Pull the crop in off any full-width line of prose sitting on its top or bottom edge.

    A scanned figure's image box often overlaps the last line of the stem above it, so the crop
    opens with half a sentence ("from the given figures (a) and (b)"). Only lines that run most of
    the figure's width and sit right at an edge are trimmed -- a figure's own labels, "(a)" and
    "(b)", are short and sit inside it, so they survive.
    """
    for _ in range(3):
        band = max(6.0, box.height * 0.14)
        cut = None
        for l in lines:
            if l.x1 - l.x0 < box.width * 0.5 or not l.intersects(box):
                continue
            if l.y1 <= box.y0 + band and l.y1 < box.y1 - band:
                cut = ("top", l.y1 + 1.5)
            elif l.y0 >= box.y1 - band and l.y0 > box.y0 + band:
                cut = ("bottom", l.y0 - 1.5)
        if not cut:
            break
        if cut[0] == "top":
            box.y0 = cut[1]
        else:
            box.y1 = cut[1]
    return box


def _is_option_image(rec, chunk):
    """True when the OPTIONS themselves are pictures.

    Detected from the record rather than the page: when the four option strings are empty or near
    empty, there was nothing to read because the choices were drawn. These are the questions whose
    panel order is code-specific, so a figure from another code must not be attached.
    """
    opts = [(rec.get("options_en") or {}).get(k) or "" for k in "1234"]
    return sum(1 for o in opts if len(_norm(o)) < 3) >= 2


def match(records, chunks):
    """[(record, chunk, score)] -- best booklet question per record.

    Matching is on the normalised stem, with a difflib ratio as the fallback: the records came from
    a scrape whose notation differs from the print ("10-4" vs "10–4", lost subscripts), so an exact
    key alone finds maybe three in five. The ratio is compared against a high threshold because a
    wrong pairing here produces a figure attached to the wrong question, which is worse than none.
    """
    cand = [(c, set(_tokens(c["text"]))) for c in chunks]

    out = []
    for rec in records:
        toks = set(_tokens(record_text(rec)))
        # A record with only a handful of distinctive words is matched on STRICTER terms rather
        # than refused. Containment divides by that count, so three coincidental words out of four
        # score 0.75 -- which is how a physics question about a suspended wire once paired with a
        # biology question about anaphase. But a flat floor of eight words refused the questions
        # that most need a figure: "The equivalent capacitance of the system shown in the following
        # circuit is" reduces to five distinctive words and matches its printed page exactly. So a
        # short record must clear a perfect containment AND a wide margin over the runner-up.
        if len(toks) < 4:
            out.append((rec, None, 0.0))
            continue
        short = len(toks) < 8

        # CONTAINMENT, not a sequence ratio: what share of this record's distinctive words appear
        # in the printed question. A sequence ratio was tried first and scored 0.36-0.50 on
        # questions that are demonstrably present, because the record stores maths as LaTeX, stores
        # match-lists in their own fields, and orders options differently from the print -- all of
        # which move characters around without changing which words are there. Containment is blind
        # to order and notation and separated these cleanly: 171 of 198 at 0.8 or better.
        scored = sorted(((len(toks & t) / len(toks), c) for c, t in cand), key=lambda x: -x[0])
        best, chunk = scored[0][0], scored[0][1]
        runner = scored[1][0] if len(scored) > 1 else 0.0
        shared = len(toks & set(_tokens(chunk["text"])))
        # An ABSOLUTE overlap floor alongside the ratio. A ratio alone is a share of whatever the
        # record happens to hold, so it says nothing about how much evidence the pairing rests on;
        # eight words in common is the least that distinguishes one NEET question from another --
        # unless the record has fewer than eight to give, in which case every one of them must be
        # present and the runner-up must be far behind.
        if short:
            if best < 0.999 or (best - runner) < 0.25:
                out.append((rec, None, round(best, 3)))
                continue
        elif shared < 8:
            out.append((rec, None, round(best, 3)))
            continue

        # Accepted only when good AND clearly better than the next candidate. The margin is the
        # important half: a wrong pairing attaches another question's figure and answer to this
        # record, which is worse than reporting no match at all. At these thresholds no 2024 record
        # is ambiguous, so the margin costs nothing and guards the match-list questions, which are
        # near-identical apart from their lists.
        if best < 0.75 or (best - runner) < 0.08:
            out.append((rec, None, round(best, 3)))
        else:
            out.append((rec, chunk, round(best, 3)))
    return out


def record_text(rec):
    """Everything the printed question would show, assembled from the record.

    The match-lists and statement blocks live in their own fields, so a record's `stem_en` alone is
    a fraction of what is on the page; leaving them out is what made Match-List questions
    unmatchable.
    """
    parts = [rec.get("stem_en") or ""]

    # Placeholder and degenerate options are left OUT of the comparison. A question whose options
    # read "image option will be added soon" four times, or whose four options are identical, is
    # exactly the question most in need of repair from the real paper -- and including that text
    # buries the stem's own words under boilerplate that appears on dozens of other broken rows,
    # so the match is rejected for ambiguity precisely where it is most wanted.
    opts = [(rec.get("options_en") or {}).get(k) or "" for k in "1234"]
    real = [o for o in opts if len(_norm(o)) >= 3]
    if len(set(_norm(o) for o in real)) > 1 and not any(
            "willbeadded" in _norm(o) or "imageoption" in _norm(o) for o in real):
        parts += opts
    for field in ("list_i", "list_ii", "statements"):
        parts += _values(rec.get(field))
    return " ".join(parts)


def _values(v):
    """Leaf strings of a nested record field, WITHOUT its JSON keys.

    Match-lists and statement blocks are lists of {"label": "A", "text": "..."} objects. Stringing
    the object itself puts the words "label" and "text" into the comparison, where they appear in
    every record and in no printed paper -- which read as the records carrying foreign content, on
    20 of 154 questions, when the words were put there by this function.
    """
    if isinstance(v, dict):
        out = []
        for x in v.values():
            out += _values(x)
        return out
    if isinstance(v, (list, tuple)):
        out = []
        for x in v:
            out += _values(x)
        return out
    return [str(v)] if v not in (None, "") else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", required=True)
    ap.add_argument("--pdf", help="override the source PDF")
    ap.add_argument("--report", action="store_true", help="match + verify, write CSV")
    ap.add_argument("--crop", action="store_true", help="also cut figures")
    ap.add_argument("--apply", action="store_true", help="write figures and record provenance")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--allow-unofficial", action="store_true",
                    help="permit cropping from a source that is not an official booklet")
    args = ap.parse_args()

    path = args.pdf or rc.pp("inputs", "papers", f"{args.year}.pdf")
    if not os.path.exists(path):
        print(f"no source PDF at {path}")
        return 1

    import fitz
    doc, chunks = parse_booklet(path)
    if not chunks:
        print(f"{os.path.basename(path)}: no question starts found -- is there a text layer? "
              f"({sum(len(p.get_text()) for p in doc)} text chars)")
        return 1
    code = re.search(r"Code-_?([A-Z]\d?)_?", doc[min(3, doc.page_count - 1)].get_text() or "")
    code = code.group(1) if code else "unknown"
    key = booklet_key(doc)
    print(f"{os.path.basename(path)}: {doc.page_count} pages, booklet code {code}, "
          f"{len(chunks)} questions parsed, {len(key)} answers in its own key grid")

    # Not every PDF in inputs/papers/ is an exam booklet: 2023.pdf is a chapter-wise coaching
    # compilation that reprints NEET questions under topic headings. Its diagrams are redrawn by
    # the publisher, not the board's own artwork, and its option order is its own. Cropping from it
    # would repeat in a new form the exact mistake this file exists to undo, so it is refused
    # unless asked for explicitly.
    head = " ".join((doc[0].get_text() + " " + doc[min(2, doc.page_count - 1)].get_text()).split())
    official = bool(re.search(r"Test Booklet|GENERAL INSTRUCTION|NEET \(UG\)", head))
    if not official:
        print("  NOT an official booklet (no 'Test Booklet' / 'NEET (UG)' masthead) -- "
              "likely a coaching compilation, whose diagrams are redrawn and whose option order "
              "is its own")
        if args.crop and not args.allow_unofficial:
            print("  refusing to crop figures from it; pass --allow-unofficial to override")
            args.crop = False

    recs = []
    for p in sorted(glob_records()):
        with open(p, encoding="utf-8") as fh:
            r = json.load(fh)
        if str(r.get("year")) == str(args.year):
            recs.append((p, r))
    print(f"{len(recs)} records for {args.year}")

    pairs = match([r for _, r in recs], chunks)
    by_id = {r.get("question_id"): (p, r) for p, r in recs}

    if key:
        ok, agree, total, rate = key_is_trustworthy(key, pairs)
        if ok:
            print(f"its key grid agrees with the records on {agree}/{total} answers "
                  f"({rate:.0%}) -- used as a second answer source")
        else:
            print(f"its key grid agrees with the records on only {agree}/{total} answers "
                  f"({rate:.0%}, chance is 25%) -- the grid does not belong to this question "
                  f"order, so it is IGNORED and answers are not checked against it")
            key = {}

    furniture = page_furniture(doc)
    tally = collections.Counter()
    rows = []
    stamp = datetime.date.today().isoformat()
    out_dir = rc.pp("papers", "figures", str(args.year), f"source_{code}")
    touched = {}

    for rec, chunk, score in pairs:
        qid = rec.get("question_id")
        row = {"question_id": qid, "subject": rec.get("subject"),
               "our_code_q": " ".join(rec.get("paper_codes") or []),
               "source_q_no": chunk["qno"] if chunk else "",
               "match_score": score, "has_figure_flag": bool(rec.get("has_figure")),
               "figure_cut": "", "verdict": "",
               "answer_verdict": "", "our_answer_text": "", "source_answer_text": "",
               "note": "",
               "stem_head": " ".join((rec.get("stem_en") or "").split())[:90]}
        if not chunk:
            row["verdict"] = "not_in_source"
            tally["not_in_source"] += 1
            rows.append(row)
            continue

        # option VALUES as a set -- order is code-specific and deliberately not compared
        ours = {_norm(v)[:40] for v in (rec.get("options_en") or {}).values() if _norm(v)}
        src = _norm(chunk["text"])
        missing = [o for o in ours if o and o not in src]
        row["verdict"] = "matched" if not missing else "option_text_absent_from_source"
        if missing:
            row["note"] = f"{len(missing)} of {len(ours)} option values not found on the page"
        tally[row["verdict"]] += 1

        # Cross-source answer check: our key says option K of OUR code; the booklet's own grid says
        # option J of ITS code. Compare the TEXT each one selects.
        ours_opt = str(rec.get("official_answer") or "")
        src_opt = key.get(chunk["qno"])
        src_opts = chunk_options(chunk["text"])
        # Where a diagram sits between the options, the page's text runs the figure's own labels
        # ("1 uF 2uF A B") in among them, and the extracted "option text" is really the drawing.
        # Those are reported as unreliable rather than compared, because a comparison against
        # figure labels manufactures a disagreement on a question that may be perfectly correct.
        unreliable = (len(src_opts) < 4
                      or any("" <= ch <= "" for ch in "".join(src_opts.values()))
                      or min((len(_norm(v)) for v in src_opts.values()), default=0) < 2)
        if unreliable:
            row["answer_verdict"] = "answer_not_checkable"
            row["note"] = (row["note"] or
                           f"only {len(src_opts)} of 4 options readable on the page -- a diagram "
                           f"or symbol font breaks the text order here")
            tally["answer_not_checkable"] += 1
        elif ours_opt in "1234" and ours_opt and src_opt and str(src_opt) in src_opts:
            a = _norm((rec.get("options_en") or {}).get(ours_opt))[:40]
            b = _norm(src_opts[str(src_opt)])[:40]
            row["our_answer_text"] = ((rec.get("options_en") or {}).get(ours_opt) or "")[:40]
            row["source_answer_text"] = src_opts[str(src_opt)][:40]
            if not a or not b:
                row["answer_verdict"] = "answer_text_empty"
            elif a == b or a.startswith(b[:18]) or b.startswith(a[:18]):
                row["answer_verdict"] = "answer_corroborated"
            else:
                row["answer_verdict"] = "ANSWER_DISAGREES_WITH_SOURCE"
            tally[row["answer_verdict"]] += 1
        else:
            row["answer_verdict"] = "answer_not_checkable"
            tally["answer_not_checkable"] += 1

        if args.crop and rec.get("has_figure"):
            if _is_option_image(rec, chunk):
                row["figure_cut"] = "refused"
                row["note"] = (f"options are pictures; panel order belongs to code {code}, our "
                               f"record is code {(rec.get('paper_codes') or ['?'])[0]} -- a crop "
                               f"from another code would contradict the options")
                tally["option_image_wrong_code"] += 1
            else:
                boxes = []
                for pi, r in chunk["rects"]:
                    boxes += [(pi, b) for b in _graphics(doc[pi], r, furniture)]
                if not boxes:
                    row["figure_cut"] = "no_graphic_found"
                    tally["no_graphic_found"] += 1
                else:
                    pi, box = max(boxes, key=lambda b: b[1].get_area())
                    box = fitz.Rect(box) + (-4, -4, 4, 4)
                    box &= doc[pi].rect
                    rel = os.path.join("papers", "figures", str(args.year),
                                       f"source_{code}", f"{qid}.png")
                    if args.apply:
                        os.makedirs(out_dir, exist_ok=True)
                        doc[pi].get_pixmap(clip=box, dpi=args.dpi).save(rc.pp(rel))
                        p, r = by_id[qid]
                        r["figure_path_source"] = rel
                        r.setdefault("repairs", []).append({
                            "date": stamp, "by": "scripts/paper_source_match.py",
                            "kind": "figure_cut_from_source",
                            "notes": [f"figure cut from {os.path.basename(path)} page {pi + 1} "
                                      f"(booklet code {code}, question {chunk['qno']}), matched to "
                                      f"this record at score {score}; replaces a cdn.mathpix.com "
                                      f"URL matched by wording against a different question bank, "
                                      f"which SPEC.md Section 4 forbids"]})
                        touched[qid] = (p, r)
                    row["figure_cut"] = rel
                    tally["figure_cut"] += 1
        rows.append(row)

    print()
    for k, v in tally.most_common():
        print(f"   {v:4d}  {k}")

    if args.apply and touched:
        for qid, (p, r) in touched.items():
            with open(p, "w", encoding="utf-8") as fh:
                json.dump(r, fh, ensure_ascii=False, indent=1)
                fh.write("\n")
        print(f"\nwrote {len(touched)} records and {tally['figure_cut']} figures "
              f"to {os.path.relpath(out_dir, rc.pp())}")
    elif args.crop and not args.apply:
        print("\n(no --apply: nothing written)")

    if args.report:
        out = rc.pp("exports", "review", "papers", f"SOURCE_MATCH_{args.year}.csv")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(sorted(rows, key=lambda r: (r["verdict"] == "matched", r["question_id"])))
        print(f"wrote {os.path.relpath(out, rc.pp())}")
    return 0


def glob_records():
    import glob
    return glob.glob(rc.pp("papers", "records", "Q-*.json"))


if __name__ == "__main__":
    sys.exit(main())
