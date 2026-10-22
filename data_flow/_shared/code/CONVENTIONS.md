# Conventions for script-only steps (`run_step.py <STEP> --auto`)

This file is the contract between `run_step.py` (the runner) and every step-only script it
invokes, so scripts can be built in parallel without seeing the runner's code, and the runner
can be built without seeing the scripts. If anything here turns out to be wrong once both sides
exist, reconcile by editing this file and both sides together — don't let one side silently
drift from it.

## Who this applies to

Every step in `config/steps.yaml` whose `agent` field is exactly `"script"` (pure script, no
agent call at all): currently **S0**, **A7**, **A9**. (Steps whose `agent` field mixes script and
agent, e.g. A5 `"script | a5-passage-linker"` or A6 `"script + x-adjudicator"`, are hybrids —
`run_step.py` calls their script half the same way, as described below, but may also produce
`--list` lines for the agent half.)

## The calling convention

A script-only step's real implementation is one Python script at a fixed path under `scripts/`,
named in that step's own section of `docs/SPEC.md` (e.g. A6 → `scripts/pair_passages.py`, A7 →
`scripts/diff_pairs.py`, A9 → `scripts/write_change_log.py`; S0 → `scripts/intake_check.py`).

`run_step.py <STEP> --auto` invokes it once per item in scope (after applying any
`--chapters`/`--papers`/`--items` filter), as a **subprocess**, like this:

```
python3 scripts/<script_name>.py --chapter-id <ID>
```

or, for a step whose item isn't a chapter (S0's item is the whole `inputs/` tree, so it takes no
item argument at all):

```
python3 scripts/<script_name>.py
```

Concretely, today:

| Step | Script | Invocation |
|---|---|---|
| S0 | `scripts/intake_check.py` | `python3 scripts/intake_check.py` (no args — one run covers all of `inputs/`) |
| A6 | `scripts/pair_passages.py` | `python3 scripts/pair_passages.py --chapter-id <CHAPTER_ID>` |
| A7 | `scripts/diff_pairs.py` | `python3 scripts/diff_pairs.py --chapter-id <CHAPTER_ID>` |
| A9 | `scripts/write_change_log.py` | `python3 scripts/write_change_log.py --chapter-id <CHAPTER_ID>` |
| D3 | `scripts/fetch_passages.py` | `python3 scripts/fetch_passages.py --item-id <QID>` |
| D10 | `scripts/build_groups.py` | `python3 scripts/build_groups.py --subtopic-id <SUBTOPIC_ID>` (or `--all`) |

`<CHAPTER_ID>` is the project's real chapter id (`{SUBJ}{CLASS}-CH{nn}`, e.g. `BIO11-CH10`, spec
6.1) — the runner determines which chapter ids are in scope for the step by scanning upstream
output (e.g. for A7 it's every chapter that has an `ncert/pairs/<CHAPTER>.json` from A6) and
applying `--chapters` if given, then calls the script once per chapter id, in order.

### Rules every script-only step's script must follow

1. **Run as a plain `python3` subprocess, no special environment contract beyond `cwd` = the
   project root** (`pyq_bank/`). Resolve all paths relative to `cwd`, the same way `lib/io.py`'s
   `PROJECT_ROOT` does (so the script also works correctly if invoked directly by a person from
   the project root, not only via the runner). Use `scripts/lib/io.py`'s atomic-write helpers for
   anything you write.
2. **Exit code 0 means success.** Any non-zero exit code means the runner treats the item as
   failed for this run (no fallback chain — these steps have none per `config/steps.yaml`
   `fallback: []` — a non-zero exit is logged to `run_log.csv` and surfaces as a blocked item with
   a generic `<STEP>_SCRIPT_FAILED` note; fix the script and re-run, per spec 18.7 Recovery).
   Raise/exit non-zero only for a genuine failure (e.g. required upstream file missing) — a script
   that found nothing to do for an item it was asked to do is still success (exit 0), since
   "nothing changed" is also what idempotence requires on a second run.
3. **Write your output to exactly the path `config/steps.yaml`'s step entry implies** (its
   `Writes` line in spec Sections 8–14 / Section 6.4's data-contract path), nothing else. For the
   three steps above: A6 → `ncert/pairs/<CHAPTER>.json`; A7 → `ncert/diffs/<CHAPTER>.jsonl`; A9 →
   `ncert/change_log.csv` and `ncert/deleted_topics.csv`; S0 → `register/intake_report.md` (plus
   flags, see below).
4. **Idempotent**: running the same invocation twice in a row must produce the same output and do
   no new work the second time (spec 5.9) — check whether your output already reflects the current
   input before redoing work, the same way the runner itself does for agent-driven steps.
5. **Raise flags through `scripts/lib/flags.py::raise_flag`**, never by writing to
   `flags/flags.jsonl` directly — use the step's own flag codes from `config/steps.yaml` /
   spec Section 16 (e.g. S0 → `S0_MISSING_INPUT`; A6 has no script-raised flag code of its own
   beyond what the adjudicator path produces).
6. **May print anything to stdout/stderr** for progress — the runner does not parse your stdout at
   all; it only checks your exit code and then reads your output file(s) itself. Print as much or
   as little as is useful for a human watching a long run.
7. **Never call a subagent, never shell out to `claude`, never make a network call.** A script-only
   step is pure, deterministic, standard-library-plus-`scripts/lib` Python (spec 4 rule 2 — "one
   decision per **agent** call" — a script makes no decisions at all, only computation). Where a
   step's text describes an adjudicator in the loop (A6's weak pairs), that is handled by the
   hybrid path below, not by the script shelling out itself.
8. **Read only what your step is allowed to read** (spec Rule 3) — in practice this is automatic
   since you're reading your own already-scoped upstream files (e.g. A7 reads only the one
   chapter's `ncert/pairs/<CHAPTER>.json` and the passage files it references), not arbitrary
   project state.

### Hybrid steps (A5, A6 today)

For a hybrid step, `--auto` runs the script half exactly as above first (e.g.
`pair_passages.py --chapter-id <ID>` for A6, which does the Jaccard/Hungarian matching and writes
`ncert/pairs/<CHAPTER>.json` directly for every passage it could confidently resolve). For any
item the script could not resolve on its own (A6: a "weak" pair, similarity 0.50–0.85), the
script's convention is to still write a row for it (`result: "pair"`, `adjudicated: false`) so the
file always has exactly one entry per passage per the A6 check, but `run_step.py A6 --list`
separately looks at `ncert/pairs/<CHAPTER>.json` afterwards for weak/unresolved rows and emits
`x-adjudicator` list lines for those, the same way any other agent-driven step would. The script
itself never calls or waits on the adjudicator — that happens through the normal `--list` /
agent-call / `--check` loop, same as any agent step.

D3 (`fetch_passages.py`) is a hybrid of a different shape: its item is a QUESTION, not a chapter
(hence `--item-id <QID>` instead of `--chapter-id`, per this file's own escape hatch below), and
its escape-hatch agent is `d2-subtopic-picker` (a STEP D2 call, not a step-owned adjudicator) —
spec 12/D3's own "On failure: zero latest passages → re-run D2 once". `fetch_passages.py` itself
never dispatches that call (rule 7 above still holds): it always writes `steps/D3/out/<QID>.json`
(even with an empty `latest` list) and exits 0; `step_plugins.D3Plugin.check()` is the one that
notices an empty `latest`, writes the `d2-subtopic-picker` work file with
`note_from_runner: "previous subtopics had no passages"`, and — once that call is answered — calls
`fetch_passages.fetch_for_item()` directly, in-process, to re-fetch with the revised subtopics
before re-checking. Still zero after that one retry → blocked, `D3_NO_PASSAGES`, no further retry.

D10 (`build_groups.py`) is the one genuinely PURE script step in Stage D (`agent: "script"`, spec
12/D10 ends "No judgement."). Its item is a SUBTOPIC, hence `--subtopic-id <ID>` under the same
escape hatch as D3's `--item-id`; `--all` does every subtopic that has a D9-resolved question, for
hand-running it standalone. It reads each canonical question record's own `d9_possible_repeats`
and `d2_subtopic_ids`, takes the union-find closure within one subtopic, and writes
`steps/D10/out/<SUBTOPIC_ID>.json`. One wrinkle worth knowing because it is easy to get wrong:
repeat-group ids are COUNTER-BACKED and never reused (`lib/ids.py::next_repeat_group_id`, spec
6.1), so blindly re-minting on every run would burn ids and change the file on a no-op rerun
(violating rule 4 above). The script therefore reads its own previous output first and reuses the
`group_id` of any component whose member set is exactly unchanged. `step_plugins.D10Plugin` also
imports `build_groups.subtopics_with_work()` in-process (only that function) so `--list`/`--check`
and the script can never disagree about which subtopics have work; the group building itself is
still a subprocess call, per rule 1.

## Why this shape

- A fixed `--chapter-id <ID>` flag (rather than e.g. passing a work-item JSON path) keeps a
  script-only step's CLI trivial to hand-build and test standalone (`python3 scripts/diff_pairs.py
  --chapter-id BIO11-CH10` from a terminal, no runner needed), while still letting the runner
  drive it item-by-item and filter with `--chapters`.
- Exit code as the only success signal (no stdout parsing) is the simplest contract that still
  lets scripts log freely for humans.
- Writing to the spec-mandated path directly (not to `steps/<STEP>/out/`) matches how Sections
  8–14 and 6.4 actually describe these steps' outputs — unlike the agent-driven steps, a
  script-only step's real artifact already has a fixed home in `ncert/`, `register/`, etc.

If your script's natural shape doesn't fit `--chapter-id` (for instance if `write_change_log.py`
needs both a chapter id and something else), add the extra flag and send a note back so this file
gets updated to match — this file is the source of truth for the calling convention, so whichever
side changes first should update it in the same change.

## Note from building A6/A7/A9 (2026-10-09)

All three scripts (`pair_passages.py`, `diff_pairs.py`, `write_change_log.py`) now run correctly
as exactly `python3 scripts/<script>.py --chapter-id <ID>`, no other required flags, confirmed
against hand-built fixtures for `BIO12-CH06` and `BIO12-CH13` (passages/links for both editions
under `ncert/passages/`, `ncert/links/`; see those chapters' output under `ncert/pairs/`,
`ncert/diffs/`, `ncert/change_log.csv`, `ncert/deleted_topics.csv`).

One gap this surfaced and resolved: **A9 (`write_change_log.py`) needs A8's resolved judgements**,
but A8 is an agent step not built in this project and the spec gives no fixed per-chapter
aggregate path for its output (A8's own item is one pair, not a chapter — spec 5.8's
`steps/<STEP>/out/<ITEM>.<run>.json` pattern doesn't name a chapter-level file). Rather than add a
required flag (which would have broken the bare `--chapter-id` invocation above),
`write_change_log.py` defines its own default input path for this:
**`steps/A8/out/<CHAPTER_ID>.judgements.json`** — a JSON array of A8-shaped objects
(`schemas/A8.json`'s fields, `change_type` already resolved, never `"unsure"`), one per
non-identical pair from that chapter's A7 diffs. `--judgements <path>` still exists to override it
for testing. If `run_step.py` ends up assembling A8's results differently (e.g. one file per pair
under `steps/A8/out/` that something else aggregates, or a different path entirely), either write
the aggregate to that path before calling `write_change_log.py`, or re-point it with
`--judgements`; update this note if the convention settles somewhere else.

A6 (`pair_passages.py`) additionally writes an adjudication-request file to
`steps/A6/work/<CHAPTER>__<old_passage_id>__<new_passage_id>.input.json` (in `x-adjudicator`'s own
input shape) for every weak pair (0.50–0.85), as a byproduct of applying the step's own
"weak + unsure → keep as pair, `A6_WEAK_PAIR`" default (via `scripts/lib/flags.py`, deduplicated
across reruns). Per this file's own "Hybrid steps" section above, `run_step.py A6 --list` is
expected to build its own `x-adjudicator` input directly from `ncert/pairs/<CHAPTER>.json`'s weak
rows rather than read these work files — so treat them as an informational trail only
(`adjudicated` stays `false` until something rewrites the pairs file), not as something the
runner needs to consume. `pair_passages.py` also accepts `--adjudications <path>` (a JSON array of
already-resolved `x-adjudicator`-shaped `{old_passage_id, new_passage_id, choice: "A"|"B"|"unsure"}`
rows) and will honour `"A"` (pair, `adjudicated: true`) / `"B"` (split into removed+added,
`adjudicated: true`) if the runner's resolution step chooses to re-invoke the script that way
instead of patching `ncert/pairs/<CHAPTER>.json` directly — either mechanism works against the
same file shape.
