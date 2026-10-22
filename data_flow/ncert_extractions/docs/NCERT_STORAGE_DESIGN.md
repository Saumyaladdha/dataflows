# Storing the NCERT extraction so it renders correctly when fetched

**What this answers:** how to keep chapters, subtopics, headings, paragraphs, figures and page
numbers so that a product can fetch them and rebuild the page faithfully — in DynamoDB plus a CDN.

Grounded in what the extraction actually holds today, measured rather than assumed:

| what | how many |
|---|---|
| blocks — heading, paragraph, list, table, equation, figure, box | **12,428** |
| passages — section-sized groupings with a heading | **3,620** |
| passage → subtopic links | **1,990** |
| figure crops | 250 |
| page images | 4,034 |

---

## 1. The one decision everything follows from: the BLOCK is the atom

A page read already produces an ordered list of typed blocks:

```json
{"n": 2, "kind": "paragraph", "page": "002", "chapter_num": 1, "book_id": "BIO11L",
 "text": "Born on 5 July 1904, in Kempten, Germany, ERNST MAYR...",
 "bbox": [...], "continues_from_previous": false}
```

**That list, in order, IS the page.** `kind` is a closed vocabulary — `heading`, `paragraph`,
`list`, `table`, `equation`, `figure`, `box` — and a renderer that switches on it reproduces the
page. So the block is what gets stored, and everything else is an index over blocks.

The **passage** (a section-sized run of blocks under one heading) is a different thing and is stored
separately: it is what evidence quotes against and what search returns. Storing only passages would
lose reading order and the table/figure boundaries; storing only blocks would lose the section a
line belongs to. Both are kept, and the passage points at its blocks.

**Do not store prose as one HTML string.** The moment the text is HTML, a typo fix means a re-render
and the structure is no longer queryable — you cannot ask "which paragraph mentions Chargaff" of a
blob. Store structure; render at read time.

---

## 2. DynamoDB: one table, composite keys

Table `ncert_content`, on-demand billing.

| item | PK | SK |
|---|---|---|
| book | `BOOK#BIO12L` | `META` |
| chapter | `BOOK#BIO12L` | `CH#04` |
| subtopic | `BOOK#BIO12L#CH#04` | `ST#BIO12-CH04-ST03` |
| **block** | `BOOK#BIO12L#CH#04` | `PG#021#BL#003` |
| **passage** | `BOOK#BIO12L#CH#04` | `PS#BIO12L-CH04-P87` |
| figure | `BOOK#BIO12L#CH#04` | `FIG#BIO12L-CH04-P87` |

The chapter is the partition for everything inside it, which is the right grain: a chapter is
~30 pages × ~8 blocks ≈ **240 items**, so one `Query` returns a whole chapter in reading order, and
`SK begins_with PG#021` returns one page. No item approaches the 400 KB limit.

### Block item

```json
{
  "PK": "BOOK#BIO12L#CH#04",
  "SK": "PG#021#BL#003",
  "kind": "paragraph",
  "order": 21003,
  "text": "Colour Blindness : It is a sex-linked recessive disorder due to defect in either red or green cone of eye...",
  "page_file": "021",
  "page_printed": 73,
  "passage_id": "BIO12L-CH04-P87",
  "section_heading": "4.8.2 Mendelian Disorders",
  "subtopic_id": "BIO12-CH04-ST08",
  "continues_from_previous": false,
  "bbox": [68, 212, 523, 338],
  "edition": "latest",
  "reprint": "2026-27",
  "extracted_by": "A2 a2-page-reader",
  "text_source": null
}
```

Three fields earn their place and are easy to leave out:

- **`order`** — `page × 1000 + block`, so a client sorts without parsing keys.
- **`page_printed` ALONGSIDE `page_file`.** The extraction numbers pages within the chapter PDF, so
  "page 021" is the 21st page of the chapter file and the **73rd page of the textbook**. An audit of
  the evidence map found every card citing the file number: a student looking up "page 21" lands in
  a different chapter. Store both and display the printed one.
- **`text_source`** — set when the text came from an A2S transcription of a table or equation rather
  than from the page read. That is the difference between a line a script verified against the book
  and one a second step reconstructed, and a reviewer needs to see it.

### Passage item

Carries the quotable text, the heading, the page span, and the block range it covers:

```json
{"PK": "BOOK#BIO12L#CH#04", "SK": "PS#BIO12L-CH04-P87",
 "passage_id": "BIO12L-CH04-P87", "section_heading": "4.8.2 Mendelian Disorders",
 "page_start_file": "021", "page_start_printed": 73, "page_end_file": "021",
 "kind": "paragraph", "blocks": ["PG#021#BL#003"], "subtopic_id": "BIO12-CH04-ST08",
 "text": "Colour Blindness : It is a sex-linked recessive disorder..."}
```

### Indexes

| GSI | PK | SK | answers |
|---|---|---|---|
| `by_subtopic` | `subtopic_id` | `order` | "render everything under Mendelian Disorders" |
| `by_passage` | `passage_id` | `order` | "give me the blocks of the passage a quote cites" |
| `by_printed_page` | `BOOK#BIO12L` | `page_printed` | "show textbook page 73" |

Only those three. Every other question this content gets asked — *which passage contains this
line?* — is a text search, and DynamoDB is the wrong tool for it; that belongs in OpenSearch or a
`pg_trgm` index fed from the same records.

---

## 3. Images: S3 behind a CDN, never in the table

Two kinds, and they are used differently:

```
s3://ncert-assets/
  figures/BIO12L/CH04/BIO12L-CH04-P87.png      # a cropped figure, shown INSIDE the rendered page
  pages/BIO12L/CH04/021.png                     # the whole page scan, shown as EVIDENCE beside a quote
  pages/BIO12L/CH04/021.webp                    # same, for the web
```

- The block or passage item stores the **key**, not a URL: `"figure_key": "figures/BIO12L/CH04/BIO12L-CH04-P87.png"`. The CDN host belongs in configuration, so the domain can change without rewriting 12,428 rows.
- Serve from CloudFront with a long `max-age` and **content-hashed paths** (`…-P87.a1b2c3.png`) so a re-extraction invalidates by changing the path rather than by purging the cache.
- Page scans are ~1 MB each and there are 4,034 of them — roughly 4 GB. Convert to WebP for the web (typically 4–6× smaller) and keep the PNG as the archival original.

---

## 4. The render contract

The renderer switches on `kind` and nothing else. This is already how `export_paper_v2` and
`build_ncert_paper_map` work, which is why it is worth fixing as a contract:

| kind | renders as | notes |
|---|---|---|
| `heading` | `<h3>` carrying the section number | `4.8.2 Mendelian Disorders` |
| `paragraph` | `<p>`, joined to the previous one when `continues_from_previous` | the flag exists because a paragraph split across a page break is ONE paragraph |
| `list` | `<ul>` / `<ol>` | NCERT's `(i) (ii)` numbering is in the text |
| `table` | `<table>` from the A2S header + rows | `text_source` says it came from A2S |
| `equation` | the transcribed form, with its printed equation number | cite as `Eq. (1.5)` |
| `figure` | `<figure>` with the CDN image and its caption | caption and labels from A2S |
| `box` | an aside — NCERT's worked examples | |

Two rules that are not obvious and both come from defects already found:

1. **Join on `continues_from_previous`.** A paragraph broken across pages must be rejoined or a
   quoted sentence spanning the break cannot be found in either half.
2. **A block whose `text` is empty and whose kind is `table`/`figure`/`equation` is ART THAT HAS NOT
   BEEN TRANSCRIBED.** Render the image and mark it as not-yet-quotable — never render an empty
   paragraph. 263 such blocks were filled by folding A2S output back in; the rest are still empty,
   and a question whose answer depends on one of them is unanswerable from the text.

---

## 5. Why not the alternatives

| option | why not |
|---|---|
| **HTML blobs in S3, one per chapter** | fast to serve, impossible to query, and a one-word fix means re-rendering a whole chapter. The evidence pipeline needs "which passage contains this exact line", which a blob cannot answer. |
| **Postgres** | honestly a good fit — the data is relational and the text search is free. Choose DynamoDB for operational reasons (no instance to run, scales to zero), not because it models this better. If a text index is needed anyway, Postgres with `pg_trgm` collapses two systems into one. |
| **Everything in one DynamoDB item per page** | a page is under 400 KB so it fits, but then a passage cannot be fetched without reading its whole page, and the subtopic index becomes impossible. |
| **Images as base64 in the table** | breaks the 400 KB limit at the first page scan and makes every read expensive. |

---

## 6. Writing it, and keeping it honest

- **Idempotent writes keyed by content.** Re-extracting a chapter must converge, not duplicate.
  `PutItem` on the composite key does this for free.
- **An extraction is a version.** Keep `reprint` (`2026-27`) and `edition` (`latest` / `older`) on
  every item. The two editions renumber their chapters — `Principles of Inheritance and Variation`
  is chapter 4 of the latest Class XII Biology and chapter 5 of the older one — so **never join the
  editions on chapter number.** Join on title, or on the A6 pairing once it has run.
- **Write a manifest row per extraction run**: `PK=RUN#2026-10-22`, with counts per book and the
  step versions. Without it, "is this chapter fully extracted?" is unanswerable after the fact, and
  a half-finished chapter looks exactly like a complete one.
- **`scripts/export_to_dynamo.py`** emits the items described here from the existing JSONL, so the
  design can be loaded and queried before anyone commits to it.

---

# Part 2 — the save plan, with formatting, measured

Part 1 stored `text` as a plain string. That is enough to QUOTE a line and not enough to RENDER it
the way NCERT prints it: italics on *Drosophila melanogaster*, bold on a defined term, green
halogens, H₂O, 10⁹. This part fixes that and states exactly what is written, where, and how.

## 2.1 The numbers that decide the design

Measured across all 71 extracted chapters:

| | |
|---|---|
| blocks | **12,428** |
| text per block | median **103** chars · mean 220 · p95 833 · max 4,377 |
| blocks per chapter | median **84** · max 862 |
| total text | **2.6 MB** raw, ~**6.8 MB** as items |
| kinds | paragraph 5,839 · equation 2,077 · heading 1,417 · list 1,373 · figure 815 · box 758 · table 146 |

Three consequences, and they are the whole reason to measure first:

1. **Nothing comes near DynamoDB's 400 KB item limit.** The largest block is 4.4 KB of text; with
   runs and metadata, call it 6 KB. There is no need to offload any text to S3.
2. **A whole chapter is one Query.** 84 items × ~570 B ≈ 48 KB median; the worst chapter, 862
   blocks, is ~490 KB — still inside a single 1 MB Query page. No pagination logic needed.
3. **The corpus is small enough to be cheap and to re-load from scratch.** 6.8 MB on-demand is
   fractions of a cent per month. Treat a full reload as routine, not as a migration.

## 2.2 The block item, with formatting

```json
{
  "PK": "BOOK#BIO12L#CH#04",
  "SK": "PG#021#BL#003",
  "order": 21003,
  "kind": "paragraph",

  "runs": [
    {"t": "Morgan worked with the tiny fruit flies, "},
    {"t": "Drosophila melanogaster", "i": true},
    {"t": ", which were found very suitable for such studies."}
  ],
  "text": "Morgan worked with the tiny fruit flies, Drosophila melanogaster, which were found very suitable for such studies.",

  "book_id": "BIO12L",
  "subject": "biology",
  "class": 12,
  "edition": "latest",
  "reprint": "2026-27",
  "chapter_num": 4,
  "page_file": "021",
  "page_printed": 73,
  "passage_id": "BIO12L-CH04-P87",
  "section_heading": "4.8.2 Mendelian Disorders",
  "subtopic_id": "BIO12-CH04-ST08",
  "continues_from_previous": false,

  "column": "body",
  "bbox": ["0.2835", "0.4522", "0.8722", "0.6800"],
  "size_rel": "1.0",
  "color": "#231f20",

  "run_source": "scripts/extract_ncert_layout.py (PDF text layer)",
  "text_source": null
}
```

**The attribute is `class`, spelled out.** `klass` only ever existed because `class` is a reserved
word in Python; it is not one in DynamoDB's item model, and the stored data should not carry a
workaround for the language that happens to write it. Python reads it as `item["class"]`, which is
legal — only a bare `item.class` would not be.

It does cost one thing, and it is worth knowing before the first query is written: **`CLASS` is on
DynamoDB's reserved-word list.** That never affects storing or reading the attribute, but any
expression naming it directly is rejected, so it must be aliased:

```python
table.query(
    KeyConditionExpression=Key("PK").eq("BOOK#BIO12L#CH#04"),
    ProjectionExpression="#cls, subject, edition, #txt",
    ExpressionAttributeNames={"#cls": "class", "#txt": "text"},   # both reserved
)
```

`text` is reserved too, and `text` is read on nearly every query — so the alias map is needed
regardless of what this one attribute is called. Naming it `class` adds nothing new to carry.

**`bbox`, `size_rel` and `color` are the printed POSITION and APPEARANCE**, which is what makes a
faithful re-render possible rather than an approximation. `bbox` is `[x0, y0, x1, y1]` as fractions
of the page, so it is independent of the DPI anything was rendered at; `column` is `side` / `body` /
`full`; `size_rel` is the element's type size over that page's own body size. They are stored as
STRINGS, not numbers: DynamoDB's `N` is decimal-exact but the SDKs round-trip it through
float/Decimal differently per language, and a `0.4522` returning as `0.45220000000000005` moves a
rendered block. These values are only ever handed to CSS -- never compared, never sorted on -- so
string is the correct type and not a compromise.

**`runs` and `text` are both stored, and that redundancy is deliberate.** `text` is the exact string
every quote in the evidence pipeline is verified against — `scripts/lib/quote_verify.py` re-finds
quoted lines in it word for word — so it must stay byte-identical to what the checker already uses.
`runs` is what renders. `text` is derived by concatenating the runs, and a write that produces a
`text` differing from the stored one is a bug, not an update.

Run keys, all optional and all absent by default:

| key | means |
|---|---|
| `i` | italic — species names, book titles, NCERT's emphasis |
| `b` | bold — a term being defined |
| `c` | colour: `"green"` (halogens) `"magenta"` (OH, NO₂, NH₂) `"cyan"` (NCERT's own headings) |
| `sc` | small caps — NCERT fakes these with two type sizes, see 2.4 |
| `sup` / `sub` | superscript / subscript run |

A block with no formatting carries **one run with just `t`**, so nothing is special-cased and the
renderer has one path.

## 2.3 How runs get filled: a fold, not a rewrite

The agents that find formatting already exist and **their output is not being used** —
`a2b-bold-marker`, `a2i-italic-marker`, `a2n-notation-fixer`, `a2l-layout-reader`. This is the same
bug as the A2S transcriptions, which sat in `steps/A2S/out/` unread until `fold_a2s_into_passages.py`
was written: a step that produces a record nothing consumes is a step that has not run.

So the order is:

```
A2   read the page image            -> blocks with plain text
A2S  transcribe tables/equations    -> fold_a2s_into_passages.py   (done)
A2B  mark bold spans        \
A2I  mark italic spans       >      -> fold_marks_into_runs.py      (to write)
A2N  fix notation (sub/sup) /
```

`fold_marks_into_runs.py` takes each block's plain text plus the marker spans and emits `runs`,
asserting that concatenating them reproduces `text` exactly. **Until it runs, every block has one
plain run and renders as it does today** — no regression, no enrichment.

## 2.4 Headings split

```json
{"kind": "heading", "level": 3, "number": "4.8.2", "title": "Mendelian Disorders",
 "runs": [{"t": "Mendelian Disorders"}], "text": "4.8.2 Mendelian Disorders"}
```

The number is separated so a renderer can set it in NCERT's style and a search can match the title
alone. `level` comes from the number's depth: `4` → 2, `4.8` → 3, `4.8.2` → 4.

## 2.5 Rendering one paragraph on its own

The API is `render_block(block) -> HTML`. Nothing in a block depends on its neighbours **except**
`continues_from_previous`, so a single paragraph renders standalone:

```python
def render_block(block, previous=None):
    if block["kind"] == "paragraph":
        runs = "".join(render_run(r) for r in block["runs"])
        if block.get("continues_from_previous") and previous is None:
            runs = "&hellip; " + runs      # say it is a continuation rather than pretend otherwise
        return '<p class="ncert">%s</p>' % runs
```

That composes upward with no second renderer: a passage is its blocks, a section is its passages, a
chapter is its sections. **One function, every level.**

The stylesheet is the NCERT look and its numbers are measured, not chosen — 19 px type, subscript
0.58 em with 0.33 em drop, bond line 1.6 px, `#009848` green, `#E80088` magenta, TeX Gyre Bonum for
Bookman Light. Ship it as `ncert.css` so notes, the app and doubt chat render identically.

## 2.6 Writing it

```
BatchWriteItem, 25 items per call  ->  12,428 blocks = 498 calls  ->  under a minute
```

- **Idempotent.** `PutItem` on `(PK, SK)` converges on re-extraction; no delete-then-insert, so a
  failed run never leaves a chapter half-empty.
- **One manifest row per run**: `PK=RUN#2026-10-22`, `SK=BOOK#BIO12L#CH#04`, with the block count,
  the step versions and which folds have been applied. Without it, "is this chapter fully
  extracted?" is unanswerable afterwards, and **a half-extracted chapter looks exactly like a
  complete one** — which is how 1,003 transcribed A2S blocks went unnoticed for weeks.
- **Never join the two editions on chapter number.** They renumber: `Principles of Inheritance and
  Variation` is chapter 4 of the latest Class XII Biology and chapter 5 of the older one. Join on
  title, or on the A6 pairing once it has run.

## 2.7 Images

Text in DynamoDB, images in S3 behind CloudFront, the item storing the **key** and never the URL so
the domain can change without rewriting 12,428 rows:

```
figures/BIO12L/CH04/BIO12L-CH04-P87.a1b2c3.png    # cropped figure, rendered inside the page
pages/BIO12L/CH04/021.a1b2c3.webp                  # page scan, shown as evidence beside a quote
```

Content-hashed paths, so a re-extraction invalidates by changing the path rather than by purging the
cache. 4,034 page scans at ~1 MB are ~4 GB as PNG; WebP typically cuts that 4–6×.

## 2.8 The order to build it

1. **`export_to_dynamo.py`** — emit today's blocks and passages as items, with one plain run each.
   Load, query, render. This proves the shape before anything depends on it.
2. **`fold_marks_into_runs.py`** — run A2B/A2I/A2N over one chapter, fold, and diff the rendered
   page against its scan.
3. **`page_printed`** — the printed number per chapter, which the evidence-map audit showed is
   missing everywhere (file page 021 is printed page 73; the offsets are +52 for Ch 4 and +78 for
   Ch 5 of Class XII Biology).
4. **`ncert.css` + `render_block`** — one renderer, shared by every product.
5. **Only then** the loader into the real table.
