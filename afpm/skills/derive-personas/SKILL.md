---
name: derive-personas
description: Derive evidence-based personas from patterns that recur across real interviews and survey results — bottom-up, every trait traceable to evidence
argument-hint: "[interview/survey files to draw from; defaults to all real-source material in product/]"
disable-model-invocation: true
---

# /derive-personas

Derive personas bottom-up from real research evidence. The opposite move from `/generate-personas`: that one invents archetypes top-down as hypotheses; this one clusters patterns that actually showed up in the data.

Input: $ARGUMENTS

## Workflow

1. **Gather the evidence.** From the named files, or by default: transcripts in `product/interviews/` marked `source: real`, survey analyses in `product/insights/` marked `source: survey`, plus any raw material the user points to. If the corpus is thin (fewer than ~4–5 real interviews and no survey data), say so — patterns from 1–2 conversations are anecdotes — and offer to proceed anyway with the personas explicitly marked low-confidence.

2. **Cluster by behavior, not demographics.** Read the corpus and group interviewees/respondents by recurring patterns in goals, pains, workflows, and context — two people with different job titles who share the same struggle belong together; same title, different struggle, apart. Present the candidate clusters with their supporting evidence and rough coverage (how many sources support each) before writing any persona.

3. **Draft one persona per confirmed cluster,** using the structure from the `synthetic-personas` skill, with two differences: every major trait must be traceable to the evidence (attach 1–3 supporting quotes per section — never fill gaps with invention; a section without evidence stays marked "no evidence yet"), and the header carries `source: derived` plus the list of source files with coverage.

4. **Reconcile with existing personas** in `product/personas/`. For each existing synthetic persona: validated by a cluster (note it and suggest merging the evidence in), contradicted (say how, and suggest revising or retiring it), or simply not observed in the data yet (leave it, noted). The user decides; never delete anything unasked.

5. **Present the set, iterate, and save** each persona to `product/personas/{name-slug}.md`. Derived and synthetic personas live in the same directory, distinguished by the `source:` header.

6. **Close in one line:** the whole loop works with derived personas too — interview them (`/interview-persona`), run critique panels (`/critique-spec`) — now with the personas standing on evidence instead of hypothesis.

## Language

Conversation and the saved personas in the language of the conversation (matching the existing persona files).
