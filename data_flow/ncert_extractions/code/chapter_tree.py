#!/usr/bin/env python3
"""Turn one extracted chapter into the CHAPTER JSON -- the nested tree that is the truth.

    from chapter_tree import build_chapter_json
    doc = build_chapter_json(layout, reprint="2024-25", lang="EN")

`docs/NCERT_INDEX_SCHEMA.md` is the specification; this module implements it. DynamoDB rows and
the search index are both built FROM this file, never the other way round, so if the table is
ever wrong it is refilled from here.

STORE THE CHAPTER AS A TREE, NOT AS BOXES ON A PAGE
-----------------------------------------------------
The thing a product asks for is "1.2.2 Genus, paragraph 1" -- never "page 7, block 4". So the
unit of storage is a piece of the chapter's STRUCTURE, and its position on the page becomes one
of its attributes rather than its identity. Three consequences fall out of that, and each one
fixes a real defect in the box-per-page model:

  * A PARAGRAPH BROKEN ACROSS A PAGE IS ONE PIECE, NOT TWO. 1.1 paragraph 1 ends page 3 at
    "biodiversity or the number and" and finishes on page 4. As two rows it is two half
    sentences, neither quotable. As one node with two `boxes` it is one paragraph that happens
    to be printed in two places.

  * A LIST IS ONE PIECE. The four universal rules of nomenclature run from page 4 to page 5;
    as four loose rows the list has no head and no order.

  * A FIGURE BELONGS WHERE IT IS MENTIONED, NOT WHERE IT IS PRINTED. Figure 1.1 is printed
    beside the end of 1.2.6 but belongs to 1.2.7, which is the section that discusses it. The
    printed position is kept in `boxes` so the page can still be reconstructed exactly.

WHAT IS DELIBERATELY NOT IN THE TREE
--------------------------------------
The running header, the folio, the reprint line and the opener's own contents list. They are
page FURNITURE and live on the page and chapter rows. Left in the tree they surface as content:
"4 Biology" and "2024-25" turn up in read-along, in search results and in an AI prompt as though
NCERT had written them.
"""

import hashlib
import re

# Prefixes are part of the id, so an id says what it is without a lookup: `p_7Kq2xP` is a
# paragraph, `s_qwULfF` a section. Matches the schema's examples.
_ID_PREFIX = {
    "para": "p", "section": "s", "figure": "f", "table": "t", "list": "l",
    "question": "q", "box": "b", "equation": "e", "example": "x",
    "summary": "s", "exercises": "s", "chapter": "c", "unit": "u",
}
_B62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def stable_id(kind, book_base, chapter_num, path):
    """A permanent id for one piece, e.g. `p_7Kq2xP`.

    Hashed from (book WITHOUT its edition letter, chapter, tree path) and NOT from the text,
    because the English and the Hindi book must give the SAME id to the same paragraph -- the
    schema's whole point is that a PYQ mapped once works for both. Their structure lines up
    (same sections, same figures, same paragraphs), so position is the thing they share and
    content is the thing they do not.

    It is also why the id survives a re-extraction: block numbers shift when a page is read
    again, tree positions do not.
    """
    seed = f"{book_base}|{chapter_num}|{path}".encode("utf-8")
    h = int.from_bytes(hashlib.blake2b(seed, digest_size=8).digest(), "big")
    out = []
    for _ in range(6):
        out.append(_B62[h % 62])
        h //= 62
    return f"{_ID_PREFIX.get(kind, 'n')}_{''.join(out)}"


# A mark must cover the WORD and nothing else. The text layer routinely runs a trailing full
# stop, comma or closing bracket into the italic run -- "Solanum." is stored italic WITH its
# full stop -- and that then renders as an italic punctuation mark the book does not print.
_TRIM_TAIL = " \t.,;:!?)]}’”"
_TRIM_HEAD = " \t([{‘“"


def runs_to_body_marks(runs):
    """[{t,b,i,sc,script}] -> (body, marks) with marks as CHARACTER OFFSETS into body.

    Offsets, not nested spans, because a product needs to pull ONE SENTENCE out of a paragraph
    and keep its italics. With offsets that is arithmetic on the sentence's own range; with a
    chain of formatted pieces it means re-walking and re-splitting the chain every time.
    """
    body, marks = [], []
    pos = 0
    # COLOURED TYPE. BIO12L ch05 p097 prints the inserted `B`, `BI`, `BIG` of `RAM HAS BRE DCA P`
    # in red inside black bold. A formatted run whose ink is neither the block's own (by
    # characters -- a blue caption's marks carry no colour) nor near-black carries `color`.
    inks = {}
    for r in runs or []:
        if r.get("color"):
            inks[r["color"]] = inks.get(r["color"], 0) + len((r.get("t") or "").strip())
    block_ink = max(inks, key=inks.get) if inks else None

    def _own_colour(c):
        if not c or c == block_ink or not re.fullmatch(r"#[0-9a-fA-F]{6}", c):
            return None
        r_, g_, b_ = (int(c[i:i + 2], 16) for i in (1, 3, 5))
        return c.lower() if (r_ * 299 + g_ * 587 + b_ * 114) / 1000 > 60 else None
    for r in runs or []:
        t = r.get("t", "")
        if not t:
            continue
        body.append(t)
        flags = {k: True for k in ("b", "i", "sc") if r.get(k)}
        if r.get("script"):
            flags[r["script"]] = True          # sup / sub are marks too
        if flags and _own_colour(r.get("color")):
            flags["color"] = _own_colour(r.get("color"))
        if flags:
            start, end = pos, pos + len(t)
            # Pull the mark in off surrounding whitespace and punctuation.
            # ...but a bracket the mark itself OPENS is kept: the book bolds `Intra Uterine
            # Devices (IUDs)` and `Figure 3.1(a)` whole (BIO12L ch03 p044), and trimming the `)`
            # left `**(IUDs**)` in the Markdown and an unbalanced mark in the JSON.
            # A mark that is WHOLLY one bracket pair, `(Psilotum)`, still loses both brackets:
            # the Markdown sets `(*Psilotum*)`, as it always has (BIO11L ch03).
            def _pairs(s):
                return s.count("(") + s.count("[") - s.count(")") - s.count("]")
            while start < end and t[start - pos] in " \t\n":
                start += 1
            while end > start and t[end - pos - 1] in " \t\n":
                end -= 1
            seg = t[start - pos:end - pos]
            whole = (len(seg) > 2 and seg[0] in "([" and seg[-1] in ")]"
                     and _pairs(seg[1:-1]) == 0)
            while start < end and t[start - pos] in _TRIM_HEAD and (whole or not (
                    t[start - pos] in "([" and _pairs(t[start - pos:end - pos]) <= 0)):
                start += 1
            # ...and an italic question keeps its `?`: the book sets `... behind the procedure?`
            # (BIO12L ch06 p004) wholly in Bookman-LightItalic, `?` included, and trimming it set
            # the `?` upright in all three deliverables.
            while end > start and t[end - pos - 1] in _TRIM_TAIL and (whole or not (
                    t[end - pos - 1] in ")]" and _pairs(t[start - pos:end - pos]) >= 0)) and not (
                    t[end - pos - 1] in "?!" and flags.get("i") and not flags.get("b")):
                end -= 1
            if end > start:
                marks.append({"from": start, "to": end, **flags})
        pos += len(t)
    text = "".join(body)
    # Merge marks that touch and carry the same flags -- one word split across two runs by a
    # colour change should be one mark, not two.
    # Join marks that the book prints as ONE italic phrase but the text layer split.
    #
    # `P. tigris` comes back as `P` and `tigris` with the abbreviating full stop between them
    # in its own unformatted run, so a +1 tolerance leaves two marks where the page prints one
    # -- the schema calls this out by name ("`P. tigris` is cut into three pieces"). The gap is
    # only closed over PUNCTUATION AND SPACE: closing it over letters would silently italicise
    # a word the book sets upright.
    merged = []
    for m in marks:
        if merged:
            prev = merged[-1]
            same = all(prev.get(k) == m.get(k) for k in ("b", "i", "sc", "sup", "sub", "color"))
            gap = text[prev["to"]:m["from"]]
            if same and len(gap) <= 2 and not gap.strip(" .,'-’"):
                prev["to"] = m["to"]
                continue
        merged.append(dict(m))
    return text, merged


# A hyphen that ENDS A PRINTED LINE: the agent's text keeps the book's line break, `four-\nchambered`.
# Only the newline is cut -- a hyphen and a SPACE is mid-line and printed so (`followed by MTP-
# this is ...`, BIO12L ch03 p046, was welded to `MTP-this` when spaces were cut too).
# `pre-\nand post-natal` keeps its break.
_LINE_END_HYPHEN = re.compile(r"(?<=[A-Za-z])-\n(?=[a-z])(?!(?:and|or|to|as|nor)\b)")


def line_end_hyphen_cuts(text):
    """Offsets of the spaces to delete after line-end hyphens in `text`, ascending."""
    return [m.start() + 1 for m in _LINE_END_HYPHEN.finditer(text or "")]


_SENT_END = re.compile(r"(?<=[.!?’”])\s+(?=[A-Z‘“(])")


def split_sentences(body):
    """[{n, from, to}] -- where each sentence starts and ends.

    The NCERT line card, Meri NCERT and PYQ mapping all work line by line, so the paragraph is
    not the smallest useful unit. Splitting on a full stop followed by a capital keeps
    `P. pardus` and `e.g.` intact, which splitting on a bare full stop does not.
    """
    if not body:
        return []
    out, start, n = [], 0, 0
    for m in _SENT_END.finditer(body):
        n += 1
        out.append({"n": n, "from": start, "to": m.start()})
        start = m.end()
    n += 1
    out.append({"n": n, "from": start, "to": len(body)})
    return out


def to_body_md(body, marks):
    """`**bold**`, `*italic*` and `<sup>`/`<sub>`, ready to hand to a model.

    Superscript and subscript are inline HTML, which CommonMark passes through. Dropping them
    made the Markdown say `20th` where the book, the JSON marks and the exact render all print
    `20<sup>th</sup>` -- and `10-2` for `10⁻²` is a different number, not a style.
    """
    # A PRINTED ASTERISK OPENING THE BODY IS TEXT: Table 4.2's footnote `*Echinodermata exhibits
    # radial or bilateral symmetry ...` (BIO11L ch04 p047). Unescaped, Markdown reads it as the
    # start of italics; escaped, it prints the star the book prints.
    def lit(i, s):
        return "\\" + s if i == 0 and s.startswith("*") else s
    if not marks:
        return lit(0, body)
    # Markdown has no colour: marks the JSON keeps apart only by `color` (a red `B` inside black
    # bold) are one emphasis here, or `**B****RE DCA P**` breaks the bold.
    joined = []
    for m in sorted(({k: v for k, v in m.items() if k != "color"} for m in marks),
                    key=lambda x: x["from"]):
        if joined and all(joined[-1].get(k) == m.get(k) for k in ("b", "i", "sc", "sup", "sub")) \
                and not body[joined[-1]["to"]:m["from"]].strip() \
                and m["from"] - joined[-1]["to"] <= 1:
            joined[-1]["to"] = max(joined[-1]["to"], m["to"])
            continue
        joined.append(dict(m))
    marks = joined
    edits = []
    for m in marks:
        a, b = m["from"], m["to"]
        if m.get("b") or m.get("i"):
            # `*` and `**` only work hugging a word. The book sets the `(` after *Chara* italic
            # across a line break (BIO11L ch03 p004), and `*Chara (*Figure 3.1a)` printed its
            # asterisks. Spaces, an opening bracket at the end and closing punctuation at the
            # start stay outside the markers; the JSON marks keep exactly what the book prints.
            while a < b and body[a] in " \t\n)]},.;:":
                a += 1
            while b > a and body[b - 1] in " \t\n([{":
                b -= 1
            if a == b:
                continue
        m = {**m, "from": a, "to": b}
        open_, close = "", ""
        if m.get("b"):
            open_ += "**"; close = "**" + close
        if m.get("i"):
            open_ += "*"; close = "*" + close
        if m.get("sup"):
            open_ += "<sup>"; close = "</sup>" + close
        if m.get("sub"):
            open_ += "<sub>"; close = "</sub>" + close
        if not open_:
            continue
        edits.append((m["from"], m["to"], open_, close))
    out, pos = [], 0
    for a, b, open_, close in sorted(edits):
        if a < pos:
            continue
        out.append(lit(pos, body[pos:a])); out.append(open_)
        out.append(lit(a, body[a:b])); out.append(close)
        pos = b
    out.append(lit(pos, body[pos:]))
    return "".join(out)


def terms_in(body, marks):
    """The bold key terms of a paragraph -- what becomes a TERM row."""
    seen, out = set(), []
    for m in marks:
        if not m.get("b"):
            continue
        t = body[m["from"]:m["to"]].strip()
        if 2 <= len(t) <= 60 and t.lower() not in seen:
            seen.add(t.lower())
            out.append(t)
    return out


# --------------------------------------------------------------------------------------------
# ROLE -> SCHEMA KIND
# --------------------------------------------------------------------------------------------
_KIND = {
    "chapter_title": "chapter_title",
    "paragraph": "para", "list": "list", "figure": "figure", "table": "table",
    "figure_caption": "figure", "side_note": "box", "section_heading": "section",
}
# Never content. See the module docstring.
# `chapter_title` is NOT furniture. The running head, the folio and the reprint line are --
# they repeat on every page and are drawn from the design. But `Chapter 1 / The Living World`
# is printed ONCE, on the chapter's own title page, and it is the first thing a reader sees.
# Excluding it meant the rendered chapter simply began on page 4 with no heading page at all.
_FURNITURE = {"page_furniture", "running_header", "page_number", "reprint_line",
              "contents_entry"}

_SECTION_RE = re.compile(r"^\s*(\d+(?:\.\d+){0,3})\s+(\S.*)$")
_UNNUMBERED = {"summary": "summary", "exercises": "exercises", "exercise": "exercises",
               "glossary": "summary"}


def classify_heading(text):
    """('1.2.2', 'Genus', 2) | (None, 'Summary', 0) | None -- number, title, depth.

    Depth is the count of dots: `1.2` is a TOPIC (depth 1), `1.2.2` a SUBTOPIC (depth 2),
    `1.2.2.1` a sub-subtopic (depth 3 -- 25 headings across 7 of the English files go this
    deep, e.g. Animal Kingdom's `4.2.11.1 Class - Cyclostomata`).
    """
    t = (text or "").strip()
    m = _SECTION_RE.match(t)
    if m:
        return m.group(1), m.group(2).strip(), m.group(1).count(".")
    key = re.sub(r"[^a-z]", "", t.lower())
    if key in _UNNUMBERED and len(t) < 40:
        return None, t.strip().title(), 0
    return None
