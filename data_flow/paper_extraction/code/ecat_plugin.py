"""ECAT's step plugin: category rating over PRE-BUILT GROUP PACKETS.

Kept in its own module rather than appended to the 11k-line `scripts/step_plugins.py`, and wired in
from `get_plugins()`. ECAT does not fit the shape of the other E plugins, which all derive one item
per question from `papers/records/`:

  * ITS ITEM IS A GROUP, NOT A QUESTION. `scripts/build_ecat_packets.py` turns the 580 rated
    questions into 45 (subject x E1 type) groups and 120 packets of at most six. The grouping is the
    point: docs/question_categories/RULEBOOK.md rule 0.7 requires similar questions to be judged
    against each other, because v1 was tagged in paper order and gave one match-list question
    `check_each_statement` and another `elimination` with no stated reason for the difference.

  * ITS INPUTS ALREADY EXIST ON DISK. The other E plugins build an agent input per item at --list
    time. ECAT's are built in one pass, so --list enumerates `steps/ECAT/work/*.runA.input.json`
    and never writes one. That also means the packets are reproducible and reviewable before a
    single agent runs, which matters for 120 of them.

  * IT WRITES NO RECORD FIELDS. The other E steps store tags onto `papers/records/`. ECAT fills the
    judgement columns of `docs/question_categories/SHEET_V2.csv`, which `--auto` merges once the
    outputs exist, so a half-finished run leaves the sheet untouched rather than partly rewritten.
"""

import collections
import glob
import json
import os
import sys

import runner_core as rc

ListLine = collections.namedtuple(
    "ListLine", ["item_id", "agent", "input_path", "output_path", "run_label"])

WORK = ("steps", "ECAT", "work")
OUT = ("steps", "ECAT", "out")
SHEET = ("docs", "question_categories", "SHEET_V2.csv")

#: the sheet columns ECAT owns. Everything else on the row is script-derived and must not be touched.
AGENT_COLUMNS = ["E3_concept", "E4a_cognitive_demand", "E4b_solution_structure",
                 "E4c_strategy_available", "E5_traps", "E5_trap_routes"]


class ECATPlugin:
    step = "ECAT"
    agent = "e-category-rater"

    # ------------------------------------------------------------------ listing
    def _packets(self, filters=None):
        """{item_id: input path}, for every built packet, honouring --items."""
        wanted = set((filters or {}).get("items") or [])
        out = {}
        for path in sorted(glob.glob(rc.pp(*WORK, "*.runA.input.json"))):
            item_id = os.path.basename(path).replace(".runA.input.json", "")
            if wanted and item_id not in wanted:
                continue
            out[item_id] = path
        return out

    def _out_path(self, item_id):
        return rc.pp(*OUT, "%s.runA.json" % item_id)

    def list_items(self, filters):
        lines = []
        for item_id, path in self._packets(filters).items():
            if os.path.exists(self._out_path(item_id)):
                continue
            lines.append(ListLine(item_id, self.agent,
                                  os.path.relpath(path, rc.pp()),
                                  os.path.relpath(self._out_path(item_id), rc.pp()), "runA"))
        return lines

    def list_reason(self):
        packets = self._packets()
        if not packets:
            return ("ECAT has no packets. Build them first: "
                    "`python3 scripts/build_ecat_packets.py --apply` (it reads "
                    "docs/question_categories/SHEET_V2.csv, which "
                    "scripts/build_category_sheet_v2.py --apply writes).")
        done = sum(1 for i in packets if os.path.exists(self._out_path(i)))
        return ("ECAT: all %d packet(s) already have output. Run `run_step.py ECAT --check` to "
                "validate them, then `--auto` to merge the ratings into "
                "docs/question_categories/SHEET_V2.csv." % done)

    # ------------------------------------------------------------------ checking
    def check(self, filters):
        """Validate every output that exists; re-list anything that failed."""
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
        import ECAT as ecat_check
        import jsonschema

        schema = json.load(open(rc.pp("schemas", "ECAT.json"), encoding="utf-8"))
        failed, passed = [], 0
        for item_id, in_path in self._packets(filters).items():
            out_path = self._out_path(item_id)
            if not os.path.exists(out_path):
                continue
            packet = json.load(open(in_path, encoding="utf-8"))
            try:
                data = json.load(open(out_path, encoding="utf-8"))
            except ValueError as exc:
                failed.append((item_id, in_path, "output is not valid JSON: %s" % exc))
                continue
            try:
                jsonschema.validate(data, schema)
            except jsonschema.ValidationError as exc:
                failed.append((item_id, in_path, "schema: %s" % exc.message))
                continue
            ok, message = ecat_check.check(data, item=packet, root=rc.pp())
            if ok:
                passed += 1
                print("ECAT %-34s PASS  %s" % (item_id, message), file=sys.stderr)
            else:
                failed.append((item_id, in_path, message))

        for item_id, in_path, message in failed:
            print("ECAT %-34s FAIL  %s" % (item_id, message), file=sys.stderr)
        total = len(self._packets(filters))
        waiting = total - passed - len(failed)
        print("ECAT --check: %d passed, %d failed, %d packet(s) still without output (of %d)"
              % (passed, len(failed), waiting, total), file=sys.stderr)

        # Re-list the failures so the runner's loop dispatches them again, with the check message
        # carried in the input so the agent is told exactly what to fix (Universal rule 9).
        lines = []
        for item_id, in_path, message in failed:
            packet = json.load(open(in_path, encoding="utf-8"))
            packet["PREVIOUS ATTEMPT FAILED"] = message
            retry = rc.pp(*WORK, "%s.retry1.input.json" % item_id)
            with open(retry, "w", encoding="utf-8") as fh:
                json.dump(packet, fh, ensure_ascii=False, indent=1)
            lines.append(ListLine(item_id, self.agent, os.path.relpath(retry, rc.pp()),
                                  os.path.relpath(self._out_path(item_id), rc.pp()), "retry1"))
        return lines

    # ------------------------------------------------------------------ merging
    def auto(self, filters):
        """Merge passing ratings into SHEET_V2.csv. All-or-nothing per column, by design.

        A half-finished run must not leave the sheet half-rewritten: a reader cannot tell a blank
        that means "not yet judged" from one that means "judged and undecidable" (SPEC Rule 19), and
        the sheet is the artefact people read. So the merge refuses while any packet is unrated, and
        says how many are outstanding.
        """
        import csv
        packets = self._packets(filters)
        missing = [i for i in packets if not os.path.exists(self._out_path(i))]
        if missing:
            print("ECAT --auto: %d of %d packet(s) have no output yet, so the sheet is left "
                  "untouched. Outstanding: %s%s"
                  % (len(missing), len(packets), ", ".join(sorted(missing)[:5]),
                     " ..." if len(missing) > 5 else ""), file=sys.stderr)
            return

        ratings = {}
        for item_id in packets:
            data = json.load(open(self._out_path(item_id), encoding="utf-8"))
            for r in (data.get("ratings") or []):
                ratings[r.get("question_id")] = r

        path = rc.pp(*SHEET)
        rows = list(csv.DictReader(open(path, encoding="utf-8")))
        fields = list(rows[0].keys())
        for column in AGENT_COLUMNS + ["ECAT_verdicts", "ECAT_group_note"]:
            if column not in fields:
                fields.append(column)

        filled = 0
        for row in rows:
            r = ratings.get(row["question_id"])
            if not r:
                continue
            filled += 1
            row["E3_concept"] = r.get("concept") or ""
            row["E4a_cognitive_demand"] = r.get("cognitive_demand") or ""
            row["E4b_solution_structure"] = r.get("solution_structure") or ""
            row["E4c_strategy_available"] = "; ".join(r.get("strategy_available") or [])
            row["E5_traps"] = "; ".join(t["label"] for t in (r.get("traps") or []))
            row["E5_trap_routes"] = " | ".join(
                "%s@%s: %s" % (t["label"], t["option"], t["route"]) for t in (r.get("traps") or []))
            row["ECAT_verdicts"] = "; ".join(r.get("verdicts") or [])

        with open(path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        print("ECAT --auto: merged %d rating(s) into %s"
              % (filled, os.path.join(*SHEET)), file=sys.stderr)
