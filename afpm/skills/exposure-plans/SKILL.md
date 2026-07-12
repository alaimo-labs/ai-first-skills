---
name: exposure-plans
description: How to build an Exposure Plan — an ordered set of accumulative reveal levels that validate a feature's hypothesis layer by layer, each level testing one falsifiable belief. Use when slicing a feature, planning a progressive reveal, designing how to validate a hypothesis in stages, or deciding what to expose to which users in what order.
---

# Exposure Plans

An Exposure Plan turns a feature spec's hypothesis into an ordered set of reveal levels. Each level adds a visible layer of the product and tests one belief. It answers: what becomes visible, in what order, to whom, under what belief.

## Core mental model

- **Build ≠ Reveal.** The Exposure Plan controls what becomes visible, independent of how the code lands. Default mechanism: build whole, flip layers on with feature flags. Incremental development (no flags, ship each layer as built) is a lighter alternative only when every level exposes to the entire deployment population AND the coding agent maintains context across iterations. The plan suggests a mechanism; engineering owns the final call.
- **Each level accumulates.** Level 2 includes everything in Level 1. You never remove something that was revealed; you add.
- **Each level tests one belief.** One clear falsifiable claim per level, written from the user/business perspective, never technical.
- **The set of beliefs validated across levels = the spec's hypothesis resolved.**
- **Audience characterization, not traffic percentages.** Describe who is exposed by behavior or role ("active users with 3+ sessions in the last 2 weeks"), never by technical cohort ("10% of traffic").

## Terminology (strict)

- **Bet / belief / assumption** — level-scoped claims. Reserve "hypothesis" for the spec-level hypothesis being resolved.
- **Value** = desirability + utility: will users want this, use it, get something real from it?
- **Viability** = will this work for the business (economics, operations, support, legal)?
- **Level** = one accumulative reveal step that tests one belief.
- **Validation** = the success criterion for a level: what evidence says "advance", what says "stop".

## Language

Write the plan in the same language as the spec. If Spanish spec → entire output in professional neutral Spanish (no voseo: "divide", not "dividí"), including section titles and level names.

## Workflow

### Step 1 — Locate or confirm the hypothesis

Use the spec's `## Bet` / `## Hypothesis` sections verbatim if present. If absent, derive an implicit hypothesis in one sentence from the Overview + Success Criteria, show it to the user, and ask them to confirm or correct it before continuing. If proceeding without confirmation, prepend the plan with: `> ⚠ Derived hypothesis — confirm before validating.` (in the spec's language).

### Step 2 — Decompose the hypothesis into sequenced beliefs

Quality bar for a belief:

- Active-voice claim: "Users understand…", "Customers act on…".
- Falsifiable — describable evidence could make the team say "no, this didn't hold".
- User/business framing — not "the system detects patterns correctly" but "users find the detected patterns actionable enough to change what they do next".
- Load-bearing — if belief N fails, belief N+1 is uninterpretable or irrelevant. Order accordingly.

### Step 3 — Decide how many levels

- Single-capability feature: 1 level may be enough.
- Typical feature: 2–4 levels.
- Large feature with loosely-coupled modules: up to 5.
- **Never exceed 5.** If 6+ feel necessary, the feature is too big — say so in open questions and suggest splitting the spec.

Each level must add something **user-visible**. Not internal polish, not pipeline work.

### Step 4 — Write each level

- **Level name** — what's revealed, from the user's lens. Short.
- **What is revealed** — concrete list of what's visible, including what is deliberately still dark.
- **Belief** — the one falsifiable claim this level tests.
- **Audience** — who is exposed, by behavior or role.
- **Duration** — typically 1–3 weeks.
- **Validation** — **Advance if:** evidence the belief held. **Stop if:** evidence it didn't.

Keep each level dense and short — grasped in under 30 seconds, no sub-sections.

### Step 5 — Reveal mechanism

If the user expressed a preference (flags or incremental), adopt it — binding, don't argue, don't switch silently — but honestly note fit in 2–3 lines (e.g., "incremental was chosen, but Level 2 targets a behavioral sub-cohort which incremental can't deliver").

Otherwise recommend one: **feature flags** by default; **incremental** only when no level needs sub-cohort targeting AND the coding agent maintains context across iterations. Name the driver explicitly.

### Step 6 — Close

- **Parallel validations** — viability risks (operational cost at scale, regulatory exposure, partner dynamics) and precondition risks needing non-product investigation alongside the reveal. One or two sentences each.
- **Open questions for the product team** — what the plan can't resolve alone: audience recruitment constraints, internal team capacity, existing data that could reduce early risk.

## Output

Markdown, saved to `product/exposure-plans/{spec-slug}.md`. No preamble, no closing fluff — the document IS the response.

## Anti-patterns

- Levels as audience cohorts. A level is a product layer turning on, not a different group being exposed.
- Technical rollout plans. Recommending the mechanism is in scope; naming flag platforms, canary infra, or deployment rings is not.
- Viability beliefs as levels — they go in Parallel validations.
- More than one belief per level.
- Vague validations. "See how it goes" is not a validation; validations have a concrete threshold and an advance/stop decision.
- Treating the spec's claims as facts. "Users will return weekly" is a belief to test, not a given.
- Mixed languages.
