# Inorganic Chemistry render flow

One command builds a chapter's Markdown and HTML:

```bash
python3 scripts/export_inorganic_chemistry_html.py CHE12L-ch05 \
    --pdf inputs/ncert/latest/Class_12th/Chemistry/Chapter_5.pdf \
    --title "Chemistry Class 12 (Latest NCERT) — Unit 5: Coordination Compounds"
```

`--skip-measure` reuses the existing measurement instead of re-reading the PDF; `--no-pdf` skips
the printed PDF; `--fit <n>` forces a print scale instead of measuring one.

## The three modules, and why they are separate from the other subjects

| File | Does |
|---|---|
| `scripts/inorganic_chemistry_measure.py` | Measures the printed layout **directly from the PDF's text and vector layer**. Replaces step A2L for this book. |
| `scripts/inorganic_chemistry_model.py` | Joins A2/A2S/A2B/A2N to that measurement into one **chapter model** — the single source both exports render from. |
| `scripts/export_inorganic_chemistry_html.py` | Renders the model as Markdown and as HTML, and cuts the diagram crops. |

`export_ncert_chapter_html.py` keeps every per-subject difference in `_SUBJECT_PROFILES`, keyed by
the chapter id's first three letters. That key **cannot tell organic chemistry from inorganic** —
both are `CHE` — and the `CHE` entry it holds is a copy of Biology's defaults: A4 sheet, no
furniture, no panels, continuous flow. Rendering Coordination Compounds through it gave the wrong
trim, no folio, no worked-example panels and no Summary.

Fixing that in place meant either changing `CHE` (re-rendering the organic chapters already
approved) or adding a fourth profile key the table has no way to select. Hence a separate flow. It
reuses what is genuinely shared — the A2/A2S/A2B/A2N loaders from `export_ncert_chapter_review.py`,
`lib/pdf.py`, the vendored KaTeX and Bookman — and shares **no layout code at all**, which is the
only arrangement in which a change made for this book cannot reach Biology or Physics.

## Why this book gets a better render than the scan-based flows

The latest-edition Chemistry PDFs are **not scans**. They carry a real text layer and a real
vector layer, and three things follow that no scan-based flow can do:

1. **Equations and formulae are set as text, not shipped as screenshots.** NCERT prints
   `[Co(NH3)6]3+` as five spans at three point sizes on three baselines; a flattened text layer
   loses that. The measurement keeps each span's size and baseline, so the real sub/superscript
   structure is recovered and set as live, selectable, searchable text — **328 script characters**
   across this chapter. Only genuine diagrams are images.
2. **The crops carry no watermark.** `© NCERT / not to be republished` is a separate image object
   here, repeated at the same rectangle on every page — which is how the measurement identifies it
   without being told — so it is deleted before a figure is rendered.
3. **The layout is measured, not estimated, and covers every page.** Step A2L had reached 14 of
   this chapter's 23 pages, missing p001, the opener. Reading the PDF covers all 23, exactly.

## What the book does that the other two do not

Measured off `Chapter_5.pdf`, every value read from the PDF's own objects:

- **Trim 576 × 784.8 pt** (203.2 × 276.9 mm) — not A4. Body 10.5 pt on 12.6 pt leading.
- **Marginal-heading layout.** `5.2 …` headings are set in the outer column in a script face with
  a salmon rule under them; `5.4.2 …` are inline bold grey; `(a) …` are bold-italic grey.
- **No top band.** Furniture is a **footer**: a `#fecb03` folio tab, the running header, and a
  rule running to the outer edge — mirrored per spread, and suppressed on the opener, where the
  book paints a white patch over the tab.
- **Panels**: Example `#81c4e2`, scientist/feature `#fecb03`, Summary `#c8dc5c`, each a white
  rounded panel with one coloured bar whose **side is measured per panel** — this chapter prints
  it left on three pages and right on four.
- **Objectives** `#f48480` L-bracket; **Intext Questions / Exercises** a `#f48480` margin bar;
  table headers `#f48480`; opener banner `#d0afd3` with a `#ffeda9` tab bleeding off the top.

## Outputs (all under `exports/review/`)

```
html_data/<CHAPTER>_inorganic_layout.json   the measurement
<CHAPTER>_INORGANIC.md                      the chapter as Markdown, structure named in fences
<CHAPTER>_inorg_figures/*.png               diagram crops, 300 dpi, watermark-free
html/<CHAPTER>_INORG_READER.html            the chapter as the book sets it
<CHAPTER>_INORGANIC.pdf                     the same, printed one book page per sheet
```

## The PDF, and why it is printed from its own copy

The reader and the printed sheet want different things. The reader scrolls, so it shows the
chapter at the book's own type size and lets a page be as deep as its content needs. A printed
sheet cannot: a book page running even 2% past the sheet either spills a sliver onto a second page
or, with `break-inside` honoured, pushes the whole sheet over and leaves a blank behind it.

So the fit is applied **only to the copy that gets printed**. A probe injected into that copy
reports, from the real rendering engine, how far the worst sheet overruns; the build then trims
the print copy's type and artwork together — keeping the book's own ratio between a diagram and
the prose beside it — and measures again, up to six damped passes, stopping at the largest size
where every book page still fits. The printed sheet's height is then pinned, which is safe because
the loop has already verified the content clears it.

Measured on CHE12L-ch05: the worst sheet overran by 16%, the print copy settled at 87%, and the
PDF is **23 pages for 23 book pages, no blanks**, at the book's own 203.2 × 276.9 mm trim. The
reader stays at 100%.

Four layout faults were found by chasing that page count, and each was a fidelity fault too:
NCERT sets its Summary, Exercises and Answers at 9.5pt rather than the body's 10.5; it separates
paragraphs with a measured 18pt first-line indent and no space; it runs exercise sub-options in
two and three columns rather than down the page; and a figure crop was catching the tail of the
prose line that wraps around it, printing those words twice.

The HTML does **not** print extraction gaps on the page — the reader is the book and nothing else.
Gaps are still counted by the build and named per block in the Markdown, so nothing is hidden.

## Adding another inorganic chapter

Nothing in these modules is specific to `CHE12L-ch05`. Point it at another chapter and its PDF.
What it needs is A2 output for the pages; A2S/A2B/A2N improve the result but are not required —
an untranscribed equation or box is recovered from the text layer rather than reported missing.
