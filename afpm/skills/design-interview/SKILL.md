---
name: design-interview
description: Design an interview guide for real user research from what you want to learn or validate — grounded in your insights, assumptions, and personas
argument-hint: "[what you want to learn/validate, or an opportunity/insight/idea/spec file]"
disable-model-invocation: true
---

# /design-interview

Design an interview guide for research with real users, following the `interview-guides` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the learning goals.** If the arguments state them or name a file (an opportunity brief, insight, idea brief, or spec), start there. Otherwise scan `product/` for the strongest candidates — the **Research agenda** rows of `product/opportunities/` briefs marked for interviews, what the latest `product/research/` file left as "needs primary research", the "why"s a survey analysis raised, open assumptions in ideas/specs, insights marked `source: synthetic` awaiting verification, hypotheses — propose 2–4 goals and confirm with the user before proceeding.

2. **Load context.** Read `product/overview.md`, the personas relevant to the goals, the opportunity brief when there is one (its segment is the participant profile), `product/research/`, and — if a survey on the same goals has been analyzed — its analysis in `product/insights/` for the opt-in pool. Ask who the real participants will be; map them to a persona/segment so the guide's participant profile is concrete.

3. **Resolve the mode.** Exploration (open discovery) or validation (testing a specific idea/prototype). If not obvious from the goals, ask — one question, two options.

4. **Draft the guide** per the `interview-guides` skill: goals with their beliefs-at-risk and falsification notes, funnel structure, non-leading questions with probes, stimulus section only in validation mode.

5. **Present and iterate.** Walk the user through the goal→question mapping — every question they can't trace to a goal gets cut. Adjust until they own it.

6. **Draft the recruitment plan** — the guide's closing section: where, how, and how many.
   - **Channels:** the primary source is the survey respondents who opted in to a conversation, when a survey with the screening + opt-in block exists — selected by their answers, prioritizing those who contradict a belief over those who confirm it (the confirmers teach less). When that survey carries a **Distribution** section, the plan **references** it as the upstream source ("the opt-ins will come from the channels in [survey file]") instead of repeating its channels, and names channels of its own only for what the survey doesn't cover — a segment its channels don't reach. Without a survey, or to fill the gaps: where these participants actually are, named concretely — own customer base, communities, LinkedIn, intercepts, panels — not "social media".
   - **Screening:** 2–3 screener questions derived from the participant profile, with explicit disqualifiers — data from the wrong people is worse than no data.
   - **Target:** how many interviews (typically 5–8 per segment; saturation — answers start repeating — beats hitting a quota).

7. **Save** to `product/interview-guides/{YYYY-MM-DD-HHMM}-{slug}.md` (timestamp = creation date).

8. **Close with next steps in one line each:** pretest the guide before it meets real participants (`/test-interview-guide` — runs the guide against a synthetic persona and diagnoses what breaks), and after the real interviews, bring the transcripts to `/extract-insights`.

## Language

Conversation and the saved guide in the language of the conversation.
