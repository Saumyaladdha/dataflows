"""LaTeX-ish normalisation for comparing two independent readings of the same maths/chemistry
content (spec 5.7), e.g. B3 vs B4. This is for comparison only, never for display: it never
changes a digit, sign, letter or their order.
"""
import re

_UNICODE_MAP = {
    "Ω": r"\Omega",
    "μ": r"\mu",
    "ρ": r"\rho",
    "×": r"\times",
    "−": "-",  # U+2212 MINUS SIGN -> ASCII hyphen-minus; the sign itself is untouched
}

# \, \; \! are LaTeX *spacing* commands (thin/medium/negative-thin space). For comparison we
# collapse each to one ordinary space rather than deleting it outright, so "4\,\Omega" lines up
# with "4 Ω"/"$4 \Omega$" which spell the same gap with a literal space instead of a LaTeX
# spacing command (see T1: all three must normalise equal).
_SPACE_CMDS = re.compile(r"\\[,;!]")
_TEXT_CMD = re.compile(r"\\text\{([^{}]*)\}")


def normalise(s):
    """Normalise a LaTeX-ish string for comparing two readings of the same content: collapses
    whitespace, turns \\, \\; \\! spacing commands into a plain space, unwraps \\text{X} to X,
    maps a fixed set of Unicode math symbols (Ω μ ρ × −) to their LaTeX names, and drops $
    delimiters. Never changes digits, signs, letters or their order."""
    if s is None:
        return ""
    text = s

    for uni, rep in _UNICODE_MAP.items():
        text = text.replace(uni, rep)

    text = _SPACE_CMDS.sub(" ", text)

    prev = None
    while prev != text:
        prev = text
        text = _TEXT_CMD.sub(r"\1", text)

    text = text.replace("$", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


if __name__ == "__main__":
    a = normalise("4 Ω")
    b = normalise(r"4\,\Omega")
    c = normalise(r"$4 \Omega$")
    assert a == b == c, (a, b, c)

    assert normalise("4 Ω") != normalise("40 Ω")
    assert normalise("−2") != normalise("2")

    assert normalise(r"\text{NaCl}") == "NaCl"
    assert normalise(r"$\text{H}_2\text{O}$") == r"H_2O"
    assert normalise("5 × 10") == r"5 \times 10"
    assert normalise("  a   b  ") == "a b"

    print("latex_normalise.py self-check OK:", repr(a), repr(b), repr(c))
