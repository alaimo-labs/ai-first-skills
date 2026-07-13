---
name: persona-critique
description: How to run a persona critique — a synthetic persona reviews a spec, PRD, or product idea in character and returns a structured rating with strengths, concerns, and suggestions. Use when critiquing a spec with personas, getting user feedback on a document, running a review panel, or stress-testing a PRD from the user's perspective.
---

# Persona Critique

A persona critique has a synthetic persona review a product document (spec, PRD, idea brief) from THEIR perspective — not a generic quality review, but "does this address MY needs, goals, and frustrations?"

## Roleplay rules

- Respond fully in character as the persona. Never break character or acknowledge being an AI.
- Respond in the SAME language as the document under review.
- Weigh the persona's technical literacy and device preferences when evaluating: a low-literacy persona should flag complexity a developer persona wouldn't notice.
- Not all features will be relevant to the persona — saying "this part isn't for me" is valid and useful feedback.
- Honesty over politeness: enthusiasm must be earned by the document actually addressing the persona's frustrations.

## Critique format (per persona)

```markdown
### {Persona name} — {role}

**Overall rating:** X/5

**Strengths:** (what works well for my needs)
- …

**Concerns:** (what worries or frustrates me)
- …

**Suggestions:** (specific improvements)
- …

{1–2 sentences of additional commentary, in character}
```

Rating scale: 1 = this doesn't solve anything for me → 5 = I'd fight to get this.

## Panel synthesis

When multiple personas critique the same document, add a synthesis section after the individual critiques — written as the researcher, NOT in character:

- Points of agreement across personas (strongest signal)
- Conflicts between personas (design tensions the user must decide on)
- The 2–3 highest-impact changes suggested by the panel overall

Save panels to `product/insights/{YYYY-MM-DD-HHMM}-critique-{spec-slug}.md`.
