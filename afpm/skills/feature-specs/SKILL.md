---
name: feature-specs
description: Structure and quality bar for evidence-grounded feature specs — problem, user journey, critical user stories with acceptance criteria, and a falsifiable hypothesis. Use when writing a feature spec or PRD, defining user stories or acceptance criteria, mapping a user journey, or turning insights into a spec.
---

# Feature Specs

A feature spec in this method is a **bet backed by evidence**, not an enterprise PRD. It stays short enough to critique in one sitting and carries everything the downstream skills need: personas critique it, and the exposure plan is derived from its hypothesis. Nothing in the spec floats free — every claim traces to an insight, and through it to a quote from an interview.

## Language

Write the spec in the same language as the conversation and the product context.

## Structure

```markdown
# {Feature name}

## Problem
{2–4 sentences: the pain, its cost, and why now.}
> Evidence: "{quote or paraphrase}" — {persona}, {insight or interview file}

## Who it's for
{The persona(s) this serves, by name, with one line on why them.}

## User journey
{The primary persona's path, from their point of view:}
1. **Trigger** — {what happens in their life/work that starts the journey}
2. {step} — {what they do, what they see}
3. …
N. **Outcome** — {the moment they get the value; what is different now}

## Critical user stories

### {Story title}
As {persona name}, I want {action}, so that {benefit}.

Acceptance criteria:
- [ ] {observable, testable condition}
- [ ] …

Traces to: {insight title or file}

## Hypothesis
We believe {users} will {behavior} because {motivation}.
We're wrong if {observable signal}.

## Alternatives considered
{Only when the idea comes from `/explore-solutions`. One link and one line per alternative — the comparison lives in the solutions file, not here.}
Explored in: product/solutions/{file}
- {alternative} — discarded: {reason}
- {alternative} — parked: {reason}

## Tested before spec
{Only when the alternative has a tests file. One link and one line per test — the analysis lives in the tests file, not here. A spec decision that changed what a test covered says so.}
Tested in: product/tests/{file}
- T1 {test name} — passed (real, n=…) · {belief}
- T2 {test name} — failed (synthetic, rehearsal) · {belief}
- {or} riskiest belief not tested (declared)
- {if applicable} T{n} — result no longer applies: {what this spec changed}

## Assumptions
{References to `product/overview.md` — the single belief registry; the spec keeps no separate list.}
- [feature: {slug}] [{risk}] {belief as registered} {— owner: {role}, only when it differs from the default}
```

## Assumptions and risk

Assumptions live in `product/overview.md` — the single belief registry — tagged `[feature: {slug}]`; the spec's Assumptions section references them and never keeps its own list. New assumptions surfaced while drafting are proposed to the registry with the user's approval. Classify each by risk, one of four fixed English tokens:

| Risk | The question it carries | Default owner |
| --------------- | ------------------------------------------------------------ | ------------- |
| `[value]` | Do they want it — does it solve a problem they care about? | PM |
| `[usability]` | Can they figure out how to use it? | UX |
| `[feasibility]` | Can we build it with the time, skills, and tech we have? | Tech |
| `[viability]` | Does it work for the business — revenue or sponsorship? | PM |

The owner derives from the risk; write it down only when the real owner differs from the default. Every assumption needs a nameable owner — an assumption nobody owns is an assumption nobody will test.

## Quality bar

- **Traceable.** Every story and journey step must be justified by an insight or interview moment. If the evidence doesn't exist, don't invent it — register the claim as an assumption instead. The Assumptions section is a feature, not a confession.
- **Journey is grounded, not aspirational.** Steps describe what interviews revealed about how this persona actually works, with the feature inserted at the point of pain — not an idealized flow. Name the step where value lands.
- **Critical stories only: 3–5.** This is discovery, not a backlog. Each story should be INVEST-shaped — independent, negotiable, valuable, estimable, small, testable — with the persona's real name as the role, never a generic "user."
- **Acceptance criteria are observable: 3–6 per story.** Each one answers yes/no by looking at the product — no "works well", no "is intuitive". Include at least one edge case. Well-written criteria double as validation signals for the exposure plan later.
- **Hypothesis is falsifiable.** The "we're wrong if" clause names a signal you could actually observe. This block is what `exposure-plans` decomposes — a spec without it can't be sliced.
- **Alternatives are linked, not re-argued.** When the idea descends from a solutions file, the spec says which alternatives lost and why in one line each and links the file; it never rewrites the comparison. A spec whose idea skipped the exploration omits the section — the idea brief already records `solutions explored: no (declared)`.
- **What was tested is fixed.** When the alternative has a tests file (see the `solution-testing` skill), the spec links it under *Tested before spec* with one line per test — result and provenance — and keeps the tested version: the mechanism, who does what, the behavior measured, the segment. A spec decision that changes one of them invalidates that test's result; the spec says so in the same section (`result no longer applies`), and the belief is unverified again for the new version. An alternative that came from an exploration and was never tested declares it: `riskiest belief not tested (declared)`.
- **The spec is written from a tested alternative without an idea brief.** When the bet is a solutions file plus its analyzed tests file, the opportunity, the persona, the value proposition, what it replaces, and the smallest version come from those files by reference; the spec asks only the detail decisions that remain.
- **Accessible.** Short sentences, no jargon a newcomer to the product would trip on.

## Location

Save to `product/specs/{YYYY-MM-DD-HHMM}-{slug}.md` — the timestamp is the creation date, so specs sort chronologically. Revise in place without renaming: after a critique panel, edit this file rather than creating a new one.
