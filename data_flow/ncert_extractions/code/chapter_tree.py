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
    for r in runs or []:
        t = r.get("t", "")
        if not t:
            continue
        body.append(t)
        flags = {k: True for k in ("b", "i", "sc") if r.get(k)}
        if r.get("script"):
            flags[r["script"]] = True          # sup / sub are marks too
        if flags:
            start, end = pos, pos + len(t)
            # Pull the mark in off surrounding whitespace and punctuation.
            while start < end and t[start - pos] in _TRIM_HEAD:
                start += 1
            while end > start and t[end - pos - 1] in _TRIM_TAIL:
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
            same = all(prev.get(k) == m.get(k) for k in ("b", "i", "sc", "sup", "sub"))
            gap = text[prev["to"]:m["from"]]
            if same and len(gap) <= 2 and not gap.strip(" .,'-’"):
                prev["to"] = m["to"]
                continue
        merged.append(dict(m))
    return text, merged


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
    """`**bold**` and `*italic*`, ready to hand to a model."""
    if not marks:
        return body
    edits = []
    for m in marks:
        open_, close = "", ""
        if m.get("b"):
            open_ += "**"; close = "**" + close
        if m.get("i"):
            open_ += "*"; close = "*" + close
        if not open_:
            continue
        edits.append((m["from"], m["to"], open_, close))
    out, pos = [], 0
    for a, b, open_, close in sorted(edits):
        if a < pos:
            continue
        out.append(body[pos:a]); out.append(open_)
        out.append(body[a:b]); out.append(close)
        pos = b
    out.append(body[pos:])
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
