#!/usr/bin/env python3
"""Prepare a NEET booklet for the page-by-page Stage B flow: page images, boundaries, crops.

    python3 scripts/extract_paper_v2.py --probe
    python3 scripts/extract_paper_v2.py --paper <pdf> --dry-run
    python3 scripts/extract_paper_v2.py --year 2022 2023 2024 --apply

WHAT THIS IS, AND WHY IT IS NOT A TEXT PARSER
---------------------------------------------
Stage B is defined page by page, the same way Stage A reads NCERT:

    B1  register the paper            page_images + text_layer
    B2  find question boundaries      ITEM = ONE PAGE -> boxes in image pixels
    (script)  crop one image per question        <- config/steps.yaml B2's own note:
                                                    "figure/option cropping are SCRIPT-side
                                                     (the question-crop step after this agent
                                                     returns boxes)"
    B3  read one question             ITEM = ONE QUESTION -> reads the QUESTION IMAGE
    B9/B9S/B10  recover, confirm and split figures

This script is that script side. It renders the pages, measures the boundaries, and cuts the crops.
It does NOT decide what a question says -- B3 does, from the image.

That distinction is the whole reason the first attempt at this file was wrong. A pure text-layer
parser reached 100% on answers and 99.8% on four-option questions and was still unsafe, because
`codebook/A2`'s rule for NCERT applies verbatim to these booklets:

    "This rule does NOT apply to superscripts, subscripts, radicals, absolute-value bars,
     inequalities, hat symbols or the degree symbol -- the text_layer regularly LOSES these even
     when its plain prose is exact."

A NEET paper is full of exactly those: 10^-7, CO2, sqrt(2), >=, 37 degrees. The text layer is the
right source for prose and the wrong source for the characters that decide a numeric answer. So the
text draft this script produces is a HINT and a cross-check for B3, never the record -- which is
also why `--dry-run` reports agreement between the two rather than claiming an accuracy figure.

HOW FIGURES ARE HANDLED, AND WHY ONE MECHANISM COVERS ALL OF THEM
-----------------------------------------------------------------
Not by pulling embedded images. Measured on one real page of NEET 2024 Code-Q2: 2 embedded images
against 212 vector paths. A chemical structure, a circuit, a ray diagram, a graph and a match-list
table in these papers are VECTOR art plus text labels -- there is no image object to pull, and
`get_images` returns the publisher's logo and nothing else of use.

Instead the question's own REGION is rendered. One mechanism then captures raster, vector,
composite and tabular figures identically, which is what "we do not need a separate flow" means in
practice: the figure crop falls out of the same geometry pass that cuts the question crop.

Two conventions are borrowed from Stage A because they are already proven there:

  * the crop is GROWN outward from the block's own box toward its neighbours, and
    `target_box_in_crop` says which part inside it is actually the subject -- a2-special-transcriber
    needs this because a tight crop loses the caption and a loose one imports the next figure;
  * figures are not described. A figure crop goes to a transcriber for its CAPTION and LABELS,
    copied exactly. Nothing in this pipeline writes a prose description of a drawing.

Bounding boxes are in IMAGE PIXELS at `lib.pdf.DEFAULT_DPI`, matching schemas/B2.json's
"[x0, y0, x1, y1] in image pixels" and the boxes every Stage A agent already returns.
"""

import argparse
import collections
import datetime
import glob
import hashlib
import json
import os
import re
import sys
import warnings

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
from lib import pdf as lib_pdf  # noqa: E402

#: THE SOURCES LIVE IN THE REPO. They used to be read from a folder in the owner's Downloads, which
#: meant the pipeline could not be handed to anyone: the corpus recorded paths like
#: `NEET_Papers/2015/NEET_2015_Code_A_official.pdf` that resolved on exactly one machine. The ten
#: booklets this corpus is built from are 25 MB in total, so they are simply kept here, and the
#: external tree is a fallback for re-extracting a booklet that has not been brought in yet.
SOURCE_ROOT = rc.source_dir("NEET_Papers")
#: Where the originals came from. Only consulted when a file is absent from SOURCE_ROOT.
EXTERNAL_ROOT = os.path.expanduser("~/Downloads/Saumya_NEET_work/NEW/NEET_Papers")


def resolve_source(relative):
    """A source PDF, from the repo if it is here and from the original tree if it is not."""
    inside = os.path.join(os.path.dirname(SOURCE_ROOT), relative)
    if os.path.exists(inside):
        return inside
    outside = os.path.join(os.path.dirname(EXTERNAL_ROOT), relative)
    if os.path.exists(outside):
        return outside
    raise FileNotFoundError(
        "%s is in neither source_papers/ nor %s. Copy the booklet into the repo -- the "
        "pipeline must not depend on one machine's Downloads folder." % (relative, EXTERNAL_ROOT))
#: The v2 corpus lives beside the old one, never on top of it. `papers/` stays as the reference the
#: new numbers are compared against; nothing here reads or writes it.
OUT = rc.corpus()
DPI = lib_pdf.DEFAULT_DPI          # 200; bboxes below are pixels at this dpi

FAMILIES = [
    ("aakash", re.compile(r"Corporate Office\s*:\s*Aakash Tower|Aakash Educational", re.I)),
    ("aakash_classic", re.compile(r"Answers?\s*&\s*Solutions", re.I)),
    ("solution_inline", re.compile(r"^\s*1\s*\.", re.M)),
]
Q_ALONE = re.compile(r"^\s*(\d{1,3})\s*[.)]\s*$")
#: A question number printed on the same line as its stem. The space after the dot is OPTIONAL:
#: 2020 Code-F1 prints `108.The average thermal energy...` with none, and requiring one lost 46 of
#: its 200 questions -- a whole block, 108 and 111-135, which looked like a source defect rather
#: than a pattern that was too strict. The lookahead for a capital or a bracket is what keeps a
#: decimal out: `1.5` does not match because `5` is a digit, while `108.The` and `19. The` both do.
Q_INLINE = re.compile(r"^\s*(\d{1,3})\s*[.)]\s*(?=[A-Z(\[])")
#: A question number printed with NO full stop. 2017 Code-A prints question 51 as a bare `51`, a
#: typesetting slip, and the question vanished into q50 -- its working became q50's solution lines.
#: A bare number is otherwise everywhere in shredded maths ("1", "9", "2" on their own rows), so it
#: is accepted ONLY as the exact next expected question number at its column's left edge -- see
#: analyse().
Q_BARE = re.compile(r"^\s*(\d{1,3})\s*$")
#: How far right of its column's leftmost line a bare number may sit and still be a question number.
#: Question numbers are flush with the column edge (2017 Code-A: q51 and q131 both at x0=315); a
#: stray digit from a fraction or a figure label sits indented under its text.
BARE_NUMBER_EDGE_PT = 3.0
#: The running page number, `- 15 -`, at the START of a line.
PAGE_NUMBER = re.compile(r"^\s*-\s*\d{1,3}\s*-")
#: A footer line's wording: Aakash's office address, or any publisher's web address.
FOOTER_TEXT = re.compile(r"Aakash|Corporate Office|www\.[a-z0-9-]+\.[a-z]{2,}", re.I)
#: A page number printed on its own in the footer band, as Vedantu does (`2`, `15`).
BARE_PAGE_NUMBER = re.compile(r"^\s*\d{1,3}\s*$")
#: ...and only this far down the page. See page_furniture().
BARE_PAGE_NUMBER_BAND = 0.95
#: ANY printed answer line, including one naming several options -- `Answer (1 & 2)* Both answers
#: are correct.` (2017 Code-A q18), `Answer (1 & 4)` (q50). ANSWER above reads one option and missed
#: these, so the question crop ran past the answer (E7V, which must never see an answer, reads that
#: crop) and the answer line was glued onto option 4's text.
ANSWER_LINE = re.compile(r"^\s*(?:Answer(?:\s*Key)?|Ans|Solution)\s*[:.]?\s*\(([^)]*)\)(\*?)", re.I)
#: ...and what its brackets must hold to count: two or more option labels and nothing else, so
#: `Solution : (Given ...)` is never read as an answer line.
MULTI_OPTION = re.compile(r"^\s*[1-4a-dA-D](?:\s*(?:&|,|and|or)\s*[1-4a-dA-D])+\s*$", re.I)
#: Option markers, by STYLE. The publishers disagree, and the disagreement is not cosmetic:
#:
#:   digits  Aakash              (1) (2) (3) (4)
#:   lower   Vedantu 2021        (a) (b) (c) (d)   under an explicit "Options:" line
#:   upper   2020 Code-F1        (A) (B) (C) (D)   while (a)-(d) are MATCH-LIST ITEMS on the same page
#:
#: The last row is why case cannot be folded. Question 18 of 2020 Code-F1 prints its List-I items as
#: `(a) Bacillus`, `(b) Thermus aquaticus` and its OPTIONS as `(A) (a)-(iii); (b)-(ii); ...`. Reading
#: both cases as options parses the list items as the answer set and corrupts the question; reading
#: digits only parsed 0 of 200 on Vedantu's 2021 booklet. So the style is MEASURED per booklet --
#: see detect_option_style() -- rather than assumed or merged.
OPTION_STYLES = {
    "digits": re.compile(r"^\s*\(([1-4])\)\s*(.*)$"),
    "lower": re.compile(r"^\s*\(([a-d])\)\s*(.*)$"),
    "upper": re.compile(r"^\s*\(([A-D])\)\s*(.*)$"),
}
OPTION_KEY = {"a": "1", "b": "2", "c": "3", "d": "4",
              "A": "1", "B": "2", "C": "3", "D": "4",
              "1": "1", "2": "2", "3": "3", "4": "4"}
#: The permissive pattern, used only where any marker will do (locating where options begin).
OPTION = re.compile(r"^\s*\(([1-4a-dA-D])\)\s*(.*)$")
OPTIONS_LABEL = re.compile(r"^\s*Options\s*:\s*$", re.I)
#: Every answer marker the corpus uses. `Answer (3*)` marks a question NTA later altered; the star is
#: preserved because it is the only in-band record of that.
#: Answer markers, in the order they are trusted. The option label may be a DIGIT or a LETTER for
#: the same reason as OPTION above -- `Answer: (c)` is how the Vedantu-distributed booklets print it,
#: and a digit-only pattern found 0 of 200 answers on 2021 Code-O1 while reporting no error.
#: `Answer (3*)` marks a question NTA later altered; the star is preserved because it is the only
#: in-band record of that.
ANSWER = [re.compile(p, re.I) for p in (
    r"^\s*Answer\s*[:.]?\s*\(([1-4a-dA-D])(\*?)\)",
    r"^\s*Answer\s*Key\s*:\s*\(([1-4a-dA-D])(\*?)\)",
    r"^\s*Solution\s*:\s*\(([1-4a-dA-D])(\*?)\)",
    r"^\s*Ans\s*[.:]\s*\(([1-4a-dA-D])(\*?)\)")]
#: `Sol` may carry no stop at all: 2017 Code-A q008 prints a bare "Sol" beside its circuit, and
#: requiring "Sol." or "Sol:" lost that whole solution. A whole word, so "Solve"/"Solid" never match.
SOLUTION_START = re.compile(r"^\s*(?:Sol\b\s*[.:]?|Solution\s*[.:]|Hide\s+solution)", re.I)
INSTRUCTIONS = re.compile(r"Important Instructions|GENERAL INSTRUCTION|Do not open this Test Booklet", re.I)
CODE_IN_HEADER = re.compile(r"\(Code[-\s_]*([A-Z]{1,2}\d?|\d{2})[-\s_]*\)", re.I)
#: Fallback when the booklet does not print its code in a running header -- 2019's paper prints only
#: "Important Instructions" on page 1. Taken from the FILE NAME, and only as a fallback, because
#: b1-paper-registrar's own rule is that a code must be confirmed from the page where it can be:
#: the real 2021 folder named a code "GAJAHA-M1" that does not exist in that year's key.
CODE_IN_FILENAME = re.compile(r"(?:Code|Set)[-\s_]*([A-Z]{1,2}\d?|\d{2})(?=[-\s_.]|$)", re.I)


def booklet_code(doc_head_text, path):
    """(code, where it came from). `header` is trusted; `filename` is a fallback worth flagging."""
    match = CODE_IN_HEADER.search(doc_head_text)
    if match:
        return match.group(1).upper(), "header"
    match = CODE_IN_FILENAME.search(os.path.basename(path))
    if match:
        return match.group(1).upper(), "filename"
    return None, "none"

#: Figure thresholds, in PDF points on the 612x792 page these booklets use. Set from the measured
#: distribution over one booklet's 152 ink bands, not guessed: inline maths (fraction bars, radical
#: overbars, table rules) clusters below 40pt tall and under 8 paths, real diagrams above both.
MIN_FIG_HEIGHT_PT = 40.0
MIN_FIG_WIDTH_PT = 40.0
MIN_FIG_PATHS = 8
LOGO_MAX_AREA_PT = 2600.0
#: An image that repeats on at least this share of a booklet's pages is page furniture -- a
#: watermark, a logo, a banner -- never a figure. Measured, not assumed: in NEET 2024 Code-Q2 the
#: Aakash watermark is image xref 818, drawn on 81 of 82 pages at the identical rect
#: (172,272)-(435,514). The first version of this script emitted it as a 263x242pt "figure" on
#: question after question, which is why 65.5% of questions appeared to carry one.
FURNITURE_PAGE_SHARE = 0.25
#: How many pages the furniture scan looks at. Bounded so one bad booklet cannot stall a whole run.
FURNITURE_SAMPLE_PAGES = 24
#: A page carrying more images than this is not a page with pictures on it -- it is a SLICED SCAN,
#: where the whole page has been cut into fragments. Measured: 2022/Set_T2 renders 148-169 image
#: fragments per page, against 1-6 on a normal booklet page. Its figure geometry is meaningless
#: (every fragment is "an image"), so it is skipped and reported, exactly like MAX_PATHS_PER_PAGE.
MAX_IMAGES_PER_PAGE = 40
#: A stroked path this long in one dimension and this thin in the other is a RULE, not a drawing: a
#: page border, a column separator, a table edge, a header underline. Measured on 2021 Code-O1,
#: whose pages carry a printed border -- four rules at (24,24,24,817), (571,24,571,817) and so on.
#: Merged, they became one band covering the entire page, and it passed every other figure test
#: (big enough, enough members, little text inside it), so 126 of 200 questions were reported as
#: carrying option panels and every crop was a full page.
RULE_LENGTH_SHARE = 0.80
RULE_THICKNESS_PT = 3.0
#: No figure covers most of a page. A band this large is a frame, a watermark or a geometry bug.
MAX_FIGURE_PAGE_SHARE = 0.60
#: A furniture rect may veto the vector paths drawn inside it only if it is SMALL -- a logo or a
#: compact watermark. Measured: 2017 Code-C and 2018 Code-AA each carry a page-sized border image
#: covering 90% of the page, correctly flagged as furniture because it repeats on every page. Letting
#: it veto by containment dropped every vector path on the page, so those booklets reported 0 figures
#: while their pages held 208 and 893 drawings respectively.
FURNITURE_VETO_MAX_SHARE = 0.25
#: A page is two-column when its line starts fall into two groups separated by a gutter at least
#: this wide, with real content on both sides. Measured: 2017 Code-C starts its left column at
#: x0 47-69 and its right at 315-338 on a 612pt page, so the gutter is ~245pt wide; a single-column
#: Aakash page spreads continuously from 48 to 183 with no gap of any size. Treating a two-column
#: page as one column makes a question's region span both columns, so its options are read out of a
#: neighbouring question: measured, 2017 Code-C parsed 78 of 179 option sets that way.
MIN_GUTTER_PT = 60.0
MIN_COLUMN_LINES = 8
#: A gutter crosses this little text, as a share of the page's busiest column position.
GUTTER_MAX_SHARE = 0.06
#: Reading order within a page: the whole left column precedes the whole right.
COLUMN_RANK = {"full": 0, "left": 0, "right": 1}
#: Two text fragments belong to the same visual ROW when their vertical extents overlap by at least
#: this share of the shorter one. Set loose enough to catch a marker and its text whose baselines
#: differ by under a point, tight enough not to merge consecutive printed lines.
ROW_OVERLAP_SHARE = 0.45
#: Only a line this short is merged into the one it shares a row with. A marker like `(1)` or a
#: stray exponent is this size; a line of prose never is, so prose lines are never glued together.
MARKER_MAX_CHARS = 6
#: A fragment this much smaller than its row's dominant type size is a super or subscript.
SCRIPT_SIZE_SHARE = 0.80
#: A horizontal rule this short is a FRACTION BAR, not a border or a table edge. A stacked fraction
#: has no linear form in a PDF text layer -- its numerator and denominator are separate rows and the
#: bar between them is a drawn path -- so a question containing one CANNOT be read from text and must
#: be read from its image. Measured on 2015 Code-A q177, whose options are L/I, L/I+1, L/I-1 and
#: (L+I)/(L-I): the numerators and denominators scattered across option boundaries and came out as
#: "I L", "I + 1 L", "I - 1 L+I", "L-I". Nothing in the text says a fraction was ever there.
FRACTION_BAR_MAX_WIDTH_PT = 60.0
FRACTION_BAR_MAX_HEIGHT_PT = 2.5
FRACTION_BAR_MIN_WIDTH_PT = 4.0
#: ...and each column carries at least this much, so a tapering right margin is not read as one.
COLUMN_MIN_SHARE = 0.30
#: How far a figure crop is grown toward its neighbours before `target_box_in_crop` is computed.
GROW_PT = 14.0
#: A question crop is padded at the top. The span begins at the question NUMBER's baseline, but a
#: stacked fraction's numerator, a radical's overbar and a superscript all sit ABOVE that line, so a
#: crop cut exactly at the baseline slices them off. Reported by the reading agents on real crops:
#: 2015 Code-A q041 lost the substrate structure in its own stem, and q164 lost the numerator of the
#: fraction after "in a radius", leaving only the bar and the denominator.
CROP_PAD_TOP_PT = 12.0
#: ...and a little at the bottom, for descenders and an option's trailing subscript.
CROP_PAD_BOTTOM_PT = 4.0
#: A page with more stroked paths than this is not a page with a diagram on it -- it is a traced
#: scan or a pathological render, and walking its paths costs minutes for nothing. Measured: a normal
#: page of these booklets holds 0-250 paths; the cap is an order of magnitude above that, so it
#: never fires on real content. The page is still read for TEXT; only its figure geometry is skipped,
#: and the skip is reported rather than silent.
MAX_PATHS_PER_PAGE = 4000


def _sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def _px(value):
    """PDF points -> pixels at DPI, the unit schemas/B2.json and every Stage A bbox use."""
    return round(value * DPI / 72.0, 1)


def document_furniture(doc):
    """Image xrefs that repeat across the booklet's pages, i.e. watermarks, logos and banners.

    A document-level measurement, because that is the only level at which "this mark is on every
    page" is visible. A per-page rule cannot tell a watermark from a diagram: both are large, both
    sit mid-page, and the watermark is the bigger of the two.
    """
    import collections as _c
    # SAMPLED, not exhaustive. `get_images(full=True)` walks a page's resource tree, and on a
    # pathological booklet that walk does not return in usable time -- measured on
    # 2022/Set_T2/Download_Now.pdf, where scanning all 27 pages never completed while every other
    # per-page call on the same file took milliseconds.
    #
    # Sampling costs nothing in accuracy for the thing being detected: a watermark is on nearly
    # every page by definition, so a spread of 24 pages finds it as surely as all 82 would. The
    # threshold is applied to the SAMPLE, not the document, so the share means the same thing.
    total = len(doc)
    if total <= FURNITURE_SAMPLE_PAGES:
        sampled = list(range(total))
    else:
        step = total / float(FURNITURE_SAMPLE_PAGES)
        sampled = sorted({int(i * step) for i in range(FURNITURE_SAMPLE_PAGES)})
    pages_with = _c.defaultdict(set)
    for index in sampled:
        for xref, _rect in image_rects(doc[index]):
            pages_with[xref].add(index)
    threshold = max(2, int(len(sampled) * FURNITURE_PAGE_SHARE))
    return {xref for xref, pages in pages_with.items() if len(pages) >= threshold}


def detect_family(doc):
    """(family, chars_per_page). `scanned` and `ocr_scan` are both refused by the extractor.

    `ocr_scan` is the case that hides: a booklet whose pages are SLICED SCANS carrying an OCR text
    layer looks like a text source by every character count, and is not one. Measured on
    2022/Set_T2/Download_Now.pdf -- 2,123 chars per page, so it passed the text test, while every
    page is cut into 150-400 image fragments and only 1 of its 200 questions could be located.

    An OCR layer is exactly what SPEC Rule 26 refuses: its characters are a machine's reading of a
    picture, so the digits and exponents that decide a NEET answer carry no more authority than the
    scan itself, while the chars-per-page count makes it indistinguishable from a real text layer
    further downstream. Refusing it here is the only place that distinction is still visible.
    """
    n = min(len(doc), 8)
    text = "".join(doc[i].get_text("text") for i in range(n))
    cpp = len(text) // max(n, 1)
    if cpp < 200:
        return "scanned", cpp
    sliced = sum(1 for i in range(n) if len(doc[i].get_image_info()) > MAX_IMAGES_PER_PAGE)
    if sliced >= max(2, n // 2):
        return "ocr_scan", cpp
    for name, pattern in FAMILIES:
        if pattern.search(text):
            return name, cpp
    return "unknown_text", cpp


def image_rects(page):
    """[(xref, Rect)] for every image on the page, from ONE call.

    `get_image_info()` returns all of them together. The obvious-looking alternative --
    `get_images()` then `get_image_rects(xref)` per image -- costs one display-list search per
    image, and a sliced-scan page carries 150+ of them: measured, that combination did not finish a
    27-page booklet, while this returns in milliseconds.
    """
    import pymupdf
    out = []
    for info in page.get_image_info(xrefs=True):
        bbox = info.get("bbox")
        if not bbox:
            continue
        out.append((info.get("xref", 0), pymupdf.Rect(bbox)))
    return out


def page_furniture(page, furniture_xrefs=frozenset()):
    """(header_y, footer_y, logo_rects) measured on THIS page, in points.

    Measured, never assumed: the running header is `- 75 -` over `NEET (UG)-2024 (Code-Q2)` and the
    publisher logo sits beside it. A2's page-coverage rule is the precedent -- furniture that is
    excluded has to be identified explicitly, or it ends up inside a crop and the crop opens with
    the publisher's branding. That is how the first cropper produced figures that looked right.
    """
    height = page.rect.height
    header_y, footer_y = 0.0, height
    removed = []
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            text = "".join(s.get("text", "") for s in line.get("spans", []))
            y0, y1 = line["bbox"][1], line["bbox"][3]
            # The page number is matched at the START of the line (`- 15 -`), never anywhere in it.
            # Searched anywhere, a chemical name near the top of a page matched: 2017 Code-A page 15
            # carries "Y-But-2-enal", whose `-2-` was read as a page number, so the header cut went
            # to y=129.7 and took q59's number -- and the question with it -- out of the page.
            if y1 < height * 0.18 and (PAGE_NUMBER.match(text) or
                                       re.search(r"NEET\s*\(UG\)", text)):
                header_y = max(header_y, y1 + 2.0)
                removed.append(text.strip())
            # The footer, by any publisher's wording. Vedantu prints `www.vedantu.com` and a bare
            # page number on one row at y=769 (2017 Code-A); matched only on Aakash's wording, that
            # row and the rule under it were cut into every crop that crosses a page break.
            # A bare number counts only in the bottom 5%: Vedantu's page number sits at y=769 of 792
            # (97%), while chemistry subscripts printed on their own row reach y=716 (90%) -- on
            # 2017 Code-A page 15 a 10% band took five of them for page numbers and cut the page.
            if y0 > height * 0.90 and (PAGE_NUMBER.match(text) or FOOTER_TEXT.search(text)
                                       or (BARE_PAGE_NUMBER.match(text)
                                           and y0 > height * BARE_PAGE_NUMBER_BAND)):
                footer_y = min(footer_y, y0 - 2.0)
                removed.append(text.strip())
    # A REPEATED image in the top band is the running header's artwork. Vedantu's booklets print a
    # logo there (2017 Code-A: xref 2264 at y 7-44 on every page, content from y 47.7) and no header
    # TEXT at all, so the text test above never fired and every page-break crop opened with the logo.
    for xref, rect in image_rects(page):
        if xref in furniture_xrefs and rect.y1 < height * 0.18:
            header_y = max(header_y, rect.y1 + 2.0)
    logos = []
    for xref, rect in image_rects(page):
        if (xref in furniture_xrefs or rect.get_area() <= LOGO_MAX_AREA_PT
                or rect.y1 <= header_y or rect.y0 >= footer_y):
            logos.append((xref, rect))
    return header_y, footer_y, logos, removed


def coverage_profile(lines, page_width, bin_pt=10.0):
    """How many text lines CROSS each x bin. The basis for finding a gutter."""
    bins = int(page_width / bin_pt) + 1
    cover = [0] * bins
    for line in lines:
        first = max(0, int(line["x0"] / bin_pt))
        last = min(bins - 1, int(line["x1"] / bin_pt))
        for index in range(first, last + 1):
            cover[index] += 1
    return cover, bin_pt


def columns(lines, page_width):
    """(gutter_x, left_bounds, right_bounds) for a two-column page, or None for one column.

    Decided from a VERTICAL PROJECTION PROFILE -- how many lines cross each x position -- not from
    where lines start. Two earlier attempts used line starts and both failed:

      * widest gap between consecutive starts: a handful of indented lines start mid-page and bridge
        the gutter, so on 2017 Code-C the largest gap was 94pt and sat in the wrong place;
      * histogram of starts with a valley test: found 3 of 16 real two-column pages and produced a
        false positive on 2024 Code-Q2, which is single-column.

    A crossing profile is robust because an indented line still does not CROSS the gutter. Measured
    on page 9 of each booklet, writing # for dense, + for sparse and . for empty:

        2017 Code-C  ....++#######################+.++##########++++++++++++++.....   two columns
        2018 Code-AA .......##########+###+++++++++.++.#############++++++#+++.....   two columns
        2019 Code-P1 ......##+#########+++.++++++..+++###############++++++++....     two columns
        2024 Code-Q2 .......++##########++++++++....++++++.........................   one column
        2021 Code-O1 .......#########+++++++.....................................     one column
        2015 Code-A  ..#################++++++++++++++++++.........................   one column

    The test is a near-empty valley in the middle of the page with substantial text on BOTH sides.
    A single column tapers to nothing on its right and has no text beyond it, so it cannot pass.
    """
    if len(lines) < MIN_COLUMN_LINES * 2:
        return None
    cover, bin_pt = coverage_profile(lines, page_width)
    peak = max(cover) if cover else 0
    if not peak:
        return None
    low = int(len(cover) * 0.35)
    high = int(len(cover) * 0.65)
    if high <= low:
        return None
    middle = cover[low:high]
    valley = min(middle)
    if valley > peak * GUTTER_MAX_SHARE:
        return None
    at = low + middle.index(valley)
    # substantial text must sit on both sides of the valley, or it is just a right margin
    left_peak = max(cover[:at]) if at else 0
    right_peak = max(cover[at + 1:]) if at + 1 < len(cover) else 0
    if min(left_peak, right_peak) < peak * COLUMN_MIN_SHARE:
        return None
    gutter = (at + 0.5) * bin_pt
    left = [l for l in lines if (l["x0"] + l["x1"]) / 2.0 < gutter]
    right = [l for l in lines if (l["x0"] + l["x1"]) / 2.0 >= gutter]
    if len(left) < MIN_COLUMN_LINES or len(right) < MIN_COLUMN_LINES:
        return None
    return (gutter,
            (min(l["x0"] for l in left), max(l["x1"] for l in left)),
            (min(l["x0"] for l in right), max(l["x1"] for l in right)))


def fragment_gutter(fragments, page_width, bin_pt=10.0):
    """The x of a two-column gutter, measured from FRAGMENT coverage, or None.

    The same projection-profile test as `columns()`, run on fragments rather than composed rows,
    because rows cannot be built until the gutter is known -- grouping a row across the gutter is
    what splices two questions together.
    """
    if len(fragments) < MIN_COLUMN_LINES * 2:
        return None
    bins = int(page_width / bin_pt) + 1
    cover = [0] * bins
    for fragment in fragments:
        first = max(0, int(fragment["x0"] / bin_pt))
        last = min(bins - 1, int(fragment["x1"] / bin_pt))
        for index in range(first, last + 1):
            cover[index] += 1
    peak = max(cover) if cover else 0
    if not peak:
        return None
    low, high = int(bins * 0.35), int(bins * 0.65)
    if high <= low:
        return None
    middle = cover[low:high]
    valley = min(middle)
    if valley > peak * GUTTER_MAX_SHARE:
        return None
    at = low + middle.index(valley)
    left_peak = max(cover[:at]) if at else 0
    right_peak = max(cover[at + 1:]) if at + 1 < bins else 0
    if min(left_peak, right_peak) < peak * COLUMN_MIN_SHARE:
        return None
    return (at + 0.5) * bin_pt


def text_lines(page, header_y, footer_y):
    """The page's text, as PDF lines, with two targeted repairs.

    PDF LINES ARE THE UNIT, not reconstructed rows. Rebuilding rows from spans was tried and made
    things materially worse: with tight leading, consecutive printed lines overlap vertically and
    merged, so 2024 Code-Q2 fell from 200 complete option sets to 87 and 2017 Code-C from 179
    questions to 123. The line structure the PDF already carries is better than anything rebuilt
    from fragments, and it is only wrong in two specific, repairable ways.

    REPAIR 1 -- a marker separated from its text. An option's `(1)` and its text are two line objects
    whose baselines differ by under a point, and the TEXT often sits slightly ABOVE its own marker:

        y0=139.38  x0=49.6   '(CH3)2C = CH -CH2 -CH3'    <- option 1's text
        y0=140.06  x0=27.1   '(1)'                        <- option 1's marker

    Ordered by y, the text comes first: it is absorbed into the stem, `(1)` collects option 2's text,
    every option shifts up one and option 4 comes out EMPTY. Measured on 2015 Code-A, that happened
    on question after question while the row counts looked correct. So a SHORT line that overlaps a
    neighbour vertically is merged into it in x order -- short, because only a marker or a stray
    exponent is ever this size, never a line of prose.

    REPAIR 2 -- super and subscripts. Spans materially smaller than their line's dominant size are
    marked `^{}` or `_{}` by whether their baseline sits above or below it, so `[Xe]4f^{7}5d^{1}6s^{2}`
    survives instead of flattening to `[Xe]4f 75d16s2`. These are the characters SPEC Rule 28 is
    about: they decide a chemistry answer, so losing them is not a formatting loss.

    WHAT NEITHER REPAIR CAN FIX: a stacked fraction. Its numerator, bar and denominator are three
    unrelated objects on different rows and there is no linear text form to recover -- see
    `fraction_bars()` and the `needs_image_read` flag. Those questions are read from the image by B3.
    """
    raw = []
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = [sp for sp in line.get("spans", []) if sp.get("text", "").strip()]
            if not spans:
                continue
            x0, y0, x1, y1 = line["bbox"]
            if y1 <= header_y or y0 >= footer_y:
                continue
            dominant = max(spans, key=lambda sp: (sp.get("size", 0.0),
                                                  sp["bbox"][2] - sp["bbox"][0]))
            parts, previous = [], None
            for span in spans:
                text = span["text"]
                if (span.get("size", 0.0) < dominant.get("size", 0.0) * SCRIPT_SIZE_SHARE
                        and text.strip()):
                    raised = (span.get("origin", (0, span["bbox"][3]))[1]
                              < dominant.get("origin", (0, dominant["bbox"][3]))[1] - 0.5)
                    text = ("^{%s}" if raised else "_{%s}") % text.strip()
                if previous is not None and span["bbox"][0] - previous > 1.2:
                    parts.append(" ")
                parts.append(text)
                previous = span["bbox"][2]
            composed = "".join(parts).strip()
            if composed:
                raw.append({"y0": y0, "y1": y1, "x0": x0, "x1": x1, "text": composed})

    # NO ROW RECONSTRUCTION. Two versions of it were tried and both made the draft worse than the
    # PDF's own line structure -- full rebuild from spans cost 2024 Code-Q2 113 of its 200 option
    # sets, and a targeted short-line merge still cost 2017 Code-C 25 questions. The marker/text
    # split those were meant to fix is real, but it is a symptom of the same thing a stacked fraction
    # is: THIS CONTENT IS NOT LINEAR TEXT. The fix is not a better parser, it is reading the image --
    # which is how Stage A reads NCERT and why that extraction is sound. See `needs_image_read`.
    raw.sort(key=lambda r: (round(r["y0"], 1), r["x0"]))
    return raw


def ink(page, header_y, footer_y, logos, furniture_xrefs=frozenset()):
    """Figure-bearing geometry: embedded images and vector paths, furniture removed.

    The watermark is excluded by XREF, not by geometry. Excluding it by rect would also drop any
    real diagram that happens to sit behind it -- and on these pages the watermark covers the exact
    middle of the text column, so that is most of them.
    """
    import pymupdf
    out = []
    page_area = page.rect.width * page.rect.height

    def page_spanning(rect):
        """A single element as big as the page is furniture -- a border, a background, a frame.

        Dropped HERE, before merging, not rejected afterwards as an oversized band. Merging is
        vertical, so one page-spanning element glues every real figure on the page into a single
        band that then fails the page-size test -- and the page reports no figures at all. Measured
        on 2015 Code-A: every page carries an element at (16,-12,596,804), larger than the 612x792
        page itself and absent from the repeated-xref furniture list, and all 56 pages came back
        with 0 figures while holding 603 drawings and 229 images between them.
        """
        return rect.get_area() >= page_area * MAX_FIGURE_PAGE_SHARE

    furniture_rects = [r for _x, r in logos]
    # only a small furniture mark may veto content drawn inside it -- see FURNITURE_VETO_MAX_SHARE
    veto_rects = [r for r in furniture_rects
                  if r.get_area() <= page_area * FURNITURE_VETO_MAX_SHARE]
    images = image_rects(page)
    if len(images) > MAX_IMAGES_PER_PAGE:
        # a sliced scan: every fragment is "an image", so figure geometry says nothing here
        return out, -len(images)
    for xref, rect in images:
        if xref in furniture_xrefs:
            continue
        if rect.y1 <= header_y or rect.y0 >= footer_y:
            continue
        if page_spanning(rect):
            continue
        if any(rect.intersects(bad) and rect.get_area() <= bad.get_area() * 1.3
               for bad in veto_rects):
            continue
        out.append(("image", pymupdf.Rect(rect)))
    drawings = page.get_drawings()
    if len(drawings) > MAX_PATHS_PER_PAGE:
        return out, len(drawings)
    page_width, page_height = page.rect.width, page.rect.height
    for drawing in drawings:
        rect = pymupdf.Rect(drawing["rect"])
        if rect.y1 <= header_y or rect.y0 >= footer_y or rect.is_empty:
            continue
        # a long thin rule is a border, separator or underline -- never a diagram
        if ((rect.width >= page_width * RULE_LENGTH_SHARE and rect.height <= RULE_THICKNESS_PT)
                or (rect.height >= page_height * RULE_LENGTH_SHARE
                    and rect.width <= RULE_THICKNESS_PT)):
            continue
        # the watermark is also stroked as vector in some booklets; a path that lands inside a known
        # furniture rect and is no bigger than it is part of that mark
        if page_spanning(rect):
            continue
        if any(bad.contains(rect) for bad in veto_rects):
            continue
        out.append(("vector", rect))
    return out, 0


def merge_bands(rects, gap=6.0):
    """Cluster ink into vertical bands: one diagram should be one region, not 200 paths.

    Vertical rather than 2-D: these pages are single-column, and a graph's curve, its axes and its
    labels share a y-range while sitting far apart in x. A 2-D clustering splits a plot from its own
    axis labels.
    """
    import pymupdf
    if not rects:
        return []
    ordered = sorted(rects, key=lambda r: r[1].y0)
    bands, kinds, current, members = [], {ordered[0][0]}, pymupdf.Rect(ordered[0][1]), 1
    for kind, rect in ordered[1:]:
        if rect.y0 <= current.y1 + gap:
            current |= rect
            kinds.add(kind)
            members += 1
        else:
            bands.append((kinds, current, members))
            kinds, current, members = {kind}, pymupdf.Rect(rect), 1
    bands.append((kinds, current, members))
    return bands


def is_figure(kinds, rect, members, lines, page_area=None):
    """Is this band a real diagram, or inline maths?

    Four tests, each answering a way the naive version was wrong:
      size      a fraction bar or radical overbar is short and thin; a diagram is not
      substance a single stroked path is a rule, not a drawing
      coverage  a band whose y-range is fully covered by text lines is the underline of the text,
                not a picture beside it -- computed as a UNION of line extents, because summing
                per-line overlaps double-counts and produced coverage above 1.0
      images    an embedded image of real size is a figure whatever its path count
    """
    # nothing that covers most of the page is a figure
    if page_area and rect.get_area() >= page_area * MAX_FIGURE_PAGE_SHARE:
        return False
    big_image = "image" in kinds and rect.get_area() > LOGO_MAX_AREA_PT
    if not big_image:
        if rect.height < MIN_FIG_HEIGHT_PT or rect.width < MIN_FIG_WIDTH_PT:
            return False
        if members < MIN_FIG_PATHS:
            return False
    spans = sorted((max(l["y0"], rect.y0), min(l["y1"], rect.y1))
                   for l in lines if l["y0"] < rect.y1 and l["y1"] > rect.y0)
    covered, cursor = 0.0, None
    for start, end in spans:
        if cursor is None or start > cursor:
            covered += end - start
            cursor = end
        elif end > cursor:
            covered += end - cursor
            cursor = end
    if not big_image and covered >= rect.height * 0.80:
        return False
    return True


def best_draft(lines, preferred):
    """Read one question, trying the booklet's usual marker style first and the others after.

    Needed because the style can change WITHIN a booklet. 2020 Code-F1 sets its Biology half with
    `(A)-(D)` options and its Physics half differently, so a single style chosen from the first 60
    questions explained 90 of 178 and left the rest with no options at all -- which reads as a
    source defect rather than as a style that stopped applying at question 91.

    A style is only accepted over the preferred one when it yields a COMPLETE set of four, so a
    match-list question cannot have its `(a)`-`(d)` list items promoted to options just because the
    real options were not found.
    """
    draft = read_text_draft(lines, preferred)
    draft["option_style_used"] = preferred
    if len(draft["options"]) == 4:
        return draft
    for style in OPTION_STYLES:
        if style == preferred:
            continue
        candidate = read_text_draft(lines, style)
        if len(candidate["options"]) == 4:
            candidate["option_style_used"] = style
            return candidate
    return draft


def detect_option_style(pages, spans, sample=60):
    """Which marker style this booklet prints its options in: digits, lower or upper.

    Measured, by trying each style over the first `sample` questions and counting how many yield
    exactly four options. The winner is the style that explains the most questions -- which is the
    only test that distinguishes 2020 Code-F1 (upper, with lowercase match-list items) from
    Vedantu's 2021 booklet (lower), since both print lowercase letters in parentheses.
    """
    scores = {}
    for style in OPTION_STYLES:
        complete = 0
        for span in spans[:sample]:
            trial = read_text_draft(span_lines(pages, span), style)
            if len(trial["options"]) == 4:
                complete += 1
        scores[style] = complete
    best = max(scores, key=lambda k: scores[k])
    return best, scores


def fraction_bars(page, top, bottom):
    """Short horizontal rules in a y band -- the drawn bars of stacked fractions.

    Their presence is the signal that this question's text layer is structurally incomplete, however
    clean the characters look. See FRACTION_BAR_MAX_WIDTH_PT.
    """
    found = []
    for drawing in page.get_drawings():
        rect = drawing["rect"]
        if rect.y1 <= top or rect.y0 >= bottom:
            continue
        if (FRACTION_BAR_MIN_WIDTH_PT <= rect.width <= FRACTION_BAR_MAX_WIDTH_PT
                and rect.height <= FRACTION_BAR_MAX_HEIGHT_PT):
            found.append([round(v, 1) for v in (rect.x0, rect.y0, rect.x1, rect.y1)])
    return found


def read_text_draft(lines, option_style="digits"):
    """Parse one question's lines into a DRAFT stem/options/answer.

    A draft, not a record: see the module docstring. B3 reads the image; this is the cross-check and
    the thing that lets `--dry-run` report where the two disagree.
    """
    stem, options, answer, starred = [], {}, None, False
    current, solution_at, answer_at = None, None, None
    answers, answer_line = [], None
    for position, line in enumerate(lines):
        text = line["text"].strip()
        if not text:
            continue
        if solution_at is None and SOLUTION_START.match(text):
            solution_at = position
        if answer is None and answer_at is None:
            hit = next((p.match(text) for p in ANSWER if p.match(text)), None)
            if hit:
                answer = OPTION_KEY.get(hit.group(1), hit.group(1))
                starred, current = bool(hit.group(2)), None
                answer_at, answers, answer_line = position, [answer], text
                continue
            # SEVERAL options accepted (`Answer (1 & 2)*`): the answer line all the same. The single
            # `official_answer` stays None -- it cannot hold two -- and every accepted option is kept
            # in `official_answers`, with the printed line verbatim in `answer_line`.
            several = ANSWER_LINE.match(text)
            if several and MULTI_OPTION.match(several.group(1)):
                answers = sorted({OPTION_KEY[c] for c in re.findall(r"[1-4a-dA-D]",
                                                                      several.group(1))})
                starred, current = bool(several.group(2)), None
                answer_at, answer_line = position, text
                continue
        if solution_at is not None:
            continue
        if OPTIONS_LABEL.match(text):
            continue                       # an explicit "Options:" heading is furniture, not a stem
        match = OPTION_STYLES[option_style].match(text)
        if match:
            current = OPTION_KEY[match.group(1)]
            options[current] = match.group(2).strip()
            continue
        if current:
            options[current] = (options[current] + " " + text).strip()
        else:
            inline = Q_INLINE.match(text)
            stem.append(text[inline.end():] if inline and position == 0 else text)
    draft = re.sub(r"\s+", " ", " ".join(stem)).strip()
    return {"stem": re.sub(r"^\d{1,3}\s*[.)]\s*", "", draft), "options": options,
            "official_answer": answer, "answer_starred": starred,
            "official_answers": answers, "answer_line": answer_line,
            "solution_at": solution_at, "answer_at": answer_at,
            "solution_lines": solution_lines(lines, solution_at),
            "unmarked_lines_after_answer": unmarked_after_answer(lines, answer_at, solution_at)}


def solution_lines(lines, solution_at):
    """The publisher's worked solution as printed lines, from its marker to the question's end.

    A DRAFT, exactly as the stem draft is: a worked solution is nothing but fractions, radicals and
    exponents, the content a text layer cannot represent, so `b3s-solution-reader` reads the
    solution crop and this is its cross-check. Kept rather than discarded because until now every
    line of it was thrown away at `if solution_at is not None: continue` while the booklets print a
    solution under most questions.

    The marker is stripped from the first line, and on the `solution_inline` family that line is
    BOTH markers -- 2019-2021 print `Solution: (4) <working>` where SOLUTION_START and ANSWER match
    the same line and `solution_at == answer_at` -- so the `(4)` is stripped too and the working
    starts ON that line, not after it.
    """
    if solution_at is None:
        return []
    out = []
    for position in range(solution_at, len(lines)):
        text = lines[position]["text"].strip()
        if position == solution_at:
            marker = SOLUTION_START.match(text)
            if marker:
                text = text[marker.end():]
            # The marker's own punctuation (`Sol. :`, `Solution: (4) -`) is stripped from the FRONT
            # only: the solution's last character is content -- a full stop, a closing bracket.
            text = re.sub(r"^\s*\(\s*[1-4a-dA-D]\s*\*?\s*\)", "", text).lstrip(" :.-\t").rstrip()
        if text:
            out.append(text)
    return out


def unmarked_after_answer(lines, answer_at, solution_at):
    """How many lines follow the printed answer with NO solution marker in between.

    A MEASUREMENT, not a solution. 2019 reports 0 solutions of 174 and 2020 38 of 178: either those
    booklets print no working, or they print it under a wording SOLUTION_START does not match. The
    two look identical in the solution count and need opposite fixes. This count tells them apart
    without guessing -- a booklet with many unmarked lines after its answers has working the marker
    misses -- so the regex can be widened from evidence, not from a hunch.
    """
    if answer_at is None or solution_at is not None:
        return 0
    return sum(1 for line in lines[answer_at + 1:] if line["text"].strip())


def two_column_share(doc, sample=16):
    """What fraction of sampled pages look two-column.

    Used to REFUSE a booklet rather than to parse it. A two-column booklet parsed as one column does
    not fail loudly -- it reads a question's options out of the neighbouring column and reports a
    number: 2017 Code-C came back with 179 questions and only 78 complete option sets, which looks
    like a figure to improve rather than a layout that was never supported.
    """
    pages = min(len(doc), sample)
    if not pages:
        return 0.0
    hits = 0
    for index in range(pages):
        page = doc[index]
        header_y, footer_y, _logos, _removed = page_furniture(page)
        lines = text_lines(page, header_y, footer_y)
        if columns(lines, page.rect.width):
            hits += 1
    return hits / float(pages)


def analyse(doc):
    """Per page: lines, figure bands and furniture. Per question: its span across pages."""
    furniture_xrefs = document_furniture(doc)
    pages = []
    for index in range(len(doc)):
        page = doc[index]
        header_y, footer_y, logos, removed = page_furniture(page, furniture_xrefs)
        lines = text_lines(page, header_y, footer_y)
        # READING ORDER. On a two-column page it is the whole left column, then the whole right --
        # not interleaved by y, which is what sorting by y alone would do and which would splice two
        # unrelated questions together. A line belongs to the column its MIDPOINT falls in, so a
        # wide figure caption does not jump columns.
        split = columns(lines, page.rect.width)
        if split:
            gutter = split[0]
            for line in lines:
                line["column"] = ("left" if (line["x0"] + line["x1"]) / 2.0 < gutter else "right")
        else:
            for line in lines:
                line["column"] = "full"
        lines.sort(key=lambda l: (COLUMN_RANK[l["column"]], round(l["y0"], 1), l["x0"]))
        rects, skipped = ink(page, header_y, footer_y, logos, furniture_xrefs)
        page_area = page.rect.width * page.rect.height
        bands = [(k, r, m) for k, r, m in merge_bands(rects)
                 if is_figure(k, r, m, lines, page_area)]
        if skipped > 0:
            print("      page %d: %d vector paths exceeds MAX_PATHS_PER_PAGE -- figure geometry "
                  "skipped for this page, text still read" % (index + 1, skipped), file=sys.stderr)
        elif skipped < 0:
            print("      page %d: %d image fragments exceeds MAX_IMAGES_PER_PAGE -- this page is a "
                  "sliced scan, figure geometry skipped, text still read"
                  % (index + 1, -skipped), file=sys.stderr)
        pages.append({"lines": lines, "bands": bands, "header_y": header_y,
                      "footer_y": footer_y, "removed": removed, "paths_skipped": skipped,
                      # A SLICED-SCAN page's text is OCR, and OCR drops content silently. Measured
                      # on 2023 Code-E3, a HYBRID booklet: pages 1-20 are real text and 21+ are
                      # sliced scans, so `detect_family` sampling the first 8 pages calls the whole
                      # booklet a text source. Question 94 then came back with options (1) and (3)
                      # only -- (2) and (4) are simply not in the text layer -- and 51 of 200
                      # questions looked like a parser fault instead of an unreadable source.
                      "text_reliable": skipped >= 0,
                      "columns": split, "width": page.rect.width, "height": page.rect.height})

    starts, seen = [], set()
    for index, page in enumerate(pages):
        if INSTRUCTIONS.search("".join(l["text"] for l in page["lines"][:12])):
            continue
        # A column's QUESTION-NUMBER edge, measured from the numbers that are printed properly. Not
        # the column's leftmost line: on 2017 Code-A page 13 a line straddling the gutter put the
        # right column's leftmost x0 at 273 while every question number there sits at 315.
        edges = {}
        for line in page["lines"]:
            if Q_ALONE.match(line["text"]) or Q_INLINE.match(line["text"]):
                edges[line["column"]] = min(edges.get(line["column"], line["x0"]), line["x0"])
        for line in page["lines"]:
            top = line["y0"]
            match = Q_ALONE.match(line["text"]) or Q_INLINE.match(line["text"])
            if not match:
                # See Q_BARE: the exact next number, flush with its column's number edge, or nothing.
                bare = Q_BARE.match(line["text"])
                expected = (max(seen) + 1) if seen else 1
                edge = edges.get(line["column"])
                if (bare and int(bare.group(1)) == expected and edge is not None
                        and line["x0"] <= edge + BARE_NUMBER_EDGE_PT):
                    match = bare
            if not match:
                continue
            # The question starts at the top of the number's ROW, not at the number: q51's first
            # stem line sits 1pt ABOVE its bare `51`, and starting at the number gave that line to
            # q50. The same holds for a PRINTED `3.` -- on 2017 Code-A, q003's, q028's and q077's
            # first stem lines sit above their numbers, so each went into the previous question's
            # solution draft, and q056's `56.` glyph tops were cut into q055's solution crop.
            height = line["y1"] - line["y0"]
            for other in page["lines"]:
                overlap = min(other["y1"], line["y1"]) - max(other["y0"], line["y0"])
                if (other["column"] == line["column"] and height > 0
                        and overlap >= ROW_OVERLAP_SHARE * min(height, other["y1"] - other["y0"])):
                    top = min(top, other["y0"])
            number = int(match.group(1))
            if not 1 <= number <= 200 or number in seen:
                continue
            seen.add(number)
            starts.append((index, line["column"], top, number))

    spans = []
    for position, (index, column, y0, number) in enumerate(starts):
        if position + 1 < len(starts):
            nxt = starts[position + 1]
            end_index, end_column, end_y = nxt[0], nxt[1], nxt[2]
        else:
            end_index, end_column, end_y = len(pages) - 1, "right", pages[-1]["height"]
        spans.append({"qno": number, "page": index, "column": column, "y0": y0,
                      "end_page": end_index, "end_column": end_column, "y1": end_y})
    return pages, spans


def split_unnumbered(pages, spans):
    """Give a question whose NUMBER was never printed its own span.

    MEASURED, NOT GUESSED: 2017 Code-A prints no `130.` -- the stem's first line, number and all, is
    missing from the booklet, and the rest of q130 ("protein with 333 amino acids ... how many
    codons will be altered?", its options, `Answer (3)` and its solution) opens the next column. With
    no number to start a span, all of it was read as part of q129's solution, and the paper had 179
    questions. A span cannot hold two printed answers, so a second `Answer (N)` IS the evidence of a
    second question. It starts at the first column or page break after the first answer -- where a
    question with a lost first line resumes -- and is numbered one after the span's own, only when
    that number is free. Without a break to start it at, the span is left whole and reported.
    """
    taken = {span["qno"] for span in spans}
    out = []
    for span in spans:
        lines = span_lines(pages, span)
        answers = [i for i, line in enumerate(lines) if ANSWER_LINE.match(line["text"])]
        if len(answers) < 2 or span["qno"] + 1 in taken:
            out.append(span)
            continue
        start = next((i for i in range(answers[0] + 1, answers[1] + 1)
                      if (lines[i]["page"], lines[i]["column"])
                      != (lines[i - 1]["page"], lines[i - 1]["column"])), None)
        if start is None:
            print("q%d: two printed answers in one span and no column break between them -- "
                  "left whole, check the booklet" % span["qno"])
            out.append(span)
            continue
        first = lines[start]
        out.append(dict(span, end_page=first["page"], end_column=first["column"], y1=first["y0"]))
        out.append(dict(span, qno=span["qno"] + 1, page=first["page"], column=first["column"],
                        y0=first["y0"], number_printed=False))
        taken.add(span["qno"] + 1)
        print("q%d: its number is not printed; split from q%d at page %d %s column"
              % (span["qno"] + 1, span["qno"], first["page"] + 1, first["column"]))
    return out


def _order_key(page_index, column, y):
    """Document reading position: page, then column, then height down that column."""
    return (page_index, COLUMN_RANK.get(column, 0), round(y, 1))


def span_lines(pages, span):
    """Every line of one question, in reading order, across pages and columns.

    Compared on reading POSITION, not on y: a question can start at the foot of the left column and
    end at the top of the right, where its last line has a SMALLER y than its first. Comparing y
    alone drops those lines, which is how a two-column question loses its options.
    """
    begin = _order_key(span["page"], span["column"], span["y0"])
    finish = _order_key(span["end_page"], span["end_column"], span["y1"])
    out = []
    for index in range(span["page"], span["end_page"] + 1):
        for line in pages[index]["lines"]:
            here = _order_key(index, line["column"], line["y0"])
            if here < begin or here >= finish:
                continue
            out.append(dict(line, page=index))
    out.sort(key=lambda l: _order_key(l["page"], l["column"], l["y0"]))
    return out


def question_parts(pages, span, clamp_above=True):
    """B2-shaped `parts`: one box per (page, column) the question occupies, in image pixels.

    A two-column question has two parts -- the foot of the left column and the head of the right --
    which is exactly what schemas/B2.json's `parts` array and its `continues_on_next` flag exist for.
    Each box is clipped to its own column's measured x range, so a crop never includes the
    neighbouring column's text.
    """
    parts = []
    begin = _order_key(span["page"], span["column"], span["y0"])
    finish = _order_key(span["end_page"], span["end_column"], span["y1"])
    for index in range(span["page"], span["end_page"] + 1):
        page = pages[index]
        split = page.get("columns")
        for column in (("left", "right") if split else ("full",)):
            if split:
                x0, x1 = split[1] if column == "left" else split[2]
                x0, x1 = max(0.0, x0 - 6.0), min(page["width"], x1 + 6.0)
            else:
                x0, x1 = 0.0, page["width"]
            top, bottom = page["header_y"], page["footer_y"]
            if _order_key(index, column, top) < begin:
                if _order_key(index, column, bottom) <= begin:
                    continue
                top = span["y0"]
            if _order_key(index, column, bottom) >= finish:
                if _order_key(index, column, top) >= finish:
                    continue
                bottom = span["y1"]
            if bottom - top < 4.0:
                continue
            # pad, but never past this page's own furniture -- and never into the PREVIOUS
            # question. The top pad exists for marks that sit above the first line (a numerator, an
            # overbar), and it reached the line above as well: 143 of 2017 Code-A's 180 question
            # crops opened with a sliced sliver of the previous question's last line. Stopped just
            # below the nearest text line wholly above this one in the same column.
            above = [l["y1"] for l in page["lines"]
                     if l["column"] == column and l["y1"] <= top + 0.5 and l["y0"] < top - 0.5]
            floor = (max(above) + 1.0) if above else page["header_y"]
            if clamp_above and top > floor:
                top = max(page["header_y"], floor, top - CROP_PAD_TOP_PT)
            else:
                # a SOLUTION span starts pre-padded at its `Answer (N)` line, which must stay in
                top = max(page["header_y"], top - CROP_PAD_TOP_PT)
            bottom = min(page["footer_y"], bottom + CROP_PAD_BOTTOM_PT)
            parts.append({"column": column, "page": index,
                          "bbox": [_px(x0), _px(top), _px(x1), _px(bottom)]})
    return parts


def question_figures(pages, span, lines, draft):
    """Figure regions for one question, each with a grown crop and its target box.

    Clipped at `Sol.`: a worked solution routinely draws its own diagram, and harvesting that as the
    question's figure is the easiest error to make here.
    """
    import pymupdf
    option_tops = [l["y0"] for l in lines if OPTION.match(l["text"].strip())]
    first_option = min(option_tops) if option_tops else None
    # Where the QUESTION stops and the worked solution begins. `Answer (N)` is the anchor, not
    # `Sol.`: the answer line always precedes the solution, and a solution's own diagram routinely
    # starts a few points ABOVE the `Sol.` label because the drawing sits beside it -- measured on
    # 2024 Code-Q2 q50, whose solution figure begins at y=515 while `Sol.` sits at y=529.5. Anchored
    # on `Sol.` with a top-edge test, that figure was emitted as the question's own option panel.
    cut_page = cut_y = None
    for key in ("answer_at", "solution_at"):
        position = draft.get(key)
        if position is not None and position < len(lines):
            page_index, y = lines[position]["page"], lines[position]["y0"]
            if cut_page is None or (page_index, y) < (cut_page, cut_y):
                cut_page, cut_y = page_index, y

    found = []
    for index in range(span["page"], span["end_page"] + 1):
        page = pages[index]
        for kinds, rect, _members in page["bands"]:
            if index == span["page"] and rect.y1 <= span["y0"]:
                continue
            if index == span["end_page"] and rect.y0 >= span["y1"]:
                continue
            # A band that straddles the cut is assigned by where MOST of it lies, so a drawing that
            # starts just above the `Answer` line but belongs to the solution is still excluded.
            midpoint = (rect.y0 + rect.y1) / 2.0
            if cut_page is not None and (index > cut_page
                                         or (index == cut_page and midpoint >= cut_y)):
                continue
            if first_option is not None and index == span["page"]:
                role = "stem_figure" if rect.y1 <= first_option else "option_panels"
            else:
                role = "stem_figure"
            grown = pymupdf.Rect(max(rect.x0 - GROW_PT, 0), max(rect.y0 - GROW_PT, page["header_y"]),
                                 min(rect.x1 + GROW_PT, page["width"]),
                                 min(rect.y1 + GROW_PT, page["footer_y"]))
            found.append({
                "page": index,
                "role": role,
                "kinds": sorted(kinds),
                # the crop that gets rendered, grown toward neighbours as Stage A does
                "crop_bbox": [_px(grown.x0), _px(grown.y0), _px(grown.x1), _px(grown.y1)],
                # and which part of that crop is actually this figure
                "target_box_in_crop": [_px(rect.x0 - grown.x0), _px(rect.y0 - grown.y0),
                                       _px(rect.x1 - grown.x0), _px(rect.y1 - grown.y0)],
            })
    return found


def stitch_vertical(pieces, out_path):
    """Join a question's parts top to bottom into one image, and remove the pieces.

    The parts are already in reading order -- page by page, and within a page the whole left column
    before the whole right -- so stacking them is the order a reader meets them. They are joined on a
    white ground at the width of the widest piece, centred, with a thin gap so a reader can see where
    the break was rather than being shown a seam that looks like printing.
    """
    from PIL import Image
    images = []
    for piece in pieces:
        if os.path.exists(piece):
            images.append(Image.open(piece).convert("RGB"))
    if not images:
        return None
    gap = 10
    width = max(i.width for i in images)
    height = sum(i.height for i in images) + gap * (len(images) - 1)
    canvas = Image.new("RGB", (width, height), "white")
    y = 0
    for n, image in enumerate(images):
        canvas.paste(image, ((width - image.width) // 2, y))
        y += image.height + gap
    canvas.save(out_path)
    for image in images:
        image.close()
    for piece in pieces:
        if os.path.exists(piece):
            os.remove(piece)
    return out_path


#: Everything one booklet's SCRIPTS produce, by where it lands. A fresh extraction clears it first.
BOOKLET_DIRS = ("crops", "figures", "figures_agent", "solutions", "pages")
#: Agent steps whose items are `<paper_id>__q...`. NOT cleared by default: an agent read costs a
#: dispatch and re-extracting does not change the question it read -- the handover's own rule is
#: that the 358 existing solves must not be re-run for cosmetics. Cleared only with
#: `--clear-agent-reads`, for when the crops themselves changed enough to invalidate the reads.
BOOKLET_STEPS = ("B3V", "B3S", "B3F", "B6V", "QSUBJ", "QCHAP", "QTOPIC", "E7V")
#: ECAT packets mix questions from several booklets, so they cannot be cleared per booklet. They are
#: cleared whole: a packet carrying an old read of one question is stale for every question in it.
CORPUS_STEPS = ("ECAT",)


def clear_previous(out_root, paper_id, agent_reads=False):
    """Delete what an earlier run's scripts produced for this booklet, so this run's output is fresh.

    The owner's rule: whatever runs produces FRESH data -- JSON, crops, exports -- and the previous
    data is removed rather than left beside it. Re-cut crops beside an old JSON is a booklet
    assembled from two runs that no file says were mixed. Agent answers are removed only when
    `agent_reads` is set (see BOOKLET_STEPS). Returns the number of paths removed.
    """
    import shutil
    removed = []
    for name in BOOKLET_DIRS:
        removed.append(os.path.join(out_root, name, paper_id))
    removed += [os.path.join(out_root, "papers", "%s.json" % paper_id),
                os.path.join(out_root, "exports", "csv", "%s.csv" % paper_id),
                os.path.join(out_root, "exports", "html", "%s.html" % paper_id)]
    for step in (BOOKLET_STEPS if agent_reads else ()):
        for kind in ("work", "out"):
            removed += glob.glob(rc.pp("steps", step, kind, "%s__*" % paper_id))
    for step in (CORPUS_STEPS if agent_reads else ()):
        for kind in ("work", "out"):
            removed += glob.glob(rc.pp("steps", step, kind, "*"))
    count = 0
    for target in removed:
        if os.path.isdir(target):
            shutil.rmtree(target)
            count += 1
        elif os.path.exists(target):
            os.remove(target)
            count += 1
    return count


def previous_cdn(out_root, paper_id):
    """{relative image path: {"url", "sha256"}} from this booklet's previous JSON, before it is cleared.

    THE FRESH JSON MUST NOT COST A RE-UPLOAD. Clearing the old record also clears every CDN link on
    it, and re-uploading bytes the CDN already holds puts a second copy there under a new URL --
    the NCERT side measured exactly this before it carried URLs forward by SHA. So the links are
    read here and re-attached after the new crops are cut, ONLY where the new file's sha256 matches:
    a crop whose pixels changed gets no link and is uploaded fresh by upload_paper_assets.py.
    """
    path = os.path.join(out_root, "papers", "%s.json" % paper_id)
    links = {}
    if not os.path.exists(path):
        return links
    try:
        with open(path, encoding="utf-8") as fh:
            old = json.load(fh)
    except ValueError:
        return links
    for question in old.get("questions") or []:
        for rel, entry in (question.get("cdn") or {}).items():
            if entry.get("url") and entry.get("sha256"):
                links[rel] = entry
    return links


def cut_point(lines, draft):
    """(page, column, y0) of the line that ENDS the question: the printed `Answer (N)` or the
    solution marker, whichever comes first in reading order. None when neither is printed.

    The same anchor question_figures() uses, for the same measured reason: `Answer (N)` always
    precedes the solution, while a solution's drawing can start above its own `Sol.` label.
    """
    best = None
    for key in ("answer_at", "solution_at"):
        position = draft.get(key)
        if position is None or position >= len(lines):
            continue
        line = lines[position]
        here = (line["page"], line["column"], line["y0"])
        if best is None or _order_key(*here) < _order_key(*best):
            best = here
    return best


def extract(path, write=False, out_root=None, render_pages=False, keep_previous=False,
            clear_agent_reads=False):
    import pymupdf
    doc = pymupdf.open(path)
    family, cpp = detect_family(doc)
    head = "".join(doc[i].get_text("text") for i in range(min(3, len(doc))))
    code, code_from = booklet_code(head, path)
    year = re.search(r"NEET\s*\(?UG\)?[-\s]*(20\d\d)", head) or re.search(r"(20\d\d)", path)
    meta = {
        "source_pdf": os.path.relpath(path, os.path.dirname(SOURCE_ROOT)),
        "sha256_16": _sha(path), "family": family, "chars_per_page": cpp, "pages": len(doc),
        "booklet_code": code,
        # Recorded, not assumed: a code read off a filename has not been confirmed by the page, and
        # b1-paper-registrar would set trust "unsure" for exactly this case.
        "booklet_code_from": code_from,
        "year": int(year.group(1)) if year else None,
        "dpi": DPI, "bbox_unit": "px",
        "extracted_at": datetime.datetime.now().strftime("%Y-%m-%d"),
        "extractor": "code/extract_paper_v2.py",
    }
    # Two-column booklets are now PARSED, not refused -- columns() measures the gutter and
    # question_parts() emits one box per (page, column). The share is still recorded, because a
    # booklet's column count is the first thing to check when its numbers look wrong.
    share = two_column_share(doc)
    meta["two_column_share"] = round(share, 2)
    meta["layout"] = "two_column" if share >= 0.5 else "single_column"
    if family in ("scanned", "ocr_scan"):
        doc.close()
        return meta, [], []

    pages, spans = analyse(doc)
    spans = split_unnumbered(pages, spans)
    option_style, style_scores = detect_option_style(pages, spans)
    meta["option_style"] = option_style
    meta["option_style_scores"] = style_scores
    paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
    questions, b2_pages = [], collections.defaultdict(list)

    for span in spans:
        lines = span_lines(pages, span)
        draft = best_draft(lines, option_style)
        figures = question_figures(pages, span, lines, draft)
        # THE QUESTION CROP STOPS AT THE PRINTED ANSWER. It used to run to the next question, so it
        # carried `Answer (N)` and the whole worked solution -- and E7V, which must never see an
        # answer, is handed this crop. Clipped at the answer line (less the bottom pad, so the pad
        # does not pull the top of `Answer` back in), the crop is the question and nothing after.
        cut = cut_point(lines, draft)
        question_span = span
        solution_span = None
        if cut:
            question_span = dict(span, end_page=cut[0], end_column=cut[1],
                                 y1=cut[2] - CROP_PAD_BOTTOM_PT)
            if draft.get("solution_at") is not None:
                # ...and the SOLUTION crop starts exactly there, at the answer line's top (the top
                # pad is pre-subtracted the same way), and runs to where the question span ends:
                # the next question's first line, across a page or column break if it does.
                # Its END is the next question's first line, less the bottom pad: padding past that
                # line pulled the top half of the next question's stem into the crop (seen on the
                # first synthetic test), and a solution crop must hold nothing of the next question.
                solution_span = dict(span, page=cut[0], column=cut[1], y0=cut[2] + CROP_PAD_TOP_PT,
                                     y1=span["y1"] - CROP_PAD_BOTTOM_PT)
        parts = question_parts(pages, question_span)
        solution = question_parts(pages, solution_span, clamp_above=False) if solution_span else []
        touched = {p["page"] for p in parts} or {span["page"]}
        text_reliable = all(pages[i].get("text_reliable", True) for i in touched)

        # WHY THIS QUESTION MAY NEED READING FROM ITS IMAGE. Each reason is a structural fact about
        # the source, not a guess: a stacked fraction has no linear text form, a sliced-scan page's
        # text is OCR, and an option set that is short, duplicated or incomplete cannot be the
        # printed one. B3 reads the crop for these; the draft is not a cross-check for them.
        reasons = []
        if not text_reliable:
            reasons.append("page is a sliced scan: its text is OCR")
        bars = []
        for part in parts:
            page_obj = doc[part["page"]]
            top = part["bbox"][1] * 72.0 / DPI
            bottom = part["bbox"][3] * 72.0 / DPI
            bars += fraction_bars(page_obj, top, bottom)
        if bars:
            reasons.append("%d stacked fraction bar(s): numerator and denominator are separate rows"
                           % len(bars))
        values = [v.strip() for v in draft["options"].values()]
        if len(draft["options"]) < 4:
            reasons.append("only %d of 4 options found" % len(draft["options"]))
        if any(not v for v in values):
            reasons.append("an option came out empty")
        if values and len(set(values)) < len(values):
            reasons.append("two options are identical as read")
        if values and max(len(v) for v in values) <= 3:
            reasons.append("every option is 3 characters or fewer: likely symbols or pictures")
        record = {
            "paper_id": paper_id, "qno": span["qno"],
            "year": meta["year"], "booklet_code": meta["booklet_code"],
            "page": span["page"] + 1,
            "parts": parts,
            # B3 reads this image. The draft below is a cross-check, never the record.
            "question_image": os.path.join("crops", paper_id, "q%03d.png" % span["qno"]),
            "text_layer_draft": draft,
            # False when any page this question sits on is a sliced scan: its text is OCR, so the
            # draft above is not a cross-check for B3, it is a second guess. B3 must read the image.
            "text_layer_reliable": text_reliable,
            "needs_image_read": bool(reasons),
            "needs_image_read_why": reasons,
            "fraction_bars": bars,
            "figures": figures,
            "figure_images": [],
            # The publisher's worked solution as an IMAGE -- b3s-solution-reader reads this, and
            # `text_layer_draft.solution_lines` is only its cross-check. One box per (page, column)
            # it occupies, stitched in reading order, so a solution that runs onto the next page is
            # never read as whole when only its first half was cut.
            "solution_image": (os.path.join("solutions", paper_id, "q%03d.png" % span["qno"])
                               if solution else None),
            "solution_parts": solution,
            "source_pdf": meta["source_pdf"],
            # False only for a question split out by split_unnumbered(): its number -- and the
            # stem line it sat on -- is missing from the booklet itself.
            "number_printed": span.get("number_printed", True),
        }
        for part in parts:
            b2_pages[part["page"]].append({"qno": span["qno"],
                                           "parts": [{"column": part["column"],
                                                      "bbox": part["bbox"]}],
                                           "continues_on_next": len(parts) > 1
                                           and part is not parts[-1]})
        questions.append(record)

    carried = previous_cdn(out_root, paper_id) if write else {}
    if write and not keep_previous:
        cleared = clear_previous(out_root, paper_id, agent_reads=clear_agent_reads)
        if cleared:
            print("      %s: removed %d path(s) from the previous run" % (paper_id, cleared),
                  file=sys.stderr)

    if write:
        # Every crop of this booklet in ONE pass over ONE open document. Per-crop opening of a
        # 70-to-85-page PDF does not scale: three years of every code is ~13,000 crops, and the
        # per-crop version was still inside its first booklet after three minutes at full CPU.
        jobs, stitch = [], []

        def queue(parts, rel):
            """Queue one stitched image cut from `parts`, written to `rel` under the corpus."""
            out = os.path.join(out_root, rel)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            if len(parts) == 1:
                jobs.append((parts[0]["page"] + 1, parts[0]["bbox"], out))
                return
            # A QUESTION THAT SPANS A PAGE OR COLUMN BREAK NEEDS ALL ITS PARTS. Cropping only the
            # first cuts the question off mid-way: 2015 Code-A q138 runs from the foot of page 36
            # onto page 37, and the first-part-only crop ended after option (1), so the agent could
            # not see options 2-4 and they came back blank. 55 of that booklet's 177 questions span
            # more than one part, which is the single largest source of blank options in the
            # corpus. A solution is cut by the same rule, for the same reason.
            pieces = []
            for n, part in enumerate(parts):
                piece = out.replace(".png", ".part%d.png" % n)
                jobs.append((part["page"] + 1, part["bbox"], piece))
                pieces.append(piece)
            stitch.append((out, pieces))

        for record in questions:
            if record["parts"]:
                queue(record["parts"], record["question_image"])
            if record["solution_parts"]:
                queue(record["solution_parts"], record["solution_image"])
            for n, figure in enumerate(record["figures"], 1):
                rel = os.path.join("figures", paper_id,
                                   "q%03d_%s_%d.png" % (record["qno"], figure["role"], n))
                out = os.path.join(out_root, rel)
                os.makedirs(os.path.dirname(out), exist_ok=True)
                jobs.append((figure["page"] + 1, figure["crop_bbox"], out))
                figure["image"] = rel
                record["figure_images"].append(rel)
        if jobs:
            # ...with the booklet's repeated images (watermark, logo) blanked: a screenshot that
            # reaches the JSON or the page carries the publisher's print and nothing else.
            lib_pdf.crop_boxes(path, jobs, dpi=DPI, unit="px",
                               hide_xrefs=document_furniture(doc))
        for out, pieces in stitch:
            stitch_vertical(pieces, out)
        if carried:
            from lib import cdn
            for record in questions:
                links = {}
                for rel in cdn.image_paths(record):
                    entry = carried.get(rel)
                    local = os.path.join(out_root, rel)
                    if entry and os.path.exists(local) and cdn.sha256(local) == entry["sha256"]:
                        links[rel] = entry
                if links:
                    record["cdn"] = links
                    cdn.write_url_fields(record)
        if render_pages:
            for index in sorted({p["page"] for q in questions for p in q["parts"]}):
                out = os.path.join(out_root, "pages", paper_id, "p%03d.png" % (index + 1))
                os.makedirs(os.path.dirname(out), exist_ok=True)
                lib_pdf.render_page_to_png(path, index + 1, dpi=DPI, out_path=out)

    b2 = [{"page": index + 1, "questions": qs,
           "top_continues_from_previous": {"left": False, "right": False},
           "note": "boundaries measured from the text layer; this source has one full-width column"}
          for index, qs in sorted(b2_pages.items())]
    doc.close()
    return meta, questions, b2


def probe():
    import pymupdf
    paths = sorted(set(glob.glob(os.path.join(SOURCE_ROOT, "*", "*.pdf")) +
                       glob.glob(os.path.join(SOURCE_ROOT, "*", "*", "*.pdf"))))
    rows, by_hash, scanned = collections.Counter(), {}, []
    for path in paths:
        digest = _sha(path)
        if digest in by_hash:
            rows["duplicate_bytes"] += 1
            continue
        by_hash[digest] = path
        try:
            doc = pymupdf.open(path)
            family, _ = detect_family(doc)
            doc.close()
        except Exception:
            rows["unreadable"] += 1
            continue
        rows[family] += 1
        if family in ("scanned", "ocr_scan"):
            scanned.append(os.path.relpath(path, SOURCE_ROOT))
    print("%d pdf(s), %d unique by content\n" % (len(paths), len(by_hash)))
    for family, count in rows.most_common():
        print("   %-18s %d" % (family, count))
    print("\n%d scanned booklet(s) are SKIPPED -- a scan needs OCR, and mixing OCR with a text\n"
          "layer is how the first 2022 corpus ended up at 75%%." % len(scanned))
    return 0


def pick_booklets(paths):
    """One booklet per (year, code): the same file arrives under several names, byte-identical.

    Deduplicated by SIZE first and only then by content hash. 74 of the corpus's 211 files are exact
    duplicates (`Download_Here.pdf` beside the same bytes under their real name), and two files of
    different sizes can never be identical -- so grouping by size costs a stat() and removes almost
    all of the hashing. Hashing every file up front cost about 4 seconds each over ~150 candidates,
    which was most of the wall time of a three-year run before any question was read.
    """
    import pymupdf
    by_size = collections.defaultdict(list)
    for path in paths:
        try:
            by_size[os.path.getsize(path)].append(path)
        except OSError:
            continue
    unique = []
    for size, group in by_size.items():
        if len(group) == 1:
            unique.append(group[0])
            continue
        seen_hashes = {}
        for path in sorted(group):
            digest = _sha(path)
            if digest not in seen_hashes:
                seen_hashes[digest] = path
                unique.append(path)

    best = {}
    for path in sorted(unique):
        try:
            doc = pymupdf.open(path)
            family, cpp = detect_family(doc)
            code, _from = booklet_code("".join(doc[i].get_text("text")
                                               for i in range(min(3, len(doc)))), path)
            doc.close()
        except Exception:
            continue
        if family in ("scanned", "ocr_scan"):
            continue
        if not code:
            # A BOOKLET WITH NO READABLE CODE IS REFUSED, not filed under `<year>_NA`. Measured on the
            # full Drive tree: 2021 holds Download_Now.pdf and four subject-wise "with Solutions"
            # files, none printing a code in a header or a filename. All five became paper id
            # `2021_NA` and overwrote one another's JSON and crops, the last one silently winning.
            # A booklet that cannot be told apart from its neighbours cannot be audited, so it is
            # reported and skipped -- the same rule as a scan.
            print("   skipped, no booklet code in header or filename: %s"
                  % os.path.relpath(path, os.path.dirname(SOURCE_ROOT)), file=sys.stderr)
            continue
        # Either separator: on Windows the glob returns backslashes, and a `/`-only pattern made every
        # year "?" -- so 2022's Code-Q1 and 2024's Code-Q1 shared one key and one of them was dropped.
        year = re.search(r"[\\/](20\d\d)[\\/]", path)
        key = (year.group(1) if year else "?", code or os.path.basename(path))
        if key not in best or cpp > best[key][0]:
            best[key] = (cpp, path)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", action="store_true")
    ap.add_argument("--paper")
    ap.add_argument("--year", nargs="*")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--render-pages", action="store_true",
                    help="also render full page images (B1 page_images); large, off by default")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--clear-agent-reads", action="store_true",
                    help="also delete this booklet's agent answers (B3V, B3S, B6V, ...) -- only "
                         "when the crops changed enough that the reads describe other pictures")
    ap.add_argument("--keep-previous", action="store_true",
                    help="do NOT clear the booklet's earlier crops, JSON, exports and agent reads "
                         "first (default: every run starts fresh)")
    args = ap.parse_args()

    if args.probe:
        return probe()
    if not (args.apply or args.dry_run):
        ap.error("pass --probe, --dry-run or --apply")

    if args.paper:
        paths = [args.paper]
    elif args.year:
        paths = []
        for year in args.year:
            paths += sorted(set(glob.glob(os.path.join(SOURCE_ROOT, year, "*.pdf")) +
                                glob.glob(os.path.join(SOURCE_ROOT, year, "*", "*.pdf"))))
    else:
        ap.error("pass --paper or --year")

    print("scanning %d candidate file(s) to pick one booklet per (year, code)..." % len(paths),
          file=sys.stderr)
    best = pick_booklets(paths)
    out_root = rc.pp(*OUT)
    print("%d booklet(s) with a text layer, one per (year, code)\n" % len(best))
    print("%-5s %-4s %5s %6s %7s %7s %7s %7s %7s %7s" %
          ("year", "code", "q", "4-opt", "answers", "figs", "stem", "panels", "img?", "ocr"))
    total = collections.Counter()
    for n, (key, (_cpp, path)) in enumerate(sorted(best.items()), 1):
        if args.limit and n > args.limit:
            break
        print("   [%d/%d] %s %s  %s" % (n, len(best), key[0], key[1], os.path.basename(path)),
              file=sys.stderr)
        meta, questions, b2 = extract(path, write=args.apply, out_root=out_root,
                                      render_pages=args.render_pages,
                                      keep_previous=args.keep_previous,
                                      clear_agent_reads=args.clear_agent_reads)
        four = sum(1 for q in questions if len(q["text_layer_draft"]["options"]) == 4)
        answers = sum(1 for q in questions if q["text_layer_draft"]["official_answer"])
        figs = sum(len(q["figures"]) for q in questions)
        stem = sum(1 for q in questions for f in q["figures"] if f["role"] == "stem_figure")
        panels = sum(1 for q in questions for f in q["figures"] if f["role"] == "option_panels")
        withfig = sum(1 for q in questions if q["figures"])
        unreliable = sum(1 for q in questions if not q["text_layer_reliable"])
        needs_image = sum(1 for q in questions if q["needs_image_read"])
        print("%-5s %-4s %5d %6d %7d %7d %7d %7d %7d %7s" %
              (key[0], key[1], len(questions), four, answers, figs, stem, panels, needs_image,
               ("%d OCR" % unreliable) if unreliable else ""))
        for field, value in (("booklets", 1), ("questions", len(questions)), ("four", four),
                             ("answers", answers), ("figures", figs),
                             ("questions_with_figures", withfig),
                             ("text_unreliable", unreliable),
                             ("needs_image_read", needs_image)):
            total[field] += value
        if args.apply:
            base = os.path.join(out_root, "papers")
            os.makedirs(base, exist_ok=True)
            paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
            with open(os.path.join(base, "%s.json" % paper_id), "w", encoding="utf-8") as fh:
                json.dump({"meta": meta, "questions": questions, "b2_boundaries": b2},
                          fh, ensure_ascii=False, indent=1)

    q = max(total["questions"], 1)
    print("\n%d booklets, %d questions" % (total["booklets"], q))
    print("   four options in the text draft : %d (%.1f%%)" % (total["four"], 100.0 * total["four"] / q))
    print("   official answer printed        : %d (%.1f%%)" % (total["answers"], 100.0 * total["answers"] / q))
    print("   questions carrying a figure    : %d (%.1f%%)  across %d figure crops"
          % (total["questions_with_figures"], 100.0 * total["questions_with_figures"] / q,
             total["figures"]))
    print("   must be read from the image     : %d (%.1f%%) -- B3 reads the crop; the text layer\n"
          "                                     cannot represent what these questions print"
          % (total["needs_image_read"], 100.0 * total["needs_image_read"] / q))
    if total["text_unreliable"]:
        print("   questions on a sliced-scan page : %d (%.1f%%) -- their text is OCR and the draft "
              "is NOT\n                                    a cross-check; B3 must read the crop"
              % (total["text_unreliable"], 100.0 * total["text_unreliable"] / q))
    print("\n   The option/answer figures describe the TEXT DRAFT only. B3 reads the question image\n"
          "   and is the record: the text layer loses superscripts, subscripts and radicals, which\n"
          "   is exactly where a NEET numeric answer is decided (codebook A2's rule).")
    if args.dry_run:
        print("(dry run -- nothing written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
