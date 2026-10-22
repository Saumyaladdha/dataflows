---
description: Apply reviewer decisions and run the cascade (Stage F3).
---
1. Run `python scripts/apply_review.py`. It applies review/decisions.csv, writes review/corrections.jsonl and prints the stale (item, step) list.
2. Re-run the stale steps in stage order exactly as /run-step does (use --items).
3. Run `python scripts/compute_counts.py` for affected subtopics.
4. Run `python scripts/build_review_pack.py --new-only` and report the new flags.
