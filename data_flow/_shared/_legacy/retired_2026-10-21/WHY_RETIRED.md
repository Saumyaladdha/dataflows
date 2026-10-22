# Retired 2026-10-21 — the separately published NTA answer keys

`read_official_key.py` parsed NTA's published key PDFs into 176 per-booklet-code JSON files in
`papers_v2/official_keys/`, and the export joined them in as a third answer alongside the booklet's
printed answer and our own blind solve.

**It was removed from the flow by the owner's decision, on measured evidence.**

NEET prints the same questions in roughly 24 booklet codes with the options reordered, so a key is
only meaningful against the code it was published for. The PDFs for 2016, 2017 and 2022 carry no
`BOOK : <code>` heading to split on, so they parsed into a single year-wide key. Joined to the
booklet we actually hold, that key contradicted the booklet's own printed answer on:

| booklet | disagreed with the printed answer |
|---------|-----------------------------------|
| 2016_X  | 125 of 175 (71%) |
| 2017_C  | 131 of 176 (74%) |
| 2022_Q1 | 155 of 198 (78%) |

Those are not findings. They are one wrong join, repeated — the key belongs to a different code.
A source that is silently wrong is worse than no source, because it arrives labelled "official".

**What replaces it.** The booklet prints its own answer under every question, and that is now the
official answer the corpus uses (`answer_official` in the CSV). The independent check is no longer
a document join but `b6-blind-solver`, which answers the question having seen no answer at all —
a check that cannot be wrong for the silent reason a mis-joined key is.

**Do not re-introduce this step** without first solving the code-matching problem: proving, per
booklet, that a key PDF was published for the exact code in hand. Until then the join is a guess.

Kept here rather than deleted so the measurement above can be reproduced.
