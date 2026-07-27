---
name: analyze-survey
description: Analyze survey results — quantitative summary by learning goal, coded open-ends, and actionable insights extracted from the data
argument-hint: "[results file (CSV/markdown) or pasted data; optionally the survey design file]"
disable-model-invocation: true
---

# /analyze-survey

Analyze survey results, following the analysis guidance in the `survey-design` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the inputs.** The results may arrive as a file path (CSV or markdown export from any survey tool), pasted data, or a file already in the repo. Find the matching survey design in `product/surveys/` (or ask for it) — it carries the learning goals and the goal-per-question mapping that structure the whole analysis. Without a design file, reconstruct the apparent goals from the questions and confirm them with the user.

2. **Establish the denominator.** n, recruitment channel, response rate if known. State the limits up front and let every later claim inherit them; with small or self-selected samples, keep findings directional and say so.

3. **Analyze per the `survey-design` skill,** organized by learning goal, not question order: distributions for closed questions, segment cuts where screening/demographic data allows, open-ends coded into themes with mention counts and 1–2 verbatim quotes each. For each goal: what was believed, what the data shows, what decision follows.

4. **Extract insights** to the `insight-extraction` quality bar: actionable, grounded in numbers or quotes, prioritized by impact. Flag every "why" the data raises as a candidate for follow-up interviews — surveys say what, not why.

5. **Present and iterate.** Show the analysis; let the user challenge segment cuts or codings before saving.

6. **Save** to `product/insights/{YYYY-MM-DD-HHMM}-{slug}.md` with a header listing the survey design file, the results source, n, and `source: survey`.

7. **Close with the natural next step in one line:** feed the findings into a spec (`/write-spec`), design follow-up interviews for the open "why"s (`/design-interview`), or — once enough real data has accumulated — derive evidence-based personas (`/derive-personas`).

## Language

Conversation and the saved analysis in the language of the conversation.
