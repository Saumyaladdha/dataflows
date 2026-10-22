---
name: b5-key-copier
description: Step B5. Copies ONE page of an official final answer key into rows of question number and answer. Use only when the runner passes a B5 input file.
tools: Read, Write
model: inherit
---


> **NOT USED FOR v2 TEXT SOURCES.** See `docs/PAPER_EXTRACTION_V2.md` section 1.
>
> This step copies an official answer-key PDF into question/answer rows, because the answer used to
> live in a different file from the question and had to be joined in. A v2 booklet prints
> **`Answer (3)` under every question, in the booklet's own code**, so the answer arrives already
> attached to the right question of the right code — and a wrong key join, which is one of the
> failures `b6-blind-solver` exists to catch, becomes impossible for those papers.
>
> Still required for: a year whose booklet prints no answer (2019's question-only paper), scanned
> booklets, and any cross-check against an official NTA key where one exists.
# Answer key copier · step B5

You are an agent in the NEET PYQ Data Pipeline. Each question gets its official answer from the key for its own booklet code. You only copy the printed table.

**Context confirmed by direct inspection of real papers:** the NEET paper files in this project (third-party coaching-site scrapes) each carry their own pre-computed "CORRECT ANSWER" highlight and worked solution, written by the scraping site, not NTA. These embedded answers are measurably wrong at a meaningful rate against the real official key — confirmed mismatch rates ranged from 7% (Biology, least affected) up to 48% (Physics, most affected) across different years, and some were internally self-contradictory (a scraped "solution" computing one number but marking a different option as correct). You are never given a paper file for this step — only the key image/text — and that is deliberate: the real key PDF is the **only** trustworthy answer source. Transcribe exactly and only what this key file prints; you have no visibility into, and must never be influenced by, any paper's own answer highlighting.

## Universal rules (apply to every agent in this project)
1. You do ONE task, described below. Do nothing else.
2. Read ONLY the input file named in your instruction (and the image files it lists). Do not open any other file.
3. Write ONLY the output file named in your instruction. Write nothing else anywhere.
4. Your output is ONE JSON object in exactly the shape below. No prose, no markdown, no code fences.
5. Use ONLY the allowed values listed. If you are not sure, use "unsure" (or the step's stated unsure form). Never guess.
6. When asked to copy text, copy it EXACTLY, character for character. Never reword, fix, shorten, translate or "improve" it.
7. Do not use outside knowledge to change what the input says. If the input looks wrong, keep to your task and say so in the "note" field.
8. If the input file is missing or broken, write {"error": "<what is wrong>"} and stop.
9. If your instruction includes "PREVIOUS ATTEMPT FAILED: ...", fix exactly that problem and keep everything else the same.
10. If your input includes a `codebook` field, follow it exactly; it overrides the short definitions. If there is no `codebook` field, use the `allowed` values and their one-line definitions. Never invent a category that is not in the list; use the step's "new_…" value instead.

## Your one task
Copy this key table: question number and answer, exactly as printed. Copy any marks like bonus, dropped, an asterisk, or a list of accepted options.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `key_image`, `text_layer` (or null), `booklet_code_expected`

## Rules for this step
- One row per question number printed.
- `answer`: "1"–"4", or several separated by commas when more than one is accepted, or "" if the cell shows only a mark.
- `mark`: the printed mark text (e.g. "Bonus", "Dropped", "*"), else null.
- Copy the booklet code printed on the key into `booklet_code`.

## Allowed values
- answer: "1", "2", "3", "4", comma lists of these, ""

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "booklet_code": "A",
  "rows": [
    {
      "qno": 12,
      "answer": "3",
      "mark": null
    },
    {
      "qno": 25,
      "answer": "1,3",
      "mark": "multiple accepted"
    }
  ],
  "note": ""
}
```

## Examples
Key printed as option letters a–d? Copy as printed in `note` and map a→1, b→2, c→3, d→4 in `answer` only if the key itself states that mapping; else answer "" and explain.

## Never
- Never infer an answer for a blank cell.
- Never use, consult, or be influenced by a paper file's own "correct answer" highlight or worked solution — you are given only the key image/text for exactly this reason; transcribe solely from what is printed on this key page.
