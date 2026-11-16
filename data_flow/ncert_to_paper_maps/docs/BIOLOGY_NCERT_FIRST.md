# Biology, NCERT-first — the prompt and the runbook

One document, two parts. **Part A** is the prompt to hand to whoever runs the papers; they
paste it into Claude Code and fill in one path. **Part B** is the runbook their Claude follows,
and the reference for anyone maintaining this afterwards.

Everything here is about **Biology questions only**. Physics and Chemistry are read, counted
and left exactly as they are: their NCERT corpus has not been extracted, so the steps that tie
a question to a printed line cannot run for them. Every script selects on
`classification.subject == "Biology"` and writes nothing outside that set.

---

# Part A — the prompt to send

> Send everything between the rules below. The receiver pastes it into Claude Code, in the
> repo, and replaces the one placeholder with their folder path.

---

I need you to run the **Biology NCERT-first** flow over my extracted NEET papers.

**Read `data_flow/ncert_to_paper_maps/docs/BIOLOGY_NCERT_FIRST.md` (Part B) before you touch
anything.** It carries the reasoning behind every rule below, the verification you are expected
to run, and a list of mistakes already made on this exact task — read that section especially,
because several of them look like success until you check properly.

## My folder

My extracted papers are here: `<PASTE YOUR FOLDER PATH OR LINK HERE>`

Each paper folder has `questions.json`, `question_paper.html` and `question_paper.md` already
built. If my folder is not laid out as `data_flow/paper_extraction/data/<year>/<paper>/`, tell
me what you found and where you would put it before moving anything.

## What is already done — do not redo it

- **Extraction is finished.** Stems, options, figures, the publisher's printed solution and its
  screenshot are already in the records. Do not re-read any PDF.
- **The exam-topic mapping is already in the records.** Do not recompute it. This flow retires
  it into an archive file and replaces it with NCERT's own chapter and printed subtopic.

## What I want done

**Biology questions only.** Physics and Chemistry must be left exactly as they are. Every
script already selects on `classification.subject == "Biology"`; do not widen that.

**Update `question_paper.html` in place** — the Biology cards inside the paper I already have.
Do not build a separate preview file. `make_biology_ncert_page.py --into-paper` does this; the
flag is not optional. The same goes for `question_paper.md` and `questions.json`: the three
deliverables I already have must end up consistent with each other.

For every Biology question, produce the same card we settled on for the five trial questions in
`2024_S1` — **q101, q106, q107, q153, q157**. Open one of those first and match it:

1. chapter and subtopic named the way **NCERT** names them, not the coaching taxonomy
2. the **exact NCERT line**, quoted character for character, with its passage id
3. directly under it, **one or two plain sentences saying what that line means** — this is what
   a student reads first, and it must settle the question
4. the full reasoning and the per-option refusals **behind a click**, not on the surface
5. **one solution, not two.** The publisher's working is a reviewer, never a source; its
   scanned image stays on the card as evidence
6. a picture only where one genuinely helps — NCERT's own figure, the booklet's figure with the
   deciding parts marked, or a drawn schematic. **No picture is a correct and common answer**
7. the printed NCERT page itself, cropped to the paragraph the quote comes from
8. **traps, categories and difficulty kept.** If my export does not already carry them, run the
   ECAT and E7 steps too — §6 of the runbook has the commands, and they must run *before* the
   page writer

## How to run it

One command drives the whole thing, per paper:

```bash
cd data_flow/ncert_to_paper_maps
python3 code/run_biology.py --paper <paper> --build
```

It prints what is done, what is next, and the exact dispatch line for every question that still
needs an agent. Send those as parallel subagents in batches, then run the command again. When
every step is in, `--write` runs the five writers.

Six agent steps per question: D1 chapter → D2 printed subtopic → D4 the exact lines → D5 the
older edition → D12 the solution → D13 the picture.

## Please do these things

- **Back up `questions.json`, `question_paper.html` and `question_paper.md` before the
  writers.** They edit in place, and several papers can no longer be re-exported.
- **Start with one paper end to end** and show it to me before running the rest. Five questions
  behaved well; a hundred will turn up cases they did not — questions with no figure, with no
  NCERT evidence, out of syllabus.
- **Run the checks in §8 and paste me the numbers**, not a summary. §9 explains why: on this
  task a check that asked a slightly wrong question passed while seven of ten quoted lines were
  missing from the page.
- **Tell me the count** before you start: how many Biology questions across my papers, and
  therefore how many agent runs. It is roughly six per question.
- If NCERT contradicts a booklet's printed answer, **do not change the printed key.** The flow
  marks the card for review and records the disagreement. Flag those to me.
- If anything in the runbook does not match what you find, **stop and tell me** rather than
  adapting around it.

---

### Before you send this

The receiving repo needs the seven JSON files listed in §4 below, **8.2 MB**, under
`data_flow/ncert_to_paper_maps/maps/`. **Nothing in the repo builds them** — they came from the
NCERT extraction — so they must be shipped with the code or the flow cannot start.

The agent briefs in `ncert_to_paper_maps/agents/` must also be copied into `.claude/agents/`,
and a newly added agent only becomes available after the Claude Code session restarts.

---

# Part B — the runbook

## 1. Why this exists

A teacher reviewed one exported paper, question by question. The same complaint came back again
and again, and it was never about a wrong fact:

> "'Phosphoglyceride' is not an NCERT Biology term. Keep the note to what NCERT says."
> "The 'choline' part goes beyond NCERT."
> "'circular, double-stranded' is more than NCERT states here."
> "Correct for the main point. 'Phosphate-choline head' is not in NCERT Biology, it is
> Chemistry level."

The facts were right every time. The **words** were not NCERT's. A student revising from the
book meets a term it never uses and cannot place it; a teacher reading the same line cannot
tell whether it is examinable.

So the order was reversed. NCERT comes **first** — chapter, printed subtopic, and the exact
lines that make the answer correct — and those lines become the vocabulary the solution is
written in. The agent's brief says it plainly: *the NCERT text in your input is not background
reading, it is your dictionary.*

## 2. The decisions behind the card, and what was rejected

Read this before changing anything. Most of these look like preferences and are not.

**One solution, not two.** Cards used to carry the publisher's working and an independent
solve. The publisher is now read by the agent **after** it has written its own, as a reviewer,
to catch something missed. Its wording is never copied and its structure never inherited. Its
scanned image stays on the card because that is evidence of what the booklet printed.

**The publisher's numbering is gone.** The review objected to solutions reading "1. 2. 3. 4.".
That numbering was ours: `solution.steps` is our reshaping of prose the publisher never
numbered — 198 of 200 questions on the trial paper. `solution.printed_lines` is what it
actually printed, and that is what survives.

**A short line in front, the reasoning behind a click.** The request was "make the solution
smaller". Measured first: explanations ran 92–110 words, while the trap block ran 180–335 —
the explanation was never the bulk. Cutting it would have brought back the original problem, so
instead `in_short` (one or two plain sentences, ≤30 words) sits directly under the quoted line
and everything else went behind a disclosure.

**`in_short` must unpack the quoted line, not float free.** The instruction was *"NCERT ki
exact line hi chahiye ya toh usko expand karke neeche thoda samjha de — this line means that."*
q106 shows why: NCERT's line begins "When **they** are flaccid…", and the quote alone leaves
"they" dangling. The short line resolves it.

**At most one mention of NCERT inside `explanation`.** The card already prints the quote and its
passage id directly above. An early draft spent four of its hundred words on "NCERT names",
"the book adds", "the book gives" — attribution crowding out biology.

**Never redraw a real biological structure.** A cell, an organ, a tissue section, an organism —
the book has drawn them correctly and a redrawing invents detail. Drawing is only for diagrams
of an *idea*: a phospholipid beside a glyceride, a chain of numbered segments, before-and-after.
For real structures: NCERT's own figure, or the booklet's figure with the deciding parts marked.

**`none` is a correct answer for the picture.** q107 is a name-to-name match; the agent
considered NCERT's Figure 2.5(c) (Agaricus), found it would settle only one of four pairs, and
chose nothing. A bad diagram is worse than no diagram.

**The AI never draws.** It writes a spec, code checks the spec, a renderer draws it. The
project's own architecture note gives the reason: *a wrong atom in a SMILES still draws a
valid-looking picture, so nobody notices.* The same is true of a mislabelled cell.

**One drawing vocabulary in the repo.** Biology drawings go through
`ncert_extractions/code/render_figure.py` — the renderer that already draws the physics
figures. An earlier hand-rolled primitive set produced a curling leaf built from two straight
lines that read as an open-topped box.

**The exam taxonomy is retired, not deleted.** It is work someone intends to map properly
later, and it cannot be recovered by rerunning anything. See §7.

**The printed key is never overwritten.** Where NCERT contradicts it, the card shows a *Marked
for review* box and the record gets `disagrees_with_printed_key`. Changing a booklet's answer
in the data is a claim no pipeline should make silently.

## 3. What is assumed to be done already

**Do not re-run extraction.** The papers arrive already extracted. Nothing in this flow
re-reads a PDF.

**Do not redo the exam-topic mapping.** It is already in the records. This flow *retires* it
(§7) rather than recomputing it.

What this flow adds is only the NCERT half.

## 4. What must be in the folder

```
data_flow/
  ncert_to_paper_maps/
    code/                      the D-step packet builders and the runner
    agents/                    the agent briefs (also copied into .claude/agents/)
    maps/                      8.2 MB of these seven — THE NCERT CORPUS. Required.
      ncert_heading_index.json   chapter sections and subtopic names   (D1, D2, D4, D12)
      paragraphs.json            passage text                          (D12)
      page_html.json             rendered pages + NCERT figures        (D13, page windows)
      older_blocks.json          the previous edition                  (D5)
      edition_pairs.json         which old chapter pairs with which new (D5)
      passage_pages.json         which page a passage sits on          (page windows)
      neet_syllabus_2026.json    the official NTA syllabus text        (syllabus label)
  paper_extraction/
    code/                      the joiners and the HTML/MD writers
    data/<year>/<paper>/       questions.json, question_paper.html, question_paper.md
```

## 5. Running one paper

```bash
cd data_flow/ncert_to_paper_maps
python3 code/run_biology.py --paper 2024_S1            # status
python3 code/run_biology.py --paper 2024_S1 --build    # + build the next step's packets
```

It prints a table and then the exact dispatch lines for the first unfinished step:

```
step  what it answers              done
D1    which NCERT chapter          100/100
D2    which printed subtopic        98/100   <-- next

next: D2 (d2-subtopic-picker) for 2 question(s)

   dispatch one subagent per line (send them in parallel, in batches):
     Use the d2-subtopic-picker subagent. Input: steps/D2/work/2024_S1.q106.runA.input.json  Output: steps/D2/out/2024_S1.q106.runA.json
```

Send those as parallel subagents, then run the command again.

| step | agent | what it answers |
|---|---|---|
| D1 | `d1-chapter-picker` | which NCERT chapter the question tests |
| D2 | `d2-subtopic-picker` | which **printed** subtopic, by the book's heading |
| D4 | `d4-evidence-quoter` | the exact line(s) that make the answer correct |
| D5 | `d5-older-line-finder` | the same fact in the previous edition, or none |
| D12 | `d12-ncert-solution-writer` | the student-facing solution, in NCERT's words |
| D13 | `d13-solution-diagram` | which picture belongs on the card, if any |

The order is enforced by the data, not by memory: D2's packet is built from D1's answer, and
D12's from D4's lines. A step cannot be built early.

An agent that returns `unsure` is not a failure. D2 answered `unsure` for the cockroach
question because the latest edition has no heading covering it — which is the correct answer,
and the syllabus step later marked that question out of syllabus on two independent sources.

### When every step is in

```bash
python3 code/run_biology.py --paper 2024_S1 --write
```

| writer | what it does |
|---|---|
| `join_ncert_map_into_export.py` | NCERT mapping + the syllabus label into `questions.json` |
| `join_ncert_card_into_html.py` | the evidence card and the rendered page into the HTML |
| `join_ncert_first_into_export.py` | the NCERT-first solution into `questions.json`, and retires what it replaces |
| `make_biology_ncert_page.py --into-paper` | rewrites the Biology cards **inside** `question_paper.html` |
| `make_biology_ncert_md.py` | rewrites the Biology sections of `question_paper.md` |

`join_ncert_card_into_html.py` refuses to run twice; pass `--replace` to rebuild its cards.

Without `--questions`, the page and markdown writers take **every Biology question that has a
D12 solution**. A question whose solution has not been written keeps the card it already has —
the old solution is never removed until the new one exists to replace it.

## 6. Categories, traps and difficulty

**Most papers in this corpus already carry them.** At the time of writing: ECAT on 17 of 19
papers, difficulty on all 19. Check before running anything — rating a question that is
already rated wastes an agent and can overwrite a reviewed answer:

```python
# per paper, from questions.json
sum(1 for q in qs if (q.get('categories') or {}).get('qtype'))     # ECAT done
sum(1 for q in qs if (q.get('difficulty') or {}).get('level'))     # difficulty done
```

Only where they are missing:

```bash
cd data_flow/paper_extraction
python3 code/build_ecat_packets_export.py --paper <paper> --apply   # -> e-category-rater
python3 code/build_e7_packets_export.py   --paper <paper> --apply   # -> e7-difficulty-rater
python3 code/join_ecat_into_export.py       --paper <paper> --apply
python3 code/join_difficulty_into_export.py --paper <paper> --apply
```

Run them **before** `make_biology_ncert_page.py`. The page transform keeps the trap blocks and
attaches the difficulty reason to the difficulty rating; if they are not there yet, the card is
built without them and re-running the transform later will not add them back without a rebuild.

### The ECAT vocabulary is fixed — do not invent values

| where | what it holds |
|---|---|
| `paper_extraction/schemas/ECAT.json` | the output shape the agent must produce |
| `paper_extraction/config/allowed_values.yaml` | every permitted value for `qtype`, `asks`, trap labels |
| `_shared/docs/question_categories/RULEBOOK.md` | what each value means, with worked examples |
| `paper_extraction/code/checks/ECAT.py` | the check that enforces both |

The axes are `qtype` (how the question is built), `asks` (what the student must produce) and
the trap (the one way a wrong option attracts), with `other_options` carrying a `role` of
`trap` or `filler`.

**A new type must be named.** The vocabulary has an escape hatch, `qtype: "new_type"`, and
exactly one question in 200 used it. When an agent takes it, it must fill
`qtype_proposed: {name, why}` — and the renderer must print that name. An earlier version threw
the name away and showed only `new_type` with a generic gloss, which tells a reader nothing. On
the trial paper that one question proposed `pair_options`, with a paragraph explaining why
neither `mcq` nor `match_columns` fits.

### How the NCERT-first card treats what ECAT produces

| row | what happens |
|---|---|
| The catch · Also pulls · Why it is wrong | **kept, unchanged** — these are the trap analysis and the review asked for them |
| `difficulty` | kept; the "why it is tricky" text is folded into the rating as its reason, instead of standing three rows away as if it were more trap commentary |
| `what makes it harder` | dropped — on the trial paper it restated the ECAT catch in different words |
| `Concept`, `Note` | dropped — these predate the NCERT-vocabulary rule and carry the exact terms the review objected to |

Those four were not preferences. Printing every field of one question side by side showed
`confusing options`, `why it is tricky`, `what makes it harder` and the ECAT catch block all
saying the same sentence — that the student mistakes lecithin for a glyceride because they
forget the phosphate. The ECAT block says it best, so it is the one kept.

## 7. What is retired, and why nothing is deleted

`join_ncert_first_into_export.py` moves these out of the record and into
`<paper>/archive/retired_fields.json`, keyed by question id:

| field | why |
|---|---|
| `classification.chapter` | the coaching chapter; NCERT's own chapter replaces it |
| `classification.subtopics` | byte-identical duplicate of the next row — same id, name and why |
| `classification.examtopicmapping_subtopics` | the exam taxonomy; the printed NCERT subtopic replaces it |
| `solution.full_text`, `.html`, `.steps` | three more copies of the publisher's working; `steps` is the numbering the review objected to |
| `categories.concept`, `.note` | these carry the exact wording the review called out ("phosphate-choline head"), because they predate the NCERT-vocabulary rule and it never reached them |

**Kept:** `solution.printed_lines`, `solution.screenshot`, `classification.ncert_subtopics`,
all of `ncert_mapping` (the page's quote windows are built from its `context` fields), all of
`categories` apart from the two fields above, `syllabus`, `difficulty`.

## 8. How to check your work

Run these and report the **numbers**, not "looks good". Each one failed at least once on this
task while the page looked fine.

**a. The page is structurally intact.** `<div>`s must balance exactly; the writer refuses to
write if they do not, but check the file you ended up with.

```python
h = open('question_paper.html', encoding='utf-8').read()
len(re.findall(r'<div\b', h)) - len(re.findall(r'</div>', h))     # must be 0
len(re.findall(r'<div class="q" id="q', h))                        # == questions in the paper
len(re.findall(r'class="sol ncert"', h))                           # == biology questions done
```

**b. Nothing else was touched.** The count of untouched `<div class="sol pub">` blocks must
equal *(all questions − biology questions rewritten)*.

**c. Every quoted NCERT line is actually visible.** Ask it the right way round: for each card,
every marked line in the evidence card must fall inside one of the paragraph windows. Do **not**
ask whether the lines inside a window fit — see §9.

**d. No line is sliced by a window edge.** Scope the scan to one window at a time: each window
embeds the whole page's markup, so a scan that runs past the end reads the *next* window's
lines against this window's coordinates and reports phantom failures.

**e. Drawn figures pass the layout check.** `render_solution_diagram.layout_problems(spec)` must
return an empty list for every `draw` decision — no label overlapping another, none outside the
canvas, every `size` a number.

**f. The three deliverables agree.** The same questions carry `ncert_first` in `questions.json`,
`class="sol ncert"` in the HTML, and `**Solution** — answer` in the markdown.

**g. Spot-read two cards in a browser.** Numbers do not catch a diagram that is correct and
unreadable.

## 9. Mistakes already made on this task

Every one of these produced output that looked right. They are listed so you do not spend the
hours again.

**A check that asked the wrong question.** The verification asked *"do the lines inside this
window fit inside it?"* and answered 4/4. The real question was *"is every marked line shown
anywhere?"* — and seven of q157's ten were not, because the crop took only the first of three
printed pages. A check that passes while the defect it exists to catch is present is worse than
no check: it buys false confidence.

**A checker that skipped what it could not measure.** The label-overlap checker caught an
exception computing a label's box and moved on. Every label in that spec carried
`size: "normal"` — a word where the renderer writes a number — so every label was skipped and
the spec passed with zero problems. Report what you cannot measure; never skip it silently.

**Cutting a block by searching for the next marker.** The first page transform ended a solution
block at the next `<div class="sol |meta|ecat|ncm`. On this paper `<div class="sol ai">` closes
*before* the classify table, which is a sibling — so the cut swallowed difficulty, steps,
confusing options, Type, Asks and Concept: exactly the fields that were meant to be kept. Find a
block's end by counting `<div` against `</div>`.

**Cropping one axis.** Cropping the NCERT page vertically kept the full 215.9mm sheet width.
That page's text column starts at `left:67.73mm`, so the paragraph sat far to the right of the
card and ran off its edge. Crop both axes, from the lines' own geometry.

**Shifting with a negative margin.** `.sheet` carries `margin:6mm auto` from the chapter
stylesheet, which a margin-based shift adds to — pushing the band down and clipping its last
line. Shift with an absolutely positioned layer instead.

**Detecting paragraphs by indent.** NCERT indents a paragraph's first line, so the obvious rule
is to look for a larger `left`. On this extraction every line of a page carried
`left:67.73mm` — the indent is leading space inside the text, not geometry. The test never
fired and a window grew to 211mm, the whole page. Use the signals that *are* in the geometry: a
`blk h` heading is a hard boundary, and a short last line ends a paragraph.

**Scoping a stylesheet without thinking about `body`.** The chapter sheets set the book's type
on `body`. Prefixing every selector with the chapter class turned that into
`.ncm-ch-x body`, which can never match inside a div — 28 dead rules per chapter, so every
embedded NCERT page rendered in the wrong font and looked, in the owner's words, "white and
weird". Map `body`/`html`/`:root` onto the wrapper element.

**`tension: 0` divided by zero.** The renderer's Catmull-Rom control points divide by
`6 * tension`, so a spec asking for straight segments lost the whole figure. It now means
straight.

**A stale agent brief.** An agent's brief is loaded into its system prompt when the session
registers it. Editing the brief does not reach an already-registered agent: two specs were
written against a superseded vocabulary for exactly that reason. The drawing vocabulary is now
generated from the renderer's own function signatures and carried inside every D13 packet, read
fresh each run. If you edit an agent brief, restart the session.

**An option that was unreachable in practice.** D13 was allowed to mark an NCERT figure, but
the packet passed only a CDN URL and the agent can only read local files — so it always fell
back to showing the figure unmarked, and said so. The packet now downloads them. When an agent
explains why it could not do something, that is usually a defect in its input.

**A blind `str.replace` with an empty search string.** A slice computed as
`s[s.index(a):s.index(b)]` came out empty because `b` appeared *before* `a` in the file;
`replace("", new)` then inserted the new text between every character and grew a 35 KB file to
49 MB. Prefer the editing tools over in-place string surgery, and check a computed slice is
non-empty before using it.

**Environment surprises.** Python here is 3.6 (`subprocess.run` has no `capture_output`) and
has no CA bundle (`urlopen` on the CDN fails `CERTIFICATE_VERIFY_FAILED` while `curl`, using
the system trust store, succeeds).

## 10. What "done" looks like, per question

```
chapter          Class XI, Chapter 9
ncert chapter    Biomolecules
ncert subtopic   9.1 How to Analyse Chemical Composition?
syllabus         In syllabus — Biology Unit 3: Cell Structure and Function

Solution                                                        answer 3
  WHAT NCERT SAYS
  [the printed page, cropped to this paragraph, the line highlighted]
  BIO11L-CH09-P09

  That line calls lecithin an example of the lipids carrying phosphorous —
  the phospholipids of the cell membrane. So lecithin is a phospholipid,
  not a glyceride.

  [the diagram, if D13 chose one]

  ▸ the full reason, and why each other option fails

  ▸ printed solution, as in the booklet

difficulty · steps · confusing options · Type · Asks
Categories — The catch / Also pulls / Why it is wrong
NCERT mapping — older NCERT, supports the answer, the page itself
```

The five trial questions are worth opening before you start, because each shows a different
case the flow has to handle:

| question | what it demonstrates |
|---|---|
| **q101** | the clean case — NCERT names the thing outright; a drawn schematic (glyceride vs phospholipid) |
| **q106** | NCERT's own Figure 6.5 marked with pins; the short line resolves a dangling "they" in the quote |
| **q107** | a match-the-columns question; evidence on **two** printed pages, so two windows; picture `none` |
| **q153** | out of syllabus — cockroach is gone from the latest edition and from the official NTA text; no quote, so `rests_on_ncert: "no"` |
| **q157** | NCERT **contradicts** the printed key; the booklet's figure marked with three pins and a legend |
