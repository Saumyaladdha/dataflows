# `data/` — what goes where

Four folders. The first three hold the same chapter at the same path, so a script only ever has
to swap the first word.

```
data/
├── new_ncert/   the current NCERT            ← the pipeline writes this
├── old_ncert/   the previous NCERT           ← you upload this
├── mapping/     old ↔ new                    ← a script writes this
└── dynamodb/    rows ready to load           ← generated, never edit by hand
```

---

## The path is identical in all three

```
new_ncert/class_12/biology/ch01_sexual-reproduction-in-flowering-plants/chapter.json
old_ncert/class_12/biology/ch01_sexual-reproduction-in-flowering-plants/chapter.json
mapping/  class_12/biology/ch01_sexual-reproduction-in-flowering-plants/change.json
```

So a script finds its three files like this:

```python
for new in glob("data/new_ncert/class_*/*/ch*/chapter.json"):
    old    = new.replace("new_ncert", "old_ncert")
    change = new.replace("new_ncert", "mapping").replace("chapter.json", "change.json")
```

Nothing to match, no lists to maintain.

---

## 1 · `new_ncert/` — already here

34 chapters: 32 biology, 2 physics. Written by the extraction pipeline. Do not edit by hand.

```
new_ncert/class_12/biology/ch01_sexual-reproduction-in-flowering-plants/
    chapter.json          the content
    chapter.md
    chapter-exact.html
    figures/
```

---

## 2 · `old_ncert/` — upload here

**Folder name comes from the NEW edition, not the old one.**

The old book often numbers the chapter differently. That number is already inside the file at
`chapter.number`, so the folder does not need to carry it.

```
new_ncert/class_12/biology/ch01_sexual-reproduction-in-flowering-plants/   ← new chapter 1
old_ncert/class_12/biology/ch01_sexual-reproduction-in-flowering-plants/   ← old chapter 2 goes here
                                                                              (chapter.number = 2 inside)
```

Put one file in each folder:

```
old_ncert/class_12/biology/ch01_…/chapter.json
```

Same shape as `new_ncert`'s `chapter.json` — same keys, same `tree`.

### Chapters that were deleted

A chapter that exists only in the old edition has no folder in `new_ncert/`, so it goes under
`_dropped/` with its **own** old name:

```
old_ncert/class_12/biology/_dropped/ch01_reproduction-in-organisms/chapter.json
old_ncert/class_12/biology/_dropped/ch09_strategies-for-enhancement-in-food-production/chapter.json
old_ncert/class_12/biology/_dropped/ch16_environmental-issues/chapter.json
```

The script reads `_dropped/` and knows these have no counterpart.

---

## 3 · `mapping/` — the script writes here

Two files per chapter.

### `pair.json` — which old chapter this is

```json
{
  "latest": { "chapter_no": 1, "reprint": "2026-27",
              "title": "SEXUAL REPRODUCTION IN FLOWERING PLANTS" },
  "older":  { "chapter_no": 2, "reprint": "2022-23",
              "title": "SEXUAL REPRODUCTION IN FLOWERING PLANTS" },
  "matched_on": "title"
}
```

For a deleted chapter, written under `mapping/class_12/biology/_dropped/ch01_…/pair.json`:

```json
{
  "latest": null,
  "older":  { "chapter_no": 1, "reprint": "2022-23",
              "title": "REPRODUCTION IN ORGANISMS" },
  "verdict": "chapter_removed",
  "affects_answers": true
}
```

### `change.json` — a list, one entry per change

```json
[
  {
    "n": 1,
    "change_type": "edited",

    "from": { "id": "p_RO3LHI", "chapter_no": 2, "reprint": "2022-23",
              "address": "Ch 2 › 2.1", "page": 6,
              "body": "The number of species that are known and described range between 1.7-1.8 million." },

    "to":   { "id": "p_yXCbmf", "chapter_no": 1, "reprint": "2026-27",
              "address": "Ch 1 › 1.1", "page": 4,
              "body": "The number of species that are known and described range between 20 million." },

    "diff": [
      { "op": "same", "text": "The number of species that are known and described range between " },
      { "op": "del",  "text": "1.7-1.8" },
      { "op": "ins",  "text": "20" },
      { "op": "same", "text": " million." }
    ],
    "similarity": 0.94,

    "verdict": "fact_changed",
    "why": "The species count changed from 1.7-1.8 million to 20 million.",
    "affects_answers": true
  }
]
```

| `change_type` | written by the script | fields |
|---|---|---|
| `edited` | the text changed | `from` + `to` + `diff` |
| `moved` | same text, different place | `from.address` + `to.address` |
| `removed` | in the old edition, gone from the new | `from` only, `to: null` |
| `added` | new in this edition | `to` only, `from: null` |

| `verdict` | written by `a8-change-judge` | meaning |
|---|---|---|
| `fact_changed` | a stated fact is different | past answers need review |
| `fact_removed` | the fact is gone | past questions are out of syllabus |
| `fact_added` | new material | |
| `wording_only` | rewritten, same fact | nothing to review |

`change_type` is mechanical — a script can decide it. `verdict` is judgement — only the agent can,
because a diff cannot tell `1.7-1.8 million → 20 million` apart from a sentence that was merely
rephrased.

### `report.md` — optional, human-readable

A short summary of the chapter's changes. Generated, safe to delete.

---

## 4 · `dynamodb/` — generated

Flat JSON lists of rows, ready to batch-write. Built from the three folders above. **Never edit
by hand** — the next regeneration overwrites it.

---

## Rules

1. **Folder names come from `new_ncert/`.** The old chapter number lives inside the file.
2. **Never edit `dynamodb/`.** It is derived.
3. **`pair.json` before `change.json`.** The diff needs to know which old chapter to compare
   against. Comparing chapter 1 against chapter 1 is how `CHG_BIO12-ch01.json` ended up with 94
   "added" and 92 "removed" and zero matches — it had compared *Reproduction in Organisms*
   against *Sexual Reproduction in Flowering Plants*, two unrelated chapters.
4. **A `change.json` with no `moved` and no `edited` is broken.** It means nothing matched, which
   means the wrong chapters were compared. Check `pair.json` first.

---

## State, 2026-10-30

| | |
|---|---|
| `new_ncert/` | 34 chapters (32 biology, 2 physics) |
| `old_ncert/` | **empty** — folders created, files not uploaded |
| `mapping/` | **empty** — nothing generated yet |
| `dynamodb/` | partial, and the two existing change files are wrong (see rule 3) |

The old biology chapters are sitting in `~/Downloads/DATA_NCERT/OLD_ncert_class11_bio/` (22) and
`OLD_ncert_class12_bio/` (16). They need to be copied into `old_ncert/` under the **new** edition's
folder names.
