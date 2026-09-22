---
name: design-survey
description: Design a survey questionnaire from what you want to measure or validate — grounded in your insights and assumptions, with a distribution plan (named channels, one link each, target n, dates), ready to paste into any survey tool
argument-hint: "[what you want to measure/validate, or an opportunity/insight/idea/spec file]"
disable-model-invocation: true
---

# /design-survey

Design a survey questionnaire, following the `survey-design` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the learning goals.** If the arguments state them or name a file (opportunity brief, insight, idea brief, spec), start there. Otherwise scan `product/` for candidates — the **Research agenda** rows of `product/opportunities/` briefs marked for a survey, what the latest `product/research/` file left as "needs primary research", assumptions to quantify, synthetic insights awaiting verification, a hypothesis needing numbers — propose 2–4 goals and confirm before proceeding. If the goals are exploratory "why" questions with no prior qualitative work, say that a survey is the wrong instrument and suggest `/design-interview` instead.

2. **Load context.** Read `product/overview.md`, the relevant personas, the opportunity brief when there is one (its segment is the respondent profile), and `product/research/`. Ask who the respondents will be and roughly how many are reachable; define the screening criteria against a persona/segment. Then ask **which channels the survey will go out through** — one question at a time, each with a recommended answer derived from the opportunity brief's segment and the personas (where do these people actually gather?), per the `survey-design` skill's distribution rules: named channels, whom each reaches and its bias, approximate reach (`unknown` is a valid answer — never invent a number), a target n per segment that matters, a first-review date. If the user names only an own channel (customers, followers, the product's community), say in one line that it over-represents the already satisfied and propose a second channel that reaches whom the first doesn't.

3. **Draft the questionnaire** per the `survey-design` skill: screening first, every question annotated with the goal it serves, under ~12 questions, 1–3 open-ends near the end, and — by default — the closing **screening + opt-in block**: the interview disqualifiers and "would you accept a 30-minute conversation?" with a contact field. In this flow the interviews are recruited among the respondents, so the survey is also the recruitment instrument; drop the block only if the user says interviews are off the table. The **Distribution** section is part of the questionnaire too, after the opt-in block: the channel table (channel, who it reaches and its bias, approximate reach or `unknown`, one link per channel), the target n per segment, the first-review date, and the close (a date, or "open until target n"). If the channels' summed reach cannot produce the target n at a reasonable response rate, say so here, before publishing.

4. **Present and iterate.** Walk the user through the goal→question mapping and the wording of the riskiest questions (anything near "would you…" gets rewritten to behavior). Adjust until they own it.

5. **Save** to `product/surveys/{YYYY-MM-DD-HHMM}-{slug}.md` (timestamp = creation date). Remind the user the `> Goal:` annotations and the Distribution section are internal — strip them when pasting into their survey tool (any tool works; the questionnaire is plain markdown) — and that it pays to create one link per channel in the tool (form copies, a URL parameter, or a hidden field) so the analysis can cut by channel.

6. **Close with the next step in one line:** distribute through the channels in the table; on the first-review date, bring the export (CSV or pasted) to `/analyze-survey` together with this design file — the opt-ins it lists become the recruitment pool for `/design-interview`.

## Language

Conversation and the saved questionnaire in the language of the conversation (or the respondents' language if the user says it differs).
