---
name: write-spec
description: Draft an evidence-grounded feature spec from your insights and personas — or from a tested alternative in a solutions file — problem, user journey, critical user stories with acceptance criteria, falsifiable hypothesis
argument-hint: "[feature idea, idea brief, insight file, or solutions file + tests file; defaults to picking from recent insights]"
disable-model-invocation: true
---

# /write-spec

Draft a feature spec from existing discovery artifacts, following the `feature-specs` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the bet.** Three valid entries:
   - An **idea brief** in `product/ideas/`, a feature idea in one line, or an insight file — start there.
   - A **tested alternative**: a solutions file in `product/solutions/` whose alternative has an analyzed tests file in `product/tests/` (`status: analyzed`, decision `continue` and ready for spec), with no idea brief. The spec inherits from those two files the opportunity, the persona, the value proposition, what it replaces, and the version that was tested; it never re-asks them. Detail decisions that remain are asked one at a time, each with a recommended answer.
   - A solutions file whose alternative has **no tests file** → say so in one line and suggest `/design-solution-tests` first; if the user continues, the spec records under *Tested before spec* that the riskiest belief was not tested (`not tested (declared)`).
   Otherwise read the recent files in `product/insights/`, propose the insight that looks highest-impact as the one to bet on, and confirm with the user before proceeding.

2. **Load the evidence.** Read `product/overview.md` (belief registry included — beliefs already registered for this feature or the product bear on the bet), the personas in `product/personas/` relevant to the chosen insight, the interview transcripts the insight cites, and any market research in `product/research/` that bears on the bet. When the idea brief carries `solutions explored: {file}`, or the bet is a tested alternative, read that file in `product/solutions/` — the comparison and the value proposition are already settled; the spec links them, never rewrites them. When a tests file exists (`solutions tested: {file}` in the brief, or the solutions file's `tests:` line), read it too: **what was tested is fixed.** Note the mechanism, who does what, the behavior measured, and the segment of each test that passed. Identify the primary persona for the journey and confirm the choice if it isn't obvious.

3. **Draft** per the `feature-specs` skill: problem with cited evidence, user journey from the primary persona's point of view, 3–5 critical user stories with observable acceptance criteria, the falsifiable hypothesis block, and assumptions. When the idea comes from an exploration, add the short **Alternatives considered** section: a link to the solutions file and one line per discarded alternative with its reason — no re-evaluation. When a tests file exists, add the short **Tested before spec** section next to it: a link to the tests file and one line per test with its result and provenance — no re-analysis. Where the evidence is thin, the claim becomes an assumption — never invent quotes or journey steps.

4. **Present and iterate.** Show the draft; walk the user through the journey and the hypothesis in particular (those carry the most judgment). Adjust until they own it — the spec is their bet, not the agent's. **If a decision changes something that was tested** — the mechanism, who does what, the behavior measured, the segment — say so before applying it: "this changes what T{n} tested; that result no longer applies." The belief under that test is open again for the new version: the spec records the change under *Tested before spec* (which test, what changed, `result no longer applies`), the Assumptions section lists the belief as unverified for this version, and the close suggests `/design-solution-tests` for it. The user may continue; the spec never pretends the old result covers the new version.

5. **Register the assumptions in the overview — the spec keeps no list of its own.** `product/overview.md` is the single belief registry. Reuse the feature slug from the idea brief when the spec descends from one; otherwise use the spec's slug. For each assumption: already registered → the spec's Assumptions section references it; new → propose appending `[feature: {slug}] [risk] {assumption}` to the overview's unverified beliefs — risk classified per the `feature-specs` skill's four categories, with their default owners — and write nothing without the user's approval.

6. **Save** to `product/specs/{YYYY-MM-DD-HHMM}-{slug}.md` and suggest the natural next step in one line: run the critique panel over it (`/critique-spec`) — or, when a decision invalidated a test, `/design-solution-tests` for the changed version first.
