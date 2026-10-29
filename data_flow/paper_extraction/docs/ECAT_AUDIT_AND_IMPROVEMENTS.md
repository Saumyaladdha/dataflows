# Why the E1–E5 category rater was inaccurate, and how to fix it

**Audience:** an agent or engineer picking up the category-rating step. This document is
self-contained — you do not need the repository or the data to follow the reasoning. Every claim
that rests on a measurement says so, and §15 lets you re-derive all of them.

---

## 0. In plain words

The agent's job is to label each exam question: what type it is, what the student must produce,
what kind of knowledge it tests, how much thinking it needs, and which wrong options are traps.

It did that job properly. What surrounded it did not.

1. **We promised it information we never sent.** The brief says *"the question type has already
   been worked out for you."* It had not been. The agent didn't crash — it guessed and carried on.
   That is the whole root cause: when a field is missing, an AI doesn't raise an error, it fills
   the gap with something that reads just as confident.
2. **So it used a match-the-columns label on a ratio question.** Not carelessness. It had not been
   told what kind of question it was looking at.
3. **We gave it what each label means, but not what each label is *not*.** Like saying "a chair is
   for sitting" and never "a sofa isn't a chair." Everything looks like it fits something.
4. **The page reviewers check the work against prints the rule backwards.** Our rulebook has a
   column headed **"not"**; our code copies it into a box labelled **"requires."** People were
   grading against the opposite of the rule.
5. **Three safety checks couldn't run — and reported PASS.** They needed the fields from point 1.
   "Couldn't check" looked exactly like "checked and clean."
6. **Nothing double-checks this step.** Every other step in the pipeline has an independent
   second opinion. This one used to have two runs and a tie-breaker; when five steps were merged
   into one, that quietly disappeared.

**The evidence that the agent was fine:** 367 of 367 explanations follow the exact required
sentence shape, 35 of 37 labels are in active use, zero invented labels, zero forbidden phrasings.
That is an agent following orders precisely. The errors land exactly where the orders were wrong,
missing, or impossible to check.

**Fix order:** send the missing fields → fix the definitions page → make a blocked check say
BLOCKED → *then* re-rate. Rewriting the prompt first would be the fourth most useful thing to do.

---

## 1. What this step is

A NEET question is classified on five axes. The step that fills them is called **ECAT**, run by an
agent called `e-category-rater`.

| axis | what it records | example value |
|---|---|---|
| **E1** question type | the shape on the page | `match_the_lists`, `assertion_reason`, `plain_mcq` |
| **E2** answer format | what the student must produce | `pick_match_code`, `pick_order`, `pick_ratio` |
| **E3** content shape | what kind of knowledge is tested | `definition_term`, `reaction`, `trend` |
| **E4** thinking | the cognitive work demanded | `recall`, `application`, `calculation` |
| **E5** traps | per *wrong* option: why someone reaches for it | `wrong_pairing`, `neighbouring_fact` |

Two ideas carry most of the weight:

**A trap is not simply a wrong option.** It is a wrong option that a *prepared* student reaches
for, and the record must name the reach — the half-remembered rule, the plausible-but-wrong
operation. The agent must give the trap's **label**, the **option number** it lands on, and the
**route** that leads there. A trap that cannot be tied to an option and a route is not written
down.

**Questions are judged in groups, not in paper order.** An earlier version tagged one match-list
question `check_each_statement` and a near-identical one `elimination`, with no stated reason for
the difference. So the agent now receives several questions of the same type at once and must
justify any difference between them.

Everything above is sound design. What follows is about the machinery around it.

---

## 2. The chain, and the six places accuracy can leak

Accuracy is not a property of the agent. It is a property of a chain, and the chain is only as
good as its weakest link:

```
  1  SOURCE          the question, its options, its printed answer
          │
  2  PACKET BUILDER  assembles what the agent sees: question + already-decided fields
          │          (E1, E2, E3, polarity, whether the source is damaged)
  3  BRIEF           the instructions: the task, the rules, the output shape
          │
  4  AGENT           the judgement
          │
  5  CHECK           mechanical refusal of answers that break a stated rule
          │
  6  GLOSSARY → PAGE what a human reviewer reads the work against
```

Here is the finding that matters: **five of the six links were faulty, and link 4 — the agent —
was not one of them.**

| link | state | consequence |
|---|---|---|
| 1 source | partly damaged, known | fine — the damage is recorded elsewhere |
| **2 packet builder** | **drops every decided field** | the agent invents what it was meant to be given |
| **3 brief** | **claims those fields were supplied** | the agent has no way to know they are missing |
| 4 agent | follows the brief precisely | — |
| **5 check** | **3 of 7 rules cannot fire; returns PASS anyway** | errors pass as verified |
| **6 glossary** | **prints each rule's *opposite*** | reviewers validate against an inverted rule |

An agent cannot repair a chain it cannot see. That is why "write a better prompt" is the *fourth*
most valuable thing to do here, not the first.

---

## 3. Failure 1 — information starvation, and why it produces confident invention

### The mechanism

This is the most important idea in this document, and it generalises far beyond this step.

The packet builder for the current corpus emits essentially one field beyond the question text:
the correct answer. It does **not** emit E1, E2, E3, the task polarity, or whether the source is
known-damaged. The brief, meanwhile, opens with:

> *A SCRIPT has already carried the mechanical fields across and derived `task_polarity`,
> `review_status` and `key_checked_against`. Your job is the part that needs judgement.*

For the entire current corpus that sentence is false.

Now ask what an agent does with that. **It does not fail.** A language model handed an input that
is missing a field it was promised does not raise an error — it fills the gap, because filling
gaps is what it does. The question shape is obvious from reading the question, so the agent infers
E1/E2/E3 and proceeds.

And here is the damage: **the inferred values are indistinguishable from supplied ones.** They
arrive in the same fields, with the same confidence, and nothing downstream marks them. What was
designed as *script-derived fact* became *unverified agent judgement* for the whole corpus,
silently.

> **Transferable rule.** A missing input does not produce a visible error in an agent pipeline. It
> produces a confident invention. Therefore: either the builder guarantees the field, or the brief
> must say "this may be absent — derive it and mark it derived." Never promise an input you do not
> send.

### Why it destroyed the trap labels specifically

A trap label is defined *relative to a question shape*. `wrong_pairing` means **"one pair in a
match code is swapped."** For that label to be legal, the question must be a match code — which is
`E2_answer_form`, which was not in the packet.

So the agent applied `wrong_pairing` to a question asking for a **ratio** (`1:2:1`), where there
are no pairs to swap. It was not being careless. It was reasoning from a definition with its
precondition removed. Corpus-wide this happened **five** times; an external reviewer found two of
them by hand while checking only ten questions.

### Evidence

| field in the packet | old corpus (580 questions) | current corpus (404) |
|---|---|---|
| `E1_question_type` | 580 | **0** |
| `E2_answer_form` | 580 | **0** |
| `E3_content_shape` | 578 | **0** |
| `task_polarity` | 580 | **0** |
| `review_status` | 580 | **0** |
| answer | 580 | 398 |

### Fix

Make the builder emit those five fields. Then correct the brief's opening paragraph so it is true.
**Everything else in this document is secondary to this.**

---

## 4. Failure 2 — a vocabulary given without its boundaries

### The mechanism

Each of the five axes is a **closed vocabulary**: a fixed list of labels, intended as a partition.
The rulebook defines each label in two columns — what it **means**, and what it is **not**:

| label | means | not |
|---|---|---|
| `definition_term` | what a term or quantity means… | explaining why a thing behaves as it does |
| `structure_chemical` | the structure and bonding of a named species… | the transformation it undergoes |
| `reaction` | what a reagent does to a substrate… | why it goes that way |

The second column is what turns a list of labels into a *partition*. Without it, every label is
plausible for some reading of almost any question, and a classifier will over-apply — not from
carelessness, but because nothing told it where one label stops and the next begins.

The agent was shown the `means` column. It was not shown the `not` column.

> **Transferable rule.** A closed vocabulary needs negative definitions as much as positive ones.
> *"This, not that"* is what makes a label decidable. Supplying only `means` guarantees boundary
> errors and then makes them look like carelessness.

### The same bug, pointed at the reviewer

The rulebook's six tables do **not** share a header. Three are `| label | means | not |`. One is
`| label | means | required evidence |`. The glossary builder maps *column 3* to a field it calls
`requires` — **regardless of what the header says**.

So on the page a human reviews the work against, three of the five axes print the exclusion as a
requirement:

| label | the page says "requires" | what the rulebook's column actually is |
|---|---|---|
| `definition_term` | explaining why a thing behaves as it does | **not** |
| `structure_chemical` | the transformation it undergoes | **not** |
| `formula_or_law` | a stored number | **not** |

A reviewer checking a tag against that line is checking it against **the opposite of the rule**.
When the external reviewer reported that two E3 definitions "did not match the question", they
were reading this bug, not a tagging error.

A related instance: a definition that wraps onto a second line in the source file is truncated at
the line break, so every card using `elimination` displays the sentence *"name the one pair or fact
and the options it"* — cut off before "strikes out".

> **Transferable rule.** The definition the *reviewer* reads and the definition the *agent* follows
> must be generated from one source and verified against it. A reviewer validating against a
> corrupted rule produces corrections that are themselves wrong, and the error compounds instead of
> being caught.

---

## 5. Failure 3 — checks that cannot fire, and return PASS

### The mechanism

The check module enforces seven rules. Three of them depend on fields the packet builder stopped
sending (Failure 1). When the field is absent the rule has nothing to compare against — so it does
not fail, and it does not warn. **It passes.**

| rule | depends on | status |
|---|---|---|
| no trap on a question whose source is damaged | `review_status` | **cannot fire — 361 of 367 ratings** |
| no trap on the correct answer | the answer | cannot fire for 6 |
| every group member rated exactly once | packet membership | fires *within* a packet only |

Consider what a `PASS` means here. It does not mean "checked and clean". It means "could not
check", rendered identically to "checked and clean". A reviewer sees green and moves on. **Silent
abstention is worse than no check at all**, because no check leaves you uncertain, while a false
pass leaves you confident and wrong.

The codebase already learned this once. The check module's own comments record an earlier instance
— a rule that read only the old spelling of the answer field and therefore never fired on the new
corpus — described there as *"the worst kind of broken check."* The lesson was written down and
the shape recurred three more times, because the lesson was recorded as a comment rather than as a
mechanism.

> **Transferable rule.** Every check has three outcomes, not two: **PASS**, **FAIL**, and
> **BLOCKED — the input needed to evaluate this rule was absent**. A check that cannot distinguish
> the third from the first will eventually report safety it never verified. Make BLOCKED
> structurally impossible to ignore.

### The duplicate-rating consequence

Coverage is enforced *within* a packet. Two generations of packet builder both produced live work,
so three questions were rated **twice, by different packets, with different results and no
adjudication**. Which one gets published is decided by filename sort order.

One of those questions carries a verdict saying *the source is damaged, do not infer traps* and
**three traps**, which the rulebook forbids outright. The rule exists. The check for it could not
fire. The contradiction shipped.

---

## 6. Failure 4 — unfalsifiable fields drift toward whatever reads well

### The mechanism

Three of the agent's fields are prose: `concept`, `route`, `reason`. They are the most valuable
fields on the card — a teacher checking the work reads the route and nothing else — and **nothing
can check them**.

Fields that cannot be checked do not stay honest by themselves. They drift toward what reads
convincingly, because that is the only gradient acting on them. The specific drift here is
**overgeneralisation**: a true-about-this-question observation inflated into a general law.

Real examples found by an external reviewer:

| written in a route or reason | why it is false |
|---|---|
| "RNA is single-stranded" | double-stranded RNA exists — rotaviruses |
| "a pleiotropic gene has several *unrelated* effects" | unrelatedness is not required; one metabolic pathway suffices |
| "coding genes occur only in non-repetitive DNA" | repeats occur inside coding genes — the CAG repeat in *HTT* |
| a human genome size quoted as a universal | genome size varies enormously between organisms |

Measured across the corpus: **25** routes and reasons contain absolutes of this class.

Note *why* this happens. A trap route must explain a pull, and a general law is the most persuasive
kind of explanation available. The field's incentive is toward the sweeping claim, and no counter-
force exists. Compare the evidence step elsewhere in this pipeline, where every quoted line is
**re-found in the textbook word for word by a script** — a paraphrase cannot survive, which is what
makes "verified" mean something there. The category rater has no equivalent.

> **Transferable rule.** Any prose field that nothing verifies will drift. Either anchor it (quote
> a source and check the quote), constrain it (ban the construction that goes wrong), or review it
> (a second agent whose only job is to refute). Writing "be accurate" in the brief is not one of
> the three.

### A boundary the brief leaves implicit

The brief correctly forbids claims about student behaviour — *"a common error"*, *"most students"*
— because the project holds no response data, and an unfalsifiable claim about frequency is exactly
the kind of thing that cannot be reviewed.

But its own approved example reads *"A student who remembers only 'SN1 goes through a flat
carbocation' concludes the configuration is kept."* That is permitted, and should be: it names a
**route**, which is a property of the reasoning, not a claim about how often anyone takes it.

The distinction — *route allowed, frequency forbidden* — is correct and load-bearing, and it exists
nowhere as a rule. A reader has to infer it from one worked example.

> **Transferable rule.** If a rule has an exception that your own examples rely on, write the
> exception down. An inferred boundary will be inferred differently by the next reader.

---

## 7. Failure 5 — consolidation quietly removed the safeguards

E1–E5 used to be separate steps. Two of them carried independent verification:

| step | independent runs | disagreement handling |
|---|---|---|
| E4 · thinking (old) | **2** | **adjudicator** |
| E5 · traps (old) | **2** | **adjudicator** |
| **E1–E5 merged (now)** | **1** | retry only |

Merging the steps merged away the second opinion. This was almost certainly not a decision — it is
what happens when five things become one thing and nobody re-derives the safeguards.

It is worth seeing how unusual that leaves this step. Everywhere else in this pipeline, a judgement
is checked by something that disagrees with it independently:

- the question read from the page image is cross-checked against a second reading, with an
  adjudicator for mismatches;
- the publisher's printed answer is cross-checked by an agent that **solves the question having
  seen no answer at all**;
- every quoted textbook line is re-found in the book, word for word, by a script.

The category rater alone ships a single unreviewed judgement straight into the deliverable. An
external review of ten questions found substantive problems in most of them. That is not a
surprising result for an unverified single pass — it is the expected one.

> **Transferable rule.** When steps are merged, list the safeguards of each input step and
> explicitly re-adopt or consciously retire each one. Safeguards are the first thing lost in a
> refactor because they are not features and nothing breaks when they vanish.

---

## 8. Failure 6 — consistency was fixed; correctness was assumed to follow

Grouping was introduced to fix a real defect: similar questions getting different labels for no
stated reason. It worked. Judged as a group, similar questions now get similar labels and the
agent must justify differences.

But consistency and correctness are **different axes**. Grouping guarantees that similar questions
are labelled *alike*. It does nothing about them being labelled *wrongly* — and in fact a group
makes a single misreading propagate across every member of it, consistently.

The five label/shape mismatches of §3 are exactly this: internally consistent and uniformly wrong.

> **Transferable rule.** Agreement is not accuracy. A process that raises agreement without adding
> an independent correctness check will raise your confidence faster than it raises your quality.

---

## 9. Is the vocabulary itself sound? Mostly yes

The failures above are all machinery. The categories are a separate question, and they come out
well — which matters, because it means **this is a repair job, not a redesign**.

### What is healthy

| | |
|---|---|
| trap labels defined | 37 |
| **in active use** | **35** |
| trap instances recorded | 805 |
| `strategy_available` | 5 of 5 used |
| `solution_structure` | 3 of 3 used |
| `cognitive_demand` | 8 of 9 used |
| labels invented outside the allowed list | **0** |

A vocabulary where 35 of 37 labels earn their keep is a working one — neither bloated with dead
terms nor collapsed onto three favourites. Every E5 label also carries a *required evidence*
clause (`wrong_pairing` → "which pair, which option"), which is why E5 is the one axis the external
reviewer raised no definition complaints about: its rulebook table really is headed
`required evidence`, so the glossary bug of §4 does not touch it.

The vocabulary has also survived one honest cleanup already. Four v1 definitions were found
unsupportable and removed — among them `obviously_wrong`, defined as *"no student who read the stem
would be drawn to it"*, a claim about student behaviour that no amount of reading a paper can
establish.

### Gap 1 — one axis has no definitions at all

`strategy_available` has five values — `elimination`, `estimation`, `symmetry`,
`dimensional_check`, `unit_sanity`. **All five are in use. None has a written definition.**
`elimination` alone has been applied **119 times**. The rulebook carries them as a bare list rather
than a table, so the review page prints *"no definition in the rulebook"* in red beside every one.

This is the only place where the vocabulary is genuinely incomplete rather than merely
mis-displayed, and it is small: write the table.

### Gap 2 — two labels cannot currently be used

| label | why it is unused |
|---|---|
| `old_ncert_fact` | requires *"the change-log entry (Stage A), not an opinion"* — and Stage A has produced no change logs for these chapters. **Blocked on an upstream step, not a bad label.** |
| `no_elimination_route` | plausibly just rare — it needs all four options to be source terms of the same kind |

Neither is a reason to delete anything. `old_ncert_fact` should be recorded as *blocked*, so it is
not mistaken for a label nobody wanted.

### Gap 3 — some fine boundaries cannot be judged until §4 is fixed

Look at the two most-used neighbours on the trap axis:

> `other_one_fact` — a fact about a different member of the **same family** (another hormone,
> another organelle)
> `neighbouring_fact` — a fact about an adjacent concept, where the **families differ** rather than
> the members

That is a real and useful distinction, and a fine one — exactly the kind that stays sharp only if
you are shown the "not" column, which the agent was not. `other_one_fact` accounts for **19% of all
traps**, which is enough to warrant a re-check after the fix, though not by itself proof of
anything.

The external reviewer's two queries are the same class: is `definition_term` right for a question
asking a thing's *significance* rather than its *definition*? Does `structure_chemical` cover
nucleic-acid properties? Both are boundary calls, and neither can be settled while the page is
printing each rule backwards.

### Baseline distributions — keep these, to compare after the re-run

```
cognitive_demand    recall 45% · calculation 20% · application 19% · rest 16%
solution_structure  single_step 53% · independent_checks 24% · multi_step 21%
traps               top 3 labels = 37% of 805 instances
strategy            elimination 119 · estimation 18 · dimensional_check 8 · unit_sanity 7 · symmetry 3
```

Nothing alarming here. 45% recall is plausible for a Biology-heavy sample, and all of it comes from
**2 papers out of 10** — so thin values such as `dimensional_reasoning` (used once) are a coverage
artefact, not a design flaw. They are Physics labels, and Physics is barely in the sample.

---

## 10. What good looks like

Pulling the rules together, a rating step that is accurate by construction has six properties:

1. **Every decided field is supplied, never inferred** — and where inference is unavoidable, the
   output marks the field as inferred so nothing downstream mistakes it for fact.
2. **Every label arrives with its boundary** — `means` *and* `not` — and the definition the agent
   follows is generated from the same source as the definition the reviewer reads.
3. **Every prose claim has a machine-checkable companion.** If a route says *"swapping rows c and
   d yields option 3"*, the output carries that transformation in a structured field, a script
   applies it, and the claim is confirmed or refused. Prose persuades; structure verifies.
4. **Every check reports BLOCKED when it cannot run**, and a BLOCKED is as visible as a FAIL.
5. **Every judgement meets an independent challenger** — not a re-rater, which tends to agree, but
   a **refuter** whose only job is to find the flaw, returning `{confirmed, which_field, why}`.
6. **"Unsure" is cheap, legible and distinct from "not yet done".** An agent that cannot decide
   must have an answer that costs it nothing, or it will guess — and a guess is indistinguishable
   from knowledge once written down.

---

## 11. What NOT to change

Over-correction is the likeliest way to make this worse. Six things to leave alone:

1. **Do not redesign the vocabulary.** §9 measured it: 35 of 37 labels in use, zero invented. The
   labels are not why the output was wrong.
2. **Do not delete the two unused labels.** One is blocked on an upstream step; one is rare. An
   unused label costs nothing; a missing one forces a wrong fit.
3. **Do not rewrite the brief first.** It is a good brief. Fix the input it describes, then make
   the four small additions in §12 — not a rewrite.
4. **Do not "improve" the agent's output style.** 367 of 367 reasons already follow the required
   shape. That constraint is working; changing it would cost the one thing that is reliable.
5. **Do not re-rate anything before P0 lands.** Re-rating against an inverted definition produces
   *different* wrong answers, not better ones.
6. **Do not extend to the remaining eight papers yet.** The cost of re-running 358 ratings is
   small; the cost of re-running 1,869 is not.

---

## 12. The plan, in priority order

### P0 — harness repairs. No agent re-runs. Roughly a day.

1. **Make the packet builder supply E1, E2, E3, `task_polarity` and `review_status`**, as the
   earlier builder did. Everything else is downstream of this.
2. **Correct the brief's opening paragraph** so it describes the input actually sent.
3. **Fix the glossary column mapping** — read each table's header rather than assuming column 3 is
   a requirement; render the `not` column on the page as *"not this: …"*; join wrapped lines before
   extracting, which also fixes the truncated definition.
4. **Write the `strategy_available` definition table** (§9, Gap 1) — five labels, 155 uses between
   them, no definitions today.
5. **Retire one of the two packet builders** and adjudicate the three double-rated questions
   instead of letting filename order decide.
6. **Add a BLOCKED outcome to the check module** and return it wherever a required input is
   absent.
7. **Mark `old_ncert_fact` as blocked-on-Stage-A**, so an unusable label is not read as an
   unwanted one.

### P1 — new checks. Roughly a day. Catches six known failure modes permanently.

8. **Verify the claimed derivation.** Require a structured transformation beside the prose route;
   apply it; assert the result matches the printed option it claims to produce.
9. **Enforce label/shape compatibility.** Declare which question formats each label is legal for;
   refuse the rest.
10. **Detect cross-axis contradiction** — e.g. a rating that lists `elimination` as available while
    its prose says no elimination route exists.
11. **Require option claims to quote the option.** Any statement about what an option *says* must
    quote text that appears in it.
12. **Detect duplicates across packets**, not only within one.

### P2 — brief and schema. Half a day.

13. **Add a no-generalisation rule:** a route explains *this* option in *this* question and must
    not state a general law; where a general fact is load-bearing, quote a source for it.
14. **Write down the route/frequency boundary** that the brief currently only implies.
15. **Add an `assumptions` field** so an answer that holds only under an unstated reading says so,
    and the verdict can read *agrees under assumption* rather than a bare *agrees*.
16. **Pass both `means` and `not`** to the agent once the glossary is fixed.

### P3 — structure.

17. **Add a refute-only second pass** (§10.5). This is where the false general claims would have
    been caught.
18. **Land `x-brief-auditor` as a running step** (§14) — the brief and schema exist; it needs a
    `steps.yaml` entry, an input-packet plugin and a check.
19. **Split "verified" into four independent statuses** — the source quote is genuine / the answer
    is right / the question is unambiguous / the tags are sound. One flag covering four claims is
    how a real quotation ends up validating a wrong difficulty rating.

### P4 — coverage and review.

20. **Re-rate the 358 existing ratings** once P0 and P1 land. They were made without the shape
    fields their labels are defined against, so they are a pilot, not data.
21. **Re-check the `other_one_fact` / `neighbouring_fact` boundary** (§9, Gap 3) against the
    re-rated set, now that the agent can see where one stops.
22. **Only then extend to the remaining eight papers.**

---

## 13. How to tell the fix worked

Run the audit in §15 after each stage. These are the numbers to expect.

| measure | today | after P0 | after P1 | after P3 |
|---|---|---|---|---|
| packet questions carrying `E1`/`E2`/`E3` | 0 of 404 | **404** | 404 | 404 |
| ratings where the damaged-source rule cannot fire | 361 | **0** | 0 | 0 |
| checks reporting PASS without evaluating | 3 rules | **0** | 0 | 0 |
| label/shape mismatches | 5 | 5 *(not yet re-rated)* | **0 — refused at check time** | 0 |
| questions rated twice, unadjudicated | 3 | **0** | 0 | 0 |
| labels with no definition on the page | 5 | **0** | 0 | 0 |
| axes showing the inverted column | 3 of 5 | **0** | 0 | 0 |
| sweeping general claims | 25 | 25 | 25 | **falling — measure it** |

Two cautions on reading that table:

- **P0 does not reduce the mismatch count.** It makes the mismatches *impossible to repeat*; the
  existing five stay until the re-rate in P4. Do not read a flat number as a failed fix.
- **The general-claims count is the only measure of §6**, and a regex counting the word "always"
  cannot tell a correct absolute from a false one. Treat a falling count as encouraging, never as
  proof. The real test is the refuter in P3.

Two things are not measurable by script and need a person: whether a trap route actually names a
*pull* rather than restating the error, and whether a `concept` is written in words a student could
revise from. Sample ten of each per paper.

---

## 14. A step that finds this class of problem by itself

Everything above was found by hand, once. That is the wrong shape for it. The six failures are not
one-offs peculiar to this step — they are **kinds**, and each will recur in the next brief anyone
writes. A promised-but-absent field, a definition without its boundary, a rule no script can
enforce: these recur because the conditions that produce them recur.

So the audit is now itself a step.

**`x-brief-auditor`** — brief at `agents/x-brief-auditor.md`, output schema at
`schemas/XAUDIT.json`. It audits a step's **instructions** against the outputs they produced, and
returns the text that replaces each instruction that failed.

### What it is given

The step's brief, its codebook, its schema, its check — and a sample of outputs **paired with the
exact input each one was produced from.**

That pairing is the method, not a convenience. An output field with no corresponding input field is
the signature of `promised_input_absent`, which is the root cause in §3 — and it is **invisible if
you read either side alone**. A reviewer reading only outputs sees a careless agent. A reviewer
reading only the brief sees a reasonable document. The fault is only visible in the gap between
them.

### What a finding must contain

Four things. A finding missing any of them is not written down.

1. **The instruction, quoted** from the brief character for character — so a reader can find it.
   Where the failure is an *absent* instruction, quote the nearest passage that should have carried
   it.
2. **At least one real output that demonstrates it** — item id, field, the actual value. An
   imagined example is a guess.
3. **The cause**, from the closed list in §2–§8: `promised_input_absent`, `missing_boundary`,
   `unverifiable_instruction`, `implicit_exception`, `contradiction`, `no_escape_hatch`,
   `wrong_owner`, `instruction_was_correct`.
4. **Exact replacement text** — the words that go in the file, not a description of a change.

### The rule that does the most work

Every finding says *where* the fix belongs: `brief`, `packet_builder`, `codebook`, `schema` or
`check`. And:

> **If a script could detect the failure, the fix belongs in `check`, not `brief`.**

This is the rule prompt audits break most often, because adding a sentence to a prompt is easy and
writing a check is work. **A prompt rule nobody enforces is a wish.**

The worked case is §3's. A trap label meaning *"one pair in a match code is swapped"* was applied
to a ratio question. The tempting fix is a sentence in the brief: *"check the label suits the
question type."* The correct fix is two, and neither is in the brief: the packet builder must
supply the question type, and the check must refuse that label where the type is not a match code.
**The brief needs no new sentence at all.**

### What it is forbidden to produce

These are the failure modes of prompt audits, and each is worse than silence because it looks like
work and changes nothing:

- *"be more careful"*, *"improve accuracy"*, *"add more detail"*, *"consider doing X"*. The test
  that catches all of them: **if your replacement text would make sense in a brief for a different
  step, it is not specific enough.**
- advice with no quoted instruction;
- a finding supported only by reasoning about what an agent *might* do;
- blaming the agent for an instruction it followed;
- rewriting the whole brief, which destroys what works and makes the change unreviewable.

### Two things that keep it honest

**`instruction_was_correct` is a legal verdict** and the brief insists on it. An audit that blames
the brief for everything is as useless as one that blames the agent for everything. Sometimes the
instruction was right, clear and checkable, and the agent erred or the source was damaged — say so.

**A `working` list is required** — instructions checked and found sound, each with its evidence
(*"every output used the required sentence shape; 367 of 367"*). This is not politeness. It is what
stops the next person rewriting a constraint that was holding the output together, and it is how a
reader knows what was actually examined.

Findings are ordered by `outputs_affected` — **counted, never estimated**, since it is the only
ranking signal available.

### Output

```json
{
  "step": "ECAT",
  "findings": [
    {
      "id": "F1",
      "cause": "promised_input_absent",
      "fix_in": "packet_builder",
      "instruction_quoted": "A SCRIPT has already carried the mechanical fields across …",
      "evidence": [{"item_id": "2016_X#q100", "field": "traps[0].label",
                    "value": "wrong_pairing",
                    "why_it_shows_the_failure": "the label is defined as 'one pair in a match code is swapped' and this question asks for a ratio; the input carries no E2_answer_form, so the agent had nothing to test it against"}],
      "replacement_text": "The packet builder must emit `E1_question_type`, `E2_answer_form`, `E3_content_shape`, `task_polarity` and `review_status` on every question …",
      "outputs_affected": 404
    }
  ],
  "working": [
    {"instruction_quoted": "`reason` uses the rulebook's fixed shape …",
     "evidence": "367 of 367 outputs follow it exactly"}
  ]
}
```

`findings` may be empty. Finding nothing is a valid answer and is better than inventing one.

### What it still needs before it runs

The brief and schema exist. Three pieces do not:

1. an `XAUDIT` entry in `config/steps.yaml`;
2. a plugin that builds the input packets — the join of outputs to the inputs that produced them;
3. `code/checks/XAUDIT.py`, enforcing what a schema cannot: that every `instruction_quoted`
   actually appears in the brief, that every `item_id` exists, that findings are ordered by
   `outputs_affected`, and — the important one — that `fix_in: brief` is not used for something a
   script could check.

That last check is the auditor auditing itself against its own central rule, which is the right
place for it.

---

## 15. The measurements, and how to re-derive them

All figures are from the ratings on disk, joined to the packets the agent was given.

| | measured |
|---|---|
| ratings audited | 367 |
| questions in the corpus | 1,869 |
| questions rated | **358 — 19%**, covering **2 papers of 10** |
| packet questions carrying `E1_question_type` | **0 of 404** |
| packet questions carrying `review_status` | **0 of 404** |
| ratings where the damaged-source rule cannot fire | **361 of 367** |
| ratings where the no-trap-on-the-answer rule cannot fire | 6 |
| trap labels applied to a shape their definition excludes | 5 |
| sweeping general claims in `route` or `reason` | 25 |
| questions rated twice by different packets, unadjudicated | 3 |
| rulebook tables whose `not` column is published as `requires` | 3 of 6 |
| trap labels defined / in use | 37 / 35 |
| `strategy_available` labels defined / documented | 5 / **0** |

### What the agent got right

Worth stating plainly, because it narrows the work and because it is the evidence for this
document's central claim:

- **367 of 367** reasons use the rulebook's required sentence shape.
- **35 of 37** available trap labels are in active use.
- Both non-trap verdicts are being applied where intended.
- Exactly **one** blank judgement field, and it carries a note explaining itself.
- **Zero** labels invented outside the allowed list.
- **Zero** forbidden frequency claims survived the existing check.

This is what a well-behaved agent looks like. The failures sit precisely where the instructions
were wrong, absent, or unverifiable — which is the argument for fixing the harness before
rewriting the prompt.

### Re-audit script

Run from the `paper_extraction/` directory. Expected output on today's data is given below it.

```python
import json, glob, re, collections
inp = {}
for p in glob.glob('steps/ECAT/work/*.input.json'):
    for q in (json.load(open(p, encoding='utf-8')).get('questions') or []):
        inp[q.get('question_id')] = q
rat = []
for p in sorted(glob.glob('steps/ECAT/out/*.json')):
    rat += (json.load(open(p, encoding='utf-8')).get('ratings') or [])

GEN = re.compile(r"\b(always|never|in all cases|universally"
                 r"|all (RNA|DNA|genes|proteins|cells|organisms)"
                 r"|every (gene|cell|organism|RNA|DNA))\b", re.I)
d = collections.Counter()
for r in rat:
    q = inp.get(r.get('question_id'), {})
    e2 = q.get('E2_answer_form') or r.get('format') or ''
    ans = str(q.get('official_answer') or q.get('correct_answer') or '').strip()
    if not str(q.get('review_status') or '').strip(): d['damaged-source rule cannot fire'] += 1
    if not ans:                                       d['answer rule cannot fire'] += 1
    for t in (r.get('traps') or []):
        lab = t.get('label')
        if lab == 'wrong_pairing' and e2 != 'pick_match_code':      d['label/shape mismatch'] += 1
        if lab in ('sequence_endpoint_or_adjacency', 'reversed_order') and e2 != 'pick_order':
            d['label/shape mismatch'] += 1
        if GEN.search(str(t.get('route') or '')):                   d['sweeping general claim'] += 1
    if GEN.search(str(r.get('reason') or '')):                      d['sweeping general claim'] += 1
seen = collections.Counter(r.get('question_id') for r in rat)
d['rated more than once'] = sum(1 for v in seen.values() if v > 1)

print(len(rat), 'ratings')
for k, v in d.most_common():
    print('%-34s %4d' % (k, v))
```

```
367 ratings
damaged-source rule cannot fire     361
sweeping general claim               25
answer rule cannot fire               6
label/shape mismatch                  5
rated more than once                  3
```

Worth landing as a script that runs on every build, so these numbers stay honest rather than
needing an audit to rediscover.

---

## 16. The six rules, collected

If you take nothing else from this document:

1. **A missing input produces a confident invention, not an error.** Never promise an agent an
   input you do not send.
2. **A closed vocabulary needs its negative definitions.** *This, not that* is what makes a label
   decidable.
3. **Every check has three outcomes.** PASS, FAIL, and BLOCKED — and BLOCKED must never render as
   PASS.
4. **Unverifiable prose drifts.** Anchor it, constrain it, or have something refute it.
5. **Merging steps merges away their safeguards.** Re-derive them deliberately.
6. **Agreement is not accuracy.** Consistency mechanisms raise confidence faster than quality.
