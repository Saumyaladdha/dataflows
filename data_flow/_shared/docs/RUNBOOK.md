# RUNBOOK — the whole pipeline, end to end

**If you are a Claude session opening this project for the first time, read this file and then run
`.venv/bin/python scripts/pipeline_status.py`. Between them you will know what this system is, what
has been done, and what to do next.**

This file explains what each stage MEANS and how to run it. It deliberately **never states how much
is done** — a document that quotes progress is wrong the day after it is written and a stale number
looks exactly like a fresh one. Progress is measured by the status script, every time, off disk.

---

## 0. What this project is

A checked question bank of past NEET questions. Every question is read from its own printed image,
classified into the product's taxonomy, rated for difficulty and on five fixed axes, and then tied
to **either** an exact line of NCERT **or** a concept and approach — the choice depends on the
subject, and that routing is the single most important rule here (§6).

The governing documents, in order of authority:

| file | what it governs |
|---|---|
| `docs/SPEC.md` | the full specification. When this runbook and SPEC disagree, **SPEC wins** |
| `CLAUDE.md` | the operating rules for a session: what never to do, and the measured facts behind each rule |
| `docs/PAPER_EXTRACTION_V2.md` | the paper corpus: format families, figure cutting, evidence routing |
| `docs/question_categories/RULEBOOK.md` | the E1–E5 vocabulary and what every label means |
| **this file** | how the stages fit together and how to run them |
| `scripts/pipeline_status.py` | **where we actually are**, measured, never asserted |

---

## 1. The shape of the whole thing

Two halves that meet at the end:

```
  NCERT SIDE                              PAPER SIDE
  ──────────                              ──────────
  A1  register the books                  B1  build the paper corpus from the PDFs
  A2  read each page FROM ITS IMAGE       B3V read each question FROM ITS IMAGE
  A2S transcribe tables / equations       B6V solve it blind, key withheld
  A3  split pages into passages           QSUBJ confirm the subject from the heading
  FOLD fold A2S back into passage text    QCHAP assign the chapter (list chosen BY subject)
  A5  link passages to subtopics          QTOPIC assign the subtopic
  A6  pair the old edition with the new   E7V band the difficulty
                                          ECAT rate E1–E5, in groups of similar questions
                              ╲                         ╱
                               ╲                       ╱
                      D4V  quote the NCERT line   ‖   QCA  concept + approach
                            (Biology, Organic,         (Physics, Physical Chemistry)
                             Inorganic)
                                         │
                            EXPORT  paper pages + CSVs
                            MAP     the NCERT evidence map
```

**Everything is per item.** A stage does not wait for the one before it to finish — it runs on
whatever that stage has produced. 358 questions read means every per-question stage can run on
those 358 today. The status script reports this as "ready, but capped by how far B3V has got".

---

## 2. The one pattern every stage follows

```bash
.venv/bin/python scripts/run_step.py <STEP> --list     # prints one line per item of work
# invoke the named subagent once per printed line, with exactly:
#   Use the <agent> subagent. Input: <input path>. Output: <output path>. Do nothing else.
.venv/bin/python scripts/run_step.py <STEP> --check    # repeat until it prints DONE
```

A step is defined in `config/steps.yaml`, implemented by a plugin in `scripts/*_plugin.py`
(registered in `scripts/step_plugins.py:get_plugins()`), validated against `schemas/<STEP>.json`,
and executed by the agent named in `.claude/agents/`.

**Never run two waves of the same step at once.** On 2026-10-21 a hand-sliced ECAT list was
re-dispatched twice on top of running agents; packets were written, overwritten and rewritten, and
which brief's work survived was decided by whichever agent finished last. If a brief turns out to
be wrong mid-run, **let the wave finish, then re-run**. The full account is in `CLAUDE.md`.

**Scripts make no judgements. Agents make no files they were not told to make.** That split is why
any output can be re-derived and any judgement can be re-asked.

---

## 3. The NCERT side, in detail

### A1 — register the books
One record per book: id (`BIO12L` = Biology, class 12, Latest; `…O` = Older edition), source PDF,
chapter ranges. Everything downstream is scoped by this.

### A2 — read each page from its IMAGE
`a2-page-reader` is handed a rendered page image **and** the PDF's text layer, and the rule is that
**the image is the record and the text layer is only a cross-check.** This is not a preference. A
stacked fraction has no linear text form at all — numerator, drawn bar and denominator are three
unrelated objects on different rows — so no parser recovers it, and a pipeline that trusts the text
layer silently loses every one.

Output: `blocks`, each `{n, kind, text}` where kind is `heading`, `paragraph`, `list`, `table`,
`figure`, `equation`, `box`. Running headers and footers are removed. Page images live at
`steps/A2/work/<BOOK>-ch<NN>-p<NNN>.png` and are what the evidence map shows a reader.

### A2S — transcribe the blocks a page read cannot carry
A `table`, `equation`, `figure` or `box` block is a picture on the page. `a2-special-transcriber`
reads the block crop and writes its content: a table becomes header + rows, an equation its
transcribed form **with its printed equation number**, a figure its caption and labels.

**This stage is load-bearing and was ignored for a long time, at a measured cost.** Until a block is
transcribed, the passage text built from that page **breaks off where the block sits**:

```
"Then Ohm's law states that  where the constant of proportionality R..."
"its kinetic energy K  is"
"From Eq. (3.62), we obtain,"
```

Six evidence agents could not quote `V = IR`, `K = ½mv²` or Raoult's law — not because the section
was missing, but because the formula is a picture and the picture had not been read.

### FOLD — put the transcriptions back into the passage text
`scripts/fold_a2s_into_passages.py --apply`

A2S writes to `steps/A2S/out/` and **nothing used to read it back**. The codon table was transcribed
in full while an agent searched the whole book for "lysine" and reported an NCERT gap. This folds
each transcription into its passage, matched by (book, chapter, page, kind) and ordinal within the
page — never by the passage's own `blocks` field, which is numbered per chapter while A2S items are
numbered per page, and the two disagree.

Run it **after every A2S wave**. A mismatch in count is reported and left untouched, never guessed.

### A3 — split pages into passages
`a3-passage-splitter` cuts a chapter's blocks into section-sized passages. Output lands in
`ncert/passages/<BOOK>.jsonl`, one JSON object per line:

```json
{"passage_id": "BIO12L-CH04-P87", "book_id": "BIO12L", "chapter_num": 4,
 "section_heading": "4.8.2 Mendelian Disorders", "page_start": "021", "kind": "paragraph",
 "text": "Colour Blindness : It is a sex-linked recessive disorder ..."}
```

**This file is the ground truth for every quote in the system.** `scripts/lib/quote_verify.py`
re-finds every quoted line here, word for word, whitespace-insensitively and hyphen-aware.

### A5 — link passages to subtopics
Needed by the older D3 subtopic scoping. D4V's chapter scoping does **not** need it, which is why
evidence work has proceeded with only four books linked.

### A6 — pair the old edition with the new
**Never run.** Until it is, `build_ncert_paper_map.older_chapter_numbers` matches an old chapter to
a new one **by title**, read off the chapter's own first page where NCERT prints `CHAPTER 5` and the
title beneath it — and returns **nothing** when no title matches.

This is not fussiness. **The editions renumber.** `Principles of Inheritance and Variation` is
chapter 4 of the latest Class XII Biology and chapter 5 of the older one. Looking up the same number
in the older book fetches `Reproductive Health` and presents it as the older edition of a genetics
page — worse than showing nothing, because the page looks authoritative.

---

## 4. The paper side, in detail

### B1 — build the corpus
`papers_v2/` is live; `papers/` is the frozen v1 reference (`docs/CORPUS_VERSIONS.md`). Three facts
about these booklets drive everything: **the answer is printed under every question** (so no key
join), **the figure sits in the question's own region** (so no cross-source figure matching), and
**boundaries are measured from the text layer** (so the agent path is for scanned booklets only). A
scanned booklet is refused, never OCR'd into the same corpus.

### B3V — read each question from its own image
`b3-question-reader` reads the crop at `papers_v2/crops/<paper>/q<NNN>.png` and **its output is the
record**. It reports `stem_en`, `options_en`, `statements`, `list_i`/`list_ii`, `structure`
(plain / match / statements / table / list / assertion_reason), `has_figure`, `negative_words_seen`.

**Known defect:** every crop is cut from a reprint that prints `Solution: (n)` and full working
directly beneath the options, **inside the question's own region**. So the crop shows the answer.
Four agents reported it independently. The inputs for B6V, E7V and QCA are carefully answer-free and
the image they are told to treat as the record is not — so the isolation those steps depend on is a
promise the agents are keeping, not a property of the data. Recorded in `docs/OPEN_QUESTIONS.md`;
`cut_agent_figures.py` already measures that boundary for figures and is not yet applied to crops.

### B6V — solve it blind
The key is withheld. The booklet's printed answer is the official answer (the NTA key PDFs were
removed from this flow on 2026-10-21 — `legacy/retired_2026-10-21/`), and this solve is the
independent check. Where they disagree the card says so, prominently.

### QSUBJ → QCHAP → QTOPIC — and the order is a rule
QCHAP's closed chapter list is chosen **by subject**, so a wrong subject is a wrong list and the
agent can only answer `unsure`. **QCHAP therefore refuses any question whose subject is merely a
positional guess.** Three booklets print no section heading, and in 2017 Code C **all 179**
positional guesses were wrong. Never run QCHAP ahead of QSUBJ to save a pass.

When the taxonomy has no home for a question, the agent answers `unsure` and fills
`proposed_chapter` / `proposed_topic`; `scripts/extend_taxonomy.py --apply` mints those into
`papers_v2/mappings/taxonomy_additions.json`, which is merged **on top of** the scanned index and
never written into it.

---

## 5. Difficulty (E7V) and the five axes (ECAT)

### E7V — difficulty
`e7-difficulty-rater`, schema `schemas/E7V.json`. Bands:

| band | means |
|---|---|
| **easy** | one recall or one substitution — 1 step |
| **medium** | two or three linked steps |
| **hard** | four or more, a non-obvious insight, synthesis across chapters, or distractors that are the exact result of a plausible wrong route |

`steps` is **required and is the spine**: the checker enforces that `steps_to_solve` agrees with the
band (1 / 2–3 / 4+) unless `what_makes_it_hard` names a factor that overrides the count **and**
`note` says so. Without that the step count becomes decoration and the band is a feeling with a
number beside it.

**The input carries no answer, in any form.** A rater who can see the answer reasons backwards from
it, and the route to a known answer always looks shorter than the route a candidate has to find.

### ECAT — E1 to E5
`e-category-rater`, schema `schemas/ECAT.json`, vocabulary `config/allowed_values.yaml` (v0.3,
generated from `docs/question_categories/RULEBOOK.md` — 25 axes, ~200 values).

| axis | field | what it records |
|---|---|---|
| **E1** | `question_type` | the SHAPE ON THE PAGE, decided from layout alone — `plain_mcq`, `match_list`, `assertion_reason`, `statement_set` |
| **E2** | `format` | what the ANSWER must contain — `calculate_value`, `name_or_identify`, `pick_both_parts` |
| **E3** | `content_shape` + `concept` | what is being tested, plus the actual concept in words |
| **E4** | `cognitive_demand`, `solution_structure`, `strategy_available`, `strategy_evidence` | the thinking: recall / application / calculation; single-step or multi-step-dependent; whether elimination or estimation is available, and the evidence for saying so |
| **E5** | `traps` — a list of `{label, option, route}` | one trap per option, with its **route**: the PULL that makes a wrong option attractive, not merely the error it causes |

**The item is a GROUP of up to six questions**, not one question — RULEBOOK rule 0.7 requires
similar questions to be judged against each other. v1 was tagged in paper order and gave one
match-list question `check_each_statement` and another `elimination` with no stated reason anywhere.
Packets are built by `scripts/build_ecat_packets_v2.py`, grouped by `(paper_id, subject, structure)`
— `structure` being what B3V measured about the page, the nearest honest stand-in for E1, which is
what this step is for.

Escapes: `new_type`, `new_format`, `new_shape`, `new_trap`. A label outside the vocabulary is a
finding, not an error.

---

## 6. Evidence is routed BY SUBJECT — the most important rule here

```
Biology, Organic, Inorganic  →  D4V  quote the exact NCERT line, highlighted in the page text
Physics, Physical Chemistry  →  QCA  the CONCEPT (the relation) and the APPROACH (one line)
```

**Why.** A numerical's answer is a **value** and NCERT prints **sentences**. Twelve evidence agents
on physics and physical chemistry returned `partly supported` over and over, and in every case the
thing the solution needed was a display equation (carried as an image), a constant inside a table
row, or a relation taught in another chapter — never a sentence that was absent. A part-matched
NCERT paragraph on such a question is **worse than none**, because it reads as evidence.

**And the middle case.** Biology, Organic and Inorganic content IS in NCERT, numericals included —
the law of segregation, 9:3:3:1, the 0.34 nm rise per base pair. So a *solving* question in those
subjects gets **both**: the quoted line carrying the formula or constant, **and** the approach in
words. A stated-fact question gets the quote alone; a route under "which of these is a hormone"
would be padding dressed as method.

"Solving question" is read off the question's own record — ECAT's `format` is `calculate_value`, or
`cognitive_demand` is `calculation`, or D4 recorded `derivation_steps` for a `rule_used` /
`rules_chained` link. **Never inferred from the chapter name**: Heredity asks both the probability
of an affected grandson and the name of an X-linked disorder.

The routing lives in code, not in judgement: `build_evidence_inputs.py` skips those two branches and
counts them as routed; `qca_plugin.py` offers them, scoped by the **confirmed** subject.

### D4V — what the agent may search
The input ships a ranked 15-passage shortlist, and **the shortlist is not a boundary.** Nine of the
first twelve agents reported, and three proved, that the one decisive passage was ranked out:
`BIO12L-CH04-P39` states the ABO alleles verbatim; `BIO12L-CH04-P87` gives colour blindness's 50 per
cent; `PHY12L-CH03-P66` carries the negative temperature coefficient. So the input also carries:

- `chapter_index` — every passage of the chapter with heading and page, **including the empty
  `printed_as_art` placeholders**, so an agent can tell "NCERT omits this" from "NCERT draws this";
- `search_this_file` — the book file itself, which this step alone may open;
- `older_edition_passages` — because the 2023 rationalisation cut sections a 2015 paper still asks;
- `other_books_you_may_search` — because a fact can simply live elsewhere (polysome is in Class XI
  *Cell: The Unit of Life*, not Molecular Basis).

A quote fetched that way counts exactly as much as one from the shortlist. **`scripts/checks/D4.py`
verifies the quote against the BOOK**, not against the shortlist — a stricter test, not a looser
one. `not_at_all` is only available after that search, and for Biology it is almost always the
search and not the book, because NEET Biology is written from NCERT.

**Measured:** re-running 20 weak verdicts with those fields moved **11 of 15** from
`not_at_all`/`partly` to `fully`.

---

## 7. Export, and what a reader sees

```bash
.venv/bin/python scripts/export_paper_v2.py --html --all          # one page + CSV per booklet
.venv/bin/python scripts/build_ncert_paper_map.py --finished --sample   # the evidence map
.venv/bin/python scripts/make_standalone_page.py <in.html> <out.html>   # one file, images inlined
.venv/bin/python scripts/make_artifact_bundle.py <in.html> <dir>        # publishable bundle
```

`export_paper_v2.question_card()` renders ONE question card and **both pages import it**, so the
paper export and the evidence map cannot drift apart. A card carries: the booklet crop beside what
was extracted, the printed answer against the blind solve with a verdict, the placement with its
reasons, the difficulty with its steps, and the five axes each with what the label MEANS and why
this question has it.

LaTeX is rendered **offline** by `scripts/lib/texhtml.py` — no CDN, no KaTeX, nothing fetched. A
page must stay self-contained because the shareable file inlines every asset and the artifact viewer
blocks external hosts. `greek_in_relation()` turns `lambda` into λ **only in relation fields**
(concept, approach, solving steps) — applying it to prose turned "a lambda phage vector" into "a λ
phage vector".

---

## 8. Figures we draw ourselves

`docs/FIGURE_RENDERING_PLAN.md` is the full plan; `docs/FIGURE_SPEC_REFERENCE.md` is the vocabulary.

- **Physics**: a spec of primitives → `scripts/render_figure.py` → inline SVG. Coordinates are
  mathematical (y up). Every angle the figure labels goes in `angles_claimed` and is **recomputed
  from the drawn coordinates** — this has already caught a vector drawn at 40.7° under a 60° label,
  and a "45°" triangle measuring 43.2°.
- **Organic**: a card of SMILES → `scripts/render_reaction.py` → RDKit. The renderer reports each
  molecule's formula so a wrong SMILES is caught; this is a **pilot** and is superseded by the
  Arivihan Chemistry Renderer package, which adds OPSIN (name → structure) as an independent check.
- `scripts/build_figure_compare.py` puts every redraw beside the scan it claims to reproduce.

---

## 9. Running things in parallel — what is safe and what is not

**Safe:** different steps at once; one step sharded across many agents, each with a disjoint item
list; anything read-only.

**Not safe:** two waves of the same step (§2); quarantining a step's outputs while its agents are
still writing — the older agents then write into a directory emptied for a newer run, and the newer
run's outputs are the ones that look missing.

**Rules for any fan-out brief:**
- give each agent a **disjoint** list of items, and tell it to skip an output that already exists;
- tell it to use a **scratchpad filename unique to its shard** — two QCA agents wrote a helper to
  the same path, the second clobbered the first, and the first then executed the second's script;
- tell it to write with **explicit UTF-8** — a shard under Python 3.6 truncated two files at their
  first non-ASCII character;
- after the wave, run `--check` and read what the agents reported. Several of this project's most
  valuable findings came from agents disagreeing with their own brief.

---

## 10. Where everything lives

| path | what |
|---|---|
| `.claude/agents/*.md` | every agent brief — the judgement each one makes, and why |
| `config/steps.yaml` | step definitions: item, agent, schema, check, flags, fallback |
| `config/allowed_values.yaml` | the closed vocabularies for E1–E5 |
| `schemas/*.json` | the shape of every step's output |
| `scripts/*_plugin.py` | how a step lists its work and checks it |
| `scripts/checks/*.py` | the per-step validators |
| `steps/<STEP>/work/` · `out/` | inputs built for agents · what they wrote |
| `ncert/passages/<BOOK>.jsonl` | **the ground truth every quote is verified against** |
| `ncert/figures/`, `steps/A2/work/*.png` | NCERT figure crops and page images |
| `papers_v2/papers/*.json` | the question records |
| `papers_v2/crops/<paper>/q<NNN>.png` | the printed question images |
| `papers_v2/exports/html/`, `csv/` | one page and one CSV per booklet |
| `ncert_book_mapping/` | the evidence map, its CSV, the shareable file, the PDF |
| `figures/specs/`, `cards/`, `svg/` | redrawn figures and their sources |
| `flags/flags.jsonl` | every doubt raised inside a step |
| `docs/OPEN_QUESTIONS.md` | decisions taken under uncertainty, with the default chosen |
| `docs/CORPUS_VERSIONS.md` | what was deleted or superseded, and why |
| `legacy/` | superseded outputs, kept because they are the measurement that justified a change |

---

## 11. When a requirement changes

Change these together, or the next session inherits a contradiction:

1. **The agent brief** in `.claude/agents/` — the judgement itself.
2. **The schema** in `schemas/` — the shape it must produce.
3. **The check** in `scripts/checks/` or the plugin — what makes an output acceptable.
4. **`config/steps.yaml`** — if the item, agent or flags changed.
5. **This runbook and `docs/SPEC.md`** — what the stage means.
6. **`CLAUDE.md`** — only if the change creates a rule a future session must not break, and then
   **with the measurement that justifies it**. Every rule in that file names what went wrong.

And if the change invalidates existing outputs, **move them to `legacy/<step>_superseded_<date>/`
rather than deleting them**, and log it in `docs/CORPUS_VERSIONS.md`. The 20 superseded D4V packets
are kept for exactly this reason: three of them name a passage that was proved to exist and to have
been absent from that run's shortlist, which is the measurement that justified the search fix.

---

## 12. The honest limits, so nobody over-trusts this

- **A rendered figure is never evidence.** It is a view of a question, like the crop.
- **`D4V` is not registered in `config/steps.yaml`**, so `run_step.py D4V --check` does not run its
  checker automatically. The verification that every quoted line re-finds in the book has been done
  by hand and by the agents; it is not yet enforced. **Fix this before the next evidence wave.**
- **Two papers print no answer at all** — `2019_P1` and `2020_F1`, 352 questions — so there is
  nothing for evidence to support. They need the answer extraction fixed or B6V run over them.
- **`polysome` appears in no ingested book**: BIO11L chapter 8 was never extracted. A question can
  be unanswerable from the corpus without NCERT lacking the fact.
- **Key disputes are recorded, never adjudicated.** `2016_X q053` is the clearest: NCERT states
  option 2 and the record says option 3.
