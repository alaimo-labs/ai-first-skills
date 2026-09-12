---
name: frame-opportunity
description: Frame an opportunity — a problem for a segment, backed by signals — before any solution is chosen. Evidence-grounded questioning, one question at a time; unknowns become beliefs, and the output is a research agenda, not a feature
argument-hint: "<the opportunity as it arrived: a strategy line, a signal, a request, or an idea you want to look underneath>"
disable-model-invocation: true
---

# /frame-opportunity

Help the user understand a problem space before deciding what to build, following the `opportunity-framing` skill. The agent interrogates; the user decides. **This skill never asks what the solution looks like** — that question belongs to `/clarify-idea`, later.

Input: $ARGUMENTS

## Workflow

1. **Capture the opportunity as it arrived.** From the arguments, or ask for it in one line if empty. Restate it in one sentence to anchor the starting point. If what arrived is a solution ("a better whiteboard"), say so, park it as a *candidate idea* for the bottom of the brief, and work on the problem underneath it: "what would have to be true about these people for a better whiteboard to matter?" If what arrived is an outcome ("increase retention"), say so too — the outcome lives in the overview; the question here is which problem, for whom, would move it.

2. **Load the evidence first.** Read `product/overview.md` (mode, sponsor, the belief registry — note which registered beliefs, product-wide or from other opportunities, touch this one), `product/personas/`, `product/research/`, recent `product/insights/`, and existing `product/opportunities/` (an opportunity already framed for the same problem is reused, not duplicated). Facts that live in these artifacts are looked up, never asked.

3. **Question loop.** Same rules as `/clarify-idea` — one question at a time; every question carries a recommended answer grounded in the evidence, cited; ask decisions, not facts (what only real users could answer is a belief, not a question for the user); "I don't know" is a finding; stop at shared understanding, typically 5–8 decisions — walking this tree in order, never asking downstream while upstream is unresolved:
   - **What problem**, stated as a behavior or a cost ("team leads re-decide the same thing twice a week"), never as a missing feature.
   - **For whom**: which existing personas suffer it, which don't, and whether a persona is missing. A missing persona is noted in the brief and `/generate-personas` is suggested for the gap in one line — not run.
   - **What signals** support it, each with its provenance label (`real` / `survey` / `secondary` / `synthetic` / `unverified`). Numbers quoted in a brief or a deck are `unverified` signals until the source is named.
   - **What business outcome** it serves — commercial: revenue, retention, upgrade; internal: the sponsor's metric or a cost avoided. Read the mode from the overview.
   - **What would have to be true** for this to be worth pursuing: the value belief and the viability belief of the opportunity, stated so an instrument could prove them wrong.
   - **Constraints** that bound any future solution — budget, dates, compliance — recorded as facts, not as decisions about the solution.

   If the user drifts into solutions, park the idea under candidate ideas and return to the problem. Never ask "what would it look like?", "which features?", or "how would it work?".

4. **Synthesize** into an opportunity brief per the `opportunity-framing` skill's format: statement (problem + segment + why now), segment and personas touched with the missing persona if any, signals table with provenance, business outcome, constraints, beliefs referenced from the registry, the **research agenda** (per belief: the cheapest instrument that resolves it, the decision it unlocks, by when — this section is the skill's real payoff), and candidate ideas parked along the way, explicitly marked *not evaluated*. **Show the full brief in the conversation** before asking to save it.

5. **Register the beliefs in the overview — the brief keeps no list of its own.** `product/overview.md` is the single belief registry. For each belief: if it matches one already registered (product-wide or from another opportunity), the brief references that line; if new, propose appending it to the unverified beliefs as `[opportunity: {slug}] [value|viability] {belief}` — slug = the brief's slug; `[usability]`/`[feasibility]` only when one bounds the whole opportunity, per the knowledge skill — ranked among the existing beliefs by impact × uncertainty. Write nothing to the overview without the user's approval. No `product/overview.md` yet → suggest `/start-product` in one line and keep the beliefs in the brief, marked as pending registration.

6. **Save** to `product/opportunities/{YYYY-MM-DD-HHMM}-{slug}.md` (timestamp = creation date) once the user has seen the brief and agreed. Discarded opportunities are worth saving too, with `status: discarded` and *why* — the next person who brings the same problem finds the reasoning.

7. **Close with the next step in one line, following the research agenda:** `/research-market` on this opportunity first (secondary is cheap and narrows the agenda); then `/design-survey` and `/design-interview` for what the market can't answer — interviews recruited among the survey's opt-ins; `/clarify-idea` only once the problem holds, pointing at this opportunity so the idea inherits its beliefs.

## Language

Conversation and the saved brief in the language of the conversation. The belief tags and provenance labels are fixed English tokens in every language, like `source:` values.
