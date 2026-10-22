"""Quote-matching text normalisation, per spec 5.7. `normalise_quote` is for matching only:
it collapses whitespace, joins end-of-line hyphenation, straightens curly quotes and expands
ligatures. It deliberately does NOT case-fold, does NOT remove punctuation and does NOT change
any word — see the proof in the self-check below, which asserts case and punctuation survive.
"""
import re

_CURLY_QUOTES = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "′": "'", "″": '"',
}
_LIGATURES = {
    "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl",
    "ﬅ": "st", "ﬆ": "st",
}


def _normalise_with_positions(s):
    """Core normaliser shared by `normalise_quote` and quote_verify.find: walks the original
    string once, producing the normalised characters together with, for each one, the index of
    the original character it came from — so a match on the normalised string can be mapped back
    to a span in the original text. A hyphen is only treated as a line-wrap join when a real
    newline (not just a stray mid-word hyphen) separates it from the next word character.
    """
    if s is None:
        s = ""
    out_chars = []
    out_idx = []
    n = len(s)
    i = 0
    while i < n:
        ch = s[i]

        if ch in _LIGATURES:
            for c in _LIGATURES[ch]:
                out_chars.append(c)
                out_idx.append(i)
            i += 1
            continue

        if ch in _CURLY_QUOTES:
            out_chars.append(_CURLY_QUOTES[ch])
            out_idx.append(i)
            i += 1
            continue

        if ch == "-":
            j = i + 1
            while j < n and s[j] in " \t":
                j += 1
            if j < n and s[j] == "\n" and out_chars and out_chars[-1].isalnum():
                k = j + 1
                while k < n and s[k] in " \t\r\n":
                    k += 1
                if k < n and s[k].isalnum():
                    i = k  # drop the hyphen and the line break entirely; words join up
                    continue
            out_chars.append(ch)
            out_idx.append(i)
            i += 1
            continue

        if ch.isspace():
            if out_chars and out_chars[-1] == " ":
                i += 1
                continue
            out_chars.append(" ")
            out_idx.append(i)
            i += 1
            continue

        out_chars.append(ch)
        out_idx.append(i)
        i += 1

    while out_chars and out_chars[0] == " ":
        out_chars.pop(0)
        out_idx.pop(0)
    while out_chars and out_chars[-1] == " ":
        out_chars.pop()
        out_idx.pop()

    return "".join(out_chars), out_idx


def normalise_quote(s):
    """Normalise a quoted NCERT line for matching only: collapse whitespace/line breaks to
    single spaces, join end-of-line hyphenation, straighten curly quotes, expand ligatures.
    Case, punctuation and words are never touched."""
    text, _ = _normalise_with_positions(s)
    return text


if __name__ == "__main__":
    assert normalise_quote("chroma-\ntids") == "chromatids"
    assert normalise_quote("chroma-  \n  tids") == "chromatids"
    assert normalise_quote("well-known fact") == "well-known fact"  # mid-line hyphen kept
    assert normalise_quote("line one\nline   two") == "line one line two"
    assert normalise_quote("“hello’s”") == '"hello\'s"'
    assert normalise_quote("scientiﬁc") == "scientific"
    assert normalise_quote("  padded  ") == "padded"

    # Prove case and punctuation are preserved exactly (no case-folding, no stripping):
    original = "The Mitochondria, often called the 'power-house', is NOT fully understood."
    normalised = normalise_quote(original)
    assert normalised == original, normalised
    assert normalised.lower() != normalised  # case survived
    assert "," in normalised and "'" in normalised and "." in normalised  # punctuation survived
    assert "power-house" in normalised  # a genuine mid-word hyphen (no newline) is untouched

    print("text_normalise.py self-check OK:", repr(normalise_quote("chroma-\ntids  across\nlines")))
