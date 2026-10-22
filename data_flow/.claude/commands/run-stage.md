---
description: Run every step of a stage in order. Usage: /run-stage <0|A|B|C|D|E|smoke> [filters]
argument-hint: <stage> [filters]
---
Run `python scripts/run_stage.py $ARGUMENTS --plan` to get the ordered steps. For each step follow /run-step exactly. Stop if a step prints STOP and report why.
