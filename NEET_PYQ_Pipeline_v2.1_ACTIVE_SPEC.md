# NEET PYQ Pipeline · Build and Run Specification for Claude Code

**Audience:** Claude Code (the main session and its subagents). People can read it too, but it is written as instructions for you, Claude Code.
**Version:** v2.1 · 8 October 2026
**Owner:** Ekta Rajput
**Status:** nothing is built yet. You will build it, then run it.

## Contents

0. How to use this document · 1. Mission · 2. What we learned from real papers · 3. Core concepts · 4. Rules you must never break · 5. Architecture · 6. Data contracts · 7. Build plan (M0–M8) · 8. Stage 0 · 9. Stage A · 10. Stage B · 11. Stage C · 12. Stage D · 13. Stage E · 14. Stage F · 15. Cascade map · 16. Flag catalogue · 17. Allowed values · 18. Runbook · 19. Reporting · 20. Open decisions · Appendix A `CLAUDE.md` · Appendix B agent files · Appendix C slash commands · Appendix D config files · Appendix E tests

---

## 0. How to use this document

**You are Claude Code working in the project folder `pyq_bank/`.** This document is your complete specification. It tells you what to build, in what order, how every step works, what every file looks like, and when something counts as done.

### 0.1 Reading order

1. Sections 1–4: what we are building, what we learned from real papers, the concepts, and the rules you must never break. Read these fully before writing any code.
2. Sections 5–7: architecture, data contracts, and the build plan (milestones M0–M8). Follow the milestones in order.
3. Sections 8–14: one section per stage (0, A, B, C, D, E, F). Each step has the same template. Implement exactly what the step says.
4. Sections 15–20: cascade map, flags, allowed values, runbook, reporting, open decisions.
5. Appendices: the exact text of `CLAUDE.md`, every agent file, every slash command, the config files and the test list. Create these files from the appendices word for word, then extend the configs as the step sections say.

### 0.2 How to read the step template

Every step in Sections 8–14 uses this layout:

| Field | Meaning |
|---|---|
| **Purpose** | Why the step exists, in one or two sentences |
| **Item** | What one unit of work is (a page, a question, a pair…) and how many agent runs it gets |
| **Worker** | `SCRIPT` (you write Python, no judgement), `AGENT` (a subagent makes one judgement), or both |
| **Reads** | Exact files and fields. Pass an agent **only** these fields |
| **Procedure** | Numbered actions. Each says who does it: SCRIPT or AGENT |
| **Agent output** | The JSON the agent must write. The full prompt is in Appendix B |
| **Checks** | What the check script verifies. Every check must exist as code |
| **On failure** | The fallback chain for this step and the flags it raises |
| **Writes** | Exact output files |
| **Done when** | The acceptance condition for this step on a run |
| **Pitfalls** | What usually goes wrong, including problems seen in the real data |

### 0.3 When something is unclear

- **Do not stop and wait for a person.** People act only in Stage F.
- Pick the safest reading that keeps every rule in Section 4. Write the question and your chosen default in `docs/OPEN_QUESTIONS.md` (create it if missing) with the date, the section number, and what you did.
- If two parts of this document seem to disagree, the more specific one wins (a step section beats a general section), and Section 4 beats everything.
- Never invent data, quotes, answers, categories or codebooks.

### 0.4 What "Claude Code does everything" means here

- **You build** every script, schema, config and test from this document (milestones M1–M3).
- **You run** the pipeline by calling the runner script, which tells you exactly which subagent to call on which file (milestones M4 onward).
- **Subagents** (files in `.claude/agents/`) make one small judgement each, on one input file, and write one JSON output.
- **Scripts** do everything else: reading PDFs, cutting, joining, comparing, counting, searching, validating, logging.
- **People** review everything at the end, in Stage F, and only there.

---

## 1. Mission

Build a question bank of every past NEET question (first scope: NEET 2016–2026, every sitting) in Physics, Chemistry and Biology, where every question:

1. is copied **exactly** (text, options, maths in LaTeX, figures cropped from the official PDF), with an answer from the **official final key**;
2. is linked to an **NCERT chapter, subtopic, and the exact NCERT line(s) or rule(s)** that prove the answer, verified word for word by a script;
3. knows whether that answer still holds in **today's NCERT** (reprint 2026-27) and keeps both answers if an edition change altered it;
4. is linked to **repeats** of the same fact or problem in other years;
5. is tagged with **how** it was asked: question type, format, content shape, thinking, traps, and six descriptive tags.

The bank feeds **Feature 1 of the NCERT Test Generator**: a student uploads an NCERT page, the system finds the page's subtopic, and plans a test from real past questions on that subtopic, in the formats NEET uses today.

### 1.1 Success criteria

| Criterion | Target |
|---|---|
| Text exact after double reading | ≥ 99% (measured on the gold set) |
| Every answer joined to the right key | 100% |
| Chapter correct | ≥ 98% |
| Subtopic correct | ≥ 95% |
| Every NCERT quote found word for word in the named edition | 100% (script) |
| Right evidence passage | ≥ 95% |
| No known repeat missed | 0 missed on the gold set |
| Thinking tag agreement with faculty | ≥ 85% per subject |
| Counts | computed by script, never typed; totals match 100% |
| Release | per chapter, only after Stage F empties that chapter's queue and Ekta signs off |

---

## 2. What we learned from real papers (and what it means for you)

Ten real papers were analysed before this spec was written: NEET 2013, AIPMT 2014, AIPMT 2015, NEET 2016 Phase I and II, NEET 2017, 2018, 2019, NEET 2026 (3 May, cancelled) and NEET 2026 (21 June re-exam). 1,800 questions in total, about 650 read in full. The owner also has these as spreadsheets ("legacy sheets"). Each finding below ends with **what you must do because of it**.

Question IDs like `2019#44` mean "row 44 of the 2019 legacy sheet". They are used only as examples here; the bank uses its own IDs (Section 6).

### 2.1 The paper changed shape between 2019 and 2026

In Biology, plain one-line questions were 80–93% of every paper from 2013 to 2019, and 38–39% of both 2026 papers. Their place went to: Match List-I/List-II (up to 22%), lettered statements A–E with "Choose the correct answer from the options given below" (up to 19%), arrange-in-order (up to 13%), fill-in-the-blank "____" (up to 18% in June 2026), Statement I/II (9%), and Assertion–Reason (6%). Match lists also spread to Physics and Chemistry in 2026. Constants are given in the stem far more often (12–13 per paper vs 1–6 earlier).

**What you must do:** implement the full v0.1 question-type and format lists (Section 17). Make the E1 pattern rules recognise every structure above. Parse statements A–E, List-I/List-II rows (including five-item lists A–E vs I–V), and match codes as structured fields in B3, not as free text.

**Update (2026-10-09, from a 10-paper sample spanning 2016–2025, one full paper per year, ~500 questions sampled across all three subjects — see Section 2.8):** match-lists, Assertion–Reason, Statement I/II and lettered A–E combination questions are **not a 2026-only phenomenon**. The 2024 MAIN paper alone already shows ~10% match-the-lists questions, 8 Assertion–Reason, 8 Statement I/II and 5 lettered-combination questions, spread across Physics, Chemistry **and** Biology, not concentrated in Biology. Treat the "2019→2026" framing above as the end-points of a gradual shift that was already well underway by 2024, not a sudden change at 2026.

### 2.2 The legacy tags are not usable

The legacy "Question Type" column combines a structure with a thinking word, and the thinking word depends on the **subject**, not the question: no Biology question is ever "Conceptual", no Physics or Chemistry question is ever "Factual". A rule-based check of all 1,800 found 367 clear contradictions (275 calculations labelled "Conceptual/Analytical"; 59 match questions labelled "Statement-Based"; 20 "Diagram-Based" with no figure; 16 "Numerical" with no calculation; 6 "Assertion-Reason" with no assertion) and 311 questions whose real structure has no legacy value at all. The legacy chapter list is a coaching list ("Modern Physics", "Mole Concept", "Capacitor", "Kinematics", "Salt Analysis"), with colliding chapter numbers, and many 2018–2019 questions are filed in the wrong chapter (about 1 in 5 Biology questions sampled).

**What you must do:** never pass any legacy column to any agent; never use it to set any field. Store it only as `legacy_chapter`, `legacy_topic`, `legacy_question_type` for comparison in Stage F (Section 14.2). D1 maps to **NCERT's** chapter list built in Stage A.

### 2.3 Deleted NCERT content is a measurable share of old papers

6–10% of every 2013–2019 paper (10–18 questions per paper) comes from chapters that the analysis believes were removed in NCERT's rationalisation: Transport in Plants, Mineral Nutrition, Digestion and Absorption, Reproduction in Organisms, Strategies for Enhancement in Food Production, Environmental Issues (Biology); The Solid State, Surface Chemistry, General Principles of Isolation of Elements, Polymers, Chemistry in Everyday Life, Hydrogen, s-Block Elements, Environmental Chemistry, States of Matter (Chemistry). Both 2026 papers have 1 each. Topic-level removals inside surviving chapters add more: transistor amplifiers and logic gates appear in 2013–2019 Physics and not in the 2026 samples.

**What you must do:** treat that list as a **hypothesis only**. Stage A builds the real change log from the two editions; that is the only evidence D6 may use. In the pilot, include at least one chapter next to removed content so D5–D7 and deleted-content notes are exercised.

**Update (2026-10-09), from directly inspecting the real Class 12 NCERT books (both editions, all three subjects — Class 11 older edition not yet available):**
- The hypothesis list above is confirmed exactly right for all three named Biology chapters, and for 5 of the 6 named Chemistry chapters — **but it misses "The p-Block Elements,"** which is genuinely absent from both the latest Class 12 *and* Class 11 Chemistry books, with no surviving home anywhere in the current syllabus. Add it to the watch list.
- **Removal pattern differs structurally by subject, which matters for how A6/A7 should expect to find changes:** Chemistry lost 6 whole chapters cleanly (survivors are word-for-word identical apart from renumbering); Physics lost only 1 whole chapter (Communication Systems) and the real cuts are *within* surviving chapters (e.g. Semiconductor Electronics lost its entire transistors/logic-gates sub-section, confirmed via the older edition's own exercise numbering reaching 14.15 vs the latest stopping at 14.6); Biology lost 3 whole chapters, with one fragment (Single Cell Protein) surviving by migrating into a different surviving chapter's sub-section (Microbes in Human Welfare) rather than disappearing cleanly.
- **A confirmed, concrete fact-change example** (not a wording change): Biology's Evolution chapter, age of the universe, "almost 20 billion years old" (older) → "almost 13.8 billion years old" (latest) — everything else in the chapter is word-for-word identical. Useful as a real worked example for A8 prompt-tuning.
- Not every outdated number gets refreshed: Biodiversity and Conservation carried forward the same biosphere-reserve/hotspot counts unchanged in both editions, despite being real-world-outdated in both. Don't assume every stale-sounding figure is a missed update — only Stage A7's actual diff decides.

### 2.4 Physics links to NCERT through rules, not answer sentences

In 28 Physics questions read from the 2026 papers: about 14% had an NCERT line that states the answer; ~40% needed one rule plus maths; ~30% chained two or more rules; ~11% applied an NCERT idea to a new case with no calculation; ~5% needed a result NCERT does not give. About 80% of all Physics questions have numeric or formula answers.

**What you must do:** implement `link_type` and `derivation_steps` in D4 exactly as Section 12 says, the derivation cross-check script, and D6 rule 0 (rule-based links are `latest_ncert`). Never mark a question `outside_ncert` only because no sentence states the final number.

### 2.5 Repeats are common

At least 25 clear repeat pairs exist in the ten papers, for example: an exact repeat seven years apart (`2019#44` → `2026-May#10`, work to raise a mass to height R); the stretched-wire problem (`2013#15`, then "melted and stretched n times" in `2017#4`); LCR power loss with new values (`2016-P1#40` → `2018#28`); graft rejection asked in 2015, 2017 and 2019; PCR steps (`2018#101`) returning as an arrange-in-order question (`2026-May#132`); post-synaptic receptors (`2017#106`) returning as fill-in-the-blank (`2026-May#179`). A word-similarity search found about 220 candidate pairs above its threshold, many false (shared words such as "Match List-I").

**What you must do:** keep D9 inclusive (a wide net) and D11 strict (a careful verdict, two runs). Never group questions by surface similarity alone.

### 2.6 Data defects you will meet

| Defect | Seen as | Handle in |
|---|---|---|
| Options run together with no separator | "…isa) Boron…b) Beryllium…" (most of the June 2026 sheet) | B3 output must have four separate option fields; `option_parser.py` must split inline options |
| Options that are images lost their content | ~20 questions with empty "a) b) c) d)" (e.g. `2017#59`, `2018#64`) | B3 crops each image option; empty option text is a check failure |
| Duplicated options | 5 questions (e.g. `2016-P2#88`) | B3 raises `B3_DUPLICATE_OPTIONS` (high) |
| Figures only as remote links | all 177 images in the legacy sheets are `cdn.mathpix.com` links | Always crop figures from the official PDFs; never depend on a URL |
| Missing answers | 2 questions in June 2026 (a Vernier zero-error question, an EM wave question) | B5 blocks with `B5_KEY_ROW_MISSING`, or B8 handles if the key marks them bonus/dropped |
| Copy typos | "Polymide", "micorspores", "Schotten-Baumen", "Identity Z" for "Identify Z" | B4's second reading against the official PDF |
| Statements in the stem written as "(a) … (b) …" | looks like options | `option_parser.py` must take the **last** complete a)–d) run as the options |

### 2.7 Scope gaps

- **2020–2025 are missing** from the data this spec's v0.1 taxonomy was originally built from (10 papers, §2's opening list), as are the 2020 re-exam and the 2024 retest. They must be collected as official PDFs (intake will flag them missing). **Update (2026-10-09):** papers and keys for 2020, 2021, 2022, 2023, 2024 (MAIN, confirmed via the key's own exam-date header) and 2025 have since landed in `inputs/` and were readable — this gap is no longer about *availability*, only about confirming each file is a genuine official scan before B1 registers it (see Section 2.8). The 2020/2024 re-exam and retest specifically are still unconfirmed as present.
- **2013 (NEET), 2014 and 2015 (AIPMT)** exist. Whether they join the bank is the owner's decision (Section 20). Until decided, intake treats them as **out of scope**: register them, but do not run B onward on them.

### 2.8 What a 10-paper sample (2016–2025, one paper per year, real data) confirmed

Before any real build work, one full paper per year from 2016–2025 (all three subjects, ~500 questions sampled, spread across early/mid/late in each subject) was checked question-by-question against the v0.1 taxonomy in Section 17. This is a genuine out-of-sample check for the years not in the original 10-paper analysis (2020–2025) and a consistency check for the years that were (2016–2019).

**Taxonomy held up well.** Across ~500 sampled questions, the large majority mapped cleanly onto existing `question_type`/`format`/`content_shape` values with zero changes needed. Only two genuine gaps surfaced, both narrow and Chemistry-specific:
- A list whose items are **structures to count/judge**, not statements or options (e.g. "how many of the following structures obey Hückel's rule," with i–vii as drawn rings) — nothing in E1 names this shape; `list_of_statements` assumes lettered text claims.
- A **backward-direction** reaction question — given the products and a reagent, identify the starting reactant — which `predict_product` (E2) doesn't cover, since it assumes reactant→product direction.

Two usability notes, not new values: a question can legitimately need **two E1 tags at once** (e.g. a fill-in-the-blank that also requires reading a figure), and a two-statement judge-each item labelled "A/B" should fold into the same handling as one labelled "I/II" — same structure, different label convention.

**Chemistry does not behave like either Physics or Biology, consistently, across all 10 years sampled.** Physics was numerical/application-dominated in every single year (in two of the ten sampled papers, 100% of sampled Physics questions were numerical/application with zero pure recall). Biology was recall/elimination-dominated in every year. Chemistry split along **sub-branch**, not year: physical-chemistry questions (kinetics, equilibrium, electrochemistry, solutions) matched Physics' numerical/application profile; organic/inorganic questions matched Biology's recall/elimination profile — roughly 40–60% on each side, varying by paper. **Any `thinking` (E4) prior conditioned on subject alone will misclassify a large share of Chemistry questions; it should be conditioned on B7's physical/organic/inorganic branch instead.**

**Biology is rarely numerical, not never.** Two clear counter-examples turned up (a PCR-amplification question needing `2^n`, a dihybrid-cross phenotypic-ratio question) — the working assumption should soften from "Biology has no numerical questions" to "numerical Biology questions are rare but real."

**`thinking` cannot be inferred from `question_type` or subject, even as a default.** A 2024 Physics Assertion–Reason question required a real calculation inside the reasoning step (not just judging the A/R relationship) — Assertion–Reason and Statement I/II items do not automatically mean `thinking: reasoning`. Confirmed separately: a 2024 Biology question that *looked* numerical (asking "how many molecules of ATP and NADPH") was pure memorised recall with no calculation at all — the inverse trap. `thinking` must stay a strict per-question judgement in E4, never a shortcut keyed off E1/E2 or subject.

---

## 3. Core concepts

| Term | Meaning you must apply |
|---|---|
| **Latest edition** | NCERT reprint 2026-27. The answer students are taught follows it. Book ID letter `L`. |
| **Older edition** | The last NCERT edition before rationalisation. Letter `O`. |
| **Lab manual** | NCERT practical manuals for Physics and Chemistry. Letter `M`. The only NCERT source for practical topics (e.g. salt analysis, metre bridge, Vernier). |
| **Passage** | One complete idea from NCERT (paragraph, table, figure with caption, box, or equation with its explaining lines), with a fixed ID. |
| **Subtopic** | A small idea inside a chapter that a NEET question could test. Defined on the latest edition. It is the link between questions and student pages. |
| **Change log** | One row per difference between an older passage and its latest partner: fact changed, fact removed, fact added, wording only. |
| **Sitting** | One occasion the exam was held: MAIN, PH2 (2016 Phase II), REEXAM, RETEST, CANCELLED. Every sitting is analysed. |
| **Booklet code** | A version of one sitting's paper with questions (and sometimes options) shuffled. Keys differ by code. Read one master code per sitting; read a second code only to fill missing pages. |
| **Final key** | The exam body's final answer key. Never the provisional key. |
| **Bonus / dropped** | A faulty question. Kept, fixed in B8, original stored beside the fix. |
| **Official answer** | From the final key (or B8's correction for faulty questions). |
| **Latest answer** | The answer by the latest NCERT (D7). Usually the same. When different, both are stored and the latest is taught. |
| **Syllabus status** | `latest_ncert`, `lab_manual`, `deleted_content`, `outside_ncert` (D6). |
| **Reason note** | A short student-facing note saying where the answer comes from, in a fixed template, quoting lines exactly (D6, D7). |
| **link_type** | How a question connects to NCERT: `states_answer`, `rule_used`, `rules_chained`, `concept_applied`, `beyond_ncert_method` (D4). |
| **Booklet duplicate** | Same question in two codes of one sitting → merged into one record (C1). |
| **Repeat** | Same fact or problem in a different year → separate records linked by a repeat group (D8–D11). |
| **Flag** | A record that a person must look at an item in Stage F. |
| **Provisional value** | A value used to keep going, which Stage F approves or corrects. |
| **Blocked** | An item that cannot sensibly continue; later steps skip it. |
| **Cascade** | After a Stage F edit, every later step that depends on the edited value is cleared and re-run automatically. |
| **Pilot** | Three chapters (one per subject) run end to end before the full run. |
| **Gold set** | 90 questions (30 per subject) whose every field a reviewer confirmed in the pilot's Stage F. Used to score every step. |

### 3.1 The five reason-note templates (D6/D7)

Copy every quoted line exactly from the edition named.

| note_type | Template |
|---|---|
| `same_both` | Answer from the latest NCERT: "<latest line or rule>". |
| `written_differently` | Answer from the latest NCERT: "<latest line>". Remember: the older NCERT wrote it as "<older line>". Same fact; follow the latest wording. |
| `answer_changed` | By the latest NCERT the answer is (<latest>): "<latest line>". The older NCERT said "<older line>", which gave (<official>). Follow the latest. |
| `deleted` | This question is from content deleted from the latest NCERT. The answer is according to the older NCERT: "<older line>". |
| `outside` | This fact is not in any NCERT edition. The answer is from the official key. |
| `outside_rules` | This question uses a result that is not given in NCERT. The NCERT rules involved are: "<rule 1>", "<rule 2>". The answer is from the official key. |
| `lab_manual` | Answer from the NCERT lab manual: "<line>". |

### 3.2 The four layers of the bank

| Layer | Holds | Filled by |
|---|---|---|
| 1 Clean questions | text, options, figures, official answer, status, source, booklet codes, repeat links | B, C, D7, D11 |
| 2 Where it comes from | chapter, subtopics, link_type, evidence, derivation steps, older lines, status, reason note | D |
| 3 Tags | E1–E6 values, codebook version | E |
| 4 Counts | per subtopic statistics | F4 (script only) |

---

## 4. Rules you must never break

1. **The order of work is decided by the runner script, never by an agent and never by you mid-run.** You follow `run_step.py --list` exactly. You do not reorder, skip, add or merge items.
2. **One decision per agent call.** One item, one judgement, one output file.
3. **Agents get only the fields the step lists.** Never pass whole books, other questions (except where a step says so, like D9), legacy columns, coaching material or answer keys to agents that must not see them.
4. **Every NCERT claim is a verified quote.** A script searches the named edition for every quoted line, word for word (Section 5.7). A quote that is not found is rejected.
5. **Agents never retype source text they were asked only to locate.** A3 returns block numbers; B2 returns boxes; the script cuts.
6. **"unsure" is always allowed and never forced into a value.**
7. **Every output is checked by a script before the next step uses it.** Status is always one of `pass`, `flagged`, `blocked`, `skipped`, `stale`.
8. **Never wait for a person mid-run.** Doubt becomes a flag. Use the fallback chain (Section 5.5). Continue with a provisional value, or block the item.
9. **Never edit an agent's output by hand, never answer a judgement yourself instead of calling its agent, never fix data in `inputs/`.** Corrections happen only through Stage F decisions.
10. **The blind solver (B6) and the latest-answer checker (D7) never see coaching material**, and B6 never sees the key.
11. **Counts are computed, never typed.**
12. **Nothing is released without Stage F.** Only `export_tables.py` writes `data/` tables, and only for chapters signed off in `review/releases.csv`.
13. **Legacy sheets are never the bank.** Every question enters at B1 from an official PDF.
14. **Every output stores its agent, prompt version and time**, and every run writes `run_log.csv` rows.

---

## 5. Architecture

### 5.1 The loop

```
run_step.py <STEP> --list
   → prints work lines: item_id | agent | input_path | output_path | run_label
for each line, in order:
   you invoke the subagent:  "Use the <agent> subagent. Input: <input_path>. Output: <output_path>. Do nothing else."
run_step.py <STEP> --check
   → validates every new output, runs scripts/checks/<STEP>.py, applies the fallback chain,
     writes statuses, flags and run_log rows, and either prints a NEW list (retries,
     second runs, adjudications) or prints DONE
repeat until DONE
```

Script-only steps have no agent lines: `run_step.py <STEP> --auto` runs them directly.

### 5.2 Two ways to call agents

- **Interactive (default):** you, the main Claude Code session, invoke the subagent for each list line using the Task/Agent mechanism, with exactly the instruction line above.
- **Headless (for scale, optional):** `run_step.py <STEP> --auto` shells out once per line to Claude Code in non-interactive mode (`claude -p "<instruction line>"`). Check `claude --help` for the exact flags of the installed version (permissions, output format, which agents are loaded) and implement `scripts/lib/agents.py` accordingly. Set project permissions in `.claude/settings.json` so agents can read only `steps/`, `ncert/`, `papers/` and write only their own output path.

Both modes must produce identical files. The runner never cares how the output file was produced; it only checks it.

### 5.3 Subagents

- Every agent file has YAML frontmatter: `name`, `description`, `tools: Read, Write`, `model: inherit`.
- Subagents do **not** see `CLAUDE.md`. Each agent file therefore repeats the universal rules (Appendix B).
- `Read` is also how a vision agent opens page or question images listed in its input.
- No agent gets `Bash`, web access or other tools.
- `model: inherit` everywhere. Some Claude Code versions have had problems routing subagents to a different model, so do **not** rely on a different model for a second opinion. Where a step needs an independent second reading (B4 without a text layer), use a **different method**: different instructions, a different view of the input, and no access to the first reading.

### 5.4 Item status

| Status | Meaning | Next step runs? |
|---|---|---|
| `pass` | All checks passed, no doubt | yes |
| `flagged` | A value exists but needs a human look | yes, with the provisional value |
| `blocked` | Nothing sensible can continue | no; later steps skip the item |
| `skipped` | The step does not apply | yes |
| `stale` | Cleared by the cascade; must re-run | re-run first |

An item's overall status is the worst across its steps: blocked > flagged > pass.

### 5.5 The fallback chain

Each step section says which links it uses.

1. **Retry once**: same agent, fresh input file, with `PREVIOUS ATTEMPT FAILED: <check message>` appended to the instruction line.
2. **Second opinion** (if the step defines one): an independent run B, which never sees run A.
3. **Adjudicator**: `x-adjudicator` gets the step's task text, allowed values, the same evidence, run A, run B (or both readings with differing spans highlighted), and the failed check.
4. **Decided** → provisional value + flag (normal or high). **Unsure / invalid** → the step's safe default + flag, or `blocked` + blocker flag if the step has no safe default.

Never loop beyond this chain. B6 never retries (Section 10).

### 5.6 Flags

Append one JSON object per line to `flags/flags.jsonl`:

```json
{"flag_id": "FL-000317", "item_type": "question", "item_id": "Q-000123", "step": "D1",
 "code": "D1_ADJUDICATED", "severity": "normal",
 "message": "Run A: BIO11-CH10; run B: unsure; adjudicator chose BIO11-CH10.",
 "provisional_value": {"chapter_ids": ["BIO11-CH10"]},
 "evidence": ["steps/D1/out/Q-000123.runA.json", "steps/D1/out/Q-000123.runB.json", "steps/D1/out/Q-000123.adjudicated.json"],
 "prompt_version": "v1", "created_at": "2026-10-20T11:42:05+05:30",
 "status": "open", "decision": null, "reviewer": null, "decided_at": null}
```

Severities: `blocker` (item blocked), `high` (touches answer, evidence or what students are taught), `normal` (adjudicated judgement or draft needing approval), `low` (cosmetic or medium confidence). Full catalogue: Section 16.

### 5.7 Text normalisation and quote verification (used by many checks)

`scripts/lib/text_normalise.py :: normalise_quote(s)` — for quote matching only:
- collapse all whitespace and line breaks to single spaces;
- join end-of-line hyphenation (`chroma-\ntids` → `chromatids`);
- curly quotes → straight quotes; ligatures (ﬁ, ﬂ) → letters;
- **no** case folding, **no** punctuation removal, **no** word changes.

`scripts/lib/quote_verify.py :: find(quote, passage_text)` returns the span or `None`. Reject any quote containing `...` or `…`. `find_in_edition(quote, book_ids)` searches all passages of the named edition.

`scripts/lib/latex_normalise.py :: normalise(s)` — for comparing two readings only: collapse spaces; remove `\,` `\;` `\!`; `\text{X}` → `X`; Unicode Ω→`\Omega`, μ→`\mu`, ρ→`\rho`, ×→`\times`, −→`-`; drop `$` delimiters. **Never** change digits, signs, letters or order.

### 5.8 Folder layout

```
pyq_bank/
├── CLAUDE.md                       # Appendix A
├── .claude/agents/*.md             # Appendix B (34 agents)
├── .claude/commands/*.md           # Appendix C
├── .claude/settings.json           # tool permissions
├── docs/
│   ├── SPEC.md                     # this document
│   └── OPEN_QUESTIONS.md           # your questions and chosen defaults
├── config/
│   ├── steps.yaml                  # every step (Appendix D skeleton; you complete it)
│   ├── cascade.yaml                # Section 15
│   └── allowed_values.yaml         # Section 17
├── codebook/                       # written by the owner later; may be empty (Section 13.0)
├── inputs/                         # raw files, read-only
│   ├── manifest.csv
│   ├── ncert/latest/  ncert/older/  ncert/lab_manuals/
│   ├── papers/  keys/  notices/  coaching/  legacy_sheets/
├── register/  books.csv  papers.csv  counters.json  intake_report.md
├── ncert/
│   ├── pages/<BOOK>/p<NNN>.png
│   ├── blocks/<BOOK>.jsonl
│   ├── passages/<BOOK>.jsonl
│   ├── chapters/<SUBJ><CLASS>.json    # latest-edition chapter list with headings
│   ├── subtopics/<CHAPTER>.json
│   ├── links/<BOOK>.jsonl
│   ├── pairs/<CHAPTER>.json
│   ├── diffs/<CHAPTER>.jsonl
│   ├── change_log.csv  deleted_topics.csv
│   └── search_index/
├── papers/
│   ├── pages/<PAPER>/p<NN>.png
│   ├── questions/<PAPER>/<QNO>.png  <QNO>_fig.png  <QNO>_opt<k>.png
│   └── records/<QID>.json           # the merged question record, updated step by step
├── steps/<STEP>/
│   ├── prompt_version.txt
│   ├── work/<ITEM>.<run>.input.json
│   ├── out/<ITEM>.<run>.json        # run = runA | runB | adjudicated | retry1
│   └── status/<ITEM>.json
├── flags/flags.jsonl
├── review/ queue.csv  review_pack/  decisions.csv  corrections.jsonl  releases.csv
├── gold/ gold_set.csv  scores.md
├── data/ questions.csv  ncert_links.csv  tags.csv  subtopic_stats.csv
├── run_log.csv
├── schemas/<STEP>.json
├── scripts/ (Section 7)
└── tests/  fixtures/
```

`papers/records/<QID>.json` is the single current record of a question. Every step that produces a question field writes it **both** to its own `steps/<STEP>/out/` file (history) and into the record (current value), together with the source step and prompt version of that field.

### 5.9 Prompt versions and idempotence

- `steps/<STEP>/prompt_version.txt` holds the current version (`v1`, `v2`…). When you change an agent file's behaviour, bump it and say so in `docs/OPEN_QUESTIONS.md`.
- An item "needs" a step when its previous steps are `pass`/`flagged`/`skipped`, it isn't blocked, and it has no output for the step's **current** prompt version (or is `stale`).
- Running a command twice in a row must do nothing the second time.

### 5.10 Run log

`run_log.csv` columns: `run_id, item_id, step, run, agent, prompt_version, started_at, ended_at, check, check_message, retry_of, status_after`.

### 5.11 Parallelism

Within one step, items are independent: you may process list lines in parallel. Across steps, an item's step starts only after its previous step has a status. Stages run in order A → B → C → D → E → F, except that Stage A and Stage B may run in parallel (B does not need A until D1).

---

## 6. Data contracts

### 6.1 IDs

| ID | Pattern | Example | Notes |
|---|---|---|---|
| Book | `{SUBJ}{CLASS}{ED}` | `BIO11L`, `BIO11O`, `PHY12M` | SUBJ ∈ PHY, CHE, BIO; ED ∈ L, O, M. Part 1/Part 2 share one ID; record the part per page range |
| Chapter | `{SUBJ}{CLASS}-CH{nn}` | `BIO11-CH10` | Latest-edition numbering |
| Passage | `{BOOK}-CH{nn}-P{nn}` | `BIO11L-CH10-P07` | Edition letter in the ID so editions never collide |
| Subtopic | `{SUBJ}{CLASS}-CH{nn}-ST{nn}` | `BIO11-CH10-ST03` | Latest edition only |
| Paper | `NEET-{YEAR}-{SITTING}-{CODE}` | `NEET-2023-MAIN-A` | SITTING ∈ MAIN, PH2, REEXAM, RETEST, CANCELLED |
| Question | `Q-{6 digits}` | `Q-000123` | Never reused, even after deletion |
| Change | `CL-{4 digits}` | `CL-0014` | |
| Repeat group | `RG-{4 digits}` | `RG-0042` | |
| Flag | `FL-{6 digits}` | `FL-000317` | |

Counters live in `register/counters.json`; `scripts/lib/ids.py` is the only code that issues IDs.

### 6.2 Register tables

`register/books.csv`: `book_id, subject, class, language, edition, part_ranges, reprint_text_exact, reprint_page, file, status`
`register/papers.csv`: `paper_id, file_kind (paper|key), exam, year, sitting, booklet_code, language, trust (official|memory_based), source, file, in_scope (yes|no), status`

### 6.3 Question record (`papers/records/<QID>.json`)

```json
{
  "question_id": "Q-000123",
  "exam": "NEET", "year": 2023, "sitting": "MAIN",
  "paper_codes": ["A:112"], "option_map": null,
  "subject": "Biology", "branch": "botany",
  "stem_en": "…", "statements": [{"label": "A", "text": "…"}], "list_i": [], "list_ii": [],
  "options_en": {"1": "…", "2": "…", "3": "…", "4": "…"}, "option_images": {},
  "structure": "statements", "negative_words": [], "has_figure": false, "figure_file": null,
  "official_answer": "1", "answer_source": "inputs/keys/NEET_2023_MAIN_CodeA_finalkey.pdf",
  "status": "normal", "issue_reason": null, "corrected_answer": null, "corrected_stem": null,
  "latest_answer": "1", "answer_changed": false, "change_note": null,
  "trust": "official", "source_file": "…", "source_page": 24,
  "chapter_ids": ["BIO11-CH10"], "subtopic_ids": ["BIO11-CH10-ST03"],
  "link_type": "states_answer",
  "evidence": [{"for": "statement A", "passage_id": "BIO11L-CH10-P06", "exact_line": "…"}],
  "derivation_steps": [], "covers": "fully",
  "older_evidence": [{"for": "statement A", "passage_id": "BIO11O-CH10-P05", "exact_line": "…"}],
  "syllabus_status": "latest_ncert", "note_type": "same_both", "reason_note": "…", "change_ids": [],
  "fact_line": "…", "repeat_group_id": "RG-0042", "repeat_label": "same_fact_new_format", "related_ids": [],
  "question_type": "list_of_statements", "format": "pick_correct_combination", "content_shape": "process",
  "category_primary": "elimination", "category_secondary": "process", "category_why": "…",
  "option_traps": {"2": {"trap": "wrong_pairing", "why": "…"}},
  "stem_context": "plain", "answer_form": "combination_code", "negation": "none",
  "item_count": 4, "constants_given": false, "figure_role": "none",
  "codebook_version": "none",
  "legacy_chapter": null, "legacy_topic": null, "legacy_question_type": null,
  "explanation_source": "ours",
  "field_sources": {"official_answer": {"step": "B5", "prompt_version": "v1", "status": "pass"}},
  "review_status": "pending", "release_status": "unreleased"
}
```

`field_sources` must have an entry for every non-null field.

### 6.4 NCERT tables

- `ncert/blocks/<BOOK>.jsonl`: `block_id, book_id, page_start, page_end, kind, text, table (rows), figure (caption, labels), latex, continues_from_previous, continues_on_next`
- `ncert/passages/<BOOK>.jsonl`: `passage_id, book_id, chapter_id, section_heading, kind, page_start, page_end, text, blocks`
- `ncert/chapters/<SUBJ><CLASS>.json`: list of `{chapter_id, title, headings: [{number, text}]}` for the **latest** edition, plus `older_title` mapping for older chapters (A6)
- `ncert/subtopics/<CHAPTER>.json`: `{chapter_id, version, approval, subtopics: [{subtopic_id, name, from_heading, description, passages}]}`
- `ncert/links/<BOOK>.jsonl`: `passage_id, subtopic_id | "none", method (heading|agent|adjudicated)`
- `ncert/pairs/<CHAPTER>.json`: list of `{old_passage_id, new_passage_id, similarity, result: pair|removed|added, adjudicated}`
- `ncert/diffs/<CHAPTER>.jsonl`: `{pair: [old, new], identical, diff: [{old, new}]}`
- `ncert/change_log.csv`: `change_id, chapter_id, subtopic_id, old_passage_id, new_passage_id, change_type, old_fact, new_fact, could_flip_an_answer, old_text, new_text, affected_questions, approval`
- `ncert/deleted_topics.csv`: `old_passage_id, chapter_id, old_pages, heading, subtopic_hint`

### 6.5 Review tables

- `review/queue.csv`: `priority, chapter_id, flag_id, item_id, step, code, severity, message, evidence_page`
- `review/decisions.csv`: `flag_id_or_item, field, decision (approve|correct|edit|block), corrected_value_json, reviewer, comment, decided_at`
- `review/corrections.jsonl`: `{item_id, field, old, new, step_corrected, reviewer, reason, flag_id, at, cascade: [...]}`
- `review/releases.csv`: `chapter_id, released_at, signed_by, gold_score_snapshot, open_flags`

### 6.6 Final tables (`data/`, written only by `export_tables.py`)

`questions.csv` (Layer 1), `ncert_links.csv` (Layer 2, one row per question–subtopic), `tags.csv` (Layer 3), `subtopic_stats.csv` (Layer 4). Columns = the record fields of each layer (6.3) plus `review_status`.

---

## 7. Build plan (milestones)

Work through the milestones in order. At the end of each, print the report in Section 19 and stop only if the milestone's "done when" fails.

### M0 · Set up the project

- [ ] Create the folder layout (5.8).
- [ ] Create `CLAUDE.md`, all agent files, all command files and the three config files from Appendices A–D, word for word.
- [ ] Create `docs/OPEN_QUESTIONS.md` with the open decisions in Section 20.
- [ ] Create `.claude/settings.json` restricting agent tools to Read/Write within the project.

**Done when:** every file in Appendices A–D exists and `claude agents` (or `/agents`) lists all 34 agents.

### M1 · Libraries

Write `scripts/lib/`: `io.py` (atomic writes, jsonl append, csv), `ids.py`, `text_normalise.py`, `quote_verify.py`, `latex_normalise.py`, `option_parser.py`, `search_index.py`, `flags.py`, `status.py`, `records.py` (read/update `papers/records/<QID>.json` with `field_sources`), `agents.py` (build instruction lines; headless call), `coaching_guard.py`, `pdf.py` (render pages to PNG at 200 dpi, extract text layer by page and by box, crop boxes).

**Done when:** unit tests T1–T8 in Appendix E pass.

### M2 · Runner and configs

Write `scripts/run_step.py` (`--list`, `--check`, `--auto`, filters `--chapters`, `--papers`, `--items`), `scripts/run_stage.py` (`--plan`), `scripts/status.py`. Complete `config/steps.yaml` for every step from Sections 8–14 (input_fields, output schema, check, fallback, flags with severities, safe default). Write `schemas/<STEP>.json` for every agent output in Sections 8–14.

**Done when:** T9–T12 pass (idempotence, fallback chain, stale handling, coaching guard).

### M3 · Step scripts and checks

Write every script-only step and every `scripts/checks/<STEP>.py` named in Sections 8–14, plus `build_review_pack.py`, `apply_review.py`, `cascade.py`, `compute_counts.py`, `score_gold.py`, `export_tables.py`, `intake_check.py`, `legacy_match.py`.

**Done when:** T13–T30 pass.

### M4 · Smoke test

Create `tests/fixtures/` with: 3 NCERT pages (one paragraph split across a page break, one table split across a page break, one equation), each in a latest and an older version with one planted fact change; 6 question images (a Biology statements question, a Physics numerical whose text layer says "40 Ω" while the image says "4 Ω", a match-the-lists question, a question with a figure, a question split across two columns, a bonus question with a notice) and a key. Run `/run-stage smoke`.

**Done when:** every fixture item has a status for every step; the planted "40 Ω" misread is flagged at B4; the planted fact change reaches the change log and D7; editing one answer in a test `decisions.csv` makes exactly the cascade's steps `stale` and re-runs them.

### M5 · Pilot run (no people)

Follow Section 18.1.

### M6 · Pilot review (Stage F, people)

Build the review pack; wait for `review/decisions.csv`; apply; build the gold set; score (Section 18.2). This is the only milestone where you wait for people, and you wait only between commands, never inside a step.

### M7 · Fix and re-score

For every step under target on the gold set: improve its agent prompt, bump its version, re-run, re-score, until every target is met.

### M8 · Full run, full review, release

Follow Section 18.3–18.5.

---

## 8. Stage 0 · Intake

### S0 · Intake check

- **Purpose:** prove every required input is present before anything is read, and mark what is in scope.
- **Worker:** SCRIPT (`scripts/intake_check.py`).
- **Reads:** `inputs/` tree; `inputs/manifest.csv` (columns: `file, kind (ncert|lab_manual|paper|key|notice|coaching|legacy_sheet), subject, class, edition, year, sitting, booklet_code, source, downloaded_on`); official sitting lists in `inputs/notices/`.
- **Procedure:**
  1. SCRIPT: list every file under `inputs/`; every file must have exactly one manifest row and every row a file.
  2. SCRIPT: for each NCERT subject × class (Physics, Chemistry, Biology × 11, 12), require one `latest` and one `older` book (Physics and Chemistry may be two PDFs each for Part 1 and Part 2); require Physics and Chemistry lab manuals.
  3. SCRIPT: for each year 2016–2026, for each sitting on the official list, require a paper and a **final** key whose booklet code matches the paper (or a key covering all codes). Known sittings that must exist: 2016 MAIN and PH2; 2019 MAIN and REEXAM; 2020 MAIN and REEXAM; 2024 MAIN and RETEST; 2026 CANCELLED (3 May) and REEXAM (21 June); MAIN for every other year.
  4. SCRIPT: mark papers outside 2016–2026 `in_scope = no` (2013–2015 until the owner decides; Section 20).
  5. SCRIPT: legacy sheets → `inputs/legacy_sheets/` only; verify none are referenced as papers.
- **Checks:** as above.
- **On failure:** each missing item → flag `S0_MISSING_INPUT` (blocker) for that book or sitting. The rest of the run continues.
- **Writes:** `register/intake_report.md` (present, missing, out of scope), flags.
- **Done when:** the report exists and every missing item has a flag.
- **Pitfalls:** the legacy analysis had **no 2020–2025 papers**; expect those flags until they are collected. Keys must be the **final** key; a provisional key is a missing input.

---

## 9. Stage A · NCERT index and change log

Runs once per reprint. Order: A1 → A2 → A2S → A3 → A4 → A5 → A6 → A7 → A8 → A9. Also builds `ncert/chapters/<SUBJ><CLASS>.json` (latest-edition chapter lists with headings) as a by-product of A2/A3 headings; D1 needs it.

### A1 · Register the books

- **Purpose:** every NCERT link must point to one exact printing.
- **Item:** one book PDF · 1 run · **Worker:** SCRIPT + AGENT `a1-book-registrar`.
- **Reads:** the PDF's first 6 pages rendered as images; their text layer; the manifest row's edition.
- **Procedure:**
  1. SCRIPT: render pages 1–6; extract their text layer; write the input file.
  2. AGENT: read the pages; copy the reprint/imprint line exactly; give subject, class, language, part, edition seen.
  3. SCRIPT: check; assign `book_id`; append to `register/books.csv`.
- **Agent output:** `{"subject","class","language","part","edition_seen","reprint_text_exact","reprint_page","is_lab_manual","note"}`.
- **Checks:** (1) `reprint_text_exact` non-empty and found on that page's text layer when one exists; (2) `edition_seen` equals the manifest edition; (3) exactly one latest and one older book per subject-class (plus manuals).
- **On failure:** retry once. No reprint line → `reprint = "unknown"`, flag `A1_REPRINT_NOT_FOUND` (high). Edition mismatch → use the manifest edition, flag `A1_EDITION_MISMATCH` (high). Every row also gets `A1_REGISTER_DRAFT` (low).
- **Writes:** `steps/A1/out/*`, `register/books.csv`.
- **Done when:** every NCERT file has a register row.
- **Pitfalls:** the imprint is often on the back of the title page.

### A2 · Read the pages

- **Purpose:** turn every page into text blocks; join anything split across a page break.
- **Item:** one page · 1 run · **Worker:** SCRIPT + AGENT `a2-page-reader`.
- **Reads:** page image; that page's text layer; the previous page's last block (kind + last ~100 characters).
- **Procedure:**
  1. SCRIPT: render every page at 200 dpi; extract the text layer; process pages **in order**.
  2. AGENT: list blocks in reading order (left column first), kind of each, text (copy the text layer's characters when they match the image), whether the first block continues from the previous page and whether the last continues on the next; mark tables, figures and equations `needs_special` with a box.
  3. SCRIPT: remove headers/footers the agent listed; queue special blocks for A2S.
- **Agent output:** `{"blocks":[{"n","kind","text","needs_special","bbox","continues_from_previous","continues_on_next"}],"first_block_continues_from_previous","last_block_continues_on_next","running_header_footer_removed","note"}`.
- **Checks:** (1) pages read = PDF pages; (2) page N's `last_block_continues_on_next` equals page N+1's `first_block_continues_from_previous`; (3) with a text layer, each paragraph's text matches it (≥ 99% characters after whitespace normalisation); (4) no header/footer text inside blocks.
- **On failure:** retry once. Continuation disagreement → adjudicator with both page images → `A2_JOIN_ADJUDICATED` (normal). Text-layer mismatch → keep the text-layer text, `A2_TEXT_MISMATCH` (normal). Unreadable page → `blocked`, `A2_UNREADABLE` (blocker).
- **Writes:** `steps/A2/out/*`.
- **Done when:** every page has a status.

### A2S · Transcribe special blocks

- **Item:** one table, figure or equation crop · 1 run · **Worker:** SCRIPT + AGENT `a2-special-transcriber`.
- **Procedure:** SCRIPT crops the box; AGENT copies a table row by row, a figure's caption and every label, or an equation in LaTeX; SCRIPT stores it in the block.
- **Checks:** table rows have consistent column counts; LaTeX parses; caption non-empty for figures.
- **On failure:** retry once; then keep the crop image with empty text and flag `A2_SPECIAL_UNREAD` (normal).
- **After A2 and A2S (SCRIPT):** join blocks split across page breaks wherever both flags agree (or the adjudicator decided), keeping `page_start` and `page_end`. A table split across pages with a repeated header row becomes one table with one header. Write `ncert/blocks/<BOOK>.jsonl`.

### A3 · Split into passages

- **Purpose:** passages that each hold one complete idea, with fixed IDs. The agent chooses cuts by block number; the script cuts.
- **Item:** one section (blocks under one heading) · 1 run · **Worker:** AGENT `a3-passage-splitter` + SCRIPT.
- **Reads:** book_id, chapter, section heading, numbered blocks (n, kind, text).
- **Procedure:** AGENT returns lists of block numbers; SCRIPT cuts, assigns IDs in reading order, writes passages. **Both editions use the same agent and prompt.**
- **Agent output:** `{"passages":[[1],[2,4],[3],[5]],"note"}`.
- **Checks:** every block exactly once; order kept except "paragraph – figure/box – paragraph continued", where the interrupter is its own passage; concatenation of passages equals the section text word for word.
- **On failure:** retry once; then the safe default "one passage per block" + `A3_DEFAULT_CUTS` (normal).
- **Writes:** `ncert/passages/<BOOK>.jsonl`; `ncert/chapters/<SUBJ><CLASS>.json` from headings.
- **Done when:** every section of every book is cut.

### A4 · Write the subtopic list

- **Purpose:** the shared language between past questions and student pages. Latest edition only.
- **Item:** one latest-edition chapter · **2 runs** · **Worker:** AGENT `a4-subtopic-writer` ×2 + adjudicator + SCRIPT.
- **Reads:** chapter id and title; all headings with numbers; passages (id, kind, first 200 characters).
- **Procedure:** run A and run B independently; SCRIPT matches subtopics by heading and passage overlap; disagreements → adjudicator merges into one list; SCRIPT assigns `ST01…` in order.
- **Agent output:** `{"chapter","subtopics":[{"n","name","from_heading","passages"}],"note"}`.
- **Checks:** every passage covered by ≥ 1 subtopic; names unique; 4–15 subtopics (soft: outside → flag only); run A/B match rate ≥ 70% (soft).
- **On failure:** retry once; adjudicator. Every chapter gets `A4_SUBTOPICS_DRAFT` (normal; high if match rate < 70%) because every list must be approved in Stage F.
- **Writes:** `ncert/subtopics/<CHAPTER>.json` (`approval: "pending"`).
- **Pitfalls:** names describe ideas, not pages. New Class 11 books are due in 2027-28; subtopics must survive new passage IDs.

### A5 · Link passages to subtopics

- **Item:** one passage, either edition · 1 run · **Worker:** SCRIPT; AGENT `a5-passage-linker` only when headings don't decide.
- **Procedure:** latest passages: copy A4's assignment. Older passages: SCRIPT matches by identical heading text; otherwise AGENT chooses a subtopic id or `none` ("topic not in the latest book").
- **Checks:** exactly one subtopic or `none`; id exists.
- **On failure:** unsure → adjudicator → still unsure → `none` + `A5_UNSURE` (normal). `none` is the safe default.
- **Writes:** `ncert/links/<BOOK>.jsonl`.

### A6 · Pair old and new passages

- **Item:** one chapter · **Worker:** SCRIPT (`pair_passages.py`); adjudicator for weak pairs.
- **Procedure:** within each subtopic (and among `none` passages for removals), compute similarity = Jaccard on word 3-grams after `normalise_quote`; solve a one-to-one assignment (Hungarian). ≥ 0.85 → pair; 0.50–0.85 → **weak** → adjudicator ("same idea / not same / unsure"); < 0.50 for all candidates → `removed` (older) or `added` (latest). Also map older chapter titles to latest chapter ids.
- **Checks:** every passage exactly one of pair / removed / added.
- **On failure:** weak + unsure → keep as pair, `A6_WEAK_PAIR` (normal).
- **Writes:** `ncert/pairs/<CHAPTER>.json`.

### A7 · Find the differences

- **Item:** one pair · **Worker:** SCRIPT (`diff_pairs.py`).
- **Procedure:** word-level diff after `normalise_quote`. Identical → drop. A moved page break never counts (A2 joined text first).
- **Writes:** `ncert/diffs/<CHAPTER>.jsonl`.

### A8 · Judge one change

- **Item:** one non-identical pair · **2 runs** · **Worker:** AGENT `a8-change-judge` ×2 + adjudicator.
- **Reads:** older text, latest text, highlighted differences.
- **Agent output:** `{"change_type": fact_changed|fact_removed|fact_added|wording_only|unsure, "old_fact","new_fact","could_flip_an_answer","why","confidence"}`.
- **Checks:** runs A and B agree on `change_type`.
- **On failure:** disagreement → adjudicator → `A8_ADJUDICATED` (normal). Every non-wording change → `A8_FACT_CHANGE` (normal). Wording-only with `could_flip_an_answer: true` → `A8_WORDING_RISK` (normal).
- **Pitfalls:** "usually found in X" → "found in X" is wording that can flip an "always true?" question. Keep wording-only rows.

### A9 · Write the change log

- **Item:** one chapter · **Worker:** SCRIPT (`write_change_log.py`).
- **Procedure:** one row per non-identical pair with A8's result; every `removed` passage → `deleted_topics.csv`. After Stage D, fill `affected_questions` from every question whose D4/D5 evidence cites either passage.
- **Writes:** `ncert/change_log.csv` (`approval: pending`), `ncert/deleted_topics.csv`.
- **Done when:** every non-identical pair has a row; every removed passage is listed.
- **Pitfall:** the analysis's list of removed chapters (Section 2.3) is a hypothesis. Do not write any row from it; only from the books.

---

## 10. Stage B · Extract papers

Order per paper: B1 → B2 → B3 → B4 → B5 → B6 → B7 → B8. Only papers with `in_scope = yes`.

### B1 · Register the paper

- **Item:** one paper or key file · 1 run · **Worker:** SCRIPT + AGENT `b1-paper-registrar`.
- **Reads:** cover page and first question page images; their text layer; the manifest row.
- **Procedure:** AGENT copies exam name, date, booklet/test code and any re-exam/retest/phase wording exactly; says whether it agrees with the manifest. SCRIPT assigns `paper_id` and writes the row.
- **Agent output:** `{"file_kind","exam","year","sitting","booklet_code","language","trust","cover_text_exact":{"code","date"},"agrees_with_manifest","note"}`.
- **Checks:** one row per file; paper and key codes match; every official sitting has both.
- **On failure:** disagreement → use the **cover text** (printed evidence beats the typed manifest), `B1_MANIFEST_MISMATCH` (normal). Every row → `B1_REGISTER_DRAFT` (low).
- **Writes:** `register/papers.csv`.

### B2 · Find the questions on each page

- **Item:** one page (in order; left column then right) · 1 run · **Worker:** SCRIPT + AGENT `b2-boundary-finder`.
- **Reads:** page image, column layout (detected by SCRIPT), previous page's last question and its continuation flag.
- **Procedure:** AGENT returns each question number with box(es) and continuation flags; SCRIPT crops, stitches parts of split questions into one image `papers/questions/<PAPER>/<QNO>.png`, crops the figure and each image option separately.
- **Agent output:** `{"page","questions":[{"qno","parts":[{"column","bbox"}],"continues_on_next"}],"top_continues_from_previous":{"left","right"},"note"}`.
- **Checks:** numbers continuous across pages; total = the paper's printed count (180; **200 for 2021–2024** because Section B printed 50/50/100 with 180 attempted — store all 200); continuation flags agree; boxes don't overlap; section headers and instructions excluded.
- **On failure:** retry; adjudicator with both pages → `B2_BOUNDARY_ADJUDICATED` (normal). Missing number → `blocked`, `B2_MISSING_QNO` (blocker).

### B3 · Read one question

- **Item:** one question image · 1 run · **Worker:** AGENT `b3-question-reader` + SCRIPT.
- **Reads:** the stitched question image; separate figure and option crops.
- **Procedure:** AGENT copies stem, statements, List-I/List-II rows, the four options and any table exactly, with all maths, units, chemical formulas and Greek letters in LaTeX; records structure, figure, negative words. SCRIPT runs `option_parser.py` checks.
- **Agent output:** `{"stem_en","statements":[{"label","text"}],"list_i":[{"label","text"}],"list_ii":[{"label","text"}],"options_en":{"1","2","3","4"},"option_images":{"1": "<crop path or null>",…},"structure","has_figure","figure_bbox","negative_words_seen","note"}`.
- **Allowed `structure`:** plain, statements, list, match, table, assertion_reason, statement_i_ii.
- **Checks:** exactly four options; each option has text **or** an image (never both empty); no two options identical; match lists equal length (or the list lengths printed); LaTeX parses; statements labelled consecutively.
- **On failure:** retry. Fewer than four options → back to B2 once for this question (likely a bad join). Duplicated options → `B3_DUPLICATE_OPTIONS` (high), continue (B4 decides). Still broken → `blocked`, `B3_OPTION_COUNT` or `B3_UNREADABLE` (blocker).
- **Pitfalls from real data:** options run together with no separators ("…isa) …b) …"); statements written as "(a) … (b) …" inside the stem (the real options are the **last** complete a)–d) run); five-item lists (A–E vs I–V); image options that become empty text if not cropped.

### B4 · Read it a second way

- **Item:** one question · **Worker:** SCRIPT (text layer) **or** AGENT `b4-second-reader` (no text layer) + SCRIPT compare.
- **Procedure:**
  1. If the PDF has a text layer inside the question's box: SCRIPT extracts it, splits options with `option_parser.py`, converts symbols to LaTeX by fixed rules. No agent.
  2. Else: AGENT `b4-second-reader` transcribes **line by line** first, then assembles fields, without seeing B3's output.
  3. SCRIPT compares B3 and B4 field by field after `latex_normalise`.
- **On failure (mismatch):** adjudicator sees the image and both readings with differing spans highlighted and chooses span by span → continue with the adjudicated text, `B4_MISMATCH_ADJUDICATED` (**high** if the span is a number, unit, sign, option label or negative word; else normal).
- **Writes:** the record's text fields with `field_sources` = B3/B4/adjudicated.

### B5 · Attach the answer key

- **Item:** one key page · 1 run · **Worker:** AGENT `b5-key-copier` + SCRIPT.
- **Procedure:** AGENT copies the key table exactly (qno, answer, marks like Bonus/Dropped/*, multiple accepted). SCRIPT joins on **(paper_id, qno)** — never qno alone — and sets `status`.
- **Agent output:** `{"booklet_code","rows":[{"qno","answer","mark"}],"note"}`.
- **Checks:** every question exactly one row; answers ∈ {1,2,3,4} or a comma list; key text layer agrees.
- **On failure:** missing row → `blocked`, `B5_KEY_ROW_MISSING` (blocker). Disagreement with text layer → adjudicator with the key image, `B5_KEY_ADJUDICATED` (high).
- **Status values:** normal, bonus, dropped, multiple_accepted (multiple_accepted is handled in B8).
- **Pitfall:** the analysed June 2026 data had two questions with no answer; expect blocks or B8 cases there.

### B6 · Solve it without the key

- **Item:** one question · 1 run, **no retry** · **Worker:** AGENT `b6-blind-solver` + SCRIPT.
- **Reads:** stem, statements, lists, options, figure image. **Never** the key, coaching material or NCERT.
- **Agent output:** `{"answer","reason","working","confidence","note"}`.
- **Checks:** compare with the official answer (any accepted option counts).
- **On disagreement:** `B6_DISAGREES_WITH_KEY` (high) with an automatic hint: one question → "check text and figure"; > 10% of a paper → "check B5 join for this paper"; B4 also mismatched → "check B4 spans"; status bonus/dropped → "see B8". The question continues with the **official** answer.
- **Why no retry:** a retry only argues with itself; the disagreement is the signal. In Physics this is the strongest misread check (one wrong digit changes the computed answer).

### B7 · Sort by subject and branch

- **Item:** one question · **Worker:** SCRIPT; AGENT `b7-chem-branch-sorter` for Chemistry only.
- **Procedure:** subject and Biology branch (botany/zoology) from the paper's section headings. Chemistry: AGENT chooses physical/organic/inorganic or unsure.
- **On failure:** unsure → adjudicator → still unsure → branch whose NCERT chapters contain most of the question's key terms (SCRIPT, `search_index.keyword_rank`), `B7_BRANCH_GUESS` (normal).
- **Pitfall:** mixed cases (magnetic moment of a complex ion is inorganic content with a calculation).

### B8 · Fix bonus and dropped questions

- **Item:** each question with status bonus, dropped or multiple_accepted · 1 run · **Worker:** AGENT `b8-faulty-fixer` + SCRIPT.
- **Reads:** the question; status and key row; the exam body's notice text; up to 15 latest-edition passages chosen by keyword search.
- **Agent output:** `{"issue_reason","notice_says","proposed_answer","supporting_quote":{"passage_id","text"},"corrected_stem","corrected_options","confidence","note"}`.
- **Allowed `issue_reason`:** two_correct_options, no_correct_option, hindi_english_mismatch, error_in_question, outdated_ncert, other, unsure.
- **Checks:** supporting quote verified in the latest edition; reason allowed.
- **What continues:** downstream uses `corrected_answer` (and `corrected_stem`) provisionally. **Every** B8 output → `B8_CORRECTION` (high). The original is never overwritten.

---

## 11. Stage C · Remove duplicates

### C1 · Merge booklet codes

- **Purpose:** each question exists once. Runs only for sittings where 2+ codes were read; otherwise `skipped`.
- **Item:** one shortlisted pair (code A question, closest code B question, same sitting) · 1 run · **Worker:** SCRIPT + AGENT `c1-booklet-matcher`.
- **Procedure:**
  1. SCRIPT: normalise LaTeX and spacing for both sets; shortlist for each A question its most similar B question.
  2. AGENT: exact_same or not_exact; differing spans; option map if exact.
  3. SCRIPT: one-to-one check; count check; key consistency through the option map.
- **Agent output:** `{"verdict": exact_same|not_exact, "option_map": {"A1":"B2",…}|null, "differences":[{"a","b"}]}`.
- **Checks:** only exact_same merges; one-to-one; both codes' keys point to the same option through the map.
- **On failure:** not_exact → re-run B3 and B4 on **both** copies with note "possible misread", compare again; still not exact → adjudicator with both images, `C1_READING_FIXED` (high). Unmatched → keep separate, `C1_UNMATCHED` (normal). Key inconsistency → `C1_KEY_INCONSISTENT` (high), re-check B5 for the sitting.
- **Writes:** one record per unique question with `paper_codes` (e.g. `["A:12","B:47"]`) and `option_map`.
- **Never:** merge across sittings or years. Those relations are D9–D11's job.

---

## 12. Stage D · Map to NCERT and find repeats

**The answer used in Stage D** is `corrected_answer` when B8 made one, else `official_answer`. After D7, D4 also runs for `latest_answer` if it differs, and D8–E5 use `latest_answer` (what students are taught).

Order per question: D1 → D2 → D3 → D4 → D5 → D6 → D7 → D8. Then per subtopic: D9 (per question) → D10 → D11.

### D1 · Pick the chapter

- **Item:** one question · **2 runs** · **Worker:** AGENT `d1-chapter-picker` ×2.
- **Reads:** stem, statements, lists, options; the answer (number and text); the **latest-edition** chapter list (id, title, top-level headings) for the question's subject and branch only. Never the legacy chapter.
- **Agent output:** `{"chapter_ids":[…] | ["unsure"], "why", "confidence"}`. A second chapter only if the question truly needs two.
- **Checks:** ids exist; runs agree.
- **On failure:** disagreement or unsure → adjudicator → `D1_ADJUDICATED` (normal). Adjudicator unsure → run A's choice if any, else the chapter `search_index.keyword_rank` ranks first, `D1_GUESS` (high).
- **Pitfall:** the legacy sheets put many 2018–2019 questions in the wrong chapter and use coaching chapter names; that is exactly why this step never sees them.

### D2 · Pick the subtopic

- **Item:** one question · **2 runs** · **Worker:** AGENT `d2-subtopic-picker` ×2.
- **Reads:** the question; the answer; that chapter's subtopic list (id, name, one-line description). For two chapters, both lists.
- **Agent output:** `{"subtopic_ids":[…] | ["unsure"], "why", "confidence"}`; two only if the question compares or combines them.
- **Checks:** ids exist in the (draft or approved) list; runs agree.
- **On failure:** as D1 → `D2_ADJUDICATED` (normal) / `D2_GUESS` (high).

### D3 · Fetch the passages

- **Item:** one question · **Worker:** SCRIPT (`fetch_passages.py`).
- **Procedure:** (a) latest passages linked to the subtopics; if > 15, rank by word overlap with stem + answer and keep 15; (b) their older partners from A6; (c) every older passage of the same chapter tagged `none` (possible deleted content); (d) for Physics/Chemistry, lab-manual passages whose words match the question.
- **On failure:** zero latest passages → re-run D2 once with note "previous subtopics had no passages"; still zero → `blocked`, `D3_NO_PASSAGES` (blocker).
- **Writes:** `steps/D3/out/<QID>.json` with three lists: `latest`, `older`, `lab_manual`.

### D4 · Quote the evidence

- **Purpose:** prove where the answer comes from in NCERT, and record how the question connects.
- **Item:** one question × one answer · 1 run (+ retry) · **Worker:** AGENT `d4-evidence-quoter` + SCRIPT.
- **Reads:** the question; `answer_to_support` (number + text); D3 latest passages (id + full text); the owner's link-type guidance `codebook/D4_link_type.md` **only if that file exists**.
- **Agent output:**

```json
{
  "link_type": "rule_used",
  "evidence": [{"for": "rule", "passage_id": "PHY12L-CH03-P08", "exact_line": "R = \\rho \\frac{l}{A}"}],
  "derivation_steps": ["volume constant, so A' = A/2 when l' = 2l", "R' = rho(2l)/(A/2) = 4R = 16 ohm"],
  "supports_answer": "fully",
  "missing": [],
  "note": ""
}
```

- **link_type values** (from the real-paper analysis, Section 2.4):

| Value | Use when | What is quoted | Real example |
|---|---|---|---|
| `states_answer` | One NCERT line states the answer (most Biology) | that line | Kepler's T ∝ R^{3/2} (`2026-Jun#14`) |
| `rule_used` | One NCERT rule plus plain maths | the rule | terminal voltage V = E − Ir (`2026-May#21`); stretched wire (`2013#15`) |
| `rules_chained` | Two or more NCERT rules one after another | one quote per rule | photon vs electron momentum (`2026-Jun#19`); black-hole radius from escape speed (`2014#11`) — an unfamiliar story is **not** beyond NCERT |
| `concept_applied` | NCERT explains the idea; the question applies it to a new case without calculation | the concept line | metre bridge with cell and galvanometer interchanged (`2026-May#22`) |
| `beyond_ncert_method` | Needs a result or method NCERT doesn't give | the NCERT rules that are involved, if any | field at the centre of a loop split into unequal arcs (`2026-Jun#11`) |

- **Quote rules:** one continuous span from one passage per quote; shortest span that states the fact/rule; no ellipses; one quote per statement for statement questions, including the line that shows a false statement is false; for match questions one quote per pair used.
- **`derivation_steps`:** only algebra, arithmetic, unit conversion or logic. A step that needs a physics/chemistry fact needs its own quote (or the type is `beyond_ncert_method`). The last step ends at the answer value. Empty for `states_answer`.
- **`supports_answer`:** `fully` = every needed part and every rule used in the steps is quoted; `partly`; `not_at_all` (with `evidence: []`).
- **Checks:**
  1. every `exact_line` found word for word in its passage (`quote_verify.find`);
  2. `passage_id` is one of the inputs;
  3. `link_type` allowed; `rule_used` has ≥ 1 quote with `for: "rule"`; `rules_chained` has ≥ 2; `states_answer` has no derivation steps;
  4. statement questions marked `fully` have a quote per statement;
  5. **derivation cross-check** (numericals): parse the last step's value and compare with the answer option's value (and with B6's working when present); mismatch → `D4_DERIVATION_MISMATCH` (normal).
- **On failure:** quote not found → retry with "Quote N not found in passage P; copy exactly"; still not found → drop it, downgrade `supports_answer`, `D4_QUOTE_NOT_FOUND` (high). `partly` → `D4_PARTLY` (normal). `not_at_all` → `D4_NO_SUPPORT` (normal). `beyond_ncert_method` → `D4_BEYOND_NCERT` (normal; agents may overuse it).

### D5 · Find the line in the older NCERT

- **Item:** one question · 1 run (+ retry) · **Worker:** AGENT `d5-older-line-finder` + SCRIPT.
- **Reads:** question; answer; D4's verified lines (or none); D3's older passages.
- **Agent output:** `{"older":[{"for","passage_id","exact_line"}],"none_for":[…],"note"}`; same `for` labels as D4.
- **Checks:** every older line found word for word in the **older** edition.
- **On failure:** retry; drop, `D5_QUOTE_NOT_FOUND` (normal).

### D6 · Latest NCERT or outside NCERT?

- **Item:** one question · **Worker:** SCRIPT decides status; AGENT `d6-status-note-writer` writes the note; SCRIPT verifies.
- **Status rules (SCRIPT, first match wins):**
  0. D4 `link_type` ∈ {rule_used, rules_chained, concept_applied} with ≥ 1 verified rule quote → `latest_ncert`.
  1. D4 has verified latest lines → `latest_ncert`.
  2. Else a verified lab-manual line exists → `lab_manual`.
  3. Else D5 has a verified older line in a passage on `deleted_topics.csv` → `deleted_content`.
  3b. Else D5 has a verified older line in a passage that has a change-log entry → `latest_ncert`, note type decided by D7.
  4. Else → `outside_ncert`; if `link_type = beyond_ncert_method`, note type `outside_rules`.
- **Agent task:** write the note in the template for the status (Section 3.1), quoting lines exactly; choose `written_differently` only when the older line states the **same fact** in different words.
- **Agent output:** `{"syllabus_status","note_type","reason_note","quoted_lines":[{"edition","passage_id","text"}]}`.
- **Checks:** every quoted line exists in the edition it names; note matches its template.
- **On failure:** retry; then SCRIPT fills the template from verified lines, `D6_TEMPLATE_NOTE` (low). Note types written_differently, deleted, outside, outside_rules → `D6_NOTE_APPROVAL` (normal).
- **Real examples:** `2015#180` (venue of the 2012 UN climate conference) is `outside_ncert`, never `deleted_content`; old Polymers or Solid State questions are expected `deleted_content` once Stage A confirms the removal; salt-analysis questions (2026 May) are expected `lab_manual`.

### D7 · Check the answer against the latest NCERT

- **Runs for:** every question whose D4/D5 passages have a change-log entry, and every question whose older line differs from its latest line. Others → `skipped` with `latest_answer = official answer`.
- **Item:** one question · 1 run · **Worker:** AGENT `d7-latest-answer-checker` + SCRIPT.
- **Reads:** question, options, official answer, D4 lines, D5 lines, change-log entries on those passages. **No coaching material, no B6 output.**
- **Agent output:** `{"latest_answer","same_as_official","quote","change_id","sentence_for_note","note"}`.
- **Checks:** quote verified in the latest edition; `change_id` exists and covers an evidence passage.
- **On failure / results:** `same_as_official: false` → always `D7_ANSWER_CHANGED` (high), note type becomes `answer_changed`, sentence appended, and D4 re-runs for `latest_answer`. No change-log entry explains it → `D7_UNEXPLAINED_CHANGE` (high).

### D8 · Write the fact line

- **Item:** one question · 1 run · **Worker:** AGENT `d8-fact-line-writer`.
- **Reads:** question; latest answer; subtopic; D4 evidence.
- **Agent output:** `{"fact_line","facts":[…],"confidence"}`.
- **Style:** present tense, subject first, NCERT's term, no option numbers, no "which of the following". Numericals: "Problem: <setup in general terms>. Rule: <formula>." with no specific numbers. Statement questions: the fact of each **true** statement joined by " | ".
- **On failure:** low confidence → `D8_LOW_CONFIDENCE` (low).

### D9 · Find possible repeats

- **Item:** one question · 1 run · **Worker:** AGENT `d9-repeat-finder`.
- **Reads:** this question's id, year, fact line, facts; a table of every other question in the same subtopic(s) from **other years**: id, year, sitting, fact line.
- **Agent output:** `{"possible_repeats":[…], "none": true|false}`.
- **Rule:** inclusive. If unsure, include. Every question runs D9, so links are seen from both sides; a one-sided link is kept.
- **Checks:** ids exist, same subtopic, other year.

### D10 · Build candidate groups

- **Item:** one subtopic · **Worker:** SCRIPT (`build_groups.py`): union-find over D9 links; one candidate group per connected component; each question in at most one group per subtopic. No judgement.

### D11 · Confirm each group

- **Item:** one candidate group · **2 runs** · **Worker:** AGENT `d11-group-confirmer` ×2 + adjudicator.
- **Reads:** every member's id, year, sitting, first 300 characters of stem, answer text, fact line.
- **Agent output:** `{"groups":[{"fact_line","first","members":[{"id","label"}]}],"related":[{"id","related_to"}],"removed":[…]}`.
- **Labels:** first, exact_same, reworded, same_fact_new_format, same_problem_new_numbers (repeats); same_concept_different_fact → `related`; different → `removed`. Labels are relative to the **earliest** member.
- **Checks:** every member exactly once; first = earliest year/sitting; groups ≥ 2 members; runs agree.
- **On failure:** disagreement → adjudicator → `D11_ADJUDICATED` (normal).
- **Real pairs for orientation:** `2013#136`→`2016-P2#108` exact_same; `2015#125`→`2019#120` reworded; `2017#106`→`2026-May#179` same_fact_new_format; `2016-P1#40`→`2018#28` same_problem_new_numbers; `2013#7` (n-type) vs `2019#33` (p-type) related, **not** reworded.
- **Writes:** `repeat_group_id`, `repeat_label`, `related_ids` on each record.

---

## 13. Stage E · Tag

### 13.0 Codebooks: the owner writes them, you use them if present

The owner will write tagging codebooks later. You must **not** write, generate or guess a codebook.

- The runner looks for `codebook/E1.md`, `codebook/E2.md`, `codebook/E3.md`, `codebook/E4.md`, `codebook/E5.md`, `codebook/E6.md`, `codebook/D4_link_type.md`, `codebook/D11.md`.
- **If a file exists**, the runner passes its full text to the agent as the `codebook` field, and records its file hash as `codebook_version` on every tag it produced.
- **If a file is missing**, the agent receives only the allowed values with their one-line definitions from `config/allowed_values.yaml` (Section 17), and `codebook_version = "none"`.
- When a codebook file is added or changed later, the cascade re-runs the steps that used it (Section 15).
- E4 (thinking) is the exception that needs a codebook to be useful: until `codebook/E4.md` exists, E4 runs with the eight draft categories and their one-line definitions, and every E4 output gets `E4_NO_CODEBOOK` (low).

**The five tags answer five different questions; never mix them:**

| Tag | Question |
|---|---|
| E1 question_type | How is the question **built**? |
| E2 format | What must the student **pick**? |
| E3 content_shape | What **NCERT material** is it built on? |
| E4 thinking | What must the student do **in their head**? |
| E5 trap | Why does each **wrong option** attract? |
| E6 descriptive | stem context, answer form, negation, item count, constants given, figure role |

### E0 · Discover categories from real papers

- **Purpose:** give the owner data for writing codebooks. E0 does **not** create codebooks or change allowed values.
- **Worker:** AGENT `e0-open-look` (per question), AGENT `e0-category-grouper` (per tag), SCRIPT.
- **Sample:** ~300 questions from the most recent papers available (both 2026 papers, plus 2021–2025 once collected), ~100 per subject, across many chapters.
- **Procedure:**
  1. `e0-open-look`: with **no categories shown**, complete "To get this right, the student must ___" and describe in free words how the question is built, what it asks to pick, what NCERT material it uses, and why each wrong option might attract.
  2. `e0-category-grouper`: per tag, group the free answers; compare with the allowed values; mark keep / new / merge / drop; counts per subject; years seen; 2 example question ids.
  3. SCRIPT: export `codebook/E0_findings/category_sheet.csv` with columns `tag, category, definition, subjects, example_1, example_2, count_physics, count_chemistry, count_biology, years_seen, decision`.
- **Flags:** `E0_FINDINGS_READY` (normal), one per tag, so Stage F shows them to the owner.
- **Never:** write `codebook/E*.md`. Those are the owner's.

### E1 · Question type

- **Item:** one question · **Worker:** SCRIPT patterns first (`type_patterns.py`); AGENT `e1-type-tagger` only when no pattern decides.
- **Patterns (apply in this priority order; first match wins):**
  1. "Assertion" → `assertion_reason`
  2. "Statement I"/"Statement-I"/"two statements" (without Assertion) → `statement_i_ii`
  3. "Column III" or three-column rows → `match_three_columns`
  4. "List-I"/"List I"/"Column I"/"Match" with two lists → `match_the_lists`
  5. "correctly matched"/"wrongly matched"/"mismatch"/"correct match"/"incorrectly paired", options are single pairs → `pair_options`
  6. "arrange"/"sequence"/"correct order of events|steps|stages" → `arrange_in_order`
  7. "(increasing|decreasing|correct) order of <property>"/"largest to smallest" → `rank_by_property`
  8. B3 `structure = statements` with combination options → `list_of_statements`
  9. reaction arrow or scheme image in the stem, asking for X/Y/Z/product/reagent/name → `reaction_scheme`
  10. options are images: graphs → `graph_options`; structures → `structure_options`
  11. figure with letter labels A–D to identify → `diagram_labelled`
  12. figure referred to and needed → `figure_to_read`
  13. "____" → `fill_in_blank`
  14. "…are respectively" where the **answer** has two or more parts → `multi_part_respectively`
  15. options are full statements to judge → `statement_options`
  16. otherwise → `single_statement`
- **Agent output:** `{"question_type","new_description","confidence"}`.
- **On failure:** `new_type` → `E_NEW_CATEGORY` (normal) with the description.
- **Boundaries seen in real data:** "Two statements A and B" with no because-link (`2026-May#25`) is `statement_i_ii`, although the legacy sheet called it Assertion-Reason; "how many plants among …" (`2015#130`) is `single_statement` (items, not statements); "…two arms are 5 Ω and R Ω respectively" (`2014#27`) is **not** `multi_part_respectively`; "correct order of organisation of genetic material from largest to smallest" (`2015#161`) is `rank_by_property`, not `arrange_in_order`.

### E2 · Format

- **Item:** one question · 1 run · **Worker:** AGENT `e2-format-tagger` + SCRIPT guard.
- **Key test:** look at the **options**: what kind of thing differs between them?
- **Agent output:** `{"format","new_description","confidence"}`.
- **Negative-word guard (SCRIPT):** if B3's `negative_words_seen` is non-empty (NOT, EXCEPT, INCORRECT, FALSE, WRONG, MISMATCH) and the options are single items or statements, the format must be `pick_incorrect` or `odd_one_out`; if the options are combinations or match codes, the format stays `pick_correct_combination` / `pick_match_code` and the negative is recorded in E6. If the stem has no negative word, the format must not be `pick_incorrect`.
- **On failure:** guard fails → retry with "The stem contains <word>"; then adjudicator → `E2_NEGATIVE_GUARD` (high).
- **Boundaries seen in real data:** "How many grams of HNO₃…" (`2013#50`) is `calculate_value`, not `count_correct`; "not a stem modification" (`2016-P1#121`) is `odd_one_out`, while "Select the incorrect statement" is `pick_incorrect`; "proportional to the cube of temperature… Cp/Cv is" (`2013#22`) is `calculate_value`, not `pick_proportionality`; "Humboldt described for the first time:" (`2017#111`) is `name_or_identify`, not `pick_scientist_or_date`.

### E3 · Content shape

- **Item:** one question · 1 run · **Worker:** AGENT `e3-shape-tagger`.
- **Reads:** question; D4 evidence lines **with their passage kinds**. Judge the NCERT material, not the question's layout.
- **Agent output:** `{"content_shape","why","new_description","confidence"}`.
- **On failure:** new → `E_NEW_CATEGORY`; medium confidence → `E3_MEDIUM` (low).

### E4 · Thinking

- **Item:** one question · **2 runs** · **Worker:** AGENT `e4-thinking-tagger` ×2 + adjudicator.
- **Reads:** question; latest answer; D4 evidence; `codebook` (owner's `codebook/E4.md` if present, else the eight draft categories from Section 17).
- **Agent output:** `{"primary","secondary","why","confidence","codebook_version"}`.
- **Tie-break:** primary = whatever makes the question hard; at most one secondary.
- **Checks:** values from the given list; runs agree on primary and on whether a secondary exists; confidence not low.
- **On failure:** adjudicator → `E4_ADJUDICATED` (normal). No codebook file → also `E4_NO_CODEBOOK` (low).

### E5 · Traps

- **Item:** one wrong option of one question (3 per question) · **2 runs each** · **Worker:** AGENT `e5-trap-tagger` ×2 + adjudicator.
- **Reads:** question; latest answer; the **one** wrong option; D4 evidence; change-log entries on the evidence passages (so `old_ncert_fact` can be recognised).
- **Agent output:** `{"option","trap","why","new_description","confidence"}`.
- **On failure:** disagreement → adjudicator → `E5_ADJUDICATED` (normal); new → `E_NEW_CATEGORY`.

### E6 · Descriptive tags

- **Item:** one question · **Worker:** SCRIPT (`describe_tags.py`); AGENT `e6-context-tagger` only for `stem_context` when patterns don't decide.
- **SCRIPT fills:** `answer_form` (from parsed options), `negation` (from `negative_words_seen`: none/single/double), `item_count` (lettered statements or list rows only; items inside one sentence count as 0), `constants_given` ("Given:", "[Take …]", "(At. no. …)"), `figure_role` (none / needed / decorative / options_are_figures), and `stem_context` by patterns ("a student", "experiment", "observed", a table in the stem, a reaction arrow, an equation to use, a scientist or date).
- **Agent output (stem_context only):** `{"stem_context","why","confidence"}`.
- **Rule for stem_context:** if two apply, choose the one the question cannot be answered without (e.g. "A biologist studied rats… natality 250…" is `data_given`, not `case_scenario`).
- **On failure:** `E6_CONTEXT_UNSURE` (low).

### Legacy fields

`legacy_match.py` matches each bank question to the legacy sheets by text similarity (≥ 0.85 on word 3-grams after normalisation, same year) and stores `legacy_chapter`, `legacy_topic`, `legacy_question_type`. These are never inputs to any agent. Stage F shows them beside the pipeline's values.

---

## 14. Stage F · Final review, editing, cascade, counts, release

Stage F is the only place people work. You build the pack, wait for decisions **between commands**, then apply them.

### F1 · Build the review queue and pack

- **Worker:** SCRIPT (`build_review_pack.py`).
- **Collect:** every open flag; an **audit sample** of `pass` items (5% per step, at least 20 per step per run, stratified by subject and year, fixed random seed); every draft needing approval; in the first full review, the E4 agreement sample (50 questions per subject shown **without** agent tags).
- **Order:** (1) blocker; (2) book and paper registers; (3) subtopic lists and change-log rows; (4) high (answers, keys, misreads, evidence, changed answers, corrections); (5) normal; (6) E0 findings and new categories; (7) low and the audit sample. Group by chapter.
- **Pack:** one HTML page per item in `review/review_pack/` with: the value in question (provisional value highlighted); the evidence (page/question image, both readings with differing spans, agent runs side by side, adjudicator choice, verified quotes with surrounding passage text); the legacy values if any; **what editing this re-runs** (from the cascade map); an approve / correct / block form that writes to `review/decisions.csv`. Also write `review/queue.csv` for spreadsheet review.

### F2 · Review and edit (people)

Reviewers approve or correct any flag, **and may edit any field of any item even if it passed**. Who reviews what: registers and intake → Ekta; subtopic lists, change log, passage cuts, answers, misreads, corrections, evidence, notes, changed answers, repeat groups, tags → faculty of that subject.

### F3 · Apply decisions and run the cascade

- **Worker:** SCRIPT (`apply_review.py`, `cascade.py`) + the runner.
- **Procedure:**
  1. Read new rows of `review/decisions.csv`.
  2. **approve** → close the flag; set the value's status `approved` with reviewer and date.
  3. **correct / edit** → write the new value as an output of step `F2` for that item (history), update the record, append to `review/corrections.jsonl`, close the flag, call the cascade.
  4. **block** → set `release_status = blocked_by_reviewer`.
  5. Cascade: map each changed field to the steps that read it (Section 15), mark them `stale` for the affected items, follow transitively, then run the stale (item, step) pairs **in stage order** with the normal runner. Re-runs whose output equals the previous output raise no flag; flags that no longer apply are set `auto_closed`.
  6. Rebuild the pack with `--new-only`.

### F4 · Compute the counts

- **Worker:** SCRIPT (`compute_counts.py`).
- **Per subtopic:** `unique_questions` (each repeat group counted once), `questions_total`, `years_asked`, `last_asked`, `category_mix_recent` (primary thinking since 2021), `format_mix_recent`, `question_type_mix_recent`, `repeat_groups` (≥ 2 members). Compute twice: all questions and released only.
- **Check:** totals equal the number of question–subtopic links. Never edit counts by hand.

### F5 · Release and export

A chapter is released when: its queue is empty; its subtopic list and change-log rows are approved; its audit sample meets the targets; and Ekta has a row in `review/releases.csv`. Then `export_tables.py` writes released rows to `data/`. Later corrections go through F2–F4 and re-export.

### F6 · Gold set and scoring (pilot only, then every run)

1. From the reviewed pilot, choose 90 questions (30 per subject) spread across years, formats and the pilot chapters.
2. A reviewer confirms **every** field of each (not only flagged ones).
3. Save `gold/gold_set.csv`.
4. `score_gold.py` compares each step's output with the gold values and writes `gold/scores.md` against the targets in Section 1.1 and each step's target.

---

## 15. Cascade map

When a field changes (Stage F edit, prompt version bump, new codebook file), these steps become `stale` for the affected items, then whatever reads **their** outputs, transitively.

| Changed | Re-run |
|---|---|
| Book register (edition, reprint) | A2–A9 for that book; D3–D7, E3, E5 for questions citing it |
| Passage cuts or text | A4–A9 for the chapter; D3 onward for questions in the chapter |
| Subtopic list | A5 for the chapter; D2 onward for questions in the chapter; F4 |
| Passage → subtopic link | A6, A7 for the chapter; D3 onward for questions in that subtopic |
| Pair | A7–A9 for the pair; D5–D7 for questions citing either passage |
| Change-log row | D6, D7, E5, F4 for its affected questions |
| Paper register | B5 onward for that paper |
| Question boundaries | B3 onward for that question |
| Question text/options | B6, B7, D1 onward, E1–E6, F4 |
| Official answer or status | B6, B8, D1 onward, E4, E5, F4 |
| B8 correction | D1 onward, E1–E6, F4 |
| Subject/branch | D1 onward, F4 |
| Chapter | D2 onward, F4 |
| Subtopic | D3–D8, E3–E5 for the question; D9–D11 and F4 for the old and new subtopic |
| Evidence | D5–D8, E3–E5; D9–D11 and F4 for the subtopic |
| Older line | D6, D7 |
| Status/note | D7 |
| Latest answer | D4 (for the new answer), D8, E4, E5; D9–D11 and F4 for the subtopic |
| Fact line | D9–D11, F4 for the subtopic |
| Repeat groups | F4 |
| A codebook file added/changed | the step that reads it, for every question; F4 |
| Allowed value renamed/merged/split | that tag's step on affected questions; F4 |
| Any E tag | F4 |

Write this as `config/cascade.yaml` (Appendix D) and make `cascade.py` derive the same answer from each step's `input_fields` in `steps.yaml`; a test (T25) checks the two agree.

---

## 16. Flag catalogue

| Code | Step | Severity | Raised when | Provisional value |
|---|---|---|---|---|
| S0_MISSING_INPUT | 0 | blocker | required input missing | — |
| A1_REGISTER_DRAFT | A1 | low | every book row | the row |
| A1_REPRINT_NOT_FOUND | A1 | high | no reprint line found | unknown |
| A1_EDITION_MISMATCH | A1 | high | edition ≠ manifest | manifest edition |
| A2_JOIN_ADJUDICATED | A2 | normal | continuation flags disagreed | adjudicated join |
| A2_TEXT_MISMATCH | A2 | normal | vision ≠ text layer | text layer |
| A2_UNREADABLE | A2 | blocker | page unreadable | — |
| A2_SPECIAL_UNREAD | A2S | normal | table/figure/equation unread | crop only |
| A3_DEFAULT_CUTS | A3 | normal | cuts failed twice | one passage per block |
| A4_SUBTOPICS_DRAFT | A4 | normal (high if runs < 70% matched) | every chapter | adjudicated list |
| A5_UNSURE | A5 | normal | subtopic unclear | none |
| A6_WEAK_PAIR | A6 | normal | weak and unsure | pair |
| A8_ADJUDICATED | A8 | normal | runs disagreed | adjudicated type |
| A8_FACT_CHANGE | A8 | normal | any non-wording change | the change |
| A8_WORDING_RISK | A8 | normal | wording-only that could flip an answer | wording_only |
| B1_REGISTER_DRAFT | B1 | low | every paper row | the row |
| B1_MANIFEST_MISMATCH | B1 | normal | cover ≠ manifest | cover |
| B2_BOUNDARY_ADJUDICATED | B2 | normal | boundaries disagreed | adjudicated |
| B2_MISSING_QNO | B2 | blocker | question number missing | — |
| B3_OPTION_COUNT | B3 | blocker | ≠ 4 options after re-join | — |
| B3_UNREADABLE | B3 | blocker | unreadable | — |
| B3_DUPLICATE_OPTIONS | B3 | high | two options identical | as read |
| B4_MISMATCH_ADJUDICATED | B4 | high (number/unit/sign/label/negative) or normal | readings differ | adjudicated text |
| B5_KEY_ROW_MISSING | B5 | blocker | no key row | — |
| B5_KEY_ADJUDICATED | B5 | high | key copy ≠ text layer | adjudicated |
| B6_DISAGREES_WITH_KEY | B6 | high | blind answer ≠ key | official answer |
| B7_BRANCH_GUESS | B7 | normal | branch unsure | keyword branch |
| B8_CORRECTION | B8 | high | every faulty question | proposed correction |
| C1_READING_FIXED | C1 | high | codes differed, reading corrected | corrected text |
| C1_UNMATCHED | C1 | normal | no one-to-one partner | separate |
| C1_KEY_INCONSISTENT | C1 | high | keys disagree via map | — |
| D1_ADJUDICATED / D2_ADJUDICATED | D1/D2 | normal | runs disagreed | adjudicated |
| D1_GUESS / D2_GUESS | D1/D2 | high | adjudicator unsure | run A / keyword rank |
| D3_NO_PASSAGES | D3 | blocker | none after re-running D2 | — |
| D4_QUOTE_NOT_FOUND | D4 | high | quote not found after retry | dropped |
| D4_PARTLY | D4 | normal | partial support | partly |
| D4_NO_SUPPORT | D4 | normal | no latest support | not_at_all |
| D4_DERIVATION_MISMATCH | D4 | normal | last step ≠ answer or B6 | as given |
| D4_BEYOND_NCERT | D4 | normal | beyond_ncert_method | outside_rules note |
| D5_QUOTE_NOT_FOUND | D5 | normal | older quote not found | dropped |
| D6_TEMPLATE_NOTE | D6 | low | template used | template note |
| D6_NOTE_APPROVAL | D6 | normal | written_differently / deleted / outside / outside_rules | the note |
| D7_ANSWER_CHANGED | D7 | high | latest ≠ official | both kept |
| D7_UNEXPLAINED_CHANGE | D7 | high | no change-log entry explains it | both kept |
| D8_LOW_CONFIDENCE | D8 | low | | the line |
| D11_ADJUDICATED | D11 | normal | runs disagreed | adjudicated groups |
| E0_FINDINGS_READY | E0 | normal | per tag | — |
| E_NEW_CATEGORY | E1–E5 | normal | a "new_…" answer | new_…:<description> |
| E2_NEGATIVE_GUARD | E2 | high | format conflicts with a negative word | adjudicated |
| E3_MEDIUM | E3 | low | medium confidence | the shape |
| E4_ADJUDICATED | E4 | normal | runs disagreed / low confidence | adjudicated |
| E4_NO_CODEBOOK | E4 | low | no codebook/E4.md yet | draft categories |
| E5_ADJUDICATED | E5 | normal | runs disagreed | adjudicated |
| E6_CONTEXT_UNSURE | E6 | low | | best guess |
| AUDIT_SAMPLE | any | low | random pass item | the value |

---

## 17. Allowed values (v0.1, from the real-paper analysis)

These are **lists with one-line definitions**, not codebooks. Write them to `config/allowed_values.yaml` (Appendix D). Every list that ends with "new_…" grows: a new value is added only after Stage F names it.

### 17.1 Fixed lists

- sitting: MAIN, PH2, REEXAM, RETEST, CANCELLED
- subject / branch: Physics; Chemistry (physical, organic, inorganic); Biology (botany, zoology)
- official_status: normal, bonus, dropped, multiple_accepted
- issue_reason: two_correct_options, no_correct_option, hindi_english_mismatch, error_in_question, outdated_ncert, other
- structure (B3): plain, statements, list, match, table, assertion_reason, statement_i_ii
- supports_answer: fully, partly, not_at_all
- link_type: states_answer, rule_used, rules_chained, concept_applied, beyond_ncert_method
- syllabus_status: latest_ncert, lab_manual, deleted_content, outside_ncert
- note_type: same_both, written_differently, answer_changed, deleted, outside, outside_rules, lab_manual
- change_type: fact_changed, fact_removed, fact_added, wording_only
- repeat_label: first, exact_same, reworded, same_fact_new_format, same_problem_new_numbers (+ related: same_concept_different_fact; removed: different)
- confidence: high, medium, low

### 17.2 E1 question_type

| Value | One-line definition |
|---|---|
| single_statement | One stem, four short options |
| statement_options | Each option is a full statement to judge |
| list_of_statements | Lettered statements in the stem; options are combinations or a count |
| statement_i_ii | Exactly two statements; options are true/false combinations |
| assertion_reason | Assertion and Reason; options include whether R explains A |
| match_the_lists | Two lists; options are match codes |
| match_three_columns | Three columns: item · property · group |
| pair_options | Each option is one pair; pick the correct/wrong match |
| arrange_in_order | Order of events or steps in time |
| rank_by_property | Order by a property (size, energy, acidity…) |
| fill_in_blank | Stem has a blank "____" |
| diagram_labelled | Figure with letter labels to identify |
| figure_to_read | Figure, circuit or graph needed to answer |
| graph_options | The options are graphs or figures |
| structure_options | The options are chemical structures |
| reaction_scheme | A reaction or sequence is shown; identify X/Y/Z, product, reagent or name |
| multi_part_respectively | The answer has two or more parts given together |
| list_of_structures | A lettered/numbered list in the stem whose items are drawn structures or figures to judge/count, not text statements (e.g. "how many of structures i–vii obey rule X") — added 2026-10-09, confirmed on a real 2023 Chemistry question |
| new_type | none fits |

**Labelling conventions (added 2026-10-09):** a two-statement judge-each item labelled "A" and "B" is the same structure as `statement_i_ii` (labelled "I"/"II") — tag it `statement_i_ii` regardless of the label style used. A question may need two E1 tags at once (e.g. a `fill_in_blank` stem that also requires reading a figure) — record both rather than forcing one.

### 17.3 E2 format

| Value | What the student picks |
|---|---|
| pick_correct | the one true option |
| pick_incorrect | the false statement (NOT, EXCEPT, wrong, false, mismatch) |
| count_correct | how many listed items or statements satisfy a condition |
| pick_correct_combination | a combination of lettered items |
| pick_match_code | an A-?, B-?, … code |
| pick_order | a sequence or ranking |
| odd_one_out | the item not in a group or without a property |
| calculate_value | a number |
| derive_expression | a formula in given symbols |
| pick_ratio | a ratio |
| pick_proportionality | "∝ …" |
| name_or_identify | a name or term |
| identify_structure_or_compound | a compound or structure |
| predict_product | the product of a given reaction (forward direction: reactant + reagent → product) |
| identify_reactant | the starting reactant, given the product(s) and reagent (backward direction) — added 2026-10-09, confirmed on a real 2022 Chemistry question asking for X given O3/Zn-H2O and the two products |
| identify_reagent_or_condition | reagents, catalysts or conditions |
| identify_reaction_or_process_name | the name of a reaction or process |
| classify_into_group | the group, kingdom, phylum, class or family |
| pick_explanation | the reason (because, due to, most appropriate explanation) |
| predict_effect | what happens or stays constant when something changes |
| pick_graph | a graph |
| judge_two_statements | the truth of Statement I and II |
| judge_assertion_reason | A, R and whether R explains A |
| pick_scientist_or_date | a person or date |
| expand_abbreviation | a full form |
| new_format | none fits |

### 17.4 E3 content_shape

one_line, list, example_list, table, diagram, labelled_diagram, graph, formula, derived_result, experiment_classic, practical_procedure, comparison, process, cycle_or_pathway, life_cycle, exception, classification_hierarchy, definition_term, trend, reaction_mechanism, structure_chemical, nomenclature_rule, value_or_data, scientist_history, applied_context, biological_equation, disease_cause, current_affairs, new_shape.

One-line definitions for the less obvious ones: `derived_result` = a result NCERT derives (not just states); `practical_procedure` = a lab-manual procedure; `cycle_or_pathway` = a metabolic/physiological cycle; `trend` = a periodic or structural trend; `value_or_data` = a number, size or percentage stated in NCERT; `applied_context` = an application NCERT describes; `current_affairs` = time-bound fact in no edition (always outside NCERT).

### 17.5 E4 thinking (draft, until `codebook/E4.md` exists)

| Category | One-line definition |
|---|---|
| recall | one fact decides the answer |
| elimination | several separate statements must each be judged |
| process | getting an order or chain right is the hard part |
| confusion | the question explicitly contrasts similar things |
| reasoning | judge whether a "because" holds |
| diagram_graph | a figure or graph must be read |
| application | apply an NCERT rule to a case NCERT doesn't describe |
| numerical | choose a formula and calculate |

**Candidates seen in real papers** (for E0 and the owner, not for E4 until a codebook includes them): trend_ranking, classification, proportional_reasoning, estimation, symbolic_derivation, spatial_structural, data_interpretation, experimental_reasoning, multi_concept.

**Confirmed from a 10-paper sample, 2016–2025, ~500 questions (2026-10-09) — rules for whoever applies this table, human or agent:**
- **Never key a Chemistry prior off the subject label alone.** Physical-chemistry questions (kinetics, equilibrium, electrochemistry, solutions) behave like Physics — numerical/application-dominated. Organic/inorganic questions behave like Biology — recall/elimination-dominated. This split held across every year sampled. Condition the `thinking` prior on B7's branch output (physical/organic/inorganic), not on "Chemistry" as one bucket.
- **Biology is rarely `numerical`, not never.** Confirmed real counter-examples (PCR's `2^n`, a dihybrid-cross phenotypic ratio) — don't hard-code Biology to exclude `numerical`.
- **`thinking` cannot be shortcut from `question_type`, `format`, or subject — it needs a per-question read every time.** Confirmed both directions: a Physics Assertion–Reason question needed a real calculation inside the A/R judgement (not just `reasoning`), and a Biology question that *looked* numerical ("how many molecules of ATP and NADPH") was pure memorised recall with no calculation at all.

### 17.6 E5 trap

look_alike_term, wrong_pairing, half_true, wrong_order, ignores_exception, extreme_word, old_ncert_fact, opposite_answer, calculation_slip, swapped_positions, number_near_miss, unit_conversion_slip, sign_or_direction, scientist_swap, name_variant, invalid_comparator, impossible_value, reversed_cause_effect, partial_combination, new_trap.

### 17.7 E6

- stem_context: plain, case_scenario, experiment_setup, real_world, data_given, table_given, figure_given, reaction_given, equation_given, historical
- answer_form: term, number_with_unit, expression, ratio, statement, combination_code, match_code, order, structure_image, graph_image
- negation: none, single, double
- item_count: integer (lettered statements or list rows)
- constants_given: yes, no
- figure_role: none, needed, decorative, options_are_figures

---

## 18. Runbook

### 18.1 Pilot run (M5, no people)

1. `/run-stage 0` (intake).
2. `/run-stage A` on **all** books (D1 needs every chapter list).
3. `/run-stage B --papers 2024-2026` (all sittings of those years).
4. `/run-stage C`.
5. `/run-step D1` on every pilot-paper question.
6. `/run-stage D --chapters PILOT` and `/run-stage E --chapters PILOT`, where PILOT = one chapter per subject chosen by the owner (Section 20). If not chosen yet, use the defaults: Biology "Cell Cycle and Cell Division" (statements, figures, a chapter near removed content), Physics "Current Electricity" (numerical-heavy, rule-based links), Chemistry an organic chapter such as "Aldehydes, Ketones and Carboxylic Acids" (reaction schemes, structure options). Record the choice in `docs/OPEN_QUESTIONS.md`.
7. `/run-step E0` on its sample.
8. `/status`; report (Section 19).

### 18.2 Pilot review (M6)

1. `/review-pack --chapters PILOT`. Report the queue size and the pack path. Stop.
2. When the owner says decisions are filled in: `/apply-review`. Repeat 1–2 until the pilot queue is empty.
3. Build the gold set (F6), run `python scripts/score_gold.py`, report `gold/scores.md`.

### 18.3 Fix and re-score (M7)

For each step under target: read its failures in `gold/scores.md`, improve the agent file (never relax a check), bump its prompt version, `/run-step <STEP> --chapters PILOT`, let the cascade re-run, re-score. Record each change in `docs/OPEN_QUESTIONS.md`.

### 18.4 Full run (M8)

`/run-stage B` (remaining in-scope papers) → `/run-stage C` → `/run-stage D` → `/run-stage E` → `/status`.

### 18.5 Full review and release

`/review-pack` chapter by chapter → owner decisions → `/apply-review` → `python scripts/compute_counts.py` → when a chapter qualifies (F5) and has a sign-off row → `python scripts/export_tables.py --chapters <ID>`.

### 18.6 Maintenance

- **New paper (e.g. 2027):** intake → B → C → D → E for its questions, then D9–D11 and F4 for every subtopic it touches → Stage F.
- **New NCERT edition (Class 11 books due 2027-28):** Stage A for the new books; A6–A9 against the current latest edition; the new books become latest; cascade re-runs D3–D7 for affected questions. Subtopics carry over by idea.
- **New or changed codebook file:** cascade re-runs the step that reads it (Section 15).

### 18.7 Recovery

- A command interrupted mid-step: run the same command again; the runner continues from what has no output (idempotence).
- An agent writes invalid JSON: the check fails and the fallback chain runs; never hand-edit the file.
- A script bug found: fix it, add a test, re-run the affected steps with `--items`; never edit outputs.

---

## 19. What to report after each command

Print, in this order and nothing else:

1. **Command and scope** (e.g. "/run-step D4 --chapters PILOT").
2. **Counts by status** for the step(s): pass, flagged, blocked, skipped, stale.
3. **New flags by severity and code** (top 10 codes).
4. **Blocked items** (ids and reasons, up to 20; then "and N more").
5. **Anything you could not implement or decided by default**, with the `docs/OPEN_QUESTIONS.md` entry number.
6. **Next command** the runbook calls for.

---

## 20. Open decisions for the owner

Write these into `docs/OPEN_QUESTIONS.md` at M0. Until decided, use the default.

| # | Decision | Default until decided |
|---|---|---|
| 1 | Include NEET 2013 and AIPMT 2014–2015 in the bank? | No: register them, `in_scope = no` |
| 2 | Collect 2020–2025 main papers, the 2020 re-exam and the 2024 retest (missing from the analysed data) | Intake flags them missing |
| 3 | Pilot chapters | Section 18.1 defaults |
| 4 | Coaching solutions: licensed? | Not licensed: reviewer reference only, never in agent inputs |
| 5 | Codebooks for E1–E6, D4 link_type, D11 | None yet: agents use Section 17 lists; E4 flags `E4_NO_CODEBOOK` |
| 6 | Hindi | English only |
| 7 | NCERT Exemplar as an extra source (would turn some beyond_ncert_method questions into linked ones) | Not used |

---

# Appendix A · `CLAUDE.md`

Create this file at the project root, word for word.

````markdown
# CLAUDE.md · NEET PYQ Pipeline

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

## Where things are
Agents `.claude/agents/` · commands `.claude/commands/` · step definitions `config/steps.yaml` · cascade `config/cascade.yaml` · allowed values `config/allowed_values.yaml` · outputs `steps/<STEP>/out/` · current question records `papers/records/` · flags `flags/flags.jsonl` · review `review/` · final tables `data/` · log `run_log.csv`.
````

---

# Appendix B · Agent files

Create one file per block in `.claude/agents/`, word for word. All agents have only Read and Write tools and `model: inherit`. The universal rules are repeated in each file because subagents do not see `CLAUDE.md`.

| Agent | Step |
|---|---|
| `a1-book-registrar` | A1 |
| `a2-page-reader` | A2 |
| `a2-special-transcriber` | A2 |
| `a3-passage-splitter` | A3 |
| `a4-subtopic-writer` | A4 |
| `a5-passage-linker` | A5 |
| `a8-change-judge` | A8 |
| `b1-paper-registrar` | B1 |
| `b2-boundary-finder` | B2 |
| `b3-question-reader` | B3 |
| `b4-second-reader` | B4 |
| `b5-key-copier` | B5 |
| `b6-blind-solver` | B6 |
| `b7-chem-branch-sorter` | B7 |
| `b8-faulty-fixer` | B8 |
| `c1-booklet-matcher` | C1 |
| `d1-chapter-picker` | D1 |
| `d2-subtopic-picker` | D2 |
| `d4-evidence-quoter` | D4 |
| `d5-older-line-finder` | D5 |
| `d6-status-note-writer` | D6 |
| `d7-latest-answer-checker` | D7 |
| `d8-fact-line-writer` | D8 |
| `d9-repeat-finder` | D9 |
| `d11-group-confirmer` | D11 |
| `e0-open-look` | E0 |
| `e0-category-grouper` | E0 |
| `e1-type-tagger` | E1 |
| `e2-format-tagger` | E2 |
| `e3-shape-tagger` | E3 |
| `e4-thinking-tagger` | E4 |
| `e5-trap-tagger` | E5 |
| `e6-context-tagger` | E6 |
| `x-adjudicator` | any |

## `.claude/agents/a1-book-registrar.md`

````markdown
---
name: a1-book-registrar
description: Step A1. Reads the first pages of one NCERT book PDF and drafts its register row (subject, class, edition, exact reprint text). Use only when the runner passes an A1 input file.
tools: Read, Write
model: inherit
---

# Book registrar · step A1

You are an agent in the NEET PYQ Data Pipeline. Every NCERT link in the bank must point to one exact printing. You record which printing this file is.

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
Look at the page images. Find the title page and the imprint/reprint line. Copy the reprint text exactly as printed. Identify subject, class, language, part and edition.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `file`: the PDF path
- `folder_edition_hint`: latest, older or lab_manual (the folder it was placed in)
- `page_images`: the first 6 pages as images
- `text_layer`: text of those pages, if the PDF has one

## Rules for this step
- The reprint line often reads like "Reprint 2026-27" or "First Edition … Reprinted …". Copy the whole line exactly.
- `reprint_page` is the 1-based page number among the images where you found it.
- `edition_seen`: say what the book itself shows. Do not just copy the folder hint.
- If you cannot find a reprint line, set `reprint_text_exact` to "" and explain in `note`.

## Allowed values
- subject: Physics, Chemistry, Biology
- class: 11, 12
- language: English, Hindi, other
- part: null, 1, 2
- edition_seen: latest, older, lab_manual, unsure

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "subject": "Biology",
  "class": 11,
  "language": "English",
  "part": null,
  "edition_seen": "latest",
  "reprint_text_exact": "Reprint 2026-27",
  "reprint_page": 2,
  "is_lab_manual": false,
  "note": ""
}
```

## Examples
Input: first pages of the Biology Class 11 latest PDF; page 2 has "Reprint 2026-27".
Output: as above.

Input: a scan where the imprint is cut off.
Output: `{"subject": "Physics", "class": 12, "language": "English", "part": 1, "edition_seen": "unsure", "reprint_text_exact": "", "reprint_page": null, "is_lab_manual": false, "note": "Imprint area cut off on page 2."}`

## Never
- Never fill in a reprint year you did not see printed.
- Never decide the edition from the file name alone.
````

## `.claude/agents/a2-page-reader.md`

````markdown
---
name: a2-page-reader
description: Step A2. Reads ONE NCERT page image into ordered text blocks and says whether the first/last block continues across the page break. Use only when the runner passes an A2 input file.
tools: Read, Write
model: inherit
---

# NCERT page reader · step A2

You are an agent in the NEET PYQ Data Pipeline. Turn one textbook page into clean text blocks, so passages can be cut and quotes can be verified word for word later.

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
List every block on the page in reading order with its kind. Copy paragraph text exactly. Mark tables, figures and equations for the special transcriber instead of transcribing them yourself. Answer the two continuation questions.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `book_id`, `page`
- `image`: the page image
- `text_layer`: the PDF text for this page, or null
- `previous_page_last_block`: kind and last ~100 characters of the previous page's last block

## Rules for this step
- Reading order: top to bottom; on two-column pages, left column first.
- When `text_layer` exists and matches what you see, copy its characters (it is exact). Read from the image only where the text layer is missing or clearly garbled.
- Remove running headers, footers and page numbers; list what you removed in `running_header_footer_removed`.
- `first_block_continues_from_previous` is true when the page starts mid-sentence, mid-table or mid-box (use `previous_page_last_block` to judge).
- `last_block_continues_on_next` is true when the page ends mid-sentence, mid-table or mid-box.
- A box ("Do you know?", activity, summary box) is its own block.
- For tables, figures and equations set `needs_special: true`, give a bounding box `[x0, y0, x1, y1]` in image pixels, and leave `text` empty.

## Allowed values
- kind: paragraph, heading, table, figure, box, equation, list

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "blocks": [
    {
      "n": 1,
      "kind": "paragraph",
      "text": "chromatids move towards opposite poles. ...",
      "continues_from_previous": true
    },
    {
      "n": 2,
      "kind": "figure",
      "needs_special": true,
      "bbox": [
        72,
        300,
        520,
        610
      ],
      "text": ""
    },
    {
      "n": 3,
      "kind": "heading",
      "text": "10.2.4 Telophase"
    }
  ],
  "first_block_continues_from_previous": true,
  "last_block_continues_on_next": false,
  "running_header_footer_removed": [
    "BIOLOGY",
    "163"
  ],
  "note": ""
}
```

## Examples
Previous page ended "…splits and the"; this page starts "chromatids move towards opposite poles." → first block `continues_from_previous: true`.

## Never
- Never describe a picture in words.
- Never merge text from the previous page into your blocks; only flag the continuation.
- Never correct spelling or grammar.
````

## `.claude/agents/a2-special-transcriber.md`

````markdown
---
name: a2-special-transcriber
description: Step A2 (special blocks). Transcribes ONE table, figure caption with labels, or equation from an NCERT page crop. Use only when the runner passes an A2-special input file.
tools: Read, Write
model: inherit
---

# Table, figure and equation transcriber · step A2

You are an agent in the NEET PYQ Data Pipeline. Tables, figure labels and equations lose their structure in plain text extraction. You copy them in a structured, exact form.

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
Depending on `kind`: table → copy it row by row; figure → write its caption and every label exactly; equation → write it in LaTeX exactly as printed.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `kind`: table, figure or equation
- `image`: the crop
- `text_layer`: text inside the crop, or null
- `table_continues_from_previous`: true if this table continues from the previous page

## Rules for this step
- Table: `header` is the header row; `rows` are the data rows; each cell copied exactly. If the table continues from the previous page and the header row is repeated, set `repeated_header: true` and still give the header.
- Figure: `caption` exactly as printed (e.g. "Figure 10.2 …"); `labels` every label word/line on the figure, top-left to bottom-right. No description of the drawing.
- Equation: `latex` exactly as printed; keep the equation number if printed, in `number`.

## Allowed values
- kind: table, figure, equation

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "kind": "table",
  "header": [
    "Feature",
    "Mitosis",
    "Meiosis"
  ],
  "rows": [
    [
      "Number of divisions",
      "One",
      "Two"
    ]
  ],
  "repeated_header": false,
  "note": ""
}
```

## Examples
Equation crop showing R = ρ l / A → `{"kind": "equation", "latex": "R = \\rho \\frac{l}{A}", "number": "(3.16)", "note": ""}` (number illustrative)

## Never
- Never compute, simplify or rearrange an equation.
- Never add cells or labels that are not printed.
````

## `.claude/agents/a3-passage-splitter.md`

````markdown
---
name: a3-passage-splitter
description: Step A3. Decides where ONE section of an NCERT chapter splits into one-idea passages, replying only with block numbers. Use only when the runner passes an A3 input file.
tools: Read, Write
model: inherit
---

# Passage splitter · step A3

You are an agent in the NEET PYQ Data Pipeline. Each passage must hold one complete idea so it can serve as evidence for a question. You choose the cuts; the script cuts, so no word can change.

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
Split this section into passages. Each passage holds one complete idea: a paragraph, a table, a figure with its caption, a box, or an equation with the lines that explain it. If a figure or box interrupts a paragraph, keep the paragraph as one passage (its two parts together) and the figure or box as its own passage. Do not rewrite anything. Reply only with the block numbers of each passage.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `book_id`, `chapter`, `section_heading`
- `blocks`: numbered blocks (n, kind, text) in reading order, already joined across page breaks

## Rules for this step
- Every block number must appear exactly once.
- A heading block belongs to the passage that follows it.
- A sentence that introduces a list belongs with the list.
- An equation and the one or two lines that explain it are one passage.
- Keep blocks in reading order inside each passage, except the paragraph-interrupted-by-figure case.

## Allowed values
- block numbers from the input only

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "passages": [
    [
      1
    ],
    [
      2,
      4
    ],
    [
      3
    ],
    [
      5
    ]
  ],
  "note": ""
}
```

## Examples
Blocks: 1 intro, 2 prophase (first part), 3 figure, 4 prophase (rest), 5 metaphase → `[[1], [2, 4], [3], [5]]`.

## Never
- Never output text, only block numbers.
- Never drop or repeat a block.
````

## `.claude/agents/a4-subtopic-writer.md`

````markdown
---
name: a4-subtopic-writer
description: Step A4. Drafts the list of NEET-testable subtopics for ONE chapter of the latest NCERT edition. Use only when the runner passes an A4 input file.
tools: Read, Write
model: inherit
---

# Subtopic writer · step A4

You are an agent in the NEET PYQ Data Pipeline. Subtopics are the shared language between past questions and student pages. Your list is a draft; faculty approve it at the end.

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
List the subtopics in this chapter that a NEET question could test. Use the book's own headings where they exist. Each subtopic is one idea a question could be about: not the whole chapter, not a single sentence. For each, give a short name, the heading it comes from, and the passage IDs it covers.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `chapter`, `chapter_title`
- `headings`: all headings with numbers
- `passages`: id, kind, first 200 characters

## Rules for this step
- Every passage must be covered by at least one subtopic.
- Prefer the book's heading wording for names.
- Usually 4–15 subtopics per chapter; a very short chapter may have fewer.
- Names describe the idea, not the page ("Stages of mitosis", not "Page 162").
- A box or figure belongs to the subtopic of the text it illustrates.

## Allowed values
- passage IDs from the input only

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "chapter": "BIO11-CH10",
  "subtopics": [
    {
      "n": 1,
      "name": "Phases of the cell cycle",
      "from_heading": "10.1",
      "passages": [
        "BIO11L-CH10-P01",
        "BIO11L-CH10-P02"
      ]
    },
    {
      "n": 3,
      "name": "Stages of mitosis",
      "from_heading": "10.2",
      "passages": [
        "BIO11L-CH10-P05",
        "BIO11L-CH10-P06",
        "BIO11L-CH10-P07"
      ]
    }
  ],
  "note": ""
}
```

## Examples
A chapter with headings 10.1 Cell cycle, 10.2 M phase (10.2.1–10.2.4 four stages), 10.3 Significance of mitosis, 10.4 Meiosis… → one subtopic per heading-level idea; the four stage sub-headings together become "Stages of mitosis" unless questions could clearly target each stage alone.

## Never
- Never invent content not in the chapter.
- Never number subtopic IDs yourself; the script assigns ST01, ST02…
````

## `.claude/agents/a5-passage-linker.md`

````markdown
---
name: a5-passage-linker
description: Step A5. Links ONE NCERT passage (either edition) to a subtopic of its chapter's latest-edition list, or none. Use only when headings did not decide and the runner passes an A5 input file.
tools: Read, Write
model: inherit
---

# Passage-to-subtopic linker · step A5

You are an agent in the NEET PYQ Data Pipeline. Every passage of both books needs a subtopic so the right passages can be fetched for each question. 'none' marks older content whose topic is no longer in the latest book.

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
Which subtopic does this passage belong to? Say none if the topic is not in the latest book.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `passage`: id, edition, kind, full text
- `subtopics`: id, name, and short descriptions for this chapter (latest edition)

## Rules for this step
- Choose the subtopic whose idea the passage explains, not one that merely shares a word.
- `none` only when no subtopic covers the idea at all.

## Allowed values
- subtopic_id: one ID from the list, none, unsure
- confidence: high, medium, low

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "passage_id": "BIO11O-CH10-P15",
  "subtopic_id": "none",
  "confidence": "high",
  "note": "Topic not present in latest chapter headings."
}
```

## Examples
An older passage describing the anaphase events → the "Stages of mitosis" subtopic.

## Never
- Never pick two subtopics.
````

## `.claude/agents/a8-change-judge.md`

````markdown
---
name: a8-change-judge
description: Step A8. Judges ONE changed pair of NCERT passages (older vs latest) as fact changed, removed, added, or wording only. Use only when the runner passes an A8 input file.
tools: Read, Write
model: inherit
---

# Edition change judge · step A8

You are an agent in the NEET PYQ Data Pipeline. The change log must separate real fact changes from rewording, because changed facts can change past answers.

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
Here is what the older book said and what the latest book says, with differences highlighted. Did a fact change, was a fact removed or added, or only the wording changed? Write the old fact and the new fact in one line each. Also say whether this change could flip the answer to a question.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `old_passage`: id and text
- `new_passage`: id and text
- `diff`: list of {old, new} spans

## Rules for this step
- `fact_changed`: the same topic now states a different claim (a number, name, stage, example, rule).
- `fact_removed`: the latest book no longer states a fact the older book stated.
- `fact_added`: the latest book states a fact the older book did not.
- `wording_only`: the meaning is the same.
- `could_flip_an_answer`: true if an 'always/only/all', 'NOT', count or matching question could have a different answer. Words like usually, always, only, all, some, never matter.
- If several kinds apply, choose the most important (fact_changed > fact_removed > fact_added > wording_only) and mention the rest in `why`.

## Allowed values
- change_type: fact_changed, fact_removed, fact_added, wording_only, unsure
- confidence: high, medium, low

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "change_type": "fact_changed",
  "old_fact": "X happens in phase 1.",
  "new_fact": "X happens in phase 2.",
  "could_flip_an_answer": true,
  "why": "The phase named for X is different.",
  "confidence": "high"
}
```

## Examples
Old "The cell divides into two daughter cells." New "The cell splits into two daughter cells." → wording_only, could_flip false.
Old "usually found in X" New "found in X" → wording_only, could_flip true (an ALWAYS question changes).

## Never
- Never treat a page-break or hyphenation difference as a change.
````

## `.claude/agents/b1-paper-registrar.md`

````markdown
---
name: b1-paper-registrar
description: Step B1. Reads the cover of ONE NEET paper or key file and drafts its register row. Use only when the runner passes a B1 input file.
tools: Read, Write
model: inherit
---

# Paper registrar · step B1

You are an agent in the NEET PYQ Data Pipeline. Every question must be traceable to an exact exam, year, sitting and booklet code. You record what the file is from its own printed cover.

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
Read the cover and first page. Copy the exam name, date, booklet/test code and any re-exam/retest/phase wording exactly as printed. Compare with the manifest row and say whether they agree.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `file`, `manifest_row` (what the collector typed)
- `page_images`: cover and first question page
- `text_layer`: if present

## Rules for this step
- `sitting` follows the printed cover. If the cover doesn't say, use the manifest and say so in `note`.
- `booklet_code` exactly as printed (e.g. A, B, P1, Q3).
- `file_kind`: paper or key.

## Allowed values
- exam: NEET, other
- sitting: MAIN, PH2, REEXAM, RETEST, CANCELLED, unsure
- file_kind: paper, key
- trust: official, memory_based, unsure

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "file_kind": "paper",
  "exam": "NEET",
  "year": 2024,
  "sitting": "RETEST",
  "booklet_code": "B",
  "language": "English",
  "trust": "official",
  "cover_text_exact": {
    "code": "Test Booklet Code: B",
    "date": "<exact text copied from the input>"
  },
  "agrees_with_manifest": true,
  "note": ""
}
```

## Examples
Manifest says MAIN, cover says "Re-Examination" → sitting REEXAM, agrees_with_manifest false, note explains.

## Never
- Never use the file name as evidence when the cover is readable.
````

## `.claude/agents/b2-boundary-finder.md`

````markdown
---
name: b2-boundary-finder
description: Step B2. Finds where each question starts and ends on ONE paper page image, including questions continuing across columns or pages. Use only when the runner passes a B2 input file.
tools: Read, Write
model: inherit
---

# Question boundary finder · step B2

You are an agent in the NEET PYQ Data Pipeline. Each question must become one complete image, even when it is split across a column or page.

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
List each question number on this page and its box(es). Say whether the text at the very top of each column belongs to a question from the previous column or page, and whether the last question continues on the next column or page.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `paper_id`, `page`, `image`
- `layout`: one_column or two_column (detected by script)
- `previous_page`: last question number and whether it was marked as continuing

## Rules for this step
- Reading order: left column top→bottom, then right column top→bottom.
- A question's box includes its number, stem, statements/lists/figure and all four options.
- Exclude section headers ("Section B"), instructions and page furniture.
- Boxes as [x0, y0, x1, y1] in image pixels; a question split between columns has two parts.

## Allowed values
- column: left, right, full

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "page": 7,
  "questions": [
    {
      "qno": 31,
      "parts": [
        {
          "column": "left",
          "bbox": [
            40,
            80,
            290,
            260
          ]
        }
      ]
    },
    {
      "qno": 35,
      "parts": [
        {
          "column": "right",
          "bbox": [
            310,
            600,
            560,
            790
          ]
        }
      ],
      "continues_on_next": true
    }
  ],
  "top_continues_from_previous": {
    "left": false,
    "right": false
  },
  "note": ""
}
```

## Examples
Top of the right column shows options (3) and (4) with no question number → `top_continues_from_previous.right: true`; those lines belong to the last question of the left column.

## Never
- Never renumber questions; copy the printed numbers.
````

## `.claude/agents/b3-question-reader.md`

````markdown
---
name: b3-question-reader
description: Step B3. Copies ONE NEET question image exactly (stem, statements, lists, four options), with all maths in LaTeX. Use only when the runner passes a B3 input file.
tools: Read, Write
model: inherit
---

# Question reader · step B3

You are an agent in the NEET PYQ Data Pipeline. The bank needs every question copied exactly. One wrong digit or a missed NOT ruins a question.

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
Copy this question exactly: the question, any statements, lists or table, and the four options. Write all maths, units, symbols and values in LaTeX. Say whether it has a figure or graph, and list any negative words exactly as printed.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `question_image`: the joined image of one question
- `paper_id`, `qno`

## Rules for this step
- Put statements (A, B, C… or I, II…) in `statements` with their labels.
- Match questions: List I items in `list_i`, List II in `list_ii`, with their labels.
- Options keyed "1"–"4" exactly as printed after (1)–(4).
- LaTeX for every number with a unit (`$4\,\Omega$`), every formula, every chemical formula (`$\mathrm{H_2SO_4}$`), every Greek letter.
- Keep bold/capitalised NOT, EXCEPT as words in the text; also list them in `negative_words_seen`.
- `figure_bbox`: box of the figure inside the image, if any.

## Allowed values
- structure: plain, statements, list, match, table, assertion_reason, statement_i_ii
- negative_words_seen: any of NOT, EXCEPT, INCORRECT, FALSE, WRONG (as printed)

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "stem_en": "A wire of resistance $4\\,\\Omega$ is stretched to twice its length. What is its new resistance?",
  "statements": [],
  "list_i": [],
  "list_ii": [],
  "options_en": {
    "1": "$2\\,\\Omega$",
    "2": "$8\\,\\Omega$",
    "3": "$16\\,\\Omega$",
    "4": "$4\\,\\Omega$"
  },
  "structure": "plain",
  "has_figure": false,
  "figure_bbox": null,
  "negative_words_seen": [],
  "note": ""
}
```

## Examples
A question with only options (1) and (2) visible → copy what is there and write in note: "Only 2 options visible; question may continue elsewhere."

## Never
- Never solve the question.
- Never fill in a blurry digit by guessing; copy what you see and mention it in note.
````

## `.claude/agents/b4-second-reader.md`

````markdown
---
name: b4-second-reader
description: Step B4. Independently re-reads ONE question image line by line when the PDF has no text layer. Use only when the runner passes a B4 input file.
tools: Read, Write
model: inherit
---

# Second reader (no text layer) · step B4

You are an agent in the NEET PYQ Data Pipeline. A second, independent reading catches misreads. You must not see or imitate the first reading.

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
Transcribe the question image line by line, top to bottom, exactly as printed. Then assemble the same fields as the first reader: stem, statements, lists, four options, LaTeX for all maths.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `question_image`, `paper_id`, `qno`

## Rules for this step
- First fill `lines`: every printed line in order, exactly. Then build the fields from those lines.
- Same LaTeX rules as the first reader: units, formulas, chemical formulas, Greek letters.
- For every number, check it digit by digit against the image.

## Allowed values
- structure: plain, statements, list, match, table, assertion_reason, statement_i_ii

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "lines": [
    "17. A wire of resistance 4 Ω is stretched to twice its length.",
    "What is its new resistance?",
    "(1) 2 Ω (2) 8 Ω",
    "(3) 16 Ω (4) 4 Ω"
  ],
  "stem_en": "<exact text copied from the input>",
  "statements": [],
  "list_i": [],
  "list_ii": [],
  "options_en": {
    "1": "<exact text copied from the input>",
    "2": "<exact text copied from the input>",
    "3": "<exact text copied from the input>",
    "4": "<exact text copied from the input>"
  },
  "structure": "plain",
  "has_figure": false,
  "negative_words_seen": [],
  "note": ""
}
```

## Examples
(Same field rules as b3-question-reader.)

## Never
- Never ask for or use any other reading of this question.
````

## `.claude/agents/b5-key-copier.md`

````markdown
---
name: b5-key-copier
description: Step B5. Copies ONE page of an official final answer key into rows of question number and answer. Use only when the runner passes a B5 input file.
tools: Read, Write
model: inherit
---

# Answer key copier · step B5

You are an agent in the NEET PYQ Data Pipeline. Each question gets its official answer from the key for its own booklet code. You only copy the printed table.

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
````

## `.claude/agents/b6-blind-solver.md`

````markdown
---
name: b6-blind-solver
description: Step B6. Solves ONE NEET question without the answer key, to catch misreads, wrong key joins and faulty questions. Use only when the runner passes a B6 input file.
tools: Read, Write
model: inherit
---

# Blind solver · step B6

You are an agent in the NEET PYQ Data Pipeline. If your independent answer differs from the official key, a person checks the text, the join and the key at the end. Your answer must be genuinely independent.

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
Answer this question. Give the option number and one line of reason. For a numerical, show the working.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `stem_en`, `statements`, `list_i`, `list_ii`, `options_en`, `figure_image` (if any)

## Rules for this step
- Choose exactly one option, or "unsure".
- If two options look correct or none does, still pick your best, set confidence low, and say so in `note` (this helps find faulty questions).
- If a value looks impossible (e.g. a 40 Ω result for an option list in single digits), say so in `note`.

## Allowed values
- answer: "1", "2", "3", "4", unsure
- confidence: high, medium, low

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "answer": "3",
  "reason": "Volume constant: R is proportional to l squared, so 4 x 2^2 = 16 ohm.",
  "working": "R' = rho(2l)/(A/2) = 4R = 16",
  "confidence": "high",
  "note": ""
}
```

## Examples
Statements question where you find C false and A, B, D true → choose the option "A, B and D only".

## Never
- Never look for or use an answer key, coaching solution or NCERT passage.
````

## `.claude/agents/b7-chem-branch-sorter.md`

````markdown
---
name: b7-chem-branch-sorter
description: Step B7. Says whether ONE Chemistry question is physical, organic or inorganic chemistry. Use only when the runner passes a B7 input file.
tools: Read, Write
model: inherit
---

# Chemistry branch sorter · step B7

You are an agent in the NEET PYQ Data Pipeline. The branch decides which chapter list D1 sees.

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
Is this physical, organic or inorganic chemistry? Say unsure if it mixes branches.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `stem_en`, `options_en`, `statements`

## Rules for this step
- physical: calculations and laws (pH, thermodynamics, kinetics, solutions, electrochemistry, states of matter, atomic structure calculations).
- organic: carbon compounds, reactions, mechanisms, named reactions, isomerism, functional groups, biomolecules and polymers as chemistry.
- inorganic: periodic properties, bonding of elements, s/p/d/f-block, coordination compounds, metallurgy, qualitative tests of ions.

## Allowed values
- branch: physical, organic, inorganic, unsure
- confidence: high, medium, low

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "branch": "organic",
  "confidence": "high",
  "why": "Asks for a reaction product of an alkene."
}
```

## Examples
"Calculate the magnetic moment of [Fe(CN)6]3-" → inorganic (coordination compounds) with confidence medium; the calculation does not make it physical.

## Never
- Never answer the question itself.
````

## `.claude/agents/b8-faulty-fixer.md`

````markdown
---
name: b8-faulty-fixer
description: Step B8. For ONE bonus, dropped or multiple-accepted question, records why it could not be marked and drafts a correction by today's NCERT. Use only when the runner passes a B8 input file.
tools: Read, Write
model: inherit
---

# Faulty question fixer · step B8

You are an agent in the NEET PYQ Data Pipeline. Every question stays in the bank. A faulty question is corrected and the reason recorded; a person approves every correction at the end.

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
Why could this question not be marked with one answer? Choose a reason. Then give the answer that is correct by today's NCERT, quoting the supporting line exactly from the passages given. If no answer can fix it, propose the smallest correction to the question or options.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- the question (stem, statements, lists, options)
- `status` and the key row
- `notice_text`: the exam body's notice, if any
- `latest_passages`: up to 15 latest-edition passages (id + text)

## Rules for this step
- Use the notice when it states a reason.
- `supporting_quote` must be copied exactly from one of the passages, with its passage_id.
- `corrected_stem` / `corrected_options` only when choosing an answer cannot fix the question; change as little as possible.

## Allowed values
- issue_reason: two_correct_options, no_correct_option, hindi_english_mismatch, error_in_question, outdated_ncert, other, unsure
- proposed_answer: "1"–"4", unsure
- confidence: high, medium, low

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "issue_reason": "two_correct_options",
  "notice_says": "Options (1) and (3) both accepted.",
  "proposed_answer": "3",
  "supporting_quote": {
    "passage_id": "BIO12L-CH04-P13",
    "text": "<exact text copied from the input>"
  },
  "corrected_stem": null,
  "corrected_options": null,
  "confidence": "medium",
  "note": ""
}
```

## Examples
No correct option because of a printing error in option (3) → issue_reason error_in_question, proposed_answer "3" with corrected_options {"3": "..."}.

## Never
- Never delete or rewrite the original question; the correction is stored beside it.
````

## `.claude/agents/c1-booklet-matcher.md`

````markdown
---
name: c1-booklet-matcher
description: Step C1. Decides whether TWO questions from different booklet codes of the same sitting are exactly the same question, and maps their options. Use only when the runner passes a C1 input file.
tools: Read, Write
model: inherit
---

# Booklet code matcher · step C1

You are an agent in the NEET PYQ Data Pipeline. Each question must appear once in the bank. Within one sitting, codes hold the same questions in a different order, so a near-match means one reading is wrong.

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
Are these two exactly the same question: same words, same numbers, same options? Ignore only formatting (spacing, LaTeX style) and the order of the options. Answer exact_same or not_exact. If not exact, list what differs. If exact, give the option mapping.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `a`: paper_id, qno, stem, statements, lists, options (normalised)
- `b`: the same for the shortlisted partner

## Rules for this step
- Every word, number, unit, sign and label must match. Formatting does not count.
- `option_map` maps each A option to the B option with the same content, e.g. {"A1": "B2"}.
- In `differences`, give the exact differing spans from each side.

## Allowed values
- verdict: exact_same, not_exact

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "verdict": "exact_same",
  "option_map": {
    "A1": "B2",
    "A2": "B1",
    "A3": "B4",
    "A4": "B3"
  },
  "differences": []
}
```

## Examples
A says "0.2 m", B says "2 m", all else equal → `{"verdict": "not_exact", "option_map": null, "differences": [{"a": "0.2 m", "b": "2 m"}]}`

## Never
- Never call two questions exact_same because they test the same fact.
````

## `.claude/agents/d1-chapter-picker.md`

````markdown
---
name: d1-chapter-picker
description: Step D1. Picks which NCERT chapter ONE question tests, from its subject's chapter list. Use only when the runner passes a D1 input file.
tools: Read, Write
model: inherit
---

# Chapter picker · step D1

You are an agent in the NEET PYQ Data Pipeline. First narrowing: the whole subject down to one chapter.

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
Which chapter does this question test? Choose one. Choose a second chapter only if the question truly needs two (for example, its statements come from two chapters). Or say unsure.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question: stem, statements, lists, options
- `correct_answer`: the option number and its text
- `chapters`: id, title, top-level headings (only this subject and branch)

## Rules for this step
- Use the correct answer to see which fact is being tested.
- Do not pick a second chapter because a word from it appears in passing.

## Allowed values
- chapter_ids: one or two IDs from the list, or ["unsure"]
- confidence: high, medium, low

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "chapter_ids": [
    "BIO11-CH10"
  ],
  "why": "Asks about events of anaphase.",
  "confidence": "high"
}
```

## Examples
Statements: A and B about photosynthesis, C and D about respiration → two chapters.

## Never
- Never pick a chapter outside the list.
````

## `.claude/agents/d2-subtopic-picker.md`

````markdown
---
name: d2-subtopic-picker
description: Step D2. Picks one or two subtopics ONE question tests, from its chapter's subtopic list. Use only when the runner passes a D2 input file.
tools: Read, Write
model: inherit
---

# Subtopic picker · step D2

You are an agent in the NEET PYQ Data Pipeline. Second narrowing. The subtopic is how past questions meet student pages, so it must be right.

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
Which subtopic does this question test? Choose one, or two if the question truly tests two.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question: stem, statements, lists, options
- `correct_answer`
- `subtopics`: id, name, one-line description (this chapter only)
- `note_from_runner`: e.g. "previous choice had no passages" (optional)

## Rules for this step
- Choose by the fact the correct answer depends on.
- Two subtopics only when the question compares or combines them (e.g. mitosis vs meiosis).

## Allowed values
- subtopic_ids: one or two IDs from the list, or ["unsure"]
- confidence: high, medium, low

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "subtopic_ids": [
    "BIO11-CH10-ST03"
  ],
  "why": "Each statement is about a stage of mitosis.",
  "confidence": "high"
}
```

## Examples
"Which feature is seen in meiosis but not in mitosis?" → [Stages of mitosis, Meiosis I].

## Never
- Never invent a subtopic name.
````

## `.claude/agents/d4-evidence-quoter.md`

````markdown
---
name: d4-evidence-quoter
description: Step D4. Copies the exact NCERT line(s) that make the correct answer of ONE question correct (or the exact formula for a numerical). Use only when the runner passes a D4 input file.
tools: Read, Write
model: inherit
---

# Evidence quoter · step D4

You are an agent in the NEET PYQ Data Pipeline. Every answer must be provable from NCERT. A script searches the book for every line you copy; anything not found word for word is rejected.

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
First decide HOW this question connects to NCERT (link_type). Then copy the exact NCERT line(s): the line that states the answer, or, for a calculation or applied question, one exact line per rule or law the solution uses. List the maths/logic steps between the rules in derivation_steps. For a statement question, copy one line per statement (including the line that shows a false statement is false). Copy word for word; do not reword. If no line supports it, return no evidence.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question: stem, statements, lists, options
- `answer_to_support`: the option number and its text
- `passages`: 5–15 latest-edition passages (id + full text)
- `codebook`: the owner's codebook text from codebook/D4_link_type.md, present ONLY if that file exists

## Rules for this step
- link_type: states_answer = a line states the answer; rule_used = one NCERT rule plus plain maths; rules_chained = two or more NCERT rules one after another; concept_applied = NCERT explains the idea and the question applies it to a new case; beyond_ncert_method = the solution needs a result or method NCERT does not give.
- Each `exact_line` is a continuous span copied from ONE passage. Never join pieces from different places.
- Copy the shortest span that states the fact or rule (usually one sentence or one equation). Ellipses are not allowed inside a quote.
- `for` says which part it supports: "answer", "statement A", "statement C is false", "List I-P matches List II-2", "rule".
- `derivation_steps`: short steps in words or LaTeX between the rules. ONLY algebra, arithmetic, unit conversion or logic. If a step needs a physics/chemistry fact, that fact needs its own quote (or the link_type is beyond_ncert_method). The last step must end at the answer value. Empty for states_answer.
- `supports_answer`: fully (every needed part, and every rule used in the steps, has a quote), partly (some), not_at_all (none).
- List unsupported parts in `missing`.
- For beyond_ncert_method, still quote any NCERT rules the solution uses, and say in `note` which result is not in NCERT.

## Allowed values
- link_type: states_answer, rule_used, rules_chained, concept_applied, beyond_ncert_method
- supports_answer: fully, partly, not_at_all

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "link_type": "states_answer",
  "derivation_steps": [],
  "evidence": [
    {
      "for": "statement B",
      "passage_id": "BIO11L-CH10-P07",
      "exact_line": "the two daughter chromatids begin their migration towards the two opposite poles."
    }
  ],
  "supports_answer": "partly",
  "missing": [
    "statement A",
    "statement D"
  ],
  "note": ""
}
```

## Examples
Numerical (stretched wire) → `{"link_type": "rule_used", "evidence": [{"for": "rule", "passage_id": "PHY12L-CH03-P08", "exact_line": "R = \\rho \\frac{l}{A}"}], "derivation_steps": ["volume constant so A' = A/2 when l' = 2l", "R' = rho(2l)/(A/2) = 4R = 16 ohm"], "supports_answer": "fully", "missing": [], "note": ""}`

Field at the centre of a loop split into arcs of unequal resistance → link_type beyond_ncert_method; quote the NCERT rule for the field at the centre of a circular loop; note: "Field of an arc is not given in NCERT."

## Never
- Never paraphrase. A paraphrase is rejected and counts as a failure.
- Never quote from memory; only from the passages given.
````

## `.claude/agents/d5-older-line-finder.md`

````markdown
---
name: d5-older-line-finder
description: Step D5. Copies the exact line in the OLDER NCERT edition that covers the same fact as ONE question's answer, or says none. Use only when the runner passes a D5 input file.
tools: Read, Write
model: inherit
---

# Older-edition line finder · step D5

You are an agent in the NEET PYQ Data Pipeline. We keep how the older book stated each fact, so changed or reworded facts can be explained with evidence.

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
Copy the exact line in the OLDER NCERT that covers the same fact as this answer. Copy word for word; do not reword. If the older book has no such line, say none for that part.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question and `answer_to_support`
- `latest_evidence`: D4's verified lines (may be empty)
- `older_passages`: older-edition partners and older passages from removed topics (id + text)

## Rules for this step
- Same quoting rules as the evidence quoter: one continuous span from one passage, no ellipses.
- Give one older line per part that D4 covered (same `for` labels), plus lines for parts D4 could not cover if the older book has them.

## Allowed values
- passage IDs from older_passages only

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "older": [
    {
      "for": "statement B",
      "passage_id": "BIO11O-CH10-P05",
      "exact_line": "<exact text copied from the input>"
    }
  ],
  "none_for": [],
  "note": ""
}
```

## Examples
Latest book has no line for the answer, older removed passage has it → older contains that line; this becomes deleted content in D6.

## Never
- Never quote the latest edition here.
````

## `.claude/agents/d6-status-note-writer.md`

````markdown
---
name: d6-status-note-writer
description: Step D6. Writes the short reason note for ONE question in the fixed template for its syllabus status, quoting lines exactly. Use only when the runner passes a D6 input file.
tools: Read, Write
model: inherit
---

# Status and reason note writer · step D6

You are an agent in the NEET PYQ Data Pipeline. Students and reviewers must see in seconds where the answer comes from and how the older book said it.

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
Write the reason note for this question using the template for its status and note type. Copy every quoted line exactly. If the older NCERT says the same fact in different words, add: Remember: the older NCERT wrote it as "...". If the content was deleted, say the answer is according to the older NCERT, with the exact older line.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `syllabus_status` (decided by the script)
- `latest_evidence`, `older_evidence`, `lab_manual_evidence` (verified lines)
- `change_log_entries` on these passages

## Rules for this step
- Templates:
  - same_both: Answer from the latest NCERT: "<latest line>".
  - written_differently: Answer from the latest NCERT: "<latest line>". Remember: the older NCERT wrote it as "<older line>". Same fact; follow the latest wording.
  - deleted: This question is from content deleted from the latest NCERT. The answer is according to the older NCERT: "<older line>".
  - outside: This fact is not in any NCERT edition. The answer is from the official key.
  - outside_rules: This question uses a result that is not given in NCERT. The NCERT rules involved are: "<rule 1>", "<rule 2>". The answer is from the official key.
  - For rule-based links (rule_used, rules_chained, concept_applied) the same_both or written_differently template quotes the rule(s) as the latest line.
  - lab_manual: Answer from the NCERT lab manual: "<line>".
- Choose written_differently only when the older line states the same fact in different words.
- If several lines are quoted, quote the one that decides the answer; list all in `quoted_lines`.

## Allowed values
- note_type: same_both, written_differently, deleted, outside, outside_rules, lab_manual

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "syllabus_status": "latest_ncert",
  "note_type": "same_both",
  "reason_note": "Answer from the latest NCERT: \"...\".",
  "quoted_lines": [
    {
      "edition": "L",
      "passage_id": "BIO11L-CH10-P07",
      "text": "<exact text copied from the input>"
    }
  ]
}
```

## Examples
Older line says "six" where latest says "seven" → this is not written_differently (the fact differs); keep note_type same_both from the latest line and leave the change to D7.

## Never
- Never add explanations outside the template.
````

## `.claude/agents/d7-latest-answer-checker.md`

````markdown
---
name: d7-latest-answer-checker
description: Step D7. Answers ONE question again using only the latest NCERT lines and says whether that matches the official answer, citing the change-log entry if not. Use only when the runner passes a D7 input file.
tools: Read, Write
model: inherit
---

# Latest-NCERT answer checker · step D7

You are an agent in the NEET PYQ Data Pipeline. Some past answers changed between editions. We keep both and teach the latest. Faculty approve every changed answer at the end.

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
By the latest NCERT, which option is correct? Quote the latest line. Is it the same as the official answer? If not, which change-log entry explains it? Write the extra sentence for the reason note.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question and options; `official_answer`
- `latest_evidence`, `older_evidence`
- `change_log_entries`: id, type, old fact, new fact, passages

## Rules for this step
- Decide only from the latest lines given. Do not use what you remember about NCERT.
- `quote` must be copied exactly from latest_evidence or the latest passage text given.
- If the answer differs, `change_id` must be one of the entries given; if none explains it, set change_id null and explain in note.
- Sentence template: By the older NCERT the answer was (<official>); by the latest NCERT it is (<latest>).

## Allowed values
- latest_answer: "1"–"4", unsure

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "latest_answer": "3",
  "same_as_official": false,
  "quote": "<exact text copied from the input>",
  "change_id": "CL-0031",
  "sentence_for_note": "By the older NCERT the answer was (2); by the latest NCERT it is (3).",
  "note": ""
}
```

## Examples
Change log says wording_only and the latest line still supports the official option → same_as_official true, sentence_for_note "".

## Never
- Never use coaching material or the blind solver's answer.
````

## `.claude/agents/d8-fact-line-writer.md`

````markdown
---
name: d8-fact-line-writer
description: Step D8. Writes the one standard fact line (or problem line) that ONE question tests. Use only when the runner passes a D8 input file.
tools: Read, Write
model: inherit
---

# Fact line writer · step D8

You are an agent in the NEET PYQ Data Pipeline. Questions from different years that test the same thing should get almost the same line, so repeats can be found.

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
In one line, in the standard wording, write the exact fact this question tests. For a numerical, write the problem type and the rule it uses.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question; `answer_taught` (latest answer)
- `subtopic`
- `evidence`: verified latest lines

## Rules for this step
- Present tense, subject first, NCERT's own term, no option numbers, no "which of the following".
- Numerical: start with "Problem:" then the setup in general terms, then "Rule:" and the formula. Leave out the specific numbers.
- Statement questions: write the fact of each TRUE statement, separated by " | ", in `fact_line`, and list them in `facts`.
- Prefer the evidence wording when it states the fact directly.

## Allowed values
- confidence: high, medium, low

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "fact_line": "Fungal cell walls are made of chitin.",
  "facts": [
    "Fungal cell walls are made of chitin."
  ],
  "confidence": "high"
}
```

## Examples
4 Ω wire doubled → `{"fact_line": "Problem: new resistance of a stretched wire at constant volume. Rule: R = rho l / A, so R is proportional to l squared.", "facts": [], "confidence": "high"}`

## Never
- Never include year, option letters or specific numbers of a numerical.
````

## `.claude/agents/d9-repeat-finder.md`

````markdown
---
name: d9-repeat-finder
description: Step D9. For ONE question, lists other-year questions in the same subtopic that might test the same fact or problem. Inclusive: if unsure, include. Use only when the runner passes a D9 input file.
tools: Read, Write
model: inherit
---

# Repeat finder · step D9

You are an agent in the NEET PYQ Data Pipeline. This is a wide net. Missing a real repeat loses it forever; a false candidate is removed in D11 at no cost.

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
Which of these other questions might test the same fact or the same problem as this one? List their IDs, or say none. If unsure, include it.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `this`: id, year, fact_line, facts
- `others`: id, year, sitting, fact_line (same subtopic, other years)

## Rules for this step
- Include same fact in any wording or format, and same problem type with different numbers.
- Include a statement question if any one of its facts matches.
- Do not include questions that only share the subtopic name.

## Allowed values
- IDs from `others` only

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "possible_repeats": [
    "Q-000045",
    "Q-000981"
  ],
  "none": false
}
```

## Examples
This: "Fungal cell walls are made of chitin." Others include a 2023 statement question whose facts include chitin → include it.

## Never
- Never list this question's own ID.
````

## `.claude/agents/d11-group-confirmer.md`

````markdown
---
name: d11-group-confirmer
description: Step D11. Confirms ONE candidate repeat group: which members truly test the same fact or problem, labels each against the first year, and splits mixed groups. Use only when the runner passes a D11 input file.
tools: Read, Write
model: inherit
---

# Repeat group confirmer · step D11

You are an agent in the NEET PYQ Data Pipeline. Repeat groups are the most useful signal in the bank: facts NEET keeps returning to.

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
These questions might test the same thing. Which ones truly do? Label each against the first year the fact was asked. If the group holds two different facts, split it into two groups. Move 'same concept, different fact' members to related, and drop 'different' ones.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `members`: id, year, sitting, stem (first 300 characters), answer text, fact_line
- `codebook`: the owner's codebook text from codebook/D11.md, present ONLY if that file exists

## Rules for this step
- The first member of a group is the earliest year (earliest sitting within a year).
- Labels are relative to that first member.
- Every input member must appear exactly once: in a group, in related, or in removed.
- A group needs at least 2 members; a lone member goes to related or removed.

## Allowed values
- label: first, exact_same, reworded, same_fact_new_format, same_problem_new_numbers
- related (same_concept_different_fact), removed (different)

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "groups": [
    {
      "fact_line": "Fungal cell walls are made of chitin.",
      "first": "Q-000045",
      "members": [
        {
          "id": "Q-000045",
          "label": "first"
        },
        {
          "id": "Q-000877",
          "label": "same_fact_new_format"
        }
      ]
    }
  ],
  "related": [
    {
      "id": "Q-000512",
      "related_to": "Q-000045"
    }
  ],
  "removed": []
}
```

## Examples
Candidate {2017 anaphase, 2020 anaphase+metaphase statements, 2024 metaphase} → group 1 {2017 first, 2020 same_fact_new_format}; 2024 related to 2017 (same concept, different fact).

## Never
- Never merge two different facts into one group.
````

## `.claude/agents/e0-open-look.md`

````markdown
---
name: e0-open-look
description: Step E0.1. For ONE question, describes in free words what the student must do and how the question works, with NO categories shown. Use only when the runner passes an E0 input file.
tools: Read, Write
model: inherit
---

# Open look (category discovery) · step E0

You are an agent in the NEET PYQ Data Pipeline. Categories must come from real papers, not imagination. Your free answers are grouped later.

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
Complete: "To get this right, the student must ___". Then, in a few words each: how the question is built; what it asks the student to pick; what NCERT material it uses; and for each wrong option, why a student might pick it.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question, answer taught, evidence lines, subject

## Rules for this step
- Write plain, short phrases. Do not use labels like "elimination" or "recall"; describe the action.
- One phrase per wrong option.

## Allowed values
- free text

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "student_must": "check each of four statements about mitosis stages and reject the one that puts an event in the wrong stage",
  "built_as": "four lettered statements, options are combinations",
  "asks_to_pick": "the combination of correct statements",
  "ncert_material": "the ordered description of mitosis stages",
  "wrong_options": {
    "2": "includes the false statement C",
    "3": "includes C and drops true ones",
    "4": "assumes all four are true"
  }
}
```

## Examples
Numerical → student_must: "choose the resistance formula, use constant volume, and square the length ratio".

## Never
- Never mention or invent category names.
````

## `.claude/agents/e0-category-grouper.md`

````markdown
---
name: e0-category-grouper
description: Step E0.2. Groups the free open-look answers for ONE tag into categories, compares with the starting list, and reports keep/new/merge/drop with counts and examples. Use only when the runner passes an E0-group input file.
tools: Read, Write
model: inherit
---

# Category grouper · step E0

You are an agent in the NEET PYQ Data Pipeline. Turns ~300 free descriptions into a data-based category list for faculty to judge.

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
Read all the free answers for this tag. Group answers that say the same thing. Name each group and define it in one line. Compare with the starting list and mark each category keep, new, merge or drop. Give 2 example question IDs, the subjects it appears in, and the count per subject.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `tag`: thinking, question_type, format, content_shape or trap
- `starting_list`: names and definitions
- `answers`: list of {question_id, subject, year, text}

## Rules for this step
- Every answer goes into exactly one group (or "unclear").
- A starting-list category with no answers → drop (or keep with count 0 if rare by nature; say why).
- Two starting categories you cannot tell apart in the answers → merge.
- A group that fits no starting category → new.

## Allowed values
- decision: keep, new, merge, drop

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "tag": "thinking",
  "categories": [
    {
      "name": "elimination",
      "definition": "<exact text copied from the input>",
      "decision": "keep",
      "subjects": [
        "Biology",
        "Chemistry"
      ],
      "count": {
        "Physics": 3,
        "Chemistry": 21,
        "Biology": 47
      },
      "years_seen": [
        2021,
        2022,
        2023,
        2024,
        2025,
        2026
      ],
      "examples": [
        "Q-000123",
        "Q-000877"
      ]
    }
  ],
  "unclear": [
    "Q-000999"
  ]
}
```

## Examples
Many answers say "find the one that breaks the rule" → new category "spot the exception".

## Never
- Never place one answer in two groups.
````

## `.claude/agents/e1-type-tagger.md`

````markdown
---
name: e1-type-tagger
description: Step E1. Tags how ONE question is built, only when script patterns did not decide. Use only when the runner passes an E1 input file.
tools: Read, Write
model: inherit
---

# Question type tagger · step E1

You are an agent in the NEET PYQ Data Pipeline. Question type is the structure on the page. It is not the format (what to pick) or the trap.

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
Which question type is this? Choose from the list, or say new_type and describe it in one line.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question with its structure field
- `codebook`: the owner's codebook text from codebook/E1.md, present ONLY if that file exists
- `allowed`: the allowed values with one-line definitions

## Rules for this step
- Judge only the structure: how many statements, lists, a figure, an order to arrange.

## Allowed values
- question_type: single_statement, statement_options, list_of_statements, statement_i_ii, assertion_reason, match_the_lists, match_three_columns, pair_options, arrange_in_order, rank_by_property, fill_in_blank, diagram_labelled, figure_to_read, graph_options, structure_options, reaction_scheme, multi_part_respectively, new_type (plus any added in the allowed list you are given)

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "question_type": "list_of_statements",
  "new_description": "",
  "confidence": "high"
}
```

## Examples
"Statement I: ... Statement II: ..." with options both true / both false / I true II false / I false II true → statement_i_ii.

## Never
- Never tag the format here.
````

## `.claude/agents/e2-format-tagger.md`

````markdown
---
name: e2-format-tagger
description: Step E2. Tags what ONE question asks the student to pick. Use only when the runner passes an E2 input file.
tools: Read, Write
model: inherit
---

# Format tagger · step E2

You are an agent in the NEET PYQ Data Pipeline. Format is the demand. A script cross-checks negative words, because missing a NOT flips the answer.

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
What does this question ask the student to pick? Choose from the list, or say new_format.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question; `negative_words_seen`
- `codebook`: the owner's codebook text from codebook/E2.md, present ONLY if that file exists
- `allowed`: the allowed values with one-line definitions

## Rules for this step
- If the stem contains NOT, EXCEPT, INCORRECT, FALSE or WRONG about what to pick, the format is pick_incorrect (or odd_one_out if it asks for the one that differs).
- "How many are correct" → count_correct. Options that are letter combinations → pick_correct_combination.

## Allowed values
- format: pick_correct, pick_incorrect, count_correct, pick_correct_combination, pick_match_code, pick_order, odd_one_out, calculate_value, derive_expression, pick_ratio, pick_proportionality, name_or_identify, identify_structure_or_compound, predict_product, identify_reagent_or_condition, identify_reaction_or_process_name, classify_into_group, pick_explanation, predict_effect, pick_graph, judge_two_statements, judge_assertion_reason, pick_scientist_or_date, expand_abbreviation, new_format (plus any added)

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "format": "pick_correct_combination",
  "new_description": "",
  "confidence": "high"
}
```

## Examples
"All of the following occur in prophase EXCEPT" → pick_incorrect.

## Never
- Never ignore a negative word.
````

## `.claude/agents/e3-shape-tagger.md`

````markdown
---
name: e3-shape-tagger
description: Step E3. Tags what kind of NCERT material ONE question is built on, from its evidence. Use only when the runner passes an E3 input file.
tools: Read, Write
model: inherit
---

# Content shape tagger · step E3

You are an agent in the NEET PYQ Data Pipeline. Content shape tells the test generator what kind of NCERT content becomes a NEET question.

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
What kind of NCERT material is this question built on? Choose from the list, or say new_shape.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question; evidence lines with their passage kinds (paragraph, table, figure, equation, box)
- `codebook`: the owner's codebook text from codebook/E3.md, present ONLY if that file exists
- `allowed`: the allowed values with one-line definitions

## Rules for this step
- Judge the NCERT material in the evidence, not how the question looks.
- A table passage → usually table; an equation → formula; ordered stages → process; two things contrasted → comparison; a stated exception → exception.

## Allowed values
- content_shape: one_line, list, example_list, table, diagram, labelled_diagram, graph, formula, derived_result, experiment_classic, practical_procedure, comparison, process, cycle_or_pathway, life_cycle, exception, classification_hierarchy, definition_term, trend, reaction_mechanism, structure_chemical, nomenclature_rule, value_or_data, scientist_history, applied_context, biological_equation, disease_cause, current_affairs, new_shape (plus any added)
- confidence: high, medium, low

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "content_shape": "process",
  "why": "Evidence is the ordered stages of mitosis.",
  "new_description": "",
  "confidence": "high"
}
```

## Examples
Evidence is R = rho l / A → formula.

## Never
- Never tag from the question layout alone.
````

## `.claude/agents/e4-thinking-tagger.md`

````markdown
---
name: e4-thinking-tagger
description: Step E4. Tags what ONE question makes the student do in their head, using the codebook. Use only when the runner passes an E4 input file.
tools: Read, Write
model: inherit
---

# Thinking tagger · step E4

You are an agent in the NEET PYQ Data Pipeline. Thinking is the hardest tag. Two independent runs must agree; disagreements are settled and reviewed at the end.

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
What must the student do in their head to get this right? Choose a primary category from the codebook, and a secondary only if the question clearly needs a second kind of thinking.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question; answer taught; evidence lines; `codebook` (the owner's codebook/E4.md if it exists, else the eight draft categories with one-line definitions) and `codebook_version`

## Rules for this step
- Follow each category's tag-when and don't-tag-when exactly.
- Tie-break: the primary is whatever makes the question hard. At most one secondary.
- Use the evidence to decide recall vs application (is this exact case in NCERT?).
- `why` is one sentence a reviewer can check in seconds.

## Allowed values
- primary/secondary: the category names in `codebook` if present, otherwise the draft categories given in the input (secondary may be null)
- confidence: high, medium, low

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "primary": "elimination",
  "secondary": "process",
  "why": "The student must check four statements, each about a different stage of mitosis.",
  "confidence": "high",
  "codebook_version": "v1-draft"
}
```

## Examples
"Arrange four events of mitosis in order" → primary process, secondary null.

## Never
- Never use a category that is not in the list you were given.
````

## `.claude/agents/e5-trap-tagger.md`

````markdown
---
name: e5-trap-tagger
description: Step E5. For ONE wrong option of ONE question, tags the trap that makes it look right. Use only when the runner passes an E5 input file.
tools: Read, Write
model: inherit
---

# Trap tagger · step E5

You are an agent in the NEET PYQ Data Pipeline. Traps let tests plant realistic wrong options and give students specific feedback.

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
Why could a student pick this wrong option? Choose one trap from the list, or say new_trap and describe it in one line.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question; answer taught; `wrong_option` (number and text); evidence lines; change-log entries on the evidence passages
- `codebook`: the owner's codebook text from codebook/E5.md, present ONLY if that file exists
- `allowed`: the allowed values with one-line definitions

## Rules for this step
- One trap for this one option.
- old_ncert_fact only when a change-log entry shows this option was right by the older book.
- calculation_slip covers wrong formula, missed square, unit or power-of-ten errors; say which in why.

## Allowed values
- trap: look_alike_term, wrong_pairing, half_true, wrong_order, ignores_exception, extreme_word, old_ncert_fact, opposite_answer, calculation_slip, swapped_positions, number_near_miss, unit_conversion_slip, sign_or_direction, scientist_swap, name_variant, invalid_comparator, impossible_value, reversed_cause_effect, partial_combination, new_trap (plus any added)
- confidence: high, medium, low

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "option": "2",
  "trap": "calculation_slip",
  "why": "Forgot to square the length ratio: 4 x 2 = 8.",
  "new_description": "",
  "confidence": "high"
}
```

## Examples
Option includes statement C (a true event placed in the wrong stage) → wrong_pairing.

## Never
- Never tag the correct option.
````

## `.claude/agents/e6-context-tagger.md`

````markdown
---
name: e6-context-tagger
description: Step E6. Tags how ONE question's stem is framed (plain, scenario, experiment, data, table, etc.), only when script patterns did not decide. Use only when the runner passes an E6 input file.
tools: Read, Write
model: inherit
---

# Stem context tagger · step E6

You are an agent in the NEET PYQ Data Pipeline. Recent papers wrap facts in stories, setups and data. This tag lets generated tests copy that framing.

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
How is this question's stem framed? Choose one value from the list.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- question stem and options; B3 structure; whether a figure exists
- `codebook`: the owner's codebook text from codebook/E6.md, present ONLY if that file exists

## Rules for this step
- case_scenario: a person, patient or situation story (a student observes, a couple, a farmer).
- experiment_setup: an experiment or measurement described (pendulum timing, metre bridge, a test on sap).
- real_world: an everyday device or application (a heater, a microwave oven).
- data_given / table_given / figure_given / reaction_given / equation_given: the stem is built on that material.
- historical: a scientist, discovery or date.
- plain: none of the above.
- If two apply, choose the one the question cannot be answered without.

## Allowed values
- stem_context: plain, case_scenario, experiment_setup, real_world, data_given, table_given, figure_given, reaction_given, equation_given, historical, unsure

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "stem_context": "experiment_setup",
  "why": "Describes a student timing 30 oscillations of a pendulum.",
  "confidence": "high"
}
```

## Examples
"A room heater is rated 400 W, 220 V. If the supply drops to 200 V…" → real_world.

## Never
- Never tag what the student must pick; that is the format.
````

## `.claude/agents/x-adjudicator.md`

````markdown
---
name: x-adjudicator
description: Shared. Settles a disagreement between two runs (or two readings) of ONE item for any step, so nothing waits for a person mid-run. Use only when the runner passes an adjudication input file.
tools: Read, Write
model: inherit
---

# Adjudicator · step any

You are an agent in the NEET PYQ Data Pipeline. You let the pipeline continue without a person. Every value you choose is flagged and reviewed at the end, so honesty about uncertainty matters more than always choosing.

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
Here are the step's task, its allowed values, the evidence, and two outputs that disagree (or fail a check). Choose the output that is correct, or combine them only where the step's rules allow, or say unsure.

## Input
You receive one JSON file at the input path in your instruction. It contains:
- `step` and its one-line task and rules
- `allowed_values`
- `evidence`: the same input the step's agent saw (and images if any)
- `run_a`, `run_b` (or `reading_a`, `reading_b` with highlighted differing spans)
- `failed_check` (if any)

## Rules for this step
- Decide from the evidence, not from which run sounds more confident.
- For readings (B4, C1): choose span by span which reading matches the image.
- Your chosen value must pass the step's own rules (allowed values, exact quotes).
- If neither is right and you can't produce a valid value from the evidence, say unsure.

## Allowed values
- choice: A, B, combined, unsure

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "choice": "A",
  "value": {
    "chapter_ids": [
      "BIO11-CH10"
    ]
  },
  "why": "The answer depends on the order of mitosis stages, covered in chapter 10.",
  "confidence": "medium"
}
```

## Examples
B4: reading A "40 Ω", reading B "4 Ω", image shows a single 4 → `{"choice": "B", "value": {"span": "4"}, "why": "Single digit 4 in the image; the extra mark is part of the Ω symbol.", "confidence": "medium"}`

## Never
- Never produce a value outside the allowed values.
- Never prefer a run because it was first.
````

---

# Appendix C · Slash commands

Create one file per block in `.claude/commands/`.


## `.claude/commands/build.md`

````markdown
---
description: Build the project (milestones M0–M4 in docs/SPEC.md).
---
Read docs/SPEC.md Sections 0–7, 15–17 and Appendices A–E.
1. M0: create the folder layout (SPEC 5.8) and every file in Appendices A–D word for word; create docs/OPEN_QUESTIONS.md from SPEC Section 20.
2. M1: write scripts/lib/ as SPEC 7/M1 lists; write tests T1–T8; run them until green.
3. M2: write run_step.py, run_stage.py, status.py; complete config/steps.yaml for every step from SPEC Sections 8–14 (input_fields, schema, check, fallback, flags, safe default); write schemas/; tests T9–T12.
4. M3: write every script-only step and every scripts/checks/<STEP>.py; tests T13–T30.
5. Print: files created, tests passed/failed, and every default you chose (with its OPEN_QUESTIONS entry).
Do not touch inputs/. Do not call any agent during the build.
````

## `.claude/commands/run-step.md`

````markdown
---
description: Run one step for every item that needs it. Usage: /run-step <STEP> [--chapters X] [--papers Y] [--items Z]
argument-hint: <STEP> [filters]
---
1. Run `python scripts/run_step.py $ARGUMENTS --list`. If it prints AUTO, run `python scripts/run_step.py $ARGUMENTS --auto` instead and go to step 4.
2. For each printed line (item | agent | input | output | run), in order, invoke the named subagent with exactly:
   `Use the <agent> subagent. Input: <input path>. Output: <output path>. Do nothing else.`
3. Run `python scripts/run_step.py $ARGUMENTS --check`. If it prints a new list, repeat step 2 for it, then --check again, until it prints DONE.
4. Report as docs/SPEC.md Section 19 says.
Never answer a judgement yourself; never skip, reorder or add items.
````

## `.claude/commands/run-stage.md`

````markdown
---
description: Run every step of a stage in order. Usage: /run-stage <0|A|B|C|D|E|smoke> [filters]
argument-hint: <stage> [filters]
---
Run `python scripts/run_stage.py $ARGUMENTS --plan` to get the ordered steps. For each step follow /run-step exactly. Stop if a step prints STOP and report why.
````

## `.claude/commands/status.md`

````markdown
---
description: Show pipeline status.
---
Run `python scripts/status.py $ARGUMENTS` and report: items per status per step; open flags by severity and code; blocked items; stale items; review queue size per chapter.
````

## `.claude/commands/review-pack.md`

````markdown
---
description: Build the Stage F review queue and pack. Usage: /review-pack [--chapters X] [--new-only]
---
Run `python scripts/build_review_pack.py $ARGUMENTS`. Report queue size by priority group and chapter, and the path of review/review_pack/index.html. Then stop: people fill review/decisions.csv. Do not approve or edit anything yourself.
````

## `.claude/commands/apply-review.md`

````markdown
---
description: Apply reviewer decisions and run the cascade (Stage F3).
---
1. Run `python scripts/apply_review.py`. It applies review/decisions.csv, writes review/corrections.jsonl and prints the stale (item, step) list.
2. Re-run the stale steps in stage order exactly as /run-step does (use --items).
3. Run `python scripts/compute_counts.py` for affected subtopics.
4. Run `python scripts/build_review_pack.py --new-only` and report the new flags.
````

---

# Appendix D · Config files

## Step overview

| Step | Stage | Name | Item | Agent / worker | Runs | Needs |
|---|---|---|---|---|---|---|
| S0 | 0 | Intake check | inputs | `script` | 1 | - |
| A1 | A | Register the books | book | `a1-book-registrar` | 1 | S0 |
| A2 | A | Read the pages | page | `a2-page-reader` | 1 | A1 |
| A2S | A | Transcribe special blocks | block | `a2-special-transcriber` | 1 | A2 |
| A3 | A | Split into passages | section | `a3-passage-splitter` | 1 | A2S |
| A4 | A | Write the subtopic list | chapter | `a4-subtopic-writer` | 2 | A3 |
| A5 | A | Link passages to subtopics | passage | `script | a5-passage-linker` | 1 | A4 |
| A6 | A | Pair old and new passages | chapter | `script + x-adjudicator` | 1 | A5 |
| A7 | A | Find the differences | pair | `script` | 1 | A6 |
| A8 | A | Judge one change | pair | `a8-change-judge` | 2 | A7 |
| A9 | A | Write the change log | chapter | `script` | 1 | A8 |
| B1 | B | Register the paper | file | `b1-paper-registrar` | 1 | S0 |
| B2 | B | Find question boundaries | page | `b2-boundary-finder` | 1 | B1 |
| B3 | B | Read one question | question | `b3-question-reader` | 1 | B2 |
| B4 | B | Read it a second way | question | `script | b4-second-reader` | 1 | B3 |
| B5 | B | Attach the answer key | key page | `b5-key-copier` | 1 | B4 |
| B6 | B | Solve without the key | question | `b6-blind-solver` | 1 | B5 |
| B7 | B | Subject and branch | question | `script | b7-chem-branch-sorter` | 1 | B5 |
| B8 | B | Fix bonus/dropped | faulty question | `b8-faulty-fixer` | 1 | B7 |
| C1 | C | Merge booklet codes | pair | `c1-booklet-matcher` | 1 | B8 |
| D1 | D | Pick the chapter | question | `d1-chapter-picker` | 2 | C1, A9 |
| D2 | D | Pick the subtopic | question | `d2-subtopic-picker` | 2 | D1 |
| D3 | D | Fetch the passages | question | `script` | 1 | D2 |
| D4 | D | Quote the evidence | question × answer | `d4-evidence-quoter` | 1 | D3 |
| D5 | D | Older-edition line | question | `d5-older-line-finder` | 1 | D4 |
| D6 | D | Status and reason note | question | `script + d6-status-note-writer` | 1 | D5 |
| D7 | D | Latest-NCERT answer | question | `d7-latest-answer-checker` | 1 | D6 |
| D8 | D | Fact line | question | `d8-fact-line-writer` | 1 | D7 |
| D9 | D | Possible repeats | question | `d9-repeat-finder` | 1 | D8 (all questions of the subtopic) |
| D10 | D | Candidate groups | subtopic | `script` | 1 | D9 |
| D11 | D | Confirm groups | group | `d11-group-confirmer` | 2 | D10 |
| E0 | E | Category discovery | sample | `e0-open-look, e0-category-grouper` | 1 | D8 |
| E1 | E | Question type | question | `script | e1-type-tagger` | 1 | D7 |
| E2 | E | Format | question | `e2-format-tagger` | 1 | E1 |
| E3 | E | Content shape | question | `e3-shape-tagger` | 1 | E2 |
| E4 | E | Thinking | question | `e4-thinking-tagger` | 2 | E3 |
| E5 | E | Traps | wrong option | `e5-trap-tagger` | 2 | E4 |
| E6 | E | Descriptive tags | question | `script | e6-context-tagger` | 1 | E1 |
| F1 | F | Review queue and pack | run | `script` | 1 | E5, E6, D11 |
| F2 | F | Review and edit | item | `PEOPLE` | 1 | F1 |
| F3 | F | Apply decisions, cascade | decision | `script` | 1 | F2 |
| F4 | F | Counts | subtopic | `script` | 1 | F3 |
| F5 | F | Release and export | chapter | `script` | 1 | F4 |

## `config/steps.yaml` (skeleton; complete it in M2)

````yaml
# config/steps.yaml — skeleton. Complete input_fields, output_schema, check, fallback, flags and safe_default from SPEC Sections 8–14.

S0:
  stage: "0"
  name: "Intake check"
  item: "inputs"
  agent: "script"
  runs: 1
  needs: "-"
  input_fields: []
  output_schema: schemas/S0.json
  check: scripts/checks/S0.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

A1:
  stage: "A"
  name: "Register the books"
  item: "book"
  agent: "a1-book-registrar"
  runs: 1
  needs: "S0"
  input_fields: []
  output_schema: schemas/A1.json
  check: scripts/checks/A1.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

A2:
  stage: "A"
  name: "Read the pages"
  item: "page"
  agent: "a2-page-reader"
  runs: 1
  needs: "A1"
  input_fields: []
  output_schema: schemas/A2.json
  check: scripts/checks/A2.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

A2S:
  stage: "A"
  name: "Transcribe special blocks"
  item: "block"
  agent: "a2-special-transcriber"
  runs: 1
  needs: "A2"
  input_fields: []
  output_schema: schemas/A2S.json
  check: scripts/checks/A2S.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

A3:
  stage: "A"
  name: "Split into passages"
  item: "section"
  agent: "a3-passage-splitter"
  runs: 1
  needs: "A2S"
  input_fields: []
  output_schema: schemas/A3.json
  check: scripts/checks/A3.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

A4:
  stage: "A"
  name: "Write the subtopic list"
  item: "chapter"
  agent: "a4-subtopic-writer"
  runs: 2
  needs: "A3"
  input_fields: []
  output_schema: schemas/A4.json
  check: scripts/checks/A4.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

A5:
  stage: "A"
  name: "Link passages to subtopics"
  item: "passage"
  agent: "script | a5-passage-linker"
  runs: 1
  needs: "A4"
  input_fields: []
  output_schema: schemas/A5.json
  check: scripts/checks/A5.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

A6:
  stage: "A"
  name: "Pair old and new passages"
  item: "chapter"
  agent: "script + x-adjudicator"
  runs: 1
  needs: "A5"
  input_fields: []
  output_schema: schemas/A6.json
  check: scripts/checks/A6.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

A7:
  stage: "A"
  name: "Find the differences"
  item: "pair"
  agent: "script"
  runs: 1
  needs: "A6"
  input_fields: []
  output_schema: schemas/A7.json
  check: scripts/checks/A7.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

A8:
  stage: "A"
  name: "Judge one change"
  item: "pair"
  agent: "a8-change-judge"
  runs: 2
  needs: "A7"
  input_fields: []
  output_schema: schemas/A8.json
  check: scripts/checks/A8.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

A9:
  stage: "A"
  name: "Write the change log"
  item: "chapter"
  agent: "script"
  runs: 1
  needs: "A8"
  input_fields: []
  output_schema: schemas/A9.json
  check: scripts/checks/A9.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

B1:
  stage: "B"
  name: "Register the paper"
  item: "file"
  agent: "b1-paper-registrar"
  runs: 1
  needs: "S0"
  input_fields: []
  output_schema: schemas/B1.json
  check: scripts/checks/B1.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

B2:
  stage: "B"
  name: "Find question boundaries"
  item: "page"
  agent: "b2-boundary-finder"
  runs: 1
  needs: "B1"
  input_fields: []
  output_schema: schemas/B2.json
  check: scripts/checks/B2.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

B3:
  stage: "B"
  name: "Read one question"
  item: "question"
  agent: "b3-question-reader"
  runs: 1
  needs: "B2"
  input_fields: []
  output_schema: schemas/B3.json
  check: scripts/checks/B3.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

B4:
  stage: "B"
  name: "Read it a second way"
  item: "question"
  agent: "script | b4-second-reader"
  runs: 1
  needs: "B3"
  input_fields: []
  output_schema: schemas/B4.json
  check: scripts/checks/B4.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

B5:
  stage: "B"
  name: "Attach the answer key"
  item: "key page"
  agent: "b5-key-copier"
  runs: 1
  needs: "B4"
  input_fields: []
  output_schema: schemas/B5.json
  check: scripts/checks/B5.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

B6:
  stage: "B"
  name: "Solve without the key"
  item: "question"
  agent: "b6-blind-solver"
  runs: 1
  needs: "B5"
  input_fields: []
  output_schema: schemas/B6.json
  check: scripts/checks/B6.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

B7:
  stage: "B"
  name: "Subject and branch"
  item: "question"
  agent: "script | b7-chem-branch-sorter"
  runs: 1
  needs: "B5"
  input_fields: []
  output_schema: schemas/B7.json
  check: scripts/checks/B7.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

B8:
  stage: "B"
  name: "Fix bonus/dropped"
  item: "faulty question"
  agent: "b8-faulty-fixer"
  runs: 1
  needs: "B7"
  input_fields: []
  output_schema: schemas/B8.json
  check: scripts/checks/B8.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

C1:
  stage: "C"
  name: "Merge booklet codes"
  item: "pair"
  agent: "c1-booklet-matcher"
  runs: 1
  needs: "B8"
  input_fields: []
  output_schema: schemas/C1.json
  check: scripts/checks/C1.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

D1:
  stage: "D"
  name: "Pick the chapter"
  item: "question"
  agent: "d1-chapter-picker"
  runs: 2
  needs: "C1, A9"
  input_fields: []
  output_schema: schemas/D1.json
  check: scripts/checks/D1.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

D2:
  stage: "D"
  name: "Pick the subtopic"
  item: "question"
  agent: "d2-subtopic-picker"
  runs: 2
  needs: "D1"
  input_fields: []
  output_schema: schemas/D2.json
  check: scripts/checks/D2.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

D3:
  stage: "D"
  name: "Fetch the passages"
  item: "question"
  agent: "script"
  runs: 1
  needs: "D2"
  input_fields: []
  output_schema: schemas/D3.json
  check: scripts/checks/D3.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

D4:
  stage: "D"
  name: "Quote the evidence"
  item: "question × answer"
  agent: "d4-evidence-quoter"
  runs: 1
  needs: "D3"
  input_fields: []
  output_schema: schemas/D4.json
  check: scripts/checks/D4.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

D5:
  stage: "D"
  name: "Older-edition line"
  item: "question"
  agent: "d5-older-line-finder"
  runs: 1
  needs: "D4"
  input_fields: []
  output_schema: schemas/D5.json
  check: scripts/checks/D5.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

D6:
  stage: "D"
  name: "Status and reason note"
  item: "question"
  agent: "script + d6-status-note-writer"
  runs: 1
  needs: "D5"
  input_fields: []
  output_schema: schemas/D6.json
  check: scripts/checks/D6.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

D7:
  stage: "D"
  name: "Latest-NCERT answer"
  item: "question"
  agent: "d7-latest-answer-checker"
  runs: 1
  needs: "D6"
  input_fields: []
  output_schema: schemas/D7.json
  check: scripts/checks/D7.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

D8:
  stage: "D"
  name: "Fact line"
  item: "question"
  agent: "d8-fact-line-writer"
  runs: 1
  needs: "D7"
  input_fields: []
  output_schema: schemas/D8.json
  check: scripts/checks/D8.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

D9:
  stage: "D"
  name: "Possible repeats"
  item: "question"
  agent: "d9-repeat-finder"
  runs: 1
  needs: "D8 (all questions of the subtopic)"
  input_fields: []
  output_schema: schemas/D9.json
  check: scripts/checks/D9.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

D10:
  stage: "D"
  name: "Candidate groups"
  item: "subtopic"
  agent: "script"
  runs: 1
  needs: "D9"
  input_fields: []
  output_schema: schemas/D10.json
  check: scripts/checks/D10.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

D11:
  stage: "D"
  name: "Confirm groups"
  item: "group"
  agent: "d11-group-confirmer"
  runs: 2
  needs: "D10"
  input_fields: []
  output_schema: schemas/D11.json
  check: scripts/checks/D11.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

E0:
  stage: "E"
  name: "Category discovery"
  item: "sample"
  agent: "e0-open-look, e0-category-grouper"
  runs: 1
  needs: "D8"
  input_fields: []
  output_schema: schemas/E0.json
  check: scripts/checks/E0.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

E1:
  stage: "E"
  name: "Question type"
  item: "question"
  agent: "script | e1-type-tagger"
  runs: 1
  needs: "D7"
  input_fields: []
  output_schema: schemas/E1.json
  check: scripts/checks/E1.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

E2:
  stage: "E"
  name: "Format"
  item: "question"
  agent: "e2-format-tagger"
  runs: 1
  needs: "E1"
  input_fields: []
  output_schema: schemas/E2.json
  check: scripts/checks/E2.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

E3:
  stage: "E"
  name: "Content shape"
  item: "question"
  agent: "e3-shape-tagger"
  runs: 1
  needs: "E2"
  input_fields: []
  output_schema: schemas/E3.json
  check: scripts/checks/E3.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

E4:
  stage: "E"
  name: "Thinking"
  item: "question"
  agent: "e4-thinking-tagger"
  runs: 2
  needs: "E3"
  input_fields: []
  output_schema: schemas/E4.json
  check: scripts/checks/E4.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

E5:
  stage: "E"
  name: "Traps"
  item: "wrong option"
  agent: "e5-trap-tagger"
  runs: 2
  needs: "E4"
  input_fields: []
  output_schema: schemas/E5.json
  check: scripts/checks/E5.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

E6:
  stage: "E"
  name: "Descriptive tags"
  item: "question"
  agent: "script | e6-context-tagger"
  runs: 1
  needs: "E1"
  input_fields: []
  output_schema: schemas/E6.json
  check: scripts/checks/E6.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

F1:
  stage: "F"
  name: "Review queue and pack"
  item: "run"
  agent: "script"
  runs: 1
  needs: "E5, E6, D11"
  input_fields: []
  output_schema: schemas/F1.json
  check: scripts/checks/F1.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

F2:
  stage: "F"
  name: "Review and edit"
  item: "item"
  agent: "PEOPLE"
  runs: 1
  needs: "F1"
  input_fields: []
  output_schema: schemas/F2.json
  check: scripts/checks/F2.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

F3:
  stage: "F"
  name: "Apply decisions, cascade"
  item: "decision"
  agent: "script"
  runs: 1
  needs: "F2"
  input_fields: []
  output_schema: schemas/F3.json
  check: scripts/checks/F3.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

F4:
  stage: "F"
  name: "Counts"
  item: "subtopic"
  agent: "script"
  runs: 1
  needs: "F3"
  input_fields: []
  output_schema: schemas/F4.json
  check: scripts/checks/F4.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null

F5:
  stage: "F"
  name: "Release and export"
  item: "chapter"
  agent: "script"
  runs: 1
  needs: "F4"
  input_fields: []
  output_schema: schemas/F5.json
  check: scripts/checks/F5.py
  fallback: []
  flags: {}
  safe_default: null
  codebook_file: null
````

## `config/cascade.yaml`

````yaml
# config/cascade.yaml — SPEC Section 15
book_register:        {rerun_book: [A2, A2S, A3, A4, A5, A6, A7, A8, A9], rerun_questions_citing: [D3, D4, D5, D6, D7, E3, E5]}
passage_cuts:         {rerun_chapter: [A4, A5, A6, A7, A8, A9], rerun_questions_in_chapter: [D3, D4, D5, D6, D7, D8, D9, D10, D11, E3, E4, E5, F4]}
subtopic_list:        {rerun_chapter: [A5], rerun_questions_in_chapter: [D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, E3, E4, E5, F4]}
passage_link:         {rerun_chapter: [A6, A7], rerun_questions_in_subtopic: [D3, D4, D5, D6, D7, D8, D9, D10, D11, E3, E4, E5, F4]}
pair:                 {rerun_pair: [A7, A8, A9], rerun_questions_citing: [D5, D6, D7]}
change_log_row:       {rerun_affected_questions: [D6, D7, E5, F4]}
paper_register:       {rerun_paper: [B5, B6, B7, B8, C1, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, E1, E2, E3, E4, E5, E6, F4]}
question_boundaries:  {rerun_question: [B3, B4, B5, B6, B7, B8, C1, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, E1, E2, E3, E4, E5, E6, F4]}
question_text:        {rerun_question: [B6, B7, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, E1, E2, E3, E4, E5, E6, F4]}
official_answer:      {rerun_question: [B6, B8, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, E4, E5, F4]}
b8_correction:        {rerun_question: [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, E1, E2, E3, E4, E5, E6, F4]}
subject_branch:       {rerun_question: [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, E3, E4, E5, F4]}
chapter:              {rerun_question: [D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, E3, E4, E5, F4]}
subtopic:             {rerun_question: [D3, D4, D5, D6, D7, D8, E3, E4, E5], rerun_old_and_new_subtopic: [D9, D10, D11, F4]}
evidence:             {rerun_question: [D5, D6, D7, D8, E3, E4, E5], rerun_subtopic: [D9, D10, D11, F4]}
older_line:           {rerun_question: [D6, D7]}
status_note:          {rerun_question: [D7]}
latest_answer:        {rerun_question: [D4, D8, E4, E5], rerun_subtopic: [D9, D10, D11, F4]}
fact_line:            {rerun_subtopic: [D9, D10, D11, F4]}
repeat_groups:        {rerun_subtopic: [F4]}
codebook_file:        {rerun_all_questions_of_step_that_reads_it: true, then: [F4]}
allowed_value_change: {rerun_affected_questions_of_that_tag_step: true, then: [F4]}
any_e_tag:            {rerun_subtopic: [F4]}
````

## `config/allowed_values.yaml`

````yaml
# config/allowed_values.yaml — v0.1, from the analysis of 10 real papers (SPEC Section 17). Lists, not codebooks.
version: v0.1
sitting: [MAIN, PH2, REEXAM, RETEST, CANCELLED]
subject: [Physics, Chemistry, Biology]
branch: {Chemistry: [physical, organic, inorganic], Biology: [botany, zoology]}
official_status: [normal, bonus, dropped, multiple_accepted]
issue_reason: [two_correct_options, no_correct_option, hindi_english_mismatch, error_in_question, outdated_ncert, other]
structure: [plain, statements, list, match, table, assertion_reason, statement_i_ii]
supports_answer: [fully, partly, not_at_all]
link_type:
  states_answer: one NCERT line states the answer
  rule_used: one NCERT rule plus plain maths
  rules_chained: two or more NCERT rules one after another
  concept_applied: NCERT explains the idea; the question applies it to a new case without calculation
  beyond_ncert_method: needs a result or method NCERT does not give
syllabus_status: [latest_ncert, lab_manual, deleted_content, outside_ncert]
note_type: [same_both, written_differently, answer_changed, deleted, outside, outside_rules, lab_manual]
change_type: [fact_changed, fact_removed, fact_added, wording_only]
repeat_label: [first, exact_same, reworded, same_fact_new_format, same_problem_new_numbers]
question_type:
  single_statement: one stem, four short options
  statement_options: each option is a full statement to judge
  list_of_statements: lettered statements in the stem; options are combinations or a count
  statement_i_ii: exactly two statements; options are true/false combinations
  assertion_reason: Assertion and Reason; options include whether R explains A
  match_the_lists: two lists; options are match codes
  match_three_columns: three columns (item, property, group)
  pair_options: each option is one pair; pick the correct or wrong match
  arrange_in_order: order of events or steps in time
  rank_by_property: order by a property (size, energy, acidity)
  fill_in_blank: stem has a blank
  diagram_labelled: figure with letter labels to identify
  figure_to_read: figure, circuit or graph needed to answer
  graph_options: the options are graphs or figures
  structure_options: the options are chemical structures
  reaction_scheme: a reaction or sequence is shown; identify X/Y/Z, product, reagent or name
  multi_part_respectively: the answer has two or more parts given together
  new_type: none fits
format:
  pick_correct: the one true option
  pick_incorrect: the false statement (NOT, EXCEPT, wrong, false, mismatch)
  count_correct: how many listed items or statements satisfy a condition
  pick_correct_combination: a combination of lettered items
  pick_match_code: an A-?, B-? code
  pick_order: a sequence or ranking
  odd_one_out: the item not in a group or without a property
  calculate_value: a number
  derive_expression: a formula in given symbols
  pick_ratio: a ratio
  pick_proportionality: is proportional to
  name_or_identify: a name or term
  identify_structure_or_compound: a compound or structure
  predict_product: the product of a given reaction
  identify_reagent_or_condition: reagents, catalysts or conditions
  identify_reaction_or_process_name: the name of a reaction or process
  classify_into_group: the group, kingdom, phylum, class or family
  pick_explanation: the reason (because, due to, most appropriate explanation)
  predict_effect: what happens or stays constant when something changes
  pick_graph: a graph
  judge_two_statements: truth of Statement I and II
  judge_assertion_reason: A, R and whether R explains A
  pick_scientist_or_date: a person or a date
  expand_abbreviation: a full form
  new_format: none fits
content_shape: [one_line, list, example_list, table, diagram, labelled_diagram, graph, formula, derived_result, experiment_classic, practical_procedure, comparison, process, cycle_or_pathway, life_cycle, exception, classification_hierarchy, definition_term, trend, reaction_mechanism, structure_chemical, nomenclature_rule, value_or_data, scientist_history, applied_context, biological_equation, disease_cause, current_affairs, new_shape]
thinking_draft:
  recall: one fact decides the answer
  elimination: several separate statements must each be judged
  process: getting an order or chain right is the hard part
  confusion: the question explicitly contrasts similar things
  reasoning: judge whether a because holds
  diagram_graph: a figure or graph must be read
  application: apply an NCERT rule to a case NCERT does not describe
  numerical: choose a formula and calculate
thinking_candidates_for_owner: [trend_ranking, classification, proportional_reasoning, estimation, symbolic_derivation, spatial_structural, data_interpretation, experimental_reasoning, multi_concept]
trap: [look_alike_term, wrong_pairing, half_true, wrong_order, ignores_exception, extreme_word, old_ncert_fact, opposite_answer, calculation_slip, swapped_positions, number_near_miss, unit_conversion_slip, sign_or_direction, scientist_swap, name_variant, invalid_comparator, impossible_value, reversed_cause_effect, partial_combination, new_trap]
stem_context: [plain, case_scenario, experiment_setup, real_world, data_given, table_given, figure_given, reaction_given, equation_given, historical]
answer_form: [term, number_with_unit, expression, ratio, statement, combination_code, match_code, order, structure_image, graph_image]
negation: [none, single, double]
figure_role: [none, needed, decorative, options_are_figures]
confidence: [high, medium, low]
````

---

# Appendix E · Tests that must exist and pass

| # | Test | Must show |
|---|---|---|
| T1 | `latex_normalise` | `4 Ω`, `4\,\Omega` and `$4 \Omega$` are equal; `4 Ω` vs `40 Ω` differ; `−2` vs `2` differ |
| T2 | `normalise_quote` + `quote_verify.find` | a quote across a hyphenated line break is found; a paraphrase is not; a quote with "…" is rejected |
| T3 | `option_parser` inline | "The correct statement isa) Boron…b) Beryllium…c) …d) …" → 4 options |
| T4 | `option_parser` stem statements | "(a) Flowers… (b) Calyx… Choose… a) (a),(b) b) … c) … d) …" → statements stay in the stem; the last a)–d) run is the options |
| T5 | `option_parser` image options | empty option text with image crops → valid; empty text and no crop → invalid |
| T6 | `ids` | IDs never reused across restarts |
| T7 | `records` | every set field gets a `field_sources` entry |
| T8 | `coaching_guard` | a B6 or D7 input containing coaching provenance is rejected |
| T9 | runner idempotence | two `--auto` runs in a row: the second writes nothing |
| T10 | fallback chain | check fail → retry line; second fail → run B; disagreement → adjudicator; unsure → safe default or block, with the right flag |
| T11 | prompt version bump | bumping D4's version lists every D4 item again |
| T12 | stale handling | a stale item is listed before new items |
| T13 | A2 continuation | page N says continues, page N+1 says not → mismatch detected |
| T14 | A3 rejoin | a dropped block and a repeated block are both detected |
| T15 | A6 pairing | strong, weak, removed and added cases classified |
| T16 | A7 diff | a moved page break is not a difference |
| T17 | B2 numbering | a missing question number is detected; 200-question papers (2021–2024) pass |
| T18 | B3 checks | duplicated options flagged high; 3 options sent back to B2 |
| T19 | B4 compare | a digit difference is classified high; a spacing difference is not a difference |
| T20 | B5 join | joins use (paper_id, qno); a qno-only join is impossible |
| T21 | C1 key consistency | a wrong option map is caught |
| T22 | D4 link_type rules | rules_chained with one quote fails; states_answer with derivation steps fails |
| T23 | D4 derivation check | steps ending at 16 Ω match option "16 Ω"; steps ending at 8 Ω raise D4_DERIVATION_MISMATCH |
| T24 | D6 status rules | rule 0 gives latest_ncert for rule_used; 3b gives latest_ncert for a changed fact; beyond_ncert_method gives outside_rules |
| T25 | cascade | `cascade.py` from `steps.yaml` input_fields agrees with `cascade.yaml`; editing an official answer marks exactly the listed steps stale |
| T26 | D10 grouping | links A–B and B–C form one group |
| T27 | E1 patterns | each of the 16 pattern rules has a passing and a failing example (SPEC 13, E1 boundaries) |
| T28 | E2 negative guard | "NOT" with pick_correct is rejected; "incorrect statement(s)" with combination options keeps pick_correct_combination and records negation |
| T29 | codebook loading | with no `codebook/E2.md`, the input has `allowed` and no `codebook`; with the file, `codebook` is present and `codebook_version` is its hash |
| T30 | F4 counts | a repeat group of 2 counts once in unique_questions; totals equal question–subtopic links |

