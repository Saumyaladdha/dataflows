#!/usr/bin/env python3
"""Renders docs/question_categories/*.csv into one browsable HTML page.

    python3 scripts/render_category_sheet.py            # -> docs/question_categories/sheet.html

Reads the two CSVs that build_category_sheet.py writes and embeds them as JSON. Every number on
the page comes from the CSVs; none is typed here.
"""

import argparse
import csv
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

DEFECT_CATS = {"C14", "C15"}  # source defects, not exam traps -- a real distinction, shown as one

_PAGE = """<title>NEET Question Traps</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root {
  --paper:#f7f8fa; --card:#ffffff; --ink:#15181f; --ink-2:#4a5160; --ink-3:#737c8c;
  --rule:#dfe3ea; --rule-2:#eceff4;
  --accent:#1f49a6; --accent-soft:#e8edf9; --accent-ink:#163b86;
  --warn:#9a5b06; --warn-soft:#fdf1dd; --defect:#962a33; --defect-soft:#fbe9ea;
  --shadow:0 1px 2px rgba(20,24,33,.05),0 6px 18px -8px rgba(20,24,33,.12);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper:#0e1116; --card:#161b22; --ink:#e8ebf0; --ink-2:#aab2c0; --ink-3:#7d8694;
    --rule:#272e38; --rule-2:#1d232c;
    --accent:#8fb0f0; --accent-soft:#18243a; --accent-ink:#b8cdf7;
    --warn:#e0ab5c; --warn-soft:#2a2113; --defect:#e8909a; --defect-soft:#2e171b;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 22px -10px rgba(0,0,0,.6);
  }
}
:root[data-theme="dark"] {
  --paper:#0e1116; --card:#161b22; --ink:#e8ebf0; --ink-2:#aab2c0; --ink-3:#7d8694;
  --rule:#272e38; --rule-2:#1d232c;
  --accent:#8fb0f0; --accent-soft:#18243a; --accent-ink:#b8cdf7;
  --warn:#e0ab5c; --warn-soft:#2a2113; --defect:#e8909a; --defect-soft:#2e171b;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 22px -10px rgba(0,0,0,.6);
}
* { box-sizing:border-box; }
body {
  margin:0; background:var(--paper); color:var(--ink);
  font:400 15px/1.6 "IBM Plex Sans", ui-sans-serif, system-ui, sans-serif;
  -webkit-font-smoothing:antialiased;
}
.wrap { max-width:1120px; margin:0 auto; padding:clamp(28px,5vw,64px) clamp(18px,4vw,36px) 96px; }
h1,h2,h3 { font-family:Archivo, "IBM Plex Sans", sans-serif; text-wrap:balance; margin:0; }
h1 { font-size:clamp(30px,5.2vw,46px); font-weight:700; letter-spacing:-.022em; line-height:1.08; }
.sub { color:var(--ink-2); font-size:clamp(16px,2vw,18px); max-width:62ch; margin:16px 0 0; }
.meta { display:flex; flex-wrap:wrap; gap:10px 28px; margin:28px 0 0; padding:18px 0 0;
  border-top:1px solid var(--rule); }
.meta div { display:flex; flex-direction:column; gap:3px; }
.meta dt, .lbl { font:500 11px/1.2 "IBM Plex Mono", monospace; letter-spacing:.09em;
  text-transform:uppercase; color:var(--ink-3); }
.meta dd { margin:0; font:500 22px/1 Archivo, sans-serif; font-variant-numeric:tabular-nums; }
section { margin-top:clamp(44px,6vw,72px); }
h2 { font-size:clamp(21px,2.6vw,26px); font-weight:600; letter-spacing:-.012em; }
.note { color:var(--ink-2); max-width:70ch; margin:12px 0 0; font-size:14.5px; }
.note b { color:var(--ink); font-weight:600; }

.grid { display:grid; gap:14px; margin-top:26px;
  grid-template-columns:repeat(auto-fill, minmax(330px, 1fr)); }
.cat { background:var(--card); border:1px solid var(--rule); border-radius:12px; padding:18px 18px 16px;
  box-shadow:var(--shadow); display:flex; flex-direction:column; gap:12px; }
.cat.defect { border-color:color-mix(in srgb, var(--defect) 40%, var(--rule)); }
.cat-top { display:flex; align-items:baseline; gap:10px; }
.cid { font:500 12px/1 "IBM Plex Mono", monospace; color:var(--accent-ink);
  background:var(--accent-soft); padding:5px 7px; border-radius:5px; letter-spacing:.04em; }
.cat.defect .cid { color:var(--defect); background:var(--defect-soft); }
.cat h3 { font-size:16.5px; font-weight:600; letter-spacing:-.008em; flex:1; }
.n { font:500 13px/1 "IBM Plex Mono", monospace; color:var(--ink-3); font-variant-numeric:tabular-nums; }
.shape { font:400 12.5px/1.5 "IBM Plex Mono", monospace; color:var(--ink-2);
  background:var(--rule-2); border-radius:6px; padding:8px 10px; }
.trap { font-size:14px; color:var(--ink); margin:0; }
.trap em { color:var(--warn); font-style:normal; font-weight:600; }
.spot { font-size:12.5px; color:var(--ink-3); margin:0; }
ol.steps { margin:2px 0 0; padding:0; list-style:none; counter-reset:s;
  border-top:1px solid var(--rule-2); padding-top:11px; display:flex; flex-direction:column; gap:7px; }
ol.steps li { counter-increment:s; position:relative; padding-left:26px; font-size:13.5px;
  color:var(--ink-2); }
ol.steps li::before { content:counter(s); position:absolute; left:0; top:1px;
  font:500 10px/16px "IBM Plex Mono", monospace; width:16px; height:16px; text-align:center;
  border-radius:4px; background:var(--accent-soft); color:var(--accent-ink); }
.cat.defect ol.steps li::before { background:var(--defect-soft); color:var(--defect); }

.chips { display:flex; flex-wrap:wrap; gap:7px; margin:22px 0 0; }
.chip { font:500 12px/1 "IBM Plex Mono", monospace; letter-spacing:.03em; cursor:pointer;
  background:var(--card); color:var(--ink-2); border:1px solid var(--rule); border-radius:999px;
  padding:8px 12px; }
.chip[aria-pressed="true"] { background:var(--accent); color:#fff; border-color:var(--accent); }
.chip:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }

.q { background:var(--card); border:1px solid var(--rule); border-radius:11px; padding:16px 17px;
  margin-top:11px; box-shadow:var(--shadow); }
.q.defect { border-left:3px solid var(--defect); }
.q-head { display:flex; flex-wrap:wrap; align-items:center; gap:9px; margin-bottom:11px; }
.qid { font:500 12.5px/1 "IBM Plex Mono", monospace; color:var(--ink); }
.tag { font:500 10.5px/1 "IBM Plex Mono", monospace; letter-spacing:.06em; text-transform:uppercase;
  padding:4px 6px; border-radius:4px; background:var(--rule-2); color:var(--ink-3); }
.tag.neg { background:var(--warn-soft); color:var(--warn); }
.tag.fig { background:var(--accent-soft); color:var(--accent-ink); }
.tag.c { background:var(--accent-soft); color:var(--accent-ink); }
.q.defect .tag.c { background:var(--defect-soft); color:var(--defect); }
.qtext { white-space:pre-wrap; font-size:14.5px; color:var(--ink); margin:0 0 11px; }
.opts { display:grid; gap:5px; margin:0 0 4px; }
.opt { font:400 13px/1.45 "IBM Plex Mono", monospace; color:var(--ink-2);
  background:var(--rule-2); border-radius:5px; padding:6px 9px; overflow-x:auto; }
details { margin-top:11px; border-top:1px solid var(--rule-2); padding-top:10px; }
summary { cursor:pointer; font:500 11px/1.2 "IBM Plex Mono", monospace; letter-spacing:.08em;
  text-transform:uppercase; color:var(--ink-3); }
summary:focus-visible { outline:2px solid var(--accent); outline-offset:3px; }
footer { margin-top:72px; padding-top:20px; border-top:1px solid var(--rule); color:var(--ink-3);
  font-size:13px; }
@media (prefers-reduced-motion:no-preference) { .q, .cat { transition:border-color .15s ease; } }
</style>

<div class="wrap">
<h1>NEET Question Traps</h1>
<p class="sub">Every question shape found in the extracted NEET papers, what content each shape
needs, the mechanism that makes it answerable-but-wrong, and the four steps that defuse it.</p>

<dl class="meta">
  <div><dt>Questions classified</dt><dd data-f="nq"></dd></div>
  <div><dt>Categories</dt><dd data-f="ncat"></dd></div>
  <div><dt>Exam traps</dt><dd data-f="ntrap"></dd></div>
  <div><dt>Source defects</dt><dd data-f="ndefect"></dd></div>
  <div><dt>Worked examples</dt><dd data-f="nex"></dd></div>
</dl>

<section>
  <h2>The categories</h2>
  <p class="note">Derived from the corpus, not assumed: each count is how many of the classified
  questions fall in that category. The last two are <b>not exam traps</b> &mdash; they are defects in
  our source material, where the printed question has no single answer or its options were never
  captured. They are separated because the response differs: a trap is solved, a defect is re-acquired.</p>
  <div class="grid" id="cats"></div>
</section>

<section>
  <h2>Worked examples</h2>
  <p class="note">Real question ids with the text as transcribed. For match and assertion&ndash;reason
  shapes the stem alone is boilerplate, so the lists and statements are shown with it &mdash; that is
  where all the discriminating content lives.</p>
  <div class="chips" id="chips"></div>
  <div id="qs"></div>
</section>

<footer>Generated from <span class="qid">docs/question_categories/*.csv</span> by
<span class="qid">scripts/render_category_sheet.py</span>. Question text is as transcribed from the
source images; nothing here is reconstructed.</footer>
</div>

<script id="data" type="application/json">__DATA__</script>
<script>
(function(){
  var D = JSON.parse(document.getElementById('data').textContent);
  var DEFECT = __DEFECT__;
  var isDef = function(c){ return DEFECT.indexOf(c) >= 0; };

  var f = {
    nq: D.classified, ncat: D.categories.length,
    ntrap: D.categories.filter(function(c){ return !isDef(c.cat_id); }).length,
    ndefect: D.categories.filter(function(c){ return isDef(c.cat_id); }).length,
    nex: D.questions.length
  };
  Object.keys(f).forEach(function(k){
    var el = document.querySelector('[data-f="' + k + '"]');
    if (el) el.textContent = f[k];
  });

  var esc = function(s){ var d = document.createElement('div'); d.textContent = s == null ? '' : s; return d.innerHTML; };

  document.getElementById('cats').innerHTML = D.categories.map(function(c){
    return '<article class="cat' + (isDef(c.cat_id) ? ' defect' : '') + '">' +
      '<div class="cat-top"><span class="cid">' + esc(c.cat_id) + '</span>' +
      '<h3>' + esc(c.category_name) + '</h3>' +
      '<span class="n">' + esc(c.count_in_corpus) + '</span></div>' +
      '<div class="shape">' + esc(c.content_shape) + '</div>' +
      '<p class="trap">' + esc(c.trap_mechanism) + '</p>' +
      '<p class="spot">Spot it: ' + esc(c.how_to_spot) + '</p>' +
      '<ol class="steps">' + [c.step_1, c.step_2, c.step_3, c.step_4]
        .map(function(s){ return '<li>' + esc(s) + '</li>'; }).join('') + '</ol>' +
      '</article>';
  }).join('');

  var active = 'ALL';
  var cats = D.categories.map(function(c){ return c.cat_id; });
  document.getElementById('chips').innerHTML =
    ['ALL'].concat(cats).map(function(c){
      return '<button class="chip" type="button" data-c="' + c + '" aria-pressed="' +
        (c === 'ALL') + '">' + c + '</button>';
    }).join('');

  function render(){
    var rows = D.questions.filter(function(q){ return active === 'ALL' || q.cat_id === active; });
    document.getElementById('qs').innerHTML = rows.map(function(q){
      var tags = '<span class="tag c">' + esc(q.cat_id) + ' &middot; ' + esc(q.category_name) + '</span>';
      if (q.structure) tags += '<span class="tag">' + esc(q.structure) + '</span>';
      if (q.negative_words) tags += '<span class="tag neg">' + esc(q.negative_words) + '</span>';
      if (q.has_figure === 'True') tags += '<span class="tag fig">figure</span>';
      var opts = (q.options || '').split(' | ').filter(Boolean)
        .map(function(o){ return '<div class="opt">' + esc(o) + '</div>'; }).join('');
      return '<article class="q' + (isDef(q.cat_id) ? ' defect' : '') + '">' +
        '<div class="q-head"><span class="qid">' + esc(q.question_id) + '</span>' + tags + '</div>' +
        '<p class="qtext">' + esc(q.question_text) + '</p>' +
        '<div class="opts">' + opts + '</div>' +
        '<details><summary>Trap &amp; steps</summary>' +
        '<p class="trap" style="margin-top:10px">' + esc(q.trap_mechanism) + '</p>' +
        '<ol class="steps">' + [q.step_1, q.step_2, q.step_3, q.step_4]
          .map(function(s){ return '<li>' + esc(s) + '</li>'; }).join('') + '</ol>' +
        '</details></article>';
    }).join('');
  }

  document.getElementById('chips').addEventListener('click', function(e){
    var b = e.target.closest('.chip');
    if (!b) return;
    active = b.dataset.c;
    this.querySelectorAll('.chip').forEach(function(x){
      x.setAttribute('aria-pressed', String(x.dataset.c === active));
    });
    render();
  });
  render();
})();
</script>
"""


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=rc.pp("docs", "question_categories"))
    args = ap.parse_args()

    cats = _read(os.path.join(args.dir, "categories.csv"))
    qs = _read(os.path.join(args.dir, "questions.csv"))

    # The corpus total comes from meta.json, which the builder writes from its own record set.
    # It is deliberately NOT derived by summing `count_in_corpus`: a question can carry several
    # categories (a figure question with numeric options is both C11 and C03), so that sum is a
    # tally of memberships and is larger than the number of questions.
    with open(os.path.join(args.dir, "meta.json"), encoding="utf-8") as fh:
        meta = json.load(fh)

    data = {
        "categories": cats,
        "questions": qs,
        "classified": meta["questions_classified"],
    }
    page = (_PAGE
            .replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
            .replace("__DEFECT__", json.dumps(sorted(DEFECT_CATS))))
    out = os.path.join(args.dir, "sheet.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"wrote {os.path.relpath(out, rc.pp())}  "
          f"({len(cats)} categories, {len(qs)} examples, {len(page):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
