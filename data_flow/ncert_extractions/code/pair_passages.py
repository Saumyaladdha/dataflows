#!/usr/bin/env python3
"""A6 - pair old and new NCERT passages within one chapter (spec docs/SPEC.md Section 9/A6,
6.4, schemas/A6.json).

SCRIPT-only matching, with the shared x-adjudicator used (by the run_step.py loop, not by this
script) only for "weak" candidates. Procedure, per spec:

  Within each subtopic (and among "none"-linked passages, for removals), compute
  similarity = Jaccard on word 3-grams after normalise_quote; solve a one-to-one assignment
  (Hungarian). >= 0.85 -> pair. 0.50-0.85 -> weak -> adjudicator ("same idea / not same /
  unsure"). < 0.50 for all candidates -> removed (older) or added (latest). Also map older
  chapter titles to latest chapter ids.

This script performs the deterministic matching and threshold classification itself (SCRIPT).
It does not call any agent directly -- no script in this project does (spec 5.1/5.2: only the
main Claude Code session invokes subagents, driven by run_step.py's --list/--check loop). For
every "weak" candidate this script instead:
  1. writes an adjudication request file under steps/A6/work/, in the exact input shape
     x-adjudicator expects (spec 5.6/x-adjudicator agent file), so the interactive loop can
     pick it up once it exists, and
  2. applies spec 9/A6's own documented on-failure default for the "unsure" case -- "weak +
     unsure -> keep as pair, A6_WEAK_PAIR (normal)" -- immediately, via a deduplicated flag.

If a resolved adjudication is already available (e.g. a prior x-adjudicator run), pass it via
--adjudications and this script will honour it ("A" = same idea -> pair, adjudicated=true;
"B" = not the same idea -> split into removed+added, adjudicated=true) instead of the default.
This keeps the script idempotent and usable standalone, while staying wired for the real loop.

Usage:
    python3 scripts/pair_passages.py --chapter-id BIO12-CH06
    python3 scripts/pair_passages.py --chapter-id BIO12-CH06 --old-chapter-title Evolution
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import flags as lib_flags
from lib import io as lib_io
from lib.text_normalise import normalise_quote

try:
    from scipy.optimize import linear_sum_assignment
except ImportError:  # pragma: no cover - exercised only when scipy truly isn't installed
    linear_sum_assignment = None

PAIR_THRESHOLD_DEFAULT = 0.85
WEAK_THRESHOLD_DEFAULT = 0.50
PROMPT_VERSION = "v1"

CHAPTER_ID_RE = re.compile(r"^([A-Z]{3})(1[12])-CH(\d{2})$")


def derive_book_ids(chapter_id):
    """{SUBJ}{CLASS}-CH{nn} -> ({SUBJ}{CLASS}O, {SUBJ}{CLASS}L), per spec 6.1's book/chapter ID
    patterns (older edition letter O, latest edition letter L)."""
    m = CHAPTER_ID_RE.match(chapter_id)
    if not m:
        raise ValueError(f"chapter_id {chapter_id!r} does not match {{SUBJ}}{{CLASS}}-CH{{nn}}")
    subj, cls, _ = m.groups()
    return f"{subj}{cls}O", f"{subj}{cls}L"


def word_trigrams(text):
    """Word 3-grams of `text` after normalise_quote (spec 9/A6). Passages shorter than 3 words
    fall back to a single gram of all their words, so short passages never produce an empty set
    on both sides by construction alone (two passages can still be genuinely unrelated)."""
    words = normalise_quote(text).split()
    if len(words) >= 3:
        return {tuple(words[i:i + 3]) for i in range(len(words) - 2)}
    if words:
        return {tuple(words)}
    return set()


def jaccard(a, b):
    """Jaccard similarity of two sets. Two passages with no words at all are trivially identical
    (1.0); one empty and one non-empty are trivially unrelated (0.0)."""
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def load_passages(book_id, chapter_id, passages_dir=None):
    """Every passage of `book_id` whose chapter_id is `chapter_id` (ncert/passages/<BOOK>.jsonl,
    spec 6.4). Chapter ids are latest-edition numbering for both editions (the mapping from an
    older book's own printed chapter number to the shared chapter_id is assumed already settled
    by the time A3 cuts passages; this script's own job re: chapter identity is only to record
    the older *title* against that chapter_id -- see update_chapter_title_mapping)."""
    path = os.path.join(passages_dir or lib_io.project_path("ncert", "passages"), f"{book_id}.jsonl")
    return [p for p in lib_io.read_jsonl(path) if p.get("chapter_id") == chapter_id]


def load_links(book_id, links_dir=None):
    """passage_id -> subtopic_id (or 'none') from ncert/links/<BOOK>.jsonl (spec 6.4)."""
    path = os.path.join(links_dir or lib_io.project_path("ncert", "links"), f"{book_id}.jsonl")
    return {row["passage_id"]: row.get("subtopic_id", "none") for row in lib_io.read_jsonl(path)}


def group_by_subtopic(passages, links):
    """Group passages by their own linked subtopic_id ('none' passages form their own group, so
    they compete for removal/addition only against each other -- spec 9/A6: 'within each
    subtopic (and among none-linked passages for removals)')."""
    groups = {}
    for p in passages:
        st = links.get(p["passage_id"], "none")
        groups.setdefault(st, []).append(p)
    return groups


def _greedy_assignment(sim):
    """Fallback one-to-one assignment (greedy, highest-similarity-first) used only if scipy is
    unavailable. scipy.optimize.linear_sum_assignment (true Hungarian) is preferred and used
    whenever importable."""
    n = len(sim)
    m = len(sim[0]) if sim else 0
    candidates = sorted(
        ((sim[i][j], i, j) for i in range(n) for j in range(m)), key=lambda t: t[0], reverse=True
    )
    used_r, used_c = set(), set()
    row_ind, col_ind = [], []
    for _s, i, j in candidates:
        if i in used_r or j in used_c:
            continue
        used_r.add(i)
        used_c.add(j)
        row_ind.append(i)
        col_ind.append(j)
    return row_ind, col_ind


def _solve_assignment(sim):
    if linear_sum_assignment is not None:
        cost = [[1.0 - s for s in row] for row in sim]
        row_ind, col_ind = linear_sum_assignment(cost)
        return list(row_ind), list(col_ind)
    return _greedy_assignment(sim)  # pragma: no cover - only without scipy


def _row_best(sim, i):
    return max(sim[i]) if sim[i] else 0.0


def _col_best(sim, j):
    col = [row[j] for row in sim]
    return max(col) if col else 0.0


def assign_within_group(old_list, new_list, pair_threshold, weak_threshold):
    """One subtopic group's old/new passages -> (pairs, weak, removed, added).
    pairs/weak: list of (old_passage, new_passage, similarity).
    removed: list of (old_passage, best_similarity_found) -- old passages with no acceptable
      match anywhere in this group.
    added: list of (new_passage, best_similarity_found) -- same, for new passages.
    """
    if not old_list and not new_list:
        return [], [], [], []
    if not old_list:
        return [], [], [], [(p, 0.0) for p in new_list]
    if not new_list:
        return [], [], [(p, 0.0) for p in old_list], []

    old_grams = [word_trigrams(p["text"]) for p in old_list]
    new_grams = [word_trigrams(p["text"]) for p in new_list]
    sim = [[jaccard(og, ng) for ng in new_grams] for og in old_grams]

    row_ind, col_ind = _solve_assignment(sim)

    matched_old_idx, matched_new_idx = set(), set()
    pairs, weak = [], []
    for r, c in zip(row_ind, col_ind):
        s = sim[r][c]
        if s >= pair_threshold:
            pairs.append((old_list[r], new_list[c], s))
        elif s >= weak_threshold:
            weak.append((old_list[r], new_list[c], s))
        else:
            # Hungarian's own best assignment for this row/column is still below the weak
            # threshold: this is exactly spec 9/A6's "< 0.50 for all candidates" case, so
            # neither side counts as matched to anything.
            continue
        matched_old_idx.add(r)
        matched_new_idx.add(c)

    removed = [(old_list[i], _row_best(sim, i)) for i in range(len(old_list)) if i not in matched_old_idx]
    added = [(new_list[j], _col_best(sim, j)) for j in range(len(new_list)) if j not in matched_new_idx]
    return pairs, weak, removed, added


def _adjudication_work_path(chapter_id, old_p, new_p):
    return lib_io.project_path(
        "steps", "A6", "work", f"{chapter_id}__{old_p['passage_id']}__{new_p['passage_id']}.input.json"
    )


def _write_adjudication_work_file(chapter_id, old_p, new_p, sim):
    """Write the weak-pair adjudication request in x-adjudicator's own input shape (its agent
    file, .claude/agents/x-adjudicator.md: step, allowed_values, evidence, run_a/run_b or
    reading_a/reading_b, failed_check). A6 has no two runs to disagree -- the two "readings"
    offered are the two possible resolutions (pair it / don't), so the adjudicator is choosing
    between them from the evidence, exactly as its generic contract describes."""
    payload = {
        "step": "A6",
        "task": "Decide whether these two NCERT passages (one per edition) describe the same "
                "idea closely enough to be treated as the same passage across editions.",
        "allowed_values": {
            "choice": ["A", "B", "unsure"],
            "A": "same idea -- pair old_passage with new_passage",
            "B": "not the same idea -- do not pair them (each is removed/added instead)",
        },
        "evidence": {
            "old_passage": {"passage_id": old_p["passage_id"], "text": old_p["text"]},
            "new_passage": {"passage_id": new_p["passage_id"], "text": new_p["text"]},
            "similarity": round(sim, 4),
        },
        "run_a": None,
        "run_b": None,
        "failed_check": f"A6_WEAK_PAIR: similarity {sim:.4f} is between 0.50 and 0.85",
    }
    lib_io.atomic_write_json(_adjudication_work_path(chapter_id, old_p, new_p), payload)


def _flag_already_open(item_id, code, flags_path):
    if not os.path.exists(flags_path):
        return False
    for f in lib_io.read_jsonl(flags_path):
        if f.get("item_id") == item_id and f.get("code") == code and f.get("status") == "open":
            return True
    return False


def _raise_weak_pair_flag(chapter_id, old_p, new_p, sim, flags_path):
    item_id = f"{old_p['passage_id']}|{new_p['passage_id']}"
    if _flag_already_open(item_id, "A6_WEAK_PAIR", flags_path):
        return  # idempotent: don't re-raise on a rerun
    lib_flags.raise_flag(
        item_type="passage_pair",
        item_id=item_id,
        step="A6",
        code="A6_WEAK_PAIR",
        severity="normal",
        message=f"Similarity {sim:.4f} (0.50-0.85) in chapter {chapter_id}; no adjudication "
                f"decision available yet, so the candidate pair was kept as 'pair' per the "
                f"step's safe default.",
        provisional_value={"result": "pair", "old_passage_id": old_p["passage_id"],
                            "new_passage_id": new_p["passage_id"]},
        evidence=[_adjudication_work_path(chapter_id, old_p, new_p)],
        prompt_version=PROMPT_VERSION,
        flags_path=flags_path,
    )


def resolve_weak_pairs(weak, adjudications, chapter_id, flags_path):
    """weak: list of (old_passage, new_passage, similarity).
    adjudications: {(old_id, new_id): {"choice": "A"|"B"|"unsure", ...}} of already-decided
    x-adjudicator outputs (empty dict if none supplied -- the normal case before the real
    run_step.py loop exists).
    Returns (resolved_pairs, resolved_removed, resolved_added):
      resolved_pairs: list of (old_passage, new_passage, similarity, adjudicated_bool)
      resolved_removed / resolved_added: list of (passage, similarity) -- only populated when an
        adjudicator explicitly said "not the same" (choice B).
    """
    resolved_pairs, resolved_removed, resolved_added = [], [], []
    for old_p, new_p, sim in weak:
        _write_adjudication_work_file(chapter_id, old_p, new_p, sim)
        decision = (adjudications or {}).get((old_p["passage_id"], new_p["passage_id"]))
        choice = (decision or {}).get("choice")
        if choice == "A":
            resolved_pairs.append((old_p, new_p, sim, True))
        elif choice == "B":
            resolved_removed.append((old_p, sim))
            resolved_added.append((new_p, sim))
        else:
            # choice is "unsure", or no adjudication has been run yet at all: spec 9/A6's own
            # on-failure default -- "weak + unsure -> keep as pair, A6_WEAK_PAIR (normal)".
            resolved_pairs.append((old_p, new_p, sim, False))
            _raise_weak_pair_flag(chapter_id, old_p, new_p, sim, flags_path)
    return resolved_pairs, resolved_removed, resolved_added


def _load_adjudications(path):
    with open(path, "r", encoding="utf-8") as f:
        rows = json.load(f)
    return {(r["old_passage_id"], r["new_passage_id"]): r for r in rows}


def _pair_entry(old_p, new_p, sim, adjudicated):
    return {
        "old_passage_id": old_p["passage_id"],
        "new_passage_id": new_p["passage_id"],
        "similarity": round(sim, 4),
        "result": "pair",
        "adjudicated": adjudicated,
    }


def _removed_entry(old_p, sim, adjudicated):
    return {
        "old_passage_id": old_p["passage_id"],
        "new_passage_id": None,
        "similarity": round(sim, 4),
        "result": "removed",
        "adjudicated": adjudicated,
    }


def _added_entry(new_p, sim, adjudicated):
    return {
        "old_passage_id": None,
        "new_passage_id": new_p["passage_id"],
        "similarity": round(sim, 4),
        "result": "added",
        "adjudicated": adjudicated,
    }


def _entry_sort_key(e):
    return (e["old_passage_id"] or "", e["new_passage_id"] or "")


def update_chapter_title_mapping(chapter_id, old_chapter_title, chapters_dir=None):
    """Spec 9/A6: 'Also map older chapter titles to latest chapter ids.' Spec 6.4:
    ncert/chapters/<SUBJ><CLASS>.json carries an `older_title` field per latest-edition chapter
    entry. Updates (or creates a minimal stub for) that chapter's entry. No-op if no title was
    given -- this script can run per-chapter without a title on every call."""
    if not old_chapter_title:
        return None
    subj_class = chapter_id.split("-CH")[0]
    path = os.path.join(chapters_dir or lib_io.project_path("ncert", "chapters"), f"{subj_class}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            chapters = json.load(f)
    else:
        chapters = []
    for ch in chapters:
        if ch.get("chapter_id") == chapter_id:
            ch["older_title"] = old_chapter_title
            lib_io.atomic_write_json(path, chapters)
            return path
    chapters.append({"chapter_id": chapter_id, "title": None, "headings": [], "older_title": old_chapter_title})
    lib_io.atomic_write_json(path, chapters)
    return path


def pair_chapter(chapter_id, old_book=None, new_book=None, old_chapter_title=None,
                  pair_threshold=PAIR_THRESHOLD_DEFAULT, weak_threshold=WEAK_THRESHOLD_DEFAULT,
                  adjudications_path=None, passages_dir=None, links_dir=None, chapters_dir=None,
                  out_path=None, flags_path=None):
    """Run A6 for one chapter end to end and return the list of entries written (same shape as
    the output file, schemas/A6.json)."""
    default_old, default_new = derive_book_ids(chapter_id)
    old_book = old_book or default_old
    new_book = new_book or default_new

    old_passages = load_passages(old_book, chapter_id, passages_dir)
    new_passages = load_passages(new_book, chapter_id, passages_dir)
    old_links = load_links(old_book, links_dir)
    new_links = load_links(new_book, links_dir)

    old_groups = group_by_subtopic(old_passages, old_links)
    new_groups = group_by_subtopic(new_passages, new_links)

    adjudications = _load_adjudications(adjudications_path) if adjudications_path else {}
    flags_path = flags_path or lib_flags.FLAGS_PATH

    all_pairs, all_weak, all_removed, all_added = [], [], [], []
    for st in sorted(set(old_groups) | set(new_groups)):
        pairs, weak, removed, added = assign_within_group(
            old_groups.get(st, []), new_groups.get(st, []), pair_threshold, weak_threshold
        )
        all_pairs.extend(pairs)
        all_weak.extend(weak)
        all_removed.extend(removed)
        all_added.extend(added)

    resolved_pairs, weak_removed, weak_added = resolve_weak_pairs(
        all_weak, adjudications, chapter_id, flags_path
    )

    entries = []
    entries += [_pair_entry(o, n, s, False) for (o, n, s) in all_pairs]
    entries += [_pair_entry(o, n, s, adj) for (o, n, s, adj) in resolved_pairs]
    entries += [_removed_entry(p, s, False) for (p, s) in all_removed]
    entries += [_removed_entry(p, s, True) for (p, s) in weak_removed]
    entries += [_added_entry(p, s, False) for (p, s) in all_added]
    entries += [_added_entry(p, s, True) for (p, s) in weak_added]
    entries.sort(key=_entry_sort_key)

    out_path = out_path or lib_io.project_path("ncert", "pairs", f"{chapter_id}.json")
    lib_io.atomic_write_json(out_path, entries)

    update_chapter_title_mapping(chapter_id, old_chapter_title, chapters_dir)

    n_pair = len(all_pairs) + len(resolved_pairs)
    n_removed = len(all_removed) + len(weak_removed)
    n_added = len(all_added) + len(weak_added)
    print(
        f"A6 pair_passages: chapter={chapter_id} old_book={old_book} new_book={new_book} "
        f"-> pair={n_pair} (weak={len(all_weak)}) removed={n_removed} added={n_added} "
        f"wrote {out_path}"
    )
    return entries


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--chapter-id", required=True, help="e.g. BIO12-CH06")
    parser.add_argument("--old-book", help="default: derived as {SUBJ}{CLASS}O from --chapter-id")
    parser.add_argument("--new-book", help="default: derived as {SUBJ}{CLASS}L from --chapter-id")
    parser.add_argument("--old-chapter-title", help="older edition's own title for this chapter, "
                                                      "for ncert/chapters/<SUBJ><CLASS>.json's older_title")
    parser.add_argument("--pair-threshold", type=float, default=PAIR_THRESHOLD_DEFAULT)
    parser.add_argument("--weak-threshold", type=float, default=WEAK_THRESHOLD_DEFAULT)
    parser.add_argument("--adjudications", help="optional JSON file of already-resolved x-adjudicator "
                                                  "outputs for weak pairs (list of {old_passage_id, "
                                                  "new_passage_id, choice, ...})")
    parser.add_argument("--passages-dir", help="override ncert/passages (testing)")
    parser.add_argument("--links-dir", help="override ncert/links (testing)")
    parser.add_argument("--chapters-dir", help="override ncert/chapters (testing)")
    parser.add_argument("--out", help="override output path (default ncert/pairs/<CHAPTER>.json)")
    parser.add_argument("--flags-path", help="override flags/flags.jsonl (testing)")
    args = parser.parse_args()

    try:
        pair_chapter(
            chapter_id=args.chapter_id,
            old_book=args.old_book,
            new_book=args.new_book,
            old_chapter_title=args.old_chapter_title,
            pair_threshold=args.pair_threshold,
            weak_threshold=args.weak_threshold,
            adjudications_path=args.adjudications,
            passages_dir=args.passages_dir,
            links_dir=args.links_dir,
            chapters_dir=args.chapters_dir,
            out_path=args.out,
            flags_path=args.flags_path,
        )
    except (FileNotFoundError, ValueError, KeyError) as exc:
        print(f"A6 pair_passages FAILED for chapter {args.chapter_id}: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
