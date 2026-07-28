---
name: map-frictions
description: Analyze a user journey step by step to identify cognitive frictions where AI could add real value (Cognitive Friction Map)
argument-hint: "[journey file or description; elicits the journey if none exists]"
disable-model-invocation: true
---

# /map-frictions

Map cognitive frictions across the steps of a user journey, following the `cognitive-frictions` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the journey.** If a file was named, use it. If the journey was described or pasted in the conversation, use that. If a spec in `product/specs/` contains a journey section, offer to analyze that journey. With nothing to start from, elicit it: who is the actor (link to a persona from `product/personas/` if one fits), what goal they pursue, and the steps from trigger to outcome — one user action or decision per step, typically 5–15. Confirm the step list before analyzing.

2. **Analyze each step** through the MFC lens per the `cognitive-frictions` skill: which of the four categories applies (if any — never force a friction onto a frictionless step) with a one-line why per category, the friction (mental effort), the problem (observable consequence, one sentence), the evidence metric, and severity as frequency × intensity. Evidence metrics come from data already in the repo (insights, survey analyses, research, analytics the user shares) — when nothing measures a friction yet, propose the metric to instrument marked "not yet measured", never invented numbers.

3. **Prioritize.** Rank the identified frictions by severity and state each one's metric impact — the input metric it degrades, per `product/overview.md` or specs. If the product declares no input metrics yet, note that once and mark each impact as proposed. The top of the ranking is the list of AI-opportunity candidates.

4. **Save** to `product/journeys/{YYYY-MM-DD-HHMM}-{journey-slug}.md`: journey (actor, goal, steps), the per-step friction map, and the ranked opportunities — in the language of the conversation, with a header noting the persona (if any) and the journey's source (elicited, spec, existing file).

5. **Suggest next steps** in natural language: shape the top friction into a feature idea with `/clarify-idea` or straight into a spec with `/write-spec`; or pressure-test whether the friction is real by interviewing a persona with `/interview-persona`.
