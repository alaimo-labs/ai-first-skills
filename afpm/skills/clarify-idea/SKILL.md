---
name: clarify-idea
description: Present a fuzzy feature idea and get it clarified through evidence-grounded questioning, one question at a time — decisions stay yours, unknowns become assumptions
argument-hint: "<the idea, in a sentence or two>"
disable-model-invocation: true
---

# /clarify-idea

Help the user sharpen a feature idea through questioning — a brainstorming partner that interrogates, not an assistant that embellishes. The user thinks; the agent asks.

Input: $ARGUMENTS

## Workflow

1. **Capture the idea.** From the arguments, or ask for it in one line if empty. Restate it back in one sentence to anchor the starting point.

2. **Load the evidence first.** Read `product/overview.md`, the personas, recent insights, and any market research in `product/research/`. Facts that live in these artifacts are looked up, never asked — the user's time goes to decisions only. If a market question dominates the idea (competitors, pricing) and no research exists, suggest `/research-market` in one line and continue.

3. **Question loop.** Rules, in order of importance:
   - **One question at a time.** Ask, wait for the answer, then decide the next question. Never a battery of questions.
   - **Every question carries a recommended answer** ("my read: X, because your insight Y says… — agree?"). Give the user something to react to, not a blank page.
   - **Ask decisions, not facts.** If it can be answered from `product/`, look it up. If it can't be answered from `product/` *and* only real users could answer it, it isn't a question for the user either — name it as an assumption and move on.
   - **Ground questions in evidence when it exists, citing it.** "Your 07-12 insight says users abandon at the import step — is this idea attacking that, or something else?"
   - **Walk the dependency tree in order:** what problem → for whom (which persona) → why would they care (the value) → what shape it takes (scope, smallest version) → what could kill it (risks). Don't ask downstream questions while an upstream decision is unresolved.
   - **"I don't know" is a finding, not a failure.** Record it as an open assumption and continue.
   - **Stop at shared understanding, not exhaustion.** When new questions stop changing the idea (typically 5–10 decisions), summarize and confirm with the user before writing anything.

4. **Synthesize** into an idea brief: the clarified idea (problem, persona, value, smallest shape), the decisions made along the way, and the open assumptions ranked by how badly they could kill the idea. **Show the full brief in the conversation** — never ask the user to confirm or save content they haven't seen yet.

5. **Save** to `product/ideas/{YYYY-MM-DD-HHMM}-{slug}.md` (timestamp = creation date) once the user has seen the brief and agreed. Discarded ideas are worth saving too — note *why* they died; that's product memory.

6. **Close with the natural next step in one line:** if the idea holds, draft the spec (`/write-spec`); if a risky assumption dominates, test it first (`/interview-persona` in validation mode).

## Language

Conversation and the saved brief in the language of the conversation.
