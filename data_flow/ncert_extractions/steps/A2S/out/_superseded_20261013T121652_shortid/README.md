# Superseded A2S outputs — old short item_id scheme

156 transcriptions written under the pre-fix item_id `<BOOK>-p<page>-b<n>`, which omits the
chapter. Every chapter PDF restarts at page 1, so that key collides: 14 of these ids match a
block in BOTH CHE12L ch01 and ch09, and the old `out[item_id] = rec` dict silently kept only one.

They are superseded for two reasons, not one:

1. **Identity.** The id cannot be trusted. `_identity_and_clipping_triage.json` records which
   block each output most likely describes (recovered by replaying the old loop order), but for
   the 14 colliding ids that is inference, not evidence.
2. **Completeness.** All 156 were transcribed from crops of the bare bbox with no padding. The
   eleven workers who produced them reported roughly 50 crops that cut captions mid-sentence, cut
   above-arrow reagents away entirely, or sat so misaligned that the crop was mostly the previous
   block's prose.

Kept, not deleted: this is real agent work and the project rule is never to delete it. The
re-run writes chapter-qualified ids from padded crops, so nothing here is overwritten.

An attempt to measure clipping per item (ink in the padding bands) is in the triage file and is
NOT reliable — on a dense NCERT page the bands catch the neighbouring paragraph, so it reported
136 of 156 clipped against the ~50 the readers actually saw. Recorded only so the next person
does not repeat it.
