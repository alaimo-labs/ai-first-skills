---
name: design-interview
description: Design an interview guide for real user research from what you want to learn or validate — grounded in your insights, assumptions, and personas
argument-hint: "[what you want to learn/validate, or an insight/idea/spec file]"
disable-model-invocation: true
---

# /design-interview

Design an interview guide for research with real users, following the `interview-guides` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the learning goals.** If the arguments state them or name a file (an insight, idea brief, or spec), start there. Otherwise scan `product/` for the strongest candidates — open assumptions in ideas/specs, insights marked `source: synthetic` awaiting verification, hypotheses — propose 2–4 goals and confirm with the user before proceeding.

2. **Load context.** Read `product/overview.md` and the personas relevant to the goals. Ask who the real participants will be; map them to a persona/segment so the guide's participant profile is concrete.

3. **Resolve the mode.** Exploration (open discovery) or validation (testing a specific idea/prototype). If not obvious from the goals, ask — one question, two options.

4. **Draft the guide** per the `interview-guides` skill: goals with their beliefs-at-risk and falsification notes, funnel structure, non-leading questions with probes, stimulus section only in validation mode.

5. **Present and iterate.** Walk the user through the goal→question mapping — every question they can't trace to a goal gets cut. Adjust until they own it.

6. **Save** to `product/interview-guides/{YYYY-MM-DD-HHMM}-{slug}.md` (timestamp = creation date).

7. **Close with next steps in one line each:** pretest the guide before it meets real participants (`/test-interview-guide` — runs the guide against a synthetic persona and diagnoses what breaks), and after the real interviews, bring the transcripts to `/extract-insights`.

## Language

Conversation and the saved guide in the language of the conversation.
