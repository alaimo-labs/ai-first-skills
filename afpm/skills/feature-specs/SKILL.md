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

## Assumptions
- {unvalidated belief the spec rests on}
```

## Quality bar

- **Traceable.** Every story and journey step must be justified by an insight or interview moment. If the evidence doesn't exist, don't invent it — write the claim under Assumptions instead. The Assumptions section is a feature, not a confession.
- **Journey is grounded, not aspirational.** Steps describe what interviews revealed about how this persona actually works, with the feature inserted at the point of pain — not an idealized flow. Name the step where value lands.
- **Critical stories only: 3–5.** This is discovery, not a backlog. Each story should be INVEST-shaped — independent, negotiable, valuable, estimable, small, testable — with the persona's real name as the role, never a generic "user."
- **Acceptance criteria are observable: 3–6 per story.** Each one answers yes/no by looking at the product — no "works well", no "is intuitive". Include at least one edge case. Well-written criteria double as validation signals for the exposure plan later.
- **Hypothesis is falsifiable.** The "we're wrong if" clause names a signal you could actually observe. This block is what `exposure-plans` decomposes — a spec without it can't be sliced.
- **Accessible.** Short sentences, no jargon a newcomer to the product would trip on.

## Location

Save to `product/specs/{YYYY-MM-DD-HHMM}-{slug}.md` — the timestamp is the creation date, so specs sort chronologically. Revise in place without renaming: after a critique panel, edit this file rather than creating a new one.
