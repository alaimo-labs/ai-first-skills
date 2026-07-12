---
name: insight-extraction
description: How to extract actionable product insights from user interview transcripts (real or synthetic) — focus areas, quality bar, and output format. Use when analyzing interviews, synthesizing research, extracting insights, or turning transcripts and user feedback into product decisions.
---

# Insight Extraction

You are acting as a UX researcher extracting actionable insights from user interviews. Works on synthetic interview transcripts and on transcripts of real interviews the user pastes in or points to.

## Language

Extract insights in the SAME language as the interview transcript. Spanish transcript → Spanish insights.

## Task

Analyze the transcript and extract 3–5 key insights valuable for product development. More than 5 means you're listing observations, not insights.

## Focus areas

- User pain points and frustrations
- Feature requests or needs
- Workflow preferences
- Technical constraints or requirements
- Unmet needs or opportunities
- Decision criteria for tool adoption
- Integration requirements
- Success metrics and KPIs

## Quality bar

- **Actionable and specific** — an insight implies a product decision. "Users dislike the onboarding" is an observation; "users abandon onboarding at the data-import step because they don't have their data at hand — allow skipping and importing later" is an insight.
- **Grounded** — every insight must be traceable to something actually said in the transcript. Quote or paraphrase the supporting moment. Never invent evidence.
- **Quantified when possible** — time saved, errors reduced, frequency of the pain.
- **Balanced** — identify both problems and opportunities; consider technical, organizational, and personal factors.
- **Prioritized** — order by potential product impact.

## Output format

One insight per section:

```markdown
## {Short insight title, max ~100 chars}

{Detailed explanation, 2–4 sentences: the need or pain, its consequence, and what it implies for the product.}

> Evidence: "{supporting quote or paraphrase from the transcript}" — {persona/interviewee}
```

Save to `product/insights/{topic-or-persona-slug}-{date}.md`, with a header listing the source transcript(s). When extracting across multiple interviews, note which insights recur across interviewees — recurrence is the strongest prioritization signal.

## Caveat for synthetic sources

When the source interviews are synthetic, remind the user (once, briefly) that synthetic insights are hypotheses to check against real users, not evidence. Mark the insights file `source: synthetic` in its header.
