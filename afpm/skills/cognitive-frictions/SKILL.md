---
name: cognitive-frictions
description: The Cognitive Friction Map (MFC) — four categories of cognitive friction (transformation, limiter, standardizer, evaluator points) for finding where AI adds real value in a user journey. Use when analyzing a journey or workflow for AI opportunities, identifying cognitive frictions or bottlenecks in user tasks, or deciding which steps of a process deserve an AI feature.
---

# Cognitive Frictions (MFC)

The Cognitive Friction Map (Mapa de Fricción Cognitiva, MFC) was created at Alaimo Labs from dozens of client engagements searching for real AI opportunities in existing products; these four categories capture most situations where AI generates genuine value.

A **cognitive friction** is any task that depends on human mental effort, judgment, or knowledge and could be automated, standardized, or amplified with AI. Frictions are the invisible bottlenecks that limit the quality, speed, and scalability of a process.

## Language

Produce the friction map in the language of the conversation. The framework's category names may keep their English form with a translation on first use.

## Why map frictions

Never add AI "because we can." Every AI feature should resolve a specific, observable friction that is limiting users — ideally one whose removal would move the product's input metrics. The map turns the vague question "where could AI help?" into a step-by-step diagnosis of the journey.

## The lens

For each step of the journey, ask:

- What type of mental effort does this step demand from the user?
- Is that effort the best use of their cognitive energy?
- Where does human processing become the bottleneck?

## The four categories

1. **Transformation Points** — the user acts as a translator between formats, contexts, or abstraction levels: converting information from the form it exists in to the form the task needs. Signals: "turn X into Y," adapting content per context, going from vague to concrete. Examples: converting a doctor's "you need more exercise" into a specific training plan; translating a monthly budget into per-category purchase decisions; turning "the app is confusing" feedback into technical requirements.

2. **Limiter Points** — the task is humanly possible, but its scale or complexity exceeds what the user can process in the time available: too much information, too many options, not enough attention. Signals: exhaustive comparison, manual review of large volumes, real-time monitoring of many signals. Examples: comparing 50 insurance options across 15 variables; screening 200 CVs to shortlist 5; watching 20 live performance metrics.

3. **Standardizer Points** — the user's personal judgment, mood, or interpretation introduces unwanted variability into a process that needs consistency; there is a pattern to follow but no clear guide enforcing it. Signals: "it depends who does it," quality varies by person or day. Examples: support agents answering the same question with different tones and solutions; teachers grading similar essays inconsistently; designers applying a brand guide differently in each piece.

4. **Evaluator Points** — the step requires specialized knowledge, experience, or expert judgment the user doesn't fully possess. Not missing information — missing the ability to interpret and apply it. Signals: decisions made with low confidence, "I wish an expert could look at this." Examples: a founder with no legal training judging a contract; first-time parents deciding whether symptoms warrant an urgent visit; a non-technical PM prioritizing tech debt against new features.

## Quality bar

- **Grounded in the step** — name the concrete mental effort and who bears it, not a generic "this is hard."
- **Don't force it** — not every step has a friction; a map where every step scores dilutes the real bottlenecks.
- **One "why" per category** — a step can show more than one category; name each with a one-line why, dominant first.
- **Problem ≠ friction** — the friction names the mental effort; the problem states its observable consequence for the user, in one falsifiable sentence.
- **Evidence metrics are real** — quantify each friction with data the repo already holds (analytics, survey results, insights, research). If nothing measures it yet, propose the metric to instrument and mark it "not yet measured" — never invent numbers.
- **Severity = frequency × intensity** — how often the step happens and how much effort or error it causes.
- **Metric impact** — name the input metric (or north-star input) the friction degrades. If the product declares no metrics yet, name the one it *would* affect, flagged as proposed.
- **Opportunity, not solution** — a friction describes the bottleneck, not the AI feature. Shaping the feature is a later step.

## Output format

For each step with friction:

```markdown
### {N}. {Step name}

- **Category:** {Transformation | Limiter | Standardizer | Evaluator — one or more, dominant first}
  - **Why {category}:** {one line per named category: what makes this step that kind of friction}
- **Friction:** {the mental effort demanded and who bears it — 1–3 sentences}
- **Problem:** {the observable consequence for the user, one falsifiable sentence}
- **Evidence metric:** {measurable signal from existing repo evidence; or the metric to instrument, marked "not yet measured"}
- **Severity:** {high | medium | low} — {frequency × intensity rationale}
- **Metric impact:** {which input metric it degrades; "proposed" if the product declares none yet}
```

Close with a ranked list of the top frictions (severity first) — these are the AI-opportunity candidates.

Save to `product/journeys/{YYYY-MM-DD-HHMM}-{journey-slug}.md`, with the journey itself (actor, goal, steps) at the top and the friction map below, and a header noting the persona involved (if any) and where the journey came from (elicited, spec, existing file).
