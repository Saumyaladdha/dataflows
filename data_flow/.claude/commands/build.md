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
