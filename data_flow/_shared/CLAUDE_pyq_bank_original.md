# CLAUDE.md · NEET PYQ Pipeline

## START HERE if you are new to this project

```bash
.venv/bin/python scripts/pipeline_status.py --detail   # where we ACTUALLY are, measured from disk
```

Then read **`docs/RUNBOOK.md`** — the whole flow end to end: what each stage means, how the agents
fit together, how E1-E5 and difficulty are decided, how evidence is routed by subject, how to run
things in parallel safely, and what to change when a requirement changes.

Those two are the entry point and they split the work deliberately: the runbook explains what
things MEAN and never quotes progress; the status script measures progress and never explains. A
document that states how much is done is wrong the day after it is written, and a stale number
looks exactly like a fresh one.

| if you want to know | read |
|---|---|
| where the project stands, what to run next | `scripts/pipeline_status.py` |
| how any stage works, and why | `docs/RUNBOOK.md` |
| the full specification (wins over everything) | `docs/SPEC.md` |
| what must never be done, with the measurement behind each rule | this file |
| what E1-E5 labels mean | `docs/question_categories/RULEBOOK.md` |
| the paper corpus: formats, figures, evidence routing | `docs/PAPER_EXTRACTION_V2.md` |
| drawing our own figures | `docs/FIGURE_RENDERING_PLAN.md`, `docs/FIGURE_SPEC_REFERENCE.md` |
| decisions taken under uncertainty | `docs/OPEN_QUESTIONS.md` |

Before handing this repo to anyone, run `.venv/bin/python scripts/check_portable.py`. It must say
PASS: the ten source booklets live in `inputs/papers_v2_sources/` and nothing on the live path reads
from a folder that exists on one machine only.

---

You are the main Claude Code session for this project. Your full specification is `docs/SPEC.md`. Read Sections 0–7 of it before doing anything, and the stage section before running that stage. When this file and SPEC.md seem to differ, SPEC.md wins.

## What you are building
A checked question bank of past NEET questions linked to exact NCERT lines and rules, with edition checks, repeat groups and tags. People review only at the end (Stage F).

## Your jobs
1. **Build** (milestones M0–M4 in SPEC Section 7): write every script, schema, config and test. Scripts are plain Python and make no judgements.
2. **Run** (M5 onward): for each step, run `python scripts/run_step.py <STEP> --list`, invoke the named subagent once per printed line with exactly
   `Use the <agent> subagent. Input: <input path>. Output: <output path>. Do nothing else.`
   then run `python scripts/run_step.py <STEP> --check`; repeat until it prints `DONE`.
3. **Report** after every command in the format of SPEC Section 19.

## Never
- Never decide the order of work, skip, reorder, merge or add items. The runner decides.
- Never answer a judgement yourself instead of calling its agent.
- Never edit an agent's output, never edit `inputs/`, never type a count.
- Never wait for a person inside a step. Doubt becomes a flag in `flags/flags.jsonl`.
- Never pass legacy-sheet columns, coaching material or answer keys to agents that must not see them (B6 never sees the key; B6 and D7 never see coaching material).
- Never treat the analysis's list of removed NCERT chapters as evidence; only Stage A's change log counts.
- Never release a chapter; only `export_tables.py` does, after a sign-off row in `review/releases.csv`.

## When unsure
Choose the safest reading that keeps every rule, continue, and record the question and your default in `docs/OPEN_QUESTIONS.md`.

## Paper extraction (read before any Stage B work)
The paper corpus was rebuilt in 2026-10 from `Saumya_NEET_work/NEW`. Two documents govern it:
- `docs/PAPER_EXTRACTION_V2.md` — the format families, the page-by-page procedure, how figures are
  cut, and the four tests that decide figure-or-not. Section 7 is what makes the flow survive a new
  publisher's layout.
- `docs/CORPUS_VERSIONS.md` — `papers/` is the frozen v1 reference; `papers_v2/` is live.

Three things changed that affect which steps to run: the answer is **printed under every question**
(so B5's key join is not needed for these papers), the figure is **in the question's own region**
(so B9's cross-source figure matching is not needed, and B9S became the standard check rather than a
rescue), and boundaries are **measured from the text layer** (so B2's agent is the path for scanned
booklets only). A scanned booklet is refused, never OCR'd into the same corpus.

**The classification chain runs after export, and its ORDER IS A RULE, not a convention:**

    QSUBJ  ->  QCHAP  ->  QTOPIC        then  E7V (difficulty)  and  ECAT (E1-E5)

                                       then, BY SUBJECT:  D4V (NCERT line)  or  QCA (concept)

QCHAP's closed chapter list is chosen BY SUBJECT, so a wrong subject is a wrong list and the agent
can only answer `unsure`. QCHAP therefore **refuses** any question whose subject is merely a
positional guess. Three booklets print no section heading at all, and in 2017 Code-C all 179
positional guesses were wrong. Never run QCHAP ahead of QSUBJ to save a pass.

**Evidence is routed BY SUBJECT, and the routing is in code, not in judgement (2026-10-21):**

    Biology, Organic, Inorganic   ->  D4V   quote the exact NCERT line, highlighted in the page text
    Physics, Physical Chemistry   ->  QCA   the CONCEPT (the relation) and the APPROACH (one line)

A numerical's answer is a VALUE and NCERT prints SENTENCES. Twelve evidence agents on physics and
physical chemistry returned `partly supported` over and over, and in every case the thing the
solution needed was a display equation (carried as an image, so missing from the passage text), a
constant in a table row, or a relation from another chapter -- not a sentence that was absent. A
part-matched NCERT paragraph on such a question is worse than none, because it reads as evidence.

`build_evidence_inputs.py` skips those two branches and counts them as routed; `qca_plugin.py`
offers them, scoped by the CONFIRMED subject and (for chemistry) by QCHAP's branch, never by the
positional guess. Organic chemistry stays with D4V on purpose: its reactions are printed as
equations and are quoted like any other evidence.

**The NTA key PDFs were removed from this flow on 2026-10-21** (`legacy/retired_2026-10-21/`). The
booklet's own printed answer is the official answer; the independent check is `b6-blind-solver`. Do
not re-introduce a key join without first proving the PDF was published for the exact booklet code.

When the taxonomy has no home for a question, the agent answers `unsure` and fills
`proposed_chapter` / `proposed_topic`; `scripts/extend_taxonomy.py --apply` mints those into
`papers_v2/mappings/taxonomy_additions.json`, which is merged ON TOP of the scanned index and never
written into it.


## Never run two waves of the same step at once

`run_step.py <STEP> --list` then one agent per printed line then `--check` is not a style; it is what
keeps two agents off the same file. On 2026-10-21 I sliced ECAT's list by hand and re-dispatched
twice on top of still-running agents, and the result was three waves writing `steps/ECAT/out/`
together: packets written, overwritten, and written again, with agents reporting "six of my nine
packets were overwritten after I wrote them". Nothing was corrupted -- no duplicated question ids,
every axis filled -- but which brief's work survived was decided by whichever agent finished last,
which is not a thing anyone can review.

If a brief turns out to be wrong mid-run, **let the wave finish, then re-run**. Quarantining outputs
while their authors are still writing is what caused the collisions: the older agents then wrote
into a directory that had been emptied for a newer run, so the newer run's outputs were the ones
that looked missing.

## Three things measured on 2026-10-21 that every future wave needs

**The editions renumber, so never carry a chapter number across them.** `Principles of Inheritance
and Variation` is chapter 4 of the latest Class XII Biology and chapter 5 of the older one. Looking
up the same number in the older book fetches `Reproductive Health` and presents it as the older
edition of a genetics page -- which is worse than showing nothing, because the page looks
authoritative. `build_ncert_paper_map.older_chapter_numbers` matches BY TITLE, read off the
chapter's own first page where NCERT prints `CHAPTER 5` and the title, and returns NOTHING when no
title matches. Old↔new pairing (step A6) has still never run; this is the stopgap until it does.

**The question crops contain the publisher's printed solution.** Every crop is cut from a Vedantu
reprint that prints `Solution: (n)` and full working directly beneath the options, inside the
question's own region. Four agents reported it independently. The inputs for B6V, E7V and QCA are
carefully answer-free, and the image they are told to treat as the record is not -- so the isolation
those steps depend on is a promise the agents are keeping, not a property of the data.
`cut_agent_figures.py` already measures that boundary for figures (`solution_tops`); it is not being
applied to the question crop. Recorded in `docs/OPEN_QUESTIONS.md`.

**Shard agents must namespace their scratchpad filenames.** Two QCA agents wrote a helper to the
same scratchpad path; the second clobbered the first, and the first then executed the second's
script and wrote part of another shard's range before dying on an encoding error. Nothing was
corrupted, but the run became unattributable. Any brief that fans out N agents over a list must
tell them to use a filename unique to their shard, and to write with explicit UTF-8 -- a shard
writing under Python 3.6 truncated two files at their first non-ASCII character.

## Where things are
Agents `.claude/agents/` · commands `.claude/commands/` · step definitions `config/steps.yaml` · cascade `config/cascade.yaml` · allowed values `config/allowed_values.yaml` · outputs `steps/<STEP>/out/` · current question records `papers/records/` · flags `flags/flags.jsonl` · review `review/` · final tables `data/` · log `run_log.csv`.
