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
    whole = _smallcaps_run(letters)
    if whole or len(letters) < 3:
        return whole
    # A LINE MAY OPEN IN SMALL CAPS AND GO ON IN TEXT. The Unit 4 biography (BIO11L ch11 p002)
    # sets `MELVIN CALVIN born in Minnesota ...` as `M`+`ELVIN`+` C`+`ALVIN` then the body at
    # the capitals' size; the whole-line test failed on the lower-case body, so the name reached
    # the page in plain capitals. The leading capitals are tested on their own, and only where
    # the text goes on at their large size, after a word break.
    k = 0
    while k < len(letters) and re.fullmatch(_SC_CHARS, letters[k]["text"]):
        k += 1
    # The break may be a typed space or only a gap on the page: `TABLE 11.1` + `Fill in the
    # Columns ...` (BIO11L ch11 p148) is `T`+`ABLE`+` 11.1`, then the caption at 9.5pt with no
    # space character between them.
    gap = letters[k]["bbox"][0] - letters[k - 1]["bbox"][2] if k < len(letters) else 0
    if k < 2 or k == len(letters) or not (letters[k]["text"][:1].isspace()
                                          or letters[k - 1]["text"][-1:].isspace()
                                          or gap > 0.15 * letters[k - 1]["size"]):
        return None
    head = _smallcaps_run(letters[:k])
    if not head:
        return None
    return head + [(s["text"], round(s["size"], 1), False) for s in letters[k:]]


_SC_CHARS = r"[A-Z0-9 .,;:'’‘?!()&\-–—]+"


def _smallcaps_run(letters):
    """`_smallcaps` for spans that must ALL be small caps (see there)."""
    if len(letters) < 2:
        return None
    # Punctuation rides along with the letters: `2.6 VIRUSES, VIROIDS, PRIONS AND LICHENS`
    # (BIO11L ch02 p019) splits as `V` + `IRUSES,` -- the comma kept the whole heading out, and
    # it reached the JSON and the page in plain capitals beside its small-caps siblings.
    # ...and so does a dash: `1.1 FLOWER – A FASCINATING ORGAN OF` (BIO12L ch01 p003) sets
    # an en dash in the span `– A F`, and the heading printed in plain title case.
    # ...and so does a closing `?` or apostrophe: `6.3 WHAT ARE THE EVIDENCES FOR EVOLUTION?`
    # (BIO12L ch06 p004) ends on a 14pt `?` span, `4.1 MENDEL’S LAWS` (ch04 p003) sets `’S`.
    if not all(re.fullmatch(_SC_CHARS, s["text"]) for s in letters):
        return None
    sizes = sorted({round(s["size"], 1) for s in letters})
    if len(sizes) < 2:
        return None
    small, large = sizes[0], sizes[-1]
    if not (0.42 <= small / large <= 0.88):
        return None
    # The small size carries LETTERS. A line whose small spans are digits alone is a formula
    # with a subscript: the turnover line `H2O.` (BIO11L ch12 p162) is `H` + a 7pt `2` + `O.`,
    # read as small caps it reached the JSON as `h2o` flagged `sc`, with no subscript at all.
    # (A small-caps heading may still hold one: `11.8 THE C4 PATHWAY` sets `HE`, `ATHWAY` and
    # the subscript `4` all small.)
    if not any(round(s["size"], 1) < (small + large) / 2 and re.search(r"[A-Z]", s["text"])
               for s in letters):
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
    #
    # AND A BUCKET HAS EDGES. Two pieces of one row can still fall either side of one: Figure
    # 3.1's caption (BIO11L ch03 p025) printed `(a) Green algae ... Figure 3.1 Algae :` because
    # its two first-row pieces sat across a 3pt boundary. Rows are therefore grouped by OVERLAP
    # (`_line_rows`), which has no edges, and read left to right within a row.
    row_list = _line_rows(lines)
    lines = [l for row in row_list for l in row]
    # SIZE AND BASELINE ARE A PROPERTY OF THE PRINTED ROW, not of one line object. The text
    # layer can carry a subscript as a line of its own: the `2` of `N2- fixing` (BIO11L ch03
    # p032) is a 6.1pt line under the 10.5pt row. Measured against itself it is a normal
    # character, so `N2` reached the page as a plain 2. Against its row it is plainly a
    # subscript. Same row also means no forced space between `N` and its `2`.
    row_of = {}
    for row in row_list:
        spans_r = [s for l in row for s in l["spans"] if s["text"].strip()]
        if not spans_r:
            continue
        rsize = max(s["size"] for s in spans_r)
        rbase = max(s["bbox"][3] for s in spans_r if s["size"] >= rsize - 0.05)
        for k, l in enumerate(row):
            row_of[id(l)] = (rsize, rbase, row[k + 1] if k + 1 < len(row) else None)
    runs, dehyphenated = [], []
    for li, line in enumerate(lines):
        spans = [s for s in line["spans"] if s["text"].strip()]
        if not spans:
            continue
        line_size, line_base, same_row_next = row_of.get(
            id(line), (max(s["size"] for s in spans), max(s["bbox"][3] for s in spans), None))
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
                "sc": bool(sc and sc[i][2]),
                # Script detection is SKIPPED inside small caps. The small letters there sit on
                # the SAME baseline as the capitals, but their font box is shorter, so the
                # baseline test reads every one of them as a superscript -- which rendered
                # `The Living World` as `T`+`he `(sup)+`L`+`iving `(sup).
                "script": None if sc and sc[i][2] else _script(s, line_size, line_base),
                "color": "#%06x" % s["color"],
                "size": round(s["size"], 1),
                "font": s["font"],
            })
        # A piece followed by more of the SAME printed row: a space only where the page leaves
        # a word gap, never a forced one (`N` + subscript `2` stays `N2`).
        if same_row_next is not None and pieces:
            nx = [t for t in same_row_next["spans"] if t["text"].strip()]
            gap = (nx[0]["bbox"][0] - spans[-1]["bbox"][2]) if nx else 0
            if gap > line_size * 0.15 and not pieces[-1]["t"].endswith(" "):
                pieces[-1]["t"] += " "
            runs.extend(pieces)
            continue
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

    # A MERGED RUN TAKES ITS FIRST TEXT PIECE'S SIZE -- NOT A BULLET'S. Size is not part of the
    # merge key and the first piece sets it (a small-caps run thereby keeps its capitals' size).
    # BIO11L ch12 p161 opens each list item with a 14pt `•`, so the whole 10.5pt list became
    # one 14pt run and the exact render set it at 14pt with its lines piled onto each other.
    merged = []
    for r in runs:
        key = (r["b"], r["i"], r["sc"], r["script"], r["color"], r["font"])
        if merged and merged[-1]["_key"] == key:
            merged[-1]["t"] += r["t"]
            if merged[-1].pop("_bullet_size", False) and _BULLET_ONLY.sub("", r["t"]):
                merged[-1]["size"] = r["size"]
            elif not _BULLET_ONLY.sub("", merged[-1]["t"]):
                merged[-1]["_bullet_size"] = True
        else:
            r = dict(r); r["_key"] = key
            if not _BULLET_ONLY.sub("", r["t"]):
                r["_bullet_size"] = True
            merged.append(r)
    for r in merged:
        r.pop("_key")
        r.pop("_bullet_size", None)
        r["t"] = re.sub(r"\s+", " ", r["t"])
    merged = [r for r in merged if r["t"].strip() or r["t"] == " "]
    text = "".join(r["t"] for r in merged).strip()
    return merged, text, dehyphenated


_BULLET_ONLY = re.compile(r"[\s•●▪■◦]+")


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
    # A NUMBERED, BOLD HEADING NEAR THE TOP IS A HEADING. `1.2.1 Stamen, Microsporangium and
    # Pollen Grain` (BIO12L ch01 p005) opens its page at y 0.108 -- the Class 12 page is 777.6pt,
    # its header sits higher -- and was taken for the running head and dropped from the chapter.
    # Class 12 sets its fourth-level headings ITALIC, not bold, at 12pt: `4.2.2.1 Incomplete
    # Dominance` opens BIO12L ch04 p010 at y 0.107 and went the same way.
    if (y0f < 0.11 and re.match(r"^\d+\.\d+(\.\d+)*\s+\S", text) and runs
            and (runs[0].get("b") or runs[0].get("i")) and size >= body_size * 1.05):
        return "section_heading"
    # A TABLE OR FIGURE CAPTION IS NEVER THE RUNNING HEAD. `Table 4.1: Contrasting Traits Studied
    # by` opens BIO12L ch04 p005 at y 0.108 -- the Class 12 sheet's head sits higher -- and was
    # filed as the head, so the table had no caption to grow from and vanished from all three
    # deliverables, its rows with it.
    if (y0f < 0.11 or y0f > 0.92) and len(text) < 60 and not _TABLE_RE.match(text) \
            and not re.match(r"(?i)^fig(ure|\.)\s*\d+\.\d+", text.strip()):
        if size <= body_size * 1.2:
            return "running_header"
        # A page that is ALL figure has no prose, so its "body size" is the artwork labels' and
        # the head line looks oversized. A title never carries a folio, though: BIO11L ch9 p004
        # (`Biomolecules 107`, Figure 9.1 filling the page) was typed chapter_title, lost its
        # folio, and came out as page "4", verso.
        folio, head, _ = split_head_line(text, runs)
        if folio is not None and head and not re.match(r"(?i)(chapter|unit)\b", head):
            return "running_header"
        return "chapter_title"
    if size >= body_size * 1.8:
        return "chapter_title"
    if re.match(r"^\d+\.\d+(\.\d+)?\s", text) and (size > body_size * 1.05 or runs[0]["b"]):
        return "section_heading"
    # A FOURTH- OR FIFTH-LEVEL HEADING IS SET ITALIC, often at body size: `4.2.11.3 Class --
    # Osteichthyes` (BIO11L ch04 p048, Bookman-LightItalic 10.5) and `4.2.2.2 Co-dominance`
    # (BIO12L ch04, 12pt). Typed a paragraph, the first was absorbed into Figure 4.20 as a label
    # and lost from all three deliverables. A short, numbered, italic or larger line is a heading.
    if (re.match(r"^\d+(\.\d+){3,}\s+\S", text) and len(text) < 80
            and (size > body_size * 1.05 or runs[0]["b"] or runs[0].get("i"))):
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
        # Long is not prose: Figure 3.1's caption lists every alga it shows (BIO11L ch03 p025,
        # 190 characters) and was typed a paragraph, losing its figure number. Prose is a long
        # text that ENDS a sentence.
        looks_like_prose = ((len(text) > 160 and text.rstrip().endswith("."))
                            or re.match(r"^(indicates|shows|gives|lists|is|are|was|were|"
                                        r"presents|summaris|describ)", tail, re.I))
        # ...unless it is SET as a caption: its label a bold run of its own, the text below body
        # size. Figure 1.8's caption (BIO12L ch01 p010) is 197 characters ending in a full stop,
        # `Figure 1.8` in Bookman-Demi at 9.5pt over 10.5pt prose, and was typed a paragraph.
        label = re.match(r"^(Figure|Fig\.|TABLE|Table)\s*\d+\.\d+", text).group(0)
        set_as_caption = (runs and runs[0].get("b") and runs[0]["t"].strip().startswith(label)
                          and size < body_size * 0.97)
        if set_as_caption or not looks_like_prose:
            return "figure_caption"
    # A note set in the MARGINAL RAIL, not in the measure. The rail mirrors every page, so
    # testing only the left edge found it on versos and missed it on every recto -- measured on
    # BIO11L ch3 p007, whose rail runs x 0.70-0.95 and whose marginal labels classified as body
    # paragraphs. The measure is 0.588 of the sheet wide in both Biology classes, so anything
    # starting beyond 0.68 is past the end of the widest measure a page can set.
    # A rail note is also NARROW. On a recto the measure itself starts at x 0.10, so a block set a
    # half-point under body size ran the whole measure and still passed the left-edge test:
    # BIO11L ch02 p011's `The three-domain system has also been proposed...` (10pt against
    # 10.5pt, 0.588 wide) became a side box. The rail is about 0.17 of the sheet wide.
    if ((x0f < 0.30 or x0f > 0.68) and size < body_size
            and (bbox[2] - bbox[0]) / page_w < 0.40):
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


def visible_drawings(page, hairlines=False):
    """Every filled or stroked path, with `rect` cut to the part of it that actually PRINTS.

    A path's own rect is not where it prints: a clip path decides that. Figure 10.2's pale-blue
    panel (BIO11L ch10 p004) is a radial gradient drawn as ~100 concentric rings, the outer ones
    spanning x 0.24-1.21 of the page, all clipped to the panel at 0.59-0.86. Clustering the raw
    rects built a figure box running to x=1.03 and starting below the panel's top, so the crop
    cut the Early Prophase circle in half and padded into blank margin. The clip stack is read
    from `get_drawings(extended=True)`: a clip at level L bounds every item nested deeper than L.
    A path clipped away entirely is not returned.

    A ZERO-AREA SCISSOR IS NOT A CLIP. Figure 3.2's drawn panels (BIO11L ch03 p028) sit inside
    clips MuPDF reports as `[494,513,498,513]` -- no height -- yet the artwork prints. Honouring
    them emptied every path in panels (a)-(c) and their labels fell out as loose paragraphs, so
    a degenerate scissor is treated as unknown and the enclosing clip stays in force.
    """
    vis = _read_drawings(page)[0]
    return vis if hairlines else [d for d in vis if not d.get("hairline")]


def path_rects(page):
    """Every path's own rect, clipped or not -- what `get_drawings()` reports, from the same read."""
    return _read_drawings(page)[1]


def _read_drawings(page):
    # Keyed by the file's normalised full path: the figure join opens the same PDF as
    # `source_pdfs/...` where the extractor used `source_pdfs\...`, missed the cache, and
    # re-read p014's 1.83 million paths -- the BIO12L ch01 build ran 45 minutes.
    key = (os.path.normcase(os.path.abspath(page.parent.name)), page.number)
    if key not in _DRAWINGS:
        _DRAWINGS[key] = _disk_cached(page, key[0])
    return _DRAWINGS[key]


# AND ONE READ PER PAGE ACROSS BUILDS. A chapter is rebuilt many times while it is checked, and
# every build walked every page's drawings again (BIO12L ch01: 25 pages, p014 alone 51s). The
# reads are kept on disk under `cache/drawings/<pdf sha256>/`, keyed by the file's CONTENT, so
# a changed PDF can never be served an old read. Only the fields the pipeline uses are kept,
# compressed: a dense page is ~3 MB and loads in a second. Bump `_DRAW_CACHE_VERSION` whenever
# `_visible_drawings` or `_coarse_drawings` changes what it returns.
_DRAW_CACHE_VERSION = 2
_DRAW_CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                               "cache", "drawings")
_DRAW_KEEP = ("type", "rect", "fill", "color", "width", "fill_opacity", "seqno", "items", "coarse",
              "hairline")
_PDF_SHA = {}


def _pdf_sha(path):
    if path not in _PDF_SHA:
        import hashlib
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                h.update(chunk)
        _PDF_SHA[path] = h.hexdigest()[:20]
    return _PDF_SHA[path]


def _disk_cached(page, path):
    import pickle
    import zlib
    try:
        f = os.path.join(_DRAW_CACHE_DIR, _pdf_sha(path),
                         "p%04d.v%d.pkl.z" % (page.number + 1, _DRAW_CACHE_VERSION))
    except OSError:
        f = None
    if f and os.path.exists(f):
        try:
            with open(f, "rb") as fh:
                return pickle.loads(zlib.decompress(fh.read()))
        except Exception:                                   # noqa: BLE001 -- re-read below
            pass
    if _content_bytes(page) > _HEAVY_PAGE_BYTES:
        coarse = _coarse_drawings(page)
        got = (coarse, [d["rect"] for d in coarse])
    else:
        vis, raw = _visible_drawings(page)
        slim = []
        for d in vis:
            y = {k: d[k] for k in _DRAW_KEEP if k in d}
            it = y.get("items") or []
            # A long path is artwork; consumers only count its segments' kinds.
            y["items"] = it if len(it) <= 16 else [(i[0],) for i in it[:17]]
            slim.append(y)
        got = (slim, raw)
    if f:
        try:
            os.makedirs(os.path.dirname(f), exist_ok=True)
            tmp = f + ".tmp%d" % os.getpid()
            with open(tmp, "wb") as fh:
                fh.write(zlib.compress(pickle.dumps(got, protocol=5), 1))
            os.replace(tmp, f)
        except OSError:
            pass
    return got


# ONE READ PER PAGE. Five steps walk a page's drawings (figure clustering, drawn marks, fills,
# panels, vector ink), and BIO12L ch01 p014 holds 1.83 million paths -- a 281 MB content stream
# that takes four minutes per read, so the chapter never finished building. Reads are kept for
# the life of the process, keyed by file and page.
_DRAWINGS = {}
#: Compressed content above this is drawn artwork too dense to walk path by path. BIO12L ch01
#: p014 is 24.7 MB; the largest page of BIO11L ch01-ch10 is 2 MB.
_HEAVY_PAGE_BYTES = 8_000_000


def _hex(rgb):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(c * 255))) for c in rgb[:3])


#: Resolution of the one low-resolution render `_fill_shows` samples per page.
_DECOR_CHECK_DPI = 36


def _fill_shows(page, rect, fill, cache):
    """True when a filled shape's colour actually PRINTS over a fair part of its own box.

    A clip is not the only way a shape is hidden: it can be painted and then covered. Figure
    2.10 (BIO12L ch02 p010) draws two peach rounded shapes and paints its picture over them, so
    the book shows none of either -- and the render, drawing decor over the crop, showed both
    above the ovum. The page is rendered once, small, and a shape whose colour covers under a
    fiftieth of its interior is not decoration anyone can see (the opener's green frame,
    mostly under its photograph, still shows round the edges and is kept).
    """
    if "pix" not in cache:
        cache["pix"] = page.get_pixmap(dpi=_DECOR_CHECK_DPI, alpha=False)
    pix = cache["pix"]
    k = _DECOR_CHECK_DPI / 72.0
    x0, y0 = int(rect.x0 * k) + 1, int(rect.y0 * k) + 1
    x1, y1 = int(rect.x1 * k) - 1, int(rect.y1 * k) - 1
    if x1 <= x0 or y1 <= y0:
        return True                       # too small to sample: keep it
    want = [round(c * 255) for c in fill[:3]]
    hit = tot = 0
    for y in range(max(0, y0), min(pix.height, y1)):
        for x in range(max(0, x0), min(pix.width, x1)):
            px = pix.pixel(x, y)
            tot += 1
            hit += sum(abs(a - b) for a, b in zip(px, want)) <= 45
    return not tot or hit >= tot / 50


def page_decor(page, figure_boxes, ruled_boxes=()):
    """The page's decoration as the PDF draws it: [{z, kind, bbox_pt, fill, stroke, width,
    opacity, radius}], in paint order (`z` is MuPDF's sequence number, the same order the page
    is painted in).

    THE BOOK'S PANELS ARE VECTOR SHAPES, AND ONLY THEIR MEASUREMENT REPRODUCES THEM. The Class 12
    opener (BIO12L ch01 p003) paints a pale-green panel #d4ead4 over the whole head of the page,
    an orange band #f7941d under it, a peach rounded box #fee6cb behind the contents list and a
    green frame behind the photograph; the summary sits in a tinted box with a double rule and
    captions on tinted strips. None of that is an image, so none of it was cut as art, and the
    render drew the panel's colour behind each title line instead -- boxes round the words --
    and no band, box or tint at all.

    Kept: filled or stroked shapes of a panel's size (>= 20 x 6pt, or a rule >= 40pt long), and
    a rounded box (a few curve segments). Left out: anything centred inside a figure (that is
    the figure's own drawing), the watermark and its 10% mask, a white page ground, and paths
    reaching far off the page.
    """
    import book_design
    pw, ph = page.rect.width, page.rect.height
    out = []
    _pix = {}
    for d in visible_drawings(page, hairlines=True):
        if d.get("coarse"):
            return None
        r = d["rect"]
        w, h = r.width, r.height
        fill, stroke = d.get("fill"), (d.get("color") if "s" in (d.get("type") or "") else None)
        # A stroked straight line is recorded as the band of ink it prints (`rect` already
        # carries the stroke's width): a filled rule, so it draws at its true weight.
        if d.get("hairline"):
            fill, stroke = stroke, None
        if not fill and not stroke:
            continue
        if r.x0 < -0.1 * pw or r.x1 > 1.1 * pw or r.y0 < -0.1 * ph or r.y1 > 1.1 * ph:
            continue
        # FURNITURE BLEEDS. A folio tab or band runs off the trim; it is never a figure's own
        # drawing, however a figure box lies, and its thin keyline (5pt under BIO12L ch01's
        # folio tab) counts too. On p012 an early figure box covered the tab's centre and the
        # tab was dropped, leaving the white folio `12` on white.
        bleeds = r.x0 <= 1 or r.y0 <= 1 or r.x1 >= pw - 1 or r.y1 >= ph - 1
        panel = (w >= 20 and h >= 6 and w * h >= 300) or (bleeds and w >= 20 and h >= 2)
        rule = stroke and ((w >= 40 and h < 3) or (h >= 40 and w < 3))
        if d.get("hairline"):
            panel, rule = False, max(w, h) >= 40
            # a table's grid and a figure's own lines are in their crops, not page decoration
            if any(f[0] - 2 <= (r.x0 + r.x1) / 2 <= f[2] + 2 and f[1] - 2 <= (r.y0 + r.y1) / 2
                   <= f[3] + 2 for f in ruled_boxes):
                continue
        if not (panel or rule):
            continue
        items = [it[0] for it in d.get("items") or []]
        # A box is a few straight sides, or a rounded box: four corners of at most two curve
        # segments each (the opener's contents box is 4 sides + 8 curves).
        if any(k not in ("re", "qu", "l", "c") for k in items) or len(items) > 16:
            continue                      # an outline of artwork, not a box
        if items.count("c") > 8 or items.count("l") > 6:
            continue
        frac = (r.x0 / pw, r.y0 / ph, r.x1 / pw, r.y1 / ph)
        if book_design.is_watermark(frac) or (fill and (d.get("fill_opacity") or 1) < 0.2):
            continue
        if fill and min(fill) > 0.97 and w * h > 0.6 * pw * ph:
            continue                      # the white ground
        cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
        if bleeds:
            figure_boxes_here = []
        else:
            figure_boxes_here = figure_boxes
        if any(f[0] <= cx <= f[2] and f[1] <= cy <= f[3] and w * h < 0.7 * (f[2] - f[0]) * (f[3] - f[1])
               for f in figure_boxes_here):
            continue
        if fill and panel and not _fill_shows(page, r, fill, _pix):
            _pix.setdefault("hidden", []).append(r)
            continue                      # painted, then covered: the book never shows it
        # ...and so is the OUTLINE drawn round it as a separate path, which the colour test
        # cannot see through: Figure 2.10's two shapes left their thin black keylines behind.
        if not fill and stroke and panel and any(
                abs(r.x0 - q.x0) < 0.6 and abs(r.y0 - q.y0) < 0.6
                and abs(r.x1 - q.x1) < 0.6 and abs(r.y1 - q.y1) < 0.6
                for q in _pix.get("hidden", [])):
            continue
        radius = 0.0
        if "c" in items:
            c0 = next(it for it in d["items"] if it[0] == "c")
            radius = round(min(abs(c0[1].x - c0[4].x), abs(c0[1].y - c0[4].y)) or
                           max(abs(c0[1].x - c0[4].x), abs(c0[1].y - c0[4].y)), 1)
        out.append({"z": d.get("seqno"), "kind": "rule" if rule and not panel else "panel",
                    "bbox_pt": [round(r.x0, 2), round(r.y0, 2), round(r.x1, 2), round(r.y1, 2)],
                    "fill": _hex(fill) if fill else None,
                    "stroke": _hex(stroke) if stroke else None,
                    "width": round(d.get("width") or 0, 2) if stroke else None,
                    "opacity": round(d["fill_opacity"], 3)
                    if fill and (d.get("fill_opacity") or 1) < 0.999 else None,
                    "radius": radius or None})
    return out


def _stamp_image_z(page, elements):
    """Give each placed picture element its paint-order number (`z`), matched by box from the
    page's bbox log, so page art can be drawn in the book's order among `page_decor` shapes:
    on the Class 12 opener the green panel is painted OVER the header picture's lower half."""
    log = [(i, b) for i, (kind, b) in enumerate(page.get_bboxlog()) if "image" in kind]
    for e in elements:
        if e["role"] not in ("page_furniture", "figure"):
            continue
        eb = e["bbox_pt"]
        best = None
        for i, b in log:
            ix = min(eb[2], b[2]) - max(eb[0], b[0]); iy = min(eb[3], b[3]) - max(eb[1], b[1])
            if ix <= 0 or iy <= 0:
                continue
            u = ((eb[2] - eb[0]) * (eb[3] - eb[1]) + (b[2] - b[0]) * (b[3] - b[1]) - ix * iy)
            iou = ix * iy / u if u else 0
            if iou > 0.9 and (best is None or iou > best[1]):
                best = (i, iou)
        if best:
            e["z"] = best[0]


def _content_bytes(page):
    doc = page.parent
    return sum(int(doc.xref_get_key(x, "Length")[1] or 0) for x in page.get_contents())


def _coarse_drawings(page, cell=4.0):
    """A page too dense to walk path by path, as its painted area on a `cell`-pt grid.

    `get_bboxlog` gives every path's printed box in under a minute where `get_drawings` takes
    four; the boxes are merged into grid rows of touching cells, so clustering sees the same
    outline of ink from a few thousand rects. No colours: a fill sampled from a page like this
    is artwork, never a tint the renderer needs.
    """
    import numpy as np
    w, h = page.rect.width, page.rect.height
    nx, ny = int(w // cell) + 1, int(h // cell) + 1
    grid = np.zeros((ny, nx), bool)
    # Vectorised: 1.8 million boxes in a Python loop took minutes. A box within one or two
    # cells each way (nearly all of them) marks its corner cells at once; the few larger ones
    # are painted one by one.
    b = np.array([bb for kind, bb in page.get_bboxlog() if "path" in kind], float).reshape(-1, 4)
    x0 = np.clip((b[:, 0] // cell).astype(int), 0, nx - 1)
    y0 = np.clip((b[:, 1] // cell).astype(int), 0, ny - 1)
    x1 = np.clip((b[:, 2] // cell).astype(int), 0, nx - 1)
    y1 = np.clip((b[:, 3] // cell).astype(int), 0, ny - 1)
    ok = (b[:, 2] > b[:, 0]) & (b[:, 3] > b[:, 1])
    small = ok & (x1 - x0 <= 1) & (y1 - y0 <= 1)
    for yy in (y0, y1):
        for xx in (x0, x1):
            grid[yy[small], xx[small]] = True
    for i in np.flatnonzero(ok & ~small):
        grid[y0[i]:y1[i] + 1, x0[i]:x1[i] + 1] = True
    out = []
    for gy in range(ny):
        row = np.flatnonzero(np.diff(np.r_[0, grid[gy].astype(np.int8), 0]))
        for a, b in zip(row[::2], row[1::2]):
            r = pymupdf.Rect(a * cell, gy * cell, b * cell, (gy + 1) * cell) & page.rect
            if not r.is_empty:
                out.append({"type": "f", "rect": r, "fill": None, "coarse": True})
    return out


def _visible_drawings(page):
    out, raw, clips = [], [], []          # clips: [(level, effective rect)]
    for d in page.get_drawings(extended=True):
        lvl = d.get("level", 0)
        while clips and clips[-1][0] >= lvl:
            clips.pop()
        if d["type"] == "clip":
            r = pymupdf.Rect(d["scissor"])
            if r.width < 1 or r.height < 1:
                r = clips[-1][1] if clips else page.rect
            elif clips:
                r = r & clips[-1][1]
            clips.append((lvl, r))
            continue
        if d["type"] == "group" or "rect" not in d:
            continue
        r = pymupdf.Rect(d["rect"])
        raw.append(pymupdf.Rect(r))
        # A RULE HAS NO AREA. A straight stroked line is a zero-height rect, and `is_empty` threw
        # every one away -- so the orange double rule under EXERCISES and the grey bar under the
        # Class 12 contents box (BIO12L ch03-ch06) never reached `page_decor`. Such a line is
        # kept as the band its stroke paints, flagged `hairline`; `visible_drawings` hands it
        # only to callers that ask, so no other consumer sees a drawing it did not see before.
        hair = False
        if (r.is_empty and "s" in (d.get("type") or "") and (d.get("width") or 0) > 0
                and (r.width == 0) != (r.height == 0)
                and all(it[0] == "l" for it in d.get("items") or [])):
            half = d["width"] / 2.0
            r = (pymupdf.Rect(r.x0, r.y0 - half, r.x1, r.y1 + half) if r.height == 0
                 else pymupdf.Rect(r.x0 - half, r.y0, r.x1 + half, r.y1))
            hair = True
        if clips:
            r = r & clips[-1][1]
        if r.is_empty:
            continue
        out.append(dict(d, rect=r, hairline=True) if hair else dict(d, rect=r))
    return out, raw


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
    for d in visible_drawings(page):
        r = d["rect"]
        if r.width <= 0 or r.height <= 0:
            continue
        if r.width >= 0.97 * page_w and r.height >= 0.97 * page_h:
            continue                      # the page ground
        if r.y1 / page_h <= HEAD_ZONE or r.y0 / page_h >= FOOT_ZONE:
            continue                      # header band / strip / folio tab / footer bar
        if r.width >= 0.95 * page_w:
            continue                      # a full-bleed bar is furniture, never a figure
        # A SHAPE TOUCHING THE TRIM IS FURNITURE (the rule `page_decor` keeps). The Class 12
        # folio tab runs off the left edge two-thirds down; clustered with Figure 4.1 (BIO12L
        # ch04 p004) and Figure 4.11 (p018) it pulled both boxes to x 0. Not on a coarse page:
        # its strips are rows of grid cells, and a row reaching the trim is not furniture (BIO12L
        # ch01 p014's Figure 1.11 then clustered across into the next column).
        if not d.get("coarse") and (r.x0 <= 1 or r.x1 >= page_w - 1):
            continue
        # THE WATERMARK'S MASK IS A PATH. Every page of BIO11L ch02 carries one solid black
        # fill at exactly the watermark's rect (65,192)-(532,658). It touches every drawing in
        # the middle of the page, so clustering fused all of a page's figures, the mask and the
        # text into one page-sized blob -- which the text test below then threw away, and
        # Figures 2.1, 2.3 and 2.6 rendered as labels with no artwork. No real figure is one
        # path covering a third of the page; a drawing is made of many small ones.
        frac = (r.x0 / page_w, r.y0 / page_h, r.x1 / page_w, r.y1 / page_h)
        if design_lib.is_watermark(frac) or r.width * r.height > 0.30 * page_w * page_h:
            continue
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


def _absorb_drawn_marks(page, elements, page_w, page_h, pad=14.0):
    """Grow each figure to take in the small DRAWN marks beside it.

    Not every label is text. Figure 3.3's `(a)` under the Selaginella photograph (BIO11L ch03
    p031) is drawn as vector outlines, not set as a character -- the text layer has no `(a)`
    there at all -- and `vector_figures` discards clusters that small as dust. So the crop
    stopped at the photograph's edge and panel (a) printed with no label while (b), (c), (d)
    had theirs. A small cluster within the label reach of a figure is taken into it, by the
    same rules as a text label: it may not make the figure overlap another figure, and the
    grown box may not reach running text (so the crop never bakes prose into the picture).
    """
    figs = [e for e in elements if e["role"] == "figure"]
    if not figs:
        return
    texts = [e["bbox_pt"] for e in elements if e["role"] not in
             ("figure", "page_furniture") and (e.get("text") or "").strip()]
    rects = []
    for d in visible_drawings(page):
        r = d["rect"]
        if 0 < r.width < 40 and 0 < r.height < 40 and r.y0 / page_h > 0.13 and r.y1 / page_h < 0.92:
            rects.append((r.x0, r.y0, r.x1, r.y1))
    if not rects:
        return
    for (mx0, my0, mx1, my1), _n in merge_image_blocks(rects, page_w, page_h, gap_pt=3.0, min_pt=4.0):
        mb = [mx0, my0, mx1, my1]
        if (mx1 - mx0) > 40 or (my1 - my0) > 40 or any(_overlaps(mb, t) for t in texts):
            continue
        near = [f for f in figs if _overlaps(mb, f["bbox_pt"], pad)]
        if len(near) != 1:
            continue
        fig = near[0]
        fb = fig["bbox_pt"]
        grown = [min(fb[0], mx0), min(fb[1], my0), max(fb[2], mx1), max(fb[3], my1)]
        if any(o is not fig and _overlaps(grown, o["bbox_pt"]) for o in figs):
            continue
        if any(_overlaps(grown, t, _CROP_PAD) and not _overlaps(fb, t, _CROP_PAD) for t in texts):
            continue
        fig["bbox_pt"] = grown


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


def _line_rows(lines):
    """A block's line objects grouped into PRINTED ROWS, rows top to bottom, each left to right.

    PyMuPDF orders a block's lines by its own stream, which for a caption set as a little table
    is column by column: Figure 3.1's caption (BIO11L ch03 p025) came out `(a) Green algae (i)
    Volvox (ii) Ulothrix Figure 3.1 Algae : (b) Brown algae ...`, the figure number in the
    middle. A row is every line whose height overlaps it by half -- a superscript `th` raised
    3pt above `20` still overlaps its line, so it stays where it was printed.
    """
    rows = []
    for ln in sorted(lines, key=lambda l: (l["bbox"][1] + l["bbox"][3]) / 2):
        y0, y1 = ln["bbox"][1], ln["bbox"][3]
        for r in rows:
            ov = min(y1, r["y1"]) - max(y0, r["y0"])
            if ov >= 0.5 * min(y1 - y0, r["y1"] - r["y0"]):
                r["lines"].append(ln)
                r["y0"], r["y1"] = min(r["y0"], y0), max(r["y1"], y1)
                break
        else:
            rows.append({"y0": y0, "y1": y1, "lines": [ln]})
    rows.sort(key=lambda r: r["y0"])
    return [sorted(r["lines"], key=lambda l: l["bbox"][0]) for r in rows]


_LABEL_ROW = re.compile(r"^\s*(?:\(\s*[a-z](?:\s*-\s*[ivx]+)?\s*\)\s*)+$")


def _line_text(ln):
    return "".join(s.get("text", "") for s in ln.get("spans", []))


def _split_offcolumn_tail(blocks, gap=40.0):
    """A block's LAST lines, set well left of all its others in another face, are their own block.

    The Unit 3 biography (BIO11L ch08 p002) prints the portrait's caption `G.N. Ramachandran`
    (Bookman-Demi, x 100) under the photograph, and the text layer files it as the last line of
    the biography beside it (Bookman-Light, every line at x 246). The paragraph's box then
    spanned the portrait -- the render set the biography over the photograph -- and the agent's
    text, which never repeats the caption, replaced the name out of the chapter. Trailing lines
    starting > `gap` points left of every other line, in a different face, are split off.
    """
    def face(lines):
        c = collections.Counter()
        for ln in lines:
            for s in ln.get("spans", []):
                if s.get("text", "").strip():
                    c[s.get("font")] += len(s["text"].strip())
        return c.most_common(1)[0][0] if c else None

    def union(lines):
        bs = [ln["bbox"] for ln in lines]
        return (min(b[0] for b in bs), min(b[1] for b in bs),
                max(b[2] for b in bs), max(b[3] for b in bs))
    out = []
    for b in blocks:
        lines = b.get("lines") if b.get("type") == 0 else None
        if not lines or len(lines) < 3:
            out.append(b)
            continue
        # The block's own left edge is where MOST of its lines start: a two-line caption tail
        # must not set the bar for its own second line.
        x0s = sorted(round(ln["bbox"][0]) for ln in lines)
        main_x0 = x0s[len(x0s) // 2]
        k = len(lines)
        while k > 2 and _line_text(lines[k - 1]).strip() and lines[k - 1]["bbox"][0] < main_x0 - gap:
            k -= 1
        if k < len(lines) and min(ln["bbox"][0] for ln in lines[:k]) < main_x0 - gap:
            k = len(lines)                  # the block's body starts out there too: not a tail
        tail, rest = lines[k:], lines[:k]
        # ...or a caption: `Figure 10.2 c to e : A diagrammatic / view of stages in Mitosis`
        # (BIO11L ch10 p124) is mostly in the paragraph's own light face, under its picture at x
        # 80 while the Cytokinesis paragraph runs at x 257 -- glued on, it widened that paragraph
        # over the figure and the caption was lost. A tail that opens with its label goes too.
        is_caption = bool(tail) and _CAPTION_START.match(_line_text(tail[0]).strip())
        if not tail or (face(tail) == face(rest) and not is_caption):
            out.append(b)
            continue
        out.append({**b, "lines": rest, "bbox": union(rest)})
        out.append({**b, "lines": tail, "bbox": union(tail)})
    return out


def _drop_overprint(blocks, tol=1.0):
    """One line for text the page draws several times over itself, marked bold.

    FAKE BOLD. NCERT sets some headings in a light italic and thickens it by drawing the same
    text repeatedly, each copy nudged a fraction of a point: BIO11L ch04 p047 draws `Class --
    Cyclostomata` FIVE times, offsets within 0.35pt. The text layer returns every copy, so the
    heading read `Class -- CyclostomataClass -- CyclostomataClass -- ...` and overflowed its box.
    A line whose text matches a kept line drawn within `tol` points of it is the same ink: it
    is dropped, and the kept copy is flagged bold (PyMuPDF flag 16), because that is how it
    prints. Text repeated ELSEWHERE on the page is untouched.
    """
    # A COPY OF THE LINE'S START IS THE SAME INK TOO. BIO12L ch01 p011 thickens the label of
    # `(i) Autogamy : In this type, pollination ...` by drawing `Autogamy` four more times at the
    # line's own origin. Those copies matched no whole line, so one was kept beside the full line:
    # the text held `Autogamy` twice, its bold copy was placed on the NEXT `Autogamy` in the
    # paragraph (`rare. Autogamy in such flowers`, printed plain) and the label stayed unbold.
    # Such a copy is dropped and the full line's leading characters are flagged bold.
    every = [(ln, _line_text(ln).strip()) for b in blocks
             if b.get("type") == 0 for ln in b.get("lines") or []]
    prefix_copies = set()
    for ln, t in every:
        for other, ot in every:
            if (other is ln or not t or len(ot) <= len(t) or not ot.startswith(t)
                    or abs(other["bbox"][0] - ln["bbox"][0]) >= tol
                    or abs(other["bbox"][1] - ln["bbox"][1]) >= tol):
                continue
            prefix_copies.add(id(ln))
            done = 0
            for s in other["spans"]:
                if done >= len(t):
                    break
                if s["text"].strip():
                    s["flags"] = s.get("flags", 0) | 16
                done += len(s["text"].lstrip() if done == 0 else s["text"])
            break
    kept = []                                   # (text, x0, y0, line)
    out = []
    for b in blocks:
        if b.get("type") != 0 or not b.get("lines"):
            out.append(b)
            continue
        lines = []
        for ln in b["lines"]:
            if id(ln) in prefix_copies:
                continue
            t = _line_text(ln).strip()
            x0, y0 = ln["bbox"][0], ln["bbox"][1]
            twin = next((k for k in kept if t and k[0] == t
                         and abs(k[1] - x0) < tol and abs(k[2] - y0) < tol), None)
            if twin:
                for s in twin[3]["spans"]:
                    s["flags"] = s.get("flags", 0) | 16
                continue
            kept.append((t, x0, y0, ln))
            lines.append(ln)
        if lines:
            bx = [l["bbox"] for l in lines]
            out.append({**b, "lines": lines,
                        "bbox": (min(x[0] for x in bx), min(x[1] for x in bx),
                                 max(x[2] for x in bx), max(x[3] for x in bx))})
    return out


_CAPTION_START = re.compile(r"^\s*(?:Figure|Fig\.|TABLE|Table)\s*\d")


def _join_caption_lines(elements, gap_pt=4.0):
    """A caption's second line, set as a block of its own, is still the caption.

    The text layer can return a two-line caption as two blocks: Figure 8.2 (BIO11L ch08 p006)
    gives `Figure 8.2 Diagram showing comparison of` and, 1.7pt under it, `eukaryotic cell with
    other organisms`; Figure 8.10 gives its `(b) Diagrammatic representation ...` line apart. The
    second block was classed as a side note, placed in reading order after the next paragraph,
    so the join could not hand it to the agent's caption and it printed as a box of loose text.
    A block directly under a `Figure n.m` caption, inside its width and in its type size, is
    the caption's next line.
    """
    caps = [e for e in elements if e["role"] == "figure_caption"
            and _CAPTION_START.match(e.get("text") or "") and e.get("runs")]
    gone = set()
    for cap in caps:
        size = cap["runs"][-1].get("size")
        grown = True
        while grown:
            grown = False
            cb = cap["bbox_pt"]
            for i, e in enumerate(elements):
                if i in gone or e is cap or e["role"] not in ("side_note", "paragraph", "list"):
                    continue
                eb, txt = e["bbox_pt"], (e.get("text") or "").strip()
                if not txt or not e.get("runs") or _CAPTION_START.match(txt):
                    continue
                # It STARTS under the caption; it may run wider than the first line. Figure 1.2's
                # first line `Figure 1.2 (a) A typical stamen;` (BIO12L ch01 p005) is shorter than
                # `(b) three-dimensional cut section`, which was refused, absorbed into the
                # figure as a label, and lost from the caption. The type size keeps prose out.
                # A caption's `Note:` is set a little apart -- 4.7pt under Figure 4.11's last line
                # (BIO12L ch04 p018) -- and was printed as a loose paragraph under the figure.
                reach = 8.0 if re.match(r"(?i)note\s*:", txt) else gap_pt
                if not (-1.0 <= eb[1] - cb[3] <= reach
                        and cb[0] - 2 <= eb[0] < cb[2]):
                    continue
                if size is None or any(abs((r.get("size") or 0) - size) > 0.3 for r in e["runs"]):
                    continue
                # A TABLE's caption runs on in its own bold: `Table 4.1: Contrasting Traits
                # Studied by` / `Mendel in Pea` (BIO12L ch04 p005). Only a bold line continues it,
                # so the header row under it is never taken.
                if re.match(r"\s*(TABLE|Table)", cap.get("text") or "") and not all(
                        r.get("b") for r in e["runs"] if (r.get("t") or "").strip()):
                    continue
                cap["text"] = cap["text"].rstrip() + " " + txt
                cap["runs"] = cap["runs"] + [dict(cap["runs"][-1], t=" ")] + e["runs"]
                cap["bbox_pt"] = [min(cb[0], eb[0]), cb[1], max(cb[2], eb[2]), eb[3]]
                cap["_x0"], cap["_x1"] = cap["bbox_pt"][0], cap["bbox_pt"][2]
                cap["_lines"] = (cap.get("_lines") or []) + (e.get("_lines") or [])
                cap["line_count"] = (cap.get("line_count") or 1) + (e.get("line_count") or 1)
                gone.add(i)
                grown = True
                break
    return [e for i, e in enumerate(elements) if i not in gone]


def _split_caption_columns(blocks, row_gap=20.0):
    """A figure caption and the prose in the NEXT COLUMN are two blocks, even when the text
    layer delivers them as one.

    Measured on BIO11L ch04 p038: the left column's `Figure 4.2 Showing germinal layers : (a)
    Diploblastic (b) Triploblastic` and the right column's paragraph `Animals in which the cells
    are arranged in two embryonic layers ...` arrive as ONE block. Read row by row they
    interleave, the agent's paragraph text then replaced the whole block, and the caption
    disappeared from the chapter.

    The caption's group is its `Figure n.m` line plus every line joined to it -- on the same
    row within `row_gap` points, or overlapping it horizontally. It is split off only when what
    is left is a separate column that shares no horizontal span with it, so a caption set as a
    little table (Figure 3.1's label beside its rows) stays whole, and a table row is never cut.
    """
    out = []
    for b in blocks:
        lines = b.get("lines") if b.get("type") == 0 else None
        cap = next((l for l in lines or [] if _CAPTION_START.match(_line_text(l))), None)
        if not cap:
            out.append(b)
            continue
        group, grown = [cap], True
        gx0, gx1 = cap["bbox"][0], cap["bbox"][2]
        while grown:
            grown = False
            for l in lines:
                if any(l is g for g in group):
                    continue
                x0, y0, x1, y1 = l["bbox"]
                same_row = any(min(y1, g["bbox"][3]) - max(y0, g["bbox"][1]) > 0
                               and (x0 - g["bbox"][2] < row_gap and g["bbox"][0] - x1 < row_gap)
                               for g in group)
                below = any(0 <= y0 - g["bbox"][3] < 14.0 for g in group)
                if same_row or (below and min(x1, gx1) - max(x0, gx0) > 0):
                    group.append(l)
                    gx0, gx1 = min(gx0, x0), max(gx1, x1)
                    grown = True
        rest = [l for l in lines if not any(l is g for g in group)]
        if not rest or any(min(l["bbox"][2], gx1) - max(l["bbox"][0], gx0) > 0 for l in rest):
            out.append(b)
            continue
        for part in (group, rest):
            bx = [l["bbox"] for l in part]
            out.append({**b, "lines": part,
                        "bbox": (min(x[0] for x in bx), min(x[1] for x in bx),
                                 max(x[2] for x in bx), max(x[3] for x in bx))})
    return out


def _split_head_from_title(blocks, page_h):
    """The running head is its own line, even when the text layer files it with a title.

    BIO12L ch03 p010 prints `BIOLOGY` (8pt, y 0.077) above the orange 30pt `EXERCISES`, and the
    layer returns both as ONE block. It classified as a chapter title, `EXERCISES` opened the
    section and `BIOLOGY` was left over as a content box in the JSON, the Markdown and the page.
    A first row in the head zone (top 11% of the page) set at under 60% of the size of the rows
    below it is split off as a block of its own, which then classifies as the running head.
    """
    out = []
    for b in blocks:
        if b.get("type") != 0 or len(b.get("lines") or []) < 2:
            out.append(b)
            continue
        rows = _line_rows(b["lines"])
        if len(rows) < 2:
            out.append(b)
            continue

        def size(r):
            return max((s["size"] for ln in r for s in ln["spans"] if s["text"].strip()),
                       default=0)
        head, rest = rows[0], [ln for r in rows[1:] for ln in r]
        top = min(ln["bbox"][1] for ln in head)
        if top < 0.11 * page_h and 0 < size(head) < 0.6 * max(size(r) for r in rows[1:]):
            for part in (head, rest):
                bx = [ln["bbox"] for ln in part]
                out.append({**b, "lines": part,
                            "bbox": (min(x[0] for x in bx), min(x[1] for x in bx),
                                     max(x[2] for x in bx), max(x[3] for x in bx))})
            continue
        out.append(b)
    return out


def _trim_line_start(ln, k):
    """Cut the first `k` characters off a text line, span by span (text and `chars` alike)."""
    for s in ln.get("spans") or []:
        if k <= 0:
            break
        cut = min(k, len(s.get("text", "")))
        s["text"] = s["text"][cut:]
        if s.get("chars"):
            s["chars"] = s["chars"][cut:]
            if s["chars"]:
                s["bbox"] = (s["chars"][0]["bbox"][0],) + tuple(s["bbox"][1:])
        k -= cut
    ln["spans"] = [s for s in ln.get("spans") or [] if s.get("text")]


def _drop_overlap_copies(blocks, tol=1.0):
    """Fake bold drawn as OVERLAPPING PIECES, not whole copies, kept once.

    BIO11L ch12 p157 thickens the question `What then would be the maximum ...` with copies
    that start part-way along the line -- `What then would be the`, then `the maximum` begun
    inside it, then `maximum` again. No copy is a whole line or a line's start, so
    `_drop_overprint` kept them all: the text read `be the the maximum maximum`, the agent's
    text no longer matched, and only `What then would be` came out italic. A line that STARTS
    INSIDE another line's box on the same baseline and opens with that line's own ending is
    the same ink: the repeated part is cut (all of it, when nothing else is left), and both
    lines are flagged bold, as `_drop_overprint` flags whole copies.
    """
    rows = sorted((ln for b in blocks if b.get("type") == 0 for ln in b.get("lines") or []),
                  key=lambda ln: ln["bbox"][0])
    gone = set()
    for ln in rows:
        t = _line_text(ln)
        if not t.strip():
            continue
        x0, y0 = ln["bbox"][0], ln["bbox"][1]
        for o in rows:
            if o is ln or id(o) in gone or abs(o["bbox"][1] - y0) >= tol:
                continue
            if not (o["bbox"][0] + tol < x0 < o["bbox"][2] - tol):
                continue
            ot = _line_text(o).rstrip()
            def whole_words(j):
                head = t[:j].rstrip()
                return (len(head) >= 3 and ot.endswith(head)
                        and (len(ot) == len(head) or not ot[-len(head) - 1].isalnum())
                        and (j == len(t) or not t[j - 1].isalnum() or not t[j].isalnum()))
            k = max((j for j in range(3, len(t) + 1) if whole_words(j)), default=0)
            if not k:
                continue
            # Bold where the ink is doubled: the copy, and only the TAIL of the line it lies
            # on -- `cent. What then would be` starts with plain `cent.`, drawn once.
            left = len(t[:k].rstrip())
            for s in reversed(o.get("spans") or []):
                if left <= 0:
                    break
                if s.get("text", "").strip():
                    s["flags"] = s.get("flags", 0) | 16
                left -= len(s.get("text", "").rstrip() if left == len(t[:k].rstrip())
                            else s.get("text", ""))
            # What is left of the line after the repeated part is bold only in the face of the
            # copy: `ammonotelic in nature.` (BIO11L ch16 p205) repeats the italic `ammonotelic`
            # and prints `in nature.` once, upright -- it came out bold, as did `(ETS) (Figure
            # 12.4) and it is` (ch12 p160). `the maximum` (ch12 p157) is the copy's own face.
            seen, head_fonts = 0, set()
            for s in ln.get("spans") or []:
                if s.get("text", "")[:max(0, k - seen)].strip():
                    head_fonts.add(s.get("font"))
                seen += len(s.get("text", ""))
            if not t[k:].strip():
                gone.add(id(ln))
            else:
                _trim_line_start(ln, k)
            for s in ln.get("spans") or []:
                if s.get("text", "").strip() and s.get("font") in head_fonts:
                    s["flags"] = s.get("flags", 0) | 16
            break
    if not gone:
        return blocks
    out = []
    for b in blocks:
        if b.get("type") == 0 and b.get("lines"):
            lines = [ln for ln in b["lines"] if id(ln) not in gone]
            if not lines:
                continue
            b = {**b, "lines": lines}
        out.append(b)
    return out


def _prepare_text_blocks(blocks):
    """Put each text block's lines in reading order, and split panel labels off captions.

    PANEL LABELS ARE NOT CAPTION. Figure 3.5's photographs are labelled `(a)` and `(b)` under
    each picture, and the text layer delivers those two labels in the SAME block as the caption
    below them: the page printed `(b) (a) Figure 3.5 Angiosperms : ...`. Leading rows made only
    of labels are split off, one element per label at its own measured position, so each joins
    the panel it sits under (`_absorb_figure_labels`) and the caption starts at `Figure`. A block
    that is nothing but labels -- `(d) (c)` under two panels of Figure 3.3 -- is split the same
    way, so neither label can drag one panel's box across the other.
    """
    blocks = _split_offcolumn_tail(_split_caption_columns(
        _drop_overlap_copies(_drop_overprint(blocks))))
    out = []
    for b in blocks:
        if b.get("type") != 0 or not b.get("lines"):
            out.append(b)
            continue
        rows = _line_rows(b["lines"])
        texts = [" ".join(_line_text(l) for l in r).strip() for r in rows]
        lead = 0
        while lead < len(rows) and _LABEL_ROW.match(texts[lead] or "x"):
            lead += 1
        rest = [l for r in rows[lead:] for l in r]
        if lead and (lead == len(rows) or re.match(r"^\s*(Figure|Fig\.)\s*\d", texts[lead])):
            for r in rows[:lead]:
                for ln in r:
                    out.append({**b, "lines": [ln], "bbox": tuple(ln["bbox"])})
            if not rest:
                continue
        else:
            rest = [l for r in rows for l in r]
        bx = [l["bbox"] for l in rest]
        out.append({**b, "lines": rest,
                    "bbox": (min(x[0] for x in bx), min(x[1] for x in bx),
                             max(x[2] for x in bx), max(x[3] for x in bx))})
    return out


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
        raw["blocks"] = _split_head_from_title(_prepare_text_blocks(raw["blocks"]), ph)
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
                # A GAP UNDER HALF THE TYPE SIZE IS A SCRIPT OR A GLYPH, NOT A LINE. The `₀` of
                # `G₀` sits 2.6pt under its line (BIO11L ch10 p129, exercise 4) and a Wingdings
                # bullet 3pt off its text (p121); taken as the pitch, the render packed the lines
                # 2.6pt apart and exercises 3 and 4 printed on top of each other.
                _sz = sorted(s.get("size", 0) for l in b["lines"] for s in l["spans"]
                             if (s.get("text") or "").strip())
                _floor = max(1.0, 0.5 * _sz[len(_sz) // 2]) if _sz else 1.0
                gaps = [g for g in gaps if g > _floor]
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
        elements = _join_caption_lines(elements)

        # Vector artwork, where the page draws rather than places its figure.
        # Only RUNNING TEXT can disqualify a cluster. A diagram's own labels (`Head`, `Collar`,
        # `Cell wall`) sit inside its box, and counting them as text covered by the drawing
        # rejected the dividing-bacterium figure (BIO11L ch02 p014) for being "on top of" its
        # own labels. The threshold is the label length `_absorb_figure_labels` uses.
        _text_boxes = [e["bbox_pt"] for e in elements if len((e.get("text") or "").strip()) > 42]
        _img = merge_image_blocks(fragments, pw, ph)
        _vec = vector_figures(page, _text_boxes, pw, ph)
        # Drop a vector cluster that an image block already covers -- the same figure found
        # twice is worse than found once.
        def _overlaps_any(b, others):
            for (o, _n) in others:
                if not (b[2] < o[0] or o[2] < b[0] or b[3] < o[1] or o[3] < b[1]):
                    return True
            return False
        # A DRAWING TOUCHING AN IMAGE FIGURE IS PART OF IT. Figure 3.2 (BIO11L ch03 p028) is a
        # scanned image for the mosses and vector paths for the Marchantia thalli above them;
        # the vector half was dropped as "already covered", so the thalli printed as bare
        # labels. It now grows the image figure instead of being discarded.
        # But a panel of a GRID must not swallow its neighbours: on p031 Figure 3.3's vector
        # (b) Equisetum touches the scanned (d), and their union overlapped (a) and (c), which
        # would print parts of them twice. Such a drawing is kept as a panel of its own -- it
        # is a real drawing beside real figures, so no caption needs to vouch for it.
        grown_img, panels = [], []
        for k, (ib, inn) in enumerate(_img):
            ib = list(ib)
            others = [o for j, (o, _n) in enumerate(_img) if j != k]
            for vb, vn in list(_vec):
                if not _overlaps(vb, ib, 9.0):
                    continue
                union = [min(ib[0], vb[0]), min(ib[1], vb[1]),
                         max(ib[2], vb[2]), max(ib[3], vb[3])]
                _vec.remove((vb, vn))
                if any(_overlaps(union, o) for o in others):
                    panels.append((vb, vn))
                else:
                    ib, inn = union, inn + vn
            grown_img.append((tuple(ib), inn))
        _img = grown_img + panels
        # A BOX INSIDE ANOTHER IS THE SAME FIGURE FOUND TWICE. Figure 8.3(b)'s animal cell
        # (BIO11L ch08 p008) is one vector drawing with two small placed images inside it; the
        # drawing became a panel and the two images stayed figures of their own, so every label
        # round the cell was refused (absorbing it would overlap a "figure") and printed as a
        # paragraph -- `Nucleus`, `reticulum`, `Cytoplasm` as running text.
        _img = [(b, n) for k, (b, n) in enumerate(_img)
                if not any(j != k and o[0] - 2 <= b[0] and o[1] - 2 <= b[1]
                           and b[2] <= o[2] + 2 and b[3] <= o[3] + 2
                           and (o[2] - o[0]) * (o[3] - o[1]) > (b[2] - b[0]) * (b[3] - b[1])
                           for j, (o, _n) in enumerate(_img))]

        # ONE CAPTION, ONE FIGURE -- WHICH MAY BE SEVERAL DRAWINGS IN A ROW. Figure 2.1 prints
        # cocci, bacilli, spirilla and vibrio side by side, and Figure 2.6 its (a) and (b), each a
        # separate cluster. A GRID is rows stacked: Figure 3.2 prints (a)(b) above (c)(d). A
        # cluster sharing most of its height with another, or just above or below it across no
        # running text, is the same figure.
        def _same_figure(u, c):
            same_row = (min(u[3], c[3]) - max(u[1], c[1])
                        >= 0.3 * min(u[3] - u[1], c[3] - c[1]))
            if same_row:
                return True
            gap_top, gap_bot = (u[3], c[1]) if c[1] >= u[3] else (c[3], u[1])
            if gap_bot - gap_top > 45.0 or min(u[2], c[2]) <= max(u[0], c[0]):
                return False
            return not any(gap_top - 1 <= (t[1] + t[3]) / 2 <= gap_bot + 1
                           for t in _text_boxes)

        # A DRAWING BESIDE AN IMAGE FIGURE IS ANOTHER PANEL OF IT. Figure 8.1 (BIO11L ch08
        # p005) places the tracheid and the mesophyll as images and DRAWS the blood cells,
        # epithelium and nerve cell; Figure 8.10 places (a) and draws (b). The image panels
        # "accounted for" the one caption, so every drawn panel was discarded and its labels
        # printed as paragraphs. The image vouches for the figure the way a caption does: a
        # drawing in its row or grid, with no running text between them, is the same figure.
        # Panels are chained, so a row above the drawing joins through it.
        def _clear_between(u, c):
            gx0, gx1 = min(u[2], c[2]), max(u[0], c[0])
            gy0, gy1 = min(u[3], c[3]), max(u[1], c[1])
            lo_x, hi_x = min(gx0, gx1), max(gx0, gx1)
            lo_y, hi_y = min(gy0, gy1), max(gy0, gy1)
            return not any(lo_x <= (t[0] + t[2]) / 2 <= hi_x and lo_y <= (t[1] + t[3]) / 2 <= hi_y
                           for t in _text_boxes)
        _vec = [(b, n) for b, n in _vec if not _overlaps_any(b, _img)]
        if _img and _vec:
            groups = [[list(b), n] for b, n in _img]
            adopted = True
            while adopted:
                adopted = False
                for vb, vn in list(_vec):
                    hit = [g for g in groups
                           if _same_figure(vb, g[0]) and _clear_between(vb, g[0])]
                    if not hit:
                        continue
                    _vec.remove((vb, vn))
                    g = hit[0]
                    g[0] = [min(g[0][0], vb[0]), min(g[0][1], vb[1]),
                            max(g[0][2], vb[2]), max(g[0][3], vb[3])]
                    g[1] += vn
                    # the grown figure now takes in whatever image panels it reaches
                    for o in [o for o in groups if o is not g and _overlaps(g[0], o[0])]:
                        g[0] = [min(g[0][0], o[0][0]), min(g[0][1], o[0][1]),
                                max(g[0][2], o[0][2]), max(g[0][3], o[0][3])]
                        g[1] += o[1]
                        groups.remove(o)
                    adopted = True
            _img = [(tuple(b), n) for b, n in groups]
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
            # Keeping only the nearest cluster kept one panel of a row (Figure 2.1) and one row
            # of a grid (Figure 3.2's Marchantia thalli came out as bare labels), so the chosen
            # cluster grows by `_same_figure`.
            pool, picked = sorted(_vec, key=lambda bn: _dist_to_cap(bn[0])), []
            while pool and len(picked) < _unclaimed:
                (bx0, by0, bx1, by1), bn = pool.pop(0)
                grown = True
                while grown:
                    grown = False
                    for c in list(pool):
                        if _same_figure((bx0, by0, bx1, by1), c[0]):
                            pool.remove(c)
                            bx0, by0 = min(bx0, c[0][0]), min(by0, c[0][1])
                            bx1, by1 = max(bx1, c[0][2]), max(by1, c[0][3])
                            bn += c[1]
                            grown = True
                picked.append(((bx0, by0, bx1, by1), bn))
            _vec = picked
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
        # TABLES BEFORE FIGURE LABELS. Table 4.1's seven rows (BIO12L ch04 p005) sit 14pt left of
        # Figure 4.2 and were absorbed as its labels, so the table grew from its caption into
        # nothing and the rows left the chapter. A table claims its rows first.
        elements = _mark_tables(elements, pw, ph)
        elements = _absorb_figure_labels(elements, pw, ph, body_size=body_size)
        _absorb_drawn_marks(page, elements, pw, ph)

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
            # A PAGE OF ANOTHER SIZE IS ITS OWN SHEET. The page record carries the page's own
            # size as `sheet_pt` (below), so an offset onto the 612 x 784 Class 11 sheet only
            # SHIFTS the page: BIO12L's 568.8 x 777.6 pages set every element 21.6pt right and
            # 3.2pt down, and art bleeding off the edge came out at x +0.038 instead of -0.038.
            if abs(pw - sheet_w) > 2.0 or abs(ph - sheet_h) > 2.0:
                dx, dy, note = 0.0, 0.0, f"own sheet ({pw:.1f}x{ph:.1f}pt)"
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
            # KEEP THE MEASURED LINES, for the text join to split on.
            #
            # PyMuPDF can return several printed paragraphs as ONE block. Measured on BIO11L ch02
            # p012, the Viroids, Prions and Lichens paragraphs arrive as a single 1,277-character
            # element; A2 correctly reads them as three. With only the block's box, the join had
            # nowhere to put the second and third paragraph and dropped them -- 2 paragraphs
            # gone from a finished chapter. Each line's box is measured, so a split on them is
            # measured too, never an estimate.
            if e.get("_lines"):
                e["line_boxes_pt"] = [{"bbox_pt": [round(v, 1) for v in lbox], "text": ltext}
                                      for lbox, ltext in e["_lines"]]
            e.pop("_lines", None)
            e.pop("_spans", None)
        # reading order: side column first, then body, top to bottom
        order = {"side": 0, "full": 1, "body": 1}
        elements.sort(key=lambda e: (order.get(e["column"], 1), e["bbox"][1]))

        imprint = next((e["text"] for e in elements if e["role"] == "reprint_line"), None)
        # THE PAGE'S OWN DECORATION, measured: panels, bands, boxes, tints and borders, in the
        # order the PDF paints them, and the paint order of its placed pictures (see
        # `page_decor`). A page too dense to walk path by path keeps the design's furniture.
        heavy = _content_bytes(page) > _HEAVY_PAGE_BYTES
        decor = None if heavy else page_decor(
            page, [e["bbox_pt"] for e in elements if e["role"] == "figure"],
            [e["bbox_pt"] for e in elements if e["role"] in ("figure", "table")
             and e.get("bbox_pt")])
        if not heavy:
            _stamp_image_z(page, elements)
        pages.append({
            "page_file": "%03d" % (pi + 1),
            "page_width_pt": round(pw, 1), "page_height_pt": round(ph, 1),
            "sheet_pt": [round(sheet_w, 1), round(sheet_h, 1)],
            "_measured_offset": (dx, dy) if note.startswith("uncropped")
            or note == "canonical" or note.startswith("own sheet") else None,
            "sheet_note": note,
            "_decor_pt": decor,
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
    for d in visible_drawings(page):
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


def _absorb_figure_labels(elements, page_w, page_h, pad=14.0, body_size=None):
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
                # Short is judged per PRINTED LINE: the text layer fuses neighbouring labels into
                # one block -- Figure 8.2 (BIO11L ch08 p006) gives `A typical eukaryotic cell
                # Viruses (0.02-0.2µm)`, two labels, 44 characters -- and that block was kept as
                # prose. A prose line runs 60+ characters; a stack of a few short lines does not
                # (Figure 8.1's `Mesophyll cells / (round and oval) / A tracheid / (elongated)` is
                # four), and the total cap keeps a narrow marginal note out.
                # (The layer also cuts a line at every odd glyph -- `(0.02-0.2`, `\x1f`, `m)` --
                # so rows are counted by vertical position, not by line objects.)
                lines = [(b, t) for b, t in e.get("_lines") or [] if t]
                rows = []
                for b, _t in sorted(lines, key=lambda bt: bt[0][1] + bt[0][3]):
                    mid = (b[1] + b[3]) / 2
                    if not rows or mid - rows[-1] > 4.0:
                        rows.append(mid)
                if not txt or (len(txt) > 42 and not (
                        lines and len(rows) <= 4 and len(txt) <= 90
                        and all(len(t) <= 42 for _b, t in lines))):
                    continue
                # ...and short is ALSO judged by WIDTH. A justified line in a narrow column holds
                # few characters: BIO11L ch10 p004's bullet `Spindle fibres attach to kinetochores
                # of / chromosomes.` is two lines of <= 42 characters set 273pt wide beside Figure
                # 10.2, and it was swallowed into the figure and lost from the chapter. A label
                # is never set across a column; no line of one runs past 180pt.
                if any(b[2] - b[0] > 180.0 for b, _t in lines):
                    continue
                # ...and by TYPE. Diagram labels are set below the body size (9.5, 9.3, 9.0,
                # 7.7pt measured on BIO11L ch08); the last words of a paragraph are not. BIO11L
                # ch08 p014 opens its right column with `the aleuroplasts store proteins.` --
                # the end of a sentence from the page before, 10.5pt body type, 32 characters --
                # and it was swallowed into Figure 8.8. Body-size text that ends a sentence is
                # prose.
                body_type = (body_size and e.get("runs")
                             and all(abs((r.get("size") or 0) - body_size) <= 0.15
                                     for r in e["runs"] if (r.get("t") or "").strip()))
                if body_type and re.search(r"[.?!]$", txt):
                    continue
                # ...and body type that CONTINUES A PARAGRAPH'S MEASURE is prose, sentence end
                # or not. BIO12L ch02 p012 sets `Immediately after / implantation, the inner cell
                # / mass (embryo) differentiates` -- a new paragraph, 10.5pt, in the narrow
                # column beside Figure 2.12, 3.4pt under the paragraph before on its left edge --
                # and it was swallowed as a label and lost (it runs on to the next page).
                if body_type and len(rows) >= 2 and any(
                        o is not e and o["role"] in ("paragraph", "list")
                        and abs(o["bbox_pt"][0] - e["bbox_pt"][0]) <= 1.5
                        and 0 <= e["bbox_pt"][1] - o["bbox_pt"][3] <= 20.0
                        for o in elements):
                    continue
                if not _overlaps(e["bbox_pt"], fb, pad):
                    continue
                # A label may not drag its figure over a NEIGHBOURING figure. On BIO11L ch03
                # p031 the text layer runs `(d) (c)` -- two panels' labels -- into one block, and
                # absorbing it stretched panel (d) across (a) and (c): one crop printing parts of
                # three. Such a label stays text rather than merge two figures.
                grown = [min(fb[0], e["bbox_pt"][0]), min(fb[1], e["bbox_pt"][1]),
                         max(fb[2], e["bbox_pt"][2]), max(fb[3], e["bbox_pt"][3])]
                if any(o is not fig and _overlaps(grown, o["bbox_pt"]) for o in figs):
                    continue
                fb[0] = min(fb[0], e["bbox_pt"][0]); fb[1] = min(fb[1], e["bbox_pt"][1])
                fb[2] = max(fb[2], e["bbox_pt"][2]); fb[3] = max(fb[3], e["bbox_pt"][3])
                fig["bbox_pt"] = fb
                fig["absorbed_labels"] = fig.get("absorbed_labels", []) + [txt]
                absorbed.add(i)
                changed = True
    kept = [e for i, e in enumerate(elements) if i not in absorbed]
    _trim_figures_from_text(figs, kept)
    return kept


# The crop pad `cut_figures.PAD_PT`. A figure box must clear real text by at least this much,
# or the crop -- a render of the page region -- carries that text as pixels.
_CROP_PAD = 4.0


def _trim_figures_from_text(figs, elements):
    """Pull each figure's box back off any REAL text it reaches into.

    A figure crop is a render of a page region, so whatever text sits inside it is baked into
    the picture -- and that same text is drawn again as live text. Measured on BIO11L ch02: the
    clusters of Figures 2.1 and 2.6 reached down to their own captions and Figure 2.1's up into
    the last line of the paragraph above, so `Figure 2.6 (a) Tobacco Mosaic Virus` and
    `(Figure 2.1).` printed twice, a pixel copy half-covered by the live one.

    Labels have already been absorbed, so anything still overlapping is a caption or prose. The
    box gives way on the side the text is on, by the crop pad as well, so the crop stops short
    of it. A trim that would collapse the figure is not made -- a crop with a stray line is
    better than no artwork.
    """
    skip = ("figure", "page_furniture", "page_number", "running_header", "reprint_line")
    for fig in figs:
        for e in elements:
            if e is fig or e["role"] in skip or not (e.get("text") or "").strip():
                continue
            fb, tb = fig["bbox_pt"], e["bbox_pt"]
            if not _overlaps(tb, fb, _CROP_PAD):
                continue
            # The side to give way on: the one that loses the least artwork.
            cut = {"top": tb[3] + _CROP_PAD + 0.5 - fb[1],
                   "bottom": fb[3] - (tb[1] - _CROP_PAD - 0.5),
                   "left": tb[2] + _CROP_PAD + 0.5 - fb[0],
                   "right": fb[2] - (tb[0] - _CROP_PAD - 0.5)}
            side = min(cut, key=cut.get)
            nb = list(fb)
            if side == "top":
                nb[1] = tb[3] + _CROP_PAD + 0.5
            elif side == "bottom":
                nb[3] = tb[1] - _CROP_PAD - 0.5
            elif side == "left":
                nb[0] = tb[2] + _CROP_PAD + 0.5
            else:
                nb[2] = tb[0] - _CROP_PAD - 0.5
            if nb[2] - nb[0] >= 0.5 * (fb[2] - fb[0]) and nb[3] - nb[1] >= 0.5 * (fb[3] - fb[1]):
                fig["bbox_pt"] = nb


# CASE-SENSITIVE, deliberately. NCERT sets the caption in caps -- `TABLE 1.1 Organisms with
# their Taxonomic Categories` -- while the prose that refers to it is title case: `Table 1.1
# indicates the taxonomic categories to which some common organisms belong.` A case-insensitive
# match swallowed that sentence and every paragraph after it into a "table", cropping a block
# of running prose as an image.
# Class 12 sets its captions in title case WITH A COLON -- `Table 4.1: Contrasting Traits Studied
# by Mendel in Pea` (BIO12L ch04) -- which prose never does, so that form is a caption too.
_TABLE_RE = re.compile(r"^\s*(?:TABLE\s*\d+\.\d+|Table\s*\d+\.\d+\s*:)")


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
        consumed.add(start)
        # A CAPTION'S SECOND LINE IS CAPTION, NOT ROW ONE. Table 11.1 (BIO11L ch11 p148) prints
        # `Fill in the Columns 2 and 3 ... differences` / `between C3 and C4 Plants`, the second
        # line in the caption's bold face, its `3` and `4` as lone subscript pieces. All five
        # pieces became a two-row "grid", the real rows (read by A2S) a second, captionless
        # table, and the caption lost its end. Pieces directly under the caption, inside its
        # width and in its face (or digits set small), join it.
        cb = cap["bbox_pt"]
        lh = max(cb[3] - cb[1], 1.0) if "\n" not in (cap.get("text") or "") else 14.0
        face = next((r.get("font") for r in cap.get("runs") or [] if (r.get("t") or "").strip()), None)
        cont = [j for j in order[pos[start] + 1:]
                if j not in consumed and elements[j].get("role") not in ("figure", "page_furniture")
                and cb[3] - 2.0 <= elements[j]["bbox_pt"][1] <= cb[3] + 0.8 * lh
                and elements[j]["bbox_pt"][0] >= cb[0] - 4.0 and elements[j]["bbox_pt"][2] <= cb[2] + 4.0
                and (all(r.get("font") == face for r in elements[j].get("runs") or []
                         if (r.get("t") or "").strip())
                     or re.fullmatch(r"\s*\d\s*", elements[j].get("text") or ""))]
        # ...as ONE LINE OF WORDS: its pieces sit a word gap apart. A header row is also bold
        # and directly under the caption, but its cells stand a column apart -- Table 2.1's
        # `Characters  Monera  Protista ...` (BIO11L ch02 p011) was swallowed into the caption
        # and its cells printed loose.
        xs = sorted((elements[j]["bbox_pt"] for j in cont), key=lambda b: b[0])
        tight = all(b[0] - a[2] <= 1.5 * lh for a, b in zip(xs, xs[1:]))
        if cont and face and tight and any(not re.fullmatch(r"\s*\d\s*", elements[j].get("text") or "")
                                           for j in cont):
            runs = list(cap.get("runs") or [])
            if runs and not (runs[-1].get("t") or "").endswith(" "):
                runs[-1] = {**runs[-1], "t": runs[-1]["t"] + " "}
            for j in sorted(cont, key=lambda j: elements[j]["bbox_pt"][0]):
                e = elements[j]
                if re.fullmatch(r"\s*\d\s*", e.get("text") or ""):
                    if runs:
                        runs[-1] = {**runs[-1], "t": runs[-1]["t"].rstrip()}
                    runs.append({**((e.get("runs") or [{}])[0]), "t": e["text"].strip() + " ",
                                 "script": "sub"})
                else:
                    if runs and not runs[-1]["t"].endswith(" "):
                        runs[-1] = {**runs[-1], "t": runs[-1]["t"] + " "}
                    runs.extend(dict(r) for r in e.get("runs") or [])
                consumed.add(j)
                eb = e["bbox_pt"]
                cb = [min(cb[0], eb[0]), min(cb[1], eb[1]), max(cb[2], eb[2]), max(cb[3], eb[3])]
            cap["runs"] = runs
            cap["text"] = re.sub(r"\s+", " ", "".join(r["t"] for r in runs)).strip()
            cap["bbox_pt"] = cb
        box = list(cap["bbox_pt"])
        members, parts = [], [cap.get("text", "")]
        for k in range(pos[start] + 1, len(order)):
            j = order[k]
            e = elements[j]
            if j in consumed:
                continue
            eb = e["bbox_pt"]
            # FURNITURE IS NOT A STOP, NOR A FOLIO BESIDE THE TABLE. The watermark spans the page
            # and sorts in among the rows (Table 4.3, BIO12L ch04 p016, cut after row 2), and the
            # Class 12 folio sits in the margin two-thirds down (Table 4.2, p011, `61` beside
            # row 2): each ended the table, leaving its last rows loose over the grid.
            if e["role"] == "page_furniture" or (
                    e["role"] in ("page_number", "running_header")
                    and (eb[0] >= box[2] or eb[2] <= box[0])):
                continue
            if e["role"] in ("section_heading", "page_furniture", "page_number",
                             "running_header", "reprint_line", "figure"):
                break
            if eb[1] - box[3] > 26.0:
                break
            # THE TABLE'S OWN COLUMN BAND, ENFORCED. Once a row has set the table's width, a
            # block reaching well past it is the page's running text, not a row: on BIO11L ch04
            # p046 the right-column paragraph `Phylum Chordata is divided into three subphyla:
            # Urochordata or Tunicata ...` starts 14pt under Table 4.1 and runs 25pt past its
            # right edge -- inside the gap test, so it was swallowed into the table and the
            # sentence vanished from the chapter. It is skipped, not a stop: rows may continue.
            # ...but a ROW starts at the table's own left edge, however far it reaches: Table
            # 4.1's row 2 (`Central nervous system is dorsal, hollow and single.`) is the widest
            # row and was skipped by the width test alone, then printed loose over the grid.
            starts_at_table = abs(eb[0] - box[0]) <= 12.0
            if members and not starts_at_table and (eb[0] < box[0] - 12.0
                                                    or eb[2] > box[2] + 12.0):
                continue
            # THE OTHER COLUMN'S PROSE IS NOT THE FIRST ROW. The band test above waits for a
            # first row, so on a two-column page the next block down -- BIO11L ch09 p105's left
            # column `In higher classes you will learn about how to analyse ...`, wholly left of
            # `TABLE 9.1` in the right column -- became row one; the table then spanned the page
            # and a 31x9 grid of prose and cells replaced it. A long block lying entirely beside
            # the caption's own span is the next column's text. A short cell is never refused.
            cb = cap["bbox_pt"]
            if (len((e.get("text") or "").strip()) > 80
                    and (eb[2] < cb[0] - 8.0 or eb[0] > cb[2] + 8.0)):
                continue
            # A BLOCK SET LARGER THAN EVERY ROW IS THE RUNNING TEXT AGAIN. Table 4.3 (BIO12L ch04
            # p016) sets its rows at 9.5pt and the paragraph under it, `During Anaphase of meiosis
            # I ...`, at 10.5pt, starting at the table's left edge 10pt below the last row -- so
            # it was taken as a row, and the figure under it with it. Judged only inside the table's own
            # column: Table 9.4 (BIO11L ch09 p006) has the left column's prose sorted among its rows.
            # Each block by the size most of its characters are set in: one larger glyph (the
            # minus of `PO4 3-`, BIO11L ch09 Table 9.2) is not running text.
            def main_size(el):
                c = collections.Counter()
                for r in el.get("runs") or []:
                    c[r.get("size") or 0] += len((r.get("t") or "").strip())
                return c.most_common(1)[0][0] if c else 0
            # ...and running text is LONG: Table 9.2's last row `PO4 3-, SO4 2-` is itself set
            # at 10.5pt among 9.5pt rows, 13 characters.
            row_sz = max((main_size(m) for m in members), default=0)
            if members and row_sz and main_size(e) >= row_sz + 0.5 \
                    and len((e.get("text") or "").strip()) > 60:
                break
            # A FOOTNOTE ENDS THE TABLE: `* Adapted from CNR Rao, ...` under Table 9.1 (BIO11L
            # ch09 p002) is the table's source note, not a row.
            if members and re.match(r"^\s*[*†]\s*\w", e.get("text") or ""):
                break
            box[0] = min(box[0], eb[0]); box[1] = min(box[1], eb[1])
            box[2] = max(box[2], eb[2]); box[3] = max(box[3], eb[3])
            members.append(e)
            parts.append(e.get("text", ""))
            consumed.add(j)
        # NO ROWS UNDER IT: the grid was read elsewhere (an A2S table under the caption), so
        # the caption stays a caption and joins that table, rather than becoming an empty one.
        if not members:
            cap["role"] = "figure_caption"
            continue
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
    return [e for i, e in enumerate(elements) if i not in consumed
            or (i in idx and e.get("role") in ("table", "figure_caption"))]


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
        decor = p.pop("_decor_pt", None)
        if decor is not None:
            p["decor"] = [dict({k: v for k, v in d.items() if k != "bbox_pt"},
                               bbox=[round((d["bbox_pt"][0] + dx) / sw, 4),
                                     round((d["bbox_pt"][1] + dy) / sh, 4),
                                     round((d["bbox_pt"][2] + dx) / sw, 4),
                                     round((d["bbox_pt"][3] + dy) / sh, 4)])
                          for d in decor]
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
