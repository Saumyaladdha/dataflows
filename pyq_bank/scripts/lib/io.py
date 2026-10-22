"""Standard-library-only I/O helpers used by every other module: atomic writes (so a crash
never leaves a half-written file), JSONL append/read, and CSV read/write.
"""
import csv
import json
import os
import tempfile

# scripts/lib/io.py -> scripts/lib -> scripts -> project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def project_path(*parts):
    """Join path components onto the project root (the folder that contains scripts/, ncert/, papers/, ...)."""
    return os.path.join(PROJECT_ROOT, *parts)


def ensure_parent(path):
    """Create the parent directory of `path` if it doesn't already exist."""
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)


def atomic_write_bytes(path, data: bytes):
    """Write `data` to `path` by writing to a temp file in the same directory and renaming it,
    so a crash mid-write never leaves a half-written file at `path`."""
    ensure_parent(path)
    d = os.path.dirname(path) or "."
    fd, tmp_path = tempfile.mkstemp(dir=d, prefix=".tmp_", suffix="_" + os.path.basename(path))
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, path)
    except BaseException:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise


def atomic_write_text(path, text: str, encoding="utf-8"):
    """Atomically write a text string to `path`."""
    atomic_write_bytes(path, text.encode(encoding))


def atomic_write_json(path, obj, indent=2):
    """Atomically write `obj` to `path` as pretty-printed JSON."""
    atomic_write_text(path, json.dumps(obj, indent=indent, ensure_ascii=False) + "\n")


def append_jsonl(path, obj):
    """Append one JSON object as a single line to the JSONL file at `path`, creating it (and its
    parent folder) if needed. Appending a short line is not a full atomic-replace, but each append
    is flushed and fsync'd so a crash cannot corrupt earlier lines."""
    ensure_parent(path)
    line = json.dumps(obj, ensure_ascii=False)
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")
        f.flush()
        os.fsync(f.fileno())


def read_jsonl(path):
    """Yield each line of a JSONL file as a parsed dict, in order. Yields nothing if the file
    does not exist; blank lines are skipped."""
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


def write_csv(path, rows, fieldnames):
    """Atomically write `rows` (an iterable of dicts) to `path` as CSV with a header row of
    `fieldnames`."""
    ensure_parent(path)
    d = os.path.dirname(path) or "."
    fd, tmp_path = tempfile.mkstemp(dir=d, prefix=".tmp_", suffix="_" + os.path.basename(path))
    try:
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, path)
    except BaseException:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise


def read_csv(path):
    """Return every row of a CSV file at `path` as a list of dicts (empty list if the file does
    not exist)."""
    if not os.path.exists(path):
        return []
    with open(path, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def append_csv_row(path, row, fieldnames):
    """Append one row to a CSV file, writing the header first if the file doesn't exist yet.
    Rewrites the whole file atomically (CSVs here are small register tables, not logs)."""
    rows = read_csv(path)
    rows.append(row)
    write_csv(path, rows, fieldnames)


if __name__ == "__main__":
    import shutil

    tmp_dir = tempfile.mkdtemp(prefix="io_selfcheck_")
    try:
        p = os.path.join(tmp_dir, "sub", "a.json")
        atomic_write_json(p, {"x": 1})
        assert json.load(open(p)) == {"x": 1}

        jl = os.path.join(tmp_dir, "a.jsonl")
        append_jsonl(jl, {"n": 1})
        append_jsonl(jl, {"n": 2})
        assert list(read_jsonl(jl)) == [{"n": 1}, {"n": 2}]
        assert list(read_jsonl(os.path.join(tmp_dir, "missing.jsonl"))) == []

        csv_p = os.path.join(tmp_dir, "a.csv")
        write_csv(csv_p, [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}], ["a", "b"])
        rows = read_csv(csv_p)
        assert rows == [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]

        print("io.py self-check OK. PROJECT_ROOT =", PROJECT_ROOT)
    finally:
        shutil.rmtree(tmp_dir)
