#!/usr/bin/env python3
"""Run one NCERT-mapping step (D1, D2, D4, D5, QCA) through the API, over prebuilt packets.

WHY NOT `paper_extraction/code/run_step_api.py` DIRECTLY
-------------------------------------------------------
That runner resolves its brief as `paper_extraction/agents/<name>.md` and finds its work
through `step_plugins`. The Stage D briefs live in THIS module's `agents/`, and the plugins
cannot see these papers at all -- `run_step.py D1 --list` reports "every ready question's
subject has zero chapters indexed", because a finished export is not a pipeline record. So
this driver keeps the two things that are actually shared -- `one()`, which sends one input and
writes one output, and `load_env()` -- and supplies the brief and the work list itself. The
briefs are NOT copied: both paths read `agents/<name>.md` from the module that owns the step.

Usage:
    python3 code/run_ncert_step_api.py D1 --paper 2024_S1 --limit 2 --dry-run
    python3 code/run_ncert_step_api.py D1 --paper 2024_S1
    python3 code/run_ncert_step_api.py QCA --paper 2024_S1 --concurrency 8
"""

import argparse
import concurrent.futures
import glob
import os
import sys
import time

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(HERE))
PX = os.path.join(REPO, "data_flow", "paper_extraction", "code")
sys.path.insert(0, PX)

import run_step_api as api          # noqa: E402  -- `one()` and `load_env()` only


def brief_for(step):
    """(agent, system prompt) from THIS module's steps.yaml and THIS module's agents/."""
    import yaml
    cfg = yaml.safe_load(open(os.path.join(HERE, "config", "steps.yaml"), encoding="utf-8"))
    agent = (cfg.get(step) or {}).get("agent")
    if not agent:
        sys.exit("step %s declares no single agent in config/steps.yaml" % step)
    path = os.path.join(HERE, "agents", "%s.md" % agent)
    if not os.path.exists(path):
        sys.exit("no brief at %s" % path)
    text = open(path, encoding="utf-8").read()
    if text.startswith("---"):                     # front matter declares tools this path
        end = text.find("\n---", 3)                # does not grant, so it is dropped
        if end != -1:
            text = text[end + 4:]
    return agent, text.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("step")
    ap.add_argument("--paper", required=True)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--concurrency", type=int, default=6)
    ap.add_argument("--max-tokens", type=int, default=8000)
    ap.add_argument("--model", default=None)
    ap.add_argument("--redo", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    work = os.path.join(HERE, "steps", a.step, "work")
    out_dir = os.path.join(HERE, "steps", a.step, "out")
    ins = sorted(glob.glob(os.path.join(work, "%s.*.input.json" % a.paper)))
    if not ins:
        sys.exit("no packets at %s/%s.*.input.json -- build them first" % (work, a.paper))

    jobs, done = [], 0
    for p in ins:
        o = os.path.join(out_dir, os.path.basename(p).replace(".input.json", ".json"))
        if os.path.exists(o) and not a.redo:
            done += 1
            continue
        jobs.append((p, o))
    # `done` IS COUNTED BEFORE --limit TRUNCATES, because the first version of this printed
    # `len(ins) - len(jobs)` as "already done" and so reported a --limit 2 run over 100 fresh
    # packets as "98 already done". A runner that overstates its own progress is worse than
    # one that fails.
    held = 0
    if a.limit:
        held = max(0, len(jobs) - a.limit)
        jobs = jobs[:a.limit]

    agent, system = brief_for(a.step)
    env = api.load_env()
    # SAME RESOLUTION AS run_step_api.py: .env decides, so both paths move together when
    # the model changes. A hardcoded default here would silently diverge from the briefs.
    model = a.model or os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5")
    key = os.environ.get("ANTHROPIC_API_KEY")
    print("step %s  agent %s" % (a.step, agent))
    print("  brief     : agents/%s.md  (%d chars)" % (agent, len(system)))
    print("  packets   : %d found, %d already done, %d to run%s"
          % (len(ins), done, len(jobs),
             ("  (%d held back by --limit)" % held) if held else ""))
    print("  model     : %s" % model)
    print("  env       : %s   api key: %s" % (env or "none", "yes" if key else "NO"))
    if a.dry_run or not jobs:
        for p, o in jobs[:3]:
            print("    %s -> %s" % (os.path.basename(p), os.path.basename(o)))
        print("(dry run)" if a.dry_run else "(nothing to do)")
        return 0
    if not key:
        sys.exit("no ANTHROPIC_API_KEY")

    import anthropic
    client = anthropic.Anthropic(api_key=key)
    os.makedirs(out_dir, exist_ok=True)
    t0 = time.time()
    ok = fail = tin = tout = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.concurrency) as pool:
        futs = [pool.submit(api.one, client, model, system, p, o, a.max_tokens)
                for p, o in jobs]
        for f in concurrent.futures.as_completed(futs):
            name, status, i_tok, o_tok = f.result()
            tin += i_tok
            tout += o_tok
            if status == "ok":
                ok += 1
            else:
                fail += 1
                print("  %-40s %s" % (name, status))
    print("\n  %d ok, %d failed in %.0fs" % (ok, fail, time.time() - t0))
    print("  tokens: %s in, %s out" % (f"{tin:,}", f"{tout:,}"))
    print("\n  NOT VERIFIED -- check the outputs before trusting them.")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
