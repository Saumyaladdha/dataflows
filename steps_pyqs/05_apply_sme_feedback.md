# Prompt: apply a round of SME (subject expert) feedback

Use this after the subject experts fill in a review sheet like `PCB Artifact New Data Verification.xlsx`. That sheet has one tab per subject and one block per question, with four rows: About the question, Chapter and Topic, Level, Trap inside the question.

---

## Step 1: turn the sheet into data

```
<venv-python> ../builder/read_sme_sheet.py "<path to the .xlsx>" ../data/sme_review_round<N>.json
```

`<venv-python>` is any Python that has `openpyxl`, for example `Arivihan_Work/Student_Data_Studies/gems_student_definition/.venv/bin/python`. Blank rows mean "not reviewed yet". Comments may be in Hinglish.

## Step 2: read the comments and sort them

For tricky comments, also follow `01_shared_rules.md` §5.5: generic traps, the key named as a trap, or the right level with the wrong reason.

Sort every comment into one of these kinds:

| Kind | What to do |
|---|---|
| **Level** | Follow the SME unless the comment rests on a factual mistake. Then add the question as a new calibration example in `01_shared_rules.md` §1, so the rubric itself learns. |
| **Topic** | Switch to the topic the SME names if it exists in the AWS table. If it does not exist, keep the closest table topic and add a `tableIssues` item. If the SME objects to a table topic *name*, that is a table issue, not an analysis error. |
| **NCERT reference** | Check it in the current NCERT PDF first. If ours is right for the current book, keep it, add the section title, and note the older numbering if it is known. Do not change a correct reference. |
| **Explanation wording** | Rewrite with NCERT's exact terms. |
| **Trap** | Add the trap the SME names (often a look-alike word or a half-true option) as the main trap or as an extra way. Keep the student-path format. |
| **"All good"** | Keep the entry as it is. |

## Step 3: update the rules, then the data

1. Add anything general you learned to `01_shared_rules.md`: new calibration examples, a new trap source, a new topic rule. Raise its version number and say what changed.
2. Add question-specific facts to `04_subject_notes.md`.
3. Re-run `02_analyse_branch.md` for each branch that has comments. The prompt tells the analyst to reuse the previous round and apply the comments. Record how each comment was handled in that question's `smeNotes`; the page shows it as "Expert review". Questions that leave the grid go to `reserves_<branch>.json`.
4. Re-write the findings with `06_write_findings.md`.

## Step 4: rebuild, publish and report back

- Rebuild the pages with `../builder/build_page.py` and republish them to the same artifact links.
- Make a fresh review sheet for the next round with `../builder/make_sme_sheet.py`.
- Send the table problems (`tableIssues`, collected by the builder into `AWS_Topic_Table_Issues.md`) to whoever maintains the AWS table.
