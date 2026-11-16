#!/usr/bin/env python3
"""Insert the NCERT mapping card -- quote, paragraph, and the real page with the line marked --
into an exported paper's `question_paper.html`.

EVERY CLASS THIS FILE EMITS IS PREFIXED `ncm-`, AND THAT IS NOT TIDINESS
------------------------------------------------------------------------
The first version styled its quotes with `class="q"` and its gaps with `class="gap"`. The
paper's OWN stylesheet already defines both, and `.q` is the question card itself:

    .q { background:var(--card); border:1px solid var(--rule); border-radius:7px;
         padding:16px 18px; margin:0 0 16px }

So all 544 inline quote spans were painted as full question cards -- a dark filled box in dark
mode, overflowing its table cell, with the text barely legible. The data underneath was right
the whole time; only the class name was wrong. A card injected into someone else's document
shares their global namespace, so it must never use a bare word as a class name.

ONE QUOTE IS ONE BLOCK, BECAUSE MATCH-THE-COLUMN EXISTS
-------------------------------------------------------
A match question cites one line per pairing: q156 carries three latest lines and four older
ones. Run together as inline spans they are unreadable. Each line now gets its own bordered
block headed by the PART OF THE ANSWER it settles ("List I-D matches List II-II"), so a reader
sees at a glance which pairings the book covers and which it does not -- which is exactly what
`supports_answer: partly` means and was previously invisible.

AND THE PARAGRAPH AROUND THE QUOTE
----------------------------------
A quoted sentence with nothing around it cannot be checked: a reader cannot see whether the
next sentence qualifies it. Each block therefore carries the full NCERT paragraph it was cut
from, collapsed, with the quoted line marked inside it. The same text is written into
`questions.json` by `join_ncert_map_into_export.py`, so the JSON and the page agree.

WHAT IS AND IS NOT CLAIMED BY THE EMBEDDED PAGE
-----------------------------------------------
The geometry is the book's -- `exact_css` positions every printed line absolutely. The GLYPHS
ARE NOT: `exact_css` names its fonts by content hash and the bytes were never stored (a
table-wide scan for `FONT#` returns zero, and no font file exists under the NCERT source), so
those @font-face rules are dropped and the fallback stack renders. Every embedded page says so.

Usage:
    python3 code/join_ncert_card_into_html.py --paper 2024_S1
    python3 code/join_ncert_card_into_html.py --paper 2024_S1 --apply
"""

import argparse
import collections
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPS = os.path.join(os.path.dirname(HERE), "ncert_to_paper_maps")
sys.path.insert(0, os.path.join(MAPS, "code"))

import render_ncert_quote as rq            # noqa: E402  -- highlight() and usable_css()

CARD_CSS = """
.ncm{margin:10px 0 0;border:1px solid #c9d6cf;border-radius:4px;background:#f6faf8;color:#1f2937}
.ncm>h4{margin:0;padding:6px 10px;font:700 11px/1.4 -apple-system,Segoe UI,Roboto,sans-serif;
 letter-spacing:.06em;text-transform:uppercase;color:#1f4f3a;background:#e8f0ea;
 border-bottom:1px solid #c9d6cf}
.ncm table{width:100%;border-collapse:collapse;font:13px/1.5 Georgia,serif;background:none}
.ncm th{width:140px;text-align:left;vertical-align:top;padding:7px 10px;color:#3a4a43;
 font-weight:400;background:#f0f5f2;border-bottom:1px solid #e3ebe6;border-radius:0}
.ncm td{padding:7px 10px;border-bottom:1px solid #e3ebe6;color:#1f2937;background:none;
 border-radius:0}
.ncm-ev{margin:0 0 8px;padding:6px 10px;border-left:3px solid #7aa88f;background:#fff;
 border-radius:0 3px 3px 0}
.ncm-ev:last-child{margin-bottom:0}
.ncm-ev.ncm-old{border-left-color:#b08968;background:#fffdfa}
.ncm-for{display:block;font:600 11px/1.4 -apple-system,Segoe UI,Roboto,sans-serif;color:#1f4f3a;
 margin:0 0 3px}
.ncm-old .ncm-for{color:#7a4f28}
/* THE QUOTE AND THE PARAGRAPH ARE SET IN THE BOOK'S OWN TYPE, not in a guess at it. Every
   value below is copied from the chapter's `exact_css`, which was measured off the PDF:

       body { font-family: NcertBody,"TeX Gyre Bonum",Bookman,Georgia,serif; color:#231f20 }
       .grp { text-align:justify }          body size 10.5pt, leading 1.27

   `NcertBody` will not resolve -- its bytes were never stored -- but the rest of that stack is
   the real fallback chain the book itself declares, so the page and this paragraph degrade the
   same way instead of diverging. The ink colour #231f20 is the book's, not black. */
.ncm-line{margin:0;font-style:italic;font-size:10.5pt;line-height:1.27;color:#231f20;
 font-family:NcertBody,"TeX Gyre Bonum",Bookman,Georgia,serif}
.ncm-src{display:block;margin-top:4px;font:10px/1.4 ui-monospace,Menlo,monospace;color:#6b7a73}
.ncm-para{margin:6px 0 0;padding:9px 11px;background:#fff;border:1px solid #e3ebe6;
 border-radius:2px;font-family:NcertBody,"TeX Gyre Bonum",Bookman,Georgia,serif;
 font-size:10.5pt;line-height:1.27;color:#231f20;text-align:justify}
.ncm-para mark{background:#fff3a3;padding:0;color:inherit}
.ncm-warn{color:#8a5a00}
.ncm-sy{display:inline-block;padding:2px 8px;border-radius:3px;font:700 11px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.04em;text-transform:uppercase}
.ncm-sy-in{background:#d8efdf;color:#13543a}
.ncm-sy-out{background:#f6d6d2;color:#8a2318}
.ncm-sy-check{background:#fdecc8;color:#7a5200}
.ncm-sy-none{background:#e6e8ea;color:#4b5563}
.ncm-basis{display:block;margin-top:4px;font:12px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;color:#4b5563}
.ncm details.ncm-page{margin:0;border-top:1px solid #c9d6cf}
.ncm details.ncm-page>summary{padding:6px 10px;cursor:pointer;
 font:12px -apple-system,sans-serif;color:#1f4f3a}
.ncm-pagewrap{overflow-x:auto;background:#8d8d8d;padding:10px}
.ncm mark.ncq{background:#fff3a3;color:inherit;padding:0;box-shadow:0 0 0 1px #e8cf4d}
"""


def chapter_class(chapter_id):
    """A CSS-safe class per chapter, so one stylesheet can serve every card using it."""
    return "ncm-ch-" + re.sub(r"[^A-Za-z0-9]+", "-", chapter_id).strip("-").lower()


def chapter_styles(pages, chapters):
    """One <style> block carrying every used chapter's sheet, each scoped to its own class.

    Emitted once per DOCUMENT, not once per page. The first version put a <style> beside every
    embedded page, and a question whose evidence spans ten printed pages carried ten copies of
    the same 8 KB: 97% of the inserted bytes were stylesheet.
    """
    out = []
    for chid in sorted(chapters):
        css, _dropped = rq.usable_css((pages.get("_css") or {}).get(chid, ""))
        if not css:
            continue
        cls = "." + chapter_class(chid)

        def scope(sel):
            """Prefix one selector with the chapter's class.

            `body` IS THE WRAPPER, NOT SOMETHING INSIDE IT. The chapter sheets were written for
            a standalone page, so they set the book's type on `body`: font-family NcertBody,
            ink colour #231f20, the grey surround. Prefixing that blindly gives
            `.ncm-ch-bio11l-ch09 body`, which can never match -- a <body> does not live inside
            a <div>. Twenty-eight such rules were silently dead on every card, so the embedded
            page kept the exported paper's own font and rendered pale and wrong: the sheet was
            white (that rule is a class, so it survived) but the type on it was not the book's.
            Mapping body/html/:root onto the wrapper itself is what makes the page read as the
            printed page.
            """
            s = sel.strip()
            return cls if s.lower() in ("body", "html", ":root") else "%s %s" % (cls, s)

        scoped = re.sub(r"(^|})\s*([^@}{]+)\{",
                        lambda m: "%s %s{" % (m.group(1),
                                              ",".join(scope(p) for p in m.group(2).split(","))),
                        css)
        out.append(scoped)
    return ("<style>%s</style>" % "".join(out)) if out else ""


#: How much of the book to show around a quoted line, in characters either side.
#: Sentence-snapped, so the real window is a little wider than this.
CONTEXT_CHARS = 300


def shared_window(paragraph, lines):
    """One window covering every quote that came from the same passage, each one marked.

    A match-the-column question cites one line per pairing and they often sit in the SAME
    NCERT paragraph: q200's four blanks all come from `BIO12L-CH02-P22`. Rendering a window per
    quote printed that paragraph four times with only the highlight moving, and then four more
    times for the older edition. One window with four marks says the same thing once, and it
    also shows something the repeats hid -- that the four facts are consecutive sentences of a
    single passage, which is why the question works.

    Returns (html, True) or (None, False) if no quote could be located.
    """
    spans = []
    for line in lines:
        at = paragraph.find(line)
        if at != -1:
            spans.append((at, at + len(line)))
    if not spans:
        return None, False
    spans.sort()

    # QUOTES THAT ARE FAR APART GET THEIR OWN WINDOW. Merging the whole range between the first
    # and last quote works when they are neighbouring sentences, and fails badly when they are
    # not: two quotes 4,000 characters apart in one of BIO12L-CH05's blobs produced a 4,991-
    # character "window", the same wall of text the window was introduced to prevent. Quotes
    # are clustered first, and a gap wider than twice the context budget starts a new cluster.
    clusters = [[spans[0]]]
    for a, b in spans[1:]:
        if a - clusters[-1][-1][1] > 2 * CONTEXT_CHARS:
            clusters.append([(a, b)])
        else:
            clusters[-1].append((a, b))

    parts = []
    for cl in clusters:
        lo = max(0, cl[0][0] - CONTEXT_CHARS)
        hi = min(len(paragraph), cl[-1][1] + CONTEXT_CHARS)
        if lo > 0:
            dot = paragraph.rfind(". ", lo, cl[0][0])
            lo = dot + 2 if dot != -1 else lo
        if hi < len(paragraph):
            dot = paragraph.find(". ", cl[-1][1], hi)
            hi = dot + 1 if dot != -1 else hi
        chunk, cur = [], lo
        for a, b in cl:
            if a < cur:        # overlapping quotes -- keep the first mark, skip the nested one
                continue
            chunk.append(html.escape(paragraph[cur:a]))
            chunk.append("<mark>%s</mark>" % html.escape(paragraph[a:b]))
            cur = b
        chunk.append(html.escape(paragraph[cur:hi]))
        parts.append(("&hellip; " if lo > 0 else "") + "".join(chunk)
                     + (" &hellip;" if hi < len(paragraph) else ""))
    return "".join('<p class="ncm-para">%s</p>' % p for p in parts), True


def context_window(paragraph, line):
    """A few lines of the book either side of the quote -- never the whole passage.

    The first version printed the entire stored passage. For most chapters that is a real
    paragraph, but not for all: BIO12L-CH05 is stored as 16 passages for the whole of Molecular
    Basis of Inheritance, four of them 7,000-15,000 characters with sentences from different
    printed pages run together. One quote there dumped most of a chapter into the card, and a
    question citing three lines from that passage printed the same wall three times.

    So the card shows a WINDOW: about 300 characters each way, snapped outward to sentence
    boundaries so it never starts or ends mid-clause, with an ellipsis where it was cut. The
    passage id is right above it for anyone who wants the rest.

    Returns (before, quote, after, cut_left, cut_right) or None if the quote is not in the text.
    """
    at = paragraph.find(line)
    if at == -1:
        return None
    lo, hi = max(0, at - CONTEXT_CHARS), min(len(paragraph), at + len(line) + CONTEXT_CHARS)
    # snap outward to a sentence start / end so the window reads as prose
    if lo > 0:
        dot = paragraph.rfind(". ", lo, at)
        lo = dot + 2 if dot != -1 else lo
    if hi < len(paragraph):
        dot = paragraph.find(". ", at + len(line), hi)
        hi = dot + 1 if dot != -1 else hi
    return (paragraph[lo:at], line, paragraph[at + len(line):hi], lo > 0, hi < len(paragraph))


def row(label, value):
    return '<tr><th>%s</th><td>%s</td></tr>' % (label, value) if value else ""


def evidence_html(items, edition, paragraphs):
    """One block per quoted line: what it settles, the line, its source, the paragraph around it."""
    # GROUPED BY PASSAGE, IN THE ORDER THE QUOTES WERE GIVEN. Several findings commonly share
    # one NCERT paragraph, and the book's context only has to be shown once for all of them.
    groups, order = {}, []
    for e in items or []:
        if not e.get("exact_line"):
            continue
        pid = e.get("passage_id")
        if pid not in groups:
            groups[pid] = []
            order.append(pid)
        groups[pid].append(e)

    out = []
    for pid in order:
        g = groups[pid]
        quotes = []
        for e in g:
            quotes.append('%s<p class="ncm-line">&ldquo;%s&rdquo;</p>'
                          % (('<span class="ncm-for">%s</span>' % html.escape(str(e["for"])))
                             if e.get("for") else "", html.escape(e["exact_line"])))
        # THE CONTEXT IS SHOWN, NOT HIDDEN BEHIND A DISCLOSURE: it is what lets a reader see
        # whether the next sentence qualifies the quote, and nobody opens fifty disclosures.
        para = (paragraphs or {}).get(pid) or ""
        para_html = ""
        if para:
            para_html, _ok = shared_window(para, [e["exact_line"] for e in g])
            para_html = para_html or ""
        out.append('<div class="ncm-ev%s">%s<span class="ncm-src">%s</span>%s</div>'
                   % (" ncm-old" if edition == "older" else "",
                      "".join(quotes), html.escape(str(pid or "")), para_html))
    return "".join(out)


#: How each syllabus label reads on the page, and the colour it carries.
SYLLABUS_FACE = {
    "in_syllabus":     ("In syllabus", "ncm-sy-in"),
    "out_of_syllabus": ("OUT OF SYLLABUS", "ncm-sy-out"),
    "needs_review":    ("Needs review", "ncm-sy-check"),
    "not_verified":    ("Not verified", "ncm-sy-none"),
}


def syllabus_row(syl):
    """The syllabus verdict, as a row of the QUESTION's own classify table -- not the NCERT card.

    It was inside the NCERT mapping card at first, and that was a category error the owner
    caught: whether a question is on the NEET syllabus is a fact about the QUESTION and the
    NMC's list, not about where its answer sits in a textbook. NCERT and the syllabus genuinely
    disagree -- p-Block is Unit 10 of the NEET syllabus and was dropped from the rationalised
    NCERT -- so filing the verdict under "NCERT mapping" would have implied a relation that
    does not hold. It now sits with `subject` / `chapter` / `subtopic`, where the question's
    other classifications are, and chemistry and physics questions carry it whether or not
    they have any NCERT mapping at all.

    `not_verified` is printed as loudly as `in_syllabus`: a blank would be read as "fine".
    """
    if not syl:
        return ""
    face, cls = SYLLABUS_FACE.get(syl.get("label"), ("Not verified", "ncm-sy-none"))
    against = str(syl.get("against") or "")
    return ('<tr><th>syllabus</th><td><span class="ncm-sy %s">%s</span>'
            '<span class="ncm-basis">%s</span>%s</td></tr>'
            % (cls, html.escape(face), html.escape(str(syl.get("basis") or "")),
               ('<span class="ncm-src">judged against: %s</span>' % html.escape(against))
               if against else ""))


def build_card(qid, mapping, pages, passages, used_chapters, paragraphs):
    tbl = []
    ch = mapping.get("chapter") or {}
    if ch.get("ncert_chapter_ids"):
        conf = ('<span class="ncm-src" style="display:inline;margin-left:6px">%s confidence</span>'
                % html.escape(ch["confidence"])) if ch.get("confidence") else ""
        tbl.append(row("NCERT chapter",
                       "; ".join(html.escape(c) for c in ch["ncert_chapter_ids"]) + conf))

    subs = mapping.get("ncert_subtopics") or []
    if subs:
        tbl.append(row("ncert_subtopic", "; ".join(
            html.escape("%s %s" % (s.get("printed_number") or "", s.get("name") or s.get("id")))
            for s in subs)))

    latest = mapping.get("latest") or {}
    if latest.get("lines"):
        tbl.append(row("latest NCERT", evidence_html(latest["lines"], "latest", paragraphs)))
    if latest.get("supports_answer"):
        extra = ""
        if latest.get("missing"):
            extra = ('<div class="ncm-warn">not covered by the book: %s</div>'
                     % html.escape("; ".join(str(x) for x in latest["missing"])))
        tbl.append(row("supports the answer", "%s &middot; %s%s"
                       % (html.escape(latest["supports_answer"]),
                          html.escape(str(latest.get("link_type") or "")), extra)))

    older = mapping.get("older") or {}
    if older.get("lines"):
        tbl.append(row("older NCERT", evidence_html(older["lines"], "older", paragraphs)))
    if older.get("none_for"):
        tbl.append(row("older edition had no line for",
                       '<span class="ncm-warn">%s</span>'
                       % html.escape("; ".join(str(x) for x in older["none_for"]))))

    ca = mapping.get("concept_approach") or {}
    if ca.get("concept"):
        tbl.append(row("concept", html.escape(ca["concept"])))
    if ca.get("approach"):
        tbl.append(row("approach", html.escape(ca["approach"])))
    if not tbl:
        return None, 0

    # the real page, with the quote marked
    marked = 0
    by_page = collections.defaultdict(list)
    for e in (latest.get("lines") or []):
        info = passages.get(e.get("passage_id"))
        if info and e.get("exact_line"):
            for pg in info["pages"]:
                by_page[(info["chapter_id"], pg)].append(e["exact_line"])
    chunks = []
    for (chid, pg), quotes in sorted(by_page.items()):
        raw = (pages.get(chid) or {}).get(pg)
        if not raw:
            continue
        out, hits, _ = rq.highlight(raw, quotes)
        marked += hits
        used_chapters.add(chid)
        fallback = ("" if not (pages.get("_css") or {}).get(chid, "").count("__FONT:")
                    else " &middot; glyphs are a fallback (the embedded fonts were never stored)")
        chunks.append('<p class="ncm-src">%s &middot; printed page %s &middot; %d line(s) marked'
                      '%s</p><div class="ncm-pagewrap %s">%s</div>'
                      % (html.escape(chid), html.escape(pg), hits, fallback,
                         chapter_class(chid), out))
    page_html = ('<details class="ncm-page">'
                 '<summary>the NCERT page itself, with the line marked</summary>%s</details>'
                 % "".join(chunks)) if chunks else ""

    return ('<div class="ncm" id="ncm-%s"><h4>NCERT mapping</h4><table>%s</table>%s</div>'
            % (qid, "".join(tbl), page_html)), marked


def strip_previous(src):
    """Remove an earlier run's NCERT cards so a fresh mapping can be re-inserted.

    WHY BALANCED MATCHING AND NOT A REGEX TO `</div>`. A card contains the rendered NCERT page,
    which is itself hundreds of nested divs -- one per printed line. A lazy `.*?</div>` would stop
    at the first inner line and leave the rest of the page behind as orphaned markup. So each
    card's end is found by counting `<div` against `</div>` from its own opening tag.

    Three things are removed, because the insert step adds three things: the cards, the two
    stylesheets (the card sheet and the per-chapter sheets, both recognisable by the `.ncm`
    class prefix they define), and the `syllabus` row spliced into each classify table.
    """
    out, removed = src, {"cards": 0, "stylesheets": 0, "syllabus rows": 0}
    while True:
        m = re.search(r'<div class="ncm" id="ncm-[^"]*">', out)
        if not m:
            break
        i, depth = m.start(), 0
        end = -1
        for t in re.finditer(r'<div\b|</div>', out[m.start():]):
            depth += -1 if t.group(0) == '</div>' else 1
            if depth == 0:
                end = m.start() + t.end()
                break
        if end < 0:                      # unbalanced: leave it rather than cut blindly
            break
        out = out[:m.start()] + out[end:]
        removed["cards"] += 1
    for sm in reversed(list(re.finditer(r'<style>(.*?)</style>', out, re.S))):
        if '.ncm' in sm.group(1):
            out = out[:sm.start()] + out[sm.end():]
            removed["stylesheets"] += 1
    out, n = re.subn(r'<tr[^>]*><th>syllabus</th>.*?</tr>', '', out, flags=re.S)
    removed["syllabus rows"] = n
    return out, removed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--replace", action="store_true",
                    help="strip an earlier run's cards first, then re-insert")
    a = ap.parse_args()

    year = a.paper.split("_")[0]
    base = os.path.join(HERE, "data", year, a.paper)
    doc = json.load(open(os.path.join(base, "questions.json"), encoding="utf-8"))
    pages = json.load(open(os.path.join(MAPS, "maps", "page_html.json"), encoding="utf-8"))
    passages = json.load(open(os.path.join(MAPS, "maps", "passage_pages.json"), encoding="utf-8"))
    paragraphs = json.load(open(os.path.join(MAPS, "maps", "paragraphs.json"), encoding="utf-8"))
    src = open(os.path.join(base, "question_paper.html"), encoding="utf-8").read()

    if 'class="ncm"' in src:
        if not a.replace:
            print("this paper already carries NCERT cards -- re-run with --replace")
            return
        src, gone = strip_previous(src)
        print("   stripped previous: %s" % ", ".join("%d %s" % (v, k) for k, v in gone.items()))

    report = collections.Counter()
    used_chapters = set()

    # WHERE EVERY QUESTION CARD ENDS, FOUND ONCE. The first version spliced each card into the
    # document with `out = out[:cut] + card + out[cut:]`, which rebuilds the whole 8 MB string
    # 148 times -- the run did not finish inside two minutes. The cut points are all known from
    # one scan, so the document is assembled in a single pass instead.
    starts = [(m.group(1), m.start()) for m in
              re.finditer(r'<div class="q" id="(q\d+)"', src)]
    ends = {}
    for i, (qid, at) in enumerate(starts):
        ends[qid] = starts[i + 1][1] if i + 1 < len(starts) else len(src)

    inserts = []
    for q in doc["questions"]:
        # A QUESTION WITH NO MAPPING STILL GETS A CARD, because it still gets a syllabus
        # label -- and `not_verified` is precisely the value that must not be invisible.
        m = q.get("ncert_mapping") or {}
        if not m and not q.get("syllabus"):
            report["no mapping"] += 1
            continue
        qid = q["question_id"].split("__")[-1]
        if qid not in ends:
            report["question div not found"] += 1
            continue
        card, marked = build_card(qid, m, pages, passages, used_chapters, paragraphs)
        if not card:
            report["mapping empty"] += 1
            continue
        inserts.append((ends[qid], card))
        report["card inserted"] += 1
        report["pages marked"] += 1 if marked else 0

    # THE SYLLABUS ROW GOES INTO THE QUESTION'S OWN CLASSIFY TABLE, under the subtopics.
    # Anchored on the LAST subtopic-ish row rather than on a fixed one, because the table is
    # not the same shape on every question: 24 of 200 print `why subtopic 1` / `why subtopic 2`
    # where the other 176 print a single `why this subtopic`, and `subtopic 2` itself is
    # sometimes the last row. Anchoring on one name would have dropped the row on the rest.
    SUB_ROW = re.compile(r'<tr[^>]*><th>(?:subtopic \d|why this subtopic|why subtopic \d)'
                         r'</th>.*?</tr>', re.S)
    for q in doc["questions"]:
        syl = q.get("syllabus")
        qid = q["question_id"].split("__")[-1]
        if not syl or qid not in ends:
            continue
        start = next((a for i, (qq, a) in enumerate(starts) if qq == qid), None)
        if start is None:
            continue
        slice_ = src[start:ends[qid]]
        last = None
        for m in SUB_ROW.finditer(slice_):
            last = m
        if last is None:
            report["no subtopic row to anchor on"] += 1
            continue
        inserts.append((start + last.end(), syllabus_row(syl)))
        report["syllabus row inserted"] += 1

    chunks, last = [], 0
    for at, card in sorted(inserts):
        chunks.append(src[last:at])
        chunks.append(card)
        last = at
    chunks.append(src[last:])
    out = "".join(chunks)

    out = out.replace("</style>", "</style><style>%s</style>%s"
                      % (CARD_CSS, chapter_styles(pages, used_chapters)), 1)
    print("%s" % a.paper)
    for k, v in sorted(report.items()):
        print("   %-26s %3d" % (k, v))
    print("   html grows %.1f MB -> %.1f MB" % (len(src) / 1e6, len(out) / 1e6))
    if not a.apply:
        print("(nothing written -- pass --apply)")
        return
    open(os.path.join(base, "question_paper.html"), "w", encoding="utf-8").write(out)
    print("wrote question_paper.html")


if __name__ == "__main__":
    main()
