---
name: design-solution-tests
description: Starting from a solutions file, design the cheapest test that could refute the riskiest belief of each alternative under test, before anything is built — what to do, with whom, the signal, the threshold, and the decision for each result. Material is built with /build-solution-test; results are analyzed with /analyze-solution-tests
argument-hint: "<solutions file or opportunity slug>"
disable-model-invocation: true
---

# /design-solution-tests

Design how to test the alternatives chosen in a solution exploration before anything is built, following the `solution-testing` skill. The agent proposes; the user decides. **This skill never builds the test material, never runs the tests, and never writes a spec** — the material belongs to `/build-solution-test`, the run to the team, the spec to `/write-spec` after `/analyze-solution-tests`.

It fills the gap between `/explore-solutions` and `/write-spec`: an exploration ends with alternatives chosen *for testing*, and without this step the pipeline specifies a solution nobody has seen react to. The ten interviews behind an alternative prove the pain exists; that this solution relieves it is still a belief until someone reacts to it.

Input: $ARGUMENTS

## Workflow

1. **Resolve the solutions file.** From the argument — a file in `product/solutions/`, or an opportunity slug matched against the files' `opportunity:` field (the latest file wins; if several match, ask which). If none exists, say so in one line and suggest `/explore-solutions`. With `status: back-to-research`, stop: name the instrument the file asks for (`/design-survey`, `/design-interview`, or `/research-market`) instead — there is nothing to test yet. Take the alternatives under test (`chosen` or `testing-several`) and the riskiest belief of each from the comparison table. If a tests file for this solutions file already exists in `product/tests/`, say so and ask whether to add tests to it (a next step after a pass) or start a new file.

2. **Load the evidence.** Read the solutions file, the opportunity brief, `product/overview.md` (the belief registry and each belief's status annotation), `product/insights/`, `product/personas/` (type and whether each suffers the problem), and `product/corrections.md`. Facts that live in these artifacts are looked up, never asked. For each alternative under test, state in one or two lines what the evidence shows about the **problem** and what it shows about **this solution** — separately. When the desirability judgment in the solutions file rests only on problem evidence (interviews or surveys about the pain, nobody reacting to the solution), say it plainly before proposing anything: "the pain is evidenced; that this solution relieves it is not." Offer, with approval, to revise that cell in the solutions file to `mixed` with the note `pain evidenced, relief not tested`.

3. **Confirm the belief to test per alternative.** Usually the riskiest belief from the solutions file. If another belief is riskier now, given step 2 — typically the value belief, once it turns out no one has reacted to the solution — propose it with the reason. One belief per test; an alternative may get a second test only for a second belief, and the one that would kill it fastest goes first. Quote the belief as registered in `product/overview.md`. If it is not in the registry yet, propose registering it as `[feature: {slug}] [{risk}] {belief}` with approval — write nothing to the overview without it. No `product/overview.md` yet → suggest `/start-product` in one line and quote the belief from the solutions file, marked as pending registration.

4. **Propose the cheapest test that could refute it**, by risk type, from the menu in `solution-testing` — value: concierge, Wizard of Oz, prototype shown with a concrete commitment, fake door; usability: prototype plus five people from the segment doing a real task; feasibility: a technical test with real data or a known answer key, metric with threshold, owned by tech; viability: a conversation with whoever decides the purchase or the sponsor, a price test. If the solutions file already describes a test, compare: when it is a late step (a multi-week pilot, a build, anything that needs the product to exist), propose a cheaper first step and keep the original as **Next step if it passes**. One question at a time, each with a recommended answer; the user may prefer a bigger first step, in which case the design records why.

5. **Write each test complete before it runs**, per the format in `solution-testing`: what we do, with whom and how many (segment, recruitment), material needed, duration, signal and threshold, decision rule (`continue` / `change` / `discard`), expected provenance, next step if it passes. Push back, with the reason, on opinion signals ("they liked it"), on a missing threshold, on a threshold that could be moved after the fact, and on a test whose result would not change the decision — such a test is not designed. For feasibility tests the signal is technical — accuracy, time, cost — with its threshold, and the owner is tech; never force it into user behavior. When the participants will be colleagues, classmates, or acted roles, the expected provenance is `synthetic` and the design says the run is a rehearsal.

6. **Specify the material, do not build it.** If a test needs a prototype, a prompt, a script, a page, or a sheet, write in the test's **Material needed** line the minimum it must have to produce the signal, and nothing more: what the person sees or does, what is captured, what is deliberately left out. A test that needs nothing reads `none needed`. Building it is `/build-solution-test`; this skill creates no file under `product/tests/materials/`.

7. **Show the full file in the conversation, then save** to `product/tests/{YYYY-MM-DD-HHMM}-{opportunity-slug}.md` (timestamp = creation date) with `status: designed` once the user agrees — never ask to save content the user has not seen. Offer, with approval, to add a `tests: {file}` line to the solutions file's frontmatter and to replace its per-alternative test description with a reference to this file.

8. **Close in one line:** `/build-solution-test` for each test whose Material needed is not `none needed` (name them, file and test id), then run the tests with their capture sheets, then `/analyze-solution-tests` with the results. If any expected provenance is `synthetic`, say once that the run is a rehearsal and will not move any belief.

## Language

Conversation and the saved file in the language of the conversation. Risk tags, test-type tokens, `status:` values, decision tokens (`continue`, `change`, `discard`), and provenance labels are fixed English tokens in every language, like `source:` values.
