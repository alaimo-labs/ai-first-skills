---
name: research-market
description: Run secondary research / benchmarking on your product's market — competitors, alternatives, pricing, trends — with every claim labeled by provenance, mapped back to your unverified beliefs
argument-hint: "[research question or topic; defaults to questions derived from your overview's beliefs]"
disable-model-invocation: true
---

# /research-market

Run secondary research, following the `secondary-research` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the research questions.** From the arguments, or derive them from the artifacts: unverified beliefs in `product/overview.md` that secondary evidence could bear on ("does something like this already exist?", "what does the market charge?"), open assumptions in idea briefs or specs. Propose 2–4 questions and confirm before running — research without a question returns trivia.

2. **State the method up front.** Check what the environment offers: web search available or model knowledge only; subagents available or sequential. Tell the user what the run will be (e.g. "web search via 4 parallel agents" or "model knowledge only — everything will be labeled as unverified") and let them redirect before spending the time.

3. **Run the lanes** per the `secondary-research` skill — direct competitors, alternatives/non-consumption, pricing and business models, positioning, trends — one subagent per lane in parallel when possible, sequentially otherwise. Every finding carries its provenance label; unknowns stay unknown.

4. **Synthesize:** the 2–3 findings that change decisions, the per-lane detail, and the belief-impact table — for each belief in the overview: supported, contradicted, or untouched by the findings. Close the artifact with what still needs primary research.

5. **Present and iterate.** Walk the user through the belief-impact table in particular; let them challenge verdicts before saving.

6. **Save** to `product/research/{YYYY-MM-DD-HHMM}-{slug}.md` (timestamp = creation date) with the `source: secondary` header block from the knowledge skill. Research files live apart from `product/insights/` on purpose — insights are evidence about your users; research is evidence about the market.

7. **Close with the natural next step in one line:** the beliefs the research couldn't touch are the interview/survey agenda (`/design-interview`, `/design-survey`); findings that reshape the idea feed `/clarify-idea` or `/write-spec`.

## Language

Conversation and the saved research in the language of the conversation.
