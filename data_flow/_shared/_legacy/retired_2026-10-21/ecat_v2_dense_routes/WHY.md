# ECAT ratings re-run for readable routes

These ratings were correct. Every label came from `config/allowed_values.yaml`, every trap named an
option and a route, no trap sat on a key, and the checker passed all of them.

They were re-run because the ROUTES WERE UNREADABLE. A route is read by a person, on a page, beside
the question — and most of these spent their words arguing for the label rather than describing the
mistake:

> "the four options are two magnitudes crossed with the factor root two - 10 with 14 (10 root 2) and
> 20 with 28 (20 root 2) - and option 1 is the member only that grid explains: no named operation on
> 20 m, 50 percent and g = 10 m/s^2 produces 10 m/s, which is instead the half of the keyed value
> needed to complete the pattern"

60 words, and a reader still has to work out what a student did wrong. The same trap, written for a
human: *"Halves the speed instead of the energy. Gives 10 m/s, half the correct 20 m/s."*

That was my omission, not the raters'. The brief asked for evidence and said nothing about who reads
it, so they wrote complete justifications — which is what the instruction actually asked for. The
writing standard now lives in `.claude/agents/e-category-rater.md` under "How to write a route".

Kept because the LABELS here are independent evidence: where the re-run picks a different label for
the same option, that disagreement is worth looking at.
