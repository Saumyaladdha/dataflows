#!/usr/bin/env python3
"""Every agent step of ONE chapter, listed and checked from the chapter PDF alone.

    python code/chapter_steps.py prepare PHY11L-ch01 [--pdf "C:/.../Chapter_1.pdf"]
    python code/chapter_steps.py list  A2  PHY11L-ch01
    python code/chapter_steps.py check A2  PHY11L-ch01
    python code/chapter_steps.py status PHY11L-ch01

Steps: A2 (page text), A2S (tables, equations, figures), A2L (printed layout), FIGP (physics
figures we draw ourselves), A3 (passages), A4 (subtopics). `list` and `check` print one work item
per line in run_step's format -- `item | agent | input | output | run` -- so a dispatcher (the
saved workflow `.claude/workflows/ncert-chapter-pipeline.js`) can hand each line to one agent.
`check` prints the items that still need an agent (retries) and ends with `DONE <STEP> ...` when
none do.

WHY THIS EXISTS. `run_step.py` walks the whole corpus and assumes its intermediate files are on
disk: A2's work inputs, `ncert/blocks/<BOOK>.jsonl`, an A2 status for every page. On a fresh
chapter none of them are, so `--list` printed "No books registered yet" (A2), "none found" (A2S,
A3) or crashed (A2L), and every chapter so far went through these steps by hand-made workarounds.
PHY11L-ch01 was built twice with only A2 run -- 0 equations transcribed, 0/12 pages measured, no
passages -- and every display equation on pages 5-11 came out garbled. This driver rebuilds what
each step needs from the PDF and the earlier steps' outputs, scoped to one chapter, and reuses
the plugins' own input builders and the step checks unchanged.
"""

import argparse
import glob
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import runner_core as rc        # noqa: E402
import step_plugins as sp       # noqa: E402
from lib import io as lib_io    # noqa: E402
from lib import pdf as lib_pdf  # noqa: E402

SUBJECT_DIR = {"BIO": "biology", "CHE": "chemistry", "PHY": "physics"}
FIGP_AGENT = "figp-figure-redrawer"
STRUCTURE_RUN = "tree"


def parse_cid(cid):
    import re
    m = re.fullmatch(r"(([A-Z]{3})(\d{2})([LO]))-ch(\d+)", cid)
    if not m:
        raise SystemExit(f"bad chapter id {cid!r}; expected like PHY11L-ch01")
    return m.group(1), m.group(2), int(m.group(3)), m.group(4), int(m.group(5))


def chapter_pdf(cid):
    _book, subj, klass, ed, num = parse_cid(cid)
    return os.path.join(ROOT, "source_pdfs", "new" if ed == "L" else "old", f"class_{klass}",
                        SUBJECT_DIR[subj], f"Chapter_{num}.pdf")


def emit(lines):
    for ll in lines:
        print(sp.format_list_line(ll))


def best_out(step, item_id):
    """(run_label, path) of the newest output for an item: retry1 outranks runA."""
    for run in ("retry1", "runA"):
        p = sp._out_path(step, item_id, run)
        if os.path.exists(p):
            return run, p
    return None, None


# ---------------------------------------------------------------- prepare -------------------
def prepare(cid, pdf=None):
    """Put the PDF where the build reads it, refuse a PDF with no text layer, build every page's
    A2 input, and rebuild this chapter's `ncert/blocks` records from the A2 reads on disk."""
    book, subj, klass, ed, num = parse_cid(cid)
    dest = chapter_pdf(cid)
    if pdf:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        if os.path.abspath(pdf) != os.path.abspath(dest):
            shutil.copyfile(pdf, dest)
    if not os.path.exists(dest):
        raise SystemExit(f"{cid}: no PDF at {os.path.relpath(dest, ROOT)} -- pass --pdf")
    import fitz
    doc = fitz.open(dest)
    empty = [i + 1 for i, p in enumerate(doc) if not p.get_text().strip()]
    # A "Microsoft: Print To PDF" copy has no text layer at all and wrecks every measurement
    # (BIO12L ch01, LESSONS 15). An opener page with only art may be empty; most pages may not.
    if len(empty) > max(1, doc.page_count // 4):
        raise SystemExit(f"{cid}: {len(empty)}/{doc.page_count} pages have no text layer -- this "
                         f"is a printed copy, not the official NCERT PDF")
    books = lib_io.read_csv(rc.pp("register", "books.csv"))
    if not any(r.get("book_id") == book for r in books):
        raise SystemExit(f"{cid}: {book} is not in register/books.csv (run A1 for the book first)")
    a2 = sp.A2Plugin()
    made = 0
    for p in range(1, doc.page_count + 1):
        item = a2._item_id(book, num, p)
        path = sp._work_input_path("A2", item, "runA")
        if not os.path.exists(path):
            sp._write_json(path, a2._build_input(book, num, dest, p))
            made += 1
    n_blocks = sync_blocks(cid)
    print(f"prepared {cid}: {doc.page_count} pages, {made} A2 input(s) built, {n_blocks} A2 "
          f"block(s) in ncert/blocks/{book}.jsonl; pdf {os.path.relpath(dest, ROOT)}")


def chapter_pages(cid):
    book, _s, _k, _e, num = parse_cid(cid)
    return [sp.A2Plugin._item_id(book, num, p) for p in range(1, lib_pdf.page_count(chapter_pdf(cid)) + 1)]


def sync_blocks(cid):
    """Rewrite this chapter's records in ncert/blocks/<BOOK>.jsonl from the A2 reads that passed.

    A2's `_post_assembly` APPENDS when a page first passes, so a page read before the blocks file
    existed (every PHY11L page) never reached it, and a re-read page would be there twice. A2S and
    A2L read their work from this file, so the chapter's records are replaced wholesale."""
    book, _s, _k, _e, num = parse_cid(cid)
    path = rc.pp("ncert", "blocks", f"{book}.jsonl")
    keep = [r for r in (lib_io.read_jsonl(path) if os.path.exists(path) else [])
            if r.get("chapter_num") != num]
    n = 0
    for item in chapter_pages(cid):
        st = rc.read_item_status("A2", item) or {}
        if st.get("status") not in ("pass", "flagged"):
            continue
        run = st.get("run") or "runA"
        data = sp._read_json(sp._out_path("A2", item, run)) if os.path.exists(
            sp._out_path("A2", item, run)) else None
        if not isinstance(data, dict) or not data.get("blocks"):
            continue
        page = int(item.rsplit("-p", 1)[1])
        for b in data["blocks"]:
            rec = dict(b)
            rec.update(book_id=book, chapter_num=num, page=f"{page:03d}")
            keep.append(rec)
            n += 1
        last = data["blocks"][-1]
        sp._write_json(rc.pp("steps", "A2", "status", f"{item}.last_block.json"),
                       {"kind": last.get("kind"), "text_tail": (last.get("text") or "")[-100:]})
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        for r in keep:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    sp.A2SPlugin._page_blocks_cache = None
    return n


# ---------------------------------------------------------------- A2 ------------------------
def list_a2(cid):
    lines = []
    for item in chapter_pages(cid):
        st = rc.read_item_status("A2", item)
        if st and st.get("status") in ("pass", "flagged", "blocked"):
            continue
        run, _ = best_out("A2", item)
        if run or rc.read_pending("A2", item):
            continue
        lines.append(sp.ListLine(item, "a2-page-reader",
                                 sp._relpath(sp._work_input_path("A2", item, "runA")),
                                 sp._relpath(sp._out_path("A2", item, "runA")), "runA"))
    return lines


def check_a2(cid):
    inputs = {}
    for item in chapter_pages(cid):
        p = sp._work_input_path("A2", item, "runA")
        if os.path.exists(p):
            inputs[item] = sp._read_json(p)
    lines = sp.resolve_single_run_items("A2", sp.get_cfg("A2"), "a2-page-reader", inputs, {},
                                        lambda *a: None)
    sync_blocks(cid)
    return lines


# ---------------------------------------------------------------- A2S -----------------------
def list_a2s(cid):
    sync_blocks(cid)
    lines = sp.A2SPlugin().list_items({"chapters": [cid + "-"]})
    # An input with no crop makes every agent correctly answer {"error": ...} -- a whole wasted
    # round on BIO12L ch07-10 (2026-10-27). Refuse to hand those out.
    blind = [ll.item_id for ll in lines
             if not (sp._read_json(os.path.join(ROOT, ll.input_path)) or {}).get("image")]
    if blind:
        raise SystemExit(f"A2S inputs without a crop image: {blind}")
    return lines


def check_a2s(cid):
    pending = {k: v for k, v in sp.A2SPlugin()._pending_special_blocks().items()
               if k.startswith(cid + "-")}
    inputs = {}
    for item in pending:
        for run in ("retry1", "runA"):
            p = sp._work_input_path("A2S", item, run)
            if os.path.exists(p):
                inputs[item] = sp._read_json(p)
                break
    return sp.resolve_single_run_items("A2S", sp.get_cfg("A2S"), "a2-special-transcriber",
                                       inputs, {}, lambda *a: None)


# ---------------------------------------------------------------- A2L -----------------------
def list_a2l(cid):
    import book_design
    if not book_design.a2l_join(parse_cid(cid)[0]):
        return []                      # the build does not take A2L for this book: no agents
    return sp.A2LPlugin().list_items({"chapters": [cid + "-"]})


def check_a2l(cid):
    import book_design
    if not book_design.a2l_join(parse_cid(cid)[0]):
        return []
    return sp.A2LPlugin().check({"chapters": [cid + "-"]})


# ---------------------------------------------------------------- FIGP ----------------------
def _chapter_doc(cid):
    import cdn_publish
    cdir = cdn_publish.chapter_dir(cid)
    path = os.path.join(cdir, "chapter.json")
    if not os.path.exists(path):
        raise SystemExit(f"{cid}: no chapter.json yet -- build the chapter before FIGP/A3/A4")
    with open(path, encoding="utf-8") as fh:
        return cdir, json.load(fh)


def _figures(doc):
    out = []

    def rec(ns):
        for n in ns:
            if n.get("kind") == "figure" and n.get("image_local"):
                out.append(n)
            rec(n.get("children") or [])
    rec(doc["tree"])
    return out


def figp_item(cid, image_local):
    return f"{cid}-{os.path.splitext(os.path.basename(image_local))[0]}"


def _bridge(*args):
    """lib/physics_figure, figure_text, print_trace and spec_trace live in paper_extraction, whose
    package is also called `lib` -- so they run in their own process (code/figp_bridge.py)."""
    r = subprocess.run([sys.executable, os.path.join(HERE, "figp_bridge.py"), *args],
                       capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
    if r.returncode:
        raise SystemExit(f"figp_bridge {args[0]} failed: {(r.stderr or r.stdout)[-800:]}")
    return json.loads(r.stdout.strip().splitlines()[-1])


def list_figp(cid):
    """One item per figure of a PHYSICS chapter that the PDF draws as vector art.

    A photograph or a raster scan has no geometry to check a spec against, and the brief rules
    pictorial figures out of scope anyway, so only figures with vector strokes inside their box
    are queued -- each a figure we can redraw and prove against the print."""
    _book, subj, _k, _e, _n = parse_cid(cid)
    if subj != "PHY":
        return []
    cdir, doc = _chapter_doc(cid)
    pdf = chapter_pdf(cid)
    work = rc.pp("steps", "FIGP", "work")
    os.makedirs(work, exist_ok=True)
    lines = []
    for fig in _figures(doc):
        item = figp_item(cid, fig["image_local"])
        st = rc.read_item_status("FIGP", item)
        if st and st.get("status") in ("pass", "flagged", "blocked"):
            continue
        if best_out("FIGP", item)[0] or rc.read_pending("FIGP", item):
            continue
        page = int(fig.get("page_file") or fig["pages"][0])
        crop = os.path.join(work, f"{item}.png")
        shutil.copyfile(os.path.join(cdir, fig["image_local"]), crop)
        probe = _bridge("probe", pdf, str(page - 1), json.dumps(fig["image_bbox"]))
        if probe["strokes"] < 3:
            continue
        inp = {"item_id": item, "image": sp._relpath(crop), "caption": fig.get("caption") or "",
               "figure_number": fig.get("number"), "printed_text": probe["printed_text"],
               "source_pdf": sp._relpath(pdf), "page_index": page - 1,
               "bbox_frac": fig["image_bbox"]}
        sp._write_json(sp._work_input_path("FIGP", item, "runA"), inp)
        lines.append(sp.ListLine(item, FIGP_AGENT, sp._relpath(sp._work_input_path("FIGP", item, "runA")),
                                 sp._relpath(sp._out_path("FIGP", item, "runA")), "runA"))
    return lines


def check_figp(cid):
    """Check each written spec (figp_bridge `check`: renders, angles, netlist, every printed word,
    and line-for-line agreement with the print), draw the passing ones to steps/FIGP/drawn/, and
    queue one retry carrying the previous output and what failed."""
    lines = []
    pv = rc.get_prompt_version("FIGP")
    drawn_dir = rc.pp("steps", "FIGP", "drawn")
    os.makedirs(drawn_dir, exist_ok=True)
    for inp_path in sorted(glob.glob(rc.pp("steps", "FIGP", "work", f"{cid}-*.runA.input.json"))):
        item = os.path.basename(inp_path)[:-len(".runA.input.json")]
        st = rc.read_item_status("FIGP", item)
        if st and st.get("status") in ("pass", "flagged"):
            continue
        run, out = best_out("FIGP", item)
        if not run:
            continue
        res = _bridge("check", inp_path, out, os.path.join(drawn_dir, f"{item}.svg"))
        if res["ok"]:
            rc.write_item_status("FIGP", item, "pass", pv,
                                 extra={"run": run, "check_message": res["msg"],
                                        "layout": res.get("layout"), "svg": sp._relpath(
                                            os.path.join(drawn_dir, f"{item}.svg"))
                                        if res.get("drawn") else None})
            rc.clear_pending("FIGP", item)
            continue
        if run == "runA":
            retry = dict(sp._read_json(inp_path))
            retry["PREVIOUS OUTPUT"] = sp._read_json(out)
            retry["PREVIOUS ATTEMPT FAILED"] = res["msg"]
            sp._write_json(sp._work_input_path("FIGP", item, "retry1"), retry)
            rc.write_pending("FIGP", item, {"reason": res["msg"], "next_run": "retry1"})
            lines.append(sp.ListLine(item, FIGP_AGENT, sp._relpath(sp._work_input_path("FIGP", item, "retry1")),
                                     sp._relpath(sp._out_path("FIGP", item, "retry1")), "retry1"))
        else:
            # Still wrong after the retry: the chapter keeps the printed crop for this figure.
            rc.write_item_status("FIGP", item, "flagged", pv,
                                 extra={"run": run, "check_message": res["msg"]})
    return lines


# ---------------------------------------------------------------- A3 / A4 -------------------
def _structure_status(step, item, ok, msg):
    rc.write_item_status(step, item, "pass" if ok else "pending", rc.get_prompt_version(step),
                         extra={"run": STRUCTURE_RUN, "check_message": msg})


def list_a3(cid):
    import structure_inputs
    lines = []
    for item, inp, out in structure_inputs.write_a3(cid):
        if os.path.exists(out) and _a3_ok(inp, out)[0]:
            continue
        lines.append(sp.ListLine(item, "a3-passage-splitter", sp._relpath(inp), sp._relpath(out),
                                 STRUCTURE_RUN))
    return lines


def _a3_ok(inp, out):
    data = sp._read_json(out)
    if not isinstance(data, dict) or "error" in data:
        return False, "missing or error output"
    # The check must get the input WRAPPED, or it passes vacuously (LESSONS / acceptance notes).
    return rc.run_step_check("A3", data, {"input_data": sp._read_json(inp)})


def check_a3(cid):
    """A3 outputs are matched to the tree by fingerprint, so a stale output (one whose section no
    longer has the same blocks) is simply re-listed; there is no retry file -- the re-dispatch
    reads the same fresh input."""
    lines = []
    for ll in list_a3(cid):
        out = os.path.join(ROOT, ll.output_path)
        if os.path.exists(out):
            ok, msg = _a3_ok(os.path.join(ROOT, ll.input_path), out)
            _structure_status("A3", ll.item_id, ok, msg)
            if not ok:
                os.replace(out, out + ".failed")
                print(f"# A3 {ll.item_id} failed its check: {msg[:300]}")
        lines.append(ll)
    return lines


def list_a4(cid):
    import structure_inputs
    inp, out = structure_inputs.write_a4(cid)
    if os.path.exists(out):
        data = sp._read_json(out)
        ok, _msg = rc.run_step_check("A4", data, {"input_data": sp._read_json(inp)})
        if ok:
            return []
    item = os.path.basename(inp)[:-len(f".{STRUCTURE_RUN}.input.json")]
    return [sp.ListLine(item, "a4-subtopic-writer", sp._relpath(inp), sp._relpath(out), STRUCTURE_RUN)]


def check_a4(cid):
    import structure_inputs
    inp, out = structure_inputs.write_a4(cid)
    if not os.path.exists(out):
        return list_a4(cid)
    ok, msg = rc.run_step_check("A4", sp._read_json(out), {"input_data": sp._read_json(inp)})
    item = os.path.basename(inp)[:-len(f".{STRUCTURE_RUN}.input.json")]
    _structure_status("A4", item, ok, msg)
    if ok:
        return []
    os.replace(out, out + ".failed")
    print(f"# A4 {item} failed its check: {msg[:300]}")
    return list_a4(cid)


STEPS = {
    "A2": (list_a2, check_a2), "A2S": (list_a2s, check_a2s), "A2L": (list_a2l, check_a2l),
    "FIGP": (list_figp, check_figp), "A3": (list_a3, check_a3), "A4": (list_a4, check_a4),
}


def status(cid):
    pages = chapter_pages(cid)
    a2 = [rc.read_item_status("A2", p) or {} for p in pages]
    print(f"{cid}: {len(pages)} pages")
    print(f"  A2   {sum(s.get('status') == 'pass' for s in a2)} pass, "
          f"{sum(s.get('status') == 'flagged' for s in a2)} flagged, "
          f"{sum(not s for s in a2)} unresolved")
    for step in ("A2S", "A2L", "FIGP"):
        outs = glob.glob(rc.pp("steps", step, "out", f"{cid}-*.json"))
        print(f"  {step:<4} {len(outs)} output(s)")
    print(f"  A3   {len(glob.glob(rc.pp('steps', 'A3', 'out', f'{cid}-s*.{STRUCTURE_RUN}.json')))} section output(s)")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("verb", choices=["prepare", "list", "check", "status"])
    ap.add_argument("args", nargs="+")
    ap.add_argument("--pdf")
    a = ap.parse_args()
    if a.verb == "prepare":
        return prepare(a.args[0], a.pdf)
    if a.verb == "status":
        return status(a.args[0])
    step, cid = a.args[0].upper(), a.args[1]
    if step not in STEPS:
        raise SystemExit(f"unknown step {step}; one of {sorted(STEPS)}")
    lister, checker = STEPS[step]
    lines = (lister if a.verb == "list" else checker)(cid)
    emit(lines)
    if a.verb == "check" and not lines:
        print(f"DONE {step} {cid}")
    elif a.verb == "list" and not lines:
        print(f"# {step} {cid}: nothing to dispatch")


if __name__ == "__main__":
    main()
