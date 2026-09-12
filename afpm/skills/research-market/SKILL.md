---
name: research-market
description: Run secondary research / benchmarking on your product's market — competitors, alternatives, pricing, trends — with every claim labeled by provenance, mapped back to your unverified beliefs
argument-hint: "[research question, topic, or an opportunity file; defaults to questions derived from your overview's beliefs]"
disable-model-invocation: true
---

# /research-market

Run secondary research, following the `secondary-research` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the research questions.** From the arguments, or derive them from the artifacts: unverified beliefs in `product/overview.md` that secondary evidence could bear on ("does something like this already exist?", "what does the market charge?") — `[product]` and `[opportunity: {slug}]` beliefs alike — plus the **Research agenda** of the briefs in `product/opportunities/` (the rows marked for secondary research are pre-written questions) and open assumptions in idea briefs or specs. When the arguments name an opportunity, scope the run to that opportunity's beliefs and agenda. Propose 2–4 questions and confirm before running — research without a question returns trivia.

2. **State the method up front.** Check what the environment offers: web search available or model knowledge only; subagents available or sequential. Tell the user what the run will be (e.g. "web search via 4 parallel agents" or "model knowledge only — everything will be labeled as unverified") and let them redirect before spending the time.

3. **Run the lanes** per the `secondary-research` skill — direct competitors, alternatives/non-consumption, pricing and business models, positioning, trends — one subagent per lane in parallel when possible, sequentially otherwise. Every finding carries its provenance label; unknowns stay unknown.

4. **Synthesize:** the 2–3 findings that change decisions, the per-lane detail, and the belief-impact table — for each belief in the overview touched by the questions, the opportunity's `[opportunity: {slug}]` beliefs included, not only the `[product]` ones: supported, contradicted, or untouched by the findings. Close the artifact with what still needs primary research. **The impact table lives in the research file only.** This skill never writes to `product/overview.md`: market evidence cannot verify beliefs about your users, so it earns no `confirmed`/`contradicted` annotation, and whether a contradiction warrants `weakened` is `/review-evidence`'s call, with the research file as its evidence.

5. **Present and iterate.** Walk the user through the belief-impact table in particular; let them challenge verdicts before saving.

6. **Save** to `product/research/{YYYY-MM-DD-HHMM}-{slug}.md` (timestamp = creation date) with the `source: secondary` header block from the knowledge skill — including `opportunity: {slug}` when the run was scoped to one, so the brief's research agenda can be traced to this file without editing the brief. The only files this skill writes are its own research files. Research files live apart from `product/insights/` on purpose — insights are evidence about your users; research is evidence about the market.

7. **Close with the natural next step in one line:** the beliefs the research couldn't touch are the primary-research agenda — when an opportunity is in play, name explicitly which go to a survey (`/design-survey`: how many, how often, how much) and which to interviews (`/design-interview`: why, what they do today), aligned with the brief's research agenda; findings that reshape the idea feed `/clarify-idea` or `/write-spec`.

## Language

Conversation and the saved research in the language of the conversation.
