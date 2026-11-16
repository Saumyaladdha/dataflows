# The prompt to hand over

Send everything between the lines below to whoever is running the papers. They paste it into
Claude Code, in the repo, and answer the one question it asks.

---

I need you to run the **Biology NCERT-first** flow over my extracted NEET papers.

**Read `data_flow/ncert_to_paper_maps/docs/BIOLOGY_NCERT_FIRST.md` first and follow it.** It is
the runbook for exactly this task. Everything below is a summary of what it says, so that you
know what you are being asked for before you open it.

## My folder

My extracted papers are here: `<PASTE YOUR FOLDER PATH OR LINK HERE>`

Each paper folder has `questions.json`, `question_paper.html` and `question_paper.md` already
built. If my folder is not laid out as `data_flow/paper_extraction/data/<year>/<paper>/`, tell
me what you found and where you would put it before moving anything.

## What is already done — do not redo it

- **Extraction is finished.** Stems, options, figures, the publisher's printed solution and its
  screenshot are already in the records. Do not re-read any PDF.
- **The exam-topic mapping is already in the records.** Do not recompute it. The flow retires
  it into an archive file and replaces it with NCERT's own chapter and printed subtopic.

## What I want done

**Biology questions only.** Physics and Chemistry must be left exactly as they are — their
NCERT corpus is not extracted, so the steps cannot run for them. Every script in the flow
already selects on `classification.subject == "Biology"`; do not widen that.

For every Biology question, produce the same card we settled on for the five trial questions in
`2024_S1` (q101, q106, q107, q153, q157) — open one of those and match it:

1. chapter and subtopic named the way **NCERT** names them, not the coaching taxonomy
2. the **exact NCERT line**, quoted character for character, with its passage id
3. directly under it, **one or two plain sentences saying what that line means** — this is what
   a student reads first, and it must settle the question
4. the full reasoning and the per-option refusals **behind a click**, not on the surface
5. **one solution, not two.** The publisher's working is a reviewer, never a source; its
   scanned image stays on the card as evidence
6. a picture only where one genuinely helps — NCERT's own figure, the booklet's figure with the
   deciding parts marked, or a drawn schematic. No picture is a correct and common answer
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

## A note for whoever sends this

The receiving repo needs `data_flow/ncert_to_paper_maps/maps/` (~9 MB). **Nothing in the repo
builds those files** — they came from the NCERT extraction — so they must be shipped with the
code or the flow cannot start.

The agent briefs in `ncert_to_paper_maps/agents/` must also be copied into `.claude/agents/`,
and a newly added agent only becomes available after the Claude Code session restarts.
