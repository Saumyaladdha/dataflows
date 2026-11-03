#!/usr/bin/env python3
"""Put the VERIFIED redraws onto the paper's figure records.

    python3 code/publish_drawn_figures.py --paper-id 2026_11 --apply

WHY THIS IS SEPARATE FROM render_figure_cards.py
------------------------------------------------
`render_figure_cards.py` draws a spec ON the booklet's own vector geometry and checks it against
that geometry, atom for atom. It REFUSES a figure the booklet prints as a picture, and its own
note says why: the standalone renderer once "floated 2016_A q034's gates off their wires and
shrank q010's labels", and with no printed geometry there is nothing to catch that.

2026_11 is the case that refusal was written for -- the booklet carries 90 embedded images where
2017 Code-A carried none, so most of its figures are rasters and the geometric check cannot run.
That left the paper with no redraws at all.

So the check is supplied a different way: every redraw is rendered, put beside the printed crop,
and JUDGED BY EYE, with the verdict and its reason recorded per figure. This script publishes
only what that pass accepted, and records `checked_by: "visual comparison with the print"` so
nobody later mistakes it for the geometric check -- they are not the same evidence and the record
says which one a figure has.

A rejected redraw is dropped, not downgraded. The printed crop stays, which is what the page
showed before.
"""

import argparse
import json
import os
import shutil

import runner_core as rc


def publish(paper_id, apply_=False):
    verdicts = rc.pp("steps", "FIGP", "work", "%s_visual_check.json" % paper_id)
    if not os.path.exists(verdicts):
        raise SystemExit("no visual check at %s -- run the comparison first" % verdicts)
    checked = {c["name"]: c for c in json.load(open(verdicts, encoding="utf-8"))["checked"]}
    accepted = {k: v for k, v in checked.items() if v.get("verdict") == "accept"}
    print("%s: %d checked, %d accepted, %d rejected"
          % (paper_id, len(checked), len(accepted), len(checked) - len(accepted)))

    src_dir = rc.pp("papers", "figures_drawn_review", paper_id)
    out_dir = rc.pp("papers", "figures_drawn", paper_id)
    rec_path = rc.pp("papers", "papers", "%s.json" % paper_id)
    rec = json.load(open(rec_path, encoding="utf-8"))
    by_qno = {q["qno"]: q for q in rec["questions"]}

    published = 0
    for name, v in sorted(accepted.items()):
        svg = os.path.join(src_dir, name + ".svg")
        if not os.path.exists(svg):
            print("  missing render for %s" % name); continue
        qno = int(name.split("__q")[1][:3])
        q = by_qno.get(qno)
        if not q:
            print("  no question %d" % qno); continue
        rel = os.path.join("figures_drawn", paper_id, name + ".svg")
        if apply_:
            os.makedirs(out_dir, exist_ok=True)
            shutil.copyfile(svg, os.path.join(out_dir, name + ".svg"))
            # KEYED BY THE PRINTED IMAGE IT REDRAWS, not by the spec's own name. The export
            # looks the drawing up as `q["drawn"][<image path>]` while rendering that image, so
            # a drawing filed under its spec name is never found and the page shows the crop
            # alone -- which is what happened on the first publish of this paper.
            printed = (v.get("printed") or "").replace("papers/", "", 1)
            if not printed:
                print("  %s has no printed path recorded; skipped" % name); continue
            q.setdefault("drawn", {})[printed] = {
                "method": "physics_spec",
                "renderer": "lib/physics_figure.render (standalone)",
                "layout": "spec",
                "status": "drawn",
                # NAMED, so it is never confused with the geometric check. A figure checked by
                # eye and one checked against the booklet's own vector paths carry different
                # weight, and the record has to say which one this is.
                "checked_by": "visual comparison with the print",
                "check_note": v.get("why", ""),
                "printed_compared": v.get("printed", ""),
                "source": "spec",
                # `figure_id` is read straight into the <img alt> by the export, so it has to
                # be here or the page build dies on a KeyError at render time.
                "figure_id": name.split("__", 1)[1],
                # `svg`, because that is the key `lib/cdn.image_paths` collects -- writing the
                # path under `image` instead meant the uploader never saw these files and they
                # stayed local while everything around them went to the CDN.
                "svg": rel,
                "image": {"path": rel},
            }
        published += 1
    if apply_:
        json.dump(rec, open(rec_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("  %d redraw(s) %s" % (published, "published" if apply_ else "would be published"))
    for name, v in sorted(checked.items()):
        if v.get("verdict") != "accept":
            print("  REJECTED %-34s %s" % (name, " ".join((v.get("why") or "").split())[:90]))
    return published


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper-id", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    publish(a.paper_id, a.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
