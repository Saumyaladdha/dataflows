"""What a printed figure SAYS, and whether a redraw of it says all of it.

A redraw can be valid and still incomplete. On 2017 Code-A, q061's scheme printed X (C2H6O), A, Y,
Z, "Cu / 573 K", the Tollens reagent and "Silver mirror observed", and the drawing showed one
molecule; q053's BCl3 printed "120 deg" and the drawing had no angle. Every check passed, because no
check knew what the printed figure contained.

These booklets are vector PDFs, so it is known exactly: the words inside the figure's box on the
page. `printed_text()` reads them. `missing()` compares them with the words a card actually DRAWS
(labels, scheme text, annotations -- never the card's description). A printed word is accounted for
when it is drawn, when it is chemistry the structure itself shows (an atom symbol, a subscript), or
when the agent listed it in `excluded_text` with a reason (a stem line that strays into the box).
Anything else is MISSING, and the card goes back to its agent naming each word.
"""

import re
import unicodedata

#: Greek and symbols the booklets set in the Symbol font, which the text layer returns as private-use
#: code points (U+F0xx): 2017_A's drafts carry  for lambda and  for Delta.
SYMBOL_FONT = {"a": "α", "b": "β", "c": "χ", "d": "δ", "e": "ε", "f": "φ", "g": "γ", "h": "η",
               "l": "λ", "m": "μ", "n": "ν", "p": "π", "q": "θ", "r": "ρ", "s": "σ", "t": "τ",
               "w": "ω", "D": "Δ", "W": "Ω", "F": "Φ", "q": "θ", "°": "°"}
#: One printed token: a word, a number, or a single Greek letter / degree sign.
TOKEN = re.compile(r"[A-Za-z]+|\d+(?:\.\d+)?|[°α-ωΑ-Ω]")
#: The publisher's answer and solution markers (with an answer's option number), and an option's
#: own number: layout, not figure content.
MARKERS = re.compile(r"\b(?:Answer|Ans)\b\.?\s*(?:\(\s*[1-4](?:\s*[&,]\s*[1-4])*\s*\)\*?)?"
                     r"|\bSol(?:ution)?\b\s*[.:]?", re.I)
#: A sub- or superscript: digits, a charge, brackets.
SCRIPT = re.compile(r"^[0-9+\-–−()]+$")
OPTION_NUMBER = re.compile(r"\(\s*[1-4]\s*\)")
#: A token that is nothing but element symbols -- NH, OH, Cl, CH -- which a structure draws itself.
ELEMENTS_ONLY = re.compile(r"^(?:[A-Z][a-z]?)+$")
ELEMENT = re.compile(r"[A-Z][a-z]?")


def normalise(text):
    """Fold the text layer's encodings onto plain characters: subscripts to digits, Symbol-font
    Greek to Greek, the two Deltas to one, every dash to a hyphen."""
    out = []
    for ch in text or "":
        code = ord(ch)
        if 0xF000 <= code <= 0xF0FF:
            ch = SYMBOL_FONT.get(chr(code - 0xF000), " ")
        out.append(ch)
    text = unicodedata.normalize("NFKC", "".join(out))
    return (text.replace("∆", "Δ").replace("–", "-").replace("—", "-")
            .replace("−", "-").replace("º", "°"))


def printed_text(doc, page_index, box_px, dpi):
    """The words printed inside `box_px` (pixels at `dpi`) on one page, as one normalised string.

    Built from styled SPANS, each kept when at least half of it lies in the box -- clipping by
    character left fragments at every edge ("swer (2)" from the `Answer (2)` above a solution
    figure, "respec" from a stem line beside q036's spring), each read as a label the drawing had
    dropped. A SCRIPT -- a digit or charge set under 72% of the size of the text it touches -- is
    joined to that text: the layer stores CH3I's "3" and C2H6O's "2" and "6" as spans of their own,
    often on a line of their own (their baseline differs), and apart they read as standalone
    numbers. Locants are not scripts: q089's 1-6 are 80% of the atom size and touch nothing.
    The publisher's Answer/Sol. markers are dropped.
    """
    import pymupdf
    k = 72.0 / dpi
    clip = pymupdf.Rect(box_px[0] * k, box_px[1] * k, box_px[2] * k, box_px[3] * k)
    spans = []
    for block in doc[page_index].get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span.get("text", "")
                rect = pymupdf.Rect(span["bbox"])
                area = rect.width * rect.height
                if text.strip() and area > 0 and (rect & clip).get_area() >= 0.5 * area:
                    spans.append({"text": text, "rect": rect, "size": span["size"], "tail": ""})
    kept = []
    for span in spans:
        base = None
        if SCRIPT.match(span["text"].strip()):
            # the span this one is written against: ends where it starts, overlaps it vertically,
            # and is set at least ~1.4x larger
            for other in spans:
                r, o = span["rect"], other["rect"]
                if (other is not span and span["size"] < 0.72 * other["size"]
                        and o.x1 - 2.0 <= r.x0 <= o.x1 + 2.5
                        and min(r.y1, o.y1) - max(r.y0, o.y0) > 0):
                    base = other
                    break
        if base is not None:
            base["tail"] += span["text"].strip()
        else:
            kept.append(span)
    text = " ".join(s["text"].rstrip() + s["tail"] for s in kept)
    return normalise(re.sub(r"\s+", " ", MARKERS.sub(" ", text))).strip()


def tokens(text):
    return TOKEN.findall(normalise(OPTION_NUMBER.sub(" ", text or "")))


def missing(printed, drawn_texts, excluded_texts=(), elements=None):
    """Printed tokens no drawn text, no structure and no exclusion accounts for, in printed order.

    `elements` is the set of element symbols the card's structures contain (None for a physics
    figure): with it, an atom-label token (NH, OH, Cl) and a one- or two-digit subscript or charge
    count are the structure's own and need no separate label.
    """
    drawn = set()
    for text in drawn_texts:
        drawn.update(tokens(text))
    for text in excluded_texts:
        drawn.update(tokens(text))
    lower = {t.lower() for t in drawn}
    out = []
    for word in normalise(OPTION_NUMBER.sub(" ", printed or "")).split():
        attached = bool(re.search(r"[A-Za-z]", word))
        for token in TOKEN.findall(word):
            if token in drawn or (len(token) > 1 and token.lower() in lower):
                continue
            if elements is not None:
                if ELEMENTS_ONLY.match(token) and set(ELEMENT.findall(token)) <= (elements | {"H"}):
                    continue
                # a subscript or count ATTACHED to its atoms ("NH2", "CH3") is the structure's
                # own; a digit standing alone is a printed label -- q089's locants 1-6 were
                # excused as "subscripts" and the drawing shipped without them
                if token.isdigit() and len(token) <= 2 and attached:
                    continue
            if token not in out:
                out.append(token)
    return out
