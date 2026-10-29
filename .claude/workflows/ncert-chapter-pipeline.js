export const meta = {
  name: 'ncert-chapter-pipeline',
  description: 'Build one NCERT chapter end to end: every agent step (A2, A2S, A2L, FIGP, A3, A4) with checks and one retry, then the exact HTML + JSON + MD, CDN links and the page-by-page compare',
  whenToUse: 'Build or rebuild data/new_ncert/class_NN/<subject>/chNN_*/ for one NCERT chapter with no manual steps. args: {chapter_id: "PHY11L-ch01", pdf?: "C:/Users/vitth/Downloads/Chapter_1.pdf"}',
  phases: [
    { title: 'Prepare', detail: 'copy the PDF into source_pdfs, refuse a printed copy, build page inputs' },
    { title: 'Read', detail: 'A2 page reads' },
    { title: 'Special', detail: 'A2S tables/equations/figures and A2L printed layout, together' },
    { title: 'Build', detail: 'first chapter.json, so figures and sections exist' },
    { title: 'Structure', detail: 'FIGP figure redraws (physics) and A3 passages, together; then A4 subtopics' },
    { title: 'Publish', detail: 'final build: exact HTML + JSON + MD, CDN links, rows, compare with the book' },
  ],
}

// One agent per item, each following its brief (agents/<name>.md). Scripts are run by a RUNNER
// agent that executes exact commands and reports their output; it decides nothing. All listing and
// checking is code/chapter_steps.py, scoped to this one chapter.

const ROOT = args.root || 'C:/Users/vitth/OneDrive/Desktop/NCERT extraction and NEET PYQ mapping/data_flow/ncert_extractions'
const CID = args.chapter_id
const PDF = args.pdf || null
const MAX_RETRIES = 1
const PY = 'python -X utf8'

// How each agent checks its own output before it reports (the same checks chapter_steps runs).
const SELF_CHECK = {
  A2: (o, i) => `${PY} -c "import json,sys; sys.path.insert(0,'code'); from checks import A2; print(A2.check(json.load(open('${o}',encoding='utf-8')), {'input_data': json.load(open('${i}',encoding='utf-8'))}))"`,
  A2S: (o, i) => `${PY} -c "import json,sys; sys.path.insert(0,'code'); from checks import A2S; print(A2S.check(json.load(open('${o}',encoding='utf-8')), {'input_data': json.load(open('${i}',encoding='utf-8'))}))"`,
  A2L: (o, i) => `${PY} -c "import json,sys; sys.path.insert(0,'code'); import runner_core as rc; from checks import A2L; out=json.load(open('${o}',encoding='utf-8')); print(rc.validate_schema('A2L', out), A2L.check(out, {'blocks': json.load(open('${i}',encoding='utf-8'))['blocks']}))"`,
  FIGP: (o, i) => `${PY} code/figp_bridge.py check ${i} ${o} steps/FIGP/drawn/_selfcheck.svg`,
  A3: (o, i) => `${PY} -c "import json,sys; sys.path.insert(0,'code'); from checks import A3; print(A3.check(json.load(open('${o}',encoding='utf-8')), {'input_data': json.load(open('${i}',encoding='utf-8'))}))"`,
  A4: (o, i) => `${PY} -c "import json,sys; sys.path.insert(0,'code'); from checks import A4; print(A4.check(json.load(open('${o}',encoding='utf-8')), {'input_data': json.load(open('${i}',encoding='utf-8'))}))"`,
}

// Rules each step's agents broke at least once (LESSONS / project memory), said up front.
const TRAPS = {
  A2: 'One page only. List every removed running header/footer line, including the "2024-25" stamp.',
  A2S: 'A figure with no printed labels or caption inside the box must have a `note` starting with "unsure:". Copy every character as printed; equations in LaTeX exactly as printed. `target_box_in_crop` is your block; the rest of the crop is context.',
  A2L: 'The field is `font`, never `face`; `page_kind` goes inside `page`. The "2024-25" stamp is NOT a page_number. A block continuing into the other column keeps its `n` where it starts and `n: null` on the continuation.',
  FIGP: 'The caption is not part of the drawing. Every word in `printed_text` is a label or in `excluded_text` with why. If the check says "labels the print does not have", those words are outlined art in the PDF: drop them as labels and say so in note.',
  A3: 'Ignore the input key `_fingerprints`.',
  A4: '',
}

const RUN = {
  type: 'object',
  properties: {
    stdout: { type: 'string', description: 'the complete stdout+stderr of the commands, verbatim' },
    exit_code: { type: 'integer', description: 'exit code of the LAST command' },
  },
  required: ['stdout', 'exit_code'],
}
const DONE = {
  type: 'object',
  properties: { written: { type: 'boolean' }, check: { type: 'string' }, note: { type: 'string' } },
  required: ['written', 'check', 'note'],
}

async function runner(label, commands, phaseName) {
  const prompt = [
    'You run shell commands for a data pipeline and report their output. You decide nothing and change nothing else.',
    `Working directory: ${ROOT}`,
    'Run EACH command below, in order, from that directory (cd into it first; quote the path, it has spaces). Use the Bash tool.',
    'Do not fix, retry or skip anything. Report the combined stdout and stderr of all commands verbatim, and the exit code of the last one.',
    '',
    ...commands.map((c, i) => `${i + 1}. ${c}`),
  ].join('\n')
  const result = await agent(prompt, { label, phase: phaseName, schema: RUN, agentType: 'general-purpose' })
  return result || { stdout: '', exit_code: 1 }
}

function parseLines(stdout) {
  // chapter_steps.py list/check print one work item per line: item | agent | input | output | run
  return (stdout || '').split(/\r?\n/).filter(l => l.split(' | ').length === 5).map(l => {
    const [item, agentName, input, output, run] = l.split(' | ').map(s => s.trim().replace(/\\/g, '/'))
    return { item, agentName, input, output, run }
  })
}

function dispatch(step, lines, phaseName) {
  return parallel(lines.map(line => () => agent([
    `You are the ${line.agentName} agent of an NCERT textbook extraction pipeline (step ${step}).`,
    `Your instructions are the brief at: ${ROOT}/agents/${line.agentName}.md -- read it first and follow it exactly, including its universal rules and its output shape.`,
    `Your input file: ${ROOT}/${line.input}`,
    `Write exactly ONE JSON object (no markdown, no code fences) to: ${ROOT}/${line.output}`,
    'Write it with the Write tool, never through a shell heredoc: Git Bash halves backslashes and corrupts LaTeX and JSON.',
    `Any relative path inside the input file (images, the PDF) is relative to ${ROOT}. Use the Read tool to look at image files.`,
    TRAPS[step] ? `Known traps for this step: ${TRAPS[step]}` : '',
    'If the input carries PREVIOUS OUTPUT / PREVIOUS ATTEMPT FAILED (or previous_attempt_failed), fix exactly what the failure names and keep the rest.',
    `Then check your output from ${ROOT}: ${SELF_CHECK[step](line.output, line.input)}`,
    'If the check fails, fix what it names and check again (at most 3 rounds). Report the final check result.',
    'Do this one item only. Read only the brief, the input file and the files it names. Do not open, create or edit any other project file.',
  ].filter(Boolean).join('\n'), { label: `${step} ${line.item}`, phase: phaseName, schema: DONE, agentType: 'general-purpose' })))
}

async function step(name, phaseName) {
  const listed = await runner(`${name} list`, [`${PY} code/chapter_steps.py list ${name} ${CID}`], phaseName)
  const lines = parseLines(listed.stdout)
  log(`${name}: ${lines.length} item(s) to run`)
  if (lines.length) await dispatch(name, lines, phaseName)
  for (let attempt = 0; attempt <= MAX_RETRIES; attempt++) {
    const checked = await runner(`${name} check`, [`${PY} code/chapter_steps.py check ${name} ${CID}`], phaseName)
    const retries = parseLines(checked.stdout)
    if (!retries.length) {
      log(`${name}: DONE`)
      return { step: name, ok: true }
    }
    if (attempt === MAX_RETRIES) {
      log(`${name}: ${retries.length} item(s) still failing after retry -- left for review`)
      return { step: name, ok: false, failing: retries.map(r => r.item) }
    }
    log(`${name}: retrying ${retries.length} item(s)`)
    await dispatch(name, retries, phaseName)
  }
}

if (!CID) throw new Error('pass args.chapter_id, e.g. {"chapter_id": "PHY11L-ch01", "pdf": "C:/Users/vitth/Downloads/Chapter_1.pdf"}')
const report = []
// Physics and chemistry designs are not yet in book_design.MEASURED_KEYS; their builds run on the
// provisional design and say so.
const BUILD = `${PY} code/run_chapter.py ${CID} --allow-unmeasured`

phase('Prepare')
const prep = await runner('prepare', [`${PY} code/chapter_steps.py prepare ${CID}${PDF ? ` --pdf "${PDF}"` : ''}`], 'Prepare')
if (prep.exit_code) throw new Error(`prepare failed:\n${prep.stdout.slice(-1500)}`)

phase('Read')
report.push(await step('A2', 'Read'))

phase('Special')
report.push(...(await parallel([() => step('A2S', 'Special'), () => step('A2L', 'Special')])).filter(Boolean))

phase('Build')
await runner('first build', [`${BUILD} --no-cdn --no-compare`], 'Build')

phase('Structure')
report.push(...(await parallel([() => step('FIGP', 'Structure'), () => step('A3', 'Structure')])).filter(Boolean))
// A4 reads the passages A3 produced, which only a build joins into the tree.
await runner('passages build', [`${BUILD} --no-cdn --no-compare`], 'Structure')
report.push(await step('A4', 'Structure'))

phase('Publish')
const publish = await runner('final build', [
  `powershell -NoProfile -Command "$env:ARIVIHAN_TOKEN=[Environment]::GetEnvironmentVariable('ARIVIHAN_TOKEN','User'); $env:ARIVIHAN_USER_ID=[Environment]::GetEnvironmentVariable('ARIVIHAN_USER_ID','User'); python -X utf8 code/run_chapter.py ${CID} --allow-unmeasured"`,
  `${PY} code/chapter_steps.py status ${CID}`,
], 'Publish')

const failing = report.filter(r => r && !r.ok)
log(failing.length ? `steps with items left for review: ${failing.map(r => r.step).join(', ')}` : 'every step DONE')
return { chapter_id: CID, steps: report, publish_tail: (publish.stdout || '').slice(-2500), publish_exit: publish.exit_code }
