"""Builds the exact instruction line the main session gives a subagent (spec 5.1), and a stub
for headless invocation (spec 5.2).
"""


def build_instruction_line(agent_name, input_path, output_path):
    """Return the exact instruction string for invoking one subagent on one input/output pair,
    per spec 5.1: "Use the <agent> subagent. Input: <input_path>. Output: <output_path>. Do
    nothing else.\""""
    return f"Use the {agent_name} subagent. Input: {input_path}. Output: {output_path}. Do nothing else."


def call_headless(agent_name, input_path, output_path):
    """Shell out once to Claude Code in non-interactive mode (`claude -p "<instruction line>"`)
    to run one subagent headlessly, for `run_step.py <STEP> --auto` (spec 5.2).

    NOT IMPLEMENTED: this build environment could not run `claude --help` to confirm the
    installed version's flags — the `claude` binary was not resolvable on PATH here (`which
    claude` / `type claude` both failed), so there is no way to verify, rather than guess,
    things like: the exact non-interactive flag (`-p` vs `--print`), how to scope which agents
    load, the permission-mode flag needed to restrict Read/Write as spec 5.2 requires ("agents
    can read only steps/, ncert/, papers/ and write only their own output path"), and the
    output-format flag needed to detect success/failure reliably from a script.

    To implement once that's confirmed: build the instruction line with
    `build_instruction_line`, then `subprocess.run(["claude", "-p", instruction, ...], check=True,
    capture_output=True, text=True, timeout=...)` with whatever permission/output-format flags
    the installed version documents, raising on a non-zero exit or a missing output file.
    """
    raise NotImplementedError(
        "call_headless: could not confirm the installed `claude` CLI's non-interactive flags "
        "in this environment (claude was not on PATH to run `claude --help`). See this "
        "function's docstring for exactly what to implement once the flags are confirmed."
    )


if __name__ == "__main__":
    line = build_instruction_line("a1-book-registrar", "steps/A1/work/BIO11L.input.json",
                                   "steps/A1/out/BIO11L.json")
    expected = ("Use the a1-book-registrar subagent. Input: steps/A1/work/BIO11L.input.json. "
                "Output: steps/A1/out/BIO11L.json. Do nothing else.")
    assert line == expected, line

    try:
        call_headless("a1-book-registrar", "in.json", "out.json")
        raise AssertionError("expected NotImplementedError")
    except NotImplementedError:
        pass

    print("agents.py self-check OK:", line)
