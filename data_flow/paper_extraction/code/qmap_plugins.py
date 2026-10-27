"""Plugins for the three question-mapping steps: subject, then chapter, then subtopic.

A CHAIN, AND THE ORDER IS THE POINT
-----------------------------------
    QSUBJ   subject (+ Biology branch)  -- only where the paper printed NO section heading
    QCHAP   chapter, from that subject's chapter list
    QTOPIC  topic, from THAT chapter's topic list

Each step narrows the list the next one chooses from, so a wrong subject cannot be rescued by a good
chapter guess, and a wrong chapter puts the right topic out of reach. That is why each plugin refuses
to run before its predecessor has answered, rather than falling back to a default: a default here
would hide which link in the chain broke.

The chapter and topic lists come from `papers_v2/mappings/chapter_index.json`, built from the
product's own `ExamChapterTopicMappings` table. The lists are CLOSED -- an agent that composes a
chapter name produces something the product cannot show -- so each item carries the exact list its
agent may choose from, and the check validates against that carried list rather than against a copy
of its own.
"""

import collections
import glob
import re
import json
import os
import sys

import runner_core as rc

ListLine = collections.namedtuple(
    "ListLine", ["item_id", "agent", "input_path", "output_path", "run_label"])

CORPUS = rc.corpus()
INDEX = rc.mappings() + ("chapter_index.json",)
B3V_OUT = ("steps", "B3V", "out")

_INDEX_CACHE = {}


ADDITIONS = rc.mappings() + ("taxonomy_additions.json",)


def chapter_index():
    """{subject: [chapter records]} -- the product taxonomy, plus the local additions on top.

    The scan of `ExamChapterTopicMappings` is only part of the vocabulary: it holds 26 Chemistry,
    32 Biology and 31 Physics chapters against roughly 97 in the NEET syllabus, and the mapping
    agents ran into the shortfall on hundreds of questions. `scripts/extend_taxonomy.py` turns what
    they asked for into `taxonomy_additions.json`, and this merges it so a later run can actually
    ANSWER with the chapter it wanted instead of recording `unsure` a second time.

    Added rows keep `added_locally: true` all the way through, so nothing downstream can mistake a
    chapter this project minted for one the product owns.
    """
    if not _INDEX_CACHE:
        path = rc.pp(*INDEX)
        if not os.path.exists(path):
            return {}
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        grouped = collections.defaultdict(list)
        for chapter in data["chapters"]:
            grouped[chapter["subject"]].append(chapter)

        extra = rc.pp(*ADDITIONS)
        if os.path.exists(extra):
            with open(extra, encoding="utf-8") as fh:
                added = json.load(fh)
            for chapter in added.get("chapters") or []:
                grouped[chapter["subject"]].append(
                    {"subject": chapter["subject"], "chapter": chapter["chapter"],
                     "chapter_code": chapter["chapter_code"], "added_locally": True,
                     "topics": chapter.get("topics") or []})
            # A topic wanted INSIDE an existing chapter is appended to that chapter, matched on the
            # same canonical form extend_taxonomy.py used, so an en-dash or a leading "The" cannot
            # silently create a second copy of a chapter that is already there.
            by_canon = {(c["subject"], _canonical(c["chapter"])): c
                        for chapters in grouped.values() for c in chapters}
            for topic in added.get("topics_in_existing_chapters") or []:
                target = by_canon.get((topic["subject"], _canonical(topic["chapter"])))
                if target is not None:
                    target.setdefault("topics", []).append(
                        {"topic_id": topic["topic_id"], "topic": topic["topic"],
                         "added_locally": True})
        _INDEX_CACHE.update(grouped)
    return _INDEX_CACHE


def _canonical(title):
    """Must stay identical to extend_taxonomy.canonical -- they key the same thing."""
    text = re.sub(r"\s*\([^)]*\)\s*$", "", (title or "").strip()).lower()
    text = text.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")
    text = re.sub(r"\s*-\s*practice$", "", text)
    text = re.sub(r"\s+practice$", "", text)
    text = re.sub(r"^the\s+", "", text)
    return re.sub(r"[^a-z0-9]+", "", text)


def agent_read(paper_id, qno):
    """B3V's read of the question -- the text every mapping step judges from."""
    path = rc.pp(*B3V_OUT, "%s__q%03d.runA.json" % (paper_id, qno))
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except ValueError:
        return None
    return None if "error" in data else data


def _step_out(step, item_id):
    return rc.pp("steps", step, "out", "%s.runA.json" % item_id.replace("#", "__"))


def _read_out(step, item_id):
    path = _step_out(step, item_id)
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except ValueError:
        return None
    return None if "error" in data else data



def _image_path(relative):
    """A corpus image as a path from the PIPELINE ROOT, the base every agent resolves against.

    The record stores `crops/2017_A/q055.png`, relative to the corpus folder. Passed through as-is,
    the agent looked for it under the root, found nothing, and decided from the stem alone -- five
    QSUBJ agents on 2017 Code-A reported the image missing. B3V and E7V already convert; these did not.
    """
    return os.path.relpath(rc.pp(*CORPUS, relative), rc.pp()) if relative else None

class _QBase:
    """Shared walking of the corpus. Each subclass decides which questions it owns."""
    step = None
    agent = None
    schema = None

    #: Repeated "<n>. (<d>)" pairs: a row of the booklet's printed answer-key grid, segmented as a
    #: question by mistake. 2019_P1 q031 and q050 are the known cases, and both have no options at
    #: all. Mapping one would spend an agent call to file a wrong row, so the whole chain skips it.
    KEY_GRID = re.compile(r"\b\d{1,3}\.\s*\(\s*[1-4]\s*\)")

    def _is_key_grid(self, question):
        draft = question.get("text_layer_draft") or {}
        return len(self.KEY_GRID.findall(draft.get("stem") or "")) >= 3

    def _corpus(self, filters=None):
        wanted = set((filters or {}).get("items") or [])
        papers = set((filters or {}).get("papers") or [])
        out = {}
        for path in sorted(glob.glob(rc.pp(*CORPUS, "papers", "*.json"))):
            with open(path, encoding="utf-8") as fh:
                paper = json.load(fh)
            meta = paper["meta"]
            paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
            if papers and paper_id not in papers:
                continue
            for question in paper["questions"]:
                item_id = "%s#q%03d" % (paper_id, question["qno"])
                if wanted and item_id not in wanted:
                    continue
                if self._is_key_grid(question):
                    continue
                out[item_id] = (paper_id, question)
        return out

    def _input_path(self, item_id, run_label="runA"):
        return rc.pp("steps", self.step, "work",
                     "%s.%s.input.json" % (item_id.replace("#", "__"), run_label))

    def _write_input(self, item_id, payload, run_label="runA"):
        path = self._input_path(item_id, run_label)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=1)
        return path

    def _line(self, item_id, path, run_label="runA"):
        return ListLine(item_id, self.agent, os.path.relpath(path, rc.pp()),
                        os.path.relpath(_step_out(self.step, item_id), rc.pp()), run_label)

    def _question_view(self, read):
        """Only what the agent needs to judge: the question and its correct answer."""
        return {
            "stem_en": read.get("stem_en"),
            "statements": read.get("statements") or [],
            "list_i": read.get("list_i") or [],
            "list_ii": read.get("list_ii") or [],
            "options_en": read.get("options_en") or {},
        }

    def check(self, filters):
        import jsonschema
        schema = json.load(open(rc.pp("schemas", self.schema), encoding="utf-8"))
        passed, failed, tally = 0, [], collections.Counter()
        for item_id, (paper_id, question) in self._corpus(filters).items():
            out_path = _step_out(self.step, item_id)
            if not os.path.exists(out_path):
                continue
            try:
                data = json.load(open(out_path, encoding="utf-8"))
            except ValueError as exc:
                failed.append((item_id, "output is not valid JSON: %s" % exc))
                continue
            try:
                jsonschema.validate(data, schema)
            except jsonschema.ValidationError as exc:
                failed.append((item_id, "schema: %s" % exc.message))
                continue
            problem = self.validate(data, item_id, paper_id, question, tally)
            if problem:
                failed.append((item_id, problem))
            else:
                passed += 1
        for item_id, message in failed:
            print("%s %-22s FAIL  %s" % (self.step, item_id, message), file=sys.stderr)
        total = len(self._corpus(filters))
        print("%s --check: %d passed, %d failed, %d without output (of %d)"
              % (self.step, passed, len(failed), total - passed - len(failed), total),
              file=sys.stderr)
        if tally:
            print("%s %s" % (self.step, dict(tally)), file=sys.stderr)
        lines = []
        for item_id, message in failed:
            source = self._input_path(item_id)
            if not os.path.exists(source):
                continue
            payload = json.load(open(source, encoding="utf-8"))
            payload["PREVIOUS ATTEMPT FAILED"] = message
            lines.append(self._line(item_id, self._write_input(item_id, payload, "retry1"),
                                    "retry1"))
        return lines

    def validate(self, data, item_id, paper_id, question, tally):
        return None


class QSUBJPlugin(_QBase):
    """Subject, ONLY for questions whose paper printed no section heading."""
    step = "QSUBJ"
    agent = "q-subject-confirmer"
    schema = "QSUBJ.json"

    def _owned(self, filters=None):
        out = {}
        for item_id, (paper_id, question) in self._corpus(filters).items():
            # A printed heading is a measurement; it is never re-judged by an agent.
            if "printed heading" in (question.get("subject_from") or ""):
                continue
            out[item_id] = (paper_id, question)
        return out

    def list_items(self, filters):
        lines = []
        for item_id, (paper_id, question) in self._owned(filters).items():
            if os.path.exists(_step_out(self.step, item_id)):
                continue
            read = agent_read(paper_id, question["qno"])
            draft = question.get("text_layer_draft") or {}
            if read is None:
                # Three booklets -- 2017_C, 2018_AA, 2019_P1 -- print NO section heading anywhere,
                # so every one of their 533 questions has only a positional guess. Requiring a B3V
                # image read first meant QSUBJ could not run on them at all, which in turn handed
                # QCHAP the wrong subject's chapter list. Naming the subject needs far less of the
                # question than solving it does, so the draft is enough here.
                read = {"stem_en": draft.get("stem") or "",
                        "options_en": draft.get("options") or {}}
            payload = dict(self._question_view(read))
            payload.update({
                "paper_id": paper_id, "qno": question["qno"],
                "correct_answer": draft.get("official_answer"),
                # A HINT with a known failure rate, never a default -- see the step's safe_default.
                "position_guess": {"subject": question.get("subject"),
                                   "branch": question.get("branch"),
                                   "how": question.get("subject_from")},
                "question_image": _image_path(question.get("question_image")),
            })
            lines.append(self._line(item_id, self._write_input(item_id, payload)))
        return lines

    def list_reason(self):
        owned = self._owned()
        if not owned:
            return ("QSUBJ has nothing to confirm: every question either had its subject read off a "
                    "printed section heading, or has not been read by B3V yet.")
        done = sum(1 for i in owned if os.path.exists(_step_out(self.step, i)))
        return "QSUBJ: all %d unheaded question(s) already confirmed." % done

    def validate(self, data, item_id, paper_id, question, tally):
        tally[data.get("subject") or "?"] += 1
        if data.get("agrees_with_position") is False:
            tally["DISAGREES WITH POSITION"] += 1
        if data.get("subject") in ("Physics", "Chemistry") and data.get("branch"):
            return "branch %r set on a %s question; branch is Biology-only" % (data["branch"],
                                                                              data["subject"])
        return None


class QCHAPPlugin(_QBase):
    """Chapter, from the subject's closed chapter list."""
    step = "QCHAP"
    agent = "q-chapter-picker"
    schema = "QCHAP.json"

    @staticmethod
    def _subject_of(paper_id, item_id, question):
        """The confirmed subject: the agent's where there is one, else the printed heading."""
        confirmed = _read_out("QSUBJ", item_id)
        if confirmed and confirmed.get("subject") not in (None, "unsure"):
            return confirmed["subject"], confirmed.get("branch")
        return question.get("subject"), question.get("branch")

    def _owned(self, filters=None):
        """Every question with a known subject, read by the agent OR still only drafted.

        B3V's image read used to be required here. It is not any more, and the difference matters
        less for this step than for any other: a chapter is decided by WHICH IDEA the answer turns
        on, and the words that carry that -- `leghaemoglobin`, `potentiometer`, `Frenkel` -- survive
        the text layer intact. What the text layer loses is stacked fractions, drawn structures and
        scripts, which change whether a question can be SOLVED, not which chapter teaches it.

        The source is carried into the payload as `stem_source` so it is never invisible: a mapping
        made from a draft is re-runnable once B3V reaches that booklet, and
        scripts/remap_after_read.py lists exactly those.
        """
        out = {}
        for item_id, (paper_id, question) in self._corpus(filters).items():
            subject, _branch = self._subject_of(paper_id, item_id, question)
            if not subject or subject == "unsure":
                continue          # the chain cannot proceed on an unknown subject
            # A POSITIONAL GUESS IS NOT A SUBJECT. The chapter list handed to the agent is chosen BY
            # subject, so a wrong subject means a wrong closed list, and the agent can then only
            # answer `unsure` -- which is what happened to 108 questions before this guard existed.
            # QSUBJ must confirm these first. Measured: of 43 positional guesses in 2015_A that
            # QSUBJ checked, 43 were wrong.
            heading = "printed heading" in (question.get("subject_from") or "")
            if not heading and not _read_out("QSUBJ", item_id):
                continue
            out[item_id] = (paper_id, question)
        return out

    def list_items(self, filters):
        index = chapter_index()
        lines = []
        for item_id, (paper_id, question) in self._owned(filters).items():
            if os.path.exists(_step_out(self.step, item_id)):
                continue
            subject, branch = self._subject_of(paper_id, item_id, question)
            chapters = index.get((subject or "").lower(), [])
            if not chapters:
                continue
            read = agent_read(paper_id, question["qno"])
            draft = question.get("text_layer_draft") or {}
            if read is None:
                read = {"stem_en": draft.get("stem") or "",
                        "options_en": draft.get("options") or {}}
            payload = dict(self._question_view(read))
            payload.update({
                "paper_id": paper_id, "qno": question["qno"],
                "subject": subject, "branch": branch,
                "stem_source": "b3v_image_read" if agent_read(paper_id, question["qno"])
                               else "text_layer_draft -- fractions and drawings are LOST here; "
                                    "judge the chapter from the words that survive",
                "correct_answer": (question.get("text_layer_draft") or {}).get("official_answer"),
                # The CLOSED list, carried with the item so the check validates against the same
                # list the agent saw rather than a second copy that could drift from it.
                "chapters": [{"chapter_code": c["chapter_code"], "chapter": c["chapter"],
                              "topics": [t["topic"] for t in c["topics"]]} for c in chapters],
                "question_image": _image_path(question.get("question_image")),
            })
            lines.append(self._line(item_id, self._write_input(item_id, payload)))
        return lines

    def list_reason(self):
        owned = self._owned()
        if not owned:
            return ("QCHAP has nothing to map: every question is either unread by B3V or has no "
                    "confirmed subject yet. Run B3V, then QSUBJ for the unheaded booklets.")
        done = sum(1 for i in owned if os.path.exists(_step_out(self.step, i)))
        return "QCHAP: all %d question(s) already mapped to a chapter." % done

    def validate(self, data, item_id, paper_id, question, tally):
        codes = data.get("chapter_codes") or []
        if codes == ["unsure"]:
            tally["unsure"] += 1
            if not (data.get("note") or "").strip():
                return ("unsure with no `note`: an unsure chapter is only useful if it says which "
                        "chapter was expected, which is how a taxonomy gap gets fixed")
            return None
        source = self._input_path(item_id)
        if os.path.exists(source):
            allowed = {c["chapter_code"]
                       for c in json.load(open(source, encoding="utf-8")).get("chapters", [])}
            outside = [c for c in codes if c not in allowed]
            if outside:
                return ("chapter_code(s) %s are not in the list this item carried -- the list is "
                        "closed, and a composed chapter is one the product cannot show"
                        % ", ".join(outside))
        tally["mapped"] += 1
        if len(codes) == 2:
            tally["two chapters"] += 1
        return None


class QTOPICPlugin(_QBase):
    """Subtopic, from the chosen chapter's own closed topic list."""
    step = "QTOPIC"
    agent = "q-subtopic-picker"
    schema = "QTOPIC.json"

    def _owned(self, filters=None):
        out = {}
        for item_id, (paper_id, question) in self._corpus(filters).items():
            chosen = _read_out("QCHAP", item_id)
            if not chosen:
                continue
            codes = chosen.get("chapter_codes") or []
            if not codes or codes == ["unsure"]:
                continue          # no chapter means no topic list to choose from
            out[item_id] = (paper_id, question)
        return out

    def list_items(self, filters):
        index = chapter_index()
        by_code = {c["chapter_code"]: c for chapters in index.values() for c in chapters}
        lines = []
        for item_id, (paper_id, question) in self._owned(filters).items():
            if os.path.exists(_step_out(self.step, item_id)):
                continue
            chosen = _read_out("QCHAP", item_id)
            code = (chosen.get("chapter_codes") or [None])[0]
            chapter = by_code.get(code)
            if not chapter:
                continue
            read = agent_read(paper_id, question["qno"])
            draft = question.get("text_layer_draft") or {}
            if read is None:
                # Mirrors QCHAP._owned: a topic is decided by which idea the answer turns on, and
                # the words that carry that survive the text layer. Without this fallback the step
                # raised for every booklet B3V has not reached, which is nine of the ten.
                read = {"stem_en": draft.get("stem") or "",
                        "options_en": draft.get("options") or {}}
            payload = dict(self._question_view(read))
            payload.update({
                "paper_id": paper_id, "qno": question["qno"],
                "subject": chapter["subject"], "branch": question.get("branch"),
                "stem_source": "b3v_image_read" if agent_read(paper_id, question["qno"])
                               else "text_layer_draft -- fractions and drawings are LOST here",
                "chapter": {"chapter_code": code, "chapter": chapter["chapter"]},
                "correct_answer": (question.get("text_layer_draft") or {}).get("official_answer"),
                # ONE chapter's topics. Counts are included so the agent can see the taxonomy's
                # shape -- the step's rules forbid using them to pick the busiest topic.
                "topics": [{"topic_id": t["topic_id"], "topic": t["topic"],
                            "existing_questions": t.get("questions")} for t in chapter["topics"]],
                "note_from_runner": ("the chapter was picked with %s confidence"
                                     % chosen.get("confidence")) if chosen.get("confidence") else "",
                "question_image": _image_path(question.get("question_image")),
            })
            lines.append(self._line(item_id, self._write_input(item_id, payload)))
        return lines

    def list_reason(self):
        owned = self._owned()
        if not owned:
            return ("QTOPIC has nothing to map: no question has a chapter yet. Run QCHAP first -- a "
                    "topic list only exists inside a chosen chapter.")
        done = sum(1 for i in owned if os.path.exists(_step_out(self.step, i)))
        return "QTOPIC: all %d question(s) already mapped to a topic." % done

    def validate(self, data, item_id, paper_id, question, tally):
        ids = data.get("topic_ids") or []
        if ids == ["unsure"]:
            tally["unsure"] += 1
            return None
        source = self._input_path(item_id)
        if os.path.exists(source):
            payload = json.load(open(source, encoding="utf-8"))
            allowed = {t["topic_id"] for t in payload.get("topics", [])}
            outside = [i for i in ids if i not in allowed]
            if outside:
                return ("topic_id(s) %s are not in this chapter's list -- a topic from elsewhere "
                        "means the CHAPTER choice was wrong, which belongs in `note`"
                        % ", ".join(outside))
        tally["mapped"] += 1
        names = [n.lower() for n in (data.get("topic_names") or [])]
        if any("unspecified" in n for n in names):
            tally["unspecified placeholder"] += 1
        return None
