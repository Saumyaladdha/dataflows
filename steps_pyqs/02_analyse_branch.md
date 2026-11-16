# Prompt: analyse one branch of NEET questions

Copy this prompt into a new Claude session (or give it to a helper agent). Fill in every `{{…}}` value first. Run one copy per branch; branches can run in parallel.

**Values to fill:**

| Placeholder | What to put |
|---|---|
| `{{SUBJECT}}` | Physics / Chemistry / Biology |
| `{{BRANCH}}` | physics / organic / inorganic / physical / botany / zoology |
| `{{N_PER_LEVEL}}`, `{{N_TOTAL}}` | e.g. 3 and 9, or 5 and 15 |
| `{{PIPELINE}}` | this `pipeline` folder |
| `{{ANALYSIS}}` | the folder above it (`Analysis_of_NEET_PYQ`) |
| `{{PAPERS}}` | `Arivihan_Work/NEET_Question_Papers` |
| `{{NCERT}}` | `Arivihan_Work/NCERT_Books` |
| `{{WORK}}` | a scratch folder for downloads, extracted text and scripts (never inside `{{PIPELINE}}`) |

---

You are analysing NEET **{{SUBJECT}}** questions, branch **{{BRANCH}}**, for Ekta (Head of AI at Arivihan, an Indian edtech for NEET and board students).

**Your job:** fill a grid of **{{N_PER_LEVEL}} Easy, {{N_PER_LEVEL}} Medium and {{N_PER_LEVEL}} Hard** questions from this branch, and write a deep analysis of each as JSON.

## Read first (stay inside these folders; never open personal files on this laptop)
1. The rules, which you must follow exactly: `{{PIPELINE}}/prompts/01_shared_rules.md`
2. The output schema: `{{PIPELINE}}/prompts/03_output_schema.md`
3. The notes for this subject: `{{PIPELINE}}/prompts/04_subject_notes.md`. These cover:
   - the branch question lists for code 11 and code 50;
   - questions to avoid;
   - the map from old to new NCERT numbering;
   - PDFs whose text comes out broken.
4. A finished example of each question type in `{{PIPELINE}}/data/` (see 03).
5. The previous round for this branch, if it exists: `{{PIPELINE}}/data/<branch>.json` (current) or `{{PIPELINE}}/data/previous_round/{{BRANCH}}.json` (version 1).
   - Reuse what is still right, and re-rate every level with the current rubric.
   - Apply every SME comment for this branch from the newest `{{PIPELINE}}/data/sme_review_round*.json`.
   - Questions may move between cells: refill short cells and trim overfull ones (rules §6).

## Inputs
- **Questions file**, NEET 2026 code 11 (the cancelled 3 May paper): `{{ANALYSIS}}/questions.json`. Each question has a printed image at `question.screenshot.cdn_url`.
- **Valid 21 June paper**, code 50, used only to fill short cells:
  - text: `{{PIPELINE}}/data/code50.txt` (Aakash prints "Answer (x)" under each question; split on form feeds `\f` to find a question's page);
  - PDF: `{{PAPERS}}/NEET_2026/ReNEET_2026-06-21_Valid_Paper/ReNEET2026_Code50_Questions_Answers_English.pdf`;
  - NTA final key: `{{PAPERS}}/NEET_2026/NTA_Official/NTA_ReNEET2026_Final_Answer_Key_All_Codes.csv`.
- **AWS topic table** (saved copy): `{{ANALYSIS}}/ExamChapterTopicMappings_snapshot_2026-11-03.json`.
  - To refresh it: `aws dynamodb scan --table-name ExamChapterTopicMappings --output json`.
- **Verified question bank** (read-only; used for topic tie-breaks and evidence):
  `aws dynamodb query --table-name NEETAdaptiveQuestionGeneratorDataVerified --index-name topic_id-difficulty_level-index --key-condition-expression "topic_id = :t" --expression-attribute-values '{":t":{"S":"<topic_id>"}}' --projection-expression "question_id,question,options,difficulty_level" --output json`
  - Follow `LastEvaluatedKey` if the result is paged. The AWS CLI is logged in; region ap-southeast-1.
- **NCERT PDFs** (current books): `{{NCERT}}/chapters/`. Extract text with `pdftotext -layout`. If the text is garbled, render the page (rules §3).
- **Images**:
  - Code 11: `curl` the `cdn_url` into `{{WORK}}` and open it with the Read tool.
  - Code 50: crop the question with `pdftoppm -f N -l N -r 200 -x X -y Y -W 1470 -H H -png <pdf> <out>` and open it to check. Record it as `{"source":"pdf50","page":N,"y0":Y,"y1":Y+H}`, measured on the 200 dpi render and excluding the "Answer (x)" line. The builder crops at x = 110, width 1470.

## Output
1. `{{PIPELINE}}/data/{{BRANCH}}.json`: a JSON array of exactly **{{N_TOTAL}}** objects, following `03_output_schema.md`.
2. `{{PIPELINE}}/data/reserves_{{BRANCH}}.json`: every rated question you left out, as `[{"id","n","paper","level","reason"}]`.
3. Put everything else (images, text, scripts) in `{{WORK}}`.

## Final reply (keep it short)
- The chosen questions, with level and a one-line reason each.
- Which questions changed level or cell compared with the previous round, and why.
- How each SME comment was handled.
- Which questions came from code 50, and why.
- Any answer disputes.
- New `tableIssues`.
- Anything in these prompt files that was unclear or missing. The prompts are reused, so this feedback improves them.
