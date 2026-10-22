#!/usr/bin/env python3
"""Builds the next dispatch wave for a step, never re-assigning work already in flight.

    python3 scripts/build_wave.py A2S --size 14 --groups 6
    python3 scripts/build_wave.py A3  --size 13 --groups 6 --first BIO11L-ch01 BIO11L-ch02

Why this script exists. Dispatching a step by hand means picking "items with no output yet", and
that set is WRONG while earlier agents are still running: an item another agent is working on has
no output until it finishes, so it looks available and gets handed out twice. Measured on the real
A2S run: 30 items were assigned to two agents at once (18 across waves 2-3, 12 across waves 1-3).
Two of them collided visibly -- one worker reported "another agent is writing this same group ...
it overwrote my outputs for ch04-p003-b1, ch04-p003-b6, ch04-p004-b1, ch04-p005-b3" -- and the
rest simply burned a second agent's budget on work already done.

I first recorded those collisions as harmless, reasoning that two agents reading the same page
produce the same blocks, so the loser's file is equivalent and last-writer-wins leaves one valid
output. **That was wrong, and a later collision proved it.** On BIO11O-ch14-p009 the surviving
version had LOST its per-block `continues_from_previous` flags and its note falsely claimed the
previous page was unavailable; the agent that lost the race said so explicitly. A race decided by
write order can preserve the worse answer. Treat these as data-destroying, not merely wasteful.

How: every wave this script writes is recorded under steps/<STEP>/work/_waves/, and every later
wave excludes ids named in any previous wave file as well as ids that already have output.

--retry re-opens work stranded by a dead agent, but it is NOT "re-offer everything unfinished".
That was the trap: an agent still running has written no output, so its items look stranded. I fell
into it three times in one session -- twice after documenting why it happens -- which is why the
guard is now in the code instead of in my memory. --retry only re-offers ids from waves that have
been quiet for --retry-after minutes (default 20); ids from newer waves stay excluded. So an id is
never silently handed out twice, and never permanently stranded either.
"""

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402


def _wave_dir(step):
    d = rc.pp("steps", step, "work", "_waves")
    rc.ensure_dir(d)
    return d


def _assigned(step, quiet_minutes=None):
    """Item ids handed to some earlier wave of this step.

    With `quiet_minutes`, returns only ids from waves whose file was written at least that long
    ago -- i.e. the ones plausibly belonging to an agent that has since died rather than one still
    working. That distinction is the whole point of this function's second caller, --retry.
    """
    out = set()
    d = _wave_dir(step)
    cutoff = (time.time() - quiet_minutes * 60) if quiet_minutes else None
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".json"):
            continue
        path = os.path.join(d, fn)
        if cutoff is not None and os.path.getmtime(path) > cutoff:
            continue                       # too recent: assume its agents are still running
        try:
            with open(path, encoding="utf-8") as fh:
                out |= set(json.load(fh).get("item_ids") or [])
        except (OSError, json.JSONDecodeError):
            continue
    return out


def _has_output(step, item_id):
    for run in ("runA", "retry1", "retry2"):
        if os.path.exists(rc.pp("steps", step, "out", f"{item_id}.{run}.json")):
            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("step")
    ap.add_argument("--size", type=int, default=14, help="items per group")
    ap.add_argument("--groups", type=int, default=6, help="how many groups to emit")
    ap.add_argument("--first", nargs="*", default=[],
                    help="id prefixes to put at the front of the queue")
    ap.add_argument("--retry", action="store_true",
                    help="re-offer previously assigned ids that still have no output AND whose "
                         "wave has been quiet for --retry-after minutes")
    ap.add_argument("--retry-after", type=int, default=20, metavar="MIN",
                    help="with --retry, only re-offer ids from waves older than this many "
                         "minutes (default 20). Guards against re-assigning work an agent is "
                         "still doing, which is how the same item gets handed out twice.")
    ap.add_argument("--list-file", default=None,
                    help="read candidate ids from a saved `run_step.py --list` output "
                         "instead of re-listing (re-listing can take many minutes)")
    args = ap.parse_args()

    if args.list_file:
        with open(args.list_file, encoding="utf-8") as fh:
            candidates = [ln.split("|")[0].strip() for ln in fh if " | " in ln]
    else:
        print("no --list-file given; run `run_step.py <STEP> --list > f` first", file=sys.stderr)
        return 2

    pending = [i for i in candidates if not _has_output(args.step, i)]
    if args.retry:
        # --retry must NOT simply re-offer everything unfinished. "Has no output" never means
        # "nobody is working on it": an agent that is still running has not written its output
        # yet, so its items look stranded. I made exactly that mistake three times in one
        # session -- twice after writing down why it happens -- and the third race kept the
        # WEAKER of two outputs for BIO11O-ch14-p009, losing its per-block continuation flags.
        # So a retry only re-offers ids from waves that have been quiet for `--retry-after`
        # minutes; ids from newer waves stay excluded exactly as in a normal build.
        stale_assigned = _assigned(args.step, quiet_minutes=args.retry_after)
        fresh_assigned = _assigned(args.step) - stale_assigned
        queue = [i for i in pending if i not in fresh_assigned]
        note = (f"retry: re-offering ids from waves older than {args.retry_after} min; "
                f"held back {len(pending) - len(queue)} id(s) from waves still likely running")
    else:
        assigned = _assigned(args.step)
        queue = [i for i in pending if i not in assigned]
        note = f"excluded {len(pending) - len(queue)} ids already assigned to an earlier wave"

    # stable priority: requested prefixes first, original order within each bucket
    def rank(i):
        for n, pre in enumerate(args.first):
            if i.startswith(pre):
                return n
        return len(args.first)
    queue.sort(key=rank)

    stamp = time.strftime("%Y%m%dT%H%M%S")
    out_dir = os.path.join(_wave_dir(args.step), "")
    groups, taken = [], []
    for g in range(args.groups):
        chunk = queue[g * args.size:(g + 1) * args.size]
        if not chunk:
            break
        groups.append(chunk)
        taken += chunk

    scratch = os.environ.get("PYQ_WAVE_OUT") or rc.pp("steps", args.step, "work", "_waves", stamp)
    rc.ensure_dir(scratch)
    for n, chunk in enumerate(groups, 1):
        p = os.path.join(scratch, f"group_{n:02d}.txt")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("\n".join(chunk) + "\n")
        print(f"group_{n:02d}: {len(chunk):3d}  {p}")

    with open(os.path.join(out_dir, f"wave_{stamp}.json"), "w", encoding="utf-8") as fh:
        json.dump({"step": args.step, "stamp": stamp, "item_ids": taken,
                   "groups": len(groups), "note": note}, fh, indent=1)

    print(f"\ncandidates {len(candidates)} | no output yet {len(pending)} | "
          f"newly assigned {len(taken)}")
    print(note)
    return 0


if __name__ == "__main__":
    sys.exit(main())
