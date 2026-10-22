#!/usr/bin/env python3
"""Per-paper review export: one CSV and one HTML page per NEET paper, for checking accuracy
against the real question paper and the real answer key.

    python3 scripts/export_paper_review.py                 # every paper found
    python3 scripts/export_paper_review.py --paper 2023     # one year

Writes `exports/review/papers/<PAPER>_REVIEW.csv` and `<PAPER>_REVIEW.html`, plus
`exports/review/papers/ALL_PAPERS.csv` across every paper.

Why this exists, and why it leads with provenance rather than content:

Accuracy cannot be judged from the extracted text alone. A stem can read perfectly and still be
the wrong question, or carry the right answer letter against the wrong option order. So every row
names, for that one question, WHICH source file the question came from, WHICH key file the answer
came from, and what the pipeline's own independent solver (step B6, which never sees the key)
concluded. A reviewer holding the real paper and the real key can then check any row end to end
without opening the pipeline.

The `agreement` column is the single most useful sort order: B6 answered blind, so a row where it
disagrees with the official key is either a misread stem, a misread option order, a wrong key, or
a genuinely hard question -- and all four are worth a human's time. Rows where it agrees are
corroborated by two independent routes and need the least attention.
"""

import argparse
import collections
import csv
import hashlib
import html
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

# Column order is deliberate: identity, then the question, then the two independent answers, then
# provenance. A reviewer reads left to right and has what they need before the long text columns.
COLUMNS = [
    "question_id", "paper", "paper_codes", "q_no", "subject", "structure",
    # merged_into names the row this one was reconciled into: the SAME question read from another
    # booklet code. A reviewer should read only the rows where it is empty -- those are the live
    # questions, one per question -- and treat the rest as the evidence of what each code printed.
    # option_order_by_code is each code's printed option numbers mapped onto this row's order,
    # which is what lets one official answer be checked against every code's key.
    "merged_into", "option_order_by_code", "repairs",
    "official_answer", "b6_answer", "agreement", "b6_confidence", "trust", "status",
    # stem_full is stem_en WITH the structured parts folded back in. 198 of this corpus's 698
    # questions are match / assertion-reason / statement types whose content lives in `list_i`,
    # `list_ii` and `statements` rather than in `stem_en` -- an earlier version of this exporter
    # emitted stem_en alone, so every one of those arrived at the reviewer looking empty or
    # truncated and a page-by-page audit reported them as "all 8 list items dropped, question
    # unanswerable". The data was never lost; the export was.
    "stem_en", "stem_full", "list_i", "list_ii", "statements",
    "option_1", "option_2", "option_3", "option_4",
    # figure_path is the repo-wide location; figure_rel is the copy beside THIS review, so a
    # reviewer who moves or uploads the folder still has working image references.
    "has_figure", "figure_path", "figure_rel", "figure_exists",
    "answer_source", "source_file", "b6_reason", "issue_reason", "review_verdict", "review_note",
]


def _dedup_key(row):
    """What makes two rows the SAME question: its text. Booklet codes cannot be used -- a row
    extracted from the E2 booklet records only its E2 position and never names its E1 twin."""
    blob = " ".join([row.get("stem_full") or row.get("stem_en") or ""]
                    + [row.get(f"option_{k}") or "" for k in "1234"])
    norm = re.sub(r"[^a-z0-9]", "", blob.lower())
    return norm[:200] if len(norm) >= 60 else f"__unique__{row.get('question_id')}"


def _paper_key(rec):
    return "_".join(str(rec.get(k) or "?") for k in ("exam", "year", "sitting"))


def _q_no(rec):
    """The printed question number, taken from the paper codes (e.g. 'E1:1' -> 1).

    Paper codes carry the number PER BOOKLET CODE, because NEET shuffles question order between
    codes. The first code's number is used for sorting, and the full list is kept in its own
    column so a reviewer checking a specific booklet can find the right number.
    """
    codes = rec.get("paper_codes") or []
    for c in codes:
        if ":" in str(c):
            tail = str(c).split(":")[-1]
            if tail.isdigit():
                return int(tail)
    return None


def _render_items(items):
    """A list of {label, text} rendered as one readable cell: '(a) AM radio waves | (b) ...'."""
    out = []
    for it in items or []:
        if isinstance(it, dict):
            lab = (it.get("label") or "").strip()
            txt = (it.get("text") or "").strip()
            out.append(f"{lab} {txt}".strip())
        else:
            out.append(str(it).strip())
    return " | ".join(x for x in out if x)


def _stem_full(rec):
    """The whole question as a reader needs it: the stem plus whatever structured parts the
    record holds. A match question's stem is often just 'Match List-I with List-II' -- useless on
    its own -- and for one record (Q-000397) the stem is empty while both lists are populated."""
    parts = [(rec.get("stem_en") or "").strip()]
    st = _render_items(rec.get("statements"))
    if st:
        parts.append(st)
    li, lii = _render_items(rec.get("list_i")), _render_items(rec.get("list_ii"))
    if li:
        parts.append("List-I: " + li)
    if lii:
        parts.append("List-II: " + lii)
    return "\n".join(p for p in parts if p)


def _row(rec):
    opts = rec.get("options_en") or {}
    fig = rec.get("figure_path")
    official = rec.get("official_answer")
    b6 = rec.get("b6_answer")
    if official in (None, "") or b6 in (None, ""):
        agreement = "not_solved"
    elif str(official) == str(b6):
        agreement = "agree"
    else:
        agreement = "DISAGREE"
    return {
        "question_id": rec.get("question_id"),
        "paper": _paper_key(rec),
        "paper_codes": "; ".join(str(c) for c in (rec.get("paper_codes") or [])),
        "q_no": _q_no(rec),
        "subject": rec.get("subject"),
        "structure": rec.get("structure"),
        "merged_into": rec.get("merged_into") or "",
        "option_order_by_code": json.dumps(rec.get("option_order_by_code"),
                                           sort_keys=True) if rec.get("option_order_by_code")
                                else "",
        # Every mechanical change ever made to this record, newest last, so a reviewer can see what
        # was repaired and on what grounds rather than having to infer it from the values.
        "repairs": " | ".join(f"{e.get('date')} {e.get('kind')}: {'; '.join(e.get('notes') or [])}"
                              for e in (rec.get("repairs") or [])),
        "official_answer": official,
        "b6_answer": b6,
        "agreement": agreement,
        "b6_confidence": rec.get("b6_confidence"),
        "trust": rec.get("trust"),
        "status": rec.get("status"),
        "stem_en": (rec.get("stem_en") or "").strip(),
        "stem_full": _stem_full(rec),
        "list_i": _render_items(rec.get("list_i")),
        "list_ii": _render_items(rec.get("list_ii")),
        "statements": _render_items(rec.get("statements")),
        "option_1": (opts.get("1") or "").strip(),
        "option_2": (opts.get("2") or "").strip(),
        "option_3": (opts.get("3") or "").strip(),
        "option_4": (opts.get("4") or "").strip(),
        "has_figure": bool(rec.get("has_figure") or fig),
        "figure_path": fig or "",
        "figure_rel": "",
        # Stated explicitly rather than left for the reviewer to discover: a figure recorded but
        # not on disk is a real defect, and silently showing a blank would hide it.
        "figure_exists": bool(fig and os.path.exists(rc.pp(fig)) or (fig and os.path.exists(fig))),
        "answer_source": rec.get("answer_source") or "",
        "source_file": rec.get("source_file") or "",
        "b6_reason": (rec.get("b6_reason") or rec.get("b6_note") or "").strip()[:400],
        "issue_reason": rec.get("issue_reason") or "",
        # Left blank on purpose: these two are for the REVIEWER to fill in, so the CSV can be
        # edited in place and handed back as the accuracy record.
        "review_verdict": "",
        "review_note": "",
    }


def _html_for(paper, rows, out_dir):
    def esc(v):
        return html.escape(str(v if v is not None else ""))

    agree = sum(1 for r in rows if r["agreement"] == "agree")
    dis = sum(1 for r in rows if r["agreement"] == "DISAGREE")
    uns = sum(1 for r in rows if r["agreement"] == "not_solved")
    solved = agree + dis
    parts = [f"""<title>{esc(paper)} review</title>
<style>
 :root {{ --ink:#1f1b16; --muted:#6b6257; --line:#ded6c8; --bad:#b3261e; --ok:#1b7a3d;
          --paper:#fffdf9; }}
 body {{ margin:0; background:var(--paper); color:var(--ink);
        font:15px/1.5 "Iowan Old Style",Georgia,serif; }}
 header {{ padding:22px 28px; border-bottom:2px solid var(--line); position:sticky; top:0;
           background:var(--paper); }}
 h1 {{ margin:0 0 6px; font-size:1.4rem; }}
 .counts {{ color:var(--muted); font-size:.92rem; }}
 .q {{ padding:18px 28px; border-bottom:1px solid var(--line); }}
 .q.disagree {{ background:#fdf2f1; border-left:4px solid var(--bad); }}
 .hd {{ display:flex; gap:12px; align-items:baseline; flex-wrap:wrap;
        font:600 .86rem/1 ui-sans-serif,system-ui; color:var(--muted); margin-bottom:8px; }}
 .verdict.DISAGREE {{ color:var(--bad); }}
 .verdict.agree {{ color:var(--ok); }}
 .stem {{ margin:0 0 10px; }}
 ol.opts {{ margin:0 0 10px 1.2em; padding:0; }}
 ol.opts li {{ margin:2px 0; }}
 ol.opts li.official {{ font-weight:700; }}
 ol.opts li.b6::after {{ content:" \\2190 B6"; color:var(--muted); font-weight:400;
                          font-size:.85em; }}
 .src {{ font:.8rem/1.45 ui-monospace,Menlo,monospace; color:var(--muted);
         background:#f6f1e7; padding:7px 10px; border-radius:3px; white-space:pre-wrap; }}
 img.fig {{ max-width:min(100%,420px); border:1px solid var(--line); display:block; margin:8px 0; }}
 .nofig {{ color:var(--bad); font-size:.85rem; }}
</style>
<header><h1>{esc(paper)} — accuracy review</h1>
<div class="counts">{len(rows)} questions &middot; B6 agrees with the official key on
<strong>{agree}</strong> of {solved} solved
({(100.0 * agree / solved if solved else 0):.1f}%) &middot;
<strong>{dis}</strong> disagree &middot; {uns} not solved.
B6 answers without ever seeing the key, so a disagreement is an independent signal, not a
duplicate of it.</div></header>"""]
    for r in rows:
        cls = "q disagree" if r["agreement"] == "DISAGREE" else "q"
        parts.append(f'<div class="{cls}" id="{esc(r["question_id"])}">')
        parts.append(
            f'<div class="hd"><span>{esc(r["question_id"])}</span>'
            f'<span>Q{esc(r["q_no"])}</span><span>{esc(r["subject"])}</span>'
            f'<span>codes: {esc(r["paper_codes"])}</span>'
            f'<span class="verdict {esc(r["agreement"])}">key={esc(r["official_answer"])} '
            f'/ B6={esc(r["b6_answer"])} &middot; {esc(r["agreement"])}</span>'
            f'<span>trust: {esc(r["trust"])}</span><span>{esc(r["status"])}</span></div>')
        stem_show = r["stem_full"] or r["stem_en"]
        parts.append('<p class="stem">'
                     + "<br>".join(esc(x) for x in stem_show.split("\n")) + '</p>')
        parts.append("<ol class=\"opts\">")
        for i in "1234":
            klass = []
            if str(r["official_answer"]) == i:
                klass.append("official")
            if str(r["b6_answer"]) == i:
                klass.append("b6")
            parts.append(f'<li class="{" ".join(klass)}">{esc(r["option_" + i])}</li>')
        parts.append("</ol>")
        if r["has_figure"]:
            if r["figure_exists"]:
                rel = r.get("figure_rel") or (
                    os.path.relpath(rc.pp(r["figure_path"]), out_dir)
                    if not os.path.isabs(r["figure_path"]) else r["figure_path"])
                parts.append(f'<img class="fig" src="{esc(rel)}" alt="figure for '
                             f'{esc(r["question_id"])}">')
            else:
                parts.append(f'<div class="nofig">figure recorded but not on disk: '
                             f'{esc(r["figure_path"])}</div>')
        if r["b6_reason"]:
            parts.append(f'<div class="src">B6 reasoning: {esc(r["b6_reason"])}</div>')
        parts.append(
            f'<div class="src">question paper: {esc(r["source_file"])}\n'
            f'answer key:     {esc(r["answer_source"])}</div>')
        parts.append("</div>")
    return "\n".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", help="substring of the paper key, e.g. 2023")
    args = ap.parse_args()

    recs = []
    rec_dir = rc.pp("papers", "records")
    for name in sorted(os.listdir(rec_dir)):
        if not name.endswith(".json"):
            continue
        with open(os.path.join(rec_dir, name), encoding="utf-8") as fh:
            recs.append(json.load(fh))

    rows = [_row(r) for r in recs]
    if args.paper:
        rows = [r for r in rows if args.paper in r["paper"]]
    rows.sort(key=lambda r: (r["paper"], r["subject"] or "", r["q_no"] or 0))

    out_dir = rc.pp("exports", "review", "papers")
    os.makedirs(out_dir, exist_ok=True)

    by_paper = collections.defaultdict(list)
    for r in rows:
        by_paper[r["paper"]].append(r)

    # Each paper gets its OWN figures folder beside its review, holding only the figures that
    # paper actually uses. The shared papers/figures/ directory covers every paper at once, so a
    # review handed to someone else -- or uploaded -- would arrive with broken images or with 69
    # files when 10 were wanted. Copying the subset keeps the CSV, the HTML and the images one
    # self-contained unit, which is how the NCERT chapter bundles already work.
    for paper, prs in by_paper.items():
        fig_dir = os.path.join(out_dir, f"{paper}_figures")
        wanted = [r for r in prs if r["has_figure"] and r["figure_exists"]]
        if not wanted:
            continue
        os.makedirs(fig_dir, exist_ok=True)
        # Deduplicated BY CONTENT. The same diagram was saved once per row, so a question read from
        # two booklet codes left two byte-identical PNGs under two question ids -- an earlier audit
        # found 6 such pairs, and after the rows were merged the second copy of each belonged to no
        # live row and read as an unreferenced or stale asset. Hashing means one file per distinct
        # image, with every row that shows it pointing at the same name.
        by_hash = {}
        for r in wanted:
            src = r["figure_path"] if os.path.isabs(r["figure_path"]) else rc.pp(r["figure_path"])
            if not os.path.exists(src):
                continue
            with open(src, "rb") as fh:
                digest = hashlib.md5(fh.read()).hexdigest()
            name = by_hash.get(digest)
            if not name:
                name = os.path.basename(src)
                by_hash[digest] = name
                shutil.copy2(src, os.path.join(fig_dir, name))
            # the HTML now points at the paper's own copy rather than the shared directory
            r["figure_rel"] = f"{paper}_figures/{name}"

    with open(os.path.join(out_dir, "ALL_PAPERS.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)

    print(f"{len(rows)} questions across {len(by_paper)} papers")
    for paper, prs in sorted(by_paper.items()):
        with open(os.path.join(out_dir, f"{paper}_REVIEW.csv"), "w", newline="",
                  encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=COLUMNS)
            w.writeheader()
            w.writerows(prs)
        with open(os.path.join(out_dir, f"{paper}_REVIEW.html"), "w", encoding="utf-8") as fh:
            fh.write(_html_for(paper, prs, out_dir))
        agree = sum(1 for r in prs if r["agreement"] == "agree")
        dis = sum(1 for r in prs if r["agreement"] == "DISAGREE")
        uns = sum(1 for r in prs if r["agreement"] == "not_solved")
        # PER DISTINCT QUESTION, not per row. NEET prints the same questions in several booklet
        # codes, and this corpus holds more than one code per paper as separate rows -- 2023 is
        # 299 rows covering 191 distinct questions. A per-row agreement rate therefore counts some
        # questions twice and is not an accuracy figure at all: reported per row, 2023 reads
        # 171/199 = 85.9%, but per distinct question it is 147/170. The per-row number is kept
        # alongside it so the difference is visible rather than hidden.
        # The live rows are the ones scripts/merge_paper_codes.py did NOT mark `merged_into`: one
        # row per question, with every code it was printed in listed in paper_codes. Preferred over
        # re-deriving the grouping from the text here, because the merge used the option SET (order
        # is a property of the code) and recorded its reasoning in each record's `repairs`, so two
        # different groupings in one repo would be a second source of truth. The text key is still
        # the fallback for a record the merge could not group at all.
        live = [r for r in prs if not r.get("merged_into")]
        dq = {}
        for r in live:
            dq.setdefault(_dedup_key(r), r)
        d_agree = sum(1 for r in dq.values() if r["agreement"] == "agree")
        d_dis = sum(1 for r in dq.values() if r["agreement"] == "DISAGREE")
        figs = sum(1 for r in prs if r["has_figure"])
        figs_missing = sum(1 for r in prs if r["has_figure"] and not r["figure_exists"])
        solved = agree + dis
        d_solved = d_agree + d_dis
        print(f"  {paper}: {len(prs)} rows / {len(dq)} distinct questions")
        print(f"      per distinct question: agree {d_agree}/{d_solved}"
              f" ({(100.0 * d_agree / d_solved if d_solved else 0):.1f}%)"
              f"  <-- the accuracy figure")
        print(f"      per row (inflated by duplicates): {agree}/{solved}"
              f" ({(100.0 * agree / solved if solved else 0):.1f}%)"
              f" | disagree {dis} | not solved {uns}")
        print(f"      figures {figs} ({figs_missing} missing on disk)")
    print(f"wrote {os.path.relpath(out_dir, rc.pp())}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
