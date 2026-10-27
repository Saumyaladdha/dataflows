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
    # Second census, 2017 Code-A (2026-10-26): `\\ge` printed red inside a printed solution, and
    # `\\varepsilon` (16 uses, the emf of a cell) beside it. The relation and variant-Greek families
    # are added WHOLE rather than one name at a time, because an agent that writes `\\ge` writes
    # `\\le` the next day; checks/latex_census.py is what proves nothing is still missing.
    "ge": "≥", "le": "≤", "ne": "≠", "gt": "&gt;", "lt": "&lt;", "geqslant": "⩾", "leqslant": "⩽",
    "varepsilon": "ε", "varphi": "φ", "vartheta": "ϑ", "varrho": "ϱ", "varpi": "ϖ",
    "varsigma": "ς", "digamma": "ϝ", "Gamma": "Γ", "Xi": "Ξ", "Upsilon": "Υ",
    "implies": "⟹", "iff": "⟺", "Leftarrow": "⇐", "Leftrightarrow": "⇔",
    "rightleftarrows": "⇄", "leftrightarrows": "⇆", "mapsto": "↦", "nearrow": "↗",
    "searrow": "↘", "hookrightarrow": "↪", "rightharpoonup": "⇀", "leftharpoondown": "↽",
    "ast": "∗", "mid": "∣", "nmid": "∤", "colon": ":", "neg": "¬", "lnot": "¬", "land": "∧",
    "lor": "∨", "wedge": "∧", "vee": "∨", "cap": "∩", "cup": "∪", "setminus": "∖",
    "subseteq": "⊆", "supseteq": "⊇", "triangle": "△", "square": "□", "checkmark": "✓",
    "langle": "⟨", "rangle": "⟩", "lbrace": "{", "rbrace": "}", "vert": "|", "Vert": "‖",
    "prod": "∏", "oint": "∮", "iint": "∬", "aleph": "ℵ", "Re": "ℜ", "Im": "ℑ",
    "textdegree": "°", "textperthousand": "‰", "permil": "‰",
    "vdots": "⋮", "ddots": "⋱", "approxeq": "≊", "doteq": "≐", "asymp": "≍", "bot": "⊥",
}
#: Text-style commands and the tag each one renders as. `\\textit` carried 9 species names on
#: 2017 Code-A (Ectocarpus, Fucus) and printed red; the whole family is listed so the next variant
#: does not.
TEXT_STYLES = {"mathrm": "span", "text": "span", "textrm": "span", "textnormal": "span",
               "operatorname": "span", "mathsf": "span", "textsf": "span", "texttt": "span",
               "mathtt": "span", "mathbf": "b", "textbf": "b", "boldsymbol": "b", "bm": "b",
               "mathit": "i", "textit": "i", "emph": "i", "textsl": "i", "mathcal": "i",
               "mathscr": "i", "mathbb": "b"}
#: Accents, as combining characters after their base. `\\ddot{u}` wrote "Lieberkühn" (2017_A q97).
ACCENTS = {"hat": "\u0302", "widehat": "\u0302", "vec": "\u20d7", "overrightarrow": "\u20d7",
           "bar": "\u0304", "overline": "\u0305", "tilde": "\u0303", "widetilde": "\u0303",
           "dot": "\u0307", "ddot": "\u0308", "check": "\u030c", "breve": "\u0306",
           "acute": "\u0301", "grave": "\u0300", "mathring": "\u030a"}
#: Accents drawn by CSS above their base, not as a combining character. U+20D7 (the vector
#: arrow) is missing from most text fonts and showed as a box: 2017_A q009's solution read
#: "a□ = -4 i m/s^2". An arrow or a bar over a whole group needs a box anyway.
CSS_ACCENTS = {"vec": "\u2192", "overrightarrow": "\u2192", "hat": "\u02c6", "widehat": "\u02c6",
               "dot": "\u02d9", "ddot": "\u00a8", "tilde": "\u02dc", "widetilde": "\u02dc",
               "check": "\u02c7", "breve": "\u02d8", "acute": "\u00b4", "grave": "`",
               "mathring": "\u02da"}
BAR_ACCENTS = ("bar", "overline")
#: A dotless base under an accent, so \hat{i} is one mark, not a hat over a dot.
DOTLESS = {"i": "ı", "j": "ȷ"}


def accent(name, body):
    """One accent over its base: a CSS overlay for arrows and bars, a combining mark otherwise."""
    base = body.strip()
    if name in BAR_ACCENTS:
        return '<span class="ovl">%s</span>' % _render(base)
    if name in CSS_ACCENTS:
        # the mark is its own element ABOVE the base, so it sits right in every font: a combining
        # character drifts to the side of a dotless i in Georgia ("i ^") and a missing one is a box
        shown = DOTLESS.get(base) or _render(base)
        return ('<span class="acc"><span class="acc-m">%s</span><span class="acc-b">%s</span></span>'
                % (CSS_ACCENTS[name], shown))
    return "%s%s" % (_render(base), ACCENTS[name])


def _optional(tex, i):
    """A LaTeX optional argument `[...]` at `i`, brackets nested, or (None, i) when there is none."""
    j = i
    while j < len(tex) and tex[j] == " ":
        j += 1
    if j >= len(tex) or tex[j] != "[":
        return None, i
    depth = 0
    for k in range(j, len(tex)):
        if tex[k] == "[":
            depth += 1
        elif tex[k] == "]":
            depth -= 1
            if depth == 0:
                return tex[j + 1:k], k + 1
    return None, i


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
                if spacer == "\\":
                    out.append("<br>")        # a line break: substack rows, aligned lines
                elif spacer in (",", ":", ";", " "):
                    out.append("&thinsp;" if spacer == "," else "&nbsp;")
                elif spacer == "!":
                    pass                      # negative thin space: no HTML equivalent, drop it
                else:
                    out.append(html.escape(spacer))   # an escaped literal such as \{ or \%
                i += 2
                continue
            name = match.group(1)
            i += 1 + len(name)
            if name in ("frac", "dfrac", "tfrac", "cfrac"):
                numerator, i = _group(tex, i)
                denominator, i = _group(tex, i)
                out.append('<span class="frac"><span class="num">%s</span>'
                           '<span class="den">%s</span></span>'
                           % (_render(numerator), _render(denominator)))
            elif name in TEXT_STYLES:
                body, i = _group(tex, i)
                tag = TEXT_STYLES[name]
                out.append("<%s class=\"up\">%s</%s>" % (tag, _render(body), tag))
            elif name == "ce":
                body, i = _group(tex, i)
                out.append('<span class="up">%s</span>' % _ce(body))
            elif name == "substack":
                body, i = _group(tex, i)
                out.append('<span class="stack">%s</span>' % _render(body))
            elif name in ("xrightarrow", "xleftarrow", "overset", "underset"):
                # An arrow (or a symbol) carrying a label. Rendered as arrow-with-label rather than
                # dropped, because in a reaction the label IS the reagent -- the chemistry is in it.
                below = None
                if name in ("xrightarrow", "xleftarrow"):
                    below, i = _optional(tex, i)
                first, i = _group(tex, i)
                if name in ("overset", "underset"):
                    second, i = _group(tex, i)
                    # STACKED, label over (or under) its base. The old form set the label small
                    # BESIDE the base, so a reagent over a reaction arrow read as stray text.
                    out.append('<span class="ovs %s"><span class="ovs-l">%s</span>'
                               '<span class="ovs-b">%s</span></span>'
                               % ("ovs-over" if name == "overset" else "ovs-under",
                                  _render(first), _render(second)))
                else:
                    # A STRETCHABLE arrow: as long as its longer label, the reagent above it and
                    # the condition below (`\xrightarrow[573 K]{Cu}`). The old form was one
                    # fixed arrow glyph with the label floated over it: a long reagent ran over
                    # the formulas on both sides, and the [below] argument printed as raw text
                    # ("->573 K]Cu" on 2017_A q061).
                    out.append('<span class="xarr %s"><span class="xa-t">%s</span>'
                               '<span class="xa-l"></span><span class="xa-b">%s</span></span>'
                               % ("xa-left" if name == "xleftarrow" else "xa-right",
                                  _render(first) or "&nbsp;",
                                  _render(below) if below else "&nbsp;"))
            elif name == "sqrt":
                index, i = _optional(tex, i)
                body, i = _group(tex, i)
                if index:
                    out.append('<sup class="rootidx">%s</sup>' % _render(index))
                out.append('<span class="rad">√</span><span class="sqrt">%s</span>'
                           % _render(body))
            elif name in ACCENTS:
                body, i = _group(tex, i)
                out.append(accent(name, body))
            elif name in ("underline", "underbrace", "overbrace"):
                body, i = _group(tex, i)
                tag = "u" if name == "underline" else "span"
                out.append("<%s>%s</%s>" % (tag, _render(body), tag))
            elif name in ("cancel", "bcancel", "xcancel", "sout"):
                body, i = _group(tex, i)
                out.append("<s>%s</s>" % _render(body))
            elif name == "boxed":
                body, i = _group(tex, i)
                out.append('<span class="boxed">%s</span>' % _render(body))
            elif name in ("left", "right", "big", "Big", "bigg", "Bigg", "bigl", "bigr", "Bigl",
                          "Bigr", "displaystyle", "textstyle", "scriptstyle", "limits",
                          "nolimits", "middle", "nonumber"):
                continue                      # sizing hints carry no content
            elif name in FUNCTIONS:
                out.append('<span class="up">%s</span>' % name)
            elif name in ("quad", "qquad", "enspace", "hspace", "hfill"):
                if name == "hspace":
                    _skip, i = _group(tex, i)
                out.append("&nbsp;&nbsp;")
            elif name == ",":
                out.append("&thinsp;")
            elif name in SYMBOLS:
                out.append(SYMBOLS[name])
            else:
                # UNKNOWN: left visible as written, so a gap can be seen and fixed
                out.append('<span class="tex-unknown">\\%s</span>' % html.escape(name))
        elif char in "^_":
            # A BARE COMMAND is the whole script: `120^\circ` is "120" with \circ raised. Taking
            # one character took only the backslash, and 2017_A q053's stem read "120circ".
            command = re.match(r"\\([A-Za-z]+)", tex[i + 1:])
            if command:
                body, i = command.group(0), i + 1 + command.end()
            else:
                body, i = _group(tex, i + 1)
            tag = "sup" if char == "^" else "sub"
            if tag == "sup" and body.strip() in ("\\circ", "{\\circ}", "\\degree"):
                out.append("°")                  # a raised circle IS the degree sign
            else:
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


_CE_TOKEN = re.compile(r"<=>|<->|->|<-|\^\{[^}]*\}|\^[0-9]*[+-]|[A-Z][a-z]?|\d+|\s+|.")


def _ce(body):
    """mhchem's `\\ce{...}`, the common subset: counts after an element or bracket become
    subscripts, `^2-` / `^{2-}` charges become superscripts, `->` and `<=>` become arrows. Agents
    reach for `\\ce{H2SO4}` unprompted, and without this it printed red."""
    out, previous = [], ""
    for token in _CE_TOKEN.findall(body):
        if token in ("->", "<-", "<=>", "<->"):
            out.append({"->": " ⟶ ", "<-": " ⟵ ", "<=>": " ⇌ ", "<->": " ⟷ "}[token])
        elif token.startswith("^"):
            out.append("<sup>%s</sup>" % html.escape(token[1:].strip("{}")))
        elif token.isdigit() and (previous[-1:].isalpha() or previous[-1:] in ")]"):
            out.append("<sub>%s</sub>" % token)
        else:
            out.append(html.escape(token))
        if not token.isspace():
            previous = token
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
        return '<span class="rad">√</span><span class="sqrt">%s</span>' % inner

    out = _PROSE_ROOT.sub(root, escaped)
    out = _PROSE_FRACTION.sub(
        lambda m: '<span class="frac"><span class="num">%s</span>'
                  '<span class="den">%s</span></span>' % (m.group(1), m.group(2)), out)
    return _PROSE_INDEX.sub(r'\1<sub class="tex">\2</sub>', out)


#: LaTeX spacing and escaped literals typed OUTSIDE `$...$`, between maths spans.
_PROSE_COMMANDS = re.compile(r"\\(quad|qquad|[,;: ]|\{|\}|%|_|#)")


def _commands_in_prose(escaped):
    """`$x = 5t$ \\quad $y = 10t$` (2017_A q9's printed solution) printed "\\quad" literally,
    because only text inside `$` was rendered. Spacing becomes space; `\\{` becomes a brace."""
    def one(match):
        name = match.group(1)
        if name in ("quad", "qquad"):
            return "&nbsp;&nbsp;&nbsp;"
        if name in (",", ";", ":", " "):
            return "&thinsp;"
        return name
    return _PROSE_COMMANDS.sub(one, escaped)


def _scripts_in_prose(escaped):
    """Render `_{3}` and `^2` in already-escaped text. Runs on escaped input, which is safe because
    `html.escape` leaves braces, carets and underscores untouched."""
    def sub(m):
        tag = "sub" if m.group(1) == "_" else "sup"
        return "<%s class=\"tex\">%s</%s>" % (tag, m.group(2), tag)
    def render(chunk):
        chunk = _commands_in_prose(chunk)
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


#: A LaTeX command written in PROSE, outside any `$...$`, with its brace arguments (one level of
#: nesting): `\frac{dv}{dt}`, `\Delta`, `\underset{x}{y}`. Agents write these in notes and reasons --
#: 9 of them on 2017 Code-A -- and they printed as raw source.
_BARE_LATEX = re.compile(r"\\(?!quad\b|qquad\b)[A-Za-z]+(?:\{(?:[^{}]|\{[^{}]*\})*\})*")


def _prose(chunk):
    """Prose between maths spans: escaped, scripts rendered, and any bare LaTeX command rendered as
    maths when the renderer knows it (an unknown one stays visible, as everywhere else)."""
    out, last = [], 0
    for match in _BARE_LATEX.finditer(chunk):
        name = re.match(r"\\([A-Za-z]+)", match.group(0)).group(1)
        known = (name in SYMBOLS or name in TEXT_STYLES or name in ACCENTS or name in FUNCTIONS
                 or name in ("frac", "dfrac", "tfrac", "cfrac", "sqrt", "ce", "substack",
                             "overset", "underset", "xrightarrow", "xleftarrow", "underline",
                             "boxed", "cancel"))
        if not known:
            continue
        out.append(_scripts_in_prose(html.escape(chunk[last:match.start()])))
        out.append('<span class="math">%s</span>' % _render(match.group(0)))
        last = match.end()
    out.append(_scripts_in_prose(html.escape(chunk[last:])))
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
        out.append(_prose(text[last:match.start()]))
        body = next(g for g in match.groups() if g is not None)
        out.append('<span class="math">%s</span>' % _render(body))
        last = match.end()
    out.append(_prose(text[last:]))
    rendered = "".join(out)
    return rendered.replace("\n", "<br>") if line_breaks else rendered.replace("\n", " ")


CSS = """
.math{white-space:nowrap}
.math .up{font-style:normal}
.frac{display:inline-block;vertical-align:-0.55em;text-align:center;margin:0 .16em;
 font-size:.88em;line-height:1.3}
.frac .num{display:block;border-bottom:1.2px solid currentColor;padding:0 .28em .1em}
.frac .den{display:block;padding:.1em .28em 0}
.frac sub{vertical-align:-.18em}.frac sup{vertical-align:.36em}
.rad{font-size:1.04em;margin-left:.04em}
.sqrt{border-top:1.1px solid currentColor;padding:.04em .02em 0 .04em;white-space:nowrap}
.acc{position:relative;display:inline-block;line-height:1;padding-top:.18em}
.acc-m{position:absolute;left:0;right:0;top:-.38em;text-align:center;font-size:.62em;
 line-height:1;font-style:normal}
.acc-b{line-height:1}
.ovl{display:inline-block;border-top:1px solid currentColor;padding-top:.04em;line-height:1}
.rootidx{font-size:.55em;margin-right:-.35em;vertical-align:.9em}
.xarr{display:inline-flex;flex-direction:column;align-items:stretch;vertical-align:middle;
 margin:0 .3em;min-width:2em;text-align:center;line-height:1.1}
.xa-t,.xa-b{font-size:.68em;padding:0 .4em;white-space:nowrap}
.xa-l{position:relative;height:0;border-top:1.2px solid currentColor;margin:.12em 0}
.xa-right .xa-l::after,.xa-left .xa-l::before{content:"";position:absolute;top:-.3em;
 border-top:.27em solid transparent;border-bottom:.27em solid transparent}
.xa-right .xa-l::after{right:-1px;border-left:.5em solid currentColor}
.xa-left .xa-l::before{left:-1px;border-right:.5em solid currentColor}
.math sup,.math sub{font-size:.72em;line-height:0}
sup.tex,sub.tex{font-size:.72em;line-height:0}
.labelled{position:relative;display:inline-block;padding:0 .15em}
.labelled .lbl{position:absolute;left:0;right:0;bottom:.85em;font-size:.6em;text-align:center;
 white-space:nowrap;line-height:1}
.over,.under{font-size:.72em}
.ovs{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;
 line-height:1.05;margin:0 .1em}
.ovs-under{flex-direction:column-reverse}
.ovs-l{font-size:.68em}
.stack{display:inline-flex;flex-direction:column;align-items:center;line-height:1.1}
.boxed{border:1px solid currentColor;padding:0 .2em}
.tex-unknown{color:#b33;font-family:ui-monospace,monospace;font-size:.85em}
"""
