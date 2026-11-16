# Prompt: write the findings for one subject page

Run this after every branch of a subject has its `data/<branch>.json`. It writes `data/findings_<subject>.json`, which the builder needs for the page's "What stands out" and "How I checked" sections.

---

Read every `data/<branch>.json` for **{{SUBJECT}}**, together with `data/reserves_<branch>.json` and the subject's part of `04_subject_notes.md`. Then write `{{PIPELINE}}/data/findings_{{subject}}.json`:

```json
{
  "cards": [["Short title", "2–4 sentences with <b>numbers</b> and question numbers"], …],
  "how":   ["<b>Label</b>: one sentence", …],
  "next":  "One or two sentences: what the reader should check, and what can be done next."
}
```

## Cards (4 to 6)
Each card is one **pattern across the questions**, never a summary of a single question. Back every claim with question numbers and counts taken from the data. Good patterns to look for:

| Pattern | Example |
|---|---|
| How often each level came from code 11 vs code 50, and what that says about the paper | Only 3 of 45 code 11 physics questions are Hard |
| Distance from NCERT by level | Easy = NCERT copies; Hard = not an NCERT copy |
| NCERT's old answer printed as a trap | Physics Q1 (500), Physics Q11 (1.5) |
| The most common trap sources | Look-alike words, half-true options, missing factors |
| Where the hardest step is not punished by any option | Physics Q3, Q18, Q35 |
| Answer problems in the paper | Chemistry Q58 has two correct options |
| Table and bank gaps | Sorted by how much they matter; full list in `AWS_Topic_Table_Issues.md` |
| Where the SMEs and the questions file's labels disagree | Count, and the direction of the difference |

## How (5 to 8 lines)
Say where the topics, bank counts, NCERT references, answers and figures came from. Name the level rule and the SME round used. Say which questions came from code 50 and why. Point to `pipeline/` for the prompts.

## Writing rules
Same as `01_shared_rules.md` §9: very simple English, short sentences, no Hindi, and only `<b>`, `<i>`, `<sub>`, `<sup>` tags.
