# Output schema: one object per question

Each branch file (`data/<branch>.json`) is a JSON array of these objects. The page builder (`../builder/build_page.py`) reads them directly, and `build_page.problems()` checks the required fields.

```json
{
  "id": "c55",                       // required. Prefix by branch: p (physics), c (chemistry, all three branches), b (botany), z (zoology).
                                     //   Add "r" for code 50: rp29, rc60, rb112, rz150. (Round 1 used "re" for code 50 chemistry; rename to "rc".)
  "n": 55,                           // required. Question number in its paper
  "paper": "11",                     // required. "11" = cancelled 3 May paper, "50" = valid 21 June paper
  "branch": "organic",               // required. physics | organic | inorganic | physical | botany | zoology (from the subject notes, not from the chapter)
  "title": "Short plain title",      // required
  "answer": "(1) …",                 // required. Option number + text
  "chapter": "…",                    // required. AWS table chapter_display_name, exactly
  "code": "CHENEETENG…",             // required. AWS table chapter_code
  "topic": {"num": 3, "name": "…", "prio": "LOW", "trend": "0 Ques in last 5 years"},  // required. ONE final topic (rules §2), values copied from the table
  "ncertTopic": "10.5 Nucleic Acids", // required. Rules §2: section number + title; "Example 6.11"; or "Not in current NCERT (…)"
  "whyTopic": ["…", "… our bank: <b>12 of 47</b> (keywords: …)"],  // required. 1–3 lines
  "others": [{"num": 5, "name": "…", "chapter": "(only if another chapter)", "prio": "…", "trend": "…", "why": "Rejected because …"}],  // optional, max 2; shown behind "Why not these topics?"
  "tableIssues": [{"type": "name_mismatch | missing_topic | duplicate | not_in_ncert | numbering | bank_gap", "detail": "…"}],
                                     // optional. bank_gap = the verified bank has no or very few questions where it should, or files them under another topic
  "level": "easy | medium | hard",   // required. Rules §1
  "borderline": false,               // optional. true only when the question meets no Hard line and nothing better exists
  "fileLevel": "…",                  // required. The questions file's own label, or "not in file"
  "previousLevel": "…",              // optional. Earlier round's level; "hard (borderline)" if it was borderline; omit for questions new to the grid
  "steps": ["…"],                    // required. How to solve it
  "shortcut": "…",                   // optional. A short way to solve it
  "reasons": [["Why Medium", "…"], ["Why not Hard", "…"], ["NCERT link", "…"]],  // required. Explain any change from previousLevel here
  "deep": {                          // required
    "idea": "<b>How the options are built</b> …",
    "mult": [["label", "note", true]],     // optional chips: third value true = right, "x" = false, false = neutral
    "traps": [                             // required. Order: main, other traps, fillers, correct last
      {"k": "2", "v": "option text", "role": "main",   // role: main | trap | filler | correct (exactly one main, exactly one correct)
       "who": "<b>Who falls:</b> …",
       "ways": [{"name": "Way A · … (optional)", "steps": [["ok", "…"], ["bad", "…", "fix …"]]}],
       "proof": "<b>How I checked:</b> … (required for fillers)",
       "feels": "<b>Why it feels right:</b> …"}
    ],
    "check": "<b>Fastest route</b> … (only this one <b>)",
    "rank": "…",                                            // optional. e.g. "Most dangerous: …"
    "notCaughtTitle": "Mistakes the options do not catch",  // optional
    "notCaught": [["short title", "text"]]                  // optional
  },
  "note": "…",                       // optional. Shown under the traps
  "smeNotes": "How the SME comment was handled",  // optional. Shown on the page as "Expert review"
  "type": "Single-answer MCQ | Match the following | Statement type | Sequence (arrange in order) | Two-part MCQ",  // required
  "typeSub": "…", "typeWhy": "…",    // required
  "src": "NCERT Class 12 Chemistry (current book), Unit 10 Biomolecules, section 10.5 Nucleic Acids (older books: Unit 14) …",  // required. Rules §3
  "explain": {"asks": "…", "idea": "…"},  // required. Rules §4: use NCERT terms
  "image": {"source": "cdn", "url": "…"}  // required. Or {"source": "pdf50", "page": 16, "y0": 146, "y1": 490}. Optional "show": visible width in px
}
```

Do not use the old version 1 fields `gap` (use `tableIssues`) or `others[].tag`.

**Finished examples in `../data/`:**

| Question type | Example |
|---|---|
| Statement type | `inorganic.json` c88; `zoology.json` z162 |
| Match the following | `inorganic.json` c68; `botany.json` b96 |
| Sequence | `zoology.json` z138; `botany.json` b109 |
| Numerical | `physical.json` rc60; `physics.json` p4 |
| Figure / circuit | `physics.json` p18 |
| Two-part MCQ | `organic.json` c67 |
