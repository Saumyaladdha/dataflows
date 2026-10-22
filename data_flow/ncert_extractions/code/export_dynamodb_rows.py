#!/usr/bin/env python3
"""Turn one extracted chapter into DynamoDB ROWS, in the shape the schema artifact specifies.

    from export_dynamodb_rows import chapter_rows
    rows = chapter_rows(layout, title)

THE MODEL: ONE TABLE, ONE PARTITION PER CHAPTER
------------------------------------------------
A chapter is one partition and its blocks sort by printed position, so the whole chapter, a
single page, or one paragraph are each a single query with nothing to reassemble afterwards.

    PK                       SK                        what it holds
    BOOK#BIO11L              CH#01                     the chapter: title, page range,
                                                       counts, measured palette
    BOOK#BIO11L#CH#01        PG#003#BL#005             one block -- paragraph, heading,
                                                       list, table, figure
    BOOK#BIO11L#CH#01        PS#BIO11L-CH01-P12        one passage, what an exam-question
                                                       quote cites
    BOOK#BIO11L#CH#01        LAYOUT#PG#003             the page's geometry: size, columns,
                                                       body type size
    PAIR#BIO11               LATEST#01                 old<->new chapter pairing, matched
                                                       on TITLE

WHY THE SORT KEY IS PRINTED POSITION AND NOT AN INDEX
-------------------------------------------------------
`PG#003#BL#005` sorts a chapter into reading order for free, so "give me page 3" is a
`begins_with(SK, "PG#003")` and "give me the chapter" is the bare partition. Nothing downstream
has to hold the chapter in memory to put it back in order.

WHY THE PAIR ROW MATCHES ON TITLE
-----------------------------------
`CLAUDE.md` records the measurement: the editions renumber. `Principles of Inheritance and
Variation` is chapter 4 of the latest Class XII Biology and chapter 5 of the older one, so
looking up the same NUMBER in the other edition fetches `Reproductive Health` and presents it
as the older edition of a genetics page -- worse than showing nothing, because the page looks
authoritative. The pair row is written only when the two titles actually match.
"""

import re

_EDITION_WORD = {"L": "latest", "O": "older", "M": "lab_manual"}
_SUBJECT_WORD = {"BIO": "biology", "CHE": "chemistry", "PHY": "physics"}

# Blocks that are page furniture carry no content a query would ever ask for, and writing them
# would put the folio and the running head into the same stream as the chapter's prose.
_SKIP_ROLES = {"page_furniture"}


def _num(v, dp=4):
    """DynamoDB numbers travel as strings, which is also how the schema artifact shows them."""
    return f"{float(v):.{dp}f}"


def _runs(el):
    """The element's runs, carrying only what is actually set.

    The schema shows `{"t": "...", "i": true}` -- a run records the flags that are TRUE and
    omits the rest, so a plain run is one key. Writing `"b": false, "i": false, "sc": false`
    on every run of a 1,100-page corpus is a lot of bytes saying nothing.
    """
    out = []
    for r in el.get("runs") or []:
        t = r.get("t", "")
        if not t:
            continue
        run = {"t": t}
        for k in ("b", "i", "sc"):
            if r.get(k):
                run[k] = True
        if r.get("script"):
            run["script"] = r["script"]
        out.append(run)
    return out


def _ids(layout):
    book = layout["book_id"]
    subject, klass, edition = book[:3], book[3:5], book[5]
    return book, _SUBJECT_WORD.get(subject, subject.lower()), int(klass), \
        _EDITION_WORD.get(edition, edition)


def chapter_rows(layout, title, passages=None):
    """Every row this chapter produces, in write order."""
    book, subject, klass, edition = _ids(layout)
    ch = layout["chapter_num"]
    part = f"BOOK#{book}#CH#{ch:02d}"
    common = {"book_id": book, "subject": subject, "class": klass,
              "edition": edition, "chapter_num": ch}
    rows = []

    folios, kinds, colours = [], {}, {}
    n_blocks = 0
    for page in layout["pages"]:
        pf = page["page_file"]
        folio = page.get("printed_page_number")
        if isinstance(folio, int):
            folios.append(folio)

        # ---- LAYOUT row: the page's own geometry -----------------------------------------
        rows.append({
            "PK": part, "SK": f"LAYOUT#PG#{pf}",
            "page_file": pf,
            "printed_page_number": folio,
            "page_side": page.get("page_side"),
            "page_width_pt": _num(page["page_width_pt"], 1),
            "page_height_pt": _num(page["page_height_pt"], 1),
            "sheet_pt": [_num(v, 1) for v in page.get("sheet_pt", [])],
            "sheet_offset_pt": [_num(v, 1) for v in page.get("sheet_offset_pt", [0, 0])],
            "body_text_size_pt": _num(page["body_text_size_pt"], 1),
            "columns": [{"name": c.get("name"), "x0": _num(c["x0"]), "x1": _num(c["x1"]),
                         "elements": c.get("elements")} for c in page.get("columns") or []],
            "margin_side": page.get("margin_side"),
            "has_text_layer": bool(page.get("has_text_layer")),
            "imprint": page.get("imprint"),
            "text_source": page.get("text_source"),
            **common,
        })

        # ---- BLOCK rows: one per printed block, sorted by printed position ---------------
        n = 0
        for el in page["elements_in_reading_order"]:
            if el["role"] in _SKIP_ROLES:
                continue
            n += 1
            n_blocks += 1
            runs = _runs(el)
            colour = (el.get("runs") or [{}])[0].get("color")
            bbox = el.get("bbox_sheet") or el["bbox"]
            row = {
                "PK": part, "SK": f"PG#{pf}#BL#{n:03d}",
                "kind": el["role"],
                "column": el.get("column"),
                "bbox": [_num(v) for v in bbox],
                "size_rel": _num(el.get("size_rel", 1.0), 2),
                "text": el.get("text", ""),
                **common,
                "page_file": pf,
            }
            if colour:
                row["color"] = colour
            if runs:
                row["runs"] = runs
            if el.get("figure_file"):
                row["figure_file"] = el["figure_file"]
            if el.get("table_text"):
                row["table_text"] = el["table_text"]
            if el.get("line_pitch_pt"):
                row["line_pitch_pt"] = _num(el["line_pitch_pt"], 2)
            # Provenance travels with the block: a consumer must be able to tell a line an
            # agent read off the page image from one lifted out of the PDF's text layer.
            if el.get("text_source"):
                row["text_source"] = el["text_source"]
            if el.get("a2_block_n") is not None:
                row["a2_block_n"] = el["a2_block_n"]
            rows.append(row)
            kinds[el["role"]] = kinds.get(el["role"], 0) + 1
            if colour:
                colours[colour] = colours.get(colour, 0) + 1

    # ---- PASSAGE rows ---------------------------------------------------------------------
    for p in passages or []:
        rows.append({"PK": part, "SK": f"PS#{p['passage_id']}", **common, **p})

    # ---- CHAPTER row ----------------------------------------------------------------------
    palette = [c for c, _ in sorted(colours.items(), key=lambda kv: -kv[1])[:6]]
    rows.append({
        "PK": f"BOOK#{book}", "SK": f"CH#{ch:02d}",
        "chapter_title": title,
        "pages": len(layout["pages"]),
        "page_range": ([min(folios), max(folios)] if folios else None),
        "blocks": n_blocks,
        "block_kinds": kinds,
        "palette": palette,
        "source_pdf": layout.get("source_pdf"),
        "design_key": layout.get("design_key"),
        "sheet_pt": [_num(v, 1) for v in (layout.get("sheet_pt") or [])],
        "text_join": layout.get("text_join"),
        **common,
    })
    return rows


def pair_row(subject, klass, latest_num, older_num, title):
    """The old<->new pairing for one chapter. Written ONLY when the titles match."""
    return {
        "PK": f"PAIR#{subject.upper()}{klass}",
        "SK": f"LATEST#{latest_num:02d}",
        "chapter_title": title,
        "latest_chapter_num": latest_num,
        "older_chapter_num": older_num,
        "matched_on": "title",
        "subject": _SUBJECT_WORD.get(subject.upper(), subject.lower()),
        "class": int(klass),
    }


def normalise_title(t):
    """Titles are compared with case, spacing and punctuation folded away -- the editions
    reset `PLANT KINGDOM` and `Plant Kingdom` differently and both mean the same chapter."""
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()
