#!/usr/bin/env python3
"""Put the A2S AGENT's transcriptions of TABLES, EQUATIONS and FIGURES onto the elements.

    from join_agent_special import apply_agent_special
    stats = apply_agent_special(layout, "BIO11L-ch01")

The third joiner, after `join_agent_text` (words) and `join_agent_layout` (arrangement). A2S is
asked for the things a page's running text does not contain: the cells of a table, the LaTeX of
an equation, the content of a figure.

WHY THE AGENT BEATS THE GEOMETRY HERE, MEASURED
-------------------------------------------------
A table's columns CAN be rebuilt from span positions -- `_cell_grid` in
`extract_page_layout.py` does it, clustering the x of every span. On BIO11L ch01's Table 1.1
that recovers a 6 x 7 grid, which is the right shape. But it recovers it IMPERFECTLY:

    geometry grid   'Monocotyledona'     'Phylum/'  +  'Division'  as two header rows
    A2S             'Monocotyledonae'    'Phylum/ Division'        as one header cell

The truncation is not a bug in the clustering; it is the text layer cutting a word at a column
boundary, and no amount of geometry recovers a character that is not there. The agent read the
page image and transcribed what is printed.

So A2S wins for a table, and the geometry grid stays as the FALLBACK for the pages A2S has not
covered -- which is most of them: 1,014 A2S outputs exist corpus-wide against ~3,300 pages.

WHAT A2S RETURNS, BY KIND
---------------------------
    table      caption, header[], rows[][], repeated_header
    equation   latex
    figure     the figure's own text content and labels

Each file is named `<chapter>-p<page>-b<block>.<run>.json`, so it is matched on the PAGE and the
BLOCK NUMBER -- the same `n` A2 assigned, which `join_agent_text` has already written onto the
element as `a2_block_n`. That makes the match exact rather than positional; nothing is matched
by guessing which table on the page was meant.
"""

import glob
import json
import os
import re

_RUN_PRIORITY = {"adjudicated": 0, "retry2": 1, "retry1": 2, "runB": 3, "runA": 4}
_NAME_RE = re.compile(r"-p(\d+)-b(\d+)\.(\w+)\.json$")


def a2s_files(chapter, steps_dir="steps"):
    """{(page, block): path} keeping the most-settled run for each block."""
    best = {}
    for path in glob.glob(os.path.join(steps_dir, "A2S", "out", f"{chapter}-p*-b*.json")):
        m = _NAME_RE.search(os.path.basename(path))
        if not m:
            continue
        key = (int(m.group(1)), int(m.group(2)))
        rank = _RUN_PRIORITY.get(m.group(3), 9)
        if key not in best or rank < best[key][0]:
            best[key] = (rank, path)
    return {k: v[1] for k, v in best.items()}


def _italic_words(els):
    """The italic fragments the page printed in these elements' runs, for re-applying to cells.

    A2S returns cells as plain strings, so every genus in a table came out upright --
    `(a) Chlamydomonas`, `Homo sapiens` -- although the book sets them in italic. The text layer
    knows which runs are italic; those fragments are matched back into the cells by text."""
    out = []
    for e in els:
        for r in e.get("runs") or []:
            t = re.sub(r"\s+", " ", r.get("t") or "").strip(" ,;:.")
            if r.get("i") and len(t) >= 3 and t not in out:
                out.append(t)
    return out


_SUB = str.maketrans("0123456789+-=()n", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₙ")
_SUP = str.maketrans("0123456789+-=()n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ")
_SYMBOLS = {r"\oplus": "⊕", r"\male": "♂", r"\female": "♀", r"\times": "×",
            r"\rightarrow": "→", r"\to": "→", r"\pm": "±", r"\%": "%", r"\frown": "",
            # BIO11L ch09: the enzyme-class reactions and the carbonic anhydrase equilibrium
            r"\longrightarrow": "→", r"\leftarrow": "←", r"\longleftarrow": "←",
            r"\rightleftharpoons": "⇌", r"\leftrightarrow": "↔", r"\displaystyle": "",
            r"\delta": "δ", r"\Delta": "Δ", r"\alpha": "α", r"\beta": "β", r"\gamma": "γ",
            r"\mu": "µ", r"\cdot": "·", r"\circ": "°", r"\ldots": "…", r"\cdots": "…"}
_SPACES = (r"\quad", r"\qquad", r"\,", r"\;", r"\:", r"\ ")


def latex_to_runs(latex, like):
    """Simple printed notation as text runs -- or None when the LaTeX is beyond that.

    Covers what NCERT sets inline: symbols, sub/superscripts whose characters have Unicode
    forms, `\\underline` / `\\overline` (as combining marks: G̲ superior ovary, G̅ inferior),
    `\\text` and `\\textbf`. A fraction, a root or a matrix returns None and the element keeps
    the text it had; printing half an equation is worse than printing the flat one.
    `\\overset{\\frown}{...}` -- the adhesion arc of a floral formula -- has no Unicode form and is
    dropped from the TEXT only; the node keeps the full LaTeX.
    """
    base = next((r for r in (like.get("runs") or []) if r.get("t", "").strip()), {})
    runs, bold = [], [False]
    s, i = latex, 0

    def emit(t, b=None):
        if not t:
            return
        b = bold[0] if b is None else b
        if runs and runs[-1]["b"] == b:
            runs[-1]["t"] += t
        else:
            runs.append({"t": t, "b": b, "i": False, "sc": False, "script": None,
                         "color": base.get("color", "#231f20"), "size": base.get("size"),
                         "font": base.get("font")})

    def group(j):
        """(content, end) of the {...} group or single token starting at j."""
        while j < len(s) and s[j] == " ":
            j += 1
        if j < len(s) and s[j] == "{":
            depth, k = 0, j
            while k < len(s):
                depth += {"{": 1, "}": -1}.get(s[k], 0)
                if depth == 0:
                    return s[j + 1:k], k + 1
                k += 1
            raise ValueError("unbalanced")
        if j < len(s) and s[j] == "\\":
            m = re.match(r"\\[A-Za-z]+", s[j:])
            return m.group(0), j + len(m.group(0))
        return s[j:j + 1], j + 1

    def plain(t):
        if t.strip() in ("", r"\frown"):
            return ""
        out = latex_to_runs(t, like)
        if out is None:
            raise ValueError(t)
        return "".join(r["t"] for r in out)

    try:
        while i < len(s):
            c = s[i]
            if c in "_^":
                g, i = group(i + 1)
                t = plain(g)
                table = _SUB if c == "_" else _SUP
                if any(ch not in "0123456789+-=()n" for ch in t):
                    return None
                emit(t.translate(table))
                continue
            if c in "{}":
                i += 1
                continue
            if c != "\\":
                emit(c)
                i += 1
                continue
            sp_ = next((x for x in _SPACES if s.startswith(x, i)), None)
            if sp_:
                emit(" ")
                i += len(sp_)
                continue
            m = re.match(r"\\[A-Za-z]+", s[i:])
            if not m:
                return None
            cmd = m.group(0)
            i += len(cmd)
            if cmd in _SYMBOLS:
                emit(_SYMBOLS[cmd])
                # the space after a Greek letter's name only ends the name: `\delta P` is `δP`.
                # Arrows and floral symbols keep theirs (`A → B`, `⊕ ⚥ K₅`).
                if cmd in (r"\delta", r"\Delta", r"\alpha", r"\beta", r"\gamma", r"\mu") \
                        and s[i:i + 1] == " ":
                    i += 1
            elif cmd in (r"\text", r"\mathrm", r"\textbf", r"\mathbf"):
                g, i = group(i)
                emit(plain(g), b=cmd in (r"\textbf", r"\mathbf") or None)
            elif cmd in (r"\underline", r"\overline"):
                g, i = group(i)
                mark = "̲" if cmd == r"\underline" else "̅"
                emit("".join(ch + mark for ch in plain(g)))
            elif cmd == r"\overset":
                top, i = group(i)
                g, i = group(i)
                # A group drawn ON an atom is its side chain: the Lyases reaction (BIO11L ch09
                # p117) sets X and Y over C-C, read in line as `C(X)`. A bond stroke `|` or the
                # floral formula's adhesion arc carries no word and is dropped.
                t = plain(top).replace("|", "").strip()
                emit(plain(g) + ((t if t.startswith("(") and t.endswith(")") else f"({t})")
                                 if t else ""))
            elif cmd == r"\underset":
                below, i = group(i)
                g, i = group(i)
                # A name set under a formula: `CO₂` over `carbon dioxide` reads `CO₂ (carbon dioxide)`.
                t = plain(below).strip()
                emit(plain(g) + ((f" {t}" if t.startswith("(") and t.endswith(")") else f" ({t})")
                                 if t else ""))
            elif cmd in (r"\left", r"\right"):
                # Sized brackets print as their bracket: the logistic equation's
                # `rN\left(\frac{K - N}{K}\right)` reads `rN((K - N)/K)`. `\left.` prints nothing.
                while i < len(s) and s[i] == " ":
                    i += 1
                d = s[i:i + 1]
                if d == "\\":
                    m2 = re.match(r"\\[{}|]", s[i:])
                    if not m2:
                        return None
                    d = m2.group(0)[1:]
                    i += 1
                i += 1
                emit("" if d == "." else d)
            elif cmd == r"\frac":
                # A FRACTION IN LINE: `rate = δP/δt`. Flattened by the text layer it read `P rate =
                # δ t δ` (BIO11L ch09 p113) -- a slash keeps numerator and denominator whole.
                num, i = group(i)
                den, i = group(i)
                a, b = plain(num), plain(den)
                wrap = (lambda x: f"({x})" if re.search(r"[\s+\-]", x) else x)
                emit(f"{wrap(a)}/{wrap(b)}")
            elif cmd in (r"\xrightarrow", r"\xleftarrow", r"\xrightleftharpoons"):
                # An arrow with its condition set over (and under) it: the enzyme's name is
                # printed words and is kept, `⇌ (Carbonic anhydrase)`.
                labels = []
                while i < len(s) and s[i] == " ":
                    i += 1
                if i < len(s) and s[i] == "[":
                    k = s.index("]", i)
                    labels.append(plain(s[i + 1:k]))
                    i = k + 1
                g, i = group(i)
                labels.insert(0, plain(g))
                arrow = {r"\xrightarrow": "→", r"\xleftarrow": "←"}.get(cmd, "⇌")
                lab = ", ".join(x.strip() for x in labels if x.strip())
                emit(f" {arrow}" + (f" ({lab}) " if lab else " "))
            else:
                return None
    except ValueError:
        return None
    text = re.sub(r" {2,}", " ", "".join(r["t"] for r in runs)).strip()
    if not text:
        return None
    for r in runs:
        r["t"] = re.sub(r" {2,}", " ", r["t"])
    runs[0]["t"] = runs[0]["t"].lstrip()
    runs[-1]["t"] = runs[-1]["t"].rstrip()
    return [r for r in runs if r["t"]]


_CELL_SCRIPT = re.compile(r"([\^_])(?:\{([^{}]*)\}|([A-Za-z0-9+\-]))")


def cell_scripts(cell):
    """A2S cell text with `^`/`_` notation -> (plain text, sup/sub marks).

    A2S writes a superscript as `I^A` (BIO12L ch04 Table 4.2's blood-group alleles), and the
    cell went into the JSON, the Markdown and the page as the literal `I^A`. The cell keeps its
    printed letters, `IA`, and the script is a mark -- the same shape as a body's marks."""
    out, marks, pos = [], [], 0
    for m in _CELL_SCRIPT.finditer(cell or ""):
        out.append(cell[pos:m.start()])
        at = sum(len(x) for x in out)
        t = m.group(2) if m.group(2) is not None else m.group(3)
        if t:
            out.append(t)
            marks.append({"from": at, "to": at + len(t),
                          ("sup" if m.group(1) == "^" else "sub"): True})
        pos = m.end()
    out.append((cell or "")[pos:])
    return "".join(out), marks


def cell_marks(grid, r, c, italics):
    """Marks for cell (r, c): its scripts, plus italic over the whole cell when the page printed
    its letters in italic (`cell_italics` holds the layer's fragments, `I A I A`, spaced and
    cased by the PDF's runs, so letters are compared). None for a cell without scripts -- its
    italics are set by fragment, as before."""
    got = next((x["marks"] for x in grid.get("cell_marks") or []
                if x.get("row") == r and x.get("col") == c), None)
    if not got:
        return None
    text = grid["cells"][r][c] or ""
    key = re.sub(r"[^a-z0-9]", "", text.lower())
    ital = bool(key) and any(key in re.sub(r"[^a-z0-9]", "", f.lower()) for f in italics or [])
    return ([{"from": 0, "to": len(text), "i": True}] if ital else []) + list(got)


def _table_from_cells(page, sp):
    """The page's text blocks that ARE this table, merged into one element -- or None.

    A table A2 saw has no text of its own in A2's output (A2S transcribes it), so nothing on the
    page carries its block number and nothing is of role `table`. Measured on BIO11L ch03 p036:
    exercise 10's Column I / Column II match table reached the render as a heading line plus a
    run-on paragraph -- `(a) Chlamydomonas (i) Moss (b) Cycas (ii) ...` -- while A2S held all
    four rows correctly. A block belongs to the table when every one of its words is a word of
    the transcribed cells; they are merged into the first, whose box grows to cover them all.
    """
    def words(s):
        return [w for w in re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).split() if w]
    cells = (sp.get("header") or []) + [c for r in (sp.get("rows") or []) for c in r]
    soup = set(words(" ".join(c for c in cells if c)))
    if not soup:
        return None
    els = page["elements_in_reading_order"]
    hits = [e for e in els
            if e["role"] in ("paragraph", "list", "side_note", "box")
            and len(words(e.get("text"))) >= 2 and set(words(e.get("text"))) <= soup]
    if not hits:
        return None
    first = hits[0]
    for k in ("bbox", "bbox_sheet", "bbox_pt"):
        if all(h.get(k) for h in hits):
            bs = [h[k] for h in hits]
            first[k] = [min(b[0] for b in bs), min(b[1] for b in bs),
                        max(b[2] for b in bs), max(b[3] for b in bs)]
    # The merged blocks are TABLE CELLS, not a caption: the table's text is its grid. Leaving the
    # joined text on the element made it the table's caption, and the whole table printed a
    # second time above itself in bold -- pushing the grid down onto exercise 11.
    first["cell_italics"] = _italic_words(hits)
    first["text"] = ""
    first["runs"] = []
    first.pop("line_boxes_pt", None)
    page["elements_in_reading_order"] = [e for e in els if not any(e is h for h in hits[1:])]
    return first


def _a2_block_box(chapter, page_no, block_n, steps_dir):
    """A2's measured box for block `block_n` on page `page_no`, in PDF points -- or None.
    A2 measures on its 200 dpi page image."""
    import glob as _glob
    paths = sorted(_glob.glob(os.path.join(steps_dir, "A2", "out",
                                           f"{chapter}-p{page_no:03d}.*.json")))
    for p in paths:
        try:
            with open(p, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        for b in data.get("blocks") or []:
            if b.get("n") == block_n and len(b.get("bbox") or []) == 4:
                return [v * 72.0 / 200.0 for v in b["bbox"]]
    return None


def _cover(a, b):
    """The share of element box `a` that lies inside A2's box `b`."""
    ix = max(0.0, min(a[2], b[2]) - max(a[0], b[0]))
    iy = max(0.0, min(a[3], b[3]) - max(a[1], b[1]))
    area = max(1e-6, (a[2] - a[0]) * (a[3] - a[1]))
    return ix * iy / area


def _flatten_latex(tex):
    """`= (\\pm 0.01/9.89) \\times 100 \\% \\\\ = \\pm 0.1 \\%` -> `= (± 0.01/9.89) × 100 % = ± 0.1 %`."""
    t = tex or ""
    for a, b in (("\\pm", "±"), ("\\times", "×"), ("\\%", "%"), ("\\\\", " "), ("\\,", " "),
                 ("\\ ", " "), ("\\cdot", "·"), ("\\pi", "π"), ("&", "")):
        t = t.replace(a, b)
    t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", t)
    t = re.sub(r"\\(?:text|mathrm|mathbf|left|right)\b", "", t)
    t = re.sub(r"\\begin\{[a-z*]+\}|\\end\{[a-z*]+\}", "", t)
    t = re.sub(r"[{}]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def apply_agent_special(layout, chapter, steps_dir="steps"):
    """Merge A2S transcriptions into `layout`, in place. Returns counts."""
    stats = {"files": 0, "tables": 0, "equations": 0, "figures": 0, "unmatched": 0}
    files = a2s_files(chapter, steps_dir)
    stats["files"] = len(files)
    if not files:
        layout["special_join"] = stats
        return stats

    claimed = set()                       # elements an A2S read has already filled, this pass
    for (page_no, block_n), path in sorted(files.items()):
        if page_no < 1 or page_no > len(layout["pages"]):
            stats["unmatched"] += 1
            continue
        page = layout["pages"][page_no - 1]
        try:
            with open(path, encoding="utf-8") as fh:
                sp = json.load(fh)
        except (OSError, json.JSONDecodeError):
            stats["unmatched"] += 1
            continue

        kind = (sp.get("kind") or "").lower()
        target = next((e for e in page["elements_in_reading_order"]
                       if e.get("a2_block_n") == block_n), None)
        if target is None:
            # The block may not have survived as its own element -- a table's caption is merged
            # with its rows, a figure's label is absorbed into the artwork. Fall back to the
            # element of the right KIND on that page, which is unambiguous when there is one.
            want = {"table": "table", "equation": "paragraph", "figure": "figure"}.get(kind)
            cands = [e for e in page["elements_in_reading_order"] if e["role"] == want]
            # ...and with TWO tables on the page, the one under A2's own box. BIO11L ch09 p109
            # prints Tables 9.4 and 9.5; the second is cut as a picture, so one `table` element
            # stood on the page and BOTH reads fell back to it -- 9.5's `Protein | Functions`
            # rows overwrote 9.4's `Component | % of the total cellular mass`. A read takes the
            # element its measured box covers (a table typed as a picture included), never one
            # another read has filled; the single-candidate rule stands when A2 gave no box.
            box = _a2_block_box(chapter, page_no, block_n, steps_dir)
            if box:
                pool = [e for e in page["elements_in_reading_order"]
                        if id(e) not in claimed and e.get("bbox_pt")
                        and (e["role"] == want or (kind == "table" and e["role"] == "figure"))]
                # AN EQUATION NEVER TAKES A2's PROSE. PHY11L ch01 p006's 9.89 g equation covered
                # the sentence `Similarly, the relative error in 9.89 g is` best and replaced it;
                # its own line was the layer's `= (± 0.01/9.89) ...`. (Unmeasured books only.)
                import book_design
                if kind == "equation" and not book_design.is_measured(chapter.split("-ch")[0]):
                    pool = [e for e in pool if e.get("text_source") != "a2-agent"]
                    # ...nor a gathered copy that still holds prose (`the relative error in
                    # 9.89 g = ...`): the equation's own line has no words of four letters
                    bare = [e for e in pool
                            if len(re.findall(r"[A-Za-z]{4,}", e.get("text") or "")) < 2]
                    if any(_cover(e["bbox_pt"], box) >= 0.3 for e in bare):
                        pool = bare
                scored = sorted(((_cover(e["bbox_pt"], box), k) for k, e in enumerate(pool)),
                                reverse=True)
                target = pool[scored[0][1]] if scored and scored[0][0] >= 0.3 else None
            else:
                cands = [e for e in cands if id(e) not in claimed]
                target = cands[0] if len(cands) == 1 else None
        if target is None and kind == "table":
            target = _table_from_cells(page, sp)
        if target is None:
            stats["unmatched"] += 1
            continue
        claimed.add(id(target))
        # AN EQUATION SITS IN ITS OWN BOX. A gathered copy carrying prose (`the relative error in
        # 9.89 g = ...`, PHY11L ch01 p006) spans the sentence above it, and the typeset equation
        # was drawn over that sentence. It takes A2's measured equation box. (Unmeasured books.)
        import book_design
        if (kind == "equation" and not book_design.is_measured(chapter.split("-ch")[0])
                and len(re.findall(r"[A-Za-z]{4,}", target.get("text") or "")) >= 2):
            eb = _a2_block_box(chapter, page_no, block_n, steps_dir)
            # A2's box is an estimate: it started 5pt inside the sentence above it. The equation
            # begins under any A2 prose line it overlaps from above.
            for o in page["elements_in_reading_order"] if eb else []:
                ob = o.get("bbox_pt")
                if (o is not target and ob and o.get("text_source") == "a2-agent"
                        and min(ob[2], eb[2]) - max(ob[0], eb[0]) > 0
                        and ob[1] < eb[1] < ob[3] < eb[3]):
                    h = eb[3] - eb[1]
                    eb = [eb[0], ob[3] + 1.0, eb[2], ob[3] + 1.0 + h]
            if eb and page.get("page_width_pt"):
                pw, ph = page["page_width_pt"], page["page_height_pt"]
                sw, sh = page.get("sheet_pt") or (pw, ph)
                dx, dy = page.get("sheet_offset_pt") or (0.0, 0.0)
                target["bbox_pt"] = list(eb)
                target["bbox"] = [round(eb[0] / pw, 4), round(eb[1] / ph, 4),
                                  round(eb[2] / pw, 4), round(eb[3] / ph, 4)]
                target["bbox_sheet"] = [round((eb[0] + dx) / sw, 4), round((eb[1] + dy) / sh, 4),
                                        round((eb[2] + dx) / sw, 4), round((eb[3] + dy) / sh, 4)]
                target.pop("line_boxes_pt", None)

        if kind == "table":
            header = sp.get("header") or []
            rows = sp.get("rows") or []
            if header or rows:
                target["role"] = "table"
                # The AGENT's grid replaces the geometry one. The geometry grid is kept beside
                # it so a reviewer can see both, and so a later check can flag a disagreement
                # instead of silently preferring one.
                if target.get("table_grid"):
                    target["table_grid_measured"] = target["table_grid"]
                    # THE CAPTION'S SECOND LINE IS NOT A ROW. The measured region starts at the
                    # caption, so `in Non-living and Living Matter*` (Table 9.1) and `Constituents
                    # of Living Tissues` (9.2, BIO11L ch09 p105) were the measured grid's first row
                    # -- and went with it when A2S's grid replaced it. A leading measured row none
                    # of whose words A2S has in any cell continues the caption.
                    soup = set(re.findall(r"[a-z0-9]+", " ".join(
                        c for r in ([sp.get("header") or []] + (sp.get("rows") or []))
                        for c in r if c).lower()))
                    tail = []
                    for row in (target["table_grid"].get("cells") or [])[:2]:
                        t = re.sub(r"\s+", " ", " ".join(c for c in row if c)).strip()
                        ws = re.findall(r"[a-z0-9]+", t.lower())
                        if not ws or any(w in soup for w in ws):
                            break
                        tail.append(t)
                    if tail and (target.get("text") or "").strip():
                        extra = " " + " ".join(tail)
                        target["text"] = target["text"].rstrip() + extra
                        if target.get("runs"):
                            target["runs"] = list(target["runs"]) + [
                                dict(target["runs"][-1], t=extra)]
                cells, scripts = [], []
                for ri, row in enumerate(([header] if header else []) + rows):
                    plain_row = []
                    for ci, cell in enumerate(row):
                        text, mk = cell_scripts(cell)
                        plain_row.append(text)
                        if mk:
                            scripts.append({"row": ri, "col": ci, "marks": mk})
                    cells.append(plain_row)
                target["table_grid"] = {
                    "rows": len(rows) + (1 if header else 0),
                    "cols": max([len(header)] + [len(r) for r in rows] or [0]),
                    "cells": cells,
                    "repeated_header": sp.get("repeated_header", False),
                    "source": "a2s-agent",
                }
                if scripts:
                    target["table_grid"]["cell_marks"] = scripts
                if sp.get("caption"):
                    target["table_caption"] = sp["caption"]
                if "cell_italics" not in target:
                    target["cell_italics"] = _italic_words([target])
                target["special_source"] = "a2s-agent"
                stats["tables"] += 1
        elif kind == "equation" and sp.get("latex"):
            target["latex"] = sp["latex"]
            target["special_source"] = "a2s-agent"
            shown = latex_to_runs(sp["latex"], target)
            if shown:
                # Nothing downstream typesets LaTeX, so the element prints its TEXT -- which for
                # an equation is the text layer's flattening of it. Measured on BIO11L ch05: the
                # floral formula of Figure 5.16 printed as `⊕  K2+2 C4 A2+4 G(2)`, the bisexual
                # sign gone, every subscript on the line and the superior-ovary underline lost.
                target["text"] = "".join(r["t"] for r in shown)
                target["runs"] = shown
                target["text_source"] = "a2s-agent"
            elif not book_design.is_measured(chapter.split("-ch")[0]):
                # Multi-line LaTeX (`\\`) gives no runs, and the node kept whatever text it had
                # -- `the relative error in 9.89 g` for the 9.89 g equation (PHY11L ch01 p006).
                # Its text is the equation, flattened.
                flat = _flatten_latex(sp["latex"])
                target["text"] = flat
                target["runs"] = [dict((target.get("runs") or [{}])[0], t=flat)]
                target["text_source"] = "a2s-agent"
            stats["equations"] += 1
        elif kind == "figure":
            for k in ("caption", "labels", "description"):
                if sp.get(k):
                    target[f"figure_{k}"] = sp[k]
            target["special_source"] = "a2s-agent"
            stats["figures"] += 1

    layout["special_join"] = stats
    return stats
