#!/usr/bin/env python3
"""Run one agent step through the API instead of through Claude Code subagents.

    python3 code/run_step_api.py B3V --paper 2026_11 --limit 3 --dry-run
    python3 code/run_step_api.py B3V --paper 2026_11 --limit 3
    python3 code/run_step_api.py B3V --paper 2026_11            # the whole step

WHY THIS EXISTS
---------------
Every agent in `agents/` declares `tools: Read, Write` and nothing else. Measured across all 30:
not one searches the repo, runs a script, or reacts to what it finds. Each is a pure function --
read one input file (and perhaps one image), write one output file.

A Claude Code subagent carries a whole agent loop to do that, and one paper costs about 1,164 of
them (180 each for B3V, B3S, B6V, QCHAP, QTOPIC, plus the packet steps and the figures). The loop
is the expensive part and none of it is used.

So this sends the same brief and the same input to the API directly. The briefs are untouched --
the same `agents/<name>.md` file drives both paths, so nothing has to be kept in sync.

WHAT STAYS WITH THE ORCHESTRATOR
--------------------------------
Everything that caught a real fault in this corpus: that 23 figure crops contained the printed
answer and so defeated the blind solve; that ECAT packets shipped with `correct_answer: null` and
43 questions were rated without a key; that a change log compared two unrelated chapters and its
186 rows were worthless. None of those were found by an agent. They were found by running a check
over what the agents produced. This script does not do that, and must not be mistaken for doing it
-- it writes files, and they still have to be checked.
"""

import argparse
import base64
import concurrent.futures
import glob
import json
import mimetypes
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def load_env():
    """Read the repo's .env without adding a dependency. Real environment wins."""
    for up in (ROOT, os.path.dirname(ROOT), os.path.dirname(os.path.dirname(ROOT))):
        p = os.path.join(up, ".env")
        if not os.path.exists(p):
            continue
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())
        return p
    return None


def brief_for(step):
    """(agent name, system prompt) from config/steps.yaml plus agents/<name>.md."""
    import yaml
    cfg = yaml.safe_load(open(os.path.join(ROOT, "config", "steps.yaml"), encoding="utf-8"))
    entry = cfg.get(step) or {}
    agent = entry.get("agent")
    if not agent or "script" in str(agent):
        raise SystemExit("step %s has no single agent (agent=%r)" % (step, agent))
    path = os.path.join(ROOT, "agents", "%s.md" % agent)
    if not os.path.exists(path):
        raise SystemExit("no brief at %s" % path)
    text = open(path, encoding="utf-8").read()
    # Drop the YAML front matter: it declares tools this path does not grant.
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    return agent, text.strip()


def image_block(rel):
    """An input's image as a content block, or None when the file is not there."""
    p = rel if os.path.isabs(rel) else os.path.join(ROOT, rel)
    if not os.path.exists(p):
        return None
    mime = mimetypes.guess_type(p)[0] or "image/png"
    with open(p, "rb") as fh:
        data = base64.standard_b64encode(fh.read()).decode("ascii")
    return {"type": "image",
            "source": {"type": "base64", "media_type": mime, "data": data}}


IMAGE_KEYS = ("question_image", "solution_image", "figure_image", "page_image", "image")


def user_content(payload):
    """The input file as the user turn: its images first, then the JSON itself."""
    blocks = []
    for k in IMAGE_KEYS:
        v = payload.get(k)
        for rel in (v if isinstance(v, list) else [v]):
            if isinstance(rel, str) and rel:
                b = image_block(rel)
                if b:
                    blocks.append(b)
    blocks.append({"type": "text", "text": json.dumps(payload, ensure_ascii=False, indent=1)})
    return blocks


def extract_json(text):
    """The JSON object an agent wrote, whether or not it fenced it."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n", "", text)
        text = re.sub(r"\n```$", "", text.strip())
    try:
        return json.loads(text)
    except ValueError:
        pass
    # last resort: the outermost braces
    i, j = text.find("{"), text.rfind("}")
    if i != -1 and j > i:
        return json.loads(text[i:j + 1])
    raise ValueError("no JSON object in the reply")


def one(client, model, system, in_path, out_path, max_tokens, retries=2):
    payload = json.load(open(in_path, encoding="utf-8"))
    last = None
    for attempt in range(retries + 1):
        try:
            msg = client.messages.create(
                model=model, max_tokens=max_tokens, system=system,
                messages=[{"role": "user", "content": user_content(payload)}])
            text = "".join(b.text for b in msg.content if b.type == "text")
            data = extract_json(text)
            with open(out_path, "w", encoding="utf-8") as fh:
                json.dump(data, fh, ensure_ascii=False, indent=1)
            return (os.path.basename(out_path), "ok",
                    msg.usage.input_tokens, msg.usage.output_tokens)
        except Exception as exc:                 # reported per item, never swallowed
            last = exc
            if attempt < retries:
                time.sleep(2 ** attempt)
    return (os.path.basename(out_path), "FAIL: %s: %s" % (type(last).__name__, last), 0, 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("step")
    ap.add_argument("--paper", help="only inputs whose name contains this")
    ap.add_argument("--limit", type=int, help="first N inputs only -- use this to test")
    ap.add_argument("--max-tokens", type=int, default=8000)
    ap.add_argument("--concurrency", type=int,
                    default=int(os.environ.get("AGENT_CONCURRENCY", "8")))
    ap.add_argument("--model", default=None)
    ap.add_argument("--redo", action="store_true", help="rewrite outputs that already exist")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    env = load_env()
    key = os.environ.get("ANTHROPIC_API_KEY")
    model = a.model or os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5")
    agent, system = brief_for(a.step)

    work = os.path.join(ROOT, "steps", a.step, "work")
    out_dir = os.path.join(ROOT, "steps", a.step, "out")
    pattern = os.path.join(work, "*%s*.input.json" % (a.paper or ""))
    inputs = sorted(glob.glob(pattern))
    jobs = []
    for p in inputs:
        o = os.path.join(out_dir, os.path.basename(p).replace(".input.json", ".json"))
        if os.path.exists(o) and not a.redo:
            continue
        jobs.append((p, o))
    if a.limit:
        jobs = jobs[:a.limit]

    print("step %s  ->  agent %s" % (a.step, agent))
    print("  brief   : agents/%s.md  (%d chars)" % (agent, len(system)))
    print("  model   : %s" % model)
    print("  env     : %s" % (env or "not found"))
    print("  inputs  : %d matching, %d to run" % (len(inputs), len(jobs)))
    if a.dry_run:
        for p, o in jobs[:5]:
            print("    would run %s" % os.path.basename(p))
        print("(dry run -- nothing sent)")
        return 0
    if not jobs:
        print("  nothing to do")
        return 0
    if not key:
        raise SystemExit("ANTHROPIC_API_KEY not set (looked in .env and the environment)")

    import anthropic
    client = anthropic.Anthropic(api_key=key)
    os.makedirs(out_dir, exist_ok=True)

    t0 = time.time()
    ok = fail = tin = tout = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.concurrency) as pool:
        futs = [pool.submit(one, client, model, system, p, o, a.max_tokens) for p, o in jobs]
        for f in concurrent.futures.as_completed(futs):
            name, status, i_tok, o_tok = f.result()
            tin += i_tok; tout += o_tok
            if status == "ok":
                ok += 1
            else:
                fail += 1
                print("  %-44s %s" % (name, status))
    print("\n  %d ok, %d failed in %.0fs" % (ok, fail, time.time() - t0))
    print("  tokens: %s in, %s out" % (f"{tin:,}", f"{tout:,}"))
    print("\n  NOT VERIFIED. Run the step's own check before trusting these:")
    print("    python3 code/run_step.py %s --check --papers %s" % (a.step, a.paper or "<paper>"))
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
