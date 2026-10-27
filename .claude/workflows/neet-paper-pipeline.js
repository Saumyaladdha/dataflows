export const meta = {
  name: 'neet-paper-pipeline',
  description: 'Run one NEET booklet end to end: extract, every agent step with checks and retries, figures, CDN upload, data/ export',
  whenToUse: 'Build or rebuild data/<year>/<paper_code>/ for a NEET booklet with no manual steps. args: {paper_id, pdf?}',
  phases: [
    { title: 'Prepare', detail: 'extract the booklet (if a pdf is given) and assign subjects' },
    { title: 'Read', detail: 'B3V question reads, then B3S solution reads' },
    { title: 'Figures', detail: 'cut every boxed figure, lift exact vector copies' },
    { title: 'Agents', detail: 'B6V, QSUBJ, FIGC, FIGP together; then QCHAP, QTOPIC, E7V' },
    { title: 'Taxonomy', detail: 'mint missing topics, re-ask the questions that wanted them' },
    { title: 'Publish', detail: 'draw checked cards, upload to the CDN, export through the LaTeX gate' },
  ],
}

// One agent per item, each following its brief -- the pipeline's contract (CONVENTIONS rule 7: a
// script never calls an agent; this workflow is the dispatcher). The scripts are run by a RUNNER
// agent that executes exact commands and reports their output; it decides nothing.

const ROOT = args.root || 'C:/Users/vitth/OneDrive/Desktop/NCERT extraction and NEET PYQ mapping/data_flow/paper_extraction'
const PAPER = args.paper_id
const PDF = args.pdf || null
const MAX_RETRIES = 1

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
  properties: { written: { type: 'boolean' }, note: { type: 'string' } },
  required: ['written', 'note'],
}

async function runner(label, commands, phaseName) {
  const prompt = [
    'You run shell commands for a data pipeline and report their output. You decide nothing and change nothing else.',
    `Working directory: ${ROOT}`,
    'Run EACH command below, in order, with the Bash tool, from that directory (cd into it first; quote the path, it has spaces).',
    'Do not fix, retry or skip anything. Report the combined stdout and stderr of all commands verbatim, and the exit code of the last one.',
    '',
    ...commands.map((c, i) => `${i + 1}. ${c}`),
  ].join('\n')
  const result = await agent(prompt, { label, phase: phaseName, schema: RUN, agentType: 'general-purpose' })
  return result || { stdout: '', exit_code: 1 }
}

function parseLines(stdout) {
  // run_step.py --list/--check print one work item per line: item | agent | input | output | label
  return (stdout || '').split(/\r?\n/).filter(l => l.split(' | ').length === 5).map(l => {
    const [item, agentName, input, output, run] = l.split(' | ').map(s => s.trim())
    return { item, agentName, input, output, run }
  })
}

function dispatch(step, lines, phaseName) {
  return parallel(lines.map(line => () => agent([
    `You are the ${line.agentName} agent of a NEET question-paper extraction pipeline (step ${step}).`,
    `Your instructions are the brief at: ${ROOT}/agents/${line.agentName}.md -- read it first and follow it exactly, including its universal rules and its output shape.`,
    `Your input file: ${ROOT}/${line.input.replace(/\\/g, '/')}`,
    `Write exactly ONE JSON object (no markdown, no code fences) to: ${ROOT}/${line.output.replace(/\\/g, '/')}`,
    `Any relative path inside the input file (images, etc.) is relative to ${ROOT}. Use the Read tool to look at image files.`,
    'If the input carries PREVIOUS OUTPUT and PREVIOUS ATTEMPT FAILED, start from the previous output and change only what the failure names.',
    'Do this one item only. Read only the brief, the input file and the files it names. Do not open, create or edit any other file.',
    'When the output file is written, report written=true.',
  ].join('\n'), { label: `${step} ${line.item}`, phase: phaseName, schema: DONE, agentType: 'general-purpose' })))
}

async function step(name, phaseName) {
  const listed = await runner(`${name} list`, [`python code/run_step.py ${name} --list --papers ${PAPER}`], phaseName)
  let lines = parseLines(listed.stdout)
  log(`${name}: ${lines.length} item(s) to run`)
  if (lines.length) await dispatch(name, lines, phaseName)
  for (let attempt = 0; attempt <= MAX_RETRIES; attempt++) {
    const checked = await runner(`${name} check`, [`python code/run_step.py ${name} --check --papers ${PAPER}`], phaseName)
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

if (!PAPER) throw new Error('pass args.paper_id, e.g. {"paper_id": "2017_A", "pdf": "source_papers/NEET_Papers/2017/NEET_2017_Code_A_official.pdf"}')
const report = []

phase('Prepare')
const prep = []
if (PDF) prep.push(`python code/extract_paper_v2.py --paper "${PDF}" --apply`)
prep.push(`python code/assign_subject.py --paper-id ${PAPER} --apply`)
await runner('extract + subject', prep, 'Prepare')

phase('Read')
report.push(await step('B3V', 'Read'))
report.push(await step('B3S', 'Read'))

phase('Figures')
await runner('cut + vector', [
  `python code/cut_agent_figures.py --paper-id ${PAPER} --apply`,
  `python code/vector_figures.py --paper-id ${PAPER} --apply`,
], 'Figures')

phase('Agents')
// Independent of each other once B3V/B3S and the figures exist: run together.
const wave = await parallel([
  () => step('B6V', 'Agents'), () => step('QSUBJ', 'Agents'),
  () => step('FIGC', 'Agents'), () => step('FIGP', 'Agents'),
])
report.push(...wave.filter(Boolean))
// QCHAP needs QSUBJ; QTOPIC needs QCHAP; E7V needs QSUBJ -- the chain and E7V run side by side.
const chain = await parallel([
  async () => [await step('QCHAP', 'Agents'), await step('QTOPIC', 'Agents')],
  async () => [await step('E7V', 'Agents')],
])
report.push(...chain.filter(Boolean).flat())

phase('Taxonomy')
const tax = await runner('taxonomy gaps', [
  `python code/collect_taxonomy_gaps.py --apply`,
  `python code/extend_taxonomy.py --apply`,
  `python code/requeue_taxonomy_gaps.py --paper-id ${PAPER} --apply`,
], 'Taxonomy')
if (/(\d+) QTOPIC answer\(s\) re-queued/.test(tax.stdout) && !/\b0 QTOPIC answer/.test(tax.stdout)) {
  report.push(await step('QTOPIC', 'Taxonomy'))
}

phase('Publish')
const publish = await runner('cards + upload + export', [
  `python code/render_figure_cards.py --paper-id ${PAPER} --apply`,
  `powershell -NoProfile -Command "$env:ARIVIHAN_TOKEN=[Environment]::GetEnvironmentVariable('ARIVIHAN_TOKEN','User'); $env:ARIVIHAN_USER_ID=[Environment]::GetEnvironmentVariable('ARIVIHAN_USER_ID','User'); python code/upload_paper_assets.py --paper-id ${PAPER}; python code/upload_paper_assets.py --paper-id ${PAPER} --verify --apply"`,
  `python code/upload_paper_assets.py --paper-id ${PAPER} --check`,
  `python code/upload_paper_assets.py --paper-id ${PAPER} --verify`,
  `python code/checks/latex_census.py --paper-id ${PAPER} --strict`,
  `python code/export_paper_v2.py --data --paper-id ${PAPER}`,
], 'Publish')

const failing = report.filter(r => r && !r.ok)
log(failing.length ? `steps with items left for review: ${failing.map(r => r.step).join(', ')}` : 'every step DONE')
return { paper_id: PAPER, steps: report, publish_tail: (publish.stdout || '').slice(-1500), publish_exit: publish.exit_code }
