---
name: clarify-idea
description: Starting from one idea already chosen (a solution, not a problem), get it clarified through evidence-grounded questioning, one question at a time — decisions stay yours, unknowns become assumptions. To compare alternatives for a problem first, use /explore-solutions
argument-hint: "<the idea, in a sentence or two>"
disable-model-invocation: true
---

# /clarify-idea

Help the user sharpen a feature idea through questioning — a brainstorming partner that interrogates, not an assistant that embellishes. The user thinks; the agent asks.

**This skill starts from one idea already chosen and defines it — depth, not breadth.** It answers "what exactly is this idea?", not "which solutions are there and which one is worth it?" — that comparison belongs to `/explore-solutions`, which starts from an opportunity and ends with alternatives chosen for testing. It is the path **without** exploration: an idea that arrives already decided. With exploration, the path is `/explore-solutions` → `/design-solution-tests` → tests → `/analyze-solution-tests` → `/write-spec`, and what this skill defines (opportunity, problem, persona, value, what it replaces, smallest version, what kills it) is already settled in the opportunity brief, the solutions file, and the tests — so this skill suggests skipping itself. When the user runs it anyway over an explored alternative, it inherits what was settled instead of re-asking it.

Input: $ARGUMENTS

## Workflow

1. **Capture the idea.** From the arguments, or ask for it in one line if empty. Restate it back in one sentence to anchor the starting point.

2. **Load the evidence first.** Read `product/overview.md` — belief registry included: note which registered beliefs, product-wide, from an opportunity, or from other features, touch this idea — plus `product/opportunities/` (framed problems this idea may answer), `product/solutions/` (explorations that compared alternatives for those problems — one of them may have chosen this very idea), the personas, recent insights, and any market research in `product/research/`. Facts that live in these artifacts are looked up, never asked — the user's time goes to decisions only. If a market question dominates the idea (competitors, pricing) and no research exists, suggest `/research-market` in one line and continue.

3. **Question loop.** Rules, in order of importance:
   - **One question at a time.** Ask, wait for the answer, then decide the next question. Never a battery of questions.
   - **Every question carries a recommended answer** ("my read: X, because your insight Y says… — agree?"). Give the user something to react to, not a blank page.
   - **Ask decisions, not facts.** If it can be answered from `product/`, look it up. If it can't be answered from `product/` *and* only real users could answer it, it isn't a question for the user either — name it as an assumption and move on.
   - **Ground questions in evidence when it exists, citing it.** "Your 07-12 insight says users abandon at the import step — is this idea attacking that, or something else?"
   - **First decision, before anything else: which opportunity does this idea answer?** Three outcomes, none of them blocking:
     - (a) **An existing one** in `product/opportunities/` — the brief references it, inherits its beliefs and research agenda, and the loop never re-asks what the opportunity already resolved (problem, segment, signals, outcome). Recommend the match when one is evident. Then look for a solutions file for that opportunity in `product/solutions/`:
       - **One exists and its `chosen:` names this idea** → read it and inherit the comparison, the value proposition, and the `[feature: {slug}]` beliefs it proposed (reuse its slug). The loop never re-asks the problem, the persona, the value, or what the idea replaces — those were settled with the user there; it starts at the shape (scope, smallest version) and what could kill it. The brief records `solutions explored: {file}`. Then look for a tests file for that solutions file in `product/tests/` (its `solutions:` field names it):
         - **One exists** → suggest in one line going to `/write-spec` naming the solutions and tests files: everything this skill defines is already settled there. Never block; if the user continues, **what was tested is fixed** — the loop does not reopen the mechanism, who does what, the behavior measured, or the segment of a tested alternative; a decision that would change one of them is flagged as "this changes what T{n} tested; that result no longer applies", and the brief records `solutions tested: {tests file}`.
         - **None exists** → suggest `/design-solution-tests` in one line, so the alternative's riskiest belief is tested before it is defined and specified. Never block; if the user continues, the brief records `solutions tested: no (declared)`.
       - **One exists but chose something else** → say so in one line (the idea was discarded or parked, with its reason) and ask whether the user wants to overrule that decision; if yes, continue and log the reversal in `product/corrections.md` with approval.
       - **None exists** → suggest `/explore-solutions` on the opportunity in one line, so this idea competes with alternatives before it is defined. Never block: the user may declare they continue with this idea, and the brief records `solutions explored: no (declared)`.
     - (b) **None, declared by the user** — the brief records `opportunity: none (declared)` and the implicit assumption is registered explicitly as `[feature: {slug}] [value] {the problem X exists for Y}`, so the skipped level leaves a trace.
     - (c) **"I'd rather frame it first"** — suggest `/frame-opportunity` in one line and stop; the idea comes back once the problem holds.
   - **Walk the dependency tree in order:** which opportunity → what problem → for whom (which persona) → why would they care (the value) → what shape it takes (scope, smallest version) → what could kill it (risks). Don't ask downstream questions while an upstream decision is unresolved.
   - **"I don't know" is a finding, not a failure.** Record it as an open assumption and continue.
   - **Stop at shared understanding, not exhaustion.** When new questions stop changing the idea (typically 5–10 decisions), summarize and confirm with the user before writing anything.

4. **Synthesize** into an idea brief: an `opportunity:` field (the parent opportunity's slug, or `none (declared)`), a `solutions explored:` field when a parent opportunity exists (the solutions file it descends from, or `no (declared)`), a `solutions tested:` field when a solutions file exists (the tests file, or `no (declared)`), the clarified idea (problem, persona, value, smallest shape), the decisions made along the way, and the open assumptions ranked by how badly they could kill the idea. **Show the full brief in the conversation** — never ask the user to confirm or save content they haven't seen yet.

5. **Register the assumptions in the overview — the brief keeps no list of its own.** `product/overview.md` is the single belief registry. For each open assumption: if it matches a belief already registered — including the parent opportunity's `[opportunity: {slug}]` beliefs, which the idea inherits rather than re-registers, and the `[feature: {slug}]` beliefs an exploration already proposed for this alternative — the brief references that line; if it's new, propose appending it to the overview's unverified beliefs as `[feature: {slug}] [risk] {assumption}` — slug = the brief's slug; risk = `[value]`, `[usability]`, `[feasibility]`, or `[viability]` — and write nothing to the overview without the user's approval. The brief's assumptions section then holds references to the registry (each belief as registered, in kill-order), never an independent list. No `product/overview.md` yet → suggest `/start-product` in one line and keep the assumptions in the brief, marked as pending registration.

6. **Save** to `product/ideas/{YYYY-MM-DD-HHMM}-{slug}.md` (timestamp = creation date) once the user has seen the brief and agreed. Discarded ideas are worth saving too — note *why* they died; that's product memory. When the brief has no parent opportunity, offer in one line to save the problem + persona pair as a minimal `product/opportunities/{YYYY-MM-DD-HHMM}-{slug}.md` (`status: minimal`; statement, segment, the `[feature: {slug}] [value]` belief referenced, no research agenda yet — see the `opportunity-framing` skill), so future ideas on the same problem have somewhere to hang — only if the user accepts.

7. **Close with the natural next step in one line:** if the idea holds, draft the spec (`/write-spec`); if a risky assumption dominates and the idea descends from a solutions file, test it first (`/design-solution-tests`); without one, `/interview-persona` in validation mode as a cheap rehearsal.

## Language

Conversation and the saved brief in the language of the conversation.
