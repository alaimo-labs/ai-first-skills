---
name: synthetic-personas
description: How to create rich, diverse synthetic user personas (archetypes) for product discovery — structure, design principles, and diversity requirements. Use when creating personas, user archetypes, synthetic users, or when the user asks to model their target users, segments, or audiences.
---

# Synthetic Personas

A synthetic persona is a versatile user archetype that can adapt to different contexts and scenarios. Well-built personas power downstream discovery work: interviews, spec critiques, and feedback sessions all roleplay these profiles, so depth here pays off everywhere else.

## Language

Write personas in the language of the conversation and of the product context. If the user works in Spanish, all persona content — names aside — is in Spanish.

## Archetype design principles

1. Create personality templates, NOT specific situations.
2. Focus on WHO they are (demographics, personality), not just WHAT they do.
3. Include psychological drivers that apply across contexts.
4. Define behavioral patterns that transcend specific tasks.
5. Make them feel like real, multi-dimensional people.

## Persona structure

Each persona is one markdown file with this structure:

```markdown
# {Full name}

> "{A quote revealing their core mindset or philosophy}"

- **Role:** their professional role or life situation
- **Age range:** e.g., 25–34 (optional)
- **Location:** e.g., urban tech hub (optional)
- **Industry:** e.g., technology (optional)
- **Technical literacy:** low | medium | high
- **Experience level:** novice | intermediate | expert

## Goals

Long-term aspirations, professional objectives, personal motivations (bulleted).

## Frustrations

General pain points, recurring challenges, systemic issues they face (bulleted).

## Typical tasks

Regular responsibilities, common activities, typical workflows (bulleted).

## Device preferences

Primary device, secondary device, platform preferences.
```

## Diversity requirements

A persona SET must vary across:

- Experience levels (novice, intermediate, expert)
- Technical literacy (low, medium, high)
- Age ranges
- Professional roles and industries
- Work styles and preferences

Never generate a set of personas that are minor variations of the same person. Each persona must have a clearly distinct perspective on the product's problem space. When personas already exist in the project, read them first and avoid duplicating them.

## Quality bar

- Clear, distinct roles and perspectives
- Realistic goals and frustrations expressed concretely (not "wants efficiency" but "loses two hours a week reconciling spreadsheets by hand")
- Varied technical capabilities
- Feels like a real person with authentic needs

## Anti-patterns

- Personas defined only by demographics with no psychology
- Every persona already loving the product idea — include skeptics
- Frustrations without consequences (always tie a pain to lost time, errors, stress, or money)
- Personas that mirror the product team instead of its actual users
