"""questions.json v3: one record per question, grouped, renderable as it stands.

WHY A NEW SHAPE. The v2 record was right field by field and hard to use: a question was spread
over six fields, a drawn option was the string "[structure in figure]" with its SMILES three levels
down in `agent_figures[0].drawn.card.species[]`, every image had its own pair of path/URL fields
under a different name, and a drawing carried both `card` and `spec` with one always null. A
consumer that asked for "the question" got half of it. v3 groups the same facts:

  question   {full_text, html, stem, format, statements, list_i, list_ii, figures, chemistry,
              options[{key, text, chemistry, figure}], screenshot}
  answer     {publisher, publisher_accepted, publisher_starred, publisher_line, ai, ai_confidence,
              verdict}
  solution   {full_text, html, steps, figures[...after_step], screenshot, concludes, complete,
              agrees_with_answer, printed_lines}
  ai_solution, classification, difficulty, source, status, pending

THE BUILDING BLOCKS, the same everywhere:
  Asset    {path, cdn_url, sha256, type}            path is relative to papers/
  Figure   {id, text, printed: {png, svg}, drawn}   printed = the booklet's own figure, exact
  Drawn    {method, renderer, status, checks, image, ...data}   our drawing, from checked data
  Species  {label, name, smiles, formula, inchikey, name_check, image}

`full_text` is the whole question (or solution) as ONE string in reading order -- Markdown with
$...$ LaTeX, a drawn structure written as its name and SMILES, a figure as its one-line text -- so
a search or a model that is handed the record gets all of it. `html` is the same content rendered
(LaTeX already HTML, images by CDN URL) for a page that just needs to show it.
"""

import collections
import html
import os
import re

from lib import cdn, texhtml

SCHEMA = "neet-pyq/question-record/v3"

CONTENT_TYPES = {".png": "image/png", ".svg": "image/svg+xml", ".jpg": "image/jpeg"}
RENDERERS = {"smiles": "RDKit (code/lib/chem_cards.py)", "spec": "code/lib/physics_figure.py",
             "booklet": "booklet geometry (code/lib/print_trace.py)",
             "traced": "the printed picture traced to vector lines (code/lib/raster_trace.py)"}
METHODS = {"smiles": "smiles", "spec": "physics_spec"}
OPTION_LABEL = re.compile(r"^\(?\s*([1-4])\s*\)?$")

#: The reader's description of a drawn structure inside an option ("[structure: benzene ring with
#: $\mathrm{OH}$]") -- words about a picture, not words printed in the booklet.
DRAWING_NOTE = re.compile(r"\[\s*(?:chemical\s+)?(?:structure|figure|image|diagram|drawing)\b[^\]]*\]",
                          re.I)


def option_words(text, species_count, has_picture):
    """An option's PRINTED words, once its picture or structures carry the drawing.

    2018_AA q052 option (1) was read as "[structure: benzene ring with CH(CH3)2], [structure:
    benzene ring with OH], CH3CH(OH)CH3" and printed beside the very image of those three products.
    The bracketed notes go; what is left stays when it is printed next to the drawing (q068's "and
    I2"), and goes when the option's structures already account for it: two notes plus one listed
    formula against three species means the formula is the third structure in the picture.
    Without a picture or structures, the note is the only account of the option and is kept.
    """
    text = text or ""
    if not (has_picture or species_count) or not DRAWING_NOTE.search(text):
        return text
    notes = len(DRAWING_NOTE.findall(text))
    rest = [p.strip() for p in DRAWING_NOTE.split(text)]
    rest = ", ".join(p.strip(" ,;") for p in rest if p.strip(" ,;"))
    if species_count and notes + len([p for p in rest.split(",") if p.strip()]) == species_count:
        return ""
    return rest


def formula_picture_option(text, species, drawn_status, others_plain):
    """True when an option's picture is a structure its printed words already spell out in full.

    2015_A q001 option (3): the booklet prints "(CH3)2CH-CH(CH3)-CH=CH2" as a picture (the CH3
    branch hangs below the line) among three options printed as text. The reader wrote the whole
    formula out and a picture-printed figure is not redrawn, so the option showed its crop, a SMILES
    line and the same formula again -- unlike the other three. User, 2026-10-29: "make it consistent
    options". Such an option is shown as text like its neighbours; its crop and SMILES stay in the
    record. 2018_AA q090's orbital boxes are not a structure, so they stay a picture.
    """
    text = (text or "").strip()
    return bool(text and species and others_plain and drawn_status == "not_on_print"
                and not DRAWING_NOTE.search(text)
                and not re.fullmatch(r"\[[^\]]*(structure|figure|image)[^\]]*\]", text, re.I))


def options_shown_as_text(options):
    """The keys of v3 `options` whose picture is shown as their text (formula_picture_option)."""
    return {o["key"] for o in options
            if o["figure"] and formula_picture_option(
                o["text"], o["chemistry"], (o["figure"].get("drawn") or {}).get("status"),
                all(not p["figure"] for p in options if p is not o))}

#: The stylesheet every `html` field assumes, carried once in the document's meta.
RENDER_CSS = texhtml.CSS + """
.q-stem,.s-step{line-height:1.6}
.q-statements,.q-options,.s-steps{margin:.4em 0 .4em 1.6em;padding:0}
.q-statements{list-style:none;margin-left:.4em}
.q-options{list-style:none;margin-left:0}
.q-options li{margin:.25em 0}.q-options .key{font-weight:600;margin-right:.4em}
.q-match{border-collapse:collapse;margin:.5em 0}
.q-match th,.q-match td{border:1px solid #bbb;padding:.25em .6em;text-align:left;vertical-align:top}
.q-fig,.s-fig{margin:.5em 0}.q-fig img,.s-fig img{max-width:100%;height:auto;background:#fff}
.chem{display:inline-flex;flex-direction:column;align-items:center;margin:.2em .6em .2em 0;
 vertical-align:middle}.chem img{max-height:9em;background:#fff}.chem .name{font-size:.8em}
"""


def _posix(path):
    return path.replace("\\", "/") if path else path


def asset(q, path):
    """Asset for one local file of this question: its path, CDN URL, sha256 and media type."""
    if not path:
        return None
    return collections.OrderedDict([
        ("path", _posix(path)), ("cdn_url", cdn.url_for(q, path)),
        ("sha256", cdn.sha_for(q, path)),
        ("type", CONTENT_TYPES.get(os.path.splitext(path)[1].lower(), "application/octet-stream"))])


def clean_smiles(smiles):
    """The SMILES with drawing handles (atom-map numbers) removed, canonical -- what an app renders."""
    try:
        from rdkit import Chem, RDLogger
        RDLogger.DisableLog("rdApp.*")
        mol = Chem.MolFromSmiles(smiles or "")
        if mol is None:
            return smiles
        for atom in mol.GetAtoms():
            atom.SetAtomMapNum(0)
        return Chem.MolToSmiles(mol)
    except Exception:                                           # noqa: BLE001
        return re.sub(r":\d+\]", "]", smiles or "")


def species_record(q, item, svg_path, shown_as=None):
    return collections.OrderedDict([
        ("label", item.get("label") or ""), ("name", item.get("name") or ""),
        ("smiles", clean_smiles(item.get("smiles"))),
        ("formula", item.get("formula")), ("inchikey", item.get("inchikey")),
        ("name_check", item.get("name_check")),
        # "structure": a printed drawing this SMILES was laid on atom for atom; "text": printed as
        # a formula ("+ CH3I"); null where the figure is not a vector drawing
        ("shown_as", shown_as),
        ("image", asset(q, svg_path))])


def _checks(entry):
    """What code verified about a drawing, in words a reader can audit."""
    if entry.get("source") == "smiles":
        species = (entry.get("card") or {}).get("species") or []
        tally = collections.Counter(s.get("name_check") for s in species)
        shown = collections.Counter(m.get("shown_as") for m in entry.get("print_match") or [])
        return collections.OrderedDict([
            ("smiles_parse", "pass" if species else "n/a"),
            ("name_check", ", ".join("%d %s" % (n, k) for k, n in sorted(tally.items())) or "n/a"),
            ("print_match", ("%d structure(s) match the printed drawing atom for atom, %d printed "
                             "as a formula" % (shown["structure"], shown["text"]))
             if entry.get("layout") == "booklet" else
             "picture-printed figure: the print itself, traced" if entry.get("layout") == "traced"
             else "not a vector figure: drawn by RDKit"),
            ("printed_text", "pass" if entry.get("status") == "drawn" else entry.get("status"))])
    spec = entry.get("spec") or {}
    match = entry.get("print_match") or {}
    return collections.OrderedDict([
        ("renders", "pass" if entry.get("status") == "drawn" else entry.get("status")),
        ("print_match", ("all %d label(s) printed; %d%% of the spec's lines on the printed ones, "
                         "%d%% of the printed lines covered"
                         % (match.get("labels", 0), 100 * match.get("precision", 0),
                            100 * match.get("recall", 0)))
         if entry.get("layout") == "booklet" else
         "picture-printed figure: the print itself, traced" if entry.get("layout") == "traced"
         else "not a vector figure: drawn from the spec"),
        ("angles", "%d claimed, all within 1.5 deg" % len(spec.get("angles_claimed") or [])
         if spec.get("angles_claimed") else "none claimed"),
        ("netlist", "matches the drawn wires" if spec.get("netlist") else "not a circuit"),
        ("printed_text", "pass" if entry.get("status") == "drawn" else entry.get("status"))])


def drawn_record(q, entry):
    if not entry:
        return None
    source = entry.get("source")
    layout = entry.get("layout")
    out = collections.OrderedDict([
        ("method", METHODS.get(source, source)),
        ("renderer", RENDERERS.get(layout if layout in ("booklet", "traced") else source)),
        ("layout", layout),
        ("status", entry.get("status")), ("checks", _checks(entry)),
        ("image", asset(q, entry.get("svg"))), ("message", entry.get("message"))])
    if source == "smiles":
        card = entry.get("card") or {}
        singles = entry.get("species_svgs") or []
        out["kind"] = card.get("kind")
        out["reaction_smiles"] = card.get("reaction_smiles")
        shown = entry.get("print_match") or []
        out["species"] = [species_record(q, s, singles[n] if n < len(singles) else None,
                                         shown[n]["shown_as"] if n < len(shown) else None)
                          for n, s in enumerate(card.get("species") or [])]
        out["scheme"] = card.get("scheme")
        out["draw_hints"] = [{"smiles": s.get("smiles"), "orient": s.get("orient"),
                              "explicit_h": s.get("explicit_h"), "annotations": s.get("annotations"),
                              "abbreviate": s.get("abbreviate", True)}
                             for s in card.get("species") or []]
        out["excluded_text"] = card.get("excluded_text") or []
        out["confidence"] = card.get("confidence")
        out["note"] = card.get("note")
    else:
        out["spec"] = entry.get("spec")
        out["unreadable"] = entry.get("unreadable") or []
    return out


def figure_text(entry):
    if not entry:
        return None
    if entry.get("source") == "smiles":
        return (entry.get("card") or {}).get("text") or None
    return (entry.get("spec") or {}).get("title") or None


def figure_record(q, figure_id, png, extra=None):
    vector = q.get("vector") or {}
    entry = (q.get("drawn") or {}).get(png)
    out = collections.OrderedDict([
        ("id", figure_id), ("text", figure_text(entry)),
        ("printed", collections.OrderedDict([("png", asset(q, png)),
                                             ("svg", asset(q, vector.get(png)))])),
        ("drawn", drawn_record(q, entry))])
    if extra:
        out.update(extra)
    return out


def _src(asset_obj):
    """The link an `html` field uses: the CDN URL with the file's fingerprint, so a drawing redone
    under the same name is fetched again rather than served from a browser's cache."""
    asset_obj = asset_obj or {}
    url = asset_obj.get("cdn_url")
    if url and asset_obj.get("sha256"):
        return "%s?v=%s" % (url, asset_obj["sha256"][:12])
    return url or asset_obj.get("path") or ""


def _img(figure, alt):
    """An <img> of a figure's PRINTED copy -- the exact vector where one exists."""
    printed = figure["printed"]
    best = printed.get("svg") or printed.get("png")
    return '<img src="%s" alt="%s" loading="lazy">' % (html.escape(_src(best)), html.escape(alt or ""))


def _chem_html(species):
    return "".join('<span class="chem"><img src="%s" alt="%s"><span class="name">%s</span></span>'
                   % (html.escape(_src(s["image"])), html.escape(s["name"]), html.escape(s["name"]))
                   for s in species)


def _chem_text(species):
    return "; ".join("%s [SMILES: %s]" % (s["name"] or "structure", s["smiles"]) for s in species)


def build(q, flat, read):
    """The v3 record for one question, from the v2 record `flat` (whose helpers stay the single
    source of every value) and the paper JSON entry `q` (figures, drawings, CDN links)."""
    qno = q["qno"]
    agent_images = q.get("agent_figure_images") or []
    option_images = q.get("agent_option_images") or {}

    # ---- figures and the chemistry they carry ------------------------------------------------
    question_figures, option_figures, question_chem = [], {}, []
    option_chem = collections.defaultdict(list)
    for png in agent_images:
        fig = figure_record(q, "question", png)
        species = (fig["drawn"] or {}).get("species") or []
        to_options = 0
        for s in species:
            m = OPTION_LABEL.match(s["label"] or "")
            if m and m.group(1) in (flat["options"] or {}):
                option_chem[m.group(1)].append(s)
                to_options += 1
            else:
                question_chem.append(s)
        # a figure whose every structure is an option's is the OPTIONS' picture, not the stem's
        fig["shows"] = ("options" if species and to_options == len(species)
                        else "question_and_options" if to_options else "question")
        question_figures.append(fig)
    for key, png in sorted(option_images.items()):
        fig = figure_record(q, "option_%s" % key, png)
        fig["shows"] = "option"
        option_figures[key] = fig
        option_chem[key].extend((fig["drawn"] or {}).get("species") or [])
    for figure in flat.get("figures") or []:
        if figure.get("local") and not figure.get("superseded_by_agent"):
            fig = figure_record(q, "geometric_%s" % figure.get("role"), figure["local"])
            fig["shows"] = "question"
            question_figures.append(fig)

    options = []
    for key in sorted((flat["options"] or {}).keys()):
        text = flat["options"][key] or ""
        if re.fullmatch(r"\s*\[[^\]]*(structure|figure|image)[^\]]*\]\s*", text, re.I):
            text = ""                                   # a placeholder, not printed text
        text = option_words(text, len(option_chem.get(key, [])), key in option_figures)
        options.append(collections.OrderedDict([
            ("key", key), ("text", text), ("chemistry", option_chem.get(key, [])),
            ("figure", option_figures.get(key))]))

    stem = flat["question_text"] or ""
    statements = [s for s in flat["statements"] if isinstance(s, dict)] or \
                 [{"label": "", "text": s} for s in flat["statements"]]
    fmt = flat.get("structure") or "plain"

    # ---- question.full_text and question.html -------------------------------------------------
    lines = [stem]
    for fig in question_figures:
        if fig["shows"] != "options" and fig["text"]:
            lines.append("[Figure: %s]" % fig["text"])
    if question_chem:
        lines.append("[Structures: %s]" % _chem_text(question_chem))
    lines += ["(%s) %s" % (s.get("label"), s.get("text")) if s.get("label") else s.get("text")
              for s in statements]
    if flat["list_i"]:
        lines.append("List-I: " + "; ".join("(%s) %s" % (i.get("label"), i.get("text"))
                                            for i in flat["list_i"]))
        lines.append("List-II: " + "; ".join("(%s) %s" % (i.get("label"), i.get("text"))
                                             for i in flat["list_ii"]))
    as_text = options_shown_as_text(options)
    for opt in options:
        parts = [opt["text"]] if opt["text"] else []
        if opt["key"] in as_text:
            pass
        elif opt["chemistry"]:
            parts.insert(0, _chem_text(opt["chemistry"]))
        if opt["figure"] and opt["figure"]["text"] and not opt["chemistry"]:
            parts.insert(0, "[Figure: %s]" % opt["figure"]["text"])
        lines.append("(%s) %s" % (opt["key"], " ".join(parts).strip()))
    full_text = "\n".join(l for l in lines if l)

    h = ['<div class="q-stem">%s</div>' % texhtml.to_html(stem, line_breaks=True)]
    for fig in question_figures:
        if fig["shows"] == "options":
            continue                         # its structures are drawn on their options below
        h.append('<figure class="q-fig">%s</figure>' % _img(fig, fig["text"] or "figure"))
    if question_chem and not any(f["shows"] != "options" for f in question_figures):
        h.append('<div class="q-chem">%s</div>' % _chem_html(question_chem))
    if statements:
        h.append('<ol class="q-statements">%s</ol>' % "".join(
            "<li>%s%s</li>" % ("<b>(%s)</b> " % html.escape(s.get("label")) if s.get("label") else "",
                               texhtml.to_html(s.get("text") or "")) for s in statements))
    if flat["list_i"]:
        rows = max(len(flat["list_i"]), len(flat["list_ii"]))
        cells = []
        for n in range(rows):
            a = flat["list_i"][n] if n < len(flat["list_i"]) else {}
            b = flat["list_ii"][n] if n < len(flat["list_ii"]) else {}
            cells.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
                         % (html.escape(a.get("label", "")), texhtml.to_html(a.get("text", "")),
                            html.escape(b.get("label", "")), texhtml.to_html(b.get("text", ""))))
        h.append('<table class="q-match"><thead><tr><th colspan="2">List-I</th>'
                 '<th colspan="2">List-II</th></tr></thead><tbody>%s</tbody></table>' % "".join(cells))
    opts = []
    for opt in options:
        body = []
        if opt["key"] in as_text:
            pass
        elif opt["figure"] and not opt["chemistry"]:
            body.append(_img(opt["figure"], "option %s" % opt["key"]))
        elif opt["chemistry"]:
            body.append(_chem_html(opt["chemistry"]))
        if opt["text"]:
            body.append(texhtml.to_html(opt["text"]))
        opts.append('<li><span class="key">(%s)</span>%s</li>' % (opt["key"], " ".join(body)))
    h.append('<ol class="q-options">%s</ol>' % "".join(opts))
    for fig in question_figures:
        if fig["shows"] == "options":
            h.append('<details class="q-printed"><summary>options as printed</summary>'
                     '<figure class="q-fig">%s</figure></details>' % _img(fig, "options as printed"))
    question_html = "".join(h)

    question = collections.OrderedDict([
        ("full_text", full_text), ("html", question_html), ("stem", stem), ("format", fmt),
        ("statements", statements), ("list_i", flat["list_i"]), ("list_ii", flat["list_ii"]),
        ("figures", question_figures), ("chemistry", question_chem), ("options", options),
        ("negative_words", flat["negative_words_seen"]),
        ("number_printed", q.get("number_printed", True)),
        ("restored_opening", flat["restored_opening"]),
        ("screenshot", asset(q, q.get("question_image")))])

    # ---- solution -----------------------------------------------------------------------------
    steps = flat["publisher_solution_stepwise"]
    sol_figures = [figure_record(q, "solution_%d" % n, f["image"],
                                 {"after_step": f.get("after_step", 0), "kind": f.get("kind")})
                   for n, f in enumerate(q.get("solution_figures") or [], 1)]
    by_step = collections.defaultdict(list)
    for fig in sol_figures:
        by_step[min(int(fig["after_step"] or 0), len(steps))].append(fig)
    text_lines, html_items = [], []
    for fig in by_step.get(0, []):
        text_lines.append("[Figure: %s]" % (fig["text"] or "figure"))
    lead = "".join('<figure class="s-fig">%s</figure>' % _img(f, f["text"] or "figure")
                   for f in by_step.get(0, []))
    for n, step in enumerate(steps, 1):
        text_lines.append("%d. %s" % (n, step))
        figs = by_step.get(n, [])
        text_lines += ["[Figure: %s]" % (f["text"] or "figure") for f in figs]
        html_items.append('<li class="s-step">%s%s</li>' % (
            texhtml.to_html(step), "".join('<figure class="s-fig">%s</figure>'
                                           % _img(f, f["text"] or "figure") for f in figs)))
    solution_html = (lead + '<ol class="s-steps">%s</ol>' % "".join(html_items)) if (steps or lead) else ""
    solution = collections.OrderedDict([
        ("full_text", "\n".join(text_lines)), ("html", solution_html), ("steps", steps),
        ("figures", sol_figures), ("screenshot", asset(q, q.get("solution_image"))),
        ("concludes", flat["publisher_concludes"]), ("complete", flat["publisher_solution_complete"]),
        ("agrees_with_answer", flat["verdict_self"]),
        ("printed_lines", flat["publisher_solution_draft"])])

    ai_steps = flat["ai_solution_stepwise"]
    ai_solution = collections.OrderedDict([
        ("steps", ai_steps),
        ("html", '<ol class="s-steps">%s</ol>' % "".join(
            '<li class="s-step">%s</li>' % texhtml.to_html(s) for s in ai_steps) if ai_steps else ""),
        ("why", flat["ai_why"]), ("confidence", flat["ai_confidence"])])

    subtopics = [collections.OrderedDict([("id", flat["subtopic_%d_id" % n]),
                                          ("name", flat["subtopic_%d_name" % n]),
                                          ("why", flat["subtopic_%d_why" % n])])
                 for n in (1, 2) if flat["subtopic_%d_id" % n]]
    return collections.OrderedDict([
        ("question_id", flat["question_id"]), ("paper_code", flat["paper_code"]),
        ("year", flat["year"]), ("booklet_code", flat["booklet_code"]), ("qno", qno),
        ("flags", flat["flags"]),
        ("question", question),
        ("answer", collections.OrderedDict([
            ("publisher", flat["publisher_answer"]),
            ("publisher_text", flat["publisher_answer_text"]),
            ("publisher_accepted", flat["publisher_answers_accepted"]),
            ("publisher_starred", flat["publisher_answer_starred"]),
            ("publisher_line", flat["publisher_answer_line"]),
            ("ai", flat["ai_answer"]), ("ai_text", flat["ai_answer_text"]),
            ("ai_confidence", flat["ai_confidence"]), ("verdict", flat["verdict_answer"])])),
        ("solution", solution),
        ("ai_solution", ai_solution),
        ("classification", collections.OrderedDict([
            ("subject", flat["subject"]), ("subject_from", flat["subject_from"]),
            ("subject_why", flat["subject_why"]), ("subject_confidence", flat["subject_confidence"]),
            ("stream", flat["stream"]), ("branch", flat["branch"]),
            ("chapter", collections.OrderedDict([
                ("code", flat["chapter_code"]), ("name", flat["chapter_name"]),
                ("why", flat["chapter_why"]), ("confidence", flat["chapter_confidence"])])),
            ("subtopics", subtopics), ("taxonomy_gap", flat["taxonomy_gap"])])),
        ("difficulty", collections.OrderedDict([
            ("level", flat["difficulty_level"]), ("steps", flat["difficulty_steps"]),
            ("step_list", flat["difficulty_step_list"]), ("why", flat["difficulty_why"]),
            ("what_makes_it_hard", flat["what_makes_it_hard"])])),
        ("source", collections.OrderedDict([
            ("pdf", flat["source_pdf"]), ("page", flat["page"]), ("read_from", flat["read_from"]),
            ("note", flat["read_note"]), ("text_layer_reliable", flat["text_layer_reliable"]),
            ("needs_image_read", flat["needs_image_read"]),
            ("is_key_grid_row", flat["is_key_grid_row"]),
            ("superseded_geometric_crops", [f for f in flat.get("figures") or []
                                            if f.get("superseded_by_agent")])])),
        ("status", flat["status"]), ("pending", flat["pending"]),
    ])


def assets_in(record):
    """Every Asset object anywhere in a record (for the images-without-CDN count)."""
    out = []

    def walk(value):
        if isinstance(value, dict):
            if set(value) >= {"path", "cdn_url", "sha256", "type"}:
                out.append(value)
                return
            for v in value.values():
                walk(v)
        elif isinstance(value, list):
            for v in value:
                walk(v)
    walk(record)
    return out
