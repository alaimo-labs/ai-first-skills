---
name: survey-design
description: How to design survey questionnaires and analyze their results — question types, wording bias, ordering, scales, quantitative summaries, and coding open-ended responses. Use when designing a survey or questionnaire, writing survey questions, choosing scales, or analyzing survey results and responses.
---

# Survey Design

Surveys quantify what interviews discovered. They answer "how many / how much / which segment" — never "why". A survey written before any qualitative work usually measures the team's assumptions with false precision; when that's the situation, say so and suggest interviews first.

## Language

Write the questionnaire and analysis in the language of the conversation — and, if different, in the language the respondents will read.

## Designing the questionnaire

### From goals to questions

Same chain as interviews: 2–4 learning goals (from assumptions, synthetic insights to verify, a hypothesis), each mapped to the decision the answer will drive. Every question must trace to a goal; cut the rest. Length target: **under 5 minutes** (~10–12 questions) — completion rate drops with every screen.

### Question types

- **Single / multiple choice** — for known option sets. Always include an escape ("Other", "None of these"); options must be exhaustive and non-overlapping.
- **Likert scales** — for agreement/satisfaction/frequency. Use 5 points, label every point, keep the same direction throughout the survey.
- **Ranking** — only with ≤5 items; beyond that respondents satisfice.
- **Open-ended** — expensive to answer and to analyze; 1–3 maximum, placed near the end. One "what's the hardest part of X for you?" open-end is often the most valuable question in the survey.
- **Screening questions** — first, to qualify respondents against the target profile; route out those who don't match rather than diluting the data.

### Wording and ordering

- No leading ("How much do you love…"), no loaded terms, no double-barreled questions ("fast and reliable"), no jargon the respondent may not share.
- Ask about behavior and frequency ("in the last month, how many times…") over intention ("would you…").
- General before specific; behavior before opinion; demographics last.
- Never make an opinion question required — forced answers are noise.

### Questionnaire format

```markdown
# Survey: {topic}

- **Learning goals:** {2–4, each with the decision it informs}
- **Target respondents:** {profile + screening criteria}
- **Estimated length:** {n questions, ~X min}

## Screening
S1. {question} → disqualify if {answer}

## Questions
Q1. {question} [type: single choice | likert-5 | open | …]
   - {options if applicable}
   > Goal: {which learning goal this serves}
```

The `> Goal:` annotations are for the team, not the respondent — strip them when pasting into the survey tool.

## Analyzing the results

- **Report the denominator first.** n, response rate if known, and how respondents were recruited — every claim inherits these limits. With n < 30 per segment, report patterns as directional, never as percentages with confidence.
- **Closed questions:** distribution per question, then cut by the segments that matter (from screening/demographic questions). A difference between segments is the finding; an overall average usually hides it.
- **Open-ends:** code them like interview data — group responses into recurring themes, count mentions per theme, keep 1–2 verbatim quotes per theme as evidence.
- **Map back to goals.** Structure the analysis by learning goal, not by question order: what did we believe, what did the data show, what's the decision.
- **Honesty over neatness.** Surveys say *what*, not *why* — flag every "why" the data raises as a candidate for follow-up interviews. Note self-selection and wording limitations where they bite.

Insights extracted from survey data follow the same quality bar as the `insight-extraction` skill: actionable, grounded (in numbers or quotes), prioritized.

## Anti-patterns

- Surveying to discover (open exploration is interview work; surveys measure)
- Percentages quoted from tiny or self-selected samples without saying so
- Scale direction flipping mid-survey (respondents on autopilot answer the pattern, not the question)
- "Would you pay for X?" as a validation question — stated intent inflates wildly; ask about current behavior and spend instead
- Analyzing question by question instead of goal by goal
