"""One plugin per step in config/steps.yaml: S0, A1-A9, B1-B9, C1, D1-D11, E0-E6, F1-F6 -- every
step the config declares now has one, so `run_step.py <STEP>` works for all of them. Each plugin
exposes up to three methods, called by run_step.py:

  list_items(filters)  -> list[ListLine]   # fresh items only; agent-driven/hybrid steps
  check(filters)        -> list[ListLine] or []   # resolves outstanding runs; [] means nothing
                                                     # left pending from this call (run_step.py
                                                     # decides DONE vs not by also checking
                                                     # whether list_items is now empty)
  auto(filters)         -> None             # script-only / hybrid steps: invoke the real script

A plugin that has no agent at all (S0, A7, A9, D10, F1, F3-F6) implements only auto()+check();
list_items() returns [] with a human-readable reason (run_step.py prints the "script-only"
message using that reason). A hybrid plugin (A5, A6, D3, E1, E6) implements all three. F2 is the
one PEOPLE step: it implements list_items()+list_reason()+check() and deliberately NO auto(),
because people do that step and the runner must say so rather than pretend to run it.

Shared conventions (see docs/CONVENTIONS... actually scripts/CONVENTIONS.md for --auto; this
docstring covers --list/--check):
  - work input file:  steps/<STEP>/work/<item_id>.<run_label>.input.json
  - agent output file: steps/<STEP>/out/<item_id>.<run_label>.json
  - run_label in {"runA", "runB", "retry1", "adjudicated"} (folder layout note, spec 5.8) --
    for a 1-run step the (only) run is still called "runA", not "run1"; see docs/OPEN_QUESTIONS.md.
  - a failing check()'s message (scripts/checks/<STEP>.py) is "; "-joined segments, each
    optionally "<FLAG_CODE>: <detail>" using a code from that step's config/steps.yaml `flags`
    map -- see runner_core.parse_check_message.
"""
import collections
import contextlib
import os
import re
import subprocess
import sys

try:
    import fcntl
    _HAS_FCNTL = True
except ImportError:  # pragma: no cover - non-POSIX fallback
    _HAS_FCNTL = False

import runner_core as rc
import pair_passages  # C1 reuses its pure Jaccard/Hungarian matching functions (word_trigrams,
                        # jaccard, _solve_assignment) for cross-booklet-code shortlisting -- see
                        # C1Plugin. Safe to share despite pair_passages.py's own `from scripts.lib
                        # import ...` imports resolving to separate module objects than this
                        # file's `from lib import ...` ones (two names for the same file) --
                        # C1Plugin only calls pair_passages' pure, I/O-free functions, never the
                        # ones that touch lib_io/lib_flags, so the duplicate-module-instance risk
                        # that would matter for monkeypatched tests (see tests/test_run_step.py)
                        # never actually applies here.
import fetch_passages  # D3 (step_plugins.D3Plugin) calls fetch_passages.fetch_for_item() directly,
                        # in-process, for its own D2-retry re-fetch (spec 12/D3 On failure) rather
                        # than shelling out to `--auto` a second time mid-check(). Same dual-import
                        # -path quirk as pair_passages above (fetch_passages.py's own `from
                        # scripts.lib import ...` vs this file's `from lib import ...`), but SAFE
                        # here even though fetch_for_item is NOT pure I/O-free: lib_io/lib_records
                        # have no meaningful in-memory state (no caches, no locks that matter across
                        # the two module instances) -- both names resolve to the exact same
                        # PROJECT_ROOT and therefore the exact same files on disk, so two separate
                        # module objects reading/writing those files is equivalent to one.
import build_groups  # D10 (step_plugins.D10Plugin) asks it which subtopics have D9-resolved work
                      # (subtopics_with_work()) so the runner and the script can never disagree
                      # about what exists; the actual group building is still a `--auto`
                      # SUBPROCESS call, per scripts/CONVENTIONS.md. Same dual-import-path quirk
                      # as fetch_passages/pair_passages below, and safe for the same reason (no
                      # in-memory state that matters across the two module objects; both resolve
                      # to the same PROJECT_ROOT and therefore the same files on disk).
import codebook_version  # spec 13.0's codebook_version: ONE hash formula in the repo, in one
                          # place. _d_codebook() (D4/D11) and _e_codebook() (E1-E6) both delegate
                          # to codebook_version.load(), and scripts/checks/E4.py recomputes the
                          # same value to catch a codebook that never reached its agent -- which
                          # only works because there is a single formula to agree with. The module
                          # imports nothing but runner_core, so this is cheap.
import qmap_plugins  # QSUBJ/QCHAP/QTOPIC: the question-mapping chain
import b6v_plugin  # B6V's plugin: solve one v2 question with no key
import b3v_plugin  # B3V's plugin: read one v2 question from its image
import e7v_plugin  # E7V's plugin: band one v2 question by the work it takes
import qca_plugin  # QCA's plugin: the concept and approach of a physics/phys-chem question
import b3f_plugin  # B3F's plugin: one item per figure crop of the v2 paper corpus
import ecat_plugin  # ECAT's plugin: grouped category rating over pre-built packets
import describe_tags  # E6's SCRIPT half (spec 13/E6): the five descriptive fields outright, and
                       # `stem_context` by pattern, with `stem_context: None` as the designed
                       # trigger for an e6-context-tagger call. Also the project's one option-shape
                       # classifier (answer_form), reused by E2's negative-word guard and E5's
                       # partial_combination rule rather than copied.
import e0_category_sheet  # E0's step-3 SCRIPT (the category sheet) and, more importantly here,
                           # its documented sample floor -- E0Plugin refuses to dispatch below the
                           # same numbers rather than keeping a second copy of them.
import legacy_match  # assert_no_legacy: spec Section 13's "the legacy fields are never inputs to
                      # any agent", as a precondition in code. Every E work-input file goes through
                      # _e_write_agent_input(), which calls it first.
import tag_values  # Stage E's single reader of config/allowed_values.yaml (spec 17). Nothing in
                    # this file types a tag value or a value list.
import type_patterns  # E1's SCRIPT half (spec 13/E1): 16 patterns in spec's priority order, first
                       # match wins; classify() -> (None, reason) is the designed trigger for an
                       # e1-type-tagger call.
import recover_figures  # B9 (step_plugins.B9Plugin) calls its shortlist_and_fetch()/attach_figure()
import split_figures  # B10 (step_plugins.B10Plugin) calls its candidates()/crop_panels()
                        # in-process -- same precedent and same dual-import-path quirk as
                        # fetch_passages above, and safe for the same reason (no in-memory state
                        # that matters across the two module objects; both resolve to the same
                        # PROJECT_ROOT and therefore the same files on disk). recover_figures is
                        # the ONLY place in this codebase that reads inputs/legacy_sheets/, and it
                        # reads only the Question/Year/Subject/"Class NEET" columns -- never the
                        # sheets' Chapter Name / Chapter No / Topic / Question Type / Answer
                        # judgement columns (CLAUDE.md), enforced in its own _row_cells().
from lib import coaching_guard  # noqa: F401  (imported so a future plugin can wire it in; A1-A9 don't need it)
from lib import ids as lib_ids
from lib import io as lib_io
from lib import latex_normalise
from lib import option_parser
from lib import pdf as lib_pdf
from lib import quote_verify
from lib import records as lib_records
from lib import scrape_sanitize
from lib import search_index
from lib import sittings
from lib import text_normalise

ListLine = collections.namedtuple("ListLine", ["item_id", "agent", "input_path", "output_path", "run_label"])


def format_list_line(ll):
    return f"{ll.item_id} | {ll.agent} | {ll.input_path} | {ll.output_path} | {ll.run_label}"


def _relpath(abspath):
    return os.path.relpath(abspath, rc.pp())


def _work_input_path(step, item_id, run_label):
    return rc.pp("steps", step, "work", f"{item_id}.{run_label}.input.json")


def _out_path(step, item_id, run_label):
    return rc.pp("steps", step, "out", f"{item_id}.{run_label}.json")


def _write_json(path, obj):
    rc.ensure_dir(os.path.dirname(path))
    lib_io.atomic_write_json(path, obj)


def _read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        import json
        return json.load(f)


def _list_out_files(step):
    out_dir = rc.pp("steps", step, "out")
    if not os.path.isdir(out_dir):
        return []
    return sorted(f for f in os.listdir(out_dir) if f.endswith(".json"))


def _parse_out_filename(fn):
    """'<item_id>.<run_label>.json' -> (item_id, run_label), or None if `fn` does not have that
    shape. item_id schemes in this build never contain '.', so a plain rsplit is normally safe --
    but an agent dispatched with an explicit 'output: steps/<STEP>/out/<ID>.runA.json' instruction
    has still, on real data, written '<ID>.json' instead (missing the run label entirely). Before
    this returned None, a single such file crashed `_outputs_by_item` with an unpacking
    ValueError, which is called at the TOP of resolve_single_run_items -- so one agent's filename
    slip on ONE item silently broke `--check` for every item of that step, across every chapter,
    until someone happened to run it and saw the traceback. Returning None here and skipping the
    file in `_outputs_by_item` (with a loud stderr warning so the stray file is not invisible)
    turns that from a hard stop into a non-event for every item that IS named correctly."""
    stem = fn[:-len(".json")]
    if "." not in stem:
        return None
    item_id, run_label = stem.rsplit(".", 1)
    return item_id, run_label


@contextlib.contextmanager
def _locked_file(lock_path):
    """Hold an exclusive OS lock on a sidecar .lock file for the duration of the block -- same
    pattern as lib/ids.py's _locked_counters_file, used here by B3Plugin's (paper_id, qno) ->
    question_id index so two concurrent --check calls can never mint two different Q-IDs for the
    same real question (the ID itself is already race-safe via lib_ids' own counter lock; this
    additionally protects the index file that remembers which ID a question already got, so a
    rerun is idempotent rather than silently minting a second ID for the same question)."""
    rc.ensure_dir(os.path.dirname(lock_path))
    f = open(lock_path, "a+")
    try:
        if _HAS_FCNTL:
            fcntl.flock(f, fcntl.LOCK_EX)
        yield
    finally:
        if _HAS_FCNTL:
            fcntl.flock(f, fcntl.LOCK_UN)
        f.close()


# ===========================================================================
# Generic single-run retry-chain resolver, shared by A1, A2S, A3 (and A2's per-page half).
# ===========================================================================

_RUN_ORDER = {"runA": 0, "retry1": 1}


def _outputs_by_item(step):
    """{item_id: {run_label: filename}} for every file currently in steps/<STEP>/out/.

    A malformed filename (missing its run label, e.g. an agent wrote 'p001.json' instead of the
    instructed 'p001.runA.json') is skipped, not fatal -- see _parse_out_filename's docstring for
    why a hard crash here is worse than a loud warning. The file stays on disk, unresolved, until
    a person renames it or the item is re-dispatched; everything else in the step keeps working."""
    out = collections.defaultdict(dict)
    for fn in _list_out_files(step):
        parsed = _parse_out_filename(fn)
        if parsed is None:
            print(f"WARNING [{step}]: skipping malformed output filename "
                  f"{os.path.join('steps', step, 'out', fn)!r} (expected '<item_id>.<run_label>.json')",
                  file=sys.stderr)
            continue
        item_id, run_label = parsed
        out[item_id][run_label] = fn
    return out


def resolve_single_run_items(step, cfg, agent_name, item_ids_with_builders, check_context_extra,
                              post_assembly, always_flag_codes=None, agent_inputs=None):
    """Drive the retry-once chain (spec 5.5, used by steps whose fallback is just ["retry"] or
    starts with it) for every item in `item_ids_with_builders`: {item_id: input_dict}.

    For each item already resolved (status file exists with current prompt_version and status !=
    stale), does nothing. Otherwise looks at its newest output file (retry1 if present, else
    runA); if none exists yet, does nothing this round (still waiting on the agent). Returns the
    list of new ListLines to work next (retry1 calls), and writes status/flags/run_log for any
    item that reaches a terminal resolution this round.

    `item_ids_with_builders[item_id]` serves two different purposes for steps whose per-item check
    needs context the AGENT never sees: it is both the check's `context["input_data"]` and, by
    default, the body of the retry work-input file. For A1/A2S/A3 those two really are the same
    dict. They are NOT for D4 (whose check context is {passages: {id: text}, structure,
    statements, answer_to_support} while the agent's own input is {question, answer_to_support,
    passages: [{id, text}], codebook}) or for D5/D8/D9 built the same way.

    REAL BUG this parameter fixes (found while building D5-D11, 2026-10-12, never triggered on
    real data because D4 has never been dispatched for real): without it, a D4 retry -- the one
    fallback rung spec 12/D4 names by name, for exactly the "quote not found" case that is D4's
    most likely failure -- wrote the CHECK CONTEXT to steps/D4/work/<QID>.retry1.input.json and
    handed the agent an input with no `question` field at all, `passages` as an id->text mapping
    instead of the list of {id, text} its agent file documents, and no `codebook`. Pass
    `agent_inputs={item_id: <the real agent input dict>}` and the retry file is built from that
    instead; omit it and behaviour is exactly as before.
    """
    prompt_version = rc.get_prompt_version(step)
    fallback = cfg.get("fallback") or []
    flags_catalogue = cfg.get("flags") or {}
    always_flag_codes = always_flag_codes or []
    outputs = _outputs_by_item(step)
    new_lines = []

    for item_id, build_input in item_ids_with_builders.items():
        existing_status = rc.read_item_status(step, item_id)
        if existing_status and existing_status.get("status") != "stale" \
                and existing_status.get("prompt_version") == prompt_version:
            continue  # already resolved for this prompt version

        runs_here = outputs.get(item_id, {})
        if "retry1" in runs_here:
            run_label, fn = "retry1", runs_here["retry1"]
        elif "runA" in runs_here:
            run_label, fn = "runA", runs_here["runA"]
        else:
            continue  # nothing written yet; still waiting

        data = _read_json(_out_path(step, item_id, run_label))
        started = rc.now_iso()
        if isinstance(data, dict) and "error" in data:
            ok, msg = False, f"agent reported error: {data['error']}"
        else:
            ok_schema, schema_msg = rc.validate_schema(step, data)
            if not ok_schema:
                ok, msg = False, schema_msg
            else:
                context = {"item_id": item_id, "step": step, "input_data": build_input,
                            "project_root": rc.pp()}
                context.update(check_context_extra or {})
                ok, msg = rc.run_step_check(step, data, context)
        ended = rc.now_iso()

        if ok:
            status = "pass"
            for code in always_flag_codes:
                rc.raise_flag("item", item_id, step, code, flags_catalogue.get(code, "low"),
                               "every item of this step gets this flag", provisional_value=data,
                               prompt_version=prompt_version)
            post_assembly(item_id, run_label, data, status)
            rc.write_item_status(step, item_id, status, prompt_version,
                                   extra={"run": run_label, "check_message": msg})
            rc.append_run_log(item_id, step, run_label, agent_name, prompt_version, started,
                                ended, "pass", msg, None, status)
            continue

        if run_label == "runA" and "retry" in fallback:
            rc.append_run_log(item_id, step, run_label, agent_name, prompt_version, started,
                                ended, "fail", msg, None, "pending")
            rc.write_pending(step, item_id, {"reason": msg, "next_run": "retry1"})
            retry_input = dict((agent_inputs or {}).get(item_id) or build_input)
            retry_input["previous_attempt_failed"] = msg
            _write_json(_work_input_path(step, item_id, "retry1"), retry_input)
            new_lines.append(ListLine(item_id, agent_name, _relpath(_work_input_path(step, item_id, "retry1")),
                                        _relpath(_out_path(step, item_id, "retry1")), "retry1"))
            continue

        # Retry exhausted (or no retry in this step's chain): resolve via safe_default/flags.
        segments = rc.parse_check_message(cfg, msg)
        resolved_data = dict(data) if isinstance(data, dict) and "error" not in data else {}
        safe_default = cfg.get("safe_default")
        blocked = False
        for code, detail in segments:
            severity = flags_catalogue.get(code, "normal") if code else "normal"
            flag_code = code or f"{step}_CHECK_FAILED"
            if isinstance(safe_default, dict) and code:
                # field-level default keyed by a lowercased guess of the flag's subject; plugins
                # that need a specific mapping pass it via post_assembly instead, so this is best
                # effort only (covers A1's reprint/edition fields, see checks/A1.py).
                pass
            rc.raise_flag("item", item_id, step, flag_code, severity,
                           detail or msg, provisional_value=resolved_data,
                           prompt_version=prompt_version)
            if safe_default is None:
                blocked = True
        for code in always_flag_codes:
            rc.raise_flag("item", item_id, step, code, flags_catalogue.get(code, "low"),
                           "every item of this step gets this flag", provisional_value=resolved_data,
                           prompt_version=prompt_version)

        status = "blocked" if blocked else "flagged"
        post_assembly(item_id, "retry1" if run_label == "retry1" else run_label, resolved_data, status)
        rc.write_item_status(step, item_id, status, prompt_version,
                               extra={"run": run_label, "check_message": msg})
        rc.append_run_log(item_id, step, run_label, agent_name, prompt_version, started, ended,
                            "fail", msg, "runA" if run_label == "retry1" else None, status)

    return new_lines


# ===========================================================================
# S0 - Intake check (pure script)
# ===========================================================================

class S0Plugin:
    step = "S0"

    def list_items(self, filters):
        return []

    def list_reason(self):
        return "S0 is a script-only step (scripts/intake_check.py). Nothing to list; run `run_step.py S0 --auto`."

    def auto(self, filters):
        script = rc.pp("scripts", "intake_check.py")
        if not os.path.exists(script):
            print(f"S0 --auto: {script} does not exist yet (owned by a parallel build pass). "
                  "Nothing to run.", file=sys.stderr)
            return
        started = rc.now_iso()
        result = subprocess.run([sys.executable, script], cwd=rc.pp())
        ended = rc.now_iso()
        prompt_version = rc.get_prompt_version("S0")
        status = "pass" if result.returncode == 0 else "blocked"
        rc.append_run_log("inputs", "S0", "runA", None, prompt_version, started, ended,
                            "pass" if result.returncode == 0 else "fail",
                            f"exit code {result.returncode}", None, status)

    def check(self, filters):
        """Two layers: (1) the whole-run status intake_check.py itself already writes to
        steps/S0/status/inputs.json (item_id "inputs") -- this method does NOT touch that file,
        only reads it, since intake_check.py (a parallel build pass, scripts/intake_check.py) owns
        writing it as part of --auto. (2) this build's own per-item validation: every real
        steps/S0/out/<item>.json record (one per required ncert_book/lab_manual/paper/key/
        legacy_sheet slot, per schemas/S0.json) is schema- and check-validated here, with its OWN
        item_id (the out-file's stem, e.g. "ncert-Biology-12-latest") so there is no filename
        collision with "inputs.json"."""
        prompt_version = rc.get_prompt_version("S0")
        report_path = rc.pp("register", "intake_report.md")
        out_dir = rc.pp("steps", "S0", "out")
        if not os.path.exists(report_path) or not os.path.isdir(out_dir):
            return []  # S0 --auto hasn't run yet (or intake_check.py doesn't exist yet)

        open_flags = [f for f in lib_io.read_jsonl(rc.pp("flags", "flags.jsonl")) if f.get("status") == "open"]
        any_new = False
        for fn in sorted(os.listdir(out_dir)):
            if not fn.endswith(".json"):
                continue
            item_id = fn[: -len(".json")]
            existing = rc.read_item_status("S0", item_id)
            if existing and existing.get("prompt_version") == prompt_version:
                continue
            data = _read_json(os.path.join(out_dir, fn))
            started = rc.now_iso()
            ok_schema, schema_msg = rc.validate_schema("S0", data)
            if ok_schema:
                ok, msg = rc.run_step_check("S0", data, {"item_id": item_id, "step": "S0", "open_flags": open_flags})
            else:
                ok, msg = False, schema_msg
            ended = rc.now_iso()
            status = "pass" if ok else "flagged"
            rc.write_item_status("S0", item_id, status, prompt_version, extra={"check_message": msg})
            rc.append_run_log(item_id, "S0", "runA", None, prompt_version, started, ended,
                                "pass" if ok else "fail", msg, None, status)
            any_new = True
        return []


# ===========================================================================
# A1 - Register the books
# ===========================================================================

class A1Plugin:
    step = "A1"
    agent = "a1-book-registrar"

    def _candidate_items(self, filters):
        """One representative PDF per (edition, class, subject) book-set under inputs/ncert/ —
        per docs/OPEN_QUESTIONS.md's 2026-10-09 A1/A2 file-layout decision, the real files are
        one-PDF-per-chapter, not one-PDF-per-book, so A1 registers the whole chapter set as one
        logical book from a single representative file (Chapter_1 when present, else the first
        file sorted) rather than dispatching a1-book-registrar once per chapter file."""
        groups = {}
        for relpath, abspath in rc.iter_ncert_files():
            parsed = rc.parse_ncert_relpath(relpath)
            key = (parsed["edition_code"], parsed["class_num"], parsed["subject"])
            item_id = rc.ncert_item_id(relpath)
            candidate = (item_id, relpath, abspath, parsed)
            chosen = groups.get(key)
            if chosen is None:
                groups[key] = candidate
            else:
                chosen_chapter = chosen[3].get("chapter_num")
                this_chapter = parsed.get("chapter_num")
                # Prefer chapter 1 (most reliably carries the reprint/imprint line, per the
                # real NCERT inspection); otherwise keep the first file in sorted order.
                if chosen_chapter != 1 and this_chapter == 1:
                    groups[key] = candidate
        out = []
        for item_id, relpath, abspath, parsed in groups.values():
            if not rc.item_passes_filters(item_id, filters):
                continue
            out.append((item_id, relpath, abspath, parsed))
        return out

    def list_items(self, filters):
        if not rc.s0_has_run():
            return []  # needs=S0 (spec 5.9); nothing to do until register/intake_report.md exists
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for item_id, relpath, abspath, parsed in self._candidate_items(filters):
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id):
                continue
            if os.path.exists(_out_path(self.step, item_id, "runA")):
                continue  # already dispatched, waiting on --check
            work_path = _work_input_path(self.step, item_id, "runA")
            if os.path.exists(work_path):
                pass  # already prepared on an earlier --list call; don't re-render (idempotence)
            else:
                input_data = self._build_input(item_id, relpath, abspath, parsed)
                _write_json(work_path, input_data)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        if not rc.s0_has_run():
            return ("A1 needs S0 (register/intake_report.md). S0 has not produced it yet, so A1 "
                    "has nothing ready to list (spec 5.9: an item needs a step once its previous "
                    "step is pass/flagged/skipped).")
        return ("A1: no candidate NCERT PDF matched the given filters, or every matching item "
                "already has output pending --check (nothing NEW to list — spec 5.9 idempotence).")

    def _build_input(self, item_id, relpath, abspath, parsed):
        work_dir = rc.pp("steps", self.step, "work")
        rc.ensure_dir(work_dir)
        n_pages = min(6, lib_pdf.page_count(abspath))
        page_images, text_layer = [], []
        for p in range(1, n_pages + 1):
            png_path = os.path.join(work_dir, f"{item_id}_p{p}.png")
            lib_pdf.render_page_to_png(abspath, p, out_path=png_path)
            page_images.append(_relpath(png_path))
            text_layer.append(lib_pdf.extract_text_layer(abspath, p))
        return {
            "file": relpath.replace(os.sep, "/"),
            "file_abs": _relpath(abspath),
            "folder_edition_hint": parsed["edition_code"],
            "subject_hint": parsed["subject"],
            "class_hint": parsed["class_num"],
            "page_images": page_images,
            "text_layer": text_layer,
        }

    def _post_assembly(self, item_id, run_label, data, status):
        if not data or "subject" not in data:
            return
        edition = data.get("edition_seen")
        if edition not in ("latest", "older", "lab_manual"):
            edition = None
        if not edition:
            return
        try:
            book_id = lib_ids.make_book_id(data["subject"], data["class"], {"latest": "L", "older": "O", "lab_manual": "M"}[edition])
        except Exception:
            return
        books_path = rc.pp("register", "books.csv")
        rows = lib_io.read_csv(books_path)
        fieldnames = ["book_id", "subject", "class", "language", "edition", "part_ranges",
                      "reprint_text_exact", "reprint_page", "file", "status"]
        if any(r.get("book_id") == book_id for r in rows):
            return  # one row per book (spec A1 check 3); first successful file wins
        rows.append({
            "book_id": book_id, "subject": data["subject"], "class": data["class"],
            "language": data.get("language", "English"), "edition": edition,
            "part_ranges": str(data.get("part") or ""),
            "reprint_text_exact": data.get("reprint_text_exact", ""),
            "reprint_page": str(data.get("reprint_page") or ""),
            "file": item_id, "status": status,
        })
        lib_io.write_csv(books_path, rows, fieldnames)

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        candidates = {item_id: None for item_id, *_ in self._candidate_items(filters)}
        # Rebuild each candidate's input_data from its already-written work file (not re-rendered).
        item_inputs = {}
        for item_id in candidates:
            for run_label in ("retry1", "runA"):
                p = _work_input_path(self.step, item_id, run_label)
                if os.path.exists(p):
                    item_inputs[item_id] = _read_json(p)
                    break
        return resolve_single_run_items(
            self.step, get_cfg(self.step), self.agent, item_inputs, {},
            self._post_assembly, always_flag_codes=["A1_REGISTER_DRAFT"],
        )


# ===========================================================================
# A2 - Read the pages (per page). Item id scheme (2026-10-10, see docs/OPEN_QUESTIONS.md): the
# real inputs/ncert/ layout is one PDF per NCERT chapter, not one PDF per book (A1's 2026-10-09
# decision), and a book's full chapter set must ALL be read, not just A1's single representative
# registration file (confirmed by direct run: A1+A2 run for real against BIO12L only ever touched
# Chapter_1.pdf's 23 pages, never chapters 2-13). Since every chapter file restarts at page 1,
# page number alone stops being unique within a book once more than one chapter is in play, so the
# item id carries the chapter number too: "{book_id}-ch{chapter_num:02d}-p{page:03d}", e.g.
# "BIO12L-ch01-p001". previous_page_last_block and the cross-page continuity check are both scoped
# to (book_id, chapter_num) -- a chapter boundary is a real NCERT-chapter boundary, never a
# continuation, even though each file's own page numbering restarts at 1 just like a continuation
# would look.
# ===========================================================================

class A2Plugin:
    step = "A2"
    agent = "a2-page-reader"

    _ITEM_ID_RE = re.compile(r"^(?P<book_id>.+)-ch(?P<chapter_num>\d+)-p(?P<page>\d+)$")

    @staticmethod
    def _item_id(book_id, chapter_num, page_num):
        return f"{book_id}-ch{chapter_num:02d}-p{page_num:03d}"

    @classmethod
    def _parse_item_id(cls, item_id):
        """-> (book_id, chapter_num, page_num) or None if item_id isn't this step's own scheme."""
        m = cls._ITEM_ID_RE.match(item_id)
        if not m:
            return None
        return m.group("book_id"), int(m.group("chapter_num")), int(m.group("page"))

    def _registered_books(self):
        return lib_io.read_csv(rc.pp("register", "books.csv"))

    def _book_chapter_files(self, book_row):
        """Every chapter PDF belonging to this book's (edition, class, subject) group -- the same
        grouping key A1Plugin._candidate_items() uses, just without collapsing to one
        representative file -- sorted by chapter number. A file with no detectable chapter number
        is skipped (there is no number to build the item id / passage addressing scheme from);
        this hasn't happened for any real file seen so far (rc.extract_chapter_num handles every
        real naming pattern), but a stray file must not silently crash enumeration."""
        edition = book_row.get("edition")
        try:
            class_num = int(book_row.get("class"))
        except (TypeError, ValueError):
            return []
        subject = book_row.get("subject")
        out = []
        for relpath, abspath in rc.iter_ncert_files():
            parsed = rc.parse_ncert_relpath(relpath)
            if parsed["edition_code"] != edition or parsed["class_num"] != class_num or parsed["subject"] != subject:
                continue
            if parsed["chapter_num"] is None:
                continue
            out.append((parsed["chapter_num"], relpath, abspath))
        out.sort(key=lambda t: t[0])
        return out

    @staticmethod
    def _chapter_pdf_abspath(book_id, chapter_num):
        """Resolve (book_id, chapter_num) back to the real chapter PDF's absolute path, by
        matching register/books.csv's (edition, class, subject) group against
        rc.iter_ncert_files() -- the same grouping key _book_chapter_files() uses above. Added
        2026-10-12 (see docs/OPEN_QUESTIONS.md) for A2SPlugin's real bug fix: ncert/blocks/*.jsonl
        records carry book_id/chapter_num/page/bbox but never the source PDF path itself, so A2S
        needs this to crop a needs_special block's bbox out of the real page. Returns None if the
        book isn't registered or no chapter file matches."""
        books = lib_io.read_csv(rc.pp("register", "books.csv"))
        row = next((r for r in books if r.get("book_id") == book_id), None)
        if not row:
            return None
        edition = row.get("edition")
        try:
            class_num = int(row.get("class"))
        except (TypeError, ValueError):
            return None
        subject = row.get("subject")
        for relpath, abspath in rc.iter_ncert_files():
            parsed = rc.parse_ncert_relpath(relpath)
            if (parsed["edition_code"] == edition and parsed["class_num"] == class_num
                    and parsed["subject"] == subject and parsed["chapter_num"] == chapter_num):
                return abspath
        return None

    def list_items(self, filters):
        books = self._registered_books()
        if not books:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for row in books:
            book_id = row["book_id"]
            for chapter_num, relpath, abspath in self._book_chapter_files(row):
                n_pages = lib_pdf.page_count(abspath)
                for p in range(1, n_pages + 1):
                    item_id = self._item_id(book_id, chapter_num, p)
                    if not rc.item_passes_filters(item_id, filters):
                        continue
                    status = rc.read_item_status(self.step, item_id)
                    if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                        continue
                    if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                        continue
                    input_data = self._build_input(book_id, chapter_num, abspath, p)
                    _write_json(_work_input_path(self.step, item_id, "runA"), input_data)
                    lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                            _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return "A2 needs A1 (register/books.csv rows). No books registered yet."

    def _build_input(self, book_id, chapter_num, abspath, page_num):
        work_dir = rc.pp("steps", self.step, "work")
        rc.ensure_dir(work_dir)
        item_id = self._item_id(book_id, chapter_num, page_num)
        png_path = os.path.join(work_dir, f"{item_id}.png")
        lib_pdf.render_page_to_png(abspath, page_num, out_path=png_path)
        prev_block = None
        if page_num > 1:
            # Same-chapter previous page only -- a chapter's own page 1 never inherits a
            # continuation from a different NCERT chapter (see module-level note above).
            prev_item_id = self._item_id(book_id, chapter_num, page_num - 1)
            prev_path = rc.pp("steps", self.step, "status", f"{prev_item_id}.last_block.json")
            prev_block = _read_json(prev_path) if os.path.exists(prev_path) else None
        return {
            "book_id": book_id, "chapter_num": chapter_num, "page": page_num,
            "image": _relpath(png_path),
            "text_layer": lib_pdf.extract_text_layer(abspath, page_num),
            "previous_page_last_block": prev_block,
        }

    def _post_assembly(self, item_id, run_label, data, status):
        if not data or "blocks" not in data:
            return
        parsed = self._parse_item_id(item_id)
        if not parsed:
            return
        book_id, chapter_num, page_num = parsed
        blocks_path = rc.pp("ncert", "blocks", f"{book_id}.jsonl")
        for b in data["blocks"]:
            record = dict(b)
            record["book_id"] = book_id
            record["chapter_num"] = chapter_num
            record["page"] = f"{page_num:03d}"
            lib_io.append_jsonl(blocks_path, record)
        if data.get("blocks"):
            last_block_path = rc.pp("steps", self.step, "status", f"{item_id}.last_block.json")
            last = data["blocks"][-1]
            _write_json(last_block_path, {"kind": last.get("kind"), "text_tail": (last.get("text") or "")[-100:]})

    def check(self, filters):
        books = self._registered_books()
        work_dir = rc.pp("steps", self.step, "work")
        item_inputs = {}
        if os.path.isdir(work_dir):
            valid_prefixes = set()
            for row in books:
                book_id = row["book_id"]
                for chapter_num, relpath, abspath in self._book_chapter_files(row):
                    valid_prefixes.add(f"{book_id}-ch{chapter_num:02d}-p")
            for run_label in ("retry1", "runA"):
                suffix = f".{run_label}.input.json"
                for fn in os.listdir(work_dir):
                    if not fn.endswith(suffix):
                        continue
                    item_id = fn[: -len(suffix)]
                    if item_id in item_inputs:
                        continue
                    if any(item_id.startswith(p) for p in valid_prefixes):
                        item_inputs[item_id] = _read_json(os.path.join(work_dir, fn))
        new_lines = resolve_single_run_items(self.step, get_cfg(self.step), self.agent, item_inputs, {},
                                               self._post_assembly)
        self._check_cross_page_continuity(books)
        return new_lines

    def _check_cross_page_continuity(self, books):
        """Spec Section 9/A2 check (2): page N's last_block_continues_on_next must equal page
        N+1's first_block_continues_from_previous. This is a cross-item check that can only run
        once both pages have output, so it lives here (after resolve_single_run_items), not in
        scripts/checks/A2.py's single-page check. Scoped per (book_id, chapter_num): N and N+1 are
        only ever compared within the same NCERT chapter file -- page 1 of chapter 2 is never
        compared against the last page of chapter 1, since those are two different real NCERT
        chapters, not a continuation (see module-level note above). A mismatch is a real signal
        two independent page reads disagree about a page break -- per the step's 'On failure',
        that's an adjudication case (A2_JOIN_ADJUDICATED, normal), not a hard failure of either
        page; this build has no synchronous adjudicator call wired in yet, so it raises the flag
        and leaves both pages' own status untouched, matching the A6_WEAK_PAIR precedent elsewhere
        in this codebase (flag + keep going, rather than block)."""
        out_dir = rc.pp("steps", self.step, "out")
        if not os.path.isdir(out_dir):
            return
        flags_path = rc.pp("flags", "flags.jsonl")
        for row in books:
            book_id = row["book_id"]
            for chapter_num, relpath, abspath in self._book_chapter_files(row):
                prefix = f"{book_id}-ch{chapter_num:02d}-p"
                pages = sorted(
                    int(fn[len(prefix):-len(".runA.json")])
                    for fn in os.listdir(out_dir)
                    if fn.startswith(prefix) and fn.endswith(".runA.json")
                )
                for p in pages:
                    if (p + 1) not in pages:
                        continue
                    item_a = self._item_id(book_id, chapter_num, p)
                    item_b = self._item_id(book_id, chapter_num, p + 1)
                    path_a = _out_path(self.step, item_a, "runA")
                    path_b = _out_path(self.step, item_b, "runA")
                    data_a, data_b = _read_json(path_a), _read_json(path_b)
                    if not data_a or not data_b or "error" in data_a or "error" in data_b:
                        continue
                    last_a = data_a.get("last_block_continues_on_next")
                    first_b = data_b.get("first_block_continues_from_previous")
                    if last_a == first_b:
                        continue
                    item_id = f"{item_a}|{item_b}"
                    if self._flag_already_open(item_id, "A2_JOIN_ADJUDICATED", flags_path):
                        continue
                    rc.raise_flag(
                        item_type="page_pair", item_id=item_id, step=self.step,
                        code="A2_JOIN_ADJUDICATED", severity="normal",
                        message=(f"Page {p}'s last_block_continues_on_next={last_a} but page {p+1}'s "
                                  f"first_block_continues_from_previous={first_b} -- two independent "
                                  f"page reads disagree about this page break; needs adjudication."),
                        provisional_value={"page_a": p, "last_a": last_a, "page_b": p + 1, "first_b": first_b},
                        evidence=[_relpath(path_a), _relpath(path_b)],
                        prompt_version=rc.get_prompt_version(self.step),
                    )

    @staticmethod
    def _flag_already_open(item_id, code, flags_path):
        if not os.path.exists(flags_path):
            return False
        for f in lib_io.read_jsonl(flags_path):
            if f.get("item_id") == item_id and f.get("code") == code and f.get("status") == "open":
                return True
        return False


# ===========================================================================
# A2S - Transcribe special blocks
# ===========================================================================

class A2SPlugin:
    step = "A2S"
    agent = "a2-special-transcriber"

    def _pending_special_blocks(self):
        """Blocks A2 marked needs_special, read back from ncert/blocks/*.jsonl, that have no
        A2S output yet. Keyed by a synthetic item_id '<book_id>-p<page>-b<n>'."""
        blocks_dir = rc.pp("ncert", "blocks")
        if not os.path.isdir(blocks_dir):
            return {}
        out = {}
        unnumbered = {}   # (book, chapter, page) -> how many `n`-less blocks seen there so far
        for fn in sorted(os.listdir(blocks_dir)):
            if not fn.endswith(".jsonl"):
                continue
            book_id = fn[: -len(".jsonl")]
            for rec in lib_io.read_jsonl(os.path.join(blocks_dir, fn)):
                if rec.get("needs_special"):
                    # chapter_num is REQUIRED in this key, not decoration. Every chapter PDF
                    # restarts at page 1, so without it chapter 1's page 4 block 2 and chapter 9's
                    # page 4 block 2 are both "<BOOK>-p004-b2"; `out` is a dict, so one silently
                    # overwrites the other and can never be transcribed -- while A2S still reports
                    # DONE. Measured on real data before the fix: 131 collisions across the corpus
                    # (PHY11L 49, PHY12L 40, BIO12L 28, CHE12L 14), i.e. 131 equations/figures/
                    # tables quietly dropped. This is the same defect already fixed for A2 and A3
                    # on 2026-10-10 (their ids gained ch{NN} for exactly this reason); A2S was
                    # missed because no multi-chapter book had special blocks until Physics and
                    # Chemistry were indexed.
                    ch = rec.get("chapter_num")
                    ch_part = f"-ch{int(ch):02d}" if ch is not None else ""
                    # A block with NO `n` must still get a unique id. A2's schema requires `n`,
                    # but one real page's output violates that (BIO12L-ch03-p001 -- already
                    # recorded as KNOWN_BAD in tests/test_a2_check.py, "all 7 blocks miss the
                    # required `n` field") and those blocks reached ncert/blocks anyway. Formatting
                    # None straight into the key gave BOTH of that page's figures the id
                    # "BIO12L-ch03-p001-bNone", so the dict kept one and the other could never be
                    # transcribed -- while A2S still reported DONE. That is the same silent-drop
                    # failure the chapter fix above exists to prevent, so it gets the same
                    # treatment rather than being left as "only 2 blocks".
                    #
                    # Measured across the corpus: 1675 needs_special blocks, exactly 2 without `n`,
                    # both figures on that one page, colliding on one id. Found because an A2S
                    # worker quoted the literal id "BIO12L-ch03-p001-bNone" back in its report.
                    #
                    # The fallback numbers them by order of appearance within their page, which is
                    # deterministic for a given blocks file. It is a WORKAROUND for bad upstream
                    # output, not a substitute for `n`: if that page is ever re-read by A2 the ids
                    # may shift, so the real fix remains re-reading it.
                    n = rec.get("n")
                    if n is None:
                        page_key = (book_id, ch_part, str(rec.get("page")))
                        unnumbered[page_key] = unnumbered.get(page_key, 0) + 1
                        n = f"ix{unnumbered[page_key]}"
                    item_id = f"{book_id}{ch_part}-p{rec.get('page')}-b{n}"
                    out[item_id] = rec
        return out

    #: (book_id, chapter_num, page) -> every block A2 recorded there, special or not. Built once
    #: per process. The crop grower needs the NON-special blocks most of all: a figure's caption is
    #: usually the paragraph-kind block immediately below it, and the whole point is to reach the
    #: gap between them rather than guess a pixel distance.
    _page_blocks_cache = None

    @classmethod
    def _blocks_on_page(cls, book_id, chapter_num, page):
        if cls._page_blocks_cache is None:
            cache = {}
            blocks_dir = rc.pp("ncert", "blocks")
            if os.path.isdir(blocks_dir):
                for fn in sorted(os.listdir(blocks_dir)):
                    if not fn.endswith(".jsonl"):
                        continue
                    book = fn[: -len(".jsonl")]
                    for rec in lib_io.read_jsonl(os.path.join(blocks_dir, fn)):
                        key = (book, rec.get("chapter_num"), str(rec.get("page")))
                        cache.setdefault(key, []).append(rec)
            cls._page_blocks_cache = cache
        return cls._page_blocks_cache.get((book_id, chapter_num, str(page)), ())

    def list_items(self, filters):
        pending = self._pending_special_blocks()
        if not pending:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for item_id, rec in pending.items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            # Real bug fix (2026-10-12, see docs/OPEN_QUESTIONS.md): this previously passed the
            # raw bbox list itself as "image" -- never a readable path -- because A2S had never
            # been exercised against real needs_special blocks before (the 2 earlier Biology
            # chapters had none). Crop the block's own bbox out of its real source page into an
            # actual PNG, matching a2-special-transcriber's documented input contract ("image:
            # the crop").
            image_value = None
            crop_origin = None      # (x, y) of the crop's top-left in page pixels
            book_id = rec.get("book_id")
            chapter_num = rec.get("chapter_num")
            bbox = rec.get("bbox")
            try:
                page_num = int(rec.get("page"))
            except (TypeError, ValueError):
                page_num = None
            if book_id and chapter_num is not None and page_num and bbox:
                abspath = A2Plugin._chapter_pdf_abspath(book_id, chapter_num)
                if abspath:
                    work_dir = rc.pp("steps", self.step, "work")
                    rc.ensure_dir(work_dir)
                    crop_path = os.path.join(work_dir, f"{item_id}.png")
                    # Pad the recorded bbox, and pad it MORE vertically.
                    #
                    # A2's box bounds the drawing, not the thing a transcriber needs to read. A
                    # figure's caption sits below it and reagent labels sit above it, so a crop
                    # of the bare bbox clips exactly the text this step exists to capture.
                    # Reported from real transcriptions: CHE12L-p010-b14 and p020-b14 both lost
                    # their captions mid-sentence ("...The total vapour", "...rises in the thistle
                    # funnel due to"), p021-b15 lost half the reagent labels above its arrows, and
                    # p013-b17 was so misaligned that the crop was mostly prose from the previous
                    # block with two structures clipped to a few pixels at the bottom edge.
                    # pymupdf clips the rect to the page, so over-wide values are safe.
                    # Pad asymmetrically BY KIND, because NCERT puts a table's title ABOVE it and
                    # a figure's caption BELOW it, and both are content this step exists to
                    # capture. Reported from real crops: figure captions cut off at the bottom
                    # (CHE12L p010-b14 and p020-b14, each ending mid-sentence) and a table title
                    # cut off at the top (BIO12L-ch04-p014-b2, where only the second line "and
                    # Genes" survived and "Table 4.3: ..." was above the frame). A single
                    # symmetric pad has to be large on both sides to catch either, which drags in
                    # more of the neighbouring column than necessary; leaning the extra margin the
                    # way the text actually sits costs nothing.
                    #
                    # Widened horizontally 24 -> 56 on 2026-10-13, after the first large A2S wave.
                    # Six workers independently reported captions clipped at the LEFT margin --
                    # "gure 10.1" (BIO12L-ch10-p004-b2), "re 6.2" (BIO11L-ch06-p003-b8), "re 17.1"
                    # (BIO11L-ch17-p003-b3, clipped at both edges), "igure 10.1"
                    # (BIO11L-ch10-p002-b6) -- because an NCERT caption line is typically wider
                    # than the artwork it sits under and starts to the left of the block's bbox.
                    #
                    # The trade is deliberately asymmetric, on the workers' own evidence: the same
                    # reports describe over-inclusion as "minor over-inclusion from padding, none
                    # lost content", and every one of them correctly excluded the neighbouring
                    # sliver and said so in `note`. A reader can ignore a fragment it can see; it
                    # cannot recover a glyph that was never rendered. So prefer too much frame.
                    # y grows DOWNWARD in these pixel coords, so `top` is subtracted from y0.
                    kind = (rec.get("kind") or "").strip().lower()
                    if kind == "table":
                        pad_top, pad_bottom = 96, 56     # title sits above the table
                    elif kind == "figure":
                        pad_top, pad_bottom = 72, 96     # caption below; labels crowd the top edge
                    else:
                        pad_top, pad_bottom = 72, 72     # equation / box: numbers sit to the side
                    pad_x = 56
                    # Then GROW toward the neighbouring blocks instead of guessing a bigger pad.
                    #
                    # A fixed pad cannot work, and three rounds of enlarging it is the evidence:
                    # a caption may be one line or three, so 96 px catches "Figure 1.10 A
                    # wind-pollinated plant ..." and still loses line 2 of "Figure 1.11 (a)
                    # Pollination by water in Vallisneria; (b) ...". The bbox bounds the ARTWORK;
                    # the caption lives in the white space underneath it, and the real boundary is
                    # not a distance at all -- it is wherever the next block starts.
                    #
                    # So: look at this page's other blocks, keep the ones whose horizontal span
                    # overlaps this one (same column), and extend up/down to just short of the
                    # nearest neighbour above and below. Everything in that gap belongs to this
                    # block -- in NCERT it is the caption or the title, which is exactly what was
                    # being cut. The per-kind pad above stays as the FLOOR, so a block with no
                    # neighbour in its column is unaffected, and MAX_GROW caps the reach so a
                    # figure at the foot of a sparse page cannot swallow half the page.
                    #
                    # Requiring column overlap is what makes this safe on two-column pages: the
                    # adjacent column's paragraphs have no x-overlap, so they neither limit the
                    # growth nor get pulled in by it.
                    # OPEN_GROW is used when there is no recorded block in that direction at all.
                    # It is deliberately larger than the floor: if A2 recorded nothing there, the
                    # only things that can be in the space are this block's own caption and white
                    # paper, and pymupdf clips the rect at the page edge, so reaching further
                    # cannot pull in another block's text. This is what fixes the figures whose
                    # caption is NOT a separate block -- BIO12L-ch01-p012-b1 and ch04-p011-b1 both
                    # have no sibling below them, so neighbour-growth alone left them at the floor
                    # and their second caption line stayed outside the frame.
                    MAX_GROW, OPEN_GROW, GAP = 260, 200, 8
                    x0, y0, x1, y1 = bbox[0], bbox[1], bbox[2], bbox[3]
                    top, bottom = y0 - pad_top, y1 + pad_bottom   # the per-kind FLOOR
                    left, right = x0 - pad_x, x1 + pad_x
                    up = down = lf = rt = None
                    for sib in self._blocks_on_page(book_id, chapter_num, rec.get("page")):
                        sb = sib.get("bbox")
                        if not sb or sib.get("n") == rec.get("n"):
                            continue
                        if min(x1, sb[2]) - max(x0, sb[0]) > 0:        # same column
                            if sb[3] <= y0:
                                up = sb[3] if up is None else max(up, sb[3])
                            elif sb[1] >= y1:
                                down = sb[1] if down is None else min(down, sb[1])
                        if min(y1, sb[3]) - max(y0, sb[1]) > 0:        # same row band
                            if sb[2] <= x0:
                                lf = sb[2] if lf is None else max(lf, sb[2])
                            elif sb[0] >= x1:
                                rt = sb[0] if rt is None else min(rt, sb[0])
                    # Grow only OUTWARD, never past a neighbour, never past MAX_GROW. Horizontal
                    # growth is what the later reports were asking for: captions clipped to
                    # "gure 17.1" and labels reduced to their tail letters ("oles", "leus") are a
                    # left-edge problem, and a caption line is routinely wider than the artwork.
                    top = min(top, max(up + GAP, y0 - MAX_GROW)) if up is not None else y0 - OPEN_GROW
                    bottom = max(bottom, min(down - GAP, y1 + MAX_GROW)) if down is not None else y1 + OPEN_GROW
                    left = min(left, max(lf + GAP, x0 - MAX_GROW)) if lf is not None else x0 - OPEN_GROW
                    right = max(right, min(rt - GAP, x1 + MAX_GROW)) if rt is not None else x1 + OPEN_GROW
                    padded = [left, top, right, bottom]
                    lib_pdf.crop_box(abspath, page_num, padded, crop_path,
                                      dpi=lib_pdf.DEFAULT_DPI, unit="px")
                    image_value = _relpath(crop_path)
                    # pymupdf clips the rect to the page, so the rendered crop starts at the
                    # clamped origin, not the requested one -- clamp here too or the offsets lie.
                    crop_origin = (max(0.0, padded[0]), max(0.0, padded[1]))
            input_data = {"kind": rec.get("kind"), "image": image_value,
                           "text_layer": rec.get("text") or None,
                           "table_continues_from_previous": rec.get("continues_from_previous", False)}
            # Where the TARGET block sits inside the padded crop, in crop pixels.
            #
            # The crop deliberately reaches past the block's own box to catch a caption or table
            # title, and on a densely packed page that can pull in a sibling. A worker hit exactly
            # that and said so: CHE11L-ch07-p012-b2's crop holds three display equations, it could
            # not tell which one A2's box pointed at, transcribed the vertically centred one and
            # warned that "if A2's box pointed at one of the other two, that output is of the wrong
            # line". A crop that shows several candidates with no way to say which is meant is an
            # ambiguity the input can simply resolve, so it now does: `[x0, y0, x1, y1]` of the
            # block relative to the crop's own top-left. Everything outside it is context.
            if crop_origin is not None and bbox:
                ox, oy = crop_origin
                input_data["target_box_in_crop"] = [
                    round(bbox[0] - ox), round(bbox[1] - oy),
                    round(bbox[2] - ox), round(bbox[3] - oy)]
            _write_json(_work_input_path(self.step, item_id, "runA"), input_data)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return "A2S needs A2 output with needs_special blocks (ncert/blocks/*.jsonl); none found yet."

    def _post_assembly(self, item_id, run_label, data, status):
        pass  # joining into ncert/blocks/<BOOK>.jsonl happens in the "after A2 and A2S" script
              # pass, not modelled separately here given no real upstream data exists yet to join.

    def check(self, filters):
        pending = self._pending_special_blocks()
        item_inputs = {}
        for item_id in pending:
            for run_label in ("retry1", "runA"):
                p = _work_input_path(self.step, item_id, run_label)
                if os.path.exists(p):
                    item_inputs[item_id] = _read_json(p)
                    break
        return resolve_single_run_items(self.step, get_cfg(self.step), self.agent, item_inputs, {},
                                          self._post_assembly)


# ===========================================================================
# A3 - Split into passages. Item id / sectioning scheme (2026-10-10, see docs/OPEN_QUESTIONS.md):
# real A2 output has no `section_heading` field at all (confirmed against the 123 real BIO12L
# blocks) -- the old grouping-by-that-field collapsed every block in a book into one giant
# "default" section, and would now also wrongly mix chapters once a book has more than one
# chapter's blocks on file. Sections are derived from the real block stream instead: a new section
# starts at each kind:"heading" block, scoped within each (book_id, chapter_num) group (A2's own
# fix #1); blocks before a chapter's first heading form an implicit opening section. Item id:
# "{book_id}-ch{chapter_num:02d}-s{ordinal:02d}" (ordinal = 1-based position of the section within
# its chapter, in block/page order).
# ===========================================================================

class A3Plugin:
    step = "A3"
    agent = "a3-passage-splitter"

    _ITEM_ID_RE = re.compile(r"^(?P<book_id>.+)-ch(?P<chapter_num>\d+)-s(?P<ordinal>\d+)$")
    # re.DOTALL is required, not cosmetic: a real NCERT subsection heading can wrap across two
    # lines inside one heading block (confirmed: BIO12L Chapter 3's "3.1 REPRODUCTIVE HEALTH –
    # PROBLEMS AND\nSTRATEGIES"), and without DOTALL `.+` can't cross the embedded "\n", so the
    # whole match silently fails and a real numbered heading falls through to "title_candidate"
    # instead -- confirmed as the reason "3.1" was missing from BIO12-CH03's headings list.
    # Chapter 1's own headings happened to all be single-line, which is why this didn't surface
    # there first -- 2026-10-10, docs/OPEN_QUESTIONS.md.
    _HEADING_NUM_RE = re.compile(r"^(?P<number>\d+(?:\.\d+)*)\s+(?P<text>.+)$", re.DOTALL)
    # Strips a leading "CHAPTER N" banner line whether or not it got merged into the same heading
    # block as the chapter's own title. Confirmed as a real shape difference between chapters:
    # BIO12L Chapter 1's opener is TWO heading blocks ("CHAPTER 1", then "SEXUAL REPRODUCTION IN
    # FLOWERING PLANTS"); Chapter 3's opener is ONE heading block, literally "CHAPTER 3\nREPRODUCTIVE
    # HEALTH" -- different real agent calls read the same kind of banner differently depending on
    # its exact layout. Stripping this prefix before classifying makes both shapes resolve to the
    # same clean title instead of leaving "CHAPTER 3\n" baked into Chapter 3's title only because
    # of how that one page happened to get chunked -- 2026-10-10, docs/OPEN_QUESTIONS.md.
    # 2026-10-12: the digit-only form above was too narrow and silently produced two WRONG chapter
    # titles the first time a non-Biology chapter was assembled for real. Two further real banner
    # shapes, both confirmed against the actual A2 output:
    #   - PHY11L ch08's banner is the number spelled as a WORD -- literally "CHAPTER EIGHT", in its
    #     own heading block, with the real title "MECHANICAL PROPERTIES OF SOLIDS" in the next
    #     section. `\d+` never matched it, so "CHAPTER EIGHT" became the lowest-ordinal
    #     title-candidate and locked in as PHY11-CH08's title.
    #   - CHE12L ch09's banner is "Unit 9": NCERT Chemistry labels its chapters "Unit N", not
    #     "Chapter N". Same failure -- CHE12-CH09's title came out as "Unit 9" instead of "Amines".
    # NCERT Biology additionally uses "UNIT N" for its thematic multi-chapter divider pages, which
    # are likewise banners rather than titles or subsections, so covering "UNIT" is right there too.
    # The chapter title feeds A4's `chapter_title` input and D1, so a wrong one propagates.
    _BANNER_NUMBER = (
        r"(?:\d+"
        r"|ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN"
        r"|ELEVEN|TWELVE|THIRTEEN|FOURTEEN|FIFTEEN|SIXTEEN|SEVENTEEN|EIGHTEEN|NINETEEN"
        r"|TWENTY(?:[-\s](?:ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE))?"
        r")"
    )
    _CHAPTER_PREFIX_RE = re.compile(
        r"^(?:CHAPTER|UNIT)\s+" + _BANNER_NUMBER + r"\s*\n*\s*", re.IGNORECASE)

    # Unnumbered headings that name a PART OF EVERY CHAPTER and so can never be a chapter's title.
    #
    # Real bug this fixes, found 2026-10-13 by four A4 workers reporting it independently across
    # both runs: `_chapters()` takes the chapter title to be the first "title_candidate" heading in
    # ordinal order, on the assumption that the chapter's own banner is always ordinal 1. When a
    # chapter's banner page has not been read yet -- which is the normal state while A2 is only
    # part-way through a book -- the first unnumbered heading encountered is whatever structural
    # heading A2 did reach, and "SUMMARY" or "EXERCISES" became the title. Measured: 11 of the 15
    # A4 work inputs carried `chapter_title: "SUMMARY"` and one carried `"EXERCISES"`.
    #
    # The existing (page, n) sort fixed the ORDERING half of this (file append order is not page
    # order); it cannot fix the case where the banner is simply absent. Leaving the title EMPTY is
    # the right answer there: empty is visibly missing and can be flagged, whereas "SUMMARY"
    # silently propagates into A4's `chapter_title` and into D1's chapter choice, which is exactly
    # what the comment above _BANNER_NUMBER warns about.
    _STRUCTURAL_HEADINGS = frozenset({
        "SUMMARY", "SUMMARISE", "EXERCISE", "EXERCISES", "NOTE", "NOTES", "GLOSSARY",
        "APPENDIX", "APPENDICES", "ANSWERS", "ANSWER KEY", "REFERENCES", "FURTHER READING",
        "FURTHER READINGS", "SUGGESTED READING", "SUGGESTED READINGS", "INTRODUCTION",
        "CONTENTS", "INDEX", "BIBLIOGRAPHY", "ACKNOWLEDGEMENT", "ACKNOWLEDGEMENTS",
        "PREFACE", "FOREWORD", "SUMMARY AND CONCLUSION", "KEY WORDS", "KEYWORDS",
        "DO YOU KNOW", "ACTIVITY", "ACTIVITIES", "OBJECTIVES", "LEARNING OBJECTIVES",
    })

    @staticmethod
    def _item_id(book_id, chapter_num, ordinal):
        return f"{book_id}-ch{chapter_num:02d}-s{ordinal:02d}"

    @classmethod
    def _parse_item_id(cls, item_id):
        m = cls._ITEM_ID_RE.match(item_id)
        if not m:
            return None
        return m.group("book_id"), int(m.group("chapter_num")), int(m.group("ordinal"))

    def _sections(self):
        """{(book_id, chapter_num, ordinal): {"heading_text": str|None, "blocks": [rec, ...]}},
        built by walking each book's ncert/blocks/<BOOK>.jsonl, sorted into true (page, n) reading
        order, and cutting a new section at every kind:"heading" block, scoped per chapter_num (a
        heading never starts a new section that crosses a chapter boundary, and a chapter boundary
        never merges into the previous chapter's trailing section).

        The explicit (page, n) sort (added 2026-10-10 -- see docs/OPEN_QUESTIONS.md) is required,
        not optional: confirmed against the real BIO12L.jsonl that the file's own append order is
        NOT page order -- A2Plugin.check() (both before and after this fix) discovers each page's
        work-input file via os.listdir(), which is not guaranteed sorted, so _post_assembly can
        append page 9's blocks, then page 10's, then page 22's, then page 6's, etc. A section
        walk over raw file order on real data put the chapter's "EXERCISES" heading (actually its
        last page) ahead of "CHAPTER 1" and the real chapter-title banner (actually its first
        page), corrupting both section order and the title-derivation heuristic below. Sorting by
        (page, n) first makes the walk correct regardless of the file's append order."""
        blocks_dir = rc.pp("ncert", "blocks")
        if not os.path.isdir(blocks_dir):
            return {}
        by_chapter = collections.defaultdict(list)
        for fn in sorted(os.listdir(blocks_dir)):
            if not fn.endswith(".jsonl"):
                continue
            book_id = fn[: -len(".jsonl")]
            for rec in lib_io.read_jsonl(os.path.join(blocks_dir, fn)):
                # Real blocks written before the A2 chapter_num fix (the original 23 BIO12L pages)
                # lack this field; they are all genuinely Chapter_1 (the only chapter processed
                # before the fix existed), so default to 1 rather than drop them -- see
                # docs/OPEN_QUESTIONS.md. Post-fix blocks always carry it explicitly.
                chapter_num = int(rec.get("chapter_num") or 1)
                by_chapter[(book_id, chapter_num)].append(rec)

        sections = {}
        for (book_id, chapter_num), blocks in by_chapter.items():
            blocks.sort(key=lambda r: (str(r.get("page") or ""), r.get("n") or 0))
            ordinal = 0
            current_heading = None
            current_blocks = []
            for rec in blocks:
                if rec.get("kind") == "heading":
                    if current_blocks:
                        ordinal += 1
                        sections[(book_id, chapter_num, ordinal)] = {
                            "heading_text": current_heading, "blocks": current_blocks,
                        }
                    current_heading = rec.get("text")
                    current_blocks = []
                current_blocks.append(rec)
            if current_blocks:
                ordinal += 1
                sections[(book_id, chapter_num, ordinal)] = {
                    "heading_text": current_heading, "blocks": current_blocks,
                }
        return sections

    @staticmethod
    def _unread_pages_in(book_id, chapter_num, blocks):
        """Pages inside this section's own span that A2 never produced output for.

        A2 runs per page and A3 concatenates whatever A2 produced, in page order. If a page in
        the middle of a chapter was never read, A3 cannot tell that gap from a genuine page break:
        it joins the text either side and the section silently acquires content from a different
        topic -- including the heading that would have announced the change, which lived on the
        unread page.

        This is not hypothetical. `BIO11L-ch02-s12` is headed "2.2.5 Protozoans" and holds four
        blocks of protozoan text from page 006 followed by four blocks of FUNGI text from page
        008 (conidia, plasmogamy, karyogamy, mycelium). Page 007 -- carrying the "2.3 FUNGI"
        heading -- has no A2 output. The result is not a gap but WRONG data: those passages are
        filed as evidence about protozoans, and Stage D would offer them to an agent as the NCERT
        basis for a protozoan question, with nothing downstream able to contradict it.

        Measured when found: 3 of 19 chapters affected, 9 pages, all BIO11L -- and every one of
        those pages HAD an A2 work input, so A2 was offered them and simply never finished.
        """
        pages = sorted({b.get("page") for b in blocks if b.get("page") is not None})
        if len(pages) < 2:
            return ()
        try:
            lo, hi = int(pages[0]), int(pages[-1])
        except (TypeError, ValueError):
            return ()
        out_dir = rc.pp("steps", "A2", "out")
        if not os.path.isdir(out_dir):
            return ()
        unread = []
        for p in range(lo, hi + 1):
            stem = f"{book_id}-ch{int(chapter_num):02d}-p{p:03d}"
            if not any(os.path.exists(os.path.join(out_dir, f"{stem}.{r}.json"))
                       for r in ("runA", "retry1", "retry2")):
                unread.append(p)
        return tuple(unread)

    def list_items(self, filters):
        sections = self._sections()
        if not sections:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        self._bridged = []
        for (book_id, chapter_num, ordinal), info in sections.items():
            item_id = self._item_id(book_id, chapter_num, ordinal)
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            chapter_id = f"{book_id[:-1]}-CH{chapter_num:02d}"
            blocks = info["blocks"]
            # Refuse to hand over a section assembled across an unread page. Splitting it would
            # produce passages attributed to whichever heading happened to survive, so the honest
            # move is to withhold the section until A2 has read the page -- a missing section is
            # recoverable, mis-attributed evidence is not.
            unread = self._unread_pages_in(book_id, chapter_num, blocks)
            if unread:
                self._bridged.append((item_id, unread))
                rc.raise_flag("item", item_id, self.step, "A3_SECTION_SPANS_UNREAD_PAGE",
                              (get_cfg(self.step).get("flags") or {}).get(
                                  "A3_SECTION_SPANS_UNREAD_PAGE", "blocker"),
                              f"section spans pages {blocks[0].get('page')}-{blocks[-1].get('page')} "
                              f"but A2 produced no output for page(s) {list(unread)}; its blocks may "
                              f"join text from two different topics across the gap, so it is withheld "
                              f"until A2 reads those pages",
                              prompt_version=prompt_version)
                continue
            input_data = {
                "book_id": book_id, "chapter": chapter_id,
                "section_heading": info["heading_text"] or "",
                # Local 1-based numbering for THIS section only -- A2's own block numbers (n)
                # reset every page, so they are not unique across a whole chapter and can't be
                # used directly once a section spans more than one page. `page` is carried through
                # (not in A3's spec'd input_fields, but needed to compute page_start/page_end on
                # the passage records this plugin writes; see docs/OPEN_QUESTIONS.md) purely for
                # the SCRIPT half to use in _post_assembly -- it isn't anything the agent is asked
                # to act on.
                "blocks": [{"n": i + 1, "kind": b.get("kind"), "text": b.get("text"), "page": b.get("page")}
                            for i, b in enumerate(blocks)],
            }
            _write_json(_work_input_path(self.step, item_id, "runA"), input_data)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        withheld = getattr(self, "_bridged", None)
        if withheld:
            detail = ", ".join(f"{sid} (unread page{'s' if len(p) != 1 else ''} {list(p)})"
                               for sid, p in sorted(withheld))
            return ("A3 is WITHHOLDING sections that span a page A2 never read, because their "
                    f"blocks may join text from two different topics across the gap: {detail}. "
                    "Each has an A3_SECTION_SPANS_UNREAD_PAGE blocker. Run A2 on those pages "
                    "first; the sections will list themselves once the gap is closed.")
        return "A3 needs A2/A2S output (ncert/blocks/<BOOK>.jsonl); none found yet."

    @classmethod
    def _classify_heading(cls, text):
        """-> ("skip", None) for no/empty heading (the implicit opening section); ("chapter_marker",
        None) for a bare "CHAPTER N" banner (not real chapter content); ("numbered", {"number",
        "text"}) for a real numbered subsection heading (goes into ncert/chapters' `headings`
        list); ("title_candidate", text) for anything else -- in practice the chapter's own title
        banner (e.g. "SEXUAL REPRODUCTION IN FLOWERING PLANTS"), confirmed as the real shape in
        BIO12L's actual Chapter_1 opening blocks. This is a heuristic, not spec text -- logged in
        docs/OPEN_QUESTIONS.md as a judgment call."""
        text = (text or "").strip()
        if not text:
            return "skip", None
        stripped = cls._CHAPTER_PREFIX_RE.sub("", text).strip()
        if not stripped:
            return "chapter_marker", None  # was only ever "CHAPTER N", nothing else
        text = stripped  # drop a merged "CHAPTER N" prefix either way; harmless no-op when absent
        m = cls._HEADING_NUM_RE.match(text)
        if m:
            return "numbered", {"number": m.group("number"), "text": m.group("text").strip()}
        if text.strip().upper().rstrip(" :.") in cls._STRUCTURAL_HEADINGS:
            # A real, unnumbered heading, but a BOILERPLATE one -- it names a part of every
            # chapter, so it can never be this chapter's title. Kept out of title candidacy only;
            # it is still a genuine section heading and still cuts a section.
            return "structural", text
        return "title_candidate", text

    def _rebuild_chapters_file(self, book_id):
        """Spec Section 9: 'Also builds ncert/chapters/<SUBJ><CLASS>.json ... as a by-product of
        A2/A3 headings; D1 needs it.' Latest-edition only (spec 6.4's chapters contract is
        explicitly 'for the latest edition').

        Replaces an earlier incremental version that patched this file once per section as each
        section's own A3 output resolved (see docs/OPEN_QUESTIONS.md, 2026-10-10 entry): that
        version picked whichever section happened to resolve *first* as the chapter title
        (sections can resolve out of order -- parallel dispatch, retries, etc.) and then could
        never self-correct, because its 'idempotent' guard was 'only set the title if unset,'
        which locks in a wrong first guess permanently. Confirmed on real BIO12L data: Chapter
        1's title got set to "EXERCISES" (the chapter's last section) instead of "Sexual
        Reproduction in Flowering Plants" (its first section), because the exercises section's
        A3 output happened to resolve before the opening section's did.

        This version is stateless and idempotent by construction instead: every call recomputes
        the whole chapter's title + headings from scratch using `_sections()` (which is itself
        sorted into true (page, n) reading order), so title = the lowest-ordinal section's
        title-candidate heading (the chapter's own opening banner, always ordinal 1 in a
        correctly-sorted walk) and headings = every numbered heading across the chapter's
        sections, in ordinal order -- never raced, never stuck wrong, safe to call every check()."""
        if not book_id.endswith("L"):
            return
        subj_class = book_id[:-1]
        sections = self._sections()
        by_chapter = collections.defaultdict(list)
        for (b_id, chapter_num, ordinal), info in sections.items():
            if b_id != book_id:
                continue
            by_chapter[chapter_num].append((ordinal, info.get("heading_text")))

        chapters_path = rc.pp("ncert", "chapters", f"{subj_class}.json")
        rc.ensure_dir(os.path.dirname(chapters_path))
        chapters = []
        for chapter_num in sorted(by_chapter):
            entries = sorted(by_chapter[chapter_num], key=lambda t: t[0])  # by ordinal
            title = ""
            headings = []
            for ordinal, heading_text in entries:
                kind, payload = self._classify_heading(heading_text)
                if kind == "numbered":
                    if not any(h.get("number") == payload["number"] and h.get("text") == payload["text"]
                               for h in headings):
                        headings.append(payload)
                elif kind == "title_candidate" and not title:
                    # First title-candidate by ordinal order = the chapter's own opening banner.
                    title = payload
            chapter_id = f"{subj_class}-CH{chapter_num:02d}"
            existing = {c["chapter_id"]: c for c in (_read_json(chapters_path) or [])} \
                if os.path.exists(chapters_path) else {}
            older_title = existing.get(chapter_id, {}).get("older_title")
            entry = {"chapter_id": chapter_id, "title": title, "headings": headings}
            if older_title:
                entry["older_title"] = older_title  # preserve A6's later contribution, if any
            chapters.append(entry)

        _write_json(chapters_path, chapters)

    def _post_assembly(self, item_id, run_label, data, status):
        if not data or "passages" not in data:
            return
        parsed = self._parse_item_id(item_id)
        if not parsed:
            return
        book_id, chapter_num, ordinal = parsed
        input_path = _work_input_path(self.step, item_id, run_label)
        input_data = _read_json(input_path) if os.path.exists(input_path) else {}
        local_blocks = {b["n"]: b for b in (input_data.get("blocks") or [])}
        chapter_id = input_data.get("chapter") or f"{book_id[:-1]}-CH{chapter_num:02d}"
        section_heading = input_data.get("section_heading") or None

        passages_path = rc.pp("ncert", "passages", f"{book_id}.jsonl")
        for block_nums in data["passages"]:
            chosen = [local_blocks[n] for n in block_nums if n in local_blocks]
            if not chosen:
                continue
            kinds = {b.get("kind") for b in chosen}
            kind = next(iter(kinds)) if len(kinds) == 1 else "mixed"
            pages = [b.get("page") for b in chosen if b.get("page")]
            text = " ".join(b.get("text") or "" for b in chosen).strip()
            passage_id = lib_ids.next_passage_id(book_id, chapter_num)
            lib_io.append_jsonl(passages_path, {
                "passage_id": passage_id, "book_id": book_id, "chapter_id": chapter_id,
                "chapter_num": chapter_num, "section_heading": section_heading,
                "kind": kind, "page_start": min(pages) if pages else None,
                "page_end": max(pages) if pages else None,
                "text": text, "blocks": block_nums,
            })

    def check(self, filters):
        sections = self._sections()
        item_inputs = {}
        book_ids = set()
        for (book_id, chapter_num, ordinal) in sections:
            book_ids.add(book_id)
            item_id = self._item_id(book_id, chapter_num, ordinal)
            for run_label in ("retry1", "runA"):
                p = _work_input_path(self.step, item_id, run_label)
                if os.path.exists(p):
                    item_inputs[item_id] = _read_json(p)
                    break
        result = resolve_single_run_items(self.step, get_cfg(self.step), self.agent, item_inputs, {},
                                            self._post_assembly)
        for book_id in book_ids:
            self._rebuild_chapters_file(book_id)
        return result


# ===========================================================================
# A4 - Write the subtopic list (2 runs + adjudicator)
# ===========================================================================

class A4Plugin:
    step = "A4"
    agent = "a4-subtopic-writer"

    def _chapters(self):
        chapters_dir = rc.pp("ncert", "chapters")
        out = {}
        if os.path.isdir(chapters_dir):
            for fn in sorted(os.listdir(chapters_dir)):
                if fn.endswith(".json"):
                    out[fn[: -len(".json")]] = _read_json(os.path.join(chapters_dir, fn))
        return out

    def _passages_for_chapter(self, chapter_file, item_id):
        """Real passages for one latest-edition chapter, read from ncert/passages/<chapter_file>L
        .jsonl (chapter_file is the ncert/chapters/<SUBJ><CLASS>.json stem, e.g. "BIO12"; the
        latest-edition book_id is always that stem + "L", spec 6.1/6.3 naming). Returns the shape
        the a4-subtopic-writer agent file's Input section names: "id, kind, first 200 characters"
        -- field name "text" chosen for consistency with every other agent's passage-preview
        field (e.g. a5-passage-linker's passage.text), since spec 9/A4 does not name the field
        itself (judgment call, see report)."""
        book_id = f"{chapter_file}L"
        path = rc.pp("ncert", "passages", f"{book_id}.jsonl")
        if not os.path.exists(path):
            return []
        out = []
        for p in lib_io.read_jsonl(path):
            if p.get("chapter_id") == item_id:
                out.append({"id": p.get("passage_id"), "kind": p.get("kind"), "text": (p.get("text") or "")[:200]})
        return out

    @staticmethod
    def _a3_incomplete_sections(chapter_file, item_id):
        """Sections of this chapter that A3 has not split yet, or () when the chapter is done.

        `needs: A3` in config/steps.yaml was being enforced only as "A3 has produced a chapters
        file at all". That is not the same thing: A4 writes a subtopic list for ONE chapter from
        that chapter's passages, so it must not run until every section of that chapter has been
        split. Without this gate the step offered real work on BIO11L-ch02 with 6 of its 20
        sections done, and the agent would have derived a chapter's subtopics from under a third
        of its text -- output that looks valid, passes its own schema, and is quietly wrong.

        A3's item ids are `<BOOK>-ch<NN>-s<NN>` and a chapter_id here is `<SUBJ><CLASS>-CH<NN>`
        (e.g. BIO11-CH01 -> BIO11L-ch01), so the two are matched on the book+chapter prefix.
        Work-input files are the source of truth for "which sections exist", because A3's own
        list_items writes one per section before any agent runs.
        """
        m = re.match(r"(.+?)-CH(\d+)$", item_id or "", re.I)
        if not m:
            return ()
        prefix = f"{chapter_file}L-ch{int(m.group(2)):02d}-s"
        work_dir = rc.pp("steps", "A3", "work")
        out_dir = rc.pp("steps", "A3", "out")
        if not os.path.isdir(work_dir):
            return ()
        pending = []
        for fn in os.listdir(work_dir):
            if not fn.startswith(prefix) or not fn.endswith(".input.json"):
                continue
            sec = fn.split(".")[0]
            done = any(os.path.exists(os.path.join(out_dir, f"{sec}.{r}.json"))
                       for r in ("runA", "retry1", "retry2"))
            if not done:
                pending.append(sec)
        return tuple(sorted(pending))

    def list_items(self, filters):
        chapters = self._chapters()
        if not chapters:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        self._held_back = []
        for chapter_file, chapter_data in chapters.items():
            for chapter in chapter_data if isinstance(chapter_data, list) else [chapter_data]:
                item_id = chapter.get("chapter_id", chapter_file)
                if not rc.item_passes_filters(item_id, filters):
                    continue
                status = rc.read_item_status(self.step, item_id)
                if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                    continue
                unsplit = self._a3_incomplete_sections(chapter_file, item_id)
                if unsplit:
                    # Hold the chapter back rather than hand over a partial passage set.
                    self._held_back.append((item_id, len(unsplit)))
                    continue
                passages = self._passages_for_chapter(chapter_file, item_id)
                for run_label in ("runA", "runB"):
                    if rc.read_pending(self.step, f"{item_id}:{run_label}") or \
                            os.path.exists(_out_path(self.step, item_id, run_label)):
                        continue
                    input_data = {"chapter": item_id, "chapter_title": chapter.get("title", ""),
                                   "headings": chapter.get("headings", []), "passages": passages}
                    _write_json(_work_input_path(self.step, item_id, run_label), input_data)
                    lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, run_label)),
                                            _relpath(_out_path(self.step, item_id, run_label)), run_label))
        return lines

    def list_reason(self):
        if not self._chapters():
            return "A4 needs A3 output (ncert/chapters/<SUBJ><CLASS>.json); none found yet."
        held = getattr(self, "_held_back", None)
        if held:
            detail = ", ".join(f"{cid} ({n} section{'s' if n != 1 else ''} unsplit)"
                               for cid, n in sorted(held))
            return ("A4 is holding every remaining chapter back because A3 has not finished it: "
                    f"{detail}. A subtopic list must be written from a chapter's COMPLETE passage "
                    "set, so these will list themselves once A3 is done -- run A3 to DONE first.")
        return "A4: every chapter already has runA+runB output on disk (or is resolved/awaiting adjudication) -- nothing fresh to list."

    # -----------------------------------------------------------------
    # Real 2-run merge + adjudicator (spec 9/A4 Procedure/Checks/On failure), following the
    # same real-dispatch adjudicator shape as C1Plugin._start_adjudicator/_resolve_after_
    # adjudication (the most complete precedent in this file for "write an x-adjudicator work
    # file now, apply its real output on a later --check call") and A6Plugin/pair_passages.py's
    # own "script matches most pairs, adjudicator only for what the script can't decide" split.
    # -----------------------------------------------------------------

    @staticmethod
    def _norm_heading(h):
        return (h or "").strip().lower()

    @staticmethod
    def _jaccard(a, b):
        a, b = set(a or []), set(b or [])
        if not a and not b:
            return 0.0
        return len(a & b) / len(a | b)

    def _match_subtopics(self, subs_a, subs_b):
        """Greedy best-match pairing between run A's and run B's draft subtopic lists, by passage-
        set Jaccard overlap (spec 9/A4 Procedure: "SCRIPT matches subtopics by heading and passage
        overlap"). Threshold 0.5 ("mostly the same passages") counts as a real script-level match
        -- spec gives no exact number, so this is a judgment call (see report); heading equality
        is used only as a tie-breaker among candidates already above the passage-overlap floor,
        since two runs can legitimately phrase/number a heading differently while covering the
        same passages. Returns (pairs: list[(i, j, score)], unmatched_a: set[int], unmatched_b:
        set[int])."""
        scored = []
        for i, sa in enumerate(subs_a or []):
            for j, sb in enumerate(subs_b or []):
                score = self._jaccard(sa.get("passages"), sb.get("passages"))
                if score >= 0.5:
                    same_heading = self._norm_heading(sa.get("from_heading")) == self._norm_heading(sb.get("from_heading"))
                    scored.append((score, same_heading, i, j))
        scored.sort(key=lambda t: (t[0], t[1]), reverse=True)
        used_a, used_b, pairs = set(), set(), []
        for score, _same, i, j in scored:
            if i in used_a or j in used_b:
                continue
            used_a.add(i)
            used_b.add(j)
            pairs.append((i, j, score))
        unmatched_a = set(range(len(subs_a or []))) - used_a
        unmatched_b = set(range(len(subs_b or []))) - used_b
        return pairs, unmatched_a, unmatched_b

    def _direct_merge(self, subs_a, subs_b, pairs, unmatched_a, unmatched_b):
        """Deterministic script-only merge used both for a clean full match and as the documented
        safe default ("adjudicator-merged list", config/steps.yaml A4 safe_default) when the
        adjudicator itself comes back unsure: matched pairs take run A's name/from_heading
        (judgment call -- spec doesn't say which side's wording wins on a match; run A is treated
        as canonical by convention, same as A8's adjudicator precedent never preferring a run "for
        being first" only applies to genuine disagreements, not a script-level agreement) with the
        union of both runs' passage ids (guarantees full coverage even if one run's wording missed
        a passage the other caught); unmatched subtopics from EITHER run are kept as their own
        entries rather than dropped, since dropping real agent-identified content would violate
        the A4 check's "every passage covered" rule."""
        merged = []
        for i, j, _score in pairs:
            sa, sb = subs_a[i], subs_b[j]
            passages = sorted(set(sa.get("passages") or []) | set(sb.get("passages") or []))
            merged.append({"name": sa.get("name"), "from_heading": sa.get("from_heading"), "passages": passages})
        for i in sorted(unmatched_a):
            merged.append({"name": subs_a[i].get("name"), "from_heading": subs_a[i].get("from_heading"),
                            "passages": sorted(set(subs_a[i].get("passages") or []))})
        for j in sorted(unmatched_b):
            merged.append({"name": subs_b[j].get("name"), "from_heading": subs_b[j].get("from_heading"),
                            "passages": sorted(set(subs_b[j].get("passages") or []))})
        return merged

    def _write_subtopics_file(self, item_id, merged, match_rate, adjudicated):
        """Writes ncert/subtopics/<CHAPTER>.json in the spec 6.4 shape: {chapter_id, version,
        approval, subtopics:[{subtopic_id, name, from_heading, description, passages}]}.
        subtopic_id = "<chapter>-ST<nn>" (matches the A5 fixture's own example id shape,
        tests/test_checks_fixtures.py FIXTURES["A5"]: "BIO12-CH06-ST01"). The agent output has no
        `description` field (a4-subtopic-writer.md's Output block only gives n/name/from_heading/
        passages); since A5's own Input contract wants "name, and short descriptions" for each
        subtopic it shows the linker agent, and spec 9/A4 does not say how the script should
        synthesise one, this build reuses `name` as `description` too (judgment call, see
        report) rather than fabricating prose beyond what either run actually wrote."""
        subtopics = []
        for n, s in enumerate(merged, start=1):
            subtopics.append({
                "subtopic_id": f"{item_id}-ST{n:02d}",
                "name": s.get("name"),
                "from_heading": s.get("from_heading"),
                "description": s.get("name"),
                "passages": s.get("passages") or [],
            })
        payload = {"chapter_id": item_id, "version": 1, "approval": "pending", "subtopics": subtopics}
        _write_json(rc.pp("ncert", "subtopics", f"{item_id}.json"), payload)
        return payload

    def _run_check(self, item_id, chapter_file, data):
        if isinstance(data, dict) and "error" in data:
            return False, f"agent reported error: {data['error']}"
        ok, msg = rc.validate_schema(self.step, data)
        if not ok:
            return False, msg
        all_ids = [p["id"] for p in self._passages_for_chapter(chapter_file, item_id)]
        context = {"item_id": item_id, "step": self.step, "input_data": {"all_passage_ids": all_ids}}
        return rc.run_step_check(self.step, data, context)

    def _start_adjudicator(self, item_id, chapter, data_a, data_b, prompt_version):
        payload = {
            "step": "A4",
            "task": "Run A and run B each drafted this chapter's NEET-testable subtopic list "
                     "independently. They disagree (some subtopics in one run have no clear "
                     "passage-overlap match in the other). Decide the single correct merged list.",
            "allowed_values": {
                "choice": ["A", "B", "combined", "unsure"],
                "A": "run A's list is correct as-is",
                "B": "run B's list is correct as-is",
                "combined": "neither list alone is right; value.subtopics gives the merged list "
                             "([{name, from_heading, passages}], every chapter passage covered)",
                "unsure": "cannot decide -- the script will fall back to a union of both runs",
            },
            # The passages MUST be here. x-adjudicator.md defines `evidence` as "the same input
            # the step's agent saw", and A4's agents see `passages` -- id, kind and the first 200
            # characters of each. Sending only the chapter title and headings left the adjudicator
            # deciding how to group 52 passages while unable to read any of them: it could compare
            # the two runs' groupings against each other and against the section structure, but
            # never against the text being grouped. The BIO12-CH02 adjudicator noticed the gap
            # itself and recorded its confidence as medium because of it.
            #
            # Rebuilt from ncert/passages/ rather than passed down, because by the time a dispute
            # is adjudicated the run inputs may have been regenerated; reading the passage store
            # gives the adjudicator exactly what the agents were given.
            "evidence": {"chapter": item_id, "chapter_title": chapter.get("title", ""),
                          "headings": chapter.get("headings", []),
                          "passages": self._passages_for_chapter(
                              item_id.split("-CH")[0] if "-CH" in item_id else item_id, item_id)},
            "run_a": data_a.get("subtopics"), "run_b": data_b.get("subtopics"),
            "failed_check": "run A and run B subtopic lists do not fully match by passage overlap",
        }
        _write_json(_work_input_path(self.step, item_id, "adjudicated"), payload)
        rc.write_pending(self.step, item_id, {"stage": "adjudicating"})
        return [ListLine(item_id, "x-adjudicator",
                           _relpath(_work_input_path(self.step, item_id, "adjudicated")),
                           _relpath(_out_path(self.step, item_id, "adjudicated")), "adjudicated")]

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        chapters = self._chapters()
        new_lines = []
        for chapter_file, chapter_data in chapters.items():
            for chapter in chapter_data if isinstance(chapter_data, list) else [chapter_data]:
                item_id = chapter.get("chapter_id", chapter_file)
                if not rc.item_passes_filters(item_id, filters):
                    continue
                existing = rc.read_item_status(self.step, item_id)
                if existing and existing.get("status") != "stale" and existing.get("prompt_version") == prompt_version:
                    continue

                # Keyed off the adjudication work-input file's existence (not the pending marker
                # alone, which write_item_status clears once resolved) so a rerun after the
                # status file is deleted/stale doesn't re-dispatch a fresh adjudicator call for a
                # chapter that already has one in flight or already resolved -- same idempotency
                # requirement as every other step (spec 5.9).
                if os.path.exists(_work_input_path(self.step, item_id, "adjudicated")):
                    adj_path = _out_path(self.step, item_id, "adjudicated")
                    if not os.path.exists(adj_path):
                        continue  # still waiting on the adjudicator
                    adj_data = _read_json(adj_path)
                    run_a = _read_json(_out_path(self.step, item_id, "runA"))
                    run_b = _read_json(_out_path(self.step, item_id, "runB"))
                    choice = adj_data.get("choice")
                    started = ended = rc.now_iso()
                    if choice == "A":
                        merged = [{"name": s.get("name"), "from_heading": s.get("from_heading"),
                                   "passages": s.get("passages") or []} for s in run_a.get("subtopics", [])]
                        note = "adjudicator chose run A"
                    elif choice == "B":
                        merged = [{"name": s.get("name"), "from_heading": s.get("from_heading"),
                                   "passages": s.get("passages") or []} for s in run_b.get("subtopics", [])]
                        note = "adjudicator chose run B"
                    elif choice == "combined" and isinstance((adj_data.get("value") or {}).get("subtopics"), list) \
                            and (adj_data.get("value") or {}).get("subtopics"):
                        merged = [{"name": s.get("name"), "from_heading": s.get("from_heading"),
                                   "passages": s.get("passages") or []} for s in adj_data["value"]["subtopics"]]
                        note = "adjudicator combined both runs"
                    else:  # unsure (or an out-of-contract value) -> documented safe default: union merge
                        pairs, un_a, un_b = self._match_subtopics(run_a.get("subtopics", []), run_b.get("subtopics", []))
                        merged = self._direct_merge(run_a.get("subtopics", []), run_b.get("subtopics", []), pairs, un_a, un_b)
                        note = f"adjudicator {choice or 'unsure'} -- used safe-default union merge"
                    # Severity still escalates on the original run A/run B match rate (spec 9/A4:
                    # "high if run A/run B match rate < 70%"), independent of how the adjudicator
                    # resolved it -- a disagreement that reached the adjudicator because the two
                    # drafts barely overlapped is exactly the case this escalation is for.
                    _pairs0, _un_a0, _un_b0 = self._match_subtopics(run_a.get("subtopics", []), run_b.get("subtopics", []))
                    denom0 = max(len(run_a.get("subtopics", [])), len(run_b.get("subtopics", [])), 1)
                    match_rate0 = len(_pairs0) / denom0
                    severity = "high" if match_rate0 < 0.70 else "normal"
                    self._write_subtopics_file(item_id, merged, match_rate=match_rate0, adjudicated=True)
                    rc.raise_flag("item", item_id, self.step, "A4_SUBTOPICS_DRAFT",
                                   severity, f"match_rate={match_rate0:.2f}; {note}",
                                   provisional_value={"adjudicated": True, "choice": choice, "match_rate": match_rate0},
                                   prompt_version=prompt_version)
                    rc.write_item_status(self.step, item_id, "flagged", prompt_version,
                                           extra={"check_message": note})
                    rc.append_run_log(item_id, self.step, "adjudicated", "x-adjudicator", prompt_version,
                                        started, ended, "pass", note, None, "flagged")
                    continue

                run_a_path = _out_path(self.step, item_id, "runA")
                run_b_path = _out_path(self.step, item_id, "runB")
                if not (os.path.exists(run_a_path) and os.path.exists(run_b_path)):
                    continue  # still waiting on one of the two runs
                data_a, data_b = _read_json(run_a_path), _read_json(run_b_path)
                ok_a, msg_a = self._run_check(item_id, chapter_file, data_a)
                ok_b, msg_b = self._run_check(item_id, chapter_file, data_b)
                started = ended = rc.now_iso()

                if not (ok_a and ok_b):
                    # One (or both) runs failed their own per-run check. Spec 9/A4 "On failure:
                    # retry once; adjudicator." This build does not implement a second retry
                    # dispatch for a 2-run step (no real run ever needed it -- both real agent
                    # dispatches passed their own check, see report); the honest fallback actually
                    # exercised here is to proceed with whichever run(s) did pass, same spirit as
                    # A8Plugin's existing precedent of degrading gracefully on a single bad run
                    # rather than blocking the whole chapter.
                    if ok_a and not ok_b:
                        merged = [{"name": s.get("name"), "from_heading": s.get("from_heading"),
                                   "passages": s.get("passages") or []} for s in data_a.get("subtopics", [])]
                        note = f"run B invalid ({msg_b}); used run A only"
                    elif ok_b and not ok_a:
                        merged = [{"name": s.get("name"), "from_heading": s.get("from_heading"),
                                   "passages": s.get("passages") or []} for s in data_b.get("subtopics", [])]
                        note = f"run A invalid ({msg_a}); used run B only"
                    else:
                        rc.write_item_status(self.step, item_id, "blocked", prompt_version,
                                               extra={"check_message": f"runA: {msg_a}; runB: {msg_b}"})
                        rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version,
                                            started, ended, "fail", f"runA: {msg_a}; runB: {msg_b}", None, "blocked")
                        continue
                    self._write_subtopics_file(item_id, merged, match_rate=None, adjudicated=False)
                    rc.raise_flag("item", item_id, self.step, "A4_SUBTOPICS_DRAFT",
                                   "high", note,
                                   provisional_value={"run_a_ok": ok_a, "run_b_ok": ok_b},
                                   prompt_version=prompt_version)
                    rc.write_item_status(self.step, item_id, "flagged", prompt_version,
                                           extra={"check_message": note})
                    rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version,
                                        started, ended, "pass", note, None, "flagged")
                    continue

                subs_a, subs_b = data_a.get("subtopics", []), data_b.get("subtopics", [])
                pairs, unmatched_a, unmatched_b = self._match_subtopics(subs_a, subs_b)
                denom = max(len(subs_a), len(subs_b), 1)
                match_rate = len(pairs) / denom

                if not unmatched_a and not unmatched_b:
                    # Full one-to-one match: SCRIPT merges directly, no adjudicator needed (spec
                    # 9/A4: adjudicator is only for "disagreements").
                    merged = self._direct_merge(subs_a, subs_b, pairs, unmatched_a, unmatched_b)
                    self._write_subtopics_file(item_id, merged, match_rate, adjudicated=False)
                    severity = "high" if match_rate < 0.70 else "normal"
                    note = f"match_rate={match_rate:.2f}; script-merged (full match)"
                    rc.raise_flag("item", item_id, self.step, "A4_SUBTOPICS_DRAFT", severity, note,
                                   provisional_value={"match_rate": match_rate, "adjudicated": False},
                                   prompt_version=prompt_version)
                    rc.write_item_status(self.step, item_id, "flagged", prompt_version,
                                           extra={"check_message": note, "match_rate": match_rate})
                    rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version,
                                        started, ended, "pass", note, None, "flagged")
                else:
                    # Real disagreement (unmatched subtopics on at least one side) -> adjudicator,
                    # per chapter (spec 9/A4 item unit), carrying both full draft lists.
                    rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version,
                                        started, ended, "pass",
                                        f"match_rate={match_rate:.2f}; disagreement -> adjudicator",
                                        None, "pending")
                    new_lines.extend(self._start_adjudicator(item_id, chapter, data_a, data_b, prompt_version))
        return new_lines


# ===========================================================================
# A5 - Link passages to subtopics (hybrid: script copies A4 for latest; agent for undecided older)
# ===========================================================================

class A5Plugin:
    step = "A5"
    agent = "a5-passage-linker"

    def _older_book_ids(self):
        passages_dir = rc.pp("ncert", "passages")
        if not os.path.isdir(passages_dir):
            return []
        return sorted(fn[: -len(".jsonl")] for fn in os.listdir(passages_dir) if fn.endswith("O.jsonl"))

    def _chapter_id_for_passage(self, passage_id):
        # BIO12O-CH06-P01 -> BIO12-CH06 (drop the edition letter, keep SUBJ+CLASS+CH).
        book_part, rest = passage_id.split("-", 1)  # "BIO12O", "CH06-P01"
        subj_class = book_part[:-1]  # drop trailing edition letter (L/O/M)
        chapter_part = rest.split("-", 1)[0]  # "CH06"
        return f"{subj_class}-{chapter_part}"

    def _subtopics_for_chapter(self, chapter_id):
        path = rc.pp("ncert", "subtopics", f"{chapter_id}.json")
        if not os.path.exists(path):
            return []
        data = _read_json(path)
        return [{"id": s["subtopic_id"], "name": s.get("name"), "description": s.get("description")}
                for s in data.get("subtopics", [])]

    def _undecided_older_passages(self):
        """Older-edition passages the SCRIPT half (identical-heading-text match) could not
        resolve: every passage in ncert/passages/<BOOK-O>.jsonl with no row yet in
        ncert/links/<BOOK-O>.jsonl for it. (The real heading-match itself is the other build
        pass's A3/A2 domain, already reflected in ncert/links/*.jsonl by the time this runs --
        this plugin only looks at what's left unlinked.)"""
        out = {}
        for book_id in self._older_book_ids():
            passages = list(lib_io.read_jsonl(rc.pp("ncert", "passages", f"{book_id}.jsonl")))
            links = list(lib_io.read_jsonl(rc.pp("ncert", "links", f"{book_id}.jsonl")))
            linked_ids = {link["passage_id"] for link in links}
            for p in passages:
                if p["passage_id"] not in linked_ids:
                    out[p["passage_id"]] = p
        return out

    def list_items(self, filters):
        pending = self._undecided_older_passages()
        if not pending:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for passage_id, passage in pending.items():
            item_id = passage_id
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            chapter_id = self._chapter_id_for_passage(passage_id)
            input_data = {
                "passage": {"id": passage_id, "edition": "older", "kind": passage.get("kind"),
                             "text": passage.get("text")},
                "subtopics": self._subtopics_for_chapter(chapter_id),
            }
            _write_json(_work_input_path(self.step, item_id, "runA"), input_data)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        if not self._older_book_ids():
            return "A5: no ncert/passages/<BOOK-O>.jsonl found yet (needs A3 on the older edition)."
        return ("A5: every older-edition passage already has an ncert/links/<BOOK-O>.jsonl row "
                "(SCRIPT heading match resolved them all) -- nothing left needing the agent.")

    def _latest_book_ids(self):
        passages_dir = rc.pp("ncert", "passages")
        if not os.path.isdir(passages_dir):
            return []
        return sorted(fn[: -len(".jsonl")] for fn in os.listdir(passages_dir) if fn.endswith("L.jsonl"))

    def auto(self, filters):
        """Real SCRIPT half for latest-edition passages (spec 9/A5 Procedure: "latest passages:
        copy A4's assignment"). Previously a stub (see git history / report) that printed a
        message and did nothing; A4 never used to produce ncert/subtopics/<CHAPTER>.json for real
        so there was nothing to copy from. Now that A4Plugin.check() writes that file for real,
        this reads each chapter's subtopic list and, for every one of its latest-edition passages,
        appends an ncert/links/<BOOK>.jsonl row: {passage_id, subtopic_id, method}. method="heading"
        -- spec 6.4's enum is heading|agent|adjudicated and does not have a distinct "copied from
        A4" value; "heading" is the closest fit since A4 itself drew subtopics from the book's own
        headings (judgment call, see report). Idempotent: skips any passage_id already present in
        the book's links file.

        Older-edition passages are NOT handled here -- those go through list_items/check below
        (SCRIPT heading-text match where decidable, agent only when it isn't), matching
        config/steps.yaml's "script | a5-passage-linker" split exactly.
        """
        for book_id in self._latest_book_ids():
            if not rc.item_passes_filters(book_id, filters):
                continue
            passages_path = rc.pp("ncert", "passages", f"{book_id}.jsonl")
            links_path = rc.pp("ncert", "links", f"{book_id}.jsonl")
            existing_links = list(lib_io.read_jsonl(links_path))
            already_linked = {row["passage_id"] for row in existing_links}
            passages = list(lib_io.read_jsonl(passages_path))

            # chapter_id -> {passage_id: subtopic_id}, read fresh per book so a chapter whose A4
            # hasn't finished yet (no ncert/subtopics/<CHAPTER>.json) is simply skipped this round
            # (idempotent: will be picked up on a later --auto call once A4 catches up).
            subtopics_cache = {}
            written = 0
            for p in passages:
                passage_id = p.get("passage_id")
                if passage_id in already_linked:
                    continue
                chapter_id = p.get("chapter_id")
                if chapter_id not in subtopics_cache:
                    st_path = rc.pp("ncert", "subtopics", f"{chapter_id}.json")
                    subtopics_cache[chapter_id] = _read_json(st_path) if os.path.exists(st_path) else None
                chapter_subs = subtopics_cache[chapter_id]
                if not chapter_subs:
                    continue  # A4 not done yet for this chapter
                subtopic_id = "none"
                for s in chapter_subs.get("subtopics", []):
                    if passage_id in (s.get("passages") or []):
                        subtopic_id = s.get("subtopic_id")
                        break
                lib_io.append_jsonl(links_path, {"passage_id": passage_id, "subtopic_id": subtopic_id, "method": "heading"})
                already_linked.add(passage_id)
                written += 1
            if written:
                print(f"A5 --auto: wrote {written} link row(s) to {_relpath(links_path)}", file=sys.stderr)

    def _post_assembly(self, item_id, run_label, data, status):
        if not data or "subtopic_id" not in data:
            return
        book_id = item_id.rsplit("-CH", 1)[0]
        links_path = rc.pp("ncert", "links", f"{book_id}.jsonl")
        lib_io.append_jsonl(links_path, {"passage_id": item_id, "subtopic_id": data["subtopic_id"], "method": "agent"})

    def check(self, filters):
        """Known simplification (see report): A5's real fallback chain is unsure -> ADJUDICATOR
        -> still unsure -> safe default "none" + A5_UNSURE (no retry rung at all -- its
        config/steps.yaml fallback is just ["adjudicator"]). resolve_single_run_items only knows
        retry-then-safe-default (no adjudicator hop); since "retry" isn't in A5's fallback list it
        correctly skips straight to safe-default resolution on a failing check, but that means an
        unsure A5 run resolves to "none" one step earlier than spec 9/A5 intends (skipping the
        adjudicator). A real fix needs a second generic resolver (single-run-then-adjudicator, no
        retry) alongside this one; not built given no real upstream data exists yet to exercise an
        actual A5 disagreement end to end."""
        pending = self._undecided_older_passages()
        item_inputs = {}
        for passage_id in pending:
            for run_label in ("retry1", "runA"):
                p = _work_input_path(self.step, passage_id, run_label)
                if os.path.exists(p):
                    item_inputs[passage_id] = _read_json(p)
                    break
        return resolve_single_run_items(self.step, get_cfg(self.step), self.agent, item_inputs, {},
                                          self._post_assembly)


# ===========================================================================
# A6 - Pair old and new passages (hybrid: pair_passages.py + x-adjudicator for weak pairs)
# ===========================================================================

class A6Plugin:
    step = "A6"
    agent = "x-adjudicator"

    def _chapter_ids_in_scope(self, filters):
        chapters_dir = rc.pp("ncert", "chapters")
        ids_ = []
        if os.path.isdir(chapters_dir):
            for fn in os.listdir(chapters_dir):
                if fn.endswith(".json"):
                    for ch in _read_json(os.path.join(chapters_dir, fn)) or []:
                        cid = ch.get("chapter_id")
                        if cid and rc.item_passes_filters(cid, filters):
                            ids_.append(cid)
        return sorted(set(ids_))

    def auto(self, filters):
        script = rc.pp("scripts", "pair_passages.py")
        if not os.path.exists(script):
            print(f"A6 --auto: {script} does not exist yet (owned by a parallel build pass, "
                  "see scripts/CONVENTIONS.md). Nothing to run.", file=sys.stderr)
            return
        for chapter_id in self._chapter_ids_in_scope(filters):
            started = rc.now_iso()
            result = subprocess.run([sys.executable, script, "--chapter-id", chapter_id], cwd=rc.pp())
            ended = rc.now_iso()
            prompt_version = rc.get_prompt_version(self.step)
            status = "pass" if result.returncode == 0 else "blocked"
            rc.append_run_log(chapter_id, self.step, "runA", None, prompt_version, started, ended,
                                "pass" if result.returncode == 0 else "fail",
                                f"exit code {result.returncode}", None, status)

    def list_items(self, filters):
        """Weak/unresolved pairs left behind by pair_passages.py, needing x-adjudicator."""
        lines = []
        for chapter_id in self._chapter_ids_in_scope(filters):
            pairs_path = rc.pp("ncert", "pairs", f"{chapter_id}.json")
            if not os.path.exists(pairs_path):
                continue
            pairs = _read_json(pairs_path)
            for i, row in enumerate(pairs):
                if row.get("result") == "pair" and row.get("adjudicated") is False and \
                        0.50 <= row.get("similarity", 1.0) < 0.85:
                    item_id = f"{chapter_id}-pair{i:03d}"
                    if os.path.exists(_out_path(self.step, item_id, "adjudicated")):
                        continue
                    input_data = {"step": "A6", "old_passage_id": row.get("old_passage_id"),
                                   "new_passage_id": row.get("new_passage_id"),
                                   "similarity": row.get("similarity")}
                    _write_json(_work_input_path(self.step, item_id, "adjudicated"), input_data)
                    lines.append(ListLine(item_id, self.agent,
                                            _relpath(_work_input_path(self.step, item_id, "adjudicated")),
                                            _relpath(_out_path(self.step, item_id, "adjudicated")), "adjudicated"))
        return lines

    def list_reason(self):
        return "A6: nothing in ncert/pairs/<CHAPTER>.json yet (needs pair_passages.py --auto first)."

    def check(self, filters):
        """Validates ncert/pairs/<CHAPTER>.json (pair_passages.py's real output, spec 6.4) against
        schemas/A6.json + scripts/checks/A6.py, per chapter in scope. Any x-adjudicator output for
        a weak pair is expected to patch that chapter's ncert/pairs/<CHAPTER>.json in place before
        the next --check call (not modelled as a separate per-pair output file here, since A6's
        real artifact is the one whole-chapter file -- see scripts/checks/A6.py's docstring)."""
        prompt_version = rc.get_prompt_version(self.step)
        for chapter_id in self._chapter_ids_in_scope(filters):
            existing = rc.read_item_status(self.step, chapter_id)
            if existing and existing.get("prompt_version") == prompt_version:
                continue
            pairs_path = rc.pp("ncert", "pairs", f"{chapter_id}.json")
            if not os.path.exists(pairs_path):
                continue
            started = rc.now_iso()
            data = _read_json(pairs_path)
            ok, msg = rc.validate_schema(self.step, data)
            if ok:
                ok, msg = rc.run_step_check(self.step, data, {"item_id": chapter_id, "step": self.step})
            ended = rc.now_iso()
            weak_unresolved = sum(
                1 for row in data if isinstance(data, list) and row.get("result") == "pair"
                and not row.get("adjudicated") and 0.50 <= row.get("similarity", 1.0) < 0.85
            ) if isinstance(data, list) else 0
            status = "pass" if ok else "flagged"
            rc.write_item_status(self.step, chapter_id, status, prompt_version,
                                   extra={"check_message": msg, "weak_unresolved_pairs": weak_unresolved})
            rc.append_run_log(chapter_id, self.step, "runA", None, prompt_version, started, ended,
                                "pass" if ok else "fail", msg, None, status)
        return self.list_items(filters)


# ===========================================================================
# A7 - Find the differences (pure script)
# ===========================================================================

class A7Plugin:
    step = "A7"

    def list_items(self, filters):
        return []

    def list_reason(self):
        return "A7 is a script-only step (scripts/diff_pairs.py). Nothing to list; run `run_step.py A7 --auto`."

    def _chapter_ids_in_scope(self, filters):
        pairs_dir = rc.pp("ncert", "pairs")
        ids_ = []
        if os.path.isdir(pairs_dir):
            for fn in os.listdir(pairs_dir):
                if fn.endswith(".json"):
                    cid = fn[: -len(".json")]
                    if rc.item_passes_filters(cid, filters):
                        ids_.append(cid)
        return sorted(ids_)

    def auto(self, filters):
        script = rc.pp("scripts", "diff_pairs.py")
        if not os.path.exists(script):
            print(f"A7 --auto: {script} does not exist yet (owned by a parallel build pass, "
                  "see scripts/CONVENTIONS.md). Nothing to run.", file=sys.stderr)
            return
        for chapter_id in self._chapter_ids_in_scope(filters):
            started = rc.now_iso()
            result = subprocess.run([sys.executable, script, "--chapter-id", chapter_id], cwd=rc.pp())
            ended = rc.now_iso()
            prompt_version = rc.get_prompt_version(self.step)
            status = "pass" if result.returncode == 0 else "blocked"
            rc.append_run_log(chapter_id, self.step, "runA", None, prompt_version, started, ended,
                                "pass" if result.returncode == 0 else "fail",
                                f"exit code {result.returncode}", None, status)

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        for chapter_id in self._chapter_ids_in_scope(filters):
            diffs_path = rc.pp("ncert", "diffs", f"{chapter_id}.jsonl")
            started = ended = rc.now_iso()
            if not os.path.exists(diffs_path):
                continue
            all_ok, messages = True, []
            for line in lib_io.read_jsonl(diffs_path):
                ok, msg = rc.validate_schema(self.step, line)
                if ok:
                    ok, msg = rc.run_step_check(self.step, line, {"item_id": chapter_id, "step": self.step})
                if not ok:
                    all_ok = False
                    messages.append(msg)
            status = "pass" if all_ok else "flagged"
            rc.write_item_status(self.step, chapter_id, status, prompt_version,
                                   extra={"check_message": "; ".join(messages) or "ok"})
            rc.append_run_log(chapter_id, self.step, "runA", None, prompt_version, started, ended,
                                "pass" if all_ok else "fail", "; ".join(messages) or "ok", None, status)
        return []


# ===========================================================================
# A8 - Judge one change (2 runs + adjudicator)
# ===========================================================================

class A8Plugin:
    step = "A8"
    agent = "a8-change-judge"

    def _pairs_needing_judgement(self):
        diffs_dir = rc.pp("ncert", "diffs")
        out = {}
        if os.path.isdir(diffs_dir):
            for fn in sorted(os.listdir(diffs_dir)):
                if fn.endswith(".jsonl"):
                    chapter_id = fn[: -len(".jsonl")]
                    for i, line in enumerate(lib_io.read_jsonl(os.path.join(diffs_dir, fn))):
                        if not line.get("identical", True):
                            out[f"{chapter_id}-pair{i:03d}"] = line
        return out

    def list_items(self, filters):
        pending = self._pairs_needing_judgement()
        if not pending:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for item_id, line in pending.items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            for run_label in ("runA", "runB"):
                if os.path.exists(_out_path(self.step, item_id, run_label)):
                    continue
                old_id, new_id = line.get("pair", [None, None])
                input_data = {"old_passage": {"id": old_id}, "new_passage": {"id": new_id},
                               "diff": line.get("diff", [])}
                _write_json(_work_input_path(self.step, item_id, run_label), input_data)
                lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, run_label)),
                                        _relpath(_out_path(self.step, item_id, run_label)), run_label))
        return lines

    def list_reason(self):
        return "A8 needs A7 output (ncert/diffs/<CHAPTER>.jsonl) with non-identical pairs; none found yet."

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        pending = self._pairs_needing_judgement()
        for item_id in pending:
            existing = rc.read_item_status(self.step, item_id)
            if existing and existing.get("status") != "stale" and existing.get("prompt_version") == prompt_version:
                continue
            run_a, run_b = _out_path(self.step, item_id, "runA"), _out_path(self.step, item_id, "runB")
            if not (os.path.exists(run_a) and os.path.exists(run_b)):
                continue
            data_a, data_b = _read_json(run_a), _read_json(run_b)
            started = ended = rc.now_iso()
            ok_a, _ = rc.validate_schema(self.step, data_a)
            ok_b, _ = rc.validate_schema(self.step, data_b)
            agree = ok_a and ok_b and data_a.get("change_type") == data_b.get("change_type")
            if not agree:
                rc.raise_flag("item", item_id, self.step, "A8_ADJUDICATED",
                               flags_cat.get("A8_ADJUDICATED", "normal"),
                               f"run A: {data_a.get('change_type') if ok_a else 'invalid'}; "
                               f"run B: {data_b.get('change_type') if ok_b else 'invalid'}",
                               prompt_version=prompt_version)
            change_type = data_a.get("change_type") if agree and ok_a else "unsure"
            if change_type not in ("fact_changed", "fact_removed", "fact_added") and change_type == "wording_only" \
                    and (data_a.get("could_flip_an_answer") or (ok_b and data_b.get("could_flip_an_answer"))):
                rc.raise_flag("item", item_id, self.step, "A8_WORDING_RISK",
                               flags_cat.get("A8_WORDING_RISK", "normal"), "wording-only change could flip an answer",
                               prompt_version=prompt_version)
            elif change_type in ("fact_changed", "fact_removed", "fact_added"):
                rc.raise_flag("item", item_id, self.step, "A8_FACT_CHANGE",
                               flags_cat.get("A8_FACT_CHANGE", "normal"), f"change_type={change_type}",
                               prompt_version=prompt_version)
            status = "flagged" if change_type != "unsure" else "flagged"
            rc.write_item_status(self.step, item_id, status, prompt_version,
                                   extra={"check_message": f"change_type={change_type}"})
            rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version, started,
                                ended, "pass", f"change_type={change_type}", None, status)
        return []


# ===========================================================================
# A9 - Write the change log (pure script)
# ===========================================================================

class A9Plugin:
    step = "A9"

    def list_items(self, filters):
        return []

    def list_reason(self):
        return "A9 is a script-only step (scripts/write_change_log.py). Nothing to list; run `run_step.py A9 --auto`."

    def _chapter_ids_in_scope(self, filters):
        diffs_dir = rc.pp("ncert", "diffs")
        ids_ = []
        if os.path.isdir(diffs_dir):
            for fn in os.listdir(diffs_dir):
                if fn.endswith(".jsonl"):
                    cid = fn[: -len(".jsonl")]
                    if rc.item_passes_filters(cid, filters):
                        ids_.append(cid)
        return sorted(ids_)

    def auto(self, filters):
        script = rc.pp("scripts", "write_change_log.py")
        if not os.path.exists(script):
            print(f"A9 --auto: {script} does not exist yet (owned by a parallel build pass, "
                  "see scripts/CONVENTIONS.md). Nothing to run.", file=sys.stderr)
            return
        for chapter_id in self._chapter_ids_in_scope(filters):
            started = rc.now_iso()
            result = subprocess.run([sys.executable, script, "--chapter-id", chapter_id], cwd=rc.pp())
            ended = rc.now_iso()
            prompt_version = rc.get_prompt_version(self.step)
            status = "pass" if result.returncode == 0 else "blocked"
            rc.append_run_log(chapter_id, self.step, "runA", None, prompt_version, started, ended,
                                "pass" if result.returncode == 0 else "fail",
                                f"exit code {result.returncode}", None, status)

    def check(self, filters):
        """ncert/change_log.csv and ncert/deleted_topics.csv are shared, whole-project files
        (spec 5.8 -- unlike ncert/pairs/<CHAPTER>.json and ncert/diffs/<CHAPTER>.jsonl), but
        write_change_log.py only ever replaces one chapter's rows per run (its own docstring), so
        this validates and tracks status per chapter (the item unit spec 9/A9 actually names),
        filtering the shared CSVs down to each chapter's own rows, with real cross-reference
        counts (expected_diff_count, expected_removed_passage_ids) from that chapter's own A7/A6
        output when available."""
        prompt_version = rc.get_prompt_version(self.step)
        change_log_path = rc.pp("ncert", "change_log.csv")
        deleted_path = rc.pp("ncert", "deleted_topics.csv")
        if not (os.path.exists(change_log_path) or os.path.exists(deleted_path)):
            return []
        all_change_rows = lib_io.read_csv(change_log_path)
        all_deleted_rows = lib_io.read_csv(deleted_path)
        for row in all_change_rows:
            row["could_flip_an_answer"] = str(row.get("could_flip_an_answer", "")).strip().lower() in ("true", "1", "yes")
            row["affected_questions"] = [v for v in (row.get("affected_questions") or "").split("|") if v]

        for chapter_id in self._chapter_ids_in_scope(filters):
            existing = rc.read_item_status(self.step, chapter_id)
            if existing and existing.get("prompt_version") == prompt_version:
                continue
            started = rc.now_iso()
            chapter_change_rows = [r for r in all_change_rows if r.get("chapter_id") == chapter_id]
            chapter_deleted_rows = [r for r in all_deleted_rows if r.get("chapter_id") == chapter_id]
            combined = {"change_log_rows": chapter_change_rows, "deleted_topics_rows": chapter_deleted_rows}

            diffs_path = rc.pp("ncert", "diffs", f"{chapter_id}.jsonl")
            expected_diff_count = sum(1 for line in lib_io.read_jsonl(diffs_path) if not line.get("identical", True)) \
                if os.path.exists(diffs_path) else None
            pairs_path = rc.pp("ncert", "pairs", f"{chapter_id}.json")
            expected_removed = [row.get("old_passage_id") for row in _read_json(pairs_path) if row.get("result") == "removed"] \
                if os.path.exists(pairs_path) else None

            ok, msg = rc.validate_schema(self.step, combined)
            if ok:
                ok, msg = rc.run_step_check(self.step, combined, {
                    "item_id": chapter_id, "step": self.step,
                    "expected_diff_count": expected_diff_count,
                    "expected_removed_passage_ids": expected_removed,
                })
            ended = rc.now_iso()
            status = "pass" if ok else "flagged"
            rc.write_item_status(self.step, chapter_id, status, prompt_version, extra={"check_message": msg})
            rc.append_run_log(chapter_id, self.step, "runA", None, prompt_version, started, ended,
                                "pass" if ok else "fail", msg, None, status)
        return []


# ===========================================================================
# Stage B shared helpers
# ===========================================================================

def _b_item_id_for_relpath(relpath):
    """Deterministic item_id for a raw inputs/papers or inputs/keys file, used by B1Plugin as
    the pre-registration item identity (before a paper_id exists) -- same spirit as A1Plugin's
    ncert_item_id: the whole project-relative path, '/' -> '__', extension stripped."""
    stem = os.path.splitext(relpath.replace(os.sep, "/"))[0]
    return stem.replace("/", "__")


def _b_manifest_rows():
    return lib_io.read_csv(rc.pp("inputs", "manifest.csv"))


def _b_manifest_item_map():
    """{item_id: (relpath, manifest_row_dict)} for every inputs/manifest.csv row whose `file`
    column is set -- used by B1 to build its own candidates and by B2+ to resolve a registered
    paper_id's row["file"] (which holds this same item_id, matching register/books.csv's own
    "file = item_id, not a path" convention) back to a real PDF path on disk."""
    out = {}
    for row in _b_manifest_rows():
        relpath = row.get("file")
        if not relpath:
            continue
        out[_b_item_id_for_relpath(relpath)] = (relpath, row)
    return out


# ===========================================================================
# B1 - Register the paper (spec 10/B1; .claude/agents/b1-paper-registrar.md)
# ===========================================================================

class B1Plugin:
    step = "B1"
    agent = "b1-paper-registrar"

    def _candidate_rows(self, filters):
        out = []
        for row in _b_manifest_rows():
            if row.get("kind") not in ("paper", "key"):
                continue
            relpath = row.get("file")
            if not relpath:
                continue
            item_id = _b_item_id_for_relpath(relpath)
            if not rc.item_passes_filters(item_id, filters):
                continue
            out.append((item_id, relpath, row))
        return out

    def list_items(self, filters):
        if not rc.s0_has_run():
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for item_id, relpath, row in self._candidate_rows(filters):
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id):
                continue
            if os.path.exists(_out_path(self.step, item_id, "runA")):
                continue  # already dispatched, waiting on --check
            work_path = _work_input_path(self.step, item_id, "runA")
            if not os.path.exists(work_path):
                input_data = self._build_input(item_id, relpath, row)
                _write_json(work_path, input_data)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        if not rc.s0_has_run():
            return ("B1 needs S0 (register/intake_report.md). S0 has not produced it yet, so B1 "
                    "has nothing ready to list.")
        return ("B1: no candidate paper/key file (inputs/manifest.csv kind=paper|key) matched the "
                "given filters, or everything matching already has output pending --check.")

    #: How an official NTA key states which booklet it is for. Three real spellings, all observed:
    #:   "TEST BOOKLET CODE : A"  /  "BOOKLET CODE: A"   -- 2022-2024
    #:   "SET : A"                                        -- some sittings
    #:   "BOOK : E1"                                      -- 2020, and the word CODE never appears
    #: The third alternative was added 2026-10-13. Without it the 2020 key yielded an EMPTY code
    #: set even though page 1 plainly reads "EXAM DATE : 13.09.2020 / BOOK : E1", so every 2020
    #: paper was forced to `trust: unsure` -- reported by a B1 worker that correctly declined to
    #: upgrade 20 items with no corroboration available. The colon is REQUIRED in that branch so
    #: the bare word "book" in running prose cannot be read as a code.
    #: Two deliberate narrowings, both from a real false positive (2026-10-13):
    #:
    #: 1. The CODE ITSELF is matched case-sensitively, via `(?-i:...)`, while the surrounding
    #:    LABEL stays case-insensitive. A printed booklet code is always upper case (A, AA, E1,
    #:    M1); lower-case words are prose.
    #: 2. `SET` now REQUIRES its colon.
    #:
    #: Why: the old pattern read page 30 of the 2016 phase-2 key -- "a gene or set of genes" --
    #: as the booklet code "of", making `official_key_codes(2016, PH2)` the single-element set
    #: ['OF']. That is worse than an empty set, because a B1 worker then found a page that
    #: legitimately PRINTS "Code - AA", saw AA missing from a code set it had every reason to
    #: trust, read that as the key contradicting the page, and downgraded a case-1 `official` to
    #: `unsure`. The worker reasoned correctly from a poisoned input and flagged that ['OF'] looked
    #: "suspiciously short", which is how this was found. Either narrowing alone kills this match;
    #: both are kept because the failure mode -- noise that masquerades as authoritative
    #: corroboration -- is the most expensive one this field has.
    _B1_KEY_CODE_RE = re.compile(
        r"(?:TEST\s+)?BOOK(?:LET)?\s*CODE\s*:?\s*(?-i:([A-Z]{1,2}\d?))\b"
        r"|SET\s*:\s*(?-i:([A-Z]{1,2}\d?))\b"
        r"|\bBOOK\s*:\s*(?-i:([A-Z]{1,2}\d?))\b",
        re.IGNORECASE)

    #: A booklet code carried in a KEY FILE'S NAME, e.g. NEET_answers-key_2018-AA.pdf -> AA.
    #: Deliberately CASE-SENSITIVE (no re.IGNORECASE), because case is the only thing separating a
    #: real code from the descriptive suffixes the same directory uses: `-neet.pdf` (2019-2025),
    #: `-phase-1.pdf` (2016) and `-Re_neet.pdf` (2026) must NOT be read as the codes NEET, 1 or
    #: RE. Requiring 1-2 UPPER-case letters, an optional digit, and then `.pdf` rejects all three
    #: -- "neet" is lower case, "1" has no letter, and "Re_neet" has a letter case mix and an
    #: underscore before `.pdf`. Verified against all 30 key files actually present.
    _B1_KEY_FILENAME_CODE_RE = re.compile(r"-([A-Z]{1,2}\d?)\.pdf$")

    @classmethod
    def _official_key_codes(cls, year, sitting):
        """Every booklet code the OFFICIAL NTA key for this (year, sitting) actually prints.

        Read straight off the key PDF, so this is a fact about the authoritative document, not a
        judgement -- the agent still decides what to do with it.

        Why B1 needs it: the agent file's own GAJAHA example reasons about whether a
        folder-implied code "appears in the real key's code set", but nothing ever handed the
        agent that set, so it could only ever answer the weaker question "is this code printed on
        this page". Two real papers here (2024 code-Q1, 2022 code-Q2) are scraped renderings whose
        page furniture lost the code line, and both were therefore registered with an empty
        booklet_code -- which strands every one of their questions at B5, since _find_key_page
        needs a code to pick the key page. Checked directly: Q1 and Q2 are both genuine codes
        printed in their years' official keys (2024 prints M1-T6, 48 codes). That is independent
        corroboration from the authoritative source, which is categorically different from a
        folder name agreeing with itself.
        """
        want = (str(year), (sitting or "MAIN"))
        codes = set()
        for row in _b_manifest_rows():
            relpath = row.get("file")
            if not relpath or (row.get("kind") or "").strip() != "key":
                continue
            if (str(row.get("year") or "").strip(), (row.get("sitting") or "MAIN").strip()) != want:
                continue
            abspath = rc.pp(relpath)
            if not os.path.exists(abspath):
                continue
            for page in range(1, lib_pdf.page_count(abspath) + 1):
                for m in cls._B1_KEY_CODE_RE.finditer(lib_pdf.extract_text_layer(abspath, page) or ""):
                    # One group per alternative in _B1_KEY_CODE_RE; exactly one is set per match.
                    # Taken as a group list rather than `group(1) or group(2)` so that adding a
                    # fourth spelling later cannot silently raise AttributeError on None here.
                    hit = next((g for g in m.groups() if g), None)
                    if hit:
                        codes.add(hit.upper())
            # Some years publish ONE KEY FILE PER BOOKLET CODE, with the code only in the file
            # name and nothing resembling "Test Booklet Code: X" inside. 2018 is exactly this:
            # 22 files, NEET_answers-key_2018-AA.pdf through -ZZ.pdf. Reading only the text layer
            # therefore returned an EMPTY code set for 2018 and every 2018 paper was forced to
            # `trust: unsure`, because the agent had nothing to corroborate against -- reported by
            # a B1 worker that correctly refused to upgrade 20 items on no evidence. The code in
            # the name IS the authoritative source's own statement of which booklet the key is
            # for, so it counts, and harvesting it is parsing, not judgement.
            m = cls._B1_KEY_FILENAME_CODE_RE.search(os.path.basename(abspath))
            if m:
                codes.add(m.group(1).upper())
        return sorted(codes)

    @staticmethod
    def _key_codes_discriminating(codes):
        """Can matching a code against `codes` actually FAIL? Returns (bool, one-line reason).

        This exists because "the code is in the official key's set" sounds like corroboration and
        for several years is worth nothing at all. Most NTA years number booklets as a letter from
        a small block times a digit 1-6, and in 2020, 2021, 2023 and 2024 the key lists **every
        single combination**: 2021 is exactly M/N/O/P x 1-6 = 24 of 24, 2020 and 2024 are 48 of 48.
        A code drawn from that letter-digit space therefore matches BY CONSTRUCTION -- an invented
        suffix matches exactly as surely as a real one, so a match carries no information.

        Other years are genuinely selective and a wrong code can fail: 2018 covers 19 of the 26
        doubled letters (73%) and 2019 covers 28 of 48 (58%). That is not hypothetical -- the real
        file `neet_2018_code-QQ` was correctly left `unsure` precisely because the 2018 key runs
        AA..ZZ but skips QQ.

        Added 2026-10-13 after I told five B1 workers that a scraped slug's suffix could be
        corroborated against the key set, which was wrong for the complete-cross-product years and
        wrongly upgraded 47 items to `memory_based`. One worker pushed back, noting the agent file's
        own GAJAHA-M1 example says `unsure` and naming the items to revisit if the instruction was
        wrong. It was. The judgement is computed here rather than left to the agent, because it is
        arithmetic about the key's code space, not a reading of any page.
        """
        pairs = [c for c in codes if len(c) == 2 and c[0].isalpha() and c[1].isdigit()]
        if pairs:
            letters = {c[0] for c in pairs}
            digits = {c[1] for c in pairs}
            combos = len(letters) * len(digits)
            if combos and len(pairs) >= combos:
                return False, (
                    f"the key lists every one of the {combos} combinations of letters "
                    f"{''.join(sorted(letters))} x digits {''.join(sorted(digits))}, so ANY code of "
                    f"that shape matches by construction and a match proves nothing")
            return True, (
                f"the key lists {len(pairs)} of {combos} possible letter-digit combinations, so a "
                f"wrong code can fail this check")
        doubles = [c for c in codes if len(c) == 2 and c.isalpha()]
        if doubles:
            return True, (
                f"the key lists {len(doubles)} of the 26 doubled-letter codes, so a wrong code can "
                f"fail this check (the real file code-QQ did)")
        if not codes:
            return False, "no code set could be read from the official key for this year/sitting"
        return True, f"the key lists {len(codes)} codes"

    @classmethod
    def _key_code_fields(cls, row):
        """The official code set PLUS whether matching against it can actually fail.

        Shipped together deliberately. The set on its own reads as corroboration whatever its
        shape, and for the complete-cross-product years that reading is wrong -- see
        `_key_codes_discriminating`. Handing the agent the caveat in the same breath as the data
        is the only way it can weigh case 2 of the three-way booklet-code rule honestly.
        """
        codes = cls._official_key_codes(row.get("year"), row.get("sitting"))
        ok, why = cls._key_codes_discriminating(codes)
        return {
            "official_key_codes": codes,
            "official_key_codes_can_fail": ok,
            "official_key_codes_note": why,
        }

    def _build_input(self, item_id, relpath, row):
        """Section 10/B1 Reads: 'cover page and first question page images; their text layer; the
        manifest row.' The real scraped papers in this project have no separate NTA-style cover
        page -- page 1 already carries both the site's paper-identity banner (title, code, date
        text) AND question 1's full card, overlay included (confirmed by direct inspection,
        docs/OPEN_QUESTIONS.md 2026-10-11 B-stage build). So both page_images[0] (cover-equivalent)
        and page_images[1] (first question page) come from the same real file's pages 1-2.

        Per this task's brief and the Master Plan's risk #1 fix: text_layer is never the raw
        page text -- every page's text layer is run through scrape_sanitize.strip_overlay_text
        before the agent ever sees it, even though B1's own job (cover identity, not question
        content) would survive contamination either way; sanitizing here is cheap and keeps the
        rule ("clean any text-layer content before it's handed to a B-stage agent") uniform rather
        than quietly making an exception for the one step where it technically wouldn't matter."""
        work_dir = rc.pp("steps", self.step, "work")
        rc.ensure_dir(work_dir)
        abspath = rc.pp(relpath)
        n_pages = min(2, lib_pdf.page_count(abspath))
        page_images, text_layer = [], []
        for p in range(1, n_pages + 1):
            png_path = os.path.join(work_dir, f"{item_id}_p{p}.png")
            lib_pdf.render_page_to_png(abspath, p, out_path=png_path)
            page_images.append(_relpath(png_path))
            raw_text = lib_pdf.extract_text_layer(abspath, p)
            clean_text, _n_stripped = scrape_sanitize.strip_overlay_text(raw_text)
            text_layer.append(clean_text)
        return {
            "file": relpath.replace(os.sep, "/"),
            "manifest_row": row,
            "page_images": page_images,
            "text_layer": text_layer,
            **self._key_code_fields(row),
        }

    def _post_assembly(self, item_id, run_label, data, status):
        if not data or "file_kind" not in data:
            return
        input_path = _work_input_path(self.step, item_id, run_label)
        input_data = _read_json(input_path) if os.path.exists(input_path) else {}
        manifest_row = input_data.get("manifest_row") or {}

        sitting = data.get("sitting")
        if sitting not in lib_ids.SITTINGS:
            # Agent rule: "sitting follows the printed cover; if the cover doesn't say, use the
            # manifest and say so in note" -- 'unsure' or an invalid value both fall back here.
            sitting = manifest_row.get("sitting") or "MAIN"

        booklet_code = data.get("booklet_code") or ""
        # make_paper_id needs *some* code to build a stable id even when the agent correctly
        # refuses to confirm one (trust: unsure, booklet_code ""); falling back to the manifest's
        # folder-derived code for ID CONSTRUCTION ONLY -- never for the row's own `booklet_code`
        # column, which stays exactly what the agent found (possibly empty) -- keeps the register
        # row honest per the agent file's "Never promote a folder/filename-implied code" rule
        # while still giving the paper a usable, stable id. Judgment call, see report.
        code_for_id = booklet_code or manifest_row.get("booklet_code") or "X"
        year = data.get("year") or manifest_row.get("year")
        try:
            year_int = int(year)
        except (TypeError, ValueError):
            return
        try:
            paper_id = lib_ids.make_paper_id(year_int, sitting, code_for_id)
        except ValueError:
            return

        papers_path = rc.pp("register", "papers.csv")
        rows = lib_io.read_csv(papers_path)
        fieldnames = ["paper_id", "file_kind", "exam", "year", "sitting", "booklet_code",
                      "language", "trust", "source", "file", "in_scope", "status"]
        in_scope = "yes" if year_int in sittings.IN_SCOPE_YEARS else "no"
        new_row = {
            "paper_id": paper_id, "file_kind": data.get("file_kind", ""),
            "exam": data.get("exam", ""), "year": year_int, "sitting": sitting,
            "booklet_code": booklet_code, "language": data.get("language", "English"),
            "trust": data.get("trust", "unsure"), "source": manifest_row.get("source", ""),
            "file": item_id, "in_scope": in_scope, "status": status,
        }
        # One row per FILE (spec Checks 1): a paper file and its matching key file share the same
        # paper_id (it names the (year, sitting, code) paper, not the file), distinguished by
        # file_kind -- so the dedup key is (paper_id, file_kind), not paper_id alone.
        #
        # REPLACE the existing row rather than returning early. The early return made this
        # register append-only, so a legitimate B1 RE-RUN could never correct a row it had
        # already written: the new agent output was read, validated, and then silently dropped.
        # Hit for real on NEET-2024-MAIN-Q1 and NEET-2022-MAIN-Q2 -- a re-run under the revised
        # booklet-code rule produced the codes Q1/Q2 with `trust: memory_based`, --check reported
        # DONE, and the register still read `booklet_code` empty / `trust: unsure`, which left all
        # 398 of their questions stranded at B5 exactly as before. A step whose output cannot
        # reach the register is indistinguishable from a step that never ran, and the failure is
        # invisible because nothing errors.
        #
        # Matching on (paper_id, file_kind) keeps the one-row-per-file rule: the row is rewritten
        # in place, never duplicated, and never appended alongside its own earlier version.
        for i, r in enumerate(rows):
            if r.get("paper_id") == paper_id and r.get("file_kind") == data.get("file_kind"):
                rows[i] = new_row
                break
        else:
            rows.append(new_row)
        lib_io.write_csv(papers_path, rows, fieldnames)

    def check(self, filters):
        item_inputs = {}
        for item_id, relpath, row in self._candidate_rows(filters):
            for run_label in ("retry1", "runA"):
                p = _work_input_path(self.step, item_id, run_label)
                if os.path.exists(p):
                    item_inputs[item_id] = _read_json(p)
                    break
        return resolve_single_run_items(
            self.step, get_cfg(self.step), self.agent, item_inputs, {},
            self._post_assembly, always_flag_codes=["B1_REGISTER_DRAFT"],
        )


# ===========================================================================
# B2 - Find question boundaries (spec 10/B2; .claude/agents/b2-boundary-finder.md)
# ===========================================================================

class B2Plugin:
    step = "B2"
    agent = "b2-boundary-finder"

    _ITEM_ID_RE = re.compile(r"^(?P<paper_id>.+)-p(?P<page>\d+)$")

    @staticmethod
    def _item_id(paper_id, page_num):
        return f"{paper_id}-p{page_num:03d}"

    @classmethod
    def _parse_item_id(cls, item_id):
        m = cls._ITEM_ID_RE.match(item_id)
        if not m:
            return None
        return m.group("paper_id"), int(m.group("page"))

    def _registered_papers(self):
        rows = lib_io.read_csv(rc.pp("register", "papers.csv"))
        return [r for r in rows if r.get("file_kind") == "paper" and r.get("in_scope") == "yes"]

    def _paper_row(self, paper_id):
        for r in self._registered_papers():
            if r.get("paper_id") == paper_id:
                return r
        return None

    def _paper_abspath(self, paper_row):
        if not paper_row:
            return None
        entry = _b_manifest_item_map().get(paper_row.get("file"))
        if not entry:
            return None
        relpath, _row = entry
        return rc.pp(relpath)

    @staticmethod
    def _detect_layout(abspath, page_num):
        """Lightweight column-count heuristic, not a rigorous layout detector (documented
        simplification, see report). REAL BUG FOUND AND FIXED during this build (see
        docs/OPEN_QUESTIONS.md / the build report): the first version counted ANY text block on
        the left half vs right half of the page, which misread page 3 of the real
        neet_2023_code-E1.pdf as "two_column" -- confirmed by direct inspection of PyMuPDF's own
        block list that the "right-side" blocks were actually tiny inline-math glyph fragments
        from a rendered fraction/equation (e.g. "1/C_eq = 1/C1 + ..."), each only ~8-27pt wide,
        not a second column of real content. The real page (confirmed by rendering and visually
        inspecting it) is genuinely one full-width question card per question, stacked vertically
        -- the same single-column shape every paper in this project uses (Master Plan: all are
        neet.training/vedantu.com HTML-scrape renders, never a genuine two-column NTA print scan).
        Fix: only count a block as real column evidence if it is at least 15% of the page's width
        (filters out narrow formula-glyph fragments and single option-number labels like "(1)"),
        and require several such wide blocks on EACH side before calling it two_column at all --
        a real two-column layout has many independent paragraph-width blocks per side, not a
        handful of fragments."""
        try:
            import pymupdf as fitz
            with fitz.open(abspath) as doc:
                page = doc[page_num - 1]
                width = page.rect.width
                blocks = page.get_text("blocks") or []
        except Exception:
            return "one_column"
        mid = width / 2.0
        min_width = width * 0.15
        left = [b for b in blocks
                if b[2] <= mid * 0.95 and (b[3] - b[1]) > 0 and (b[2] - b[0]) >= min_width]
        right = [b for b in blocks
                 if b[0] >= mid * 1.05 and (b[3] - b[1]) > 0 and (b[2] - b[0]) >= min_width]
        if len(left) >= 3 and len(right) >= 3:
            return "two_column"
        return "one_column"

    def list_items(self, filters):
        papers = self._registered_papers()
        if not papers:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for row in papers:
            paper_id = row["paper_id"]
            if filters.get("papers") and not any(t in paper_id for t in filters["papers"]):
                continue
            abspath = self._paper_abspath(row)
            if not abspath or not os.path.exists(abspath):
                continue
            n_pages = lib_pdf.page_count(abspath)
            for p in range(1, n_pages + 1):
                item_id = self._item_id(paper_id, p)
                if not rc.item_passes_filters(item_id, filters):
                    continue
                status = rc.read_item_status(self.step, item_id)
                if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                    continue
                if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                    continue
                input_data = self._build_input(paper_id, abspath, p)
                _write_json(_work_input_path(self.step, item_id, "runA"), input_data)
                lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                        _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("B2 needs B1 (register/papers.csv rows with file_kind=paper, in_scope=yes). "
                "None registered yet, or every matching page already has output pending --check -- "
                "use --items '<PAPER_ID>-p001' etc. to scope to specific real pages, since a "
                "127-page paper otherwise lists every page at once.")

    def _build_input(self, paper_id, abspath, page_num):
        work_dir = rc.pp("steps", self.step, "work")
        rc.ensure_dir(work_dir)
        item_id = self._item_id(paper_id, page_num)
        png_path = os.path.join(work_dir, f"{item_id}.png")
        lib_pdf.render_page_to_png(abspath, page_num, out_path=png_path)
        layout = self._detect_layout(abspath, page_num)
        previous_page = None
        if page_num > 1:
            prev_path = rc.pp("steps", self.step, "status", f"{self._item_id(paper_id, page_num - 1)}.last_q.json")
            previous_page = _read_json(prev_path) if os.path.exists(prev_path) else None
        return {
            "paper_id": paper_id, "page": page_num, "image": _relpath(png_path),
            "layout": layout, "previous_page": previous_page,
        }

    def _post_assembly(self, item_id, run_label, data, status):
        """SCRIPT half of B2 (spec 10/B2 procedure step 3): crops each question's box into
        papers/questions/<PAPER>/<QNO>.png. Multi-part (split-column/split-page) questions are
        NOT stitched into one image here -- only the first part is cropped, with a sidecar
        '<QNO>.STITCH_STUB.json' note recorded so the gap is auditable rather than silently wrong.
        This is a deliberate scope cut for this build pass (documented in the report, per the
        task's own allowance to stub cropping infra rather than sacrifice real-data verification
        time on it) -- the real agent-boundary-finding half is fully real and tested; only the
        less common multi-part STITCHING is stubbed."""
        if not data or "questions" not in data:
            return
        parsed = self._parse_item_id(item_id)
        if not parsed:
            return
        paper_id, page_num = parsed
        abspath = self._paper_abspath(self._paper_row(paper_id))
        if not abspath:
            return
        out_dir = rc.pp("papers", "questions", paper_id)
        rc.ensure_dir(out_dir)
        last_q = None
        for q in (data.get("questions") or []):
            qno = q.get("qno")
            parts = q.get("parts") or []
            if qno is None or not parts:
                continue
            crop_path = os.path.join(out_dir, f"{qno}.png")
            bbox = parts[0].get("bbox")
            if bbox and len(bbox) == 4:
                lib_pdf.crop_box(abspath, page_num, bbox, crop_path, dpi=200, unit="px")
                if len(parts) > 1:
                    _write_json(os.path.join(out_dir, f"{qno}.STITCH_STUB.json"), {
                        "note": "multi-part question (split column/page); stitching not "
                                 "implemented in this build pass -- only the first part was "
                                 "cropped. See docs/OPEN_QUESTIONS.md / the build report.",
                        "parts": parts,
                    })
            last_q = {"qno": qno, "continues_on_next": bool(q.get("continues_on_next"))}
        if last_q:
            _write_json(rc.pp("steps", self.step, "status", f"{item_id}.last_q.json"), last_q)

    def check(self, filters):
        papers = self._registered_papers()
        item_inputs = {}
        work_dir = rc.pp("steps", self.step, "work")
        if os.path.isdir(work_dir):
            valid_prefixes = {f"{row['paper_id']}-p" for row in papers}
            for run_label in ("retry1", "runA"):
                suffix = f".{run_label}.input.json"
                for fn in os.listdir(work_dir):
                    if not fn.endswith(suffix):
                        continue
                    item_id = fn[: -len(suffix)]
                    if item_id in item_inputs or not any(item_id.startswith(p) for p in valid_prefixes):
                        continue
                    if not rc.item_passes_filters(item_id, filters):
                        continue
                    item_inputs[item_id] = _read_json(os.path.join(work_dir, fn))
        return resolve_single_run_items(self.step, get_cfg(self.step), self.agent, item_inputs, {},
                                          self._post_assembly)


# ===========================================================================
# B3 - Read one question (spec 10/B3; .claude/agents/b3-question-reader.md)
#
# Custom (non-generic) check(): unlike A1/A2S/A3's plain retry-then-safe-default shape, B3's real
# fallback chain has THREE distinct outcomes for a failing check (spec 10/B3 "On failure"):
#   - duplicate options -> flag high, CONTINUE as "flagged" (B4 decides later) -- no retry at all;
#   - too few options / unreadable -> retry once, then BLOCK (no safe default) if still broken.
# config/steps.yaml's own safe_default for B3 is a single dict mixing a real default (duplicates)
# and a null (option-count/unreadable) under two different keys -- resolve_single_run_items's
# generic "if safe_default is None: blocked=True" can't tell those apart from one shared dict (see
# its own docstring's "best effort only" caveat), so B3 needs its own small resolver instead of
# reusing it, the same way A4/A6/A8 already have their own custom check() for similar reasons.
# ===========================================================================

class B3Plugin:
    step = "B3"
    agent = "b3-question-reader"

    @staticmethod
    def _item_id(paper_id, qno):
        return f"{paper_id}-q{int(qno):04d}"

    _ITEM_ID_RE = re.compile(r"^(?P<paper_id>.+)-q(?P<qno>\d+)$")

    @classmethod
    def _parse_item_id(cls, item_id):
        m = cls._ITEM_ID_RE.match(item_id)
        if not m:
            return None
        return m.group("paper_id"), int(m.group("qno"))

    def _cropped_questions(self):
        """{item_id: (paper_id, qno, crop_path)} for every papers/questions/<PAPER>/<QNO>.png
        B2's SCRIPT half has already produced -- B3's real upstream readiness signal, since B2
        isn't modelled with its own per-question status file."""
        out = {}
        questions_dir = rc.pp("papers", "questions")
        if not os.path.isdir(questions_dir):
            return out
        for paper_id in sorted(os.listdir(questions_dir)):
            paper_dir = os.path.join(questions_dir, paper_id)
            if not os.path.isdir(paper_dir):
                continue
            for fn in sorted(os.listdir(paper_dir)):
                if not fn.endswith(".png"):
                    continue
                qno_str = fn[: -len(".png")]
                if not qno_str.isdigit():
                    continue
                item_id = self._item_id(paper_id, int(qno_str))
                out[item_id] = (paper_id, int(qno_str), os.path.join(paper_dir, fn))
        return out

    def list_items(self, filters):
        pending = self._cropped_questions()
        if not pending:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for item_id, (paper_id, qno, crop_path) in pending.items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            # Matches b3-question-reader.md's Input exactly (question_image, paper_id, qno) --
            # deliberately NOT extended with a text_layer field; see the module docstring and the
            # build report for how strip_overlay_text still protects this step (via B2's box
            # already ending before the overlay card, and via this plugin's OWN check() -- below
            # -- scanning the agent's output for overlay leakage as an independent script-side
            # integrity gate, rather than by changing this step's already-finalised input_fields).
            input_data = {"question_image": _relpath(crop_path), "paper_id": paper_id, "qno": qno}
            _write_json(_work_input_path(self.step, item_id, "runA"), input_data)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return "B3 needs B2 output (papers/questions/<PAPER>/<QNO>.png); none found yet."

    def _qid_index_path(self):
        return rc.pp("papers", "records", "_qid_index.json")

    def _get_or_mint_qid(self, paper_id, qno):
        path = self._qid_index_path()
        with _locked_file(path + ".lock"):
            index = _read_json(path) if os.path.exists(path) else {}
            key = f"{paper_id}#{qno}"
            if key in index:
                return index[key]
            qid = lib_ids.next_question_id()
            index[key] = qid
            _write_json(path, index)
            return qid

    def _write_record(self, paper_id, qno, data, status, prompt_version):
        qid = self._get_or_mint_qid(paper_id, qno)

        paper_row = None
        for r in lib_io.read_csv(rc.pp("register", "papers.csv")):
            if r.get("paper_id") == paper_id and r.get("file_kind") == "paper":
                paper_row = r
                break
        if paper_row:
            # Spec 6.3's record example uses the short booklet CODE in paper_codes (e.g. "A:112"),
            # not the full paper_id -- that field is what C1 later compares within one sitting to
            # merge booklet-code duplicates. These values originate from B1's registration, not
            # this step's own agent call, so they are attributed to step "B1" in field_sources,
            # with B3's own transcription fields attributed separately below.
            code = paper_row.get("booklet_code") or paper_id
            b1_prompt_version = rc.get_prompt_version("B1")
            try:
                year_val = int(paper_row["year"]) if paper_row.get("year") else None
            except (TypeError, ValueError):
                year_val = None
            lib_records.set_fields(qid, {
                "exam": paper_row.get("exam"),
                "year": year_val,
                "sitting": paper_row.get("sitting"),
                "paper_codes": [f"{code}:{qno}"],
                "source_file": paper_row.get("source"),
                "trust": paper_row.get("trust"),
            }, step="B1", prompt_version=b1_prompt_version, status="pass")

        fields = {
            "question_id": qid,
            "stem_en": data.get("stem_en"),
            "statements": data.get("statements") or [],
            "list_i": data.get("list_i") or [],
            "list_ii": data.get("list_ii") or [],
            "options_en": data.get("options_en") or {},
            "structure": data.get("structure"),
            "has_figure": data.get("has_figure", False),
            "negative_words": data.get("negative_words_seen") or [],
        }
        lib_records.set_fields(qid, fields, step=self.step, prompt_version=prompt_version,
                                 status=status)
        return qid

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        pending = self._cropped_questions()
        new_lines = []
        for item_id, (paper_id, qno, _crop_path) in pending.items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            existing = rc.read_item_status(self.step, item_id)
            if existing and existing.get("status") != "stale" and existing.get("prompt_version") == prompt_version:
                continue
            runs_here = {}
            for run_label in ("retry1", "runA"):
                p = _out_path(self.step, item_id, run_label)
                if os.path.exists(p):
                    runs_here[run_label] = p
            if "retry1" in runs_here:
                run_label, out_path = "retry1", runs_here["retry1"]
            elif "runA" in runs_here:
                run_label, out_path = "runA", runs_here["runA"]
            else:
                continue  # still waiting on the agent

            data = _read_json(out_path)
            started = rc.now_iso()
            if isinstance(data, dict) and "error" in data:
                ok, msg = False, f"agent reported error: {data['error']}"
            else:
                ok, msg = rc.validate_schema(self.step, data)
                if ok:
                    ok, msg = rc.run_step_check(self.step, data, {"item_id": item_id, "step": self.step})
            ended = rc.now_iso()

            if ok:
                dupes = option_parser.find_duplicate_options(data.get("options_en") or {})
                if dupes:
                    rc.raise_flag("item", item_id, self.step, "B3_DUPLICATE_OPTIONS",
                                   flags_cat.get("B3_DUPLICATE_OPTIONS", "high"),
                                   f"duplicate option text: {dupes}", provisional_value=data,
                                   prompt_version=prompt_version)
                    status = "flagged"
                else:
                    status = "pass"
                self._write_record(paper_id, qno, data, status, prompt_version)
                rc.write_item_status(self.step, item_id, status, prompt_version,
                                       extra={"run": run_label, "check_message": msg})
                rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version,
                                    started, ended, "pass", msg, None, status)
                continue

            if run_label == "runA":
                rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version,
                                    started, ended, "fail", msg, None, "pending")
                rc.write_pending(self.step, item_id, {"reason": msg, "next_run": "retry1"})
                retry_input = dict(_read_json(_work_input_path(self.step, item_id, "runA")))
                retry_input["previous_attempt_failed"] = msg
                _write_json(_work_input_path(self.step, item_id, "retry1"), retry_input)
                new_lines.append(ListLine(item_id, self.agent,
                                            _relpath(_work_input_path(self.step, item_id, "retry1")),
                                            _relpath(_out_path(self.step, item_id, "retry1")), "retry1"))
                continue

            # Retry exhausted: block, per spec (no safe default for option-count/unreadable).
            code = "B3_UNREADABLE"
            if msg.startswith("B3_OPTION_COUNT"):
                code = "B3_OPTION_COUNT"
            rc.raise_flag("item", item_id, self.step, code, flags_cat.get(code, "blocker"), msg,
                           evidence=[_relpath(out_path)], prompt_version=prompt_version)
            rc.write_item_status(self.step, item_id, "blocked", prompt_version,
                                   extra={"run": run_label, "check_message": msg})
            rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version, started,
                                ended, "fail", msg, "runA", "blocked")
        return new_lines


# ===========================================================================
# B4 - Read it a second way (spec 10/B4; .claude/agents/b4-second-reader.md)
#
# SCRIPT branch (text layer exists inside the question's box): extract + sanitize + split, no
# agent call -- this is the common path on a paper with ~100% text-layer coverage (confirmed for
# neet_2023_code-E1 per docs/OPEN_QUESTIONS.md 2026-10-10). AGENT branch (b4-second-reader, no
# text layer) is implemented too but expected to rarely/never trigger on this paper.
# ===========================================================================

class B4Plugin:
    step = "B4"
    agent = "b4-second-reader"

    def _b3_passed_items(self):
        """Every B3 item with a usable (pass/flagged) status and no B4 status yet for the current
        prompt version -- B4's real upstream readiness signal (needs: B3)."""
        prompt_version = rc.get_prompt_version(self.step)
        status_dir = rc.pp("steps", "B3", "status")
        out = {}
        if not os.path.isdir(status_dir):
            return out
        for fn in sorted(os.listdir(status_dir)):
            if not fn.endswith(".json") or ".pending" in fn:
                continue
            item_id = fn[: -len(".json")]
            b3_status = rc.read_item_status("B3", item_id)
            if not b3_status or b3_status.get("status") not in ("pass", "flagged"):
                continue
            b4_status = rc.read_item_status(self.step, item_id)
            if b4_status and b4_status.get("status") != "stale" and b4_status.get("prompt_version") == prompt_version:
                continue
            parsed = B3Plugin._parse_item_id(item_id)
            if not parsed:
                continue
            out[item_id] = parsed  # (paper_id, qno)
        return out

    def _question_bbox(self, paper_id, qno):
        """Recovers the real PDF-page/bbox a question was cropped from, by re-reading B2's own
        runA output for whichever page produced papers/questions/<PAPER>/<QNO>.png -- B4's SCRIPT
        branch needs the ORIGINAL pdf box (to extract the real embedded text layer inside it), not
        the already-cropped PNG B3 read."""
        out_dir = rc.pp("steps", "B2", "out")
        if not os.path.isdir(out_dir):
            return None
        prefix = f"{paper_id}-p"
        for fn in sorted(os.listdir(out_dir)):
            if not (fn.startswith(prefix) and fn.endswith(".runA.json")):
                continue
            page_item_id = fn[: -len(".runA.json")]
            parsed = B2Plugin._parse_item_id(page_item_id)
            if not parsed:
                continue
            _paper_id, page_num = parsed
            data = _read_json(os.path.join(out_dir, fn))
            if not isinstance(data, dict):
                continue
            for q in (data.get("questions") or []):
                if q.get("qno") == qno:
                    parts = q.get("parts") or []
                    if parts and parts[0].get("bbox"):
                        return page_num, parts[0]["bbox"]
        return None

    def list_items(self, filters):
        """Only ever returns AGENT-branch (b4-second-reader) lines -- the SCRIPT branch (text
        layer present) is resolved entirely inside check(), with no agent dispatch at all, per
        spec 10/B4 procedure step 1."""
        pending = self._b3_passed_items()
        if not pending:
            return []
        lines = []
        for item_id, (paper_id, qno) in pending.items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            located = self._question_bbox(paper_id, qno)
            if not located:
                continue
            page_num, bbox = located
            paper_row = B2Plugin()._paper_row(paper_id)
            abspath = B2Plugin()._paper_abspath(paper_row)
            if not abspath:
                continue
            raw_text = lib_pdf.extract_text_in_box(abspath, page_num, bbox, dpi=200, unit="px")
            if raw_text.strip():
                continue  # SCRIPT branch applies; resolved in check(), no agent line for this item
            crop_path = rc.pp("papers", "questions", paper_id, f"{qno}.png")
            input_data = {"question_image": _relpath(crop_path), "paper_id": paper_id, "qno": qno}
            _write_json(_work_input_path(self.step, item_id, "runA"), input_data)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("B4: every B3-passed question either already has B4 output, or has a text layer "
                "in its box (resolved by the SCRIPT branch in --check, no agent line needed), or "
                "has no B2 boundary box recovered yet.")

    _NEGATIVE_WORDS = {"NOT", "EXCEPT", "INCORRECT", "FALSE", "WRONG"}

    @classmethod
    def _mismatch_severity(cls, b3_options, b4_options, mismatched_keys):
        """Spec 10/B4's own flag severity is conditional, not a fixed value: 'high (span is a
        number, unit, sign, option label or negative word) else normal'. config/steps.yaml quotes
        that condition verbatim as the catalogue string (not a plain enum value) -- REAL BUG FOUND
        while running B4 for real: passing that descriptive string straight to
        lib/flags.py::raise_flag crashes with ValueError (severity must be one of
        blocker/high/normal/low). Fixed here by actually evaluating the condition per mismatched
        option instead of reading a severity string out of the config."""
        for key in mismatched_keys:
            combined = f"{b3_options.get(key, '')} {b4_options.get(key, '')}"
            if any(ch.isdigit() for ch in combined):
                return "high"
            if any(w in combined.upper() for w in cls._NEGATIVE_WORDS):
                return "high"
        return "normal"

    def _script_branch(self, paper_id, qno, page_num, bbox, abspath):
        """Spec 10/B4 procedure step 1: SCRIPT extracts the text layer inside the question's PDF
        box, sanitizes it (Master Plan risk #1 -- this box can still include trailing overlay text
        if B2's agent boxed slightly wide, so stripping here is a real second line of defence, not
        a formality), splits options with option_parser, and compares against B3's own reading
        after latex_normalise. No agent call."""
        raw_text = lib_pdf.extract_text_in_box(abspath, page_num, bbox, dpi=200, unit="px")
        clean_text, _n = scrape_sanitize.strip_overlay_text(raw_text)
        split = option_parser.split_inline_options(clean_text)
        return clean_text, split

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        pending = self._b3_passed_items()
        b2plugin = B2Plugin()
        for item_id, (paper_id, qno) in pending.items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            located = self._question_bbox(paper_id, qno)
            if not located:
                continue
            page_num, bbox = located
            paper_row = b2plugin._paper_row(paper_id)
            abspath = b2plugin._paper_abspath(paper_row)
            if not abspath:
                continue
            raw_text = lib_pdf.extract_text_in_box(abspath, page_num, bbox, dpi=200, unit="px")
            started = rc.now_iso()

            b3_record_qid = None
            index = _read_json(rc.pp("papers", "records", "_qid_index.json")) or {}
            b3_record_qid = index.get(f"{paper_id}#{qno}")
            b3_record = lib_records.read_record(b3_record_qid) if b3_record_qid else {}

            if raw_text.strip():
                # SCRIPT branch: no agent call at all.
                clean_text, split = self._script_branch(paper_id, qno, page_num, bbox, abspath)
                b3_options = b3_record.get("options_en") or {}
                mismatches = []
                for key in ("1", "2", "3", "4"):
                    b3_val = latex_normalise.normalise(b3_options.get(key, ""))
                    b4_val = latex_normalise.normalise(split["options"].get(key, ""))
                    if b4_val and b3_val and b3_val != b4_val and b4_val not in b3_val and b3_val not in b4_val:
                        mismatches.append(key)
                ended = rc.now_iso()
                if mismatches and split["options"]:
                    # No synchronous adjudicator wired in yet (same precedent as A2's cross-page
                    # continuity and A6's weak pairs): flag + keep B3's reading as provisional.
                    severity = self._mismatch_severity(b3_options, split["options"], mismatches)
                    rc.raise_flag("item", item_id, self.step, "B4_MISMATCH_ADJUDICATED", severity,
                                   f"SCRIPT text-layer reading disagrees with B3 on option(s) {mismatches} "
                                   f"(sanitized text-layer options: {split['options']})",
                                   evidence=[_relpath(rc.pp('papers', 'records', f'{b3_record_qid}.json'))]
                                   if b3_record_qid else [],
                                   prompt_version=prompt_version)
                    status = "flagged"
                else:
                    status = "pass"
                if b3_record_qid:
                    lib_records.set_fields(b3_record_qid, {
                        "b4_text_layer_sanitized": clean_text,
                        "b4_script_options": split["options"],
                    }, step=self.step, prompt_version=prompt_version, status=status)
                rc.write_item_status(self.step, item_id, status, prompt_version,
                                       extra={"run": "script", "check_message":
                                              "ok" if status == "pass" else f"mismatch on {mismatches}"})
                rc.append_run_log(item_id, self.step, "script", None, prompt_version, started, ended,
                                    "pass" if status == "pass" else "fail",
                                    "ok" if status == "pass" else f"mismatch on {mismatches}", None, status)
            else:
                # AGENT branch resolution (b4-second-reader already dispatched via list_items).
                out_path = _out_path(self.step, item_id, "runA")
                if not os.path.exists(out_path):
                    continue
                data = _read_json(out_path)
                ok, msg = rc.validate_schema(self.step, data) if not (isinstance(data, dict) and "error" in data) \
                    else (False, data.get("error"))
                ended = rc.now_iso()
                status = "pass" if ok else "flagged"
                if ok and b3_record_qid:
                    lib_records.set_fields(b3_record_qid, {"b4_agent_reading": data},
                                             step=self.step, prompt_version=prompt_version, status=status)
                rc.write_item_status(self.step, item_id, status, prompt_version,
                                       extra={"run": "runA", "check_message": msg})
                rc.append_run_log(item_id, self.step, "runA", self.agent, prompt_version, started,
                                    ended, "pass" if ok else "fail", msg, None, status)
        return self.list_items(filters)


# ===========================================================================
# B5 - Attach the answer key (spec 10/B5; .claude/agents/b5-key-copier.md)
#
# Item = one key PAGE. Rather than registering the (multi-code) key PDF as a whole via B1 (a real
# structural mismatch -- one physical key file covers every booklet code of a sitting, not one
# code per file the way a paper file does; noted in the report), this plugin locates the ONE page
# matching a registered paper's own booklet_code by searching the key PDF's own printed "BOOK CODE
# : <X>" header text directly (plain keyword search, a SCRIPT operation, not a judgement) and
# dispatches b5-key-copier on exactly that page.
# ===========================================================================

class B5Plugin:
    step = "B5"
    agent = "b5-key-copier"

    # NTA prints this header FIVE different ways across years, and the original narrow pattern
    # matched only two of them -- silently stranding whole years. Surveyed across all 30 real key
    # PDFs in inputs/keys/ (one per year, first five pages):
    #     2019       "Book Code : P1"
    #     2020, 2021 "BOOK : E1"            <- no "CODE" word at all
    #     2022       "SET: X6"              <- no "BOOK" word at all
    #     2023       "BOOK CODE : E1"
    #     2024-2026  "Test Booklet Code : Q1"
    #     2018       "BOOKLET CODE"         (code printed separately)
    # When `_find_key_page` found nothing, `list_items` did a bare `continue`: the paper simply
    # vanished from B5's work list with NO flag raised, and because `_b_qid_records()` gates on
    # `official_answer`, B6/B7/B8 and C1 all became unreachable. Real cost measured this session:
    # ~398 extracted questions (2022's 200 and 2024's 198) sat with no answer while B5 reported
    # DONE. A silent skip on the step that supplies the answer is the worst possible failure mode.
    #
    # So: make BOOK/BOOKLET/SET all optional-but-anchored, and require the code to follow. Kept
    # deliberately tight on the code itself (`\b{code}\b`) so a page for Q1 never matches Q2.
    _CODE_RE_TMPL = r"(?:TEST\s+)?(?:BOOK(?:LET)?(?:\s*CODE)?|SET|Q\.?\s*P\.?\s*CODE)\s*:?\s*{code}\b"

    def _registered_papers(self):
        return [r for r in lib_io.read_csv(rc.pp("register", "papers.csv"))
                if r.get("file_kind") == "paper" and r.get("in_scope") == "yes"]

    def _key_abspath_for(self, year, sitting):
        """Finds the real key PDF covering this (year, sitting) from inputs/manifest.csv's own
        key rows (kind=key) -- independent of whether that key file has ever been through B1."""
        for row in _b_manifest_rows():
            if row.get("kind") != "key":
                continue
            if str(row.get("year")) == str(year) and (row.get("sitting") or "MAIN") == sitting:
                return rc.pp(row["file"])
        return None

    def _find_key_page(self, key_abspath, booklet_code):
        if not booklet_code:
            return None
        pattern = re.compile(self._CODE_RE_TMPL.format(code=re.escape(booklet_code)), re.IGNORECASE)
        n = lib_pdf.page_count(key_abspath)
        for p in range(1, n + 1):
            text = lib_pdf.extract_text_layer(key_abspath, p)
            if pattern.search(text):
                return p
        return None

    @staticmethod
    def _item_id(paper_id):
        return f"{paper_id}-key"

    def list_items(self, filters):
        papers = self._registered_papers()
        if not papers:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for row in papers:
            paper_id = row["paper_id"]
            item_id = self._item_id(paper_id)
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            key_abspath = self._key_abspath_for(row["year"], row["sitting"])
            if not key_abspath or not os.path.exists(key_abspath):
                continue
            page_num = self._find_key_page(key_abspath, row["booklet_code"])
            if not page_num:
                # A bare `continue` here was the second half of a real, expensive bug. When the
                # code header could not be matched (see _CODE_RE_TMPL's survey of the five real
                # formats) the paper silently dropped out of B5's work list, B5 printed DONE, and
                # ~398 extracted questions across 2022 and 2024 sat with no official answer --
                # with nothing in flags/flags.jsonl to say why. B5 supplies THE answer; it must
                # never fail quietly. `B5_KEY_ROW_MISSING` (blocker) is already declared for
                # exactly this in config/steps.yaml and was never raised.
                reason = ("booklet_code is empty on the register row, so no key page can be "
                          "looked up" if not (row.get("booklet_code") or "").strip() else
                          f"no page of {os.path.basename(key_abspath)} carries a code header "
                          f"matching {row['booklet_code']!r}")
                rc.raise_flag("item", item_id, self.step, "B5_KEY_ROW_MISSING",
                              (get_cfg(self.step).get("flags") or {}).get(
                                  "B5_KEY_ROW_MISSING", "blocker"),
                              f"{paper_id}: {reason}; every question of this paper will stay "
                              f"without an official answer, which also blocks B6/B7/B8 and C1",
                              evidence=[_relpath(key_abspath)], prompt_version=prompt_version)
                continue
            input_data = self._build_input(paper_id, key_abspath, page_num, row["booklet_code"])
            _write_json(_work_input_path(self.step, item_id, "runA"), input_data)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("B5 needs a registered paper (register/papers.csv, file_kind=paper) and a real "
                "key PDF covering its (year, sitting) in inputs/manifest.csv -- plus a page in "
                "that key whose own printed 'BOOK CODE : <X>' header matches the paper's "
                "booklet_code. None found/matched yet.")

    def _build_input(self, paper_id, key_abspath, page_num, booklet_code_expected):
        work_dir = rc.pp("steps", self.step, "work")
        rc.ensure_dir(work_dir)
        item_id = self._item_id(paper_id)
        png_path = os.path.join(work_dir, f"{item_id}.png")
        lib_pdf.render_page_to_png(key_abspath, page_num, out_path=png_path)
        raw_text = lib_pdf.extract_text_layer(key_abspath, page_num)
        # Key pages carry no answer-overlay content (confirmed: a plain qno/answer table, see
        # report) -- strip_overlay_text is a real no-op here, run anyway so every B-stage text
        # layer passes through the same sanitizer uniformly (same reasoning as B1's cover pages).
        clean_text, _n = scrape_sanitize.strip_overlay_text(raw_text)
        return {
            "key_image": _relpath(png_path), "text_layer": clean_text,
            "booklet_code_expected": booklet_code_expected,
            # Not part of b5-key-copier.md's Input contract (the agent never sees this) -- kept in
            # the work-input file only so _post_assembly can recover which real key file/page this
            # came from for the record's `answer_source` field without re-deriving it.
            "_key_file_relpath": _relpath(key_abspath), "_key_page": page_num,
        }

    def _post_assembly(self, item_id, run_label, data, status):
        """SCRIPT joins each key row onto its question's papers/records/<QID>.json by
        (paper_id, qno) -- never qno alone (spec 10/B5 procedure; Master Plan 2.1.1 #2/#5) -- and
        sets record.status from the row's mark (bonus/dropped/multiple_accepted/normal). Only
        questions B3 already minted a question_id for (via the shared _qid_index.json) can be
        joined; a key row with no matching question yet is simply not joinable this run (not a
        B5_KEY_ROW_MISSING case -- that flag is for the REVERSE gap, a question with no key row,
        handled in check() below)."""
        if not data or "rows" not in data:
            return
        paper_id = item_id[: -len("-key")] if item_id.endswith("-key") else item_id
        qid_index = _read_json(rc.pp("papers", "records", "_qid_index.json")) or {}
        prompt_version = rc.get_prompt_version(self.step)
        input_path = _work_input_path(self.step, item_id, run_label)
        input_data = _read_json(input_path) if os.path.exists(input_path) else {}
        answer_source = input_data.get("_key_file_relpath", "")
        for row in data.get("rows") or []:
            qno = row.get("qno")
            qid = qid_index.get(f"{paper_id}#{qno}")
            if not qid:
                continue
            mark = (row.get("mark") or "").strip().lower()
            answer = (row.get("answer") or "").strip()
            # The option-id legend is part of the key, not an interpretation of it. Real NEET keys
            # print a bare Option Id in the answer cell and define it in a footnote on the same
            # page -- "Note: Option Id 5 = Drop", "5 DENOTES QUESTION IS DROPPED". Agents are told
            # to copy the PRINTED mark text, so one may legitimately write mark "5" (what the cell
            # shows) where another writes "Dropped" (the legend resolved). Both are obedient and
            # they mean the same thing.
            #
            # Hit for real on Q-000004, which appears in two booklets: E1 qno 2 came back
            # mark "5", E2 qno 30 came back mark "Dropped", and only the second was recognised.
            # The first fell through every branch to `normal` while carrying an EMPTY answer, so a
            # question the key had dropped was recorded as an ordinary scorable one -- and because
            # B8 only ever looks at bonus/dropped/multiple_accepted records, its own
            # corrected_answer for that question was stranded behind a status that said it wasn't
            # needed. Matching on the digit as well as the word makes the two spellings agree.
            if "bonus" in mark:
                official_status = "bonus"
            elif "drop" in mark or mark in {"5", "res 5", "option id 5"}:
                official_status = "dropped"
            elif "," in answer:
                official_status = "multiple_accepted"
            elif not answer:
                # Invariant, independent of how any mark was spelled: a row with no answer has
                # nothing to score, so it cannot be `normal`. Reaching here means the mark is a
                # spelling nobody has taught this function yet, so flag it for a human rather than
                # guess which non-normal status it deserves -- and do NOT let it pass as normal,
                # which is the one reading that is certainly wrong.
                official_status = "dropped"
                rc.raise_flag("item", qid, self.step, "B5_UNRECOGNISED_MARK",
                              (get_cfg(self.step).get("flags") or {}).get(
                                  "B5_UNRECOGNISED_MARK", "normal"),
                              f"key row for {paper_id} qno {qno} has an empty answer and mark "
                              f"{row.get('mark')!r}, which this step does not recognise; recorded "
                              f"as `dropped` because a row with no answer cannot be `normal`, but "
                              f"the real printed meaning needs checking on the key page",
                              evidence=[_relpath(_out_path(self.step, item_id, run_label))],
                              prompt_version=prompt_version)
            else:
                official_status = "normal"
            lib_records.set_fields(qid, {
                "official_answer": row.get("answer"),
                "answer_source": answer_source,
                "status": official_status,
            }, step=self.step, prompt_version=prompt_version, status=status)

    def check(self, filters):
        papers = self._registered_papers()
        item_inputs = {}
        for row in papers:
            item_id = self._item_id(row["paper_id"])
            for run_label in ("retry1", "runA"):
                p = _work_input_path(self.step, item_id, run_label)
                if os.path.exists(p):
                    item_inputs[item_id] = _read_json(p)
                    break
        return resolve_single_run_items(self.step, get_cfg(self.step), self.agent, item_inputs, {},
                                          self._post_assembly)


# ===========================================================================
# Shared helpers for B6/B7/B8: all three steps are keyed on the real QUESTION record
# (papers/records/<QID>.json), not a page/file item the way B1-B5 are, and all three need the
# same upstream-readiness signal -- a question B5 has already joined an official_answer/status
# onto. B5's own item granularity is a key PAGE (one per paper), so there is no per-question B5
# status file the way B4 scans B3's; the record itself (official_answer/status present) is the
# real signal.
# ===========================================================================

def _b_qid_records():
    """{qid: record} for every real question record that already carries a B5 join."""
    out = {}
    records_dir = rc.pp("papers", "records")
    if not os.path.isdir(records_dir):
        return out
    for fn in sorted(os.listdir(records_dir)):
        if not fn.endswith(".json") or fn.startswith("_"):
            continue
        qid = fn[: -len(".json")]
        record = _read_json(os.path.join(records_dir, fn))
        if record.get("official_answer") is None and record.get("status") is None:
            continue  # B5 hasn't joined this question yet
        out[qid] = record
    return out


def _b_paper_id_for(record):
    """Recovers the real paper_id (e.g. 'NEET-2023-MAIN-E1') from a question record's own
    paper_codes (e.g. ['E1:1']) + exam/year/sitting -- the same (year, sitting, code) triple
    B1Plugin._post_assembly used to mint it originally, via the same lib_ids.make_paper_id."""
    codes = record.get("paper_codes") or []
    if not codes or ":" not in codes[0]:
        return None
    code = codes[0].split(":", 1)[0]
    try:
        return lib_ids.make_paper_id(int(record["year"]), record["sitting"], code)
    except (KeyError, TypeError, ValueError):
        return None


def _b_qno_for(record):
    codes = record.get("paper_codes") or []
    if not codes or ":" not in codes[0]:
        return None
    try:
        return int(codes[0].split(":", 1)[1])
    except ValueError:
        return None


# ===========================================================================
# B6 - Solve without the key (spec 10/B6; .claude/agents/b6-blind-solver.md)
#
# SAFETY-CRITICAL (Master Plan Section 7 risk #1(a); this task's own brief): B6's entire value is
# genuine independence from the official answer (spec Rule 10). Per docs/OPEN_QUESTIONS.md
# (2026-10-10/11): the sanitized TEXT layer already sitting in a question's
# papers/records/<QID>.json (stem_en/statements/list_i/list_ii/options_en, produced by B3/B4) is
# proven clean of overlay leakage end to end on real data. A raw page/question IMAGE crop is NOT
# safe even after grayscale -- scrape_sanitize.render_sanitized_crop was tested and confirmed
# insufficient: the correct-option checkmark icon is a distinct shape, not a color, and survives
# grayscale conversion. B6Plugin therefore builds its input EXCLUSIVELY from the record's own
# already-sanitized text fields -- never by re-reading the PDF, never with an image path -- and a
# question whose real content cannot be recovered from text alone (has_figure: true) is never
# dispatched to the agent at all: it resolves immediately to a B6_IMAGE_INPUT_UNSAFE flag instead
# of silently risking an answer leak through the one image-input path. No retry (config/steps.yaml
# fallback: [] -- spec 10/B6 "a retry only argues with itself; the disagreement is the signal").
# ===========================================================================

class B6Plugin:
    step = "B6"
    agent = "b6-blind-solver"

    @staticmethod
    def _item_id(qid):
        return qid

    @staticmethod
    def _build_input(record):
        """Text-only, straight from the record's own already-sanitized B3/B4 fields -- matches
        b6-blind-solver.md's Input block exactly (stem_en, statements, list_i, list_ii,
        options_en); figure_image is never included (see module note above)."""
        return {
            "stem_en": record.get("stem_en") or "",
            "statements": record.get("statements") or [],
            "list_i": record.get("list_i") or [],
            "list_ii": record.get("list_ii") or [],
            "options_en": record.get("options_en") or {},
        }

    def list_items(self, filters):
        records = _b_qid_records()
        if not records:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for qid, record in records.items():
            item_id = self._item_id(qid)
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            if record.get("has_figure"):
                # Refuse the one unsafe path outright -- resolved synchronously here, no agent
                # dispatch, no work-input file (so no image path is ever even written to disk for
                # this step).
                self._resolve_image_unsafe(qid, item_id, prompt_version)
                continue
            input_data = self._build_input(record)
            _write_json(_work_input_path(self.step, item_id, "runA"), input_data)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("B6 needs B5-joined question records (papers/records/<QID>.json with "
                "official_answer/status set). None found yet, or every joined question already "
                "resolved for this prompt version (including has_figure=true ones, resolved "
                "immediately as B6_IMAGE_INPUT_UNSAFE without ever being dispatched).")

    def _resolve_image_unsafe(self, qid, item_id, prompt_version):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        rc.raise_flag(
            "item", item_id, self.step, "B6_IMAGE_INPUT_UNSAFE",
            flags_cat.get("B6_IMAGE_INPUT_UNSAFE", "high"),
            "question has has_figure=true; B6's only way to represent a figure's content is a "
            "raw page/question image crop, which is known-unsafe (the correct-option checkmark "
            "icon survives grayscale conversion -- scrape_sanitize.py, "
            "docs/OPEN_QUESTIONS.md 2026-10-10). B6 is skipped for this question rather than risk "
            "leaking the answer through its one image-input path; the official answer is used "
            "downstream, unchecked by B6.",
            evidence=[_relpath(rc.pp("papers", "records", f"{qid}.json"))],
            prompt_version=prompt_version,
        )
        lib_records.set_fields(qid, {"b6_answer": None, "b6_agrees_with_key": None},
                                 step=self.step, prompt_version=prompt_version, status="flagged")
        rc.write_item_status(self.step, item_id, "flagged", prompt_version,
                               extra={"run": "none", "check_message": "B6_IMAGE_INPUT_UNSAFE"})
        rc.append_run_log(item_id, self.step, "none", None, prompt_version, rc.now_iso(),
                            rc.now_iso(), "fail", "B6_IMAGE_INPUT_UNSAFE: image input refused",
                            None, "flagged")

    # --- paper-level running stats, for the spec's ">10% of a paper" automatic-hint rule ---

    def _paper_stats_path(self):
        return rc.pp("steps", self.step, "status", "_paper_stats.json")

    def _record_paper_stat(self, paper_id, disagree):
        if not paper_id:
            return
        path = self._paper_stats_path()
        with _locked_file(path + ".lock"):
            stats = _read_json(path) if os.path.exists(path) else {}
            entry = stats.setdefault(paper_id, {"total": 0, "disagree": 0})
            entry["total"] += 1
            if disagree:
                entry["disagree"] += 1
            _write_json(path, stats)

    def _automatic_hint(self, record, paper_id, b3_item_id):
        """Best-effort version of spec 10/B6's automatic hint: one question -> check text and
        figure; >10% of a paper -> check B5 join for this paper; B4 also mismatched -> check B4
        spans; status bonus/dropped -> see B8. The '>10% of a paper' comparison is necessarily a
        RUNNING estimate against however many of the paper's questions this build has resolved
        through B6 so far (real data was only pulled through for a handful of questions per paper
        in this build pass, not a full ~180-200), not the paper's eventual full total --
        documented here and in the report, not hidden."""
        if record.get("status") in ("bonus", "dropped"):
            return "see B8"
        if b3_item_id:
            b4_status = rc.read_item_status("B4", b3_item_id)
            if b4_status and b4_status.get("status") == "flagged":
                return "check B4 spans"
        if paper_id:
            stats = _read_json(self._paper_stats_path()) if os.path.exists(self._paper_stats_path()) else {}
            entry = stats.get(paper_id, {"total": 0, "disagree": 0})
            total = entry["total"] + 1  # +1: this item, not yet recorded when the hint is built
            disagree = entry["disagree"] + 1
            if total and disagree / total > 0.10:
                return "check B5 join for this paper"
        return "check text and figure"

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        records = _b_qid_records()
        for qid, record in records.items():
            item_id = self._item_id(qid)
            if not rc.item_passes_filters(item_id, filters):
                continue
            existing = rc.read_item_status(self.step, item_id)
            if existing and existing.get("status") != "stale" and existing.get("prompt_version") == prompt_version:
                continue
            if record.get("has_figure"):
                continue  # already resolved synchronously in list_items(); no output to check
            out_path = _out_path(self.step, item_id, "runA")
            if not os.path.exists(out_path):
                continue  # still waiting on the agent

            data = _read_json(out_path)
            started = rc.now_iso()
            if isinstance(data, dict) and "error" in data:
                ok, msg = False, f"agent reported error: {data['error']}"
            else:
                ok, msg = rc.validate_schema(self.step, data)
                if ok:
                    context = {"official_answer": record.get("official_answer"),
                               "status": record.get("status"), "item_id": item_id, "step": self.step}
                    ok, msg = rc.run_step_check(self.step, data, context)
            ended = rc.now_iso()

            fields = {
                "b6_answer": data.get("answer") if isinstance(data, dict) else None,
                "b6_reason": data.get("reason") if isinstance(data, dict) else None,
                "b6_working": data.get("working") if isinstance(data, dict) else None,
                "b6_confidence": data.get("confidence") if isinstance(data, dict) else None,
                "b6_note": data.get("note") if isinstance(data, dict) else None,
                "b6_agrees_with_key": ok if isinstance(data, dict) and "error" not in data else None,
            }
            status = "pass" if ok else "flagged"
            lib_records.set_fields(qid, fields, step=self.step, prompt_version=prompt_version, status=status)
            rc.write_item_status(self.step, item_id, status, prompt_version,
                                   extra={"run": "runA", "check_message": msg})
            rc.append_run_log(item_id, self.step, "runA", self.agent, prompt_version, started, ended,
                                "pass" if ok else "fail", msg, None, status)

            paper_id = _b_paper_id_for(record)
            if ok:
                self._record_paper_stat(paper_id, disagree=False)
                continue

            # No retry (fallback: []): disagreement resolves immediately, flagged, and the
            # question continues downstream with the official answer regardless (safe_default is
            # a descriptive string, never substituted in -- config/steps.yaml's B6 entry).
            qno = _b_qno_for(record)
            b3_item_id = B3Plugin._item_id(paper_id, qno) if paper_id and qno is not None else None
            hint = self._automatic_hint(record, paper_id, b3_item_id)
            code = "B6_DISAGREES_WITH_KEY" if "B6_DISAGREES_WITH_KEY" in msg else f"{self.step}_CHECK_FAILED"
            rc.raise_flag("item", item_id, self.step, code, flags_cat.get(code, "high"),
                           f"{msg} -- hint: {hint}", provisional_value=data,
                           evidence=[_relpath(out_path)], prompt_version=prompt_version)
            self._record_paper_stat(paper_id, disagree=True)
        return self.list_items(filters)


# ===========================================================================
# B7 - Sort by subject and branch (spec 10/B7; .claude/agents/b7-chem-branch-sorter.md)
#
# Subject (and Biology's botany/zoology split) are pure SCRIPT, from "the paper's section
# headings" per spec -- B2/B3 do not currently capture an explicit section-heading block as real
# per-question data, so this build substitutes a real, confirmed per-question signal instead: the
# NCERT chapter/topic tag the scrape site appends verbatim after the last option (e.g. "Laws of
# Motion", "Electrostatic Potential and Capacitance" -- present in every real B4 SCRIPT-branch
# reading so far, docs/OPEN_QUESTIONS.md 2026-10-11). Only Chemistry calls the agent.
# ===========================================================================

_SUBJECT_KEYWORDS = {
    "Chemistry": [
        "amine", "alcohol", "ether", "aldehyde", "ketone", "carboxylic", "ester", "haloalkane",
        "haloarene", "polymer", "biomolecule", "equilibrium", "electrochemistry", "kinetics",
        "thermochemistry", "solution", "surface chemistry", "coordination compound", "p-block",
        "d and f block", "d- and f-block", "s-block", "periodic", "chemical bonding",
        "atomic structure", "redox", "hydrocarbon", "isomerism", "qualitative analysis",
        "environmental chemistry", "general organic chemistry", "chemistry",
    ],
    "Physics": [
        "mechanical properties", "electrostatic", "capacitance", "laws of motion", "motion in a",
        "gravitation", "thermodynamics", "kinetic theory", "oscillation", "wave optics",
        "electromagnetic", "current electricity", "magnetism", "magnetic", "atoms", "nuclei",
        "semiconductor", "communication system", "rotational motion", "system of particles",
        "units and measurement", "work, energy", "work energy", "thermal properties",
        "ray optics", "dual nature", "physics",
    ],
    "Biology": [
        "reproduction", "genetics", "evolution", "ecology", "biotechnology", "biomolecules",
        "human health", "biodiversity", "organisms and populations", "plant physiology",
        "human physiology", "digestion", "excretory", "neural control", "locomotion",
        "breathing", "body fluids", "chemical coordination", "microbes", "biology",
    ],
}

_CHEM_BRANCH_KEYWORDS = {
    "physical": "equilibrium electrochemistry kinetics thermochemistry solutions ph "
                "thermodynamics states of matter atomic structure calculation rate constant "
                "molarity molality cell potential",
    "organic": "amine alcohol ether aldehyde ketone carboxylic ester haloalkane haloarene "
               "polymer biomolecule hydrocarbon isomerism reaction mechanism functional group "
               "named reaction alkene alkyne benzene",
    "inorganic": "periodic coordination compound p-block d-block f-block s-block metallurgy "
                 "qualitative analysis bonding oxidation ionic covalent complex ligand salt "
                 "ore extraction",
}


def _b7_topic_tag(record):
    """The real per-question topic tag the scrape site appends after the last option (see module
    note above). Looked for in b4_script_options['4'] first (where it's actually embedded in this
    project's real data -- confirmed in Q-000001/2/3), falling back to the last non-empty line of
    b4_text_layer_sanitized."""
    opts = record.get("b4_script_options") or {}
    last_opt = opts.get("4") or ""
    lines = [ln.strip() for ln in last_opt.split("\n") if ln.strip()]
    if len(lines) >= 2:
        return lines[-1]
    text = record.get("b4_text_layer_sanitized") or ""
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    return lines[-1] if lines else ""


#: Where each subject sits by QUESTION NUMBER. NEET prints its paper in fixed subject blocks and
#: says so in section banners, so the question number is a DETERMINISTIC subject signal -- unlike
#: keyword guessing, which was measured at 21% accuracy on 2023 and 60% on 2022, with confident
#: wrong answers (qno 181 "Electrostatic precipitator in a thermal power plant" is a Biology
#: environmental-issues question that the keyword matcher called Physics; qno 63 "magnetic quantum
#: number / azimuthal quantum number" is Chemistry atomic structure, also called Physics).
#:
#: Verified against every record where the old matcher did assign a subject: the range agrees on
#: 53 of 59, and on all 6 disagreements the range is right and the matcher wrong (checked by
#: reading the real stems). Botany/Zoology split verified too: qno 102 "angiosperm ... embryo sac"
#: is Botany; qno 159 "Lippe's loop ... contraceptive" and qno 160 "oxygenated blood" are Zoology.
#:
#: Two real structures exist. 2021 onward: 200 questions, 50 per block. Up to 2020: 180 questions,
#: 45 per block. Keyed by the paper's real total rather than by year, so a year whose structure we
#: have not seen cannot be silently mis-split.
_B7_SUBJECT_BLOCKS = {
    200: ((50, "Physics", None), (100, "Chemistry", None),
          (150, "Biology", "botany"), (200, "Biology", "zoology")),
    180: ((45, "Physics", None), (90, "Chemistry", None),
          (135, "Biology", "botany"), (180, "Biology", "zoology")),
}


def _b7_qno(record):
    """The question's own printed number, from paper_codes entries like "E1:51"."""
    for code in record.get("paper_codes") or []:
        m = re.search(r":(\d+)\s*$", str(code))
        if m:
            return int(m.group(1))
    return None


def _b7_subject_from_qno(record):
    """(subject, branch) from the printed question number, or (None, None).

    This closes the Biology `botany`/`zoology` gap as a side effect: those values are in
    config/allowed_values.yaml but no step ever assigned them, so every Biology question read
    `branch: unsure` -- not because a step tried and failed, but because none ever tried."""
    qno = _b7_qno(record)
    if qno is None:
        return None, None
    total = _b7_paper_total(record)
    blocks = _B7_SUBJECT_BLOCKS.get(total)
    if not blocks:
        return None, None
    for upper, subject, branch in blocks:
        if qno <= upper:
            return subject, branch
    return None, None


def _b7_paper_total(record):
    """How many questions this paper really has, counted from the bank rather than assumed.

    Counting the sibling records for the same (year, sitting) is deliberate: the scrape's own
    banner is unreliable (2022's claims "Chemistry 52, Biology 98" against the real 50/100), and
    hard-coding a year->total table would silently mis-split the first year that breaks the
    pattern. Snapped to the nearest known structure only when the count is close, so a paper still
    mid-extraction does not get a wrong split."""
    year, sitting = record.get("year"), record.get("sitting")
    if year is None:
        return None
    # Scan papers/records/ DIRECTLY rather than via _b_qid_records(): that helper gates on
    # `official_answer`, so a paper whose B5 has not run yet is invisible to it -- which is
    # exactly the paper this function is needed for. Using it created a circular dependency
    # (subject needs the total, the total needed the answer, the answer needs B5) and silently
    # returned None for all 398 questions of 2022 and 2024, the very ones being fixed.
    records_dir = rc.pp("papers", "records")
    seen = set()
    if os.path.isdir(records_dir):
        for fn in os.listdir(records_dir):
            if not (fn.startswith("Q-") and fn.endswith(".json")):
                continue
            try:
                rec = _read_json(os.path.join(records_dir, fn))
            except Exception:
                continue
            if not isinstance(rec, dict) or rec.get("merged_into"):
                continue
            if rec.get("year") == year and rec.get("sitting") == sitting:
                n = _b7_qno(rec)
                if n:
                    seen.add(n)
    highest = max(seen) if seen else 0
    for total in (200, 180):
        if abs(highest - total) <= 4 or highest == total:
            return total
    return None


def _b7_detect_subject(record):
    """Real finding during this build's B7 test pull (Q-000005, a real Chemistry/organic-amine
    question, qno 51 of neet_2023_code-E1.pdf): not every real question in this scrape carries a
    trailing NCERT chapter/topic tag the way Q-000001/2/3/4 did -- Q-000005's b4 text layer ends
    right after option 4 with no tag line at all, so a tag-only lookup silently mis-detects option
    4's own text as the 'tag' and finds no subject keyword in it. Fixed by falling back to a
    keyword scan of the question's own stem_en + options_en text whenever the tag lookup finds
    nothing -- real, substantive content (e.g. 'amine', 'LiAlH4') that genuinely identifies the
    subject even with no site-supplied tag."""
    # The printed question number comes FIRST: it is deterministic where keywords are a guess.
    # See _B7_SUBJECT_BLOCKS for the measured accuracy of each and the real cases where the
    # keyword matcher was confidently wrong.
    by_qno, _branch = _b7_subject_from_qno(record)
    if by_qno:
        return by_qno

    tag = _b7_topic_tag(record).lower()
    for subject, keywords in _SUBJECT_KEYWORDS.items():
        if tag and any(kw in tag for kw in keywords):
            return subject
    fallback_text = " ".join([
        record.get("stem_en") or "",
        " ".join((record.get("options_en") or {}).values()),
    ]).lower()
    if not fallback_text.strip():
        return None
    for subject, keywords in _SUBJECT_KEYWORDS.items():
        if any(kw in fallback_text for kw in keywords):
            return subject
    return None


class B7Plugin:
    step = "B7"
    agent = "b7-chem-branch-sorter"

    @staticmethod
    def _item_id(qid):
        return qid

    def list_items(self, filters):
        """Only ever returns Chemistry-branch agent lines -- Physics/Biology (and an
        undetectable subject) resolve SCRIPT-only inside check(), no agent dispatch at all."""
        records = _b_qid_records()
        if not records:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for qid, record in records.items():
            item_id = self._item_id(qid)
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            if _b7_detect_subject(record) != "Chemistry":
                continue
            # list_i/list_ii MUST be here. They were omitted originally because the agent file's
            # Input section names only stem/options/statements -- but for a "Match List I with
            # List II" question those three fields hold nothing but boilerplate: the stem reads
            # "Match List-I with List-II." and the options are bare pairings like "A-II, B-III".
            # The whole of the chemistry sits in the two lists, so withholding them handed the
            # agent a content-free record and forced an honest `unsure`.
            #
            # Measured, not assumed: six items came back `unsure`/low for exactly this reason
            # (Q-000332, Q-000368, Q-000387, Q-000392, Q-000397, plus Q-000351/Q-000505 at low
            # confidence), and three independent agents reported it as "extraction dropped the
            # match-list tables systematically, ~21% of items". That diagnosis was wrong and worth
            # recording: checked across all 618 records, only 3 of 72 match-like items (4%) have an
            # empty list, and Q-000332's lists are fully intact on disk -- "Isothermal process" ->
            # "Carried out at constant temperature", unambiguously physical chemistry. The data was
            # never damaged; this input was simply incomplete, and the agents could only see the
            # hole, not its cause.
            input_data = {
                "stem_en": record.get("stem_en") or "",
                "options_en": record.get("options_en") or {},
                "statements": record.get("statements") or [],
                "list_i": record.get("list_i") or [],
                "list_ii": record.get("list_ii") or [],
            }
            _write_json(_work_input_path(self.step, item_id, "runA"), input_data)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("B7 needs B5-joined question records. None found yet, every matching Chemistry "
                "question already has output pending --check, or none of the ready questions are "
                "Chemistry (Physics/Biology resolve SCRIPT-only inside --check, no agent line).")

    def _script_resolve(self, qid, item_id, record, subject, prompt_version):
        """Subject (always) + Biology's botany/zoology split.

        Biology's branch used to be left `unsure` here, on the reasoning that spec derives it from
        section headings and B2/B3 never captured those per question. That was honest but left the
        taxonomy's `botany`/`zoology` values permanently unassigned -- and `unsure` on a Biology
        record then meant "no step ever tried", which reads identically to "a step tried and
        failed". The printed QUESTION NUMBER carries the same information deterministically (NEET
        lays each paper out in fixed subject blocks), verified on real stems: qno 102 "angiosperm
        ... embryo sac" is botany, qno 159 "Lippe's loop ... contraceptive" is zoology. So take it
        from there when the paper's structure is known, and only fall back to `unsure` when it is
        not. Physics and Chemistry have no botany/zoology concept; Chemistry's own branch is the
        agent's job, not this path's."""
        fields = {"subject": subject, "branch": None}
        note = None
        if subject == "Biology":
            _subject_by_qno, branch_by_qno = _b7_subject_from_qno(record)
            if branch_by_qno:
                fields["branch"] = branch_by_qno
            else:
                fields["branch"] = "unsure"
                note = ("B7 could not place this question in the paper's subject blocks (no "
                        "printed question number, or an unrecognised paper structure), so "
                        "botany/zoology is left unsure rather than guessed.")
        elif subject is None:
            note = "B7 SCRIPT subject-tag keyword match found nothing recognisable; subject left unset."
        status = "flagged" if note else "pass"
        lib_records.set_fields(qid, fields, step=self.step, prompt_version=prompt_version, status=status)
        rc.write_item_status(self.step, item_id, status, prompt_version,
                               extra={"run": "script", "check_message": note or "ok"})
        rc.append_run_log(item_id, self.step, "script", None, prompt_version, rc.now_iso(),
                            rc.now_iso(), "pass" if not note else "fail", note or "ok", None, status)

    @staticmethod
    def _keyword_rank_fallback(record):
        """SCRIPT fallback per spec 10/B7's own final line: rank the question's text against a
        small table of real per-branch NCERT-vocabulary keywords and pick the best-scoring
        branch; 'physical' (the most common branch in the real 10-paper sample, Master Plan
        Section 3.4.1) if nothing scores at all. Note: config/steps.yaml names the function
        'search_index.keyword_rank'; the real function is 'search_index.rank' -- used as named in
        the actual module, not silently renamed around (same precedent as other build-time
        spec-vs-code naming notes logged in docs/OPEN_QUESTIONS.md)."""
        query = " ".join([record.get("stem_en") or "",
                           " ".join((record.get("options_en") or {}).values())])
        items = list(_CHEM_BRANCH_KEYWORDS.items())
        ranked = search_index.rank(query, items, limit=1)
        return ranked[0][0] if ranked else "physical"

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        records = _b_qid_records()
        for qid, record in records.items():
            item_id = self._item_id(qid)
            if not rc.item_passes_filters(item_id, filters):
                continue
            existing = rc.read_item_status(self.step, item_id)
            if existing and existing.get("status") != "stale" and existing.get("prompt_version") == prompt_version:
                continue

            subject = _b7_detect_subject(record)
            if subject != "Chemistry":
                self._script_resolve(qid, item_id, record, subject, prompt_version)
                continue

            out_path = _out_path(self.step, item_id, "runA")
            if not os.path.exists(out_path):
                continue  # still waiting on the agent

            data = _read_json(out_path)
            started = rc.now_iso()
            if isinstance(data, dict) and "error" in data:
                ok, msg = False, f"agent reported error: {data['error']}"
            else:
                ok, msg = rc.validate_schema(self.step, data)
                if ok:
                    ok, msg = rc.run_step_check(self.step, data, {"item_id": item_id, "step": self.step})
            ended = rc.now_iso()

            if ok:
                fields = {"subject": "Chemistry", "branch": data.get("branch")}
                status = "pass"
                lib_records.set_fields(qid, fields, step=self.step, prompt_version=prompt_version, status=status)
                rc.write_item_status(self.step, item_id, status, prompt_version,
                                       extra={"run": "runA", "check_message": msg})
                rc.append_run_log(item_id, self.step, "runA", self.agent, prompt_version, started, ended,
                                    "pass", msg, None, status)
                continue

            # unsure, or a hard failure: no adjudicator is wired in yet (the same documented gap
            # as A5/A6, docs/OPEN_QUESTIONS.md 2026-10-09), so fall straight through to spec
            # 10/B7's own final SCRIPT fallback.
            branch = self._keyword_rank_fallback(record)
            detail = msg
            rc.raise_flag("item", item_id, self.step, "B7_BRANCH_GUESS",
                           flags_cat.get("B7_BRANCH_GUESS", "normal"),
                           f"{detail} -- SCRIPT fallback (keyword rank over NCERT-branch "
                           f"vocabulary) chose {branch!r}",
                           provisional_value=data if isinstance(data, dict) else None,
                           evidence=[_relpath(out_path)], prompt_version=prompt_version)
            fields = {"subject": "Chemistry", "branch": branch}
            status = "flagged"
            lib_records.set_fields(qid, fields, step=self.step, prompt_version=prompt_version, status=status)
            rc.write_item_status(self.step, item_id, status, prompt_version,
                                   extra={"run": "runA", "check_message": detail})
            rc.append_run_log(item_id, self.step, "runA", self.agent, prompt_version, started, ended,
                                "fail", detail, None, status)
        return self.list_items(filters)


# ===========================================================================
# B8 - Fix bonus/dropped questions (spec 10/B8; .claude/agents/b8-faulty-fixer.md)
#
# Only activates on an OFFICIAL bonus/dropped/multiple_accepted status -- i.e. record["status"]
# already set by B5 from the real key -- never from a scraped paper's own claim of being faulty
# (agent file's own hardened "Context confirmed..." paragraph).
# ===========================================================================

_B8_STATUSES = {"bonus", "dropped", "multiple_accepted"}


def _b8_notice_text():
    """inputs/notices/ is confirmed empty in this project's real data drop
    (docs/OPEN_QUESTIONS.md, 2026-10-09 S0 entry) -- this genuinely returns '' until real notice
    PDFs are collected; not a bug, just the honest current state."""
    notices_dir = rc.pp("inputs", "notices")
    if not os.path.isdir(notices_dir):
        return ""
    texts = []
    for fn in sorted(os.listdir(notices_dir)):
        if not fn.lower().endswith(".pdf"):
            continue
        path = os.path.join(notices_dir, fn)
        for p in range(1, lib_pdf.page_count(path) + 1):
            texts.append(lib_pdf.extract_text_layer(path, p))
    return "\n".join(texts)


#: book_id prefix -> subject, for scoping a passage search to the question's own subject.
_BOOK_PREFIX_SUBJECT = {"BIO": "Biology", "CHE": "Chemistry", "PHY": "Physics"}


def _passage_subject(book_id):
    """The subject a passage's book_id belongs to, or None if the prefix is unrecognised."""
    return _BOOK_PREFIX_SUBJECT.get((book_id or "")[:3].upper())


def _b8_latest_passages(record, limit=15):
    """SCRIPT keyword search for up to `limit` latest-edition NCERT passages related to this
    question (spec 10/B8 Reads), SCOPED TO THE QUESTION'S OWN SUBJECT. Searches every
    ncert/passages/<BOOK>.jsonl whose book_id is a LATEST-edition book (this project's book_id
    scheme always ends the edition letter 'L' for latest -- lib/ids.py's EDITIONS).

    The subject scope is the point, and it was missing until 2026-10-13. The search ranked every
    latest-edition passage in the corpus regardless of subject, and `search_index.rank` returns
    the best `limit` matches however poor they are, so a question whose own chapter is not indexed
    yet silently received a full set of confident-looking passages from other subjects. Measured
    on the real B8 queue: Q-000384 is a Chemistry electrochemistry/Nernst question, CHE12L
    chapter 3 is not indexed yet, and the top match in the whole pool was PHY11L-CH05-P54 at
    score 8.19 -- physics mechanics. The agent that received it reported the passages as
    off-topic and correctly returned no supporting quote, but the setup is precisely the one that
    invites a fabricated citation, and B8 asks for an exact quote from these passages.

    A score floor does NOT fix this and was measured before being rejected: 8.19 is a HIGH score
    in a pool whose median is 1.08, because a long stem shares generic words ("cell", "reaction",
    "find") with any long passage. Subject is the discriminator; after scoping, the same question's
    top matches are all CHE12L.

    Returns [] when no latest-edition passage exists for this question's subject at all -- an
    honest, reportable Stage A sequencing gap rather than a wrong-subject answer. A caller that
    gets [] should say the NCERT basis is not available yet, not reach wider."""
    passages_dir = rc.pp("ncert", "passages")
    if not os.path.isdir(passages_dir):
        return []
    want_subject = record.get("subject")
    query = " ".join([record.get("stem_en") or "",
                       " ".join((record.get("options_en") or {}).values())])
    items, by_id = [], {}
    for fn in sorted(os.listdir(passages_dir)):
        if not fn.endswith(".jsonl") or not fn[: -len(".jsonl")].endswith("L"):
            continue
        book_id = fn[: -len(".jsonl")]
        # Scope to the question's subject. An unknown subject on the record (or an unrecognised
        # book prefix) falls through to the old unscoped behaviour rather than returning nothing:
        # a missing subject is a different defect and should not silently empty the evidence.
        if want_subject and _passage_subject(book_id) and _passage_subject(book_id) != want_subject:
            continue
        for passage in lib_io.read_jsonl(os.path.join(passages_dir, fn)):
            pid = passage.get("passage_id")
            if not pid:
                continue
            items.append((pid, passage.get("text") or ""))
            by_id[pid] = passage
    if not items:
        return []
    ranked = search_index.rank(query, items, limit=limit)
    return [{"passage_id": pid, "text": by_id[pid].get("text", "")} for pid, _score in ranked]


class B8Plugin:
    step = "B8"
    agent = "b8-faulty-fixer"

    @staticmethod
    def _item_id(qid):
        return qid

    @staticmethod
    def _candidates():
        return {qid: record for qid, record in _b_qid_records().items()
                if record.get("status") in _B8_STATUSES}

    def list_items(self, filters):
        records = self._candidates()
        if not records:
            return []
        prompt_version = rc.get_prompt_version(self.step)
        notice_text = _b8_notice_text()
        lines = []
        for qid, record in records.items():
            item_id = self._item_id(qid)
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            input_data = {
                "stem_en": record.get("stem_en") or "",
                "statements": record.get("statements") or [],
                "list_i": record.get("list_i") or [],
                "list_ii": record.get("list_ii") or [],
                "options_en": record.get("options_en") or {},
                "status": record.get("status"),
                "key_row": {"qno": _b_qno_for(record), "answer": record.get("official_answer"),
                             "mark": record.get("status")},
                "notice_text": notice_text,
                "latest_passages": _b8_latest_passages(record),
            }
            _write_json(_work_input_path(self.step, item_id, "runA"), input_data)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("B8 only runs for a question whose status (set by B5 from the real official key) "
                "is bonus, dropped or multiple_accepted. None found yet, or every such question "
                "already has output pending --check.")

    @staticmethod
    def _verify_quote(data):
        quote = data.get("supporting_quote")
        if quote is None:
            return True, "ok (no supporting quote claimed)"
        text = quote.get("text")
        passage_id = quote.get("passage_id")
        passages_dir = rc.pp("ncert", "passages")
        if os.path.isdir(passages_dir):
            for fn in sorted(os.listdir(passages_dir)):
                if not fn.endswith(".jsonl"):
                    continue
                for passage in lib_io.read_jsonl(os.path.join(passages_dir, fn)):
                    if passage.get("passage_id") == passage_id:
                        if quote_verify.find(text, passage.get("text") or "") is not None:
                            return True, "ok"
                        return False, (
                            f"supporting_quote not found word-for-word in passage {passage_id!r}"
                        )
        return False, f"supporting_quote's passage_id {passage_id!r} not found in ncert/passages/"

    def _post_assembly(self, qid, data, status, prompt_version):
        fields = {
            "issue_reason": data.get("issue_reason"),
            "corrected_answer": data.get("proposed_answer"),
            "corrected_stem": data.get("corrected_stem"),
            "corrected_options": data.get("corrected_options"),
            "b8_notice_says": data.get("notice_says"),
            "b8_supporting_quote": data.get("supporting_quote"),
            "b8_confidence": data.get("confidence"),
            "b8_note": data.get("note"),
        }
        lib_records.set_fields(qid, fields, step=self.step, prompt_version=prompt_version, status=status)

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        records = self._candidates()
        for qid, record in records.items():
            item_id = self._item_id(qid)
            if not rc.item_passes_filters(item_id, filters):
                continue
            existing = rc.read_item_status(self.step, item_id)
            if existing and existing.get("status") != "stale" and existing.get("prompt_version") == prompt_version:
                continue
            out_path = _out_path(self.step, item_id, "runA")
            if not os.path.exists(out_path):
                continue  # still waiting on the agent

            data = _read_json(out_path)
            started = rc.now_iso()
            if isinstance(data, dict) and "error" in data:
                ok, msg = False, f"agent reported error: {data['error']}"
            else:
                ok, msg = rc.validate_schema(self.step, data)
                if ok:
                    ok, msg = rc.run_step_check(self.step, data, {"item_id": item_id, "step": self.step})
                if ok:
                    ok, msg = self._verify_quote(data)
            ended = rc.now_iso()

            # Every B8 output is flagged B8_CORRECTION regardless of confidence (spec 10/B8 "What
            # continues"). No retry/adjudicator chain exists for B8 at all (config/steps.yaml
            # fallback: [] -- a real spec gap, logged in docs/OPEN_QUESTIONS.md 2026-10-11); a
            # failed quote-verification is itself part of the flag detail, not a separate path.
            status = "pass" if ok else "flagged"
            if isinstance(data, dict) and "error" not in data:
                self._post_assembly(qid, data, status, prompt_version)
            rc.raise_flag("item", item_id, self.step, "B8_CORRECTION",
                           flags_cat.get("B8_CORRECTION", "high"), msg, provisional_value=data,
                           evidence=[_relpath(out_path)], prompt_version=prompt_version)
            rc.write_item_status(self.step, item_id, status, prompt_version,
                                   extra={"run": "runA", "check_message": msg})
            rc.append_run_log(item_id, self.step, "runA", self.agent, prompt_version, started, ended,
                                "pass" if ok else "fail", msg, None, status)
        return self.list_items(filters)


# ===========================================================================
# B9 - Recover the figure (NOT in docs/SPEC.md: a deliberate, owner-approved EXTENSION beyond the
# spec's Stage B, which is complete at B1-B8. See config/steps.yaml's B9 entry for the full
# rationale and the three hard constraints; .claude/agents/b9-figure-matcher.md for the agent.)
#
# Item = one question whose B3 reading says has_figure: true and which no booklet code's scrape
# actually carries an image for. Worker is SCRIPT + AGENT, the same shape as C1:
#
#   SCRIPT  shortlist the top 2-3 inputs/legacy_sheets rows by full-question-text similarity and
#           DOWNLOAD each candidate's figure to steps/B9/work/ (scripts/recover_figures.py)
#   AGENT   b9-figure-matcher sees our question + the candidate IMAGES + each candidate's sheet
#           question TEXT ONLY, and decides which belongs, or none
#   SCRIPT  accept -> papers/figures/<QID>.png + figure_path/figure_source_url on the record
#           none/low -> B9_FIGURE_UNMATCHED, attach nothing
#
# The agent judges "does this figure BELONG to this question" -- never "is this figure correct".
# It cannot verify against the original paper, and neither can anything else in this pipeline, so
# every attached figure keeps a permanent B9_FIGURE_RECOVERED (low) provenance flag.
#
# Bespoke check() rather than resolve_single_run_items: a schema-and-check-valid output saying
# {"match": "none"} is a perfectly good agent answer that must still resolve the item to
# `flagged` + B9_FIGURE_UNMATCHED, and the generic resolver can only write `pass` on a passing
# check. Same precedent as B3/A4/A6/B7/C1's own bespoke check()s. The retry-once half of spec
# 5.5's chain is reimplemented inline here (it is ~15 lines) so a malformed output still gets its
# one retry with `previous_attempt_failed` set, exactly as the generic resolver would.
# ===========================================================================

def _b9_question_view(record):
    """Our side of b9-figure-matcher's Input contract. Our own B3 reading, nothing else -- no
    official_answer, no key, no coaching material, and no question-crop image path (see the
    config/steps.yaml B9 entry's judgment-call note: the crop does not contain the figure, which
    is the whole premise of the step, and it DOES contain the correct-option checkmark and a
    coaching chapter label)."""
    return {
        "question_id": record.get("question_id"),
        "stem": record.get("stem_en") or "",
        "statements": record.get("statements") or [],
        "list_i": record.get("list_i") or [],
        "list_ii": record.get("list_ii") or [],
        "options": record.get("options_en") or {},
    }


def _b9_candidate_view(cand):
    """One candidate as the agent sees it. Everything the sheet knows beyond these five fields
    -- Chapter Name, Chapter No, Topic, Question Type, Answer -- is withheld (CLAUDE.md), and
    the source URL is withheld too (the agent has no network tool; a URL would only invite it to
    pretend it fetched one). `question_text` is the sheet's Question column with its image
    markdown stripped, so the agent never sees a URL it cannot open."""
    return {
        "candidate_id": cand["candidate_id"],
        "similarity": cand["similarity"],
        "figure_image": cand.get("figure_image"),
        "question_text": recover_figures.strip_image_markdown(cand["question_text"]),
    }


class B9Plugin:
    step = "B9"
    agent = "b9-figure-matcher"

    # ---- item space ----------------------------------------------------------------------

    def _candidates(self):
        """{qid: record} for every question that needs a figure recovered: B3 said
        has_figure: true, and the record has not been absorbed into another by a C1 merge.

        Deliberately NOT gated on the B5 join (_b_qid_records) the way B6/B7/B8/C1/D* are:
        has_figure comes from B3 and recovering a diagram has nothing to do with the answer key,
        so requiring B5 would only delay the recovery. Questions with has_figure false are not
        items of this step at all -- they get no status file and no 'skipped' marker, since the
        step does not apply to them in the same sense B3 'applies' to every question."""
        out = {}
        records_dir = rc.pp("papers", "records")
        if not os.path.isdir(records_dir):
            return out
        for fn in sorted(os.listdir(records_dir)):
            if not fn.endswith(".json") or fn.startswith("_"):
                continue
            record = _read_json(os.path.join(records_dir, fn))
            if record.get("has_figure") is not True or record.get("merged_into"):
                continue
            out[fn[: -len(".json")]] = record
        return out

    def list_reason(self):
        return ("B9 needs a question record with has_figure: true (set by B3) that no C1 merge "
                "has absorbed. None found, or every such question already has a resolved B9 "
                "status / output pending --check.")

    # ---- SCRIPT half ----------------------------------------------------------------------

    def _shortlist_path(self, item_id, run_label):
        return rc.pp("steps", self.step, "work", f"{item_id}.{run_label}.shortlist.json")

    def _load_shortlist(self, item_id, run_label):
        path = self._shortlist_path(item_id, run_label)
        return _read_json(path) if os.path.exists(path) else None

    def _build_shortlist(self, item_id, record, run_label, index):
        """Run the SCRIPT half for one question and persist its full result (scores, row ids,
        source URLs, download errors) beside the agent's own, much narrower, input file. The
        agent never sees this file; it is the provenance trail for everything the plugin does
        afterwards, and it is what makes a re-run free (the images are already cached)."""
        result = recover_figures.shortlist_and_fetch(item_id, record=record, index=index,
                                                     run_label=run_label)
        lib_io.atomic_write_json(self._shortlist_path(item_id, run_label), result)
        return result

    def _dispatch(self, item_id, record, shortlist, run_label, previous_failure=None):
        usable = [c for c in shortlist["candidates"] if c.get("figure_image")]
        input_data = {
            "question": _b9_question_view(record),
            "candidates": [_b9_candidate_view(c) for c in usable],
        }
        if previous_failure:
            input_data["previous_attempt_failed"] = previous_failure
        _write_json(_work_input_path(self.step, item_id, run_label), input_data)
        return ListLine(item_id, self.agent,
                        _relpath(_work_input_path(self.step, item_id, run_label)),
                        _relpath(_out_path(self.step, item_id, run_label)), run_label)

    # ---- terminal resolutions ---------------------------------------------------------------

    def _resolve_unmatched(self, item_id, shortlist, reason, run_label, prompt_version, flags_cat,
                           data=None):
        """Nothing is attached: no candidate cleared the floor, the agent said "none", or it said
        "low" (treated identically -- hard rule 3: a flagged ambiguous match beats a wrong
        figure). has_figure stays true, so the gap stays visible, and the flag carries the full
        shortlist as its provisional_value so a reviewer can see what WAS considered."""
        rc.raise_flag("item", item_id, self.step, "B9_FIGURE_UNMATCHED",
                      flags_cat.get("B9_FIGURE_UNMATCHED", "normal"), reason,
                      provisional_value={"shortlist": shortlist, "agent_output": data},
                      evidence=[_relpath(self._shortlist_path(item_id, run_label))],
                      prompt_version=prompt_version)
        rc.write_item_status(self.step, item_id, "flagged", prompt_version,
                             extra={"run": run_label, "check_message": reason})
        rc.append_run_log(item_id, self.step, run_label, self.agent if data else None,
                          prompt_version, rc.now_iso(), rc.now_iso(), "fail", reason, None,
                          "flagged")

    def _resolve_accepted(self, item_id, record, shortlist, cand, data, run_label, prompt_version,
                          flags_cat):
        figure_path, err = recover_figures.attach_figure(item_id, cand)
        if err:
            msg = (f"B9_FIGURE_DOWNLOAD_FAILED: agent accepted {cand['candidate_id']} "
                   f"({cand['row_id']}) but its image could not be attached: {err}")
            rc.raise_flag("item", item_id, self.step, "B9_FIGURE_DOWNLOAD_FAILED",
                          flags_cat.get("B9_FIGURE_DOWNLOAD_FAILED", "high"), msg,
                          provisional_value=data, prompt_version=prompt_version)
            self._resolve_unmatched(item_id, shortlist, msg, run_label, prompt_version, flags_cat,
                                    data=data)
            return

        extra_urls = cand["figure_urls"][1:]
        fields = {
            "figure_path": figure_path,
            "figure_source_url": cand["figure_url"],
            # Provenance only, never a judgement: which sheet row this came from, so an auditor
            # can go back to it. The sheet's chapter/topic/type/answer columns are not recorded
            # anywhere on the record (CLAUDE.md) -- only the row's identity.
            "figure_source_row": cand["row_id"],
            "figure_match_confidence": data["confidence"],
        }
        if extra_urls:
            fields["figure_source_urls_unused"] = extra_urls
        # Status on the record's own field_sources is "flagged", never "pass": a recovered figure
        # is third-party provenance that nothing in this pipeline can verify against the original
        # paper, and B9_FIGURE_RECOVERED below says so permanently.
        lib_records.set_fields(item_id, fields, step=self.step, prompt_version=prompt_version,
                               status="flagged")

        thin = (not shortlist.get("clear_gap")) or data["confidence"] == "medium"
        rc.raise_flag("item", item_id, self.step, "B9_FIGURE_RECOVERED",
                      flags_cat.get("B9_FIGURE_RECOVERED", "low"),
                      f"figure recovered from a legacy sheet ({cand['row_id']}), not from the "
                      f"original paper; b9-figure-matcher judged that it BELONGS to this question "
                      f"(confidence {data['confidence']}), NOT that it is correct -- nothing in "
                      f"this pipeline verifies it against the printed paper. why: {data['why']}",
                      provisional_value={"figure_path": figure_path,
                                         "figure_source_url": cand["figure_url"]},
                      evidence=[figure_path], prompt_version=prompt_version)
        if thin:
            rc.raise_flag("item", item_id, self.step, "B9_FIGURE_THIN_MARGIN",
                          flags_cat.get("B9_FIGURE_THIN_MARGIN", "normal"),
                          f"accepted on a thin margin: shortlist gap to the runner-up was "
                          f"{shortlist.get('gap_ratio')}x (clear at "
                          f"{recover_figures.CLEAR_GAP_RATIO}x) and agent confidence was "
                          f"{data['confidence']}",
                          provisional_value={"shortlist": shortlist, "agent_output": data},
                          prompt_version=prompt_version)
        if extra_urls:
            rc.raise_flag("item", item_id, self.step, "B9_FIGURE_EXTRA_IMAGES",
                          flags_cat.get("B9_FIGURE_EXTRA_IMAGES", "low"),
                          f"the matched sheet row carries {len(cand['figure_urls'])} images; only "
                          f"the first (the stem figure) was attached. The rest are recorded on "
                          f"the record as figure_source_urls_unused and are usually the question's "
                          f"four option diagrams -- a real remaining gap for this question.",
                          provisional_value={"unused": extra_urls}, prompt_version=prompt_version)

        msg = (f"attached {cand['candidate_id']} ({cand['row_id']}) as {figure_path}; "
               f"confidence {data['confidence']}" + (" (thin margin)" if thin else ""))
        rc.write_item_status(self.step, item_id, "flagged", prompt_version,
                             extra={"run": run_label, "check_message": msg})
        rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version, rc.now_iso(),
                          rc.now_iso(), "pass", msg, None, "flagged")

    # ---- list_items / check -----------------------------------------------------------------

    def _fresh(self, filters):
        """[(item_id, record)] for every in-scope item with no resolved status for this prompt
        version."""
        prompt_version = rc.get_prompt_version(self.step)
        out = []
        for qid, record in self._candidates().items():
            if not rc.item_passes_filters(qid, filters):
                continue
            status = rc.read_item_status(self.step, qid)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            out.append((qid, record))
        return out

    def list_items(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        todo = self._fresh(filters)
        if not todo:
            return []
        index = recover_figures.load_figure_index()
        lines = []
        for item_id, record in todo:
            if os.path.exists(_out_path(self.step, item_id, "runA")):
                continue  # already dispatched; check() drives it from here
            shortlist = self._load_shortlist(item_id, "runA") \
                or self._build_shortlist(item_id, record, "runA", index)
            for cand in shortlist["candidates"]:
                if cand.get("download_error"):
                    rc.raise_flag("item", item_id, self.step, "B9_FIGURE_DOWNLOAD_FAILED",
                                  flags_cat.get("B9_FIGURE_DOWNLOAD_FAILED", "high"),
                                  f"{cand['candidate_id']} ({cand['row_id']}) "
                                  f"{cand['figure_url']}: {cand['download_error']}",
                                  prompt_version=prompt_version)
            usable = [c for c in shortlist["candidates"] if c.get("figure_image")]
            if not shortlist["above_floor"] or not usable:
                reason = (
                    f"no legacy-sheet figure row is close enough to this question: best "
                    f"similarity {shortlist['top_similarity']} < floor "
                    f"{recover_figures.MIN_TOP_SIMILARITY}"
                    if not shortlist["above_floor"] else
                    "every shortlisted figure failed to download; nothing to show the agent")
                self._resolve_unmatched(item_id, shortlist, reason, "runA", prompt_version,
                                        flags_cat)
                continue
            lines.append(self._dispatch(item_id, record, shortlist, "runA"))
        return lines

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        fallback = cfg.get("fallback") or []
        new_lines = []

        for item_id, record in self._fresh(filters):
            runs = _outputs_by_item(self.step).get(item_id, {})
            run_label = "retry1" if "retry1" in runs else ("runA" if "runA" in runs else None)
            if run_label is None:
                continue  # never dispatched, or still waiting on the agent
            shortlist = self._load_shortlist(item_id, "runA")
            if shortlist is None:
                continue  # list_items has not built this item's shortlist yet
            by_id = {c["candidate_id"]: c for c in shortlist["candidates"]}

            data = _read_json(_out_path(self.step, item_id, run_label))
            started = rc.now_iso()
            input_data = _read_json(_work_input_path(self.step, item_id, run_label))
            if isinstance(data, dict) and "error" in data:
                ok, msg = False, f"agent reported error: {data['error']}"
            else:
                ok, msg = rc.validate_schema(self.step, data)
                if ok:
                    ok, msg = rc.run_step_check(self.step, data, {
                        "item_id": item_id, "step": self.step, "input_data": input_data,
                        "project_root": rc.pp(),
                    })

            if not ok:
                if run_label == "runA" and "retry" in fallback:
                    rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version,
                                      started, rc.now_iso(), "fail", msg, None, "pending")
                    rc.write_pending(self.step, item_id, {"reason": msg, "next_run": "retry1"})
                    new_lines.append(self._dispatch(item_id, record, shortlist, "retry1",
                                                    previous_failure=msg))
                else:
                    # Retry exhausted: a malformed verdict is no verdict, so the safe default
                    # (attach nothing) applies, exactly as it does for an honest "none".
                    self._resolve_unmatched(item_id, shortlist,
                                            f"B9_FIGURE_UNMATCHED: agent output unusable after "
                                            f"retry ({msg})", run_label, prompt_version, flags_cat,
                                            data=data)
                continue

            if data["match"] == "none" or data["confidence"] == "low":
                reason = (f"B9_FIGURE_UNMATCHED: agent match={data['match']} "
                          f"confidence={data['confidence']} -- attaching nothing. "
                          f"why: {data['why']}")
                self._resolve_unmatched(item_id, shortlist, reason, run_label, prompt_version,
                                        flags_cat, data=data)
                continue

            self._resolve_accepted(item_id, record, shortlist, by_id[data["match"]], data,
                                   run_label, prompt_version, flags_cat)

        return new_lines

    def auto(self, filters):
        """The SCRIPT half on its own (scripts/CONVENTIONS.md hybrid shape): build every in-scope
        item's shortlist and download its candidate images, so the fetching is done and cached
        before any agent is dispatched. Resolving items and emitting agent lines is still
        list_items/check's job, which cmd_auto calls straight afterwards."""
        todo = self._fresh(filters)
        if not todo:
            return
        index = recover_figures.load_figure_index()
        for item_id, record in todo:
            if self._load_shortlist(item_id, "runA") is None:
                result = self._build_shortlist(item_id, record, "runA", index)
                print(f"{item_id}: {len(result['candidates'])} candidate(s), "
                      f"top similarity {result['top_similarity']}, gap {result['gap_ratio']}x")


# ===========================================================================
# B10 - Split the recovered figure into one picture per option (NOT in docs/SPEC.md: a deliberate,
# owner-approved EXTENSION beyond the spec's Stage B, same standing as B9. See config/steps.yaml's
# B10 entry for the full justification.)
#
# Item = one question whose OPTIONS or LIST ENTRIES are pictures that were never captured, and
# which B9 has already recovered a figure for. Worker is SCRIPT + AGENT:
#   SCRIPT: find those questions, measure the figure, write the slot list (scripts/split_figures.py)
#   AGENT:  b10-figure-splitter returns one box per picture, with the label printed beside it
#   SCRIPT: crop each box to papers/figures/<QID>/<name>.png
#
# The correctness rule, enforced in scripts/checks/B10.py rather than trusted to the brief: a
# printed panel label is the SOURCE paper's label. list_i/list_ii/statements slots MAY be filled
# from it (our record holds the same labels against the same content); opt1-opt4 may NEVER be,
# because our option text is empty and booklet codes shuffle option order. The first run of this
# step claimed opt slots on four questions purely because the panels were numbered (1)-(4); for
# Q-000343 that would have mislabelled every option, since the official key for our booklet says
# 4 while the physically correct plot is printed (2).
#
# This step writes NO field onto papers/records/. Crops live on disk and the exporters resolve
# them, so re-running cannot corrupt a record.
# ===========================================================================
class B10Plugin:
    step = "B10"
    agent = "b10-figure-splitter"

    def _candidates(self):
        """{qid: record} for every question with picture-only slots AND a figure to cut from.

        Questions with placeholder slots but no recovered figure are deliberately NOT items: there
        is nothing to split, and giving them a status would claim this step had considered them.
        They stay visible as B9's own unfinished business.
        """
        records = split_figures.load_records()
        ready, _blocked = split_figures.candidates(records)
        return {qid: rec for qid, rec, _slots, _fig in ready}

    def list_reason(self):
        return ("B10 needs a question whose options or list entries are pictures (placeholder text "
                "from B3) AND a figure recovered by B9 to cut them out of. None found, or every "
                "such question already has a resolved B10 status / output pending --check.")

    def _build_agent_input(self, qid, record):
        slots = split_figures.placeholder_slots(record)
        fig = (record.get("figure_path") or "").strip()
        width, height = split_figures.image_size(rc.pp(fig))
        return {
            "question_id": qid,
            "figure_image": fig,
            "image_width": width,
            "image_height": height,
            "stem": record.get("stem_en") or "",
            "slots": [s for s, _ in slots],
            "slot_texts": {s: t for s, t in slots},
        }

    def _fresh(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        out = []
        for qid, record in self._candidates().items():
            if not rc.item_passes_filters(qid, filters):
                continue
            status = rc.read_item_status(self.step, qid)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            out.append((qid, record))
        return out

    def list_items(self, filters):
        lines = []
        for qid, record in self._fresh(filters):
            if rc.read_pending(self.step, qid) \
                    or os.path.exists(_out_path(self.step, qid, "runA")):
                continue
            _write_json(_work_input_path(self.step, qid, "runA"),
                        self._build_agent_input(qid, record))
            lines.append(ListLine(qid, self.agent,
                                  _relpath(_work_input_path(self.step, qid, "runA")),
                                  _relpath(_out_path(self.step, qid, "runA")), "runA"))
        return lines

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)

        items_with_builders, agent_inputs = {}, {}
        for qid, record in self._candidates().items():
            if not rc.item_passes_filters(qid, filters):
                continue
            payload = self._build_agent_input(qid, record)
            items_with_builders[qid] = payload
            agent_inputs[qid] = payload

        def _post(item_id, run_label, data, status):
            """Crop whatever the agent could place, and flag what it could not."""
            panels = (data or {}).get("panels") or []
            if not panels:
                rc.raise_flag("item", item_id, self.step, "B10_NO_PANELS",
                              flags_cat.get("B10_NO_PANELS", "normal"),
                              f"nothing could be cut from this question's figure: "
                              f"{str((data or {}).get('note'))[:220]}",
                              evidence=[(self._candidates().get(item_id) or {}).get("figure_path")],
                              prompt_version=prompt_version)
                return
            made, unmapped = split_figures.crop_panels(item_id, panels)
            if unmapped:
                rc.raise_flag(
                    "item", item_id, self.step, "B10_SLOTS_UNMAPPED",
                    flags_cat.get("B10_SLOTS_UNMAPPED", "normal"),
                    f"{len(unmapped)} panel(s) cut but not tied to one of this question's slots "
                    f"(source labels {sorted(unmapped)}). Expected for option slots: our option "
                    f"text was never printed, so a printed label is the source paper's option "
                    f"order and booklet codes shuffle it. A reviewer must confirm the mapping "
                    f"before these can be read as option 1-4.",
                    provisional_value={"panels": unmapped},
                    evidence=sorted(unmapped.values()), prompt_version=prompt_version)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                        agent_inputs=agent_inputs)


# ===========================================================================
# Shared page selector for every A2 BACKFILL step (A2B bold, A2I italic, A2L layout, A2N
# notation). All four answer the same question -- "which already-read A2 pages may I look at?" --
# and each used to answer it with its own private copy of this loop, which is how they silently
# drifted into agreeing on a rule that was wrong.
#
# WHY `flagged` COUNTS, NOT JUST `pass`. Every copy of this selector used to require
# `status == "pass"` exactly. A `flagged` A2 page is NOT a rejected page: spec 5.4 defines
# flagged as "a value exists but needs a human look", and "Next step runs? yes, with the
# provisional value" -- so excluding it was never the spec's rule, it was an accident of four
# copy-pasted loops.
#
# The consequence was concrete and backwards. PHY12O-ch01-p024 is flagged, and it is flagged
# because scripts/checks/A2.py scores PROSE WORDS against the page's text layer while this
# page's actual defect is NOTATION. So the single page in that chapter with the worst notation
# garble was the one page A2N -- the notation fixer -- structurally could not see. Measured at
# the time of this change: PHY12O-ch01 has 50 pages with A2 output; A2B, A2L and A2N each had
# exactly 49, and p024 was the one missing from all three. A page being flagged is the strongest
# available signal that it needs a second look, which is exactly what a backfill step is.
#
# WHAT STAYS EXCLUDED, DELIBERATELY. Checked against the real steps/A2/status/ at the time of
# this change: the only status values present are `pass` (1166) and `flagged` (12), plus 67
# `<item>.pending.json` markers which are mid-chain progress records with no `status` key at all
# and are not statuses. `blocked`, `stale` and `skipped` do not currently occur here, and all
# three are excluded on purpose rather than by accident:
#   - `blocked` (spec 5.4: "Nothing sensible can continue; later steps skip the item") -- an
#     unreadable page has no trustworthy block text to point italic/bold spans INTO, so a
#     backfill would be marking up a transcription nobody believes.
#   - `stale` (cleared by the cascade, must be re-read first) -- its block text is about to
#     change, so anything keyed to its block `n`s would be junk on arrival.
#   - `skipped` -- the step did not apply, so there is no page read to annotate.
# A missing/unparseable status file, and a pending marker, also stay excluded: no status means
# A2 has not finished with the page.
# ===========================================================================
_A2_BACKFILL_STATUSES = ("pass", "flagged")


def _a2_backfill_pages():
    """[(item_id, run_label)] for every A2 item a backfill step may annotate -- i.e. whose A2
    status is pass or flagged. run_label is the status's own newest run (retry1 where A2 was
    retried), falling back to runA."""
    out = []
    status_dir = rc.pp("steps", "A2", "status")
    if not os.path.isdir(status_dir):
        return out
    for fn in sorted(os.listdir(status_dir)):
        if not fn.endswith(".json") or ".last_block" in fn or ".pending" in fn:
            continue
        item_id = fn[:-len(".json")]
        status = rc.read_item_status("A2", item_id)
        if not status or status.get("status") not in _A2_BACKFILL_STATUSES:
            continue
        out.append((item_id, status.get("run") or "runA"))
    return out


def _a2_prose_blocks(data, kinds, extra_fields=()):
    """Read-only view of an A2 output's prose blocks for a backfill step's agent input.

    Only blocks with a real integer `n` are returned: `n` is the join key between A2's output and
    every backfill file, and a block without one cannot be addressed, covered or checked. This is
    not hypothetical -- BIO12L-ch03-p001.retry1 is a real flagged page all 7 of whose blocks lack
    the schema-required `n` (docs/OPEN_QUESTIONS.md, 2026-10-10; tests/test_a2_check.py KNOWN_BAD).
    Letting it through would hand an agent `"n": null` and guarantee a check failure it could do
    nothing about. Dropping such blocks leaves the page with no coverable blocks, so it falls out
    of the step's candidate list entirely rather than failing.
    """
    out = []
    for b in (data.get("blocks") or []):
        if not isinstance(b.get("n"), int):
            continue
        if b.get("kind") not in kinds or not (b.get("text") or "").strip():
            continue
        entry = {"n": b["n"], "kind": b.get("kind"), "text": b.get("text") or ""}
        for field in extra_fields:
            entry[field] = [t for t in (b.get(field) or []) if isinstance(t, str)]
        out.append(entry)
    return out


# ===========================================================================
# A2B - Backfill bold terms onto already-read pages (NOT in docs/SPEC.md: a deliberate,
# owner-approved EXTENSION beyond the spec's Stage A, same standing as A2S/B9/B10. See
# config/steps.yaml's A2B entry for the full justification.)
#
# Item = one page A2 has already read and PASSED, whose blocks have not yet been checked for
# bold terms. Worker is SCRIPT + AGENT: SCRIPT finds such pages and lists their paragraph/box/
# list blocks (n, kind, text) read-only from the finished A2 output; AGENT (a2b-bold-marker)
# names which of those blocks have bold prose and what the bold substrings are.
#
# This step writes NO field onto the original A2 output -- CLAUDE.md: never edit an agent's
# output. It writes its own file under steps/A2B/out/, keyed by the same item_id, and a consumer
# wanting bold terms reads both files side by side, joined on block n.
# ===========================================================================
class A2BPlugin:
    step = "A2B"
    agent = "a2b-bold-marker"

    _BOLDABLE_KINDS = ("paragraph", "box", "list")

    def _candidates(self):
        """{item_id: [{"n","kind","text"}, ...]} for every PASSED A2 page with prose blocks,
        read-only from steps/A2/out/ -- never written back to."""
        out = {}
        for item_id, run_label in self._passed_a2_pages():
            path = _out_path("A2", item_id, run_label)
            if not os.path.exists(path):
                continue
            data = _read_json(path)
            if not isinstance(data, dict):
                continue
            blocks = _a2_prose_blocks(data, self._BOLDABLE_KINDS)
            if blocks:
                out[item_id] = blocks
        return out

    def _passed_a2_pages(self):
        """Every A2 page a backfill step may annotate -- see _a2_backfill_pages for why that is
        pass OR flagged, and which statuses stay excluded."""
        return _a2_backfill_pages()

    def list_reason(self):
        return ("A2B needs an A2 page already read (status pass or flagged) with at least one "
                "paragraph/box/list block whose bold terms have not been backfilled yet. None "
                "found, or every such page already has a resolved A2B status / output pending "
                "--check.")

    def _build_agent_input(self, item_id, blocks):
        img = None
        a2_input = _read_json(_work_input_path("A2", item_id, "runA"))
        if isinstance(a2_input, dict):
            img = a2_input.get("image")
        return {"item_id": item_id, "image": img, "blocks": blocks}

    def _fresh(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        out = []
        for item_id, blocks in self._candidates().items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            out.append((item_id, blocks))
        return out

    def list_items(self, filters):
        lines = []
        for item_id, blocks in self._fresh(filters):
            if rc.read_pending(self.step, item_id) \
                    or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            _write_json(_work_input_path(self.step, item_id, "runA"),
                        self._build_agent_input(item_id, blocks))
            lines.append(ListLine(item_id, self.agent,
                                  _relpath(_work_input_path(self.step, item_id, "runA")),
                                  _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)

        items_with_builders, agent_inputs = {}, {}
        for item_id, blocks in self._candidates().items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            payload = self._build_agent_input(item_id, blocks)
            items_with_builders[item_id] = payload
            agent_inputs[item_id] = payload

        def _post(item_id, run_label, data, status):
            if status != "pass":
                rc.raise_flag("item", item_id, self.step, "A2B_INCOMPLETE",
                              flags_cat.get("A2B_INCOMPLETE", "normal"),
                              f"bold-term backfill did not complete for this page after retry",
                              prompt_version=prompt_version)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                        agent_inputs=agent_inputs)


# ===========================================================================
# A2I - Backfill ITALIC terms onto already-read pages (NOT in docs/SPEC.md: a deliberate,
# owner-approved EXTENSION beyond the spec's Stage A, same standing as A2B/A2L/A2N/A2S/B9/B10.
# See config/steps.yaml's A2I entry for the full justification.)
#
# A2B's twin for the other typesetting NCERT uses deliberately. Italics were captured NOWHERE
# before this and were actively discarded: three agent briefs told the reader to recognise
# italics only so it could throw them away, and A2's block schema is additionalProperties:false
# with no italic field. Measured loss, steps/A2B/out/PHY12O-ch01-p001.runA.json: that page's
# bold-term backfill found no bold prose at all and had to write "n=4's closing sentence
# ("Electrostatics deals with...") is italic, not bold. n=6's "elektron" and "amber" are italic,
# not bold." into its free-text note -- the chapter's own definition of electrostatics and the
# etymology of "electricity", correctly judged and then lost. The italicised sentence is very
# often the exact sentence a PYQ question quotes.
#
# Item = one already-read A2 page (status pass or flagged -- see _a2_backfill_pages) whose blocks
# have not yet been checked for italic terms. Worker is SCRIPT + AGENT: SCRIPT finds such pages
# and lists their paragraph/box/list blocks (n, kind, text, AND the bold_terms already decided
# for them) read-only from the finished A2 output plus A2B's own backfill; AGENT
# (a2i-italic-marker) names which of those blocks have italic prose and what the italic
# substrings are (enforced by scripts/checks/A2I.py).
#
# bold_terms is in the agent's input for one reason: bold and italic are mutually exclusive
# typesettings of the same characters, so the agent must see what is already claimed as bold in
# order not to repeat it, and the check enforces that -- A2I's one check beyond A2B's list.
#
# This step writes NO field onto the original A2 output -- CLAUDE.md: never edit an agent's
# output. It writes its own file under steps/A2I/out/, keyed by the same item_id, and a consumer
# wanting italic terms reads both files side by side, joined on block n.
# ===========================================================================
class A2IPlugin:
    step = "A2I"
    agent = "a2i-italic-marker"

    _ITALICABLE_KINDS = ("paragraph", "box", "list")

    def _known_bold_terms(self, item_id):
        """{block n: [bold term, ...]} already recorded for this page by step A2B, read-only.

        A page read before `bold_terms` existed carries its bold terms in A2B's separate output
        rather than on the A2 block itself, so both sources have to be consulted to tell the
        italic marker what is already spoken for."""
        status = rc.read_item_status("A2B", item_id)
        runs = [status.get("run")] if status and status.get("run") else []
        runs += ["retry1", "runA"]
        for run_label in runs:
            path = _out_path("A2B", item_id, run_label)
            if not run_label or not os.path.exists(path):
                continue
            data = _read_json(path)
            if not isinstance(data, dict) or "error" in data:
                continue
            return {b.get("n"): [t for t in (b.get("bold_terms") or []) if isinstance(t, str)]
                    for b in (data.get("blocks") or []) if isinstance(b.get("n"), int)}
        return {}

    def _candidates(self):
        """{item_id: [{"n","kind","text","bold_terms"}, ...]} for every already-read A2 page with
        prose blocks, read-only from steps/A2/out/ (+ steps/A2B/out/) -- never written back to."""
        out = {}
        for item_id, run_label in self._passed_a2_pages():
            path = _out_path("A2", item_id, run_label)
            if not os.path.exists(path):
                continue
            data = _read_json(path)
            if not isinstance(data, dict):
                continue
            blocks = _a2_prose_blocks(data, self._ITALICABLE_KINDS, extra_fields=("bold_terms",))
            if not blocks:
                continue
            backfilled = self._known_bold_terms(item_id)
            for b in blocks:
                merged = list(b["bold_terms"])
                for term in backfilled.get(b["n"]) or []:
                    if term not in merged:
                        merged.append(term)
                b["bold_terms"] = merged
            out[item_id] = blocks
        return out

    def _passed_a2_pages(self):
        """Every A2 page a backfill step may annotate -- see _a2_backfill_pages for why that is
        pass OR flagged, and which statuses stay excluded."""
        return _a2_backfill_pages()

    def list_reason(self):
        return ("A2I needs an A2 page already read (status pass or flagged) with at least one "
                "paragraph/box/list block whose italic terms have not been backfilled yet. None "
                "found, or every such page already has a resolved A2I status / output pending "
                "--check.")

    def _build_agent_input(self, item_id, blocks):
        img = None
        a2_input_path = _work_input_path("A2", item_id, "runA")
        if os.path.exists(a2_input_path):
            a2_input = _read_json(a2_input_path)
            if isinstance(a2_input, dict):
                img = a2_input.get("image")
        return {"item_id": item_id, "image": img, "blocks": blocks}

    def _fresh(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        out = []
        for item_id, blocks in self._candidates().items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            out.append((item_id, blocks))
        return out

    def list_items(self, filters):
        lines = []
        for item_id, blocks in self._fresh(filters):
            if rc.read_pending(self.step, item_id) \
                    or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            _write_json(_work_input_path(self.step, item_id, "runA"),
                        self._build_agent_input(item_id, blocks))
            lines.append(ListLine(item_id, self.agent,
                                  _relpath(_work_input_path(self.step, item_id, "runA")),
                                  _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)

        items_with_builders, agent_inputs = {}, {}
        for item_id, blocks in self._candidates().items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            payload = self._build_agent_input(item_id, blocks)
            items_with_builders[item_id] = payload
            agent_inputs[item_id] = payload

        def _post(item_id, run_label, data, status):
            if status != "pass":
                rc.raise_flag("item", item_id, self.step, "A2I_INCOMPLETE",
                              flags_cat.get("A2I_INCOMPLETE", "normal"),
                              "italic-term backfill did not complete for this page after retry",
                              prompt_version=prompt_version)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                        agent_inputs=agent_inputs)




# ===========================================================================
# A2R - Review a rendered export page against the book page (NOT in docs/SPEC.md: a deliberate,
# owner-approved extension, same standing as A2S/A2B/A2L/A2N/A2C.)
#
# Item = one page of one chapter's rendered export. Worker is SCRIPT + AGENT: SCRIPT renders the
# two pages side by side as images; AGENT (a2r-render-reviewer) says what differs.
#
# It exists because every other check in this project looks at the INPUT. Nothing judged the
# OUTPUT, so a worked example printed twice, a structure cropped in half and half-empty pages were
# all shipped by builds that reported success and were found only when the owner read the PDF.
# scripts/check_*_export.py catch what can be stated as a rule; a clipped benzene ring cannot be.
# ===========================================================================
class A2RPlugin:
    step = "A2R"
    agent = "a2r-render-reviewer"

    _EXPORTS = {   # chapter -> (source pdf, rendered pdf)
        "CHE12L-ch05": ("inputs/ncert/latest/Class_12th/Chemistry/Chapter_5.pdf",
                        "exports/review/CHE12L-ch05_INORGANIC.pdf"),
        "CHE12L-ch09": ("inputs/ncert/latest/Class_12th/Chemistry/Chapter_9.pdf",
                        "exports/review/CHE12L-ch09_ORGANIC.pdf"),
    }
    _DPI = 120     # readable without being huge; the judgement is structural, not typographic

    def list_items(self, filters):
        lines = []
        for chapter, (src, out) in sorted(self._EXPORTS.items()):
            if not rc.item_passes_filters(chapter, filters):
                continue
            src_p, out_p = rc.pp(src), rc.pp(out)
            if not (os.path.exists(src_p) and os.path.exists(out_p)):
                continue
            try:
                import pymupdf as fitz
                n = min(fitz.open(src_p).page_count, fitz.open(out_p).page_count)
            except Exception:
                continue
            for page in range(1, n + 1):
                item_id = "%s-p%03d" % (chapter, page)
                if os.path.exists(_out_path(self.step, item_id, "runA")):
                    continue
                _write_json(_work_input_path(self.step, item_id, "runA"),
                            self._build_agent_input(item_id))
                lines.append(ListLine(
                    item_id, self.agent,
                    _relpath(_work_input_path(self.step, item_id, "runA")),
                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def why_empty(self):
        return ("A2R needs a chapter with BOTH a source PDF and a rendered export PDF on disk. "
                "None found, or every page already has an A2R review.")

    def _build_agent_input(self, item_id):
        chapter, page = item_id.rsplit("-p", 1)
        page = int(page)
        src, out = self._EXPORTS[chapter]
        work = rc.pp("steps", self.step, "work")
        os.makedirs(work, exist_ok=True)
        originals, rendered = os.path.join(work, item_id + ".original.png"), \
            os.path.join(work, item_id + ".rendered.png")
        try:
            import pymupdf as fitz
            for pdf, dest in ((rc.pp(src), originals), (rc.pp(out), rendered)):
                doc = fitz.open(pdf)
                doc[page - 1].get_pixmap(dpi=self._DPI).save(dest)
                doc.close()
        except Exception:
            pass
        return {"item_id": item_id, "original_image": originals, "rendered_image": rendered}


# ===========================================================================
# A2C - Read a drawn chemical structure into SMILES (NOT in docs/SPEC.md: a deliberate,
# owner-approved extension beyond Stage A, same standing as A2S/A2B/A2L/A2N. See config/steps.yaml
# for the full justification.)
#
# Item = one A2 figure block in a CHEMISTRY chapter whose artwork is a structural formula or a
# reaction scheme. Worker is SCRIPT + AGENT: SCRIPT finds those blocks and hands over the crop
# plus whatever A2S already read from it; AGENT (a2c-structure-transcriber) writes the SMILES.
#
# Why only chemistry: a structural formula is the only thing SMILES can express. Running this over
# physics or biology figures would ask an agent to find molecules in a ray diagram.
#
# Why figures and not equations: a displayed reaction in these chapters is already transcribed as
# LaTeX by A2S and rendered as live mathematical text, so it needs nothing from this step. What
# cannot be carried as text is the DRAWN ring, and that is a figure.
# ===========================================================================
class A2CPlugin:
    step = "A2C"
    agent = "a2c-structure-transcriber"

    _CHEM = ("CHE",)

    def list_items(self, filters):
        """One ListLine per chemistry figure block that has no SMILES yet."""
        lines = []
        for item_id, run_label in _a2_backfill_pages():
            if not item_id.upper().startswith(self._CHEM):
                continue
            if not rc.item_passes_filters(item_id, filters):
                continue
            path = _out_path("A2", item_id, run_label)
            if not os.path.exists(path):
                continue
            data = _read_json(path) or {}
            for b in data.get("blocks") or []:
                if b.get("kind") != "figure" or not b.get("needs_special"):
                    continue
                n = b.get("n")
                if not isinstance(n, int):
                    continue
                block_id = "%s-b%d" % (item_id, n)
                if os.path.exists(_out_path(self.step, block_id, "runA")):
                    continue
                _write_json(_work_input_path(self.step, block_id, "runA"),
                            self._build_agent_input(block_id))
                lines.append(ListLine(
                    block_id, self.agent,
                    _relpath(_work_input_path(self.step, block_id, "runA")),
                    _relpath(_out_path(self.step, block_id, "runA")), "runA"))
        return lines

    def why_empty(self):
        return ("A2C needs a chemistry figure block that A2 marked needs_special and that has no "
                "SMILES yet. None found, or every such block already has A2C output.")

    def _build_agent_input(self, item_id):
        """The crop and what A2S already read from it. The agent is given the picture and the
        words printed in it -- never the surrounding prose, which would invite it to infer a
        structure from the text instead of reading the drawing."""
        m = re.match(r"(.+)-b(\d+)$", item_id)
        page_item, n = m.group(1), int(m.group(2))
        a2s = None
        a2s_dir = rc.pp("steps", "A2S", "out")
        if os.path.isdir(a2s_dir):
            for fn in sorted(os.listdir(a2s_dir)):
                if fn.startswith(item_id + ".") and fn.endswith(".json"):
                    a2s = _read_json(os.path.join(a2s_dir, fn)) or a2s
        payload = {
            "item_id": item_id,
            "kind": "figure",
            "image": rc.pp("steps", "A2S", "work", item_id + ".png"),
            "caption": (a2s or {}).get("caption", ""),
            "labels": (a2s or {}).get("labels", []),
        }
        return payload


# ===========================================================================
# A2L - Read the PRINTED LAYOUT of an already-read page (NOT in docs/SPEC.md: a deliberate,
# owner-approved EXTENSION beyond the spec's Stage A, same standing as A2B/A2N/A2S/B9/B10.
# See config/steps.yaml's A2L entry for the full justification.)
#
# Item = one page A2 has already read and PASSED. Worker is SCRIPT + AGENT: SCRIPT finds such
# pages and lists their blocks read-only (n, kind, and a short text_head for position-matching
# only); AGENT (a2l-layout-reader) measures the page image and reports page geometry, column
# structure, and one entry per printed element with its region, column, relative type size and
# panel colour (enforced by scripts/checks/A2L.py).
#
# Why a separate step and not a field on A2: a page's ARRANGEMENT is a different kind of fact
# from its text, needs the image rather than the text layer, and is wanted for pages already
# read and checked. This step writes NO field onto the original A2 output -- CLAUDE.md: never
# edit an agent's output. It writes its own file under steps/A2L/out/, keyed by the same
# item_id; a consumer joins the two on block n.
# ===========================================================================
class A2LPlugin:
    step = "A2L"
    agent = "a2l-layout-reader"

    _TEXT_HEAD = 80  # enough to recognise which printed block this is, not a transcription

    def _candidates(self):
        """{item_id: [{"n","kind","text_head"}, ...]} for every PASSED A2 page, read-only from
        steps/A2/out/ -- never written back to."""
        out = {}
        for item_id, run_label in self._passed_a2_pages():
            path = _out_path("A2", item_id, run_label)
            if not os.path.exists(path):
                continue
            data = _read_json(path)
            if not isinstance(data, dict):
                continue
            blocks = [{"n": b.get("n"), "kind": b.get("kind"),
                       "text_head": (b.get("text") or "")[:self._TEXT_HEAD]}
                      for b in (data.get("blocks") or []) if isinstance(b.get("n"), int)]
            if blocks:
                out[item_id] = blocks
        return out

    def _passed_a2_pages(self):
        """Every A2 page a backfill step may annotate -- see _a2_backfill_pages for why that is
        pass OR flagged, and which statuses stay excluded."""
        return _a2_backfill_pages()

    def list_reason(self):
        return ("A2L needs an A2 page already read (status pass or flagged) whose printed layout "
                "has not been measured yet. None found, or every such page already has a "
                "resolved A2L status / output pending --check.")

    def _build_agent_input(self, item_id, blocks):
        img = None
        a2_input = _read_json(_work_input_path("A2", item_id, "runA"))
        if isinstance(a2_input, dict):
            img = a2_input.get("image")
        return {"item_id": item_id, "image": img, "blocks": blocks}

    def _fresh(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        out = []
        for item_id, blocks in self._candidates().items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            out.append((item_id, blocks))
        return out

    def list_items(self, filters):
        lines = []
        for item_id, blocks in self._fresh(filters):
            if rc.read_pending(self.step, item_id) \
                    or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            _write_json(_work_input_path(self.step, item_id, "runA"),
                        self._build_agent_input(item_id, blocks))
            lines.append(ListLine(item_id, self.agent,
                                  _relpath(_work_input_path(self.step, item_id, "runA")),
                                  _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)

        items_with_builders, agent_inputs = {}, {}
        for item_id, blocks in self._candidates().items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            payload = self._build_agent_input(item_id, blocks)
            items_with_builders[item_id] = payload
            agent_inputs[item_id] = payload

        def _post(item_id, run_label, data, status):
            if status != "pass":
                rc.raise_flag("item", item_id, self.step, "A2L_INCOMPLETE",
                              flags_cat.get("A2L_INCOMPLETE", "normal"),
                              "layout measurement did not complete for this page after retry",
                              prompt_version=prompt_version)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                        agent_inputs=agent_inputs)


# ===========================================================================
# A2N - Backfill correct inline notation onto already-read pages (NOT in docs/SPEC.md: a
# deliberate, owner-approved EXTENSION beyond the spec's Stage A, same standing as A2B/A2S/B9/
# B10. See config/steps.yaml's A2N entry for the full justification.)
#
# Item = one page A2 has already read and PASSED, whose blocks have not yet been checked for
# flattened exponents/subscripts or dropped radicals. Worker is SCRIPT + AGENT: SCRIPT finds
# such pages and lists their text-bearing blocks (n, text) read-only from the finished A2
# output; AGENT (a2n-notation-fixer) restores correct notation where the stored text flattened
# or dropped it, leaving all prose wording untouched (enforced by scripts/checks/A2N.py).
#
# This step writes NO field onto the original A2 output -- CLAUDE.md: never edit an agent's
# output. It writes its own file under steps/A2N/out/, keyed by the same item_id, and a
# consumer wanting corrected text reads both files side by side, joined on block n.
# ===========================================================================
class A2NPlugin:
    step = "A2N"
    agent = "a2n-notation-fixer"

    _NOTATION_KINDS = ("paragraph", "box", "list")

    def _candidates(self):
        """{item_id: [{"n","text"}, ...]} for every PASSED A2 page with text-bearing blocks,
        read-only from steps/A2/out/ -- never written back to."""
        out = {}
        for item_id, run_label in self._passed_a2_pages():
            path = _out_path("A2", item_id, run_label)
            if not os.path.exists(path):
                continue
            data = _read_json(path)
            if not isinstance(data, dict):
                continue
            blocks = [{"n": b["n"], "text": b["text"]}
                      for b in _a2_prose_blocks(data, self._NOTATION_KINDS)]
            if blocks:
                out[item_id] = blocks
        return out

    def _passed_a2_pages(self):
        """Every A2 page a backfill step may annotate -- see _a2_backfill_pages for why that is
        pass OR flagged, and which statuses stay excluded. Widening this is what finally lets
        A2N see PHY12O-ch01-p024, the chapter's worst notation garble, which was flagged for a
        PROSE-similarity shortfall and so had been invisible to the notation fixer."""
        return _a2_backfill_pages()

    def list_reason(self):
        return ("A2N needs an A2 page already read (status pass or flagged) with at least one "
                "text-bearing block whose inline notation has not been checked yet. None found, "
                "or every such page already has a resolved A2N status / output pending --check.")

    def _build_agent_input(self, item_id, blocks):
        img = None
        a2_input = _read_json(_work_input_path("A2", item_id, "runA"))
        if isinstance(a2_input, dict):
            img = a2_input.get("image")
        return {"item_id": item_id, "image": img, "blocks": blocks}

    def _fresh(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        out = []
        for item_id, blocks in self._candidates().items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            out.append((item_id, blocks))
        return out

    def list_items(self, filters):
        lines = []
        for item_id, blocks in self._fresh(filters):
            if rc.read_pending(self.step, item_id) \
                    or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            _write_json(_work_input_path(self.step, item_id, "runA"),
                        self._build_agent_input(item_id, blocks))
            lines.append(ListLine(item_id, self.agent,
                                  _relpath(_work_input_path(self.step, item_id, "runA")),
                                  _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)

        items_with_builders, agent_inputs = {}, {}
        for item_id, blocks in self._candidates().items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            payload = self._build_agent_input(item_id, blocks)
            items_with_builders[item_id] = payload
            agent_inputs[item_id] = payload

        def _post(item_id, run_label, data, status):
            if status != "pass":
                rc.raise_flag("item", item_id, self.step, "A2N_INCOMPLETE",
                              flags_cat.get("A2N_INCOMPLETE", "normal"),
                              f"notation backfill did not complete for this page after retry",
                              prompt_version=prompt_version)
                return
            n_corrected = sum(1 for b in (data.get("blocks") or []) if b.get("corrected_text"))
            if n_corrected:
                rc.raise_flag("item", item_id, self.step, "A2N_CORRECTED",
                              flags_cat.get("A2N_CORRECTED", "normal"),
                              f"{n_corrected} block(s) on this page had flattened notation or a "
                              f"dropped radical, now corrected in steps/A2N/out/{item_id}.json",
                              prompt_version=prompt_version)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                        agent_inputs=agent_inputs)


# ===========================================================================
# C1 - Merge booklet codes (spec 11/C1; .claude/agents/c1-booklet-matcher.md)
#
# Item = one shortlisted pair (one code's question, its closest other-code partner, same
# sitting). Worker is SCRIPT + AGENT (config/steps.yaml "script | c1-booklet-matcher", fixed from
# a plain agent-driven placeholder -- see that entry's own note): SCRIPT normalises + shortlists
# + runs every check named in spec 11/C1 ("Checks": one-to-one, count, key consistency); AGENT
# only decides exact_same/not_exact per shortlisted pair. This is the first DEDUP/MERGE logic in
# the pipeline -- no precedent to copy; the merge-record shape below is a documented judgment
# call (see the build report).
#
# Bespoke (non-generic) check(): spec 11/C1's own "On failure" chain is a real multi-stage state
# machine (compare -> [not_exact] -> reread (fresh B3, and B4 only if B4 originally used its own
# agent branch) -> compare again -> [still not_exact] -> x-adjudicator -> C1_READING_FIXED or
# C1_UNMATCHED), not the generic retry-once shape resolve_single_run_items implements -- same
# precedent as B3/A4/A6/B7's own bespoke check()s. Progress through the chain is tracked via
# runner_core's own pending-marker mechanism (rc.write_pending/read_pending), storing a `stage`
# field rather than inventing a new one: "compare1" (default/implicit) -> "reread" -> "compare2"
# -> "adjudicate" -> terminal (status file written, pending cleared by write_item_status).
# ===========================================================================

def _c1_normalise_text(s):
    """SCRIPT half's own normalisation step (spec 11/C1 procedure 1: 'normalise LaTeX and
    spacing for both sets'): text_normalise.normalise_quote (whitespace/curly-quote/ligature
    cleanup) feeding latex_normalise.normalise (LaTeX spacing-command/Unicode-math/\\text
    cleanup) -- the same two normalisers B4 already uses for comparing two independent readings
    of the same content (spec 5.7), reused here rather than writing a third normaliser."""
    return latex_normalise.normalise(text_normalise.normalise_quote(s or ""))


def _c1_normalise_labelled(items):
    return [{"label": it.get("label"), "text": _c1_normalise_text(it.get("text"))} for it in (items or [])]


def _c1_normalise_options(options_en):
    return {k: _c1_normalise_text(v) for k, v in (options_en or {}).items()}


def _c1_comparison_text(record):
    """One normalised blob per question (stem + statements + list_i + list_ii + all option
    text), used only for SCRIPT-side shortlisting similarity (word-trigram Jaccard, reusing
    scripts/pair_passages.py's own functions -- see module-level `import pair_passages` note).
    Never shown to the agent as-is; the agent's real input is the field-by-field view built by
    C1Plugin._agent_view."""
    parts = [record.get("stem_en") or ""]
    parts += [s.get("text", "") for s in (record.get("statements") or [])]
    parts += [s.get("text", "") for s in (record.get("list_i") or [])]
    parts += [s.get("text", "") for s in (record.get("list_ii") or [])]
    parts += list((record.get("options_en") or {}).values())
    return _c1_normalise_text(" ".join(parts))


def _c1_item_id(qid_a, qid_b):
    return f"{qid_a}|{qid_b}"


class C1Plugin:
    step = "C1"
    agent = "c1-booklet-matcher"

    # SCRIPT shortlist threshold: a question's best cross-code candidate must clear this
    # word-trigram Jaccard similarity (on the full stem+statements+lists+options blob) before
    # C1 even dispatches the agent on it. Chosen lower than A6's passage-pairing thresholds
    # (0.50/0.85) because a whole MCQ's trigram set is far more specific than an NCERT passage's
    # (numbers/option text rarely recur across unrelated questions the way prose phrasing can).
    # REAL numbers from this build's real E1-vs-E2 (NEET-2023-MAIN) test (see report): all 5
    # genuine cross-code duplicates found scored 0.72-1.0 (1.0, 1.0, 0.8182, 0.8049, 0.72) --
    # comfortably above 0.3. This run's real E2 subset was deliberately scanned around known
    # E1 content (see report), so it did not exercise a genuine non-match candidate's real
    # score; 0.3 is a documented judgment call (spec 11/C1 names no threshold at all, only
    # "most similar"), not yet pressure-tested against a true near-miss.
    SHORTLIST_THRESHOLD = 0.3

    # ---- grouping / shortlisting --------------------------------------------------------

    def _pairs_in_scope(self, filters):
        """Returns (pairs, records, skipped_sittings):
          pairs: {item_id: (qid_a, qid_b, similarity)} for every real shortlisted pair across
            every (exam, year, sitting) with 2+ distinct NATIVE codes among B5-joined question
            records. A record's native code is paper_codes[0]'s code (never its full, possibly
            merge-grown, paper_codes list) -- the same field the shared _b_paper_id_for/_b_qno_for
            helpers already key off, and stable across a merge (merge only ever APPENDS to
            paper_codes, never reorders it), so an already-merged canonical record is never
            mistaken for belonging to the code it merely absorbed.
          records: {qid: record} (B5-joined set this call used -- callers needing a record not
            in it, e.g. after a prior merge, re-read via lib_records.read_record directly).
          skipped_sittings: {sitting_key: codes_map} for every sitting with < 2 native codes
            (spec 11/C1 purpose line: 'otherwise skipped').
        Readiness gate ('needs: B8'): reuses the same B5-join signal _b_qid_records() already
        gives B6/B7/B8 (official_answer/status present) -- this build has no cleaner global
        'B8 is fully done for this paper' signal than that per-record readiness (B8 itself only
        ever touches bonus/dropped/multiple_accepted questions; a 'normal' question needs no B8
        run at all), so a question becomes C1-eligible the moment B5 has joined it, exactly the
        same documented judgment call B6/B7/B8 already made for their own 'needs' gates."""
        records = _b_qid_records()
        groups = {}
        for qid, record in records.items():
            if record.get("merged_into"):
                continue  # already absorbed; never re-offered as either side of a new pair
            codes = record.get("paper_codes") or []
            if not codes or ":" not in codes[0]:
                continue
            code = codes[0].split(":", 1)[0]
            sitting_key = f"{record.get('exam')}|{record.get('year')}|{record.get('sitting')}"
            groups.setdefault(sitting_key, {}).setdefault(code, []).append(qid)

        pairs = {}
        skipped = {}
        for sitting_key, codes_map in groups.items():
            if len(codes_map) < 2:
                skipped[sitting_key] = codes_map
                continue
            codes_sorted = sorted(codes_map)
            code_a = codes_sorted[0]
            for code_b in codes_sorted[1:]:
                for qid_a, qid_b, sim in self._shortlist(codes_map[code_a], codes_map[code_b], records):
                    pairs[_c1_item_id(qid_a, qid_b)] = (qid_a, qid_b, sim)
        return pairs, records, skipped

    def _shortlist(self, qids_a, qids_b, records):
        """SCRIPT half, spec 11/C1 procedure 1's second half: one-to-one assignment (Hungarian,
        via pair_passages._solve_assignment -- scipy if available, greedy fallback otherwise) of
        code_a's questions to code_b's questions by word-trigram Jaccard on
        _c1_comparison_text, keeping only pairs at/above SHORTLIST_THRESHOLD. Returns
        [(qid_a, qid_b, similarity), ...] sorted by descending similarity."""
        if not qids_a or not qids_b:
            return []
        grams = {q: pair_passages.word_trigrams(_c1_comparison_text(records[q]))
                 for q in list(qids_a) + list(qids_b)}
        qa_list, qb_list = list(qids_a), list(qids_b)
        sim = [[pair_passages.jaccard(grams[a], grams[b]) for b in qb_list] for a in qa_list]
        row_ind, col_ind = pair_passages._solve_assignment(sim)
        out = [(qa_list[r], qb_list[c], sim[r][c]) for r, c in zip(row_ind, col_ind)
               if sim[r][c] >= self.SHORTLIST_THRESHOLD]
        out.sort(key=lambda t: -t[2])
        return out

    def _mark_sitting_skipped(self, sitting_key, codes_map, prompt_version):
        item_id = f"SKIP:{sitting_key}"
        existing = rc.read_item_status(self.step, item_id)
        if existing and existing.get("status") != "stale" and existing.get("prompt_version") == prompt_version:
            return
        codes = sorted(codes_map)
        rc.write_item_status(self.step, item_id, "skipped", prompt_version, extra={
            "check_message": f"only {len(codes)} code(s) registered for this sitting {codes} -- "
                              f"C1 runs only for sittings with 2+ codes read (spec 11/C1)."})
        rc.append_run_log(item_id, self.step, "skipped", None, prompt_version, rc.now_iso(),
                            rc.now_iso(), "pass", "skipped (fewer than 2 codes)", None, "skipped")

    # ---- agent input shape ---------------------------------------------------------------

    def _agent_view(self, qid, records, override=None):
        """One side of c1-booklet-matcher's real Input contract ('a'/'b': paper_id, qno, stem,
        statements, lists, options (normalised)). `override`, when given, is a fresh
        b3-question-reader output (same field names as the record: stem_en, statements, list_i,
        list_ii, options_en -- B3Plugin._write_record copies them straight across) used instead
        of the record's own current fields, for the post-reread second comparison -- this never
        mutates the real record; only a confirmed exact_same (via _resolve_exact_same) ever
        writes anything back to papers/records/.
        Field-naming judgment call: the agent file says generically 'lists'; mapped here to this
        project's own list_i/list_ii field names (the record's real field names), consistent
        with every other agent's input mirroring the record schema rather than inventing a new
        wrapper key."""
        record = records.get(qid) or lib_records.read_record(qid)
        src = override if override is not None else record
        return {
            "paper_id": _b_paper_id_for(record), "qno": _b_qno_for(record),
            "stem": _c1_normalise_text(src.get("stem_en")),
            "statements": _c1_normalise_labelled(src.get("statements")),
            "list_i": _c1_normalise_labelled(src.get("list_i")),
            "list_ii": _c1_normalise_labelled(src.get("list_ii")),
            "options": _c1_normalise_options(src.get("options_en")),
        }

    def _dispatch_compare(self, item_id, qid_a, qid_b, records, run_label, reread, prompt_version):
        view_a = self._agent_view(qid_a, records, override=(reread or {}).get("a"))
        view_b = self._agent_view(qid_b, records, override=(reread or {}).get("b"))
        input_data = {"a": view_a, "b": view_b}
        _write_json(_work_input_path(self.step, item_id, run_label), input_data)
        return [ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, run_label)),
                           _relpath(_out_path(self.step, item_id, run_label)), run_label)]

    # ---- list_items / check ---------------------------------------------------------------

    def list_items(self, filters):
        pairs, records, skipped = self._pairs_in_scope(filters)
        prompt_version = rc.get_prompt_version(self.step)
        for sitting_key, codes_map in skipped.items():
            self._mark_sitting_skipped(sitting_key, codes_map, prompt_version)
        lines = []
        for item_id, (qid_a, qid_b, _sim) in pairs.items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if os.path.exists(_out_path(self.step, item_id, "runA")):
                continue  # already dispatched (stage1 or later); check() drives it from here
            lines.extend(self._dispatch_compare(item_id, qid_a, qid_b, records, "runA", None, prompt_version))
        return lines

    def list_reason(self):
        return ("C1 needs B5-joined question records (same readiness signal as B6/B7/B8) across "
                "2+ booklet codes of the same (exam, year, sitting). None found yet, every "
                "sitting seen so far has only 1 code registered (correctly 'skipped' per spec "
                "11/C1's own purpose line -- see steps/C1/status/SKIP:*.json), every shortlisted "
                "pair's similarity is below SHORTLIST_THRESHOLD, or everything matching already "
                "has output pending --check.")

    @staticmethod
    def _validate(step, data):
        if isinstance(data, dict) and "error" in data:
            return False, f"agent reported error: {data['error']}"
        ok, msg = rc.validate_schema(step, data)
        if not ok:
            return False, msg
        return rc.run_step_check(step, data, {"item_id": None, "step": step})

    def _resolve_blocked(self, item_id, msg, run_label, prompt_version):
        """A malformed/schema-or-check-failing agent output -- not a verdict-level outcome spec
        11/C1's own 'On failure' chain names at all, so (same precedent as B1/B5's generic
        fallback for an unnamed failure) this is a hard stop, not a chain step: flag generically
        (no catalogue code names this shape failure specifically) and block."""
        rc.raise_flag("item", item_id, self.step, f"{self.step}_CHECK_FAILED", "normal", msg,
                       prompt_version=prompt_version)
        rc.write_item_status(self.step, item_id, "blocked", prompt_version,
                               extra={"run": run_label, "check_message": msg})
        rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version, rc.now_iso(),
                            rc.now_iso(), "fail", msg, None, "blocked")

    # ---- key consistency / merge -----------------------------------------------------------

    @staticmethod
    def _check_key_consistency(rec_a, rec_b, option_map):
        """Spec 11/C1 Checks: 'both codes' keys point to the same option through the map.'
        a's official_answer (possibly multi, e.g. '1,3' for multiple_accepted) is translated
        option-by-option through option_map (A<n> -> B<m>) and compared against b's own
        official_answer as a SET (order-independent) -- the only merge-blocking check that reads
        outside the one agent output, hence lives here rather than in scripts/checks/C1.py (same
        split as B5's register-level checks)."""
        ans_a, ans_b = rec_a.get("official_answer"), rec_b.get("official_answer")
        if ans_a is None or ans_b is None:
            return False, "C1_KEY_INCONSISTENT: cannot verify -- at least one side has no official_answer yet (B5 not joined)"
        a_vals = [v.strip() for v in str(ans_a).split(",") if v.strip()]
        expected_b = set()
        for v in a_vals:
            mapped = option_map.get(f"A{v}")
            if not mapped:
                return False, f"C1_KEY_INCONSISTENT: option_map has no mapping for A's official option A{v}"
            expected_b.add(mapped[1:])
        b_vals = {v.strip() for v in str(ans_b).split(",") if v.strip()}
        if expected_b != b_vals:
            return False, (f"C1_KEY_INCONSISTENT: A's official_answer {ans_a!r} maps via option_map to B "
                            f"option(s) {sorted(expected_b)}, but B's own official_answer is {ans_b!r}")
        return True, "ok"

    @staticmethod
    def _translate_option_map(qid_a, qid_b, option_map, canonical):
        """option_map is always {'A1':'B2',...} (qid_a=A, qid_b=B, per the agent's own fixed
        framing). Re-keys it by OPTION NUMBER only, in canonical->absorbed direction (inverting
        if qid_b turned out to be the lower/canonical QID), so the merged record's own
        option_map field never has to remember which side was literally 'A' or 'B'."""
        a_to_b_num = {k[1:]: v[1:] for k, v in option_map.items()}
        if canonical == qid_a:
            return a_to_b_num
        return {v: k for k, v in a_to_b_num.items()}

    def _merge_records(self, canonical, absorbed, canonical_to_absorbed_map, prompt_version, status):
        """Judgment call (see report): canonical = the lexicographically-lower Q-ID (fixed
        6-digit zero-padded, so lexicographic = numeric = earlier-minted = already carries full
        B1-B8 history) -- content fields are NEVER re-derived or copied across, only metadata:
          - canonical.paper_codes gains the absorbed record's own paper_codes entries (dedup,
            sorted) -- e.g. ["E1:1"] + ["E2:63"] -> ["E1:1","E2:63"].
          - canonical.option_map[absorbed_qid] = {canonical_opt_num: absorbed_opt_num, ...} --
            lets anything downstream translate the absorbed code's own option lettering back to
            canonical's, without needing the absorbed record's content at all.
          - canonical.merged_from gains absorbed_qid (list, so a later 3rd/4th code's merge
            accumulates rather than overwrites).
          - absorbed record is NEVER deleted or edited beyond gaining one new field,
            merged_into = canonical_qid, so nothing downstream double-counts it (spot-checkable:
            any consumer of papers/records/ that skips merged_into-tagged records sees each real
            question exactly once) while the absorbed record's own full field history (and
            field_sources audit trail) stays intact and inspectable -- reversible in the sense
            that undoing a merge means only deleting these added fields, not reconstructing lost
            content."""
        rec_c = lib_records.read_record(canonical)
        rec_a = lib_records.read_record(absorbed)
        merged_codes = sorted(set(rec_c.get("paper_codes") or []) | set(rec_a.get("paper_codes") or []))
        option_map_field = dict(rec_c.get("option_map") or {})
        option_map_field[absorbed] = canonical_to_absorbed_map
        merged_from = list(rec_c.get("merged_from") or [])
        if absorbed not in merged_from:
            merged_from.append(absorbed)
        lib_records.set_fields(canonical, {
            "paper_codes": merged_codes, "option_map": option_map_field, "merged_from": merged_from,
        }, step=self.step, prompt_version=prompt_version, status=status)
        lib_records.set_fields(absorbed, {"merged_into": canonical}, step=self.step,
                                 prompt_version=prompt_version, status=status)

    def _resolve_exact_same(self, item_id, qid_a, qid_b, data, run_label, prompt_version, flags_cat, note=""):
        option_map = data["option_map"]
        rec_a, rec_b = lib_records.read_record(qid_a), lib_records.read_record(qid_b)
        started = ended = rc.now_iso()

        # one-to-one (spec 11/C1 Checks): neither side may already be merged into a DIFFERENT
        # partner than this one (defensive -- the shortlist is already a 1:1 assignment per code
        # pair, so this should only ever trip across repeated/filtered re-runs).
        a_other = rec_a.get("merged_into") not in (None, qid_b)
        b_other = rec_b.get("merged_into") not in (None, qid_a)
        if a_other or b_other:
            msg = (f"one-to-one violated: "
                   f"{qid_a} merged_into={rec_a.get('merged_into')!r}, "
                   f"{qid_b} merged_into={rec_b.get('merged_into')!r} (expected each other or None)")
            self._resolve_blocked(item_id, msg, run_label, prompt_version)
            return

        # count check (spec 11/C1 Checks): already enforced by scripts/checks/C1.py's bijection
        # validation (exactly 4 A-keys, option_map values a permutation of all 4 B-options) --
        # self._validate() already ran that before this method is ever called.

        consistent, detail = self._check_key_consistency(rec_a, rec_b, option_map)
        if not consistent:
            rc.raise_flag("item", item_id, self.step, "C1_KEY_INCONSISTENT",
                           flags_cat.get("C1_KEY_INCONSISTENT", "high"),
                           detail + " -- re-check B5 for this sitting", provisional_value=data,
                           evidence=[_relpath(rc.pp("papers", "records", f"{qid_a}.json")),
                                     _relpath(rc.pp("papers", "records", f"{qid_b}.json"))],
                           prompt_version=prompt_version)
            rc.write_item_status(self.step, item_id, "flagged", prompt_version,
                                   extra={"run": run_label, "check_message": detail})
            rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version, started,
                                ended, "fail", detail, None, "flagged")
            return

        canonical, absorbed = sorted((qid_a, qid_b))
        c2a_map = self._translate_option_map(qid_a, qid_b, option_map, canonical)
        self._merge_records(canonical, absorbed, c2a_map, prompt_version, "pass")
        msg = f"exact_same; merged {absorbed} into {canonical}" + (f" ({note})" if note else "")
        rc.write_item_status(self.step, item_id, "pass", prompt_version,
                               extra={"run": run_label, "check_message": msg})
        rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version, started, ended,
                            "pass", msg, None, "pass")

    # ---- not_exact chain: reread -> compare2 -> adjudicate ---------------------------------

    def _start_reread(self, item_id, qid_a, qid_b, records, prompt_version):
        """Spec 11/C1 On failure: 'not_exact -> re-run B3 and B4 on both copies with note
        "possible misread"'. Dispatches a fresh b3-question-reader call per side, reusing the
        real retry mechanism every B3/B4/... agent file's universal rule 9 already honors
        (`previous_attempt_failed`) rather than inventing a new field. B4 is re-dispatched too
        ONLY when the record shows it originally used its own AGENT branch (no `b4_script_options`
        on the record -- B4Plugin's SCRIPT branch always sets that field; see B4Plugin docstring);
        when B4's SCRIPT branch ran, re-running it is a deterministic no-op (same PDF text layer,
        same parse), so it is skipped rather than wastefully re-dispatched -- a documented,
        pragmatic reading of 're-run B4' for this build's real data (B1-B6 confirmed ~100%
        text-layer coverage)."""
        new_lines = []
        parts = []
        for side, qid in (("a", qid_a), ("b", qid_b)):
            record = records.get(qid) or lib_records.read_record(qid)
            paper_id, qno = _b_paper_id_for(record), _b_qno_for(record)
            crop_path = rc.pp("papers", "questions", paper_id, f"{qno}.png")
            other = qid_b if side == "a" else qid_a
            note = (f"possible misread: step C1 found this question's booklet-code counterpart "
                    f"({other}) reads differently on a first comparison; re-transcribe carefully "
                    f"from the image.")
            b3_label = f"reread_{side}_b3"
            _write_json(_work_input_path(self.step, item_id, b3_label), {
                "question_image": _relpath(crop_path), "paper_id": paper_id, "qno": qno,
                "previous_attempt_failed": note,
            })
            new_lines.append(ListLine(item_id, "b3-question-reader",
                                        _relpath(_work_input_path(self.step, item_id, b3_label)),
                                        _relpath(_out_path(self.step, item_id, b3_label)), b3_label))
            parts.append(b3_label)
            if "b4_script_options" not in record:
                b4_label = f"reread_{side}_b4"
                _write_json(_work_input_path(self.step, item_id, b4_label), {
                    "question_image": _relpath(crop_path), "paper_id": paper_id, "qno": qno,
                    "previous_attempt_failed": note,
                })
                new_lines.append(ListLine(item_id, "b4-second-reader",
                                            _relpath(_work_input_path(self.step, item_id, b4_label)),
                                            _relpath(_out_path(self.step, item_id, b4_label)), b4_label))
                parts.append(b4_label)
        rc.write_pending(self.step, item_id, {"stage": "reread", "parts": parts})
        return new_lines

    def _collect_reread(self, item_id, parts):
        """{'a': <b3 reread output>, 'b': <b3 reread output>} -- only the B3 reread feeds the
        second comparison (C1's agent input contract is stem/statements/lists/options, all B3
        fields); a B4 reread (when dispatched) is still real integrity evidence on record but
        does not itself redefine what C1 compares, same as B4 never redefining stem_en on the
        record either."""
        out = {}
        for side in ("a", "b"):
            label = f"reread_{side}_b3"
            if label in parts:
                out[side] = _read_json(_out_path(self.step, item_id, label))
        return out

    def _start_adjudicator(self, item_id, qid_a, qid_b, records, data, prompt_version):
        """Still not_exact after reread: x-adjudicator, in its own generic Input contract (step,
        task, allowed_values, evidence, reading_a/reading_b, failed_check) -- same precedent as
        A6's own _write_adjudication_work_file for a non-two-run adjudication. x-adjudicator.md
        itself explicitly names this step ('For readings (B4, C1): choose span by span which
        reading matches the image'), so 'reading_a'/'reading_b' (not run_a/run_b) is the right
        field pair per its own Input block."""
        rec_a = records.get(qid_a) or lib_records.read_record(qid_a)
        rec_b = records.get(qid_b) or lib_records.read_record(qid_b)
        crop_a = rc.pp("papers", "questions", _b_paper_id_for(rec_a), f"{_b_qno_for(rec_a)}.png")
        crop_b = rc.pp("papers", "questions", _b_paper_id_for(rec_b), f"{_b_qno_for(rec_b)}.png")
        payload = {
            "step": "C1",
            "task": "Decide whether these two questions (one per booklet code of the same "
                     "sitting, already reread once) are really the same question with a "
                     "transcription misread on one side, or are genuinely two different "
                     "questions.",
            "allowed_values": {
                "choice": ["A", "B", "combined", "unsure"],
                "A": "reading_a matches the image; reading_b's differing span(s) were the misread",
                "B": "reading_b matches the image; reading_a's differing span(s) were the misread",
                "combined": "some spans from each side are correct; combined, they are the same question",
                "unsure": "cannot tell from the evidence -- treat as genuinely two different questions",
            },
            "evidence": {"images": [_relpath(crop_a), _relpath(crop_b)]},
            "reading_a": self._agent_view(qid_a, records),
            "reading_b": self._agent_view(qid_b, records),
            "run_a": None, "run_b": None,
            "failed_check": f"C1 not_exact twice (initial + after reread); differences: {data.get('differences')}",
        }
        _write_json(_work_input_path(self.step, item_id, "adjudicated"), payload)
        return [ListLine(item_id, "x-adjudicator",
                           _relpath(_work_input_path(self.step, item_id, "adjudicated")),
                           _relpath(_out_path(self.step, item_id, "adjudicated")), "adjudicated")]

    def _resolve_after_adjudication(self, item_id, qid_a, qid_b, data, prompt_version, flags_cat):
        choice = data.get("choice")
        started = ended = rc.now_iso()
        if choice in ("A", "B", "combined"):
            # Judgment call (see report): the adjudicator's generic contract returns a choice +
            # corrected span/value, not a full option-by-option bijection the way
            # c1-booklet-matcher's own exact_same verdict does. Absent a real cross-numbering
            # signal, assume the options were NOT reordered between codes for a question the
            # adjudicator just confirmed is the same (if they had been, the agent's OWN
            # exact_same verdict -- with a real option_map -- would have resolved this at stage 1
            # or stage 2, never reaching the adjudicator at all): identity-by-option-number.
            option_map = {f"A{n}": f"B{n}" for n in "1234"}
            rec_a, rec_b = lib_records.read_record(qid_a), lib_records.read_record(qid_b)
            consistent, detail = self._check_key_consistency(rec_a, rec_b, option_map)
            rc.raise_flag("item", item_id, self.step, "C1_READING_FIXED",
                           flags_cat.get("C1_READING_FIXED", "high"),
                           f"adjudicator choice={choice}: {data.get('why', '')}", provisional_value=data,
                           evidence=[_relpath(_out_path(self.step, item_id, "adjudicated"))],
                           prompt_version=prompt_version)
            if consistent:
                canonical, absorbed = sorted((qid_a, qid_b))
                c2a_map = self._translate_option_map(qid_a, qid_b, option_map, canonical)
                self._merge_records(canonical, absorbed, c2a_map, prompt_version, "flagged")
                msg = f"adjudicator choice={choice}; merged {absorbed} into {canonical} (reading fixed)"
                check_val = "pass"
            else:
                rc.raise_flag("item", item_id, self.step, "C1_KEY_INCONSISTENT",
                               flags_cat.get("C1_KEY_INCONSISTENT", "high"), detail,
                               provisional_value=data, prompt_version=prompt_version)
                msg = f"adjudicator choice={choice} but key-inconsistent, not merged: {detail}"
                check_val = "fail"
            rc.write_item_status(self.step, item_id, "flagged", prompt_version,
                                   extra={"run": "adjudicated", "check_message": msg})
            rc.append_run_log(item_id, self.step, "adjudicated", "x-adjudicator", prompt_version,
                                started, ended, check_val, msg, None, "flagged")
        else:  # "unsure" (or any other value -- x-adjudicator's own allowed_values enforced by
               # x-adjudicator itself, not re-validated here; an out-of-contract value is treated
               # the same conservative way as unsure, per Rule 5/"use 'unsure' if not sure")
            rc.raise_flag("item", item_id, self.step, "C1_UNMATCHED",
                           flags_cat.get("C1_UNMATCHED", "normal"),
                           f"adjudicator unsure after reread -- keeping both questions separate: {data.get('why', '')}",
                           provisional_value=data,
                           evidence=[_relpath(_out_path(self.step, item_id, "adjudicated"))],
                           prompt_version=prompt_version)
            msg = "unmatched (adjudicator unsure after reread); kept separate"
            rc.write_item_status(self.step, item_id, "flagged", prompt_version,
                                   extra={"run": "adjudicated", "check_message": msg})
            rc.append_run_log(item_id, self.step, "adjudicated", "x-adjudicator", prompt_version,
                                started, ended, "fail", msg, None, "flagged")

    def check(self, filters):
        pairs, records, skipped = self._pairs_in_scope(filters)
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        for sitting_key, codes_map in skipped.items():
            self._mark_sitting_skipped(sitting_key, codes_map, prompt_version)

        new_lines = []
        for item_id, (qid_a, qid_b, _sim) in pairs.items():
            if not rc.item_passes_filters(item_id, filters):
                continue
            existing = rc.read_item_status(self.step, item_id)
            if existing and existing.get("status") != "stale" and existing.get("prompt_version") == prompt_version:
                continue

            pending = rc.read_pending(self.step, item_id) or {}
            stage = pending.get("stage", "compare1")

            if stage == "compare1":
                out_path = _out_path(self.step, item_id, "runA")
                if not os.path.exists(out_path):
                    continue  # still waiting on the agent
                data = _read_json(out_path)
                ok, msg = self._validate(self.step, data)
                if not ok:
                    self._resolve_blocked(item_id, msg, "runA", prompt_version)
                    continue
                if data["verdict"] == "exact_same":
                    self._resolve_exact_same(item_id, qid_a, qid_b, data, "runA", prompt_version, flags_cat)
                else:
                    new_lines.extend(self._start_reread(item_id, qid_a, qid_b, records, prompt_version))
                continue

            if stage == "reread":
                parts = pending.get("parts", [])
                if any(not os.path.exists(_out_path(self.step, item_id, p)) for p in parts):
                    continue  # still waiting on one or more reread agent calls
                reread = self._collect_reread(item_id, parts)
                new_lines.extend(self._dispatch_compare(item_id, qid_a, qid_b, records, "retry1",
                                                           reread, prompt_version))
                rc.write_pending(self.step, item_id, {"stage": "compare2"})
                continue

            if stage == "compare2":
                out_path = _out_path(self.step, item_id, "retry1")
                if not os.path.exists(out_path):
                    continue
                data = _read_json(out_path)
                ok, msg = self._validate(self.step, data)
                if not ok:
                    self._resolve_blocked(item_id, msg, "retry1", prompt_version)
                    continue
                if data["verdict"] == "exact_same":
                    self._resolve_exact_same(item_id, qid_a, qid_b, data, "retry1", prompt_version,
                                               flags_cat, note="resolved after reread (possible misread)")
                else:
                    new_lines.extend(self._start_adjudicator(item_id, qid_a, qid_b, records, data, prompt_version))
                    rc.write_pending(self.step, item_id, {"stage": "adjudicate"})
                continue

            if stage == "adjudicate":
                out_path = _out_path(self.step, item_id, "adjudicated")
                if not os.path.exists(out_path):
                    continue
                data = _read_json(out_path)
                self._resolve_after_adjudication(item_id, qid_a, qid_b, data, prompt_version, flags_cat)
                continue

        return new_lines


# ===========================================================================
# D1-D4 - Stage D first slice: pick chapter -> pick subtopic -> fetch passages -> quote evidence
# (spec Section 12/D1-D4; .claude/agents/d1-chapter-picker.md, d2-subtopic-picker.md,
# d4-evidence-quoter.md; D3 has no agent file of its own, SCRIPT only, scripts/fetch_passages.py).
#
# Item = one question (D1, D2, D3) or one question x one answer (D4) -- this build only ever has
# ONE answer to support per question, since D7 (latest-NCERT answer check, D5-D11 out of this
# pass's scope) is not built: spec 12's "D4 also runs for latest_answer after D7" never triggers
# here, and `_d_answer_to_support` below only implements the "corrected_answer when B8 made one,
# else official_answer" half of the rule (documented, not silently dropped).
#
# Readiness gate: same judgment call as B6/B7/B8/C1's own "needs" gates (see C1Plugin's module
# docstring) -- any B5-joined record (_b_qid_records' own readiness signal) not already absorbed
# into another question by a C1 merge (record.get("merged_into")) is D-eligible; `needs: C1, A9`
# per-item readiness (does a chapter list even exist for this subject yet?) is checked directly in
# D1Plugin, since this build's real data only has NCERT chapters indexed for Biology (see
# D1Plugin._chapters_for_subject and the D1_NO_CHAPTERS outcome).
# ===========================================================================

_SUBJECT_PREFIX = {"Physics": "PHY", "Chemistry": "CHE", "Biology": "BIO"}


def _d_candidates():
    """{qid: record} ready for Stage D: B5-joined (same signal as B6/B7/B8/C1) and not absorbed
    into another question by a C1 merge."""
    return {qid: r for qid, r in _b_qid_records().items() if not r.get("merged_into")}


def _d_answer_to_support(record):
    """spec 12 preamble: 'The answer used in Stage D is corrected_answer when B8 made one, else
    official_answer.' Only that first half applies in this build (D7/latest_answer is out of this
    pass's scope, see module docstring)."""
    number = record.get("corrected_answer")
    if number in (None, ""):
        number = record.get("official_answer")
    options = record.get("corrected_options") or record.get("options_en") or {}
    text = options.get(str(number)) if number is not None else None
    return {"number": number, "text": text}


def _d_question_view(record):
    return {
        "stem": record.get("stem_en") or "",
        "statements": record.get("statements") or [],
        "list_i": record.get("list_i") or [],
        "list_ii": record.get("list_ii") or [],
        "options": record.get("options_en") or {},
    }


class D1Plugin:
    step = "D1"
    agent = "d1-chapter-picker"

    @staticmethod
    def _chapters_for_subject(subject):
        """Every chapter indexed for this question's subject, across every class file
        (ncert/chapters/<SUBJ><CLASS>.json, e.g. BIO11.json + BIO12.json) -- NOT narrowed by
        branch: the chapters file carries no branch field at all, and a question record's own
        `branch` (B7's output) is frequently 'unsure' itself (confirmed real: Q-000015), so there
        is no real signal to narrow by. Documented judgment call, see report."""
        prefix = _SUBJECT_PREFIX.get(subject)
        out = {}
        if not prefix:
            return out
        chapters_dir = rc.pp("ncert", "chapters")
        if os.path.isdir(chapters_dir):
            for fn in sorted(os.listdir(chapters_dir)):
                if fn.endswith(".json") and fn[: -len(".json")].startswith(prefix):
                    data = _read_json(os.path.join(chapters_dir, fn))
                    for ch in (data if isinstance(data, list) else [data]):
                        cid = ch.get("chapter_id")
                        if cid:
                            out[cid] = ch
        return out

    @staticmethod
    def _chapter_view(ch):
        return {"id": ch.get("chapter_id"), "title": ch.get("title"), "headings": ch.get("headings", [])}

    def list_items(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for qid, record in _d_candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            chapters = self._chapters_for_subject(record.get("subject"))
            if not chapters:
                continue  # zero-candidate outcome resolved entirely in check(), never dispatched
            if os.path.exists(_work_input_path(self.step, item_id, "adjudicated")):
                continue  # already past the 2-run stage, awaiting (or past) adjudication
            for run_label in ("runA", "runB"):
                if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, run_label)):
                    continue
                input_data = {
                    "question": _d_question_view(record),
                    "correct_answer": _d_answer_to_support(record),
                    "chapters": [self._chapter_view(c) for c in chapters.values()],
                }
                _write_json(_work_input_path(self.step, item_id, run_label), input_data)
                lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, run_label)),
                                        _relpath(_out_path(self.step, item_id, run_label)), run_label))
        return lines

    def list_reason(self):
        return ("D1 needs B5-joined question records not already C1-merged away, plus at least "
                "one NCERT chapter indexed (ncert/chapters/<SUBJ><CLASS>.json) for that question's "
                "subject. None ready yet, every ready question's subject has zero chapters indexed "
                "(resolved as D1_NO_CHAPTERS in --check, never dispatched), or everything else "
                "already has output pending --check.")

    def _run_check(self, item_id, chapters, data):
        if isinstance(data, dict) and "error" in data:
            return False, f"agent reported error: {data['error']}"
        ok, msg = rc.validate_schema(self.step, data)
        if not ok:
            return False, msg
        context = {"item_id": item_id, "step": self.step,
                    "input_data": {"all_chapter_ids": list(chapters.keys())}}
        return rc.run_step_check(self.step, data, context)

    @staticmethod
    def _assemble(qid, chapter_ids, why, confidence, prompt_version, status):
        lib_records.set_fields(qid, {
            "d1_chapter_ids": chapter_ids, "d1_why": why, "d1_confidence": confidence,
        }, step="D1", prompt_version=prompt_version, status=status)

    def _start_adjudicator(self, item_id, record, chapters, data_a, data_b, prompt_version):
        payload = {
            "step": "D1",
            "task": "Run A and run B each independently picked which NCERT chapter(s) this "
                     "question tests. Decide the correct chapter_ids.",
            "allowed_values": {
                "choice": ["A", "B", "combined", "unsure"],
                "A": "run A's chapter_ids is correct", "B": "run B's chapter_ids is correct",
                "combined": "value.chapter_ids gives the correct merged list (rare -- at most 2 "
                             "chapters total)",
                "unsure": "cannot decide -- the script falls back to run A's choice if valid, "
                           "else a keyword-ranked guess",
            },
            "evidence": {"question": _d_question_view(record), "correct_answer": _d_answer_to_support(record),
                          "chapters": [self._chapter_view(c) for c in chapters.values()]},
            "run_a": data_a.get("chapter_ids"), "run_b": data_b.get("chapter_ids"),
            "failed_check": "run A and run B disagree on chapter_ids (or one/both said unsure)",
        }
        _write_json(_work_input_path(self.step, item_id, "adjudicated"), payload)
        rc.write_pending(self.step, item_id, {"stage": "adjudicating"})
        return [ListLine(item_id, "x-adjudicator",
                           _relpath(_work_input_path(self.step, item_id, "adjudicated")),
                           _relpath(_out_path(self.step, item_id, "adjudicated")), "adjudicated")]

    @staticmethod
    def _keyword_guess(record, chapters):
        query = " ".join([record.get("stem_en") or "",
                           " ".join((record.get("options_en") or {}).values())])
        items = [(cid, " ".join([ch.get("title") or ""] + [h.get("text", "") for h in ch.get("headings", [])]))
                 for cid, ch in chapters.items()]
        ranked = search_index.rank(query, items, limit=1)
        return [ranked[0][0]] if ranked else ["unsure"]

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        new_lines = []
        for qid, record in _d_candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            existing = rc.read_item_status(self.step, item_id)
            if existing and existing.get("status") != "stale" and existing.get("prompt_version") == prompt_version:
                continue

            chapters = self._chapters_for_subject(record.get("subject"))
            if not chapters:
                rc.raise_flag("item", item_id, self.step, "D1_NO_CHAPTERS",
                               flags_cat.get("D1_NO_CHAPTERS", "blocker"),
                               f"no NCERT chapters indexed yet for subject {record.get('subject')!r} "
                               f"(Stage A hasn't covered it) -- D1 cannot run for this question",
                               prompt_version=prompt_version)
                rc.write_item_status(self.step, item_id, "blocked", prompt_version,
                                       extra={"check_message": "no candidate chapters for this subject"})
                rc.append_run_log(item_id, self.step, "runA", None, prompt_version, rc.now_iso(),
                                    rc.now_iso(), "fail", "no candidate chapters for this subject", None, "blocked")
                continue

            if os.path.exists(_work_input_path(self.step, item_id, "adjudicated")):
                adj_path = _out_path(self.step, item_id, "adjudicated")
                if not os.path.exists(adj_path):
                    continue
                adj_data = _read_json(adj_path)
                data_a = _read_json(_out_path(self.step, item_id, "runA"))
                data_b = _read_json(_out_path(self.step, item_id, "runB"))
                choice = adj_data.get("choice")
                started = ended = rc.now_iso()
                flag_code, severity = "D1_ADJUDICATED", flags_cat.get("D1_ADJUDICATED", "normal")
                if choice == "A":
                    chapter_ids = data_a.get("chapter_ids")
                    why, confidence = data_a.get("why", ""), data_a.get("confidence", "medium")
                    note = "adjudicator chose run A"
                elif choice == "B":
                    chapter_ids = data_b.get("chapter_ids")
                    why, confidence = data_b.get("why", ""), data_b.get("confidence", "medium")
                    note = "adjudicator chose run B"
                elif choice == "combined" and isinstance((adj_data.get("value") or {}).get("chapter_ids"), list) \
                        and (adj_data.get("value") or {}).get("chapter_ids"):
                    chapter_ids = adj_data["value"]["chapter_ids"]
                    why, confidence = adj_data.get("why", ""), adj_data.get("confidence", "medium")
                    note = "adjudicator combined both runs"
                else:  # unsure (or out-of-contract) -> spec 12/D1's own documented safe default
                    flag_code, severity = "D1_GUESS", flags_cat.get("D1_GUESS", "high")
                    a_ids = data_a.get("chapter_ids")
                    if isinstance(a_ids, list) and a_ids and a_ids != ["unsure"] \
                            and all(i in chapters for i in a_ids):
                        chapter_ids = a_ids
                        why, confidence = data_a.get("why", ""), "low"
                        note = f"adjudicator {choice or 'unsure'} -- used run A's choice"
                    else:
                        chapter_ids = self._keyword_guess(record, chapters)
                        why, confidence = "search_index.rank keyword fallback (no valid run A choice)", "low"
                        note = f"adjudicator {choice or 'unsure'} -- run A invalid too; keyword-rank guess"
                self._assemble(qid, chapter_ids, why, confidence, prompt_version, "flagged")
                rc.raise_flag("item", item_id, self.step, flag_code, severity, note,
                               provisional_value={"chapter_ids": chapter_ids, "choice": choice},
                               prompt_version=prompt_version)
                rc.write_item_status(self.step, item_id, "flagged", prompt_version, extra={"check_message": note})
                rc.append_run_log(item_id, self.step, "adjudicated", "x-adjudicator", prompt_version,
                                    started, ended, "pass", note, None, "flagged")
                continue

            run_a_path, run_b_path = _out_path(self.step, item_id, "runA"), _out_path(self.step, item_id, "runB")
            if not (os.path.exists(run_a_path) and os.path.exists(run_b_path)):
                continue
            data_a, data_b = _read_json(run_a_path), _read_json(run_b_path)
            ok_a, msg_a = self._run_check(item_id, chapters, data_a)
            ok_b, msg_b = self._run_check(item_id, chapters, data_b)
            started = ended = rc.now_iso()

            if not (ok_a and ok_b):
                if ok_a and not ok_b:
                    chapter_ids = data_a.get("chapter_ids")
                    why, confidence = data_a.get("why", ""), data_a.get("confidence", "medium")
                    note = f"run B invalid ({msg_b}); used run A only"
                elif ok_b and not ok_a:
                    chapter_ids = data_b.get("chapter_ids")
                    why, confidence = data_b.get("why", ""), data_b.get("confidence", "medium")
                    note = f"run A invalid ({msg_a}); used run B only"
                else:
                    rc.write_item_status(self.step, item_id, "blocked", prompt_version,
                                           extra={"check_message": f"runA: {msg_a}; runB: {msg_b}"})
                    rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version,
                                        started, ended, "fail", f"runA: {msg_a}; runB: {msg_b}", None, "blocked")
                    continue
                self._assemble(qid, chapter_ids, why, confidence, prompt_version, "flagged")
                rc.raise_flag("item", item_id, self.step, "D1_ADJUDICATED", flags_cat.get("D1_ADJUDICATED", "normal"),
                               note, provisional_value={"chapter_ids": chapter_ids}, prompt_version=prompt_version)
                rc.write_item_status(self.step, item_id, "flagged", prompt_version, extra={"check_message": note})
                rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version, started, ended,
                                    "pass", note, None, "flagged")
                continue

            set_a, set_b = set(data_a.get("chapter_ids") or []), set(data_b.get("chapter_ids") or [])
            if set_a == set_b and "unsure" not in set_a:
                chapter_ids = data_a.get("chapter_ids")
                self._assemble(qid, chapter_ids, data_a.get("why", ""), data_a.get("confidence", "medium"),
                                prompt_version, "pass")
                rc.write_item_status(self.step, item_id, "pass", prompt_version,
                                       extra={"check_message": "runs agree"})
                rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version, started, ended,
                                    "pass", "runs agree", None, "pass")
            else:
                rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version, started, ended,
                                    "pass", f"disagreement (A={sorted(set_a)}, B={sorted(set_b)}) -> adjudicator",
                                    None, "pending")
                new_lines.extend(self._start_adjudicator(item_id, record, chapters, data_a, data_b, prompt_version))
        return new_lines


class D2Plugin:
    step = "D2"
    agent = "d2-subtopic-picker"

    @staticmethod
    def _subtopics_for_chapters(chapter_ids):
        out = {}
        for cid in chapter_ids or []:
            path = rc.pp("ncert", "subtopics", f"{cid}.json")
            if os.path.exists(path):
                data = _read_json(path)
                for st in data.get("subtopics", []):
                    sid = st.get("subtopic_id")
                    if sid:
                        out[sid] = st
        return out

    @staticmethod
    def _subtopic_view(st):
        return {"id": st.get("subtopic_id"), "name": st.get("name"),
                 "description": st.get("description") or st.get("name")}

    @staticmethod
    def _ready_candidates():
        out = {}
        for qid, record in _d_candidates().items():
            chapter_ids = record.get("d1_chapter_ids")
            if not chapter_ids or chapter_ids == ["unsure"]:
                continue
            out[qid] = record
        return out

    def list_items(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for qid, record in self._ready_candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            subtopics = self._subtopics_for_chapters(record.get("d1_chapter_ids"))
            if not subtopics:
                continue  # resolved as a structural D2_NO_SUBTOPICS outcome in check()
            if os.path.exists(_work_input_path(self.step, item_id, "adjudicated")):
                continue
            for run_label in ("runA", "runB"):
                if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, run_label)):
                    continue
                input_data = {
                    "question": _d_question_view(record),
                    "correct_answer": _d_answer_to_support(record),
                    "subtopics": [self._subtopic_view(s) for s in subtopics.values()],
                }
                _write_json(_work_input_path(self.step, item_id, run_label), input_data)
                lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, run_label)),
                                        _relpath(_out_path(self.step, item_id, run_label)), run_label))
        return lines

    def list_reason(self):
        return ("D2 needs a resolved D1 chapter (d1_chapter_ids on the record, not unsure) with "
                "at least one drafted subtopic list for it (ncert/subtopics/<CHAPTER>.json, from "
                "A4). None ready yet, or everything ready already has output pending --check.")

    def _run_check(self, item_id, subtopics, data):
        if isinstance(data, dict) and "error" in data:
            return False, f"agent reported error: {data['error']}"
        ok, msg = rc.validate_schema(self.step, data)
        if not ok:
            return False, msg
        context = {"item_id": item_id, "step": self.step,
                    "input_data": {"all_subtopic_ids": list(subtopics.keys())}}
        return rc.run_step_check(self.step, data, context)

    @staticmethod
    def _assemble(qid, subtopic_ids, why, confidence, prompt_version, status, note_from_runner=None):
        fields = {"d2_subtopic_ids": subtopic_ids, "d2_why": why, "d2_confidence": confidence}
        if note_from_runner is not None:
            fields["d2_note_from_runner"] = note_from_runner
        lib_records.set_fields(qid, fields, step="D2", prompt_version=prompt_version, status=status)

    def _start_adjudicator(self, item_id, record, subtopics, data_a, data_b, prompt_version):
        payload = {
            "step": "D2",
            "task": "Run A and run B each independently picked which subtopic(s) this question "
                     "tests, within its D1 chapter(s). Decide the correct subtopic_ids.",
            "allowed_values": {
                "choice": ["A", "B", "combined", "unsure"],
                "A": "run A's subtopic_ids is correct", "B": "run B's subtopic_ids is correct",
                "combined": "value.subtopic_ids gives the correct merged list",
                "unsure": "cannot decide -- the script falls back to run A's choice if valid, "
                           "else a keyword-ranked guess",
            },
            "evidence": {"question": _d_question_view(record), "correct_answer": _d_answer_to_support(record),
                          "subtopics": [self._subtopic_view(s) for s in subtopics.values()]},
            "run_a": data_a.get("subtopic_ids"), "run_b": data_b.get("subtopic_ids"),
            "failed_check": "run A and run B disagree on subtopic_ids (or one/both said unsure)",
        }
        _write_json(_work_input_path(self.step, item_id, "adjudicated"), payload)
        rc.write_pending(self.step, item_id, {"stage": "adjudicating"})
        return [ListLine(item_id, "x-adjudicator",
                           _relpath(_work_input_path(self.step, item_id, "adjudicated")),
                           _relpath(_out_path(self.step, item_id, "adjudicated")), "adjudicated")]

    @staticmethod
    def _keyword_guess(record, subtopics):
        query = " ".join([record.get("stem_en") or "",
                           " ".join((record.get("options_en") or {}).values())])
        items = [(sid, f"{s.get('name') or ''} {s.get('description') or ''}") for sid, s in subtopics.items()]
        ranked = search_index.rank(query, items, limit=1)
        return [ranked[0][0]] if ranked else ["unsure"]

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        new_lines = []
        for qid, record in self._ready_candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            existing = rc.read_item_status(self.step, item_id)
            if existing and existing.get("status") != "stale" and existing.get("prompt_version") == prompt_version:
                continue

            subtopics = self._subtopics_for_chapters(record.get("d1_chapter_ids"))
            if not subtopics:
                rc.raise_flag("item", item_id, self.step, "D2_NO_SUBTOPICS",
                               flags_cat.get("D2_NO_SUBTOPICS", "blocker"),
                               f"D1 chapter(s) {record.get('d1_chapter_ids')} have no drafted "
                               f"subtopic list yet (A4 hasn't run for them) -- D2 cannot run",
                               prompt_version=prompt_version)
                rc.write_item_status(self.step, item_id, "blocked", prompt_version,
                                       extra={"check_message": "no subtopics drafted for this chapter"})
                rc.append_run_log(item_id, self.step, "runA", None, prompt_version, rc.now_iso(),
                                    rc.now_iso(), "fail", "no subtopics drafted for this chapter", None, "blocked")
                continue

            if os.path.exists(_work_input_path(self.step, item_id, "adjudicated")):
                adj_path = _out_path(self.step, item_id, "adjudicated")
                if not os.path.exists(adj_path):
                    continue
                adj_data = _read_json(adj_path)
                data_a = _read_json(_out_path(self.step, item_id, "runA"))
                data_b = _read_json(_out_path(self.step, item_id, "runB"))
                choice = adj_data.get("choice")
                started = ended = rc.now_iso()
                flag_code, severity = "D2_ADJUDICATED", flags_cat.get("D2_ADJUDICATED", "normal")
                if choice == "A":
                    subtopic_ids = data_a.get("subtopic_ids")
                    why, confidence = data_a.get("why", ""), data_a.get("confidence", "medium")
                    note = "adjudicator chose run A"
                elif choice == "B":
                    subtopic_ids = data_b.get("subtopic_ids")
                    why, confidence = data_b.get("why", ""), data_b.get("confidence", "medium")
                    note = "adjudicator chose run B"
                elif choice == "combined" and isinstance((adj_data.get("value") or {}).get("subtopic_ids"), list) \
                        and (adj_data.get("value") or {}).get("subtopic_ids"):
                    subtopic_ids = adj_data["value"]["subtopic_ids"]
                    why, confidence = adj_data.get("why", ""), adj_data.get("confidence", "medium")
                    note = "adjudicator combined both runs"
                else:
                    flag_code, severity = "D2_GUESS", flags_cat.get("D2_GUESS", "high")
                    a_ids = data_a.get("subtopic_ids")
                    if isinstance(a_ids, list) and a_ids and a_ids != ["unsure"] and all(i in subtopics for i in a_ids):
                        subtopic_ids = a_ids
                        why, confidence = data_a.get("why", ""), "low"
                        note = f"adjudicator {choice or 'unsure'} -- used run A's choice"
                    else:
                        subtopic_ids = self._keyword_guess(record, subtopics)
                        why, confidence = "search_index.rank keyword fallback (no valid run A choice)", "low"
                        note = f"adjudicator {choice or 'unsure'} -- run A invalid too; keyword-rank guess"
                self._assemble(qid, subtopic_ids, why, confidence, prompt_version, "flagged")
                rc.raise_flag("item", item_id, self.step, flag_code, severity, note,
                               provisional_value={"subtopic_ids": subtopic_ids, "choice": choice},
                               prompt_version=prompt_version)
                rc.write_item_status(self.step, item_id, "flagged", prompt_version, extra={"check_message": note})
                rc.append_run_log(item_id, self.step, "adjudicated", "x-adjudicator", prompt_version,
                                    started, ended, "pass", note, None, "flagged")
                continue

            run_a_path, run_b_path = _out_path(self.step, item_id, "runA"), _out_path(self.step, item_id, "runB")
            if not (os.path.exists(run_a_path) and os.path.exists(run_b_path)):
                continue
            data_a, data_b = _read_json(run_a_path), _read_json(run_b_path)
            ok_a, msg_a = self._run_check(item_id, subtopics, data_a)
            ok_b, msg_b = self._run_check(item_id, subtopics, data_b)
            started = ended = rc.now_iso()

            if not (ok_a and ok_b):
                if ok_a and not ok_b:
                    subtopic_ids = data_a.get("subtopic_ids")
                    why, confidence = data_a.get("why", ""), data_a.get("confidence", "medium")
                    note = f"run B invalid ({msg_b}); used run A only"
                elif ok_b and not ok_a:
                    subtopic_ids = data_b.get("subtopic_ids")
                    why, confidence = data_b.get("why", ""), data_b.get("confidence", "medium")
                    note = f"run A invalid ({msg_a}); used run B only"
                else:
                    rc.write_item_status(self.step, item_id, "blocked", prompt_version,
                                           extra={"check_message": f"runA: {msg_a}; runB: {msg_b}"})
                    rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version,
                                        started, ended, "fail", f"runA: {msg_a}; runB: {msg_b}", None, "blocked")
                    continue
                self._assemble(qid, subtopic_ids, why, confidence, prompt_version, "flagged")
                rc.raise_flag("item", item_id, self.step, "D2_ADJUDICATED", flags_cat.get("D2_ADJUDICATED", "normal"),
                               note, provisional_value={"subtopic_ids": subtopic_ids}, prompt_version=prompt_version)
                rc.write_item_status(self.step, item_id, "flagged", prompt_version, extra={"check_message": note})
                rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version, started, ended,
                                    "pass", note, None, "flagged")
                continue

            set_a, set_b = set(data_a.get("subtopic_ids") or []), set(data_b.get("subtopic_ids") or [])
            if set_a == set_b and "unsure" not in set_a:
                subtopic_ids = data_a.get("subtopic_ids")
                self._assemble(qid, subtopic_ids, data_a.get("why", ""), data_a.get("confidence", "medium"),
                                prompt_version, "pass")
                rc.write_item_status(self.step, item_id, "pass", prompt_version, extra={"check_message": "runs agree"})
                rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version, started, ended,
                                    "pass", "runs agree", None, "pass")
            else:
                rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version, started, ended,
                                    "pass", f"disagreement (A={sorted(set_a)}, B={sorted(set_b)}) -> adjudicator",
                                    None, "pending")
                new_lines.extend(self._start_adjudicator(item_id, record, subtopics, data_a, data_b, prompt_version))
        return new_lines


class D3Plugin:
    """SCRIPT (fetch_passages.py) + its one documented agent escape hatch: spec 12/D3's own 'On
    failure: zero latest passages -> re-run D2 once with note "previous subtopics had no
    passages"; still zero -> blocked, D3_NO_PASSAGES (blocker)'. config/steps.yaml's placeholder
    agent field ("script") is corrected to "script + d2-subtopic-picker" (same DISCREPANCY-
    documented correction as C1's own entry) since this is a real, if rare, agent dispatch path,
    not a pure script step."""
    step = "D3"
    agent = "d2-subtopic-picker"  # the only agent D3 itself may ever dispatch (its D2-retry escape hatch)

    @staticmethod
    def _candidates():
        out = {}
        for qid, record in _d_candidates().items():
            subtopic_ids = record.get("d2_subtopic_ids")
            if not subtopic_ids or subtopic_ids == ["unsure"]:
                continue
            out[qid] = record
        return out

    @staticmethod
    def _d3_out_path(item_id):
        return rc.pp("steps", "D3", "out", f"{item_id}.json")

    def list_items(self, filters):
        """D3's only possible --list output: a pending D2-retry dispatch. The main fetch itself
        is SCRIPT-only, driven by --auto (scripts/fetch_passages.py), per scripts/CONVENTIONS.md."""
        lines = []
        for qid in self._candidates():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            pending = rc.read_pending(self.step, item_id) or {}
            if pending.get("stage") != "d2_retry":
                continue
            if os.path.exists(_out_path(self.step, item_id, "d2_retry")):
                continue  # already answered; check() will apply it
            input_path = _work_input_path(self.step, item_id, "d2_retry")
            if os.path.exists(input_path):
                lines.append(ListLine(item_id, self.agent, _relpath(input_path),
                                        _relpath(_out_path(self.step, item_id, "d2_retry")), "d2_retry"))
        return lines

    def list_reason(self):
        return ("D3 is mostly a SCRIPT-only step (scripts/fetch_passages.py) -- run `run_step.py "
                "D3 --auto`. The only thing ever listed here is a pending D2-retry dispatch for a "
                "question whose D2 subtopics turned up zero latest passages on the first try "
                "(spec 12/D3 On failure); none pending right now.")

    def auto(self, filters):
        script = rc.pp("scripts", "fetch_passages.py")
        if not os.path.exists(script):
            print(f"D3 --auto: {script} does not exist. Nothing to run.", file=sys.stderr)
            return
        prompt_version = rc.get_prompt_version(self.step)
        for qid in self._candidates():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            pending = rc.read_pending(self.step, item_id) or {}
            if pending.get("stage") == "d2_retry":
                continue  # awaiting the agent; don't re-fetch with the stale subtopics yet
            started = rc.now_iso()
            result = subprocess.run([sys.executable, script, "--item-id", item_id], cwd=rc.pp(),
                                      capture_output=True, text=True)
            ended = rc.now_iso()
            status = "pass" if result.returncode == 0 else "blocked"
            rc.append_run_log(item_id, self.step, "runA", None, prompt_version, started, ended,
                                "pass" if result.returncode == 0 else "fail",
                                "exit 0" if result.returncode == 0 else (result.stderr or "").strip()[-500:],
                                None, status)

    def _apply_d2_retry_result(self, qid, data, prompt_version):
        """Validates a d2-subtopic-picker re-pick (dispatched by THIS step) using D2's own
        schema+check -- reused, not duplicated, since it is literally a D2 judgement, just
        triggered by D3 instead of D2Plugin's own 2-run flow (a single extra run, not a fresh
        2-run+adjudicate cycle, per spec 12/D3's own wording 're-run D2 ONCE', singular)."""
        if not isinstance(data, dict) or "error" in data:
            return False
        ok, msg = rc.validate_schema("D2", data)
        if ok:
            record = lib_records.read_record(qid)
            subtopics = D2Plugin._subtopics_for_chapters(record.get("d1_chapter_ids"))
            context = {"item_id": qid, "step": "D2", "input_data": {"all_subtopic_ids": list(subtopics.keys())}}
            ok, msg = rc.run_step_check("D2", data, context)
        if ok and data.get("subtopic_ids") not in (None, ["unsure"]):
            D2Plugin._assemble(qid, data["subtopic_ids"], data.get("why", ""), data.get("confidence", "medium"),
                                 prompt_version, "flagged", note_from_runner="previous subtopics had no passages")
            rc.raise_flag("item", qid, "D2", "D2_ADJUDICATED", "normal",
                           "re-picked by D3 after the first subtopic choice had zero latest "
                           "passages (spec 12/D3 On failure)", provisional_value=data,
                           prompt_version=prompt_version)
            return True
        return False

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        new_lines = []
        for qid in self._candidates():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            existing = rc.read_item_status(self.step, item_id)
            if existing and existing.get("status") != "stale" and existing.get("prompt_version") == prompt_version:
                continue

            pending = rc.read_pending(self.step, item_id) or {}
            already_retried = pending.get("stage") == "d2_retry"
            if already_retried:
                retry_out = _out_path(self.step, item_id, "d2_retry")
                if not os.path.exists(retry_out):
                    continue  # waiting on the agent
                applied = self._apply_d2_retry_result(item_id, _read_json(retry_out), prompt_version)
                rc.clear_pending(self.step, item_id)
                if not applied:
                    rc.raise_flag("item", item_id, self.step, "D3_NO_PASSAGES",
                                   flags_cat.get("D3_NO_PASSAGES", "blocker"),
                                   "D2 retry produced no usable subtopic choice either; blocked",
                                   prompt_version=prompt_version)
                    rc.write_item_status(self.step, item_id, "blocked", prompt_version,
                                           extra={"check_message": "D2 retry unusable"})
                    rc.append_run_log(item_id, self.step, "d2_retry", "d2-subtopic-picker", prompt_version,
                                        rc.now_iso(), rc.now_iso(), "fail", "D2 retry unusable", None, "blocked")
                    continue
                # D2's subtopics just changed -- re-fetch now, in-process, before re-checking below
                # (see the module-level `import fetch_passages` comment on why this is safe).
                fetch_passages.fetch_for_item(item_id)

            out_path = self._d3_out_path(item_id)
            if not os.path.exists(out_path):
                continue  # --auto hasn't produced this item's fetch yet
            data = _read_json(out_path)
            started = ended = rc.now_iso()
            ok, msg = rc.validate_schema(self.step, data)
            if ok:
                ok, msg = rc.run_step_check(self.step, data, {"item_id": item_id, "step": self.step})
            if not ok:
                rc.write_item_status(self.step, item_id, "blocked", prompt_version, extra={"check_message": msg})
                rc.append_run_log(item_id, self.step, "runA", None, prompt_version, started, ended,
                                    "fail", msg, None, "blocked")
                continue

            if not data.get("latest"):
                if already_retried:
                    rc.raise_flag("item", item_id, self.step, "D3_NO_PASSAGES",
                                   flags_cat.get("D3_NO_PASSAGES", "blocker"),
                                   "zero latest passages even after re-running D2 once",
                                   prompt_version=prompt_version)
                    rc.write_item_status(self.step, item_id, "blocked", prompt_version,
                                           extra={"check_message": "zero latest passages after D2 retry"})
                    rc.append_run_log(item_id, self.step, "runA", None, prompt_version, started, ended,
                                        "fail", "zero latest passages after D2 retry", None, "blocked")
                    continue
                record = lib_records.read_record(item_id)
                subtopics = D2Plugin._subtopics_for_chapters(record.get("d1_chapter_ids"))
                input_data = {
                    "question": _d_question_view(record), "correct_answer": _d_answer_to_support(record),
                    "subtopics": [D2Plugin._subtopic_view(s) for s in subtopics.values()],
                    "note_from_runner": "previous subtopics had no passages",
                }
                _write_json(_work_input_path(self.step, item_id, "d2_retry"), input_data)
                rc.write_pending(self.step, item_id, {"stage": "d2_retry"})
                rc.append_run_log(item_id, self.step, "runA", None, prompt_version, started, ended,
                                    "fail", "zero latest passages -> re-running D2 once", None, "pending")
                new_lines.append(ListLine(item_id, "d2-subtopic-picker",
                                            _relpath(_work_input_path(self.step, item_id, "d2_retry")),
                                            _relpath(_out_path(self.step, item_id, "d2_retry")), "d2_retry"))
                continue

            rc.write_item_status(self.step, item_id, "pass", prompt_version,
                                   extra={"check_message": f"latest={len(data['latest'])} "
                                                            f"older={len(data['older'])} "
                                                            f"lab_manual={len(data['lab_manual'])}"})
            rc.append_run_log(item_id, self.step, "runA", None, prompt_version, started, ended,
                                "pass", "ok", None, "pass")
        return new_lines


class D4Plugin:
    step = "D4"
    agent = "d4-evidence-quoter"

    @staticmethod
    def _d3_latest(qid):
        path = rc.pp("steps", "D3", "out", f"{qid}.json")
        if not os.path.exists(path):
            return []
        return _read_json(path).get("latest") or []

    @staticmethod
    def _build_agent_input(record, answer_to_support, latest_passages):
        """The real d4-evidence-quoter input (its agent file's own Input block): question,
        answer_to_support, passages (D3's `latest` list, id + full text), codebook (only if
        codebook/D4_link_type.md exists -- it now does).

        Factored out of list_items() so BOTH the first dispatch and a retry build the same shape
        (see resolve_single_run_items' `agent_inputs` docstring for the real bug this fixed), and
        so D7Plugin can reuse it verbatim for spec 12's "After D7, D4 also runs for latest_answer
        if it differs" -- same question, same passages, a different answer_to_support.

        The codebook now comes from D4's OWN `codebook_file` entry in config/steps.yaml (via
        _e_codebook), not from a path hard-coded here. That was a real gap, reported in
        config/_pending_E_entries.yaml 2.6(a) and fixed while wiring Stage E: D4 did read
        codebook/D4_link_type.md, but because the config did not say so, config/cascade.yaml's
        `codebook_file` rule could not see the dependency -- editing that codebook would not have
        re-run D4 -- and nothing recorded which version a stored D4 link type was made under.
        """
        agent_input = {
            "question": _d_question_view(record),
            "answer_to_support": answer_to_support,
            "passages": [{"id": p["passage_id"], "text": p["text"]} for p in latest_passages],
        }
        codebook_text, _version = _e_codebook("D4")
        if codebook_text is not None:
            agent_input["codebook"] = codebook_text
        return agent_input

    @staticmethod
    def _candidates():
        """D4 needs a D3 output that actually PASSED (steps/D3/status/<QID>.json status=='pass'),
        not merely present -- a blocked D3 (D3_NO_PASSAGES) has nothing for D4 to quote from."""
        out = {}
        for qid, record in _d_candidates().items():
            d3_status = rc.read_item_status("D3", qid)
            if not d3_status or d3_status.get("status") != "pass":
                continue
            out[qid] = record
        return out

    def list_items(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for qid, record in self._candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            agent_input = self._build_agent_input(record, _d_answer_to_support(record),
                                                   self._d3_latest(qid))
            _write_json(_work_input_path(self.step, item_id, "runA"), agent_input)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("D4 needs a PASSING D3 output (steps/D3/status/<QID>.json, status=pass -- a "
                "blocked D3_NO_PASSAGES question has nothing to quote from). None ready yet, or "
                "everything ready already has output pending --check.")

    def _post_assembly(self, item_id, run_label, data, status, prompt_version, flags_cat):
        """Re-verifies every evidence quote independently of whatever check() already decided
        (never trusts the agent's own claim) and, for any quote genuinely not found, drops it and
        downgrades supports_answer -- spec 12/D4 On failure: 'quote not found -> retry -> still
        not found -> drop it, downgrade supports_answer, D4_QUOTE_NOT_FOUND (high)'. Then raises
        the unconditional outcome flags (D4_PARTLY/D4_NO_SUPPORT/D4_BEYOND_NCERT) on whatever the
        FINAL value is, regardless of check() pass/fail -- same precedent as A8Plugin/B8Plugin
        always flagging their own outcome (see scripts/checks/D4.py's own module docstring)."""
        if not isinstance(data, dict) or "error" in data:
            lib_records.set_fields(item_id, {
                "d4_link_type": None, "d4_evidence": [], "d4_derivation_steps": [],
                "d4_supports_answer": "not_at_all", "d4_missing": [],
                "d4_note": (data or {}).get("error", "no usable output"),
            }, step=self.step, prompt_version=prompt_version, status=status)
            return

        latest = {p["passage_id"]: p["text"] for p in self._d3_latest(item_id)}
        evidence = data.get("evidence") or []
        kept, dropped = [], []
        for item in evidence:
            if not isinstance(item, dict):
                dropped.append(item)
                continue
            pid, quote = item.get("passage_id"), item.get("exact_line")
            if pid in latest and quote_verify.find(quote, latest[pid]) is not None:
                kept.append(item)
            else:
                dropped.append(item)

        supports_answer = data.get("supports_answer")
        missing = list(data.get("missing") or [])
        if dropped:
            missing = missing + [f"{d.get('for', '?')} (quote not found, dropped)"
                                   for d in dropped if isinstance(d, dict)]
            if supports_answer == "fully":
                supports_answer = "partly" if kept else "not_at_all"
            rc.raise_flag("item", item_id, self.step, "D4_QUOTE_NOT_FOUND",
                           flags_cat.get("D4_QUOTE_NOT_FOUND", "high"),
                           f"{len(dropped)} evidence quote(s) not found word-for-word in their "
                           f"passage; dropped and downgraded supports_answer to {supports_answer!r}",
                           provisional_value={"dropped": dropped}, prompt_version=prompt_version)

        link_type = data.get("link_type")
        if supports_answer == "partly":
            rc.raise_flag("item", item_id, self.step, "D4_PARTLY", flags_cat.get("D4_PARTLY", "normal"),
                           "supports_answer is partly", prompt_version=prompt_version)
        elif supports_answer == "not_at_all":
            rc.raise_flag("item", item_id, self.step, "D4_NO_SUPPORT", flags_cat.get("D4_NO_SUPPORT", "normal"),
                           "supports_answer is not_at_all", prompt_version=prompt_version)
        if link_type == "beyond_ncert_method":
            rc.raise_flag("item", item_id, self.step, "D4_BEYOND_NCERT", flags_cat.get("D4_BEYOND_NCERT", "normal"),
                           data.get("note") or "beyond_ncert_method", prompt_version=prompt_version)

        # Spec 13.0: the codebook's file hash is recorded on every tag produced with it. Written
        # through the same helper the E steps use, so D4's hash lands in the record's
        # `codebook_version` map beside theirs (and as `d4_codebook_version`, mirroring D11).
        _e_set_tags(self.step, item_id, {
            "d4_link_type": link_type, "d4_derivation_steps": data.get("derivation_steps") or [],
            "d4_evidence": kept, "d4_supports_answer": supports_answer, "d4_missing": missing,
            "d4_note": data.get("note", ""),
        }, prompt_version, status, cb_version=_e_codebook("D4")[1])

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)
        items_with_builders = {}
        agent_inputs = {}
        for qid, record in self._candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            latest = self._d3_latest(qid)
            items_with_builders[item_id] = {
                "passages": {p["passage_id"]: p["text"] for p in latest},
                "structure": record.get("structure"),
                "statements": record.get("statements") or [],
                "answer_to_support": _d_answer_to_support(record),
            }
            agent_inputs[item_id] = self._build_agent_input(
                record, _d_answer_to_support(record), latest)

        def _post(item_id, run_label, data, status):
            self._post_assembly(item_id, run_label, data, status, prompt_version, flags_cat)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                          agent_inputs=agent_inputs)


# ===========================================================================
# D5-D11 - shared helpers
#
# Everything from here down is built on one principle that spec Section 4 rule 4 states and this
# project has already been bitten by: EVERY NCERT claim is a verified quote, and verification is
# done by a script against the real book on disk, never against what an agent echoed back. D5
# verifies against the OLDER edition (ncert/passages/<BOOK>O.jsonl, reached through D3's own
# `older` list) exactly the way D4Plugin verifies against the latest; D6 re-verifies both sides
# plus the lab manual before it decides a status, and again after the agent writes the note.
# ===========================================================================

_D_PASSAGE_ID_RE = re.compile(r"^([A-Z]{3})(\d{2})([LOM])-")


def _d_passage_edition(passage_id):
    """'BIO11O-CH10-P05' -> 'O'. The edition letter of a passage's own book id (spec 6.1):
    L = latest reprint 2026-27, O = the last edition before rationalisation, M = lab manual."""
    m = _D_PASSAGE_ID_RE.match(passage_id or "")
    return m.group(3) if m else None


def _d3_lists(qid):
    """D3's three lists for one question, or three empty lists if D3 never wrote for it."""
    path = rc.pp("steps", "D3", "out", f"{qid}.json")
    if not os.path.exists(path):
        return {"latest": [], "older": [], "lab_manual": []}
    data = _read_json(path)
    return {k: (data.get(k) or []) for k in ("latest", "older", "lab_manual")}


def _d3_texts(qid, key):
    """{passage_id: full_text} for one of D3's three lists -- the on-disk passage text, which is
    what every quote in D5/D6/D7 is verified against."""
    return {p["passage_id"]: (p.get("text") or "") for p in _d3_lists(qid).get(key, [])
            if p.get("passage_id")}


def _d_change_log_rows():
    path = rc.pp("ncert", "change_log.csv")
    if not os.path.exists(path):
        return []
    return [r for r in lib_io.read_csv(path) if (r.get("change_id") or "").strip()]


def _d_change_log_by_id():
    return {r["change_id"]: r for r in _d_change_log_rows()}


def _d_change_log_by_passage():
    """{passage_id: [change_log_row, ...]} keyed by BOTH sides of every row (old_passage_id and
    new_passage_id), so "this evidence passage has a change-log entry" (spec 12/D6 rule 3b and
    12/D7's run-gate) can be asked of a latest passage or an older one.

    REAL-DATA NOTE, not hidden: ncert/change_log.csv is HEADER-ONLY in this project today. A6-A9
    have only ever run against hand-built fixture chapters, so no real change-log row exists --
    which means D6 rules 3/3b and most of D7 cannot fire on real data yet. The code below is
    built for the rows that will exist; no row was fabricated to make anything pass.
    """
    out = {}
    for row in _d_change_log_rows():
        for key in ("old_passage_id", "new_passage_id"):
            pid = (row.get(key) or "").strip()
            if pid:
                out.setdefault(pid, []).append(row)
    return out


def _d_deleted_passage_ids():
    """old_passage_id of every row in ncert/deleted_topics.csv (spec 6.4) -- the only evidence
    that content was REMOVED (CLAUDE.md: "never treat the analysis's list of removed NCERT
    chapters as evidence; only Stage A's change log counts"). Header-only today, same as above."""
    path = rc.pp("ncert", "deleted_topics.csv")
    if not os.path.exists(path):
        return set()
    return {(r.get("old_passage_id") or "").strip() for r in lib_io.read_csv(path)
            if (r.get("old_passage_id") or "").strip()}


def _d_verified_quotes(items, texts, quote_key):
    """Split `items` into (kept, dropped) by whether each one's quote is found WORD FOR WORD in
    its own named passage's on-disk text. `texts` is {passage_id: full_text}; `quote_key` is
    "exact_line" (D4/D5 evidence) or "text" (D6 quoted_lines). The single chokepoint every
    verified-quote decision in D5-D7 goes through, so there is exactly one place where "verified"
    is defined."""
    kept, dropped = [], []
    for item in items or []:
        if not isinstance(item, dict):
            dropped.append(item)
            continue
        pid, quote = item.get("passage_id"), item.get(quote_key)
        if pid in texts and quote_verify.find(quote, texts[pid]) is not None:
            kept.append(item)
        else:
            dropped.append(item)
    return kept, dropped


def _d_answer_taught(record):
    """What students are taught (spec 3 Core concepts / 12 preamble: "D8-E5 use latest_answer").
    D7's `latest_answer` when D7 set one, else the Stage-D answer (corrected_answer if B8 made
    one, else official_answer)."""
    number = record.get("latest_answer")
    if number in (None, "", "unsure"):
        return _d_answer_to_support(record)
    options = record.get("corrected_options") or record.get("options_en") or {}
    return {"number": number, "text": options.get(str(number))}


def _d_step_resolved(step, qid, allow=("pass", "flagged", "skipped")):
    """True when `step` has a current-prompt-version status for this question that later steps may
    build on (spec 5.4: pass/flagged/skipped continue; blocked does not, stale must re-run)."""
    status = rc.read_item_status(step, qid)
    if not status or status.get("status") not in allow:
        return False
    return status.get("prompt_version") == rc.get_prompt_version(step)


def _d_fresh(step, qid):
    """True when this item still needs `step` for the current prompt version (spec 5.9)."""
    status = rc.read_item_status(step, qid)
    if not status:
        return True
    return status.get("status") == "stale" or status.get("prompt_version") != rc.get_prompt_version(step)


def _d_codebook(name):
    """(text, version) for codebook/<name>, or (None, "none") if the owner has not written it
    (spec 13.0). `version` is the file's own content hash, which spec 13.0 says to record as
    `codebook_version` on every tag produced with it.

    DELEGATES to scripts/codebook_version.py::load, which is byte-for-byte the formula this
    function used to carry inline (sha256 of the raw bytes, first 12 hex characters, the literal
    "none" when the file is absent). Keeping one formula in the repo is not tidiness: scripts/
    checks/E4.py recomputes the hash to catch a codebook that never reached its agent -- a wiring
    failure that is otherwise completely invisible -- and it cannot import this 7,000-line module
    to do it, so the two implementations would have had to agree by coincidence forever."""
    return codebook_version.load(name)


# ===========================================================================
# D5 - Find the line in the older NCERT (spec 12/D5; .claude/agents/d5-older-line-finder.md)
# ===========================================================================

class D5Plugin:
    """1 run + retry, agent `d5-older-line-finder`, driven by the generic retry resolver.

    The one check that matters (spec 12/D5 Checks, verbatim): "every older line found word for
    word in the **older** edition." Enforced twice over, the same belt-and-braces D4Plugin uses:
    scripts/checks/D5.py fails the run (so the retry message can name the offending quote), and
    _post_assembly re-verifies independently of whatever the check decided and DROPS any quote
    that cannot be found, flagging D5_QUOTE_NOT_FOUND (normal) -- a quote that cannot be found is
    never kept, per spec 4 rule 4.

    A question with ZERO older passages resolves to `skipped` without an agent call. That is the
    real state of every question in the bank today: A6 (pair old and new passages) has only ever
    run against hand-built fixtures, so ncert/pairs/ is empty and no older-edition book is
    indexed, so D3's `older` list comes back empty for every real question. There is nothing for
    the agent to search, and dispatching it to say "none for everything" would be a lie dressed
    as work. D5_NO_OLDER_PASSAGES (low) records the gap on the item so it is visible rather than
    silent.
    """
    step = "D5"
    agent = "d5-older-line-finder"

    @staticmethod
    def _candidates():
        """D5 needs D4 resolved (pass/flagged -- a blocked D4 has no evidence and no answer to
        find an older partner for) and not already resolved itself."""
        out = {}
        for qid, record in _d_candidates().items():
            if not _d_step_resolved("D4", qid, allow=("pass", "flagged")):
                continue
            out[qid] = record
        return out

    @staticmethod
    def _build_agent_input(record, older_passages, latest_evidence):
        """d5-older-line-finder.md's own Input block: question, answer_to_support,
        latest_evidence (D4's verified lines, may be empty), older_passages (id + text)."""
        return {
            "question": _d_question_view(record),
            "answer_to_support": _d_answer_to_support(record),
            "latest_evidence": latest_evidence,
            "older_passages": [{"id": p["passage_id"], "text": p.get("text") or ""}
                               for p in older_passages if p.get("passage_id")],
        }

    def list_items(self, filters):
        lines = []
        for qid, record in self._candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            if not _d_fresh(self.step, item_id):
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            older = _d3_lists(qid)["older"]
            if not older:
                continue  # resolved as `skipped` in check(), never dispatched
            agent_input = self._build_agent_input(record, older, record.get("d4_evidence") or [])
            _write_json(_work_input_path(self.step, item_id, "runA"), agent_input)
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("D5 needs a resolved D4 (steps/D4/status/<QID>.json pass or flagged) AND a "
                "non-empty `older` list in steps/D3/out/<QID>.json. None ready yet, or every "
                "ready question has zero older passages (resolved as skipped + "
                "D5_NO_OLDER_PASSAGES in --check, never dispatched -- the real state today, "
                "since no older-edition book is indexed and ncert/pairs/ is empty), or "
                "everything else already has output pending --check.")

    def _resolve_no_older(self, qid, record, prompt_version, flags_cat):
        """No older edition to search -> `skipped`, every D4 `for` label recorded as none_for."""
        labels = [e.get("for") for e in (record.get("d4_evidence") or []) if isinstance(e, dict)]
        lib_records.set_fields(qid, {
            "d5_older": [], "d5_none_for": labels,
            "d5_note": "no older-edition passages were available for this question (D3's `older` "
                        "list is empty); D5 was skipped, not answered",
            "d5_older_passages_available": 0,
        }, step=self.step, prompt_version=prompt_version, status="skipped")
        rc.raise_flag("item", qid, self.step, "D5_NO_OLDER_PASSAGES",
                       flags_cat.get("D5_NO_OLDER_PASSAGES", "low"),
                       "D3 returned zero older-edition passages, so there is nothing for D5 to "
                       "search. Upstream cause: no older-edition book is indexed by Stage A and "
                       "ncert/pairs/ is empty (A6 has only run on fixtures). Consequence to know "
                       "about downstream: D6 rules 3 and 3b (deleted_content / change-log) "
                       "cannot fire for this question.",
                       evidence=[_relpath(rc.pp("steps", "D3", "out", f"{qid}.json"))],
                       prompt_version=prompt_version)
        rc.write_item_status(self.step, qid, "skipped", prompt_version,
                               extra={"run": "none", "check_message": "no older passages to search"})
        rc.append_run_log(qid, self.step, "none", None, prompt_version, rc.now_iso(), rc.now_iso(),
                            "pass", "skipped: no older passages", None, "skipped")

    def _post_assembly(self, item_id, run_label, data, status, prompt_version, flags_cat):
        """Independently re-verify every older line against the OLDER book on disk (never the
        agent's claim), drop what cannot be found, and record what D4 covered that D5 left
        unaddressed."""
        older_texts = _d3_texts(item_id, "older")
        if not isinstance(data, dict) or "error" in data:
            lib_records.set_fields(item_id, {
                "d5_older": [], "d5_none_for": [],
                "d5_note": (data or {}).get("error", "no usable output"),
                "d5_older_passages_available": len(older_texts),
            }, step=self.step, prompt_version=prompt_version, status=status)
            return

        kept, dropped = _d_verified_quotes(data.get("older"), older_texts, "exact_line")
        none_for = list(data.get("none_for") or [])
        if dropped:
            none_for += [f"{d.get('for', '?')} (older quote not found, dropped)"
                         for d in dropped if isinstance(d, dict)]
            rc.raise_flag("item", item_id, self.step, "D5_QUOTE_NOT_FOUND",
                           flags_cat.get("D5_QUOTE_NOT_FOUND", "normal"),
                           f"{len(dropped)} older line(s) not found word-for-word in the older "
                           f"edition passage they named; dropped (spec 4 rule 4 -- a quote that is "
                           f"not found is rejected, never kept)",
                           provisional_value={"dropped": dropped}, prompt_version=prompt_version)

        d4_labels = {e.get("for") for e in (lib_records.read_record(item_id).get("d4_evidence") or [])
                     if isinstance(e, dict)}
        covered = {e.get("for") for e in kept} | set(data.get("none_for") or [])
        lib_records.set_fields(item_id, {
            "d5_older": kept, "d5_none_for": none_for, "d5_note": data.get("note", ""),
            "d5_older_passages_available": len(older_texts),
            "d5_d4_labels_unaddressed": sorted(l for l in d4_labels - covered if l),
        }, step=self.step, prompt_version=prompt_version, status=status)

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)
        items_with_builders, agent_inputs = {}, {}

        for qid, record in self._candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            if not _d_fresh(self.step, item_id):
                continue
            lists = _d3_lists(qid)
            if not lists["older"]:
                self._resolve_no_older(qid, record, prompt_version, flags_cat)
                continue
            items_with_builders[item_id] = {
                "older_passages": {p["passage_id"]: (p.get("text") or "") for p in lists["older"]
                                   if p.get("passage_id")},
                "latest_passage_ids": [p["passage_id"] for p in lists["latest"] if p.get("passage_id")],
            }
            agent_inputs[item_id] = self._build_agent_input(
                record, lists["older"], record.get("d4_evidence") or [])

        def _post(item_id, run_label, data, status):
            self._post_assembly(item_id, run_label, data, status, prompt_version, flags_cat)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                          agent_inputs=agent_inputs)


# ===========================================================================
# D6 - Latest NCERT or outside NCERT? (spec 12/D6; .claude/agents/d6-status-note-writer.md)
# ===========================================================================

class D6Plugin:
    """Three parts, exactly as spec 12/D6's Worker line splits them: SCRIPT decides the status,
    AGENT writes the note, SCRIPT verifies.

    THE RULE LADDER IS LOAD-BEARING AND ITS ORDER IS THE WHOLE RULE. _decide_status() below walks
    spec 12/D6's rules 0, 1, 2, 3, 3b, 4 in that literal order, first match wins, and stops. The
    order is what makes a Physics question whose answer no NCERT sentence states still come out
    `latest_ncert` (rule 0 catches rule_used/rules_chained/concept_applied before anything else
    can), and what makes a question with a deleted older line come out `deleted_content` rather
    than `outside_ncert` (rule 3 before rule 4). Reordering it silently relabels whole families of
    real questions as off-syllabus. SPEC 2.4 is explicit: never mark a question `outside_ncert`
    only because no sentence states the final number.

    The agent never gets to change the status -- it receives the decided status and writes the
    note for it. scripts/checks/D6.py fails any output that alters it.
    """
    step = "D6"
    agent = "script + d6-status-note-writer"
    agent_name = "d6-status-note-writer"

    # spec 3.1's seven templates, as fillers. The script half uses these for the documented
    # fallback ("retry; then SCRIPT fills the template from verified lines, D6_TEMPLATE_NOTE").
    @staticmethod
    def _fill_template(note_type, latest_line=None, older_line=None, rule_lines=None):
        if note_type == "same_both":
            return f'Answer from the latest NCERT: "{latest_line}".'
        if note_type == "written_differently":
            return (f'Answer from the latest NCERT: "{latest_line}". Remember: the older NCERT '
                     f'wrote it as "{older_line}". Same fact; follow the latest wording.')
        if note_type == "deleted":
            return ('This question is from content deleted from the latest NCERT. The answer is '
                     f'according to the older NCERT: "{older_line}".')
        if note_type == "outside":
            return ("This fact is not in any NCERT edition. The answer is from the official key.")
        if note_type == "outside_rules":
            quoted = ", ".join(f'"{r}"' for r in (rule_lines or []))
            return (f"This question uses a result that is not given in NCERT. The NCERT rules "
                     f"involved are: {quoted}. The answer is from the official key.")
        if note_type == "lab_manual":
            return f'Answer from the NCERT lab manual: "{latest_line}".'
        return None

    @staticmethod
    def _candidates():
        out = {}
        for qid, record in _d_candidates().items():
            if not _d_step_resolved("D5", qid):
                continue
            out[qid] = record
        return out

    @staticmethod
    def _verified_evidence(qid, record):
        """Re-verify D4's and D5's stored evidence against the real books on disk, and separate
        out any lab-manual line. Returns (latest, older, lab_manual) lists of evidence items.

        D4Plugin and D5Plugin already dropped unverified quotes, so this normally keeps
        everything -- it is run again anyway because D6's status decision is the point at which a
        wrong quote becomes a public claim about the syllabus, and because a passage file can
        legitimately change under a record (A2/A3 re-runs, the cascade).
        """
        latest_texts = _d3_texts(qid, "latest")
        older_texts = _d3_texts(qid, "older")
        lab_texts = _d3_texts(qid, "lab_manual")

        all_latest_side = record.get("d4_evidence") or []
        latest, _ = _d_verified_quotes(all_latest_side, latest_texts, "exact_line")
        older, _ = _d_verified_quotes(record.get("d5_older") or [], older_texts, "exact_line")

        # Rule 2's "a verified lab-manual line". Checked across BOTH quoting steps' evidence,
        # because neither of them is currently given lab-manual passages at all -- see the
        # GAP note in config/steps.yaml's D6 entry and the build report. The rule is implemented
        # correctly and fires the moment a producer of lab-manual quotes exists; it is not
        # reachable today and that is reported, not papered over.
        lab_candidates = [e for e in list(all_latest_side) + list(record.get("d5_older") or [])
                          if isinstance(e, dict) and _d_passage_edition(e.get("passage_id")) == "M"]
        lab_manual, _ = _d_verified_quotes(lab_candidates, lab_texts, "exact_line")
        return latest, older, lab_manual

    @classmethod
    def _decide_status(cls, record, latest, older, lab_manual):
        """spec 12/D6 "Status rules (SCRIPT, first match wins)", rules 0, 1, 2, 3, 3b, 4, in that
        exact order. Returns (syllabus_status, rule_fired, why)."""
        link_type = record.get("d4_link_type")
        deleted_ids = _d_deleted_passage_ids()
        change_log_by_passage = _d_change_log_by_passage()

        # 0. D4 link_type in {rule_used, rules_chained, concept_applied} with >= 1 verified rule
        #    quote -> latest_ncert.
        if link_type in ("rule_used", "rules_chained", "concept_applied"):
            rule_quotes = [e for e in latest if e.get("for") == "rule"]
            if rule_quotes:
                return ("latest_ncert", "0",
                        f"link_type {link_type!r} with {len(rule_quotes)} verified rule quote(s)")

        # 1. Else D4 has verified latest lines -> latest_ncert.
        if latest:
            return ("latest_ncert", "1", f"{len(latest)} verified latest-edition line(s) from D4")

        # 2. Else a verified lab-manual line exists -> lab_manual.
        if lab_manual:
            return ("lab_manual", "2", f"{len(lab_manual)} verified lab-manual line(s)")

        # 3. Else D5 has a verified older line in a passage on deleted_topics.csv ->
        #    deleted_content.
        on_deleted = [e for e in older if e.get("passage_id") in deleted_ids]
        if on_deleted:
            return ("deleted_content", "3",
                    f"verified older line in deleted passage(s) "
                    f"{sorted({e.get('passage_id') for e in on_deleted})}")

        # 3b. Else D5 has a verified older line in a passage that has a change-log entry ->
        #     latest_ncert, note type decided by D7.
        with_change = [e for e in older if change_log_by_passage.get(e.get("passage_id"))]
        if with_change:
            return ("latest_ncert", "3b",
                    f"verified older line in passage(s) with a change-log entry "
                    f"{sorted({e.get('passage_id') for e in with_change})}; note type is D7's to "
                    f"decide")

        # 4. Else outside_ncert; if link_type = beyond_ncert_method, note type outside_rules.
        return ("outside_ncert", "4",
                f"no verified latest line, no lab-manual line, no deleted or changed older line "
                f"(link_type {link_type!r})")

    @staticmethod
    def _allowed_note_types(status, rule_fired, link_type, older):
        """Which of spec 3.1's seven templates are legal for the decided status. `answer_changed`
        is never offered here: spec 12/D7 is the only thing that may produce it ("note type
        becomes answer_changed"), and D7 runs after D6."""
        if status == "lab_manual":
            return ["lab_manual"]
        if status == "deleted_content":
            return ["deleted"]
        if status == "outside_ncert":
            return ["outside_rules"] if link_type == "beyond_ncert_method" else ["outside"]
        # latest_ncert: `written_differently` is only meaningful when there IS an older line to
        # contrast with (spec 12/D6 Agent task: "choose written_differently only when the older
        # line states the same fact in different words").
        return ["same_both", "written_differently"] if older else ["same_both"]

    def _editions_map(self, qid):
        """{"L"|"O"|"M": {passage_id: text}}, omitting an edition this question has no passages
        for, so checks/D6.py can say "edition O, for which this question has no passages at all"
        rather than a vaguer failure."""
        out = {}
        for letter, key in (("L", "latest"), ("O", "older"), ("M", "lab_manual")):
            texts = _d3_texts(qid, key)
            if texts:
                out[letter] = texts
        return out

    def _build_agent_input(self, qid, record, status, allowed_note_types, latest, older, lab_manual):
        """d6-status-note-writer.md's own Input block: syllabus_status (decided by the script),
        latest_evidence / older_evidence / lab_manual_evidence (verified lines), change_log_entries
        on these passages. `allowed_note_types` is added by this build (judgement call, see the
        report): the agent file lists all six note types as allowed, but the status the script
        already decided rules most of them out, and passing the legal set is the difference
        between the agent choosing wrongly and the agent choosing at all."""
        by_passage = _d_change_log_by_passage()
        touched = {e.get("passage_id") for e in list(latest) + list(older) + list(lab_manual)}
        entries, seen = [], set()
        for pid in sorted(p for p in touched if p):
            for row in by_passage.get(pid, []):
                if row.get("change_id") in seen:
                    continue
                seen.add(row.get("change_id"))
                entries.append({k: row.get(k) for k in
                                ("change_id", "change_type", "old_fact", "new_fact",
                                 "old_passage_id", "new_passage_id", "could_flip_an_answer")})
        return {
            "syllabus_status": status,
            "allowed_note_types": allowed_note_types,
            "latest_evidence": latest,
            "older_evidence": older,
            "lab_manual_evidence": lab_manual,
            "change_log_entries": entries,
        }

    def _prepare(self, qid, record):
        """Everything the script decides before the agent is dispatched, computed once and reused
        by list_items(), check() and the template fallback."""
        latest, older, lab_manual = self._verified_evidence(qid, record)
        status, rule_fired, why = self._decide_status(record, latest, older, lab_manual)
        allowed = self._allowed_note_types(status, rule_fired, record.get("d4_link_type"), older)
        return {"latest": latest, "older": older, "lab_manual": lab_manual, "status": status,
                "rule_fired": rule_fired, "why": why, "allowed_note_types": allowed}

    def list_items(self, filters):
        lines = []
        for qid, record in self._candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            if not _d_fresh(self.step, item_id):
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            prep = self._prepare(qid, record)
            agent_input = self._build_agent_input(qid, record, prep["status"],
                                                   prep["allowed_note_types"], prep["latest"],
                                                   prep["older"], prep["lab_manual"])
            _write_json(_work_input_path(self.step, item_id, "runA"), agent_input)
            lines.append(ListLine(item_id, self.agent_name,
                                    _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("D6 needs a resolved D5 (steps/D5/status/<QID>.json pass, flagged or skipped). "
                "None ready yet, or everything ready already has output pending --check. The "
                "status itself is decided by this plugin's own SCRIPT half before any agent call "
                "(spec 12/D6 rule ladder 0/1/2/3/3b/4) -- the agent only writes the note.")

    def _script_note(self, prep, record, note_type_hint=None):
        """Fill spec 3.1's template from VERIFIED lines only -- the documented fallback when the
        agent's note cannot be used ("then SCRIPT fills the template from verified lines,
        D6_TEMPLATE_NOTE (low)"). Which line is quoted when several are verified: the one labelled
        `for: "answer"` if there is one, else the first `for: "rule"`, else the first verified
        line (the agent file's own instruction is "quote the one that decides the answer"; a
        script cannot judge that, so it prefers the label that says so). Returns
        (note_type, reason_note_or_None, quoted_lines).

        reason_note comes back None when the template this status needs a line for has no verified
        line to put in it. That is not hypothetical: rule 3b resolves to `latest_ncert` on the
        strength of an OLDER line in a changed passage, with no verified latest line at all, and
        rule 2's lab-manual line can only arrive if some step ever quotes a lab-manual passage
        (nothing currently does -- see config/steps.yaml's D6 entry). Filling the template anyway
        would print the literal word None inside a quotation mark and present it to a student as
        NCERT's wording, so the note is left empty for Stage F to write and the flag says why.
        """
        status = prep["status"]
        latest, older, lab = prep["latest"], prep["older"], prep["lab_manual"]

        def _pick(items):
            for want in ("answer", "rule"):
                for e in items:
                    if e.get("for") == want:
                        return e
            return items[0] if items else None

        note_type = note_type_hint or prep["allowed_note_types"][0]
        quoted = []
        if status == "lab_manual":
            e = _pick(lab)
            note_type = "lab_manual"
            note = self._fill_template("lab_manual", latest_line=e["exact_line"]) if e else None
            if e:
                quoted = [{"edition": "M", "passage_id": e["passage_id"], "text": e["exact_line"]}]
        elif status == "deleted_content":
            e = _pick(older)
            note_type = "deleted"
            note = self._fill_template("deleted", older_line=e["exact_line"]) if e else None
            if e:
                quoted = [{"edition": "O", "passage_id": e["passage_id"], "text": e["exact_line"]}]
        elif status == "outside_ncert":
            if record.get("d4_link_type") == "beyond_ncert_method":
                rules = [e for e in latest if e.get("for") == "rule"] or latest
                note_type = "outside_rules"
                note = self._fill_template(
                    "outside_rules", rule_lines=[e["exact_line"] for e in rules]) if rules else None
                quoted = [{"edition": "L", "passage_id": e["passage_id"], "text": e["exact_line"]}
                          for e in rules]
            else:
                note_type = "outside"
                note = self._fill_template("outside")  # quotes nothing; always fillable
        else:  # latest_ncert
            e = _pick(latest)
            # The script never claims `written_differently` on its own: that note type asserts the
            # older line states the SAME FACT in different words, which is a judgement spec 12/D6
            # gives the agent. With no usable agent note, the honest template is same_both.
            note_type = "same_both"
            note = self._fill_template("same_both", latest_line=e["exact_line"]) if e else None
            if e:
                quoted = [{"edition": "L", "passage_id": e["passage_id"], "text": e["exact_line"]}]
        return note_type, note, quoted

    def _assemble(self, qid, status_value, note_type, reason_note, quoted_lines, prep,
                   prompt_version, item_status):
        lib_records.set_fields(qid, {
            "syllabus_status": status_value,
            "note_type": note_type,
            "reason_note": reason_note,
            "d6_quoted_lines": quoted_lines,
            "d6_rule_fired": prep["rule_fired"],
            "d6_why": prep["why"],
        }, step=self.step, prompt_version=prompt_version, status=item_status)

    def _outcome_flags(self, qid, prep, note_type, record, prompt_version, flags_cat):
        """The flags spec 12/D6 raises on the OUTCOME, regardless of whether the check passed --
        the same unconditional-outcome-flag precedent as A8/B8/D4."""
        if note_type in ("written_differently", "deleted", "outside", "outside_rules"):
            rc.raise_flag("item", qid, self.step, "D6_NOTE_APPROVAL",
                           flags_cat.get("D6_NOTE_APPROVAL", "normal"),
                           f"note_type {note_type!r} needs a reviewer's approval before students "
                           f"see it (spec 12/D6 On failure)",
                           provisional_value={"note_type": note_type}, prompt_version=prompt_version)
        # Added by this build (see config/steps.yaml's D6 entry): an `outside_ncert` verdict
        # reached while NO older edition was available at all is not the same claim as one reached
        # with the older book in hand -- rules 3 and 3b could not even be evaluated, so
        # `deleted_content` was never actually ruled out. Telling a student a question is
        # off-syllabus on that basis is exactly the error SPEC 2.4 warns about, so it is flagged.
        if prep["status"] == "outside_ncert" and not record.get("d5_older_passages_available"):
            rc.raise_flag("item", qid, self.step, "D6_STATUS_UNVERIFIABLE",
                           flags_cat.get("D6_STATUS_UNVERIFIABLE", "normal"),
                           "status is outside_ncert, but this question had ZERO older-edition "
                           "passages, so rules 3 (deleted_content) and 3b (change-log) could not "
                           "be evaluated at all -- `deleted_content` has not actually been ruled "
                           "out. Upstream cause: no older-edition book is indexed by Stage A.",
                           provisional_value={"syllabus_status": "outside_ncert"},
                           prompt_version=prompt_version)

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        fallback = cfg.get("fallback") or []
        new_lines = []

        for qid, record in self._candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            if not _d_fresh(self.step, item_id):
                continue

            runs = _outputs_by_item(self.step).get(item_id, {})
            if "retry1" in runs:
                run_label = "retry1"
            elif "runA" in runs:
                run_label = "runA"
            else:
                continue  # still waiting on the agent

            prep = self._prepare(qid, record)
            data = _read_json(_out_path(self.step, item_id, run_label))
            started = rc.now_iso()
            if isinstance(data, dict) and "error" in data:
                ok, msg = False, f"agent reported error: {data['error']}"
            else:
                ok, msg = rc.validate_schema(self.step, data)
                if ok:
                    context = {"item_id": item_id, "step": self.step, "input_data": {
                        "syllabus_status": prep["status"],
                        "allowed_note_types": prep["allowed_note_types"],
                        "editions": self._editions_map(qid),
                    }}
                    ok, msg = rc.run_step_check(self.step, data, context)
            ended = rc.now_iso()

            if ok:
                self._assemble(qid, data["syllabus_status"], data["note_type"], data["reason_note"],
                                data.get("quoted_lines") or [], prep, prompt_version, "pass")
                self._outcome_flags(qid, prep, data["note_type"], record, prompt_version, flags_cat)
                rc.write_item_status(self.step, item_id, "pass", prompt_version,
                                       extra={"run": run_label, "check_message": msg,
                                               "rule_fired": prep["rule_fired"]})
                rc.append_run_log(item_id, self.step, run_label, self.agent_name, prompt_version,
                                    started, ended, "pass", msg, None, "pass")
                continue

            if run_label == "runA" and "retry" in fallback:
                rc.append_run_log(item_id, self.step, run_label, self.agent_name, prompt_version,
                                    started, ended, "fail", msg, None, "pending")
                rc.write_pending(self.step, item_id, {"reason": msg, "next_run": "retry1"})
                retry_input = self._build_agent_input(qid, record, prep["status"],
                                                       prep["allowed_note_types"], prep["latest"],
                                                       prep["older"], prep["lab_manual"])
                retry_input["previous_attempt_failed"] = msg
                _write_json(_work_input_path(self.step, item_id, "retry1"), retry_input)
                new_lines.append(ListLine(item_id, self.agent_name,
                                            _relpath(_work_input_path(self.step, item_id, "retry1")),
                                            _relpath(_out_path(self.step, item_id, "retry1")), "retry1"))
                continue

            # Retry exhausted -> spec 12/D6 On failure: "then SCRIPT fills the template from
            # verified lines, D6_TEMPLATE_NOTE (low)".
            note_type, reason_note, quoted = self._script_note(prep, record)
            if reason_note is None:
                detail = (f"the agent's note could not be used after a retry ({msg}), AND the "
                          f"SCRIPT could not fill spec 3.1's {note_type!r} template either: this "
                          f"question's status was decided by rule {prep['rule_fired']} "
                          f"({prep['why']}) and there is no verified line of the edition that "
                          f"template quotes. The reason note is left EMPTY for Stage F to write "
                          f"rather than filled with a placeholder a student would read as NCERT's "
                          f"own wording.")
                severity = "normal"
            else:
                detail = (f"the agent's note could not be used after a retry ({msg}); the SCRIPT "
                          f"filled spec 3.1's {note_type!r} template from verified lines instead")
                severity = flags_cat.get("D6_TEMPLATE_NOTE", "low")
            self._assemble(qid, prep["status"], note_type, reason_note or "", quoted, prep,
                            prompt_version, "flagged")
            rc.raise_flag("item", item_id, self.step, "D6_TEMPLATE_NOTE", severity, detail,
                           provisional_value={"note_type": note_type, "reason_note": reason_note},
                           prompt_version=prompt_version)
            self._outcome_flags(qid, prep, note_type, record, prompt_version, flags_cat)
            rc.write_item_status(self.step, item_id, "flagged", prompt_version,
                                   extra={"run": run_label, "check_message": msg,
                                           "rule_fired": prep["rule_fired"]})
            rc.append_run_log(item_id, self.step, run_label, self.agent_name, prompt_version,
                                started, ended, "fail", msg,
                                "runA" if run_label == "retry1" else None, "flagged")
        return new_lines


# ===========================================================================
# D7 - Check the answer against the latest NCERT (spec 12/D7)
#
# INPUT RESTRICTED BY RULE, ENFORCED IN CODE. CLAUDE.md and spec Rule 10: "B6 never sees the key;
# B6 and D7 never see coaching material." D7 differs from B6 in that it IS allowed the official
# answer (it has to compare against it) but is NOT allowed coaching material -- and, by the same
# logic that makes B6 blind, must not see B6's own answer either, or its "independent" reading of
# the latest book would be anchored on another agent's guess. _build_input() below constructs the
# input field by field from an explicit ALLOWLIST and then runs _guard_d7_input(), which refuses
# any key outside that list, any B6-derived field anywhere in the nested structure, and (via
# lib/coaching_guard.py) any inputs/coaching or inputs/legacy_sheets path. It raises rather than
# warns: a leak here is not something to carry on from.
# ===========================================================================

_D7_ALLOWED_TOP_LEVEL = frozenset({
    "question", "options", "official_answer", "latest_evidence", "older_evidence",
    "change_log_entries", "previous_attempt_failed",
})

# Field names that must never appear ANYWHERE in a D7 input, at any depth. B6's own output is the
# important half: spec Rule 10 makes B6 blind precisely so its answer is independent evidence, and
# feeding it to D7 would destroy the independence in the other direction too.
_D7_FORBIDDEN_FIELD_NAMES = frozenset({
    "b6_answer", "b6_reason", "b6_working", "b6_confidence", "b6_note", "b6_agrees_with_key",
    "coaching", "coaching_solution", "solution", "explanation", "legacy_sheet", "legacy_row",
})
_D7_FORBIDDEN_FIELD_PREFIXES = ("b6_", "coaching_", "legacy_")


class D7InputGuardError(ValueError):
    """Raised when a D7 agent input would carry something spec Rule 10 forbids it."""


def _guard_d7_input(data):
    """Allowlist + denylist guard for D7's agent input. Mirrors B6Plugin's approach (build from
    named record fields only, never pass the record) but enforces it mechanically rather than by
    construction, because D7's input is assembled from four different upstream steps."""
    extra = set(data) - _D7_ALLOWED_TOP_LEVEL
    if extra:
        raise D7InputGuardError(
            f"D7 input carries field(s) {sorted(extra)} that are not on its allowlist "
            f"{sorted(_D7_ALLOWED_TOP_LEVEL)} (spec Rule 10: D7's reads are fixed by spec 12/D7)"
        )

    def walk(node, path="<root>"):
        if isinstance(node, dict):
            for k, v in node.items():
                lower = str(k).lower()
                if lower in _D7_FORBIDDEN_FIELD_NAMES or \
                        any(lower.startswith(p) for p in _D7_FORBIDDEN_FIELD_PREFIXES):
                    raise D7InputGuardError(
                        f"D7 input carries forbidden field {k!r} at {path} -- D7 never sees "
                        f"coaching material or the blind solver's answer (spec Rule 10, "
                        f"d7-latest-answer-checker.md's own Never rule)"
                    )
                walk(v, f"{path}.{k}")
        elif isinstance(node, (list, tuple)):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]")

    walk(data)
    coaching_guard.guard_d7_input(data)  # inputs/coaching/, inputs/legacy_sheets/ path check
    return data


class D7Plugin:
    """1 run, agent `d7-latest-answer-checker`, plus one escape-hatch dispatch of its own.

    WHEN IT RUNS (spec 12/D7, verbatim): "every question whose D4/D5 passages have a change-log
    entry, and every question whose older line differs from its latest line. Others -> `skipped`
    with `latest_answer = official answer`." _should_run() implements exactly that, and the gate
    is deliberately broad on the second limb: two editions almost always word a fact slightly
    differently, so "differs" catches most questions that have an older line at all. Broad is the
    safe direction -- the cost is an agent call, the cost of missing one is teaching a stale
    answer.

    REAL-DATA NOTE: ncert/change_log.csv is header-only and no older edition is indexed, so today
    BOTH limbs are false for every real question and D7 skips every one of them. That is the
    honest outcome, not a stub: the skip path is the spec's own, and it sets latest_answer =
    official answer exactly as spec says.

    THE ESCAPE HATCH: spec 12/D7's On failure says a changed answer means "D4 re-runs for
    `latest_answer`". D7 dispatches that second d4-evidence-quoter call itself, under its own step
    directory with run label `d4_latest`, validating it with D4's own schema and check -- the same
    precedent as D3Plugin owning its own d2-subtopic-picker re-dispatch. D4Plugin is left
    untouched: its own item stays the evidence for the OFFICIAL answer, and the new evidence is
    stored separately as `d4_latest_answer_evidence`, so both answers keep their own proof (spec
    3: "When different, both are stored and the latest is taught").
    """
    step = "D7"
    agent = "d7-latest-answer-checker"

    @staticmethod
    def _candidates():
        out = {}
        for qid, record in _d_candidates().items():
            if not _d_step_resolved("D6", qid):
                continue
            out[qid] = record
        return out

    @staticmethod
    def _evidence_passage_ids(record):
        return {e.get("passage_id") for e in
                (record.get("d4_evidence") or []) + (record.get("d5_older") or [])
                if isinstance(e, dict) and e.get("passage_id")}

    @classmethod
    def _change_entries_for(cls, record):
        by_passage = _d_change_log_by_passage()
        entries, seen = {}, set()
        for pid in sorted(p for p in cls._evidence_passage_ids(record) if p):
            for row in by_passage.get(pid, []):
                cid = row.get("change_id")
                if cid and cid not in seen:
                    seen.add(cid)
                    entries[cid] = row
        return entries

    @staticmethod
    def _older_differs_from_latest(record):
        """spec 12/D7's second run-trigger: "every question whose older line differs from its
        latest line". Compared per `for` label (D5 reuses D4's labels by contract), after BOTH
        normalisations spec 5.7 defines -- normalise_quote (whitespace, hyphenation, curly quotes,
        ligatures) and then latex_normalise.normalise, which 5.7 scopes to exactly this use
        ("for comparing two readings only"). Using the most generous equality means "differs"
        means the two editions genuinely say it differently, not that one used a thin space."""
        def canon(s):
            return latex_normalise.normalise(text_normalise.normalise_quote(s or ""))

        latest_by_label = {}
        for e in record.get("d4_evidence") or []:
            if isinstance(e, dict):
                latest_by_label.setdefault(e.get("for"), []).append(canon(e.get("exact_line")))
        for e in record.get("d5_older") or []:
            if not isinstance(e, dict):
                continue
            label = e.get("for")
            if label not in latest_by_label:
                continue
            if canon(e.get("exact_line")) not in latest_by_label[label]:
                return True, label
        return False, None

    @classmethod
    def _should_run(cls, record):
        """Returns (should_run: bool, why: str)."""
        entries = cls._change_entries_for(record)
        if entries:
            return True, (f"evidence passage(s) have change-log entr(ies) "
                          f"{sorted(entries.keys())}")
        differs, label = cls._older_differs_from_latest(record)
        if differs:
            return True, f"the older line for {label!r} differs from the latest line"
        return False, ("no change-log entry on any evidence passage and no older line that "
                        "differs from its latest line")

    @classmethod
    def _build_input(cls, record):
        """D7's agent input, built field by field from the ALLOWLIST and then guarded. Matches
        d7-latest-answer-checker.md's own Input block: question and options; official_answer;
        latest_evidence, older_evidence; change_log_entries."""
        question = _d_question_view(record)
        options = question.pop("options", {})  # the agent file names options separately
        data = {
            "question": question,
            "options": options,
            "official_answer": str(record.get("corrected_answer") or record.get("official_answer")),
            "latest_evidence": record.get("d4_evidence") or [],
            "older_evidence": record.get("d5_older") or [],
            "change_log_entries": [
                {k: row.get(k) for k in ("change_id", "change_type", "old_fact", "new_fact",
                                          "old_passage_id", "new_passage_id", "could_flip_an_answer")}
                for row in cls._change_entries_for(record).values()
            ],
        }
        return _guard_d7_input(data)

    def list_items(self, filters):
        lines = []
        for qid, record in self._candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            if not _d_fresh(self.step, item_id):
                continue
            pending = rc.read_pending(self.step, item_id) or {}
            if pending.get("stage") == "d4_latest":
                # The D4 re-run for the changed answer is the outstanding work, not a D7 call.
                input_path = _work_input_path(self.step, item_id, "d4_latest")
                if os.path.exists(input_path) and not os.path.exists(_out_path(self.step, item_id, "d4_latest")):
                    lines.append(ListLine(item_id, "d4-evidence-quoter", _relpath(input_path),
                                            _relpath(_out_path(self.step, item_id, "d4_latest")),
                                            "d4_latest"))
                continue
            if pending or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            should_run, _why = self._should_run(record)
            if not should_run:
                continue  # resolved as `skipped` in check(), never dispatched
            _write_json(_work_input_path(self.step, item_id, "runA"), self._build_input(record))
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("D7 needs a resolved D6, and only runs for a question whose D4/D5 evidence "
                "passages carry a change-log entry or whose older line differs from its latest "
                "line (spec 12/D7). Everything else is resolved as `skipped` with latest_answer = "
                "the official answer, never dispatched. With ncert/change_log.csv header-only and "
                "no older edition indexed, that is currently every real question.")

    def _resolve_skipped(self, qid, record, why, prompt_version):
        answer = _d_answer_to_support(record)
        lib_records.set_fields(qid, {
            "latest_answer": answer["number"],
            "d7_same_as_official": True,
            "d7_status": "skipped",
            "d7_why_skipped": why,
        }, step=self.step, prompt_version=prompt_version, status="skipped")
        rc.write_item_status(self.step, qid, "skipped", prompt_version,
                               extra={"run": "none", "check_message": f"skipped: {why}"})
        rc.append_run_log(qid, self.step, "none", None, prompt_version, rc.now_iso(), rc.now_iso(),
                            "pass", f"skipped: {why}", None, "skipped")

    def _append_sentence_to_note(self, qid, record, sentence, prompt_version):
        """spec 12/D7 On failure, verbatim: "note type becomes `answer_changed`, sentence
        appended". Done literally. Judgement recorded in the build report: the resulting note is
        then D6's own note plus D7's sentence, which is NOT character-identical to spec 3.1's
        standalone `answer_changed` template -- spec states both things and they do not quite
        agree. The literal instruction wins here because it preserves the verified D6 note the
        reviewer already has in front of them, and D7_ANSWER_CHANGED (high) puts the result in
        front of a person regardless."""
        base = (record.get("reason_note") or "").strip()
        combined = f"{base} {sentence}".strip() if base else sentence
        lib_records.set_fields(qid, {"note_type": "answer_changed", "reason_note": combined},
                                 step=self.step, prompt_version=prompt_version, status="flagged")
        return combined

    def _start_d4_rerun(self, qid, record, latest_answer, prompt_version):
        options = record.get("corrected_options") or record.get("options_en") or {}
        answer_to_support = {"number": latest_answer, "text": options.get(str(latest_answer))}
        agent_input = D4Plugin._build_agent_input(record, answer_to_support, _d3_lists(qid)["latest"])
        agent_input["note_from_runner"] = (
            "D7 found the latest NCERT supports a different option than the official key. Quote "
            "the evidence for THIS answer (the latest-NCERT answer), not the official one."
        )
        _write_json(_work_input_path(self.step, qid, "d4_latest"), agent_input)
        rc.write_pending(self.step, qid, {"stage": "d4_latest", "latest_answer": latest_answer})
        return [ListLine(qid, "d4-evidence-quoter",
                           _relpath(_work_input_path(self.step, qid, "d4_latest")),
                           _relpath(_out_path(self.step, qid, "d4_latest")), "d4_latest")]

    def _apply_d4_rerun(self, qid, record, data, prompt_version, flags_cat):
        """Validate the D4 re-run with D4's own schema + check, verify every quote independently,
        and store it as the LATEST answer's evidence -- never overwriting d4_evidence, which is
        the official answer's proof and must survive (spec 3: both are stored)."""
        latest_texts = _d3_texts(qid, "latest")
        ok = isinstance(data, dict) and "error" not in data
        msg = "ok"
        if ok:
            ok, msg = rc.validate_schema("D4", data)
        if ok:
            context = {"item_id": qid, "step": "D4", "input_data": {
                "passages": latest_texts,
                "structure": record.get("structure"),
                "statements": record.get("statements") or [],
                "answer_to_support": _d_answer_taught(record),
            }}
            ok, msg = rc.run_step_check("D4", data, context)
        kept, dropped = ([], [])
        if isinstance(data, dict) and "error" not in data:
            kept, dropped = _d_verified_quotes(data.get("evidence"), latest_texts, "exact_line")
        if dropped:
            rc.raise_flag("item", qid, self.step, "D7_QUOTE_NOT_FOUND",
                           flags_cat.get("D7_QUOTE_NOT_FOUND", "high"),
                           f"{len(dropped)} quote(s) in the D4 re-run for the latest answer were "
                           f"not found word-for-word and were dropped",
                           provisional_value={"dropped": dropped}, prompt_version=prompt_version)
        lib_records.set_fields(qid, {
            "d4_latest_answer_link_type": (data or {}).get("link_type"),
            "d4_latest_answer_evidence": kept,
            "d4_latest_answer_derivation_steps": (data or {}).get("derivation_steps") or [],
            "d4_latest_answer_supports": (data or {}).get("supports_answer"),
            "d4_latest_answer_check": msg,
        }, step=self.step, prompt_version=prompt_version, status="flagged")
        return ok, msg

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        fallback = cfg.get("fallback") or []
        new_lines = []

        for qid, record in self._candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            if not _d_fresh(self.step, item_id):
                continue

            pending = rc.read_pending(self.step, item_id) or {}
            if pending.get("stage") == "d4_latest":
                rerun_path = _out_path(self.step, item_id, "d4_latest")
                if not os.path.exists(rerun_path):
                    continue  # waiting on the re-run
                record = lib_records.read_record(item_id)
                ok, msg = self._apply_d4_rerun(item_id, record, _read_json(rerun_path),
                                                prompt_version, flags_cat)
                rc.clear_pending(self.step, item_id)
                note = (f"latest answer differs from the official key; D4 re-run for the latest "
                        f"answer {'passed' if ok else 'did not pass'} ({msg})")
                rc.write_item_status(self.step, item_id, "flagged", prompt_version,
                                       extra={"run": "d4_latest", "check_message": note})
                rc.append_run_log(item_id, self.step, "d4_latest", "d4-evidence-quoter",
                                    prompt_version, rc.now_iso(), rc.now_iso(),
                                    "pass" if ok else "fail", note, None, "flagged")
                continue

            should_run, why = self._should_run(record)
            if not should_run:
                self._resolve_skipped(qid, record, why, prompt_version)
                continue

            runs = _outputs_by_item(self.step).get(item_id, {})
            if "retry1" in runs:
                run_label = "retry1"
            elif "runA" in runs:
                run_label = "runA"
            else:
                continue

            data = _read_json(_out_path(self.step, item_id, run_label))
            official = str(record.get("corrected_answer") or record.get("official_answer"))
            started = rc.now_iso()
            if isinstance(data, dict) and "error" in data:
                ok, msg = False, f"agent reported error: {data['error']}"
            else:
                ok, msg = rc.validate_schema(self.step, data)
                if ok:
                    context = {"item_id": item_id, "step": self.step, "input_data": {
                        "latest_passages": _d3_texts(qid, "latest"),
                        "change_log_entries": self._change_entries_for(record),
                        "evidence_passage_ids": sorted(self._evidence_passage_ids(record)),
                        "official_answer": official,
                    }}
                    ok, msg = rc.run_step_check(self.step, data, context)
            ended = rc.now_iso()

            if not ok:
                if run_label == "runA" and "retry" in fallback:
                    rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version,
                                        started, ended, "fail", msg, None, "pending")
                    rc.write_pending(self.step, item_id, {"reason": msg, "next_run": "retry1"})
                    retry_input = self._build_input(record)
                    retry_input["previous_attempt_failed"] = msg
                    _write_json(_work_input_path(self.step, item_id, "retry1"),
                                 _guard_d7_input(retry_input))
                    new_lines.append(ListLine(item_id, self.agent,
                                                _relpath(_work_input_path(self.step, item_id, "retry1")),
                                                _relpath(_out_path(self.step, item_id, "retry1")), "retry1"))
                    continue
                # Retry exhausted. D7 has no safe default that could be invented without claiming
                # something about what students are taught, so the item blocks (spec 5.5 rung 4).
                rc.raise_flag("item", item_id, self.step, "D7_UNRESOLVED",
                               flags_cat.get("D7_UNRESOLVED", "blocker"),
                               f"D7 could not produce a usable latest-answer reading after a "
                               f"retry ({msg}); the official answer stands unchecked",
                               prompt_version=prompt_version)
                lib_records.set_fields(qid, {"latest_answer": _d_answer_to_support(record)["number"],
                                               "d7_status": "unresolved"},
                                         step=self.step, prompt_version=prompt_version, status="blocked")
                rc.write_item_status(self.step, item_id, "blocked", prompt_version,
                                       extra={"run": run_label, "check_message": msg})
                rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version, started,
                                    ended, "fail", msg, "runA" if run_label == "retry1" else None,
                                    "blocked")
                continue

            latest_answer = data["latest_answer"]
            same = data["same_as_official"]
            lib_records.set_fields(qid, {
                "latest_answer": official if latest_answer == "unsure" else latest_answer,
                "d7_same_as_official": same,
                "d7_quote": data.get("quote", ""),
                "d7_change_id": data.get("change_id"),
                "d7_sentence_for_note": data.get("sentence_for_note", ""),
                "d7_note": data.get("note", ""),
                "d7_status": "ran",
                "d7_why_ran": why,
            }, step=self.step, prompt_version=prompt_version,
               status="pass" if same else "flagged")

            if same:
                rc.write_item_status(self.step, item_id, "pass", prompt_version,
                                       extra={"run": run_label, "check_message": "latest answer "
                                               "matches the official key"})
                rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version, started,
                                    ended, "pass", "same as official", None, "pass")
                continue

            # same_as_official false -> ALWAYS D7_ANSWER_CHANGED (high), note becomes
            # answer_changed with the sentence appended, and D4 re-runs for the latest answer.
            rc.raise_flag("item", item_id, self.step, "D7_ANSWER_CHANGED",
                           flags_cat.get("D7_ANSWER_CHANGED", "high"),
                           f"by the latest NCERT the answer is ({latest_answer}); the official key "
                           f"says ({official}). Both are kept; the latest is taught.",
                           provisional_value={"latest_answer": latest_answer,
                                               "official_answer": official,
                                               "change_id": data.get("change_id")},
                           evidence=[_relpath(_out_path(self.step, item_id, run_label))],
                           prompt_version=prompt_version)
            if data.get("change_id") is None:
                rc.raise_flag("item", item_id, self.step, "D7_UNEXPLAINED_CHANGE",
                               flags_cat.get("D7_UNEXPLAINED_CHANGE", "high"),
                               f"the answer changed but no change-log entry explains it "
                               f"(agent note: {data.get('note', '')!r})",
                               provisional_value={"latest_answer": latest_answer},
                               prompt_version=prompt_version)
            self._append_sentence_to_note(qid, lib_records.read_record(qid),
                                           data.get("sentence_for_note", ""), prompt_version)
            rc.append_run_log(item_id, self.step, run_label, self.agent, prompt_version, started,
                                ended, "pass", f"answer changed to {latest_answer}; D4 re-running",
                                None, "pending")
            new_lines.extend(self._start_d4_rerun(item_id, lib_records.read_record(qid),
                                                    latest_answer, prompt_version))
        return new_lines


# ===========================================================================
# D8 - Write the fact line (spec 12/D8; .claude/agents/d8-fact-line-writer.md)
# ===========================================================================

class D8Plugin:
    """1 run + retry, agent `d8-fact-line-writer`. The fact line is what D9 matches on, so this
    step is where a repeat becomes findable or is lost -- hence the one content check in
    scripts/checks/D8.py that is not cosmetic (a statement question's fact_line must be the
    ' | '-join of its own `facts`, because D9 matches a statement question fact by fact).

    The answer D8 is given is `answer_taught` = latest_answer (spec 12 preamble: "D8-E5 use
    latest_answer (what students are taught)"), which is D7's value when D7 changed it and the
    official/corrected answer otherwise."""
    step = "D8"
    agent = "d8-fact-line-writer"

    @staticmethod
    def _candidates():
        out = {}
        for qid, record in _d_candidates().items():
            if not _d_step_resolved("D7", qid):
                continue
            out[qid] = record
        return out

    @staticmethod
    def _subtopic_view(record):
        """The question's D2 subtopic(s), name + description, read from ncert/subtopics/."""
        subtopics = D2Plugin._subtopics_for_chapters(record.get("d1_chapter_ids"))
        chosen = [s for sid, s in subtopics.items() if sid in (record.get("d2_subtopic_ids") or [])]
        return [D2Plugin._subtopic_view(s) for s in chosen]

    @classmethod
    def _build_agent_input(cls, record):
        """d8-fact-line-writer.md's own Input block: question; answer_taught (latest answer);
        subtopic; evidence (verified latest lines). Evidence is the latest answer's own evidence
        when D7 changed the answer and D4 re-ran for it, else D4's original evidence -- quoting
        the official answer's proof under a different taught answer would be a real mismatch."""
        evidence = record.get("d4_latest_answer_evidence") or record.get("d4_evidence") or []
        return {
            "question": _d_question_view(record),
            "answer_taught": _d_answer_taught(record),
            "subtopic": cls._subtopic_view(record),
            "evidence": evidence,
        }

    def list_items(self, filters):
        lines = []
        for qid, record in self._candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            if not _d_fresh(self.step, item_id):
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            _write_json(_work_input_path(self.step, item_id, "runA"), self._build_agent_input(record))
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("D8 needs a resolved D7 (steps/D7/status/<QID>.json pass, flagged or skipped). "
                "None ready yet, or everything ready already has output pending --check.")

    def _post_assembly(self, item_id, run_label, data, status, prompt_version, flags_cat):
        if not isinstance(data, dict) or "error" in data:
            lib_records.set_fields(item_id, {
                "d8_fact_line": None, "d8_facts": [], "d8_confidence": "low",
                "d8_note": (data or {}).get("error", "no usable output"),
            }, step=self.step, prompt_version=prompt_version, status=status)
            return
        confidence = data.get("confidence")
        if confidence == "low":
            rc.raise_flag("item", item_id, self.step, "D8_LOW_CONFIDENCE",
                           flags_cat.get("D8_LOW_CONFIDENCE", "low"),
                           f"the fact line was written with low confidence: "
                           f"{data.get('fact_line', '')!r}",
                           provisional_value={"fact_line": data.get("fact_line")},
                           prompt_version=prompt_version)
        lib_records.set_fields(item_id, {
            "d8_fact_line": data.get("fact_line"), "d8_facts": data.get("facts") or [],
            "d8_confidence": confidence, "d8_note": data.get("note", ""),
            # Also under the spec's own unprefixed names (spec 3.2 layer 2 / 12/D9's Reads line
            # call them `fact_line` and `facts`), so D9 and Stage E/F read the name the spec uses
            # rather than this file's step-prefix convention. Only D8 ever writes either.
            "fact_line": data.get("fact_line"), "facts": data.get("facts") or [],
        }, step=self.step, prompt_version=prompt_version, status=status)

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)
        items_with_builders, agent_inputs = {}, {}
        for qid, record in self._candidates().items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            items_with_builders[item_id] = {
                "structure": record.get("structure"),
                "d4_has_derivation": bool(record.get("d4_derivation_steps")
                                           or record.get("d4_latest_answer_derivation_steps")),
            }
            agent_inputs[item_id] = self._build_agent_input(record)

        def _post(item_id, run_label, data, status):
            self._post_assembly(item_id, run_label, data, status, prompt_version, flags_cat)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                          agent_inputs=agent_inputs)


# ===========================================================================
# D9 - Find possible repeats (spec 12/D9; .claude/agents/d9-repeat-finder.md)
# ===========================================================================

class D9Plugin:
    """1 run + retry, agent `d9-repeat-finder`. Deliberately a WIDE net: "inclusive. If unsure,
    include." D11 is the strict verdict, so a false candidate costs one comparison and a missed
    repeat is lost forever.

    *** SPEC QUESTION, IMPLEMENTED AS WRITTEN. *** _others_table() scopes candidates to the same
    subtopic AND OTHER YEARS, verbatim from spec 12/D9's Reads line. That makes a repeat between
    two sittings of ONE year structurally unfindable -- 2016 MAIN/PH2, 2019 MAIN/REEXAM, 2020
    MAIN/REEXAM, 2024 MAIN/RETEST, and most pointedly 2026 CANCELLED (3 May) / REEXAM (21 Jun),
    where a cancelled paper and its re-exam are the likeliest place in the whole corpus for one
    fact to be asked twice inside a year. Implemented as the spec says and raised in the build
    report rather than widened silently; codebook/D11.md §6 raises the same question
    independently. The change, if the owner wants it, is the one `year` comparison below plus the
    matching one in scripts/checks/D9.py.

    A question with an EMPTY candidate table resolves to `skipped` with no flag. That is the real
    state of the whole bank today (10 questions, all from one sitting of one year, so every
    table is empty by construction), and it will stay a common, unremarkable outcome at full
    scale for any subtopic a single year happens to own -- a flag per such question would be pure
    noise, and spec 12/D9 names no flag for it. The `skipped` status is the record.
    """
    step = "D9"
    agent = "d9-repeat-finder"

    @staticmethod
    def _candidates():
        out = {}
        for qid, record in _d_candidates().items():
            if not _d_step_resolved("D8", qid):
                continue
            if not record.get("fact_line"):
                continue
            subtopics = [s for s in (record.get("d2_subtopic_ids") or []) if s and s != "unsure"]
            if not subtopics:
                continue
            out[qid] = record
        return out

    @classmethod
    def _others_table(cls, qid, record, pool):
        """Every OTHER question that shares a subtopic with this one and is from a DIFFERENT YEAR
        (spec 12/D9 Reads). Shape: {other_qid: {year, sitting, fact_line, subtopics}}."""
        mine = {s for s in (record.get("d2_subtopic_ids") or []) if s and s != "unsure"}
        my_year = record.get("year")
        out = {}
        for other_qid, other in pool.items():
            if other_qid == qid:
                continue
            if not other.get("fact_line"):
                continue
            theirs = {s for s in (other.get("d2_subtopic_ids") or []) if s and s != "unsure"}
            if not (mine & theirs):
                continue
            if other.get("year") == my_year:
                continue  # spec 12/D9: "other years" -- see this class's docstring
            out[other_qid] = {"year": other.get("year"), "sitting": other.get("sitting"),
                               "fact_line": other.get("fact_line"), "subtopics": sorted(theirs)}
        return out

    @staticmethod
    def _build_agent_input(qid, record, others):
        """d9-repeat-finder.md's own Input block: `this` (id, year, fact_line, facts) and `others`
        (id, year, sitting, fact_line). The subtopic ids are NOT shown to the agent -- they are
        the script's scoping rule, not a judgement input, and showing them would invite grouping
        by subtopic name, which the agent file explicitly forbids ("Do not include questions that
        only share the subtopic name")."""
        return {
            "this": {"id": qid, "year": record.get("year"),
                      "fact_line": record.get("fact_line"), "facts": record.get("facts") or []},
            "others": [{"id": oid, "year": o["year"], "sitting": o["sitting"],
                         "fact_line": o["fact_line"]} for oid, o in sorted(others.items())],
        }

    def list_items(self, filters):
        pool = self._candidates()
        lines = []
        for qid, record in pool.items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            if not _d_fresh(self.step, item_id):
                continue
            if rc.read_pending(self.step, item_id) or os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            others = self._others_table(qid, record, pool)
            if not others:
                continue  # resolved as `skipped` in check(), never dispatched
            _write_json(_work_input_path(self.step, item_id, "runA"),
                         self._build_agent_input(qid, record, others))
            lines.append(ListLine(item_id, self.agent, _relpath(_work_input_path(self.step, item_id, "runA")),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        return ("D9 needs a resolved D8 with a fact_line and at least one D2 subtopic, AND at "
                "least one OTHER question in the same subtopic from a DIFFERENT YEAR. The bank "
                "currently holds 10 questions, all from one sitting of one year, so every "
                "candidate table is empty by construction and every question resolves as "
                "`skipped` in --check without an agent call.")

    def _resolve_no_candidates(self, qid, prompt_version):
        lib_records.set_fields(qid, {
            "d9_possible_repeats": [], "d9_none": True,
            "d9_note": "no other question in this subtopic from another year",
        }, step=self.step, prompt_version=prompt_version, status="skipped")
        rc.write_item_status(self.step, qid, "skipped", prompt_version,
                               extra={"run": "none",
                                       "check_message": "no other-year question in this subtopic"})
        rc.append_run_log(qid, self.step, "none", None, prompt_version, rc.now_iso(), rc.now_iso(),
                            "pass", "skipped: no candidates", None, "skipped")

    def _post_assembly(self, item_id, run_label, data, status, prompt_version):
        if not isinstance(data, dict) or "error" in data:
            lib_records.set_fields(item_id, {
                "d9_possible_repeats": [], "d9_none": True,
                "d9_note": (data or {}).get("error", "no usable output"),
            }, step=self.step, prompt_version=prompt_version, status=status)
            return
        lib_records.set_fields(item_id, {
            "d9_possible_repeats": data.get("possible_repeats") or [],
            "d9_none": bool(data.get("none")),
            "d9_note": data.get("note", ""),
        }, step=self.step, prompt_version=prompt_version, status=status)

    def check(self, filters):
        cfg = get_cfg(self.step)
        prompt_version = rc.get_prompt_version(self.step)
        pool = self._candidates()
        items_with_builders, agent_inputs = {}, {}

        for qid, record in pool.items():
            item_id = qid
            if not rc.item_passes_filters(item_id, filters):
                continue
            if not _d_fresh(self.step, item_id):
                continue
            others = self._others_table(qid, record, pool)
            if not others:
                self._resolve_no_candidates(qid, prompt_version)
                continue
            items_with_builders[item_id] = {
                "this_id": qid, "this_year": record.get("year"),
                "this_subtopics": [s for s in (record.get("d2_subtopic_ids") or [])
                                    if s and s != "unsure"],
                "others": others,
            }
            agent_inputs[item_id] = self._build_agent_input(qid, record, others)

        def _post(item_id, run_label, data, status):
            self._post_assembly(item_id, run_label, data, status, prompt_version)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                          agent_inputs=agent_inputs)


# ===========================================================================
# D10 - Build candidate groups (spec 12/D10; scripts/build_groups.py). SCRIPT only, no judgement.
# ===========================================================================

class D10Plugin:
    step = "D10"
    agent = "script"

    def list_reason(self):
        return ("D10 is a script-only step (scripts/build_groups.py, union-find over D9's links). "
                "Run `run_step.py D10 --auto`. There is never anything to --list: it makes no "
                "judgement and calls no agent.")

    @staticmethod
    def _subtopics(filters):
        """Every subtopic with at least one D9-resolved question, from build_groups.py itself --
        so the runner's idea of "what work exists" and the script's can never drift apart."""
        return [s for s in build_groups.subtopics_with_work()
                if rc.item_passes_filters(s, filters)]

    def auto(self, filters):
        script = rc.pp("scripts", "build_groups.py")
        if not os.path.exists(script):
            print(f"D10 --auto: {script} does not exist. Nothing to run.", file=sys.stderr)
            return
        prompt_version = rc.get_prompt_version(self.step)
        for subtopic_id in self._subtopics(filters):
            started = rc.now_iso()
            result = subprocess.run([sys.executable, script, "--subtopic-id", subtopic_id],
                                      cwd=rc.pp(), capture_output=True, text=True)
            ended = rc.now_iso()
            rc.append_run_log(subtopic_id, self.step, "runA", None, prompt_version, started, ended,
                                "pass" if result.returncode == 0 else "fail",
                                "exit 0" if result.returncode == 0 else (result.stderr or "").strip()[-500:],
                                None, "pass" if result.returncode == 0 else "blocked")

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        for subtopic_id in self._subtopics(filters):
            existing = rc.read_item_status(self.step, subtopic_id)
            if existing and existing.get("status") != "stale" \
                    and existing.get("prompt_version") == prompt_version:
                continue
            out_path = rc.pp("steps", "D10", "out", f"{subtopic_id}.json")
            if not os.path.exists(out_path):
                continue  # --auto hasn't built this subtopic yet
            data = _read_json(out_path)
            started = ended = rc.now_iso()
            ok, msg = rc.validate_schema(self.step, data)
            if ok:
                ok, msg = rc.run_step_check(self.step, data,
                                             {"item_id": subtopic_id, "step": self.step})
            if not ok:
                rc.raise_flag("item", subtopic_id, self.step, "D10_PARTITION_INVALID",
                               flags_cat.get("D10_PARTITION_INVALID", "blocker"),
                               f"build_groups.py's output for this subtopic is not a valid "
                               f"partition of its questions: {msg}",
                               evidence=[_relpath(out_path)], prompt_version=prompt_version)
                rc.write_item_status(self.step, subtopic_id, "blocked", prompt_version,
                                       extra={"check_message": msg})
                rc.append_run_log(subtopic_id, self.step, "runA", None, prompt_version, started,
                                    ended, "fail", msg, None, "blocked")
                continue
            note = (f"groups={len(data['groups'])} singletons={len(data['singletons'])} "
                    f"links={len(data['links_used'])}")
            rc.write_item_status(self.step, subtopic_id, "pass", prompt_version,
                                   extra={"check_message": note})
            rc.append_run_log(subtopic_id, self.step, "runA", None, prompt_version, started, ended,
                                "pass", note, None, "pass")
        return []


# ===========================================================================
# D11 - Confirm each group (spec 12/D11; .claude/agents/d11-group-confirmer.md, codebook/D11.md)
# ===========================================================================

class D11Plugin:
    """2 runs + adjudicator, item = one candidate group (item_id = its RG-nnnn group id).

    Follows the real two-run-plus-adjudicator shape D1/D2/A4 already use. Agreement is compared on
    the WHOLE partition (which groups, which members, which label each member got, who is related
    to whom, who was removed), not just the group membership -- a run that keeps the same members
    but labels a pair `exact_same` where the other says `related` has genuinely disagreed about
    what the bank will teach.

    codebook/D11.md EXISTS, so its full text is passed as the `codebook` field (spec 13.0) and its
    content hash is recorded as `codebook_version` on every record D11 writes. codebook/D11.md's
    own STATUS section notes that nothing in this codebase computed codebook_version anywhere;
    that is now true for D11 at least.

    Splits: spec 12/D11 lets one candidate group become TWO groups ("if the group holds two
    different facts, split it into two groups"). The first output group keeps the candidate's own
    RG id; each further group mints a new one (lib/ids.py, counter-backed, never reused). The
    resolved id map is written to steps/D11/out/<RG>.resolved.json and reused on a re-resolve, so
    a rerun does not burn ids (spec 5.9).
    """
    step = "D11"
    agent = "d11-group-confirmer"

    @staticmethod
    def _candidate_groups(filters=None):
        """{group_id: {"subtopic_id", "members": [qid, ...]}} from every PASSING D10 output."""
        out = {}
        out_dir = rc.pp("steps", "D10", "out")
        if not os.path.isdir(out_dir):
            return out
        for fn in sorted(os.listdir(out_dir)):
            if not fn.endswith(".json"):
                continue
            subtopic_id = fn[: -len(".json")]
            status = rc.read_item_status("D10", subtopic_id)
            if not status or status.get("status") != "pass":
                continue
            data = _read_json(os.path.join(out_dir, fn))
            for g in data.get("groups") or []:
                gid = g.get("group_id")
                if gid and (filters is None or rc.item_passes_filters(gid, filters)):
                    out[gid] = {"subtopic_id": subtopic_id, "members": g.get("members") or []}
        return out

    @staticmethod
    def _member_view(qid, record):
        """spec 12/D11 Reads: "every member's id, year, sitting, first 300 characters of stem,
        answer text, fact line"."""
        return {
            "id": qid,
            "year": record.get("year"),
            "sitting": record.get("sitting"),
            "stem": (record.get("stem_en") or "")[:300],
            "answer_text": _d_answer_taught(record).get("text"),
            "fact_line": record.get("fact_line"),
        }

    @classmethod
    def _members_meta(cls, members, pool):
        return {qid: {"year": pool[qid].get("year"), "sitting": pool[qid].get("sitting")}
                for qid in members if qid in pool}

    def _build_agent_input(self, members, pool):
        codebook_text, _version = _e_codebook(self.step)
        data = {"members": [self._member_view(qid, pool[qid]) for qid in members if qid in pool]}
        if codebook_text is not None:
            data["codebook"] = codebook_text
        return data

    def _run_check(self, group_id, members, pool, data):
        if isinstance(data, dict) and "error" in data:
            return False, f"agent reported error: {data['error']}"
        ok, msg = rc.validate_schema(self.step, data)
        if not ok:
            return False, msg
        context = {"item_id": group_id, "step": self.step,
                    "input_data": {"members": self._members_meta(members, pool)}}
        return rc.run_step_check(self.step, data, context)

    @staticmethod
    def _canonical(data):
        """The comparable shape of one run's verdict: a frozen, order-independent description of
        the whole partition. Two runs "agree" when these are equal."""
        groups = frozenset(
            frozenset((m.get("id"), m.get("label")) for m in (g.get("members") or []))
            for g in (data.get("groups") or [])
        )
        related = frozenset((r.get("id"), r.get("related_to")) for r in (data.get("related") or []))
        removed = frozenset(data.get("removed") or [])
        return (groups, related, removed)

    def list_items(self, filters):
        pool = _d_candidates()
        lines = []
        for group_id, info in self._candidate_groups(filters).items():
            if not _d_fresh(self.step, group_id):
                continue
            if os.path.exists(_work_input_path(self.step, group_id, "adjudicated")):
                continue
            for run_label in ("runA", "runB"):
                if rc.read_pending(self.step, group_id) or \
                        os.path.exists(_out_path(self.step, group_id, run_label)):
                    continue
                _write_json(_work_input_path(self.step, group_id, run_label),
                             self._build_agent_input(info["members"], pool))
                lines.append(ListLine(group_id, self.agent,
                                        _relpath(_work_input_path(self.step, group_id, run_label)),
                                        _relpath(_out_path(self.step, group_id, run_label)), run_label))
        return lines

    def list_reason(self):
        return ("D11 needs at least one candidate group from a PASSING D10 subtopic "
                "(steps/D10/out/<SUBTOPIC>.json). None exist yet: D10 can only form a group from "
                "D9 links, and every real question's D9 resolves `skipped` for want of an "
                "other-year question in the same subtopic. No real repeat group exists in this "
                "bank today.")

    def _start_adjudicator(self, group_id, members, pool, data_a, data_b, prompt_version):
        codebook_text, _version = _e_codebook(self.step)
        payload = {
            "step": "D11",
            "task": "Run A and run B each independently decided which members of this candidate "
                     "repeat group truly test the same fact, labelled each against the earliest "
                     "member, and moved or dropped the rest. They disagree. Decide the correct "
                     "verdict.",
            "allowed_values": {
                "choice": ["A", "B", "combined", "unsure"],
                "A": "run A's verdict is correct as-is",
                "B": "run B's verdict is correct as-is",
                "combined": "neither alone is right; value gives the correct {groups, related, "
                             "removed} in the same shape as the two runs",
                "unsure": "cannot decide -- the script falls back to run A if it is valid, else "
                           "run B, else the group is blocked (no repeat is ever guessed at)",
            },
            "evidence": {"members": [self._member_view(q, pool[q]) for q in members if q in pool]},
            "run_a": {k: data_a.get(k) for k in ("groups", "related", "removed")},
            "run_b": {k: data_b.get(k) for k in ("groups", "related", "removed")},
            "failed_check": "run A and run B produced different partitions of this candidate group",
        }
        if codebook_text is not None:
            payload["codebook"] = codebook_text
        _write_json(_work_input_path(self.step, group_id, "adjudicated"), payload)
        rc.write_pending(self.step, group_id, {"stage": "adjudicating"})
        return [ListLine(group_id, "x-adjudicator",
                           _relpath(_work_input_path(self.step, group_id, "adjudicated")),
                           _relpath(_out_path(self.step, group_id, "adjudicated")), "adjudicated")]

    def _resolved_path(self, group_id):
        return rc.pp("steps", self.step, "out", f"{group_id}.resolved.json")

    def _group_ids_for(self, group_id, verdict):
        """Stable RG ids for the (possibly split) output groups: the candidate's own id for the
        first, a freshly minted one for each further group, reusing whatever a previous resolution
        already assigned to the same member set so a rerun mints nothing (spec 5.9)."""
        previous = {}
        path = self._resolved_path(group_id)
        if os.path.exists(path):
            for row in (_read_json(path).get("groups") or []):
                members = frozenset(m.get("id") for m in (row.get("members") or []))
                if members and row.get("group_id"):
                    previous[members] = row["group_id"]
        assigned, used = [], set()
        for i, g in enumerate(verdict.get("groups") or []):
            key = frozenset(m.get("id") for m in (g.get("members") or []))
            gid = previous.get(key)
            if gid is None:
                if i == 0 and group_id not in used:
                    gid = group_id
                else:
                    # Mint until the id is genuinely unused in this resolution. The loop is not
                    # theoretical: the counter (register/counters.json) and the candidate group's
                    # own id can get out of step -- a hand-built or restored D10 output, a copied
                    # fixture, a counters.json restored from an older backup -- and reusing the
                    # candidate's id for a SECOND split group would silently merge two different
                    # facts back into one group, which is the exact outcome spec 12/D11 and
                    # codebook/D11.md's "Never merge two different facts into one group" forbid.
                    gid = lib_ids.next_repeat_group_id()
                    while gid in used or gid == group_id:
                        gid = lib_ids.next_repeat_group_id()
            used.add(gid)
            assigned.append(gid)
        return assigned

    def _apply_verdict(self, group_id, info, verdict, prompt_version, item_status, note):
        """Writes repeat_group_id / repeat_label / related_ids onto each member's record (spec
        12/D11 Writes). `related_ids` is written SYMMETRICALLY -- the related member points at the
        group's first, and the first points back -- because a reviewer looking at either record
        needs to see the connection, and spec names the field on "each record" without saying
        which direction. Removed members get repeat_group_id None, so a previous grouping is
        actively cleared rather than left stale."""
        _, codebook_version = _e_codebook(self.step)
        group_ids = self._group_ids_for(group_id, verdict)
        resolved_groups = []
        related_back = {}

        for gid, g in zip(group_ids, verdict.get("groups") or []):
            members = g.get("members") or []
            for m in members:
                lib_records.set_fields(m["id"], {
                    "repeat_group_id": gid, "repeat_label": m.get("label"),
                    "repeat_group_fact_line": g.get("fact_line"),
                    "d11_codebook_version": codebook_version,
                }, step=self.step, prompt_version=prompt_version, status=item_status)
            resolved_groups.append({"group_id": gid, "fact_line": g.get("fact_line"),
                                     "first": g.get("first"), "members": members})

        for r in verdict.get("related") or []:
            lib_records.set_fields(r["id"], {
                "repeat_group_id": None, "repeat_label": None,
                "related_ids": [r.get("related_to")],
                "d11_codebook_version": codebook_version,
            }, step=self.step, prompt_version=prompt_version, status=item_status)
            related_back.setdefault(r.get("related_to"), []).append(r["id"])

        for target, ids in related_back.items():
            if not target:
                continue
            existing = lib_records.read_record(target).get("related_ids") or []
            lib_records.set_fields(target, {"related_ids": sorted(set(existing) | set(ids))},
                                     step=self.step, prompt_version=prompt_version, status=item_status)

        for qid in verdict.get("removed") or []:
            lib_records.set_fields(qid, {
                "repeat_group_id": None, "repeat_label": None,
                "d11_codebook_version": codebook_version,
            }, step=self.step, prompt_version=prompt_version, status=item_status)

        _write_json(self._resolved_path(group_id), {
            "candidate_group_id": group_id, "subtopic_id": info["subtopic_id"],
            "groups": resolved_groups, "related": verdict.get("related") or [],
            "removed": verdict.get("removed") or [], "codebook_version": codebook_version,
            "note": note,
        })

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        pool = _d_candidates()
        new_lines = []

        for group_id, info in self._candidate_groups(filters).items():
            if not _d_fresh(self.step, group_id):
                continue
            members = info["members"]

            if os.path.exists(_work_input_path(self.step, group_id, "adjudicated")):
                adj_path = _out_path(self.step, group_id, "adjudicated")
                if not os.path.exists(adj_path):
                    continue
                adj = _read_json(adj_path)
                data_a = _read_json(_out_path(self.step, group_id, "runA"))
                data_b = _read_json(_out_path(self.step, group_id, "runB"))
                choice = adj.get("choice")
                started = ended = rc.now_iso()
                verdict, note = None, ""
                if choice == "A":
                    verdict, note = data_a, "adjudicator chose run A"
                elif choice == "B":
                    verdict, note = data_b, "adjudicator chose run B"
                elif choice == "combined":
                    value = adj.get("value") or {}
                    ok_c, msg_c = self._run_check(group_id, members, pool, value)
                    if ok_c:
                        verdict, note = value, "adjudicator combined both runs"
                    else:
                        note = f"adjudicator 'combined' value invalid ({msg_c}); fell back"
                if verdict is None:
                    ok_a, msg_a = self._run_check(group_id, members, pool, data_a)
                    ok_b, msg_b = self._run_check(group_id, members, pool, data_b)
                    if ok_a:
                        verdict = data_a
                        note = (note + "; " if note else "") + \
                            f"adjudicator {choice or 'unsure'} -- used run A"
                    elif ok_b:
                        verdict = data_b
                        note = (note + "; " if note else "") + \
                            f"adjudicator {choice or 'unsure'} -- run A invalid ({msg_a}); used run B"
                    else:
                        # Spec 5.5 rung 4 with no safe default: a repeat group is never guessed at.
                        rc.raise_flag("item", group_id, self.step, "D11_UNRESOLVED",
                                       flags_cat.get("D11_UNRESOLVED", "blocker"),
                                       f"neither run nor the adjudicator produced a usable verdict "
                                       f"(runA: {msg_a}; runB: {msg_b}); no repeat is claimed for "
                                       f"this candidate group",
                                       prompt_version=prompt_version)
                        rc.write_item_status(self.step, group_id, "blocked", prompt_version,
                                               extra={"check_message": f"runA: {msg_a}; runB: {msg_b}"})
                        rc.append_run_log(group_id, self.step, "adjudicated", "x-adjudicator",
                                            prompt_version, started, ended, "fail",
                                            f"runA: {msg_a}; runB: {msg_b}", None, "blocked")
                        continue
                self._apply_verdict(group_id, info, verdict, prompt_version, "flagged", note)
                rc.raise_flag("item", group_id, self.step, "D11_ADJUDICATED",
                               flags_cat.get("D11_ADJUDICATED", "normal"), note,
                               provisional_value={"choice": choice},
                               evidence=[_relpath(self._resolved_path(group_id))],
                               prompt_version=prompt_version)
                rc.write_item_status(self.step, group_id, "flagged", prompt_version,
                                       extra={"check_message": note})
                rc.append_run_log(group_id, self.step, "adjudicated", "x-adjudicator",
                                    prompt_version, started, ended, "pass", note, None, "flagged")
                continue

            run_a_path = _out_path(self.step, group_id, "runA")
            run_b_path = _out_path(self.step, group_id, "runB")
            if not (os.path.exists(run_a_path) and os.path.exists(run_b_path)):
                continue
            data_a, data_b = _read_json(run_a_path), _read_json(run_b_path)
            ok_a, msg_a = self._run_check(group_id, members, pool, data_a)
            ok_b, msg_b = self._run_check(group_id, members, pool, data_b)
            started = ended = rc.now_iso()

            if not (ok_a and ok_b):
                if ok_a:
                    verdict, note = data_a, f"run B invalid ({msg_b}); used run A only"
                elif ok_b:
                    verdict, note = data_b, f"run A invalid ({msg_a}); used run B only"
                else:
                    rc.raise_flag("item", group_id, self.step, "D11_UNRESOLVED",
                                   flags_cat.get("D11_UNRESOLVED", "blocker"),
                                   f"both runs invalid (runA: {msg_a}; runB: {msg_b}); no repeat "
                                   f"is claimed for this candidate group",
                                   prompt_version=prompt_version)
                    rc.write_item_status(self.step, group_id, "blocked", prompt_version,
                                           extra={"check_message": f"runA: {msg_a}; runB: {msg_b}"})
                    rc.append_run_log(group_id, self.step, "runA+runB", self.agent, prompt_version,
                                        started, ended, "fail", f"runA: {msg_a}; runB: {msg_b}",
                                        None, "blocked")
                    continue
                self._apply_verdict(group_id, info, verdict, prompt_version, "flagged", note)
                rc.raise_flag("item", group_id, self.step, "D11_ADJUDICATED",
                               flags_cat.get("D11_ADJUDICATED", "normal"), note,
                               prompt_version=prompt_version)
                rc.write_item_status(self.step, group_id, "flagged", prompt_version,
                                       extra={"check_message": note})
                rc.append_run_log(group_id, self.step, "runA+runB", self.agent, prompt_version,
                                    started, ended, "pass", note, None, "flagged")
                continue

            if self._canonical(data_a) == self._canonical(data_b):
                self._apply_verdict(group_id, info, data_a, prompt_version, "pass", "runs agree")
                rc.write_item_status(self.step, group_id, "pass", prompt_version,
                                       extra={"check_message": "runs agree"})
                rc.append_run_log(group_id, self.step, "runA+runB", self.agent, prompt_version,
                                    started, ended, "pass", "runs agree", None, "pass")
            else:
                rc.append_run_log(group_id, self.step, "runA+runB", self.agent, prompt_version,
                                    started, ended, "pass",
                                    "runs produced different partitions -> adjudicator", None,
                                    "pending")
                new_lines.extend(self._start_adjudicator(group_id, members, pool, data_a, data_b,
                                                           prompt_version))
        return new_lines



# ===========================================================================
# Stage E - shared helpers (spec Section 13, codebook/E*.md, config/steps.yaml E0-E6)
#
# Five things every E plugin needs, and none of them should have its own copy:
#
#   * THE CODEBOOK the step declares, and its content hash (spec 13.0). Read through
#     _e_codebook(step) from the step's own `codebook_file` entry -- never from a table in this
#     file -- so declaring one in the YAML is all it takes for the runner to start passing it,
#     and E0's deliberately-null entry stays null.
#   * THE ALLOWED VALUES with their one-line definitions, read only through scripts/tag_values.py
#     (the single reader of config/allowed_values.yaml; a second copy of a 29-value list would
#     drift, and a value invented in a plugin would be indistinguishable from a real one).
#   * THE QUESTION VIEW, and D4's evidence lines WITH their passage kinds -- the kinds are the
#     strongest single signal in E3 and are NOT in D3's output, so they are looked up from the
#     real ncert/passages/<BOOK>.jsonl here.
#   * WHICH QUESTIONS HAVE REACHED THE STEP, from the step's own `needs` entry.
#   * THE REFUSAL OF LEGACY FIELDS. Spec Section 13: `legacy_chapter` / `legacy_topic` /
#     `legacy_question_type` "are never inputs to any agent" (spec 2.2: the legacy tags are not
#     usable, and a leak would anchor the very tag Stage F compares against). Every E dispatch
#     goes through _e_write_agent_input(), which calls legacy_match.assert_no_legacy first.
#
# WHERE THE TAGS LAND ON THE RECORD. Stage F reads UNPREFIXED spec names -- export_tables.py's
# TAG_COLUMNS and build_review_pack.py's FIELD_FOR_STEP are `question_type`, `format`,
# `content_shape`, `category_primary`, `category_secondary`, `category_why`, `option_traps`,
# `stem_context`, `answer_form`, `negation`, `item_count`, `constants_given`, `figure_role`,
# `descriptive_tags`, `codebook_version` -- so _e_set_tags() writes those, plus the step-prefixed
# copies this file uses elsewhere (same both-names precedent as D8Plugin's fact_line).
# ===========================================================================

#: codebook/E0.md does not exist and must not: spec 13/E0 step 1 runs e0-open-look with NO
#: categories shown, because a tagger shown the list stops discovering and starts matching.
#: config/steps.yaml's `codebook_file: null` for E0 is therefore load-bearing, not an omission,
#: and _e_codebook() honours it by reading the YAML rather than a hard-coded map.


def _e_codebook(step):
    """(text, version) for the codebook `config/steps.yaml` declares for `step` (spec 13.0).

    Spec 13.0, verbatim: "If a file exists, the runner passes its full text to the agent as the
    `codebook` field, and records its file hash as `codebook_version` on every tag it produced.
    If a file is missing, the agent receives only the allowed values ... and
    `codebook_version = "none"`."

    Returns (None, "none") when the step declares no codebook (E0) or the declared file is
    absent. The hash itself comes from _d_codebook -> scripts/codebook_version.py, so there is
    exactly one formula in the repo.
    """
    declared = str(get_cfg(step).get("codebook_file") or "").strip()
    if not declared:
        return None, codebook_version.NONE
    name = declared[len("codebook/"):] if declared.startswith("codebook/") else declared
    return _d_codebook(name)


def _e_allowed(list_name):
    """{value: one-line definition} for one config/allowed_values.yaml list -- what spec 13.0
    means by "the allowed values with their one-line definitions" in an agent input. Lists the
    YAML carries as a plain sequence (trap, content_shape) have no definitions, so every value
    maps to "" rather than being dropped: the agent still needs the complete value list."""
    defs = tag_values.definitions(list_name)
    if defs:
        return defs
    return {value: "" for value in tag_values.values(list_name)}


_E_PASSAGE_KINDS = {}


def _e_passage_kind(passage_id):
    """The `kind` of one passage (paragraph / table / figure / equation / box / mixed), read from
    the real ncert/passages/<BOOK>.jsonl.

    D3's output carries only `passage_id` and `text`, but e3-shape-tagger's own Input block asks
    for the evidence lines WITH their passage kinds, and flattening them to bare quotes throws
    away the signal the step turns on. The book id is the passage id's own first segment
    (spec 6.1: `PHY11L-CH08-P65` lives in `PHY11L.jsonl`). None when the book is not indexed --
    which is the normal state for most of this corpus today (Stage A has indexed 2 of 13 Biology
    chapters and zero Physics/Chemistry), so a None kind is honest missing data, not an error.
    """
    if not passage_id or "-" not in passage_id:
        return None
    book_id = passage_id.split("-", 1)[0]
    if book_id not in _E_PASSAGE_KINDS:
        kinds = {}
        path = rc.pp("ncert", "passages", f"{book_id}.jsonl")
        if os.path.exists(path):
            for row in lib_io.read_jsonl(path):
                if row.get("passage_id"):
                    kinds[row["passage_id"]] = row.get("kind")
        _E_PASSAGE_KINDS[book_id] = kinds
    return _E_PASSAGE_KINDS[book_id].get(passage_id)


def _e_question_view(record):
    """_d_question_view plus the two fields the E agents' own Input blocks name by hand: B3's
    `structure` (e1-type-tagger, e6-context-tagger) and `has_figure` (e6-context-tagger)."""
    view = _d_question_view(record)
    view["structure"] = record.get("structure")
    view["has_figure"] = bool(record.get("has_figure"))
    return view


def _e_evidence_view(record, include_older=True):
    """D4's (and D5's) verified evidence lines, each with its passage kind and edition.

    These are the lines D4Plugin/D5Plugin already re-verified word for word against the real
    books and stored on the record; nothing is re-quoted here. An EMPTY list is meaningful and is
    passed as [] rather than omitted -- scripts/checks/E3.py fails a `current_affairs` tag made
    with no evidence at all, and that rule only works if the key is present."""
    out = []
    for item in record.get("d4_evidence") or []:
        if not isinstance(item, dict):
            continue
        pid = item.get("passage_id")
        out.append({"passage_id": pid, "kind": _e_passage_kind(pid), "edition": "latest",
                     "for": item.get("for"), "exact_line": item.get("exact_line")})
    if include_older:
        for item in record.get("d5_older") or []:
            if not isinstance(item, dict):
                continue
            pid = item.get("passage_id")
            out.append({"passage_id": pid, "kind": _e_passage_kind(pid), "edition": "older",
                         "for": item.get("for"), "exact_line": item.get("exact_line")})
    return out


def _e_candidates(step, filters=None):
    """{qid: record} for every canonical question whose upstream step is resolved (spec 5.4:
    pass/flagged/skipped continue, blocked does not), read from the step's own `needs` entry in
    config/steps.yaml -- the same gate D5-D9 each hard-code for themselves."""
    needs = str(get_cfg(step).get("needs") or "").split(",")[0].strip()
    out = {}
    for qid, record in _d_candidates().items():
        if filters is not None and not rc.item_passes_filters(qid, filters):
            continue
        if needs and not _d_step_resolved(needs, qid):
            continue
        out[qid] = record
    return out


def _e_check_one(step, item_id, data, input_data, extra=None):
    """(ok, message) for ONE E agent output, in exactly the order resolve_single_run_items uses:
    the universal error branch, then schemas/<STEP>.json, then scripts/checks/<STEP>.py.

    Exists so a plugin can recover the failing message in its own post_assembly (several E steps'
    safe defaults are "use the failing check's message as new_description", and the generic
    resolver does not hand the message to the callback) and so the 2-run steps can check each run
    with one call. Every check module is a pure function of (data, context), so re-running one is
    cheap and cannot disagree with the first run."""
    if isinstance(data, dict) and "error" in data:
        return False, f"agent reported error: {data['error']}"
    ok, msg = rc.validate_schema(step, data)
    if not ok:
        return False, msg
    context = {"item_id": item_id, "step": step, "input_data": input_data,
                "project_root": rc.pp()}
    context.update(extra or {})
    return rc.run_step_check(step, data, context)


def _e_write_agent_input(step, item_id, run_label, payload):
    """Write one E work-input file, refusing any `legacy_` field at any depth first.

    scripts/legacy_match.py::assert_no_legacy is the mechanism spec Section 13's "Legacy fields
    ... are never inputs to any agent" needs; calling it here means every E dispatch -- first
    run, second run, retry and adjudication alike -- goes through it, the same belt-and-braces
    B6's coaching guard already uses for the answer key."""
    legacy_match.assert_no_legacy(payload, where=f"{step} {run_label} input for {item_id}")
    path = _work_input_path(step, item_id, run_label)
    _write_json(path, payload)
    return path


def _e_set_tags(step, qid, fields, prompt_version, status, cb_version=None):
    """Write one E step's resolved tags onto papers/records/<QID>.json and record the codebook
    hash (spec 13.0: "records its file hash as codebook_version on every tag it produced").

    `codebook_version` is kept as a {step: hash} MAP, not a string: one record carries tags from
    six different codebooks (E1-E6, each with its own file and its own hash) plus D4's and D11's,
    and a single string could not say which tag was made under which version -- which is the
    whole point of recording it, since config/cascade.yaml's `codebook_file` rule re-runs "every
    question of the step that reads it" and an auditor afterwards needs to know what each stored
    tag was made with. The per-step string is also written as `e1_codebook_version` ..
    `e6_codebook_version`, mirroring the `d11_codebook_version` D11Plugin already writes.

    Writes NOTHING when every field, every field_source and the codebook hash already hold what
    this call would write (spec 5.9: "running a command twice in a row must do nothing the second
    time" -- E6 in particular stores its five script-owned fields on every --check while
    `stem_context` is still waiting on the agent, and that must not keep rewriting the record)."""
    payload = dict(fields)
    existing = lib_records.read_record(qid)
    if cb_version is not None:
        stored = existing.get("codebook_version")
        if isinstance(stored, dict):
            merged = dict(stored)
        elif stored in (None, "", codebook_version.NONE):
            # Nothing, or spec 13.0's own "no codebook" marker: there is no earlier version to
            # preserve, so start the map clean rather than carrying "none" around as history.
            merged = {}
        else:  # a plain string written by something else: keep it rather than discard it
            merged = {"_previous": stored}
        merged[step] = cb_version
        payload["codebook_version"] = merged
        payload[f"{step.lower()}_codebook_version"] = cb_version

    sources = existing.get("field_sources") or {}
    want = {"step": step, "prompt_version": prompt_version, "status": status}
    if all(existing.get(key) == value for key, value in payload.items()) \
            and all(sources.get(key) == want for key in payload):
        return existing
    return lib_records.set_fields(qid, payload, step=step, prompt_version=prompt_version,
                                   status=status)


def _e_guard_segment(cfg, msg, code):
    """The detail of the first `<code>: ...` segment of a failing check message, or the whole
    message. Used for E2's retry text, which spec 13/E2 names verbatim ("retry with 'The stem
    contains <word>'") and scripts/checks/E2.py already puts at the head of every
    E2_NEGATIVE_GUARD segment -- so the retry forwards it unchanged rather than reconstructing
    the sentence and risking a different wording (config/_pending_E_entries.yaml 2.4)."""
    for seg_code, detail in rc.parse_check_message(cfg, msg):
        if seg_code == code and detail:
            return detail
    return msg


# ===========================================================================
# E0 - Category discovery (spec 13/E0; e0-open-look + e0-category-grouper + the SCRIPT sheet)
# ===========================================================================

class E0Plugin:
    """THE ONE E STEP WITH TWO AGENTS AND A SCRIPT, in three phases (spec 13/E0's own procedure):

      E0.1  e0-open-look, once per question in the sample, answering in free words with NO
            categories shown.                              item id: <QID>
      E0.2  e0-category-grouper, once per tag, grouping those free answers against the starting
            list.                                          item id: tag__<tag>
      E0.3  a SCRIPT, scripts/e0_category_sheet.py, exporting
            codebook/E0_findings/category_sheet.csv.       driven by --auto

    `codebook_file` IS null FOR E0 AND MUST STAY null. Phase 1's entire value is that the agent
    has not been shown the categories; handing it a codebook (or an `allowed` list) would turn
    the discovery into a matching exercise and make E0.2's grouping a restatement of the list it
    was fed, which reads to the owner as confirmation of the taxonomy rather than a test of it.
    So _build_open_look_input() passes no codebook and no allowed values, and E0 is the one E
    step whose records carry no codebook_version (there is no codebook behind its findings).

    E0 NEVER WRITES codebook/E*.md OR config/allowed_values.yaml -- spec 13/E0's own Never. This
    plugin writes nothing but its own work/out/status files and the one CSV the script writes;
    scripts/e0_category_sheet.py refuses any other destination by construction.

    SAMPLE SIZE IS A REAL GATE, not a warning. Spec 13/E0 asks for ~300 questions, ~100 per
    subject, across many chapters. The bank holds 10 canonical questions from one sitting of one
    year. Dispatching 10 open-look calls and grouping them would hand the owner counts of 1 and 2
    against a taxonomy that ~500 real sampled questions already validated -- so list_items()
    refuses below scripts/e0_category_sheet.py's own documented floor (the same constants, not a
    second copy) and says so with the real numbers.
    """
    step = "E0"
    agent = "e0-open-look"
    grouper_agent = "e0-category-grouper"

    #: spec 13/E0 groups five tags; each one's free-text precursor field in the open-look output,
    #: and the config/allowed_values.yaml list it is grouped against (same map as
    #: scripts/checks/E0.py's DISCOVERY_TAGS, which is why the names match it exactly).
    TAG_SOURCE_FIELD = {
        "thinking": "student_must",
        "question_type": "built_as",
        "format": "asks_to_pick",
        "content_shape": "ncert_material",
        "trap": "wrong_options",
    }

    @staticmethod
    def _tag_item_id(tag):
        return f"tag__{tag}"

    def _sample(self, filters=None):
        """Every canonical question E0 may draw on: D8 resolved (spec 13/E0 `needs: D8` -- the
        fact line is what makes a free answer about the right fact)."""
        return _e_candidates(self.step, filters)

    def _sample_state(self):
        """(total, {subject: n}, unassigned) over the real dispatchable sample."""
        sample = self._sample()
        per_subject = {s: 0 for s in e0_category_sheet.SUBJECTS}
        unassigned = 0
        for record in sample.values():
            subject = record.get("subject")
            if subject in per_subject:
                per_subject[subject] += 1
            else:
                unassigned += 1
        return len(sample), per_subject, unassigned

    def _sample_is_adequate(self):
        total, per_subject, _unassigned = self._sample_state()
        return (total >= e0_category_sheet.SAMPLE_FLOOR
                and all(per_subject[s] >= e0_category_sheet.PER_SUBJECT_FLOOR
                        for s in e0_category_sheet.SUBJECTS))

    @staticmethod
    def _build_open_look_input(record):
        """e0-open-look.md's Input block: question, answer taught, evidence lines, subject. NO
        codebook and NO allowed values, deliberately -- see the class docstring."""
        return {
            "question": _e_question_view(record),
            "answer_taught": _d_answer_taught(record),
            "evidence": _e_evidence_view(record),
            "subject": record.get("subject"),
        }

    def _open_look_outputs(self):
        """{qid: output} for every open-look call that has an output on disk."""
        out = {}
        for fn in _list_out_files(self.step):
            item_id, run_label = _parse_out_filename(fn)
            if run_label != "runA" or item_id.startswith("tag__"):
                continue
            out[item_id] = _read_json(_out_path(self.step, item_id, run_label))
        return out

    def _answers_for_tag(self, tag, sample):
        """The free answers this tag is grouped from: [{question_id, subject, year, text}].

        scripts/checks/E0.py treats a missing `answers` list as a HARD failure for the grouper
        branch, because the per-subject counts are the step's entire output and an unreconciled
        count could silently drop a real category's members."""
        field = self.TAG_SOURCE_FIELD[tag]
        answers = []
        for qid, data in sorted(self._open_look_outputs().items()):
            if qid not in sample or not isinstance(data, dict) or "error" in data:
                continue
            # Only a free answer that PASSED its own check is grouped. One that failed is data the
            # owner must not be shown (E0 has no safe default -- see check() below), and silently
            # grouping it would put a leaked category name or an answer-as-wrong-option into the
            # counts, which are this step's entire output.
            if not _d_step_resolved(self.step, qid, allow=("pass", "flagged")):
                continue
            value = data.get(field)
            if field == "wrong_options":
                if not isinstance(value, dict) or not value:
                    continue
                text = "; ".join(f"option {k}: {v}" for k, v in sorted(value.items()))
            else:
                text = str(value or "").strip()
            if not text:
                continue
            record = sample[qid]
            answers.append({"question_id": qid, "subject": record.get("subject"),
                             "year": record.get("year"), "text": text})
        return answers

    def _build_grouper_input(self, tag, sample):
        return {
            "tag": tag,
            "starting_list": _e_allowed(tag),
            "answers": self._answers_for_tag(tag, sample),
        }

    def list_items(self, filters):
        if not self._sample_is_adequate():
            return []
        sample = self._sample(filters)
        prompt_version = rc.get_prompt_version(self.step)
        lines = []

        # Phase 1: one e0-open-look call per question in the sample.
        for qid, record in sample.items():
            status = rc.read_item_status(self.step, qid)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, qid) or os.path.exists(_out_path(self.step, qid, "runA")):
                continue
            path = _e_write_agent_input(self.step, qid, "runA", self._build_open_look_input(record))
            lines.append(ListLine(qid, self.agent, _relpath(path),
                                    _relpath(_out_path(self.step, qid, "runA")), "runA"))
        if lines:
            return lines  # the grouper cannot run until every free answer exists

        # Phase 2: one e0-category-grouper call per tag, once phase 1 is complete.
        full_sample = self._sample()
        # Every question in the sample must have been ANSWERED AND CHECKED before the grouping
        # starts -- but a question whose own open-look output was blocked (a leaked category name,
        # or a question with no answer at all, so "the answer is not one of the wrong options"
        # cannot be checked) must not block the discovery forever. So the gate is "nothing is
        # still outstanding", and _answers_for_tag then groups only the answers that passed.
        if any(_d_fresh(self.step, qid) for qid in full_sample):
            return []
        for tag in sorted(self.TAG_SOURCE_FIELD):
            item_id = self._tag_item_id(tag)
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, item_id) or \
                    os.path.exists(_out_path(self.step, item_id, "runA")):
                continue
            path = _e_write_agent_input(self.step, item_id, "runA",
                                          self._build_grouper_input(tag, full_sample))
            lines.append(ListLine(item_id, self.grouper_agent, _relpath(path),
                                    _relpath(_out_path(self.step, item_id, "runA")), "runA"))
        return lines

    def list_reason(self):
        total, per_subject, unassigned = self._sample_state()
        if not self._sample_is_adequate():
            counts = ", ".join(f"{s} {per_subject[s]}" for s in e0_category_sheet.SUBJECTS)
            return (f"E0 is NOT dispatching: its sample is {total} D8-resolved canonical "
                    f"question(s) ({counts}"
                    + (f", no subject {unassigned}" if unassigned else "")
                    + f"), and spec 13/E0 asks for ~{e0_category_sheet.SAMPLE_FLOOR} across many "
                    f"chapters with ~{e0_category_sheet.PER_SUBJECT_FLOOR} per subject "
                    f"(scripts/e0_category_sheet.py's own documented floor). Grouping this few "
                    f"free answers would hand the owner counts of 1 and 2 against a taxonomy "
                    f"~500 real sampled questions already validated. Collect the sample first; "
                    f"`python3 scripts/e0_category_sheet.py --check` prints the same numbers.")
        return ("E0: every question in the sample already has an e0-open-look output and every "
                "tag already has an e0-category-grouper output (or one pending --check). Run "
                "`run_step.py E0 --auto` to export the category sheet.")

    def auto(self, filters):
        """Phase 3: scripts/e0_category_sheet.py, the one script in E0 and the only thing E0
        writes outside its own step directory. Invoked as a subprocess per scripts/CONVENTIONS.md
        (it really does write its own output file, unlike E1's and E6's pure script halves).

        It exits non-zero when the sample is below spec 13/E0's size or when no grouper output
        exists -- both of which are the honest state of this bank today, not a script failure, so
        they are reported rather than flagged (E0's only flag code is E0_FINDINGS_READY, and
        inventing a sample-size flag would be inventing a flag)."""
        script = rc.pp("scripts", "e0_category_sheet.py")
        if not os.path.exists(script):
            print(f"E0 --auto: {script} does not exist. Nothing to run.", file=sys.stderr)
            return
        started = rc.now_iso()
        result = subprocess.run([sys.executable, script], cwd=rc.pp())
        ended = rc.now_iso()
        prompt_version = rc.get_prompt_version(self.step)
        if result.returncode != 0:
            print(f"E0 --auto: e0_category_sheet.py exited {result.returncode} -- no sheet was "
                  f"written (see its own output above for why). Nothing is flagged: E0's only "
                  f"flag code is E0_FINDINGS_READY, raised when findings EXIST.", file=sys.stderr)
        rc.append_run_log("sheet", self.step, "script", None, prompt_version, started, ended,
                            "pass" if result.returncode == 0 else "fail",
                            f"e0_category_sheet.py exit {result.returncode}", None,
                            "pass" if result.returncode == 0 else "skipped")

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)
        sample = self._sample()
        sheet_path = rc.pp(*e0_category_sheet.SHEET_RELPATH.split(os.sep))

        for item_id, run_label in self._outstanding(filters):
            data = _read_json(_out_path(self.step, item_id, run_label))
            started = rc.now_iso()
            if item_id.startswith("tag__"):
                tag = item_id[len("tag__"):]
                input_data = {"tag": tag, "starting_list": list(_e_allowed(tag)),
                               "answers": self._answers_for_tag(tag, sample)}
            else:
                record = sample.get(item_id) or lib_records.read_record(item_id)
                input_data = {"record": record,
                               "answer": _d_answer_taught(record).get("number")}
            ok, msg = _e_check_one(self.step, item_id, data, input_data)
            ended = rc.now_iso()

            # E0's fallback chain is [] and its safe_default is null (config/steps.yaml): there is
            # no retry, no second opinion and nothing to fall back to, because a discovery that
            # failed its own check is not a value that can be defaulted -- it is data the owner
            # must not be shown. A failing E0 output is blocked (spec 5.5 rung 4).
            status = "pass" if ok else "blocked"
            if ok and item_id.startswith("tag__"):
                rc.raise_flag("tag", item_id, self.step, "E0_FINDINGS_READY",
                               flags_cat.get("E0_FINDINGS_READY", "normal"),
                               f"E0 findings for the {item_id[len('tag__'):]!r} tag are ready for "
                               f"the owner: {len(data.get('categories') or [])} category row(s), "
                               f"{len(data.get('unclear') or [])} unclear answer(s). E0 never "
                               f"writes codebook/E*.md -- these are data for the owner's own "
                               f"codebook decision (spec 13/E0).",
                               provisional_value={"tag": data.get("tag")},
                               evidence=[_relpath(sheet_path)] if os.path.exists(sheet_path) else None,
                               prompt_version=prompt_version)
            rc.write_item_status(self.step, item_id, status, prompt_version,
                                   extra={"run": run_label, "check_message": msg})
            rc.append_run_log(item_id, self.step, run_label,
                                self.grouper_agent if item_id.startswith("tag__") else self.agent,
                                prompt_version, started, ended, "pass" if ok else "fail", msg,
                                None, status)
        return self.list_items(filters)

    def _outstanding(self, filters):
        """[(item_id, run_label)] for every E0 output on disk whose item still needs resolving."""
        prompt_version = rc.get_prompt_version(self.step)
        out = []
        for item_id, runs in sorted(_outputs_by_item(self.step).items()):
            if not rc.item_passes_filters(item_id, filters):
                continue
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            if "runA" in runs:
                out.append((item_id, "runA"))
        return out


# ===========================================================================
# E1 - Question type (spec 13/E1; scripts/type_patterns.py + e1-type-tagger; codebook/E1.md)
# ===========================================================================

class E1Plugin:
    """SCRIPT FIRST, AGENT ONLY WHEN NO PATTERN DECIDES (spec 13/E1, verbatim), then 1 retry.

    The script half is scripts/type_patterns.py::classify(record) -> (value, rule), whose
    (None, reason) return is the DESIGNED trigger for an e1-type-tagger call and never a failure.
    On the real bank it decides 9 of the 10 canonical questions and hands exactly one
    (Q-000005, whose four options are each a reaction -- a shape no spec pattern covers) to the
    agent. Same shape as B7Plugin: the script resolves the majority inside check() with no agent
    dispatch at all, and --list only ever emits lines for what the script could not settle.

    WHY THE SCRIPT HALF RUNS IN-PROCESS, not as a `--auto` subprocess (judgement call, reported):
    scripts/CONVENTIONS.md's subprocess contract exists for script steps that WRITE their own
    output to a fixed path (its rule 3). type_patterns.py writes nothing -- it is a pure
    classifier with a reporting CLI -- so a subprocess per question would change no pipeline
    state while costing one process per question at full scale. The precedent for importing a
    step's own script instead is D10Plugin (build_groups.subtopics_with_work), D3Plugin
    (fetch_passages.fetch_for_item) and B9Plugin (recover_figures). `--auto` prints what the
    script decided and `--check` applies it through the same function, so the two cannot disagree.
    """
    step = "E1"
    agent = "e1-type-tagger"

    def _candidates(self, filters=None):
        return _e_candidates(self.step, filters)

    @staticmethod
    def _script_decision(record):
        return type_patterns.classify(record)

    def _build_agent_input(self, record):
        """e1-type-tagger.md's Input block: the question with its `structure` field, `codebook`
        (only when the file exists, spec 13.0) and `allowed` (the values with their one-line
        definitions). Factored out so the first dispatch and the retry build the same shape --
        see resolve_single_run_items' `agent_inputs` docstring for the real bug that caused."""
        payload = {
            "question": _e_question_view(record),
            "allowed": _e_allowed("question_type"),
        }
        text, _version = _e_codebook(self.step)
        if text is not None:
            payload["codebook"] = text
        return payload

    def list_items(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for qid, record in self._candidates(filters).items():
            status = rc.read_item_status(self.step, qid)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, qid) or os.path.exists(_out_path(self.step, qid, "runA")):
                continue
            value, _rule = self._script_decision(record)
            if value is not None:
                continue  # resolved SCRIPT-only inside check(); no agent line, by design
            path = _e_write_agent_input(self.step, qid, "runA", self._build_agent_input(record))
            lines.append(ListLine(qid, self.agent, _relpath(path),
                                    _relpath(_out_path(self.step, qid, "runA")), "runA"))
        return lines

    def list_reason(self):
        candidates = self._candidates()
        if not candidates:
            return ("E1 needs a resolved D7 (steps/D7/status/<QID>.json pass, flagged or "
                    "skipped). No question has one: D7 needs D6, and D6 is agent-driven "
                    "(d6-status-note-writer) and has never been dispatched, so nothing has "
                    "reached E1 yet. Nothing is fabricated to make it look otherwise.")
        undecided = [q for q, r in candidates.items() if self._script_decision(r)[0] is None]
        if not undecided:
            return (f"E1: scripts/type_patterns.py decides all {len(candidates)} ready "
                    f"question(s) by pattern, so no agent call is needed at all -- run "
                    f"`run_step.py E1 --check` (or --auto) to store those tags.")
        return ("E1: every question the patterns could not decide already has output pending "
                "--check.")

    def auto(self, filters):
        """The script half, reported. Writes nothing itself (--check is what stores the tags, via
        the same type_patterns.classify call), so a second --auto is a no-op by construction."""
        decided = handed_over = 0
        for qid, record in self._candidates(filters).items():
            value, rule = self._script_decision(record)
            print(f"E1 --auto: {qid} -> {value or 'NEEDS-AGENT'}  [{rule}]", file=sys.stderr)
            if value is None:
                handed_over += 1
            else:
                decided += 1
        print(f"E1 --auto: scripts/type_patterns.py decided {decided} question(s) by pattern; "
              f"{handed_over} need a real e1-type-tagger call (`--list`).", file=sys.stderr)

    def _resolve_by_script(self, qid, value, rule, prompt_version, cb_version):
        _e_set_tags(self.step, qid, {
            "question_type": value,
            "e1_question_type": value,
            "e1_new_description": "",
            "e1_confidence": "high",
            "e1_decided_by": f"script pattern {rule}",
        }, prompt_version, "pass", cb_version=cb_version)
        rc.write_item_status(self.step, qid, "pass", prompt_version,
                               extra={"run": "script", "check_message": f"pattern {rule}"})
        rc.append_run_log(qid, self.step, "script", None, prompt_version, rc.now_iso(),
                            rc.now_iso(), "pass", f"type_patterns.py pattern {rule} -> {value}",
                            None, "pass")

    def _failing_message(self, item_id, data):
        record = lib_records.read_record(item_id)
        ok, msg = _e_check_one(self.step, item_id, data, {"record": record})
        return msg if not ok else "the retry's own check passed but the item was not resolved"

    def _post_assembly(self, item_id, run_label, data, status, prompt_version, flags_cat,
                        cb_version):
        usable = isinstance(data, dict) and "error" not in data
        already_flagged = set()
        if status == "pass" and usable:
            value = data.get("question_type")
            description = (data.get("new_description") or "").strip()
            decided_by = f"agent {self.agent} ({run_label})"
        else:
            # Spec 13/E1's own fallback, verbatim: "new_type -> E_NEW_CATEGORY (normal) with the
            # description". Strictly better than a near value: a stretched value is invisible in
            # Stage F, a new_type is reviewed.
            value = "new_type"
            description = self._failing_message(item_id, data)
            decided_by = f"safe default after {run_label} (spec 13/E1 On failure)"
            # resolve_single_run_items already raised one flag per segment of that message, so a
            # message that CARRIED an E_NEW_CATEGORY segment has its flag; raising a second would
            # put the same item in Stage F's queue twice (lib/flags.py appends, never dedupes).
            already_flagged = {code for code, _detail
                                in rc.parse_check_message(get_cfg(self.step), description) if code}
        if value == "new_type" and "E_NEW_CATEGORY" not in already_flagged:
            rc.raise_flag("item", item_id, self.step, "E_NEW_CATEGORY",
                           flags_cat.get("E_NEW_CATEGORY", "normal"),
                           f"question_type new_type: {description}",
                           provisional_value={"question_type": value,
                                               "new_description": description,
                                               "agent_answer": data if usable else None},
                           evidence=[_relpath(_out_path(self.step, item_id, run_label))],
                           prompt_version=prompt_version)
        _e_set_tags(self.step, item_id, {
            "question_type": value,
            "e1_question_type": value,
            "e1_new_description": description,
            "e1_confidence": (data or {}).get("confidence") if usable else "low",
            "e1_decided_by": decided_by,
        }, prompt_version, status, cb_version=cb_version)

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)
        _text, cb_version = _e_codebook(self.step)
        items_with_builders, agent_inputs = {}, {}

        for qid, record in self._candidates(filters).items():
            if not _d_fresh(self.step, qid):
                continue
            value, rule = self._script_decision(record)
            if value is not None:
                self._resolve_by_script(qid, value, rule, prompt_version, cb_version)
                continue
            # The CHECK's context and the AGENT's input are different objects here (the check
            # re-runs type_patterns.classify on the real record; the agent never sees a record),
            # so `agent_inputs` is what the retry file must be built from -- the exact bug that
            # parameter exists for.
            items_with_builders[qid] = {"record": record}
            agent_inputs[qid] = self._build_agent_input(record)

        def _post(item_id, run_label, data, status):
            self._post_assembly(item_id, run_label, data, status, prompt_version, flags_cat,
                                 cb_version)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                          agent_inputs=agent_inputs)


# ===========================================================================
# E2 - Format (spec 13/E2; e2-format-tagger; codebook/E2.md) - retry THEN adjudicator
# ===========================================================================

class E2Plugin:
    """1 run, then RETRY, then ADJUDICATOR, then spec's own guard-value safe default.

    E2 is the only E step whose fallback chain has three rungs (config/steps.yaml
    `fallback: [retry, adjudicator]`, spec 13/E2 On failure: "guard fails -> retry with 'The stem
    contains <word>'; then adjudicator -> E2_NEGATIVE_GUARD (high)"), which is why this plugin
    drives the chain itself instead of delegating to resolve_single_run_items.

    THAT IS A DELIBERATE CHOICE, NOT AN OVERSIGHT. resolve_single_run_items implements exactly
    runA -> retry1 -> safe_default and has no adjudicator hop (A5Plugin.check's docstring records
    the same limitation from the other side). Handing E2 to it would resolve a twice-failed guard
    straight to the safe default and SKIP the adjudication spec names -- on the one check in
    Stage E that can force one. The retry rung below reproduces the resolver's semantics exactly
    (same pending marker, same `previous_attempt_failed` key, same run labels), and the
    adjudicator hop follows A4Plugin/D11Plugin's real "write an x-adjudicator work file now,
    apply its output on a later --check" shape.

    THE RETRY TEXT IS SPEC'S OWN SENTENCE. scripts/checks/E2.py puts "The stem contains <word>."
    at the head of every E2_NEGATIVE_GUARD segment precisely so the retry can forward it
    unchanged; _e_guard_segment does that rather than reconstructing the wording.
    """
    step = "E2"
    agent = "e2-format-tagger"

    #: config/steps.yaml E2 safe_default, verbatim: "with a negative word and single-item/
    #: statement options, `pick_incorrect`; with combination options,
    #: `pick_correct_combination`; with match-code options, `pick_match_code`."
    _GUARD_VALUE_FOR_FORM = {"combination_code": "pick_correct_combination",
                              "match_code": "pick_match_code"}

    def _candidates(self, filters=None):
        return _e_candidates(self.step, filters)

    @staticmethod
    def _negative_words(record):
        """B3's field under either name -- it writes `negative_words`, spec 13/E2 calls it
        `negative_words_seen` -- and it must be in the agent input even when EMPTY, because an
        empty value is itself one of the guard's three cases."""
        seen = record.get("negative_words")
        if seen is None:
            seen = record.get("negative_words_seen")
        return list(seen or [])

    def _build_agent_input(self, record):
        payload = {
            "question": _e_question_view(record),
            "negative_words_seen": self._negative_words(record),
            "allowed": _e_allowed("format"),
        }
        text, _version = _e_codebook(self.step)
        if text is not None:
            payload["codebook"] = text
        return payload

    def _check_context(self, record):
        return {"record": record, "negative_words_seen": self._negative_words(record)}

    @staticmethod
    def _negative_format():
        """The format E2's negative guard REQUIRES, read from scripts/checks/E2.py.

        Read rather than restated: this value was hardcoded here as `pick_incorrect` and again in
        the check, and when `pick_correct`/`pick_incorrect`/`identify_reaction_or_process_name`
        merged into `pick_correct_statement` in allowed_values v0.3, the plugin went on storing a
        retired label that the check and the schema would both have rejected."""
        import importlib
        import sys as _sys
        checks_dir = rc.pp("scripts", "checks")
        if checks_dir not in _sys.path:
            _sys.path.insert(0, checks_dir)
        return importlib.import_module("E2").NEGATIVE_FORMATS[0]

    def _guard_required_value(self, record):
        """The format the guard itself REQUIRES, or None when the guard dictates no single value.

        None is a real outcome, not a hole: a failure that is not the guard's at all (a
        `new_format` with no description, a low-confidence tag) has no guard value, and a
        failure that is not the guard's at all (a `new_format` with no description, a
        low-confidence tag) has no guard value either. Decided with E6's real, already-tested
        option-shape classifier (describe_tags.answer_form) rather than a third copy of it."""
        if not self._negative_words(record):
            return None
        form = describe_tags.answer_form(record)
        if form in self._GUARD_VALUE_FOR_FORM:
            return self._GUARD_VALUE_FOR_FORM[form]
        return self._negative_format()

    def list_items(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for qid, record in self._candidates(filters).items():
            status = rc.read_item_status(self.step, qid)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            if os.path.exists(_work_input_path(self.step, qid, "adjudicated")):
                continue  # the adjudicator owns this item now
            if rc.read_pending(self.step, qid) or os.path.exists(_out_path(self.step, qid, "runA")):
                continue
            path = _e_write_agent_input(self.step, qid, "runA", self._build_agent_input(record))
            lines.append(ListLine(qid, self.agent, _relpath(path),
                                    _relpath(_out_path(self.step, qid, "runA")), "runA"))
        return lines

    def list_reason(self):
        if not self._candidates():
            return ("E2 needs a resolved E1 (steps/E1/status/<QID>.json). None exists: E1 needs "
                    "D7, D7 needs D6, and D6 is agent-driven and has never run.")
        return "E2: every ready question already has output pending --check."

    def _start_adjudicator(self, qid, record, run_a, run_b, msg_a, msg_b, prompt_version):
        guard_value = self._guard_required_value(record)
        payload = {
            "step": "E2",
            "task": "e2-format-tagger answered this question's `format`, failed step E2's own "
                     "negative-word guard, was retried with the guard's complaint, and failed "
                     "again. Decide the correct format.",
            "allowed_values": {
                "choice": ["A", "B", "combined", "unsure"],
                "A": "the first answer (run A) is correct as-is",
                "B": "the retry's answer is correct as-is",
                "combined": "neither is right; value.format gives the correct format (one value "
                             "from the allowed list below)",
                "unsure": "cannot decide -- the script falls back to the guard's own required "
                           "value where the guard requires one, else keeps the agent's answer as "
                           "a provisional value; either way E2_NEGATIVE_GUARD (high) is raised",
            },
            "allowed": _e_allowed("format"),
            "evidence": {"question": _e_question_view(record),
                          "negative_words_seen": self._negative_words(record),
                          "answer_form": describe_tags.answer_form(record),
                          "guard_requires": guard_value},
            "run_a": {"format": (run_a or {}).get("format"),
                       "new_description": (run_a or {}).get("new_description"),
                       "confidence": (run_a or {}).get("confidence"),
                       "failed_check": msg_a},
            "run_b": {"format": (run_b or {}).get("format"),
                       "new_description": (run_b or {}).get("new_description"),
                       "confidence": (run_b or {}).get("confidence"),
                       "failed_check": msg_b},
            "failed_check": msg_b,
        }
        text, _version = _e_codebook(self.step)
        if text is not None:
            payload["codebook"] = text
        path = _e_write_agent_input(self.step, qid, "adjudicated", payload)
        rc.write_pending(self.step, qid, {"stage": "adjudicating", "reason": msg_b})
        return [ListLine(qid, "x-adjudicator", _relpath(path),
                           _relpath(_out_path(self.step, qid, "adjudicated")), "adjudicated")]

    def _resolve(self, qid, data, run_label, prompt_version, flags_cat, cb_version,
                  note, flag_guard=False, agent_answer=None):
        """Store one resolved E2 format.

        `flag_guard` raises E2_NEGATIVE_GUARD (high) and makes the item `flagged` rather than
        `pass`. It is set for every item that reached the ADJUDICATOR at all, not only for the
        safe default -- spec 13/E2's On-failure line attaches the flag to that rung ("then
        adjudicator -> E2_NEGATIVE_GUARD (high)"), and a format a human adjudicator had to settle
        is exactly the kind of tag a reviewer should see in the Stage F queue."""
        fmt = (data or {}).get("format")
        description = ((data or {}).get("new_description") or "").strip()
        status = "flagged" if flag_guard else "pass"
        if flag_guard:
            rc.raise_flag("item", qid, self.step, "E2_NEGATIVE_GUARD",
                           flags_cat.get("E2_NEGATIVE_GUARD", "high"), note,
                           provisional_value={"agent_answer": agent_answer, "stored_format": fmt},
                           evidence=[_relpath(_out_path(self.step, qid, run_label))],
                           prompt_version=prompt_version)
        if fmt == "new_format":
            rc.raise_flag("item", qid, self.step, "E_NEW_CATEGORY",
                           flags_cat.get("E_NEW_CATEGORY", "normal"),
                           f"format new_format: {description}",
                           provisional_value={"format": fmt, "new_description": description},
                           prompt_version=prompt_version)
        _e_set_tags(self.step, qid, {
            "format": fmt,
            "e2_format": fmt,
            "e2_new_description": description,
            "e2_confidence": (data or {}).get("confidence"),
            "e2_decided_by": note,
        }, prompt_version, status, cb_version=cb_version)
        rc.write_item_status(self.step, qid, status, prompt_version,
                               extra={"run": run_label, "check_message": note})
        return status

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)
        _text, cb_version = _e_codebook(self.step)
        new_lines = []

        for qid, record in self._candidates(filters).items():
            if not _d_fresh(self.step, qid):
                continue
            context = self._check_context(record)

            # ---- rung 3: an adjudication is in flight or answered -------------------------
            adj_work = _work_input_path(self.step, qid, "adjudicated")
            if os.path.exists(adj_work):
                adj_out = _out_path(self.step, qid, "adjudicated")
                if not os.path.exists(adj_out):
                    continue  # still waiting on the adjudicator
                adj = _read_json(adj_out)
                run_a = _read_json(_out_path(self.step, qid, "runA"))
                run_b = _read_json(_out_path(self.step, qid, "retry1")) \
                    if os.path.exists(_out_path(self.step, qid, "retry1")) else None
                choice = (adj or {}).get("choice")
                started = ended = rc.now_iso()
                chosen, note = None, ""
                if choice == "A":
                    chosen, note = run_a, "adjudicator chose the first answer"
                elif choice == "B":
                    chosen, note = run_b, "adjudicator chose the retry's answer"
                elif choice == "combined":
                    value = (adj or {}).get("value") or {}
                    candidate = dict(run_b or run_a or {})
                    candidate.update({k: v for k, v in value.items()
                                       if k in ("format", "new_description", "confidence")})
                    chosen, note = candidate, "adjudicator supplied the format"
                # The adjudicator never bypasses the guard: whatever it chose is re-checked.
                if chosen is not None:
                    ok_c, msg_c = _e_check_one(self.step, qid, chosen, context)
                    if not ok_c:
                        note = f"{note} but it still fails the guard ({msg_c})"
                        chosen = None
                if chosen is not None:
                    self._resolve(qid, chosen, "adjudicated", prompt_version, flags_cat,
                                   cb_version, note=note, flag_guard=True,
                                   agent_answer=run_b or run_a)
                    rc.append_run_log(qid, self.step, "adjudicated", "x-adjudicator",
                                        prompt_version, started, ended, "pass", note, None,
                                        "flagged")
                    continue
                # Rung 4: config/steps.yaml's documented safe default.
                guard_value = self._guard_required_value(record)
                agent_answer = run_b or run_a
                if guard_value is not None:
                    stored = dict(agent_answer or {})
                    stored["format"] = guard_value
                    detail = (f"adjudicator {choice or 'unsure'}: {note or 'no usable verdict'}. "
                               f"Took the guard's own required value {guard_value!r}; the agent's "
                               f"answer {(agent_answer or {}).get('format')!r} is kept as the "
                               f"provisional value so Stage F sees both (spec 13/E2 On failure).")
                    self._resolve(qid, stored, "adjudicated", prompt_version, flags_cat,
                                   cb_version, note=detail, flag_guard=True,
                                   agent_answer=agent_answer)
                else:
                    detail = (f"adjudicator {choice or 'unsure'}: {note or 'no usable verdict'}. "
                               f"The guard requires no single value here (it rules `pick_incorrect` "
                               f"OUT rather than ruling one IN, or the failure was not the "
                               f"guard's), so the agent's own answer is kept and flagged for "
                               f"Stage F rather than replaced by a guess.")
                    self._resolve(qid, agent_answer, "adjudicated", prompt_version,
                                   flags_cat, cb_version, note=detail, flag_guard=True,
                                   agent_answer=agent_answer)
                rc.append_run_log(qid, self.step, "adjudicated", "x-adjudicator", prompt_version,
                                    started, ended, "fail", detail, None, "flagged")
                continue

            # ---- rung 1/2: runA, then one retry -------------------------------------------
            run_a_path = _out_path(self.step, qid, "runA")
            if not os.path.exists(run_a_path):
                continue  # nothing written yet; --list dispatches it
            retry_path = _out_path(self.step, qid, "retry1")
            run_label = "retry1" if os.path.exists(retry_path) else "runA"
            data = _read_json(_out_path(self.step, qid, run_label))
            started = rc.now_iso()
            ok, msg = _e_check_one(self.step, qid, data, context)
            ended = rc.now_iso()

            if ok:
                self._resolve(qid, data, run_label, prompt_version, flags_cat, cb_version,
                               note=f"{run_label}: {msg}")
                rc.append_run_log(qid, self.step, run_label, self.agent, prompt_version, started,
                                    ended, "pass", msg, "runA" if run_label == "retry1" else None,
                                    "pass")
                continue

            if run_label == "runA":
                rc.append_run_log(qid, self.step, "runA", self.agent, prompt_version, started,
                                    ended, "fail", msg, None, "pending")
                rc.write_pending(self.step, qid, {"reason": msg, "next_run": "retry1"})
                retry_input = self._build_agent_input(record)
                retry_input["previous_attempt_failed"] = _e_guard_segment(
                    cfg, msg, "E2_NEGATIVE_GUARD")
                path = _e_write_agent_input(self.step, qid, "retry1", retry_input)
                new_lines.append(ListLine(qid, self.agent, _relpath(path),
                                            _relpath(retry_path), "retry1"))
                continue

            # retry also failed -> the adjudicator rung spec names.
            data_a = _read_json(run_a_path)
            _ok_a, msg_a = _e_check_one(self.step, qid, data_a, context)
            rc.append_run_log(qid, self.step, "retry1", self.agent, prompt_version, started, ended,
                                "fail", msg, "runA", "pending")
            new_lines.extend(self._start_adjudicator(qid, record, data_a, data, msg_a, msg,
                                                       prompt_version))
        return new_lines


# ===========================================================================
# E3 - Content shape (spec 13/E3; e3-shape-tagger; codebook/E3.md)
# ===========================================================================

class E3Plugin:
    """1 run + retry, driven by the generic retry resolver (config/steps.yaml
    `fallback: [retry]`, so resolve_single_run_items' runA -> retry1 -> safe_default chain is
    exactly E3's chain).

    E3 judges the NCERT MATERIAL behind the answer, read through D4's evidence lines AND THEIR
    PASSAGE KINDS -- so the agent input carries _e_evidence_view(), which looks each kind up in
    the real ncert/passages/<BOOK>.jsonl rather than flattening the lines to bare quotes.

    TWO THINGS THAT ARE FLAGS, NEVER CHECK FAILURES, and are raised here from the RESOLVED VALUE
    rather than by parsing a passing check's message (the precedent is D4Plugin's unconditional
    outcome flags):
      * `confidence: medium` -> E3_MEDIUM (low). codebook/E3.md section 4 tells the agent to use
        medium whenever no evidence was available, and no evidence is the NORMAL state today
        (Stage A has indexed 2 of 13 Biology chapters and zero Physics/Chemistry), so failing it
        would retry every honest tag in the bank and then blame the agent for the pipeline's gap.
      * `new_shape` -> E_NEW_CATEGORY (normal), carrying the description.
    """
    step = "E3"
    agent = "e3-shape-tagger"

    def _candidates(self, filters=None):
        return _e_candidates(self.step, filters)

    def _build_agent_input(self, record):
        payload = {
            "question": _e_question_view(record),
            "evidence": _e_evidence_view(record),
            "allowed": _e_allowed("content_shape"),
        }
        text, _version = _e_codebook(self.step)
        if text is not None:
            payload["codebook"] = text
        return payload

    @staticmethod
    def _check_context(record):
        # `evidence` is passed even when empty -- scripts/checks/E3.py's rule that
        # `current_affairs` must not stand in for MISSING evidence depends on the key existing.
        return {"record": record, "evidence": _e_evidence_view(record)}

    def list_items(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for qid, record in self._candidates(filters).items():
            status = rc.read_item_status(self.step, qid)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, qid) or os.path.exists(_out_path(self.step, qid, "runA")):
                continue
            path = _e_write_agent_input(self.step, qid, "runA", self._build_agent_input(record))
            lines.append(ListLine(qid, self.agent, _relpath(path),
                                    _relpath(_out_path(self.step, qid, "runA")), "runA"))
        return lines

    def list_reason(self):
        if not self._candidates():
            return ("E3 needs a resolved E2 (steps/E2/status/<QID>.json). None exists: the E "
                    "chain starts at E1, which needs D7, which needs the agent-driven D6.")
        return "E3: every ready question already has output pending --check."

    def _failing_message(self, item_id, data):
        record = lib_records.read_record(item_id)
        ok, msg = _e_check_one(self.step, item_id, data, self._check_context(record))
        return msg if not ok else "the retry's own check passed but the item was not resolved"

    def _post_assembly(self, item_id, run_label, data, status, prompt_version, flags_cat,
                        cb_version):
        usable = isinstance(data, dict) and "error" not in data
        already_flagged = set()
        if status == "pass" and usable:
            shape = data.get("content_shape")
            why = (data.get("why") or "").strip()
            description = (data.get("new_description") or "").strip()
            confidence = data.get("confidence")
            decided_by = f"agent {self.agent} ({run_label})"
        else:
            # config/steps.yaml E3 safe_default: "retry exhausted -> new_shape with the failing
            # check's message as new_description, E_NEW_CATEGORY (normal), same reasoning as E1."
            shape = "new_shape"
            description = self._failing_message(item_id, data)
            why = (data or {}).get("why") or ""
            confidence = "low"
            decided_by = f"safe default after {run_label} (config/steps.yaml E3 safe_default)"
            already_flagged = {code for code, _detail
                                in rc.parse_check_message(get_cfg(self.step), description) if code}

        if shape == "new_shape" and "E_NEW_CATEGORY" not in already_flagged:
            rc.raise_flag("item", item_id, self.step, "E_NEW_CATEGORY",
                           flags_cat.get("E_NEW_CATEGORY", "normal"),
                           f"content_shape new_shape: {description}",
                           provisional_value={"content_shape": shape, "new_description": description,
                                               "agent_answer": data if usable else None},
                           prompt_version=prompt_version)
        if confidence == "medium":
            rc.raise_flag("item", item_id, self.step, "E3_MEDIUM",
                           flags_cat.get("E3_MEDIUM", "low"),
                           f"content_shape {shape!r} tagged with medium confidence: {why}",
                           provisional_value={"content_shape": shape},
                           prompt_version=prompt_version)
        _e_set_tags(self.step, item_id, {
            "content_shape": shape,
            "e3_content_shape": shape,
            "e3_why": why,
            "e3_new_description": description,
            "e3_confidence": confidence,
            "e3_decided_by": decided_by,
        }, prompt_version, status, cb_version=cb_version)

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)
        _text, cb_version = _e_codebook(self.step)
        items_with_builders, agent_inputs = {}, {}
        for qid, record in self._candidates(filters).items():
            items_with_builders[qid] = self._check_context(record)
            agent_inputs[qid] = self._build_agent_input(record)

        def _post(item_id, run_label, data, status):
            self._post_assembly(item_id, run_label, data, status, prompt_version, flags_cat,
                                 cb_version)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                          agent_inputs=agent_inputs)


# ===========================================================================
# E4 - Thinking (spec 13/E4; e4-thinking-tagger; codebook/E4.md) - 2 runs + adjudicator
# ===========================================================================

class E4Plugin:
    """2 runs + adjudicator, following A4Plugin/D11Plugin's real two-run-plus-adjudicator shape.

    THE BRANCH IS IN THE AGENT INPUT, ALWAYS, EVEN AS null. codebook/E4.md section 1 is Stage E's
    most-confirmed rule (10 of 10 real papers, no exceptions): a Chemistry expectation must be
    conditioned on B7's BRANCH and never on the word "Chemistry", because physical chemistry
    behaves numerically like Physics while organic and inorganic behave descriptively like
    Biology. scripts/checks/E4.py FAILS any item whose `context["input_data"]` has no `branch`
    key -- present even when its value is None -- precisely so a branch-blind wiring is
    impossible rather than merely discouraged. _build_agent_input() and _check_context() both put
    the key in unconditionally; nothing here omits it for a Physics record, it passes None.

    AGREEMENT IS ON THE PRIMARY AND ON WHETHER A SECONDARY EXISTS -- not on which secondary it
    is (spec 13/E4 Checks). So {numerical, diagram_graph} and {numerical, reasoning} AGREE, while
    {numerical, null} and {numerical, reasoning} DISAGREE. That asymmetry is the rule, not a
    simplification of it.

    codebook_version REACHES THE AGENT (E4's own `input_fields` lists it, because spec 13/E4 puts
    it in the agent's OUTPUT and the agent has to be told what to echo) and is recorded on the
    record. scripts/checks/E4.py recomputes the real hash and fails a "none" claimed while
    codebook/E4.md exists -- the one wiring failure that would otherwise satisfy every enum in
    total silence while mis-tagging the bank at volume.
    """
    step = "E4"
    agent = "e4-thinking-tagger"

    def _candidates(self, filters=None):
        return _e_candidates(self.step, filters)

    def _build_agent_input(self, record):
        text, version = _e_codebook(self.step)
        payload = {
            "question": _e_question_view(record),
            "answer_taught": _d_answer_taught(record),
            "evidence": _e_evidence_view(record),
            "subject": record.get("subject"),
            # NEVER omit this key, and never substitute "none" for null here: the agent is told
            # the record's own value, and schemas/E4.json's `branch_used` is what it must echo.
            "branch": record.get("branch"),
            "codebook_version": version,
        }
        if text is not None:
            payload["codebook"] = text
        return payload

    @staticmethod
    def _check_context(record):
        return {"record": record, "subject": record.get("subject"),
                 "branch": record.get("branch")}

    @staticmethod
    def _canonical(data):
        """What "the two runs agree" means for E4: the primary, and whether a secondary exists."""
        return ((data or {}).get("primary"), (data or {}).get("secondary") is not None)

    def list_items(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for qid, record in self._candidates(filters).items():
            status = rc.read_item_status(self.step, qid)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            if os.path.exists(_work_input_path(self.step, qid, "adjudicated")):
                continue
            for run_label in ("runA", "runB"):
                if rc.read_pending(self.step, qid) or \
                        os.path.exists(_out_path(self.step, qid, run_label)):
                    continue
                path = _e_write_agent_input(self.step, qid, run_label,
                                              self._build_agent_input(record))
                lines.append(ListLine(qid, self.agent, _relpath(path),
                                        _relpath(_out_path(self.step, qid, run_label)), run_label))
        return lines

    def list_reason(self):
        if not self._candidates():
            return ("E4 needs a resolved E3 (steps/E3/status/<QID>.json). None exists: the E "
                    "chain starts at E1, which needs D7, which needs the agent-driven D6.")
        return ("E4: every ready question already has runA+runB output (or is awaiting its "
                "adjudicator) -- nothing fresh to list.")

    def _start_adjudicator(self, qid, record, data_a, data_b, failed, prompt_version):
        text, version = _e_codebook(self.step)
        payload = {
            "step": "E4",
            "task": "Run A and run B each independently decided which KIND of thinking this "
                     "question tests. They disagree on the primary, or on whether a secondary "
                     "exists, or one of them is not usable. Decide the correct verdict.",
            "allowed_values": {
                "choice": ["A", "B", "combined", "unsure"],
                "A": "run A's verdict is correct as-is",
                "B": "run B's verdict is correct as-is",
                "combined": "neither alone is right; value gives the correct {primary, secondary, "
                             "why, confidence, codebook_version, branch_used} in the runs' own shape",
                "unsure": "cannot decide -- the script falls back to run A's primary with "
                           "secondary null, E4_ADJUDICATED (normal), both runs kept as "
                           "provisional values",
            },
            "allowed": _e_allowed("thinking"),
            "evidence": {"question": _e_question_view(record),
                          "answer_taught": _d_answer_taught(record),
                          "evidence": _e_evidence_view(record),
                          "subject": record.get("subject"),
                          "branch": record.get("branch")},
            "run_a": {k: (data_a or {}).get(k) for k in
                       ("primary", "secondary", "why", "confidence", "branch_used")},
            "run_b": {k: (data_b or {}).get(k) for k in
                       ("primary", "secondary", "why", "confidence", "branch_used")},
            "codebook_version": version,
            "failed_check": failed,
            # codebook/E4.md section 4, restated for the adjudicator because it is the single
            # easiest rule to break here: never merge two primaries, and never promote a secondary
            # to break a tie -- a secondary is a second KIND of thinking, not a hedge between two
            # readings of the primary.
            "never": ("Never merge two primaries into one answer and never promote a secondary to "
                       "break a tie. If the two runs are really two readings of one primary, pick "
                       "one and set confidence accordingly."),
        }
        if text is not None:
            payload["codebook"] = text
        path = _e_write_agent_input(self.step, qid, "adjudicated", payload)
        rc.write_pending(self.step, qid, {"stage": "adjudicating", "reason": failed})
        return [ListLine(qid, "x-adjudicator", _relpath(path),
                           _relpath(_out_path(self.step, qid, "adjudicated")), "adjudicated")]

    def _apply(self, qid, data, run_label, prompt_version, flags_cat, cb_version, status, note,
                provisional=None):
        primary = (data or {}).get("primary")
        secondary = (data or {}).get("secondary")
        why = ((data or {}).get("why") or "").strip()
        if status != "pass":
            rc.raise_flag("item", qid, self.step, "E4_ADJUDICATED",
                           flags_cat.get("E4_ADJUDICATED", "normal"), note,
                           provisional_value=provisional,
                           evidence=[_relpath(_out_path(self.step, qid, run_label))],
                           prompt_version=prompt_version)
        # Spec 13.0 / spec 16: raised on EVERY E4 output while codebook/E4.md does not exist, and
        # raised from the real hash rather than from a parsed check message -- so if it keeps
        # appearing after config/steps.yaml declares the file, the codebook is still not reaching
        # the agent.
        if cb_version == codebook_version.NONE:
            rc.raise_flag("item", qid, self.step, "E4_NO_CODEBOOK",
                           flags_cat.get("E4_NO_CODEBOOK", "low"),
                           "no codebook reached this tag (config/steps.yaml declares none for E4, "
                           "or the declared file is absent), so it was made from the eight draft "
                           "thinking categories only (spec 13.0/17.5)",
                           provisional_value={"category_primary": primary},
                           prompt_version=prompt_version)
        _e_set_tags(self.step, qid, {
            "category_primary": primary,
            "category_secondary": secondary,
            "category_why": why,
            "e4_primary": primary,
            "e4_secondary": secondary,
            "e4_why": why,
            "e4_confidence": (data or {}).get("confidence"),
            "e4_branch_used": (data or {}).get("branch_used"),
            "e4_decided_by": note,
        }, prompt_version, status, cb_version=cb_version)
        rc.write_item_status(self.step, qid, status, prompt_version,
                               extra={"run": run_label, "check_message": note})

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)
        _text, cb_version = _e_codebook(self.step)
        new_lines = []

        for qid, record in self._candidates(filters).items():
            if not _d_fresh(self.step, qid):
                continue
            context = self._check_context(record)

            adj_work = _work_input_path(self.step, qid, "adjudicated")
            if os.path.exists(adj_work):
                adj_out = _out_path(self.step, qid, "adjudicated")
                if not os.path.exists(adj_out):
                    continue
                adj = _read_json(adj_out)
                data_a = _read_json(_out_path(self.step, qid, "runA"))
                data_b = _read_json(_out_path(self.step, qid, "runB"))
                choice = (adj or {}).get("choice")
                started = ended = rc.now_iso()
                verdict, note = None, ""
                if choice == "A":
                    verdict, note = data_a, "adjudicator chose run A"
                elif choice == "B":
                    verdict, note = data_b, "adjudicator chose run B"
                elif choice == "combined":
                    value = (adj or {}).get("value") or {}
                    ok_c, msg_c = _e_check_one(self.step, qid, value, context)
                    if ok_c:
                        verdict, note = value, "adjudicator supplied the verdict"
                    else:
                        note = f"adjudicator 'combined' value invalid ({msg_c})"
                if verdict is None:
                    # config/steps.yaml E4 safe_default: run A's primary with secondary null.
                    # NEVER a merge of two primaries and never a promoted secondary.
                    verdict = dict(data_a if isinstance(data_a, dict) else {})
                    verdict["secondary"] = None
                    note = ((note + "; ") if note else "") + \
                        (f"adjudicator {choice or 'unsure'} -- used run A's primary "
                         f"{verdict.get('primary')!r} with secondary null (spec 13/E4 safe "
                         f"default); both runs kept as provisional values")
                self._apply(qid, verdict, "adjudicated", prompt_version, flags_cat, cb_version,
                             "flagged", note,
                             provisional={"run_a": data_a, "run_b": data_b, "choice": choice})
                rc.append_run_log(qid, self.step, "adjudicated", "x-adjudicator", prompt_version,
                                    started, ended, "pass", note, None, "flagged")
                continue

            path_a = _out_path(self.step, qid, "runA")
            path_b = _out_path(self.step, qid, "runB")
            if not (os.path.exists(path_a) and os.path.exists(path_b)):
                continue  # still waiting on one of the two runs
            data_a, data_b = _read_json(path_a), _read_json(path_b)
            ok_a, msg_a = _e_check_one(self.step, qid, data_a, context)
            ok_b, msg_b = _e_check_one(self.step, qid, data_b, context)
            started = ended = rc.now_iso()

            if ok_a and ok_b and self._canonical(data_a) == self._canonical(data_b):
                self._apply(qid, data_a, "runA", prompt_version, flags_cat, cb_version, "pass",
                             "runs agree on the primary and on whether a secondary exists")
                rc.append_run_log(qid, self.step, "runA+runB", self.agent, prompt_version, started,
                                    ended, "pass", "runs agree", None, "pass")
                continue

            parts = [f"runA: {'ok' if ok_a else msg_a}", f"runB: {'ok' if ok_b else msg_b}"]
            if self._canonical(data_a) != self._canonical(data_b):
                parts.append(
                    f"the runs disagree on (primary, has a secondary): "
                    f"A={self._canonical(data_a)} B={self._canonical(data_b)} -- agreement is on "
                    f"the primary and on WHETHER a secondary exists, never on which one it is")
            failed = "; ".join(parts)
            rc.append_run_log(qid, self.step, "runA+runB", self.agent, prompt_version, started,
                                ended, "pass", f"{failed} -> adjudicator", None, "pending")
            new_lines.extend(self._start_adjudicator(qid, record, data_a, data_b, failed,
                                                       prompt_version))
        return new_lines


# ===========================================================================
# E5 - Traps (spec 13/E5; e5-trap-tagger; codebook/E5.md) - 2 runs + adjudicator,
#      ITEM = ONE WRONG OPTION
# ===========================================================================

class E5Plugin:
    """THE ITEM IS ONE WRONG OPTION OF ONE QUESTION, not one question -- normally three items per
    question, item id `<QID>#opt<N>` (schemas/E5.json and scripts/checks/E5.py both already
    assume it; the check also accepts the shorter `<QID>#<N>`). Three wrong options of one real
    question routinely carry three DIFFERENT traps, and that difference is the whole point of the
    tag: it is what lets a generated practice test reproduce a real paper's distractor profile.

    HOW MANY ITEMS EXIST (config/steps.yaml E5 safe_default + codebook/E5.md section 1): three is
    the normal case, NOT a quota. One item per option that is not the answer students are taught,
    where that answer is, in spec 12's own order, D7's `latest_answer`, else B8's
    `corrected_answer`, else the official key -- and the official key is COMMA-JOINED for a
    `multiple_accepted` question ("1,3"), which is exactly how a question with fewer than three
    genuinely wrong options arises. A `bonus`/`dropped` question has an empty official answer, so
    unless B8 produced a `corrected_answer` there is NO answer to subtract and therefore NO E5
    item at all; real Q-000004 is `dropped` WITH a corrected_answer of 1 and is the live case for
    that branch. Nothing here ever invents a third wrong option to reach three.

    A question with no identifiable wrong option gets a question-level `skipped` status (item id
    `<QID>`, which cannot collide with `<QID>#opt<N>`) so the record shows E5 considered it and
    excluded it, rather than the question silently never appearing.

    2 runs + adjudicator per option, agreeing on the TRAP for that one option.
    """
    step = "E5"
    agent = "e5-trap-tagger"

    @staticmethod
    def _item_id(qid, number):
        return f"{qid}#opt{number}"

    def _candidates(self, filters=None):
        # The FILTER is applied to the per-option item ids, not here: `--items Q-000015` must
        # reach Q-000015#opt1..#opt4 (rc.item_passes_filters is a substring match, so it does).
        return _e_candidates(self.step)

    @staticmethod
    def _options(record):
        return record.get("corrected_options") or record.get("options_en") or {}

    @staticmethod
    def _answers_taught(record):
        """The SET of option numbers students are taught, in spec 12's order. A `multiple_accepted`
        question's official key is comma-joined (B5Plugin writes it that way, and
        scripts/checks/B6.py splits it the same way), so this returns more than one number for
        exactly those questions. Empty when the question has no answer at all -- a bonus/dropped
        question B8 could not correct, which therefore has no identifiable wrong option either."""
        for field in ("latest_answer", "corrected_answer", "official_answer"):
            raw = record.get(field)
            if raw is None or str(raw).strip() in ("", "unsure"):
                continue
            return {part.strip() for part in str(raw).split(",") if part.strip()}
        return set()

    def _wrong_options(self, record):
        """[(number, text)] for every option that is not an answer students are taught."""
        answers = self._answers_taught(record)
        if not answers:
            return []
        options = self._options(record)
        return [(number, options.get(number))
                for number in sorted(options, key=lambda k: str(k))
                if str(number) not in answers]

    def _build_agent_input(self, record, number, text_value):
        payload = {
            "question": _e_question_view(record),
            "answer_taught": _d_answer_taught(record),
            "wrong_option": {"number": str(number), "text": text_value},
            "evidence": _e_evidence_view(record),
            # The A9 change-log entries on this question's evidence passages -- the HARD
            # precondition for the `old_ncert_fact` trap (codebook/E5.md section 4), which
            # scripts/checks/E5.py fails when this list is empty. ncert/change_log.csv holds only
            # its header row today, so the list is honestly [] for every real question.
            "change_log_entries": list(D7Plugin._change_entries_for(record).values()),
            "allowed": _e_allowed("trap"),
        }
        cb_text, _version = _e_codebook(self.step)
        if cb_text is not None:
            payload["codebook"] = cb_text
        return payload

    def _check_context(self, record, number, text_value):
        return {"record": record,
                 "wrong_option": {"number": str(number), "text": text_value},
                 "change_log_entries": list(D7Plugin._change_entries_for(record).values())}

    def _items(self, filters):
        """[(item_id, qid, record, number, text)] for every E5 item in scope."""
        out = []
        for qid, record in self._candidates().items():
            for number, text_value in self._wrong_options(record):
                item_id = self._item_id(qid, number)
                if not rc.item_passes_filters(item_id, filters):
                    continue
                out.append((item_id, qid, record, number, text_value))
        return out

    def list_items(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for item_id, _qid, record, number, text_value in self._items(filters):
            status = rc.read_item_status(self.step, item_id)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            if os.path.exists(_work_input_path(self.step, item_id, "adjudicated")):
                continue
            for run_label in ("runA", "runB"):
                if rc.read_pending(self.step, item_id) or \
                        os.path.exists(_out_path(self.step, item_id, run_label)):
                    continue
                path = _e_write_agent_input(self.step, item_id, run_label,
                                              self._build_agent_input(record, number, text_value))
                lines.append(ListLine(item_id, self.agent, _relpath(path),
                                        _relpath(_out_path(self.step, item_id, run_label)),
                                        run_label))
        return lines

    def list_reason(self):
        candidates = self._candidates()
        if not candidates:
            return ("E5 needs a resolved E4 (steps/E4/status/<QID>.json). None exists: the E "
                    "chain starts at E1, which needs D7, which needs the agent-driven D6.")
        no_items = [q for q, r in candidates.items() if not self._wrong_options(r)]
        if len(no_items) == len(candidates):
            return (f"E5: all {len(candidates)} ready question(s) have no identifiable wrong "
                    f"option (a bonus/dropped question with no B8 corrected_answer has no answer "
                    f"to subtract), so there is no E5 item to tag. They are recorded `skipped` by "
                    f"--check rather than left silent.")
        return ("E5: every wrong option of every ready question already has runA+runB output (or "
                "is awaiting its adjudicator).")

    def _start_adjudicator(self, item_id, record, number, text_value, data_a, data_b, failed,
                            prompt_version):
        payload = {
            "step": "E5",
            "task": "Run A and run B each independently decided WHY this one wrong option "
                     "attracts a prepared student. They disagree, or one of them is not usable. "
                     "Decide the correct trap for this option.",
            "allowed_values": {
                "choice": ["A", "B", "combined", "unsure"],
                "A": "run A's trap is correct as-is",
                "B": "run B's trap is correct as-is",
                "combined": "neither is right; value gives the correct {option, trap, why, "
                             "new_description, confidence} in the runs' own shape",
                "unsure": "cannot decide -- the script falls back to run A's trap, "
                           "E5_ADJUDICATED (normal), both kept as provisional values",
            },
            "allowed": _e_allowed("trap"),
            "evidence": {"question": _e_question_view(record),
                          "answer_taught": _d_answer_taught(record),
                          "wrong_option": {"number": str(number), "text": text_value},
                          "evidence": _e_evidence_view(record),
                          "change_log_entries":
                              list(D7Plugin._change_entries_for(record).values())},
            "run_a": {k: (data_a or {}).get(k) for k in
                       ("option", "trap", "why", "new_description", "confidence")},
            "run_b": {k: (data_b or {}).get(k) for k in
                       ("option", "trap", "why", "new_description", "confidence")},
            "failed_check": failed,
        }
        cb_text, _version = _e_codebook(self.step)
        if cb_text is not None:
            payload["codebook"] = cb_text
        path = _e_write_agent_input(self.step, item_id, "adjudicated", payload)
        rc.write_pending(self.step, item_id, {"stage": "adjudicating", "reason": failed})
        return [ListLine(item_id, "x-adjudicator", _relpath(path),
                           _relpath(_out_path(self.step, item_id, "adjudicated")), "adjudicated")]

    def _merge_option_trap(self, qid, number, entry, prompt_version, status, cb_version):
        """Merge ONE option's resolved trap into the question record's `option_traps` (the field
        name export_tables.TAG_COLUMNS and build_review_pack.FIELD_FOR_STEP use for E5), keyed by
        option number so a re-resolution replaces that option's row and leaves the others alone."""
        existing = lib_records.read_record(qid).get("option_traps")
        rows = [r for r in (existing or []) if isinstance(r, dict)
                and str(r.get("option")) != str(number)]
        rows.append(entry)
        rows.sort(key=lambda r: str(r.get("option")))
        _e_set_tags(self.step, qid, {"option_traps": rows, "e5_option_traps": rows},
                     prompt_version, status, cb_version=cb_version)

    def _apply(self, item_id, qid, number, data, run_label, prompt_version, flags_cat, cb_version,
                status, note, provisional=None):
        trap = (data or {}).get("trap")
        why = ((data or {}).get("why") or "").strip()
        description = ((data or {}).get("new_description") or "").strip()
        if status != "pass":
            rc.raise_flag("item", item_id, self.step, "E5_ADJUDICATED",
                           flags_cat.get("E5_ADJUDICATED", "normal"), note,
                           provisional_value=provisional,
                           evidence=[_relpath(_out_path(self.step, item_id, run_label))],
                           prompt_version=prompt_version)
        if trap == "new_trap":
            rc.raise_flag("item", item_id, self.step, "E_NEW_CATEGORY",
                           flags_cat.get("E_NEW_CATEGORY", "normal"),
                           f"trap new_trap on option {number}: {description}",
                           provisional_value={"trap": trap, "new_description": description},
                           prompt_version=prompt_version)
        self._merge_option_trap(qid, number, {
            "option": str(number), "trap": trap, "why": why,
            "new_description": description,
            "confidence": (data or {}).get("confidence"),
            "decided_by": note,
        }, prompt_version, status, cb_version)
        rc.write_item_status(self.step, item_id, status, prompt_version,
                               extra={"run": run_label, "check_message": note})

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)
        _text, cb_version = _e_codebook(self.step)
        new_lines = []

        # Questions with no identifiable wrong option: recorded `skipped` at question level.
        for qid, record in self._candidates().items():
            if self._wrong_options(record):
                continue
            if not rc.item_passes_filters(qid, filters) or not _d_fresh(self.step, qid):
                continue
            answers = self._answers_taught(record)
            note = (f"no identifiable wrong option: official_status {record.get('status')!r}, "
                    f"answer(s) taught {sorted(answers) or 'none'} -- "
                    + ("a bonus/dropped question with no B8 corrected_answer has no answer to "
                       "subtract, so E5 creates no item for it and invents nothing"
                       if not answers else "every option is an accepted answer"))
            _e_set_tags(self.step, qid, {"option_traps": [], "e5_note": note},
                         prompt_version, "skipped", cb_version=cb_version)
            rc.write_item_status(self.step, qid, "skipped", prompt_version,
                                   extra={"run": "script", "check_message": note})
            rc.append_run_log(qid, self.step, "script", None, prompt_version, rc.now_iso(),
                                rc.now_iso(), "pass", note, None, "skipped")

        for item_id, qid, record, number, text_value in self._items(filters):
            if not _d_fresh(self.step, item_id):
                continue
            context = self._check_context(record, number, text_value)

            adj_work = _work_input_path(self.step, item_id, "adjudicated")
            if os.path.exists(adj_work):
                adj_out = _out_path(self.step, item_id, "adjudicated")
                if not os.path.exists(adj_out):
                    continue
                adj = _read_json(adj_out)
                data_a = _read_json(_out_path(self.step, item_id, "runA"))
                data_b = _read_json(_out_path(self.step, item_id, "runB"))
                choice = (adj or {}).get("choice")
                started = ended = rc.now_iso()
                verdict, note = None, ""
                if choice == "A":
                    verdict, note = data_a, "adjudicator chose run A"
                elif choice == "B":
                    verdict, note = data_b, "adjudicator chose run B"
                elif choice == "combined":
                    value = (adj or {}).get("value") or {}
                    ok_c, msg_c = _e_check_one(self.step, item_id, value, context)
                    if ok_c:
                        verdict, note = value, "adjudicator supplied the trap"
                    else:
                        note = f"adjudicator 'combined' value invalid ({msg_c})"
                if verdict is None:
                    verdict = data_a
                    note = ((note + "; ") if note else "") + \
                        (f"adjudicator {choice or 'unsure'} -- used run A's trap "
                         f"{(data_a or {}).get('trap')!r} (config/steps.yaml E5 safe default); "
                         f"both runs kept as provisional values")
                self._apply(item_id, qid, number, verdict, "adjudicated", prompt_version,
                             flags_cat, cb_version, "flagged", note,
                             provisional={"run_a": data_a, "run_b": data_b, "choice": choice})
                rc.append_run_log(item_id, self.step, "adjudicated", "x-adjudicator",
                                    prompt_version, started, ended, "pass", note, None, "flagged")
                continue

            path_a = _out_path(self.step, item_id, "runA")
            path_b = _out_path(self.step, item_id, "runB")
            if not (os.path.exists(path_a) and os.path.exists(path_b)):
                continue
            data_a, data_b = _read_json(path_a), _read_json(path_b)
            ok_a, msg_a = _e_check_one(self.step, item_id, data_a, context)
            ok_b, msg_b = _e_check_one(self.step, item_id, data_b, context)
            started = ended = rc.now_iso()

            if ok_a and ok_b and (data_a or {}).get("trap") == (data_b or {}).get("trap"):
                self._apply(item_id, qid, number, data_a, "runA", prompt_version, flags_cat,
                             cb_version, "pass", "runs agree on the trap")
                rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version,
                                    started, ended, "pass", "runs agree", None, "pass")
                continue

            failed = (f"runA: {'ok' if ok_a else msg_a}; runB: {'ok' if ok_b else msg_b}"
                      + ("" if (data_a or {}).get("trap") == (data_b or {}).get("trap")
                         else f"; runs disagree on the trap: A={(data_a or {}).get('trap')!r} "
                              f"B={(data_b or {}).get('trap')!r}"))
            rc.append_run_log(item_id, self.step, "runA+runB", self.agent, prompt_version, started,
                                ended, "pass", f"{failed} -> adjudicator", None, "pending")
            new_lines.extend(self._start_adjudicator(item_id, record, number, text_value, data_a,
                                                       data_b, failed, prompt_version))
        return new_lines


# ===========================================================================
# E6 - Descriptive tags (spec 13/E6; scripts/describe_tags.py + e6-context-tagger)
# ===========================================================================

class E6Plugin:
    """FIVE SCRIPT-OWNED FIELDS PLUS ONE AGENT QUESTION, 1 run + retry on that one question.

    scripts/describe_tags.py::describe(record) fills `answer_form`, `negation`, `item_count`,
    `constants_given` and `figure_role` outright, and decides `stem_context` by patterns; its
    `stem_context: None` (returned when two or more context patterns fire at once and spec's
    tie-break needs real judgement) is the DESIGNED trigger for an e6-context-tagger call. On the
    real bank exactly one of the ten canonical questions reaches the agent (Q-000013, where
    `reaction_given` and `figure_given` both fire).

    THE FIVE SCRIPT FIELDS ARE WRITTEN FOR EVERY READY QUESTION, agent or not -- including the
    ones still waiting on the agent for `stem_context`, because the other five do not depend on
    it and withholding them would stall Stage F for no reason.

    Same in-process reasoning as E1Plugin (describe_tags.py writes nothing of its own, so a
    subprocess per question would change no state), and the same `unsure` safe default spec
    13/E6 names: `plain` is NEVER the fallback -- codebook/E6.md section 2 is that `plain` can
    never win a tie-break, and this agent only runs when two or more contexts already applied.
    """
    step = "E6"
    agent = "e6-context-tagger"

    def _candidates(self, filters=None):
        return _e_candidates(self.step, filters)

    @staticmethod
    def _script_half(record):
        return describe_tags.describe(record)

    def _build_agent_input(self, record):
        payload = {
            "question": _e_question_view(record),
            "structure": record.get("structure"),
            "has_figure": bool(record.get("has_figure")),
        }
        text, _version = _e_codebook(self.step)
        if text is not None:
            payload["codebook"] = text
        return payload

    def list_items(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        lines = []
        for qid, record in self._candidates(filters).items():
            status = rc.read_item_status(self.step, qid)
            if status and status.get("status") != "stale" \
                    and status.get("prompt_version") == prompt_version:
                continue
            if rc.read_pending(self.step, qid) or os.path.exists(_out_path(self.step, qid, "runA")):
                continue
            if self._script_half(record)["stem_context"] is not None:
                continue  # the patterns decided; no agent call, by design
            path = _e_write_agent_input(self.step, qid, "runA", self._build_agent_input(record))
            lines.append(ListLine(qid, self.agent, _relpath(path),
                                    _relpath(_out_path(self.step, qid, "runA")), "runA"))
        return lines

    def list_reason(self):
        candidates = self._candidates()
        if not candidates:
            return ("E6 needs a resolved E1 (steps/E1/status/<QID>.json). None exists: E1 needs "
                    "D7, which needs the agent-driven D6.")
        undecided = [q for q, r in candidates.items()
                     if self._script_half(r)["stem_context"] is None]
        if not undecided:
            return (f"E6: scripts/describe_tags.py decides `stem_context` by pattern for all "
                    f"{len(candidates)} ready question(s), so no agent call is needed -- run "
                    f"`run_step.py E6 --check` (or --auto) to store the tags.")
        return "E6: every question the patterns could not decide already has output pending --check."

    def auto(self, filters):
        """The script half, reported. It writes nothing itself (--check stores the fields through
        the same describe_tags.describe call), so a second --auto is a no-op by construction."""
        needs_agent = 0
        for qid, record in self._candidates(filters).items():
            tags = self._script_half(record)
            print(f"E6 --auto: {qid} -> stem_context "
                  f"{tags['stem_context'] or 'NEEDS-AGENT'}  ({tags['stem_context_why']}); "
                  f"answer_form={tags['answer_form']} negation={tags['negation']} "
                  f"item_count={tags['item_count']} constants_given={tags['constants_given']} "
                  f"figure_role={tags['figure_role']}", file=sys.stderr)
            if tags["stem_context"] is None:
                needs_agent += 1
        print(f"E6 --auto: {needs_agent} question(s) need a real e6-context-tagger call "
              f"(`--list`); every other field is script-owned.", file=sys.stderr)

    _SCRIPT_FIELDS = ("answer_form", "negation", "item_count", "constants_given", "figure_role")

    def _store(self, qid, tags, stem_context, decided_by, prompt_version, status, cb_version):
        """Store E6's tags. When `stem_context` is None the item is still waiting on the agent, so
        the five script-owned fields are written (they do not depend on it, and withholding them
        would stall Stage F for no reason) and `stem_context`/`descriptive_tags` are NOT written
        at all -- writing None would look like a decided value."""
        descriptive = {k: tags[k] for k in self._SCRIPT_FIELDS}
        fields = dict(descriptive)
        fields["e6_stem_context_why"] = tags.get("stem_context_why")
        if stem_context is None:
            fields["e6_decided_by"] = decided_by
            return _e_set_tags(self.step, qid, fields, prompt_version, "pass",
                                cb_version=cb_version)
        fields.update({
            "stem_context": stem_context,
            "descriptive_tags": dict(descriptive, stem_context=stem_context),
            "e6_stem_context": stem_context,
            "e6_decided_by": decided_by,
        })
        return _e_set_tags(self.step, qid, fields, prompt_version, status, cb_version=cb_version)

    def _failing_message(self, item_id, data):
        record = lib_records.read_record(item_id)
        ok, msg = _e_check_one(self.step, item_id, data, {"record": record})
        return msg if not ok else "the retry's own check passed but the item was not resolved"

    def _post_assembly(self, item_id, run_label, data, status, prompt_version, flags_cat,
                        cb_version):
        record = lib_records.read_record(item_id)
        tags = self._script_half(record)
        usable = isinstance(data, dict) and "error" not in data
        if status == "pass" and usable:
            stem_context = data.get("stem_context")
            decided_by = f"agent {self.agent} ({run_label}): {(data.get('why') or '').strip()}"
        else:
            # config/steps.yaml E6 safe_default: `unsure`, E6_CONTEXT_UNSURE (low), the agent's
            # answer kept as the provisional value. NEVER `plain`.
            stem_context = "unsure"
            decided_by = (f"safe default after {run_label}: {self._failing_message(item_id, data)}")
        if stem_context == "unsure":
            rc.raise_flag("item", item_id, self.step, "E6_CONTEXT_UNSURE",
                           flags_cat.get("E6_CONTEXT_UNSURE", "low"),
                           f"stem_context is unsure -- {decided_by}",
                           provisional_value={"agent_answer": data if usable else None,
                                               "script_candidates": tags.get("stem_context_why")},
                           prompt_version=prompt_version)
        self._store(item_id, tags, stem_context, decided_by, prompt_version, status, cb_version)

    def _resolve_by_script(self, qid, record, tags, prompt_version, cb_version):
        self._store(qid, tags, tags["stem_context"],
                     f"script pattern: {tags['stem_context_why']}", prompt_version, "pass",
                     cb_version)
        rc.write_item_status(self.step, qid, "pass", prompt_version,
                               extra={"run": "script",
                                       "check_message": f"patterns decided: {tags['stem_context_why']}"})
        rc.append_run_log(qid, self.step, "script", None, prompt_version, rc.now_iso(),
                            rc.now_iso(), "pass",
                            f"describe_tags.py -> stem_context {tags['stem_context']}", None,
                            "pass")

    def check(self, filters):
        cfg = get_cfg(self.step)
        flags_cat = cfg.get("flags") or {}
        prompt_version = rc.get_prompt_version(self.step)
        _text, cb_version = _e_codebook(self.step)
        items_with_builders, agent_inputs = {}, {}

        for qid, record in self._candidates(filters).items():
            if not _d_fresh(self.step, qid):
                continue
            tags = self._script_half(record)
            if tags["stem_context"] is not None:
                self._resolve_by_script(qid, record, tags, prompt_version, cb_version)
                continue
            # Still waiting on the agent for stem_context: write the five script-owned fields now
            # anyway (they do not depend on it), without a status -- the item stays unresolved.
            self._store(qid, tags, None, "script fields only; stem_context awaits the agent",
                         prompt_version, "flagged", cb_version)
            items_with_builders[qid] = {"record": record}
            agent_inputs[qid] = self._build_agent_input(record)

        def _post(item_id, run_label, data, status):
            self._post_assembly(item_id, run_label, data, status, prompt_version, flags_cat,
                                 cb_version)

        return resolve_single_run_items(self.step, cfg, self.agent, items_with_builders, {}, _post,
                                          agent_inputs=agent_inputs)


# ===========================================================================
# Stage F - shared helpers (spec Section 14; scripts/f_common.py and the six F scripts)
#
# Stage F is five script-only steps and one PEOPLE step. The scripts already exist and already
# own every decision; these plugins only drive them through the runner's three verbs and validate
# what they produced, which is why they are short compared with the E plugins.
#
# WHY THE F MODULES ARE IMPORTED LAZILY. scripts/f_common.py snapshots PROJECT_ROOT (and the
# review/ paths derived from it) at IMPORT time, and the six F scripts snapshot f_common's values
# in turn -- the same gotcha tests/test_run_step.py documents for lib/flags.py's FLAGS_PATH. A
# module-level import here would bind that chain for every run_step.py call, including the ones
# that have nothing to do with Stage F, and before a test could repoint it. So each plugin
# imports what it needs at call time.
#
# WHAT THESE PLUGINS NEVER DO:
#   * never write to data/ -- only scripts/export_tables.py may (spec 6.6), and only past its own
#     release gate. F5Plugin calls export_tables.gate() (read-only) for its --check verdict and
#     the real script as a subprocess for --auto; it never calls export_chapter() and adds no
#     --force / --skip-gate / --bypass of any kind (a test asserts those strings are absent from
#     export_tables.py, and nothing here would make one true from the outside either).
#   * never dispatch a subagent from a script path. F3's cascade reports agent-driven re-runs as
#     `needs_dispatch` for a person to run through --list / invoke / --check
#     (scripts/CONVENTIONS.md rule 7); this plugin surfaces that list and runs nothing from it.
#   * never edit an agent's output. F2's corrections are NEW files under steps/F2/out/, written by
#     apply_review.py on the reviewer's behalf.
# ===========================================================================


def _f_module(name):
    """One Stage F script, imported at call time -- see the section note above."""
    import importlib
    return importlib.import_module(name)


def _f_digest(path):
    """f_common's own content digest, so "has this output changed since the last --check" means
    the same thing here as it does inside Stage F (cascade.py uses it for the same purpose)."""
    return _f_module("f_common").file_digest(path)


def _f_validate(step, item_id, data, context, prompt_version, agent=None, run="runA",
                 fail_status="flagged", evidence=None, extra=None):
    """Schema + scripts/checks/<STEP>.py for one Stage F output, then one status row and one
    run_log row. Returns (ok, message).

    No Stage F step has a fallback chain (every one's config/steps.yaml `fallback` is []) and
    none has a safe default, so there is no retry/adjudicator rung to drive here: an output
    either satisfies its own check or the item is reported as needing a fix in the script or the
    records -- never patched in the output file (spec 14/F4, CLAUDE.md rule 11)."""
    started = rc.now_iso()
    ok, msg = rc.validate_schema(step, data)
    if ok:
        ok, msg = rc.run_step_check(
            step, data, dict({"item_id": item_id, "step": step}, **(context or {})))
    ended = rc.now_iso()
    status = "pass" if ok else fail_status
    rc.write_item_status(step, item_id, status, prompt_version,
                           extra=dict({"check_message": msg, "run": run}, **(extra or {})))
    rc.append_run_log(item_id, step, run, agent, prompt_version, started, ended,
                        "pass" if ok else "fail", msg, None, status)
    return ok, msg


# ===========================================================================
# F1 - Review queue and pack (spec 14/F1; scripts/build_review_pack.py)
# ===========================================================================

class F1Plugin:
    """Pure SCRIPT step (`agent: "script"`), item = the whole RUN, so like S0 the script takes no
    item argument: `python3 scripts/build_review_pack.py [--chapters X,Y]`.

    Its output is review/review_pack/_manifest.json (schemas/F1.json's shape). The one piece of
    context scripts/checks/F1.py wants is `expected_seed`, which it compares against the
    manifest's own `seed`: the audit sample has to be REPRODUCIBLE (spec 14/F1), so the plugin
    passes build_review_pack.AUDIT_SEED -- the script's own fixed default -- rather than a number
    typed here, and `--seed` stays a testing-only override the runner never sets.

    F1 raises no flags of its own: it is the step that COLLECTS flags, and one of its own would
    mean the review queue could never empty (its config/steps.yaml `flags` map is empty for that
    reason). A failing check is therefore `flagged` with the message, not a new flag.
    """
    step = "F1"
    item_id = "run"

    def list_items(self, filters):
        return []

    def list_reason(self):
        return ("F1 is a script-only step (scripts/build_review_pack.py) whose item is the whole "
                "run. Nothing to list; run `run_step.py F1 --auto`.")

    def auto(self, filters):
        script = rc.pp("scripts", "build_review_pack.py")
        if not os.path.exists(script):
            print(f"F1 --auto: {script} does not exist. Nothing to run.", file=sys.stderr)
            return
        cmd = [sys.executable, script]
        if filters.get("chapters"):
            cmd += ["--chapters", ",".join(sorted(filters["chapters"]))]
        started = rc.now_iso()
        result = subprocess.run(cmd, cwd=rc.pp())
        ended = rc.now_iso()
        rc.append_run_log(self.item_id, self.step, "script", None,
                            rc.get_prompt_version(self.step), started, ended,
                            "pass" if result.returncode == 0 else "fail",
                            f"build_review_pack.py exit {result.returncode}", None,
                            "pass" if result.returncode == 0 else "blocked")

    def check(self, filters):
        build_review_pack = _f_module("build_review_pack")
        path = build_review_pack.MANIFEST_PATH
        if not os.path.exists(path):
            return []  # F1 --auto has not built a pack yet
        prompt_version = rc.get_prompt_version(self.step)
        existing = rc.read_item_status(self.step, self.item_id)
        data = _read_json(path)
        if existing and existing.get("status") != "stale" \
                and existing.get("prompt_version") == prompt_version \
                and existing.get("check_message") and existing.get("run_id") == data.get("run_id"):
            return []
        # The run_id is kept on the status file so a re-check of the SAME pack does nothing the
        # second time while a freshly rebuilt pack (new run_id) is always re-validated (spec 5.9).
        _f_validate(self.step, self.item_id, data,
                     {"expected_seed": build_review_pack.AUDIT_SEED}, prompt_version,
                     run="script", evidence=[_relpath(path)],
                     extra={"run_id": data.get("run_id")})
        return []


# ===========================================================================
# F2 - Review and edit (spec 14/F2) - PEOPLE
# ===========================================================================

class F2Plugin:
    """THE ONE STEP IN THE PIPELINE WITH NO AGENT AND NO SCRIPT: `agent: "PEOPLE"`.

    There is nothing for the runner to run. Reviewers work through the pack F1 built
    (review/review_pack/index.html), approve or correct any flag, and may edit any field of any
    item even if it passed; each pack page names the expected reviewer (registers and intake ->
    Ekta; subtopic lists, change log, passage cuts, answers, misreads, corrections, evidence,
    notes, changed answers, repeat groups and tags -> faculty of that subject). They write their
    decisions into review/decisions.csv, and step F3 (`apply_review.py`) applies them.

    SO WHO WRITES F2's OUTPUTS? apply_review.py does, ON THE REVIEWER'S BEHALF: a `correct` or
    `edit` decision becomes a NEW file steps/F2/out/<ITEM>.correctionNNN.<field>.json plus a
    record update, and the original step's output file is never modified. That is the mechanism
    that keeps CLAUDE.md's "never edit an agent's output" true, and it is why this plugin has a
    check() (to validate those correction files) but deliberately NO auto(): `run_step.py F2
    --auto` must say that people do this step, not pretend to run it or report a missing headless
    subagent. run_step.py's cmd_auto special-cases `step_kind(cfg) == "people"` for exactly that.

    The out-file name carries THREE dotted parts, so the generic `<item_id>.<run_label>.json`
    parser does not apply here and this plugin parses the names itself; the item id it records is
    the whole stem (`Q-000015.correction001.e4_primary`), which is unique per correction and
    keeps successive corrections to one field all visible.
    """
    step = "F2"

    def list_items(self, filters):
        return []

    def list_reason(self):
        pending = self._corrections(filters={"chapters": None, "papers": None, "items": None})
        return ("F2 is the PEOPLE step (spec 14/F2): reviewers work through the pack F1 built "
                "(review/review_pack/index.html) and write their decisions into "
                "review/decisions.csv. There is nothing for the runner to list or run -- no "
                "agent, no script. `run_step.py F3 --auto` is what applies what they wrote, and "
                "it writes their corrections as new steps/F2/out/ files on their behalf so no "
                "agent output is ever edited in place. "
                f"{len(pending)} correction file(s) exist so far.")

    def _corrections(self, filters):
        """[(item_id, path)] for every steps/F2/out/*.json correction file in scope."""
        out_dir = rc.pp("steps", self.step, "out")
        if not os.path.isdir(out_dir):
            return []
        rows = []
        for fn in sorted(os.listdir(out_dir)):
            if not fn.endswith(".json"):
                continue
            item_id = fn[: -len(".json")]
            if not rc.item_passes_filters(item_id, filters):
                continue
            rows.append((item_id, os.path.join(out_dir, fn)))
        return rows

    def check(self, filters):
        prompt_version = rc.get_prompt_version(self.step)
        for item_id, path in self._corrections(filters):
            existing = rc.read_item_status(self.step, item_id)
            if existing and existing.get("status") != "stale" \
                    and existing.get("prompt_version") == prompt_version:
                continue
            _f_validate(self.step, item_id, _read_json(path), {}, prompt_version,
                         agent="PEOPLE", run="correction", evidence=[_relpath(path)])
        return []


# ===========================================================================
# F3 - Apply decisions, cascade (spec 14/F3; scripts/apply_review.py + scripts/cascade.py)
# ===========================================================================

class F3Plugin:
    """Pure SCRIPT step. `run_step.py F3 --auto` REALLY APPLIES the reviewers' decisions: it is
    the runner's "do this step" verb, and F3's whole job is to apply review/decisions.csv, close
    the flags it answers, write each correction as a new steps/F2/out/ file, and mark the
    cascade's downstream (item, step) pairs stale.

    WHY apply_review.apply_decisions() IS CALLED IN-PROCESS instead of as a subprocess: its
    REPORT is F3's output (schemas/F3.json is the report's shape, and scripts/checks/F3.py
    validates it), and the script only ever prints that report -- it writes it nowhere. The
    subprocess contract in scripts/CONVENTIONS.md is explicit that the runner never parses a
    script's stdout, so parsing `--json` output would break it. Calling the function and writing
    its return value to steps/F3/out/run.json keeps both rules: nothing is parsed, and the report
    is a real file the check can validate. Precedent for an in-process call into a step's own
    script: D3Plugin (fetch_passages.fetch_for_item), B9Plugin (recover_figures), D10Plugin.

    AGENT-DRIVEN RE-RUNS ARE REPORTED, NEVER RUN. cascade.run_plan drives only the script-only
    steps through the normal runner and returns every agent-driven step as `needs_dispatch`,
    because a script must never call a subagent (scripts/CONVENTIONS.md rule 7). This plugin
    prints that list and does nothing with it; a person runs those through --list / invoke /
    --check.

    `--items` / `--chapters` CANNOT SCOPE F3 and the plugin says so instead of pretending: one
    apply pass reads the whole review/decisions.csv (apply_review remembers applied rows by
    digest in review/applied_decisions.jsonl, so re-running never double-applies).
    """
    step = "F3"
    item_id = "run"

    def list_items(self, filters):
        return []

    def list_reason(self):
        return ("F3 is a script-only step (scripts/apply_review.py + scripts/cascade.py). "
                "Nothing to list; run `run_step.py F3 --auto`. Agent-driven steps the cascade "
                "makes stale are reported as `needs_dispatch` in its output, for a person to run "
                "through the normal --list / invoke / --check loop.")

    def _out_path(self):
        return rc.pp("steps", self.step, "out", f"{self.item_id}.json")

    def auto(self, filters):
        apply_review = _f_module("apply_review")
        if any(filters.get(k) for k in ("chapters", "papers", "items")):
            print("F3 --auto: a filter was given but F3 cannot be scoped -- one apply pass reads "
                  "the whole review/decisions.csv. Applying all unapplied rows (already-applied "
                  "rows are skipped by digest).", file=sys.stderr)
        prompt_version = rc.get_prompt_version(self.step)
        started = rc.now_iso()
        report = apply_review.apply_decisions(apply=True, run=True, transitive=True)
        ended = rc.now_iso()
        _write_json(self._out_path(), report)

        cascade_report = (report.get("cascade") or {})
        print(f"F3 --auto: {report['rows_new']} new decision row(s) of {report['rows_total']}; "
              f"{len(report['applied'])} applied, {len(report.get('skipped') or [])} already "
              f"applied, {len(report['errors'])} rejected; cascade marked "
              f"{cascade_report.get('marked_stale', 0)} of {cascade_report.get('pairs', 0)} "
              f"pair(s) stale.", file=sys.stderr)
        for entry in (cascade_report.get("rerun") or {}).get("needs_dispatch") or []:
            print(f"F3 --auto: NEEDS DISPATCH -- {entry['step']} for "
                  f"{', '.join(entry['items'])}. A script never calls a subagent "
                  f"(scripts/CONVENTIONS.md rule 7), so run `run_step.py {entry['step']} --list`, "
                  f"invoke the named subagent for each line, then `--check`.", file=sys.stderr)
        for err in report["errors"]:
            print(f"F3 --auto: REJECTED {err.get('target')!r}: {err.get('why')}", file=sys.stderr)
        rc.append_run_log(self.item_id, self.step, "script", None, prompt_version, started, ended,
                            "fail" if report["errors"] else "pass",
                            f"{len(report['applied'])} applied, {len(report['errors'])} rejected",
                            None, "flagged" if report["errors"] else "pass")

    def check(self, filters):
        path = self._out_path()
        if not os.path.exists(path):
            return []  # F3 --auto has not run yet
        prompt_version = rc.get_prompt_version(self.step)
        data = _read_json(path)
        digest = _f_digest(path)
        existing = rc.read_item_status(self.step, self.item_id)
        if existing and existing.get("status") != "stale" \
                and existing.get("prompt_version") == prompt_version \
                and existing.get("report_digest") == digest:
            return []
        _f_validate(self.step, self.item_id, data, {}, prompt_version, run="script",
                     evidence=[_relpath(path)], extra={"report_digest": digest})
        return []


# ===========================================================================
# F4 - Counts (spec 14/F4; scripts/compute_counts.py)
# ===========================================================================

class F4Plugin:
    """Pure SCRIPT step, item = one SUBTOPIC, but ONE invocation covers every subtopic: the
    headline F4 check ("the subtopic totals equal the number of question-subtopic links", counted
    in a separate pass) is a cross-subtopic invariant, and compute_counts.py refuses to write
    ANYTHING if it fails. Running it once per subtopic would make that refusal meaningless, so
    the plugin invokes it the way the script is built --
    `python3 scripts/compute_counts.py [--chapters X,Y]` -- and then validates each
    steps/F4/out/<SUBTOPIC>.json per item.

    Never edit a count by hand (spec 14/F4, CLAUDE.md rule 11): a failing per-subtopic check is
    fixed in the records or in compute_counts.py, never in the output file.
    """
    step = "F4"

    def list_items(self, filters):
        return []

    def list_reason(self):
        return ("F4 is a script-only step (scripts/compute_counts.py). Nothing to list; run "
                "`run_step.py F4 --auto`. It makes no judgement: a count is computed, never "
                "typed.")

    def auto(self, filters):
        script = rc.pp("scripts", "compute_counts.py")
        if not os.path.exists(script):
            print(f"F4 --auto: {script} does not exist. Nothing to run.", file=sys.stderr)
            return
        cmd = [sys.executable, script]
        if filters.get("chapters"):
            cmd += ["--chapters", ",".join(sorted(filters["chapters"]))]
        started = rc.now_iso()
        result = subprocess.run(cmd, cwd=rc.pp())
        ended = rc.now_iso()
        rc.append_run_log("all_subtopics", self.step, "script", None,
                            rc.get_prompt_version(self.step), started, ended,
                            "pass" if result.returncode == 0 else "fail",
                            f"compute_counts.py exit {result.returncode}"
                            + (" (it refuses to write anything when the totals do not reconcile)"
                               if result.returncode else ""),
                            None, "pass" if result.returncode == 0 else "blocked")

    def check(self, filters):
        out_dir = rc.pp("steps", self.step, "out")
        if not os.path.isdir(out_dir):
            return []
        prompt_version = rc.get_prompt_version(self.step)
        for fn in sorted(os.listdir(out_dir)):
            # `_all.json` is compute_counts.py's own cross-subtopic aggregate for export_tables.py,
            # not a per-item output, and schemas/F4.json does not describe it.
            if not fn.endswith(".json") or fn.startswith("_"):
                continue
            item_id = fn[: -len(".json")]
            if not rc.item_passes_filters(item_id, filters):
                continue
            path = os.path.join(out_dir, fn)
            digest = _f_digest(path)
            existing = rc.read_item_status(self.step, item_id)
            if existing and existing.get("status") != "stale" \
                    and existing.get("prompt_version") == prompt_version \
                    and existing.get("counts_digest") == digest:
                continue
            _f_validate(self.step, item_id, _read_json(path), {}, prompt_version, run="script",
                         evidence=[_relpath(path)], extra={"counts_digest": digest})
        return []


# ===========================================================================
# F5 - Release and export (spec 14/F5; scripts/export_tables.py)
# ===========================================================================

class F5Plugin:
    """Pure SCRIPT step, item = one CHAPTER. The ONLY writer of data/ is
    scripts/export_tables.py, past its own six-condition release gate, after a real sign-off row
    in review/releases.csv (CLAUDE.md: "never release a chapter; only export_tables.py does").

    THIS PLUGIN ADDS NO WAY AROUND THAT GATE AND MUST NOT.
      * --auto shells out to the real script and passes nothing but `--chapters` / nothing at all.
        It never sets `--audit-target` (the script's own documented default stands), and there is
        no --force / --skip-gate / --bypass to pass even if it wanted to.
      * --check calls export_tables.gate(chapter_id) -- READ-ONLY, it evaluates conditions and
        writes nothing -- to record each chapter's verdict as steps/F5/out/<CHAPTER>.json and
        validate it against schemas/F5.json + scripts/checks/F5.py. It never calls
        export_chapter().
      * A chapter the gate refuses is recorded `blocked` with the failing condition ids, because
        the only two outcomes of this step are "released" and "refused" and a refused chapter is
        not done. There is no safe default and no flag code: F5's config/steps.yaml `flags` map
        is empty deliberately -- there is no value it could fall back to.

    Note that scripts/checks/F5.py PASSES a correctly-refused verdict (ok=false with at least one
    failed condition is a coherent verdict, and that is what the check tests). The refusal shows
    up as the item's `blocked` status and in --check's message, not as a failing check.
    """
    step = "F5"

    def _chapters(self, filters):
        export_tables = _f_module("export_tables")
        return [c for c in export_tables.known_chapters()
                if rc.item_passes_filters(c, filters)]

    def list_items(self, filters):
        return []

    def list_reason(self):
        return ("F5 is a script-only step (scripts/export_tables.py). Nothing to list; run "
                "`run_step.py F5 --check` for the gate report, or `--auto` to release every "
                "chapter that passes the gate. It refuses loudly by default and there is no "
                "override.")

    def auto(self, filters):
        script = rc.pp("scripts", "export_tables.py")
        if not os.path.exists(script):
            print(f"F5 --auto: {script} does not exist. Nothing to run.", file=sys.stderr)
            return
        cmd = [sys.executable, script]
        if filters.get("chapters"):
            cmd += ["--chapters", ",".join(sorted(filters["chapters"]))]
        else:
            cmd += ["--all-eligible"]
        started = rc.now_iso()
        result = subprocess.run(cmd, cwd=rc.pp())
        ended = rc.now_iso()
        # exit 1 = at least one requested chapter was REFUSED by the gate, which is the normal,
        # correct outcome for a chapter with no sign-off row -- not a script failure. exit 2 is a
        # real failure (e.g. F4 has not computed the counts).
        note = {0: "released every eligible chapter (or there was nothing eligible)",
                1: "refused at least one chapter: the release gate is not satisfied, nothing was "
                   "written for it",
                2: "could not run (see its own output -- most likely steps/F4/out/_all.json is "
                   "missing, i.e. F4 has not computed the counts)"}.get(
                       result.returncode, f"exit {result.returncode}")
        print(f"F5 --auto: export_tables.py exit {result.returncode} -- {note}", file=sys.stderr)
        rc.append_run_log("all_chapters", self.step, "script", None,
                            rc.get_prompt_version(self.step), started, ended,
                            "pass" if result.returncode in (0, 1) else "fail",
                            f"export_tables.py exit {result.returncode}: {note}", None,
                            "pass" if result.returncode == 0 else
                            ("flagged" if result.returncode == 1 else "blocked"))

    def check(self, filters):
        export_tables = _f_module("export_tables")
        prompt_version = rc.get_prompt_version(self.step)
        for chapter_id in self._chapters(filters):
            report = export_tables.gate(chapter_id)
            path = _out_path(self.step, chapter_id, "gate")
            _write_json(path, report)
            failed = [c["id"] for c in report.get("conditions") or [] if not c.get("ok")]
            started = rc.now_iso()
            ok, msg = rc.validate_schema(self.step, report)
            if ok:
                ok, msg = rc.run_step_check(self.step, report,
                                             {"item_id": chapter_id, "step": self.step})
            ended = rc.now_iso()
            if not ok:
                status, detail = "blocked", f"the gate verdict is not coherent: {msg}"
            elif report.get("ok"):
                status, detail = "pass", "the release gate is satisfied"
            else:
                status = "blocked"
                detail = (f"REFUSED: the release gate is not satisfied ({', '.join(failed)}). "
                          f"Nothing was written to data/ for this chapter, and there is no "
                          f"override: fix the conditions and get a sign-off row into "
                          f"review/releases.csv.")
            rc.write_item_status(self.step, chapter_id, status, prompt_version,
                                   extra={"check_message": detail, "failed_conditions": failed})
            rc.append_run_log(chapter_id, self.step, "gate", None, prompt_version, started, ended,
                                "pass" if ok else "fail", detail, None, status)
        return []


# ===========================================================================
# F6 - Gold set and scoring (spec 14/F6; scripts/score_gold.py)
# ===========================================================================

class F6Plugin:
    """Pure SCRIPT step, item = the whole RUN (one score per run, against gold/gold_set.csv).

    `needs: F3`, not F5: scoring measures the REVIEWED pilot (spec 18.2 step 3 runs it after
    apply-review, before anything is released) and spec 18.3 re-runs it after every fix, so it
    must not wait on a release.

    A MISSED TARGET IS NOT A CHECK FAILURE. gold/scores.md exists precisely to report misses so
    M7 can act on them; scripts/checks/F6.py only enforces the ARITHMETIC of the score (matched
    never exceeds checked, rate is exactly matched/checked, a criterion that checked nothing
    reports null rather than a passing verdict). F6 raises no flags: a missed target is a report,
    not a defect in an item.

    NO GOLD SET -> NO SCORE, and that is reported rather than invented. score_gold.py exits 2 and
    writes nothing when gold/gold_set.csv does not exist, which is the real state of this project
    today (gold/ is empty). The in-process half of check() re-raises the same refusal rather than
    scoring against a fabricated gold set.
    """
    step = "F6"
    item_id = "run"

    def list_items(self, filters):
        return []

    def list_reason(self):
        score_gold = _f_module("score_gold")
        if not os.path.exists(score_gold.GOLD_PATH):
            return ("F6 is a script-only step (scripts/score_gold.py), and it has nothing to "
                    "score: gold/gold_set.csv does not exist. Spec 14/F6 wants 90 "
                    "reviewer-confirmed questions (30 per subject); scoring against an invented "
                    "gold set would produce a meaningless number, so the script refuses and so "
                    "does this step.")
        return ("F6 is a script-only step (scripts/score_gold.py). Nothing to list; run "
                "`run_step.py F6 --auto`.")

    def _out_path(self):
        return rc.pp("steps", self.step, "out", f"{self.item_id}.json")

    def auto(self, filters):
        script = rc.pp("scripts", "score_gold.py")
        if not os.path.exists(script):
            print(f"F6 --auto: {script} does not exist. Nothing to run.", file=sys.stderr)
            return
        started = rc.now_iso()
        result = subprocess.run([sys.executable, script], cwd=rc.pp())
        ended = rc.now_iso()
        # exit 2 = no usable gold set. Honest, expected today, and NOT a script failure to flag.
        status = "pass" if result.returncode == 0 else ("skipped" if result.returncode == 2
                                                         else "flagged")
        rc.append_run_log(self.item_id, self.step, "script", None,
                            rc.get_prompt_version(self.step), started, ended,
                            "pass" if result.returncode == 0 else "fail",
                            f"score_gold.py exit {result.returncode}"
                            + (" (no usable gold/gold_set.csv -- nothing was scored and nothing "
                               "was written)" if result.returncode == 2 else ""),
                            None, status)

    def check(self, filters):
        score_gold = _f_module("score_gold")
        f_common = _f_module("f_common")
        prompt_version = rc.get_prompt_version(self.step)
        try:
            gold, meta, _shape = score_gold.load_gold()
        except score_gold.GoldSetProblem as e:
            rc.write_item_status(self.step, self.item_id, "skipped", prompt_version,
                                   extra={"check_message": f"nothing to score: {e}"})
            return []
        records = f_common.load_records()
        warnings, _by_subject = score_gold.gold_shape_warnings(gold, meta, records)
        result = score_gold.score(gold, meta, records)
        # schemas/F6.json's shape, which is exactly what score_gold.py --json prints: the
        # per-criterion rows without their (potentially huge) failure lists, the failure COUNT,
        # and the gold-set warnings a reader must see before trusting a number.
        payload = {
            "per_criterion": [{k: v for k, v in c.items() if k != "failures"}
                               for c in result["per_criterion"]],
            "per_step": {k: {kk: vv for kk, vv in v.items() if kk != "failures"}
                          for k, v in (result.get("per_step") or {}).items()},
            "failures": len(result["failures"]),
            "warnings": warnings,
        }
        _write_json(self._out_path(), payload)
        _f_validate(self.step, self.item_id, payload, {}, prompt_version, run="script",
                     evidence=[_relpath(self._out_path())])
        return []

_PLUGINS = None


def get_plugins():
    global _PLUGINS
    if _PLUGINS is None:
        _PLUGINS = {
            "S0": S0Plugin(), "A1": A1Plugin(), "A2": A2Plugin(), "A2S": A2SPlugin(),
            "A3": A3Plugin(), "A4": A4Plugin(), "A5": A5Plugin(), "A6": A6Plugin(),
            "A7": A7Plugin(), "A8": A8Plugin(), "A9": A9Plugin(),
            "B1": B1Plugin(), "B2": B2Plugin(), "B3": B3Plugin(), "B4": B4Plugin(),
            "B5": B5Plugin(), "B6": B6Plugin(), "B7": B7Plugin(), "B8": B8Plugin(),
            "B9": B9Plugin(), "B10": B10Plugin(), "A2B": A2BPlugin(), "A2N": A2NPlugin(),
            "A2L": A2LPlugin(), "A2I": A2IPlugin(), "A2C": A2CPlugin(), "A2R": A2RPlugin(),
            "C1": C1Plugin(),
            "D1": D1Plugin(), "D2": D2Plugin(), "D3": D3Plugin(), "D4": D4Plugin(),
            "D5": D5Plugin(), "D6": D6Plugin(), "D7": D7Plugin(), "D8": D8Plugin(),
            "D9": D9Plugin(), "D10": D10Plugin(), "D11": D11Plugin(),
            "E0": E0Plugin(), "E1": E1Plugin(), "E2": E2Plugin(), "E3": E3Plugin(),
            "E4": E4Plugin(), "E5": E5Plugin(), "E6": E6Plugin(),
            # ECAT lives in its own module: its item is a GROUP of questions read from pre-built
            # packets, not one item derived per question, so it shares none of the E1-E6 helpers.
            "ECAT": ecat_plugin.ECATPlugin(),
            # B3F's items are figure CROPS read from the v2 corpus, not per-question items derived
            # from papers/records/, so it shares none of the B1-B10 helpers either.
            "B3F": b3f_plugin.B3FPlugin(),
            # B3V reads a v2 question from its IMAGE, the way Stage A reads an NCERT page. Separate
            # from B3 because its items come from papers_v2/, not from papers/records/.
            "B3V": b3v_plugin.B3VPlugin(),
            # E7V is the difficulty JUDGEMENT per question (SPEC E7), distinct from the
            # E7 script that bands the v1 sheet from ECAT columns -- different items.
            "E7V": e7v_plugin.E7VPlugin(),
            # B6V solves a v2 question with the key withheld, so its answer is independent evidence.
            "B6V": b6v_plugin.B6VPlugin(),
            # The mapping chain: subject -> chapter -> subtopic, each narrowing the next one's list.
            "QSUBJ": qmap_plugins.QSUBJPlugin(),
            "QCHAP": qmap_plugins.QCHAPPlugin(),
            "QTOPIC": qmap_plugins.QTOPICPlugin(),
            # QCA records the CONCEPT and APPROACH instead of an NCERT quotation, for the two
            # subjects whose answers are values rather than sentences -- see qca_plugin.py.
            "QCA": qca_plugin.QCAPlugin(),
            "F1": F1Plugin(), "F2": F2Plugin(), "F3": F3Plugin(), "F4": F4Plugin(),
            "F5": F5Plugin(), "F6": F6Plugin(),
        }
    return _PLUGINS


def get_cfg(step):
    return rc.get_step_cfg(step)
