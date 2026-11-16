# Subject notes

Version 2.1 (3 Nov 2026). Read the part for your subject and branch. These notes add to `01_shared_rules.md` and never replace it.

---

## A. NCERT files and known problems

- **File names.**
  - The prefix is `ke` (Class 11) or `le` (Class 12), then `ph`, `ch` or `bo`, then part and chapter. For example, `keph101` is Class 11 Physics, Part 1, Chapter 1.
  - Files starting `kh` or `lh` are the Hindi books. Avoid them; their extracted text drops letters.
- **English PDFs whose extracted text comes out broken.** Render these pages with `pdftoppm -r 150` and read the images instead:
  - `kech202` (Class 11 Chemistry, Unit 8): garbled text.
  - `kech104` (Class 11 Chemistry, Unit 4 Bonding): drops letters.
  - `keph107` (Class 11 Physics, Gravitation): private-use characters; subtract 0xF000 from each.
- **Not on disk.** The lab manual, Exemplar and older editions are not available. Under rules §1.2 they do not count as "taught".

### Old to current NCERT numbering
SMEs often use the older (pre-2023) books. Add the old number when citing; the arrows below go from old number to current number.

| Book | Old → current |
|---|---|
| **Physics Class 11** | Chapters 2→1 (Units and Measurement), 3→2, 4→3, 5→4, 6→5, 7→6 (System of Particles and Rotational Motion), 8→7 (Gravitation), 9→8, 10→9, 11→10, 12→11, 13→12, 14→13 (Oscillations), 15→14 (Waves). Old Chapter 1 "Physical World" was removed. |
| **Physics Class 12** | Chapter numbers mostly the same; some sections shift. Example: electrostatics of conductors was 2.10 in some older books and is 2.9 now. Always check the current PDF. |
| **Chemistry Class 11** | Units 6→5 (Thermodynamics), 7→6 (Equilibrium), 8→7 (Redox), 12→8 (Organic: Some Basic Principles), 13→9 (Hydrocarbons). Removed: States of Matter, Hydrogen, s-Block, p-Block, Environmental Chemistry. |
| **Chemistry Class 12** | Units 2→1 (Solutions), 3→2 (Electrochemistry), 4→3 (Chemical Kinetics), 8→4 (d- and f-Block), 9→5 (Coordination Compounds), 10→6 (Haloalkanes), 11→7 (Alcohols), 12→8 (Aldehydes), 13→9 (Amines), 14→10 (Biomolecules). Removed: Solid State, Surface Chemistry, Metallurgy, p-Block, Polymers, Chemistry in Everyday Life. |
| **Biology Class 11** | Chapters 1–10 are the same. Then 13→11 (Photosynthesis), 14→12 (Respiration), 15→13 (Plant Growth), 17→14 (Breathing), 18→15 (Body Fluids), 19→16 (Excretory), 20→17 (Locomotion), 21→18 (Neural), 22→19 (Chemical Coordination). Removed: Transport in Plants, Mineral Nutrition, Digestion and Absorption. |
| **Biology Class 12** | Chapters 2→1 (Sexual Reproduction in Flowering Plants), 3→2, 4→3, 5→4, 6→5, 7→6, 8→7, 10→8 (Microbes), 11→9, 12→10, 13→11, 14→12, 15→13. Removed: Reproduction in Organisms, Strategies for Enhancement in Food Production, Environmental Issues. |

Check a mapping in the PDF before relying on it for a section number.

---

## B. Physics (branch `physics`)

- **Questions:** code 11 Q1–45; code 50 Q1–45. **Grid:** 5 Easy, 5 Medium, 5 Hard.
- **Common traps:**
  - a missing factor of 2 or ½;
  - unit slips (cm vs m, rpm vs per second, g vs kg) and powers of ten;
  - a formula used outside its condition (mgh at large heights);
  - figure misreading (battery polarity, diode direction, axis position).

  Test numerical slips with a script.
- **Avoid:** Q15. Graph D is also correct if downward is taken as positive.
- **Known facts:**
  - The parallel-axis theorem is not in the current NCERT text; only Table 6.1 is.
  - The meter bridge section was removed from the current NCERT.
  - The table files "number of revolutions" questions in two chapters: Rotational Motion #1 and Laws of Motion #35.
  - The table has no "Elastic Moduli" topic.
- **Version 2 result:**
  - Code 11 Hard questions: Q18, Q35, Q37.
  - From code 50: Q29 (two lenses) and Q31 (disc angular momentum about two points), both matching the NTA key.
  - Q27 is Medium under the test-series adjustment.
  - Q3 and Q27 are reserves.
- **SME round 1:**
  - Q1, Q5 and Q11 are all correct; Easy.
  - Q2 is Medium; the expert wanted an "Elastic Moduli" topic, which is missing from the table.

---

## C. Chemistry

**Questions:** code 11 Q46–90; code 50 Q46–90. **Grid:** 3 Easy, 3 Medium and 3 Hard for each branch.

| Branch | Code 11 | Code 50 (check each by reading) |
|---|---|---|
| **Organic** | Q46, 51, 52, 55, 57, 58, 60, 65, 67, 69, 70, 72, 85, 90 | Q46, 48, 50, 55, 72, 77, 79, 80, 82, 83, 86 |
| **Inorganic** | Q53, 59, 62, 63, 64, 66, 68, 76, 77, 80, 81, 82, 88 | Q49, 53, 58, 66, 67, 68, 75, 78, 81, 85, 87, 90 |
| **Physical** | Q47, 48, 49, 50, 54, 56, 61, 71, 73, 74, 75, 78, 79, 83, 84, 86, 87, 89 | Q51, 52, 54, 56, 57, 59, 60, 62, 63, 64, 69, 71, 74, 88 |

- Not yet sorted in code 50 (read them first): Q47, 61, 65, 70, 73, 76, 84, 89.
- The branch comes from these lists. The topic follows the deciding fact's chapter (rules §2, step 5). For example, Q47 is listed as physical, but its topic is in the d- and f-block chapter.

**Common traps:**
- **Organic:** a wrong reagent memory (the reagent for nitro groups used on nitriles); Markovnikov vs the peroxide effect; half-true statements.
- **Inorganic:** a trend applied where NCERT gives an exception; look-alike complexes (e.g. [NiCl<sub>4</sub>]<sup>2−</sup> vs [Ni(CN)<sub>4</sub>]<sup>2−</sup>); high spin vs low spin; dπ–pπ vs dπ–dπ.
- **Physical:** a missing stoichiometric factor (the 2 in 2A → B); log vs ln; the sign of a slope; NCERT's old numbers.

**Avoid:**
- Q58: two correct options (3 and 4); Aakash prints "3 or 4".
- Q79: sign dispute (±0.109 V).
- Q83 is safe: Aakash (4) is correct.

**Table and bank facts:**
- Surface Chemistry is not in the table or the current NCERT.
- All 23 "The p–Block Elements" topics return 0 in the bank; the bank uses a second chapter name, "P Block".
- All 7 practical-chemistry topics return 0 in the bank.
- Duplicate topic numbers: Electrochemistry has two #8; POC has two #5.
- Odd topic numbers: GOC, ISO and NOM use 6-digit numbers; Quantum Numbers is #3252; Expressing Concentration is #3262.

**Version 2 result:**
- **Organic:** all from code 11 (Hard: Q65, Q70, Q69). Q69 is Hard under rule 1.2 and is flagged for SME review.
- **Inorganic:** Hard is Q62, Q88 and code 50 Q66.
- **Physical:** Hard is Q47 plus code 50 Q60 and Q69.

**SME round 1** (organic only):
- Q51 is Easy. Section 10.5 is correct in the current book (older books: 14.5). The trap is the half-true options 1 and 3.
- Q52 is Medium. Section 8.6.1 is correct (older books: 12.6.1).
- Q72 is Easy.
- Q46 is Medium; option 4 is the trap.
- Q65 is Hard.

---

## D. Biology

**Questions:**
- Botany = code 11 Q91–135; Zoology = code 11 Q136–180. Use the paper's own sections; genetics, biotech, biomolecules and cell questions go with the section they are printed in.
- In code 50, Q91–135 mixes in some zoology items (vertebrae, frog cranial nerves, pancreas). Sort code 50 questions by chapter: plant chapters are botany, animal and human chapters are zoology.

**Grid:** 3 Easy, 3 Medium and 3 Hard for each branch.

**Common traps:**
- an NCERT line with one word swapped (mitosis ↔ meiosis, genus ↔ specific epithet, ten ↔ twelve cranial nerves);
- look-alike terms (maturation vs meristematic, lyase vs ligase, GPP vs NPP, monocondylic vs dicondylic);
- an NCERT neighbour (ampicillin vs tetracycline; NCERT's bollworm gene pair vs the corn-borer gene);
- half-true statements;
- a number borrowed from a nearby line ("last 2 pairs" of ribs).

**Wording:** use NCERT's exact terms. An SME asked for "strictly NCERT language".

**Known facts:**
- Q118 is settled as answer 2: the arc shows on NCERT Class 11, page 69.
- Q162 statement B is not strictly true (atlas–axis is a pivot joint), but the key stands.
- Q176's key ignores a true statement E, but the answer stands.
- "Strategies for Enhancement in Food Production" is not in the table or the current NCERT, yet Q112 asks about it.
- "C<sub>3</sub> Cycle" and "The Calvin Cycle" are two table topics for one pathway.
- The Morphology topics name families the current NCERT does not describe.
- Structural Organisation in Animals still lists tissue and cockroach topics that the current NCERT has removed.

**Version 2 result:** every cell was filled from code 11; nothing is borderline. Reserves: botany Q103 and Q124 (Hard); zoology Q150 (Medium).

**SME round 1** (Botany only):
- Q91: use NCERT language; show one topic; the real trap is maturation vs meristematic.
- Q104: topic name not NCERT (table issue); Medium.
- Q125: topic name not NCERT (table issue); Easy.
- Q118: one topic; the table names families not in NCERT; Hard.
- Q96: Hard.
- Q120: use the section topic "Tools of Recombinant DNA Technology"; Hard.
- Q117: Medium.
- Q103 and Q124: all good.
