#!/usr/bin/env python3
"""Write the ECAT ratings into an exported paper's three deliverables.

    python3 code/join_ecat_into_export.py --paper 2017_A
    python3 code/join_ecat_into_export.py --paper 2017_A --apply

WHY THIS EXISTS INSTEAD OF RE-EXPORTING
---------------------------------------
`export_paper_v2.py` builds the three files from the papers_v2 CORPUS record, and already knows
how to render a rating (`categories_of`, and the E1-E4 cards in `question_record`). For 2017_A
that record does not exist -- `papers/papers/` holds `2017_C.json`, the Code C booklet, and no
`2017_A.json` is on disk or anywhere in git history. The export itself is complete and correct
(the owner confirms it; 180/180 done on every field but `categories`), so the ratings are written
INTO it rather than regenerated from a source that is gone.

That makes this a patcher, not a second exporter. It does not re-render a single question: it
adds the `categories` block to each question in `questions.json`, flips `status.categories`, and
inserts one card into the matching question in `question_paper.html` and `question_paper.md`.
Everything else in the three files is left byte-for-byte alone.

IF THE 2017_A RECORD IS EVER RESTORED, delete this and run the exporter -- it renders the same
five axes natively and will do it better.
"""

import argparse
import collections
import glob
import html
import json
import os
import re

import yaml

import runner_core as rc
from lib import texhtml

OUT_DIRS = (("steps", "ECAT", "out"),)
#: ONE FIELD, ONE ROW. An earlier version put a whole axis on a line, so E3 read
#: `practical_procedure · Potentiometer null method: at balance the galvanometer carries no
#: current ...` -- a LABEL from a closed vocabulary and a sentence of free prose joined by a
#: middot, as if they were two values of one thing. They are not: the label is checkable against
#: `allowed_values.yaml`, the concept is the rater's own words. Reading one against the other is
#: the whole point of the card, and that is impossible when they share a line.
ROWS = (
    ("Type", "qtype", "label"),
    ("Asks", "asks", "label"),
    ("Concept", "concept", "text"),
)


def glossary():
    r"""{label: what it MEANS} read from the rulebook's own definition tables.

    THE SECOND COLUMN, NOT THE THIRD. The rulebook sets every axis out as
    `| \`label\` | means | not |`, and the ECAT audit's failure 2 is that the review page read
    column 3 -- the counter-example -- into a box headed "requires", so people were grading
    against the opposite of the rule. Column 2 is the definition; column 3 is deliberately not
    shown here, because a card has room for one line and the definition is the useful one.

    Without this the card prints `representation_translation` and nothing else, which tells a
    reader who does not already know the vocabulary exactly nothing.
    """
    # THE LIVE VOCABULARY FIRST. The rulebook defines the names this sheet RETIRED, so reading
    # only it left every current value bare on the card. `category_means` in allowed_values.yaml
    # carries the one-line definition beside the value it defines, and the rulebook is kept as
    # the fallback so a retired label still resolves wherever one survives.
    out = {}
    try:
        av = yaml.safe_load(open(rc.pp("config", "allowed_values.yaml"), encoding="utf-8"))
        for axis in (av.get("category_means") or {}).values():
            out.update(axis)
    except Exception:                                   # reported by the empty gloss, not hidden
        pass
    path = rc.pp("..", "_shared", "docs", "question_categories", "RULEBOOK.md")
    if not os.path.exists(path):
        return out
    row = re.compile(r"^\|\s*`([a-z0-9_]+)`\s*\|([^|]*)\|")
    for line in open(path, encoding="utf-8"):
        m = row.match(line.strip())
        if not m:
            continue
        label, means = m.group(1), " ".join(m.group(2).split())
        if means and label not in out:
            out[label] = means
    return out


def packet_fields(paper_id):
    """{question_id: {E1_question_type, ...}} as the PACKET supplied them.

    `question_type`, `format` and `content_shape` are optional in `schemas/ECAT.json`, and a
    rater told to read only its input and codebook often omits them -- it was asked for the
    judgement axes, and E1 was handed to it as given rather than asked for. The card then showed
    a question with no type at all, which is the one field a reader checks first. The packet's
    own `E1_question_type` (decided by `type_patterns`) is the answer in that case, so the card
    falls back to it rather than leaving the row out.
    """
    out = {}
    for path in sorted(glob.glob(rc.pp("steps", "ECAT", "work",
                                       "*%s*.input.json" % paper_id))):
        try:
            doc = json.load(open(path, encoding="utf-8"))
        except ValueError:
            continue
        for q in (doc.get("questions") or []):
            if q.get("question_id"):
                out[q["question_id"]] = q
    return out


def ratings_for(paper_id):
    """{question_id: (rating, group_note)} across every ECAT output for this paper."""
    found = {}
    for folder in OUT_DIRS:
        for path in sorted(glob.glob(rc.pp(*folder, "*.json"))):
            try:
                doc = json.load(open(path, encoding="utf-8"))
            except ValueError:
                continue
            if doc.get("error"):
                continue
            note = doc.get("group_note") or ""
            for rating in (doc.get("ratings") or []):
                qid = rating.get("question_id") or ""
                # Both id spellings are live in this corpus; normalise to the export's.
                qid = qid.replace("#q", "__q")
                if not qid.startswith(paper_id):
                    continue
                # A RATING A HUMAN HAS REVIEWED IS NOT OVERWRITTEN BY A LATER MACHINE PASS.
                # Re-rating the whole paper re-reads questions that were already judged and
                # corrected by hand; without this the second pass silently discards that work,
                # and the discarding is invisible because both files are valid ratings.
                if (found.get(qid) or (None,))[0] and found[qid][0].get("reviewed") \
                        and not rating.get("reviewed"):
                    continue
                found[qid] = (rating, note)
    return found


def _card_html(rating, note):
    """One `<div class="ecat">` -- the three fields, the trap, the NCERT line, the reasoning."""
    rows = []
    # THE FLAG GOVERNS THE WHOLE CARD, SO IT GOES FIRST. A reader who takes a tag from a
    # misprinted question and puts it in a count has produced a fact about the misprint.
    flags = rating.get("flags") or []
    if flags:
        rows.append('<tr><th>Not counted</th><td class="ecat-text">%s<span class="ecat-cite">%s'
                    '</span></td></tr>'
                    % ("".join('<span class="ecat-flag">%s</span>'
                               % html.escape(NAMES.get(f, f.replace("_", " "))) for f in flags),
                       html.escape(rating.get("flag_why") or "")))
    for label, field, kind in ROWS:
        value = rating.get(field)
        if not value:
            continue
        vals = [str(v).strip() for v in (value if isinstance(value, list) else [value])
                if str(v).strip()]
        if not vals:
            continue
        # A LABEL IS ESCAPED; PROSE IS RENDERED. `concept`, `route`, `why` and `note` are the
        # rater's own words and are full of maths typed as LaTeX -- `$h/\\sqrt{3mkT}$`,
        # `$\\mathrm{O_2}$`. Escaped, they printed as their own source.
        if kind == "label":
            body, cls = "".join(_chip(v) for v in vals), "ecat-label-cell"
        else:
            body, cls = texhtml.to_html(" ".join(vals)), "ecat-text"
        rows.append('<tr><th>%s</th><td class="%s">%s</td></tr>'
                    % (html.escape(label), cls, body))

    t = rating.get("trap") or {}
    if t.get("label"):
        opt = t.get("option")
        rows.append(
            '<tr><th>Where students go wrong</th><td class="ecat-label-cell">%s%s<div class="ecat-route">%s</div>'
            '</td></tr>'
            % (_chip(str(t["label"])),
               '<span class="ecat-opt">option %s</span>' % html.escape(str(opt)) if opt else "",
               texhtml.to_html(str(t.get("route", "")))))
        prop = t.get("proposed") or {}
        if prop.get("name"):
            rows.append('<tr><th>Proposed</th><td class="ecat-text">'
                        '<span class="ecat-slug">%s</span>%s</td></tr>'
                        % (html.escape(prop["name"]), html.escape(prop.get("why", ""))))

    # A SECOND REAL MISCONCEPTION, where one exists. Never one per option: most questions have
    # none. Before this field existed these were written into `note`, where they read as a
    # remark about the record rather than as a trap -- 10 of the first 30 ratings did that.
    for extra in (rating.get("also") or []):
        if not extra.get("label"):
            continue
        rows.append(
            '<tr><th>Second mistake</th><td class="ecat-label-cell">%s%s<div class="ecat-route">%s</div>'
            '</td></tr>'
            % (_chip(str(extra["label"])),
               '<span class="ecat-opt">option %s</span>' % html.escape(str(extra["option"]))
               if extra.get("option") else "",
               texhtml.to_html(str(extra.get("route", "")))))

    if rating.get("reason"):
        rows.append('<tr><th>Why this answer</th><td class="ecat-text">%s</td></tr>'
                    % texhtml.to_html(rating["reason"]))

    # THE PRINTED SENTENCE, QUOTED. `asks: fact_line` claims the question wants a line NCERT
    # states; until this row existed that claim was made from the SHAPE of the question with
    # nobody opening the book. A quote with a chapter and a page can be checked; a label cannot.
    nc = rating.get("ncert") or {}
    if nc.get("quote"):
        where = (nc.get("chapter") or "").split("_", 1)[-1].replace("-", " ")
        bits = [b for b in (where,
                            "page %s" % nc["page"] if nc.get("page") else "",
                            nc.get("ncert_subtopic") or "") if b]
        tag = ""
        if nc.get("supports") == "partial":
            tag = ('<span class="ecat-partial">partial &mdash; the student still has to join '
                   'two facts</span>')
        rows.append('<tr><th>NCERT</th><td class="ecat-text">'
                    '<span class="ecat-quote">&ldquo;%s&rdquo;</span>'
                    '<span class="ecat-cite">%s</span>%s</td></tr>'
                    % (html.escape(nc["quote"]), html.escape(" &middot; ".join(bits))
                       .replace("&amp;middot;", "&middot;"), tag))
    elif nc and nc.get("found") is False:
        # NOT A GAP IN THE RATING -- A FINDING ABOUT THE QUESTION. Four of the 2017 biology
        # questions test material the rationalised NCERT deleted, so no line can be cited and
        # saying so is more useful than leaving the row off and letting it read as unchecked.
        rows.append('<tr><th>NCERT</th><td class="ecat-text">'
                    '<span class="ecat-nonncert">Not in the current NCERT</span>'
                    '<span class="ecat-cite">%s</span></td></tr>'
                    % html.escape(nc.get("why_not") or ""))
    if rating.get("note"):
        rows.append('<tr><th>Note</th><td class="ecat-text">%s</td></tr>'
                    % texhtml.to_html(rating["note"]))
    if not rows:
        return ""
    return ('<div class="ecat"><div class="ecat-h">Categories</div>'
            '<table class="ecat-t">%s</table></div>' % "".join(rows))


def _card_md(rating, note):
    def chip(v):
        name = NAMES.get(v, v.replace("_", " "))
        gl = GLOSS.get(v)
        return "**%s** (`%s`)%s" % (name, v, " \u2014 %s" % gl if gl else "")

    bits = ["#### Categories", ""]
    for label, field, kind in ROWS:
        value = rating.get(field)
        if not value:
            continue
        vals = [str(v).strip() for v in (value if isinstance(value, list) else [value])
                if str(v).strip()]
        if not vals:
            continue
        shown = "; ".join(chip(v) for v in vals) if kind == "label" else " ".join(vals)
        bits.append("- **%s:** %s" % (label, shown))

    t = rating.get("trap") or {}
    if t.get("label"):
        bits.append("- **Trap:** %s%s  \n  %s"
                    % (chip(t["label"]),
                       " \u2014 option %s" % t["option"] if t.get("option") else "",
                       t.get("route", "")))
        prop = t.get("proposed") or {}
        if prop.get("name"):
            bits.append("- **Proposed:** `%s` \u2014 %s" % (prop["name"], prop.get("why", "")))
    for extra in (rating.get("also") or []):
        if extra.get("label"):
            bits.append("- **Also:** %s%s  \n  %s"
                        % (chip(extra["label"]),
                           " \u2014 option %s" % extra["option"] if extra.get("option") else "",
                           extra.get("route", "")))
    if rating.get("reason"):
        bits.append("- **Why:** %s" % rating["reason"])
    nc = rating.get("ncert") or {}
    if nc.get("quote"):
        where = (nc.get("chapter") or "").split("_", 1)[-1].replace("-", " ")
        bits.append("- **NCERT:** \u201c%s\u201d  \n  *%s%s*"
                    % (nc["quote"], where,
                       ", page %s" % nc["page"] if nc.get("page") else ""))
    if rating.get("note"):
        bits.append("- **Note:** %s" % rating["note"])
    return "\n".join(bits) if len(bits) > 2 else ""


#: Injected once, so the cards look like the page rather than like an afterthought.
CSS = """
.ecat{margin:10px 0 0;border:1px solid #d7dde4;border-left:3px solid #2f6f4f;border-radius:6px;
 background:#f7faf8;padding:9px 12px;font-size:13px}
.ecat-h{font-weight:700;color:#2f6f4f;font-size:11px;letter-spacing:.07em;text-transform:uppercase;
 margin-bottom:7px}
.ecat-t{width:100%;border-collapse:collapse}
.ecat-t th{text-align:left;width:104px;vertical-align:top;padding:5px 10px 5px 0;color:#6a7a72;
 font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.04em;
 border-top:1px solid #e4eae5}
.ecat-t td{padding:5px 0;vertical-align:top;border-top:1px solid #e4eae5}
.ecat-t tr:first-child th,.ecat-t tr:first-child td{border-top:0}
/* THE NAME IS THE HEADLINE, THE SLUG IS THE FOOTNOTE. The slug used to be the only thing
   printed, so a reader who did not already know the vocabulary learned nothing from the row. */
.ecat-name{font-weight:650;color:#1f4f3a;font-size:13px}
.ecat-slug{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11px;color:#7c8a83;
 background:#eef3ef;padding:1px 5px;border-radius:3px;margin-left:6px}
.ecat-label{display:inline-block;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
 font-size:12px;background:#e8f0ea;color:#1f4f3a;padding:1px 6px;border-radius:3px;margin:0 3px 2px 0}
.ecat-label-cell{color:#3a4a43;line-height:1.5}
.ecat-text{color:#3a4a43;line-height:1.5}
.ecat-gloss{color:#6a7a72;font-size:12px;margin-left:8px}
/* The option used to be a bare <b>, which inherited the page's muted body colour and came out
   paler than the gloss beside it -- the one piece of the trap row a reader actually looks for. */
.ecat-opt{display:inline-block;margin-left:8px;padding:1px 7px;border-radius:3px;
 background:#8c2f2f;color:#fff;font-weight:700;font-size:11px;letter-spacing:.03em;
 text-transform:uppercase;vertical-align:1px}
.ecat-route{color:#4a5a52;margin-top:3px;line-height:1.45}
.ecat-quote{display:block;color:#33443c;font-style:italic;line-height:1.5;
 border-left:2px solid #c3d6c9;padding-left:9px}
.ecat-cite{display:block;color:#7c8a83;font-size:11px;margin-top:3px;padding-left:11px;
 text-transform:uppercase;letter-spacing:.04em}
.ecat-partial{display:block;color:#8a6d1f;font-size:11px;margin-top:3px;padding-left:11px;
 text-transform:uppercase;letter-spacing:.04em}
.ecat-nonncert{display:inline-block;background:#f2e6e6;color:#8c2f2f;font-weight:650;
 font-size:12px;padding:1px 8px;border-radius:3px}
.ecat-flag{display:inline-block;background:#8c2f2f;color:#fff;font-weight:700;font-size:11px;
 letter-spacing:.04em;text-transform:uppercase;padding:2px 9px;border-radius:3px;margin-right:6px}
.ecat-traps{margin:0;padding-left:16px}
.ecat-traps li{margin:0 0 6px}
"""


def display_names():
    """{slug: the name a human reads}.

    The slug is the DATA and stays in the record; this is what the card prints. A value with no
    entry falls back to its own slug, so a newly added value is legible immediately and only
    loses the underscore once someone has written it a name.
    """
    try:
        av = yaml.safe_load(open(rc.pp("config", "allowed_values.yaml"), encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for axis in (av.get("display") or {}).values():
        out.update(axis)
    return out


GLOSS = glossary()
NAMES = display_names()


def _chip(value):
    """The readable name, the slug, and the definition ONLY where it adds something.

    Printing all three unconditionally made the commonest rows say one thing three times:
    `A fact NCERT states` / `fact_line` / `a fact NCERT states: what, who or where`. The
    display name is usually a tidied-up head of the definition, so when the name's words are
    already in the definition the definition is dropped from the line and kept on hover.
    """
    name = NAMES.get(value, value.replace("_", " "))
    gl = GLOSS.get(value) or ""
    nw = set(re.findall(r"[a-z]+", name.lower()))
    gw = set(re.findall(r"[a-z]+", gl.lower()))
    # A SHORT NAME CANNOT CARRY A DEFINITION, so it always keeps one. The labels used to be
    # sentences -- `A fact NCERT states` beside `a fact NCERT states: what, who or where` --
    # and suppressing the repeat was right for those. Now they are one or two words naming the
    # thing, and `Proportionality` on its own tells a reader who does not know the vocabulary
    # nothing. Only a long label that restates its own definition is still suppressed.
    covered = len(nw) > 2 and len(nw - gw) <= 1
    chip = ('<span class="ecat-name"%s>%s</span><span class="ecat-slug">%s</span>'
            % (' title="%s"' % html.escape(gl) if gl else "",
               html.escape(name), html.escape(value)))
    if gl and not covered:
        chip += '<span class="ecat-gloss">%s</span>' % html.escape(gl)
    return chip


def apply_to(paper_id, apply_=False):
    year = paper_id.split("_")[0]
    base = rc.pp("data", year, paper_id)
    jpath = os.path.join(base, "questions.json")
    hpath = os.path.join(base, "question_paper.html")
    mpath = os.path.join(base, "question_paper.md")
    if not os.path.exists(jpath):
        raise SystemExit("no export at %s" % jpath)

    found = ratings_for(paper_id)
    packets = packet_fields(paper_id)
    for qid, (rating, _note) in found.items():
        if not rating.get("question_type") and packets.get(qid, {}).get("E1_question_type"):
            rating["question_type"] = packets[qid]["E1_question_type"]
            rating["question_type_from"] = "type_patterns (the rating omitted it)"
    doc = json.load(open(jpath, encoding="utf-8"))
    rows = doc.get("questions") or []
    hit = 0
    for row in rows:
        qid = row.get("question_id")
        if qid not in found:
            continue
        rating, _note = found[qid]
        # The group note is the rater's record of how a PACKET was kept consistent. It is not a
        # property of this question, it repeats on every member of the group, and it is long --
        # so it stays in the ECAT output, where a reviewer of the rating can find it, and out of
        # the per-question record. (Owner's call.)
        row["categories"] = dict(rating)
        row.setdefault("status", {})["categories"] = "done"
        hit += 1
    counts = doc.setdefault("counts", {})
    counts["categories"] = {"done": hit, "not_run": max(0, len(rows) - hit)}

    print("%s: %d of %d questions have an ECAT rating" % (paper_id, hit, len(rows)))
    if not apply_:
        print("(nothing written -- pass --apply)")
        return hit

    with open(jpath, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)

    # --- HTML: one card per question, placed at the end of that question's block -------------
    if os.path.exists(hpath):
        page = open(hpath, encoding="utf-8").read()
        # IDEMPOTENT, AND FENCED SO IT CANNOT OVER-MATCH.
        #
        # This used to strip `<div class="ecat">.*?</div></div>`, guessing the card's end from
        # its closing tags. When the card's markup changed to end `</table></div>`, that guess
        # stopped matching the card -- so the scan ran PAST it, into the question's own markup,
        # and deleted everything up to the next `</div></div>` it could find. It emptied 29
        # question blocks on this page. A regex that deletes up to a tag it merely expects is
        # not idempotency, it is a content shredder; an explicit fence cannot do this.
        page = re.sub(r"<!--ecat:q\d+-->.*?<!--/ecat-->", "", page, flags=re.S)
        # REFRESHED, NOT ONLY INSERTED. Guarding on "is it already there" meant every later
        # style change was silently dropped on a page that had been joined once -- the card
        # markup moved on while the page kept the first run's CSS. Fenced, so it can be replaced.
        page = re.sub(r"/\*ecat-css\*/.*?/\*/ecat-css\*/", "", page, flags=re.S)
        page = page.replace("</style>", "/*ecat-css*/" + CSS + "/*/ecat-css*/</style>", 1)
        added = 0
        for row in rows:
            qid = row.get("question_id")
            if qid not in found:
                continue
            qno = row.get("qno")
            card = _card_html(*found[qid])
            if not card:
                continue
            # PLACED BEFORE THE NEXT QUESTION, NOT BY COUNTING TAGS.
            #
            # This used to anchor on the question's own container and walk forward balancing
            # `<div>`/`</div>` to find its end. The page's divs do not balance -- so the walk
            # never reached depth 0, the index stayed at the block START, and every card was
            # inserted ABOVE its own question. The card for Q91 printed before the Q91 heading.
            #
            # The next question's anchor cannot drift that way: whatever the markup does in
            # between, the end of question N is immediately before the start of question N+1.
            m = re.search(r"<div class=\"q\" id=\"q%03d\"" % qno, page)
            if not m:
                continue
            nxt = re.search(r"<div class=\"q\" id=\"q\d{3}\"", page[m.end():])
            if nxt:
                i = m.end() + nxt.start()
            else:                                   # the last question on the page
                tail = page.rfind("</div></body>")
                i = tail if tail != -1 else len(page)
            fenced = "<!--ecat:q%03d-->%s<!--/ecat-->" % (qno, card)
            page = page[:i] + fenced + page[i:]
            added += 1
        # THE SUMMARY STRIP MUST AGREE WITH THE PAGE. It carries a `rated on E1-E5` stat that
        # the export wrote once, as 0, and nothing updated -- so a page showing 26 category
        # cards still announced "0 RATED ON E1-E5" at the top, which reads as "nothing was
        # assigned" and is the first thing anyone checking the paper looks at.
        page, n_sub = re.subn(
            r'(<div class="stat"><b>)\d+(</b><span>rated on E1-E5</span></div>)',
            lambda m: "%s%d%s" % (m.group(1), added, m.group(2)), page, count=1)
        with open(hpath, "w", encoding="utf-8") as fh:
            fh.write(page)
        print("  html: %d card(s) inserted, summary counter %s"
              % (added, "updated" if n_sub else "NOT FOUND -- check the stat markup"))

    # --- Markdown: appended under each question --------------------------------------------
    if os.path.exists(mpath):
        md = open(mpath, encoding="utf-8").read()
        md = re.sub(r"\n<!--ecat-->\n.*?\n<!--/ecat-->\n", "\n", md, flags=re.S)  # idempotent
        added = 0
        for row in rows:
            qid = row.get("question_id")
            if qid not in found:
                continue
            block = _card_md(*found[qid])
            if not block:
                continue
            pat = re.compile(r"(^#+\s*(?:Q\.?\s*)?%d\b.*?)(?=^#+\s|\Z)" % row.get("qno"),
                             re.S | re.M)
            m = pat.search(md)
            if not m:
                continue
            md = (md[:m.end()].rstrip() + "\n\n<!--ecat-->\n" + block + "\n<!--/ecat-->\n\n"
                  + md[m.end():])
            added += 1
        with open(mpath, "w", encoding="utf-8") as fh:
            fh.write(md)
        print("  md:   %d block(s) inserted" % added)
    return hit


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    apply_to(a.paper, a.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
