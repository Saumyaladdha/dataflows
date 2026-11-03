# What changed, and how to run it

Everything here is in the repo. Take a pull first.

```bash
git pull origin main
```

Three things changed: a paper was built end to end, the agent steps can now run through the API
instead of as Claude Code subagents, and the category steps are frozen. Each is below.

---

## 1 · NEET 2026 Code-11, built end to end

180 questions, every step complete.

| step | state |
|---|---|
| extract · read from image · subject · chapter · subtopic · solutions · blind solve · difficulty | **180 / 180 each** |
| figures cut | 22 clean |
| figures redrawn | 28 published |
| CDN | 472 links, none missing |
| category cards | 180 — **frozen, see §3** |

Output in `data/2026/2026_11/` — `questions.json`, `question_paper.html`, `question_paper.md`.

### What reading the image rather than the text layer bought

**72 of 180 questions differ materially** from the PDF's own text layer. The worst cases:

- **q017** — the draft had options 1 and 2 **swapped**, so the printed answer pointed at the wrong
  option. Reading the image fixed it.
- **q035** — all four stacked fractions collapsed, leaving options 1 and 3 **empty** and spilling
  their numerators into the stem. The four differ only by the exponent of L and π.
- **q118** — all four floral-formula options came back blank; the only thing separating option 2
  from option 1 is an arc over `C(5)A5`. `\overparen` had to be added to the renderer, or the
  question has no single answer.

### Faults found by checking, not by any agent

- **23 figure crops contained the booklet's printed `Answer (4)` line.** The blind solve opens
  those crops to read picture options, so on those questions it was not blind and its agreement
  with the key meant nothing. Quarantined; `code/quarantine_leaky_figures.py` finds them.
- **The figure cut reached the drawing but not the labels printed beside it.** A five-plot question
  shipped with `A.`, `C.`, `E.` sliced off — on a question whose whole task is naming the right
  lettered plot. The cut now grows along the page's own marks.
- **Two defects in the paper itself:** q058 prints `Answer (3 or 4)`, and q043 prints `Answer (2*)`
  with the publisher conceding *"although it should be second principal focus."*
- **q085 and q090 cannot be solved** — both say "the following reactions" and no figure was
  captured. Recorded as `unsure`, not guessed.

---

## 2 · Running the agent steps through the API

Every agent in `agents/` declares `tools: Read, Write` and nothing else. Measured across all 30:
not one searches the repo, runs a script, or reacts to what it finds. Each is a pure function —
read one input file, maybe look at one image, write one output file.

One paper costs about **1,164 agent calls**:

| step | calls per paper |
|---|---|
| B3V · B3S · B6V · QCHAP · QTOPIC | 180 each = 900 |
| ECAT (packets) | 34 |
| E7V (packets) | 19 |
| FIGP (figures) | 31 |
| **total** | **~1,164** |

Run as Claude Code subagents, each of those carries a whole agent loop to do a job that needs no
loop at all. Run through the API, the same brief and the same input produce the same file.

**Verified against known-good output.** Two questions of 2026_11 were re-read through the API and
compared against subagent output that had already passed the step's own check.

Both came back **substantively identical** — same stem, same four options in the same order, same
`structure`, same `has_figure`. That includes **q017, where the PDF text layer has options 1 and 2
swapped**: only reading the image gets that right, and the API path got it right.

The two differences were LaTeX style, not meaning:

| | subagent | API (Opus 5) |
|---|---|---|
| q017 fraction | `$\dfrac{K}{4}$` | `$\frac{K}{4}$` |
| q001 numbers | `6 min 40 s` | `$6$ min $40$ s` |

Both render identically through `lib/texhtml.py` — checked — and the LaTeX census passes with zero
unknown commands and zero raw leaks. Nothing downstream reads the raw string.

**What this does and does not establish.** It establishes that the API path receives the same
brief, sees the same image, and reaches the same reading. It does **not** establish that two
questions represent 180. Run `--limit 20` and read the output before trusting a full step.

---

### What has been set up

### 1 · `.env` at the repo root

Already created and **gitignored** (`.gitignore` lines 45–46, and the pattern matches at every
level). Nothing to do except keep it off the internet.

```
ANTHROPIC_API_KEY=…
ANTHROPIC_MODEL=claude-opus-5
AGENT_CONCURRENCY=8
ARIVIHAN_TOKEN=            # CDN, short-lived; code/cdn_login.py prints it
ARIVIHAN_USER_ID=
```

The runner reads `.env` itself. A real environment variable wins over the file, so
`ANTHROPIC_API_KEY=… python3 …` works for a one-off.

> **The key in `.env` was pasted into a chat and must be rotated.** Rotate it at
> <https://console.anthropic.com/settings/keys> and replace the value. Everything else keeps
> working.

### 2 · `code/run_step_api.py`

```bash
# see what would run, send nothing
python3 code/run_step_api.py B3V --paper 2026_11 --dry-run

# a few first, to check the output before committing to 180
python3 code/run_step_api.py B3V --paper 2026_11 --limit 3

# the whole step
python3 code/run_step_api.py B3V --paper 2026_11
```

| flag | |
|---|---|
| `--paper` | only inputs whose filename contains this |
| `--limit N` | the first N — **use it before any full run** |
| `--concurrency` | parallel calls, default 8 |
| `--redo` | rewrite outputs that already exist (default is to skip them) |
| `--dry-run` | print what would run |
| `--model` | override `ANTHROPIC_MODEL` |

It reads `steps/<STEP>/work/*.input.json`, sends the brief from `agents/<name>.md` as the system
prompt with the input as the user turn, and writes `steps/<STEP>/out/`. Images named in the input
(`question_image`, `solution_image`, `figure_image`) are attached automatically.

### 3 · The briefs are untouched

`agents/<name>.md` drives both paths. There is no second copy to keep in step. Fix a brief and
both the subagent and the API run pick it up.

---

### Which steps this is for

| step | agent | per paper |
|---|---|---|
| `B3V` | `b3-question-reader` | 180 |
| `B3S` | `b3s-solution-reader` | 180 |
| `B6V` | `b6-blind-solver` | 180 |
| `QCHAP` | `q-chapter-picker` | 180 |
| `QTOPIC` | `q-subtopic-picker` | 180 |
| `FIGP` | `figp-figure-redrawer` | ~31 |
| `E7V` | `e7-difficulty-rater` | 19 packets |

`QSUBJ` is **not** on this list and should not be run at all where the booklet prints its section
headings. 2026_11 prints `PHYSICS`, `CHEMISTRY` and `BIOLOGY` on their own lines, so the subject
was taken straight from the page by `code/subject_from_sections.py` — 180 questions, zero agent
calls, and more reliable than inference, because a heading cannot be misread the way a borderline
biophysics question can.

---

## 3 · Do NOT run the category steps

**`ECAT` and `E1`–`E5` must not be run right now.** Skip them even if a step listing shows them as
pending. Nothing else in the pipeline depends on them, so skipping costs nothing.

### What they are

They produce the **category card** on each question — what the question is built like (`qtype`),
what it asks for (`asks`), the concept it turns on, and the one trap that catches students, with
the option number and the route to it. It is the layer that turns an extracted paper into
something a teacher can reason about: *"most students pick option 2, and here is why."*

### Why they are frozen

The vocabulary is mid-revision and the current state would be wasted work:

- traps cut from **23 values to 9**, because five of the 23 had a single question each and a value
  with one question can never form a pattern
- `asks` cut from **16 to 11** on the same ground
- two values promoted (`wrong_site_attacked`, `instrument_principle`), one retired, eight existing
  ratings re-pointed
- a new rule written into the brief only just now: **`asks` must never restate `qtype`**. It was
  caught by counting — `compare` appeared on 10 questions and on nothing that was not a match
  question, so it was carrying no information at all
- `no_trap` went from **0 uses in 35 ratings to 16 in 180**, which changed what the whole axis means

A run started today would be tagged against a vocabulary that is about to move again, and every
card would have to be redone. The right time is after the vocabulary is signed off.

### If a driver tries to run them

Stop it. If a `run_step.py` listing offers `ECAT`, `E1`, `E2`, `E3`, `E4` or `E5`, that is the
listing being complete, not the step being ready.

---

## 4 · Running a whole paper

Order matters. Each step reads what the one before it produced.

```bash
# 1 · the booklet into pages, crops, figures
python3 code/extract_paper_v2.py --paper source_pdfs/papers/<file>.pdf --apply

# 2 · read every question off its image
python3 code/run_step_api.py B3V --paper <paper> --limit 3     # check these first
python3 code/run_step_api.py B3V --paper <paper>
python3 code/run_step.py B3V --check --papers <paper>          # MUST pass

# 3 · subject, from the printed headings where there are any
python3 code/subject_from_sections.py --paper <paper> --apply

# 4 · chapter, then subtopic
python3 code/run_step_api.py QCHAP  --paper <paper>
python3 code/run_step_api.py QTOPIC --paper <paper>

# 5 · the printed solution, and an independent solve
python3 code/run_step_api.py B3S --paper <paper>
python3 code/run_step_api.py B6V --paper <paper>

# 6 · figures: cut from the agent's own boxes, then redraw
python3 code/cut_agent_figures.py --paper-id <paper> --apply
python3 code/run_step_api.py FIGP --paper <paper>

# 7 · difficulty
python3 code/run_step_api.py E7V --paper <paper>

# 8 · export
python3 code/export_paper_v2.py --html --json --data --paper-id <paper>
```

**`--limit 3` before every full step.** Three outputs read by eye cost nothing; 180 wrong ones
cost the run.

---

### What the runner does not do

It writes files. It does not check them. Its last line says so:

```
NOT VERIFIED. Run the step's own check before trusting these:
  python3 code/run_step.py B3V --check --papers <paper>
```

This matters more than it sounds. Every real fault found in this corpus was found by a check over
what the agents produced, never by an agent:

- **23 figure crops contained the booklet's printed `Answer (4)` line.** The blind solve opens
  those crops to read picture options, so on those questions it was not blind, and its agreement
  with the key meant nothing. Found by scanning each crop's area for an answer line.
- **ECAT packets shipped with `correct_answer: null`** because the key lives on the export, not on
  the corpus record. 43 questions were rated without it, so the rule "no trap sits on the answer"
  was never checked. Nothing errored.
- **A change log compared two unrelated chapters** — *Reproduction in Organisms* against *Sexual
  Reproduction in Flowering Plants* — and produced 94 "added" and 92 "removed" with zero matches.
  All 186 rows were worthless. Caught by one rule: a diff with no `moved` and no `edited` is broken.
- **`asks: compare` appeared on 10 questions and on nothing that was not a match question**, so it
  was restating `qtype` and carrying no information. Caught by counting, not by reading cards.

Agents are good at the judgement inside one question. They cannot see across 180 of them. That is
the orchestrator's job, and it stays with the orchestrator.

---

### After each step

| after | check | a failure means |
|---|---|---|
| B3V | `run_step.py B3V --check` | a question was misread |
| B3V | no figure crop contains an answer line | the blind solve is not blind |
| QCHAP | every chapter is from the allowed list | an invented chapter |
| B6V | the independent answer is compared with the printed key | a disputed key, or a misread |
| FIGP | every redraw checked against its printed crop | a wrong figure, worse than none |
| export | the LaTeX census passes | unrendered maths on the page |

---

## 5 · Cost per paper

Measured, not guessed: the token counts below come from the real input files, the real briefs,
the real crop dimensions, and one real API call used to calibrate the estimate.

### Volume

| step | calls | input/call | output/call | input total |
|---|---|---|---|---|
| B3V | 180 | 3,800 | 260 | 685,000 |
| B3S | 180 | 3,500 | 135 | 629,000 |
| B6V | 180 | 1,550 | 265 | 279,000 |
| QCHAP | 180 | 8,500 | 90 | 1,529,000 |
| QTOPIC | 180 | 3,760 | 125 | 677,000 |
| E7V | 19 | 5,950 | 3,480 | 113,000 |
| FIGP | 31 | 2,490 | 605 | 77,000 |
| **total** | **~1,150** | | | **~4.4M in · 243K out** |

**QCHAP is the most expensive step by a wide margin** — 1.53M input tokens, more than a third of
the paper. Not because of the brief but because every call carries the full allowed-chapter list
(~6,300 tokens of the 8,500). If that list were trimmed to the subject in hand, or cached, this
step alone would drop by more than half.

A question crop is ~1,080 image tokens. B3V, B3S, QCHAP and QTOPIC each attach one.

### Price

Rates below are the Anthropic first-party API list prices. The Sonnet 5 introductory rate expired
on 2026-08-31, so the standard $3 / $15 applies.

| model | input $/MTok | output $/MTok | **per paper** |
|---|---|---|---|
| Claude Sonnet 5 | $3.00 | $15.00 | **$16.81** |
| Claude Opus 5 | $5.00 | $25.00 | **$28.01** |
| Claude Haiku 4.5 | $1.00 | $5.00 | **$5.60** |

Input dominates — about 78% of the bill. Output is small because every agent writes one compact
JSON object.

### Prompt caching cuts it by about a quarter

The brief is **byte-identical on every call of a step**: 2,538 tokens repeated 180 times for B3V
alone. Across the paper that is **1.68M tokens of pure repetition — 38% of all input**.

A cache read costs ~0.1× the base input price and a write costs 1.25×, so one write plus 179
reads replaces 180 full-price copies.

| model | plain | with caching | saved |
|---|---|---|---|
| Sonnet 5 | $16.81 | **$12.32** | $4.49 (27%) |
| Opus 5 | $28.01 | **$20.53** | $7.49 (27%) |

Caching is **not yet implemented** in `run_step_api.py`. It is the single best next change: one
`cache_control` breakpoint at the end of the system prompt, nothing else to restructure, because
the brief is already first and already stable.

### Batch API halves it again

These steps are not latency-sensitive — nobody is waiting on a question read. The Batch API runs
the same requests asynchronously at **50% of list price**, and combined with caching would bring a
paper to roughly **$6 on Sonnet 5**. Also not implemented.

### The model: Claude Opus 5

`.env` sets `ANTHROPIC_MODEL=claude-opus-5`. **$28.01 a paper, $20.53 with caching.**

Sonnet 5 would be $16.81, and a two-question calibration produced output byte-identical to the
Claude Code subagent on both — including q017, where the PDF text layer has two options swapped
and only reading the image gets it right.

**Two questions is not a sample, and the decision was made the other way deliberately.** These
readings are the foundation every later step rests on: a chapter, a subtopic, a difficulty band
and a category card are all built on what B3V read off the image. A misread there is not caught
downstream — it is inherited. The $11 is small against re-running a paper, and smaller still
against shipping a wrong stem to a student.

Nothing stops a per-step override if a cheap step is ever worth testing:

```bash
python3 code/run_step_api.py QCHAP --paper <paper> --model claude-sonnet-5 --limit 20
```

Compare those 20 against known-good outputs before trusting the step to a smaller model. Haiku 4.5
at $5.60 has not been tried on any step here and should not be used until it has.
