"""question_paper.md: one booklet as Markdown, written from the SAME v3 records as questions.json.

The third deliverable beside questions.json and question_paper.html. It is built from the records
(record_v3.build), never from a second reading of the data, so whatever a fix changes in the JSON --
a restored opening, a drawing on the booklet's geometry, a flag -- is in the Markdown the same run.

Markdown with `$...$` LaTeX, as the records hold it (GitHub, Obsidian and most viewers render it).
Every image is its CDN link with the file's fingerprint, like the HTML.
"""
import record_v3


def _img(asset_obj, alt):
    src = record_v3._src(asset_obj)
    return "![%s](%s)" % (alt.replace("]", ")").replace("[", "("), src) if src else ""


def _cell(text):
    return (text or "").replace("|", "\\|").replace("\n", " ")


def _drawn(fig):
    drawn = fig.get("drawn") or {}
    if drawn.get("status") != "drawn" or not drawn.get("image"):
        return ""
    how = ("drawn on the booklet's geometry, checked against its %s"
           % ("SMILES" if drawn.get("method") == "smiles" else "figure spec")
           if drawn.get("layout") == "booklet" else "drawn by %s" % drawn.get("renderer"))
    return "%s  \n*%s*" % (_img(drawn["image"], "drawn: %s" % (fig.get("text") or fig["id"])), how)


def _figure(fig):
    printed = fig["printed"].get("svg") or fig["printed"].get("png")
    out = [_img(printed, "printed figure: %s" % (fig.get("text") or fig["id"]))]
    if fig.get("text"):
        out.append("*%s*" % fig["text"])
    drawn = _drawn(fig)
    if drawn:
        out.append(drawn)
    return "\n\n".join(o for o in out if o)


def _chem(species):
    return "; ".join("%s `%s`%s" % (s["name"] or "structure", s["smiles"],
                                    (" " + _img(s["image"], s["name"] or "structure"))
                                    if s.get("image") else "")
                     for s in species)


def question_md(r):
    q, a, sol, ai = r["question"], r["answer"], r["solution"], r["ai_solution"]
    c, d = r["classification"], r["difficulty"]
    head = "## Q%d" % r["qno"]
    tags = [c.get("subject"), c.get("stream") or c.get("branch"), (c.get("chapter") or {}).get("name")]
    lines = [head, "", " · ".join(t for t in tags if t), ""]
    for flag in r.get("flags") or []:
        lines += ["> ⚠ %s" % flag["text"], ""]
    lines += [q["stem"], ""]
    for fig in q["figures"]:
        if fig.get("shows") != "options":
            lines += [_figure(fig), ""]
    if q["chemistry"]:
        lines += ["Structures: %s" % _chem(q["chemistry"]), ""]
    for s in q["statements"]:
        lines.append("- %s%s" % ("**(%s)** " % s["label"] if s.get("label") else "", s.get("text") or ""))
    if q["statements"]:
        lines.append("")
    if q["list_i"]:
        lines += ["| List-I | | List-II | |", "|---|---|---|---|"]
        for n in range(max(len(q["list_i"]), len(q["list_ii"]))):
            x = q["list_i"][n] if n < len(q["list_i"]) else {}
            y = q["list_ii"][n] if n < len(q["list_ii"]) else {}
            lines.append("| %s | %s | %s | %s |" % (_cell(x.get("label")), _cell(x.get("text")),
                                                   _cell(y.get("label")), _cell(y.get("text"))))
        lines.append("")
    for opt in q["options"]:
        parts = []
        if opt["chemistry"]:
            parts.append(_chem(opt["chemistry"]))
        elif opt.get("figure"):
            parts.append(_figure(opt["figure"]).replace("\n\n", " "))
        if opt["text"]:
            parts.append(opt["text"])
        key = "**(%s)**" % opt["key"] if opt["key"] in (a.get("publisher_accepted") or []) else "(%s)" % opt["key"]
        lines.append("- %s %s" % (key, " — ".join(parts)))
    lines.append("")
    for fig in q["figures"]:
        if fig.get("shows") == "options":
            lines += ["Options as printed:", "", _figure(fig), ""]
    lines += ["**Answer** — booklet: (%s) · independent solve: (%s) · %s"
              % (", ".join(a.get("publisher_accepted") or []) or "none", a.get("ai") or "—",
                 a.get("verdict") or "not judged"), ""]
    if sol["steps"] or sol["figures"]:
        lines += ["**Publisher's solution**", ""]
        by_step = {}
        for fig in sol["figures"]:
            by_step.setdefault(min(int(fig.get("after_step") or 0), len(sol["steps"])), []).append(fig)
        for fig in by_step.get(0, []):
            lines += [_figure(fig), ""]
        for n, step in enumerate(sol["steps"], 1):
            lines.append("%d. %s" % (n, step))
            for fig in by_step.get(n, []):
                lines += ["", _figure(fig), ""]
        lines.append("")
    if ai["steps"]:
        lines += ["**Solved independently** (answer withheld)", ""]
        lines += ["%d. %s" % (n, s) for n, s in enumerate(ai["steps"], 1)]
        lines.append("")
    topics = ", ".join(t["name"] for t in c.get("subtopics") or [] if t.get("name"))
    lines += ["**Subtopic:** %s · **Difficulty:** %s (%s step%s)" % (
        topics or "—", d.get("level") or "—", d.get("steps") or 0, "" if d.get("steps") == 1 else "s"), ""]
    # the printed record, as in the booklet: the question, and under it the publisher's solution
    if q.get("screenshot") or sol.get("screenshot"):
        lines += ["**Printed in the booklet** (page %s)" % r["source"].get("page"), ""]
        if q.get("screenshot"):
            lines += [_img(q["screenshot"], "printed question %d" % r["qno"]), ""]
        if sol.get("screenshot"):
            lines += ["Publisher's solution, as printed:", "",
                      _img(sol["screenshot"], "printed solution %d" % r["qno"]), ""]
    return "\n".join(lines)


def write(document, path):
    meta = document["meta"]
    counts = document["counts"]
    head = ["# NEET (UG) %s · Code %s" % (meta["year"], meta["booklet_code"]), "",
            "%d questions · source `%s` · every image a CDN link (%d without one) · %d figures "
            "redrawn" % (counts["questions"], meta["source_pdf"], counts["images_without_cdn"],
                         counts["drawn_figures"]),
            "", "Generated from `questions.json` (schema `%s`) by `code/paper_md.py`; edit the "
            "pipeline, not this file." % document["schema"], ""]
    body = [question_md(r) for r in document["questions"]]
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(head) + "\n" + "\n---\n\n".join(body) + "\n")
