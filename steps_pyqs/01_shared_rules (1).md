# Shared rules for NEET PYQ question analysis

**Version 2.1** (3 Nov 2026).
- Version 1 made the first physics, chemistry and biology pages.
- Version 2 added the subject experts' (SME) feedback from `PCB Artifact New Data Verification.xlsx` (round 1).
- Version 2.1 closes the gaps that six analysts reported after running version 2 on all 60 questions. It adds: rules for overfull cells, the topic-depth rule, what counts as "taught in NCERT", tie-breaks between levels, how to handle SME comments, how to count in the bank, and fixes for broken PDF text.

Every analysis prompt in this folder points here. Follow these rules exactly. Where a rule gives an example, the example comes from real SME feedback or from a version 2 run.

---

## 1. Level (Easy / Medium / Hard)

Rate the question by **what a well-prepared student actually does in the exam**. Assume the student solves every row of a match list and judges every statement. Do **not** lower the level because a clever option-elimination shortcut exists. Record that shortcut in `deep.check` instead.

Look at two things:
- **Load**: how many separate facts, formulas, reactions or terms the student must recall or check, and how fine they are.
- **Reasoning**: how many linked steps there are, where each step needs the result of the one before.

| Level | Rule |
|---|---|
| **Easy** | One fact, one formula or one NCERT line. One or two short steps. The question is (nearly) an NCERT line, example, table, figure or list. A good student needs well under a minute. |
| **Medium** | Two to four **standard** facts or formulas: a match list or statement set whose items are standard. Or a short list of two **fine** details. Or two or three linked steps. Or a standard calculation that appears in most test series. About one to two minutes. |
| **Hard** | Any one of these is enough. **(a)** A match list or statement set of four or five items, most of them **fine details**, reactions with reagents, or look-alike pairs. **(b)** Three or more linked steps on a set-up that is neither a straight NCERT copy nor a standard test-series pattern. **(c)** The deciding content is not taught in the current NCERT textbooks (see 1.2). **(d)** A good student needs more than about two minutes (see 1.3). |

### 1.1 Standard fact or fine detail?
A fact is **standard** if it is any of these:
- a main heading or a bold term;
- a boxed or numbered formula;
- a direct definition;
- an item that most test series ask.

It is a **fine detail** if it is any of these:
- inside a paragraph;
- an item in a long list;
- an exception or a number;
- a reagent condition;
- a word that has a look-alike among the other items.

Examples:
- Chemistry Q46 (five reagents from one NCERT equation) is **Medium**.
- Chemistry Q65 (four conversions, each needing its exact reagent set) is **Hard**.

### 1.2 "Taught in the current NCERT"
- "Taught" means the content is in the current NCERT **textbooks** (the PDFs in `NCERT_Books`).
- The lab manual, Exemplar and older editions do **not** count.
- Use Hard (c) only when the outside-NCERT content **decides the answer** and must be recalled or reasoned exactly. Calibration: Biology Q118 → Hard; Chemistry Q69 (phthalein test) → Hard, flagged for SME review.
- If the outside-NCERT part is only background, rate the question by its other lines. Example: a p-block question that is decided by an in-NCERT idea.

### 1.3 Judging time
Allow about 10 seconds per printed line to read, plus 20 to 30 seconds per fact recalled or step worked. Add these up. Say the estimate in `reasons` when time decides the level.

### 1.4 Adjustments and tie-breaks
- **Test-series adjustment.** If a question is Hard only because of its steps (b), and the pattern is standard, rate it one level lower. Evidence for "standard":
  - two or more near-twins in the verified bank, **or**
  - the pattern is an NCERT example or exercise.

  State the evidence. Examples: Biology Q117 → Medium; Physics Q27 → Medium; 21 June Q62 → Medium.
- **When two bands seem to fit:**
  - Choose Hard only if one of lines (a) to (d) clearly applies.
  - Choose Medium over Easy only if the question needs two or more facts or steps. A one-rule test-series calculation stays Easy; example: Chemistry Q86.
- **A genuine Hard with a counter-argument** may carry a reason titled "Why some would call it Medium" without `borderline`. Use `borderline: true` only when the question does **not** meet any Hard line and is used only because nothing better exists.

### 1.5 Calibration examples (SME round 1 = S; version 2 runs = V)

| Question | Level | Why |
|---|---|---|
| Physics Q1, Sun–Earth distance with c = 1 (S) | Easy | One step. |
| Physics Q2, match four elastic-constant formulas (S) | Medium | Four standard formulas. |
| Physics Q27, bent-square balanced bridge (V) | Medium | Steps only; standard pattern with a bank twin. |
| Chemistry Q46, five reagents for nitriles (S) | Medium | Standard items from one equation. |
| Chemistry Q52, metamer pair, four pairs to check (S) | Medium | |
| Chemistry Q65, match four conversions with reagents (S) | Hard | Fine reagent details. |
| Chemistry Q86, Ea from ln k (V) | Easy | One rule. |
| Biology Q104, statements on naming rules (S) | Medium | |
| Biology Q109, five steps of DNA fingerprinting in order (V) | Medium | One NCERT list, five steps. |
| Biology Q138, five steps of respiration in order (V) | Easy | NCERT's list, shuffled. |
| Biology Q172, two Bt genes (V) | Medium | Two fine details. |
| Biology Q96, match four kinds of productivity (S) | Hard | Look-alike terms. |
| Biology Q120, long statement set on restriction enzymes (S) | Hard | |
| Biology Q118, Solanaceae floral formula (S) | Hard | Fine marks in the formula. |
| Biology Q117, ATP and NADPH for one glucose (S) | Medium | Standard test-series calculation. |
| Biology Q124, drones make sperm by mitosis (S) | Hard | |

Always record the questions file's label in `fileLevel`. Record the earlier round's level in `previousLevel`: leave it out for questions new to the grid, and write `"hard (borderline)"` if the earlier pick was borderline.

---

## 2. Chapter and topic

Pick **ONE final topic** from the AWS table `ExamChapterTopicMappings`. Use its exact chapter display name, chapter code, topic number and topic name. It is the only topic shown up front; showing two or three topics confused the SMEs.

**How to choose, in this order:**
1. **Find the deciding fact's NCERT section.** In a statement set, use the section of the false (deciding) statement. If several statements decide it, use the section most of them come from.
2. **Match a table topic to the NCERT section.**
   - Prefer table topics that match a numbered NCERT heading over topics that cut a section into finer pieces.
   - **If the table has both a topic for the NCERT section and a narrower sub-topic inside it, use the section topic.** Example: "Tools of Recombinant DNA Technology", not "Restriction Enzymes and Their Types" (SME round 1, Biology Q120).
   - Say in `whyTopic` that you applied this rule.
3. **Tie at the same depth:** choose the topic where the verified bank already files most questions like this one. Say which keywords you counted with.
4. **If the NCERT-matching topic is nearly empty in the bank** while another topic holds most such questions, still use the NCERT-matching topic. Add a `bank_gap` table issue that names where the bank files them (example: 21 June Q69 → "Work Done").
5. **Branch vs chapter.** The question's **branch** comes from the subject notes (paper section or branch list). Its **topic** comes from the chapter where the deciding fact lives, even if that chapter belongs to another branch. Example: Chemistry Q47 is in the physical list but its topic is in the d- and f-block chapter.

**Other fields:**
- `ncertTopic`: the current-NCERT section number and title where the deciding fact is, e.g. "5.1.1 Regions of the root".
  - For an NCERT example or exercise, give the section and add "Example 6.11".
  - If the content is not in the current NCERT, write "Not in current NCERT" and add what you know: "(older books: Unit 7, 7.3)" or "(NEET syllabus: experimental skills)".
- `others`: at most two rejected candidates, each with a reason that starts "Rejected because". Add `chapter` when a candidate is in another chapter. The page shows them only behind "Why not these topics?".
- `tableIssues`: add an item whenever the table topic's name is not NCERT wording, names things the current NCERT does not teach, is missing, is duplicated, has odd numbering, or the bank has a gap. **Do not change the table topic to hide a problem.**

---

## 3. NCERT references

- Always cite the **current NCERT** (2026-27 reprint, the rationalised books in `Arivihan_Work/NCERT_Books/chapters/`).
- Always give the **section number and section title together**, e.g. "NCERT Class 12 Chemistry (current book), Unit 10 Biomolecules, section 10.5 Nucleic Acids".
- Add the older-book number when you are sure. A map is in `04_subject_notes.md`; SMEs often use older books, and in round 1 two correct references were marked "wrong" because of this.
- Cite only what you found in the PDF. When the paper copies an NCERT line with one change, quote the line and name the change.
- **Broken text extraction.** Some PDFs come out garbled (see the subject notes). Render the page with `pdftoppm -f N -l N -r 150 -png` and read the image. For `keph107`, the private-use characters decode by subtracting 0xF000.

---

## 4. Explanation ("About the question")

- `explain.asks`: the question in plain words, one or two sentences.
- `explain.idea`: the concept behind it in two or three short sentences.
- **Use NCERT's exact technical terms**, e.g. "region of maturation", "in parallel", "revolutions". Never replace them with everyday words; in round 1 an SME found the simplified wording hard to follow.
- Keep sentences short and the joining words simple. The readers are students and subject experts.

---

## 5. Traps

### 5.1 Every wrong option gets a path
For each wrong option, write:
- the student's own steps, with right steps marked `ok` and the breaking step marked `bad` plus a short fix;
- **who falls**;
- **why it feels right**.

### 5.2 Trap sources: check these first, and name them exactly
1. **Look-alike words or terms**: maturation vs meristematic, lyase vs ligase, GPP vs NPP, dπ–pπ vs dπ–dπ.
2. **Half-true options**: say which half is false. Example: Chemistry Q51, "RNA is single-stranded" (true) "and contains thymine" (false).
3. **NCERT neighbour swap**: the fact printed next to the right one.
4. **Old NCERT answer** printed when the paper changed a number in an NCERT example.
5. **Numerical slips**: a missing factor, unit or power of ten, a sign, log vs ln, an inverted ratio. Test candidate slips with a short script.
6. **A formula or picture used outside its condition**.

### 5.3 No generic traps
Never write "a student who does not know may tick any option". If no natural path leads to an option, mark it `filler` and say what you checked.

### 5.4 Fastest route and quick check
- `deep.check` starts with one bold title, e.g. `<b>Fastest route</b>`, then plain text. That title is the only `<b>` in `check`.
- `deep.idea` says how the options are built.
- `deep.notCaught` lists mistakes the options do not catch.

### 5.5 SME comments that need care
- **Generic trap comment** ("the student may fall into any option"): keep the specific paths, and say so in `smeNotes`.
- **The SME names the key as a trap** (e.g. "options 1, 2, 3" when option 2 is the key): read it charitably. For example, the options share a row, so one row cannot decide. Say so in `smeNotes`.
- **The SME's level is right but the reason is wrong** (e.g. Q118 "outside NCERT", but it is in NCERT): follow the level, and correct the reason in `smeNotes`.
- **The SME objects to a table topic name**: log a table issue. It is not an analysis error.

---

## 6. Choosing questions for a grid

### 6.1 Filling cells
Fill each cell (branch × level) with exactly the asked number. If a cell is **short**, use this order:
1. code 11;
2. the valid 21 June paper (code 50);
3. `borderline` (the hardest left).

Previous-round code 50 picks are **dropped** when code 11 can now fill the cell.

### 6.2 Overfull cells
If a cell is **overfull** after re-rating, keep questions in this order of priority:
1. SME-reviewed questions;
2. code 11 over code 50;
3. a mix of question types;
4. stronger trap teaching (fewer fillers);
5. the previous round's pick.

Save every rated question you leave out in `data/reserves_<branch>.json`, as `[{"id", "n", "paper", "level", "reason"}]`, so its rating is not lost.

### 6.3 Other choosing rules
- Prefer a mix of types: single MCQ, match, statements, sequence, two-part, figure, numerical.
- Avoid questions with disputed answers (see the subject notes) unless you settle them with certainty.
- Look at the printed image of every question you choose.

---

## 7. Checking answers

- **Code 11** (the cancelled 3 May paper): the Aakash answer, `answer.publisher`. NTA never released a key. If the file's AI disagrees, settle it from NCERT or the printed image.
- **Code 50** (the valid 21 June paper): the NTA final key CSV. Trust NTA over Aakash.

---

## 8. Counting in the question bank

- Get topic ids from the snapshot's `topic_id` field.
- Add `options` to the query projection, and follow `LastEvaluatedKey` if the result is paged.
- Recount; do not reuse an earlier round's counts.
- Report every count with the keywords or filter you used, e.g. "12 of 47 (keywords: rpm, revolution)". The bank holds some duplicate items, so say "(N different texts)" when that matters.

---

## 9. Writing rules

- Very simple English: short sentences, common words, active voice.
- No Hindi or Devanagari in the output.
- No em-dash asides and no "not X but Y" construction. A plain "X, not Y" is fine.
- Allowed HTML inside strings: `<b>`, `<i>` (scientific names), `<sub>`, `<sup>`.
- Never invent bank counts or NCERT references.

---

## 10. Before saving, check

- [ ] Exactly one option has role `correct` and exactly one has role `main`. Traps are ordered: main, other traps, fillers, correct.
- [ ] The answer matches the key (section 7).
- [ ] The printed image of every chosen question was viewed.
- [ ] Every NCERT reference was found in the PDF, with section number and title.
- [ ] One final topic is given (section 2). `ncertTopic` is filled. `tableIssues` is filled where needed.
- [ ] The level follows section 1, and any change from `previousLevel` is explained in `reasons`.
- [ ] The grid is exactly full. Questions left out are in `reserves_<branch>.json`.
- [ ] The JSON is valid and passes `build_page.problems()`. Required fields are listed in `03_output_schema.md`.
