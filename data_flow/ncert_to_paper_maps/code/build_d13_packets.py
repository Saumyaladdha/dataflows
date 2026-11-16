#!/usr/bin/env python3
"""Build D13 packets -- everything the solution-diagram agent needs to choose a picture.

WHAT THIS STEP IS FOR
---------------------
The owner's instruction was two-sided: "draw new when possible, if not we can draw arrows if
complex diagrams of biology". So the agent has to be able to do both, which means the packet
has to carry both kinds of raw material:

  * the question's OWN printed figure, as a file it can open. q157 prints three muscle-tissue
    drawings labelled a, b and c and every option refers to them; without the image the agent
    can neither mark them nor judge whether marking is the right move.
  * every figure the mapped NCERT chapter prints, with the book's own caption. These are
    already drawn and already correct -- Figure 6.5 "T.S. of leaf : (a) Dicot (b) Monocot" is
    exactly the picture a bulliform-cell question wants, and no redrawing can improve on it.

IMAGES ARE FETCHED, NOT LINKED. This paper's figures live only on the CDN -- `papers/
figures_agent/2024_S1/` does not exist locally -- and an agent can only read files. So any
image named in a packet is downloaded once into `steps/D13/figs/` and the packet points at
the local copy. NCERT figure URLs are passed as URLs, because the agent chooses between them
by CAPTION and only needs to open one if it decides to mark it.

Usage:
    python3 code/build_d13_packets.py --paper 2024_S1 --questions q101,q106,q107,q153,q157
    python3 code/build_d13_packets.py --paper 2024_S1 --questions ... --apply
"""

import argparse
import collections
import json
import os
import re
import subprocess
import sys
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(HERE))
PAPERS = os.path.join(REPO, "data_flow", "paper_extraction", "data")
FIGDIR = os.path.join(HERE, "steps", "D13", "figs")

#: Page furniture, not figures: the chapter-opener banner and the QR code sit in every chapter.
_NOT_A_FIGURE = re.compile(r'_(header|qr)_')


def _kinds_from_renderer():
    """Read each primitive's real arguments off the renderer, rather than restating them.

    A HAND-WRITTEN LIST DRIFTS, AND EVERY DRIFT COSTS A ROUND TRIP. Three specs were refused
    in a row for believing a vocabulary that was close but not exact: `shapes` instead of
    `draw`, `box`/`text` instead of `block`/`label`, then `block` with a `fill` it does not
    accept (a filled rectangle is `band`; `block` is the hatched mechanics block). Each time
    the fix was to correct prose that had quietly fallen out of step with the code.

    So the argument lists are introspected from `render_figure.Canvas` itself. Required keys
    come from `PRIMITIVES`, which the renderer already enforces; optional ones are the
    method's remaining keyword arguments with their defaults. If someone adds a primitive or
    an option, this follows automatically.
    """
    sys.path.insert(0, os.path.join(REPO, "data_flow", "ncert_extractions", "code"))
    import inspect
    import render_figure as rf

    getargs = getattr(inspect, "getfullargspec", inspect.getargspec)
    out = {}
    for kind, required in sorted(rf.PRIMITIVES.items()):
        fn = getattr(rf.Canvas, kind, None)
        if fn is None:
            continue
        spec = getargs(fn)
        defaults = dict(zip(spec.args[-len(spec.defaults or ()):], spec.defaults or ()))
        optional = ["%s=%r" % (k, v) for k, v in defaults.items()]
        out[kind] = "required: %s%s" % (
            ", ".join(required) or "(none)",
            ("  |  optional: " + ", ".join(sorted(optional))) if optional else
            "  |  no other keys are accepted")
    return out

#: What the renderer actually draws, carried into every packet. Read off
#: `ncert_extractions/code/render_figure.py` -- the same renderer the physics figures use.
RENDERER_VOCABULARY = {
    "the_draw_block_IS_the_spec": {
        "width": 300, "height": 120, "pad": 14, "title": "...",
        "draw": "[ the list of items, under the key 'draw' -- not 'shapes' ]"},
    "frame": "mathematical: y points UP, origin bottom-left; width/height set the canvas",
    "kinds": "(filled in below from the renderer itself)",
    "there_is_no": ["box", "text", "polyline", "rect"],
    "use_instead": {"box": "block", "text": "label"},
    "colours": ["ink", "accent", "muted", "blue", "green", "red", "violet", "orange",
                "yellow", "white", "card", "palegrey", "ncert", "ncertband"],
    "no_other_colour_exists": "not black, grey, lightgrey, lightblue, gold or any hex value",
    "annotate_coordinates": ("percentages of the image, 0-100, y measured DOWN from the top "
                             "-- the opposite of the draw canvas"),
    "label_size_must_be_a_number": (
        "`size` is a number of canvas units, not a word. The renderer writes it straight into "
        "font-size, so 'normal' or 'small' is silently ignored by the browser and the label "
        "comes out at the default size, wrecking a layout you planned around it. About 15 for "
        "a heading, 11 for a note."),
    "labels_are_measured_and_collisions_are_rejected": (
        "A label is centred on its `at` point and is about 0.52 * size * len(text) wide. "
        "Work that out for each one, keep its box inside 0..width and 0..height, and keep it "
        "clear of every other label's box. The build measures this and REFUSES a spec whose "
        "labels overlap or fall off the canvas -- a 42-character label at size 15 is ~330 "
        "units wide, so it does not fit a 300-wide canvas at all. Widen the canvas, lower the "
        "size, or shorten the wording."),
}


def ncert_figures(pages, chapter_ids):
    """Every captioned figure the mapped chapter prints, in page order."""
    out = []
    for cid in chapter_ids or []:
        for pg, html_ in sorted((pages.get(cid) or {}).items()):
            for m in re.finditer(r'<img[^>]*>', html_):
                tag = m.group(0)
                src = re.search(r'src="([^"]+)"', tag)
                alt = re.search(r'alt="([^"]*)"', tag)
                if not src or _NOT_A_FIGURE.search(src.group(1)):
                    continue
                cap = (alt.group(1) if alt else "").strip()
                if not cap:
                    continue
                out.append({"url": src.group(1), "caption": cap,
                            "chapter": cid, "printed_page": pg})
    return out


def localise(figs, qid, offline):
    """Download each NCERT figure so the agent can actually LOOK at it before marking it.

    The first run could never choose "mark the book's figure". The agent said why, and it was
    right: its read tool takes local paths, the packet gave it CloudFront URLs, and its brief
    forbids marking a diagram it has not opened -- so annotating an NCERT figure was
    unreachable in practice and the step always fell back to showing the figure unmarked.
    The images are small and cached by name, so fetching them once makes the option real.
    """
    for i, f in enumerate(figs):
        if offline:
            continue
        p = fetch(f["url"], "%s_ncert%d" % (qid, i), 0)
        if p:
            f["path"] = p
    return figs


def fetch(url, qid, n):
    """Download one image into the step's cache. Returns the local path, or None.

    VIA CURL, NOT URLLIB. This machine's Python has no CA bundle -- urlopen on the CDN dies
    with CERTIFICATE_VERIFY_FAILED -- while curl uses the system trust store and succeeds.
    Shelling out keeps the certificate check rather than disabling it, which is the other
    way people get past this error.
    """
    os.makedirs(FIGDIR, exist_ok=True)
    ext = os.path.splitext(url.split("?")[0])[1] or ".png"
    path = os.path.join(FIGDIR, "%s_%d%s" % (qid, n, ext))
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return path
    try:
        # stdout/stderr spelled out rather than capture_output=: this runs on Python 3.6,
        # where that keyword does not exist and raises TypeError straight into the fallback.
        subprocess.run(["curl", "-sSf", "-o", path, url], check=True, timeout=60,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception:
        try:
            with urllib.request.urlopen(url, timeout=30) as r, open(path, "wb") as f:
                f.write(r.read())
        except Exception:
            return None
    return path if os.path.exists(path) and os.path.getsize(path) > 0 else None


def question_figures(q, qid, offline):
    """The booklet's own drawings for this question, as files the agent can open."""
    qq, out, n = q.get("question") or {}, [], 0
    srcs = [(f, f.get("text") or "figure printed with the question")
            for f in (qq.get("figures") or [])]
    srcs += [(o.get("figure") or {}, "option %s, as drawn" % o.get("key"))
             for o in (qq.get("options") or [])]
    srcs += [(f, f.get("text") or "diagram from the printed solution")
             for f in ((q.get("solution") or {}).get("figures") or [])]
    for f, what in srcs:
        png = ((f.get("printed") or {}).get("png") or {})
        local = png.get("path")
        if local and os.path.exists(os.path.join(REPO, local)):
            out.append({"path": os.path.join(REPO, local), "what": what})
            continue
        if png.get("cdn_url") and not offline:
            p = fetch(png["cdn_url"], qid, n)
            n += 1
            if p:
                out.append({"path": p, "what": what, "from": png["cdn_url"]})
    return out


RENDERER_VOCABULARY["kinds"] = _kinds_from_renderer()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--questions", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--offline", action="store_true", help="skip downloads")
    a = ap.parse_args()

    year = a.paper.split("_")[0]
    doc = json.load(open(os.path.join(PAPERS, year, a.paper, "questions.json"), encoding="utf-8"))
    Q = {q["question_id"].split("__")[-1]: q for q in doc["questions"]}
    pages = json.load(open(os.path.join(HERE, "maps", "page_html.json"), encoding="utf-8"))

    report, built = collections.Counter(), []
    for qid in [x.strip() for x in a.questions.split(",") if x.strip()]:
        q = Q.get(qid)
        if not q:
            report["no such question"] += 1
            continue
        p = os.path.join(HERE, "steps", "D12", "out", "%s.%s.runA.json" % (a.paper, qid))
        if not os.path.exists(p):
            report["no D12 solution yet"] += 1
            continue
        d12 = json.load(open(p, encoding="utf-8"))
        qq = q.get("question") or {}
        mp = q.get("ncert_mapping") or {}
        figs = question_figures(q, qid, a.offline)
        nfigs = localise(ncert_figures(pages, (mp.get("chapter") or {}).get(
            "ncert_chapter_ids") or []), qid, a.offline)
        built.append({
            "question_id": q["question_id"],
            "question": {
                "stem": qq.get("stem"),
                "statements": qq.get("statements") or [],
                "list_i": qq.get("list_i") or [], "list_ii": qq.get("list_ii") or [],
                "options": [{"key": o.get("key"), "text": (o.get("text") or "").strip()}
                            for o in (qq.get("options") or [])],
                "figures": figs,
            },
            "solution": {
                "answer_is": d12.get("answer_is"),
                "what_ncert_says": d12.get("what_ncert_says"),
                "explanation": d12.get("explanation"),
                "why_other_options_fail": d12.get("why_other_options_fail") or [],
            },
            "ncert_figures": nfigs,
            "note_from_runner": ("Open every file in question.figures before deciding. "
                                 "`none` is a correct answer when no picture serves THIS "
                                 "question's reasoning -- do not manufacture one."),
            # THE VOCABULARY TRAVELS WITH THE PACKET, NOT ONLY IN THE BRIEF. An agent's brief
            # is loaded into its system prompt when the session registers it, so editing the
            # brief does not reach an already-registered agent. Two specs were written against
            # a superseded shape list for exactly that reason and the renderer refused both.
            # Carried here, the vocabulary is read fresh on every run.
            "renderer_vocabulary": RENDERER_VOCABULARY,
        })
        report["ready"] += 1
        report["has a printed figure"] += 1 if figs else 0
        report["NCERT figures downloaded"] += len([f for f in nfigs if f.get("path")])

    print("%s: %d D13 packet(s)" % (a.paper, len(built)))
    for k, v in sorted(report.items()):
        if k != "ready":
            print("   %-34s %d" % (k, v))
    for b in built:
        print("   %-6s own-figures=%d  ncert-figures=%d"
              % (b["question_id"].split("__")[-1], len(b["question"]["figures"]),
                 len(b["ncert_figures"])))
    if not a.apply:
        print("(nothing written -- pass --apply)")
        return
    work = os.path.join(HERE, "steps", "D13", "work")
    os.makedirs(work, exist_ok=True)
    for b in built:
        qid = b["question_id"].split("__")[-1]
        json.dump(b, open(os.path.join(work, "%s.%s.runA.input.json" % (a.paper, qid)),
                          "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote %d packet(s) to steps/D13/work" % len(built))


if __name__ == "__main__":
    main()
