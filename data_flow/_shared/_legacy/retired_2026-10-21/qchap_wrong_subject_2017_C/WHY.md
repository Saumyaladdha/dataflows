# 2017_C chapter mappings, made against the WRONG subject

These 108 outputs were written before `q-subject-confirmer` had run on 2017 Code-C, when every
question in that booklet carried only a positional subject guess.

`q-chapter-picker` is handed a CLOSED chapter list chosen **by subject**. The guess for this booklet
was wrong for **179 of 179 questions** — it runs Biology (1–90), Physics (91–135), Chemistry
(136–180), not the standard Physics/Chemistry/Biology — so every one of these mappings was made
against a list from the wrong subject entirely.

The agents noticed, which is the only reason this was caught: 108 of them answered `unsure` and said
in their notes that "the chapter list this item carries is from the wrong subject". That is the
closed-list rule working exactly as designed. An agent permitted to compose a chapter name would
have produced 179 plausible, wrong rows instead, and nothing on the page would have looked amiss.

Kept rather than deleted because those notes are the evidence for the bug. `QCHAP` now refuses any
question whose subject is only a positional guess, so this cannot recur silently.
