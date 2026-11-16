#!/usr/bin/env python3
"""Build the Biology NCERT-first page by TRANSFORMING the existing cards, not replacing them.

WHY TRANSFORM AND NOT REBUILD
-----------------------------
The owner asked for a page "similar to question_paper.html" -- the printed crop, the publisher's
printed solution image, the difficulty block and, explicitly, the trap analysis: "i need traps
and all as well thats needed". All of that already renders correctly. Rebuilding it from the
JSON would mean re-deriving layout that is already right and risking a regression in the one
part nobody complained about. So each card is taken as it stands and edited.

WHY DIV CUTTING IS BALANCED AND NOT REGEX-TO-THE-NEXT-MARKER
------------------------------------------------------------
The first version found a block's end by searching forward for the next `<div class="sol |meta|
ecat|ncm`. On this paper that is wrong, and destructively so: `<div class="sol ai">` closes at
offset 4010 of the q101 card and the classify table -- difficulty, steps, confusing options,
why it is tricky, Type, Asks, Concept -- starts immediately after it as a SIBLING. The next
marker is `<div class="meta">` 1337 characters later, so the cut swallowed that whole table:
exactly the fields the owner said to keep. Every block end is now found by counting `<div`
against `</div>` from its own opening tag.

WHAT CHANGES
------------
    dropped   why this chapter · why this subtopic   -- the agent's reasoning, not a student's
              subtopic 1 · subtopic 2                -- exam-taxonomy picks, replaced by NCERT's
              Why this answer                        -- restates the stem
              Note                                   -- pipeline commentary, written for us
              the publisher's solution PROSE         -- one solution only, as asked
              the NCERT card's duplicate chapter/subtopic rows -- now shown at the top
              the older-edition quote WHEN IT IS WORD-FOR-WORD THE LATEST ONE

    changed   chapter   -> NCERT's own printed chapter title, read off the chapter opener page
              + ncert_subtopic row, from D2's printed headings
              the solution -> D12's, written in NCERT's vocabulary

    kept      the crop, the publisher's printed-solution IMAGE (scanned evidence, not a second
              solution), difficulty, steps, confusing options, why it is tricky, Type, Asks,
              Concept, every ECAT trap block, the NCERT evidence card with its highlighted page,
              the syllabus row and the answer verdict

THE EXAM TAXONOMY IS NOT DELETED, ONLY UNDISPLAYED. `classification.examtopicmapping_subtopics`
stays in `questions.json`; the owner intends to map it properly later. Showing both side by side
is what produced the review's most repeated classification complaint.

Usage:
    python3 code/make_biology_ncert_page.py --paper 2024_S1 --questions q101,q106,q107,q153,q157
    python3 code/make_biology_ncert_page.py --paper 2024_S1 --questions ... --apply
"""

import argparse
import collections
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render_solution_diagram as sd        # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPS = os.path.join(os.path.dirname(HERE), "ncert_to_paper_maps")

#: Rows the owner asked to remove, matched on the exact <th> label the page prints.
#
#  `latest NCERT` goes because the solution's "What NCERT says" block already carries that
#  quote, and the rendered page below it marks MORE lines than the row listed (4 vs 1 on q101,
#  10 vs 4 on q157) -- so removing the row loses nothing and stops the same quote appearing
#  twice on one card.
#
#  `what makes it harder` and `Concept` go because of a duplication found by printing every
#  field of q101 side by side: `confusing options`, `why it is tricky`, `what makes it harder`
#  and the ECAT "The catch" block were four statements of one sentence -- the student mistakes
#  lecithin for a glyceride because they forget the phosphate. The ECAT block says it best (it
#  names the option, the trap type and who falls for it), so it is the one kept. `Concept` had
#  a second problem: it read "phosphate-choline head", the exact term the teacher review called
#  out as "not in NCERT Biology, it is Chemistry level". It comes from the older ECAT pass, not
#  from D12, so the NCERT-vocabulary rule never reached it.
DROP_ROWS = ("why this chapter", "why this subtopic", "why subtopic 1", "why subtopic 2",
             "subtopic 1", "subtopic 2", "Why this answer", "Note",
             "NCERT chapter", "ncert_subtopic", "latest NCERT",
             "what makes it harder", "Concept")

ROMAN = {"9": "IX", "10": "X", "11": "XI", "12": "XII"}
SUBJECT = {"BIO": "Biology", "PHY": "Physics", "CHE": "Chemistry", "CHM": "Chemistry"}

#: The solution is the one block on the card a student actually reads, so it is set like
#: prose and not like a data row: a real measure, book-weight type, and enough contrast to
#: read on a screen. The earlier version used the table's 14px grey, which went pale and
#: washed-out against the card.
EXTRA_CSS = """
.sol.ncert{border-left:3px solid #5f9478;background:#fbfdfc;padding-bottom:4px}
.sol.ncert .solhead{color:#2f4c3e}
.ncert-ans{font:600 13px -apple-system,sans-serif;color:#2f4c3e}
.ncert-ans em{font-style:normal;opacity:.72}
.ncert-says{margin:0 0 15px;padding:13px 16px;background:#fdf8e6;border-left:3px solid #d9bf52;
 border-radius:0 3px 3px 0}
.ncert-says .lab{display:block;font:700 10px -apple-system,sans-serif;letter-spacing:.07em;
 text-transform:uppercase;color:#6d4a00;margin-bottom:6px}
.ncert-says q{font:italic 16px/1.65 Georgia,"Times New Roman",serif;color:#2a2418}
.ncert-says .src{display:block;margin-top:7px;font:10px ui-monospace,Menlo,monospace;
 color:#8a7a4a;letter-spacing:.03em}
.ncert-short{margin:0 0 14px;padding:12px 15px;background:#eef5f1;border-left:3px solid #5f9478;
 border-radius:0 3px 3px 0;font:16px/1.7 Georgia,"Times New Roman",serif;color:#1d2621;
 max-width:66ch}
.ncert-more{margin:4px 0 0}
.ncert-more>summary{cursor:pointer;font:600 13px -apple-system,sans-serif;color:#44705c;
 padding:7px 0}
.ncert-more[open]>summary{margin-bottom:10px}
.ncert-expl{margin:0 0 16px;max-width:66ch;font:17px/1.78 Georgia,"Times New Roman",serif;
 color:#1d2621}
.ncert-wrong{margin:0;padding:14px 0 0;list-style:none;border-top:1px solid #dfe8e3}
.ncert-wrong .lab{display:block;font:700 10px -apple-system,sans-serif;letter-spacing:.07em;
 text-transform:uppercase;color:#6b7a73;margin-bottom:8px}
.ncert-wrong li{display:flex;gap:10px;padding:5px 0;max-width:66ch;
 font:15px/1.65 Georgia,"Times New Roman",serif;color:#2b3a33}
.ncert-wrong .opt{flex:0 0 auto;min-width:22px;height:22px;margin-top:3px;border-radius:50%;
 background:#f0e2de;color:#8a2318;font:700 11px/22px -apple-system,sans-serif;text-align:center}
.ncert-review{margin:0 0 15px;padding:11px 14px;background:#fdf1ee;border-left:3px solid #b8492f;
 border-radius:0 3px 3px 0;font:14px/1.68 Georgia,"Times New Roman",serif;color:#5e241a;
 max-width:66ch}
.ncert-review b{display:block;font:700 10px/1 -apple-system,sans-serif;letter-spacing:.07em;
 text-transform:uppercase;margin-bottom:6px}
.ncert-figs{display:flex;flex-wrap:wrap;gap:12px;margin:14px 0 0}
.ncert-figs figure{margin:0;max-width:300px}
.ncert-figs img{max-width:100%;border:1px solid #d7e0da;border-radius:4px;background:#fff}
.ncert-figs figcaption{font:11px -apple-system,sans-serif;color:#6b7a73;margin-top:5px}
.ncert-same{font:13px -apple-system,sans-serif;color:#5a6b62}
.ncert-says.ncert-says-page{padding:0;background:#fffdf3;border-left:3px solid #d9bf52}
.ncert-says.ncert-says-page .lab{padding:10px 14px 0}
.ncert-says.ncert-says-page .src{padding:0 14px 10px}
.ncert-para-wrap{overflow-x:auto;margin:10px 0}
.ncert-para-zoom{overflow:hidden}
.ncert-para-pg{display:block;padding:2px 0 4px 14px;font:10px ui-monospace,Menlo,monospace;color:#9a8a5a;letter-spacing:.04em}
.ncert-para{position:relative;overflow:hidden;background:#fff;margin:0}
.ncert-para .sheet{box-shadow:none!important;margin:0!important}
.ncert-para-shift{position:absolute}
.mtc-closer{margin-top:9px}
.diffwhy{margin-top:5px;font-size:.93em;opacity:.86}
""" + sd.CSS


# ---------------------------------------------------------------- balanced cutting

def div_end(s, start):
    """Index just past the `</div>` that closes the `<div` beginning at `start`."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += -1 if m.group(0) == '</div>' else 1
        if depth == 0:
            return start + m.end()
    return -1


def cut_div(card, cls):
    """Remove `<div class="cls">...</div>` whole. Returns (card, inner_html, where_it_was)."""
    m = re.search(r'<div class="%s">' % re.escape(cls), card)
    if not m:
        return card, "", -1
    end = div_end(card, m.start())
    if end < 0:
        return card, "", -1
    return card[:m.start()] + card[end:], card[m.start():end], m.start()


# ---------------------------------------------------------------- row surgery

def drop_rows(card):
    n = 0
    for label in DROP_ROWS:
        card, k = re.subn(r'<tr[^>]*><th>%s</th>.*?</tr>' % re.escape(label), "", card, flags=re.S)
        n += k
    return card, n


def chapter_name(pages, ch_id):
    """NCERT's own printed chapter title, read off the chapter opener page.

    The heading index stores only "Chapter 9" as a title, and no map in this repo carries the
    books' chapter names. They are printed on the opener page as two `blk ct` blocks -- the
    number, then the name -- so the name is taken from there rather than invented or borrowed
    from the coaching taxonomy.
    """
    for pgno in sorted((pages.get(ch_id) or {}))[:3]:
        for m in re.finditer(r'<div class="blk ct"[^>]*>(.*?)</div>', pages[ch_id][pgno], re.S):
            t = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            if t and not re.fullmatch(r'(Chapter|Unit)\s*\d+', t, re.I):
                return t.title() if t.isupper() else t
    return ""


def chapter_label(pages, ch_ids):
    """Return (where, name) -- kept apart so the card can print them as DISTINCT rows.

    The first version crammed both into the one `chapter` cell, which read
    "Biomolecules · NCERT Class XI Biology, Chapter 9" -- the number and the book's name run
    together in a single line. The owner asked for them separated, so the pair is returned
    unjoined and `set_chapter` lays them out as their own rows.
    """
    wheres, names = [], []
    for cid in ch_ids:
        m = re.match(r'([A-Z]+)(\d+)([LO])-CH(\d+)', cid)
        name = chapter_name(pages, cid)
        if not m:
            names.append(name or cid)
            continue
        _, cls, _, num = m.groups()
        wheres.append("Class %s, Chapter %d" % (ROMAN.get(cls, cls), int(num)))
        if name:
            names.append(name)
    return " / ".join(wheres), " / ".join(names)


def set_chapter(card, where, name, subtopics):
    """Repoint `chapter` at NCERT and follow it with the book's own name and subtopic."""
    m = re.search(r'(<tr[^>]*><th>chapter</th><td[^>]*>)(.*?)(</td></tr>)', card, re.S)
    if not m:
        return card, False
    rows = ""
    if name:
        rows += '<tr><th>ncert chapter</th><td>%s</td></tr>' % html.escape(name)
    if subtopics:
        rows += ('<tr><th>ncert subtopic</th><td>%s</td></tr>'
                 % html.escape("; ".join(subtopics)))
    cell = html.escape(where) if where else "not mapped to NCERT"
    return card[:m.start()] + m.group(1) + cell + m.group(3) + rows + card[m.end():], True


def name_the_new_type(card, q):
    """When E1 proposed a NEW question type, print the name it proposed.

    The card read `New type (proposed)  new_type  "a printed shape none of the above
    describes"` -- which tells a reader nothing. The name was never missing from the data:
    q157 carries `qtype_proposed.name = "pair_options"` with a paragraph of reasoning. Only
    the renderer dropped it. One question in this paper's 200 is affected.
    """
    cats = q.get("categories") or {}
    if str(cats.get("qtype") or "") != "new_type":
        return card, False
    prop = cats.get("qtype_proposed") or {}
    nm = (prop.get("name") or "").strip()
    if not nm:
        return card, False
    cell = ('<span class="ecat-name" title="%s">%s</span>'
            '<span class="ecat-slug">proposed new type</span>'
            '<span class="ecat-gloss">%s</span>'
            % (html.escape(prop.get("why") or ""), html.escape(nm),
               html.escape((prop.get("why") or "").split(".")[0])))
    out, n = re.subn(r'(<tr[^>]*><th>Type</th><td[^>]*>).*?(</td></tr>)',
                     lambda m: m.group(1) + cell + m.group(2), card, count=1, flags=re.S)
    return out, bool(n)


#: The line a match-the-columns question ends on, which belongs BELOW the table.
_CLOSER = re.compile(r'(?i)^\s*(choose|select|identify|mark)\b.{0,80}?(correct|right)\b.{0,40}$')


def fix_mtc_order(card):
    """Put "Choose the correct answer..." after the table, where the booklet prints it.

    The extractor folds a question's whole stem into one string, so a match-the-columns item
    comes out as `Match List I with List II / Choose the correct answer from the options given
    below: / <table>` -- the instruction to choose printed BEFORE the thing being chosen
    between. The teacher review raised this on the match and statement questions: the paper
    reads lead-in, then the table, then the closing line, then the options.
    """
    # balanced, because this function's own output nests a <div> inside the stem -- a lazy
    # `.*?</div>` would cut at that inner tag on any second pass over the same card
    open_m = re.search(r'<div class="stem">', card)
    if not open_m:
        return card, False
    stop = div_end(card, open_m.start())
    if stop < 0:
        return card, False
    inner_start, inner_end = open_m.end(), stop - len('</div>')
    body = card[inner_start:inner_end]

    t = body.find('<table')
    if t < 0:
        return card, False
    end = body.find('</table>', t)
    if end < 0:
        return card, False
    end += len('</table>')

    parts = body[:t].split('<br>')
    if len(parts) < 2 or not _CLOSER.match(re.sub(r'<[^>]+>', '', parts[-1])):
        return card, False
    rebuilt = ('<br>'.join(parts[:-1]) + body[t:end]
               + '<div class="mtc-closer">' + parts[-1] + '</div>' + body[end:])
    return card[:inner_start] + rebuilt + card[inner_end:], True


def merge_tricky_into_difficulty(card):
    """Hang the difficulty REASON off the difficulty rating instead of a row of its own.

    `why it is tricky` is not a third account of the trap -- it is the justification for the
    rating, and it reads as one: "Medium rather than easy: ...". Standing alone, three rows
    below `difficulty`, it looked like more trap commentary. Attached to the rating it is the
    audit trail it was written to be.
    """
    m = re.search(r'<tr[^>]*><th>why it is tricky</th><td[^>]*>(.*?)</td></tr>', card, re.S)
    if not m:
        return card, False
    why = m.group(1)
    card = card[:m.start()] + card[m.end():]
    out, n = re.subn(r'(<tr[^>]*><th>difficulty</th><td[^>]*>)(.*?)(</td></tr>)',
                     lambda d: d.group(1) + d.group(2)
                     + '<div class="diffwhy">' + why + '</div>' + d.group(3),
                     card, count=1, flags=re.S)
    return out, bool(n)


def strip_repeats(card):
    """Drop two spans that repeat on every card without adding anything to this question.

    `ncm-src` is the syllabus provenance footnote -- the NMC notification date and the
    rationalisation note -- identical on all 200 cards, so it belongs in the document header,
    not under every question. `livewhy` is the prose half of `confusing options`; the count
    ("2 of 4 · options 3, 4") stays because that is this question's own data, while the prose
    was the third copy of what the ECAT catch block already explains.
    """
    n = 0
    card, k = re.subn(r'<span class="ncm-src">.*?</span>', "", card, flags=re.S)
    n += k
    card, k = re.subn(r'<div class="livewhy">.*?</div>', "", card, flags=re.S)
    return card, n + k


def collapse_older(card, mp):
    """When the older edition's line is word for word the latest one, say so in a sentence.

    Across the five trial questions D5 returned text identical to D4 every time, so the card was
    printing the same paragraph twice, each with its own rendered page. That is the duplication
    the owner objected to -- "we are not adding same data again and again".
    """
    latest = {(l.get("exact_line") or "").strip()
              for l in ((mp.get("latest") or {}).get("lines") or [])}
    older = {(l.get("exact_line") or "").strip()
             for l in ((mp.get("older") or {}).get("lines") or [])}
    if not latest or not older or latest != older:
        return card, False
    new = ('<tr><th>older NCERT</th><td><span class="ncert-same">The previous edition prints '
           'this in the same words &mdash; nothing changed between editions.</span></td></tr>')
    out, n = re.subn(r'<tr[^>]*><th>older NCERT</th>.*?</tr>', new, card, count=1, flags=re.S)
    return out, bool(n)


# ---------------------------------------------------------------- the one solution

def figures_for(q):
    out, qq = [], q.get("question") or {}
    for f in (qq.get("figures") or []):
        u = ((f.get("printed") or {}).get("png") or {}).get("cdn_url")
        if u:
            out.append((u, f.get("text") or "figure printed with the question"))
    for o in (qq.get("options") or []):
        u = (((o.get("figure") or {}).get("printed") or {}).get("png") or {}).get("cdn_url")
        if u:
            out.append((u, "option %s, as drawn in the booklet" % o.get("key")))
    for f in ((q.get("solution") or {}).get("figures") or []):
        u = ((f.get("printed") or {}).get("png") or {}).get("cdn_url")
        if u:
            out.append((u, f.get("text") or "diagram from the printed solution"))
    return out


#: Widest a paragraph window may render before it is scaled down to fit a card.
_PARA_FIT_MM = 118.0


def ncert_paragraph(card):
    """The book's OWN paragraph, cropped out of the rendered page, instead of a retyped quote.

    WHY THIS REPLACES THE TYPED QUOTE. "What NCERT says" used to print the sentence again in
    an italic serif of our choosing. The page render directly below it already showed that
    same sentence in the book's type, justified as the book justifies it, with the line
    marked -- so the card said the same thing twice, once in the book's voice and once in
    ours. Showing the real paragraph removes the second copy and the transcription layer
    with it: what the student reads IS the page.

    HOW THE CROP WORKS. Every printed line is an absolutely positioned div carrying its own
    `top` in millimetres, and the highlighted run is wrapped in `<mark class="ncq">`. So the
    marked lines' tops bound the passage, and the page is clipped to that band by shifting
    the whole sheet up inside a container of exactly that height. Nothing is re-laid out --
    it is the same sheet, with a window cut in it.

    It only became worth doing once the chapter stylesheet actually applied: those sheets set
    the book's type on `body`, which never matched inside a div, so before that fix the page
    rendered in the wrong font and cropping it would have shown a worse paragraph, not a
    better one.
    """
    out = []
    for m in re.finditer(r'<div class="ncm-pagewrap ([^"]*)">', card):
        end = div_end(card, m.start())
        if end < 0:
            continue
        inner = card[m.end():end - len("</div>")]
        win = _one_page_window(inner, m.group(1))
        if win:
            out.append(win)
    return "".join(out)


def _one_page_window(inner, chapter_class):
    """The marked band of ONE printed page, or "" if that page carries no marked line.

    EVIDENCE OFTEN SPANS SEVERAL PAGES AND EACH NEEDS ITS OWN WINDOW. q157's answer rests on
    lines printed on pages 002, 003 and 012 of its chapter, and q107's on two pages. The first
    version cropped a single band from the FIRST page only and silently dropped the rest --
    and the check written beside it was no better, because it asked whether the lines inside
    the window fitted rather than whether every marked line in the card was shown at all.
    """
    lines = []
    for blk in re.finditer(r'<div class="(blk[^"]*)" style="([^"]*)"[^>]*>(.*?)</div>', inner, re.S):
        st = blk.group(2)
        top = re.search(r'top:([\d.]+)mm', st)
        if not top:
            continue
        left = re.search(r'left:([\d.]+)mm', st)
        wid = re.search(r'width:([\d.]+)mm', st)
        lh = re.search(r'line-height:([\d.]+)mm', st)
        lines.append({"top": float(top.group(1)),
                      "lh": float(lh.group(1)) if lh else 4.2,
                      "left": float(left.group(1)) if left else 0.0,
                      "width": float(wid.group(1)) if wid else 0.0,
                      "head": blk.group(1).split()[-1] == "h",
                      "marked": "ncq" in blk.group(3)})
    lines.sort(key=lambda d: d["top"])
    hit = [i for i, d in enumerate(lines) if d["marked"]]
    if not hit:
        return ""

    # SNAP TO WHOLE PARAGRAPHS, NOT TO A FIXED BAND. A fixed band opened and closed
    # mid-sentence, which is what the owner saw: "does not feel I can complete paragraph".
    #
    # THE INDENT IS NOT IN THE GEOMETRY. The obvious rule -- NCERT indents a paragraph's first
    # line, so look for a larger `left` -- does not work on this extraction: every line of
    # chapter 2 page 009 carries left:67.73mm, because the indent is leading space inside the
    # text. Trusting it made the test never fire and the window grew to 211mm, the whole page.
    #
    # Two signals that ARE in the geometry do the job:
    #   a heading (`blk h`, "2.3.3 Basidiomycetes") is a hard boundary, and worth keeping as
    #   the paragraph's title;
    #   a SHORT line is a paragraph's last line -- the column runs 127mm and a final line runs
    #   14.81mm -- so it closes the block below and, seen above, closes the previous one.
    body = [d["width"] for d in lines if d["width"] > 20]
    full = max(body) if body else 0.0

    def short(d):
        return d["width"] < full - 8.0

    def far(a, b):                      # a blank line's worth of space between two lines
        return b["top"] - (a["top"] + a["lh"]) > 0.6 * a["lh"]

    lo_i, hi_i = min(hit), max(hit)
    while lo_i > 0:
        prev = lines[lo_i - 1]
        if prev["head"]:
            lo_i -= 1                   # keep the heading: it names the paragraph
            break
        if short(prev) or far(prev, lines[lo_i]):
            break
        lo_i -= 1
    while hi_i + 1 < len(lines):
        if short(lines[hi_i]):
            break                       # this line ended the paragraph
        nxt = lines[hi_i + 1]
        if nxt["head"] or far(lines[hi_i], nxt):
            break
        hi_i += 1
    span = lines[lo_i:hi_i + 1]

    # PADDING MUST NOT REACH INTO A NEIGHBOUR, or the window slices the line next to it --
    # which is how partial lines kept appearing at the top and bottom edges.
    above = lines[lo_i - 1] if lo_i > 0 else None
    below = lines[hi_i + 1] if hi_i + 1 < len(lines) else None
    first, last = span[0], max(span, key=lambda d: d["top"] + d["lh"])
    pad_up = min(2.0, (first["top"] - (above["top"] + above["lh"])) / 2.0) if above else 2.0
    pad_dn = min(2.0, (below["top"] - (last["top"] + last["lh"])) / 2.0) if below else 2.0
    top0 = first["top"] - max(pad_up, 0.0)
    bot = last["top"] + last["lh"] + max(pad_dn, 0.0)
    left0 = min(d["left"] for d in span) - 2.0
    right = max(d["left"] + d["width"] for d in span) + 2.0

    # FINAL CLAMP: no line may be sliced by an edge. Padding that merely avoids the NEXT
    # line's top is not enough -- a neighbour's box can still reach across the edge, and
    # three lines were still being cut in half after the padding rule went in. Pulling each
    # edge back to clear any straddling line is decidable from the boxes themselves, so it
    # ends the problem instead of narrowing it.
    inside = set(id(d) for d in span)
    for d in lines:
        if id(d) in inside:
            continue
        d_bot = d["top"] + d["lh"]
        if d["top"] < top0 < d_bot:         # straddles the top edge
            top0 = d_bot
        if d["top"] < bot < d_bot:          # straddles the bottom edge
            bot = d["top"]

    # The shift is an absolutely positioned layer, not a negative margin: `.sheet` carries its
    # own `margin:6mm auto` from the chapter stylesheet, which a margin-based shift adds to --
    # that 6mm was pushing the band down and clipping its last line.
    page = re.search(r'<section class="sheet" id="x(\d+)"', inner)
    tag = ('<span class="ncert-para-pg">printed page %s</span>' % page.group(1)) if page else ""
    # SHRINK TO FIT RATHER THAN CUT. A window can be wider than the card -- the chapter's text
    # column is 127mm and a two-column page pushes it out further -- and clipping it loses the
    # ends of lines. Scaling the whole window down keeps every word on screen, which is what
    # the owner asked for: "you can make big page little shrink but at least all is visible".
    w_mm, h_mm = right - left0, bot - top0
    scale = min(1.0, _PARA_FIT_MM / w_mm)
    box = ('<div class="ncert-para ncm-pagewrap %s" style="width:%.2fmm;height:%.2fmm">'
           '<div class="ncert-para-shift" style="left:-%.2fmm;top:-%.2fmm">%s</div></div>'
           % (chapter_class, w_mm, h_mm, left0, top0, inner))
    if scale < 1.0:
        box = ('<div class="ncert-para-zoom" style="height:%.2fmm">'
               '<div style="transform:scale(%.4f);transform-origin:top left;'
               'width:%.2fmm">%s</div></div>' % (h_mm * scale, scale, w_mm, box))
    return '<div class="ncert-para-wrap">%s%s</div>' % (tag, box)


def solution_diagram(paper, qid):
    """D13's picture for this solution, as HTML. Returns (html, status).

    The packet is read alongside the decision because it is the only record of what the agent
    was ALLOWED to use -- the check refuses an image the agent did not receive. It also holds
    the mapping the page needs: the agent was handed a downloaded local copy, while the page
    must load the CDN original.
    """
    out_p = os.path.join(MAPS, "steps", "D13", "out", "%s.%s.runA.json" % (paper, qid))
    in_p = os.path.join(MAPS, "steps", "D13", "work", "%s.%s.runA.input.json" % (paper, qid))
    if not os.path.exists(out_p) or not os.path.exists(in_p):
        return "", "no D13 decision"
    d13 = json.load(open(out_p, encoding="utf-8"))
    packet = json.load(open(in_p, encoding="utf-8"))
    allowed, src, meta = set(), {}, {}
    for f in ((packet.get("question") or {}).get("figures") or []):
        allowed.add(f.get("path"))
        src[f.get("path")] = f.get("from") or f.get("path")
        meta[f.get("path")] = {"from_booklet": True}
    for f in (packet.get("ncert_figures") or []):
        for key in (f.get("url"), f.get("path")):
            if not key:
                continue
            allowed.add(key)
            src[key] = f.get("url")          # the page always loads the CDN original
            meta[key] = {"chapter": f.get("chapter"), "printed_page": f.get("printed_page"),
                         "caption": f.get("caption")}
    return sd.render(d13, allowed, src, meta)


def ncert_solution_block(q, d12, printed_details, diagram_html="", para_html=""):
    says = ""
    if para_html or d12.get("what_ncert_says"):
        src = d12.get("what_ncert_says_source")
        body = para_html or ("<q>%s</q>" % html.escape(d12.get("what_ncert_says") or ""))
        says = ('<div class="ncert-says%s"><span class="lab">What NCERT says</span>%s%s</div>'
                % (" ncert-says-page" if para_html else "", body,
                   '<span class="src">%s</span>' % html.escape(src) if src else ""))

    printed = str((q.get("answer") or {}).get("publisher") or "").strip()
    mine = str(d12.get("answer_is") or "").strip()
    review = ""
    if printed and mine and printed != mine:
        review = ('<div class="ncert-review"><b>Marked for review</b>NCERT supports option %s, '
                  'but the booklet prints %s.%s</div>'
                  % (html.escape(mine), html.escape(printed),
                     " " + html.escape(d12["note"]) if d12.get("note") else ""))

    wrong = "".join('<li><b>(%s)</b> %s</li>'
                    % (html.escape(str(w.get("option"))), html.escape(str(w.get("why") or "")))
                    for w in (d12.get("why_other_options_fail") or []))

    # `terms_beyond_ncert` is NOT rendered. It is a control the writer answers to -- it forces
    # the agent to notice each word it reaches for outside the book -- but on the page it came
    # out as a raw dump of dicts, and what it mostly listed were the printed texts of the
    # options themselves ("Carbohydrates", "Amino acids"). It stays in the D12 JSON, where it
    # is a reviewable signal, and off the card, where it was noise.
    # SHORT ANSWER IN FRONT, FULL REASON BEHIND A CLICK.
    #
    # The complaint was about what a student SEES on opening a card -- "students see the
    # solution, feels oh they have given such a big solution". Measured, the explanation was
    # never the bulk: 92 to 110 words across these five, against 180 to 335 in the trap block.
    # So nothing is cut. The quoted NCERT line stays; `in_short` says what THAT line means in
    # one or two plain sentences directly beneath it; the full reasoning and the per-option
    # refusals go behind one disclosure. Shortening `explanation` was the other option and
    # would have undone this step's purpose -- solutions a student can tie back to the book.
    short = ('<p class="ncert-short">%s</p>' % html.escape(d12["in_short"])
             if d12.get("in_short") else "")
    more = ""
    if d12.get("explanation") or wrong:
        more = ('<details class="ncert-more"><summary>the full reason, and why each other '
                'option fails</summary><p class="ncert-expl">%s</p>'
                '<ul class="ncert-wrong">%s</ul></details>'
                % (html.escape(d12.get("explanation") or ""), wrong))

    # The picture is D13's considered one, not a dump of every image attached to the question.
    # The booklet's own figure is already shown in the crop beside the card, so repeating it
    # unmarked added nothing; what helps is the marked or drawn version, or nothing at all.
    return ('<div class="sol ncert"><div class="solhead">Solution<span>answer %s</span></div>'
            '%s%s%s%s%s%s</div>'
            % (html.escape(mine), review, says, short, diagram_html, more, printed_details))


def own_header(head, paper, qids):
    """Give this page its own heading instead of the full paper's extraction dashboard.

    The exported paper opens with a QA dashboard -- 200 questions, 46 figures, 39 match-lists
    rebuilt as tables, 4 answer disagreements -- and a paragraph explaining that flags are shown
    rather than tidied away. All of it counts the whole booklet and exists to hunt extraction
    faults. On a page of five questions it is both wrong (the numbers describe 200 other
    questions) and beside the point.
    """
    head, _, _ = cut_div(head, "stats")     # balanced: it is a grid of nested .stat divs
    head = re.sub(r'<div class="sub">.*?</div>',
                  '<div class="sub">%d Biology questions from %s, built NCERT-first: the '
                  'chapter and subtopic are the book&rsquo;s own, and the solution is written '
                  'in its vocabulary. %s</div>'
                  % (len(qids), paper.replace("_", " "), ", ".join(qids)),
                  head, count=1, flags=re.S)
    head = re.sub(r'(<h1>)(.*?)(</h1>)',
                  lambda m: m.group(1) + "NEET 2024 S1 &middot; Biology, NCERT-first"
                  + m.group(3), head, count=1, flags=re.S)
    return head


# ---------------------------------------------------------------- driver

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--questions",
                    help="comma-separated qids; omit to take every Biology question that has "
                         "a D12 solution")
    ap.add_argument("--into-paper", action="store_true",
                    help="rewrite the Biology cards inside question_paper.html itself, rather "
                         "than writing a separate preview file")
    ap.add_argument("--out", default="biology_ncert_first.html")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    year = a.paper.split("_")[0]
    base = os.path.join(HERE, "data", year, a.paper)
    raw = open(os.path.join(base, "question_paper.html"), encoding="utf-8").read()
    doc = json.load(open(os.path.join(base, "questions.json"), encoding="utf-8"))
    pages = json.load(open(os.path.join(MAPS, "maps", "page_html.json"), encoding="utf-8"))
    Q = {q["question_id"].split("__")[-1]: q for q in doc["questions"]}

    # BIOLOGY ONLY, AND ONLY WHERE THE REPLACEMENT EXISTS. Without `--questions` the run takes
    # every Biology question that has a D12 solution waiting. A question whose solution has not
    # been written yet keeps the card it already has -- the old solution is never removed until
    # the new one is there to put in its place.
    if a.questions:
        qids = [x.strip() for x in a.questions.split(",") if x.strip()]
    else:
        qids = [qid for qid, q in sorted(Q.items())
                if ((q.get("classification") or {}).get("subject") or "") == "Biology"
                and os.path.exists(os.path.join(MAPS, "steps", "D12", "out",
                                                "%s.%s.runA.json" % (a.paper, qid)))]
        print("   %-38s %d" % ("biology questions with a solution", len(qids)))
    if not qids:
        print("nothing to do -- run D12 first")
        return

    head = own_header(raw[:raw.find('<div class="q" id="')], a.paper, qids)
    report, cards = collections.Counter(), []
    spliced = {}
    for qid in qids:
        m = re.search(r'<div class="q" id="%s".*?(?=<div class="q" id="|\Z)' % re.escape(qid),
                      raw, re.S)
        if not m:
            report["card not found"] += 1
            continue
        p = os.path.join(MAPS, "steps", "D12", "out", "%s.%s.runA.json" % (a.paper, qid))
        if not os.path.exists(p):
            report["no D12 solution"] += 1
            continue
        d12 = json.load(open(p, encoding="utf-8"))
        q, card = Q[qid], m.group(0)
        mp = q.get("ncert_mapping") or {}

        # the publisher's printed-solution image is scanned evidence, not a second solution
        _, pub_inner, _ = cut_div(card, "sol pub")
        det = re.search(r'<details.*?</details>', pub_inner, re.S)
        printed_details = det.group(0) if det else ""
        report["printed-solution image kept"] += 1 if printed_details else 0

        card, _, at = cut_div(card, "sol pub")
        card, _, _ = cut_div(card, "sol ai")
        dia, how = solution_diagram(a.paper, qid)
        report["diagram: %s" % how] += 1
        if at >= 0:
            para = ncert_paragraph(card)
            report["NCERT paragraph shown as printed"] += 1 if para else 0
            block = ncert_solution_block(q, d12, printed_details, dia, para)
            card = card[:at] + block + card[at:]
            report["solutions 2 -> 1"] += 1
            if "ncert-review" in block:
                report["marked for review"] += 1

        card, n = drop_rows(card)
        report["rows dropped"] += n
        card, n = strip_repeats(card)
        report["repeated spans stripped"] += n
        card, named = name_the_new_type(card, q)
        report["new type given its name"] += 1 if named else 0
        card, moved = fix_mtc_order(card)
        report["'choose the correct' moved below table"] += 1 if moved else 0
        card, merged = merge_tricky_into_difficulty(card)
        report["difficulty reason attached to rating"] += 1 if merged else 0
        where, name = chapter_label(pages,
                                    (mp.get("chapter") or {}).get("ncert_chapter_ids") or [])
        subs = [("%s %s" % (s.get("printed_number") or "", s.get("name") or "")).strip()
                for s in (mp.get("ncert_subtopics") or [])]
        card, ok = set_chapter(card, where, name, subs)
        report["chapter row now NCERT's"] += 1 if ok else 0
        card, same = collapse_older(card, mp)
        report["older edition collapsed (identical)"] += 1 if same else 0
        cards.append(card)
        spliced[(m.start(), m.end())] = card
        report["rendered"] += 1

    for k, v in sorted(report.items()):
        print("   %-38s %d" % (k, v))
    if not cards:
        print("nothing rendered")
        return

    if a.into_paper:
        # THE BIOLOGY CARDS ARE REPLACED WHERE THEY STAND. Physics and Chemistry cards are not
        # read and not rewritten, so one booklet can carry NCERT-first Biology beside the
        # ordinary cards for the subjects whose NCERT corpus is not extracted yet. Assembled in
        # a single pass: splicing each card into an 8 MB string one at a time rebuilds the
        # whole document per card, which is what made an earlier join take minutes.
        out, last = [], 0
        for (lo, hi), card in sorted(spliced.items()):
            out.append(raw[last:lo])
            out.append(card)
            last = hi
        out.append(raw[last:])
        page = "".join(out)
        if "ncert-short" not in raw:                      # the card stylesheet, once
            page = page.replace("</style>", "</style><style>%s</style>" % EXTRA_CSS, 1)
        bal = len(re.findall(r'<div\b', page)) - len(re.findall(r'</div>', page))
        print("   %-38s %d" % ("div balance (0 = clean)", bal))
        print("   %-38s %.0f KB -> %.0f KB" % ("question_paper.html", len(raw) / 1000,
                                               len(page) / 1000))
        if bal != 0:
            print("REFUSING to write: the document's divs are unbalanced")
            return
        if not a.apply:
            print("(nothing written -- pass --apply)")
            return
        open(os.path.join(base, "question_paper.html"), "w", encoding="utf-8").write(page)
        print("wrote question_paper.html")
        return

    page = (head.replace("</style>", "</style><style>%s</style>" % EXTRA_CSS, 1)
            + "".join(cards) + "</div>")
    bal = len(re.findall(r'<div\b', page)) - len(re.findall(r'</div>', page))
    print("   %-38s %d" % ("div balance (0 = clean)", bal))
    if not a.apply:
        print("(nothing written -- pass --apply)   would write %s (%.0f KB)"
              % (a.out, len(page) / 1000))
        return
    open(os.path.join(base, a.out), "w", encoding="utf-8").write(page)
    print("wrote %s (%.0f KB)" % (a.out, len(page) / 1000))


if __name__ == "__main__":
    main()
