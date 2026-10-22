"""The only code that issues IDs (spec 6.1). Counter-backed ID types (question, change,
repeat group, flag, and the per-scope passage/subtopic sequence numbers) persist their counters
in register/counters.json and only ever increment, so a number is never reused even after an
item is "deleted". Book/chapter/paper IDs are deterministic formats of their inputs, not
counters, but a mint function is provided for every pattern in the table regardless.
"""
import contextlib
import json
import os

try:
    import fcntl
    _HAS_FCNTL = True
except ImportError:  # pragma: no cover - non-POSIX fallback
    _HAS_FCNTL = False

from . import io as lib_io

COUNTERS_PATH = lib_io.project_path("register", "counters.json")

SUBJECT_ABBR = {
    "physics": "PHY", "chemistry": "CHE", "biology": "BIO",
    "phy": "PHY", "che": "CHE", "bio": "BIO",
    "PHY": "PHY", "CHE": "CHE", "BIO": "BIO",
}
EDITIONS = {"L", "O", "M"}
SITTINGS = {"MAIN", "PH2", "REEXAM", "RETEST", "CANCELLED"}

_EMPTY_COUNTERS = {
    "question": 0,
    "change": 0,
    "repeat_group": 0,
    "flag": 0,
    "passage": {},
    "subtopic": {},
}


def _subject_abbr(subject):
    key = subject.strip()
    if key.upper() in {"PHY", "CHE", "BIO"}:
        return key.upper()
    try:
        return SUBJECT_ABBR[key.lower()]
    except KeyError:
        raise ValueError(f"unknown subject {subject!r}; expected Physics/Chemistry/Biology or PHY/CHE/BIO")


@contextlib.contextmanager
def _locked_counters_file(path):
    """Hold an exclusive OS lock on a sidecar .lock file for the duration of the block, so
    concurrent processes minting IDs in parallel (spec 5.11) never race on counters.json."""
    lib_io.ensure_parent(path)
    lock_path = path + ".lock"
    lock_file = open(lock_path, "a+")
    try:
        if _HAS_FCNTL:
            fcntl.flock(lock_file, fcntl.LOCK_EX)
        yield
    finally:
        if _HAS_FCNTL:
            fcntl.flock(lock_file, fcntl.LOCK_UN)
        lock_file.close()


def _load_counters():
    if not os.path.exists(COUNTERS_PATH):
        return dict(_EMPTY_COUNTERS)
    with open(COUNTERS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    for key, default in _EMPTY_COUNTERS.items():
        data.setdefault(key, default if not isinstance(default, dict) else {})
    return data


def _save_counters(counters):
    lib_io.atomic_write_json(COUNTERS_PATH, counters)


def ensure_counters_file():
    """Create register/counters.json with every counter at 0 if it doesn't already exist."""
    with _locked_counters_file(COUNTERS_PATH):
        if not os.path.exists(COUNTERS_PATH):
            _save_counters(dict(_EMPTY_COUNTERS))
    return COUNTERS_PATH


def _next_global(counter_name):
    with _locked_counters_file(COUNTERS_PATH):
        counters = _load_counters()
        counters[counter_name] = int(counters.get(counter_name, 0)) + 1
        n = counters[counter_name]
        _save_counters(counters)
    return n


def _next_scoped(counter_name, scope_key):
    with _locked_counters_file(COUNTERS_PATH):
        counters = _load_counters()
        scope = counters.setdefault(counter_name, {})
        scope[scope_key] = int(scope.get(scope_key, 0)) + 1
        n = scope[scope_key]
        _save_counters(counters)
    return n


def next_question_id():
    """Mint the next Question ID: Q-{6 digits}, never reused."""
    return f"Q-{_next_global('question'):06d}"


def next_change_id():
    """Mint the next Change ID: CL-{4 digits}, never reused."""
    return f"CL-{_next_global('change'):04d}"


def next_repeat_group_id():
    """Mint the next Repeat group ID: RG-{4 digits}, never reused."""
    return f"RG-{_next_global('repeat_group'):04d}"


def next_flag_id():
    """Mint the next Flag ID: FL-{6 digits}, never reused."""
    return f"FL-{_next_global('flag'):06d}"


def make_book_id(subject, class_, edition):
    """Build a Book ID: {SUBJ}{CLASS}{ED}, e.g. BIO11L. Deterministic from its inputs, not
    counter-backed — the same book always gets the same id."""
    edition = edition.strip().upper()
    if edition not in EDITIONS:
        raise ValueError(f"unknown edition {edition!r}; expected one of {sorted(EDITIONS)}")
    return f"{_subject_abbr(subject)}{int(class_)}{edition}"


def make_chapter_id(subject, class_, chapter_num):
    """Build a Chapter ID: {SUBJ}{CLASS}-CH{nn}, e.g. BIO11-CH10 (latest-edition numbering).
    Deterministic from its inputs, not counter-backed."""
    return f"{_subject_abbr(subject)}{int(class_)}-CH{int(chapter_num):02d}"


def next_passage_id(book_id, chapter_num):
    """Mint the next Passage ID within one book's chapter: {BOOK}-CH{nn}-P{nn}. The P-number is
    a counter scoped to (book_id, chapter_num) so it only increments and is never reused."""
    chapter_key = f"{book_id}-CH{int(chapter_num):02d}"
    n = _next_scoped("passage", chapter_key)
    return f"{chapter_key}-P{n:02d}"


def next_subtopic_id(chapter_id):
    """Mint the next Subtopic ID within one latest-edition chapter: {SUBJ}{CLASS}-CH{nn}-ST{nn}.
    The ST-number is a counter scoped to chapter_id so it only increments and is never reused."""
    n = _next_scoped("subtopic", chapter_id)
    return f"{chapter_id}-ST{n:02d}"


def make_paper_id(year, sitting, code):
    """Build a Paper ID: NEET-{YEAR}-{SITTING}-{CODE}, e.g. NEET-2023-MAIN-A. Deterministic from
    its inputs, not counter-backed."""
    sitting = sitting.strip().upper()
    if sitting not in SITTINGS:
        raise ValueError(f"unknown sitting {sitting!r}; expected one of {sorted(SITTINGS)}")
    return f"NEET-{int(year)}-{sitting}-{code}"


if __name__ == "__main__":
    import shutil
    import tempfile

    tmp_root = tempfile.mkdtemp(prefix="ids_selfcheck_")
    orig_path = COUNTERS_PATH
    try:
        COUNTERS_PATH = os.path.join(tmp_root, "register", "counters.json")  # noqa: F811
        globals()["COUNTERS_PATH"] = COUNTERS_PATH
        ensure_counters_file()

        q1, q2, q3 = next_question_id(), next_question_id(), next_question_id()
        assert [q1, q2, q3] == ["Q-000001", "Q-000002", "Q-000003"], (q1, q2, q3)

        fl1 = next_flag_id()
        assert fl1 == "FL-000001"

        cl1 = next_change_id()
        assert cl1 == "CL-0001"

        rg1 = next_repeat_group_id()
        assert rg1 == "RG-0001"

        book_id = make_book_id("Biology", 11, "L")
        assert book_id == "BIO11L", book_id
        chapter_id = make_chapter_id("Biology", 11, 10)
        assert chapter_id == "BIO11-CH10", chapter_id

        p1 = next_passage_id(book_id, 10)
        p2 = next_passage_id(book_id, 10)
        p3 = next_passage_id(book_id, 11)  # different chapter -> independent counter
        assert p1 == "BIO11L-CH10-P01", p1
        assert p2 == "BIO11L-CH10-P02", p2
        assert p3 == "BIO11L-CH11-P01", p3

        st1 = next_subtopic_id(chapter_id)
        st2 = next_subtopic_id(chapter_id)
        assert st1 == "BIO11-CH10-ST01", st1
        assert st2 == "BIO11-CH10-ST02", st2

        paper_id = make_paper_id(2023, "main", "A")
        assert paper_id == "NEET-2023-MAIN-A", paper_id

        # simulate a process restart: counters must persist on disk, not just in memory
        q4 = next_question_id()
        assert q4 == "Q-000004", q4

        print("ids.py self-check OK:", q1, q2, q3, fl1, cl1, rg1, p1, p2, p3, st1, st2, paper_id)
    finally:
        globals()["COUNTERS_PATH"] = orig_path
        shutil.rmtree(tmp_root)
