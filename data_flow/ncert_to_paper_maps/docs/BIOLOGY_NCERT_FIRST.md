# Biology, NCERT-first — the prompt and the runbook

One document, two parts. **Part A** is the prompt to hand to whoever runs the papers; they
paste it into Claude Code and fill in one path. **Part B** is the runbook their Claude follows,
and the reference for anyone maintaining this.

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

**Read `data_flow/ncert_to_paper_maps/docs/BIOLOGY_NCERT_FIRST.md` (Part B) first and follow
it.** It is the runbook for exactly this task. Everything below is a summary, so you know what
is being asked before you open it.

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

For every Biology question, produce the same card we settled on for the five trial questions in
`2024_S1` — **q101, q106, q107, q153, q157**. Open one of those and match it:

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
   ECAT and E7 steps too — §5 of the runbook has the commands

All three deliverables must end up consistent: `questions.json`, `question_paper.html` and
`question_paper.md`.

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
- **Tell me the count** before you start: how many Biology questions across my papers, and
  therefore how many agent runs. It is roughly six per question.
- If NCERT contradicts a booklet's printed answer, **do not change the printed key.** The flow
  marks the card for review and records the disagreement. Flag those to me.
- If anything in the runbook does not match what you find, stop and tell me rather than
  adapting around it.

---

### Before you send this

The receiving repo needs `data_flow/ncert_to_paper_maps/maps/` — specifically the seven JSON
files listed in §3 below, **8.2 MB**. **Nothing in the repo builds them**; they came from the
NCERT extraction, so they must be shipped with the code or the flow cannot start.

The agent briefs in `ncert_to_paper_maps/agents/` must also be copied into `.claude/agents/`,
and a newly added agent only becomes available after the Claude Code session restarts.

---

# Part B — the runbook

## 1. What this flow changes, and why

A teacher reviewed one exported paper question by question. The same complaint came back again
and again, and it was never about a wrong fact:

> "'Phosphoglyceride' is not an NCERT Biology term. Keep the note to what NCERT says."
> "The 'choline' part goes beyond NCERT."
> "Correct for the main point. 'Phosphate-choline head' is not in NCERT Biology, it is
> Chemistry level."

The facts were right every time. The **words** were not NCERT's. A student revising from the
book meets a term it never uses and cannot place it; a teacher reading the same line cannot
tell whether it is examinable.

So the order was reversed. NCERT now comes **first** — chapter, printed subtopic, and the exact
lines that make the answer correct — and those lines become the vocabulary the solution is
written in. The card a student sees carries, in this order:

1. the chapter and printed subtopic, **by the book's own names**
2. the **exact NCERT line**, quoted character for character, with its passage id
3. **what that line means**, in one or two plain sentences (this is what settles the question)
4. the full reasoning and the per-option refusals, **behind a click**
5. a picture, when one genuinely helps
6. the printed page itself, cropped to the paragraph the quote comes from
7. the trap analysis and difficulty, unchanged

And one solution, not two. The publisher's working is read by the agent as a **reviewer** — to
catch anything missed — never copied. Its scanned image stays on the card as evidence.

## 2. What is assumed to be done already

**Do not re-run extraction.** The papers arrive already extracted. Nothing in this flow
re-reads a PDF.

**Do not redo the exam-topic mapping.** It is already in the records. This flow *retires* it
(see §6) rather than recomputing it.

What this flow adds is only the NCERT half.

## 3. What must be in the folder

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

## 4. Running one paper

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

## 5. Categories, traps and difficulty

If the export does not already carry them, run these too — they are separate from the NCERT
flow and have their own agents:

```bash
cd data_flow/paper_extraction
python3 code/build_ecat_packets_export.py --paper <paper> --apply   # -> e-category-rater
python3 code/build_e7_packets_export.py   --paper <paper> --apply   # -> e7-difficulty-rater
python3 code/join_ecat_into_export.py       --paper <paper> --apply
python3 code/join_difficulty_into_export.py --paper <paper> --apply
```

Run them **before** `make_biology_ncert_page.py`, because the page transform keeps the trap
blocks and attaches the difficulty reason to the difficulty rating.

## 6. What is removed, and why nothing is deleted

`join_ncert_first_into_export.py` moves these out of the record and into
`<paper>/archive/retired_fields.json`, keyed by question id:

| field | why |
|---|---|
| `classification.chapter` | the coaching chapter; NCERT's own chapter replaces it |
| `classification.subtopics` | byte-identical duplicate of the next row — same id, name and why |
| `classification.examtopicmapping_subtopics` | the exam taxonomy; the printed NCERT subtopic replaces it |
| `solution.full_text`, `.html`, `.steps` | three more copies of the publisher's working. `steps` is **our** numbering of prose the publisher never numbered — the thing the review kept objecting to |
| `categories.concept`, `.note` | these carry the exact wording the review called out ("phosphate-choline head"), because they predate the NCERT-vocabulary rule |

**Kept:** `solution.printed_lines` (what the publisher actually printed), `solution.screenshot`,
`classification.ncert_subtopics`, all of `ncert_mapping`, all of `categories` apart from the two
fields above, `syllabus`, `difficulty`.

Nothing is deleted because the exam taxonomy is work someone intends to map properly later, and
a field gone from a 1,722-question corpus cannot be recovered by rerunning anything.

A question whose solution has not been written yet **keeps the card it already has**. The old
solution is never removed until the new one exists to put in its place.

## 7. Guardrails

- **Back up before the writers.** `make_biology_ncert_page.py --into-paper` and
  `make_biology_ncert_md.py` edit the deliverables in place. Several papers in this corpus can
  no longer be re-exported — their source PDFs are not on the machine — so an in-place edit is
  the only way to change them, and a backup is the only way back.
- The page writer **refuses to write** if the document's `<div>`s come out unbalanced.
- Physics and Chemistry cards are never read or rewritten. One paper will show NCERT-first
  Biology beside ordinary Physics/Chemistry cards; that is deliberate until their NCERT corpus
  is extracted.
- `d13-solution-diagram` downloads figures the first time it sees them, into
  `steps/D13/figs/`. They are cached by name afterwards.
- The agents' briefs are loaded into their system prompt **when the session registers them**, so
  editing a brief does not reach an already-running agent. The drawing vocabulary is therefore
  also carried inside every D13 packet, read fresh on each run.

## 8. What "done" looks like, per question

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

Where NCERT **contradicts** the booklet's printed key, the card says so in a red *Marked for
review* box and the record gets `ncert_first.disagrees_with_printed_key = true`. The printed
key is never overwritten — changing a booklet's answer in the data is a claim no pipeline
should make silently.
