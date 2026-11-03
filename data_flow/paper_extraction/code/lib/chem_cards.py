"""Chemistry structure cards: check a card's SMILES with code, and draw them with RDKit.

THE AI NEVER DRAWS. An agent (figc-structure-reader) reads a printed structure and writes its
SMILES and name; this module checks the SMILES and draws it. That split is the whole reason a
generated structure can be trusted: a wrong atom in a SMILES still draws a valid-looking picture, so
nobody would notice it -- only a check that is not the writer can.

WHAT IS CHECKED
  parse      every SMILES and reaction SMILES must parse (RDKit)
  formula    each species' molecular formula is computed and stored, so a reviewer comparing it with
             the printed structure sees an atom count, not just a picture
  name       OPSIN rebuilds the structure from the printed name and it must match the SMILES
             (InChIKey). OPSIN needs Java; where Java is absent the check is RECORDED as not run,
             never silently passed -- see `name_check()`

WHAT IS NOT CHECKED (the team guide's own limits, unchanged): a well-formed but wrong molecule, a
swapped major/minor, wrong conditions on an arrow. A drawn structure is therefore never evidence --
the exact vector copy of the printed figure stays beside it on every page.

THE LOOK. These booklets print black-and-white structures, so the drawing is monochrome: black bonds
and labels, a fixed bond length, no RDKit close-contact boxes. The team guide's NCERT colours (green
halogens, magenta O/N) belong to NCERT's style, not to an Aakash or Vedantu booklet's.
"""

import glob
import re
import os
import shutil
import subprocess

#: Groups the NEET booklets print as text on a structure (see _abbreviate).
PRINTED_ABBREVIATIONS = {"NO2", "COOH", "CO2H", "CN", "SO3H", "CF3", "CCl3"}
#: Fixed bond length in px, and the canvas each species is drawn on before cropping to the drawing.
BOND_PX = 22
CANVAS = (360, 260)


def _rdkit():
    from rdkit import Chem, RDLogger
    from rdkit.Chem import rdChemReactions, rdMolDescriptors
    from rdkit.Chem.Draw import rdMolDraw2D
    RDLogger.DisableLog("rdApp.*")
    return Chem, rdChemReactions, rdMolDescriptors, rdMolDraw2D


#: The highest valence the booklets draw on an expanded-octet atom. RDKit refuses a halogen above
#: valence 1 unless its neighbours are all more electronegative, so Br3O8's chain
#: O=Br(=O)(=O)-Br(=O)(=O)-Br(=O)(=O)=O (2019_P1 q048) did not parse; the reader fell back to
#: charge-separated single bonds, and the print's double bonds rightly rejected those.
EXPANDED_OCTET = {"Cl": 7, "Br": 7, "I": 7, "S": 6, "Se": 6, "Te": 6, "P": 5, "As": 5, "Xe": 8}


def mol_from_smiles(smiles):
    """RDKit's molecule for a SMILES, or None. A valence RDKit refuses is accepted only on an
    EXPANDED_OCTET atom within its limit; every other chemistry problem still fails the SMILES."""
    Chem = _rdkit()[0]
    mol = Chem.MolFromSmiles(smiles or "")
    if mol is not None or not smiles:
        return mol
    raw = Chem.MolFromSmiles(smiles, sanitize=False)
    if raw is None:
        return None
    for problem in Chem.DetectChemistryProblems(raw):
        if problem.GetType() != "AtomValenceException":
            return None
        atom = raw.GetAtomWithIdx(problem.GetAtomIdx())
        valence = sum(b.GetBondTypeAsDouble() for b in atom.GetBonds()) + atom.GetNumExplicitHs()
        if valence > EXPANDED_OCTET.get(atom.GetSymbol(), 0):
            return None
    try:
        Chem.SanitizeMol(raw, Chem.SANITIZE_ALL ^ Chem.SANITIZE_PROPERTIES)
    except Exception:                                           # noqa: BLE001
        return None
    raw.UpdatePropertyCache(strict=False)
    return raw


def species_facts(smiles):
    """(ok, facts|message) for one SMILES: canonical form, formula, InChIKey where it can be made."""
    Chem, _rxn, desc, _draw = _rdkit()
    mol = mol_from_smiles(smiles)
    if mol is None:
        return False, "SMILES does not parse: %s" % smiles
    facts = {"canonical": Chem.MolToSmiles(mol), "formula": desc.CalcMolFormula(mol),
             "has_wildcard": any(a.GetAtomicNum() == 0 for a in mol.GetAtoms())}
    try:
        facts["inchikey"] = None if facts["has_wildcard"] else Chem.MolToInchiKey(mol)
    except Exception:                                           # noqa: BLE001
        facts["inchikey"] = None
    return True, facts


def reaction_ok(reaction_smiles, product_may_be_blank=False):
    """`product_may_be_blank`: the card draws the reaction from its `scheme`, so a product that is
    the question's blank ("phthalic acid + NH3 --strong heating--> ?", 2019_P1 q078) is left out of
    the SMILES rather than invented. Reactants are always required."""
    _chem, rxn, _desc, _draw = _rdkit()
    try:
        reaction = rxn.ReactionFromSmarts(reaction_smiles, useSmiles=True)
    except Exception as exc:                                    # noqa: BLE001
        return False, "reaction SMILES does not parse: %s" % exc
    if reaction.GetNumReactantTemplates() == 0:
        return False, "reaction SMILES has no reactants"
    if reaction.GetNumProductTemplates() == 0 and not product_may_be_blank:
        return False, "reaction SMILES has no products"
    return True, "ok"


def _opsin_command():
    """The OPSIN command line, or None when it cannot run here (no Java, or no jar)."""
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # The bundled runtime first (tools/jdk-*-jre, unpacked there so no admin install is needed),
    # then any Java on PATH.
    bundled = sorted(glob.glob(os.path.join(here, "tools", "jdk*", "bin", "java.exe"))
                     + glob.glob(os.path.join(here, "tools", "jdk*", "bin", "java")))
    java = bundled[-1] if bundled else shutil.which("java")
    if not java:
        return None
    jars = sorted(glob.glob(os.path.join(here, "tools", "opsin*.jar")))
    return [java, "-jar", jars[-1], "-osmi"] if jars else None


def name_check(name, smiles):
    """("match" | "mismatch" | "not_run" | "unparsed", detail) for a printed name against a SMILES.

    `not_run` is a real, recorded state: OPSIN needs Java and its jar in tools/. A check that
    could not run must look different from one that passed (SPEC Rule 19)."""
    command = _opsin_command()
    if not command:
        return "not_run", "OPSIN unavailable (needs Java 8+ and tools/opsin-cli-*.jar)"
    if not name:
        return "not_run", "no name given"
    try:
        result = subprocess.run(command, input=name, capture_output=True, text=True, timeout=60)
    except Exception as exc:                                    # noqa: BLE001
        return "not_run", "OPSIN failed to run: %s" % exc
    rebuilt = (result.stdout or "").strip()
    if not rebuilt:
        return "unparsed", "OPSIN could not read the name (ions, radicals and resonance forms are out of its reach)"
    ok_a, a = species_facts(rebuilt)
    ok_b, b = species_facts(smiles)
    if not (ok_a and ok_b) or not a.get("inchikey") or not b.get("inchikey"):
        return "unparsed", "could not compare"
    if a["inchikey"] == b["inchikey"]:
        return "match", "name gives %s, SMILES gives %s" % (a["canonical"], b["canonical"])
    # A METAL COMPLEX written two ways -- Ni(CO)4 as Ni=C=O or as Ni-C#O+ -- has one skeleton and
    # differs only in InChI's charge layer once the metal is disconnected. Same compound; only
    # for complexes, since phenol and phenoxide share a skeleton too and are not the same thing.
    if _has_metal(smiles) and _skeleton(rebuilt) and _skeleton(rebuilt) == _skeleton(smiles):
        return "match", "same skeleton as the name (metal complex, charges drawn differently)"
    return "mismatch", "name gives %s, SMILES gives %s" % (a["canonical"], b["canonical"])


#: Metals whose complexes a booklet draws with dative bonds (and SMILES with charges).
_METALS = {"Fe", "Co", "Ni", "Cr", "Mn", "Pt", "Pd", "Cu", "Zn", "Ag", "Au", "Ti", "V", "Mo", "W",
           "Ru", "Rh", "Os", "Ir", "Cd", "Hg"}


def _skeleton(smiles):
    """The standard InChI without its charge and protonation layers (the key hashes them in)."""
    from rdkit import Chem
    mol = mol_from_smiles(smiles)
    if mol is None:
        return None
    inchi = Chem.MolToInchi(mol) or ""
    return "/".join(part for part in inchi.split("/") if not part.startswith(("q", "p")))


def _has_metal(smiles):
    from rdkit import Chem
    mol = mol_from_smiles(smiles)
    return bool(mol) and any(a.GetSymbol() in _METALS for a in mol.GetAtoms())


def _options(draw_module, drawer):
    options = drawer.drawOptions()
    options.useBWAtomPalette()
    options.fixedBondLength = BOND_PX
    options.bondLineWidth = 1.4
    options.flagCloseContactsDist = -1
    options.clearBackground = False
    options.padding = 0.06
    options.minFontSize = 11
    options.maxFontSize = 15
    # The booklets write a terminal methyl as CH3; RDKit draws it as a bare line end, which reads
    # as a different (skeletal) notation from the printed page.
    options.explicitMethyl = True
    return options


def _prepare(smiles, orient=None, explicit_h=None):
    """The molecule with 2-D coordinates, atom-map handles cleared, rotated per `orient`.

    `orient` = {"atom": <map number>, "deg": 90} turns the drawing so that atom points at `deg` from
    the molecule's centre -- the team guide's key. These booklets hang a ring's OH, NO2 or CH3 ABOVE
    the ring; RDKit's default lays it sideways, and a structure drawn sideways reads as a different
    picture of the same molecule. Map numbers are handles only and are never drawn.
    """
    import math
    Chem, _rxn, _desc, _draw = _rdkit()
    from rdkit.Chem import rdDepictor
    from rdkit.Geometry import Point3D
    mol = mol_from_smiles(smiles)
    if mol is None:
        return None
    handles = {}
    for atom in mol.GetAtoms():
        if atom.GetAtomMapNum():
            handles[atom.GetAtomMapNum()] = atom.GetIdx()
            # kept as a property so an annotation can find this atom after abbreviation renumbers
            atom.SetIntProp("handle", atom.GetAtomMapNum())
            atom.SetAtomMapNum(0)
    # EXPLICIT H where the booklet draws it: 2017_A q052 draws the two alpha hydrogens the aldol
    # takes ("H-" on the ring carbon); an implicit-H drawing loses exactly what the scheme is about.
    wanted = [handles[n] for n in (explicit_h or []) if n in handles]
    if wanted:
        mol = Chem.AddHs(mol, onlyOnAtoms=tuple(wanted))
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)
    if orient and orient.get("atom") in handles and mol.GetNumAtoms() > 1:
        conf = mol.GetConformer()
        points = [conf.GetAtomPosition(i) for i in range(mol.GetNumAtoms())]
        cx = sum(p.x for p in points) / len(points)
        cy = sum(p.y for p in points) / len(points)
        target = conf.GetAtomPosition(handles[orient["atom"]])
        turn = math.radians(orient.get("deg", 90)) - math.atan2(target.y - cy, target.x - cx)
        cos_t, sin_t = math.cos(turn), math.sin(turn)
        for i, p in enumerate(points):
            dx, dy = p.x - cx, p.y - cy
            conf.SetAtomPosition(i, Point3D(cx + dx * cos_t - dy * sin_t,
                                            cy + dx * sin_t + dy * cos_t, 0.0))
    # ...and which SIDE a group sits on: `orient.right` / `orient.left` names an atom the booklet
    # prints right (left) of the centre. A layout and its mirror image are the same molecule, so
    # RDKit's choice is arbitrary -- q053's BCl3 put the angle's Cl on the left, the arc with it.
    if orient and mol.GetNumAtoms() > 1:
        conf = mol.GetConformer()
        cx = sum(conf.GetAtomPosition(i).x for i in range(mol.GetNumAtoms())) / mol.GetNumAtoms()
        for side, sign in (("right", 1), ("left", -1)):
            idx = handles.get(orient.get(side))
            if idx is not None and (conf.GetAtomPosition(idx).x - cx) * sign < 0:
                for i in range(mol.GetNumAtoms()):
                    p = conf.GetAtomPosition(i)
                    conf.SetAtomPosition(i, Point3D(2 * cx - p.x, p.y, 0.0))
                break
    return mol


def _abbreviate(mol):
    """NO2, COOH, CHO, CN, SO3H, OMe... condensed to TEXT on the ring, as the booklets print them.
    RDKit's own abbreviation table, applied to the drawing only -- the stored SMILES is untouched.
    An expanded nitro group with its formal charges is a different notation from the printed page."""
    from rdkit.Chem import rdAbbreviations
    # ONLY the groups the booklets print condensed. RDKit's table also turns OCH3 into "OMe" and
    # CHO into a label; 2017_A prints "OCH3" (q080) and draws its aldehyde H-C=O in full (q089), so
    # those would be a notation the page never uses.
    keep = [a for a in rdAbbreviations.GetDefaultAbbreviations() if a.label in PRINTED_ABBREVIATIONS]
    # ...and OCH3 as the booklets write it (RDKit's own table only has "OMe")
    keep += list(rdAbbreviations.ParseAbbreviations("OCH3 *OC OCH<sub>3</sub> H<sub>3</sub>CO"))
    try:
        return rdAbbreviations.CondenseMolAbbreviations(mol, keep, maxCoverage=0.6)
    except Exception:                                           # noqa: BLE001
        return mol


def species_svg(smiles, orient=None, abbreviate=True, explicit_h=None, annotations=None, name=None):
    """An SVG drawing of one SMILES: monochrome, fixed bond length, the canvas sized to the molecule.

    A FLEXIBLE canvas (-1, -1) with the scale set from the bond length, as the team guide's renderer
    does: RDKit ignores `fixedBondLength` on a flexible canvas unless `scalingFactor` is set, and a
    fixed canvas left q55's phenols floating in four times their own area of white space.

    `annotations` are what the booklet prints ON a structure besides its atoms, each anchored to
    atoms the card tags with map numbers: `{"kind": "angle", "atoms": [a, vertex, b], "text":
    "120°"}` draws a double-headed arc at the vertex with its label (2017_A q053's BCl3 printed the
    angle, and the drawing without it said less than the page), and `{"kind": "note", "atom": n,
    "text": "1"}` writes a locant beside an atom (q089's carbon numbering).
    """
    _chem, _rxn, _desc, draw = _rdkit()
    mol = _prepare(smiles, orient, explicit_h)
    if mol is None:
        return None
    # A WILDCARD IS THE BOOKLET'S "R": 2016_A q054's R-CH2-CO-CH2-R and q056's amino acids print R
    # where the card writes [*], and RDKit's "*" read as a different structure. A polymer's chain
    # ends (q057's cis-polyisoprene) keep "*", the usual mark for a repeat unit's open bonds.
    if "poly" not in (name or "").lower():
        for atom in mol.GetAtoms():
            if atom.GetAtomicNum() == 0 and not atom.HasProp("atomLabel"):
                atom.SetProp("atomLabel", "R")
    annotations = annotations or []
    for item in annotations:
        if item.get("kind") == "note":
            for atom in mol.GetAtoms():
                if atom.HasProp("handle") and atom.GetIntProp("handle") == item.get("atom"):
                    atom.SetProp("atomNote", str(item.get("text", "")))
    if abbreviate:
        mol = _abbreviate(mol)
    conf = mol.GetConformer()
    lengths = sorted((conf.GetAtomPosition(b.GetBeginAtomIdx())
                      - conf.GetAtomPosition(b.GetEndAtomIdx())).Length() for b in mol.GetBonds())
    median = lengths[len(lengths) // 2] if lengths else 1.0
    drawer = draw.MolDraw2DSVG(-1, -1)
    options = _options(draw, drawer)
    options.scalingFactor = BOND_PX / (median or 1.0)
    options.annotationFontScale = 0.7
    drawer.DrawMolecule(mol)
    extra = []
    by_handle = {a.GetIntProp("handle"): a.GetIdx() for a in mol.GetAtoms() if a.HasProp("handle")}
    for item in annotations:
        if item.get("kind") != "angle" or len(item.get("atoms") or []) != 3:
            continue
        idx = [by_handle.get(n) for n in item["atoms"]]
        if None in idx:
            continue
        points = [drawer.GetDrawCoords(i) for i in idx]
        extra.append(_angle_mark(points, str(item.get("text", ""))))
    drawer.FinishDrawing()
    svg = _tidy(drawer.GetDrawingText())
    if extra:
        # an angle label sits outside the molecule's own box: widen the canvas so it is not clipped
        w, h = _size(svg)
        margin = 26.0
        svg = ("<svg xmlns='http://www.w3.org/2000/svg' width='%.1f' height='%.1f' "
               "viewBox='0 0 %.1f %.1f'>%s%s</svg>"
               % (w + 2 * margin, h + 2 * margin, w + 2 * margin, h + 2 * margin,
                  place(svg, margin, margin),
                  "<g transform='translate(%.1f,%.1f)'>%s</g>" % (margin, margin, "".join(extra))))
    return svg


def place(svg, x, y):
    """An SVG drawing's content moved to (x, y) inside another drawing.

    A GROUP, not a nested <svg x= y=>: a nested root's x/y is ignored by some renderers (PyMuPDF
    stacked every structure of a scheme at the top-left corner), a transform never is."""
    body = svg.strip()
    if body.startswith("<svg"):
        body = body[body.index(">") + 1:]
        body = body[:body.rindex("</svg>")]
    return "<g transform='translate(%.1f,%.1f)'>%s</g>" % (x, y, body)


def _angle_mark(points, text, radius=None):
    """A double-headed arc between the two bonds at the vertex, and its label outside the arc."""
    import math
    (ax, ay), (vx, vy), (bx, by) = [(p.x, p.y) for p in points]
    radius = radius or BOND_PX * 0.75
    a1 = math.atan2(ay - vy, ax - vx)
    a2 = math.atan2(by - vy, bx - vx)
    sweep = (a2 - a1) % (2 * math.pi)
    if sweep > math.pi:                                        # the smaller angle, as printed
        a1, a2, sweep = a2, a1, 2 * math.pi - sweep
    p1 = (vx + radius * math.cos(a1), vy + radius * math.sin(a1))
    p2 = (vx + radius * math.cos(a2), vy + radius * math.sin(a2))
    mid = a1 + sweep / 2
    tx, ty = vx + (radius + 16) * math.cos(mid), vy + (radius + 16) * math.sin(mid)

    def head(px, py, angle):
        size = 5.0
        left = (px - size * math.cos(angle - 0.45), py - size * math.sin(angle - 0.45))
        right = (px - size * math.cos(angle + 0.45), py - size * math.sin(angle + 0.45))
        return ("<path d='M %.1f %.1f L %.1f %.1f L %.1f %.1f Z' fill='#000' stroke='none'/>"
                % (px, py, left[0], left[1], right[0], right[1]))
    return ("<path d='M %.1f %.1f A %.1f %.1f 0 0 1 %.1f %.1f' fill='none' stroke='#000' "
            "stroke-width='1.2'/>%s%s<text x='%.1f' y='%.1f' font-family='Arial,Helvetica,sans-serif' "
            "font-size='13' text-anchor='middle' dominant-baseline='middle'>%s</text>"
            % (p1[0], p1[1], radius, radius, p2[0], p2[1],
               head(p2[0], p2[1], a2 + math.pi / 2), head(p1[0], p1[1], a1 - math.pi / 2),
               tx, ty, _escape(text)))


def _escape(text):
    return (text or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
_SUP = str.maketrans("0123456789+-−()", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁽⁾")


def formula_label(text):
    """A species label as printed: `[S4O6]2(-)` -> [S₄O₆]²⁽⁻⁾, `NH2` -> NH₂. Digits after an element
    symbol or `)` are subscripts; what follows a closing `]` is the charge, a superscript."""
    if not text or not re.search(r"[A-Z]", text) or " " in text.strip():
        return text
    m = re.match(r"^(.*\])\s*(\d*\(?[+\-−]\)?)$", text)
    body, charge = (m.group(1), m.group(2)) if m else (text, "")
    body = re.sub(r"(?<=[A-Za-z\)])(\d+)", lambda d: d.group(1).translate(_SUB), body)
    return body + charge.translate(_SUP)


#: Text in a scheme: the booklets' sans face, at the size of an atom label.
SCHEME_FONT = 14
SVG_SIZE = re.compile(r"<svg[^>]*?width=['\"]([\d.]+)(?:px)?['\"][^>]*?height=['\"]([\d.]+)(?:px)?['\"]")


def _size(svg):
    m = SVG_SIZE.search(svg or "")
    return (float(m.group(1)), float(m.group(2))) if m else (0.0, 0.0)


def _text_width(text, size=SCHEME_FONT):
    return 0.58 * size * len(text or "")


def scheme_svg(card):
    """A printed reaction SCHEME, row by row: structures, text, `+` and arrows with what is printed
    over and under each arrow.

    RDKit's reaction drawing could not say what the booklet says: 2017_A q052 printed
    "(i) OH-  (ii) Delta" over its arrow and the drawing showed "HO-", tiny, with the product
    flipped; q061's scheme is LETTERS (X, A, Y, Z) and condition text around one drawn reagent, and
    the drawing showed only the reagent. A scheme row is a list of items --
      {"species": n}   the card's n-th species (1-based), drawn as species_svg draws it, label below
      {"text": "..."}  printed text: a letter, a formula, "Silver mirror observed"
      {"plus": true}   a "+"
      {"arrow": {"above": "...", "below": "..."}}
    -- and a branching scheme is written as one row per branch, so every arrow and every condition
    printed is drawn and nothing is left to a layout guess.
    """
    species = card.get("species") or []
    rows_out, width, y = [], 0.0, 0.0
    gap = 10.0
    font = "font-family='Arial,Helvetica,sans-serif'"
    for row in card.get("scheme") or []:
        cells = []
        for item in row:
            if "species" in item:
                n = item["species"] - 1
                if not 0 <= n < len(species):
                    continue
                sp = species[n]
                svg = species_svg(sp["smiles"], sp.get("orient"), sp.get("abbreviate", True),
                                  sp.get("explicit_h"), sp.get("annotations"), sp.get("name"))
                w, h = _size(svg)
                label = sp.get("label") or ""
                cells.append(("species", max(w, _text_width(label, 13)), h + (18 if label else 0),
                              (svg, w, h, label)))
            elif "text" in item:
                cells.append(("text", _text_width(item["text"]) + 4, SCHEME_FONT + 6, item["text"]))
            elif item.get("plus"):
                cells.append(("text", 16.0, SCHEME_FONT + 6, "+"))
            elif "arrow" in item:
                above = (item["arrow"] or {}).get("above") or ""
                below = (item["arrow"] or {}).get("below") or ""
                length = max(56.0, _text_width(above, 12) + 16, _text_width(below, 12) + 16)
                cells.append(("arrow", length, 2 * (SCHEME_FONT + 8), (above, below)))
        if not cells:
            continue
        row_h = max(c[2] for c in cells)
        mid = y + row_h / 2
        x, parts = 0.0, []
        for kind, w, h, payload in cells:
            if kind == "species":
                svg, sw, sh, label = payload
                top = mid - h / 2
                parts.append(place(svg, x + (w - sw) / 2, top))
                if label:
                    parts.append("<text x='%.1f' y='%.1f' %s font-size='13' text-anchor='middle'>"
                                 "%s</text>" % (x + w / 2, top + sh + 14, font,
                                                 _escape(formula_label(label))))
            elif kind == "text":
                parts.append("<text x='%.1f' y='%.1f' %s font-size='%d' dominant-baseline='middle'>"
                             "%s</text>" % (x + 2, mid, font, SCHEME_FONT, _escape(payload)))
            else:
                above, below = payload
                parts.append("<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%.1f' stroke='#000' "
                             "stroke-width='1.4'/><path d='M %.1f %.1f L %.1f %.1f L %.1f %.1f Z' "
                             "fill='#000'/>" % (x + 2, mid, x + w - 8, mid, x + w - 2, mid,
                                                x + w - 10, mid - 4, x + w - 10, mid + 4))
                if above:
                    parts.append("<text x='%.1f' y='%.1f' %s font-size='12' text-anchor='middle'>"
                                 "%s</text>" % (x + w / 2, mid - 6, font, _escape(above)))
                if below:
                    # an explicit baseline, not `hanging`, which some renderers ignore and then
                    # set the text ON the arrow
                    parts.append("<text x='%.1f' y='%.1f' %s font-size='12' text-anchor='middle'>"
                                 "%s</text>" % (x + w / 2, mid + 17, font, _escape(below)))
            x += w + gap
        rows_out.append("".join(parts))
        width = max(width, x - gap)
        y += row_h + 14
    if not rows_out:
        return None
    height = y - 14
    return ("<svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' "
            "width='%.1f' height='%.1f' viewBox='0 0 %.1f %.1f'>%s</svg>"
            % (width, height, width, height, "".join(rows_out)))


def drawn_texts(card):
    """Every piece of text the drawing of this card SHOWS -- what figure_text.missing() checks the
    printed words against. Never the card's own `text` description, which is not drawn."""
    out = [s.get("label") or "" for s in card.get("species") or []]
    for s in card.get("species") or []:
        out += [str(a.get("text", "")) for a in s.get("annotations") or []]
    for row in card.get("scheme") or []:
        for item in row:
            if "text" in item:
                out.append(item["text"])
            if "arrow" in item:
                arrow = item["arrow"] or {}
                out += [arrow.get("above") or "", arrow.get("below") or ""]
    return out


def elements(card):
    """Element symbols the card's structures contain (what an atom label on the print may show)."""
    out = set()
    for s in card.get("species") or []:
        ok, facts = species_facts(s.get("smiles") or "")
        if ok:
            out |= set(re.findall(r"[A-Z][a-z]?", facts["formula"]))
    return out


def reaction_svg(reaction_smiles):
    Chem, rxn, _desc, draw = _rdkit()
    try:
        reaction = rxn.ReactionFromSmarts(reaction_smiles, useSmiles=True)
    except Exception:                                           # noqa: BLE001
        return None
    drawer = draw.MolDraw2DSVG(720, 220)
    _options(draw, drawer)
    drawer.DrawReaction(reaction)
    drawer.FinishDrawing()
    return _tidy(drawer.GetDrawingText())


def _tidy(svg):
    """Drop RDKit's XML header and its white background rect, so the drawing sits on the page."""
    svg = svg.split("?>", 1)[-1].strip() if svg.startswith("<?xml") else svg
    return svg.replace("<rect style='opacity:1.0;fill:#FFFFFF;stroke:none'", "<rect style='opacity:0'")


def check_card(card):
    """[problem, ...] for one figure card. Empty means the card passes."""
    problems = []
    kind = card.get("kind")
    species = card.get("species") or []
    if kind == "not_a_structure":
        if species or card.get("reaction_smiles"):
            problems.append("%s: not_a_structure must carry no SMILES" % card.get("figure_id"))
        return problems
    if kind == "reaction":
        # The brief keeps `reaction_smiles` only "where every species is known"; a reaction with an
        # unknown is drawn from its `scheme` alone (2019_P1 q047's "A", q078's blank product).
        if card.get("reaction_smiles") or not card.get("scheme"):
            ok, message = reaction_ok(card.get("reaction_smiles") or "",
                                      product_may_be_blank=bool(card.get("scheme")))
            if not ok:
                problems.append("%s: %s" % (card.get("figure_id"), message))
    if kind == "structures" and not species:
        problems.append("%s: kind is structures but no species are given" % card.get("figure_id"))
    for n, item in enumerate(species, 1):
        ok, facts = species_facts(item.get("smiles") or "")
        if not ok:
            problems.append("%s species %d: %s" % (card.get("figure_id"), n, facts))
            continue
        if facts["has_wildcard"] and not (card.get("note") or "").strip():
            problems.append("%s species %d uses a wildcard [*] with no note saying what it stands for"
                            % (card.get("figure_id"), n))
    if card.get("confidence") == "unsure" and not (card.get("note") or "").strip():
        problems.append("%s: confidence unsure with an empty note" % card.get("figure_id"))
    return problems


def enrich(card):
    """The card as stored on the record: each species with its formula, canonical SMILES, InChIKey
    and the outcome of the name check, so a consumer never has to re-derive them."""
    out = dict(card)
    enriched = []
    for item in card.get("species") or []:
        ok, facts = species_facts(item.get("smiles") or "")
        entry = dict(item)
        if ok:
            entry.update({"canonical_smiles": facts["canonical"], "formula": facts["formula"],
                          "inchikey": facts["inchikey"]})
        status, detail = name_check(item.get("name"), item.get("smiles") or "")
        entry["name_check"] = status
        entry["name_check_detail"] = detail
        enriched.append(entry)
    out["species"] = enriched
    return out
