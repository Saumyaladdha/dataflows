#!/usr/bin/env python3
"""Fail a built chapter that carries any defect we have already shipped once.

    python code/check_chapter.py BIO11L-ch01
    python code/check_chapter.py --all
    python code/check_chapter.py --all --strict      # non-zero exit on any FAIL

Run automatically at the end of `run_chapter.py`. Every check below exists because the defect
it names reached a finished-looking file and was found by a person reading it. A person is the
most expensive possible check and the slowest; each of these is a second.

This is the DETERMINISTIC half of the review gate. It catches what can be stated as a rule.
The other half is the agents -- `a2v-extraction-verifier` (data vs the page images) and
`a2r-render-reviewer` (render vs the page images) -- which catch what cannot: a cropped
diagram, a heading at the wrong level, a mark on the wrong word. Both halves are required
before a chapter is loaded.
"""

import argparse
import collections
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

try:
    import pymupdf
except ImportError:
    pymupdf = None


def _walk(nodes):
    for n in nodes:
        yield n
        if n.get("children"):
            yield from _walk(n["children"])


def _norm_words(s):
    return set(re.findall(r"[a-z]{4,}", (s or "").lower()))


def check(doc, chapter_dir):
    """[(level, code, message)] -- FAIL is a defect, WARN is a thing to look at."""
    out = []
    # Unit pages are part of the SOURCE FILE even though they belong to the book rather than
    # this chapter, so coverage is measured against both trees -- otherwise the check reports
    # a 13% hole that is really "those pages are stored elsewhere".
    nodes = list(_walk(doc["tree"]))
    pages = doc.get("pages") or []

    def fail(code, msg):
        out.append(("FAIL", code, msg))

    def warn(code, msg):
        out.append(("WARN", code, msg))

    # 1 ── EVERY NODE MUST KNOW ITS PAGE ------------------------------------------------
    # Section headings were built inline and never given a page key; on a chapter whose pages
    # print no folio that left 12 of them unbucketed and the renderer put all 23 pages onto
    # ONE sheet, every section overlapping the next.
    orphans = [n for n in nodes if not n.get("pages") and not n.get("page_file")]
    if orphans:
        kinds = collections.Counter(n["kind"] for n in orphans)
        fail("ORPHAN_NODES",
             f"{len(orphans)} node(s) have no page key {dict(kinds)} -- they will all render "
             f"on one sheet")

    # 2 ── THE TREE MUST COVER THE SOURCE ------------------------------------------------
    # 15% of Class 11 ch01's words were missing: the unit opener, the Mayr box, and every cell
    # of Table 1.1, which was stored only as a grid and never put into `body`.
    src_pdf = src = doc.get("source_pdf")
    if pymupdf and src and os.path.exists(os.path.join(ROOT, src)):
        pdf = pymupdf.open(os.path.join(ROOT, src))
        pdf_words = set()
        for p in pdf:
            pdf_words |= _norm_words(p.get_text())
        pdf.close()
        mine = set()
        for n in nodes:
            mine |= _norm_words(n.get("body") or n.get("title") or n.get("caption") or "")
            for it in n.get("items") or []:
                mine |= _norm_words(it.get("body"))
            g = n.get("table_grid")
            if g:
                mine |= _norm_words(" ".join(c for r in g["cells"] for c in r))
        if pdf_words:
            cover = len(pdf_words & mine) / len(pdf_words)
            missing = sorted(pdf_words - mine)
            if cover < 0.90:
                fail("TEXT_COVERAGE",
                     f"only {cover:.0%} of the source's words appear in the tree; "
                     f"{len(missing)} missing e.g. {missing[:8]}")
            elif cover < 0.97:
                warn("TEXT_COVERAGE",
                     f"{cover:.0%} coverage; {len(missing)} words missing e.g. {missing[:6]}")

    # 3 ── NOTHING MAY APPEAR TWICE ------------------------------------------------------
    bodies = [(n.get("body") or "")[:120] for n in nodes
              if n["kind"] in ("para", "question") and len(n.get("body") or "") > 60]
    dupes = [b for b, c in collections.Counter(bodies).items() if c > 1]
    if dupes:
        fail("DUPLICATE_CONTENT",
             f"{len(dupes)} block(s) appear more than once e.g. {dupes[0][:70]!r}")

    # 4 ── FIGURES MUST BE REAL ----------------------------------------------------------
    # Clustering drawing paths once reported ELEVEN figures on a chapter that prints one.
    figs = [n for n in nodes if n["kind"] == "figure"]
    named = [n for n in figs if n.get("number")]
    n_pages = max(1, len(pages))
    if len(figs) > 4 * n_pages:
        fail("FIGURE_OVERDETECT",
             f"{len(figs)} figure nodes across {n_pages} pages -- more than 4 a page is "
             f"scan fragments, not artwork")
    noimg = [n for n in figs if not (n.get("image") or n.get("image_local") or any(
        q.get("image") or q.get("image_local") for q in n.get("panels") or []))]
    if noimg:
        warn("FIGURE_NO_IMAGE",
             f"{len(noimg)} of {len(figs)} figures have no cropped image "
             f"(vector artwork needs A2L's measured box)")
    if figs and not named:
        warn("FIGURE_UNNAMED", f"none of {len(figs)} figures carries a Figure N.M number")

    # 5 ── EXERCISES MUST BE WHOLE -------------------------------------------------------
    flagged = [n for n in nodes if n.get("needs_agent_split")]
    for n in flagged:
        warn("NEEDS_AGENT_SPLIT",
             f"a block could not be split into questions safely (found "
             f"{n.get('split_attempt')}) -- re-run A2 so it returns one block per question")
    qs = [n for n in nodes if n["kind"] == "question"]
    if qs:
        nums = [int(q["number"]) for q in qs if str(q.get("number", "")).isdigit()]
        if nums and sorted(nums) != list(range(1, len(nums) + 1)):
            fail("QUESTION_GAPS", f"exercise numbers are not 1..N: {sorted(nums)}")

    # 6 ── PROVENANCE MUST BE HONEST -----------------------------------------------------
    tj = doc.get("text_join") or {}
    if tj and tj.get("pages_with_agent", 0) < tj.get("pages", 0):
        warn("UNREAD_PAGES",
             f"{tj['pages'] - tj['pages_with_agent']} of {tj['pages']} pages were never read "
             f"by a2-page-reader: {tj.get('pages_missing')}")
    lj = doc.get("layout_join") or {}
    if lj and lj.get("pages_with_agent", 0) == 0:
        warn("NO_LAYOUT_AGENT",
             "a2l-layout-reader has not run on this chapter -- every column, fill, alignment "
             "and heading size is a heuristic")
    layer = [n for n in nodes if n.get("source") == "text_layer"]
    if layer:
        warn("TEXT_LAYER_NODES",
             f"{len(layer)} of {len(nodes)} nodes still carry PDF text-layer text "
             f"(good prose, unreliable notation)")

    # 7 ── A SCAN WITH NO TEXT LAYER IS A DIFFERENT PIPELINE -----------------------------
    # EIGHT files in this corpus are pure A4 scans: 595.32 x 841.92pt, zero extractable
    # characters, thousands of image fragments. Class 12 Biology ch01 is one. Everything
    # downstream of the text layer -- boxes, marks, folios, running heads, figure captions,
    # the chapter title, table grids -- has NO SOURCE on such a page. The pipeline built it
    # anyway and reported success: 23 pages, 26 figures, 137 nodes, not one measured box and
    # not one mark. On a scan, a2l-layout-reader is not an improvement, it is the ONLY
    # geometry there is, so building without it is not allowed.
    scanned = [p for p in pages if p.get("has_text_layer") is False]
    if scanned:
        lj2 = doc.get("layout_join") or {}
        if lj2.get("pages_with_agent", 0) < len(scanned):
            fail("SCAN_WITHOUT_LAYOUT_AGENT",
                 f"{len(scanned)} of {len(pages)} pages have NO text layer and only "
                 f"{lj2.get('pages_with_agent', 0)} have an a2l-layout-reader read -- on a "
                 f"scan A2L is the only source of geometry, so every box, size and column "
                 f"here is invented")

    # 8 ── NO BOX MAY PRETEND TO BE A MEASUREMENT ----------------------------------------
    boxes = [b for n in nodes for b in (n.get("boxes") or [])]
    if boxes:
        unlabelled = [b for b in boxes if not b.get("src")]
        if unlabelled:
            fail("BOX_NO_PROVENANCE",
                 f"{len(unlabelled)} of {len(boxes)} boxes do not say where their geometry "
                 f"came from -- a guess that cannot be told from a measurement is trusted")
        est = [b for b in boxes if b.get("src") == "estimated"]
        if est and len(est) > 0.25 * len(boxes):
            fail("ESTIMATED_GEOMETRY",
                 f"{len(est)} of {len(boxes)} boxes are INVENTED reading-order guesses "
                 f"(0.10-0.90 wide, evenly subdivided) -- they describe no printed layout")
        # 127 boxes sharing one x-range is the signature of the placeholder above.
        xr = collections.Counter((round(b["bbox"][0], 2), round(b["bbox"][2], 2))
                                 for b in boxes)
        top, n_top = xr.most_common(1)[0]
        if len(boxes) >= 12 and n_top > 0.6 * len(boxes):
            fail("PLACEHOLDER_BOXES",
                 f"{n_top} of {len(boxes)} boxes share the single x-range {top} -- a real "
                 f"page has columns, indents and text wrapped around figures")
        oob = [b for b in boxes
               if not all(0.0 <= v <= 1.0 for v in b["bbox"])]
        if oob:
            fail("BOX_OUT_OF_PAGE",
                 f"{len(oob)} box(es) fall outside the page e.g. {oob[0]['bbox']} -- a "
                 f"normalised coordinate above 1.0 cannot be rendered")

    # 9 ── THE SHEET MUST BE THE BOOK'S SHEET --------------------------------------------
    # The A4 scans are a different SHAPE, not a crop: 0.707 aspect against 0.781. Forcing the
    # canonical 612x784 trim on them makes every sheet wider and shorter than the book, and
    # then no coordinate can line up however good the stylesheet is.
    for p in pages[:1]:
        sp, asp = p.get("sheet_pt"), p.get("sheet_aspect")
        if sp and asp and abs(asp - 612.0 / 784.0) > 0.02:
            warn("SHEET_NOT_CANONICAL",
                 f"this book's page is {sp[0]}x{sp[1]}pt (aspect {asp}), not the canonical "
                 f"612x784 (0.781) -- the design must be measured for it, not inherited")

    # 10 ── ONE CROP MAY NOT BE FIVE DIFFERENT FIGURES -----------------------------------
    used = collections.Counter(n.get("image_local") for n in nodes
                               if n["kind"] == "figure" and n.get("image_local"))
    reused = {k: v for k, v in used.items() if v > 1}
    if reused:
        k, v = next(iter(reused.items()))
        fail("IMAGE_REUSED",
             f"{len(reused)} crop(s) are attached to more than one figure e.g. {k} on {v} "
             f"figures -- those pages print different illustrations")
    if figs and not any((n.get("caption") or "").strip() for n in figs):
        fail("FIGURE_NO_CAPTION",
             f"not one of {len(figs)} figures has a caption -- the captions are in the tree "
             f"as ordinary paragraphs, which also corrupts the prose around them")

    # 11 ── ONE SHEET PER PAGE OF THE SOURCE ---------------------------------------------
    # The page-faithful render is the deliverable (chapter.html retired 2026-10-24).
    html = os.path.join(chapter_dir, "chapter-exact.html")
    if os.path.exists(html) and pages:
        with open(html, encoding="utf-8") as fh:
            h = fh.read()
        sheets = len(re.findall(r'class="sheet', h))
        if sheets != len(pages):
            fail("SHEET_COUNT",
                 f"the render has {sheets} sheets for a {len(pages)}-page source -- a missing "
                 f"sheet renumbers every folio after it")

    # The per-page fit is measured from chapter.json by the reflow renderer, IN MEMORY: its
    # chapter.html is no longer written (retired 2026-10-24), but what it measures -- how much
    # a page's content needs against the room the page gives -- is still the warning that a
    # block was assigned to the wrong page, and that warning protects the exact render too.
    try:
        import render_from_tree
        h_fit = render_from_tree.render(doc)
    except Exception:                                     # noqa: BLE001
        h_fit = ""
    if h_fit:
        openers = len(re.findall(r'class="sheet opener', h_fit))
        if openers > 1:
            fail("ALL_OPENERS",
                 f"{openers} of {len(pages)} sheets use the chapter-OPENER design -- only the "
                 f"chapter's first page opens a chapter")

    # 12 ── NO PAGE MAY OVERFLOW ITS SHEET -----------------------------------------------
    # The sheet is a fixed height with `overflow:hidden`, so content that does not fit is not
    # pushed onto the next page -- it DISAPPEARS, mid-sentence, under the footer bar. That is
    # invisible to every other check here, and it is what a reader notices first.
    if h_fit:
        tight = [(m.group(1), float(m.group(2)))
                 for m in re.finditer(r'id="p([^"]+)"[^>]*--fit:([0-9.]+)', h_fit)]
        bad = [(p_, f) for p_, f in tight if f < 0.72]
        if bad:
            fail("PAGE_OVERFLOW",
                 f"{len(bad)} page(s) hold more content than the sheet can show even shrunk "
                 f"to 72% e.g. page {bad[0][0]} needs {bad[0][1]:.0%} -- content is being "
                 f"clipped, which means it was assigned to the wrong page")
        shrunk = [(p_, f) for p_, f in tight if f < 0.88]
        if shrunk:
            warn("PAGE_TIGHT",
                 f"{len(shrunk)} page(s) are set below 88% to fit e.g. page {shrunk[0][0]} "
                 f"at {shrunk[0][1]:.0%}")

    # 13 ── THE CHECKS AN EXTERNAL REVIEWER RAN BY HAND ----------------------------------
    # Every one of these was a defect a person found by reading the render against the PDF.
    # Each is cheap to state as a rule, so none of them should ever need a person again.

    # (a) every referenced image must actually be on disk
    if os.path.exists(html):
        missing = sorted({src for src in re.findall(r'<img[^>]+src="([^"]+)"', h)
                          if not src.startswith("http")
                          and not os.path.exists(os.path.join(chapter_dir, src))})
        if missing:
            fail("MISSING_IMAGE",
                 f"{len(missing)} referenced image(s) are not in the chapter folder e.g. "
                 f"{missing[0]} -- the page cannot display its artwork")

    # (b) a caption must not be welded onto the prose that follows it
    for n in nodes:
        b = (n.get("body") or "")
        if n["kind"] in ("para", "box") and re.match(r"^\s*(?:Figure|Fig\.|Table)\s*\d", b):
            m = re.match(r"^\s*(?:Figure|Fig\.|Table)\s*[\d.]+\s*(.{0,400})", b, re.S)
            # A paragraph may open by MENTIONING a figure: `Figure 1.2a shows the two parts of a
            # typical stamen ...` (BIO12L ch01 p005) is the book's own sentence, not a caption.
            mentions = re.match(r"^[a-z]?\s*(?:shows|depicts|indicates|illustrates|gives|"
                                r"represents|is|are)\b", m.group(1) if m else "")
            if m and len(m.group(1)) > 160 and not mentions:
                fail("CAPTION_IN_PROSE",
                     f"a caption and the paragraph after it are one node: "
                     f"{b[:90]!r}... -- this changes what the text says, not just how it looks")
                break

    # (c) every exercise must carry a visible number
    unnumbered = [n for n in nodes if n["kind"] == "question" and not str(
        n.get("number") or "").strip()]
    if unnumbered:
        fail("QUESTION_NO_NUMBER",
             f"{len(unnumbered)} exercise(s) have no number -- a question bank cannot cite "
             f"an anonymous question")

    # (d) THE PAGE BOUNDARY CHECK -- the manual review, automated.
    # A reviewer read each PDF page and each rendered sheet and compared where they start and
    # end: "page 3 should end '...the number and'; page 4 should begin 'types of organisms'".
    # That comparison is mechanical, so it runs here on every build.
    if pymupdf and src_pdf and os.path.exists(os.path.join(ROOT, src_pdf)) \
            and os.path.exists(html):
        pdf = pymupdf.open(os.path.join(ROOT, src_pdf))
        sheets = re.findall(
            r'<section class="sheet[^"]*" id="p([^"]+)".*?(?=<section class="sheet|</body>)',
            h, re.S)
        bad_edges = []
        for i, pg in enumerate(pdf):
            words = [w for w in _norm_words(pg.get_text())]
            if len(words) < 30 or i >= len(sheets):
                continue
            body = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", sheets[i])).strip()
            mine = re.findall(r"[a-z]{4,}", body.lower())
            ptail = re.findall(r"[a-z]{4,}", pg.get_text().lower())
            if not mine or not ptail:
                continue
            # the last real word of the PDF page should appear near the end of the sheet
            if ptail[-1] not in mine[-14:]:
                bad_edges.append((i + 1, ptail[-1], mine[-1] if mine else ""))
        pdf.close()
        if len(bad_edges) > max(1, 0.25 * len(sheets)):
            fail("PAGE_BOUNDARY",
                 f"{len(bad_edges)} sheet(s) do not end where their PDF page ends e.g. page "
                 f"{bad_edges[0][0]} should end near {bad_edges[0][1]!r} but ends "
                 f"{bad_edges[0][2]!r} -- content is on the wrong page")
        elif bad_edges:
            warn("PAGE_BOUNDARY",
                 f"{len(bad_edges)} sheet(s) may not end where their PDF page ends e.g. page "
                 f"{bad_edges[0][0]} ({bad_edges[0][1]!r} vs {bad_edges[0][2]!r})")

    # (e) comparable pages must be set at comparable sizes
    if os.path.exists(html):
        fits = sorted({float(x) for x in re.findall(r'--fit:([0-9.]+)', h)})
        if len(fits) > 1 and (fits[-1] - fits[0]) > 0.20:
            warn("FIT_INCONSISTENT",
                 f"body size varies from {fits[0]:.0%} to {fits[-1]:.0%} across pages -- "
                 f"a reader sees the type change between facing pages")

    # 14 ── THE CHAPTER MUST IDENTIFY ITSELF ---------------------------------------------
    if not (doc["chapter"].get("title") or "").strip():
        fail("NO_TITLE", "the chapter has no title -- its folder will be named ch<NN>_chapter")
    if not doc.get("reprint"):
        warn("NO_REPRINT", "no imprint line was read and none could be inferred")

    # 15 ── FURNITURE MUST NOT BE CONTENT ------------------------------------------------
    for n in nodes:
        b = (n.get("body") or "").strip()
        if re.fullmatch(r"(?:\d{1,3}\s+)?(Biology|BIOLOGY)|\d{4}-\d{2}|Reprint \d{4}-\d{2}", b):
            fail("FURNITURE_AS_CONTENT",
                 f"{b!r} is page furniture and must not be a content node")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapters", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()

    paths = sorted(glob.glob(os.path.join(ROOT, "data", "*_ncert", "class_*", "*", "*",
                                          "chapter.json")))
    worst = 0
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            doc = json.load(fh)
        cid = f"{doc['book_id']}-ch{doc['chapter']['number']:02d}"
        if a.chapters and cid not in a.chapters:
            continue
        res = check(doc, os.path.dirname(p))
        fails = [r for r in res if r[0] == "FAIL"]
        warns = [r for r in res if r[0] == "WARN"]
        status = "FAIL" if fails else ("warn" if warns else "ok")
        print(f"{cid:<16} {status:<5} {len(fails)} fail, {len(warns)} warn")
        for lvl, code, msg in res:
            print(f"    {lvl:<4} {code:<22} {msg}")
        worst = max(worst, 2 if fails else (1 if warns else 0))
    if a.strict and worst >= 2:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
