# questions.json — record schema v3 (`neet-pyq/question-record/v3`)

`data/<year>/<paper_code>/questions.json` holds one booklet. It is written by
`code/export_paper_v2.py --data`, which builds the records in `code/record_v3.py`.

```jsonc
{
  "schema": "neet-pyq/question-record/v3",
  "paper_code": "2017_A",
  "meta": { "year": 2017, "booklet_code": "A", "source_pdf": "...", "dpi": 200, ... },
  "render_css": "...",          // the stylesheet every `html` field assumes; include it once
  "counts": { "questions": 180, "images": 535, "images_without_cdn": 0, "drawn_figures": 37,
              "number_not_printed": [130], "flagged": {"opening_restored": [130], ...}, ... },
  "questions": [ Record, ... ]
}
```

## Record

| key | contents |
|---|---|
| `question_id`, `paper_code`, `year`, `booklet_code`, `qno` | identity |
| `flags[]` | `{code, text}`: what a reader must know before trusting the question. `opening_restored` (the booklet lost the first line; restored from a sibling code), `opening_missing` (lost, and no sibling prints it), `publisher_no_option_correct` (the printed solution says no option is correct as printed), `answers_differ` (independent solve ≠ printed answer). Empty for a clean question. Show `text` on the card. |
| `question` | the whole question; see below |
| `answer` | `publisher`, `publisher_text`, `publisher_accepted[]` (a booklet can accept two), `publisher_starred`, `publisher_line`, `ai`, `ai_text`, `ai_confidence`, `verdict` (`agree` / `differs`) |
| `solution` | the booklet's printed solution; see below |
| `ai_solution` | `steps[]`, `html`, `why`, `confidence` (solved without seeing the answer) |
| `classification` | `subject`, `stream`, `branch`, `chapter {code, name, why, confidence}`, `subtopics[{id, name, why}]`, `taxonomy_gap` |
| `difficulty` | `level`, `steps`, `step_list`, `why`, `what_makes_it_hard` |
| `source` | `pdf`, `page`, `read_from`, `note`, `text_layer_reliable`, ... |
| `status`, `pending` | per-step state; `pending` names the step still owed |

### `question`

| key | contents |
|---|---|
| `full_text` | **The whole question as one string**, in reading order: stem, `[Figure: …]`, statements, List-I / List-II, every option. Markdown with `$…$` LaTeX. A drawn structure is written as its name and SMILES. Use it for search, AI queries and plain display. |
| `html` | The same content rendered: LaTeX already HTML, images by CDN URL, match lists as a `<table>`, options as a list with their structures. Needs `render_css`. |
| `stem` | the stem text (Markdown + LaTeX) |
| `format` | `plain` / `statements` / `match` |
| `statements[]`, `list_i[]`, `list_ii[]` | `{label, text}` |
| `figures[]` | `Figure`s that belong to the question. `shows` is `question`, `options` (the panel holding the options' structures) or `question_and_options`. |
| `chemistry[]` | `Species` drawn in the question itself, not in an option |
| `options[]` | `{key, text, chemistry[Species], figure: Figure \| null}`. `text` is empty when the option is only a drawing. |
| `number_printed` | `false` when the booklet omits the question's number (2017_A q130 also lost its first line) |
| `restored_opening` | `null`, or `{text, sources[{pdf, page, qno}]}`: the words this booklet lost, copied from the same question in the exam's other booklet codes (`lib/sibling_text.py`). `stem` and `full_text` already begin with `text`. |
| `screenshot` | `Asset`: the printed question, cut from the booklet, watermark removed |

### `solution`

| key | contents |
|---|---|
| `full_text` | the steps as one string, each `[Figure: …]` at its step |
| `html` | the steps rendered, each figure (the exact printed vector copy) under its step |
| `steps[]` | the printed working, step by step (Markdown + LaTeX) |
| `figures[]` | `Figure` + `after_step` (0 = before step 1) + `kind` |
| `screenshot` | `Asset`: the **whole printed solution** as in the booklet |
| `concludes`, `complete`, `agrees_with_answer` | what the working arrives at, and whether it matches the printed answer |
| `printed_lines[]` | the text-layer draft (a cross-check, not the record) |

## Building blocks

```jsonc
Asset   = { "path": "figures_agent/2017_A/q055.png",      // relative to papers/
            "cdn_url": "https://d30lmobgrc5gb8.cloudfront.net/…/q055_26102026.png",
            "sha256": "…", "type": "image/png" }           // or image/svg+xml

Figure  = { "id": "question" | "option_2" | "solution_1",
            "text": "one line: what the figure shows",       // used in full_text
            "printed": { "png": Asset, "svg": Asset },        // EXACT copy from the booklet PDF
            "drawn": Drawn | null }                           // OUR drawing from checked data

Species = { "label": "(1)", "name": "4-methylphenol",
            "smiles": "Cc1ccc(O)cc1",                         // clean canonical SMILES (RDKit.js-ready)
            "formula": "C7H8O", "inchikey": "…",
            "name_check": "match",                            // OPSIN rebuilt the name -> same molecule
            "shown_as": "structure",                          // laid on a printed drawing; "text" = printed as a formula
            "image": Asset }                                  // our SVG of this one structure
```

### `Drawn`: chemistry (`method: "smiles"`)

Where the booklet's figure is a vector drawing (every 2017_A chemistry figure), each SMILES is laid
on a printed structure atom for atom (`code/lib/print_trace.py`: bonds, double/triple lines, labels
such as OCH₃ and NO₂ with their hydrogens), and the drawing is made on the booklet's own geometry:
`layout: "booklet"`, renderer `booklet geometry (code/lib/print_trace.py)`. It looks like the print
because it is the print's geometry; the SMILES is proven to be the printed molecule. A scanned
figure falls back to `layout: "rdkit"`.

```jsonc
{ "method": "smiles", "renderer": "booklet geometry (code/lib/print_trace.py)", "layout": "booklet",
  "status": "drawn",
  "checks": { "smiles_parse": "pass", "name_check": "4 match",
              "print_match": "4 structure(s) match the printed drawing atom for atom, 0 printed as a formula",
              "printed_text": "pass" },
  "image": Asset,                       // the whole drawing as SVG
  "kind": "structures" | "reaction" | "not_a_structure",
  "reaction_smiles": "A.B>reagent>C",
  "species": [Species],
  "scheme": [[{"text":"X (C₂H₆O)"}, {"arrow":{"above":"Cu /","below":"573 K"}}, {"text":"A"}], …],
  "draw_hints": [{ "smiles": "[OH:1]…", "orient": {...}, "explicit_h": [...], "annotations": [...] }],
  "excluded_text": [{ "text": "a, b", "why": "curved mechanism arrows" }],
  "confidence": "certain", "note": "…" }
```

### `Drawn`: physics (`method: "physics_spec"`)

```jsonc
{ "method": "physics_spec", "renderer": "code/lib/physics_figure.py", "status": "drawn",
  "checks": { "renders": "pass", "angles": "2 claimed, all within 1.5 deg",
              "netlist": "matches the drawn wires", "printed_text": "pass" },
  "image": Asset,                       // the drawing as SVG
  "spec": { "title": "…", "width": 300, "height": 220,
            "draw": [ {"kind":"resistor","from":[..],"to":[..],"id":"R1"}, {"kind":"label",…}, … ],
            "netlist": [ {"id":"R1","between":["A","B"]} ], "angles_claimed": [ … ] },
  "unreadable": [] }
```

Where the booklet's figure is a vector drawing, the spec is checked against it
(`code/lib/spec_trace.py`): every spec label must be printed in the figure, and laid on the print by
those labels the spec's lines must lie on the printed ones and cover them. A spec that passes is
drawn on the booklet's own geometry (`layout: "booklet"`, `checks.print_match` gives the label count
and the line agreement both ways), with the type the spec's labels give (italic, serif). A scanned
figure falls back to drawing the spec (`layout: "spec"`).

A browser cannot redraw a physics `spec`. Show `image`, and keep `spec` as the checked data the
image was made from.

## The three files

`data/<year>/<paper_code>/` holds `questions.json` (this schema), `question_paper.html` (the review
page) and `question_paper.md` (each question as Markdown with `$…$` LaTeX and CDN images, written by
`code/paper_md.py` from the same records). All three come from one export run.

## How to render a record

- **Show it:** inject `question.html`, then `solution.html`, with `render_css` on the page once.
- **Build your own view:** render `stem`, then `statements` or the `list_i`/`list_ii` table, then
  `figures` (`printed.svg.cdn_url`), then `options`. For an option with `chemistry`, draw `smiles`
  with RDKit.js or SmilesDrawer, or use `image.cdn_url`.
- **Search it or send it to a model:** use `question.full_text` and `solution.full_text`.

## What guarantees it

- Every `Asset` has a `cdn_url`; `counts.images_without_cdn` must be 0.
- No drawing is published unless every word printed inside the figure's box is drawn, or excluded
  with a reason (`lib/figure_text.py`; FIGC/FIGP checks).
- Every LaTeX field must pass `checks/latex_census.py` before the export writes, which rejects:
  - unknown commands;
  - raw LaTeX left in the output;
  - an unpaired `$` or unbalanced braces;
  - an empty script;
  - an unbalanced `[]`.
