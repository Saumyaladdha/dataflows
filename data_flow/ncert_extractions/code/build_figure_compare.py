"""A side-by-side page: the figure as scanned, and the figure as redrawn.

WHY THE ORIGINAL STAYS ON THE PAGE
----------------------------------
A redraw is a CLAIM about what the original shows, and a claim needs its source beside it -- exactly
as the booklet crop sits beside the extracted text, and a quoted NCERT line beside its page scan. A
redrawn figure shown alone cannot be checked by anyone; shown beside the scan it can be checked by
anyone, in a second, without reading a spec.

This page is also where a redraw is JUDGED before any of it reaches a question card. Two faults in
the first three figures were caught here and nowhere else: a label clipped off the left edge, and --
the one that matters -- a velocity vector drawn at 40.7 degrees while its own label read 60. A
drawing that contradicts its own label is worse than the photocopy it replaced, because it looks
authoritative. Neither fault was visible in the spec; both were obvious the moment the two sat side
by side.
"""

import argparse
import html
import json
import os
import sys

CSS = """
:root{--ink:#11151d;--ink2:#4c5460;--ink3:#78808d;--rule:#d2d9e5;--ground:#dfe5f0;--card:#fff;
 --accent:#1d3156;--ok:#0d5239;--warn:#71500a;
 --sans:ui-sans-serif,system-ui,-apple-system,sans-serif;--mono:ui-monospace,SFMono-Regular,monospace;
 --serif:ui-serif,Georgia,serif}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans)}
.wrap{max-width:1180px;margin:0 auto;padding:32px 28px 90px}
.wrap::before{content:"";display:block;height:4px;border-radius:99px;margin:0 0 28px;
 background:linear-gradient(90deg,#0d4e32 0 33%,#1d3156 33% 66%,#653f08 66% 100%)}
.lede{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:22px 24px;
 margin:0 0 34px;box-shadow:0 1px 2px rgba(20,30,54,.05),0 12px 30px -18px rgba(20,30,54,.3)}
.lede h1{margin:0 0 10px;font-size:19px;letter-spacing:-.015em}
.lede p{margin:0 0 10px;font-size:13.5px;line-height:1.7;color:var(--ink2);max-width:76ch}
.lede p:last-child{margin-bottom:0}
.fig{background:var(--card);border:1px solid var(--rule);border-left:4px solid var(--accent);
 border-radius:12px;margin:0 0 30px;overflow:hidden;
 box-shadow:0 1px 2px rgba(20,30,54,.05),0 12px 30px -18px rgba(20,30,54,.3)}
.fhead{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:16px 24px;
 background:#e3eaf5;border-bottom:1px solid var(--rule)}
.fid{font:700 11.5px/1 var(--mono);letter-spacing:.06em;background:var(--accent);color:#fff;
 padding:7px 11px;border-radius:6px}
.ftitle{font:400 14.5px/1.5 var(--serif);color:var(--ink)}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:0}
@media (max-width:820px){.cols{grid-template-columns:1fr}}
.col{padding:20px 24px 24px}
.col+.col{border-left:1px solid var(--rule)}
@media (max-width:820px){.col+.col{border-left:0;border-top:1px solid var(--rule)}}
.clab{font:700 10px/1.5 var(--sans);letter-spacing:.16em;text-transform:uppercase;
 color:var(--ink3);border-bottom:1px solid #e4e9f1;padding-bottom:8px;margin-bottom:16px}
.col img{max-width:100%;height:auto;border:1px solid var(--rule);border-radius:6px;background:#fff}
.col svg{max-width:100%;height:auto}
.fig.org{border-left-color:#653f08}
.fig.bad{border-left-color:#a82d2d}
.fig.org .fhead{background:#f6ecda}
.rxn{overflow-x:auto}
.facts{display:flex;gap:22px;flex-wrap:wrap;padding:14px 24px 18px;border-top:1px solid #e4e9f1;
 font-size:12.5px;color:var(--ink2)}
.facts b{color:var(--ink)}
.chk{font:650 11.5px/1 var(--sans);padding:7px 12px;border-radius:99px;border:1px solid currentColor}
.chk.pass{color:var(--ok);background:#e0efe7}
.chk.note{color:var(--warn);background:#f8eed6}
.note{padding:0 24px 18px;font-size:13px;line-height:1.65;color:var(--ink2);max-width:80ch}
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--specs", default="figures/specs")
    ap.add_argument("--svg", default="figures/svg")
    ap.add_argument("--cards", default="figures/cards")
    ap.add_argument("--out", default="figures/compare.html")
    args = ap.parse_args()

    out_dir = os.path.dirname(os.path.abspath(args.out))
    blocks, counts = [], {"physics": 0, "organic": 0, "no original": 0}

    def original_for(figure_id):
        """The scan a redraw is claiming to reproduce, wherever it lives.

        Three naming conventions meet on this page -- NCERT figure crops, A2S block crops, and the
        paper's own question figures -- so the lookup tries each rather than assuming one.
        """
        stem = figure_id.replace("_", "-")
        for candidate in (os.path.join("ncert", "figures", stem + ".png"),
                          os.path.join("steps", "A2S", "work", stem + ".png")):
            if os.path.exists(candidate):
                return candidate
        if "-q" in stem:
            paper, qno = stem.rsplit("-", 1)
            crop = os.path.join("papers_v2", "figures_agent", paper.replace("-", "_"), qno + ".png")
            if os.path.exists(crop):
                return crop
        return None
    for name in sorted(os.listdir(args.specs)):
        if not name.endswith(".json"):
            continue
        figure_id = name[:-len(".json")]
        with open(os.path.join(args.specs, name), encoding="utf-8") as fh:
            spec = json.load(fh)
        svg_path = os.path.join(args.svg, figure_id + ".svg")
        if not os.path.exists(svg_path):
            continue
        with open(svg_path, encoding="utf-8") as fh:
            svg = fh.read()

        original = original_for(figure_id)
        rel = os.path.relpath(original, out_dir) if original else None
        counts["physics"] += 1
        counts["no original"] += 0 if rel else 1

        # Every angle the figure claims is recomputed from the coordinates that were drawn.
        checks = []
        import math
        for claim in (spec.get("angles_claimed") or []):
            vx, vy = claim["vertex"]
            rx, ry = claim["ray_to"]
            base = claim.get("measured_from")
            drawn = math.degrees(math.atan2(ry - vy, rx - vx))
            if base:
                bx, by = base
                drawn -= math.degrees(math.atan2(by - vy, bx - vx))
            drawn = abs((drawn + 180) % 360 - 180)
            ok = abs(drawn - claim["degrees"]) <= 0.6
            checks.append('<span class="chk %s">%s labelled %g&deg;, drawn %.1f&deg;</span>'
                          % ("pass" if ok else "note", "&check;" if ok else "&#9888;",
                             claim["degrees"], drawn))

        facts = ('<div class="facts"><span>primitives <b>%d</b></span>'
                 '<span>SVG <b>%.1f KB</b></span>%s%s</div>'
                 % (len(spec["draw"]), len(svg) / 1024, "".join(checks),
                    '<span>unreadable in the original: <b>%s</b></span>'
                    % html.escape("; ".join(spec["unreadable"]))
                    if spec.get("unreadable") else ""))

        blocks.append(
            '<section class="fig"><div class="fhead"><span class="fid">%s</span>'
            '<span class="ftitle">%s</span></div><div class="cols">'
            '<div class="col"><div class="clab">as scanned from the booklet</div>%s</div>'
            '<div class="col"><div class="clab">redrawn from the spec</div>%s</div></div>%s%s'
            '</section>'
            % (html.escape(figure_id.replace("_", " ")), html.escape(spec["title"]),
               '<img src="%s" alt="original scan of %s">' % (html.escape(rel), figure_id)
               if rel else '<p class="note">no original crop on disk</p>',
               svg, facts,
               '<p class="note">%s</p>' % html.escape(spec["note"]) if spec.get("note") else ""))

    # ORGANIC CARDS. Rendered through RDKit rather than the primitive renderer, so they are built
    # here rather than read from figures/svg -- but they land in the same comparison, because the
    # question a reader is answering is the same one: does the redraw show what the scan shows?
    if os.path.isdir(args.cards):
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import render_reaction
        for name in sorted(os.listdir(args.cards)):
            if not name.endswith(".json"):
                continue
            card_id = name[:-len(".json")]
            with open(os.path.join(args.cards, name), encoding="utf-8") as fh:
                card = json.load(fh)
            try:
                html_body, formulas = render_reaction.render(card, show_formula=True)
            except Exception as exc:                      # a card that cannot draw is a finding
                blocks.append('<section class="fig bad"><div class="fhead">'
                              '<span class="fid">%s</span><span class="ftitle">%s</span></div>'
                              '<p class="note">did not render: %s</p></section>'
                              % (html.escape(card_id), html.escape(card.get("title", "")),
                                 html.escape(str(exc))))
                continue
            original = original_for(card_id)
            rel = os.path.relpath(original, out_dir) if original else None
            counts["organic"] += 1
            counts["no original"] += 0 if rel else 1
            facts = ('<div class="facts"><span>structures <b>%d</b></span>%s</div>'
                     % (len(formulas),
                        "".join('<span class="chk pass">%s <b>%s</b></span>'
                                % (html.escape(n[:28]), f) for n, f in formulas)))
            blocks.append(
                '<section class="fig org"><div class="fhead"><span class="fid">%s</span>'
                '<span class="ftitle">%s</span></div><div class="cols">'
                '<div class="col"><div class="clab">as printed in NCERT</div>%s</div>'
                '<div class="col"><div class="clab">redrawn from the card</div>%s</div></div>%s%s'
                '</section>'
                % (html.escape(card_id.replace("_", " ")), html.escape(card.get("title", "")),
                   '<img src="%s" alt="NCERT scan of %s">' % (html.escape(rel), card_id)
                   if rel else '<p class="note">no original crop on disk</p>',
                   html_body, facts,
                   '<p class="note">could not be drawn: %s</p>'
                   % html.escape("; ".join(card["unreadable"]))
                   if card.get("unreadable") else ""))

    # THE REACTION RENDERER'S OWN STYLESHEET HAS TO TRAVEL WITH ITS MARKUP.
    # `render_reaction.render()` returns spans with classes -- `.unit`, `.name`, `.formula`,
    # `.arrow` -- and this page was never including the CSS that gives them meaning. Unstyled, each
    # structure drew at its intrinsic SVG size (one became a black chevron the height of the page),
    # every arrow lost its shaft and head, and a molecule's name ran straight into its formula:
    # "4-NitrotolueneC7H7NO2Br2". Every one of those was read as a renderer bug and none of them was.
    reaction_css = ""
    if os.path.isdir(args.cards):
        import render_reaction as _rr
        reaction_css = _rr.CSS

    page = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Figure redraws</title><style>%s%s</style></head><body><div class="wrap">'
        '<div class="lede"><h1>Redrawn figures, beside the scans they come from</h1>'
        '<p>Each booklet figure is a crop of a reprint, and three faults come with that: it is '
        '<b>clipped</b> where the drawing shares a region with the stem, it is <b>raster</b> at '
        'booklet resolution so it blurs when a card scales it, and it carries the publisher&rsquo;s '
        'watermark. A fourth is worse &mdash; <b>a photocopy has no colour</b>, so a question whose '
        'answer turns on which ray is blue shows three identical black arrows.</p>'
        '<p>A redraw is a <b>claim</b> about what the original shows, so the scan stays beside it. '
        'Every angle the figure labels is recomputed from the coordinates actually drawn, and '
        'reported below each pair &mdash; a drawing that contradicts its own label is worse than '
        'the photocopy it replaced, because it looks authoritative.</p></div>%s</div></body></html>'
        % (CSS, reaction_css, "".join(blocks)))

    os.makedirs(out_dir, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(page)
    print("html  %-30s %d figure(s): %d physics, %d organic, %d with no original scan, %.0f KB"
          % (args.out, len(blocks), counts["physics"], counts["organic"],
             counts["no original"], len(page) / 1024))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
