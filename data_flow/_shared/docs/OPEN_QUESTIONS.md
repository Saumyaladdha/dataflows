# Open questions and chosen defaults

Per SPEC Section 0.3: when something is unclear, do not stop and wait for a person (people act only in Stage F). Pick the safest reading that keeps every rule in Section 4, then record the question and the chosen default here with the date, the section number, and what was done. New entries are appended below the seed list as they come up during the build and run.

## Seed entries (from SPEC Section 20, open decisions for the owner)

- **2026-10-08 — Section 20, #1.** Decision: Include NEET 2013 and AIPMT 2014–2015 in the bank? Default until decided: No — register them, `in_scope = no`.
- **2026-10-08 — Section 20, #2.** Decision: Collect 2020–2025 main papers, the 2020 re-exam and the 2024 retest (missing from the analysed data). Default until decided: Intake flags them missing.
- **2026-10-08 — Section 20, #3.** Decision: Pilot chapters. Default until decided: Section 18.1 defaults.
- **2026-10-08 — Section 20, #4.** Decision: Coaching solutions: licensed? Default until decided: Not licensed — reviewer reference only, never in agent inputs.
- **2026-10-08 — Section 20, #5.** Decision: Codebooks for E1–E6, D4 link_type, D11. Default until decided: None yet — agents use Section 17 lists; E4 flags `E4_NO_CODEBOOK`.
- **2026-10-08 — Section 20, #6.** Decision: Hindi. Default until decided: English only.
- **2026-10-08 — Section 20, #7.** Decision: NCERT Exemplar as an extra source (would turn some beyond_ncert_method questions into linked ones). Default until decided: Not used.

## New entries

- **2026-10-09 — Section 9 (A1/A2), file-layout mismatch.** A1's procedure assumes one PDF per whole book, with a title/imprint page to read for the reprint line. The real files in `inputs/ncert/latest/` and `inputs/ncert/older/` are one PDF per chapter (`Chapter_N.pdf`, or for some older-edition subjects `CH-N.pdf` / `Old_ncert_<Subj>_Chapter_N.pdf`), with no single book-level PDF. Decision: treat the full chapter-PDF set for one subject×class×edition as one logical "book" for registration — one `book_id`, one `register/books.csv` row, with the reprint-year line sourced from whichever chapter file actually carries it (usually `Chapter_1.pdf`, confirmed present there for all sets checked so far). A1's check ("exactly one latest and one older book per subject-class") becomes "exactly one latest and one older *chapter set*." Downstream (A2 passage addressing, A3 chapter lists) is unaffected since passage IDs are already addressed by chapter number from the folder/file, not from a monolithic PDF's internal structure.
- **2026-10-09 — Section 9 (A1/A2), older-edition filename inconsistency.** Older-edition chapter filenames aren't uniform across subjects (`CH-N.pdf` for Chemistry, `Old_ncert_Physics_Chapter_N.pdf` / `Old_ncert_Bio_Chapter_N.pdf` for Physics/Biology, vs. the clean `Chapter_N.pdf` used everywhere in `latest/`). Decision: chapter-number extraction (wherever it lives — A1/A2 scripts or a shared helper) must normalize across all three older-edition naming patterns plus the latest-edition pattern; not something the spec text anticipated, so documenting here rather than silently working around it in code with no record.
- **2026-10-09 — Section 8 (S0), `inputs/manifest.csv` does not exist yet.** S0's whole procedure reads this file, which hasn't been created. Deferred until `scripts/intake_check.py` is written (M3) — at that point either hand-build it from the real `inputs/` tree now in place, or have intake_check.py generate a first-pass version itself. Not resolved yet; flagging so S0 isn't run against a missing file by mistake.
- **2026-10-09 — Section 5.4, `status.py` precedence for `stale`/`skipped` not specified.** Spec only orders `blocked > flagged > pass`. Decision: derived `blocked > stale > flagged > pass > skipped` from how 5.9 describes `stale` (known-invalid, must re-run before anything downstream trusts it) and `skipped` (step genuinely doesn't apply, neutral) — implemented in `scripts/lib/status.py` with reasoning in its comments.
- **2026-10-09 — Section 5.7, `latex_normalise`'s `\,` `\;` `\!` "remove" instruction.** Literal deletion breaks the normalisation's own invariant (`4\,\Omega` would stop equalling `4 \Omega`). Decision: replace with a single space instead of deleting outright, since that's the only reading under which T1's required equalities hold.
- **2026-10-09 — Section 2.6, `option_parser.py` marker ambiguity in the spec's own worked example.** A bare marker (`a)`) and a parenthesized marker (`(a)`) can both appear in one question (stem statement labels vs. real options), and treating them as one pool corrupts run-detection. Decision: treat bare and parenthesized markers as separate pools, matching how the spec's own example uses them.
- **2026-10-09 — M1 build environment.** `claude` CLI isn't on `PATH` in this environment, so `scripts/lib/agents.py::call_headless` (the `--auto` headless mode, spec 5.2) raises `NotImplementedError` with a docstring explaining what's needed — not yet implemented, not guessed at. Also: PyMuPDF was installed into a project-local `pyq_bank/.venv` rather than system Python (which is externally-managed/Homebrew-protected) — activate that venv before running anything under `scripts/`.
- **2026-10-09 — Section 8 (S0), confirmed-missing required inputs.** Per the real file audit: `inputs/ncert/lab_manuals/` is empty (Physics and Chemistry lab manuals required by S0, not yet collected), `inputs/ncert/older/Class_11th/{Biology,Chemistry,Physics}/` are empty (Class 11 older edition not yet collected — owner is adding this), `inputs/notices/` and `inputs/coaching/` are empty. These will correctly surface as `S0_MISSING_INPUT` blocker flags once S0 actually runs — expected current state, not a bug, recorded here so it isn't re-discovered as a surprise later.
- **2026-10-09 — Section 8 (S0), `inputs/manifest.csv` built, `scripts/intake_check.py` run for real.** `scripts/build_manifest.py` (a one-off builder, not a Sections 8-14 step) walked the real `inputs/` tree and wrote `inputs/manifest.csv` (359 rows: 126 ncert, 181 paper, 30 key, 22 legacy_sheet). Several judgment calls made along the way:
  - **CANCELLED sittings need no key.** S0's procedure step 3 literally requires a paper *and* a final key for every sitting on the calendar, including 2026 CANCELLED. A cancelled exam is never scored and so has no official final key by definition (confirmed in the Codebook: "expected: a cancelled sitting has no final key"). Decision: `scripts/intake_check.py` still requires the CANCELLED *paper*, but does not require a CANCELLED *key* (see `scripts/lib/sittings.py :: SITTINGS_WITHOUT_KEY_REQUIREMENT`).
  - **Ambiguous sitting splits are never guessed, and are treated as still-missing.** 2016 (MAIN/PH2), 2019 (MAIN/REEXAM), 2020 (MAIN/REEXAM) and 2024 (MAIN/RETEST) have paper and/or key files that don't distinguish which sitting they belong to by filename alone (documented as open in the Codebook itself). `build_manifest.py` leaves `sitting` blank for these rather than guess; `intake_check.py` then treats *both* required sittings for that year as `missing` (not `present`) with a message naming the candidate files, since presence of an unsplit file doesn't confirm presence of either specific sitting. This correctly produces more `S0_MISSING_INPUT` flags than a naive "file exists → present" check would, which is the point (don't silently mark something present that can't actually be verified).
  - **`inputs/_reference/` is out of S0's scope entirely.** The Codebook (Section 7) explicitly documents the Mathpix OCR material there as "not wired into intake as a formal source." Decision: `intake_check.py`'s file↔manifest reconciliation walk (procedure step 1) skips `inputs/_reference/` rather than flagging its 4 files as unmanifested.
  - **2018's per-booklet-code keys are checked against 2018's per-booklet-code papers, one code at a time**, beyond the literal year×sitting grain procedure step 3 names — because that same step's Reads line already asks for "a final key whose booklet code matches the paper (or a key covering all codes)," and 2018 is the one year in this drop where that finer match is actually checkable (keys are per-code, not one file for the year). This surfaced one real, genuine gap: paper booklet code `QQ` (2018) has no matching key file (the key set has 19 codes, the paper set has 20; `QQ` is the only one missing).
  - **2012's paper PDF is confirmed absent** (only a legacy spreadsheet exists) — out of scope anyway (pending Section 20 decision #1), but recorded as an informational `out_of_scope` item in the report rather than silently omitted, since it's a real collection gap per the Codebook, not just an in-scope/out-of-scope distinction.
  - **S0's own item status is `flagged`, never `blocked`**, even though many required items are genuinely missing. Spec 5.4 defines `blocked` as "later steps skip the item," but S0's own "On failure" line says "the rest of the run continues" — so blocking the single `inputs` item would contradict that. Individual missing books/papers/sittings get their own `S0_MISSING_INPUT` blocker *flags* (as the spec requires); the step's own overall status in `steps/S0/status/inputs.json` is `flagged` whenever any such flag exists, `pass` otherwise.

- **2026-10-09 — Section 5.1/5.2/5.5, `run_step.py`/`run_stage.py`/`scripts/checks/*` built and run against real data (S0, A1–A9).** `scripts/CONVENTIONS.md` now defines the `--auto` calling convention (`python3 scripts/<script>.py --chapter-id <ID>`, writes directly to the spec-mandated path, never to `steps/<STEP>/out/`, raises flags via `lib/flags.py`) — validated for real against the parallel A6/A7/A9 build. Judgment calls:
  - Single-run steps use run label `"runA"`, not `"run1"` (spec names both patterns loosely; picked the one consistent with the two-run steps' `runA`/`runB` naming).
  - A1's `edition_seen` check compares against the work input's `folder_edition_hint` (sourced from the manifest-driven folder layout) rather than reading `inputs/manifest.csv` directly a second time — they agree in practice, just avoids a redundant read.
  - Retry's `"PREVIOUS ATTEMPT FAILED: <message>"` text (spec 5.5) is embedded as a `previous_attempt_failed` field in the retry work-input JSON, since neither `lib/agents.py::build_instruction_line` nor `.claude/commands/run-step.md`'s fixed instruction line has a slot for it.
  - Cross-step readiness (e.g. "has A1 run yet") is keyed on each step's spec-mandated output artifact actually existing (`register/intake_report.md`, `ncert/pairs/<CHAPTER>.json`, etc.), not a separate invented status scheme — this turned out to matter once the parallel-built A6/A7/A9 scripts landed mid-build and needed to read real state.
  - **Known gap, not yet fixed:** the generic fallback resolver only implements retry→safe_default; it does not yet drive the `adjudicator` rung for steps whose chain requires one with no preceding retry (A5's chain is "unsure → adjudicator → still unsure → none"). A5 `--list` surfaces correctly but a failing A5 check currently has nowhere to route beyond safe-default. Needs a follow-up pass before A5 can run for real with full fallback fidelity.
  - Also not yet testable: A6's weak-pair adjudication *surfaces* via `--list` (confirmed working) but nothing resolves it without a real `x-adjudicator` agent call, since that agent hasn't been run yet.

- **2026-10-09 — Section 9/A2 check (2), real bug found and fixed: cross-page continuity check was never implemented.** `scripts/checks/A2.py`'s docstring claimed the check (page N's `last_block_continues_on_next` == page N+1's `first_block_continues_from_previous`) was handled "at the plugin level," but `A2Plugin.check()` never actually did this — confirmed by running A2 for real on `BIO12L` (23 pages, all independently read by separate real subagent calls): `--check` returned `DONE` with zero `A2` flags, even though a manual cross-check found a genuine mismatch at pages 1→2. Fixed by adding `A2Plugin._check_cross_page_continuity()`, which now raises a deduplicated `A2_JOIN_ADJUDICATED` (normal) flag per mismatched boundary, evidenced by both pages' output paths, matching the A6_WEAK_PAIR precedent (flag + keep going, since no synchronous adjudicator call is wired in yet).
- **2026-10-09 — Real finding from the fixed check, not just a bug report: the continuity flag's page-level definition breaks down around interleaved figures.** Re-running the fixed check against `BIO12L`'s 23 real pages found **7 of 22 page boundaries (32%) genuinely disagree** — not random noise. The pattern is systematic: on several of these pages (e.g. page 2), a figure sits spatially first, with the text that actually continues from the previous page appearing in a *later* block further down. Since `first_block_continues_from_previous` is defined as whether the page's literal first block continues, it correctly reads `false` in these cases even though the page's body text does continue — a structural mismatch between the flag's definition and NCERT's common two-column/figure-interleaved layout, not a reading error by either page's agent. **Not yet resolved**: needs either (a) a real adjudicator pass on these 7 pairs, or (b) refining the flag's definition/the a2-page-reader prompt to ask "does *any* early block continue" rather than strictly "does the first block continue," before this pattern can be trusted to self-resolve at scale across the full ~126-chapter corpus.

- **2026-10-10 — Decision: the current NEET paper/key dataset is accepted as final; we build against it as-is rather than waiting for better sources.** Full re-check confirmed nothing changed in the source drop (all 181 papers, 30 keys, 22 legacy sheets byte-identical to what's already copied), 2012/2026 papers remain genuinely absent, and the two known defects from the 10-paper validation (answer/solution overlay baked into every paper file; missing images) stand as documented in `docs/MASTER_PLAN.md` §2.1.1. Proceeding does not mean treating these as resolved — see the Master Plan's risk register (§7, risk #1) for the concrete fix needed before Stage B output can be trusted.
- **2026-10-10 — Decision: lab manuals resolved as reference-only, real gap stays open.** 4 new PDFs appeared in the source drop under `NCERT_Manual/` — genuine NCERT publications, but model-kit instruction booklets (molecular/solid-state/atomic model kits, a microscale chemistry kit), not the Laboratory Manual books with actual experiment write-ups that spec's Core Concepts define as the `lab_manual` source. Filed at `inputs/_reference/ncert_model_kits/`, explicitly **not** as `kind: lab_manual` in the manifest, so S0's `S0_MISSING_INPUT` flag for the real Laboratory Manual books stays honest. A standalone `NCERT-Class-11-Biology.pdf` found elsewhere in Downloads was also checked as a possible Class-11-older candidate and ruled out — its chapter list matches the *latest* edition exactly, and it shows no NCERT watermark/QR code/reprint stamp (third-party reformatted, same signature as the paper scrapes), so it isn't authoritative either.
- **2026-10-10 — Real data-integrity bug found and fixed: earlier A6/A7/A9 fixture testing wrote directly into real pipeline paths instead of an isolated test location.** Before running real A3/A4/A5/A8, found that the hand-built Evolution/Biodiversity fixtures used to validate A6/A7/A9 (see the 2026-10-09 A6/A7/A9 build entry above) were written into `ncert/passages/`, `ncert/chapters/`, `ncert/subtopics/`, `ncert/links/`, `ncert/pairs/`, `ncert/diffs/`, `ncert/change_log.csv`, `ncert/deleted_topics.csv`, `flags/flags.jsonl`, `run_log.csv`, and `steps/{A6,A7,A8,A9}/` directly — the same paths real pipeline output would use — rather than an isolated fixtures directory. Running real A3 would have appended real passages into the same file as fake ones. **Fixed:** all fixture-only files moved to `tests/fixtures/stage_a_validation_2026-10-09/` (preserved, not deleted); `flags.jsonl` and `run_log.csv` (which mixed real S0/A1/A2 entries with fixture ones) were surgically filtered to remove only the fixture rows, keeping every real entry. Re-verified `A1 --check` and `A2 --check` both still return `DONE` after the cleanup. **Lesson for future fixture-based testing in this project: always use a path under `tests/fixtures/`, never the real `ncert/`/`steps/`/`flags/`/`run_log.csv` paths, even for a quick validation pass.**
- **2026-10-10 — Real architectural bug found and fixed: A2 only ever processed the single chapter file A1 used for registration, never a book's other chapters.** `A2Plugin.list_items()` resolved a book's PDF via the single representative file in `register/books.csv`'s `file` column and rendered only that file's pages — meaning the pipeline as built could never index more than one of a subject's ~13-19 NCERT chapters. Fixed: `A2Plugin` now enumerates every chapter PDF for a book's (edition, class, subject) group via `rc.iter_ncert_files()`. New item-ID scheme: A2 pages are `{book_id}-ch{chapter_num:02d}-p{page:03d}` (page numbering restarts per chapter file, so chapter must be in the key); A3 sections are `{book_id}-ch{chapter_num:02d}-s{ordinal:02d}`. `previous_page_last_block` and the A2 cross-page continuity check are both strictly scoped to `(book_id, chapter_num)` — a chapter's page 1 never inherits continuation from a different chapter's last page. `chapter_num` is now carried on every block (`ncert/blocks/<BOOK>.jsonl`) and passage (`ncert/passages/<BOOK>.jsonl`). The original 23 real Chapter-1 pages were migrated to the new ID scheme and backfilled with `chapter_num: 1` (they predate this fix and lacked the field) rather than discarded — re-verified `pass` status intact afterward, 0 duplicated flags, 0 spurious run_log rows.
- **2026-10-10 — A3's `_sections()` grouped on a field (`section_heading`) that doesn't exist in real A2 output**, collapsing every block in a book into one giant "default" section instead of real per-heading sections. Fixed: sections are now derived from the real block stream itself — scoped per `(book_id, chapter_num)`, a new section starts at every `kind:"heading"` block, blocks before a chapter's first heading form an implicit opening section. **A real ordering bug was found in the process and is itself worth flagging**: `ncert/blocks/<BOOK>.jsonl` is not reliably in page order (A2's `check()` discovers work-input files via `os.listdir()`, unsorted), so the section-cutting walk now explicitly sorts blocks by `(page, n)` first — not optional, confirmed required against real data (an unsorted walk put chapter 1's "EXERCISES" section ahead of "CHAPTER 1"/the real title banner).
- **2026-10-10 — A3 never wrote `ncert/chapters/<SUBJ><CLASS>.json`** (spec Section 9's required by-product, needed by A4/D1), despite real A3 output existing. Fixed, but the first version of the fix had its own real bug: `_update_chapters_file`, called once per section inside `_post_assembly` with an "only set the title if unset" guard, raced across sections resolving out of order and permanently locked in "EXERCISES" as `BIO12-CH01`'s title instead of "SEXUAL REPRODUCTION IN FLOWERING PLANTS" — confirmed on real data, and unrecoverable by rerunning (the guard prevents ever overwriting a wrong title once set). Replaced with a stateless `_rebuild_chapters_file(book_id)`, called once per book at the end of `A3Plugin.check()`, that recomputes the whole chapter's title + headings from scratch from `_sections()` every time — title = the lowest-ordinal section's title-candidate heading, headings = every numbered heading in ordinal order. Two further real-data fixes folded into `_classify_heading`: (a) the heading-number regex needed `re.DOTALL` — a real heading wrapping across two lines in one block (`"3.1 REPRODUCTIVE HEALTH – PROBLEMS AND\nSTRATEGIES"`) was silently misclassified as a title candidate instead of a numbered heading; (b) the chapter-opener banner shape differs by chapter — Chapter 1's agent read "CHAPTER 1" and the real title as two separate heading blocks, Chapter 3's agent merged them into one block (`"CHAPTER 3\nREPRODUCTIVE HEALTH"`) — `_classify_heading` now strips a leading `"CHAPTER N"` prefix regardless of which shape it arrives in, so both resolve to the same clean title. Verified on real data: `BIO12-CH01` → "SEXUAL REPRODUCTION IN FLOWERING PLANTS" (11 headings, 1.1–1.5, correct order); `BIO12-CH03` → "REPRODUCTIVE HEALTH" (5 headings, 3.1–3.5).
- **2026-10-10 — Two real check-script false-positive patterns found on real Chapter 3 data, not yet fixed, will keep producing `flagged` (not `blocked`) pages at scale.** (a) `A2_TEXT_MISMATCH`'s ≥99%-character-match bar compares paragraph-only block text against the *whole* page's text layer, which structurally fails on any page mixing paragraph blocks with headings/boxes/lists (the non-paragraph content is real page text the ≥99% bar never credits). (b) The header/footer-removal check can false-flag when a real page number (e.g. "50") also legitimately appears inside exercise-question prose (e.g. "the past 50 years") — the check doesn't distinguish the two occurrences. Both are check-script precision issues, not agent or data errors; low priority since the fallback chain already handles them correctly (flagged for review, not blocked), but will inflate the flagged-page rate at full scale if not tightened.
- **2026-10-10 — Second real chapter (Biology 12 latest, Chapter 3 "Reproductive Health") read end-to-end by genuine subagent calls, proving the multi-chapter fix.** 10 pages: 3 `pass`, 7 `flagged` (the two false-positive patterns above, plus one genuine agent fidelity defect — a block missing the required `n` field, correctly caught by schema validation and kept flagged rather than hand-edited). All 8 of chapter 3's A3 sections resolved `pass`. Following this, `A2 --items BIO12L --check` was run again and surfaced the full remaining chapter list for the book (chapters 2, 4–13) ready to list for real processing — confirming the fix works at full-book scale (13 chapters), not just the 2 tested. Real subagent dispatch across the remaining ~200+ pages has not been done yet — scope checkpoint pending with the user before committing to that volume of real calls.
- **2026-10-10 — `docs/MASTER_PLAN.md` created.** Consolidates the full data inventory, the complete v0.2 taxonomy, per-stage build status, PCB-specific handling rules, the prioritized risk register, and the roadmap into one reference document. Read that file for the current overall picture; this file (`OPEN_QUESTIONS.md`) stays the append-only log of individual decisions as they're made.
- **2026-10-10 — Master Plan risk #1 (Stage B answer-overlay contamination) substantially resolved for the text-layer path, confirmed by direct testing, not assumption.** Built `scripts/lib/scrape_sanitize.py`. Investigated the real overlay structure directly (viewed a real rendered page): every question is visually self-contained, with the site's "Hide solution / CORRECT ANSWER: X / <explanation>" block sitting in its own region strictly *after* that question's 4 options and *before* the next question's number — never interleaved character-by-character with real content. The text layer preserves this same clean boundary verbatim, making it reliably regex-matchable (`strip_overlay_text`). Validated against 4 real papers spanning 2017/2020/2023/2025: overlay-blocks-stripped matched each paper's real question count almost exactly (180/180, 180/180, 179/180), and all 4 papers had ~100% real text-layer coverage (0–4 pages of 94–171 lacking one). **Decision: the sanitized text layer should be B1–B6's primary source whenever it exists** — this removes the contamination for the large majority of real content without needing to touch page images at all.
  - **Honest limitation found, not glossed over:** also built and tested `render_sanitized_crop` (grayscale image rendering, to neutralize the correct-option color-highlight for the rare case with no text layer). Confirmed by actually viewing the rendered output that **grayscale alone is insufficient** — the green background color is gone, but the checkmark *icon* marking the correct option is a distinct shape, not a color, and remains clearly visible after grayscale conversion. A vision agent could still identify the answer from the icon alone. This fallback path (used only when no text layer exists for a question) carries a known, unresolved residual risk — not claimed as fixed. A real fix (icon-region detection + masking) was not attempted, out of scope for this pass.
  - **Still fully open, unaffected by this fix:** the missing-image problem (figure/structure/graph-dependent questions have no real image content in these scraped files at all, text sanitization doesn't help) remains Master Plan risk #1's second half, unresolved.
  - Not yet wired into an actual Stage B script, since Stage B scripts don't exist yet (only the 8 agent prompts were updated today) — this is the library-level fix ready for Stage B to use when it's built.
- **2026-10-11 — M2: `config/steps.yaml` completed for B1-B8 and `schemas/B1.json`-`schemas/B8.json` written**, building directly from Section 10's step text plus the 8 just-refined `.claude/agents/b*.md` files (authoritative over SPEC.md's own worked examples where the two differ, per instruction). All 8 schemas are valid draft-07 (`Draft7Validator.check_schema()`) and each validates its own agent file's worked JSON example plus the universal `{"error": "..."}` branch. Judgment calls and real discrepancies found, logged in full in `config/steps.yaml`'s own per-step comments (not repeated in full here):
  - **B1 `trust` enum, three-way disagreement.** Section 6.2 (`register/papers.csv` data contract, line 415) says `trust (official|memory_based)` — two values. `b1-paper-registrar.md`'s own "Allowed values" (today's refinement) lists three: `official, memory_based, unsure`, and its own worked example actually sets `trust: "unsure"` for the real unconfirmed-booklet-code case. `config/allowed_values.yaml` has no `trust` key at all. Followed the agent file (3 values) in `schemas/B1.json` since it's the only one of the three that covers the real GAJAHA-M1 case; Section 6.2 and `allowed_values.yaml` need a follow-up fix, out of this task's scope.
  - **B3 `option_images` field, present in Section 10/B3's "Agent output" line, absent from `b3-question-reader.md`'s actual output example and Input section.** Read as: B2's SCRIPT half already crops image options to `papers/questions/<PAPER>/<QNO>_opt<k>.png` before B3 runs, so the merged record's `option_images` is SCRIPT-populated from those paths, not echoed by the B3 agent. `schemas/B3.json` matches the agent file (no `option_images` key); flagged for human confirmation before Stage B scripts are built.
  - **B3 `negative_words_seen`, 5 words in the agent file vs. 6 expected by Section 13/E2's negative-word guard** (which checks for NOT, EXCEPT, INCORRECT, FALSE, WRONG, MISMATCH — B3's own allowed set omits MISMATCH). `schemas/B3.json` follows the agent file (5 words); real gap for whoever builds E2.
  - **B7, no `note` field.** Every other B-step agent file's worked example includes `note`; `b7-chem-branch-sorter.md`'s own example (`{"branch", "confidence", "why"}`) does not. `schemas/B7.json` matches the actual example (no `note`, `additionalProperties: false`) rather than assuming uniformity.
  - **B8, no retry/adjudicator chain named in Section 10/B8**, unlike its closest analogue D4 (also quote-verifies against NCERT passages), which explicitly chains "quote not found → retry → still not found → drop it." Chose not to invent a chain the spec text doesn't state for B8 — `fallback: []` in `config/steps.yaml`, every output simply flagged `B8_CORRECTION` (high) regardless of confidence, per the step's own "What continues" text.
  - **The task brief that commissioned this work cited a flag code `B5_KEY_ROW_MISMATCH` as a worked example — no such code exists in SPEC.md.** The real Section 16 catalogue (and Section 10/B5) define `B5_KEY_ROW_MISSING` (blocker, no key row) and `B5_KEY_ADJUDICATED` (high, copy vs. text-layer disagreement). Used the real spec codes, noted the brief's inaccuracy directly in `config/steps.yaml`'s B5 entry rather than silently substituting one for the other.
  - **B4's output shape for the SCRIPT (text-layer) branch is not specified anywhere in SPEC.md as its own JSON contract** — only the AGENT branch (`b4-second-reader.md`, used solely when no text layer exists) has a worked example. `schemas/B4.json` models both as alternatives, with the script branch's shape *inferred* (B3-equivalent fields minus `lines`) and explicitly marked as inferred, not spec-quoted, in the schema's own description.
  - **Real-data residual risk, not a spec contradiction but worth preserving:** per `scripts/lib/scrape_sanitize.py`, the correct-option checkmark is drawn directly on the option itself (inside the 4-option row), not only in the separate post-options "CORRECT ANSWER" card; grayscale conversion alone does not neutralize it. B6 (no retry, by design) is the step most exposed to this if a raw `figure_image` crop ever leaked into its one image input — flagged as a critical, unresolved note in `config/steps.yaml`'s B6 entry for whoever builds the Stage B runner plugin next, since it hasn't been tested end-to-end (Stage B scripts don't exist yet).
- **2026-10-11 — Stage B runner plugins (B1–B5) built and independently re-verified against real `neet_2023_code-E1.pdf` data — confirmed, not just trusted from the building agent's own report.** Re-ran `grep -il "correct answer\|hide solution" papers/records/Q-00000{1,2,3}.json` directly — zero matches, confirming the sanitization fix genuinely protects a real end-to-end subagent call, not just the standalone text-processing test from earlier. `register/papers.csv` has 2 real rows (paper + key, both `NEET-2023-MAIN-E1`). All of B1–B5 return `DONE` when scoped with `--items` to the actually-tested paper/questions.
  - **Non-bug, but a real scoping lesson repeated from A2's earlier one:** running `run_step.py B1 --check` *unscoped* appeared to hang (20s+ timeout). Root cause: `cmd_check` in `scripts/run_step.py` deliberately falls through to `list_items()` when `check()` finds nothing to retry (so "DONE" means truly done, not just "no retries pending" — a defensible reading of spec 5.1). For B1, `list_items()` iterates the **full manifest** (211 paper/key rows across the whole project, not just the tested one), rendering 2 real PDF pages per untested candidate. This is working as designed, not a bug — but it means any `--list`/`--check` call on a B-stage step without `--items` scoping will trigger real rendering across the *entire* remaining manifest, same as A1/A2 needed scoping or backgrounding at smaller scale. Confirmed fix is procedural, not code: always scope B-stage runner commands with `--items` during incremental/test work; only run unscoped when deliberately processing the full candidate space (and expect it to take a while / background it, same as A1 did for 9 books).
  - Side effect of the above, harmless but worth knowing: the unscoped test run did render and stage real work-input files (2 pages each) for 116 of the 211 manifest candidates before being interrupted — these sit in `steps/B1/work/` as legitimate pre-staged (not dispatched, not resolved) work, safe to either use later when B1 scales up or ignore.
- **2026-10-11 — Stage B runner plugins (B6–B8) built and independently re-verified against real data — confirmed, not just trusted from the building agent's own report.** Re-verification performed directly (not re-trusting the build agent's report): `grep -il "correct answer\|hide solution\|\.png\|figure_image" steps/B6/work/*.input.json` across all 5 real work-input files returns zero matches; `Q-000001.runA.input.json` inspected directly contains only `stem_en`/`statements`/`list_i`/`list_ii`/`options_en` — no `figure_image` key at all, confirming B6 never receives a raw image path even as an unused field. `papers/records/Q-00000{1..5}.json` read directly: official/b6_answer/agrees/status/subject/branch all match the build agent's reported table exactly (4/4 answerable real questions agree with the official key: Q1 2=2, Q3 3=3, Q5 3=3 Chemistry/organic, Q4 dropped with b6_answer=1 and no official value to compare). `flags/flags.jsonl` contains a real `FL-000073` / `B6_IMAGE_INPUT_UNSAFE` (high) row for Q-000002, correctly explaining the figure-image skip. `steps/B8/out/Q-000004.runA.json` read directly: real, honest content — `supporting_quote: null` because none of the 15 retrieved passages (all Biology, since Stage A hasn't indexed Physics yet) are relevant to this rotational-motion question, `issue_reason: error_in_question`, proposed correction (moment-of-inertia 3:5 reading) matches B6's independent blind-solve finding on the same question. `run_step.py B6/B7/B8 --check --items <the 5 real QIDs>` all return `DONE`. `pytest tests/` passes (2 passed). Q-000005 confirmed as a genuine new real Chemistry question (`source_file` points at the real `neet_2023_code-E1.pdf`, stem matches real organic-chemistry content), not fabricated.
  - **B6 policy decision: any `has_figure: true` question is treated as categorically image-input-unsafe and skipped (official answer used downstream, unchecked by B6), rather than attempting to distinguish "figure is essential" from "figure is decorative."** Conservative by design, confirmed correct on the one real case tested (Q-000002, a circuit-diagram capacitance question whose option values genuinely aren't recoverable from text alone) — but this also means any question whose figure turns out to be non-essential (e.g. a purely illustrative diagram) will be skipped too, forgoing a real B6 cross-check it could otherwise have provided. Worth revisiting once more real `has_figure=true` data exists to see how often the figure is actually load-bearing.
  - **B7 subject/branch detection substitutes a real per-question signal — the scrape site's trailing NCERT chapter-tag text when present, falling back to a stem/options keyword scan when absent — for Section 10/B7's stated "paper's section headings" input**, since B2/B3 don't currently capture section headings as distinct data. The keyword-fallback path was added as a real bug fix after Q-000005 (the first real Chemistry test case) had no trailing tag at all and was silently misclassified by the tag-only version; re-verified all 5 real records classify correctly after the fix (4 Physics, 1 Chemistry/organic). Not yet exercised against real Biology data — a genuinely untested branch (`branch: "unsure"` is the defined fallback for Biology, never hit by a real question yet).
  - **B8's `latest_passages` can currently only ever return Biology content**, since Stage A has only indexed `BIO12L` so far — confirmed concretely by the real Q-000004 run, where all 15 retrieved passages were Biology and the agent correctly set `supporting_quote: null` rather than force a match. Not a new gap (already in the Master Plan's Stage A scope), but now demonstrated end-to-end rather than theoretical: until Physics/Chemistry chapters are indexed, every real B8 (and any future D-stage NCERT-grounding) call on a non-Biology question is structurally unable to cite supporting NCERT text.
  - **`config/steps.yaml` names `search_index.keyword_rank`; the real function in `scripts/lib/search_index.py` is `search_index.rank`** — used as actually named in the plugin code, consistent with the project's established practice of following real code over a stale config comment rather than silently renaming the function to match.
  - **Minor field-semantics wrinkle, not a bug: `b6_agrees_with_key` reads `True` for a dropped question (Q-000004) even though no real comparison was possible** (no official answer exists to compare against). `check_message` disambiguates this in text ("ok (dropped question, no official answer to compare against)"), but a future reader of the boolean field alone, out of context, could misread it as a genuine agreement.
  - Real bug found and fixed during the build: `_b7_detect_subject`'s first version relied solely on the scrape site's trailing NCERT chapter-tag (present on Q-000001–004); Q-000005 (the first real Chemistry test case) has no such tag, so the heuristic mis-scanned option 4's own text as the tag and found no subject. Fixed with a stem+options keyword-scan fallback; re-verified all 5 real records now classify correctly.
- **2026-10-11 — Stage C1 (Merge booklet codes) built and independently re-verified against real data — confirmed, not just trusted from the building agent's own report.** A real second booklet code (E2) was registered for the same `NEET-2023-MAIN` sitting via a genuine `b1-paper-registrar` dispatch (`register/papers.csv` now has 2 real paper rows for 2023 MAIN, E1 and E2, both `pass`), then 9 real E2 questions (pages 8/12/14/16/39, targeted by a real text-layer keyword search rather than scanning the whole paper) were run through real B2→B3→B4→B5 dispatches. Re-verified directly: `papers/records/Q-00000{1..5}.json` each now carry `paper_codes: ["E1:n","E2:m"]`, a real `option_map`, and `merged_from` pointing at the absorbed E2 record; each absorbed record (`Q-000006`, `Q-000008`, `Q-000010`, `Q-000012`, `Q-000014`) carries `merged_into` back to its canonical E1 twin — nothing deleted, both sides inspectable. `steps/C1/out/*.runA.json` (5 real files) all contain a genuine `c1-booklet-matcher` agent verdict of `exact_same` with a real bijective option_map. `run_step.py C1 --check` (scoped) returns `DONE`; `pytest tests/` passes (2 passed).
  - **Real finding, not assumed: the SCRIPT shortlister (reusing `pair_passages.py`'s Jaccard-on-word-trigrams + Hungarian assignment, built originally for A6) found all 5 genuine E1↔E2 duplicate pairs with zero manual hinting**, at similarities 1.0, 1.0, 0.8182, 0.8049, 0.72 — comfortably above the chosen `SHORTLIST_THRESHOLD = 0.3`. Confirms NEET booklet codes really do scramble question order while preserving content verbatim (scrape artifacts aside), as the spec assumed.
  - **Honest gap: no real `not_exact` case arose.** All 5 real shortlisted pairs came back `exact_same` on the first compare, so the `not_exact → reread B3/B4 → compare again → still not_exact → adjudicator` chain, `C1_KEY_INCONSISTENT`, and `C1_UNMATCHED` were never exercised against real data — only proven via isolated synthetic dry-runs (scratch scripts, not part of the repo) mirroring the existing fixture-isolation pattern. This machinery is code-verified but not yet real-data-verified; worth watching for a genuine near-miss once C1 runs at larger scale.
  - **Judgment call: merge shape.** Canonical record = lexicographically-lower Q-ID (keeps the one with the fuller B1–B8 history already attached). Canonical gains `paper_codes` (list, code:qno per side), `option_map: {absorbed_qid: {opt_num: opt_num}}`, `merged_from: [absorbed_qid, ...]`. The absorbed record is never deleted or edited beyond adding `merged_into: <canonical_qid>` — downstream consumers must treat any record with `merged_into` set as non-canonical and skip it, a new convention worth carrying into Stage D/E/F's own record-walking helpers.
  - **Judgment call: C1's `needs: B8` readiness gate uses the same B5-join signal (`official_answer`/`status` present) B6/B7/B8 already use** — no cleaner "has B8 run" signal exists yet in this build; acceptable since B8 only activates for genuinely dropped/bonus/multiple-accepted questions anyway.
  - **Judgment call: an adjudicator-confirmed merge (the synthetic-dry-run-only path) uses an identity-by-option-number option_map**, since the agent's own bijective map only ever comes from a real `exact_same` verdict, never from two `not_exact` verdicts plus an adjudicator call.
  - **Config fix: `config/steps.yaml`'s C1 entry was written speculatively before C1 existed** (plain `agent: "c1-booklet-matcher"`, no real fallback chain) and has been corrected to `agent: "script | c1-booklet-matcher"` (matching the existing A5/B4/B7 two-phase hybrid convention so `step_kind()` classifies it correctly) with the real `fallback: [reread, adjudicator]` and flag map filled in, documented inline.
  - Minor, harmless: a stale `steps/C1/status/SKIP:NEET|2023|MAIN.json` file persists from the earlier (correct, at-the-time) single-code `skipped` result — never consulted again now that real pairs exist, not a bug, just unreclaimed state.
- **2026-10-11 — A4 (subtopic writer) and A5 (passage linker) run for real for the first time, independently re-verified.** Both had ready prompts/runners but had never actually been dispatched (confirmed before this: `ncert/subtopics/` and `ncert/links/` both empty, `steps/A4/status/` and `steps/A5/status/` both empty). Closes the Master Plan's long-standing roadmap item #1. Real dispatch: 4 real `a4-subtopic-writer` calls (2 chapters × 2 runs) on the 2 already-indexed Biology chapters (`BIO12-CH01` "Sexual Reproduction in Flowering Plants", `BIO12-CH03` "Reproductive Health"), real genuine disagreement actually arose and was actually resolved — `BIO12-CH01`'s status reads `"adjudicator combined both runs"`, `BIO12-CH03`'s reads `"adjudicator unsure -- used safe-default union merge"` (the real `safe_default: "adjudicator-merged list"` path from `config/steps.yaml`, genuinely exercised, not a stub). `ncert/subtopics/BIO12-CH01.json`/`BIO12-CH03.json` read directly: real, heading-grounded subtopic lists (e.g. `BIO12-CH01-ST01` "Flower – structure and significance", `from_heading: "1.1"`, 7 real linked passages). Then A5 ran for real on top of this, producing `ncert/links/BIO12L.jsonl` (real passage→subtopic links, `method: "heading"` for the script-decided majority). `run_step.py A4/A5 --check` (scoped) both return `DONE`.
  - **Real, necessary bug fix: `A4Plugin.check()` previously never implemented the real 2-run-merge/adjudicator logic at all** — it only ever raised a `A4_SUBTOPICS_DRAFT` flag and stopped, because no real data had ever reached that code path before. Built for real: subtopic matching between runA/runB (heading-normalized Jaccard similarity, mirroring A6/C1's own trigram-Jaccard precedent), direct merge for agreeing pairs, real `x-adjudicator` dispatch (following `C1Plugin`'s adjudicator-dispatch shape, the closest existing precedent in the file) for disagreeing/unmatched subtopics, and a documented safe-default union-merge when the adjudicator itself comes back unsure. Also fixed `A4Plugin.list_reason()`'s stale/wrong message (it said "none found yet" even when real chapter data existed).
  - **Real Biology question added to the bank, closing the "zero Biology content" gap**: `Q-000015`, a genuine statement-based NEET question on the female reproductive cycle (`paper_codes: ["E1:172"]`), pulled for real through B1→B6. B6 (blind solver) independently derived option 4 (`A, C and D only`), **matching the real official answer**, correctly reasoning that statement B is false because the first menstrual cycle is menarche, not menopause — a genuine demonstration of B6 catching a real factual-confusion trap, not just an easy agreement. B7 completed afterward (subject correctly tagged `Biology`; `branch: "unsure"`, the documented safe default for Biology since branch-conditioning is Chemistry-specific — see the 2026-10-11 B6-B8 entry above). B8 does not apply (`status: "normal"`, not dropped/bonus).
  - **Minor pre-existing data wrinkle, newly observed on real Biology data, not yet fixed**: `Q-000015.b4_script_options["4"]` reads `"A, C and D only\nHuman Reproduction"` — the scrape site's trailing NCERT chapter-tag leaked into B4's SCRIPT-branch option parsing for the last option, the same leaked-tag pattern already seen and fixed for B7's subject-detection (2026-10-11 entry above) but not yet fixed at its source in B4. Harmless here only because the actually-used `options_en` field (B3-sourced) is clean and every downstream step (B5's `official_answer`, B6's answer) compares against option *numbers*, never against `b4_script_options`' raw text — but `b4_script_options` is itself slightly wrong data sitting in the record, worth a real fix when B4 is next touched.
  - **Process note: this build was interrupted mid-task by a background-agent API error** (not a logic bug — "response stopped arriving"), after Goal 1 (A4/A5) and most of Goal 2 (Q-000015 through B1-B6) had already completed and been written to real files. Verified directly that nothing was left corrupt or half-written; B7 (the one remaining real step) was completed directly afterward. Consistent with this project's standing practice: an interrupted background task's real, already-written output is trustworthy and reusable as long as it's independently re-verified before building on it, same precedent as the earlier B6-B8 stall.
- **2026-10-12 — Stage D1→D4 built and independently re-verified against real data.** Real end-to-end dispatch on `Q-000015` (7 real subagent calls: `d1-chapter-picker` ×2 + adjudicator, `d2-subtopic-picker` ×2 + adjudicator, one real D2 retry). Directly re-verified: `papers/records/Q-000015.json`'s `d1_chapter_ids`/`d2_subtopic_ids` fields, `steps/D1/status/Q-000015.json` and `steps/D2/status/Q-000015.json` (`"adjudicator unsure -- run A invalid too; keyword-rank guess"`), real `D1_GUESS`/`D2_GUESS` (high) and `D3_NO_PASSAGES` (blocker) flags in `flags/flags.jsonl`.
  - **Real, substantive finding, not a bug: both real D1 runs AND the real adjudicator independently said `unsure` for Q-000015.** Neither `BIO12-CH01` ("Sexual Reproduction in Flowering Plants") nor `BIO12-CH03` ("Reproductive Health") actually covers this question's real content (oestrus cycle / menarche / menopause) — that content genuinely belongs to NCERT's separate "Human Reproduction" chapter, which Stage A has never indexed. The real fallback chain (adjudicator unsure → `search_index.rank` keyword-guess → `D1_GUESS`) worked exactly as spec'd rather than forcing a false-confidence pick, landing on `BIO12-CH03` (the closer of the two wrong options) with `confidence: low` — the system correctly reported its own uncertainty instead of masking it. Confirms this project's recurring pattern (same shape as B7's Biology-branch gap, B8's Biology-only passage pool): **the single Biology question in the bank was picked for being topically adjacent to the 2 indexed chapters, not for actually being inside them** — a real illustration of why only 2/13 chapters being indexed is a genuine, now-doubly-demonstrated scope gap, not just a theoretical one.
  - **Real, substantive finding: D3 found zero linked passages for the guessed subtopic (`BIO12-CH03-ST15`) and correctly ran its full retry-then-block state machine.** Directly verified: `ncert/subtopics/BIO12-CH03.json` has 17 real subtopics (ST01-ST17) but `ncert/links/BIO12L.jsonl` only ever linked ST01-ST13 to real passages (confirmed by direct read — A5's real run, 2026-10-11 entry above, evidently didn't cover every subtopic's passages, or CH03's real NCERT content doesn't have enough distinct passages to cover all 17 drafted subtopics 1:1). D3's retry (a second real `d2-subtopic-picker` dispatch with the "previous subtopics had no passages" note) also came back `unsure`, so D3 correctly blocked with `D3_NO_PASSAGES` — real, honest exercise of the full spec'd fallback chain, not a shortcut. D4 was consequently never dispatched for real (gated by D3's blocked status) — its real code (schema, `scripts/checks/D4.py`'s quote-verification and derivation-cross-check logic) was instead exercised only via hand-built fixtures against real NCERT passage text (`BIO12L-CH03-P14`), honestly labeled as fixture-only, same precedent as A8's existing fixture-only status.
  - **The 5 real Physics/Chemistry questions (`Q-000001`–`Q-000005`) all correctly block at D1 with a new `D1_NO_CHAPTERS` (blocker) code**, confirmed directly: all 5 `steps/D1/status/*.json` read `"blocked" / "no candidate chapters for this subject"`. Honest, structural, expected — Stage A has indexed zero Physics/Chemistry chapters; no fabricated chapter data was used to force a pass.
  - **Real bug #1, found and fixed: `schemas/D1.json`/`D2.json` originally had no optional `note` field**, so the very first real D1 run (Q-000015, run A) — which legitimately used `note` per Universal Rule 7 ("if the input looks wrong, say so in note") to flag that neither candidate chapter really covers the content — was rejected by schema validation and silently fell through to the wrong fallback path. Fixed by adding `note` as optional in both schemas (confirmed present under each schema's `oneOf` success branch, not top-level — a flat `properties` check on the schema file will misleadingly read empty; check inside `oneOf[0].properties`).
  - **Real bug #2, found and fixed before touching real data: `scripts/checks/D4.py`'s derivation-mismatch parser (`_first_number`, now renamed `_final_number`) grabbed the FIRST number in a derivation step** (e.g. misread `"x = 2*3 = 6"` as `2`, not the intended final value `6`) instead of the value after the last `=`. Caught by the build's own fixture test, never by real data — no real numerical D4 case exists in the corpus yet to have exercised this live. `_final_number` now parses after the last `=` in the string.
  - **Judgment calls:** (1) D1/D2's adjudicator dispatch mirrors A4's real pattern (2026-10-11 entry above), simplified for a whole-list choice rather than a partial merge; "runs agree" is set equality, `unsure` never counts as agreement with anything. (2) D1 scopes candidate chapters by subject only (glob `ncert/chapters/<PREFIX>*.json`), never by branch — the chapters file carries no branch field, and a record's own `branch` is frequently itself `unsure` (true for Q-000015). (3) D3 writes to the literal spec-named path `steps/D3/out/<QID>.json` (no run_label); its D2-retry dispatch is owned by `D3Plugin` itself (not `fetch_passages.py`), and the re-fetch after a retry calls `fetch_passages.fetch_for_item()` in-process rather than a second `--auto` pass. (4) D4's `_post_assembly` always independently re-verifies every quote (never trusts the agent's own claim) and raises `D4_PARTLY`/`D4_NO_SUPPORT`/`D4_BEYOND_NCERT` based on the final verified value, separate from `checks/D4.py`'s pass/fail — a legitimate `partly` verdict must never trigger a retry on its own. (5) D3's 15-passage ranking/truncation and D1/D2's "one run invalid, one valid" degrade-gracefully branch are fixture-verified only — real data for Q-000015 topped out at 13 linked passages (under the 15 cap) and both real D1/D2 runs always passed schema validation (never hit the "one run invalid" branch for real).
- **2026-10-12 — `scripts/export_snapshot.py` built: an inspectable CSV snapshot of all pipeline state, deliberately NOT the gated release export.** Built in response to the owner asking how to download/inspect per-step data. **Judgment call on why this is a separate script, not `export_tables.py`:** spec Section 14/F5 and `CLAUDE.md` reserve `export_tables.py` → `data/` for the *gated release* export (only for a chapter with an empty review queue, approved subtopic list/change-log rows, and a real sign-off row in `review/releases.csv`) — releasing implies a person checked it. This snapshot makes no such claim, so it writes to `exports/<date>/` and never near `data/`, every row carries its real `status`/open-flag columns so nothing can be mistaken for approved output, and a `README.txt` states plainly that it is work-in-progress. It only reads the pipeline — never mutates a record or closes a flag. Tables: `questions.csv` (canonical questions only, so the row count is the real unique count), `merged_away.csv` (the other half of each C1 merge, so no extracted question silently vanishes), `passages.csv`, `subtopics.csv`, `chapters.csv`, `books.csv`, `papers.csv`, `flags.csv` (worst-severity first), `run_log.csv`, `coverage.csv` (per-step pass/flagged/blocked counts from real status files — the honest "how much is done" table). First real run: 10 questions, 5 merged-away, 105 passages, 35 subtopics, 2 chapters, 77 flags, 338 run-log rows, 20 steps with status.
  - **Real defect surfaced immediately by the snapshot, confirming the A4-over-generation hypothesis concretely: 4 of 35 drafted subtopics have ZERO passages linked by A5** — `BIO12-CH03-ST14` (Natural contraceptive methods), `ST15` (Assisted reproductive technology – IVF and ET), `ST16` (Population explosion and need for birth control), `ST17` (Transmission and prevention of STIs). This is exactly why D3 blocked for `Q-000015`: D1/D2's keyword-rank fallback routed it to `ST15`, one of the four empty shells, so no evidence could possibly be fetched. The `subtopics.csv` column pair `passages_listed_by_a4` vs `passages_linked_by_a5` was added specifically to make this class of defect visible by joining the two files — a subtopic with 0 links is a real defect, not a cosmetic gap. **Improvement needed (not yet made): A4's subtopic generation should be passage-aware**, so it cannot draft a subtopic that no real passage in the chapter can support; currently it drafts from the heading tree alone, and CH03's real passages only support 13 of the 17 headings it found.
  - **Second real defect surfaced by the snapshot, previously unnoticed: 4 questions were stranded mid-Stage-B.** `Q-000007`, `Q-000009`, `Q-000011`, `Q-000013` show `field_sources` reaching only B1/B3/B4/B5 — real `official_answer` from the real key, but no `subject`, no `b6_answer`, and no B6/B7/B8 status files at all. Root cause: the C1 build (2026-10-11 entry above) pulled 9 real E2-code questions through B1→B5 as cross-code duplicate candidates; 5 were genuinely duplicates and got merged, and these 4 turned out not to be duplicates of anything and were simply left where they stopped. **Verified this is NOT a runner tracking bug** — `run_step.py B6 --list` and `B7 --list` both correctly surface them as outstanding work, so the runner's own accounting was right and only the dispatch was never done. Being finished now. **Process lesson worth keeping: a step-scoped build task ("pull N questions through B1-B5 to test C1") can legitimately leave real items stranded part-way through a stage, and the per-question records themselves look superficially fine — only a cross-cutting view (the snapshot's `questions.csv`, where the blank `subject`/`b6_answer` columns stand out against their neighbours) made it visible.** Worth re-running the snapshot after any future partial/scoped build for exactly this reason.
- **2026-10-12 — Stage E started: `scripts/type_patterns.py` built (E1's SCRIPT half, spec 13/E1) and real-tested, surfacing one real spec gap and one real data defect.** Implements all 16 of spec 13/E1's patterns in the stated priority order, first-match-wins (that ordering is load-bearing: an Assertion-Reason question also contains two statements, and a match question also contains lists, so a different order silently reclassifies whole families of real questions). Returning `None` is a designed, non-failure outcome — spec 13/E1 says the `e1-type-tagger` AGENT runs *only* when no pattern decides, so `None` is precisely the signal to dispatch it. Self-test (`--self-test`) encodes all 4 boundary cases the spec names by question id (2026-May#25, 2015#161, 2014#27, 2015#130) plus 7 more; all 11 pass. Run `--all` against the real 10 canonical questions: 9 classified by pattern, 1 correctly handed to the agent.
  - **Real bug in my own first implementation, found by inspecting real output rather than trusting the self-test: spec rule 9 reads "reaction arrow OR SCHEME IMAGE in the stem", and I had implemented only the text-arrow half.** Real `Q-000013` ("Identify product (A) in the following reaction: [Chemical structure of a diketone ... undergoing reduction]") carries its scheme as an *image* with no text arrow, so rule 9 couldn't see it and it fell through to rule 12, mislabelled `figure_to_read` — losing the fact that it is a reaction question at all, which would have mistagged E2/E3 downstream too. Fixed with rule 9a (figure present + a reaction/scheme/synthesis word + an X/Y/Z/product/reagent ask), placed deliberately ahead of rules 11/12 since those also match a figure. Locked in as a regression case built from the real record.
  - **REAL GAP IN SPEC 13/E1's PATTERN LIST, needs the owner's decision — not something a script should decide.** When the four OPTIONS are each a chemical reaction (real `Q-000005`: "Which of the following reactions will NOT give primary amine as the product?", whose 4 options are each a distinct reagent/arrow transformation), **no spec pattern applies**: rule 9 is scoped to the stem, rule 10 covers option *images* only, and rule 15 covers prose statements. My first implementation's rule-15 heuristic wrongly claimed `statement_options` for it — four LaTeX reaction strings each read as a long "statement". A reaction equation is not a statement to judge. Fixed two ways: (a) rule 15 now excludes formula/chemical-notation-dominated options, (b) new rule 9b detects option-reactions and returns `None` so the agent decides. **Proposal for the owner:** taxonomy v0.2 already added `list_of_structures` to E1 for the "options are structures" case; this is its reaction analogue, and a `list_of_reactions` value would close the gap cleanly. Not added unilaterally — E1's allowed values are the owner's call, and `config/allowed_values.yaml` is unchanged pending that decision. Until then the agent handles it, which is the spec-correct fallback.
  - **Real data defect found while reading real option text, not yet fixed: B3 lost mathematical symbols from a real stem.** `Q-000007`'s stem reads `"If [unreadable glyph]_S E[unreadable glyph] [unreadable glyph] dS[unreadable glyph] = 0 over a surface, then :"` — the real question is Gauss's law (∮_S **E** · d**S** = 0), and the surface-integral, vector-dot and bold-vector glyphs all failed extraction, with the agent honestly marking them `[unreadable glyph]` rather than inventing symbols (correct behaviour per its own rules). **Impact is real and downstream:** D4 must quote NCERT word-for-word and E3/E4 must judge what the question tests — both are degraded when the stem's central equation is missing. The question is still answerable from its options (all four are prose), which is why B6 was never blocked on it. **Fix needed (not yet made):** B3/B4 should either render the unreadable span as an image crop (the A2S `needs_special` precedent already in this codebase handles exactly this for NCERT equations) or route such questions through a LaTeX-capable reading path; a `B3_UNREADABLE_GLYPH` flag would at least make the defect visible instead of silent. Currently no flag is raised at all, so this only came to light by eye.
- **2026-10-12 — MAJOR SOURCE FINDING, prompted by the owner challenging the "figures are unfixable" claim: the figures are not recoverable across booklet SETS, but a second, far better paper source has been sitting in `inputs/` unused the whole time.** The owner's hypothesis was that since a sitting has many booklet codes (2023 alone has 24: E1-E6, F1-F6, G1-G6, H1-H6) and C1 already proves the same question appears across them, a figure missing from one set might survive in another. **Tested directly and the hypothesis is false for these files, for a reason worth recording: all 24 real 2023 scrape PDFs contain ZERO embedded raster images** (`page.get_images()` returns 0 on every page of every set — verified across all 24). They do contain ~3,900 vector paths each, but rendering real `Q-000002`'s page (E1 p3) and looking at it confirms those paths are the scrape site's card borders and rounded option boxes, not figures: the stem says "the equivalent capacitance of the system shown in the following circuit" and **there is no circuit on the page at all**. The site's own worked solution even recites the values ("1/6 + 1/3 + 1/2") that only exist in the absent diagram. Cross-set recovery cannot work when every set is missing the figure identically.
  - **But the real answer is better than the hypothesis.** `inputs/manifest.csv` holds papers from **two distinct sources**, and only one has ever been used: 166 files from `all_neet_sets_and_ans_key/` (the per-booklet-code coaching scrapes, which B1-B8 was built and proven against), and **15 year-wise files from `NEET_PYQ/Paper/` (2017-2025 + AIPMT 2010-2015) that are properly typeset published books, not web scrapes**. Verified by rendering and reading real pages from both `2023.pdf` and `2021.pdf`:
    - **Figures are present and clean.** `2023.pdf` p20 carries the *exact* `Q-000002` capacitance question **with its circuit diagram** (3μF/3μF/3μF across terminals A-B), plus real circuit diagrams for two more questions on the same page. `2021.pdf` p15 renders full **chemical structure diagrams as options** and reaction schemes with reagents above the arrow — precisely the `structure_options`/`reaction_scheme`/`graph_options` shapes the scrapes make impossible, and the real reason E1's rule 10 has never been able to fire.
    - **Mathematics renders correctly.** `2023.pdf` p20 q17 is the same question as real `Q-000007`, whose scraped stem reads `"If [unreadable glyph]_S E[unreadable glyph] [unreadable glyph] dS[unreadable glyph] = 0"` — here it is the correct `∮ E⃗ · dS⃗ = 0`. The B3 unreadable-glyph defect logged earlier today is a *source* defect, not an agent defect, and this source fixes it.
    - **No inline answer overlay.** Grep hits for "correct answer" in `2023.pdf` are ordinary NEET stem phrasing ("choose the correct answer from the options given below"), not a leaked key; "Hide solution" appears zero times. Real answers live in a **separate solutions section on different pages**, which is structurally ideal: question pages 1-11 (Biology 1-100), 19-23 (Physics 1-50), 29-34 (Chemistry 1-50); solution pages 12-18, 24-28, 35-38. **B1-B6 can read only the question page ranges and provably never encounter an answer** — strictly safer than the current text-stripping defence, since there is nothing to strip.
    - **`2023.pdf` is complete**: 100 Biology + 50 Physics + 50 Chemistry = 200 questions, matching NEET 2023's real structure exactly. Not a selection.
    - Bonus: the book is organised **by chapter and topic**, with the real NCERT chapter name printed as a heading above each question ("Electrostatic Potential and Capacitance", "Mechanical Properties of Solid"). That is an independent, publisher-asserted chapter label — a genuine cross-check against D1's own chapter pick, and a far better signal than the scrape's trailing topic-tag that B7's subject detection currently leans on.
  - **Honest caveats, not glossed over:** (a) this is still a third-party publication, not an official NTA scan, so `trust` stays `unsure`, not `official` — the official answer keys remain the answer authority; (b) question numbering restarts per subject (Physics 1-50, Chemistry 1-50) and does **not** match official booklet numbering, so joining to the official key by qno needs a per-subject offset, and C1's cross-code merge logic does not apply to it at all (one book per year, no booklet codes); (c) the solutions sections contain third-party worked explanations — **coaching material under spec Section 20 #4**, which must never reach B6 or D7, so the page-range split must be enforced in code, not left to chance; (d) only `2023.pdf` is the "Chapter & Topicwise" title — the others are different books (`2021.pdf` is "NEET 34 Years") whose internal structure must each be verified before use rather than assumed; (e) `2017.pdf` has only 80 vector paths across 23 pages, far below its siblings, so it may genuinely lack figures and needs checking individually.
  - **Recommended change to the pipeline's source strategy (needs the owner's decision, not made unilaterally — it affects every B-stage record already built):** treat `NEET_PYQ/Paper/` as the **primary** extraction source for B1-B6, and keep `all_neet_sets_and_ans_key/` for what it is uniquely good at — booklet-code variants, which is exactly what C1 needs. The two are complementary rather than competing. This would resolve the Master Plan's risk #1 second half (missing figures) and the B3 unreadable-glyph defect in one move, and would let B6 stop refusing every `has_figure` question. Nothing has been re-extracted yet; the 10 existing questions remain scrape-sourced.
- **2026-10-12 — MAJOR FINDING, owner-prompted: the missing figures exist as live Mathpix image URLs inside the 22 legacy sheets, covering every year including the three with no other source.** The owner spotted a `cdn.mathpix.com/snip/images/...` URL and asked whether the sheets could be used for figures and LaTeX. Verified directly: **all 22 legacy sheets (`inputs/legacy_sheets/*.xlsx`, years 2010–2026) contain markdown-embedded Mathpix figure URLs — 450 URLs across 396 of 3,920 question rows (10.1%)**, plus **1,988 rows (51%) carrying real LaTeX** (`$4$ kg`, `\frac`, `\times`). Crucially the coverage includes the exact years with no figure source anywhere else: **2016 (27 figures across Phase I+II), 2019 (13), 2020 (8)**.
  - **The URLs are live and the images are ideal.** Tested with real HTTP requests: the owner's sample URL and two pulled from `NEET-UG_pyq_2020.xlsx` all return `HTTP 200`, `image/png`. Downloaded and viewed two: one is a clean logic-circuit diagram (two NOT gates into a NOR gate → Y) matching the real 2020 question "For the logic circuit shown, the truth table is"; the other is a labelled biology diagram (nuclear envelope/ER with labels A–D), i.e. a real `diagram_labelled` figure. **Both are isolated figure crops — no watermark, no answer marking, no site chrome** — strictly better as agent input than either the scrape page images (which carry the correct-option checkmark) or the Physics Wallah files (watermarked). This is the cleanest figure source in the entire project.
  - **Resolves what was logged this morning as "unfixable from this source".** Scrape figure recovery is impossible (162 of 166 files have zero images; only 2025's 4 sets have real ones) and cross-booklet-set recovery is impossible (all sets of a year fail identically). The `NEET_PYQ/Paper/` books fix some years but are watermarked/figure-poor for 2017–2019 and absent for 2016/2020. The legacy sheets close the remaining gap.
  - **CRITICAL RULE QUESTION, needs the owner's decision — do NOT wire this in before it is answered.** `CLAUDE.md` states: "Never pass legacy-sheet columns, coaching material or answer keys to agents that must not see them", and spec Section 12/D1 explains why — the sheets put many 2018–2019 questions in the *wrong* chapter and use coaching chapter names, which is precisely why D1 never sees them. **My reading, offered as a proposal not a decision:** that rule exists to keep a coaching *judgement* (its chapter/topic/question-type labels) out of agents that must judge independently. A figure image is not a judgement — it is the original exam's own content, reproduced. So the defensible split is: **use the sheet's `![](mathpix-url)` image ONLY, and never its `Chapter Name`/`Chapter No`/`Topic`/`Question Type`/`Answer` columns.** The sheet's `Answer` column in particular must never reach B6 (which is blind by design) and its chapter labels must never reach D1/D2. If the owner disagrees, the fallback is to use the sheets as a reviewer-only reference in Stage F, which still beats having no figure at all.
  - **Engineering caveats before any of this is relied on:** (a) **CDN dependency** — these are remote URLs on Mathpix's CDN, outside the project's control and capable of disappearing; if adopted, the images must be **downloaded and stored locally** (e.g. `papers/figures/<QID>.png`) with the URL kept only as provenance, never fetched at agent-run time; (b) **joining is not solved** — sheet rows must be matched to real bank questions, which is exactly what spec Section 13's `legacy_match.py` describes (≥0.85 similarity on word 3-grams after normalisation, same year) and **that script is not built yet**, so there is currently no verified way to say which sheet row corresponds to which `Q-xxxxxx`; a wrong join would attach the wrong diagram to a question, which is worse than no diagram; (c) 10.1% sheet coverage vs the ~6.5% figure-dependence measured on a real paper suggests the sheets may cover figures the scrape didn't even flag — needs checking per question rather than assumed; (d) the sheets' LaTeX is a *second* real asset here, potentially fixing the `[unreadable glyph]` defect (real `Q-000007`), but it comes from the same coaching-derived file and carries the same rule question.
  - **Not actioned.** Nothing downloaded into the project, no plugin changed, no record touched. This entry records the finding and the open decision.
- **2026-10-12 — Owner supplied an authoritative year→sitting→file index; it resolves the long-standing sitting ambiguity for the year-wise files and exposes 7 genuinely missing PDFs.** File: `~/Downloads/NEET PYQ 2010-2026 - Sheet1.csv` (67 rows), mapping each year to its PDF and XLSX per sitting under columns headed NEET / PRELIMINARY / AIIMS. Read and verified directly. **What it establishes:** 2010, 2011 and 2012 each have two sittings (Preliminary + Main) with distinct named files; 2016 has Phase I + Phase II; 2026 has the 03-05-2026 sitting plus a re-NEET on 21 Jun 2026; every other year (2013-2015, 2017-2025) has exactly one paper. This is better evidence than filename inference and should be treated as ground truth for the 15 `NEET_PYQ/Paper/` files and the 22 sheets, reserving text-matching for the 166 scrape files the index does not cover.
  - **Independently corroborates today's 2016 text-matching result.** Before seeing the index I resolved 2016 by matching each scrape file's question text against both phase sheets: all four (`code-A_P_W`, `B_Q_X`, `C_R_Y`, `D_S_Z`) matched Phase I at 11.5×–15.3× over Phase II. The index names Phase I and Phase II as separate papers, confirming the two-sitting structure. **Conclusion: all four 2016 scrape files are Phase I, and Phase II is absent from the scrape set** — the S0 "sitting could not be confirmed" flag for 2016 is now resolved, and what remains is a real missing input rather than an unknown.
  - **Seven PDFs named in the index are not on disk** (all 22 checked by filename across the source tree): `2012 pre.pdf`, `AIPMT(Mains)-2012.pdf`, `NEET UG 2016 (Phase I).pdf`, `NEET UG 2016 (Phase II).pdf`, `neet-2020_merged .pdf`, `NEET Exam 2026_(03-05-2026).pdf`, `NEET_UG(re-neet)21 Jun 2026 17-25.pdf`. **The matching `.xlsx` for every one of those IS present**, so the data exists while the paper does not. This also revises the earlier "2012 absent entirely" note (2026-10-10): the owner's own index names 2012 Preliminary and Main files, so 2012 is a retrieval gap, not a non-existent input.
  - **Judgement call, recorded because it is easy to get wrong in the other direction: the index must NOT be read as a statement of what exists.** It lists what the owner holds. `scripts/lib/sittings.py` declares 2019 → [MAIN, REEXAM], 2020 → [MAIN, REEXAM], 2024 → [MAIN, RETEST], and on the real history **the pipeline is correct**: NEET 2019 had an Odisha re-exam after Cyclone Fani, 2020 had an October re-exam for containment-zone candidates, and 2024 had a 23 June re-test for 1,563 candidates in the grace-marks case. Those sittings are real and their papers are genuinely missing. **Decision: do not edit `sittings.py` to drop them**, and do not let the index's silence be treated as evidence of absence — S0 should keep expecting them. A separate, narrower question for the owner is whether those limited re-tests are in scope at all, given they covered small candidate subsets; until decided, they stay required and flagged missing.
  - **Still genuinely open for 2019/2020/2024:** whether any of the *scrape* files for those years come from the re-exam rather than the main paper. The index cannot answer this (it does not cover the scrape set) and a sheet covering only the main sitting cannot prove a re-exam paper is absent — only that it is not among the files matched. Being tested by the verifier agent via the same text-matching method that worked for 2016.
- **2026-10-12 — Source verification built and run: ZERO disagreements across three independent transcriptions. The extracted question text is faithful.** `scripts/verify_sources.py` (new) cross-checks every canonical record against the year-wise book (`inputs/papers/2023.pdf`) and the legacy sheet (`NEET-UG_pyq_2023.xlsx`). Result on all 10 canonical records: matched in both sources 10/10; **question-text agreement: 9 all-agree, 1 minor-diff, 0 DISAGREE**; answer-TEXT agreement 7 agree, 1 minor-diff, 0 disagree (plus 1 dropped question with no answer and 1 not-comparable). This is the concrete answer to the owner's standing question "is the extracted data correct" — on the evidence available, yes.
  - **A genuinely better verification idea than the one I briefed, invented by the agent: a positional cross-check that uses no text similarity at all.** Sheet row number minus book question number must be constant within a subject. It came out **+1 (×7 Physics), +51 (×2 Chemistry), +101 (×1 Biology)** — consistent across all 10. This is what makes even the lowest-scoring text match safe to call correct, and it is independent of every threshold argument.
  - **Both apparent "disagreements" were false alarms from LaTeX spelling, not content**: `$-\dfrac{16Gm}{R}$` vs `$-\frac{16Gm}{R}$` (Q-000009), and `\rightarrow` with separate reagent labels vs `\xrightarrow[below]{above}` (Q-000005). The agent extended the briefed normalisation (LaTeX control-word stripping, unicode sub/superscript folding, digit↔letter boundary splitting) to stop reporting them; without that extension both read as DISAGREE. Flagged as a deliberate change to my brief.
  - **Corroborates the compare-by-TEXT-not-by-LETTER rule on real data:** Q-000001's scrape lists `2W/A` first while book and sheet list `Zero` first; official key says `2`, sheet says `C`, and both resolve to `W/A`. And Q-000004 (`status=dropped`): the legacy sheet independently leaves its Answer cell blank — two unrelated sources agreeing the question has no scorable answer.
  - **Threshold evidence, now from 20 real matches:** absolute similarity maxes at **0.717**, so spec Section 13's ≥0.85 rule would reject **100%** of correct matches. The gap distribution is sharply bimodal — one case at 2.42× and everything else ≥4.30× — so accept ≥3× / flag 2–3× / reject <2× was kept, costing exactly 1 conservative flag in 20 (Q-000013, whose options are figures, so there is almost no comparable text and a human genuinely should look).
- **2026-10-12 — MAJOR SOURCE DEFECT, independently verified: 149 of the 166 scrape files are INCOMPLETE, missing 1,094 questions in total.** Each neet.training page states its own question count on page 1; comparing that against the real paper length shows the shortfall. Worst cases: `neet_2022_code-Q4.pdf` states **148 of 200**, `neet_2019_code-P1.pdf` **148 of 180**, `neet_2019_code-Q2.pdf` 154/180, `neet_2016_code-C_R_Y.pdf` 168/180. **2023 — the year every current record comes from — is short on 23 of its 24 files** (195–198 of 200). Roughly one file per year carries a full count. This is a source-completeness gap, not an extraction error, and it caps achievable coverage from the scrapes alone.
  - **Important mitigation, and a reason the booklet-code sets matter more than previously thought:** different sets are missing *different* questions, so the UNION across a year's sets should reconstruct the full paper — which is precisely what C1's cross-code merge exists to do. This changes processing multiple sets per year from an optimisation into a requirement. Not yet verified that the union actually reaches 100% for any year; worth checking before relying on it.
- **2026-10-12 — Sitting ambiguity resolved for all remaining years by text-matching, with 2016 as a control.** 2016: 4/4 scrape files → Phase I at 12.3–13.2× (reproducing the 11.5–15.3× I measured independently earlier). **2019: 5/5 → MAIN (12.4–12.7×). 2020: 24/24 → MAIN (9.1–10.5×). 2024: 24/24 → MAIN (8.9–10.5×).** Every file within a year lands on the same sheet, so none is from a different sitting. **Proven absent:** 2016 PH2 from the scrape set (the Phase II sheet was in the comparison pool and all four files preferred Phase I by a wide margin). **NOT proven absent, correctly distinguished as `UNRESOLVED_ABSENCE`:** the 2019 Odisha re-exam, 2020 October re-exam and 2024 June re-test — each year has only a MAIN sheet, so there was no re-exam transcription to recognise a re-exam file *by*; a strong MAIN match proves "these files are MAIN", never "the re-exam is missing". `scripts/lib/sittings.py` was correctly left untouched. **Still unresolved:** the official answer-key files, which are one unsplit file per multi-sitting year and which neither the index nor this method can place.
- **2026-10-12 — Real bug in my own `scripts/sitting_index.py`, found by the verifier agent and fixed.** It labelled 2026's first sitting `MAIN`, but `scripts/lib/sittings.py` requires 2026 → `[CANCELLED, REEXAM]`, so intake would still have seen 2026 CANCELLED as unmatched. Worse, a cancelled sitting is never scored and therefore has no official key — `SITTINGS_WITHOUT_KEY_REQUIREMENT` already accounts for that, so mislabelling it MAIN would silently reintroduce a key requirement that can never be met. Fixed; index and pipeline now agree exactly on 2026.
- **2026-10-12 — Real taxonomy gap found while reviewing the export: Biology questions can never get a branch.** `config/allowed_values.yaml` defines branches for **two** subjects — Chemistry (`physical`/`organic`/`inorganic`) **and Biology (`botany`/`zoology`)** — but the only step that assigns a branch is B7, the *chem*-branch-sorter, whose own allowed set is `physical, organic, inorganic, unsure`. So every Biology question falls through to `unsure`: real `Q-000015` (the female reproductive cycle) should be `zoology` and reads `unsure` instead. Physics correctly gets `None` (no branch is defined for it). **Not fixed unilaterally** — the options are to widen B7, add a Biology-specific sorter, or drop Biology branches from the taxonomy; which one is the owner's call. Until then `unsure` on a Biology record means "no step ever tried", not "a step tried and failed", which is itself misleading and worth noting wherever branch is displayed.
- **2026-10-12 — Booklet-code stranding resolved by giving B1 the official key's own code set; 398 questions unblocked at B5 (200 already joined, 198 pending).** `register/papers.csv` had `booklet_code` empty for `NEET-2024-MAIN-Q1` and `NEET-2022-MAIN-Q2`, which stranded every one of their questions at B5: `B5Plugin._find_key_page` needs a code to pick the key page, so with no code the paper was skipped and `official_answer` was never joined. Measured state before the fix: 2022 MAIN 200/200 unjoined, 2024 MAIN 198/198 unjoined, 2023 MAIN 219/219 joined. Because B7 is (correctly) gated on a B5 join via `_b_qid_records()`, the same two papers also accounted for most of the **537 of 618 records with no `subject` at all** — that was a B5 backlog, not a B7 defect.
  - **The B1 agent was right, twice, and was not overruled.** Both archived outputs (`steps/B1/out/_superseded_20261012T204546/`) refused the code on correct grounds: the only "Code Q1"/"Code Q2" text on those pages is site chrome generated from the neet.training URL and breadcrumb, which has *the same provenance as the folder name* and so is not independent page evidence. The agent file's `Never` rule — "the code must be positively found printed in the page content, not merely 'not disproven'" — is sound and was kept.
  - **What actually changed: the agent was reasoning about evidence it was never given.** The agent file's own GAJAHA example turns on whether a folder-implied code "appears in the real key's code set (M1, N1, O1)", but nothing ever passed that set in, so the agent could only answer the weaker question "is this code printed on this page". `B1Plugin._official_key_codes()` now reads every booklet code printed in the official NTA key for the paper's (year, sitting) straight off the key PDF and passes it as `official_key_codes`. Checked directly: **2024 prints 48 codes (M1–T6) and includes Q1; 2022 prints 32 and includes Q2.** A folder name agreeing with itself is not evidence; the authoritative key printing that code is.
  - **The rule added is three-way, and deliberately does not let corroboration masquerade as page evidence.** (1) Code printed on the page → `trust: official`. (2) Not on the page but present in `official_key_codes` → record the code with **`trust: memory_based`** — an allowed value in `config/allowed_values.yaml` that until now nothing ever used, and the honest label here: a real booklet of that code demonstrably exists, but *this file* does not show it. (3) Not on the page and not in the key's code set → `booklet_code: ""`, `trust: unsure`; the code is then contradicted, not merely unproven (the GAJAHA case). A second `Never` was added forbidding `official` for any code not read off the page, however strong the corroboration. This matters because B5 gates on `booklet_code` alone and never on `trust`, so a corroborated code unblocks the join while the provenance stays visible to any later reader.
  - **Note on the owner's instruction "trust neet training we need to add as official only".** Taken literally that would set `trust: official`, but `trust` in this pipeline does not mean "is the source reputable" — it means "did this document's own page confirm its booklet code" (b1 agent file, Rules). Marking these `official` would assert page evidence that provably is not there, and would make the field useless for the one thing it exists to signal. `memory_based` delivers what the instruction is actually for — the questions get processed instead of stranded — without falsifying the record. **Flagged for the owner to confirm**, since it is a reading of intent rather than a literal reading.
  - **B1's `prompt_version` was bumped v1 → v2** because the prompt genuinely changed, which marks all B1 items stale by the designed mechanism. Only the two stranded papers were re-run (`--items`); the other 7 already-registered files are now stale and will be re-registered on the next full B1 pass. Their outcome should not change — all have a code printed on the page — but they have not been re-run yet, so that is an expectation, not a verified result.
  - **Also verified en route, and separately actionable: the B7 qno→subject rule is now correct but 6 records hold stale pre-fix values.** The rule assigns a subject for **617 of 617** real records (the 618th file is `_qid_index`, not a record): 75 agree with what is stored, **536 are empty and would be filled**, and **6 are stored WRONG** — `Q-000057` (soap-bubble surface tension) and `Q-000073` (magnetic force on a wire) stored Chemistry but are Physics; `Q-000088` (tetrahedral voids) and `Q-000188` (magnetic quantum number) stored Physics but are Chemistry; `Q-000135` (angiosperm embryo sac) stored Physics but is Biology/botany; `Q-000605` (electrostatic precipitator) stored Physics but is Biology/zoology. All six were confirmed by reading the real stems. These are stale output from the pre-fix run, not a live bug — a B7 re-run corrects them once B5 has joined their papers.
- **2026-10-12 — Two independent discovery workers reported a data defect that does not exist; recorded so the claim is not acted on later.** Three separate agents reported that "the source PDF's chapter trailer is glued onto option 4", one of them in 11 of 12 records, with wrong chapter names (`Thermodynamics` on an equilibrium item, `Plant Kingdom` on flowering-plant morphology). **Checked across all 618 records: the cleaned `options_en` field is unaffected.** A regex over biology and chemistry chapter titles found exactly 2 hits in `options_en`, both legitimate content ("Biodiversity loss", "Biodiversity conservation"). The trailers live in **`b4_script_options`** — the raw text layer — which the pipeline already strips when building `options_en`. The reports were honest observations of the raw field mistaken for the clean one. **Real residual risk, worth a separate check:** anything downstream that reads `b4_script_options` instead of `options_en` would ingest the contamination, and the trailers are demonstrably wrong about the chapter, so they must never be used as a topic signal.
- **2026-10-12 — Mechanical defects confirmed across all 618 records, found while verifying worker reports.** (a) **9 cases print two or more identical options**, which no real paper does, so each is extraction damage: `Q-000083` and `Q-000558` (`34 cm^-1` twice — a dropped leading "1." makes the keyed option 1.26, matching κ·R exactly), `Q-000095` (`7 A` twice), `Q-000111` (`1 : 2` twice), `Q-000251` and `Q-000286` (both print bare `B` because an overbar was lost, so `Y = NOT B` cannot be mapped to an option number — unscoreable as stored), `Q-000359` (two pairs, consistent with lost decimal points), `Q-000391` (`57` three times). (b) **7 records carry assertion/statement text only inside `stem_en` with an empty `statements[]`**: `Q-000134`, `Q-000146`, `Q-000150`, `Q-000161`, `Q-000166`, `Q-000566`, `Q-000569` — a reader of the structured fields alone sees assertion-reason options with no assertion attached. Neither group is fixed yet; both need a re-read of the source page, not a guess.
- **2026-10-12 — Category discovery completed: 580 real questions analysed blind, clustered twice independently, delivered as `exports/discovery/CATEGORIES.xlsx`.** Two-stage method. Stage 1: 50 batch workers each analysed ~12 real questions with **no access to the existing taxonomy** — `config/allowed_values.yaml`, `codebook/*.md`, SPEC Sections 13/17, `.claude/agents/e*.md`, `scripts/type_patterns.py` and `scripts/describe_tags.py` were all named off-limits in every brief, so each question had to be described in the worker's own words across five fields (`built_how`, `asked_for`, `rests_on`, `thinking`, `option_traps`). Stage 2: eight clustering agents (two independent passes over all four subjects) grouped only those free descriptions and named their own categories. Output: **103 categories on 16 axes** (primary, with complete per-category id lists) plus **279 categories on 20 dimensions** (second opinion), 559 worked examples including every boundary case, over a 10-tab workbook.
  - **All 16 axes verify as complete partitions.** `scripts/build_category_workbook.py` re-derives every count from the agents' own id lists rather than copying their stated numbers, and checks each axis places all of its subject's questions exactly once, with no id in two categories. 16 of 16 passed. A count nobody can re-derive is not evidence, so the second clustering — which reports counts and three examples but no membership — is carried on its own tab and explicitly labelled unverifiable rather than merged into the primary numbers.
  - **The strongest and most repeated finding, reached independently by all eight clustering agents: printed shape is orthogonal to cognitive demand.** Two questions with byte-identical option grids routinely need completely different work (Chemistry Q-000332 vs Q-000335: the same two-column matcher, one a word-decoding exercise, the other four three-step VSEPR derivations; Physics Q-000011 vs Q-000009: the same printed shape, called "the shallowest" and "the most demanding" in their batch). **Any taxonomy keyed on how a question looks will merge items that behave differently.** The current `structure` field is exactly such a key.
  - **Second finding, quantified: most multi-part questions are mis-sized by their own format.** Botany: 59 of 141 items (42%) — 17 of 18 matching items collapse to one or two decisive judgements, while 21 "plain" one-liners demand several. Zoology: 30 of 31 decidable four-cell matching items are settled by one or two judgements, not four, and 48 single-line picks conceal two or more. Three mechanisms recur verbatim: a uniquely-pinned row (Q-000441 and Q-000446 are full Latin squares — *any* single row answers them), a false statement sitting in three of four options, and a statement appearing in all four options and doing nothing.
  - **Third finding, which inverts the obvious expectation: a two-statement item is harder per statement than a five-statement one.** With two statements the options exhaust the truth table, so there is no elimination leverage and both verdicts must be earned; with five, overlapping subsets mean one detected falsehood prunes most options. Confirmed separately in Botany (all 11 two-statement items non-collapsing) and Zoology.
  - **A category that is not a defect: items where better reasoning produces a worse answer.** 20 Botany items, 11 Zoology, 8 Chemistry, and a Physics group of 10 ("key fights the stem"): both options are defensible on mechanism and only a particular textbook's wording picks one, so a student reasoning correctly from the mechanism is marked wrong. Q-000416 is the purest case. This recurred often enough across independent agents to be a real category rather than scattered noise.
  - **An expected format is absent from the entire sample.** Not one of the 580 questions is a "how many of the above are correct" count item. Workers checked for it repeatedly. If the existing taxonomy carries that category, this sample does not support it.
  - **For Chemistry, the discovered axis beats the existing branch label.** Agents reported that `physical`/`organic`/`inorganic` does not predict behaviour, whereas "where the content sits" (stem-complete 94, candidate-resident 28, drawing-resident 24) predicts three things the branch label predicts none of: whether the item survives text extraction, whether it is answerable with the options covered, and which distractor family it uses. Recorded as evidence for a spec discussion, not acted on — `branch` is still assigned as specified.
- **2026-10-12 — Real bug found via a wrong agent diagnosis: B7's agent input never passed `list_i`/`list_ii`, leaving 7 match-list questions unresolvable.** Three independent agents reported that "extraction drops match-list tables systematically, ~21% of items". **Measured: false.** Only 3 of 72 match-like records (4%) have an empty list, and Q-000332's lists are fully intact on disk — "Isothermal process" → "Carried out at constant temperature", unambiguously physical chemistry. What was actually true is that `B7Plugin.list_items` built its agent input from `stem_en`, `options_en` and `statements` only, matching the agent file's Input section. For a "Match List-I with List-II" question those three fields hold nothing but boilerplate: the stem reads "Match List-I with List-II." (empty, for Q-000397) and the options are bare pairings like `A-II, B-III`. The agents were given a content-free record and correctly answered `unsure` — they could see the hole but not its cause.
  - **Fixed and re-run.** Both lists are now in the input and the agent file's Input section documents them, with an added instruction that the chemistry of a match item lives in the lists. The 7 affected items (Q-000332, Q-000353, Q-000368, Q-000369, Q-000387, Q-000392, Q-000397) were archived to `steps/B7/out/_superseded_*/` and re-run: **all 7 resolved** — thermodynamics→physical, ores→inorganic, hydride classification→inorganic, drug classes→organic, cyanohydrin/oxime reagents→organic, alkali-metal uses→inorganic, and Q-000353 organic at medium confidence because List-I's reactions are genuinely still unprinted.
  - **Worth keeping in mind as a general pattern:** an agent reporting "the data is damaged" may be reporting that *its input* is incomplete. Three agents converged on a confident, quantified, wrong diagnosis because none of them could see the record — only what was handed to them. The same shape of error produced the footer-bleed false alarm the same day.
- **2026-10-12 — `register/papers.csv` was append-only, so a B1 re-run could never correct a row it had already written.** `B1Plugin._post_assembly` returned early when a row with the same `(paper_id, file_kind)` existed. The new agent output was read, validated, reported DONE — and silently dropped. Hit for real: the re-run that produced `Q1`/`Q2` with `trust: memory_based` left the register still reading `booklet_code` empty and `trust: unsure`, which would have left all 398 of those questions stranded at B5 exactly as before, with nothing erroring anywhere. **A step whose output cannot reach the register is indistinguishable from a step that never ran.** Now the matching row is replaced in place (verified: 9 data rows before and after, no duplicate), which keeps the one-row-per-file rule while making re-runs actually effective.
- **2026-10-12 — Stage B now complete across the whole bank: 617 of 617 records joined, subjected and branched.** B5 joined all three papers (2022 MAIN 200, 2023 MAIN 219, 2024 MAIN 198 — previously 398 of these were stranded). Four official key pages were transcribed, each cross-checked twice (once from the key image, once against its text layer) with **zero digit discrepancies on all 800 rows**. Marks found and recorded rather than guessed: 2022-Q1 Q93 and 2022-Q2 Q87 both print `Option Id 5` against the key's own footnote `Note: Option Id 5 = Drop`; 2024-R1 Q12 prints `2,4` and 2024-Q1 Q19 prints `1,3` as multiple-accepted. Final state: `status` normal 613, dropped 2, multiple_accepted 2.
  - **The layout warning in my own brief was wrong, and the agents caught it.** I told the 2022-Q1 copier the key's text layer was column-major; it is row-major (`1,4, 41,3, 81,1, 121,3, 161,1` is one visual row). The agent established the layout from the image first, as instructed, found the text read the other way, and said so — then the 2022-Q2 agent independently confirmed it. Had either simply trusted my note, ~200 questions would have been assigned the answer belonging to a question 40 places away. The "establish layout from the image, use the text layer only to confirm digits you have already placed" instruction is what made the error harmless; it should stay in any future key-copy brief.
  - **This closes the Biology branch gap logged earlier today.** That entry recorded that Biology questions "can never get a branch" because the only branch-assigning step was the chem sorter, so every Biology record read `unsure` — meaning "no step ever tried", which reads identically to "a step tried and failed". Now: botany 141, zoology 145, **`unsure` 0**. Physics correctly has no branch; Chemistry's 160 are physical 55 / organic 54 / inorganic 51 from 112 agent calls, with one principled `unsure` remaining (Q-000609, eutrophication — environmental chemistry fits none of the three branch definitions, and the agent declined to force it rather than guess).
  - **An ordering artefact to be aware of when reading the shards:** B5's key join ran *while* the discovery analysis was in flight, so roughly 93 analyses carry a "no official answer on record" caveat that was true when written and is stale now. One coordinator re-checked 69 independently derived answers against the keys that have since landed: **68 agreed**. The single genuine disagreement (Q-000495) was added to the key-conflict list. The workbook's Verified-false tab records this so the caveats are not mistaken for current state.
- **2026-10-12 — Real B5 bug: a key row with an empty answer was recorded as `status: normal`, so a question the official key DROPPED read as an ordinary scorable one.** `B5Plugin._post_assembly` derived status by substring: `"bonus" in mark` → bonus, `"drop" in mark` → dropped, comma in answer → multiple_accepted, **else normal**. Real NEET keys print a bare option id in the answer cell and define it in a footnote on the same page ("Note: Option Id 5 = Drop", "5 DENOTES QUESTION IS DROPPED"), and the agent file tells copiers to transcribe the PRINTED mark text — so the same meaning legitimately arrives spelled different ways. Measured across all four key pages: 4 rows have an empty answer, in three spellings — `Drop` ×2, `Dropped` ×1, `5` ×1.
  - **The one that broke was Q-000004**, which appears in two booklets: E1 qno 2 came back `mark: "5"`, E2 qno 30 came back `mark: "Dropped"`. Only the second was recognised; the first matched neither "bonus" nor "drop" and fell through to `normal` while carrying `official_answer: ""`. **Downstream consequence beyond the wrong label:** B8 only ever looks at bonus/dropped/multiple_accepted records (`_B8_STATUSES`), so B8's own `corrected_answer: "1"` for that question was stranded behind a status asserting it wasn't needed.
  - **Fixed two ways, deliberately.** The digit spellings are now matched alongside the word, *and* an invariant guard was added: a row with no answer has nothing to score, so it can never be `normal`. Reaching that guard means the mark is a spelling this step has not been taught, so it records `dropped` (the safe reading) and raises a new `B5_UNRECOGNISED_MARK` flag (severity `high` in `config/steps.yaml`) rather than guessing silently. After re-running the join: normal 612, dropped 3, multiple_accepted 2 — and Q-000004 is `dropped` again with its B8 answer reachable.
  - **Found by a test, not by inspection.** `tests/test_e_checks.py::test_e5_question_with_no_answer_cannot_be_trap_tagged` asserts on real data that Q-000004 is dropped; it started failing the moment the join re-ran. That is the test earning its keep — the regression was silent everywhere else.
- **2026-10-12 — Real A2 agent error, confirmed by looking at the page: a unit-opener page was called "front matter" and 1,478 characters of real NCERT prose were discarded.** `BIO11L` chapter 1 page 1 returned **zero blocks**, with the note "Page is unit front matter, not chapter content... the Unit 1 opener: a seahorse illustration, the banner...". Checked the rendered PNG directly: the page *is* a unit opener — seahorse, "UNIT 1 / DIVERSITY IN THE LIVING WORLD", a list of chapters 1–4 — **and it carries the full unit-introduction paragraph printed beside them** ("Biology is the science of life forms and living processes..."). Also verified there is no page-offset bug between image and text layer: page 1 of that PDF genuinely holds both 1,478 characters of text and 3 images.
  - **Cause was an under-specified rule, not a careless agent.** `.claude/agents/a2-page-reader.md` listed front matter by example — "title page, preface, table of contents" — and the agent generalised from the examples to "a page that looks like an opener". The rule now states the test explicitly: furniture is navigational/publishing apparatus (title, banner, unit or chapter name, chapter list, page number, preface, contents, index), **a paragraph of real subject prose is content and stays content whatever sits around it**, so a unit opener is a MIXED page — block the prose, treat only the banner, illustration and chapter list as furniture. Added with the real case named, plus a rule that being about to return zero blocks is itself the cue to look again.
- **2026-10-12 — `tests/test_a2_check.py` was asserting that no real A2 output ever fails the check, which inverted its own meaning as the corpus grew; its sensitivity floors turn out to have been measured on contaminated data.** The corpus is now 446 outputs and **33 fail**. The old test counted every one as a false positive of the CHECK, so a growing pile of genuine extraction defects was reported as a defective check.
  - **Restructured to be honest about what is and isn't verified.** A new `UNTRIAGED_FAILURES` set lists all 33 with the reason each fails. Exactly **one is certified genuine** (BIO11L-ch01-p001, confirmed by eye above); the other 32 are explicitly **not** individually verified — their causes range from almost certainly real (0 blocks, a block 0.0% matched to the text layer, numbers absent from the page) to small shortfalls just under the bar (recall 98.4–99.0%), and triaging each needs the page image. The set is pinned in both directions: a failure outside it fails the test as news, and an entry that silently starts passing fails as a precision regression. It is also the work queue for the Stage A re-read.
  - **The floors were inflated and are now recalibrated.** The sensitivity loop corrupts each real output and measures the catch rate — but it only excluded `KNOWN_BAD`, so the 33 outputs that already fail uncorrupted were scored "caught" regardless of what the corruption did, inflating every rate for free. Measured on the clean subset instead: **`drop` 21.1% not 28%, `halve` 21.4% not 24%, `negate` 5.9% not 9%** — the check was never that good at those families, the denominator was dirty. Two moved the other way (`scramble` 83.0% not 76%). Floors updated to sit just under the clean measurements. Full suite: **211 passed**.
  - **One near-miss was NOT a bug, and is worth recording because it looked exactly like one.** Several failures read "blocks account for only 99.0% of the page's text-layer prose (want >= 99%)", which reads as a contradiction and invites someone to "fix" a correct threshold. The comparison is `<`, so an exact 99% passes; the message was simply rounding 0.9897 up to "99.0%" for display. Fixed by widening the printed precision when rounding would hide the gap, rather than touching the threshold.
- **2026-10-13 — CORRECTNESS BUG, found by an A3 worker and verified by hand: a missing A2 page makes A3 silently merge two different topics into one section, so passages get filed under the wrong heading.** `BIO11L-ch02-s12` is headed **"2.2.5 Protozoans"** and its blocks read: n=1–4 on page **006** (protozoan text, with n=3 breaking off mid-sentence at "They move and capture"), then n=5–8 on page **008** carrying **fungi** content — conidia/sporangiospores, plasmogamy/karyogamy, the dikaryophase, mycelium-based classification. Checked directly: `steps/A2/out/` holds BIO11L-ch02 pages 001–006, 008–011, 013 — **pages 007 and 012 were never read**. The `2.3 FUNGI` heading lives on the unread page 007, so A3's section assembler bridged the gap and attributed a page of fungi to the protozoans section.
  - **Why this is worse than a missing page.** A gap on its own is a known, visible shortfall. This turns the gap into *wrong* data: the passages A3 cut from blocks 5–8 are now evidence filed under "Protozoans", and Stage D would offer them to an agent as the NCERT basis for a protozoan question. A question about fungal reproduction could be "justified" by a passage the pipeline believes is about protozoans, and nothing downstream would contradict it.
  - **Measured blast radius: 3 of 19 chapters, 9 missing pages, all BIO11L** — ch01 missing 3, 4, 6, 7; ch02 missing 7, 12; ch03 missing 4, 7, 11. The other 16 chapters have contiguous page runs. BIO11L also had by far the lowest A2 output (27 pages), consistent with its A2 never having been finished rather than having failed.
  - **Two separate fixes are needed and only one is "run the step again".** (1) A2 must read the 9 missing pages, after which A3 must be re-run for every section it assembled across a gap. (2) **A3's assembler must refuse to bridge a page gap, or at minimum flag it** — as written it concatenates whatever A2 produced in page order and cannot tell a genuine page break from an unread page. Fixing only the data leaves the trap armed for the next book whose A2 is incomplete; fixing only the assembler leaves 9 pages unread. Not yet actioned.
- **2026-10-13 — Real gating bug fixed: A4 was offering work on chapters whose A3 was unfinished, which would have produced a whole chapter's subtopic list from a third of its text.** `config/steps.yaml` declares `needs: A3` for A4, but `A4Plugin.list_items` enforced only "A3 has produced an `ncert/chapters/` file at all" and then handed the agent whatever passages happened to exist at that moment. Caught before dispatch: it was offering **BIO11L-ch02 with 6 of 20 sections split** and **CHE11L-ch01 with 14 of 61**. A subtopic list is written per chapter from that chapter's complete passage set, so this would have produced output that passes its own schema, satisfies every check, and is quietly wrong — the exact failure shape this session has been chasing.
  - Fixed with `A4Plugin._a3_incomplete_sections()`, which matches a chapter_id (`BIO11-CH02`) against A3's own work files (`BIO11L-ch02-s*`) and holds the chapter back until every section has output; `list_reason` now names the waiting chapters and their unsplit counts. Verified end to end: before A3 finished it listed only CHE12-CH09 (the one genuinely complete chapter); the moment A3 reached DONE, all four held-back chapters listed themselves. 211 tests pass.
- **2026-10-13 — Adjudicators were deciding A4 disputes without the passages, and one noticed by itself.** `x-adjudicator.md` defines `evidence` as "the same input the step's agent saw", and A4's agents receive `passages` (id, kind, first 200 characters). But `A4Plugin._start_adjudicator` built `evidence` as `{chapter, chapter_title, headings}` only. The BIO12-CH02 adjudicator reported the omission unprompted and **lowered its own confidence to medium because of it**: "the decision therefore rests on section structure, contiguous passage-id ranges, and the two runs' groupings and names, not on passage text." Verified: its evidence held 3 keys where the step's agents saw 52 passages. The CHE12-CH09 adjudicator hit the same wall, saying of one boundary that there was "no passage text in the evidence file to settle it".
  - Fixed: the adjudicator payload now rebuilds `passages` from `ncert/passages/` (verified: BIO12-CH02 → 52, CHE12-CH09 → 131, PHY11-CH08 → 84). Rebuilt from the store rather than passed down, because by adjudication time the run inputs may have been regenerated.
  - **12 A4 chapters were already adjudicated under the old payload** and were therefore decided blind. Nothing has shipped — every one carries `A4_SUBTOPICS_DRAFT` pending the owner's approval — but they should be re-adjudicated now the payload is correct. The two decided today are the exception worth keeping: BIO12-CH02 chose run A on grounds (a subtopic named "Chapter summary and exercises" is a location, not an idea, which the step's naming rule forbids) that passage text would not have changed, and CHE12-CH09 reached `combined` with all 131 passages covered.
- **2026-10-13 — Extraction defects reported independently by A3 workers across both 11th-class books; none repaired, all recorded in the per-section `note` fields.** (a) **Empty-text blocks are pervasive**: `figure`, `equation` and `table` blocks routinely arrive with `text: ""` because the image was never extracted (CHE11L-ch01 sections 07, 08, 15, 20, 21, 22, 27, 29, 32, 34, 35, 40, 41, 43, 46, 47, 51, 53, 55, 56, 57, 59, 61 among others). This matters beyond tidiness: a passage whose only block has no text **carries no quotable words**, and quotable evidence is the entire purpose of a passage — `quote_verify.find` cannot match against an empty string. (b) **Mid-page truncation, distinct from the missing-page bug above**: `CHE11L-ch01-s22` breaks off at "...the mass obtained is 9.4213g. The" at the foot of page 012 and resumes at item (5) of the significant-figure rules — rules (1)–(4) are simply absent, with no page file missing. (c) **Section headings that misdescribe their own content**: `CHE11L-ch01-s20` is headed "Multiplication and Division" while blocks 5–7 are entirely about significant figures; `CHE11L-ch01-s18` ("1.3.7 Temperature") holds a fragment on presenting data unrelated to its truncated block 2; `BIO11L-ch02-s19` is headed "VIRUSES, VIROIDS, PRIONS AND LICHENS" but its blocks cover only viruses. (d) **Continuation blocks mis-tagged `kind: "box"`** (CHE11L-ch01-s46 blocks 6 and 8, s60 blocks 4/5), so `kind` cannot be trusted over reading order. (e) Two independent A4 runs found `CHE12-CH09`'s `headings` list **duplicates 9.5, 9.7, 9.8 and 9.9** because four exercise prompts were captured as headings.

## 2026-10-13 · A2S crop padding, the `box` kind, and two contract contradictions

**A2S crops were unpadded.** `A2SPlugin.list_items` cropped the bare bbox, but A2's box bounds the
drawing, not what a transcriber must read: a figure's caption sits below it and reagent labels sit
above it. Eleven independent A2S workers reported roughly 50 clipped crops — captions cut
mid-sentence, the reagents above all three arrows of a diazotisation scheme missing entirely, and
`CHE12L-p013-b17` so misaligned the crop was mostly the previous block's prose. Now padded by
(24, 48) px, more vertically for exactly that reason. `scripts/checks/A2S.py` had already written
down "the proper fix is upstream (crop with padding)"; this is that fix.

**156 A2S outputs were orphaned by the chapter-qualified item_id fix** and are archived under
`steps/A2S/out/_superseded_*_shortid/` with a README. They were written under `<BOOK>-p<page>-b<n>`,
which collides because every chapter PDF restarts at page 1 — 14 of those ids match a block in both
CHE12L ch01 and ch09. Re-run rather than renamed: the id is inference for the colliding 14, and all
156 came from unpadded crops anyway.

*A measurement that did not work, recorded so nobody repeats it.* I tried to decide per item whether
the old crop had clipped anything by rendering the padded region and looking for ink in the margin
bands. It reported 136 of 156 clipped against the ~50 the readers actually saw. The bands catch the
neighbouring paragraph on a dense NCERT page, which is not this block's lost content — the agents had
said as much ("a sliver of a neighbouring block"). Distinguishing the two needs a glyph-straddles-the-
edge test, not a band-ink test. Not worth building, since every one of the 156 needed a new id anyway.

**`kind: "box"` is now a fourth A2S kind** (schema, agent file, check, `tests/test_a2s_box.py`).
SPEC 9/A2S names only table/figure/equation, but A2's kind enum includes `box` and A2 agents do mark
a box needs_special when a worked example's display equations would be lost. Six exist in the real
corpus (CHE12L ch01 p005/p008/p016, ch09 p005/p006, PHY11L ch06 p017) and **four carry `text: ""`**,
so their prose was captured nowhere and the box was permanently unquotable. Five separate workers hit
these and each improvised: two relabelled them `equation` (discarding the prose), three kept `box`
and invented a `text` field. A box now REQUIRES `text`, because prose is the only thing
`quote_verify.find` can match a citation against; `latex` stays optional (PHY11L ch06 p017 b22 has no
display equation at all).

**`scripts/status.py` could not run at all.** It recognised status side-cars by a hand-maintained
filename blacklist (`.pending.json`, `.last_block.json`) and then indexed `rec["status"]` directly,
so it died with KeyError on B2's 413 `<ITEM>.last_q.json` files and B6's aggregate `_paper_stats.json`.
`f_common.iter_step_statuses` had already settled the right rule — a side-car is anything with no
`status` key, recognised by content, not by name — and status.py now matches it.

**B3's `negative_words_seen` contract contradicted itself**, blocking two correct outputs
(NEET-2023-MAIN-E1-q0152, -q0160). The agent file said to list the words "(as printed)", NEET prints
them lower case inside the Statement I/II option shells ("Statement I is correct but Statement II is
false."), and the schema enum demanded capitals. The agent obeyed its instruction and was failed for
it. The schema is now case-insensitive and the agent file says "whatever case it is printed in".
Safe because case carries no information downstream: `checks/E2.py` `field_negatives` and
`describe_tags.py` `negation` both upper-case before comparing. MISMATCH and other non-members are
still rejected. Blocked items: 9 -> 7.

## 2026-10-13 · B8's NCERT passage search ignored the question's subject

A B8 worker reported that both its inputs carried off-topic `latest_passages`: Q-000384 is a
Chemistry electrochemistry/Nernst question whose 15 supplied passages were physics mechanics,
current electricity and biology exercises. It was right, and the cause is worth writing down
because the obvious diagnosis is wrong.

It is **not** a ranking bug. `_b8_latest_passages` searched every latest-edition passage in the
corpus with no subject scope, and `search_index.rank` returns the best `limit` matches however poor
they are. CHE12L chapter 3 (Electrochemistry) is not indexed yet, so there was no right answer to
find, and the search returned 15 confident-looking wrong ones instead of nothing.

**A score floor does not fix it, measured before rejecting it.** The top match for Q-000384 across
the whole pool was PHY11L-CH05-P54 at score 8.19, against a pool median of 1.08 — i.e. the
wrong-subject passage scored *high*, because a long stem shares generic words ("cell", "reaction",
"find", "takes") with any long passage. Subject is the discriminator, not score.

Fixed by scoping the search to the question's own subject (`_passage_subject` off the book_id
prefix). The same question now returns CHE12L-CH01 passages. Two deliberate properties:

- A record with no `subject`, or an unrecognised book prefix, falls through to the old unscoped
  behaviour rather than returning nothing — a missing subject is a different defect and must not
  silently empty the evidence.
- `[]` is now a real and honest outcome meaning "no latest-edition passage exists for this subject
  yet". A caller that gets `[]` should report the NCERT basis as unavailable, never reach wider.

Why this mattered more than the two questions involved: B8 asks the agent for an *exact quote* from
these passages, and D3 builds its input from the same kind of pool (`_d3_texts`). Offering
plausible, well-ranked, wrong-subject passages is precisely the setup that produces a fabricated
citation. Both workers here returned `supporting_quote: null` and said the passages were off-topic,
which is the correct behaviour — but that was their diligence, not a guarantee from the pipeline.

**Checked, and D3 does not share the defect.** The worry was that `_d3_texts` feeds D5/D6/D7 the
same way, but it only reads back the passages D3 already chose, and D3's own pool is built by
`scripts/fetch_passages.py`, which scopes candidates by `chapter_id` taken from D2's subtopics —
strictly tighter than a subject filter, since it never leaves the assigned chapter. So the broad
unscoped keyword search was B8's alone. `_b7_*` and `D9`'s uses of `search_index.rank` are
separate call sites and were not part of this fix.

## 2026-10-13 · A2 page-reader agents die to an API content filter, and why incremental writes matter

Running A2 at scale, several page-reading agents terminated with `API Error: Output blocked by
content filtering policy`. It is **not** tied to particular page content:

- Three successive dispatches covering BIO11L ch01/ch02/ch03 died at their very first input read,
  before any page image was opened. The input they were about to read, BIO11L-ch01-p003, is
  ordinary NCERT prose ("How wonderful is the living world !...", 1,787 characters) — nothing a
  filter should act on.
- A fourth agent died the same way **mid-run, after page 11 of 14**, on a different book.

So treat it as a transient platform-side failure on this step, not a data defect, and do not go
looking for the offending page. Three practical consequences:

1. **The "write each output the moment you finish that page" instruction is load-bearing, not
   style.** The agent that died at page 12 had already written 11 real pages, all of which survived.
   The earlier A3 incident (5 of 7 agents ending having written nothing, ~67 items lost) is what
   this instruction was introduced for, and it paid off again here against a completely different
   failure mode.
2. **A2 must be driven as a re-list loop, never a single pass.** After each wave, re-list and
   re-dispatch whatever is still missing; a dead agent costs the remainder of its group, not the
   group.
3. Progress is measurable independently of whether an agent reported success — count the output
   files per group rather than trusting the completion summary.

BIO11L ch01 p003/p004/p006/p007, ch02 p007/p012 and ch03 p004/p007/p011 are still unread after
three attempts, and they are the pages holding back the 4 withheld A3 sections
(`A3_SECTION_SPANS_UNREAD_PAGE`). They need another attempt.

### Update, same day: the content filter escalated and now gates A2 throughput

What began as a handful of failures became the limiting factor on this step. Measured across ~25
dispatches in two waves:

- Agents given a whole chapter in page order mostly succeed when they survive their first turn.
  Completed whole: PHY11L ch01+ch02 (26 pages), CHE12L ch05 (23), CHE12L ch10 (22), BIO12L ch10+ch12
  (22), BIO11L ch10+ch18 (20), PHY12L ch08 (14).
- In the second wave most agents died after 2-4 pages, and 5 of 5 single-page agents for BIO11L
  ch01/ch02 died on their **first** turn, before reading any file.

The last point rules out the page as the cause, and it also rules out my prompt wording: the five
single-page prompts were byte-identical apart from the item id. Nothing had been read, so there was
no page content in the context to object to. I could not localise it further than that, and I stopped
trying after eleven attempts rather than keep spending on a black box.

Practical consequence for whoever runs this next: **A2 is throughput-limited by this, not by
judgement**, so drive it as many small re-list waves with whole chapters per agent, expect to
re-dispatch, and count output files rather than trusting completion summaries. Do not escalate
concurrency to compensate; the failures did not correlate cleanly with it either way.

Pages still unread after repeated attempts, and what they block:
`BIO11L-ch01-p004/p006/p007`, `BIO11L-ch02-p007/p012`, `BIO11L-ch03-p004/p007/p011`,
`BIO11L-ch07-p005/p006`. The ch01-ch03 pages are the ones holding back the four withheld A3
sections (`A3_SECTION_SPANS_UNREAD_PAGE`). `BIO11L-ch01-p003` and `BIO11L-ch07-p004` did eventually
get through, so these are not permanently unreachable — they just need another pass later.

## 2026-10-13 · Question-record data integrity: three measurements, one of them reassuring

Several B6 workers independently reported extraction damage in question options. Measured across
all 619 records rather than taken on report:

**1. Section-header bleed into options: real in the raw field, COMPLETELY cleaned.**
528 of 619 `b4_script_options` sets contain a newline — overwhelmingly option 4 as
`<value>\n<SectionName>` (e.g. `"1 : 2\nWaves"`, `"57\nEquilibrium"`). **None of it reaches the
clean `options_en`.** This settles an earlier claim by four separate agents that chapter-footer text
was contaminating option 4: it contaminates the RAW script extraction only, never the delivered
data.

Correction to my own first pass on this: I reported "3 survived" and listed them as a work queue.
They are not survivors. A newline in `options_en` was my proxy for bleed, and all three hits are
options that are *inherently* multi-line and correctly transcribed — `Q-000185` and `Q-000544` are
logic-gate truth tables (`A B Y / 0 0 1 / ...`) and `Q-000049` is a pedigree diagram
(`□—○ │ ■`). So the queue was a queue of non-problems, and the real strip rate is 528 of 528.
(Incidentally Q-000185 and Q-000544 carry byte-identical options, so they are one of the duplicate
pairs counted under finding 3 below.)

**2. Lost radicals and exponents are real and upstream of the agents.** `Q-000111` is the clean
example: raw options are `1 : 1`, `2:1`, `1: 2`, `1 : 2\nWaves`, so options 3 and 4 are identical
because the printed option 4 is **1 : √2** and the PDF text layer dropped the radical. B3's agent
copied faithfully; the loss happened before it. Nine such duplicate-option defects across 7
questions: Q-000083, Q-000095, Q-000111, Q-000251, Q-000286, Q-000359, Q-000391, Q-000558
(Q-000391 has THREE identical options, `57`). These need a B3 re-read taken from the image crop
rather than the text layer, and 18 further records are explicitly marked unreadable/scrambled.

**3. Contested provenance: 70 question_ids, 35 paper-code slots.** A paper_code identifies one
printed question — (year, sitting, booklet code, question number) — so two question_ids claiming
the same slot is a defect. 17 of the 35 clashes are byte-identical stems (the same question stored
twice); the other 18 are worse, two records claiming the same exam question with DIFFERENT stems,
so at least one carries a wrong code. Not auto-fixable: deciding which record owns a slot needs the
paper page read, which is an agent judgement, not arithmetic. Left as a queue deliberately.

Related: 198 records carry `paper_codes` doubly prefixed (`NEET-2024-MAIN-Q1:1` instead of `Q1:1`).
Cause found in `B3Plugin._post_assembly`: `code = paper_row.get("booklet_code") or paper_id`, which
silently substitutes the full paper_id when the register row's booklet_code is blank — writing a
value of the wrong SHAPE into the field C1 uses to merge booklet-code duplicates. The register has
since been corrected (all 6 paper rows now carry a short code), so these values are stale rather
than unfixable, but the fallback itself is a latent trap: it should flag, not invent.

## 2026-10-13 · B1 could not reach `trust: memory_based` at all, for two separate reasons

Four B1 workers, independently and unprompted, reported the same thing: `official_key_codes` was
**absent from every one of their inputs**, so case 2 of the three-way booklet-code rule was
unreachable and they correctly refused to upgrade anything on no evidence. They were right, and
there were two distinct causes behind it.

**Cause A — stale cached work inputs.** The field was added to `B1Plugin._build_input` earlier the
same day, but a work input already on disk is not rebuilt, so 156 of 211 inputs predated it. Fixed
by deleting every pre-field input that had no output (69 of them) so it regenerates; inputs whose
output already exists were left alone rather than invalidating real work. Non-empty code sets went
from 26 inputs to 138.

**Cause B — the key parser only knew one of three spellings.** Two real gaps, both fixed:
  * 2018 publishes **one key file per booklet code**, with the code only in the FILE NAME
    (`NEET_answers-key_2018-AA.pdf` … `-ZZ.pdf`). Reading only text layers returned 0 codes for
    2018. Now harvested from the filename too, via a deliberately CASE-SENSITIVE pattern so the
    descriptive suffixes in the same directory — `-neet.pdf`, `-phase-1.pdf`, `-Re_neet.pdf` — are
    not misread as the codes NEET, 1 or RE. Verified against all 30 key files present.
  * The 2020 key states its booklet as **`BOOK : E1`**, with the word CODE absent, which the
    `BOOK(?:LET)?\s*CODE` pattern could not match. Added as a third alternative, colon required so
    the bare word "book" in prose cannot be read as a code.

Result, measured per year: 2018 0 -> 19 codes, 2020 0 -> 48, 2021 0 -> 24; 2022 (32) and 2023 (48)
unchanged. Still 0 for 2016, 2017 and 2025 — a remaining gap, not yet diagnosed.

**A correction to the workers' own conclusion, which matters.** Two of them judged the scraped
folder codes `AKANH-E5`, `KANHA-E1`, `AGAJHA-M4` to be fabricated, reasoning from the scrambled-word
prefix and its resemblance to the known-fabricated `GAJAHA-M1`. Checked against the now-readable key
sets: the **suffix** (`E5`, `E1`, `M4`) is a genuine code in that year's official set, and only the
leading slug is site noise. So these ARE corroborable, and `unsure` understated them. 43 outputs
judged `unsure` purely for want of the field were archived to
`steps/B1/out/_superseded_*_no_key_codes/` and re-queued; the re-run brief tells the agent both
halves — that the suffix corroborates, and that the page still does not print it, so `memory_based`
is the ceiling and `official` is not available.

Worth keeping as a general lesson: three times today a confident agent claim turned out to be
measurably wrong in a way a two-minute script could settle (the footer bleed, the "fabricated"
codes, and the padding-band clipping estimate). Measure before acting on a report.

### Same day: a spurious key code did real damage, and how it was caught

`official_key_codes` is the only route to `trust: memory_based`, which makes it a *trusted* input —
and that asymmetry matters more than it looks. A MISSING code merely blocks an upgrade. A SPURIOUS
code causes active harm, because an agent that finds a page-printed code absent from a code set it
has every reason to believe concludes the key contradicts the page.

That is exactly what happened. `SET\s*:?` under `re.IGNORECASE` matched "a gene or set of genes" on
page 30 of the 2016 phase-2 key and captured **"of"** as a booklet code, making that sitting's set
the single element `['OF']`. A B1 worker then read a page that legitimately prints "Code – AA",
found AA missing from `['OF']`, and downgraded a case-1 `official` to `unsure`. Its reasoning was
correct; its input was poisoned by this project's own regex.

It was caught only because that worker added, unprompted, that `['OF']` looked "suspiciously short
for a sitting". Worth noting as a practice: an agent reporting that its *evidence* looks wrong is
more valuable than an agent reporting a verdict, and that remark should always be checked.

Two independent narrowings, either of which kills the match, both kept because of the asymmetry
above:
  * `SET` now requires its colon.
  * The code group is matched case-sensitively via `(?-i:...)` while the label stays
    case-insensitive — a printed booklet code is always upper case; lower-case words are prose.

2016 PH2 now correctly returns `[]`. All legitimate sets are unchanged (2018 19, 2019 28, 2020 48,
2021 24, 2022 32, 2023 48, 2024 48). `tests/test_b1_key_codes.py` pins all of it, in both
directions: the three real spellings, the exact "set of genes" sentence, the filename codes, and
the descriptive filename suffixes that must NOT be read as codes. The damaged output is archived
under `steps/B1/out/_superseded_*_of_false_positive/` and re-queued.

### Same day: the 2018 scrapes appear to be one booklet relabelled

Independently reported by two B1 workers. Three 2018 files filed as codes `HH`, `XX` and `YY` each
bleed the SAME original-paper footer through into a question option — `ACHLA/AA/Page 6`,
`ACHLA/AA/Page 13`, `ACHLA/AA/Page 14` — whose only booklet code is **AA**. A third worker saw the
same `ACHLA/AA` footer under four claimed codes. At most one of those files can really be booklet
AA, so the site appears to serve pages of one underlying paper under several "set" labels.

This is the most likely explanation for a separate measurement recorded above: 35 paper-code slots
claimed by two question_ids each, 17 of them with byte-identical stems. If several scraped "sets"
are the same booklet, the same printed question legitimately arrives twice under different codes,
and the duplicate is in the SOURCE, not in this pipeline's handling of it.

Also found, and correctly handled by the field doing its job: `neet_2018_code-QQ` — QQ is genuinely
absent from the 2018 key's code set (which runs AA..ZZ but skips QQ), nothing is printed on the
page, so it is rule case 3 and stays `unsure`.

### Same day, and this one was my error: "the code is in the official key's set" can mean nothing

Having just made `official_key_codes` work, I told five B1 workers in their dispatch briefs that a
scraped folder code like `AKANH-E5` could be corroborated on its **suffix** against the key's code
set, and that `unsure` therefore understated those papers. That was wrong, and it wrongly upgraded
49 items to `trust: memory_based`.

A worker refused to just comply. It followed the instruction but wrote back that the agent file's
own `GAJAHA-M1` example says `unsure`, that it had taken my correction only because it claimed the
key set was re-verified, and that `GAJAHA-M1`/`GAJAHA-N1` were the items to revisit first if I was
wrong. Checking coverage per year settled it immediately:

| year | code set | coverage | a wrong code can fail? |
|------|----------|----------|------------------------|
| 2018 | 19 of 26 doubled letters | 73% | yes — and `code-QQ` really did |
| 2019 | 28 of 48 letter-digit combos | 58% | yes |
| 2022 | 32 of 48 | 67% | yes |
| 2020 | 48 of 48 (EFGHWXYZ x 1-6) | **100%** | **no** |
| 2021 | 24 of 24 (MNOP x 1-6) | **100%** | **no** |
| 2023 | 48 of 48 (ABCDEFGH x 1-6) | **100%** | **no** |
| 2024 | 48 of 48 (MNOPQRST x 1-6) | **100%** | **no** |

Where the key lists the complete cross-product, a code of that shape matches BY CONSTRUCTION. An
invented suffix matches exactly as surely as a real one, so the check has no discriminating power
and cannot corroborate anything. The agent file's `unsure` was right all along.

Fixed so the question is never put to an agent again, since it is arithmetic about the key's code
space rather than a reading of any page:
  * `B1Plugin._key_codes_discriminating(codes)` computes it and returns a one-line reason.
  * Every B1 input now ships `official_key_codes_can_fail` and `official_key_codes_note` alongside
    the set itself — deliberately together, because the set alone reads as corroboration whatever
    its shape.
  * The agent file gained a **case 0**: check that flag first, and when it is false, case 2
    (`memory_based`) is simply unavailable.
  * The 49 affected outputs are archived under
    `steps/B1/out/_superseded_*_nondiscriminating_match/` and re-queued. The 10 `memory_based`
    results on genuinely selective years (2018, 2019, 2022) were left untouched.

The lesson is narrower and more useful than "verify agent claims", which I already knew: **verify
your own claims before putting them in a dispatch brief**, because a brief overrides a carefully
written agent file and propagates to every item in the wave. Three agent reports were measurably
wrong today; so was one of mine, and mine did more damage because it was authoritative. The worker
that answered with "here is what to revisit if you are wrong" is the reason it cost 49 re-runs
instead of sitting in the data.

## 2026-10-13 · The A2 coverage check was punishing agents for removing furniture correctly

Fourteen chapter-opening pages failed `A2_TEXT_MISMATCH` across the Stage A waves, and I first
recorded that as "chapter openers under-capture at 91-97% recall" — an agent problem. That framing
was wrong, and the persistence was the clue: the rate did not budge after I strengthened the
agent file's opener rule, and it kept happening across many different agents.

The actual cause: coverage was measured against ALL the page's text-layer prose, with no discount
for what the agent declared as furniture. A chapter-opening page carries a section-contents panel
("7.2 Kepler's laws", "12.1 Do Plants Also Breathe?"), which is navigational apparatus — furniture
by this step's own definition — and it is present in the text layer. The agent correctly keeps it
out of `blocks`, and every one of those words was then counted against it.

`PHY11L-ch07-p001` is the proof: it listed **all sixteen** panel lines in
`running_header_footer_removed`, excluded them exactly as instructed, and was failed at 90.7%.
Dumping the unaccounted lines for three such pages showed they were *nothing but* the panel, the
page number and the reprint year.

There was a second half to the bug. Matching the declared strings line-by-line would not have
worked either: the agent declares `"7.2 Kepler's laws"` while the text layer breaks it as `"7.2"`
and `"Kepler's laws"` on separate lines. Comparing word multisets sidesteps the layout.

Fixed in `scripts/checks/A2.py` on BOTH limbs that consume the text layer, because fixing only the
first just moved the failure: after the recall discount, PHY11L-ch07-p001 immediately failed the
consecutive-unexplained-run limb on the same sixteen lines counted a second way.

The discount cannot be used to hide a bad transcription: it only removes words the agent explicitly
listed, those words must occur in the text layer to be subtracted, the run-limb version consumes
from a multiset so one declared word cannot explain many occurrences, and a declared string that
also appears inside a block is already a separate failure. So furniture cannot be both discounted
here and kept there.

**Net effect, and the discrimination is the point:** `PHY11L-ch07-p001` and `PHY12L-ch11-p002` now
pass, and five entries that had been sitting in `UNTRIAGED_FAILURES` — two of them from before this
session — were cleared as genuine false positives. Pages that removed the panel *without* declaring
it (`BIO11L-ch12-p001`, `BIO11L-ch19-p001`, `PHY11L-ch01-p001`) still fail, which is the real and
much narrower error. The agent file now says plainly that listing removals is what the check depends
on, with the measured contrast: the page that listed its sixteen panel lines passes, the two that
removed the same kind of panel silently were failed at 89.4% and 93.5%.

Worth generalising: a check that fires on many different agents doing the same reasonable thing is
more likely wrong than they are. I had the evidence for this early — the workers' own reports said
they were excluding contents panels — and still spent a round strengthening the agent file instead
of testing the check.

### Same day: A2S crop padding, measured properly the second time

The first fix padded the bbox symmetrically by (24, 48) px. Running A2S at scale -- 123 real
transcriptions across twelve workers -- showed that was both too small and the wrong SHAPE, and the
reports were specific enough to fix it from evidence rather than guesswork.

**What the workers found, grouped by edge:**
  * LEFT, repeatedly: captions beginning mid-word -- `"gure 10.1"` (BIO12L-ch10-p004-b2),
    `"re 6.2"` (BIO11L-ch06-p003-b8), `"igure 10.1"` (BIO11L-ch10-p002-b6), and
    `"re 17.1"` (BIO11L-ch17-p003-b3, clipped at both sides). An NCERT caption line is typically
    wider than the artwork above it, so it starts left of the block's bbox. Fixed 24 -> 56.
  * BOTTOM, the largest group: the whole caption band falling outside the frame. Seven items in
    BIO12L ch01 alone (p005-b4, p007-b1, p010-b1, p011-b3, p012-b1, p014-b1, p016-b3); p011-b3
    reads `"Figure 1.10 A wind-pollinated plant showing compact inflorecence and well-"` and stops.
  * TOP, which the first fix had assumed was only about reagent labels: a TABLE TITLE lost
    entirely -- BIO12L-ch04-p014-b2 kept only the second line `"and Genes"` while
    `"Table 4.3: ..."` sat above the frame -- and in-figure labels sliced through horizontally
    (BIO12L-ch05-p004-b7, where `"transcription"`/`"translation"` survive as lower halves and one
    curved-arrow label is gone).

**So the padding is now asymmetric by kind**, because NCERT puts a table's title ABOVE it and a
figure's caption BELOW it: table 96 top / 56 bottom, figure 72 top / 96 bottom, equation and box
72/72, and 56 each side throughout. A single symmetric pad would have to be large on every edge to
catch either case, dragging in more of the neighbouring column than necessary.

**Why erring large is right, on the workers' own evidence.** The same reports describe
over-inclusion as "minor over-inclusion from padding, none lost content", and every worker
correctly excluded the intruding sliver and said so in `note` -- one even cross-checked an
illegible label against the same diagram printed legibly elsewhere in the chapter
(BIO12L-ch05-p001-b4 against Figure 5.6). A reader can ignore a fragment it can see; it cannot
recover a glyph that was never rendered.

The 22 items named as clipped are archived under `steps/A2S/out/_superseded_*_clipped_crop/` and
re-queued with the new frames. Items whose reports mentioned only neighbour bleed were left alone.

#### A process note: stating a fact in a brief that is not yet true about the inputs

A wave-2 worker reported that `BIO12L-ch02-p005-b4`'s caption was clipped at the left and added
that "the widened (56,48) padding is still insufficient here". That conclusion is wrong, and it is
my fault, not the worker's: its crop had been built in the EARLIER listing with the original 24 px
horizontal padding. It believed otherwise because my dispatch brief told it "Crops are padded
(56, 48) px" -- true of the code by then, but not of the crops that wave was actually working from,
which were never regenerated before dispatch.

Taken at face value this would have pushed the horizontal padding past 56 for no reason, on
evidence from a 24 px crop. The same mistake in kind as the booklet-code instruction earlier today:
a brief that asserts something about the data, stated with more confidence than the data warranted,
and an agent reasoning correctly from it to a wrong place.

Rule for next time: a brief may describe what the STEP does, but anything it asserts about the
specific inputs in that wave has to be true of those inputs -- so either re-list before dispatching
after changing input generation, or say nothing about it and let the worker report what it sees.
Re-crop first, then tell them what the frame is.

## 2026-10-13 · I handed the same work to two agents at once; now there is a ledger

An A2S worker reported, unprompted, "**Concurrency warning for the parent:** another agent is
writing this same group. It overwrote my outputs for `ch04-p003-b1`, `ch04-p003-b6`,
`ch04-p004-b1`, `ch04-p005-b3` ... Worth de-duplicating the group assignment." It was right.

My wave-building method was "take the listed items that have no output yet". That set is simply
WRONG while earlier agents are still running: an item being worked on has no output until its
agent finishes, so it looks available and gets handed out again. Measured across the real run:
**30 items were assigned twice** -- 18 between A2S waves 2 and 3, 12 between waves 1 and 3.

Not destructive, and worth saying so precisely: both agents transcribe the same crop, so the
loser's file is equivalent content and last-writer-wins leaves one valid output. The same worker
checked and said the duplicate differed only in whether labels were joined or split per line. The
cost was a second agent's budget spent on work already done, roughly 30 items' worth.

Fixed with `scripts/build_wave.py`, which keeps a ledger under `steps/<STEP>/work/_waves/`: every
wave it emits records the ids it handed out, and every later wave excludes both ids with output AND
ids named in any earlier wave. Verified on the live queue -- building the next A2S wave reported
"excluded 8 ids already assigned to an earlier wave", which are precisely the in-flight items that
would have been duplicated again. The ledger was back-filled from the three hand-built waves so
nothing already dispatched can be re-issued.

`--retry` deliberately re-offers assigned ids that still have no output, which is the only way an
id comes back. That matters on this project because agents here are killed mid-run routinely, so
"assigned" must not mean "stranded forever" -- the two failure modes (double-assign and
never-reassign) need different switches, not one guess.

Pattern worth noticing across today: three of the most useful findings came from workers reporting
something about their own *situation* rather than their task -- "another agent is writing this
group", "['OF'] looks suspiciously short for a sitting", and "the agent file's own example says
unsure, here is what to revisit if you are wrong". All three were correct and all three found
defects in the orchestration rather than in the data. Worth reading that kind of remark first.

### Same day, third iteration: stop guessing a pad, grow to the neighbouring block

Two more rounds of worker reports showed a fixed pad cannot work, however carefully chosen. A
caption may be one line or three: 96 px caught "Figure 1.10 A wind-pollinated plant ..." and still
lost line 2 of "Figure 1.11 (a) Pollination by water in Vallisneria; (b) ...". And after the
vertical fixes, the dominant remaining complaint moved to the LEFT edge -- "gure 17.1",
and labels reduced to their tail letters ("oles", "leus", "etric") on BIO12L-ch01-p005-b4.

The insight the reports kept pointing at: the bbox bounds the ARTWORK, the caption sits in the
white space around it, and the real boundary is not a distance at all -- it is wherever the next
block starts. So the crop now GROWS outward from the per-kind floor toward the nearest recorded
block in each direction, stopping `GAP` px short of it, capped by MAX_GROW (260). Neighbours are
only considered when they overlap this block's span on the relevant axis, which is what keeps it
safe on two-column pages: the other column has no overlap, so it neither limits the growth nor
gets pulled in.

One case needed a separate rule. Several figures have NO recorded block below them at all, because
their caption was never a block in the first place -- so neighbour-growth left them at the tight
floor and changed nothing (BIO12L-ch01-p012-b1 and ch04-p011-b1 measured +0 px). When A2 recorded
nothing in a direction, the only things that can be there are this block's own caption and white
paper, and pymupdf clips the rect at the page edge, so `OPEN_GROW` (200 px) reaches into it freely.
Measured after both rules: the six still-clipped ids now gain +200 px on their clipped edges, except
ch01-p005-b4 which gains +62 px to the left because a real neighbouring block sits there -- the
logic declining to swallow it, which is the intended behaviour, not a shortfall.

Worth recording as the lesson rather than the fix: I enlarged a magic number three times (24 -> 56
-> asymmetric-by-kind) before asking what the number was a proxy FOR. The data needed to compute
the answer properly -- every block's bbox on every page -- was already on disk the whole time.

## 2026-10-13 · Half the older NCERT corpus was invisible: A1 looked done and was not

Asked point-blank what remained for Stage A, the honest answer turned out to be worse than the one
I had been giving, and in a way no amount of running A2 would have fixed.

**Measured source corpus:** 4,298 NCERT pages across 186 chapter PDFs — 1,674 latest edition,
2,478 older. A2 had read 759, every one of them latest. **The older edition was at exactly 0%**,
not the "16%" or "nearly finished" I had reported in earlier sessions. Both of those were wrong in
the same direction.

**And only half the older edition was even reachable.** A1 (the book register) showed `pass: 9,
blocked: 0`, which I had read as finished. It was not: `run_step.py A1 --list` had **4 pending
items**, three of which were the Class 11 older books. S0 had found all 12 books correctly and the
manifest held all 186 files, but with no `BIO11O`/`CHE11O`/`PHY11O` row in `register/books.csv`,
A2's `_registered_books()` could not list a single one of their pages. 60 chapter PDFs and 1,228
pages were invisible to the pipeline — and because A2's queue still showed 1,250 older pages
(Class 12 alone), the number looked like partial progress rather than a missing-book problem.

Registering them took one agent and four items. A2's pending count went from ~1,790 to **3,275**,
which is the 1,228 pages appearing. All three print a bare `2022-23` with no word "Reprint".

**The lesson about how I measured, which is the part worth keeping:** `status.py --step A1` reports
items that HAVE a status. It says nothing about items that were never listed, so a step with
unlisted work reads as complete. "Nothing is flagged or blocked" is not the same as "nothing is
left", and for any step whose item set is derived from a register, the register is the thing to
check. The right question is always `--list | wc -l`, not the status counts.

**Consequence for the change log.** A5-A9 compare latest against older editions. With the older
half at 0% they have no items and cannot start at all — so the change log is not "behind", it is
not begun, and it is gated entirely on A2 reading 2,478 older pages. Any claim about removed or
moved NCERT chapters remains unsupported by this pipeline's own evidence until then, which is
exactly what CLAUDE.md's rule about never treating the analysis's chapter list as evidence is for.

## 2026-10-13 · The scraped "booklet sets" are reshuffles of one paper, and three years now show it

Independently reported by four B1 workers across different years, each from page evidence the
`text_layer` does not contain — these fragments survive only in the page IMAGES, which is why
earlier runs that trusted the text layer never saw them.

**2022.** Five files filed as codes R3, S2, S5, S6 and T4 each bleed an original-paper footer
through a solution block reading `- 14 - NEET (UG)-2022 (Code-Q1)` or `- 6 - ... (Code-Q1)`. The
same worker went further and checked the questions themselves: the same displacement-time-graph
question appears as question 1 in R3 and T4 and as question 2 in S2, with its options permuted, and
S5 and S6 share an identical question 1 and footer. Its conclusion, which the evidence supports:
the site built its 2022 "sets" by reshuffling one Code-Q1 original.

**2024.** Two more files, filed as Q3 and R2, each bleed `NEET (UG)-2024 (Code-Q1)`.

**2018.** Three files filed HH, XX and YY each bleed `ACHLA/AA/Page 6|13|14`, whose only code is AA;
a fourth worker saw the same `ACHLA/AA` footer under four claimed codes.

**Why this matters more than a provenance nicety.** It is the best explanation yet for a separate
measurement recorded above: **35 paper-code slots claimed by two different question_ids each, 70
question_ids involved, 17 of them with byte-identical stems.** If several scraped "sets" are one
booklet relabelled, then the same printed question legitimately arrives twice under different codes
— the duplication is in the SOURCE, and no amount of pipeline work will resolve it into two
distinct exam questions, because there was only ever one.

**What is now solid, and what is not.** Solid: where a page bleeds an original footer, that footer
is real page evidence and `trust: official` on the code it prints is correct even when it
contradicts the folder (recorded as `agrees_with_manifest: false`). Not solid: any 2018/2022/2024
booklet code that rests on a folder name alone. Those are `unsure` and should stay that way.

**Owner decision this raises, which I am not making unilaterally:** if the scraped per-code "sets"
for a year are one paper reshuffled, then treating them as distinct booklets inflates the bank with
duplicate questions wearing different codes, and C1's booklet-code de-duplication cannot catch it
because the codes genuinely differ. The options are (a) keep them and accept duplicates that look
like legitimate repeats, (b) collapse each year's scraped sets to the one code its footers attest,
or (c) drop the scraped sets for years where an official paper PDF exists. That is a scope call
about what the bank claims to contain, so it belongs to the owner, not to this pipeline.

## 2026-10-13 · B5: 6,396 key rows copied, and nothing yet can check them

Two B5 workers copied 28 official key pages between them (2020, 2021, 2024-T3, 2025-45), 6,396
question/answer rows in total. I tried to validate them the obvious way -- compare each copied row
against the `official_answer` already on a question record for the same (year, booklet code, qno) --
and got **zero comparable rows**. Those four years have no questions extracted yet, so there is
nothing in the bank to agree or disagree with.

Stating that plainly because the alternative is worse: these rows look authoritative, they will be
used to mark ~6,000 questions whenever those papers are extracted, and right now their only
assurance is that two careful agents said they read them correctly. The real check arrives when
B2/B3 extract those years, and it should be run then.

**On the one discrepancy in their reports, which turned out not to be one.** Worker 1 described the
layout as "column-major" (Q.No values run DOWN each Q.No/Answer column pair, so one printed line
reads 1, 31, 61, 91, 121, 151). Worker 2 described "row-wise pairing" (each question number is
printed immediately left of its own key on the same line). Those sound contradictory and are not:
the numbers advance down each column pair, AND every number is printed adjacent to its own answer.
Both workers independently drew the same conclusion from that -- because the pairing is explicit on
the page, no assumption about reading order can shift an answer, which is exactly the failure that
a bad brief nearly caused on this step earlier (a column-major claim that would have shifted ~200
answers by 40 places). Worker 2 spelled the risk out unprompted: treating the keys as one
continuous sequence read across the printed rows would shift every answer by a block, 30 places on
the 2020 pages and 50 on the 2021 ones.

Both reported complete contiguous coverage (1-180 or 1-200, no gaps, no unreadable cells) and
copied the three multiple-accepted cells verbatim ("1,3" / "1,2" / "1,2") rather than normalising
them. No bonus or dropped marks are printed on any of these 28 pages.

## 2026-10-13 · Scoping the older-edition read, and why pairing by chapter number does not work

Trying to find a cheaper path through Stage A than reading all 2,478 older pages, I proposed
reading only the older chapters that pair with an already-indexed latest chapter: 35 chapters,
899 pages. Then I checked the assumption that pairing rests on, and it fails.

**Measured chapter counts, both editions, all six books:**

| book | latest | older | delta |
|------|-------:|------:|------:|
| Biology 11   | 19 | 22 | +3 |
| Biology 12   | 13 | 16 | +3 |
| Chemistry 11 |  9 | 14 | +5 |
| Chemistry 12 | 10 | 16 | +6 |
| Physics 11   | 14 | 15 | +1 |
| Physics 12   | 14 | 15 | +1 |
| **total**    | **79** | **98** | **+19** |

The older editions carry **19 more chapters**. So chapters were genuinely dropped, and the moment
one is dropped every later chapter number shifts — "older ch N" stops meaning "latest ch N". My
899-page estimate silently assumed the opposite, and the thing it assumed is precisely what A5-A9
exists to establish. Recording the number anyway, clearly labelled, because the SHAPE of the saving
is real even though the pairing method is not: the change log only needs older chapters whose
latest counterpart is indexed, and that is a fraction of 98.

**What a sound scoping would need instead:** match chapters by TITLE or content, not number. The
titles are available asymmetrically today, which is its own small obstacle — older Class 11 files
carry them in the filename (`2 1. The Living World.pdf`) while every latest file is just
`Chapter_N.pdf` and older Class 12 is `Old_ncert_Bio_Chapter_N.pdf`. Latest titles do exist in
`ncert/chapters/<SUBJ><CLASS>.json`, but only for chapters A2/A3 have already indexed, which is the
circularity: the cheap path through Stage A needs information Stage A produces.

**Corroboration from the pages themselves**, which is the encouraging part: the older-edition
readers are already surfacing exactly the differences the change log must record, unprompted —
older §17.6 is "one short Asthma/Emphysema passage plus an inset ... much thinner than the latest
edition's treatment" (BIO11O ch17), and older §4.2 prints as "POPULATION STABILISATION AND BIRTH
CONTROL" in the body but "Population Explosion and Birth Control" in its own contents panel
(BIO12O ch04). Both copied as printed, nothing normalised.

**Where this leaves the decision.** Reading all 98 older chapters (2,478 pages) gives a complete,
evidence-backed change log. Reading a title-matched subset gives a change log that covers the
chapters the question bank actually cites, and the 19 removed chapters are findable cheaply from the
title lists alone once those exist. Either is defensible; the second needs the owner to accept that
the change log is scoped to cited chapters rather than exhaustive. CLAUDE.md's standing rule still
applies throughout: only Stage A's own change log counts as evidence about removed chapters, never
the analysis's list.

### Older-edition retries: slow and lossy, but NOT a hard limit (I called this wrong once)

After four rounds of re-dispatch, 42 pages across BIO11O ch02, ch10, ch12, ch14, ch16, ch19 and
ch20 still have no output. Every attempt died with `API Error: Output blocked by content filtering
policy`, most of them on the agent's FIRST turn, before any input file or page image had been read.

What was varied, and did not help: group size (1, 3, 7, 13 pages), chapter-whole vs non-contiguous
grouping, ordering (putting the stubborn pages first vs last), prompt length (full brief vs four
lines), explicit instruction to minimise narration, and mixing them with pages that succeed. The
same pages fail; neighbouring pages of the same chapters succeed.

What was ruled out by measurement rather than guess:
  * **Not the page content** — several agents died before opening any file, and the inputs
    themselves are ordinary NCERT prose (BIO11L-ch01-p003's text layer is 1,787 characters of
    "How wonderful is the living world !...").
  * **Not the subject** — an apparent Biology correlation was selection bias on my part: the
    per-subject completion rates I first quoted measured which chapters I CHOSE to dispatch, not
    which survived. Physics agents (PHY12L-ch11) have died the same way.
  * **Not concurrency** — failures occur at 1 concurrent agent and at 14, with no visible
    relationship.

Session rate for reference: roughly 1 in 3 A2 dispatches killed this way, worsening over the
session. Other steps are affected far less (B6 lost one agent to a separate stall watchdog).

**CORRECTION, written minutes after the paragraph above.** I concluded here that ~42 pages were
"not currently reachable" and said I was stopping. That was wrong on the count and wrong on the
conclusion. The wave I had just dispatched when I wrote it then delivered BIO11O ch12 (7 pages),
ch16 (3) and ch19 (5), and cut ch14 from 13 to 6. Measured immediately afterwards: of 153 older
pages ever assigned, **134 are done and 19 remain** -- BIO11O ch02 (7), ch10 (5), ch14 (6), ch20
(1). I declared a limit while the evidence against it was still in flight.

What that corrects, concretely: retrying is NOT futile, it is just lossy per attempt. Pages come
through on a later try with no change to the inputs. The one prompt change that coincided with the
improvement was telling agents to keep their own narration to "one short clause per page" -- several
kills had landed on commentary turns rather than file writes, so a smaller talking surface plausibly
means less exposure. That is a correlation from a handful of waves, not a measured effect, and I am
flagging it as a hypothesis rather than a finding.

The right operating rule is therefore: keep re-dispatching stranded pages in small chapter-sized
groups with minimal narration, and expect several passes. Their ids are always recoverable as
`steps/A2/work/_waves/*.json` minus the outputs on disk.

### The same double-assignment mistake, made a second time — by me, bypassing my own fix

An A2 worker reported: "`steps/A2/out/BIO11O-ch16-p011.runA.json` was overwritten on disk by
another writer after I wrote it — same blocks and flags, only a 6px bbox difference and a different
`note`; I left their version in place."

I had claimed earlier today that `scripts/build_wave.py`'s ledger fixed double-assignment. The
ledger works. I went around it: to re-dispatch work stranded by killed agents I computed
`assigned - has_output` by hand and sent those out directly. That set is wrong for the identical
reason the original bug was wrong — **an agent that is still running has not written its output
yet, so its items look stranded.** My older-wave 3 was still in flight when I built wave 4 from
"stranded" items, and the overlap went out twice.

So the lesson from the first occurrence was recorded and then not applied, because I treated the
retry path as a special case exempt from it. It is not: "has no output" never means "nobody is
working on it", whichever way the list is built.

**What is actually needed**, and is NOT yet implemented: the retry path has to distinguish an item
assigned to a DEAD agent from one assigned to a RUNNING agent, and disk state alone cannot tell
them apart. A workable rule is to stamp each wave with a dispatch time and only re-offer items from
waves older than some quiet period with no new output appearing — `build_wave.py` already writes a
timestamped wave file, so the data is there, but `--retry` currently ignores it and re-offers every
assigned-and-unfinished id. Until that is fixed, hand-built retries should be dispatched only after
confirming the earlier wave's agents have all reported.

Damage was again minimal and for the same reason as before -- two agents reading the same page
produce the same blocks, so last-writer-wins leaves a valid file and the loser's work is equivalent
(this worker checked: a 6px bbox difference). The cost is a wasted agent, not a corrupt record. But
the honest summary is that I made the same class of error twice in one session, the second time
after writing down why it happens.

## 2026-10-13 · Working the flag backlog: what was noise, what was stale, what was one defect

Asked to resolve the flagged items, I audited all of them rather than starting to fix. Three things
came out, in descending size.

### 1. More than half the flag store was duplicate rows (1,253 of 2,371)

`lib.flags.raise_flag` appended unconditionally, so every re-run of a step re-raised the same flag.
2,371 rows represented **1,114 distinct conditions**; one had been raised **eleven times** (each B5
run re-flagged `NEET-2017-MAIN-W-key` for the same missing booklet code). The duplicates were
byte-identical apart from `flag_id` and `created_at`.

Two real harms, which is why this is code and not a reviewer's problem: spec 14/F1 builds the
reviewer's queue from open flags, so a person would have been handed 2,371 items for 1,114 real
decisions; and `open_flags` is a column of `review/releases.csv`, so the release gate was counting
noise.

`raise_flag` is now idempotent per `(item_type, item_id, step, code)` while a flag is open, pinned
by `tests/test_flag_dedup.py` (7 tests). Deliberately keyed on OPEN flags only: if a reviewer closes
a flag and the condition recurs, that is new information and must be raised again. The live store
was compacted to 1,118 rows, original preserved at `flags/flags.jsonl.*.pre-dedup`. Four conditions
keep two rows each because `review/queue.csv` already points at both siblings, and breaking a queue
reference would be worse than the duplicate -- my first compaction pass silently dropped those four
and I redid it.

### 2. Twenty-three flags are factually stale, and nothing was re-checking them

A flag records a condition at a moment; steps then re-run and some conditions stop being true, but
nothing re-tests them. `scripts/audit_flags.py` now re-tests every open flag's premise against
current data. Verified stale: **9 `A2_UNREADABLE`** (every one of those pages has since been read),
**9 `A2_SPECIAL_UNREAD`**, **4 `A3_SECTION_SPANS_UNREAD_PAGE`**, **1 `B5_KEY_ROW_MISSING`**.
`review/queue.csv`'s very first row is one of them -- `FL-000180`, "page could not be read" for
`BIO11L-ch01-p003`, a page now on disk.

**The script never closes a flag, by design.** Spec 14/F3 makes closing a reviewer's act recorded
in `review/decisions.csv` with a named reviewer, and CLAUDE.md says people review only at Stage F.
Writing those rows myself would forge the sign-off the review gate exists to require. So
`--draft-decisions` writes `review/decisions.DRAFT.csv` with `reviewer` left EMPTY -- it cannot be
applied as-is; a person puts their name on the rows they accept, renames it, and runs
`apply_review.py --apply`.

Also reported honestly: 79 flags are **still true** (61 `B5_KEY_ROW_MISSING` where the register
genuinely has no booklet code, 18 `S0_MISSING_INPUT`), and 1,016 need a person.

### 3. Of 1,016 "needs a human", 61 were one bookkeeping defect

Sampling the big classes showed most are working as designed -- `B1_REGISTER_DRAFT` (211) and
`A1_REGISTER_DRAFT` (12) are drafts awaiting approval by definition; `B4_MISMATCH_ADJUDICATED`
(179) and `A2_JOIN_ADJUDICATED` (68) record adjudications for review; `B6_DISAGREES_WITH_KEY` (54)
is the entire point of the blind solve; `B1_MANIFEST_MISMATCH` (110) is the honest consequence of
scraped papers that never print their code.

But `B1_CHECK_FAILED` (167) hid a real one: **58 of its 61 schema failures were a single mistake.**
`cover_text_exact` is declared `additionalProperties: false` with exactly `code` and `date`, and
agents kept adding sensibly-named extra keys to record other printed page text -- `site_chrome`,
`breadcrumb`, `kicker`, `subtitle`, `issuer`, `title`, `footnote`, `disclaimer`, `heading`,
`footer`, `page2_header`, `second_page_code`, `bleed_through_fragment`. The schema then rejected the
whole output, throwing away otherwise sound verdicts over where the extra observations were parked.

Not a schema problem: the field is deliberately narrow, and `note` is free text and exactly the
right home. The agent file now says so with the measurement attached, and all 61 invalid outputs are
archived and re-queued.

**Left alone deliberately:** three AIPMT outputs rejected for `year` below the schema's minimum of
2012 (`AIPMT-2010-Preliminary`, `AIPMT-2011-Main`, `AIPMT-2011-Preliminary`). The schema says this
bank covers 2012-2026 and those papers predate it, so whether they are in scope is an owner's
decision about what the bank claims to contain -- not a defect to re-run, and not mine to widen.

### Correction: the duplicate-option questions are NOT lost notation, and I asserted otherwise

I recorded earlier, and repeated to the owner, that `Q-000111`'s option 4 "is printed **1 : √2**"
and that the PDF text layer had dropped the radical. That was an INFERENCE from the physics -- if
the tension doubles, the speed ratio is 1:√2, so I reasoned the printed option must say so -- and I
stated it as an observation.

All nine duplicate-option questions were re-read with an explicit instruction to magnify the option
region and report which of two situations they found: notation lost from the text layer
(recoverable) or a genuine source defect (copy as printed). Seven have returned and **every one
confirms a genuine duplicate**, each verified by cropping the individual option regions and
magnifying 6-8x:

  * `NEET-2023-MAIN-E1-q0055` / `E2-q0060`: options 1 and 4 both read "34 cm^-1"
  * `NEET-2023-MAIN-E1-q0008` / `E2-q0011`: options 2 and 3 both read "7 A"
  * `NEET-2022-MAIN-Q1-q0011`: option 3 renders "1: 2", option 4 "1 : 2" -- differing only in
    horizontal spacing. **No radical is present on the image at all.**
  * `NEET-2024-MAIN-Q1-q0001` and `-q0014`: options 3 and 4 are both a bare letter "B"
  * `NEET-2022-MAIN-Q1-q0047`: TWO identical pairs -- 1 and 4 both "5 x 10-6 J", 2 and 3 both
    "25 x 10-6 J"
  * `NEET-2022-MAIN-Q1-q0083`: options 2, 3 AND 4 all read a bare "57"

What this does and does not establish, stated carefully because the distinction is the whole point:
the duplicates are genuine **in our source material**, not necessarily in the real NEET paper. These
are scraped renderings, and the scrape may well have destroyed the radicals and exponents before
the image was ever made -- `q0083`'s three identical "57"s and `q0001`'s bare "B"s are obviously not
what NTA printed. So the questions are unusable as they stand, and the remedy is **better source
material** (an official paper PDF), not another transcription pass. No amount of re-reading an image
can recover a character the image does not contain, and the agents were right to refuse to invent
one.

The lesson on my side is the specific one: I had a correct piece of physics and let it stand in for
a reading of the page. "The option must say 1:√2 for the question to work" is a reason to go and
LOOK, not a finding. The agents' discipline here was better than mine -- one of them had already
told me at 4x zoom that `E1-q0011`'s two "7 A" options carried no radical, exponent, decimal or unit
prefix, and I kept the √2 claim in my reporting anyway.

### The nine duplicate-option items are six questions, but not for the reason the worker gave

The re-read worker closed its report with "four of the nine are also duplicate scrapes of each
other", naming `E1-q0055`/`E2-q0060`, `E1-q0008`/`E2-q0011` and `2024 q0001`/`q0014`. The content
identity is real -- I confirmed all three pairs -- but the worker put two different things in one
basket, and only one of them is a defect.

`E1` and `E2` are two **booklet codes of the same 2023 paper**. NTA builds codes by shuffling one
question set into different orders, so the same question appearing as q0008 in E1 and q0011 in E2 is
exactly what a faithful extraction should produce. It is not a scrape defect. `2024 q0001` and
`q0014` sit in the **same booklet**, where a question cannot appear twice -- that one is a defect.

Measured properly across all 700 extracted questions, keying on stem + `list_i`/`list_ii`/
`statements` + all four options:

  * **1** true same-content-twice-in-one-booklet: `NEET-2024-MAIN-Q1 q0001`/`q0014`
  * **66** cross-booklet content matches, all between 2023 E1 and E2

My first attempt keyed on `stem_en` alone and reported **15** intra-booklet duplicates. Fourteen
were false positives of my own making: assertion-reason and match-the-list questions carry a stem
that is pure boilerplate ("Match List I with List II...") and hold every discriminating word in
`list_i`, `list_ii` and `statements`, exactly as `schemas/B3.json` intends. Seventeen questions in
2024-Q1 share one byte-identical match-list stem and are seventeen completely different questions.
This is the same mistake as the ink-band clipping measurement: an instrument that was easy to build
rather than one that measured the thing, and it inflated the count by 15x before I checked a single
record by hand.

The 66 cross-booklet matches are worth keeping as an **asset, not a finding**. Two independent
extraction runs over two differently-ordered scans produced byte-identical content for 66 question
pairs. Nothing in the pipeline asked for that agreement, so it is free corroboration that B3's
transcription is reproducible, and it is a ready-made seed for Stage C's repeat groups. It also
gives a cheap future regression test: if a B3 change breaks transcription stability, these 66 pairs
stop matching.

### I built a parallel question taxonomy without checking whether one already existed

Asked for a category sheet of question types and traps, I mined `steps/B3/out/` and invented 15
categories (C01-C15) with my own trap descriptions, wrote three scripts, two CSVs, an xlsx and an
artifact page. `exports/discovery/CATEGORIES.xlsx` already held a far better one, and had since
2026-10-13 11:21 -- hours before I started.

What already existed, and what mine was next to it:

  * **five axes, not one.** E1 question_type "How is the question BUILT?", E2 format "What must the
    student PICK?", E3 content_shape "What NCERT MATERIAL is it built on?", E4 thinking "What must
    the student do IN THEIR HEAD?", E5 trap "Why does each WRONG OPTION attract?". I had collapsed
    all five into one axis, which is why my sheet could not say anything about a question that its
    category did not already say.
  * **86 categories** across those axes (18/16/18/13/21) against my 15, each with a definition, a
    `decision` (new / renamed / merged), a `was`, a `why_this_name`, counts by subject AND by
    chemistry branch, `not_to_be_confused_with`, `both_passes_agree`, and `evidence`.
  * **580 questions already tagged**, with `question_ids` on every category -- so the per-question
    assignment existed too. E5 is explicitly multi-valued because it runs once per wrong option.
  * **two independent discovery passes** with their disagreements recorded, plus open decisions
    stated as open (E2 wants a 16th value; E3's `example_list` wants two more words).

The cost was not just wasted work. My taxonomy would have become a second, worse vocabulary for the
same questions, and the project already has a rule about exactly this -- only Stage A's change log
counts as evidence, precisely so two parallel accounts of the same thing cannot both be cited.

What I should have done before writing a line: searched for the artefact. One `find . -iname
"*categor*"` would have found it. I went to `steps/B3/out/` because that is where I had been working
all session, and mistook "where I was" for "where the answer is". The user found it, not me, and
only after I had shipped the wrong thing twice.

`scripts/export_discovery_questions.py` now writes `exports/discovery/QUESTIONS.xlsx` -- the
per-question companion to CATEGORIES.xlsx, inverting the existing `question_ids` rather than
classifying anything. `docs/question_categories/` is SUPERSEDED and kept only so this note has
something to point at; nothing should be built on it.

One real gap remains in the existing work: the per-question `why` text exists for only **240 of
2,900** cells (580 questions x 5 axes), because those reasons were written as category
ILLUSTRATIONS, not per-question evidence. Empty cells are tinted and left blank in the workbook.
Filling them with the category definition would read as per-question evidence while carrying none,
so that is agent work against each question, not a copy.

### Why question content is "missing": 189 of 201 registered papers are website prints, not papers

Traced from one cell the owner spotted -- `Q-000353`'s List I reading
`(A) [missing content — no text printed]` four times over.

What that question is: NEET 2024 Q1 q75, Chemistry, a Match List I/II where **List I is four drawn
reaction schemes**. Chain of evidence, each step checked rather than assumed:

  1. We DO hold an image: `papers/questions/NEET-2024-MAIN-Q1/75.png`, 50 KB, and it renders. So
     "no image" was the wrong hypothesis.
  2. The image does not contain the content. The scraped site flattened the whole match table into
     one run-on line -- `A. I. B. II. CrO3 C. III. KMnO4/KOH, Δ D. IV. (i) O3 (ii) Zn-H2O` -- and
     never drew the four List I structures at all. The B3 reader said exactly this in its note and
     wrote the placeholder instead of inventing four reactions. It was right to.
  3. The PDF we treat as the source paper is **not a paper**. `neet_2024_code-Q1.pdf` has
     `Creator: Chromium`, `Producer: Skia/PDF m153`, `Title: ... | neet.training`, created
     2026-10-08. It is a browser print of the same website, so it carries the identical hole:
     **0 embedded images** on the page holding q75, and the 35 "drawings" are option pills.

That third point is not about one question. Across `register/papers.csv`, **189 of 201 registered
question papers are Chromium/Skia prints** of the scrape, including every paper the 580 analysed
questions come from (2022 Q1, 2023 E1/E2, 2024 Q1). For those papers, anything the website did not
render -- reaction structures, graphs, circuits, image options -- is not recoverable from the file
we are calling the source. This is the same root cause as the 15 `(Image option - will be added
soon)` questions, as `Q-000509`/`Q-000520` that E3 could not place, and as the 23 questions whose
stem names a figure while `has_figure` is false.

**The content is recoverable, from a different file.** 12 registered papers are NOT scrape prints,
and one is the same exam year: `NEET-2024-MAIN-T3` = `NEET_PYQ/Paper/2024.pdf`, 28 pages, 86
embedded images, genuine booklet layout ("Test Booklet Code / GENERAL INSTRUCTION / The test is of
3 hours 20 minutes"). Booklet codes are shuffles of ONE question set, so Q1's q75 is in it -- as
**q67**, with identical List II (`Anhyd.AlCl3`, `CrO3`, `KMnO4/KOH Δ`, `(i) O3 (ii) Zn-H2O`), the
option permutations reordered as a different code should, and all four List I structures intact and
legible at 170 dpi: cyclohexylidene-cyclohexane to 2 cyclohexanone, benzene to benzophenone,
cyclohexanol to cyclohexanone, ethylbenzene to benzoic acid. Q1's answer 3 ("A-IV, B-I, C-II,
D-III") is T3's option 1, which is the consistency check passing.

**Two decisions for the owner, because both are rule questions and not mine.**

  1. `2024.pdf` carries a **Physics Wallah watermark**. CLAUDE.md forbids passing coaching material
     to B6 and D7. Recovering question content from it is a different use than solving, but it is
     still coaching material entering the corpus, and the register's `trust` for these needs to say
     so. I have not used it for anything.
  2. Whether the 189 scrape-print papers should keep `file_kind: paper`. They are faithful for text
     and systematically blind to drawn content, and nothing in the register currently records that
     distinction -- so a reader cannot tell a real paper from a print of a website.

The cross-booklet recovery route is cheap and already proven here: the 66 content matches measured
earlier between 2023 E1 and E2 are the same mechanism, and it means a scrape-print question with
missing drawings can often be repaired from a non-scrape paper of the same year.

### The legacy-sheet figures are real, but their OPTION NUMBERING does not transfer. Do not attach them blind.

Following the owner's reminder that the legacy sheets were agreed as the fallback when the scrape
lost an image, I tested the route end to end on one question and it fails in a way worth stating
before anything is wired in.

**The good half, verified.** `Q-000343` ("Which plot of ln k vs 1/T is consistent with Arrhenius
equation?") has all four options recorded as `(Image option - will be added soon)`. Row 74 of
`inputs/legacy_sheets/NEET-UG_pyq_2024.xlsx` is the same question, carries
`![](https://cdn.mathpix.com/snip/images/ZjfWne5_...png)`, and that URL is **live** (HTTP 200,
28 KB, 659x429 PNG). It contains exactly the four plots, and they match the independent render from
`NEET_PYQ/Paper/2024.pdf` (T3 q73) plot for plot. The sheet ALSO carries better LaTeX than our
record: `$\frac{1}{T}$` where ours has the mangled `$1\ T$`. Two independent sources agreeing is as
good as the evidence gets. Of the 2024 sheet's 30 figure rows, several are exactly the questions
already logged as broken: row 100 is `Q-000509`, row 90 is `Q-000520`, row 40 is `q0042`'s bridge
circuit, row 48 is `q0047`'s velocity-time plot.

**The half that breaks it.** The image carries its own printed `(1) (2) (3) (4)` labels, and those
labels are the labels of whichever booklet the snip came from. For this question:

  * Physics is not in doubt: `ln k = ln A - (Ea/R)(1/T)`, so the line has NEGATIVE slope and a
    positive intercept. In the image that is plot **(2)**.
  * The official NTA key for `NEET-2024-MAIN-Q1` q66 says **4**.
  * The legacy sheet's own `Answer` column says **C**, and its own option list is `a) (1) b) (2)
    c) (3) d) (4)`, so it claims **(3)** - an increasing line, which is simply wrong.

Booklet codes shuffle option order as well as question order, `option_map` on this record is
`null`, and Q-000343's own option images were never rendered, so **there is no way from this
material to learn which plot Q1 printed as its option 4.** Attaching the image as-is would create a
question whose picture makes (2) correct while its stored answer says 4: a silent contradiction,
strictly worse than the honest placeholder it replaced. The sheet's `Answer` column cannot be used
to reconcile the order either, since it disagrees with the image it ships with - which is the same
unreliability SPEC Section 2 already documents (367 rule-based contradictions in the legacy
"Question Type" column alone).

**What this changes.** The figure route is still worth having, but it is NOT "attach the image to
the question". It is two separate jobs with different risk:

  1. **Safe now:** attach the image as *supporting evidence* on the record (a figure a reviewer can
     see) and import the sheet's LaTeX for stems, without touching `options_en` or
     `official_answer`. This fixes the unreadable-stem defect and gives a reviewer the picture.
  2. **Needs a decision, and possibly is impossible:** making the four pictures into the four
     OPTIONS of a specific booklet code. That requires knowing that code's option order, which for
     a scrape-print paper does not exist in anything we hold. The realistic resolutions are to
     re-point such questions at the booklet code whose paper we actually have with images (T3 for
     2024), or to accept them as figure-illustrated but option-unresolved and let Stage F decide.

Also to fix regardless: images must be **downloaded to `papers/figures/<QID>.png`** with the URL
kept only as provenance. They are on a third-party CDN outside the project's control, and SPEC
line 141 already says never to depend on such a URL. I downloaded one to a scratch path for this
test and have not written anything into the project.

### Correction: `legacy_match.py` IS built — the 2026-10-12 note above is stale

The entry of 2026-10-12 lists among its engineering caveats that "joining is not solved — sheet
rows must be matched to real bank questions, which is exactly what spec Section 13's
`legacy_match.py` describes ... and **that script is not built yet**". That was true when written
and is not true now. `scripts/legacy_match.py` exists: 454 lines, with `match_one`,
`canonical_records`, `sheet_paths_for`, `store`, an `assert_no_legacy` guard and a `_self_test`.

Leaving the caveat uncorrected matters more than it looks: it is the stated reason the figure route
was "not actioned", and a reader deciding whether to approve that route would weigh a missing
joiner heavily. The join is in fact implemented and B9 has used it to recover 57 figures.

A full position statement now lives in `docs/WHATS_LEFT.md`, measured 2026-10-13.

### The A3 agent file promised its input was page-joined. It is not, and four workers caught it.

`.claude/agents/a3-passage-splitter.md` described its input as "numbered blocks (n, kind, text) in
reading order, **already joined across page breaks**". Four A3 workers running independently on
2026-10-13 each reported the opposite, unprompted, and one said so in as many words: "the inputs are
**not** reliably joined across page breaks, despite the agent spec's claim ... whatever produces the
A2/A3 work files may have an unjoined-paragraph bug worth checking upstream."

Named instances, from four different workers: `BIO11O-ch12-s12` (blocks 2/3), `ch12-s13` (2/3),
`ch12-s15` (4/5), `ch12-s16` (2/3), `ch18-s12` (3/5), `ch18-s13` (2/3), `BIO11O-ch17-s05` (2/3),
`ch17-s10` (2/3), `BIO11L-ch12-s11` (3/4), `ch04-s07` (2/3), `ch04-s12` (2/7), `ch04-s16` (2/4),
`ch13-s04` (2/3), `ch13-s15` (2/3), `ch13-s17` (2/3), `ch15-s09`, `ch15-s10`, `ch15-s11`.

This is the same class of defect as telling A2S agents their crops were (56,48) when the crops were
24px: **a brief asserting something about its input that is not true of the input.** It is worse
here than it looks, because the false promise invites exactly the wrong behaviour — an agent that
believes joining is done has no reason to look for a mid-sentence break, and would cut a paragraph
in half at a page boundary. Every passage so cut is broken evidence for D4's quoting and for Stage E.
The four workers all joined the fragments anyway, on their own judgement, which is why no damage was
done.

**Fixed in the brief**, which now says plainly that blocks are not reliably joined, that the agent
must decide, and that a section whose paragraphs were all page-split will legitimately produce few
passages. It also distinguishes the second case the workers found: a fragment whose other half is
not in the section at all (`BIO11L-ch04-s17` block 2 ends at "The skin of" with no continuation;
`BIO11L-ch13-s02` block 6 begins mid-sentence with no opener) — that is a sectioning gap upstream,
to be kept and noted, never invented.

**Not fixed: the underlying cause.** Whatever assembles A3's work files should be joining these, or
the promise should never have been made. Worth deciding which, because 735 A3 outputs now exist and
the ones produced before this correction relied on each worker noticing.

Two things I got wrong while chasing this, recorded so the reasoning is not repeated:
  * A worker reported `BIO11O-ch12-s06` jumping from page 003 to page 006, and I checked for
    `steps/A2/status/BIO11O-ch12-p004.json`, found nothing, and concluded the pages were read but
    unresolved. **Wrong** - I guessed the status filename. A2 has 1,047 outputs and 1,047 status
    files, none missing.
  * I then assumed it must be an `A3_SECTION_SPANS_UNREAD_PAGE` case. **Also wrong** - there are 4
    such flags and none of them is `ch12-s06`. The section legitimately skips pages whose blocks
    belong to other sections; what is real there is only the mid-sentence break.

### Stage A push, 2026-10-13: the chapter-title bug, and three A2 extraction defects the workers found

Driving Stage A to completion. Progress this session: A3 **615 -> 807** outputs, A2S **352 -> 477**,
A4 **45 -> 75** (all 15 chapters now have both runs; 2 went to adjudication because run A and run B
disagreed, which is the two-run design working). 242 tests pass.

#### Fixed: the chapter title was being taken from "SUMMARY"

`A3Plugin._chapters()` sets a chapter's title to the first `title_candidate` heading in ordinal
order, assuming the chapter's own banner is always ordinal 1. That holds only once the banner page
has been READ. While A2 is part-way through a book the banner is simply absent, so the first
unnumbered heading A2 did reach won — and **11 of the 15 A4 work inputs carried
`chapter_title: "SUMMARY"`, one carried `"EXERCISES"`.** Four A4 workers reported it independently,
across both runs, unprompted.

Worth noting the near miss: the comment above `_BANNER_NUMBER` already warned "the chapter title
feeds A4's `chapter_title` input and D1, so a wrong one propagates", and an earlier fix had added an
explicit `(page, n)` sort for exactly this symptom. That sort fixed the ORDERING half (file append
order is not page order). It cannot fix the case where the banner does not exist yet, which is why
the bug survived and looked fixed.

`_classify_heading` now returns a new `"structural"` kind for a stop-list of headings that name a
part of EVERY chapter (SUMMARY, EXERCISES, NOTE, GLOSSARY, APPENDIX, ANSWERS, REFERENCES, FURTHER
READING, ACTIVITY, OBJECTIVES, ...). They stay real section headings and still cut sections; they
are merely barred from title candidacy. Verified after the fix: **0 suspect titles**, BIO12 reads
correctly ("SEXUAL REPRODUCTION IN FLOWERING PLANTS", "HUMAN REPRODUCTION", "EVOLUTION"), and the
BIO11 chapters whose banner is still unread now hold `""` instead of `"SUMMARY"`. **Empty is the
right answer**: it is visibly missing and can be flagged, where "SUMMARY" propagates silently into
A4 and D1. The already-built A4 inputs still carry the old value and would need rebuilding.

#### Three extraction defects, each found by a worker reading real pages

1. **Duplicate extraction, `BIO11O-ch14` page 009.** In `ch14-s11` blocks 3, 5 and 7 are verbatim
   duplicates of blocks 2, 4 and 6 — the whole page-009 column appears extracted twice; `ch14-s09`
   block 8 duplicates block 7, same page. The worker could not drop them (no block may be dropped),
   so it formed passages from the first rendering and left the duplicates as their own passages with
   a note. Worth looking at A2's output for that page.
2. **A heading sectioned twice.** `BIO11O-ch14-s10` is heading-only ("14.5 THE RESPIRATORY BALANCE
   SHEET", no body) while `ch14-s11` carries the same heading PLUS the body.
3. **Foreign content inside a chapter.** `BIO11L-CH14-P02` is a biography box about Alfonso Corti
   and the mammalian AUDITORY system, sitting in the respiration chapter. Reported independently by
   both A4 runs. A2S separately transcribed `BIO11O-ch16-p002-b1` as a margin portrait of the same
   Alfonso Corti, so the box is real print, not an extraction invention — but its placement needs
   checking.

Also reported repeatedly and not yet acted on: **A4 inputs contain duplicate passages** (CH01 six
exact pairs P10=P32..P15=P37; CH03 nine pairs) and **passage-id gaps** (CH01 starts at P10; CH02
missing P27-P32, so Kingdom Fungi's introduction has no passage; CH03 missing P01-P05 and P10-P12,
leaving three listed headings with no passages at all). Both runs found these independently.

#### My own operational mistake
Several agents reported that their scratchpad validator scripts were being overwritten mid-run by
other agents, because I gave every parallel agent the same session scratchpad directory. No project
file was affected and each agent worked around it, but briefs that tell agents to write scratch
files must give them distinct paths.

### A2 at scale: the 600s stall is predictable, and write-each-page-immediately is what makes it survivable

Driving A2 on 2026-10-13. Eight chapter agents were dispatched in two waves; **all eight were killed
by the platform's 600s stall watchdog**, and the model safety classifier timed out twice in between.
None completed its chapter. And yet A2 went **1,116 -> 1,273 pages (+157)** plus 4 retries fixed,
because every brief said to write each page's output file immediately rather than batching.

The measured pattern, which is the useful part: an agent reliably finishes **10-16 pages** and then
stalls. Wave 1 produced 22/31/32/17 pages on chapters of 47/58/50/47; wave 2 added 16/13/12/9 to the
same four. That is consistent enough not to be random platform flakiness - reading a page image is
slow, and a long quiet stretch in the output stream is exactly what the watchdog kills. One agent
spent part of its window writing a validator to run the real check code, which is expensive and was
never asked for.

**Operational conclusions, for whoever drives A2 next:**
  * batch **~10 pages per agent**, not a whole chapter. A 58-page chapter is 5-6 agents, not one.
    The sequential-dependency argument for whole-chapter grouping is real but weaker than it looks:
    the continuation field is only filled after a page is CHECKED anyway, so an agent mid-chapter is
    already relying on its own previous output, and a resuming agent can read the previous page's
    output file just as easily.
  * every brief MUST say write-immediately, and say why. Had these eight batched their writes, all
    157 pages would be gone.
  * a resumed chapter needs the previous page's output path given to it explicitly, so its first
    page has real continuation evidence.
  * do not tell an agent to "validate against the schema" without saying how; several burned
    minutes hand-writing validators because `jsonschema` is not importable in their environment.

**The 4 retries were all `A2_TEXT_MISMATCH`, and all on mathematics** - the check wants >=95% of
block prose words present in order in the page's `text_layer`, >=70% per block, every number
present. Failures were subscript/exponent normalisation: `'N2=3.0 x 10-3M'` at 66.7%,
`'n/(r12 dOmega)'` at 69.2% with the numbers `12` and `22` absent from the text layer entirely. All
four passed on retry once the brief said to follow the text layer's own spelling of maths and to
mark genuinely displayed expressions `needs_special` instead of transcribing them. That check is
earning its keep.

### Some A2 "chapter" page ranges contain the book's BACK MATTER, not chapter content

Found by the worker reading `PHY12O-ch14` p045-p054. All ten of those pages are the book's back
matter -- printed pages 512-522: **p045-p049 the ANSWERS section** (tails of chapters 11-14's answer
lists), **p050-p051 the BIBLIOGRAPHY**, **p052-p054 the INDEX**. None of it is chapter-14 text.

The worker handled it exactly right and said so loudly in every `note`: `p049` carries the answer
key **for this very chapter** ("CHAPTER 14", answers 14.1-14.15), and it refused to let that stand
as chapter-14 passage text while still recording blocks (the schema rejects an empty page, and
recording them lets page-coverage see the text was accounted for deliberately rather than dropped).

Why this is not simply "the last chapter picks up the tail": **`PHY12O-ch14` is not the last
chapter** -- `PHY12O-ch15` exists with 19 pages. But ch14 carries **58 pages against the book's
35.5-page median**, the largest in the book. So the chapter split put the book's tail inside ch14,
and ch15 is a separate real chapter. `register/books.csv` shows PHY12O registered from a single file
(`older__..._Old_ncert_Physics_Chapter_1`) with an empty `part_ranges`, which is the likely origin.

**Why it matters beyond one chapter.** The A2 queue is ~2,830 pages. If other chapters' ranges
likewise absorb answer sections, bibliographies and indexes, some unknown fraction of that queue is
not chapter content at all, and reading it produces passages that D4 could later quote as NCERT
evidence when they are really an answer key or an index entry. A scan of last-chapter-vs-median page
counts found no other book whose LAST chapter is oversized, so this is not a simple systematic
pattern -- it needs checking per book against the real chapter boundaries, which is an A1 question
(`part_ranges`), not an A2 one.

**Not fixed.** Nothing was changed: the pages are read, recorded, and flagged in their notes. The
decisions are the owner's -- whether to re-split PHY12O's chapter ranges, and whether back-matter
pages should be excluded from A2's item space entirely rather than read and annotated.

Two smaller text-layer defects from the same waves, both preserved rather than silently repaired:
  * `CHE11L-ch06` p043 exercise 6.20 is missing its second partial pressure in the text layer
    entirely -- it reads `pCO= 1.4 atm and  = 0.80 atm?` -- and p045 exercise 6.35 gives the
    carbonate ion as the bare fragment `CO  `. Left as gaps, marked `needs_special`.
  * `PHY12O-ch14` p051's text layer carries a stale `"Answers"` running header although the printed
    header is `Bibliography`; both were listed as removed furniture.

#### Update: `PHY12O-ch14`'s back matter is 14 pages, and its printed page order is not monotonic

Finishing the chapter (p055-p058) extended the earlier finding. The whole stretch **p045-p058 — 14
of the chapter's 58 pages, 24% of it — is book back matter with no chapter-14 content at all**:

  * p045-p049  ANSWERS            (printed 513-517)
  * p050-p051  BIBLIOGRAPHY       (printed 518-519)
  * p052-p056  INDEX              (printed 520-524)
  * p057-p058  APPENDICES A1-A3   (printed **500-501**)

Two new facts from that:

1. **The file's printed-page order is not monotonic.** The index runs to printed 524 and the file
   then jumps BACKWARDS to printed 500-501 for the appendices, which are bound in after the index.
   Any downstream logic assuming printed page numbers rise with file page index will mis-order these
   two pages. Worth knowing before anything sorts NCERT evidence by printed page.
2. **`p058`'s text layer emits a phantom `Answers`** between the page number and `Appendices` — a
   leftover of the back-matter banner template that appears nowhere on the page. Listed in
   `running_header_footer_removed` so coverage sees it handled deliberately. This is the second such
   phantom in this chapter (p051's layer carried a stale `Answers` where the printed header reads
   `Bibliography`), so the book's text layer has a systematic banner-template artefact in its back
   matter, not a one-off.

Both workers wrote `BOOK BACK MATTER, NOT CHAPTER 14 CONTENT` at the head of every affected `note`
with an explicit must-not-be-used-as-passage-text warning, and recorded blocks rather than returning
empty pages. That is the right shape: the text is accounted for, visibly, instead of silently
dropped — but it does mean 14 pages of this chapter's A2 "coverage" is coverage of an index.

The scale question stands and is now sharper: if 24% of one chapter's range is back matter, the
~2,780-page A2 queue contains an unknown but non-trivial number of pages that are not chapter
content. Checking it is an A1 `part_ranges` question per book, and the owner's call.

### The real mechanism behind A2's maths failures: `_numbers()` folds exponents, so the honest spellings all fail

A CHE12O-ch07 worker read `scripts/checks/A2.py` rather than guessing at it, and found the thing that
explains every `A2_TEXT_MISMATCH` seen today. Recording it because the fix is counter-intuitive and
the next person will otherwise rediscover it the slow way.

**1. `_numbers()` folds a script or LaTeX exponent into the digits before it, then compares.** On
`CHE12O-ch07-p007` the page prints `200 × 10⁵ Pa`, but the text layer breaks the line so it holds
`200 × 10` then `5 Pa` — the layer's number set therefore contains `10`, and never `105`. Writing
the page faithfully as `10⁵`, or as `10^5`, or as the flattened `105`, ALL fold to the token `105`,
which is absent from the layer, so all three fail the numeric limb. The spelling that passes is the
layer's own two-token form, `200 × 10 ⁵ Pa`, which also avoids asserting a number (`105`) that is
not printed as such. **Any inline power of ten can hit this**, which is exactly the shape of the
failures on `CHE11O-ch07-p010` (`N2=3.0 × 10–3M`) and `PHY12O-ch01-p024` (`r12`).

**2. The coverage bar flips on deferral, and block ORDER does not matter.** The check demands
text-layer prose recall >= 0.99 with no unexplained run over 10 words only when the page defers
NOTHING to A2S; if any block is `needs_special` or has empty text, the bar drops to >= 0.50. Blocks
are matched against the layer independently, with order enforced only WITHIN a block. Two
consequences: faithful visual reading order is free (which is why `CHE11O-ch07-p033`'s out-of-order
layer did not trip the check, contrary to that worker's prediction), and correctly deferring a
figure, table or equation is what makes a page robust rather than risky.

**3. A real tension between the step's instruction and its check, on table-heavy pages.**
`CHE12O-ch07-p009` is almost entirely tabular. Deferring both tables whole — which is what the
instruction says to do — yields only **31.4% recall, below even the 0.50 wholesale bar**, so a
page that followed the instruction exactly could not pass. The worker kept the pure-artwork table
deferred and transcribed only the plain-text cells of the other (name / formula / oxidation state /
appearance, in the layer's own order), deferring its four scrambled preparation-equation cells
separately: 86% recall, passes. It noted the precedent (`CHE11L-ch01-p008.retry1.json` does the
same) and flagged the tension rather than hiding it. **This needs resolving in the check or the
agent file**, because on an all-table page the documented behaviour and the gate disagree.

The same worker verified its ten pages by calling `scripts/checks/A2.py`'s own `check()` with each
real input — all ten `(True, 'ok')`. That is the right way to self-verify on this step, and worth
putting in the brief in place of "validate against the schema", which sends agents hand-rolling
validators because `jsonschema` is not importable for them.

**My own error, recorded:** I dispatched `CHE12O-ch07` p011-p020 while the p001-p010 agent was still
running, so two agents were working the same chapter at once. No conflict occurred (the page ranges
were disjoint and both wrote only their own files) and the worker spotted the interleaved timestamps
and said so. But the sequential-dependency reason for one-agent-per-chapter means I should stage
batches within a chapter rather than overlap them.

#### Correction: parallel batches WITHIN one A2 chapter are safe, and that unlocks real throughput

I recorded above that dispatching `CHE12O-ch07` p011-p020 while p001-p010 was still running was my
mistake, because A2 pages are sequentially dependent. **Tested, and the seam came out correct.**

The p011-p020 worker found p010's OUTPUT did not exist yet, so it anchored on p010's **input** text
layer instead — which ends its running prose `"...attacks most metals except noble metals such as
gold and platinum. The"` — and set `first_block_continues_from_previous: true`, recording the
substitution in its `note` and predicting that p010 should end with
`last_block_continues_on_next: true`. It does. Checked directly:

    p010 last_block_continues_on_next   : True
    p011 first_block_continues_from_prev: True        -> AGREE
    p010 tail: '...gold and platinum. The'
    p011 head: 'products of oxidation depend upon the concentration of the acid...'

The sentence reads continuously across a seam written by two different agents who never saw each
other's output.

**Why this matters more than the one page.** The whole-chapter-per-agent rule existed to preserve
continuation, and it is what made the eight stalls so costly. But continuation does not actually
need the previous page's OUTPUT: the previous page's `previous_page_last_block` is null during a bulk
run anyway, and its **input text layer** is a perfectly good anchor for whether this page's first
block continues a sentence. So A2 can be parallelised **within** a chapter, not merely across
chapters — a 58-page chapter is six agents running at once rather than six in sequence.

The brief for a batch that does not start at p001 must say: read the previous page's output if it
exists, and otherwise read the previous page's INPUT text layer and anchor on how its prose ends.

### 80 of 1,221 A2 page seams contradict themselves, and nothing was checking

A `CHE11L-ch02` worker verified an invariant on its own ten pages — "page N's `last` always equals
page N+1's `first`" — and went back mid-task to flip p011's flag after reading p012, recording the
reasoning in both files. That prompted measuring it across the whole corpus. **80 of 1,221 adjacent
page seams disagree (6.6%).**

The invariant: between two adjacent pages there is exactly ONE fact about whether the prose runs
across the break, and A2 records it twice from opposite sides —
`last_block_continues_on_next` on page N, `first_block_continues_from_previous` on page N+1. When
they differ, one of the two pages is wrong about the same seam.

**Why nothing noticed.** `scripts/checks/A2.py` judges one page against one input and cannot see its
neighbour, so a cross-page contradiction is invisible to it by construction. The cause is visible in
the data: adjacent pages are read by different agents at different times, and during a bulk run
`previous_page_last_block` is null, so each side judges the seam from whatever it could see.

**Why it is not bookkeeping.** A3 uses these flags to decide whether two blocks are one page-split
paragraph — and A3 workers named ~40 such paragraphs on 2026-10-13. A wrong flag either cuts a
sentence in half, handing D4 a broken quote, or welds two unrelated paragraphs into one passage.

`tests/test_a2_page_seams.py` now pins it, with the allowance set at the measured 80 so it records
today's state rather than failing the build, to be ratcheted DOWN as seams are repaired. Verified
sensitive: flipping one agreeing seam moves the count 80 -> 81. A second test guards the checker
itself by requiring the comparison to be symmetric forwards and backwards, since a seam is one fact
seen from two sides.

Affected chapters include ones read today (`PHY12O-ch01` four times, `PHY12O-ch14`) and ones read
earlier (`CHE12L-ch01` four times, `BIO12L-ch02`, `BIO11O-ch16`), so this is long-standing and not
an artefact of this session's parallelism.

**Not repaired.** Fixing a seam means deciding which of the two pages is right, which needs the two
page images — agent work, not a script's. The 80 are now visible and counted instead of silent.

#### The seam defect is preventable: telling the agent about it produces clean seams

After ~170 more A2 pages were written, the seam measurement was repeated. **Seams rose 1,221 ->
1,244 while mismatches stayed at exactly 80** — the new pages introduced zero new contradictions,
and the rate fell 6.6% -> 6.4%.

The distribution is the interesting part, because it is causal rather than incidental:

  * `CHE11L-ch02` — **0 mismatches across all 33 pages**. Its workers were told about the invariant
    and one reported back that it had "verified consistent (every page's
    `last_block_continues_on_next` equals the next page's `first_block_continues_from_previous`)".
  * `CHE11O-ch07` p018-p036 — **5 mismatches**. That batch ran BEFORE the instruction was added.
  * `PHY12O-ch01` p001-p032 — **4 mismatches**, also from a pre-instruction wave.

So the 80 are not an inherent property of reading pages in parallel. They are what happens when
nobody tells the reader that the flag is one half of a shared fact. A brief that says so, plus the
documented substitute of anchoring on the previous page's INPUT text layer when its output does not
exist yet, produces clean seams — and one worker demonstrated the full loop: it used the input-layer
substitute for p021, then **re-checked when p020's output appeared mid-run** and confirmed the two
agreed.

Practical consequence: the existing 80 need repairing page-by-page (agent work, two images each),
but the number should stop growing now that the instruction is in the briefs. `_ALLOWED_MISMATCHES`
in `tests/test_a2_page_seams.py` should be ratcheted down as they are fixed, and any rise means a
wave ran without the instruction.

### Confirmed: 13 A2S figures have their real caption cut off by the crop boundary

Not a new bug — `scripts/checks/A2S.py` already anticipates it (comment: "crop needs fixing upstream
to include the caption line, or crop with padding") and accepts labels-without-caption as a pass
rather than rejecting it. Recording the concrete count because it had not been measured before.

**13 instances found** across `steps/A2S/out/`: 4 in `BIO12L-ch11`/`BIO12O-ch10` from today's work,
7 in `PHY11L-ch08`, 1 each in `BIO11O-ch01`. In each, the agent reported the SAME shape: the figure's
panel/diagram is inside `target_box_in_crop`, but the printed "Figure N.N ..." caption line sits just
below it, outside the box — e.g. `BIO12L-ch11-p004-b3`: "target_box_in_crop covers only the diagram
(boxes, circles, arrows); the printed caption 'Figure 11.2' sits below the box, outside it."

This is a real, mechanical undersizing of the box A2 (or A2S's crop-growing) drew for these specific
figures — not a transcription failure. The agents did the right thing: left `caption` empty rather
than invent it, and the check's own labels-OR-caption rule means these pass rather than loop forever
demanding a caption no crop will ever show them. A proper fix is upstream (grow the box to include a
caption-height margin below figure/table blocks specifically, which text blocks don't need), not
something an A2S agent can solve by reading harder.

### Organic chemistry audit (CHE12L-ch09, Amines) — what was real, what wasn't

The owner pasted a detailed external audit of the chemistry chapter export. Per standing practice
this session, every claim was checked against the real files rather than accepted on faith.

**Confirmed real, fixed at the brief level (so it stops recurring in any future chapter, any subject):**
- **Degree symbol (°) flattened to the letter `o`** — `108°` (a real bond angle) stored as `108o`;
  classification labels `(1°)/(2°)/(3°)` stored as `(1o)/(2o)/(3o)`. Same root cause as the physics
  exponent-flattening bug found earlier this session (text_layer loses the symbol, agent copies the
  flattened layer instead of reading the image) — just a different symbol. Fixed in
  `a2-page-reader.md`'s Trap 1 and mirrored into `a2n-notation-fixer.md` for backfill.
- **Chemistry locant superscripts flattened into the formula** — `¹CH₂–²CH₂–³CH₂–⁴CH₃` (locant
  numbers printed raised, counting carbons along a drawn chain) stored as `1CH2-2CH2-3CH2-4CH3`,
  reading as if the locants were ordinary formula text. Same fix locations as above.
- **A QR code classified as a `figure` block needing transcription.** CHE12L-ch09 p001 block 1 is
  the NCERT ebook-link QR code (print code `12086CH13` underneath) — decorative publisher furniture,
  not chemistry content — but A2 gave it `kind: figure, needs_special: true`, so A2S was queued to
  caption/label an image with nothing on it to transcribe. `a2-page-reader.md` now says explicitly:
  a QR code, barcode or publisher logo is furniture, omit it from `blocks` entirely, same as a
  banner illustration. The one existing instance was left as-is (never edit an agent's output); the
  rule stops new ones.
- **27 untranscribed-equation placeholders + ~13 untranscribed-figure placeholders, 39 blocks
  total, across pages 4/8/9/10/11/13/14/16/21/22** — real, matches the audit's own count exactly
  (verified by grepping the export for "not yet transcribed"). Cause: A2S simply had not run yet for
  these blocks. Not a defect in the brief; backfilled by dispatching the remaining A2S work for the
  chapter (also closes the "Table 9.2/9.3 image-only in MD" complaint, since those tables live on
  pages 8/9).
- **Exporter crop over-growth swallowing full neighbouring paragraphs** (e.g. CHE12L-ch09 p002 b2's
  crop included two full unrelated paragraphs above the figure). Root cause: `_grown_bbox`'s
  neighbour-aware growth can only stop at a sibling block's own bbox, but ordinary `paragraph`/
  `heading` blocks never carry a bbox in A2 output (only `needs_special` blocks do) — so on a page
  where a figure's immediate neighbours are plain text, the grow has nothing to stop against and
  falls back to a flat, content-blind 200px open pad in that direction. This is why the crop reads
  as "swallowed the surrounding prose": it did, genuinely, because the algorithm cannot see where
  that prose ends. Not fixed by shrinking the pad (that reintroduces the original clipped-caption
  bug the grow exists to prevent) — fixed by drawing a border around the block's own real bbox on
  top of the saved crop (`_mark_target_box` in `export_ncert_chapter_review.py`, reused by the new
  `export_ncert_chapter_html.py`), so a reviewer can see exactly which part of a generously-grown
  crop is the block and which part is context, without losing the caption-safety margin.
- **Exporter silently showed a transcribed `box` as "not yet transcribed"** — found while fixing the
  above, not in the audit itself. A2S's box kind stores prose in `text` (not `latex` — see that
  step's own brief: "`text` is the field that matters... a box returned with `latex` only reads as
  complete and can never actually be quoted"), but both review exporters only ever checked
  `a2s.get("latex")`, so a fully-transcribed box with no display equation (2 real instances in this
  chapter: CHE12L-ch09 p005-b6, p006-b7, both "Example 9.x" worked examples) rendered as pending.
  Fixed in both exporters to show `text` when present, with `latex` as a supplement, not a gate.

**Checked and did NOT reproduce — audit claims that were wrong:**
- `LiAlH4` stored as `LiA1H4` (digit 1 for letter l) — grepped the real A2 output and the export;
  the stored text already reads `LiAlH4` correctly everywhere it appears.
- "p007_b8.png has no path, not properly linked" — grepped every image embed in the export; all 25
  have a well-formed `![...](path)` with a real path, p007's included.
- Table 9.1's first-column chemical structures being "blank" — they are not blank; A2S already
  writes a descriptive placeholder for each drawn-ring structure (e.g. "NH2 (on a drawn benzene
  ring, ortho)"). This is a real, inherent representation limit (a 2D ring structure cannot become
  text) already handled about as well as it can be without redesigning the table schema to carry a
  SMILES-style field — not a bug to fix, a limit to document. The PNG crop remains the authoritative
  source for these rows.
- macOS metadata entries ("__MACOSX", `.DS_Store`) in a delivered ZIP — this pipeline does not
  produce a ZIP anywhere; nothing under `exports/review/` is ever zipped by any script here. Likely
  the owner's own Finder/zip step on their end. (One stray `.DS_Store` was sitting directly in
  `exports/review/` from Finder browsing the folder — harmless, but deleted as routine cleanup.)

### Confirmed: `target_box_in_crop` is systematically ~one line short on display-equation blocks

Reported independently by an A2S worker on PHY12O-ch01 pages 033/034 and consistent with the
already-logged "13 figures have their caption cut off by the crop boundary" finding — the same
undersizing, showing up on a different block kind.

Concrete cases: `p033-b12`'s box encloses only the equation's lead-in prose line ("The flux
through an area element ΔS is") with display equation (1.28) sitting just BELOW the lower edge;
`p033-b14`'s box straddles the tail prose line and only the top half of (1.29) — numerator
visible, denominator and the printed "(1.29)" below the edge. Milder clipping on `p033-b6`
(lower half of the line cut), `p034-b4` (right end cut) and `p034-b13` (second line cut). On
figures, `p034-b2` and `p033-b10` each lose the final printed line of their caption
("through the surface of a cylinder." / "charge q at its centre.").

The worker did the right thing in each case: because the block's `kind` is `equation` and no
other block intervenes between the box and the clipped content, it transcribed the adjacent
display equation and said so explicitly in `note` rather than returning a transcription of a
prose lead-in line as if it were the equation. That is the correct reading of "transcribe ONLY
what sits inside `target_box_in_crop`" when the box demonstrably does not contain the thing the
block is declared to BE — but it is a judgement the brief does not currently cover, and a
different worker could reasonably return just the lead-in line instead.

Two separable issues, neither fixed yet:
1. **The boxes really are short.** A2 records a bbox that clips the bottom (and sometimes the
   right) of what it marked. The export side already compensates by growing the crop toward
   neighbours, which is why the review images look right; the AGENT's `target_box_in_crop` gets
   no such compensation, so the agent and the reviewer are looking at differently-framed regions.
   Worth making `A2SPlugin` apply the same growth to `target_box_in_crop` that it applies to the
   crop itself, so the box the agent is told to honour matches the content actually present.
2. **The brief has no rule for "the box does not contain my block".** It should say what this
   worker worked out on its own: when the declared `kind` is not inside the box but is
   unambiguously adjacent with no intervening block, transcribe it and record the discrepancy in
   `note`; never return the wrong content silently, and never invent content that is absent.

Also logged from the same wave: `p041-b7` appears to be missing bracket glyphs in the page render
itself — printed as `E(r) = Ze/(4πε₀) [gap] 1/r² − r/R³ ; r < R`, with a visible gap where the
brackets enclosing `1/r² − r/R³` should be. Copied as printed per Universal rule 7, with the
suspected missing glyphs recorded in `note` rather than the expression being "repaired". This is
a source-render defect, not a transcription defect.

### RESOLVED 2026-10-15: italics are now recordable (field on A2, backfill step A2I)

**Owner approved the change on 2026-10-15, reversing the 2026-10-14 deferral below.** Built as
specified in the "Scope if picked up later" paragraph, with one deliberate difference: the
backfill is a NEW step `A2I` rather than an extra field on `A2B`, because A2B's ~1,100 finished
outputs are checked agent output and adding a required field to its schema would invalidate every
one of them (CLAUDE.md: never edit an agent's output). A2I is A2B cloned and inverted.

What landed:
- `schemas/A2.json` — `italic_terms` added as a sibling of `bold_terms` on the block definition
  (optional, so all 1,404 schema-valid A2 outputs still validate unchanged; verified).
- `.claude/agents/a2-page-reader.md` — a new rule bullet beside the `bold_terms` one, and the
  three "never include an italic term" sentences across that file and `a2b-bold-marker.md`
  changed from "discard it" to "record it in `italic_terms` instead".
- `schemas/A2I.json`, `scripts/checks/A2I.py`, `.claude/agents/a2i-italic-marker.md`,
  `config/steps.yaml` A2I entry, `step_plugins.A2IPlugin`, `tests/test_a2i_check.py` (20 cases).
- The carve-out mirrors the existing bold-vector one: italic SINGLE-LETTER maths/physics scalar
  symbols (`r`, `q`, `E`, `θ`) are excluded, because that italic is typographic convention and a
  field full of single letters is unusable. Not yet measured on real pages whether agents honour
  that line cleanly — the first A2I wave will show.
- Still open: nothing consumes `italic_terms` yet. `scripts/export_ncert_chapter_review.py`
  renders `bold_terms` (line ~344) and has no italic equivalent, so the BIO12O-ch03 p013
  rhetorical-question case below is now *capturable* but still not *rendered*. Wiring the
  exporters was out of scope for this change and is the obvious next step.

The original deferral record follows, kept because it states the evidence.

Owner's call, 2026-10-14: "leave italics one for now". Recorded rather than silently carried.

**What the gap is.** A2B captures `bold_terms` only, and its brief says so deliberately: "Bold
only — never an italic-only term (a species name like *Rhizopus*, a book title, a foreign
phrase): italics in NCERT mark something else entirely (taxonomy, emphasis-as-style, a citation),
not the book's own vocabulary." That reasoning is sound for VOCABULARY extraction, which is what
A2B exists for.

But it means italics have no representation in the pipeline's data at all, and the consequence
shows up in rendering: NCERT sets its rhetorical questions to the reader in italics — real case
BIO12O-ch03 p013, "*What do you think the doctors inject to induce delivery?*" — and the HTML
export renders them as ordinary prose, indistinguishable from the surrounding explanation. The
book is visibly making a distinction that our output cannot reproduce.

**Scope if picked up later.** Add an `italic_terms` field alongside `bold_terms` on A2 (for
future pages) and on A2B (to backfill the ~1,400 already read), with the same substring check
A2B already applies to bold. The two must be judged TOGETHER by one agent looking at one image:
the existing rule's whole job is telling bold from italic, so the agent already makes the
distinction and currently discards half of it. Re-running A2B on a measured chapter took about
4 minutes per 15 pages.

**Not a rendering bug.** Worth stating plainly so nobody later looks for it in the exporter:
there is nothing in `steps/A2B/out/` or `steps/A2/out/` to render. The data has to be captured
first.

### FIXED 2026-10-15: a flagged A2 page was invisible to every backfill step

Owner approved, 2026-10-15. A2B, A2L and A2N each selected their candidate pages with a private
copy of the same loop, and every copy required `status == "pass"` exactly. That was never the
spec's rule: spec 5.4 defines `flagged` as "a value exists but needs a human look", next step
runs **yes**, with the provisional value. Four copy-pasted loops had quietly agreed on a stricter
rule than the spec states.

The consequence was exactly backwards. `PHY12O-ch01-p024` was flagged, and it was flagged because
`scripts/checks/A2.py` scores PROSE WORDS against the page's text layer while that page's actual
defect was NOTATION — so the single page in the chapter with the worst notation garble was the one
page the notation fixer structurally could not see. Measured before the fix: PHY12O-ch01 had 50
pages with A2 output and A2B/A2L/A2N each had exactly 49, p024 being the one missing from all
three. (By the time the fix landed, p024 was being re-read for unrelated reasons and its new read
passes, so the fix's effect is now visible on the other 11 flagged pages, not on p024 itself.)

Fix: one shared `step_plugins._a2_backfill_pages()` replaces all four private loops and selects
`status in ("pass", "flagged")`. `blocked`, `stale` and `skipped` are excluded deliberately, with
the reasons written at the function (none of the three currently occurs in `steps/A2/status/`,
whose only values are `pass` and `flagged`). A page whose blocks lack the schema-required `n`
(real case `BIO12L-ch03-p001.retry1`) is also excluded, because `n` is the join key every backfill
file is addressed by — see `step_plugins._a2_prose_blocks`.

Not resolved by this: a flagged page's own A2 defect is still a flagged defect. A backfill now
annotates it, which is the point, but the annotation inherits whatever is wrong with the stored
block text. Nothing downstream currently distinguishes "backfilled from a passed read" from
"backfilled from a flagged read", and perhaps it should.

### A2L's `size_rel` 0.4-4.0 ceiling cannot express a display numeral

Found by the A2L worker on CHE12L-ch09 p001, and it is a real limitation of a check I wrote
earlier this session, not an agent error.

The chapter-opening page sets "Unit 9" with the numeral **9** as a display figure 196 px tall --
about **9.6x** the page's 20.5 px body text. `scripts/checks/A2L.py` rejects any `size_rel`
outside 0.4-4.0, on the reasoning that a value far outside that range is almost always an agent
reporting a PIXEL height instead of a ratio. That reasoning is still right for the common case,
but it makes an honest 9.6 unreportable: the worker clamped to the 4.0 ceiling and recorded the
true measurement in `note`, which is the best available behaviour but means the stored number is
knowingly wrong.

Two ways out, neither taken yet:
1. Raise the ceiling (say to 12.0) and lean on the separate "body_text_size_px is implausibly
   large for a single line" guard to catch pixel-height confusion instead. Cheapest fix.
2. Keep the ceiling for text roles and exempt a new `display_numeral` role. More precise, more
   schema.

Until then, any `size_rel` sitting exactly at 4.0 should be read as "4.0 or more, see note",
not as a measurement.

### Corrected: chemistry's grey section headings are RIGHT, my suspicion was wrong

Recorded because I flagged it as probably wrong in conversation and it was not.

On seeing `section_heading_text_color: #6d6e71` (grey) for CHE12L-ch09 I suspected edge-sampling
of an antialiased glyph, because I remembered brick red in that chapter's crops. The worker had
actually verified it: every 9.x margin heading and every in-flow sub-heading is grey `#6d6e71`,
and body text is `#221f1f`. The brick red I was remembering is real but is `#e11a22` and is used
only for the SCRIPT WORDS "Objectives" (p001) and "Exercises" (p020) -- text, not a heading
colour and not a fill. The salmon I also remembered is `#f48480`, used for marginal rules, box
bars and table header rows.

Likewise my suspicion that "all 22 pages two-column" was too uniform to be true: it is true.
This book hangs its section headings in a narrow left margin column with prose in a wider right
column, on BOTH recto and verso (demonstrated on p017, a recto, with 9.8 and 9.9 both in the
left margin). Biology's 7-of-15 is the different case, not chemistry's 22-of-22 -- the two books
have genuinely different grids, which is the whole reason layout is measured per chapter rather
than assumed per subject.

Also measured: this chapter prints NO `page_header_band` at all, and its page is 1600x2180 px,
ratio 0.734 -- NOT A4 (0.707). The latest-NCERT Chemistry edition has a different trim size from
the older-NCERT Biology scan, so "the page is A4" is a per-book fact, not a project-wide one.

## A2 block bboxes are systematically mis-aligned vertically (PHY12O-ch01, 2026-10-15)

Three independent instances found while repairing this chapter, all vertical, all different signs:

- `p022` n=1 — equation bbox sat ~80px BELOW the printed glyphs, onto blank margin. The equation
  was captured nowhere in the pipeline as a result.
- `p047` n=9 — figure bbox STOPPED ABOVE the printed caption line (`FIGURE 1.34` was 46px below
  the bottom edge), so the caption was captured nowhere.
- `p011` n=12 — equation bbox sits ~40px ABOVE the printed equation: its top edge pulls in the
  preceding prose line and its bottom edge clips the `r²` denominator. The A2S agent read the
  clipped part from just below the box and recorded that it had done so.

Each was individually repaired by re-reading the page, and in each case the re-read placed the box
correctly. But three misses of the same kind in one 50-page chapter suggests this is a systematic
weakness in how a2-page-reader estimates vertical extent, not three unlucky pages.

What is NOT yet known: whether the other ~44 pages of this chapter, and the ~1,400 pages already
read across the corpus, carry the same error silently. A bbox that is merely loose costs nothing;
one that misses its content entirely loses that content with no signal, because A2's coverage
check scores PROSE words only and a deferred block carries empty text by design — so a figure or
equation whose box points at blank paper passes every existing check.

A cheap detector worth building: for every `needs_special` block, render its bbox and measure ink
coverage. A box pointing at blank margin has near-zero ink; a box that clips will have ink running
hard against an edge. Neither condition is currently detected anywhere in the pipeline.

## Partial-bold maths runs cannot be recorded (PHY12O-ch01, 2026-10-15)

`bold_terms` requires each entry to be a verbatim substring of the block's `text`. NCERT prints a
vector named in running prose with ONLY THE LETTER bold and its subscript plain -- `E₁A` is a bold
`E` followed by a plain `₁A`. So the bold run is not any substring of `text`, and the field cannot
represent it. Reported independently by the A2B passes on p022 ("E₁A", "E₂A", "EA") and p034
(four occurrences of a bold `E` in prose).

Both agents correctly declined to invent a convention -- listing `"E"` alone would be meaningless
as a term, and listing `"E₁A"` would claim the subscript is bold when it is not.

This is distinct from the existing bold-VECTOR carve-out, which says a bold single-letter vector
symbol is typographic convention and should not be recorded at all. That carve-out happens to
cover these cases too, so nothing is being lost today. But the carve-out's stated reason (it names
a convention, not vocabulary) is not the same as "the schema cannot express it", and if the project
ever wants partial-bold runs captured, the field needs either a per-occurrence form (offset plus
length) or an explicit convention for partial-bold maths. Worth deciding before a chapter arrives
whose key vocabulary is set this way.

## `body_text_size_px` variance across measurers (CHE11L-ch02, 2026-10-15) -- PARTLY CORRECTED

A2L asks each agent to measure "the cap-to-baseline height of one line of ordinary body prose on
this page, in pixels", and every `size_rel` on the page is a ratio to it. Measured across 36 pages
of CHE11L-ch02, the value clusters by WHICH AGENT READ THE PAGE, not by the page:

    p001-005  21.5     (an earlier run)
    p006-012  20.5     (batch 1)
    p014-021  22.5     (batch 2)
    p022-035  20.0     (batches 3 and 4)
    p037-040  19.0 / 15.0 / 15.0  (batch 5)

Constant inside each batch, discontinuous at every batch boundary, on a book whose body type is
visibly uniform and whose page images are all 1750x2180. A 50% spread (15.0 to 22.5) cannot be a
property of the pages.

Why it matters: `size_rel` is a RATIO to this number, and the exporter derives a point size from
it. Pages measured by different agents therefore render body prose at different sizes, and a page
whose divisor came out low renders everything on it proportionally large. p038/p039 at 15.0 are
the worst case -- about 30% off the chapter's own mode.

What protects us today, partially: `_print_geometry` takes a median of cap heights across the
whole chapter, so the CHAPTER-level body point size is robust to outliers. What is not protected
is anything consumed per page.

Possible fixes, none implemented:
1. Have the exporter ignore per-page `body_text_size_px` entirely and use the chapter median, so
   a mis-measured page cannot distort its own type. Cheapest, and loses nothing real if the book's
   body type genuinely is uniform.
2. Make the measurement objective in the brief -- e.g. "measure the baseline-to-baseline pitch of
   the body column over TEN consecutive lines and divide by ten", which is far less sensitive to
   judging one glyph's cap height than measuring a single line is.
3. Have the check compare each page's value against the chapter's running median and flag an
   outlier beyond some tolerance, so the disagreement is visible rather than silent.

Note this was invisible on BIO12O-ch03 and PHY12O-ch01 because each was measured largely in one
pass. It only became apparent when one chapter was deliberately split across five parallel agents.

### Correction to the above, same day

The entry above was written before the last batch reported, and overstated the problem. Two of
the three clusters it called outliers are legitimate measurements:

- **p038/p039 at 15.0** -- those pages carry NO ordinary body prose at all. They are table pages,
  and 15.0 is the table's own cap height. The agent measured correctly and explicitly warned that
  `size_rel` on those pages needs rescaling before chapter-wide comparison.
- **p040-p045 at 18.0** -- real structure, not noise. This chapter has TWO body settings: the
  two-column prose pages set at 20.0px cap height / 35.7px pitch, and the closing summary and
  exercises pages set single-column at 18.0px / 31.7px.

What survives as a genuine calibration question is narrower: batch 2 reported 22.5 where batches
3 and 4 reported 20.0, on comparable two-column prose pages. That is a ~12% disagreement between
measurers on like-for-like pages, not the 50% the original entry claimed.

The lesson stands but is different from the one first written: the number is partly a property of
the page (which this chapter proves, by genuinely having two settings) and partly of the measurer.
A chapter-median override would therefore be WRONG for this book -- it would force the summary
pages to the prose pages' size. Fix option 1 in the entry above should not be applied as stated.
Options 2 (make the measurement procedure objective) and 3 (flag outliers against neighbours of
the same column structure) remain valid.

## A2L has no rule for a block that runs over the column gutter (CHE11L-ch02, 2026-10-15)

This chapter's body is two-column, and single A2 blocks frequently print as TWO regions -- a few
lines at the foot of the left column, the rest at the head of the right. It happens on at least
p009, p010, p016, p025, p026, p027, p028, p030, p031, p033, p034, p035 and p036.

Five agents measuring this chapter split two ways on how to report it:

- Batches 1-4: put the real `n` on the region where the block STARTS and `n: null` on the
  continuation, so no `n` repeats, and say in `note` which null is a tail.
- Batch 5: put `n: 3` on BOTH regions of p036's block 3.

`scripts/checks/A2L.py` rejects a duplicate block `n`, so batch 5's reading failed and p036 came
back `blocked` -- correctly, given the check, but the check is enforcing a convention the brief
never states.

Neither reading is obviously right. The n-on-both form says truthfully "this block occupies these
two regions"; the n-plus-null form keeps `n` unique but relies on a consumer reading prose in
`note` to know the second region is a tail rather than an unmatched element.

Worth deciding explicitly in the brief, because two-column books make it routine rather than rare.
The cleanest answer is probably to allow one block to carry a LIST of regions, but that is a schema
change. Until then the brief should at least name one of the two conventions so agents stop
disagreeing, and the check's duplicate-n rule should match whatever is chosen.

## A2S target boxes clip their own content -- not a physics quirk (CHE11L-ch02, 2026-10-15)

Logged earlier against PHY12O-ch01 as five vertical bbox misalignments. It recurs in chemistry, so
it is a pipeline-wide property rather than one chapter's bad luck.

On CHE11L-ch02 a single A2S batch of nine blocks reported three boxes cutting through printed
glyphs of their own content: p024-b3's left edge, and the horizontal edges of p024-b9 and
p024-b16 (the latter bisecting the result line of its own computation chain, glyphs at y 252-275
against a box bottom at 264). p024-b10's box excludes two result lines that continue the same
chain. The agents transcribed what was inside the box and recorded each clip rather than silently
reaching outside, which is the correct behaviour -- but it means the DATA is shaped by where the
box fell, not by what the page prints as one expression.

Combined with the physics findings, the pattern is: A2 places a defensible region for a block but
is not reliably tight to the printed extent of that block's content, and nothing downstream
detects it. The detector proposed earlier (render each needs_special bbox and measure ink; near
zero means it points at blank paper, ink hard against an edge means it clips) would catch both the
physics misses and these chemistry clips, and is still unimplemented.

## The A2S box offset is SYSTEMATIC and page-range correlated (CHE11L-ch02, 2026-10-15)

Earlier entries recorded A2S target boxes that miss or clip their content, first on PHY12O-ch01
and then on CHE11L-ch02, and treated it as diffuse imprecision. One agent measured it properly --
per-row ink bands on each crop PNG rather than visual judgement -- and the shape of the defect is
much more specific than that:

    p015 (five blocks)   boxes align within ~10 px        -- fine
    p018-b9              box 22 px too high
    p019-b6              box 25-35 px too high
    p019-b9              box 40-50 px too high
    p018-b12             box contains NO INK AT ALL; rows 251-342 blank.
                         Its equation (m_e v r = n.h/2pi, number 2.11) sits at y 186-250.
                         Corrected box would be ~[200, 186, 767, 250].

Every misaligned box takes in the tail of the PRECEDING prose line and clips the bottom of its own
equation -- i.e. the whole box is translated upward, not mis-sized. The offset grows across
consecutive pages (22 -> 25-35 -> 40-50) while a nearby page range is clean, which points at an
accumulating positional error in how a block's bbox is derived, not at per-page agent judgement.

Three blocks in this chapter now return the honest unsure form because their box does not contain
their content at all: p013-b6 (equation ~30 px below the box), p018-b12 (box on blank paper),
p020-b10 (box one line above its equation, which is why equation 2.16 is captured nowhere in the
chapter). All three named the corrected box in `note`.

This is worth real debugging effort rather than another round of per-page re-reads: the offsets
are measured, reproducible and page-range correlated, so whatever computes these boxes can be
tested against the ink-band measurement directly. The previously proposed detector (render each
needs_special bbox, measure ink; near-zero = points at blank paper, ink hard against an edge =
clips) would have caught every one of these before any transcription was attempted.

## 2026-10-16 · What `inputs/papers/` can and cannot verify

Every figure in the bank (58 records) carries a `figure_source_url` on `cdn.mathpix.com`, matched
by wording against the legacy sheets. SPEC.md Section 4's rule is the opposite — "Always crop
figures from the official PDFs; never depend on a URL" — and the audits found the predicted
damage: option panels in an order that contradicts the options printed beside them. The original
PDFs in `inputs/papers/` make the rule keepable for some years, but not all, and not equally:

| source | what it is | what it can verify |
|---|---|---|
| `2024.pdf` | official NEET (UG)-2024 **Code T3** booklet | stem and option VALUES; stem diagrams |
| `2018, 2025, aipmt-2010-main` | official booklets (masthead present) | same, for years not yet extracted |
| `2023.pdf` | **coaching compilation** ("Chapter & Topicwise NEET PYQ's", options a./b./c./d.) | wording only — its diagrams are the publisher's redrawings |
| `2021.pdf`, `2022.pdf` | **pure scans**, 18 text characters across 26-27 pages | nothing until OCR'd |

Three findings worth keeping, each of which cost a wrong conclusion first:

**The key grid inside `2024.pdf` does not belong to it.** Page 28 prints "1. (4) 2. (1) …", 198
answers, which looks like a gift: an answer source independent of `inputs/keys/`. Taken at face
value it reported 109 of 155 records as disagreeing with the official paper. Every one of the six
checked by hand was the grid being wrong, not the record — q115's printed options make (4)
Metaphase correct and the grid says (2) Telophase; Hind II cuts at 6 bp and the grid selects 4 bp.
The grid agrees with the records on 54/175 (31%) when matched by the booklet's own numbering and
50/195 (26%) when matched by ours; chance with four options is 25%. It belongs to neither order.
`paper_source_match.key_is_trustworthy` now gates any such grid on that agreement rate before a
single answer is compared against it, because the failure mode is silent: a stray grid rewrites
every answer in the bank and each finding looks like a defect in the data.

**Answers still cannot be verified for 2024.** With that grid rejected, nothing in `inputs/papers/`
carries an answer for the year, and the records' answers came from `inputs/keys/`, so comparing
them to it is circular. Option VALUES can still be checked, and that is where the real repairs
are: 16 records hold an option whose text is not on the printed page, including the lost-leading-
digit corruption cross-code consensus could not touch (`0.315 g` where the paper prints `0.0315 g`;
`4 mT` where it prints `4.4 mT`). Those need a reading agent, not a script — the script can only
say the strings differ.

**Matching must be on token containment, not a sequence ratio.** A `difflib` ratio scored 0.36-0.50
on questions demonstrably present in the paper, because the records hold maths as LaTeX, hold
match-lists in separate fields, and order options differently from the print — all of which move
characters without changing which words are there. Containment put 171 of 198 at 0.8 or better
with no ambiguous pairing. Two bugs found the same way are worth naming because both read as data
defects: a column margin measured from the leftmost line in the column was dragged 27pt left by a
centred "PHYSICS" heading, so no question start in that column was found and ~100 questions
reported as absent from the paper; and comparing the record's bare `stem_en` against a chunk
holding stem AND options caps the score near 0.45 for short stems.

Open: 2021 and 2022 need OCR before any of this applies to them, which is the mathpix step the
B9/B10 briefs describe. 2023 has no official source in hand at all — its figures can be confirmed
as present but not sourced, and the honest record is that they remain third-party.

### Measured extraction accuracy (`scripts/checks/extraction_accuracy.py`)

First comparison in this build against evidence from OUTSIDE the scrape. Every earlier check —
B4's second read, the paper quality checks, cross-code matching — compared the extraction with
itself, and none of them can see a value the scrape never carried.

| | matched & checkable | clean | truncated number | other numeric | foreign content | content dropped |
|---|---|---|---|---|---|---|
| 2024 (official booklet) | 155 of 198 | 137 (88%) | 6 | 5 | 6 | 1 |
| 2023 (coaching compilation) | 122 of 299 | 110 (90%) | 4 | 4 | 3 | 1 |
| 2022 (scan) | 0 | — | — | — | — | — |

All 7 truncated numbers found before the match was tightened were checked by hand against the
printed page and all 7 were real, with no false positive in that class: `1.98 mN` held as `98 mN`,
`1.20 A` as `20 A`, `2.271098 L` as `271098 L`, `3.92 m s⁻²` as `92 m s⁻²`, `52 × 10³ N` as
`5 × 10³ N`, `3.15 g` as `15 g`, `3.80 kJ/mol` as `80 kJ/mol`. In Q-000456 the damaged option is
the KEYED one: the key selects option 4, whose printed value is 3.92 m s⁻² (confirmed
independently: g = 9.8 × (1/10)/(1/2)² = 3.92), and we publish it as 92 m s⁻². That question
cannot be answered correctly from what the bank contains.

2023's two truncations settle two defects this log previously recorded as unrecoverable: the
resistor colour code (page prints 22000, record holds 2200) and the resonance frequency (page
prints 1.59, record holds 59). Both had been derived by calculation with nothing to check against;
the page agrees with the calculation in both cases. The source is a coaching compilation, so it
corroborates rather than proves — but an independent calculation and an independent printing
agreeing is as close to settled as this corpus gets.

`foreign_content` is now almost entirely the records' OWN honest markers — "unreadable notation",
"scrambled units" — left where the reader could not make out the maths. Those are a known gap
declaring itself, not invented content.

Four rounds of false signal were produced before these numbers settled, each of which first looked
like a defect in the data, and each worth remembering as a measurement failure mode:

1. The question number and the "(1)".."(4)" option labels counted as content numbers — 147 of 179
   records "numerically wrong", 0 clean.
2. `record_text` stringified `{"label": …, "text": …}` objects, putting the words "label" and
   "text" into every record and no paper — 20 records "carrying foreign content".
3. Containment divides by the record's own token count, so a record with few distinctive words
   scored 0.75 on coincidence; an absolute floor of 8 shared words was needed as well as the ratio.
4. Chunks that swallowed several questions (the compilations restart numbering in every chapter and
   interleave solutions) matched almost anything at 1.0 — 87 "content_dropped" on 2023, which fell
   to 0 once over-long chunks were dropped.

The lesson each time was the same: a discrepancy between our data and a measurement is evidence
about the PAIR, and the measurement is the newer and less tested half.

### 2026-10-16 · Cross-code merge (`scripts/merge_paper_codes.py`)

The 2023 audit's three P0 items were all consequences of one gap: the pipeline read several
booklet codes and never reconciled them. Fixed mechanically, with no transcription judgement:

| | before | after |
|---|---|---|
| 2023 rows / distinct questions | 299 rows, 212 keyed | 299 rows, **200 live** (99 marked `merged_into`) |
| live rows with no `official_answer` | 82 | **0** |
| live rows with no `subject` | 80 | **0** |
| rows with a per-code option order | 0 | 198 / 199 / 189 (2022 / 2023 / 2024) |
| `paper_quality` findings | 310 | **192** |
| `DUPLICATE_ROW` findings | 136 | 18 |

Merged rows are marked, never deleted: a surplus row is the ONLY record of what its own booklet
code printed, which is its option order, and that is what lets one official answer be checked
against every code's key (audit G4).

Three fixes inside this that each hid a whole class of failure:

**The key grid parser read 8-column tables as 5-column ones.** The 2023 key is a pipe-delimited
table with EIGHT (QNO, RES) pairs per printed row; the parser flattened the page and chunked the
numbers ten at a time, so every chunk straddled a row boundary. Code E2 came out with 133 of 200
answers, missing 18-25 and 43-48 among others -- which read as "the key has no answer for this
question" and was the stated reason 78 E2 positions were left blank. It now reads the table as a
table, and falls back to page GEOMETRY (words grouped into printed rows by y, ordered by x, then
paired) for 2022 and 2024, which print plain columns with no separators and a different column
count per year.

**Each year labels its grids differently** -- 2022 "SET: X6", 2023 "BOOK CODE : E2", 2024 "Test
Booklet Code : Q1". A page whose label does not match is skipped silently, which is how 2023's E2
key was believed absent from a file that contained it all along. All three spellings are accepted.

Validation of the parser, which matters because it now supplies answers: on 2024 code Q1 it agrees
with the records' existing `official_answer` on **193 of 193, zero differences**. All three years
now parse every code at the full 200 positions (2022: 32 codes, 2023: 48, 2024: 48).

**Subject derived from printed position.** NEET's sections are 1-50 Physics, 51-100 Chemistry,
101-200 Biology, and the codes reshuffle only WITHIN a section. Checked against every row that
already carried a subject: 617 agreements, 0 disagreements. Used only where the field was empty.

Left deliberately untouched and flagged: 3 questions whose codes' keys select DIFFERENT option text
after each code's order is mapped on (Q-000030 = E1 Q123, Q-000043 = E1 Q148, Q-000198 = E1 Q73).
The 2023 audit predicted the last of these exactly -- "the E2 print orders the options differently,
so the E2 key would land on the unrearranged bromide ... a latent error, waiting for the day the E2
key gets attached". Attaching the E2 key surfaced it, which is the check working as intended.

Still open from that audit, and why:

  * **E2 Q117-200 were never extracted** (`BOOKLET_TRUNCATED`, still CRITICAL). The source PDF is
    present; this needs a B2/B3 run, not a repair script.
  * **The 12 wrong answers and 4 panel-order figures cannot be fixed as the audit specifies.** Both
    its P0 and its G8 say to take the stem, options and figures from the NTA booklet. 848 PDFs
    across the work folders were searched: the only official booklets on disk are 2018, 2024, 2025,
    AIPMT 2014 and aipmt-2010-main. There is no NTA 2022 or 2023 paper to take them from.

### 2026-10-16 · Figure sourcing widened, option blocks captured (owner's decision)

Two changes to step B9S on the owner's instruction, both of which reverse an earlier conservative
choice of mine, and both of which are right:

**1. Option-image questions are no longer refused.** B9S originally refused to crop a question whose
options are pictures, because the panel order belongs to one booklet code and a crop from another
contradicts the options beside it. The owner's point is that an AGENT can see the mismatch where a
script cannot: it compares the panels against the record's own option text. Hence the new
`panel_order_differs` verdict and `panel_map`. A rotated crop still does not publish — the mapping
is applied first.

**2. The search covers every printed paper, not the question's own year.** Justified by measurement:
the 170 scraped booklet-code PDFs hold ZERO embedded images between them, so no search of them can
return a diagram, while the printed volumes hold 871 and reprint questions across years. A question
absent from its own year's volume is often printed in another.

Result across the three extracted years:

| | needing a picture | located in a printed paper | diagrams cut | option blocks cut |
|---|---|---|---|---|
| 2024 (official booklet) | 40 | **36** | 24 | 21 |
| 2023 (solved-paper volume) | 28 | 10 | 3 | 10 |
| 2022 (scan, no text layer) | 18 | 2 | 1 | 2 |

The headline case: `Q-000492` held four options reading "(Image option — will be added soon)" and
now carries all four acceleration-time graphs in the booklet's own (1)–(4) order. `Q-000049` — the
pedigree question BOTH audits flagged as an order mismatch — now carries the authentic four panels,
in which the consanguineous-mating symbol is the double line at panel (c).

Four cropping faults found by looking at the output rather than trusting it, each of which silently
destroyed content:

1. The option block's bottom edge was taken from the FIRST option's line, because the marker regex
   only matched option (1)/(a). Three of four panels were cut off.
2. Its top edge was taken from the label, but a picture option is taller than its label, so the
   graph for option (1) was decapitated. Any drawing straddling the label's line now pulls the edge up.
3. The block ran on past the last option into the next chapter heading.
4. The eight-distinctive-word match floor refused exactly the questions that most need a figure:
   "The equivalent capacitance of the system shown in the following circuit is" reduces to five
   words. Short records are now matched on stricter terms (perfect containment, wide margin over
   the runner-up) rather than refused — which also lifted 2024's checkable coverage from 155 to 187.

Open: **2022 can only reach 2 of 18 because its volume is a scan with no text layer.** Tesseract is
installed and OCR of a page takes about 1.3 seconds, so this is reachable; nothing else blocks it.
The 18 unfound 2023 questions are mostly absent from the volumes in hand.

### 2026-10-16 · Legacy figures are verified, not discarded (owner's decision)

The owner's instruction: the `cdn.mathpix.com` figures are acceptable to use, provided they are
CORRECT. That reframes this work correctly and exposes a gap in what had been built.

The earlier framing treated origin as the verdict -- crops from the printed page good, legacy
figures bad -- and set out to replace them. But origin is a label, not a verdict: a crop taken
from the real page can be the wrong region of it, and a legacy figure can be a perfectly good
picture of exactly this question. The gap is worse than the framing: **54 legacy figures are
published in this bank right now with no verdict of any kind against them.** Two audits looked at a
handful and found several wrong; nobody has looked at the rest. An unverified figure that happens
to be right and one that is wrong are indistinguishable from the data.

So every candidate image now gets the same judgement, and the work is per IMAGE rather than per
question:

| | 2022 | 2023 | 2024 | total |
|---|---|---|---|---|
| fresh crops from a printed paper | 14 | 13 | 29 | **56** |
| already-published figures queued for verification | 10 | 18 | 26 | **54** |

A legacy figure the agent confirms is kept. Nothing is discarded for its provenance; `figure_origin`
is carried on the work item so the agent can weigh it, and `match_score` is 0.0 for a legacy image
because no wording match was ever recorded when it was attached -- those are judged on the picture
alone.

Still open: 18 of 2023's and 8 of 2022's figure-needing questions could not be located in any
printed paper held here, so for those the legacy figure is the only candidate there will ever be,
and the verdict on it decides whether the question ships with a picture at all.

### 2026-10-16 · B9S verdicts: what the figures actually are

Step B9S run over every candidate image — crops cut from the printed papers AND the figures the
bank was already publishing. The second group is the point: 54 figures were shipping with no
verdict of any kind against them.

Results over the first 36 images judged:

| verdict | n | what it means |
|---|---|---|
| `belongs_complete` | 17 | published; the right figure, whole and clean |
| `belongs_with_junk` | 13 | the right figure, but carrying adjacent stem text or a watermark |
| `panel_order_differs` | 4 | the right four panels in the wrong order — mapping stored |
| `not_a_figure` | 1 | the question's own formula typeset as a picture |
| `wrong_figure` | **0** | — |

**Not one legacy figure was the wrong question's picture.** That settles a question that had been
argued from provenance rather than evidence: the `cdn.mathpix.com` figures are pictures of the
right questions. The defects are panel ORDER and loose cropping, and both are fixable without
sourcing a new image — which is why discarding them for their provenance would have been wrong.

**Independent replication of the outside audit.** That audit named four figures whose panels are
out of order and gave the mapping for three of them as "a–d = options 4, 1, 2, 3". The agents,
which never saw it, returned exactly that for all three — Q-000098 (Boyle's law graphs), Q-000203
(product options) and Q-000204 (dehydration options) — and a different mapping, `{a:3, b:1, c:2,
d:4}`, for Q-000049, where the audit had also said the order "differs again". Two independent
readings agreeing to the permutation is as close to proof as this corpus allows.

**One defect neither audit caught.** Q-000198's figure is `not_a_figure`: it is the question's own
reaction formula typeset as an image, carrying nothing the stem does not already say in text, and
the file is shared with another question's record. Both audits had treated it as a valid figure.

**A bug of mine the agents caught.** The first crop for Q-000492 came back `wrong_figure` — the
cropper had taken the OPTION BLOCK as the stem diagram, because it picks the largest drawing in the
question region and for a question whose options are four graphs the options are the largest
drawing. The stem's own v-t plot was never captured. Fixed by searching for the diagram only ABOVE
the option block; the recut crop came back `belongs_complete` from a second agent.

Design note worth keeping: `belongs_with_junk` does not publish, but for a legacy figure it does
NOT withdraw either — the record keeps the figure and gains `figure_verified: false`. The junk in
these is cosmetic (a line of adjacent text, the publisher's roundel) and makes no answer wrong,
unlike panel order. Where the watermark is printed into the source page itself, no crop can do
better, so that verdict is the ceiling for those questions rather than a defect to chase.

### 2026-10-16 · Same-code sources arrive: option order verified for 2023

The owner supplied two volumes that change what can be checked, and confirmed they are NTA papers:

  * `inputs/papers/2023_solutions_code-E1.pdf` — Answers & Solutions for NEET (UG)-2023, **Code-E1**,
    75 pages, 364 images. E1 is the code our 2023 records are keyed to.
  * `inputs/papers/2022_solutions_code-R6.pdf` — Questions & Answers for NEET (UG)-2022, Code-R6,
    41 pages, 120 images.

**Option ORDER is now verifiable for 2023**, which both audits listed as impossible and which was
the stated hard blocker on their P0 items. Against the E1 volume, of 85 questions whose options are
readable on both sides: **62 match the printed order position for position**, 13 differ at one to
three positions, and 10 at all four.

Examined individually, the differences are mostly transcription rather than rotation — and two of
them confirm the earlier audit's claims exactly:

| question | our record | the paper | |
|---|---|---|---|
| E1 Q21 | 2, 3, 6, 4 % | **1.2, 1.3, 1.6, 1.4 %** | lost leading "1." — audit said precisely this |
| E1 Q22 | 6 × 10⁻⁷ | **1.6 × 10⁻⁷** | lost leading "1." — audit said precisely this |
| E1 Q48 | 3.101, 3.104, 3.103, 3.102 | 3.104, 3.103, 3.102, 3.101 | **a genuine rotation**: same four values, different order |
| E1 Q17 | 3, 23, 43, 34 | 3 V, 23 V, 43 V, 34 V | the unit was dropped |
| E1 Q45 | 3 Il | 3 ll | font I-vs-l, cosmetic |

Q-000076 (E1 Q48) is the first option rotation PROVEN against a same-code source, and it explains
the audit's finding that Q48's key appeared to select the wrong option: the key is right for the
printed order, and our order is rotated against it.

Three parser faults these volumes exposed, each silently losing content:

1. **The margin rule.** It was a fraction of column width — 12% of a 306pt column is 36.7pt, while
   these volumes indent their text to 50pt, so every question start on their two-column pages was
   rejected (94 regions found of ~200). The rule is now the 10th percentile of the column's own
   line edges plus a tolerance, which also survives the centred-heading case that broke the
   previous rule. 2024 still parses 200 of 200.
2. **Worked solutions were inside the question region.** These are "Answers & Solutions" volumes, so
   each region carried the solution's prose, numbers and often its own diagram. Cutting the region
   at `Sol.` took the 2023 clean rate from 28% to 69% and `content_dropped` from 38 to 2 — and it
   stops a figure crop picking up the SOLUTION's diagram instead of the question's.
3. **A trailing "Answer" marker** was absorbed into option 4, which made 42 questions that agree
   position for position look rotated.

Note on the headline number: 2023's clean rate reads 69% against this volume where it read 87%
against the chapter-wise compilation. The lower figure is the better one — it is measured against
the actual paper for the actual code, and the earlier number was measured against a publisher's
reprint that matched only 109 of 200 questions.

Still wanted, and now worth asking for specifically: the same series for **2023 Code-E2** and
**2022 Code-Q1**, which are the other codes our records are keyed to. With those, every record in
both years could have its option order checked against its own code.

## 2026-10-21 — findings from the first papers_v2 difficulty and category runs

Raised by the agents themselves while rating 2015_A and reading 2016_X. Each is recorded here
rather than fixed silently, because each is a judgement someone else owns.

### `new_demand` exists in the schema and not in the vocabulary

`schemas/ECAT.json` permits `cognitive_demand: new_demand` (and `""`), but
`config/allowed_values.yaml` v0.3 does not list it, and that file is generated from
`RULEBOOK.md` by `build_allowed_values.py`. Every other axis has its escape hatch in BOTH places --
`new_type`, `new_format`, `new_shape`, `new_trap` -- so E4a looks like the odd one out.

**Default taken:** agents were told to follow `allowed_values.yaml`, so no rating has used
`new_demand`. Nothing is blocked. **The question for the owner:** should the rulebook define a
`new_demand` escape for E4a like the other four axes, or should the schema drop it? Adding it to
`allowed_values.yaml` by hand is not an option -- that file is generated, and a hand-edit would be
overwritten by the next build.

### Two source defects a reviewer has to settle, not a script

- **2016_X q156** -- the booklet keys option 2 (U1 > U2) and justifies it with
  "u ∝ T⁴ ∝ 1/λ⁴", which is not Wien's law. With the Wien constant the paper itself supplies,
  λ_max falls at exactly 500 nm, which makes option 3 correct. The recorded key contradicts the law
  the question is built on.
- **2015_A q045** -- stored key is 2 (sulphur dioxide), but in the self-reduction the stem names
  (2Cu2O + Cu2S -> 6Cu + SO2) SO2 is the PRODUCT and copper(I) sulphide is the reductant, which is
  option 1. Flagged `arguable_key` by two independent raters; no trap was written on either option,
  since a trap must not land on the key and which one is the key cannot be settled from our record.

Also flagged `arguable_key`: **2015_A q134** (three secure pairings strike options 1, 3 and 4,
leaving option 2, against a stored key of 4) and **2015_A q059** (option 1 is defensible if
"grandson" ranges over both F1 lines).

### 2016_X q192's crop is mis-cut and the question is not recoverable from it

`papers_v2/crops/2016_X/q192.png` holds the PREVIOUS question's worked solution. Question 192
survives only as one line clipped to the top few pixels of its glyphs at the bottom edge --
"A gas is compressed isothermally to half its initial volume. The same gas is compressed
separately" -- and no options are in frame. The read records that fragment with an explicit
`[crop cuts off here]` marker and an empty options object rather than inventing the rest. **The
boundary needs re-measuring for this question before it can be transcribed.**

### The crops are not answer-blind, and three steps depend on blindness

Every Vedantu crop prints `Solution: (n)` and the worked solution directly beneath the question.
B6V, E7V and ECAT are all meant to work without the answer, and their INPUT PAYLOADS do omit it --
but all three must open the crop when the text layer has lost a structure or a fraction, and the
printed answer is then unavoidably in frame. Several raters reported this explicitly and said they
did not use it, which is the right behaviour and is also the only safeguard currently in place.

**The fix is to trim the crop at the answer line for these steps.** The anchor already exists:
`cut_agent_figures.py` measures the first `Answer`/`Sol.` line below each question's start, which is
how 20 of 35 agent-reported figures on 2015_A were identified as the publisher's solution rather
than the question's own. The same measurement would cut an answer-free crop. Not done yet, and until
it is, blindness for those three steps rests on the agents' own discipline.


## The question crops carry the publisher's worked solution (2026-10-21)

**Found by:** QCA shards ab and ac, independently, while reading `papers_v2/crops/<paper>/qNNN.png`.

Every crop in this corpus is cut from a Vedantu reprint, and that reprint prints `Solution: (n)`
with the publisher's full working **directly beneath the options**, inside the question's own
region. So the crop shows the answer.

This matters because several steps are specified to work WITHOUT the answer, and their inputs are
carefully built answer-free:

- `b6-blind-solver` (B6V) -- the whole point of the step is an independent solve. A solver that can
  see the printed answer is not an independent source, and its agreement with the booklet proves
  nothing.
- `e7-difficulty-rater` (E7V) -- a rater who can see the answer reasons backwards from it, and the
  route to a known answer always looks shorter than the route a candidate has to find.
- `q-concept-approach` (QCA) -- same risk for `approach`.

Both QCA agents that reported it say they used the image only to confirm the stem, options and
figures, and recorded no value or option number from the printed solution. That is the right
behaviour and it is in their notes, but it is a promise rather than a guarantee.

**Default taken for now:** the briefs for these steps already say the answer must not be used, and
the agents are demonstrably following it, so no step was stopped. **The real fix** is to cut the
crop at the solution boundary -- `cut_agent_figures.py` already measures exactly that boundary for
figures (`solution_tops` / `solution_after`), so the measurement exists and is not being applied to
the question crop itself.

**Not yet decided:** whether to re-cut the whole corpus's crops (which changes every page's left
column, and the crops are also what a reviewer checks the extraction against -- the printed
solution is useful THERE) or to cut a second, solution-free crop for the blind steps only.


## Three findings from the D4V re-run (2026-10-21)

The re-run itself worked: of the first ten questions re-tested with `chapter_index` and
`search_this_file`, **seven moved from `not_at_all` or `partly` to `fully`**, and in every one of
those the deciding passage was absent from the original 15-passage shortlist and had to be fetched
from the book -- `BIO12L-CH04-P87` ("The son of a woman who carries the gene has a 50 per cent
chance of being colour blind"), `BIO12L-CH04-P67` (headed `4.5 PLEIOTROPY`), `BIO12L-CH04-P39`
(the ABO gene I alleles), `BIO12L-CH05-P20` (the only occurrence of "Chargaff" in the whole corpus).
What follows is what did NOT resolve, and why each one is a different kind of problem.

### 1. A fact printed as a TABLE cannot be quoted at all

`2015_A q104` -- "Mendel did not use: pod length" -- is settled only by **Table 4.1**, which NCERT
prints as art. Its placeholder passage `BIO12L-CH04-P11` carries empty text, so the words `axial`,
`flower position` and `pod length` occur nowhere in the book file. The agent proved from prose that
Mendel used pod shape and pod colour, but could not eliminate flower position.

**Fixed in part:** `chapter_index` now lists the empty placeholders as `printed_as_art` landmarks
(21 of them in this chapter alone), so an agent can tell "NCERT omits this" from "NCERT prints this
as a picture we have not read". **Not fixed:** the tables themselves. Step A2S transcribes table
blocks and has run for this chapter, so the content may be recoverable by feeding A2S output into
the passage text -- untested.

### 2. `Cell: The Unit of Life` is not in the corpus, and Molecular Basis questions need it

`2016_X q132` -- polysome -- searched 5.7 Translation and then the whole corpus. **`polysome` and
`polyribosome` occur zero times in any of the seven ingested book files.** The term belongs to the
ribosome subsection of Class XI *Cell: The Unit of Life*, and `BIO11L.jsonl` has no chapter 8 at all
(its chapters are 1-4, 6, 7, 10, 12-19). So the question is unprovable from the corpus regardless of
whether its chapter mapping is corrected. Two decisions pending: whether to ingest BIO11L ch5/8/9/11,
and whether a question whose fact lives in an un-ingested chapter should read `not_at_all` or a
distinct status meaning "outside the extracted corpus".

### 3. `2016_X q135` looks like a key defect, not an evidence gap

Statements (i), (ii) and (iii) are each stated word for word in 4.8.2. The keyed option requires
(iv) to be FALSE, but `BIO12L-CH04-P89` opens "Sickle-cell anaemia : This is an autosome linked
recessive trait...", which makes (iv) true as printed. By NCERT all four statements are correct and
no option says that; option 2 is as well supported as option 3. Either the stem's (iv) was
transcribed wrongly or the booklet's key is wrong. **Default taken:** the evidence packet records
`partly` with (iv) named in `missing`, and nothing adjudicates the key.

### Also: `2020_F1 q048`'s answer is recoverable

That item reached the agent with `answer_to_support` empty, and rather than erroring it evidenced all
four options from `BIO12L-CH04-P39` and reported that **option 1 is the wrong statement and
therefore the answer**. That is a usable answer for a paper whose printed answers are missing
entirely -- worth considering as a path for the other 352 questions of `2019_P1` and `2020_F1`,
alongside running `b6-blind-solver` over them.
