---
name: design-survey
description: Design a survey questionnaire from what you want to measure or validate — grounded in your insights and assumptions, ready to paste into any survey tool
argument-hint: "[what you want to measure/validate, or an insight/idea/spec file]"
disable-model-invocation: true
---

# /design-survey

Design a survey questionnaire, following the `survey-design` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the learning goals.** If the arguments state them or name a file (insight, idea brief, spec), start there. Otherwise scan `product/` for candidates — assumptions to quantify, synthetic insights awaiting verification, a hypothesis needing numbers — propose 2–4 goals and confirm before proceeding. If the goals are exploratory "why" questions with no prior qualitative work, say that a survey is the wrong instrument and suggest `/design-interview` instead.

2. **Load context.** Read `product/overview.md` and relevant personas. Ask who the respondents will be and roughly how many are reachable; define the screening criteria against a persona/segment.

3. **Draft the questionnaire** per the `survey-design` skill: screening first, every question annotated with the goal it serves, under ~12 questions, 1–3 open-ends near the end.

4. **Present and iterate.** Walk the user through the goal→question mapping and the wording of the riskiest questions (anything near "would you…" gets rewritten to behavior). Adjust until they own it.

5. **Save** to `product/surveys/{YYYY-MM-DD-HHMM}-{slug}.md` (timestamp = creation date). Remind the user the `> Goal:` annotations are internal — strip them when pasting into their survey tool (any tool works; the questionnaire is plain markdown).

6. **Close with the next step in one line:** when responses arrive, bring the export (CSV or pasted) to `/analyze-survey` together with this design file.

## Language

Conversation and the saved questionnaire in the language of the conversation (or the respondents' language if the user says it differs).
