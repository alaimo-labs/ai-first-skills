---
name: secondary-research
description: How to do secondary research and benchmarking for product discovery — provenance discipline, source hierarchy, research lanes (competitors, alternatives, pricing, trends), and mapping findings back to your unverified beliefs. Use when researching a market, benchmarking competitors, sizing an opportunity, or gathering existing knowledge about a product space.
---

# Secondary Research

Secondary research gathers what is already known about a market: competitors, alternatives, pricing, trends. It reduces uncertainty about the **market**; it cannot verify your beliefs about **your users** — those still need interviews and surveys. Keep that boundary explicit in every deliverable.

## Language

Write the research in the language of the conversation. Quotes from sources stay in their original language, translated inline when useful.

## Provenance discipline (the core rule)

Every factual claim carries a label:

- `[verificado: URL — fecha de consulta]` — found via web search/fetch, with the source.
- `[conocimiento del modelo — verificar]` — from the model's training data; may be stale or wrong.

Never mix the two silently. If web search is unavailable in the environment, say so at the top of the artifact and label everything as model knowledge — a benchmark of unlabeled LLM recall is a machine for unjustified confidence; a labeled one is an honest map of what you know versus what you assume. Pricing, feature lists, and company status go stale fast: always note dates, and prefer "unknown" over a plausible guess. **"Unknown" is a valid cell in any comparison table.**

## Source hierarchy

1. **The competitor's own site** (pricing page, docs, changelog) — best for what they offer and charge.
2. **Industry reports and reputable press** — market context and trends.
3. **User forums, reviews, communities** — sentiment and complaints; signal, not fact.
4. **Model knowledge** — starting hypotheses and vocabulary; never the final word.

## Research lanes

Cover these lanes; each can run independently (see Parallelization):

- **Direct competitors** — products solving the same problem for the same segment.
- **Alternatives and non-consumption** — what the target users actually do today: spreadsheets, WhatsApp, paper, an intern, nothing. Often the real competitor.
- **Pricing and business models** — what the market charges, in what model (subscription, commission, freemium), at what tiers.
- **Positioning** — how existing players describe themselves; where the crowded and empty spaces are.
- **Trends and market size** — direction and order of magnitude only; precise TAM figures from secondary sources are theater.

Per competitor, capture: who it's for, core value proposition, pricing, notable strengths/weaknesses, and — the part teams skip — what its existence proves (demand exists) and what it doesn't (that *your* segment will switch).

## Mapping back to beliefs

The payoff step: for each unverified belief in `product/overview.md` (and open assumptions in ideas/specs), state whether the findings **support**, **contradict**, or **say nothing**. A contradiction doesn't kill a belief — the source's segment may differ from yours — but it raises its priority for primary research. End with the beliefs that secondary evidence cannot touch: those are the interview/survey agenda.

## Parallelization

If the environment supports subagents, run one per lane in parallel; each returns raw findings with provenance labels, and the synthesis (including the belief mapping) happens in the main conversation. Without subagents, walk the lanes sequentially — same artifact, more wall-clock.

## Output format

```markdown
---
source: secondary
method: web | model-knowledge | mixed
date: {YYYY-MM-DD}
question: {what this research set out to answer}
---

# Research: {topic}

{One-paragraph summary: the 2–3 findings that change decisions.}

## {One section per lane…}

## Impacto en creencias
| Creencia (de overview.md) | Veredicto | Evidencia |
|---|---|---|
| … | apoya / contradice / no dice nada | {finding + label} |

## Qué sigue necesitando research primario
- …
```

## Anti-patterns

- Model knowledge presented as verified fact (the cardinal sin)
- Comparison tables with invented cells instead of "unknown"
- "A competitor exists" read as "the market is validated" — or as "the space is taken"
- Market sizes with three significant figures sourced from a blog
- Treating a finished benchmark as a reason to skip talking to users
