"""Render an organic reaction from a card of SMILES, names and arrow labels.

THIS IS A PILOT, AND IT IS SUPERSEDED
-------------------------------------
Arivihan already has a Chemistry Renderer (package v4.1, 21 Oct 2026) that does this properly: 127
Haloalkanes cards, 118 drawn identically to NCERT, 9 nearly, 0 different, with OPSIN rebuilding every
structure from its printed name as an independent check. That package is the thing to integrate --
see `docs/FIGURE_RENDERING_PLAN.md`. It was shared as a zip and is not on this machine, so this file
exists to show the shape working end to end on this corpus's own figures, and should be deleted the
day the package lands.

What it keeps from that design, because these are the parts that make a generated figure
trustworthy rather than merely plausible:

  * THE CARD IS THE RECORD. Molecules are SMILES, conditions are arrow labels, and the drawing is
    derived. A typo is fixed by editing the card, never by redrawing.
  * THE AI NEVER DRAWS. A wrong atom in a SMILES still draws a valid-looking picture, which is
    exactly why the structure has to be checked by something that is not the thing that wrote it.
  * EVERY STRUCTURE IS PARSED BEFORE IT IS DRAWN, and its molecular formula is reported, so a card
    that claims a product can be checked against what was actually drawn.

What it does NOT have, and the package does: OPSIN. Without a name-to-structure check, a SMILES that
parses but is the wrong molecule passes silently. That is the single reason this is a pilot.
"""

import argparse
import json
import os
import re

from rdkit import Chem
from rdkit.Chem import Draw, rdCoordGen
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem import rdMolDescriptors
from rdkit import Geometry

#: NCERT's own ink: halogens green, heteroatoms magenta, every bond black.
#: #009848 and #E80088, sampled from the PDF.
GREEN, MAGENTA, BLACK = (0.0, 0.596, 0.282), (0.910, 0.0, 0.533), (0.0, 0.0, 0.0)


#: EVERY NUMBER HERE IS MEASURED FROM THE NCERT PDF, not chosen. The values come from the Arivihan
#: Chemistry Renderer guide's measurement table, which took them from the text layer and from 400
#: dpi renders -- so they are the same numbers that produced 118 of 127 drawings identical to the
#: book. Three of them this file already had right by independent sampling (the bond length, the
#: bond line, and the two colours); the rest were guesses and are now replaced.
TYPE_PX = 19            # NCERT sets at about 11 pt; every length below is tied to this
BOND_PX = 28            # measured on NCERT rings
BOND_LINE = 1.6         # NCERT strokes about 0.085 em
SUB_SIZE = 0.58         # em, from 344 subscripts in the PDF text layer
SUB_DROP = 0.33         # em
ARROW_LINE = 0.08       # em, measured at 400 dpi
ARROW_LABEL = 0.82      # em
CHARGE_R = 0.31         # of the type size


def _overlay(drawer, mol, items):
    """Lone pairs and circled charges, placed from RDKit's OWN atom positions.

    The method is the one the Arivihan Chemistry Renderer guide records, and it is the only one that
    works: ask the drawer where it actually put the atom (`GetDrawCoords`), then push the mark
    OUTWARD along the vector from the molecule's centre to that atom, so it lands outside the ring
    rather than on top of a bond. Guessing a pixel offset cannot work, because RDKit chooses the
    layout and the scale.

    NCERT prints `:NH2` on aniline's nitrogen and circles the charge on an ammonium ion, and those
    marks are not decoration -- the lone pair is the reason aniline is a base and the whole of what
    several figures are about.
    """
    import math
    conf = mol.GetConformer()
    n = mol.GetNumAtoms()
    cx = sum(conf.GetAtomPosition(i).x for i in range(n)) / n
    cy = sum(conf.GetAtomPosition(i).y for i in range(n)) / n
    centre = drawer.GetDrawCoords(Geometry.Point2D(cx, cy))
    out = []
    for item in items:
        idx = item.get("atom")
        if idx is None or idx >= n:
            continue
        here = drawer.GetDrawCoords(Geometry.Point2D(conf.GetAtomPosition(idx).x,
                                                     conf.GetAtomPosition(idx).y))
        dx, dy = here.x - centre.x, here.y - centre.y
        length = math.hypot(dx, dy) or 1.0
        ux, uy = dx / length, dy / length
        push = item.get("push", 15)
        x, y = here.x + ux * push, here.y + uy * push
        kind = item.get("kind", "lone_pair")
        if kind == "lone_pair":
            # Two dots, set across the outward direction so they read as a pair on that atom.
            px, py = -uy, ux
            for sign in (-1, 1):
                out.append('<circle cx="%.1f" cy="%.1f" r="1.7" fill="#11151d"/>'
                           % (x + px * 3.2 * sign, y + py * 3.2 * sign))
        elif kind in ("plus", "minus"):
            sign = "+" if kind == "plus" else "\u2212"
            out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#11151d" '
                       'stroke-width="1.1"/>'
                       '<text x="%.1f" y="%.1f" font-size="9" text-anchor="middle" '
                       'dominant-baseline="central" fill="#11151d" '
                       'font-family="ui-serif,Georgia,serif">%s</text>'
                       % (x, y, CHARGE_R * TYPE_PX, x, y, sign))
    return "".join(out)


def _orient(mol, atom_map, deg):
    """Rotate the drawing so the atom carrying map number `atom_map` points at `deg` from the ring
    centre -- NCERT hangs a substituent ABOVE its ring, not off to the side.

    Placement is not cosmetic here. A reader matches a redraw to the book by where things sit, and
    a diazonium group drawn to the right of its ring reads as a different arrangement from the same
    group drawn above it.
    """
    import math
    from rdkit.Chem import rdMolTransforms
    conf = mol.GetConformer()
    target = None
    for atom in mol.GetAtoms():
        if atom.GetAtomMapNum() == atom_map:
            target = atom.GetIdx()
    if target is None:
        return
    ring_atoms = [i for ring in mol.GetRingInfo().AtomRings() for i in ring]
    if not ring_atoms:
        return
    cx = sum(conf.GetAtomPosition(i).x for i in ring_atoms) / len(ring_atoms)
    cy = sum(conf.GetAtomPosition(i).y for i in ring_atoms) / len(ring_atoms)
    pos = conf.GetAtomPosition(target)
    current = math.degrees(math.atan2(pos.y - cy, pos.x - cx))
    turn = math.radians(deg - current)
    cos_t, sin_t = math.cos(turn), math.sin(turn)
    for i in range(mol.GetNumAtoms()):
        p = conf.GetAtomPosition(i)
        x, y = p.x - cx, p.y - cy
        conf.SetAtomPosition(i, (x * cos_t - y * sin_t + cx, x * sin_t + y * cos_t + cy, 0.0))


def draw_molecule(smiles, width, height, size, bond_px=BOND_PX, orient=None,
                  abbreviate=False, overlay=None):
    """One structure as an SVG fragment, drawn the way the book draws it.

    TWO SETTINGS THAT LOOK LIKE SIZES AND ARE NOT
    ---------------------------------------------
    `baseFontSize` is a FRACTION of the bond length, not a pixel size. Setting it to the page's type
    size (17) drew atom labels four times the width of the rings they sat on -- `H2N` taller than the
    benzene ring it was attached to -- and the structures were unreadable. RDKit's own default is
    about 0.6 and the right adjustment is a nudge from there, never a point size.

    `fixedBondLength` alone does nothing on a flexible canvas: RDKit rescales to fit and the bond
    length goes with it. The scaling factor has to be set as well, from the molecule's own median
    bond length -- which is the trick the Chemistry Renderer guide records, and the reason its rings
    match NCERT's while a naive call does not.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError("RDKit cannot parse %r" % smiles)
    # A MOLECULE WITH NO BONDS CANNOT BE SCALED, AND RDKIT FILLS THE CANVAS INSTEAD.
    # `NH3`, `R-NH2` written as a bare dummy atom, a lone ion -- these have nothing to measure a
    # bond length against, so the depictor scales the single glyph until it fits the box. One card
    # rendered as a black chevron the height of the page. Such a species is a FORMULA, not a
    # structure, and the card should carry it as text; raising here says so instead of drawing it.
    if mol.GetNumBonds() == 0:
        raise ValueError(
            "%r has no bonds, so there is no bond length to scale by and RDKit will fill the "
            "canvas with one glyph. Carry it as a `text` part instead of a `mol`." % smiles)
    rdCoordGen.AddCoords(mol)
    # THE FORMULA IS TAKEN BEFORE ANY ABBREVIATION. Condensing a group replaces its atoms with a
    # dummy, so the formula of an abbreviated molecule is not its formula: sulphanilic acid came
    # back as `C6H6*N` instead of `C6H7NO3S` the moment condensing was switched on, which silently
    # destroyed the only automated check this renderer has.
    true_formula = rdMolDescriptors.CalcMolFormula(mol)
    if abbreviate:
        # NCERT CONDENSES its groups: it writes NO2 and SO3H as text on the ring rather than drawing
        # the atoms. An expanded nitro group is a different notation from the one in the book.
        from rdkit.Chem import rdAbbreviations
        mol = rdAbbreviations.CondenseMolAbbreviations(
            mol, rdAbbreviations.GetDefaultAbbreviations(), maxCoverage=0.8)
        rdCoordGen.AddCoords(mol)
    if orient:
        _orient(mol, orient.get("atom", 1), orient.get("deg", 90))
    # The map numbers are HANDLES for `orient`, never drawn.
    for atom in mol.GetAtoms():
        atom.SetAtomMapNum(0)
    drawer = rdMolDraw2D.MolDraw2DSVG(width, height)
    opts = drawer.drawOptions()
    opts.clearBackground = False
    opts.bondLineWidth = 1.6
    opts.baseFontSize = 0.62
    opts.additionalAtomLabelPadding = 0.08
    opts.fixedBondLength = bond_px
    # `fixedBondLength` ALONE DOES NOTHING on a flexible canvas: RDKit rescales to fit and the bond
    # length rescales with it. The scaling factor has to be set from the molecule's own median bond
    # length as well -- the trick recorded in the Chemistry Renderer guide, and the reason its rings
    # match NCERT's while a naive call does not.
    conformer = mol.GetConformer()
    lengths = sorted(
        (conformer.GetAtomPosition(b.GetBeginAtomIdx())
         - conformer.GetAtomPosition(b.GetEndAtomIdx())).Length()
        for b in mol.GetBonds())
    median = lengths[len(lengths) // 2] or 1.0
    opts.scalingFactor = bond_px / median
    opts.singleColourWedgeBonds = True
    opts.flagCloseContactsDist = -1          # NCERT draws atoms close together on purpose
    opts.useBWAtomPalette()
    opts.updateAtomPalette({7: MAGENTA, 8: MAGENTA, 16: MAGENTA,
                            9: GREEN, 17: GREEN, 35: GREEN, 53: GREEN})
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    extra = _overlay(drawer, mol, overlay) if overlay else ""
    drawer.FinishDrawing()
    svg = drawer.GetDrawingText()
    if extra:
        svg = svg.replace("</svg>", extra + "</svg>")
    # RDKit colours its bonds to match the atoms at each end; NCERT prints every bond black.
    svg = re.sub(r"<path class='bond-[^>]*>",
                 lambda m: re.sub(r"(stroke|fill):#[0-9A-Fa-f]{6}", r"\1:#000000", m.group(0)),
                 svg)
    svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
    svg = _tight(svg)
    svg = re.sub(r"<svg", "<svg style='overflow:visible'", svg, count=1)
    return svg, true_formula


def _tight(svg, pad=3.0):
    """Crop the viewBox to the ink. RDKit pads its canvas generously and the padding is not uniform.

    The guide does this by rasterising with cairosvg and finding the drawn pixels. Cairo is not
    installed here, so the extent is taken from the DRAWING COORDINATES instead -- every path, line,
    circle and text position in RDKit's own output -- which needs no C library and gives the same
    answer for vector output. Without it every structure sits in a box much larger than itself, so
    the gaps between reactant, plus sign and arrow are set by RDKit's padding rather than by the
    layout, and the row reads as scattered pieces.
    """
    numbers = [float(n) for n in re.findall(r"[-+]?\d*\.?\d+", " ".join(
        re.findall(r"d='([^']+)'", svg)))]
    xs, ys = numbers[0::2], numbers[1::2]
    for tag, ax, ay in (("circle", "cx", "cy"), ("ellipse", "cx", "cy"), ("text", "x", "y")):
        for m in re.finditer(r"<%s[^>]*>" % tag, svg):
            fx = re.search(r"%s='([-\d.]+)'" % ax, m.group(0))
            fy = re.search(r"%s='([-\d.]+)'" % ay, m.group(0))
            if fx and fy:
                xs.append(float(fx.group(1)))
                ys.append(float(fy.group(1)))
    if not xs or not ys:
        return svg
    x0, x1, y0, y1 = min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad
    w, h = max(x1 - x0, 1), max(y1 - y0, 1)
    svg = re.sub(r"viewBox='[^']*'", "viewBox='%.1f %.1f %.1f %.1f'" % (x0, y0, w, h), svg, count=1)
    svg = re.sub(r"width='[^']*'", "width='%.0f'" % w, svg, count=1)
    svg = re.sub(r"height='[^']*'", "height='%.0f'" % h, svg, count=1)
    return svg


def arrow(label_above, label_below, length=104):
    above = ('<span class="above">%s</span>' % label_above) if label_above else ""
    below = ('<span class="below">%s</span>' % label_below) if label_below else ""
    return ('<span class="arrow" style="--len:%dpx">%s'
            '<span class="shaft"></span><svg viewBox="0 0 10 10" class="head">'
            '<path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="#11151d" stroke-width="1.6"/>'
            '</svg>%s</span>' % (length, above, below))


CSS = """
/* EVERY LENGTH IS TIED TO THE TYPE SIZE, which is measured: NCERT sets at about 11 pt, 19 px here.
   The ratios below come from the Chemistry Renderer guide's measurement table -- 344 subscripts
   from the PDF text layer, arrows measured at 400 dpi -- rather than from taste. */
.rxn{display:flex;align-items:center;gap:0.3em;flex-wrap:nowrap;overflow-x:auto;
 padding-bottom:4px;font:400 19px/1.3 ui-serif,Georgia,'Bookman Old Style','Times New Roman',serif;
 color:#11151d}
.unit{display:flex;flex-direction:column;align-items:center;gap:0.3em}
.unit .name{display:block;font:400 0.63em/1.4 ui-sans-serif,system-ui;color:#4c5460;
 max-width:15em;text-align:center}
.unit .tag{display:block;font:700 0.5em/1.6 ui-sans-serif,system-ui;letter-spacing:.14em;
 text-transform:uppercase;color:#78808d;text-align:center}
.plus{font-size:1.05em;padding:0 0.1em}
/* An arrow is label / line / label. The line is 0.08 em and the labels 0.82 em, as measured. */
.arrow{position:relative;display:inline-flex;flex-direction:column;align-items:center;
 min-width:var(--len);margin:0 0.45em;flex:none}
.arrow .shaft{width:100%;height:0.08em;background:#11151d;margin:0.12em 0}
.arrow .head{position:absolute;right:-1px;top:50%;width:0.55em;height:0.55em;
 transform:translateY(-50%)}
.arrow .above,.arrow .below{display:block;white-space:nowrap;text-align:center;
 padding:0 0.55em 0 0;font:400 0.82em/1.45 ui-sans-serif,system-ui}
.arrow .below{color:#4c5460}
.formula{display:block;font:400 0.58em/1.5 ui-monospace,monospace;color:#9aa1ab;text-align:center}
/* A branching scheme: the rows stack and the brace spans them, as NCERT prints it. */
.scheme{display:flex;flex-direction:column;gap:0.1em}
.scheme .rxn{align-items:center}
.brace{display:inline-block;width:0.5em;align-self:stretch;min-height:2.2em;margin:0 0.2em;
 border-left:0.085em solid #11151d;border-top:0.085em solid #11151d;
 border-bottom:0.085em solid #11151d}
"""



def render(card, size=TYPE_PX, show_formula=False):
    """One card as HTML. A card is one or more ROWS.

    WHY ROWS AND NOT A ROW
    ----------------------
    A single row cannot express a branching scheme, and NCERT prints them constantly: the Sandmeyer
    reaction is one reactant, `ArN2+X-`, splitting into three parallel arrows with different copper
    reagents. Flattened into one line it became a run-on sentence -- "ArN2+X- - Cu2Cl2/HCl -> ArCl +
    N2ArN2+X- - Cu2Br2/HBr -> ..." -- which is not the figure at all. A `bracket` part draws the
    vertical brace that holds the branches together.
    """
    rows = card.get("rows")
    if rows is None:
        rows = [card["row"]]
    bodies, formulas = [], []
    for row in rows:
        body, row_formulas = _render_row(row, size, show_formula)
        bodies.append(body)
        formulas.extend(row_formulas)
    if len(bodies) == 1:
        return bodies[0], formulas
    # A branching scheme: the shared reactant sits to the left of a brace, and the branches stack.
    return ('<div class="scheme">%s</div>' % "".join(bodies)), formulas


def _render_row(row, size=TYPE_PX, show_formula=False):
    parts, formulas = [], []
    for item in row:
        if "mol" in item:
            svg, formula = draw_molecule(item["mol"], item.get("w", 150), item.get("h", 120), size,
                                         orient=item.get("orient"),
                                         abbreviate=item.get("abbreviate", False),
                                         overlay=item.get("overlay"))
            formulas.append((item.get("name") or item["mol"], formula))
            caption = ""
            if item.get("name"):
                caption += '<span class="name">%s</span>' % item["name"]
            if item.get("tag"):
                caption += '<span class="tag">%s</span>' % item["tag"]
            # The formula is a CHECK, not a caption. Printing it under a structure NCERT leaves
            # unnamed puts `C6H7N` on the page where the book prints nothing, which is noise to a
            # reader and was never the point -- the point is that the author verified it. It now
            # appears only beside a name, and the full list rides in the facts row beneath.
            if show_formula and item.get("name"):
                caption += '<span class="formula">%s</span>' % formula
            parts.append('<span class="unit">%s%s</span>' % (svg, caption))
        elif "plus" in item:
            parts.append('<span class="plus">+</span>')
        elif "arrow" in item:
            spec = item["arrow"]
            parts.append(arrow(spec.get("above", ""), spec.get("below", ""),
                               spec.get("len", 104)))
        elif "bracket" in item:
            # The tall brace NCERT draws where one reactant feeds several arrows.
            parts.append('<span class="brace"></span>')
        elif "text" in item:
            parts.append('<span class="unit">%s</span>' % item["text"])
    return '<div class="rxn">%s</div>' % "".join(parts), formulas


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cards", nargs="+")
    ap.add_argument("--out", default="figures/reactions.html")
    args = ap.parse_args()

    blocks = []
    for path in args.cards:
        with open(path, encoding="utf-8") as fh:
            card = json.load(fh)
        html, formulas = render(card, show_formula=True)
        print("  %-34s %s" % (os.path.basename(path), card.get("title", "")))
        for name, formula in formulas:
            print("      %-42s %s" % (name[:42], formula))
        blocks.append('<section><h2>%s</h2>%s</section>' % (card.get("title", ""), html))

    page = ('<!doctype html><meta charset="utf-8"><title>Reactions</title>'
            '<style>%s body{margin:0;background:#dfe5f0;font-family:ui-sans-serif,system-ui}'
            '.wrap{max-width:1100px;margin:0 auto;padding:30px 26px 80px}'
            'section{background:#fff;border:1px solid #d2d9e5;border-left:4px solid #653f08;'
            'border-radius:12px;padding:20px 24px 26px;margin:0 0 26px;'
            'box-shadow:0 1px 2px rgba(20,30,54,.05),0 12px 30px -18px rgba(20,30,54,.3)}'
            'h2{margin:0 0 18px;font-size:15px;letter-spacing:-.01em}</style>'
            '<div class="wrap">%s</div>' % (CSS, "".join(blocks)))
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(page)
    print("html  %s" % args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
