---
name: start-product
description: Start product discovery from scratch — capture the product's name, description, target users, and your unverified beliefs about them into product/overview.md, the context every other skill reads
argument-hint: "[product name or one-line idea; empty to be interviewed]"
disable-model-invocation: true
---

# /start-product

Create `product/overview.md` — the product context every other skill reads. The deliverable is small; the value is in the last section: the user's unverified beliefs about their users, which the rest of the loop exists to test.

Input: $ARGUMENTS

## Workflow

1. **Check what already exists.**
   - `product/overview.md` already there → offer to review and update it instead of overwriting; never silently replace it.
   - The repo has product context (README, docs, specs): read it, but treat it as hypothesis, not fact. Present what was inferred point by point, naming the source file for each ("from `README.md` I gather that…"), and ask the user to confirm or correct before any of it goes into the overview — documents can be stale or aspirational; only the user knows which.
   - Nothing anywhere: start from the arguments (or ask for the idea in one line) and interview the user briefly — a few questions, one at a time, not a form.

2. **Ask only for what documents can't contain.** Facts found in the repo are confirmed, not re-asked. What always needs the user: who the product is for (as specifically as they can say — "PMs" is a segment, "PMs at 10-person startups who do research themselves" is a target) and the beliefs below.

3. **Draw out the unverified beliefs.** Push for 3–5 things the user currently believes about their users but has never verified — each one concrete enough that an interview or survey could prove it wrong. If they blank, probe with prompts: who has this problem badly enough to act? why would they switch from what they do today? would they pay, and what would make it worth it? A belief everyone would agree with isn't a belief, it's a platitude — sharpen it until it's falsifiable.

4. **Draft, show, confirm, save** to `product/overview.md` (no timestamp prefix — the overview is the one living artifact, edited in place):

   ```markdown
   # {Product name}

   {What it is, in 2–4 sentences.}

   ## Para quién / Who it's for

   {Target users, specifically.}

   ## Creencias no verificadas / Unverified beliefs

   - {Belief 1 — falsifiable}
   - {Belief 2}
   - …
   ```

5. **Close with the next step in one line:** generate the persona set (`/generate-personas`) — or, if they'd rather be guided through the whole loop, `/afpm-guide-me`. If the beliefs raise market questions (does this already exist? what does it cost?), mention `/research-market` as an optional detour before the personas.

## Language

Conversation and the saved overview in the language of the conversation (section headings included).
