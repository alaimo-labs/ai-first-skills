---
name: write-spec
description: Draft an evidence-grounded feature spec from your insights and personas — problem, user journey, critical user stories with acceptance criteria, falsifiable hypothesis
argument-hint: "[feature idea or insight file; defaults to picking from recent insights]"
disable-model-invocation: true
---

# /write-spec

Draft a feature spec from existing discovery artifacts, following the `feature-specs` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the bet.** If the arguments name a feature idea or an insight file, start there. Otherwise read the recent files in `product/insights/`, propose the insight that looks highest-impact as the one to bet on, and confirm with the user before proceeding.

2. **Load the evidence.** Read `product/overview.md`, the personas in `product/personas/` relevant to the chosen insight, and the interview transcripts the insight cites. Identify the primary persona for the journey and confirm the choice if it isn't obvious.

3. **Draft** per the `feature-specs` skill: problem with cited evidence, user journey from the primary persona's point of view, 3–5 critical user stories with observable acceptance criteria, the falsifiable hypothesis block, and assumptions. Where the evidence is thin, put the claim under Assumptions — never invent quotes or journey steps.

4. **Present and iterate.** Show the draft; walk the user through the journey and the hypothesis in particular (those carry the most judgment). Adjust until they own it — the spec is their bet, not the agent's.

5. **Save** to `product/specs/{YYYY-MM-DD-HHMM}-{slug}.md` and suggest the natural next step in one line: run the critique panel over it (`/critique-spec`).
