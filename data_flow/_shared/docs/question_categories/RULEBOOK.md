# Question category rulebook · v2

One place where every label is defined, so wording cannot drift between the workbook, the sheet and
whoever is tagging. Supersedes the definitions embedded in `exports/discovery/CATEGORIES.xlsx`.

## Which artefact governs what

Seven files describe "the categories", written at different times by different scripts. Three are
authoritative and four are inputs or history. Without this map a reader cannot tell which is stale,
and a trap total was once reported from the 55-row showcase as though it described the corpus.

| artefact | status | authoritative for |
|---|---|---|
| **this file** | **live** | every label's definition, tie-break and required evidence |
| **`SHEET_V2.csv`** | **live** | the per-question classification, all 580 |
| **`categories.csv`** | **live, different purpose** | 15 composite *teaching* categories with four-step solving recipes. Its `question_type` / `content_shape` / `trap_mechanism` columns are **prose, not axis labels** — do not reconcile them against the axes. Its counts overlap by design and are hand-written (SPEC Rule 23) |
| `QUESTIONS.xlsx` | input | the v1 applied tags over 580 questions — what the corpus actually carries |
| `CATEGORIES.xlsx` | history | the v1 codebook. Its definitions are carried into this file; its `Total` column disagrees with the corpus on 28 labels and must not be cited |
| `clusters_pass_b/*.json` | input, unreconciled until now | 57 trap devices discovered per subject, folded into §5 |
| `QUESTIONS_SHOWCASE.xlsx` | history | 55 of the 580. Useful only because it is the subset whose tags carry reasons |

`scripts/checks/category_label_census.py` and `scripts/checks/category_sheet_reconcile.py` check
this map holds. Every count in this file comes from them; none is typed.

Every label below carries four things, because a definition alone has not been enough:

- **Means** — what must be true of the question for this label to apply.
- **Not** — a nearby case it must NOT be used for.
- **Tie-break** — which label wins when two could apply.
- **Evidence** — what the tagger must be able to point at in the stem or options.

## 0. Rules that apply to every axis

1. **One primary label per axis.** A second label is a `secondary_*` field, never a second primary.
   A question is not two question types because it has a figure.
2. **Reason in a fixed shape:** *"This question requires ___, demonstrated by ___."* The second blank
   quotes the stem or an option. A reason that describes students rather than the question is not a
   reason — "a student who memorised nothing can still reach the answer" says nothing about this
   question.
3. **No label about student behaviour.** We hold no response data. Frequency claims ("a common
   error") and plausibility claims ("no student would pick this") cannot be established by reading
   the paper, and must not be asserted as if they could.
4. **Every E5 trap names one option and the mistake that lands there.** A trap tag that does not say
   "option 2, reached by using ½LI instead of ½LI²" is not actionable and should be omitted.
5. **No trap or mechanism label where the source is incomplete.** If the figure, an option or the
   equation is missing, the question gets `review_status: source_incomplete` and E4/E5 stay empty.
   A clean classification cannot compensate for a question that is not all there.
6. **Fix the question and the key before finalising tags.** Tagging a question whose stem lost a
   digit produces a confident wrong classification — see §4.
7. **Tag similar questions together**, not in paper order: all match-lists, then all numericals, then
   all assertion–reason. Equal demands get equal labels, or the reason says why not.

## 1. E1 · Question type — the shape on the page

What the question LOOKS like, decided from layout alone. Nothing about difficulty or method.

| label | means | not |
|---|---|---|
| `plain_mcq` | a question and four answers, no lettered items, no lists, no scheme | anything with A/B/C or I/II |
| `match_the_lists` | two labelled lists to pair, answer is a pairing code | a single list to order |
| `arrange_in_order` | items to sequence, answer is an order | a pairing |
| `assertion_reason` | labelled Assertion and Reason, options about truth and explanation | two statements NOT labelled A/R |
| `statement_i_ii` | exactly two statements, labelled I/II or Statement I/II | three or more |
| `list_of_statements` | three or more lettered statements, answer selects a subset | exactly two |
| `figure_to_read` | the question cannot be answered without reading a figure | a figure that only decorates |
| `diagram_labelled` | a figure with labels, the answer names one | a figure read for a value |
| `graph_options` | the four OPTIONS are graphs | a graph in the stem |
| `structure_options` / `reaction_options` | the four OPTIONS are structures / reactions | a structure in the stem |
| `reaction_scheme` | a multi-arrow scheme in the stem | one reaction |
| `multi_part_respectively` | several blanks answered together ("respectively") | one blank |
| `fill_in_blank` | a printed blank in the stem | an implicit gap |
| `statement_options` | no statement block is printed: the stem is only an instruction or a trailing "because", and each option is itself a full statement to be judged | a printed block of lettered statements |
| `pair_options` | each option is a pair, group or set of same-kind items accepted or rejected whole — half an option right scores zero | two printed lists to pair |
| `list_of_structures` | a lettered list whose items are drawn structures or figures, to be judged or counted | the four OPTIONS being structures |
| `experiment_based` | **overlay** — a setup or observation is supplied and must be interpreted before anything else can start | a procedure merely mentioned |
| `table_based` | **overlay** — a table of features or measurements in the stem must be read across rows or columns | a list of statements |
| `new_type` | **escape hatch** — none of the above fits the printed shape | forcing a near fit |

**Overlays, not shapes.** `figure_to_read`, `fill_in_blank`, `experiment_based` and `table_based`
describe something laid over a shape, not a shape of their own. Record them in `E1_secondary_type`
alongside the primary label — which is what rule 0.1 means by a second label never being a second
primary. A question can be `statement_options` + `experiment_based`: the printed shape is four rival
statements, and what gates it is an experimental setup.

**Tie-break:** the answer's form decides. A graph in the stem with text options is `plain_mcq` +
`secondary_type: figure_to_read`, not `graph_options`.

`statement_options` vs `list_of_statements`: is a labelled block of statements printed above the
options? Block printed → `list_of_statements`. Content living entirely in the four options →
`statement_options`.

`pair_options` vs `match_the_lists`: `match_the_lists` needs two printed columns and a pairing code.
If one question is asked and each option bundles items, it is `pair_options`.

**`new_type` must come with a flag**, so the list is revised rather than quietly stretched. Using it
is the correct action, not a failure; forcing a question into a near-fitting label is the failure.

## 2. E2 · Format — what the ANSWER must contain

Decided from the options alone, never from how the answer is obtained. **A question that involves a
ratio can still ask for a temperature.**

| label | the answer is |
|---|---|
| `name_or_identify` | a name, term, colour, organism, scientist |
| `recall_value` | a specific stored value, held in memory rather than computed — PS II's absorption maximum, 680 nm |
| `calculate_value` | a number the student computes from the stem's numbers |
| `count_qualifying_items` | a count: how many of the listed species are aromatic, how many statements are correct, how many organisms show a stated feature |
| `derive_expression` | a symbolic expression |
| `pick_ratio` | a ratio, as a ratio |
| `pick_direction` | a direction or sense — the direction of a magnetic field, a force, or an angular acceleration (eastward, clockwise, into the page) |
| `pick_order` | an ordering of items |
| `pick_match_code` | a pairing code (A-II, B-IV, …) |
| `pick_correct_combination` | a subset of lettered statements |
| `judge_assertion_reason` | one of the four A/R verdicts |
| `judge_two_statements` | one of the four Statement I/II verdicts |
| `predict_product` | a chemical product, intermediate, starting material or the reagent set that effects a conversion |
| `pick_graph_or_label` | a graph, or a bare label read off a figure |
| `pick_correct_statement` | a whole claim graded as correct — a sentence, a balanced equation, a described process — or the incorrect one when the stem is negated |
| `pick_both_parts` | two or more independent answers that must ALL hold at once: magnitude and direction, two numbers, a pair or triple of names. Half right scores nothing |
| `pick_cause_or_effect` | one side of a causal link — a rival cause of a granted fact ("is due to"), or a rival outcome of a stated change ("on increasing X, Y will") |
| `identify_structure_or_compound` | a chemical species, where the options are drawn structures compared against each other and no reaction is printed |
| `new_format` | **escape hatch** — none of the above fits; write what you saw in the flag |

**Tie-break:** read only the four options. If they are temperatures, the label is
`calculate_value` or `recall_value` — never `pick_ratio`, however much ratio work the solution needs.
`recall_value` vs `calculate_value`: is the value stored, or computed from the stem's numbers?

`count_qualifying_items` vs `calculate_value`: counting was previously folded into
`calculate_value` as "a small integer produced by counting", which hid a distinct task — nothing is
computed, every listed item is adjudicated and the integer is the tally. `Q-000105` (how many
species obey Hückel's rule, options 4 / 6 / 2 / 5) is the clear case.

`pick_correct_statement` vs `pick_correct_combination`: are the statements printed as a lettered
block the options then select from? Block → `pick_correct_combination`. Each option a standalone
claim → `pick_correct_statement`.

`pick_cause_or_effect` vs `pick_direction`: `pick_direction` is a spatial or rotational sense
(eastward, clockwise, into the page). A quantity moving up or down **as a consequence** of a stated
change is `pick_cause_or_effect`.

`identify_structure_or_compound` vs `predict_product`: is a reaction printed? Reaction printed →
`predict_product`. Four structures ranked on a criterion → `identify_structure_or_compound`.

`pick_both_parts` vs E1 `multi_part_respectively`: these sit on different axes and usually co-occur.
E1 records that the stem asked for several things; E2 records that the answer must get them all right
together.

## 3. E3 · Content shape — what is being tested, plus the actual concept

Two fields, because the broad label alone is not revisable:

- `content_shape` — the broad kind: **what NCERT material the question is built on.** The list below
  is the whole list. It was previously described here as "the unchanged list" and never written out,
  which left the axis carrying 578 of 580 tags with no vocabulary a tagger could read.
- **`concept` — required, free text, specific.** "Critical angle from relative speeds", "Aromaticity:
  conjugation, planarity and π-electron count", "Field cancellation versus scalar potential". A
  student cannot revise `formula_or_law`; they can revise the concept.

| label | means | not |
|---|---|---|
| `formula_or_law` | a stated relation, law or rule applied, rearranged or chained — including a proportionality where constants cancel, a dimensional formula, and a limiting or boundary condition (critical angle, resonance, terminal velocity) | a stored number |
| `example_list` | a taught list or table of named items each tied to a trait, role, effect or partner; membership or the pairing IS the fact, and nothing about how it works rebuilds it | assigning items to classes by a criterion |
| `process` | a process or pathway and how it runs: the ordered steps, which stage does what, the causal link that makes the outcome happen, or the overall summary equation | a property of a structure |
| `definition_term` | what a term or quantity means, including holding two neighbouring terms apart; the strict reading of the definition decides it | explaining why a thing behaves as it does |
| `classification_hierarchy` | a scheme filing named entities into classes, groups, kingdoms or types, including the criterion that decides which box something sits in | a plain association |
| `diagram` | the material is a picture: a figure, circuit, map or apparatus sketch whose topology or geometry is the content, or a memorised labelled diagram — including where a named part sits inside a larger structure | a plot with axes |
| `structure_chemical` | the structure and bonding of a named species: geometry, electron counts (octet, VSEPR, MO filling, π electrons), oxidation states, or a structure rebuilt from memory | the transformation it undergoes |
| `trend` | behaviour across a series, or a comparison between named cases: which is larger, which way a quantity moves, **where the series breaks** | one value |
| `practical_procedure` | a named experiment, bench or field procedure, instrument or device: its setup, materials, what is in a named reagent, what an observation means, what each part is for | the law the instrument happens to exploit |
| `reaction` | what a specific reagent or condition does to a specific substrate — the transformation, its product, its reagent, or how far an oxidation is pushed | why it goes that way |
| `nomenclature_rule` | a naming, notation or sign convention that is **agreed rather than derived**: IUPAC and coordination names, a resistor colour code, what "first excited state" counts from, Cartesian signs, a pedigree symbol | a definition with physical content |
| `value_or_data` | a magnitude, count, wavelength, percentage or tabulated figure that exists only as a printed number in the source and is never supplied by the question | a number computed from the stem |
| `reaction_mechanism` | why a reaction goes the way it does: intermediate stability, attack geometry, rearrangement, the positional reach of a substituent effect | which reagent does what |
| `disease_cause` | the link between a disorder, its causal agent and its sign or symptom, entered from any of the three corners | a general example list |
| `graph` | a plot with axes is the material: a curve shape, a slope, an intercept, or which of four plots is consistent with a relation | a spatial arrangement |
| `scientist_history` | who did it, when, or which body issued it — an attribution or a date with no subject reasoning to fall back on | the content of their work |
| `current_affairs` | a time-bound fact that appears in **no** NCERT edition: a recent event, a current office-holder, a figure that changes year to year | a dated event the textbook itself records |
| `life_cycle` | which generation is which across a life cycle and what depends on what: haploid vs diploid stages, alternation of generations, which stage is dominant or free-living | any other staged sequence |
| `structure_function` | a biological structure tied to the function it performs — guard-cell wall thickening and stomatal movement | a structure merely named or located |
| `structure_property` | a chemical property that FOLLOWS from structure: acidity, stability, solubility, reactivity | the structure or electron count itself |
| `experimental_observation` | what is actually seen at the bench: flame colours, precipitates, colour changes, fluorescence | the apparatus or the protocol |
| `organism_characteristic` | the diagnostic features of a plant group, animal group or microorganism | filing that organism into a taxon |
| `new_shape` | **escape hatch** — none of the above fits; record it and flag it | forcing a near fit |

**Tie-breaks**, each one drawn from a pair that actually collided in the corpus:

- `diagram` vs E1 `figure_to_read`: different axes, and both can be true. E3 `diagram` says the
  MATERIAL is spatial — which is why a human-eye match-list with no printed figure is still
  `diagram`, since fovea and blind spot are separated only by position. E1 `figure_to_read` says a
  figure must be read to answer THIS printing of the question.
- `graph` vs `diagram`: a plotted functional relationship is `graph`; a spatial arrangement of
  parts or components is `diagram`.
- `reaction` vs `reaction_mechanism`: does the pathway decide the answer, or does the
  reagent-to-product mapping? "Which dehydrates most readily" turns on cation stability →
  `reaction_mechanism`. "Which will not give a primary amine" is reagent mapping → `reaction`.
- `value_or_data` vs `formula_or_law`: is the number stored (680 nm), or produced by a relation?
- `practical_procedure` vs `formula_or_law`: "the venturi-meter works on ___" is
  `practical_procedure` — the answer names the principle *as a fact about the instrument*. If the
  relation is applied to numbers, it is `formula_or_law`.
- `life_cycle` vs `process`: `life_cycle` is the more specific label and wins whenever the staged
  sequence is a life cycle with ploidy or generation alternation in it.
- `nomenclature_rule` vs `definition_term`: could the convention have been agreed differently
  without any physics or biology changing? Yes → `nomenclature_rule`.
- `disease_cause` vs `example_list`: is the pairing specifically disorder ↔ agent ↔ symptom?
- `current_affairs` vs `scientist_history`: both can be "an event and a year". The distinction is
  whether NCERT records it. The 1992 Rio Earth Summit is in the book, so it is
  `scientist_history`; a fact in no edition at all is `current_affairs`. **This label carries an
  invariant no other one does** and must not be folded into `scientist_history`:
  `scripts/checks/E3.py` fails any question tagged `current_affairs` whose D6 `syllabus_status`
  says it is in NCERT, because the two statements contradict each other. Merging the labels would
  delete that check — Mendel is in NCERT, so `scientist_history` cannot stand in for it.
- `structure_property` vs `structure_chemical`: **this pair resolves a contradiction** that stood in
  this section. `structure_chemical` is defined by the codebook as the structure ITSELF — geometry,
  electron counts, oxidation states — while an older inclusion rule here claimed it meant "a property
  that follows from structure" and cited cellulose-and-iodine. Those are two different labels. The
  structure is `structure_chemical`; the property it produces is `structure_property`, and
  cellulose-and-iodine is `structure_property`.
- `structure_function` vs `structure_property`: the same move in different subjects — biology's
  structure→function, chemistry's structure→property. Use the one matching the subject.
- `experimental_observation` vs `practical_procedure`: does the answer name what is OBSERVED, or how
  the apparatus is set up and what each part is for? A flame colour is
  `experimental_observation`; what a venturi-meter works on is `practical_procedure`.
- `organism_characteristic` vs `classification_hierarchy`: a diagnostic feature of a group is
  `organism_characteristic`; assigning a named organism to a taxon by a criterion is
  `classification_hierarchy`. "Which features distinguish bryophytes" is the former; "which group
  does Selaginella belong to" is the latter.

## 4. E4 · Thinking — three separate questions, not one

The old axis mixed three things and so contradicted itself: it called a question
`check_each_statement` that had a one-pair shortcut, and `direct_fact`'s definition said "no
elimination route" while `elimination` was a sibling label. Now:

**4a. `cognitive_demand` (one, required)**

| label | means | not |
|---|---|---|
| `recall` | one stored fact decides it | a rule applied to a case |
| `concept_discrimination` | choosing between two neighbouring concepts | recalling one |
| `application` | a stated rule, criterion or convention applied to this case. **The rule must be known first** — application is not knowledge-free | recall of the rule itself |
| `explanatory_reasoning` | the live decision is whether one thing accounts for another | checking two facts |
| `calculation` | arriving at a number or expression by computing | reading one off |
| `representation_translation` | moving between two representations of the same thing: an equation to a graph, a chemical name to its structure, a circuit to its equivalent | reading one representation |
| `condition_based_reasoning` | a rule applied **under a stated condition** that changes the outcome — the specified temperature, medium, reagent, or "battery disconnected" | applying a rule with no condition attached |
| `dimensional_reasoning` | the relationship is derived or settled BY dimensions | using dimensions to check an answer reached another way |

**4b. `solution_structure` (one, required)**

| label | means |
|---|---|
| `single_step` | one step, however much knowledge it needs |
| `multi_step_dependent` | step 2 needs step 1's result. **Four independent match-checks are NOT four steps** |
| `several_independent_checks` | each item verified separately, verdicts combined |

**4c. `strategy_available` (zero or more, optional)**

`elimination`, `estimation`, `symmetry`, `dimensional_check`, `unit_sanity`.

**`elimination` requires a demonstrated shortcut:** name the one pair or fact and the options it
strikes out — "fibrous → skull bones appears only in option 2". A recall question CAN offer
elimination; that is no longer a contradiction, because recall is now a demand and elimination a
strategy.

**`dimensional_reasoning` (4a) vs `dimensional_check` (4c):** the same tool in two roles. If the
question can only be answered by comparing dimensions, it is the demand. If dimensions merely
confirm an answer the student reached by substituting into a relation, it is the strategy.

**`condition_based_reasoning` vs `application`:** both apply a rule. The condition label is for the
case where a stated condition is what the question turns on — remove the phrase "battery
disconnected" or "in acidic medium" and a different option becomes correct. Its matching trap is
`condition_ignored`.

**4d. `new_demand`** — the escape hatch this axis was missing. If none of the five demands describes
what the question makes the student do, record `new_demand` with a description and a flag. E1, E2,
E3 and E5 each had one; E4 did not, so an unfamiliar demand had nowhere to go but the nearest fit.

**Retired**

| retired | replaced by |
|---|---|
| `direct_fact` | `recall` |
| `check_each_statement` | `several_independent_checks` |
| `multi_step` | `multi_step_dependent` |
| `numerical` | `calculation` |
| `diagram_graph` | E1 `figure_to_read` — it described the printing, not the thinking |
| `confusing_options` | `concept_discrimination` |
| `exception_based` | E5 `ignores_exception` — it describes a distractor |
| `changed_word` | E5 `single_word_substitution` — it describes a distractor |
| `sequence_based` | `application` + E2 `pick_order` — "the answer is an order" is an answer form, not a kind of thinking |
| `ratio_based` | `calculation` + `strategy_available: estimation` — the cancelling of constants is a strategy, not a demand |
| `explanation_based` | `explanatory_reasoning` — renamed only |

The last three were retired in `scripts/build_category_sheet_v2.py` and never written down here, so
for a while the rulebook could not account for 59 tags that the corpus carried. See Rule 21.

## 5. E5 · Trap — one option, one mistake, or nothing

Every tag states the option and the route. If neither can be named, there is no tag.

| label | means | required evidence |
|---|---|---|
| `calculation_slip` | a specific wrong operation yields a printed option | the operation and the option |
| `wrong_exponent` | a power or order-of-magnitude error yields it | the exponent and the option |
| `inverted_ratio` | the reciprocal of the right answer is printed | the option |
| `reversed_order` | the exact reverse of the right order is printed | the option |
| `wrong_pairing` | one pair in a match code is swapped | which pair, which option |
| `partial_combination` | a subset that is true but incomplete | which statement is omitted |
| `half_true` | an option with two claims, one right | the claim that fails |
| `semantic_reversal` | the relationship is reversed in words | the reversed words |
| `unit_or_conversion` | a missing or wrong conversion yields it | the conversion and the option |
| `intermediate_value` | a correct intermediate result is printed as an option | which step it is |
| `look_alike_term` | a term resembling the right one | both terms |
| `true_statement_trap` | the option is true but fails the task's polarity (NOT/EXCEPT) | the polarity |
| `other_one_fact` | a fact about a different member of the same family — another hormone, another organelle, another syndrome | which member, and which option |
| `neighbouring_fact` | a fact about an adjacent concept, disorder or event, where the families differ rather than the members | which adjacent thing |
| `ignores_exception` | the option is correct for the general rule, and this question is the exception to it | the rule and the exception |
| `scientist_swap` | the work is attributed to the wrong person | both names |
| `copied_from_stem` | the option repeats a phrase from the stem without answering the question | the repeated phrase |
| `old_ncert_fact` | the option was true in an earlier NCERT edition and the text has since changed | the change-log entry (Stage A), not an opinion |
| `single_word_substitution` | a long, fluent, almost entirely correct statement with one noun, adjective or negation swapped, so the surrounding truth vouches for the error | the swapped word |
| `sign_reversed_magnitude_right` | the magnitude and the method are right and one sign, right-hand rule or inequality is inverted | the sign, and that the magnitude matches |
| `wrong_power_of_dependence` | linear where it should be squared, squared where it should be rooted, or a root dropped | the two powers |
| `neighbouring_question_answer` | the option is a real, published, remembered result that answers a DIFFERENT question the stem superficially resembles | the other question it answers |
| `sequence_endpoint_or_adjacency` | an ordering that gets the ends right and fails on one interior adjacency, or reproduces the printed list order | which adjacency, or that it is the printed order |
| `parallel_order_decoy` | the straight positional mapping A-I, B-II, C-III, D-IV is offered as an option | that the mapping is positional |
| `true_but_out_of_scope` | the option is correct subject matter that answers a different question than the stem asked; it fails on relevance, not on truth | what the stem actually asked |
| `overclaiming_quantifier` | the option is wrong ONLY because of an "only", "all", "always" or "invariably" | the quantifier **and** the counter-example that falsifies it |
| `fabricated_term` | a term that does not exist is offered and reads as plausible chapter vocabulary | that the term appears nowhere in the source |
| `format_reflex_option` | the option is the reflex pick for the printed FORMAT rather than for the content — "both true but R is not the explanation", or "both true and R explains A" | the format, and why the content does not support the reflex |
| `no_elimination_route` | all four options are real terms from the same paragraph, so no securely-known fact strikes any of them out | that all four are source terms of the same kind |
| `complementary_grid` | the options are laid out as two magnitudes crossed with two signs, or two values crossed with two units, so no single error is self-evident | the two axes of the grid |
| `condition_ignored` | the option is what you get by dropping a stated condition — "battery disconnected", "in acidic medium", the specified temperature range | the condition, and that the option is right without it |
| `wrong_quantity` | the option answers for a neighbouring PHYSICAL quantity: diameter for radius, moment of inertia for radius of gyration | both quantities |
| `wrong_site_or_stage` | the option moves a biological event to the wrong place or the wrong time | the real site or stage, and the offered one |
| `omitted_contribution` | one force, field contribution, circuit element or term is left out of an otherwise correct sum | the omitted term and the option it yields |
| `false_explanatory_link` | both statements are true and the Reason is assumed to explain the Assertion **because they share a topic**, not because the link holds | the two true statements, and why the link fails |
| `no_derivation_route` | no arithmetic or factual route reaches this option at all; it widens the spread or completes a grid | that no route exists — demonstrated, not asserted. **This is a property of the arithmetic, never a claim about what students would pick** |
| `new_trap` | a device none of the above describes | a full description; this is the axis's unsure form |

**Tie-breaks among the close pairs:**

- `condition_ignored` vs `ignores_exception`: is the thing ignored **printed in the stem** (a
  condition) or **held in the student's head** (the exception to a general rule)? Printed →
  `condition_ignored`.
- `wrong_quantity` vs `other_one_fact`: a different physical quantity in the same problem →
  `wrong_quantity`. A fact about a different member of a family (another hormone, another syndrome)
  → `other_one_fact`.
- `wrong_site_or_stage` vs `other_one_fact`: the right event in the wrong place or time →
  `wrong_site_or_stage`. The right place with the wrong event's fact → `other_one_fact`.
- `omitted_contribution` vs `calculation_slip`: a whole term dropped from a sum →
  `omitted_contribution`. A wrong operation on the terms present → `calculation_slip`.
- `false_explanatory_link` vs `format_reflex_option`: both live on Assertion–Reason items.
  `false_explanatory_link` names why the link fails despite topical adjacency;
  `format_reflex_option` is for the hedge option ("both true, R not the explanation") chosen as a
  format reflex. Where both apply, `false_explanatory_link` is the primary — it says more.

### 5a. Verdicts that are NOT traps

The largest single cluster the per-subject analysis found was not a trap at all. These two verdicts
exist so that it stops being recorded as one.

| verdict | means | what it sets |
|---|---|---|
| `source_damage_artifact` | the option set as WE STORED IT misleads for reasons the paper never intended: lost digits, placeholder images, duplicated options, debris | `review_status: source_incomplete`, and a repair task. **Never** a trap tag |
| `arguable_key` | at least one wrong option is defensible on a reasonable reading, and the key rests on a textbook convention rather than on the subject | a review flag. The tag follows the printed key (§7); the flag records the doubt |

Across the four per-subject analyses these account for roughly 98 of the devices recorded — more
than any genuine trap. Recording our own extraction damage as a property of the question is the
single most misleading thing this axis has done.

**Retired, and why**

| retired label | replaced by | reason |
|---|---|---|
| `obviously_wrong` | `no_derivation_route` **or** `source_damage_artifact` | "no student would be drawn to it" is a claim about students that inspection cannot support. But "no arithmetic or factual route reaches this option" IS inspectable, and a large share of the old tags were in fact our own extraction damage. The device was real; only its justification was not. |
| `extreme_word` | `overclaiming_quantifier` | the original was retired for treating "only" in a combination answer as an absolute-word trap. Reinstated with the counter-example required as evidence, so the quantifier alone is not enough. |
| `sign_or_direction` | `sign_reversed_magnitude_right`, `inverted_ratio`, `reversed_order` or `semantic_reversal` | it was used for four unrelated things. The replacement must name WHAT reversed, so old tags are re-judged rather than renamed — but the tight case (all the work right, one sign wrong) is a real device and is now its own label. |
| `number_near_miss` | `calculation_slip`, `wrong_exponent` or `intermediate_value` | used where no numeric device was shown — in one case on a question with no numerical options at all. The only retirement with no inspectable form behind it. |
| `wrong_order` | `reversed_order` | renamed only; same meaning |
| `unit_conversion_slip` | `unit_or_conversion` | renamed only |
| `reversed_cause_effect`, `opposite_answer` | `semantic_reversal` | both described the same device under two names |

Every label in the replaced-by column is live above. **Three of these retirements were wrong as
first written** — `obviously_wrong`, `extreme_word` and the tight case of `sign_or_direction`
describe devices that do exist in the papers; what failed was justifying them by what a student
would do. The fix is an inspectable definition, not deletion. Rule 22 records why.

### 5b. Where these labels came from

The live list is the union of three sources, reconciled rather than chosen between:

| source | contributed |
|---|---|
| `exports/discovery/CATEGORIES.xlsx` | the original 21 labels, with definitions and corpus counts |
| `exports/discovery/clusters_pass_b/*.json` | 57 devices discovered per subject, independently of that list — the source of `no_derivation_route`, `neighbouring_question_answer`, `complementary_grid`, `no_elimination_route`, `digit_echo` evidence and both non-trap verdicts |
| the 55-row showcase | the only rows carrying an option and a route, i.e. the only tags that met rule 4 |

The per-subject analyses were run after the codebook was frozen and were never folded back into it.
That is why this axis looked settled at 21 labels while 57 devices sat in four JSON files.

## 6. Required supporting fields

| field | values | why |
|---|---|---|
| `task_polarity` | `direct`, `not`, `except`, `increasing`, `decreasing`, `maximum`, `minimum`, `respectively` | Materially changes what must be answered. Record NOT **in the task** only — not "does not" inside a biological premise, and not the NOT in standard A/R option wording. |
| `review_status` | `verified`, `provisional`, `source_incomplete` | `verified` = stem, options, figure and key all present and checked against a printed paper. `source_incomplete` = something is missing; E4/E5 stay empty. |
| `concept` | free text, specific | see §3 |
| `key_checked_against` | the source file, or `none` | a tag is only as good as the question under it |

## 7. Fix the question before tagging it — worked example

`Q-000021` (resistor colour code) is the case that proves the rule. Our record's stem reads
`(2200 ± 5%) Ω`, from which it follows that the third band is red — so an outside analysis concluded
the official key (orange) was wrong, and recommended changing it.

Both printed sources read **`(22000 ± 5%) Ω`**, and the NTA volume's own solution reads
"Resistance = (22 × 10³) ± 5%, Third band corresponds to…" with **Answer (3) Orange**.

The key was right. Our stem had lost a zero. A tagger working from our record would have recorded a
confident, well-argued, wrong classification of both the answer and its trap.

**So:** `review_status` is set from whether the question was checked against a printed paper, and no
E5 trap is written for a question whose stem or options are not confirmed.
