"""Reads/updates papers/records/<QID>.json, the single current record of a question (spec 5.8,
6.3). Every step that produces a question field writes it both to its own steps/<STEP>/out/ file
(history, handled by the step script itself) and into this record (current value), together with
a field_sources entry recording the step, prompt version and status that produced it.
"""
import json
import os

from . import io as lib_io


def record_path(question_id, project_root=None):
    """Return the path to a question's record: papers/records/<QID>.json."""
    root = project_root or lib_io.PROJECT_ROOT
    return os.path.join(root, "papers", "records", f"{question_id}.json")


def read_record(question_id, project_root=None):
    """Return the current record for a question as a dict, or a fresh empty-skeleton record
    (with just question_id and an empty field_sources) if none exists yet."""
    path = record_path(question_id, project_root)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"question_id": question_id, "field_sources": {}}


def set_field(question_id, field, value, step, prompt_version, status="pass", project_root=None):
    """Merge one field's value into a question's record (creating the record if it doesn't exist
    yet), and write the matching field_sources entry {step, prompt_version, status} for that
    field. Returns the updated record."""
    return set_fields(question_id, {field: value}, step, prompt_version, status, project_root)


def set_fields(question_id, fields, step, prompt_version, status="pass", project_root=None):
    """Merge several fields at once, all attributed to the same step/prompt_version/status —
    one field_sources entry is written per field. Returns the updated record."""
    record = read_record(question_id, project_root)
    record["question_id"] = question_id
    record.update(fields)
    sources = record.setdefault("field_sources", {})
    for field in fields:
        sources[field] = {"step": step, "prompt_version": prompt_version, "status": status}
    lib_io.atomic_write_json(record_path(question_id, project_root), record)
    return record


if __name__ == "__main__":
    import shutil
    import tempfile

    tmp_root = tempfile.mkdtemp(prefix="records_selfcheck_")
    try:
        qid = "Q-000123"
        fresh = read_record(qid, project_root=tmp_root)
        assert fresh == {"question_id": qid, "field_sources": {}}

        rec = set_field(qid, "official_answer", "1", step="B5", prompt_version="v1",
                         status="pass", project_root=tmp_root)
        assert rec["official_answer"] == "1"
        assert rec["field_sources"]["official_answer"] == {
            "step": "B5", "prompt_version": "v1", "status": "pass"
        }

        rec2 = set_fields(qid, {"stem_en": "...", "structure": "plain"}, step="B3",
                           prompt_version="v2", status="flagged", project_root=tmp_root)
        assert rec2["stem_en"] == "..." and rec2["structure"] == "plain"
        for f in ("stem_en", "structure"):
            assert rec2["field_sources"][f] == {"step": "B3", "prompt_version": "v2", "status": "flagged"}
        # earlier field must survive the second, unrelated update
        assert rec2["official_answer"] == "1"
        assert rec2["field_sources"]["official_answer"]["step"] == "B5"

        # every non-null field set so far has a field_sources entry (T7)
        for field in ("official_answer", "stem_en", "structure"):
            assert field in rec2["field_sources"]

        reloaded = read_record(qid, project_root=tmp_root)
        assert reloaded == rec2

        print("records.py self-check OK:", json.dumps(rec2, ensure_ascii=False))
    finally:
        shutil.rmtree(tmp_root)
