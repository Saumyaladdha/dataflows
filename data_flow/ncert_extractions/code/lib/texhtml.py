"""Render the LaTeX these papers actually use into plain HTML, with no network and no library.

WHY NOT KATEX OR MATHJAX
------------------------
Both were tried from a CDN and both fail in the one place the output is read: a local file opened in
an editor preview, where external scripts are blocked or there is no network. The page then shows
`$\\frac{4}{9}$` as literal source, which is harder to read than either the rendered maths or the
plain text would be -- the worst of the three outcomes.

So the LaTeX is rendered HERE, at export time, into `<sup>`, `<sub>` and a small CSS fraction. The
page that results needs nothing but itself.

WHAT THIS DELIBERATELY IS NOT
-----------------------------
Not a LaTeX engine. It covers the constructs `b3-question-reader` is instructed to emit -- fractions,
scripts, roots, Greek letters, the common operators and `\\mathrm` -- and leaves anything else EXACTLY
as written rather than guessing. An unrendered `\\overbrace` is a visible gap someone can fix; a
silently mangled one is a wrong answer that looks right.
"""

import html
import re

#: Greek and the symbols these papers use. Anything absent stays as its own source text.
SYMBOLS = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "Delta": "Δ", "epsilon": "ε",
    "zeta": "ζ", "eta": "η", "theta": "θ", "Theta": "Θ", "iota": "ι", "kappa": "κ",
    "lambda": "λ", "Lambda": "Λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π", "Pi": "Π",
    "rho": "ρ", "sigma": "σ", "Sigma": "Σ", "tau": "τ", "upsilon": "υ", "phi": "φ",
    "Phi": "Φ", "chi": "χ", "psi": "ψ", "Psi": "Ψ", "omega": "ω", "Omega": "Ω",
    "times": "×", "cdot": "·", "div": "÷", "pm": "±", "mp": "∓", "approx": "≈",
    "neq": "≠", "leq": "≤", "geq": "≥", "ll": "≪", "gg": "≫", "infty": "∞",
    "rightarrow": "→", "leftarrow": "←", "Rightarrow": "⇒", "leftrightarrow": "↔",
    "rightleftharpoons": "⇌", "to": "→", "propto": "∝", "degree": "°", "circ": "∘",
    "prime": "′", "angle": "∠", "perp": "⊥", "parallel": "∥", "therefore": "∴",
    "because": "∵", "sum": "∑", "int": "∫", "partial": "∂", "nabla": "∇",
    "hbar": "ℏ", "ell": "ℓ", "AA": "Å", "ohm": "Ω", "Omega_sym": "Ω",
    # Measured from the corpus by a census of every `\\cmd` these papers actually emit, rather
    # than guessed: longrightarrow and ominus are the reaction arrow and the standard-state circle
    # that chemistry stems use constantly.
    "longrightarrow": "⟶", "longleftarrow": "⟵", "longleftrightarrow": "⟷",
    "Longrightarrow": "⟹", "ominus": "⊖", "oplus": "⊕", "otimes": "⊗", "odot": "⊙",
    "uparrow": "↑", "downarrow": "↓", "equiv": "≡", "sim": "∼", "simeq": "≃",
    "cong": "≅", "subset": "⊂", "supset": "⊃", "in": "∈", "notin": "∉",
    "forall": "∀", "exists": "∃", "emptyset": "∅", "cdots": "⋯", "ldots": "…",
    "dots": "…", "star": "★", "bullet": "•", "dagger": "†", "lambda_": "λ",
}
#: Functions that should read upright, not italic.
FUNCTIONS = ("sin", "cos", "tan", "cot", "sec", "cosec", "csc", "log", "ln", "exp",
             "sinh", "cosh", "tanh", "max", "min", "lim")

_BRACED = r"\{([^{}]*)\}"


def _group(text, index):
    """Read one LaTeX argument starting at `index`: `{...}` with nesting, or a single character."""
    if index >= len(text):
        return "", index
    if text[index] != "{":
        return text[index], index + 1
    depth, start = 0, index
    for position in range(index, len(text)):
        if text[position] == "{":
            depth += 1
        elif text[position] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:position], position + 1
    return text[index + 1:], len(text)


def _render(tex):
    """One pass over a maths span. Recurses into every argument."""
    out, i = [], 0
    while i < len(tex):
        char = tex[i]
        if char == "\\":
            match = re.match(r"\\([A-Za-z]+)", tex[i:])
            if not match:
                # A NON-LETTER escape. `\,` is the most common thing in these stems after `\frac`
                # (128 occurrences): it is LaTeX's thin space, and the old code fell through to the
                # escaped-literal branch below and printed a comma -- turning `141\,kJ\,mol^{-1}`
                # into "141,kJ,mol-1". The spacing commands are handled first, by name.
                spacer = tex[i + 1:i + 2]
                if spacer in (",", ":", ";", " "):
                    out.append("&thinsp;" if spacer == "," else "&nbsp;")
                elif spacer == "!":
                    pass                      # negative thin space: no HTML equivalent, drop it
                else:
                    out.append(html.escape(spacer))   # an escaped literal such as \{ or \%
                i += 2
                continue
            name = match.group(1)
            i += 1 + len(name)
            if name == "frac":
                numerator, i = _group(tex, i)
                denominator, i = _group(tex, i)
                out.append('<span class="frac"><span class="num">%s</span>'
                           '<span class="den">%s</span></span>'
                           % (_render(numerator), _render(denominator)))
            elif name in ("mathrm", "text", "mathbf", "mathit", "operatorname"):
                body, i = _group(tex, i)
                tag = "b" if name == "mathbf" else ("i" if name == "mathit" else "span")
                out.append("<%s class=\"up\">%s</%s>" % (tag, _render(body), tag))
            elif name in ("xrightarrow", "xleftarrow", "overset", "underset"):
                # An arrow (or a symbol) carrying a label. Rendered as arrow-with-label rather than
                # dropped, because in a reaction the label IS the reagent -- the chemistry is in it.
                first, i = _group(tex, i)
                if name in ("overset", "underset"):
                    second, i = _group(tex, i)
                    out.append('<span class="%s">%s</span>%s'
                               % ("over" if name == "overset" else "under",
                                  _render(first), _render(second)))
                else:
                    arrow = "⟶" if name == "xrightarrow" else "⟵"
                    out.append('<span class="labelled">%s<span class="lbl">%s</span></span>'
                               % (arrow, _render(first)))
            elif name == "sqrt":
                body, i = _group(tex, i)
                out.append('<span class="sqrt">%s</span>' % _render(body))
            elif name in ("hat", "vec", "bar", "overline", "tilde"):
                body, i = _group(tex, i)
                accent = {"hat": "̂", "vec": "⃗", "bar": "̄",
                          "overline": "̄", "tilde": "̃"}[name]
                out.append("%s%s" % (_render(body), accent))
            elif name in ("left", "right", "big", "Big", "bigg", "Bigg", "displaystyle",
                          "limits", "nolimits"):
                continue                      # sizing hints carry no content
            elif name in FUNCTIONS:
                out.append('<span class="up">%s</span>' % name)
            elif name in ("quad", "qquad"):
                out.append("&nbsp;&nbsp;")
            elif name == ",":
                out.append("&thinsp;")
            elif name in SYMBOLS:
                out.append(SYMBOLS[name])
            else:
                # UNKNOWN: left visible as written, so a gap can be seen and fixed
                out.append('<span class="tex-unknown">\\%s</span>' % html.escape(name))
        elif char in "^_":
            body, i = _group(tex, i + 1)
            tag = "sup" if char == "^" else "sub"
            out.append("<%s>%s</%s>" % (tag, _render(body), tag))
        elif char in "{}":
            i += 1
        elif char == "~":
            out.append("&nbsp;")
            i += 1
        else:
            out.append(html.escape(char))
            i += 1
    return "".join(out)


_MATH = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$|\\\((.+?)\\\)|\\\[(.+?)\\\]", re.S)


#: Scripts that appear in PROSE, outside any `$...$`. The text-layer draft is full of these: the
#: superscript repair writes `HNO_{3}` straight into the draft with no delimiters, because the draft
#: is reconstructed from PDF span positions and never passed through a LaTeX writer. Rendering only
#: inside `$` would leave every drafted formula showing its own braces.
_PROSE_BRACED = re.compile(r"([_^])\{([^{}$]{1,24})\}")
#: A single character script, but only where a formula could plausibly sit: directly after a letter,
#: digit or closing bracket. This keeps `snake_case` words and stray carets in ordinary prose alone.
_PROSE_BARE = re.compile(r"(?<=[A-Za-z0-9\)\]])([_^])([0-9]{1,3}|[+-]?[0-9]{0,2}[+-]?)(?![A-Za-z0-9])")


#: ASCII maths a human types in a prose field: `root(gh)`, `root 2`, `sqrt(x)`.
#: The BARE form is restricted to things that can actually sit under a radical -- a number, or a
#: short symbol like `gh` or `2L`. English number words are excluded by name, because "root two" is
#: prose, and setting the word "two" under a radical sign produces the nonsense `\u221Atwo`.
_NUMBER_WORDS = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "it",
                 "this", "that", "the", "them", "of", "and", "is", "are")
#: Greek letters written as WORDS. An agent asked for a relation "as short as it can be written"
#: has no LaTeX to put them in, so `E = hc / lambda` and `DeltaTf = Kf m` arrive as plain words --
#: and a concept line is the most prominent sentence on a card, so `lambda` sitting in it as a word
#: is the first thing a reader sees.
#:
#: THIS IS NOT APPLIED TO PROSE, and the first attempt was: it turned "a lambda phage vector" into
#: "a λ phage vector", which is wrong and would have been wrong across every stem in the corpus.
#: `greek_in_relation` is called only on fields that ARE relations by definition -- QCA's `concept`
#: and `also_uses` -- where a Greek word can only be the letter.
_GREEK_WORDS = {"lambda": "&lambda;", "mu": "&mu;", "nu": "&nu;", "rho": "&rho;",
                "sigma": "&sigma;", "tau": "&tau;", "omega": "&omega;", "theta": "&theta;",
                "phi": "&phi;", "alpha": "&alpha;", "beta": "&beta;", "gamma": "&gamma;",
                "delta": "&delta;", "epsilon": "&epsilon;", "eta": "&eta;", "pi": "&pi;",
                "psi": "&psi;", "chi": "&chi;", "kappa": "&kappa;",
                "Delta": "&Delta;", "Omega": "&Omega;", "Sigma": "&Sigma;", "Phi": "&Phi;"}
#: Lower-case names must stand alone; the capitalised ones may prefix a symbol, because `DeltaTf`
#: and `OmegaR` are how a relation is actually typed.
_GREEK_LOWER = re.compile(r"(?<![A-Za-z])(?:%s)(?![A-Za-z])"
                          % "|".join(sorted((k for k in _GREEK_WORDS if k[0].islower()),
                                            key=len, reverse=True)))
_GREEK_UPPER = re.compile(r"(?<![A-Za-z])(?:%s)(?![a-z])"
                          % "|".join(sorted((k for k in _GREEK_WORDS if k[0].isupper()),
                                            key=len, reverse=True)))


def greek_in_relation(text, line_breaks=False):
    """`to_html`, plus Greek letters spelled out as words. For RELATION fields only."""
    out = to_html(text, line_breaks=line_breaks)
    out = _GREEK_UPPER.sub(lambda m: _GREEK_WORDS[m.group(0)], out)
    return _GREEK_LOWER.sub(lambda m: _GREEK_WORDS[m.group(0).lower()], out)

_PROSE_ROOT = re.compile(r"\b(?:root|sqrt)\s*(?:\(([^()]{1,40})\)|([A-Za-z0-9]{1,6})\b)")
#: A physics symbol with an index: `v0`, `m1`, `t2`, `C1`. One letter then one or two digits, with a
#: word boundary either side, so `10 with 14` and `Nylon-6` are untouched.
_PROSE_INDEX = re.compile(r"\b([A-Za-z])([0-9]{1,2})\b")
#: A parenthesised numeric fraction, `(1/2)`, `(3/4)`. Digits only on BOTH sides, deliberately: a
#: letter pair like `(a/b)` is far more likely to be option labels than a fraction, and rendering
#: that as a stacked fraction would invent maths that was never written.
_PROSE_FRACTION = re.compile(r"\((\d{1,3})\s*/\s*(\d{1,3})\)")


def _ascii_maths_in_prose(escaped):
    """Render the ASCII maths that appears in PROSE fields -- trap routes, reasons, notes.

    These fields are written by a rater in plain language, and a rater typing a route writes
    `v0 = root(gh) = root 200 = 14 m/s`, not `$v_0 = \\sqrt{gh}$`. The agents are now asked for
    LaTeX, but hundreds of routes already exist in ASCII and re-running them to change notation
    would be a waste. Both forms therefore render.

    Conservative on purpose. Only two constructs are recognised, and both are unambiguous in prose;
    anything else is left exactly as typed, because a wrong transform here invents maths the rater
    did not write.
    """
    def root(match):
        inner = match.group(1) if match.group(1) is not None else match.group(2)
        if match.group(1) is None and inner.lower() in _NUMBER_WORDS:
            return match.group(0)            # "root two" is prose, not a radical
        return '<span class="sqrt">%s</span>' % inner

    out = _PROSE_ROOT.sub(root, escaped)
    out = _PROSE_FRACTION.sub(
        lambda m: '<span class="frac"><span class="num">%s</span>'
                  '<span class="den">%s</span></span>' % (m.group(1), m.group(2)), out)
    return _PROSE_INDEX.sub(r'\1<sub class="tex">\2</sub>', out)


def _scripts_in_prose(escaped):
    """Render `_{3}` and `^2` in already-escaped text. Runs on escaped input, which is safe because
    `html.escape` leaves braces, carets and underscores untouched."""
    def sub(m):
        tag = "sub" if m.group(1) == "_" else "sup"
        return "<%s class=\"tex\">%s</%s>" % (tag, m.group(2), tag)
    def render(chunk):
        chunk = _PROSE_BRACED.sub(sub, chunk)
        chunk = _PROSE_BARE.sub(lambda m: sub(m) if m.group(2) else m.group(0), chunk)
        return _ascii_maths_in_prose(chunk)

    return _outside_entities(escaped, render)


#: An HTML entity produced by escaping -- `&#x27;` for an apostrophe, `&amp;`, `&lt;`. The prose
#: transforms run on ESCAPED text, so they must not reach inside one: `&#x27;` is a letter followed
#: by two digits, which is exactly the shape `_PROSE_INDEX` treats as a physics index, and
#: "Sulphur's" came out as "Sulphur&#x<sub>27</sub>;s".
_ENTITY = re.compile(r"&(?:#x?[0-9A-Fa-f]+|[A-Za-z]+);")


def _outside_entities(text, transform):
    """Apply `transform` to the parts of `text` that are not HTML entities."""
    out, last = [], 0
    for match in _ENTITY.finditer(text):
        out.append(transform(text[last:match.start()]))
        out.append(match.group(0))
        last = match.end()
    out.append(transform(text[last:]))
    return "".join(out)


def to_html(text, line_breaks=True):
    """Escape prose, render every `$...$` span, and return HTML.

    Text outside the delimiters is escaped normally, so a stray `<` in a stem is safe and an
    unbalanced `$` leaves its text alone instead of swallowing the rest of the question.

    NEWLINES BECOME `<br>`, because in these stems a line break is CONTENT, not formatting. The
    booklet prints

        O(g) + e- -> O-(g)    ; dH = -141 kJ/mol
        O-(g) + e- -> O2-(g)  ; dH = +780 kJ/mol

    as two lines, and `b3-question-reader` reads them as two lines. HTML collapses them to one, and
    the two equations then run together into a single unreadable sentence -- the same damage for
    "Statement I ... Statement II" and for any lettered part list. Pass `line_breaks=False` only
    where a single line is genuinely wanted, such as a CSV cell.
    """
    if not text:
        return ""
    out, last = [], 0
    for match in _MATH.finditer(text):
        out.append(_scripts_in_prose(html.escape(text[last:match.start()])))
        body = next(g for g in match.groups() if g is not None)
        out.append('<span class="math">%s</span>' % _render(body))
        last = match.end()
    out.append(_scripts_in_prose(html.escape(text[last:])))
    rendered = "".join(out)
    return rendered.replace("\n", "<br>") if line_breaks else rendered.replace("\n", " ")


CSS = """
.math{white-space:nowrap}
.math .up{font-style:normal}
.frac{display:inline-block;vertical-align:-0.48em;text-align:center;margin:0 .16em;
 font-size:.88em;line-height:1.05}
.frac .num{display:block;border-bottom:1.2px solid currentColor;padding:0 .28em}
.frac .den{display:block;padding:0 .28em}
.sqrt::before{content:"\\221A"}
.sqrt{border-top:1.1px solid currentColor;padding:0 .12em 0 .04em;margin-left:.04em;
 white-space:nowrap}
.math sup,.math sub{font-size:.72em;line-height:0}
sup.tex,sub.tex{font-size:.72em;line-height:0}
.labelled{position:relative;display:inline-block;padding:0 .15em}
.labelled .lbl{position:absolute;left:0;right:0;bottom:.85em;font-size:.6em;text-align:center;
 white-space:nowrap;line-height:1}
.over,.under{font-size:.72em}
.tex-unknown{color:#b33;font-family:ui-monospace,monospace;font-size:.85em}
"""
