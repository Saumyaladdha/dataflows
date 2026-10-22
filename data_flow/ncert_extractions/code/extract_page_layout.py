#!/usr/bin/env python3
"""Reads one NCERT chapter PDF's TEXT LAYER and writes the exact printed layout: every block,
its position on the page, and the formatted runs inside it.

    python3 scripts/extract_ncert_layout.py BIO11L-ch01

Writes `ncert/layout/<BOOK>-ch<NN>.json` -- one record per page, elements in reading order,
each carrying `bbox` as FRACTIONS of the page, a `column`, a `role`, and `runs` that preserve
bold / italic / small-caps / superscript / subscript / colour exactly as printed.

This is the deterministic twin of step A2L. A2L has an agent MEASURE a page image; this reads
the same facts out of the PDF itself, which is exact, free, and repeatable. 96% of the NCERT
pages in `inputs/ncert/` carry a text layer (measured 2026-10-22), so this is the primary path
and A2L is the fallback for the 7 chapter files that are pure scans.

THREE THINGS THAT ARE WRONG IF YOU DO THE OBVIOUS, each measured on a real page:

1. `flags & 16` IS NOT BOLD IN THESE BOOKS. NCERT's bold face is `Bookman-Demi`, and PyMuPDF
   reports flag-bold False for it. On BIO11L ch01 p003 the defined term `biodiversity` is set in
   Bookman-Demi; trusting the flag renders it as ordinary body text and the one word the
   paragraph exists to define stops looking defined. Weight is read from the font NAME.

2. NCERT FAKES SMALL CAPS WITH TWO TYPE SIZES. The heading `1.1 DIVERSITY IN THE LIVING WORLD`
   is stored as `D`(13.0pt) `IVERSITY`(9.1pt) `IN`(9.1) `THE`(9.1) `L`(13.0) `IVING`(9.1) ...
   Concatenating the spans gives real capitals at two sizes, which renders as ransom-note text.
   `_smallcaps` detects the alternation and rebuilds the words -- large letters are capitals,
   small letters are lowercase -- so the run carries `Diversity in the Living World` plus
   `sc: true`, and CSS `font-variant: small-caps` reproduces the printed line.

3. A SPAN IS NOT A RUN. Justified text breaks one sentence across many spans with identical
   formatting; emitting one run per span produces hundreds of needless runs and lets a word
   split across two of them. Runs are merged on (bold, italic, smallcaps, script, colour).

4. PYMUPDF DOES NOT RETURN A BLOCK'S LINES IN VISUAL ORDER. On BIO11L ch3 p001 the chapter
   title block comes back as line 0 `PLANT KINGDOM` (y 292.8) then line 1 `CHAPTER  3`
   (y 253.9), so joining them in the order given stored the chapter title as
   `Plant Kingdom Chapter 3` -- the two lines of the opener printed backwards, in the one
   element a reader looks at first. Lines are sorted by baseline before they are joined.

5. THE PAGE FURNITURE IS NOT A PARAGRAPH. The head of a Class 11 page extracts as ONE block
   reading `24 Biology` (the folio and the running head are set on the same line at opposite
   ends of the measure), and the Class 12 folio is a separate block reading `42` sitting in
   the outer margin two-thirds of the way down. Left alone, the first became a body paragraph
   and the second a one-word paragraph in the middle of the chapter. They are split out into
   `page_number` and `running_header` elements, and the folio is ALSO promoted to a page-level
   `printed_page_number` -- which is the number NCERT prints, the number a PYQ's evidence
   citation has to quote, and the number that decides whether a page is a recto or a verso.

6. MOST "IMAGES" ON AN NCERT PAGE ARE NOT FIGURES. Every page carries the full-page scan
   ground (0.99 x 1.00 of the sheet) and the standing `(c) NCERT / not to be republished`
   watermark (0.76 x 0.59, at the same bbox on all 14 pages of BIO11L ch3); body pages also
   carry the header strip art. Emitting those three as figures reproduces the page inside
   itself and pastes the watermark in as artwork. They are classified as `page_furniture`
   so a renderer can draw them as furniture and a figure cutter can skip them.
"""

import argparse
import collections
import json
import os
import re
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
import book_design as design_lib  # noqa: E402

BOLD_NAMES = ("Bold", "Demi", "Black", "Heavy", "Semibold")
ITALIC_NAMES = ("Italic", "Oblique")

# Where a book id's pages live. <SUBJECT><CLASS><EDITION>, edition L=latest O=older.
#
# The folder names say what the thing IS, which is the whole point of the 2026-10-22 re-layout:
# `source_pdfs/new/class_11/biology/` can be read at a glance, where the old
# `inputs/ncert/latest/Class_11th/Biology/` needed you to know that "latest" meant the
# rationalised edition everyone calls "new".
SUBJECT_DIR = {"BIO": "biology", "CHE": "chemistry", "PHY": "physics"}
EDITION_DIR = {"L": "new", "O": "old"}
SOURCE_ROOT = "source_pdfs"


def pdf_path(book_id, chapter_num):
    """The chapter PDF for a book id, trying every filename convention the corpus uses."""
    subject = SUBJECT_DIR[book_id[:3]]
    class_dir = "class_%s" % book_id[3:5]
    edition = EDITION_DIR[book_id[5]]
    base = os.path.join(SOURCE_ROOT, edition, class_dir, subject)
    if not os.path.isdir(base):
        raise SystemExit("no source folder %s (book %s)" % (base, book_id))
    pretty = {"biology": "Bio", "chemistry": "Chem", "physics": "Phy"}[subject]
    names = ["Chapter_%d.pdf" % chapter_num]
    if edition == "old":
        names += ["Old_ncert_%s_Chapter_%d.pdf" % (pretty, chapter_num),
                  "Old_ncert_%s_Chapter_%d.pdf" % (subject.capitalize(), chapter_num),
                  "Old_ncert_%s_Chapter_%d.pdf" % (subject[:4].capitalize(), chapter_num)]
    for n in names:
        p = os.path.join(base, n)
        if os.path.exists(p):
            return p
    # THE OLDER BOOKS DO NOT NAME THEIR FILES AFTER THE CHAPTER'S POSITION IN THE FILENAME'S
    # TAIL. `inputs/ncert/older/Class_11th/Biology/` holds `4 3. Plant Kingdom.pdf` -- a file
    # ordinal, then the printed chapter number, then the title -- so the old `[_ ]N\.pdf$`
    # pattern matched nothing and every older Class 11 chapter raised "no PDF". The chapter
    # number is the one AFTER the file ordinal, which is exactly what runner_core already
    # knows how to read (it is the same convention `iter_ncert_files` registers under), so the
    # fallback asks it rather than inventing a second rule that can disagree with the register.
    candidates = []
    for f in sorted(os.listdir(base)):
        if not f.lower().endswith(".pdf"):
            continue
        try:
            n = rc.extract_chapter_num(f, os.path.join(base, f))
        except Exception:
            n = None
        if n == chapter_num:
            candidates.append(f)
    if not candidates:
        for f in sorted(os.listdir(base)):
            if re.search(r"(?:^|[_ ])%d[. ]" % chapter_num, f) and f.lower().endswith(".pdf"):
                candidates.append(f)
    if candidates:
        return os.path.join(base, candidates[0])
    raise SystemExit("no PDF for %s ch%d under %s (saw: %s)"
                     % (book_id, chapter_num, base,
                        ", ".join(sorted(os.listdir(base))[:6]) or "nothing"))


def _weight(span):
    """Bold from the font NAME first -- see note 1 in the module docstring."""
    name = span["font"]
    return any(k in name for k in BOLD_NAMES) or bool(span["flags"] & 16)


def _slant(span):
    return any(k in span["font"] for k in ITALIC_NAMES) or bool(span["flags"] & 2)


def _smallcaps(spans):
    """Rebuild NCERT's two-size fake small caps into words plus an `sc` flag.

    Returns a list of (text, size, is_smallcaps) or None when the group is not small caps.
    The test is deliberately strict: every span must be uppercase letters/spaces only, at least
    one span must sit at a clearly smaller size than the group's largest, and the small size must
    be 42-88% of the large one (measured: 12.6/26.8 on a chapter title, 9.1/13.0 on a section
    heading). Ordinary ALL-CAPS headings set at one size are left alone.
    """
    letters = [s for s in spans if s["text"].strip()]
    if len(letters) < 2:
        return None
    if not all(re.fullmatch(r"[A-Z0-9 .'\-]+", s["text"]) for s in letters):
        return None
    sizes = sorted({round(s["size"], 1) for s in letters})
    if len(sizes) < 2:
        return None
    small, large = sizes[0], sizes[-1]
    if not (0.42 <= small / large <= 0.88):
        return None
    out = []
    for s in letters:
        is_small = round(s["size"], 1) < (small + large) / 2
        out.append((s["text"].lower() if is_small else s["text"], large, True))
    return out


def _line_reference(line):
    """(body_size, baseline_y) for a line, taken as the MODAL character size and origin.

    Modal, not maximum: a line is mostly body type with a few small characters sitting off the
    baseline, so the most common value IS the body setting. Using the maximum size works too
    until a line is mostly superscript (a units line like `m s-1 kg-3`), and using the bottom
    of the bounding box -- which is what this module did before -- fails always, because a
    subscript's box bottom sits BELOW the baseline by design and a capital's does not.
    """
    sizes, origins = collections.Counter(), collections.Counter()
    for s in line["spans"]:
        for c in s.get("chars") or ():
            if c["c"].strip():
                sizes[round(s["size"], 1)] += 1
                origins[round(c["origin"][1], 1)] += 1
    if not sizes:
        return None, None
    return sizes.most_common(1)[0][0], origins.most_common(1)[0][0]


def char_script(char, span_size, body_size, baseline):
    """'sup' / 'sub' / None for ONE character, from its own size and baseline.

    THE SINGLE BIGGEST ACCURACY DEFECT THIS MODULE HAD, AND IT WAS NOT THE PDF'S FAULT.
    PyMuPDF's span flag bit 0 marks superscripts and NOTHING marks subscripts, so reading
    formatting off the flags reported ZERO subscripts across the whole of BIO11L ch09 --
    Biomolecules, a chapter of H2O, CO2 and C6H12O6. The chapter's text came out as
    `C6H12O6 (Glucose)`, with the subscripts silently flattened into inline digits, and the
    physics equivalent -- NCERT's `2.0 x 10^11 Pa` becoming `2.0 x 1011 Pa` -- is a materially
    WRONG NUMBER stored as verified NCERT text for an evidence step to quote.

    But the information was there the whole time, one level down. Measured on the glucose line
    of BIO11L ch09 p004, character by character:

        'C' size 9.5  origin_y 201.6        'H' size 9.5  origin_y 201.6
        '6' size 5.5  origin_y 204.8        '1' size 5.5  origin_y 204.8

    The subscripts are 58% of the body size on a baseline 3.2pt lower. Reading characters
    rather than span flags recovers them exactly: re-measured after this change, the same
    chapter yields 53 subscripts, and Class 11 Physics ch01 yields 227 superscripts where the
    flags had found almost none.

    The thresholds are deliberately loose -- smaller than 78% of the body size, and off the
    baseline by more than 8% of it -- because the alternative to a borderline call here is not
    "no script", it is a wrong character in a formula.
    """
    if not body_size or baseline is None:
        return None
    if span_size >= body_size * 0.78:
        return None
    dy = char["origin"][1] - baseline
    if dy > body_size * 0.08:
        return "sub"
    if dy < -body_size * 0.08:
        return "sup"
    return None


def _script(span, line_size, line_base):
    """'sup' / 'sub' / None. PyMuPDF flags bit 0 is superscript; subscript is not flagged at all
    and has to be read off the baseline, which is why both are decided here together."""
    if span["flags"] & 1:
        return "sup"
    if span["size"] >= line_size * 0.86:
        return None
    drop = span["bbox"][3] - line_base
    if drop > line_size * 0.12:
        return "sub"
    if drop < -line_size * 0.10:
        return "sup"
    return None


def runs_for_lines(lines):
    """Lines of spans -> merged runs + the joined plain text.

    Joins lines with a space, and de-hyphenates a word broken across a line end (trailing '-'
    followed by a lowercase start), recording each join so the decision stays auditable.
    """
    # Note 4 in the module docstring: the lines come back in the order the PDF's content stream
    # happened to draw them, which on a two-line chapter title is bottom-first. Sort to the
    # order a reader sees -- baseline first, then left-to-right for lines sharing a baseline.
    # BUCKET THE BASELINE, THEN ORDER LEFT TO RIGHT.
    #
    # Sorting on the raw box bottom looks right and is wrong by a hair's breadth. Two pieces set
    # on the SAME printed line do not share a box bottom: measured on BIO11L ch01 p004, the head
    # line is one block of two pieces, `4` with bottom 76.49 and `BIOLOGY` with bottom 76.43 --
    # 0.06pt apart, because a digit and small caps have different descender boxes. Rounded to
    # one decimal those become 76.5 and 76.4, so `BIOLOGY` sorted FIRST and the line read
    # `Biology 4` instead of `4 Biology`. The folio and the running head then swapped ends of
    # the page, which flips the recto/verso test that places the folio tab and mirrors the
    # margin -- every page of the book, from a rounding difference.
    #
    # A 3pt bucket is far smaller than any real line pitch in these books (measured 12-14pt) and
    # far larger than this kind of box-bottom jitter, so same-line pieces group and genuinely
    # different lines stay apart.
    lines = sorted(lines, key=lambda l: (round(l["bbox"][3] / 3.0), round(l["bbox"][0], 1)))
    runs, dehyphenated = [], []
    for li, line in enumerate(lines):
        spans = [s for s in line["spans"] if s["text"].strip()]
        if not spans:
            continue
        line_size = max(s["size"] for s in spans)
        line_base = max(s["bbox"][3] for s in spans)
        sc = _smallcaps(spans)
        pieces = []
        for i, s in enumerate(spans):
            text = sc[i][0] if sc else s["text"]
            # A WORD SPACE CAN LIVE IN THE GAP BETWEEN TWO SPANS, NOT IN EITHER SPAN'S TEXT.
            # NCERT sets small caps as `L`+`IVING`+`W`+`ORLD` and a heading as `1.1`+`Diversity`,
            # positioning each piece rather than writing a space. Concatenating the texts gives
            # `TheLivingWorld` and `1.1Diversity`. A gap wider than a quarter of the type size is
            # a space; the tight joins inside one small-cap word stay joined. MEASURED on
            # BIO11L ch01 p003: word gaps are 0.22-0.48 of the line's largest type size
            # (`HE`|`L` 6.23/26.8, `THE`|`L` 3.82/13.0, `HAPTER`|`1` 12.97/26.8) while joins
            # inside a single small-cap word are 0.00-0.10. 0.15 splits them with margin.
            if i and not text.startswith(" ") and not pieces[-1]["t"].endswith(" "):
                gap = s["bbox"][0] - spans[i - 1]["bbox"][2]
                if gap > line_size * 0.15:
                    pieces[-1]["t"] += " "
            pieces.append({
                "t": text,
                "b": _weight(s),
                "i": _slant(s),
                "sc": bool(sc),
                # Script detection is SKIPPED inside small caps. The small letters there sit on
                # the SAME baseline as the capitals, but their font box is shorter, so the
                # baseline test reads every one of them as a superscript -- which rendered
                # `The Living World` as `T`+`he `(sup)+`L`+`iving `(sup).
                "script": None if sc else _script(s, line_size, line_base),
                "color": "#%06x" % s["color"],
                "size": round(s["size"], 1),
                "font": s["font"],
            })
        # last line's trailing hyphen folds into the next line
        if li + 1 < len(lines) and pieces:
            tail = pieces[-1]["t"]
            nxt = [t for t in lines[li + 1]["spans"] if t["text"].strip()]
            if tail.endswith("-") and len(tail) > 1 and tail[-2].isalpha() and nxt \
                    and nxt[0]["text"][:1].islower():
                pieces[-1]["t"] = tail[:-1]
                dehyphenated.append(tail)
            elif not tail.endswith(" "):
                pieces[-1]["t"] = tail + " "
        runs.extend(pieces)

    merged = []
    for r in runs:
        key = (r["b"], r["i"], r["sc"], r["script"], r["color"], r["font"])
        if merged and merged[-1]["_key"] == key:
            merged[-1]["t"] += r["t"]
        else:
            r = dict(r); r["_key"] = key
            merged.append(r)
    for r in merged:
        r.pop("_key")
        r["t"] = re.sub(r"\s+", " ", r["t"])
    merged = [r for r in merged if r["t"].strip() or r["t"] == " "]
    text = "".join(r["t"] for r in merged).strip()
    return merged, text, dehyphenated


def columns_for(elements, page_w):
    """Cluster element left edges into columns. NCERT Biology mirrors its wide margin -- the body
    starts at x=38pt on odd pages and x=170pt on even ones -- so the columns are measured per page
    rather than assumed, and a column is only declared when two clusters are >60pt apart."""
    # TEXT roles only, and the same set on both ends of the cluster. Two things used to pollute
    # this: the head line (`24 Biology`), which spans the whole sheet and is now split out into
    # a folio and a running header before this runs, and -- still live before this change --
    # `members` being taken from EVERY element, so a full-bleed image block whose left edge
    # happened to fall inside a column's range set that column's right edge to the trim.
    # Measured on BIO11L ch3 p001: the contents rail came back as x 0.098 -> 0.867, i.e. the
    # whole page, when the rail the book prints is 0.098 -> 0.243. A renderer believing that
    # draws the opening prose underneath the contents list instead of beside it.
    _TEXT_ROLES = ("paragraph", "list", "side_note", "section_heading", "figure_caption",
                   "contents_entry")
    text_els = [e for e in elements if e["role"] in _TEXT_ROLES]
    starts = sorted(e["_x0"] for e in text_els)
    if not starts:
        return []
    groups, cur = [], [starts[0]]
    for x in starts[1:]:
        if x - cur[-1] > 60:
            groups.append(cur); cur = [x]
        else:
            cur.append(x)
    groups.append(cur)
    cols = []
    for g in groups:
        members = [e for e in text_els if min(g) - 1 <= e["_x0"] <= max(g) + 1]
        if not members:
            continue
        cols.append({"x0_pt": round(min(g), 1),
                     "x1_pt": round(max(e["_x1"] for e in members), 1),
                     "elements": len(members)})
    if len(cols) > 1:
        cols[0]["name"] = "side"
        for c in cols[1:]:
            c["name"] = "body"
    else:
        # A SINGLE COLUMN IS NOT NECESSARILY FULL WIDTH. NCERT MIRRORS ITS WIDE MARGIN: measured on
        # BIO11L ch01, the verso p004 sets its body at x 0.314-0.902 with the margin on the LEFT and
        # the recto p007 at x 0.098-0.687 with the margin on the RIGHT. Calling both "full" states
        # that the text runs edge to edge, which is wrong on every page of the chapter, and a
        # renderer believing it puts body text where the book leaves white space.
        only = cols[0]
        left_f, right_f = only["x0_pt"] / page_w, only["x1_pt"] / page_w
        only["name"] = "body" if (left_f > 0.22 or right_f < 0.80) else "full"
    for c in cols:
        c["x0"] = round(c["x0_pt"] / page_w, 4)
        c["x1"] = round(c["x1_pt"] / page_w, 4)
    return cols


def margin_side(cols):
    """Which edge of the page carries the wide margin -- what a renderer needs to place its rail."""
    if not cols:
        return None
    if len(cols) > 1:
        return "left" if cols[0]["x0"] < 0.5 else "right"
    c = cols[0]
    if c["x0"] > 0.22:
        return "left"
    if c["x1"] < 0.80:
        return "right"
    return None


# The imprint NCERT prints at the foot of every page. The older books print a bare `2022-23`;
# the latest Class 11 prints `2024-25`; the latest Class 12 prints `Reprint 2026-27`. The
# original pattern here was `\d{4}-\d{2}` alone, which matched the first two and NOT the third,
# so every page of every latest Class 12 Biology chapter filed its imprint as a running header:
# measured on BIO12L-ch03, 0 elements classified `reprint_line` against 10 pages that each print
# one. The imprint is how a reader tells the editions apart on sight, so losing it loses the one
# visible marker of WHICH BOOK a page came from.
_IMPRINT_RE = re.compile(r"^(?:reprint\s+)?\d{4}\s*[-–—]\s*\d{2}$", re.I)


def is_imprint(text):
    return bool(_IMPRINT_RE.match((text or "").strip()))


def classify(text, runs, bbox, page_w, page_h, body_size):
    """What the element IS on the printed page."""
    size = max((r["size"] for r in runs), default=0)
    x0f, y0f = bbox[0] / page_w, bbox[1] / page_h
    colour = runs[0]["color"] if runs else "#000000"
    if y0f > 0.93 and is_imprint(text):
        return "reprint_line"
    # A bare number standing on its own, set in the OUTER margin rather than in the measure:
    # that is the folio, and on a Class 12 page it sits two-thirds of the way down (measured
    # BIO12L ch3 p002: `42` at x 0.110-0.138, y 0.794). Without this it classified as a
    # one-word paragraph and landed in the middle of the chapter's prose.
    if re.fullmatch(r"\d{1,3}", text.strip()) and (x0f < 0.22 or x0f > 0.78):
        return "page_number"
    # MEASURED on BIO11L ch01: every running header sits at y0 0.0825-0.0834 and the first body
    # line of the same page starts at 0.1358, so 0.11 separates them with room to spare. The
    # earlier 0.08 cut sat just ABOVE the headers and read `4 Biology` as a body paragraph.
    if (y0f < 0.11 or y0f > 0.92) and len(text) < 60:
        return "running_header" if size <= body_size * 1.2 else "chapter_title"
    if size >= body_size * 1.8:
        return "chapter_title"
    if re.match(r"^\d+\.\d+(\.\d+)?\s", text) and (size > body_size * 1.05 or runs[0]["b"]):
        return "section_heading"
    # NCERT's end-of-chapter headings carry no number -- SUMMARY, EXERCISES, GLOSSARY. They are
    # set at heading size, so size is what identifies them; without this they read as one-word
    # paragraphs and a chapter renders with no visible structure after its last numbered section.
    if len(text) < 30 and size > body_size * 1.1 and text.strip().isalpha():
        return "section_heading"
    # A CAPTION NAMES THE FIGURE; A SENTENCE MENTIONS IT. `Figure 1.1 Taxonomic categories
    # showing hierarchial arrangement` is a caption; `Table 1.1 indicates the taxonomic
    # categories to which some common organisms belong.` is running prose, and typing it as a
    # caption turned a paragraph into a figure node with no picture. A caption is short and is
    # not a sentence -- it does not end in a full stop and does not run past a line or two.
    m_cap = re.match(r"^(Figure|Fig\.|TABLE|Table)\s*\d+\.\d+(.*)$", text, re.S)
    if m_cap:
        tail = m_cap.group(2).strip()
        looks_like_prose = (len(text) > 160
                            or re.match(r"^(indicates|shows|gives|lists|is|are|was|were|"
                                        r"presents|summaris|describ)", tail, re.I))
        if not looks_like_prose:
            return "figure_caption"
    # A note set in the MARGINAL RAIL, not in the measure. The rail mirrors every page, so
    # testing only the left edge found it on versos and missed it on every recto -- measured on
    # BIO11L ch3 p007, whose rail runs x 0.70-0.95 and whose marginal labels classified as body
    # paragraphs. The measure is 0.588 of the sheet wide in both Biology classes, so anything
    # starting beyond 0.68 is past the end of the widest measure a page can set.
    if (x0f < 0.30 or x0f > 0.68) and size < body_size:
        return "side_note"
    if re.match(r"^\(?[ivx]+\)|^\(?[a-d]\)|^\d+\.\s", text.strip()):
        return "list"
    return "paragraph"


def split_head_line(text, runs):
    """`24 Biology` / `Plant Kingdom 29` -> (folio, head_text, folio_at). Else (None, text, None).

    NCERT sets the folio and the running head on ONE line at opposite ends of the measure, and
    PyMuPDF returns them as one block because they share a baseline. Measured on BIO11L ch3:
    p002 gives `24 Biology` (folio at the left, i.e. the outer edge of a verso) and p007 gives
    `Plant Kingdom 29` (folio at the right, the outer edge of a recto). Filed whole, that block
    read as a body paragraph whose first word was a number.

    `folio_at` is "start" or "end", which is independent evidence of the page side: the folio is
    always in the OUTER margin, so folio-at-start means verso and folio-at-end means recto.
    """
    t = (text or "").strip()
    m = re.match(r"^(\d{1,3})\s+(\S.*)$", t)
    if m:
        return int(m.group(1)), m.group(2).strip(), "start"
    m = re.match(r"^(.*\S)\s+(\d{1,3})$", t)
    if m:
        return int(m.group(2)), m.group(1).strip(), "end"
    if re.fullmatch(r"\d{1,3}", t):
        return int(t), "", None
    return None, t, None


def vector_figures(page, text_boxes, page_w, page_h, min_frac=0.025):
    """Figures the book DRAWS rather than places as an image.

    NCERT's flowcharts, arrows, ruled boxes and many diagrams are VECTOR art -- Figure 1.1
    (`Species -> Genus -> Family -> ... -> Kingdom`, on a pale yellow ground) has no image
    block at all, so an extractor that only looks for image blocks reports the page as having
    no figure. Measured on BIO11L ch01 p008: 0 image figures found, and the page prints one.

    The drawings ARE in the PDF -- `page.get_drawings()` returns every filled and stroked path.
    They are clustered by occupancy, the same way image slivers are, and any cluster that
    overlaps real text is dropped: a paragraph's underline or a table's rules are drawing
    operations too, and they are not figures.

    This is the FALLBACK. Where A2L has run, the agent's own `figure` bbox is better -- it is
    one judgement about what the reader sees, rather than an inference from path geometry.
    """
    # THE PAGE'S OWN FURNITURE IS DRAWN, TOO. The Class 11 header band, its grey strip, the
    # white folio tab and the green footer bar are all filled rectangles -- vector, exactly like
    # a flowchart. Clustering drawings without excluding them made the BAND the best-scoring
    # "figure" on the page, so a page-wide green strip with `8  BIOLOGY` in it was cropped and
    # dropped into the running text under the caption `Figure 1.1 Taxonomic`.
    #
    # Furniture lives in known zones: the head of the sheet and its foot. Nothing inside them
    # is artwork, so nothing inside them is clustered.
    HEAD_ZONE, FOOT_ZONE = 0.13, 0.92
    rects = []
    for d in page.get_drawings():
        r = d["rect"]
        if r.width <= 0 or r.height <= 0:
            continue
        if r.width >= 0.97 * page_w and r.height >= 0.97 * page_h:
            continue                      # the page ground
        if r.y1 / page_h <= HEAD_ZONE or r.y0 / page_h >= FOOT_ZONE:
            continue                      # header band / strip / folio tab / footer bar
        if r.width >= 0.95 * page_w:
            continue                      # a full-bleed bar is furniture, never a figure
        rects.append((r.x0, r.y0, r.x1, r.y1))
    if len(rects) < 3:
        return []
    merged = merge_image_blocks(rects, page_w, page_h, gap_pt=9.0, min_pt=28.0)
    out = []
    for (x0, y0, x1, y1), n_parts in merged:
        w, h = (x1 - x0) / page_w, (y1 - y0) / page_h
        if w < min_frac or h < min_frac:
            continue
        if n_parts < 3:
            continue                      # a rule or a single box is not a figure
        # A cluster that sits on top of running text is page decoration, not artwork.
        covered = sum(1 for tb in text_boxes
                      if tb[0] >= x0 - 2 and tb[2] <= x1 + 2
                      and tb[1] >= y0 - 2 and tb[3] <= y1 + 2)
        if covered > 3:
            continue
        out.append(((x0, y0, x1, y1), n_parts))
    return out


def merge_image_blocks(boxes, page_w, page_h, gap_pt=5.0, min_pt=10.0):
    """Thousands of image slivers -> the few real figures they are fragments of.

    A SCANNED NCERT FIGURE IS NOT ONE IMAGE BLOCK. Measured on BIO11L ch3: pages 6, 9 and 11
    return 3174, 3880 and 2625 image blocks, nearly all of them ZERO points tall and two or
    three points wide -- the figure is carried as a stack of single-scan-line strips. Taking
    those at face value produced 9683 "figures" in a 14-page chapter that prints four, and any
    consumer cutting crops from them would have written 9683 one-pixel PNGs.

    The strips are merged by occupancy rather than pairwise: the page is rasterised onto a
    `gap_pt` grid, each box marks the cells it covers, and the connected regions of marked cells
    are the figures. That is O(area) rather than O(n^2), which matters at 3880 boxes, and it
    joins a figure's parts across the small gaps the strips leave between them.

    Components smaller than `min_pt` on BOTH sides are dropped as scan dust -- a real NCERT
    figure is tens of points across, and keeping the dust is what fills a chapter's figure
    folder with blank crops.
    """
    if not boxes:
        return []
    cell = max(2.0, gap_pt)
    nx, ny = int(page_w / cell) + 2, int(page_h / cell) + 2
    owner = {}
    for idx, (x0, y0, x1, y1) in enumerate(boxes):
        cx0, cx1 = int(x0 / cell), int(max(x1, x0 + 0.1) / cell)
        cy0, cy1 = int(y0 / cell), int(max(y1, y0 + 0.1) / cell)
        for cx in range(max(0, cx0), min(nx, cx1 + 1)):
            for cy in range(max(0, cy0), min(ny, cy1 + 1)):
                owner.setdefault((cx, cy), []).append(idx)
    seen, merged = set(), []
    for start in list(owner):
        if start in seen:
            continue
        stack, cells, members = [start], [], set()
        seen.add(start)
        while stack:
            c = stack.pop()
            cells.append(c)
            members.update(owner.get(c, ()))
            cx, cy = c
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
                n = (cx + d[0], cy + d[1])
                if n in owner and n not in seen:
                    seen.add(n)
                    stack.append(n)
        xs0 = min(boxes[i][0] for i in members)
        ys0 = min(boxes[i][1] for i in members)
        xs1 = max(boxes[i][2] for i in members)
        ys1 = max(boxes[i][3] for i in members)
        if (xs1 - xs0) < min_pt and (ys1 - ys0) < min_pt:
            continue
        merged.append(((xs0, ys0, xs1, ys1), len(members)))
    merged.sort(key=lambda m: (m[0][1], m[0][0]))
    return merged


def classify_image(bbox, page_w, page_h, design):
    """`figure` or `page_furniture` for a non-text block -- see note 6 in the module docstring."""
    frac = (bbox[0] / page_w, bbox[1] / page_h, bbox[2] / page_w, bbox[3] / page_h)
    if design_lib.is_page_ground(frac):
        return "page_furniture", "page ground"
    if design_lib.is_watermark(frac):
        return "page_furniture", "watermark"
    if design is not None and design_lib.is_header_art(frac, design):
        return "page_furniture", "header art"
    if design is not None and design_lib.is_qr_code(frac, design):
        return "page_furniture", "qr code"
    return "figure", None


def extract(book_id, chapter_num):
    path = pdf_path(book_id, chapter_num)
    try:
        design = design_lib.design_for(book_id)
    except (KeyError, ValueError):
        # An unregistered book still extracts; it just does not get the canonical sheet or the
        # furniture knowledge. Saying so beats quietly using another book's grid.
        design = None
    doc = pymupdf.open(path)
    pages = []
    for pi, page in enumerate(doc):
        pw, ph = page.rect.width, page.rect.height
        raw = page.get_text("dict")
        sizes = collections.Counter()
        for b in raw["blocks"]:
            if b["type"] != 0:
                continue
            for l in b["lines"]:
                for s in l["spans"]:
                    if s["text"].strip():
                        sizes[round(s["size"], 1)] += len(s["text"])
        body_size = sizes.most_common(1)[0][0] if sizes else 10.5

        elements, fragments = [], []
        for b in raw["blocks"]:
            # A MIRRORED IMAGE COMES BACK WITH x1 < x0. The Class 12 header strip is drawn
            # flipped on recto pages, so its bbox is (38.4, 0.0, 0.0, 76.9) -- a negative width.
            # Every size test downstream then reads it as 0pt wide, so `is_header_art` did not
            # recognise it and it was emitted as a figure: measured on BIO12L ch6, every odd
            # page carried a "figure" at [0.035, 0.004, -0.0, 0.1].
            b["bbox"] = (min(b["bbox"][0], b["bbox"][2]), min(b["bbox"][1], b["bbox"][3]),
                         max(b["bbox"][0], b["bbox"][2]), max(b["bbox"][1], b["bbox"][3]))
            if b["type"] != 0:
                role, why = classify_image(b["bbox"], pw, ph, design)
                if role == "page_furniture":
                    elements.append({"role": role, "bbox_pt": [round(v, 1) for v in b["bbox"]],
                                     "_x0": b["bbox"][0], "_x1": b["bbox"][2],
                                     "runs": [], "text": "", "furniture": why})
                else:
                    fragments.append(tuple(b["bbox"]))
                continue
            runs, text, dehy = runs_for_lines(b["lines"])
            if not text:
                continue
            # THE PRINTED LINE PITCH, MEASURED, NOT ASSUMED.
            #
            # A renderer that places a block at its measured top and then sets the text at its
            # own natural leading produces a block of a DIFFERENT HEIGHT from the printed one.
            # Every such difference accumulates down the page, so blocks either collide (a
            # heading printed over the paragraph under it) or leave gaps the book does not
            # have. Measured on BIO11L ch3 p005: the printed pitch is 12.4pt on 10.5pt type
            # (1.18), against the 1.27 the stylesheet was using -- 7% taller per line, which
            # over a 20-line paragraph is a line and a half of drift.
            #
            # Carrying the pitch per block lets the renderer set `line-height` to the number
            # the page actually prints, so a block occupies the height it occupies in the book.
            ys = sorted({round(l["bbox"][3], 1) for l in b["lines"]})
            pitch = None
            if len(ys) > 1:
                gaps = [ys[i + 1] - ys[i] for i in range(len(ys) - 1)]
                gaps = [g for g in gaps if g > 1.0]
                if gaps:
                    pitch = round(sorted(gaps)[len(gaps) // 2], 2)
            el = {"bbox_pt": [round(v, 1) for v in b["bbox"]],
                  "_x0": b["bbox"][0], "_x1": b["bbox"][2],
                  "_lines": [(tuple(l["bbox"]),
                              "".join(s["text"] for s in l["spans"]).strip())
                             for l in sorted(b["lines"], key=lambda l: l["bbox"][3])],
                  "line_count": len(ys),
                  "line_pitch_pt": pitch,
                  # SPAN POSITIONS, kept only long enough to rebuild a table's columns.
                  # A table ROW arrives as ONE block whose cells are separate spans at
                  # different x -- measured on BIO11L ch01 p008, every row of Table 1.1 starts
                  # at x 84.0 and its seven cells are spans across the measure. Clustering
                  # BLOCK left-edges therefore sees a single column and no grid at all; the
                  # column structure only exists one level down.
                  "_spans": [(round(sp["bbox"][0], 1),
                              round(sp["bbox"][1], 1),
                              "".join(c["c"] for c in sp.get("chars") or ()) or sp.get("text", ""))
                             for ln in b["lines"] for sp in ln["spans"]
                             if ("".join(c["c"] for c in sp.get("chars") or ())
                                 or sp.get("text", "")).strip()],
                  "runs": runs, "text": text}
            el["role"] = classify(text, runs, b["bbox"], pw, ph, body_size)
            if dehy:
                el["dehyphenated"] = dehy
            elements.append(el)

        # Vector artwork, where the page draws rather than places its figure.
        _text_boxes = [e["bbox_pt"] for e in elements if (e.get("text") or "").strip()]
        _img = merge_image_blocks(fragments, pw, ph)
        _vec = vector_figures(page, _text_boxes, pw, ph)
        # Drop a vector cluster that an image block already covers -- the same figure found
        # twice is worse than found once.
        def _overlaps_any(b, others):
            for (o, _n) in others:
                if not (b[2] < o[0] or o[2] < b[0] or b[3] < o[1] or o[3] < b[1]):
                    return True
            return False
        _vec = [(b, n) for b, n in _vec if not _overlaps_any(b, _img)]
        # ONLY CLAIM A VECTOR FIGURE THE PAGE ITSELF NAMES.
        #
        # Clustering drawing paths finds real artwork and also finds every ruled box, every
        # underline and every tint panel -- unleashed on BIO11L ch01 it reported ELEVEN figures
        # on a chapter that prints one, all pointing at the same crop. A heuristic that wrong is
        # worse than no heuristic, because it quietly fills the figure folder and the tree with
        # things that are not figures.
        #
        # The page states its own ground truth: it prints `Figure 1.1 ...` under artwork it
        # considers a figure. So a vector cluster is kept only when the page carries a figure
        # CAPTION that no image-block figure already accounts for, and only the cluster nearest
        # that caption. Everything else waits for A2L, whose whole job is to say what a reader
        # sees as a figure -- a judgement, not an inference from path geometry.
        _caps = [e for e in elements if e["role"] == "figure_caption"
                 and re.match(r"^\s*(Figure|Fig\.)", e.get("text") or "")]
        _unclaimed = max(0, len(_caps) - len(_img))
        if _unclaimed <= 0:
            _vec = []
        elif _vec:
            def _dist_to_cap(b):
                return min((abs((b[1] + b[3]) / 2 - (c["bbox_pt"][1] + c["bbox_pt"][3]) / 2)
                            for c in _caps), default=1e9)
            _vec = sorted(_vec, key=lambda bn: _dist_to_cap(bn[0]))[:_unclaimed]
        for (fx0, fy0, fx1, fy1), n_frag in (_img + _vec):
            el = {"role": "figure", "bbox_pt": [round(fx0, 1), round(fy0, 1),
                                                round(fx1, 1), round(fy1, 1)],
                  "_x0": fx0, "_x1": fx1, "runs": [], "text": ""}
            if n_frag > 1:
                el["merged_from_fragments"] = n_frag
            elements.append(el)

        # --- split the head line into its folio and its running head ------------------------
        printed_folio, folio_at = None, None
        split_out = []
        for el in elements:
            if el["role"] != "running_header":
                split_out.append(el)
                continue
            folio, head, at = split_head_line(el["text"], el["runs"])
            if folio is not None and printed_folio is None:
                printed_folio, folio_at = folio, at
            if folio is None or not head:
                if folio is not None and not head:
                    el["role"] = "page_number"
                    el["printed_page_number"] = folio
                split_out.append(el)
                continue
            # One block becomes two elements anchored at the two ends of the same line.
            x0, y0, x1, y1 = el["bbox_pt"]
            num_w = min(26.0, (x1 - x0) * 0.3)
            if at == "start":
                num_box, head_box = [x0, y0, x0 + num_w, y1], [x0 + num_w, y0, x1, y1]
            else:
                num_box, head_box = [x1 - num_w, y0, x1, y1], [x0, y0, x1 - num_w, y1]
            split_out.append({"role": "page_number", "bbox_pt": num_box,
                              "_x0": num_box[0], "_x1": num_box[2], "runs": [],
                              "text": str(folio), "printed_page_number": folio})
            split_out.append({"role": "running_header", "bbox_pt": head_box,
                              "_x0": head_box[0], "_x1": head_box[2],
                              "runs": el["runs"], "text": head})
        elements = split_out
        _sample_fills(page, elements, pw, ph)
        elements = _absorb_figure_labels(elements, pw, ph)
        elements = _mark_tables(elements, pw, ph)

        # --- the chapter opener's section-contents list -------------------------------------
        # The opener prints the chapter's own section list in the rail beside the title. It
        # extracts as a stack of short `n.m Title` lines and classified as `side_note`, which is
        # the role for a marginal annotation -- so a renderer had no way to tell the chapter's
        # table of contents from a caption in the margin, and the opener's two-column
        # arrangement could not be rebuilt. Measured on BIO11L ch3 p001 (3.1 Algae .. 3.5
        # Angiosperms) and BIO12L ch3 p001 (3.1 .. 3.5).
        if pi == 0:
            contents_out = []
            for el in elements:
                if el["role"] != "side_note" or not re.match(r"^\d+\.\d+\s+\S", el["text"]):
                    contents_out.append(el)
                    continue
                # ONE BLOCK IS NOT ONE ENTRY. The Class 12 opener's contents list comes back as
                # a few blocks each holding several entries -- measured on BIO12L ch6, one
                # element read `6.6 Mechanism of Evolution 6.7 Hardy - Weinberg Principle 6.8 A
                # Brief Account of Evolution 6.9 Origin and Evolution of Man`, four entries run
                # together into a sentence. A new entry starts at a line beginning `n.m`, and
                # the lines carry their own boxes, so each entry gets its real position rather
                # than a share of the block's.
                entries, cur = [], None
                for lbox, ltext in el.get("_lines") or []:
                    if not ltext:
                        continue
                    if re.match(r"^\d+\.\d+(\s|$)", ltext) or cur is None:
                        cur = {"box": list(lbox), "parts": [ltext]}
                        entries.append(cur)
                    else:
                        cur["parts"].append(ltext)
                        cur["box"][0] = min(cur["box"][0], lbox[0])
                        cur["box"][1] = min(cur["box"][1], lbox[1])
                        cur["box"][2] = max(cur["box"][2], lbox[2])
                        cur["box"][3] = max(cur["box"][3], lbox[3])
                if len(entries) <= 1:
                    el["role"] = "contents_entry"
                    contents_out.append(el)
                    continue
                for ent in entries:
                    box = [round(v, 1) for v in ent["box"]]
                    contents_out.append({
                        "role": "contents_entry", "bbox_pt": box,
                        "_x0": box[0], "_x1": box[2],
                        "runs": [dict(el["runs"][0], t=" ".join(ent["parts"]))]
                        if el["runs"] else [],
                        "text": " ".join(ent["parts"]),
                    })
            elements = contents_out

        if printed_folio is None:
            for el in elements:
                if el["role"] == "page_number" and el["text"].strip().isdigit():
                    printed_folio = int(el["text"].strip())
                    x_mid = (el["bbox_pt"][0] + el["bbox_pt"][2]) / 2.0
                    folio_at = "start" if x_mid < pw / 2 else "end"
                    break

        side = ("verso" if folio_at == "start" else "recto") if folio_at else \
            design_lib.page_side(printed_folio, pi + 1)

        # --- the canonical sheet ------------------------------------------------------------
        # Body x0 is measured from real body text only -- furniture sits outside the measure and
        # would drag the offset to the trim edge.
        body_x0 = None
        body_xs = [e["_x0"] for e in elements
                   if e["role"] in ("paragraph", "list", "section_heading")
                   and (e["_x1"] - e["_x0"]) > 0.3 * pw]
        if body_xs:
            body_x0 = min(body_xs)
        # The crop is a property of the SCAN, not of a page, so it is measured on the pages that
        # can measure it and then applied to all of them. Measuring per page put the opener on a
        # different sheet from its own body pages: an opener sets its prose beside the contents
        # rail (BIO11L ch3 p001 starts at x 173.5pt) rather than on the book's 60/192pt grid, so
        # the per-page measurement read that as a 113pt crop and silently centred the page
        # instead. A figure-only page has no body text at all and could not be measured either.
        if design is not None:
            dx, dy, note = design_lib.normalise_page(pw, ph, body_x0, design, side)
            sheet_w, sheet_h = design.trim_pt
        else:
            dx, dy, note, sheet_w, sheet_h = 0.0, 0.0, "no design", pw, ph

        cols = columns_for(elements, pw)
        for e in elements:
            e["column"] = cols[0]["name"] if cols else "full"
            for c in cols:
                if c["x0_pt"] - 2 <= e["_x0"] <= c["x1_pt"]:
                    e["column"] = c["name"]
            e["bbox"] = [round(e["bbox_pt"][0] / pw, 4), round(e["bbox_pt"][1] / ph, 4),
                         round(e["bbox_pt"][2] / pw, 4), round(e["bbox_pt"][3] / ph, 4)]
            e["size_rel"] = round(max((r["size"] for r in e["runs"]), default=body_size) / body_size, 2)
            del e["_x0"], e["_x1"]
            e.pop("_lines", None)
            e.pop("_spans", None)
        # reading order: side column first, then body, top to bottom
        order = {"side": 0, "full": 1, "body": 1}
        elements.sort(key=lambda e: (order.get(e["column"], 1), e["bbox"][1]))

        imprint = next((e["text"] for e in elements if e["role"] == "reprint_line"), None)
        pages.append({
            "page_file": "%03d" % (pi + 1),
            "page_width_pt": round(pw, 1), "page_height_pt": round(ph, 1),
            "sheet_pt": [round(sheet_w, 1), round(sheet_h, 1)],
            "_measured_offset": (dx, dy) if note.startswith("uncropped")
            or note == "canonical" else None,
            "sheet_note": note,
            "printed_page_number": printed_folio,
            "page_side": side,
            "imprint": imprint,
            "body_text_size_pt": body_size,
            "columns": [{k: v for k, v in c.items() if not k.endswith("_pt")} for c in cols],
            "margin_side": margin_side(cols),
            "has_text_layer": bool(sizes),
            # THE PAGE'S OWN SIZE, not the design's canonical trim. Most of this corpus is
            # 612 x 784pt, but the 8 scanned files are A4 (595.32 x 841.92) -- a different
            # SHAPE, not a crop: 0.707 aspect against 0.781. Forcing the canonical trim on
            # them makes every rendered sheet wider and shorter than the book, so no
            # coordinate can line up however good the CSS is.
            "sheet_pt": [round(page.rect.width, 2), round(page.rect.height, 2)],
            "sheet_aspect": round(page.rect.width / page.rect.height, 4),
            "geometry_source": "text_layer" if sizes else "page_image_required",
            "elements_in_reading_order": elements,
        })
    doc.close()

    _apply_chapter_offset(pages)
    return {"book_id": book_id, "chapter_num": chapter_num, "source_pdf": path,
            "design_key": design.key if design else None,
            "sheet_pt": list(design.trim_pt) if design else None,
            "produced_by": "scripts/extract_ncert_layout.py (PDF text layer)",
            "pages": pages}


def _sample_fills(page, elements, page_w, page_h):
    """Record the FILL the book prints behind each element.

    NCERT tints its tables and its figure panels -- Table 1.1 sits on a peach ground with a
    darker header row, Figure 1.1 on pale yellow. Those are vector fills: they are in the PDF's
    drawings and nowhere in its text, so a renderer that only reads text draws every table on
    bare white and the page stops looking like the book.

    For each element the largest filled rectangle that CONTAINS it is its background. Taking the
    largest containing rect rather than any overlapping one is what keeps a table's header-row
    tint from being reported as the whole table's fill.
    """
    fills = []
    for d in page.get_drawings():
        f = d.get("fill")
        if not f:
            continue
        r = d["rect"]
        if r.width <= 2 or r.height <= 2:
            continue
        if r.width >= 0.97 * page_w and r.height >= 0.97 * page_h:
            continue
        fills.append((r.x0, r.y0, r.x1, r.y1,
                      "#%02x%02x%02x" % tuple(int(round(c * 255)) for c in f),
                      r.width * r.height))
    if not fills:
        return
    for e in elements:
        b = e.get("bbox_pt")
        if not b:
            continue
        inside = [x for x in fills
                  if x[0] <= b[0] + 2 and x[1] <= b[1] + 2
                  and x[2] >= b[2] - 2 and x[3] >= b[3] - 2]
        if inside:
            e["fill"] = min(inside, key=lambda x: x[5])[4]


def _overlaps(a, b, pad=0.0):
    return not (a[2] + pad < b[0] or b[2] + pad < a[0]
                or a[3] + pad < b[1] or b[3] + pad < a[1])


def _absorb_figure_labels(elements, page_w, page_h, pad=14.0):
    """Text standing INSIDE a figure is part of the figure, not a paragraph beside it.

    NCERT labels its diagrams with short words positioned on the artwork -- `Archegoniophore`,
    `Gemma cup`, `Rhizoids`, `(a)`, `(b)`. Those are ordinary text blocks in the PDF, so they
    came out as paragraphs and the renderer drew them as free-floating text over the page,
    producing the scatter of stray words the owner reported. They are ALSO inside the figure
    crop, because the crop is a render of that region -- so they were being shown twice.

    Absorbing them does two things at once: the figure's box grows to include its own labels
    (so the crop stops cutting them off at the artwork's edge), and they stop being drawn a
    second time as live text.

    A caption is NOT absorbed. `Figure 3.2 Bryophytes: ...` is set under the artwork and reads
    as part of the running page, so it stays a real element.

    The pad is 14pt, not the 6pt first tried. NCERT sets a diagram's labels on leader lines
    that stand well clear of the artwork -- `Haplontic`, `Gametophyte (n)`, `Sporophyte (2n)`
    around the life-cycle diagram on BIO11O ch3 p042 all sit 8-12pt outside the merged artwork
    box, so a 6pt reach left them behind as free-floating words scattered across the page.
    """
    figs = [e for e in elements if e["role"] == "figure"]
    if not figs:
        return elements
    # Grow each figure by anything short that sits inside it, repeating until nothing new is
    # absorbed -- a label just outside the artwork pulls the box out, which can then reach a
    # further label.
    absorbed = set()
    changed = True
    while changed:
        changed = False
        for fig in figs:
            fb = fig["bbox_pt"]
            for i, e in enumerate(elements):
                if i in absorbed or e["role"] in ("figure", "figure_caption", "page_furniture",
                                                  "page_number", "running_header",
                                                  "reprint_line", "section_heading"):
                    continue
                txt = (e.get("text") or "").strip()
                # Only SHORT text is a label. A paragraph that happens to sit beside a marginal
                # figure is still a paragraph, and swallowing it would delete real prose.
                if len(txt) > 42 or not txt:
                    continue
                if not _overlaps(e["bbox_pt"], fb, pad):
                    continue
                fb[0] = min(fb[0], e["bbox_pt"][0]); fb[1] = min(fb[1], e["bbox_pt"][1])
                fb[2] = max(fb[2], e["bbox_pt"][2]); fb[3] = max(fb[3], e["bbox_pt"][3])
                fig["bbox_pt"] = fb
                fig["absorbed_labels"] = fig.get("absorbed_labels", []) + [txt]
                absorbed.add(i)
                changed = True
    return [e for i, e in enumerate(elements) if i not in absorbed]


# CASE-SENSITIVE, deliberately. NCERT sets the caption in caps -- `TABLE 1.1 Organisms with
# their Taxonomic Categories` -- while the prose that refers to it is title case: `Table 1.1
# indicates the taxonomic categories to which some common organisms belong.` A case-insensitive
# match swallowed that sentence and every paragraph after it into a "table", cropping a block
# of running prose as an image.
_TABLE_RE = re.compile(r"^\s*TABLE\s*\d+\.\d+")


def _cell_grid(members, page_w, page_h):
    """Text blocks inside a table region -> a real row/column CELL GRID.

    THE TEXT LAYER GIVES A TABLE'S CELLS ROW-MAJOR WITH NO COLUMN INFORMATION, which is why
    concatenating them reads as a sentence: BIO11L ch01's Table 1.1 comes out as
    `Classes Common Major Stored Cell Wall Flagellar Habitat Name Pigments Food Number and
    Position of Insertions` -- three header rows run together. The column structure is not in
    the TEXT, but it IS in the GEOMETRY: every cell of a column starts at the same x, and every
    cell of a row shares a baseline. Clustering those two gives the grid back exactly.

    Rows are clustered on the vertical midpoint with a tolerance of half the median block
    height, so a two-line cell still belongs to one row. Columns are clustered on the left edge
    with a tolerance of 1.5% of the page width -- wide enough to absorb the sub-point jitter of
    a scan, far narrower than any real column gutter in these books.
    """
    spans = []
    for e in members:
        spans.extend(e.get("_spans") or [])
    if len(spans) < 4:
        return None
    tol_x = page_w * 0.012
    ys = sorted({y for _x, y, _t in spans})
    tol_y = 3.0

    rows = []
    for y in ys:
        if rows and abs(y - rows[-1][0]) <= tol_y:
            rows[-1][0] = (rows[-1][0] + y) / 2.0
        else:
            rows.append([y, []])
    for x, y, t in spans:
        r = min(rows, key=lambda rr: abs(rr[0] - y))
        r[1].append((x, t))

    starts = sorted(x for x, _y, _t in spans)
    cols = []
    for x in starts:
        if cols and x - cols[-1][-1] <= tol_x:
            cols[-1].append(x)
        else:
            cols.append([x])
    col_x = [sum(c) / len(c) for c in cols]
    if len(col_x) < 2 or len(rows) < 2:
        return None          # one column or one row is a paragraph, not a table

    grid = []
    for _y, cells in rows:
        row = [""] * len(col_x)
        for x, t in sorted(cells):
            ci = min(range(len(col_x)), key=lambda i: abs(col_x[i] - x))
            row[ci] = (row[ci] + " " + t).strip() if row[ci] else t.strip()
        if any(c for c in row):
            grid.append(row)
    # A WRAPPED CELL IS NOT A NEW ROW. `Musca domestica` sets over two printed lines, so the
    # second line arrives as a row whose first cell is empty and which fills only the columns
    # that wrapped. Left alone, Table 1.1 came out 9 rows for the 5 the book prints, with
    # `domestica` sitting on a row of its own. A row with an empty first cell and fewer than
    # half its columns filled is a continuation, and is folded into the row above it.
    folded = []
    for row in grid:
        filled = sum(1 for c in row if c)
        if (folded and not row[0] and filled and filled <= max(1, len(col_x) // 2)):
            for i, c in enumerate(row):
                if c:
                    folded[-1][i] = (folded[-1][i] + " " + c).strip()
            continue
        folded.append(list(row))
    if len(folded) < 2:
        return None
    return {"rows": len(folded), "cols": len(col_x), "cells": folded,
            "col_x_pt": [round(x, 1) for x in col_x]}


def _mark_tables(elements, page_w, page_h):
    """A printed TABLE becomes ONE element carrying its CELL GRID.

    An earlier version cropped the table as an image and stopped there, on the grounds that the
    column structure was unrecoverable. It is recoverable -- see `_cell_grid` -- and the schema
    asks for the grid, because a cell is what a flashcard or a PYQ cites. The crop is still cut
    and kept as `figure_file`, so a renderer can show the book's own ruled, tinted table when it
    wants fidelity and the grid when it wants data.

    The region runs from the `TABLE n.m` caption down to the last element that still sits
    inside the table's own column band, stopping at the next heading or a gap wider than two
    lines.
    """
    idx = [i for i, e in enumerate(elements) if _TABLE_RE.match(e.get("text") or "")]
    if not idx:
        return elements
    # THE ROWS ARE FOUND BY GEOMETRY, NOT BY LIST ORDER.
    #
    # PyMuPDF does not emit blocks in visual order. Measured on BIO11L ch01 p008, Table 1.1's
    # caption (y 508.5) comes back EIGHTH, after all three of its own rows (y 530.5, 570.7,
    # 599.2). Walking forward from the caption therefore found nothing at all and every table
    # came out as a bare caption with its rows left loose in the running text -- which is what
    # put `Plantae`, `Animalia`, `Monera` down the page as stray bold lines.
    order = sorted(range(len(elements)), key=lambda i: (elements[i]["bbox_pt"][1],
                                                        elements[i]["bbox_pt"][0]))
    pos = {i: k for k, i in enumerate(order)}
    consumed = set()
    for start in idx:
        if start in consumed:
            continue
        cap = elements[start]
        box = list(cap["bbox_pt"])
        members, parts = [], [cap.get("text", "")]
        consumed.add(start)
        for k in range(pos[start] + 1, len(order)):
            j = order[k]
            e = elements[j]
            if j in consumed:
                continue
            if e["role"] in ("section_heading", "page_furniture", "page_number",
                             "running_header", "reprint_line", "figure"):
                break
            eb = e["bbox_pt"]
            if eb[1] - box[3] > 26.0:
                break
            box[0] = min(box[0], eb[0]); box[1] = min(box[1], eb[1])
            box[2] = max(box[2], eb[2]); box[3] = max(box[3], eb[3])
            members.append(e)
            parts.append(e.get("text", ""))
            consumed.add(j)
        cap["role"] = "table"
        cap["bbox_pt"] = box
        _f = [m.get("fill") for m in members if m.get("fill")]
        if _f:
            cap["table_fill"] = collections.Counter(_f).most_common(1)[0][0]
        _hdr = [m.get("fill") for m in members[:3] if m.get("fill")]
        if _hdr and _hdr[0] != cap.get("table_fill"):
            cap["table_header_fill"] = _hdr[0]
        cap["table_text"] = " ".join(p for p in parts if p)
        grid = _cell_grid(members, page_w, page_h)
        if grid:
            cap["table_grid"] = grid
        cap["runs"] = []
    return [e for i, e in enumerate(elements) if i not in consumed or e.get("role") == "table"]


def _median(vals):
    vals = sorted(vals)
    return vals[len(vals) // 2]


def _apply_chapter_offset(pages):
    """Settle on ONE crop offset for the chapter and place every element on the sheet with it.

    Pages that could measure the offset vote; the median wins; pages that could not measure it
    (the opener, a figure-only page, a textless scan) inherit it. Each page records which it was
    so a reviewer can tell a measured placement from an inherited one.
    """
    votes = [p.pop("_measured_offset") for p in pages]
    good = [v for v in votes if v is not None]
    if good:
        dx = _median([v[0] for v in good])
        dy = _median([v[1] for v in good])
        source = f"chapter median of {len(good)}/{len(pages)} measured pages"
    else:
        dx = dy = 0.0
        source = "no page could be measured; pages left on their own sheet"
    for p, vote in zip(pages, votes):
        pw, ph = p["page_width_pt"], p["page_height_pt"]
        sw, sh = p["sheet_pt"]
        if vote is None:
            p["sheet_note"] = f"inherited: {source}"
        else:
            p["sheet_note"] = f"measured; {source}"
        p["sheet_offset_pt"] = [round(dx, 1), round(dy, 1)]
        for e in p["elements_in_reading_order"]:
            e["bbox_sheet"] = [round((e["bbox_pt"][0] + dx) / sw, 4),
                               round((e["bbox_pt"][1] + dy) / sh, 4),
                               round((e["bbox_pt"][2] + dx) / sw, 4),
                               round((e["bbox_pt"][3] + dy) / sh, 4)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", help="e.g. BIO11L-ch01")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    m = re.fullmatch(r"([A-Z]{3}\d{2}[LO])-ch(\d+)", a.chapter)
    if not m:
        raise SystemExit("chapter must look like BIO11L-ch01")
    book, num = m.group(1), int(m.group(2))
    data = extract(book, num)
    out = a.out or os.path.join("ncert", "layout", "%s-ch%02d.json" % (book, num))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=1, ensure_ascii=False)
    npages = len(data["pages"])
    nel = sum(len(p["elements_in_reading_order"]) for p in data["pages"])
    notext = sum(1 for p in data["pages"] if not p["has_text_layer"])
    print("%s  %d pages, %d elements -> %s%s"
          % (a.chapter, npages, nel, out,
             "  (%d pages have NO text layer)" % notext if notext else ""))


if __name__ == "__main__":
    main()
