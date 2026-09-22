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
- **Screening + opt-in block** — last, to recruit interviewees among the respondents: 1–2 disqualifiers stricter than the survey screening (the interview profile is narrower), one consent question ("would you accept a 30-minute conversation about this?"), and an optional contact field shown only to those who say yes. Never required; never before the substantive questions.

### Wording and ordering

- No leading ("How much do you love…"), no loaded terms, no double-barreled questions ("fast and reliable"), no jargon the respondent may not share.
- Ask about behavior and frequency ("in the last month, how many times…") over intention ("would you…").
- General before specific; behavior before opinion; demographics last.
- Never make an opinion question required — forced answers are noise.

### Distributing the survey

A questionnaire without a distribution plan is a document, not an instrument. The plan lives in the same file, in the **Distribution** section, and follows the same standard as the recruitment plan of the `interview-guides` skill:

- **Named channels.** Own customer base, a named email list, a named community, a named LinkedIn group, a panel. Never "social media" or "my network".
- **Who each channel reaches, and its bias.** Per channel: which segment or persona it reaches and whom it over- or under-represents. An own channel (customers, followers, the product's community) over-represents people who are already satisfied — say it in the table, don't discover it in the analysis. If only own channels are listed, add one that reaches whom they don't.
- **One link per channel** — form copies, a URL parameter, or a hidden field, depending on the tool — so every response knows where it came from and the analysis can cut by channel.
- **A target n per segment that matters, not a total.** Below 30 per segment, results are directional. If the channels' summed reach cannot produce that n at a reasonable response rate, say so before publishing. Unknown reach stays `unknown` — never an invented number.
- **Dates.** A first-review date always; the close may stay open ("open until target n"). Long windows are fine: a survey collecting responses while the team keeps working is normal.

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

## Screening + opt-in (interview recruitment)
R1. {disqualifier for the interview profile} → not a candidate if {answer}
R2. Would you accept a 30-minute conversation about this? [yes / no]
R3. If yes, how can we reach you? [open, optional]

## Distribution
| Channel | Who it reaches | Approx. reach | Link |
|---|---|---|---|
| {named channel} | {which segment / persona, and whom it over- or under-represents} | {n people it reaches, or unknown} | {one link per channel} |

- **Target n:** {per segment that matters; below 30 per segment, results are directional}
- **First review:** {date}
- **Closes:** {date, or "open until target n"}
```

The `> Goal:` annotations are for the team, not the respondent — strip them when pasting into the survey tool. The Distribution section is for the team too: it stays in the file and never goes into the tool. A survey file without it (written before the section existed) is read normally; the analysis then asks for the channel.

## Analyzing the results

- **Report the denominator first.** n, response rate if known, and how respondents were recruited — read from the design file's Distribution section when it has one (channels, reach, target n), asked otherwise — every claim inherits these limits. With reach known and the channel in the export, report the response rate per channel. With n < 30 per segment, report patterns as directional, never as percentages with confidence.
- **Cut by channel when the export carries it.** A strong difference between channels is a finding about the sample before it is a finding about the segment — say so, and weigh the channel that over-represents the satisfied accordingly.
- **Closed questions:** distribution per question, then cut by the segments that matter (from screening/demographic questions). A difference between segments is the finding; an overall average usually hides it.
- **Open-ends:** code them like interview data — group responses into recurring themes, count mentions per theme, keep 1–2 verbatim quotes per theme as evidence.
- **Map back to goals.** Structure the analysis by learning goal, not by question order: what did we believe, what did the data show, what's the decision.
- **List the opt-ins.** When the design carried the screening + opt-in block, close with the recruitment pool: who accepted a conversation, tagged by whether their answers confirm or contradict the beliefs at stake — interviews should go first to the ones who contradict.
- **Honesty over neatness.** Surveys say *what*, not *why* — flag every "why" the data raises as a candidate for follow-up interviews. Note self-selection and wording limitations where they bite.

Insights extracted from survey data follow the same quality bar as the `insight-extraction` skill: actionable, grounded (in numbers or quotes), prioritized.

## Anti-patterns

- Surveying to discover (open exploration is interview work; surveys measure)
- Percentages quoted from tiny or self-selected samples without saying so
- Scale direction flipping mid-survey (respondents on autopilot answer the pattern, not the question)
- "Would you pay for X?" as a validation question — stated intent inflates wildly; ask about current behavior and spend instead
- Analyzing question by question instead of goal by goal
- A survey with no named channel — "we'll share it" is not a distribution plan
- A survey that goes out through one own channel only and is analyzed as if it represented the segment
- One link for every channel — responses that don't know where they came from can't be cut by channel
