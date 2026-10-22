"""Splits run-together inline options and validates a question's four options (spec 2.6, used by
B3/B4). Core rule: when options run together with no separator, or when the stem itself contains
an earlier "(a) ... (b) ..." run (statement labels, not options), take the LAST complete (a)-(d)
or 1)-4) run in the text as the real options.
"""
import re

# Two separate marker styles, kept as separate pools rather than one "optional paren" pattern:
# a bare marker ("a)") is a real option marker, but a parenthesised one ("(a)") is how both stem
# statement labels AND embedded combination references inside option text ("(a),(b)") are
# written (spec 2.6's own example mixes both in one string). Merging them into one pattern would
# let an embedded "(a)" inside an option's own text break the run that contains it. The negative
# lookbehind keeps the bare pattern from also matching the "a)" tail of a parenthesised "(a)".
_LETTER_BARE = re.compile(r"(?<!\()([a-dA-D])\)")
_LETTER_PAREN = re.compile(r"\(([a-dA-D])\)")
_DIGIT_BARE = re.compile(r"(?<!\()([1-4])\)")
_DIGIT_PAREN = re.compile(r"\(([1-4])\)")

_LETTER_SEQUENCE = ["a", "b", "c", "d"]
_DIGIT_SEQUENCE = ["1", "2", "3", "4"]


def _find_complete_runs(text, pattern, sequence):
    """Scan `text` for every maximal run of markers that follow `sequence` in order (e.g.
    a,b,c,d), and return only the COMPLETE ones (all of `sequence` present) as lists of
    (start, end, value) marker-match triples, in the order they occur in `text`."""
    matches = []
    for m in pattern.finditer(text):
        raw = m.group(1)
        val = raw.lower() if raw.isalpha() else raw
        matches.append((m.start(), m.end(), val))

    runs = []
    current = []
    expected_idx = 0
    for start, end, val in matches:
        if val == sequence[0]:
            if len(current) == len(sequence):
                runs.append(current)
            current = [(start, end, val)]
            expected_idx = 1
        elif current and expected_idx < len(sequence) and val == sequence[expected_idx]:
            current.append((start, end, val))
            expected_idx += 1
        else:
            if len(current) == len(sequence):
                runs.append(current)
            current = []
            expected_idx = 0
    if len(current) == len(sequence):
        runs.append(current)
    return runs


def split_inline_options(text):
    """Take the LAST complete (a)-(d) or 1)-4) run anywhere in `text` as the real four options,
    splitting them apart even when they run together with no separator (e.g.
    "...isa) Boron...b) Beryllium...c) ...d) ..."). Everything before that run (including any
    earlier incomplete "(a) ... (b) ..." style statement labels) is returned as `stem`. Returns
    {"stem": str, "options": {"1": str, "2": str, "3": str, "4": str}} — `options` is {} if no
    complete run of four markers is found anywhere."""
    pools = [
        _find_complete_runs(text, _LETTER_BARE, _LETTER_SEQUENCE),
        _find_complete_runs(text, _LETTER_PAREN, _LETTER_SEQUENCE),
        _find_complete_runs(text, _DIGIT_BARE, _DIGIT_SEQUENCE),
        _find_complete_runs(text, _DIGIT_PAREN, _DIGIT_SEQUENCE),
    ]
    candidates = [runs[-1] for runs in pools if runs]
    if not candidates:
        return {"stem": text, "options": {}}

    last_run = max(candidates, key=lambda run: run[0][0])
    stem = text[:last_run[0][0]].rstrip()

    options = {}
    for i, (start, end, val) in enumerate(last_run):
        next_start = last_run[i + 1][0] if i + 1 < len(last_run) else len(text)
        # Whitespace only — a leading "-" must survive for a negative-number option like "-5 m/s".
        options[str(i + 1)] = text[end:next_start].strip()
    return {"stem": stem, "options": options}


def validate_options(options_en, option_images=None):
    """Check B3's four options: each of "1".."4" must have non-empty text OR an image crop
    (never both empty, per spec 2.6/10). Returns the list of option keys that are invalid (empty
    text and no image) — empty if all four are valid."""
    option_images = option_images or {}
    invalid = []
    for key in ("1", "2", "3", "4"):
        text = (options_en or {}).get(key) or ""
        image = option_images.get(key)
        if not text.strip() and not image:
            invalid.append(key)
    return invalid


def find_duplicate_options(options_en):
    """Return the list of option-text values that appear more than once among "1".."4"
    (spec B3_DUPLICATE_OPTIONS check) — empty if all four texts are distinct or blank."""
    seen = {}
    dupes = set()
    for key in ("1", "2", "3", "4"):
        text = (options_en or {}).get(key)
        if not text or not text.strip():
            continue
        norm = text.strip()
        if norm in seen:
            dupes.add(norm)
        seen[norm] = key
    return sorted(dupes)


if __name__ == "__main__":
    # T3: options run together with no separator
    t3 = "The correct statement isa) Boron is a metalloidb) Beryllium is a metalc) Carbon is a nonmetald) Nitrogen is a gas"
    r3 = split_inline_options(t3)
    assert set(r3["options"].keys()) == {"1", "2", "3", "4"}, r3
    assert r3["options"]["1"].startswith("Boron"), r3
    assert r3["options"]["4"].startswith("Nitrogen"), r3
    assert "correct statement is" in r3["stem"], r3

    # T4: stem statements (a)/(b) stay in the stem; the LAST a)-d) run is the options
    t4 = ("(a) Flowers are bright coloured (b) Calyx is usually green. "
          "Choose the correct answer from the options below: "
          "a) (a),(b) b) (a) only c) (b) only d) Neither (a) nor (b)")
    r4 = split_inline_options(t4)
    assert "(a) Flowers are bright coloured" in r4["stem"], r4
    assert "(b) Calyx is usually green" in r4["stem"], r4
    assert r4["options"]["1"] == "(a),(b)", r4
    assert r4["options"]["4"] == "Neither (a) nor (b)", r4

    # T5: image options
    assert validate_options({"1": "", "2": "x", "3": "y", "4": "z"}, {"1": "crop1.png"}) == []
    assert validate_options({"1": "", "2": "x", "3": "y", "4": "z"}, {}) == ["1"]
    assert validate_options({"1": "a", "2": "b", "3": "c", "4": "d"}) == []

    dupes = find_duplicate_options({"1": "Boron", "2": "Beryllium", "3": "Boron", "4": "Carbon"})
    assert dupes == ["Boron"], dupes

    no_run = split_inline_options("just a plain sentence with no options at all")
    assert no_run["options"] == {}

    print("option_parser.py self-check OK:", r3["options"], "|", r4["options"])
