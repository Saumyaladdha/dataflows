# D4 · link_type and quoting — codebook

## STATUS — read this first

- **Drafted by the pipeline, not written by the owner.** Claude Code wrote this on 2026-10-12 from `docs/SPEC.md` 12/D4, 2.4, 17.1 and 12/D6, `.claude/agents/d4-evidence-quoter.md`, `scripts/checks/D4.py`, `scripts/step_plugins.py` (D4's plugin), and the real Stage-D findings in `docs/OPEN_QUESTIONS.md`.
- **Not approved by the owner.** SPEC 13.0 reserved codebooks for the owner because a wrong codebook silently mis-tags the whole bank. The owner has since asked the pipeline to draft them. Treat this as a proposal.
- **This file is live the moment it exists.** `D4Plugin` reads `codebook/D4_link_type.md` off disk and passes its full text to `d4-evidence-quoter` as the `codebook` field. Before today there was no such file and the agent received only five one-line definitions. **Every D4 output produced before this file existed was produced without it** — it should be re-run (the `codebook_file` cascade in `config/cascade.yaml` covers exactly this).
- **If the owner disagrees, change this file.** Editing it changes its hash and re-triggers that cascade.
- This file overrides the one-line definitions in `config/allowed_values.yaml`. It does **not** add values: `link_type` has exactly five, and there is no `new_…` escape. If none fits, pick the closest, say why in `note`, and let the flag carry it.

---

## 1. Decide in this order

1. **First decide HOW the question connects to NCERT** (`link_type`). The quoting follows from that choice, not the other way round.
2. **Then copy the exact lines** the chosen type requires.
3. **Then write the derivation steps**, if any.
4. **Then judge `supports_answer`** against what you actually quoted.

Deciding `link_type` after quoting is how questions end up `beyond_ncert_method` — you run out of quotes and reclassify. §5 exists to stop that.

---

## 2. The five values

| Value | Use when | What you quote | Real example |
|---|---|---|---|
| `states_answer` | One NCERT line **states** the answer | that line | Kepler's T ∝ R^{3/2} (`2026-Jun#14`) |
| `rule_used` | One NCERT rule **plus plain maths** | the rule | terminal voltage V = E − Ir (`2026-May#21`); the stretched wire (`2013#15`) |
| `rules_chained` | **Two or more** NCERT rules, one after another | one quote **per rule** | photon vs electron momentum (`2026-Jun#19`); black-hole radius from escape speed (`2014#11`) |
| `concept_applied` | NCERT explains the idea; the question applies it to a new case **without calculation** | the concept line | metre bridge with cell and galvanometer interchanged (`2026-May#22`) |
| `beyond_ncert_method` | Needs a result or method NCERT does **not** give | the NCERT rules involved, if any, plus a `note` naming what is missing | field at the centre of a loop split into unequal arcs (`2026-Jun#11`) |

### `states_answer` vs `rule_used`
Does an NCERT sentence contain the answer, or does it contain a rule you then have to *use*? Most Biology is the first; most Physics is the second. Measured on 28 real Physics questions from the 2026 papers: ~14% `states_answer`, ~40% `rule_used`, ~30% `rules_chained`, ~11% `concept_applied`, ~5% `beyond_ncert_method`. Use that as a calibration check on a batch, never as a reason for a single tag.

**`states_answer` takes no derivation steps.** That is a hard check, not a convention. If you need a step, the type is not `states_answer`.

### `rule_used` vs `rules_chained`
Count the **distinct NCERT rules** the solution consumes. One → `rule_used`. Two or more → `rules_chained`, with **one quote per rule**. The checks enforce this: `rule_used` needs ≥ 1 quote with `for: "rule"`, `rules_chained` needs ≥ 2.

Do not inflate: algebra, arithmetic, unit conversion and substitution are **not** rules. Rearranging V = E − Ir is not a second rule. Converting cm to m is not a rule.

Do not deflate either: if the solution needs both "the field of a circular loop" and "resistors in parallel", those are two rules and `rule_used` is wrong.

### `concept_applied` vs `rule_used`
`concept_applied` means **no calculation happens**. The moment you compute a value, it is `rule_used` or `rules_chained`. The metre-bridge-interchanged case is the model: NCERT explains the balance condition, the question moves it to a rearranged apparatus, and nothing is computed.

### `rules_chained` vs `beyond_ncert_method` — THE ONE THAT GOES WRONG

**SPEC warns that agents overuse `beyond_ncert_method`.** It is the single most over-claimed value in this step, and claiming it has real consequences (§5).

**An unfamiliar story is not beyond NCERT.** The spec's own worked case: deriving a **black hole's radius from escape speed** (`2014#11`) is `rules_chained`, **not** `beyond_ncert_method`. Black holes are not in NCERT. Escape speed is. The question chains NCERT's escape-speed expression with the condition that the escape speed equals c — both steps are NCERT rules plus algebra. The exotic subject matter is scenery.

The test is **not** "is this topic in NCERT". The test is **"does the solution need a result or method NCERT never gives?"**

- Needs a **standard NCERT rule applied to an odd object** → `rules_chained` (or `rule_used`).
- Needs a **formula NCERT never states** (the field of a circular *arc*, as opposed to a full loop) → `beyond_ncert_method`. That is the real distinction in SPEC's own pair of examples: the full loop is in NCERT, the arc is not.

**Before you may write `beyond_ncert_method`, all four must hold:**
1. You can **name** the specific missing result or method in `note` — "the field of an arc is not given in NCERT", not "this is beyond the syllabus".
2. You have **still quoted** every NCERT rule the solution does use. `beyond_ncert_method` with empty evidence is almost always a mislabel.
3. The gap is a **method**, not a topic you personally find unfamiliar.
4. The gap is **not** "the passages I was given do not contain it" — see §3.

If any of the four fails, the type is one of the other four.

---

## 3. MISSING PASSAGES ARE NOT "BEYOND NCERT"

You are given only D3's shortlist (5–15 latest-edition passages, capped and ranked). A line that is in the book but not in your shortlist is **not** absent from NCERT.

This is not hypothetical. Stage A has indexed **2 of 13 Biology chapters and zero Physics or Chemistry chapters.** Confirmed on real data: B8's real run on `Q-000004` (a rotational-motion Physics question) received 15 passages, **all Biology**, and correctly returned no supporting quote rather than forcing a match. Real `Q-000015` reached D3 with a guessed subtopic that had no linked passages at all and correctly **blocked** with `D3_NO_PASSAGES`.

**When the passages given cannot support the answer:**
- Set `supports_answer: "not_at_all"` with `evidence: []`, or `"partly"` with whatever is genuinely there.
- List what is unsupported in `missing`.
- Say in `note` that the needed material is not among the passages supplied.
- **Pick the `link_type` the question actually has**, judged on how the physics or biology works — not on what you could quote. A Physics numerical with no passages available is still `rule_used`; it is `rule_used` with `supports_answer: not_at_all`.
- **Never** use `beyond_ncert_method` for this. `D4_NO_SUPPORT` (normal) is the honest flag; `D4_BEYOND_NCERT` makes a false claim about the textbook.

**Why it matters downstream:** D6's status rule 4 sends `beyond_ncert_method` to `outside_ncert` with note type `outside_rules`, which raises `D6_NOTE_APPROVAL` and tells a reviewer — and eventually a student — that a question is off-syllabus. SPEC 2.4 is explicit: *never mark a question `outside_ncert` only because no sentence states the final number.* Conversely, D6 rule 0 means a correctly-tagged `rule_used` / `rules_chained` / `concept_applied` with one verified rule quote lands at `latest_ncert`, which is the right answer for the large majority of Physics.

---

## 4. The quote rules — these are checked mechanically

Each `exact_line` must survive `quote_verify.find` against the passage it names. The plugin **independently re-verifies every quote and never trusts your claim.** A failed quote is retried once ("Quote N not found in passage P; copy exactly"), then dropped, with `supports_answer` downgraded and `D4_QUOTE_NOT_FOUND` (high) raised.

1. **One continuous span, from ONE passage, per quote.** Never join pieces from two places. Never stitch two sentences that are not adjacent.
2. **The shortest span that states the fact or rule** — usually one sentence or one equation. Not the paragraph around it.
3. **No ellipses inside a quote.** Ever. If you need two separated spans, that is two quote entries.
4. **Word for word, character for character.** No rewording, no fixing typos, no expanding abbreviations, no normalising symbols, no translating. A paraphrase is a failure, not a near miss.
5. **Only from the passages you were given.** Never from memory, and never a passage id you were not handed.
6. **One quote per statement, for statement questions** — including **the line that shows a false statement is false**. A statement question marked `supports_answer: "fully"` is checked for a quote per statement; a `fully` with three quotes for four statements will fail.
7. **One quote per pair used, for match questions.** Use the `for` label to say which: `"List I-P matches List II-2"`.
8. **`for` labels** say what each quote supports: `"answer"`, `"rule"`, `"statement A"`, `"statement C is false"`, `"List I-P matches List II-2"`. `rule_used` and `rules_chained` **must** have `for: "rule"` quotes — that is what the check counts.

### `derivation_steps`
- **Only** algebra, arithmetic, unit conversion or logic. Nothing else.
- **A step that needs a physics or chemistry fact needs its own quote** — or the type is `beyond_ncert_method`. This is the rule that keeps a hidden extra rule from sneaking in as "a step".
- **The last step must end at the answer value.**
- **Write the last step so the final value comes after the last `=`.** The derivation cross-check (`scripts/checks/D4.py`) parses the number **after the last equals sign** in the last step and compares it with the answer option's value (and with B6's working when present). A mismatch raises `D4_DERIVATION_MISMATCH` (normal). So `"R' = rho(2l)/(A/2) = 4R = 16 ohm"` parses correctly; a step that trails off after the number does not. (This parser was itself a real bug: the first version took the *first* number in the step and read `"x = 2*3 = 6"` as `2`.)
- **Empty for `states_answer`.**

### `supports_answer`
- `fully` — every needed part **and every rule used in the steps** is quoted.
- `partly` — some of it is. Raises `D4_PARTLY` (normal).
- `not_at_all` — none of it is, with `evidence: []`. Raises `D4_NO_SUPPORT` (normal).
- `partly` is a legitimate verdict, not a failure, and must never be inflated to `fully` to avoid a flag. The plugin raises these flags on the **final verified** value, independently of your claim, so inflating it only produces a quote-verification failure as well.

---

## 5. Where this draft is genuinely uncertain

1. **The four-part gate on `beyond_ncert_method` (§2) is mine.** SPEC gives the definition, the warning that agents overuse it, and two worked examples. The gate is my attempt to make the warning operational. It is deliberately strict — the asymmetry is intentional, because a false `beyond_ncert_method` makes a public claim that a question is off-syllabus, while a false `rules_chained` only produces a missing quote that the checks will catch.
2. **`rule_used` vs `rules_chained` when NCERT states a composite rule.** If NCERT itself writes the chained result as one expression, that is one quote and `rule_used`. I believe that is right but no real case has been checked.
3. **`concept_applied` has only one worked example** in the whole corpus (`2026-May#22`), and it is a Physics apparatus case. Its ~11% share suggests there are many more shapes it should cover.
4. **No real D4 agent run exists.** D4 was never dispatched for real — `Q-000015` blocked at D3 first, and the five Physics/Chemistry questions blocked at D1. D4's code was exercised only against hand-built fixtures over real NCERT passage text (`BIO12L-CH03-P14`). Every example in this file comes from SPEC's own real-paper analysis, not from a verified D4 output.
5. **Whether `link_type` distribution differs by subject as sharply as SPEC 2.4 claims** has not been re-validated against the 2016–2025 sample the way E1–E6 were (noted in `docs/MASTER_PLAN.md` §5). The percentages in §2 come from 28 Physics questions of the 2026 papers only.

## 6. Proposals for the owner

- **No new `link_type` values proposed.** The five cover the real distribution, and the measured risk is `beyond_ncert_method` overuse, not a missing category.
- **Consider making `beyond_ncert_method` require a non-empty `note`** as a mechanical check, not just an instruction. §2's gate item 1 is the single cheapest guard against overuse and is currently unenforced.
- **Re-run every existing D4 output** now that this file exists (§STATUS). There is little to re-run today, which makes now the cheapest possible moment.
- **NCERT Exemplar as an extra source** (SPEC Section 20 #7, still undecided) would convert some genuine `beyond_ncert_method` questions into linked ones. Relevant here: the ~5% `beyond_ncert_method` share is partly a function of which books count as NCERT.
