---
description: Run one step for every item that needs it. Usage: /run-step <STEP> [--chapters X] [--papers Y] [--items Z]
argument-hint: <STEP> [filters]
---
1. Run `python scripts/run_step.py $ARGUMENTS --list`. If it prints AUTO, run `python scripts/run_step.py $ARGUMENTS --auto` instead and go to step 4.
2. For each printed line (item | agent | input | output | run), in order, invoke the named subagent with exactly:
   `Use the <agent> subagent. Input: <input path>. Output: <output path>. Do nothing else.`
3. Run `python scripts/run_step.py $ARGUMENTS --check`. If it prints a new list, repeat step 2 for it, then --check again, until it prints DONE.
4. Report as docs/SPEC.md Section 19 says.
Never answer a judgement yourself; never skip, reorder or add items.
