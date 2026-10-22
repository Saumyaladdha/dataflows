#!/usr/bin/env python3
"""B9's SCRIPT half (step "B9 - Recover the figure", config/steps.yaml).

WHY THIS STEP EXISTS
--------------------
~6.5% of the questions in this bank carry `has_figure: true` from B3, and the scraped sources
they were read from have no image for them at all: of 166 scrape files, 162 contain zero
embedded images (only 2025's four sets have real ones). Cross-booklet-set recovery is
impossible because every set of a given year fails identically. Verified directly on this
build's own data: papers/questions/NEET-2023-MAIN-E1/3.png (Q-000002) is a clean crop of the
stem and the four options with NO circuit diagram anywhere on it -- the figure is genuinely
absent from the scrape, not merely cropped out.

The figures do exist in `inputs/legacy_sheets/*.xlsx`. All 22 sheets embed Mathpix image URLs
in markdown form (`![](https://cdn.mathpix.com/snip/images/<id>.original.fullsize.png`) inside
the `Question` column: 450 URLs across 396 of 3,920 rows (10.1%), covering every year
2010-2026. They return `HTTP 200, image/png` and are clean isolated figure crops -- no
watermark, no answer marking, no website furniture.

WHAT THIS SCRIPT IS ALLOWED TO READ FROM THE SHEETS
---------------------------------------------------
CLAUDE.md forbids passing legacy-sheet columns to agents, because the sheets put many 2018-19
questions in the WRONG chapter under coaching chapter names. The owner has authorised using
the sheets *as a figure reference only*. So this script reads, and may pass on, exactly:

    Question  (its text, and the image URLs embedded in it)
    Year, Subject, Class NEET   (paper identity only; SCRIPT-side provenance, never a judgement)

and NEVER reads `Chapter Name`, `Chapter No`, `Topic`, `Question Type` or `Answer`. That is
enforced here by `_FORBIDDEN_COLUMNS` + `_row_cells()`, not merely by convention -- in
particular the sheet's `Answer` column must never reach any agent, and above all never B6 (the
blind solver), whose entire value is not seeing the answer.

THE NETWORK CALL (documented exception to scripts/CONVENTIONS.md rule 7)
------------------------------------------------------------------------
scripts/CONVENTIONS.md rule 7 says a step script never makes a network call. B9 must, exactly
once per distinct image URL, and the exception is deliberate and bounded:

  * Every agent in this project has `tools: Read, Write` and no network tool, so an agent
    physically cannot open a URL. The image has to be on disk before the agent runs.
  * The fetch is an INGEST, not a judgement: bytes in, bytes on disk, no decision made.
  * It is cached (`papers/figures/_cache/<sha1-of-url>.<ext>`) and therefore idempotent and
    offline on every re-run -- rule 4 (idempotence) still holds exactly.
  * Total cost for all 450 URLs is ~21 MB.
  * No pipeline step ever fetches at agent-run time.

scripts/CONVENTIONS.md itself is owned by another lane and is not edited here; this docstring
and B9's config/steps.yaml entry are the record of the exception.

CLI (scripts/CONVENTIONS.md "hybrid step" shape, same `--item-id <QID>` escape hatch as D3):

    python3 scripts/recover_figures.py --item-id Q-000002   # shortlist + download for one question
    python3 scripts/recover_figures.py --stats              # per-year figure coverage of the sheets
    python3 scripts/recover_figures.py --rebuild-index      # force a re-parse of the 22 sheets

step_plugins.B9Plugin calls `shortlist_and_fetch()` / `attach_figure()` in-process (the same
precedent as D3Plugin calling fetch_passages.fetch_for_item directly). This script raises no
flags of its own: B9Plugin owns every flag so that all of B9's flag logic lives in one place.
"""
import argparse
import collections
import datetime
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from lib import io as lib_io  # noqa: E402
from lib import records as lib_records  # noqa: E402

STEP = "B9"

# ---------------------------------------------------------------------------
# Sheet reading
# ---------------------------------------------------------------------------

SHEETS_DIR_PARTS = ("inputs", "legacy_sheets")
WORKBOOK_SHEET = "All Questions"

# The ONLY columns this project is allowed to take from a legacy sheet (see module docstring).
_ALLOWED_COLUMNS = ("Question", "Year", "Subject", "Class NEET")
# Named explicitly so a future edit that tries to widen the read fails loudly instead of quietly
# re-introducing the coaching-chapter contamination CLAUDE.md warns about.
_FORBIDDEN_COLUMNS = ("Chapter Name", "Chapter No", "Topic", "Question Type", "Answer")

# `![alt](url)` markdown image, the one shape Mathpix writes into the Question column.
_IMG_MD_RE = re.compile(r"!\[[^\]]*\]\((https?://[^)\s]+)\)")
# `[a bracketed description]`, which B3 writes into a stem when it describes a missing figure in
# words (real example, Q-000013: "[Chemical structure of a diketone ...]"). Stripped on BOTH
# sides before matching so one side's prose description can't dilute the other's.
_BRACKETED_RE = re.compile(r"\[[^\]\[]*\]")


def sheets_dir():
    return lib_io.project_path(*SHEETS_DIR_PARTS)


def _index_cache_path():
    return lib_io.project_path("steps", STEP, "work", "_sheet_figure_index.json")


def _row_cells(header, row, wanted):
    """Pull only `wanted` columns out of one sheet row, by header name. Raises if `wanted` asks
    for a column this project is not allowed to read (see module docstring)."""
    bad = [c for c in wanted if c in _FORBIDDEN_COLUMNS]
    if bad:
        raise ValueError(
            f"recover_figures.py may not read legacy-sheet column(s) {bad} -- the sheets' "
            f"chapter/topic/type/answer judgements are off limits (CLAUDE.md); only "
            f"{list(_ALLOWED_COLUMNS)} may be read, and only as a figure reference."
        )
    out = {}
    for name in wanted:
        if name not in header:
            out[name] = None
            continue
        i = header.index(name)
        out[name] = row[i] if i < len(row) else None
    return out


def _parse_workbook(path):
    """Yield one dict per row of `path`'s 'All Questions' sheet that carries at least one image
    URL in its Question column. Real sheets are ragged (some rows are shorter than the header),
    hence `_row_cells`' own bounds check rather than plain indexing."""
    import openpyxl  # imported lazily so --stats is the only thing that needs it loaded

    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    try:
        if WORKBOOK_SHEET not in wb.sheetnames:
            return
        ws = wb[WORKBOOK_SHEET]
        rows = ws.iter_rows(values_only=True)
        try:
            header = [str(h) if h is not None else "" for h in next(rows)]
        except StopIteration:
            return
        for rowno, row in enumerate(rows, start=2):
            cells = _row_cells(header, row, _ALLOWED_COLUMNS)
            question = cells["Question"]
            if question is None:
                continue
            question = str(question)
            urls = _IMG_MD_RE.findall(question)
            if not urls:
                continue
            year = cells["Year"]
            try:
                year = int(year)
            except (TypeError, ValueError):
                year = None
            yield {
                "sheet_file": os.path.basename(path),
                "sheet_row": rowno,
                "question_text": question,
                "figure_urls": urls,
                "year": year,
                "subject": cells["Subject"],
                "exam_label": cells["Class NEET"],
            }
    finally:
        wb.close()


def _sheet_fingerprint():
    """(name, size, mtime) for every workbook, so a cached index is invalidated the moment the
    real inputs change -- never a bare 'file exists' check."""
    out = []
    base = sheets_dir()
    if not os.path.isdir(base):
        return out
    for fn in sorted(os.listdir(base)):
        if not fn.lower().endswith(".xlsx") or fn.startswith("~$"):
            continue
        st = os.stat(os.path.join(base, fn))
        out.append([fn, st.st_size, int(st.st_mtime)])
    return out


def load_figure_index(force_rebuild=False):
    """Every legacy-sheet row that carries at least one figure URL, as a list of dicts (see
    `_parse_workbook`). Cached to steps/B9/work/_sheet_figure_index.json keyed on the real
    workbook fingerprints, so a second B9 run re-parses nothing."""
    fingerprint = _sheet_fingerprint()
    cache_path = _index_cache_path()
    if not force_rebuild and os.path.exists(cache_path):
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                cached = json.load(f)
            if cached.get("fingerprint") == fingerprint:
                return cached["rows"]
        except (ValueError, KeyError, OSError):
            pass  # unreadable/stale cache is never fatal; just rebuild it

    rows = []
    base = sheets_dir()
    for fn, _size, _mtime in fingerprint:
        rows.extend(_parse_workbook(os.path.join(base, fn)))
    for i, r in enumerate(rows):
        r["row_id"] = f"{r['sheet_file']}#{r['sheet_row']}"
        r["_i"] = i
    lib_io.atomic_write_json(cache_path, {
        "fingerprint": fingerprint,
        "built_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "rows": rows,
    })
    return rows


# ---------------------------------------------------------------------------
# Matching
# ---------------------------------------------------------------------------

def match_normalise(text):
    """The normalisation the matching was validated with: strip `![](...)` image markdown, strip
    `[bracketed descriptions]`, unwrap `$...$` (LaTeX delimiters only -- the maths inside is
    kept, it is often the most discriminating part of a question), drop every non-alphanumeric
    character, lowercase, collapse whitespace.

    Deliberately NOT lib/text_normalise + lib/latex_normalise (what C1 uses): those preserve
    punctuation and LaTeX structure, which is right for C1 (comparing two transcriptions of the
    SAME printed page, where a stray `\\,` matters) and wrong here (comparing our transcription
    against a third party's independent Mathpix transcription, where LaTeX style, option
    lettering and punctuation differ on every single row)."""
    s = str(text or "")
    s = _IMG_MD_RE.sub(" ", s)
    for _ in range(3):  # bracketed groups do not nest in real data, but be safe
        nxt = _BRACKETED_RE.sub(" ", s)
        if nxt == s:
            break
        s = nxt
    s = s.replace("$", " ")
    s = re.sub(r"[^0-9a-zA-Z]+", " ", s)
    return " ".join(s.lower().split())


def strip_image_markdown(text, replacement="[figure]"):
    """The sheet's Question text with every `![](url)` replaced. Used when building the agent's
    input: the agent has no network tool, so a raw URL in its input could only ever invite it to
    pretend it fetched one."""
    return _IMG_MD_RE.sub(replacement, str(text or ""))


def trigrams(normalised_text):
    """Word 3-grams, same shape as pair_passages.word_trigrams but over `match_normalise`d text
    (pair_passages' own helper applies normalise_quote instead, which is the wrong normaliser
    here -- see match_normalise)."""
    words = normalised_text.split()
    if len(words) >= 3:
        return {tuple(words[i:i + 3]) for i in range(len(words) - 2)}
    return {tuple(words)} if words else set()


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def record_match_text(record):
    """FULL question text -- stem + statements + list_i + list_ii + every option -- which is what
    the matching was validated against. Stem alone is far too weak: for an image-only chemistry
    question (Q-000013) the stem is six generic words and the options carry all the signal."""
    parts = [record.get("stem_en") or ""]
    for key in ("statements", "list_i", "list_ii"):
        parts += [(it or {}).get("text", "") for it in (record.get(key) or [])]
    parts += [str(v) for v in (record.get("options_en") or {}).values()]
    return " ".join(p for p in parts if p)


# ---- thresholds (real evidence; see the build report) ----------------------------------------
#
# The spec-style "accept at absolute similarity >= 0.85" rule CANNOT be used here and was tested:
# it rejects every true match in this bank. Our transcription and the sheet's are independent
# Mathpix reads of the same printed question with different option lettering ("(1)" vs "a)"),
# different LaTeX, and -- crucially -- a figure on one side that is prose on the other, so a
# genuine match tops out well below 0.85. The real, verified numbers over the full 396-row
# candidate pool:
#
#   Q-000002 (capacitance circuit) true match 0.4118, runner-up 0.0851  -> gap 4.84x
#   Q-000013 (diketone reduction)  true match 0.1515, runner-up 0.0789  -> gap 1.92x
#
# Both true matches were confirmed by eye against the downloaded image. So:
#
#   * MIN_TOP_SIMILARITY = 0.08. The weakest real true match scores 0.1515, ~1.9x this floor;
#     nothing below the floor is ever dispatched (straight to B9_FIGURE_UNMATCHED, no agent
#     call, no figure). A higher floor (e.g. 0.12) leaves almost no margin on the single hardest
#     real case, which is an image-only chemistry question -- exactly the kind B9 exists for.
#   * CLEAR_GAP_RATIO = 1.8. The GAP to the runner-up, not the absolute score, is the real
#     signal. Both verified true matches clear 1.8 (4.84x, 1.92x); a 2.7x gap floor -- the low
#     end of the range this step was briefed with -- would have rejected Q-000013's real,
#     eyeball-verified match, so 2.7 is wrong for this data. Below 1.8 the shortlist is still
#     dispatched (the AGENT, which can see the image, is the one qualified to reject), but the
#     item is marked thin-margin and carries B9_FIGURE_THIN_MARGIN if it is accepted.
#   * The gap NEVER rejects on its own. Only the absolute floor gates dispatch, and only the
#     agent (or a low-confidence verdict) rejects a candidate. "A flagged ambiguous match beats
#     a wrong figure" is implemented by the agent's "none"/low verdict, not by arithmetic.
MIN_TOP_SIMILARITY = 0.08
MIN_CANDIDATE_SIMILARITY = 0.02
CLEAR_GAP_RATIO = 1.8
MAX_CANDIDATES = 3

_GRAM_MEMO = {}


def score_rows(record, index):
    """[(similarity, row), ...] descending, over the whole figure-bearing pool.

    The pool is deliberately the 396 rows that CARRY a figure, not all 3,920: a sheet row with
    no image cannot supply one, so including it could only ever produce a confident match to a
    row that helps nobody. Scoring is also deliberately NOT narrowed to the record's own year --
    NEET repeats questions verbatim across years, and a repeat's figure is the same figure, so
    year-narrowing would throw away real recoveries. Year is carried as provenance instead, and
    the full-pool search is what the gap numbers above were measured on."""
    ours = trigrams(match_normalise(record_match_text(record)))
    scored = []
    for row in index:
        # memoised OUTSIDE the row dict: the row dicts are what gets JSON-cached, and a set of
        # tuples is not JSON-serialisable.
        grams = _GRAM_MEMO.get(row["row_id"])
        if grams is None:
            grams = trigrams(match_normalise(row["question_text"]))
            _GRAM_MEMO[row["row_id"]] = grams
        scored.append((jaccard(ours, grams), row))
    scored.sort(key=lambda t: (-t[0], t[1]["row_id"]))
    return scored


def shortlist(record, index=None):
    """SCRIPT half's decision: which sheet rows (at most MAX_CANDIDATES) are worth showing the
    agent, and is the top one even above the floor. Returns a dict; makes no judgement about
    whether any of them is right -- that is the agent's one job."""
    index = load_figure_index() if index is None else index
    scored = score_rows(record, index)
    top = scored[0][0] if scored else 0.0
    second = scored[1][0] if len(scored) > 1 else 0.0
    gap_ratio = (top / second) if second > 0 else (float("inf") if top > 0 else 0.0)
    kept = [(s, r) for s, r in scored[:MAX_CANDIDATES] if s >= MIN_CANDIDATE_SIMILARITY]
    return {
        "top_similarity": round(top, 6),
        "runner_up_similarity": round(second, 6),
        "gap_ratio": (None if gap_ratio == float("inf") else round(gap_ratio, 4)),
        "clear_gap": gap_ratio >= CLEAR_GAP_RATIO,
        "above_floor": top >= MIN_TOP_SIMILARITY,
        "candidates": [
            {
                "candidate_id": f"cand_{n}",
                "similarity": round(s, 6),
                "row_id": r["row_id"],
                "sheet_file": r["sheet_file"],
                "sheet_row": r["sheet_row"],
                "year": r["year"],
                "subject": r["subject"],
                "exam_label": r["exam_label"],
                "figure_urls": list(r["figure_urls"]),
                "figure_url": r["figure_urls"][0],
                "question_text": r["question_text"],
            }
            for n, (s, r) in enumerate(kept, start=1)
        ],
    }


# ---------------------------------------------------------------------------
# Download-once cache
# ---------------------------------------------------------------------------

FIGURES_DIR_PARTS = ("papers", "figures")
_CACHE_DIRNAME = "_cache"
_USER_AGENT = "pyq_bank/1.0 (NEET PYQ pipeline, step B9 figure recovery)"
_MAX_BYTES = 8 * 1024 * 1024
_MAGIC = [(b"\x89PNG\r\n\x1a\n", ".png"), (b"\xff\xd8\xff", ".jpg"), (b"GIF8", ".gif")]


def figures_dir():
    return lib_io.project_path(*FIGURES_DIR_PARTS)


def _cache_dir():
    return os.path.join(figures_dir(), _CACHE_DIRNAME)


def _image_ext(data):
    for magic, ext in _MAGIC:
        if data.startswith(magic):
            return ext
    return None


def _cached_path_for(url):
    """Existing cache entry for `url`, or None. The cache key is the sha1 of the URL, so the
    same figure referenced from two sheet rows is downloaded exactly once."""
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()
    for _magic, ext in _MAGIC:
        path = os.path.join(_cache_dir(), digest + ext)
        if os.path.exists(path):
            return path
    return None


def fetch_image(url, allow_network=True):
    """Download `url` once into papers/figures/_cache/, or return the already-cached file.

    Returns (path, error). Exactly one is None. A non-image response, an oversized response or
    any network error is an error, never a half-written file -- lib_io.atomic_write_bytes means
    a partial download can never be mistaken for a cache hit on the next run."""
    cached = _cached_path_for(url)
    if cached:
        return cached, None
    if not allow_network:
        return None, "not cached and network fetching is disabled for this call"

    req = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            status = getattr(resp, "status", resp.getcode())
            ctype = (resp.headers.get("Content-Type") or "").split(";")[0].strip()
            data = resp.read(_MAX_BYTES + 1)
    except (urllib.error.URLError, urllib.error.HTTPError, OSError, ValueError) as e:
        return None, f"{type(e).__name__}: {e}"

    if status != 200:
        return None, f"HTTP {status}"
    if len(data) > _MAX_BYTES:
        return None, f"response larger than {_MAX_BYTES} bytes; refused"
    ext = _image_ext(data)
    if ext is None:
        return None, f"response is not an image (Content-Type {ctype!r}, {len(data)} bytes)"

    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()
    path = os.path.join(_cache_dir(), digest + ext)
    lib_io.atomic_write_bytes(path, data)
    return path, None


def shortlist_and_fetch(question_id, record=None, index=None, run_label="runA",
                        allow_network=True):
    """Full SCRIPT half for one question: shortlist, then download each candidate's figure into
    the cache and copy it into steps/B9/work/ under a name the agent is told to Read. Returns
    the shortlist dict, with each candidate gaining `figure_image` (project-relative path) or
    `download_error`. Writes nothing to papers/records/ and raises no flags."""
    record = lib_records.read_record(question_id) if record is None else record
    result = shortlist(record, index)
    work_dir = lib_io.project_path("steps", STEP, "work")
    for cand in result["candidates"]:
        path, err = fetch_image(cand["figure_url"], allow_network=allow_network)
        if err:
            cand["download_error"] = err
            cand["figure_image"] = None
            continue
        with open(path, "rb") as f:
            data = f.read()
        ext = os.path.splitext(path)[1]
        dest = os.path.join(work_dir, f"{question_id}.{run_label}.{cand['candidate_id']}{ext}")
        lib_io.atomic_write_bytes(dest, data)
        cand["figure_image"] = os.path.relpath(dest, lib_io.project_path())
        cand["figure_bytes"] = len(data)
    return result


def attach_figure(question_id, candidate):
    """Copy an ACCEPTED candidate's cached image to papers/figures/<QID>.<ext> and return
    (figure_path_relative, error). The bytes come from the cache, never from the network again:
    'download once, store locally' holds for the attach step too."""
    path = _cached_path_for(candidate["figure_url"])
    if path is None:
        path, err = fetch_image(candidate["figure_url"])
        if err:
            return None, err
    with open(path, "rb") as f:
        data = f.read()
    ext = os.path.splitext(path)[1] or ".png"
    dest = os.path.join(figures_dir(), f"{question_id}{ext}")
    lib_io.atomic_write_bytes(dest, data)
    return os.path.relpath(dest, lib_io.project_path()), None


# ---------------------------------------------------------------------------
# --stats
# ---------------------------------------------------------------------------

def coverage_stats():
    """Per-year figure coverage of the legacy sheets: how many rows exist, how many carry at
    least one figure, how many URLs in total. Reads every row (not just figure-bearing ones), so
    it does not reuse the cached index."""
    import openpyxl

    per_year = collections.defaultdict(lambda: {"rows": 0, "rows_with_figure": 0, "urls": 0})
    totals = {"rows": 0, "rows_with_figure": 0, "urls": 0, "sheets": 0}
    base = sheets_dir()
    for fn, _size, _mtime in _sheet_fingerprint():
        totals["sheets"] += 1
        wb = openpyxl.load_workbook(os.path.join(base, fn), read_only=True, data_only=True)
        try:
            if WORKBOOK_SHEET not in wb.sheetnames:
                continue
            rows = wb[WORKBOOK_SHEET].iter_rows(values_only=True)
            header = [str(h) if h is not None else "" for h in next(rows)]
            for row in rows:
                cells = _row_cells(header, row, _ALLOWED_COLUMNS)
                if cells["Question"] is None:
                    continue
                try:
                    year = int(cells["Year"])
                except (TypeError, ValueError):
                    year = "unknown"
                urls = _IMG_MD_RE.findall(str(cells["Question"]))
                per_year[year]["rows"] += 1
                totals["rows"] += 1
                if urls:
                    per_year[year]["rows_with_figure"] += 1
                    per_year[year]["urls"] += len(urls)
                    totals["rows_with_figure"] += 1
                    totals["urls"] += len(urls)
        finally:
            wb.close()
    return dict(per_year), totals


def _print_stats():
    per_year, totals = coverage_stats()
    print(f"{'year':<8}{'rows':>8}{'rows_with_figure':>20}{'urls':>8}{'pct':>9}")
    for year in sorted(per_year, key=str):
        d = per_year[year]
        pct = (100.0 * d["rows_with_figure"] / d["rows"]) if d["rows"] else 0.0
        print(f"{str(year):<8}{d['rows']:>8}{d['rows_with_figure']:>20}{d['urls']:>8}{pct:>8.1f}%")
    pct = (100.0 * totals["rows_with_figure"] / totals["rows"]) if totals["rows"] else 0.0
    print(f"{'TOTAL':<8}{totals['rows']:>8}{totals['rows_with_figure']:>20}{totals['urls']:>8}"
          f"{pct:>8.1f}%   ({totals['sheets']} workbooks)")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--item-id", help="One question id (Q-000002): shortlist + download.")
    parser.add_argument("--stats", action="store_true",
                        help="Print per-year figure coverage of inputs/legacy_sheets/.")
    parser.add_argument("--rebuild-index", action="store_true",
                        help="Force a re-parse of the 22 workbooks into the cached index.")
    parser.add_argument("--no-network", action="store_true",
                        help="Use only already-cached images; never fetch.")
    args = parser.parse_args(argv)

    if args.rebuild_index:
        rows = load_figure_index(force_rebuild=True)
        print(f"rebuilt figure index: {len(rows)} figure-bearing sheet rows")
    if args.stats:
        _print_stats()
    if args.item_id:
        record = lib_records.read_record(args.item_id)
        if not record.get("has_figure"):
            print(f"{args.item_id}: has_figure is not true; B9 does not apply to this question.")
            return 0
        result = shortlist_and_fetch(args.item_id, record=record,
                                     allow_network=not args.no_network)
        work_path = lib_io.project_path("steps", STEP, "work", f"{args.item_id}.runA.shortlist.json")
        lib_io.atomic_write_json(work_path, result)
        print(json.dumps({k: v for k, v in result.items() if k != "candidates"}, indent=2))
        for c in result["candidates"]:
            print(f"  {c['candidate_id']} sim={c['similarity']:.4f} {c['row_id']} "
                  f"-> {c.get('figure_image') or c.get('download_error')}")
        print(f"wrote {os.path.relpath(work_path, lib_io.project_path())}")
    if not (args.item_id or args.stats or args.rebuild_index):
        parser.error("give --item-id, --stats or --rebuild-index")
    return 0


if __name__ == "__main__":
    sys.exit(main())
