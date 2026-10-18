---
name: product-metrics
description: How to measure a revealed feature with the four AARS metrics — acquisition, activation, retention, satisfaction — each a percentage of the target audience, with an observable signal, an expanded definition, a justified signal threshold, a target reconciled with the exposure plan, and the events to instrument; how to read them as a funnel, read a retention curve, and diagnose which one is low. Use when defining success metrics or KPIs for a feature, deciding what to instrument, setting activation or retention criteria, reading usage data after a release, or diagnosing why a feature is not being used.
---

# Product Metrics (AARS)

An exposure plan says what to reveal to whom and when to advance or stop; it does not say how the feature is measured once people have it. **AARS** — **Acquisition, Activation, Retention, Satisfaction** — is the adaptation of AARRR used here: four metrics per feature, each a percentage of the same target audience, each answering a different question. The metrics say **what** is happening; the feedback says **why** (see the `feedback-analysis` skill).

Two skills run it, one per moment, like `/design-survey` and `/analyze-survey`: `/design-metrics` defines what is measured before the level is revealed; `/analyze-metrics` computes the metrics from usage data and proposes a diagnosis. Defining and reading are separate so the definition — and the target — is fixed before anyone sees a number.

## Language

Write the metrics file and the analysis in the language of the conversation. Metric tokens (`acquisition`, `activation`, `retention`, `satisfaction`), `status:` values (`designed`, `analyzed`), result tokens (`on target`, `below target`, `not computable`), and provenance labels are fixed English tokens, like `source:` values.

## The four metrics

| Metric | Question | Calculation |
| --- | --- | --- |
| `acquisition` | What share of the target audience reaches the feature? | users who reached it / target audience |
| `activation` | What share gets value from it? | users who got value / target audience |
| `retention` | What share uses it recurrently? | recurring users / target audience |
| `satisfaction` | What share is satisfied with it? | satisfied users / target audience |

## The target audience is the denominator

All four are computed over the **same** base. It comes from the overview's segment and, while the feature is in an exposure plan, from the audience of the level revealed. Never "all users": a metric over a generic audience is not actionable — it mixes people who have the problem with people who never will. In a collaborative feature, the audience is defined per person, not per account, and the definition says whether only the person who **initiates** counts or the **participants** too (they often need separate readings: the leader who opens the feature and the team that receives what it produces).

## Each metric has five parts

- **Signal:** an observable, measurable behavior in the product. Never an internal state ("understands", "is interested").
- **Expanded definition:** who counts and under which conditions (e.g. every participant of a meeting in which someone opened the feature).
- **Signal threshold:** the line that separates "opened it" from "got value", with its reason. It is not arbitrary: it comes from what getting value means in this feature, ideally from the spec's hypothesis. It says what it excludes.
- **Target:** the expected percentage of the audience, so the metric can be called low. It is reconciled with the advance / stop criteria of the exposure-plan level — it never contradicts them — and it is set before the data arrives.
- **Events needed:** what the product must log to compute it — event names and the properties the expanded definition needs (person, role, account, level, timestamp).

## Retention follows the expected frequency

The retention signal follows the natural frequency of the problem: a problem that shows up several times a week is measured weekly; one that shows up once a month, monthly. A retention measured on the wrong window produces a number that means nothing — a monthly problem measured weekly looks like churn. The frequency comes from evidence (interviews, a survey analysis); when nothing measures it, it is proposed and marked as an assumption.

**Reading the cohort curve.** Group users by the period they first activated and follow each cohort over the expected-frequency window. A curve that falls and then **flattens** means a group found value and stays; a curve that **keeps falling** without flattening means the feature loses users all the time. With few cohorts or small ones, the reading is directional and says so.

## Satisfaction has its own instrument

Satisfaction is measured with an in-app survey, CSAT, or NPS — never inferred from behavior: someone can use the feature often and be dissatisfied because they have no alternative. The metric names the **instrument**, the **question**, **when it shows** (e.g. right after the third use), and the **cut** (e.g. 4 stars or more). The AARS value stays over the target audience; the analysis also reports the response rate and the share among respondents, because a low response rate limits what the number can say.

## The metrics as a system

Acquisition, activation, and retention form a **funnel**: without reaching there is no value, without value there is no return. Satisfaction measures another dimension. If acquisition is low, improving activation does not move the total. Always read the **conversion between stages** too (of those who reached, how many got value; of those who got value, how many came back) — it locates the drop that the totals hide.

## Diagnostic patterns

Before diagnosing a low metric, check that its signal is well defined and that the data captures it: a signal threshold too strict, a window that does not follow the expected frequency, or a missing event can produce a low reading by itself.

| Pattern | What it suggests | Where to look for the why |
| --- | --- | --- |
| Low acquisition, the rest high | The feature works but people don't find it: visibility, onboarding, communication | Navigation, the steps before the acquisition signal |
| They reach it but don't activate | First use with friction, expectation not met, a usability or trust problem | Tickets, first-use comments, drop-off per step |
| They activate but don't come back | The problem is less frequent than assumed, a better alternative for recurring use, the second time is worse than the first | Feedback from those who stopped; revisit the expected frequency |
| They come back but aren't satisfied | Captive users: they use it because they have no other option. The most dangerous pattern in the long run | Comments behind the low ratings, reviews |
| High satisfaction, low retention | Liked but no habit, or rarely needed | Comments from satisfied users who did not come back |

The diagnosis ends in **hypotheses**, not in an improvement: specific and verifiable, each citing what in the data points to it (a step where people drop, a segment that behaves differently, a cohort) and naming what would confirm or contradict it — a feedback theme, a source, a direct question to users. The improvement is the PM's decision.

## Feature metrics vs. business metrics

AARS measures whether the user uses the feature as expected. The impact on the business — viability, what the sponsor needs to see — is measured apart and read alongside: when they diverge (usage up, business flat, or the reverse), there is something to investigate. Business metrics come from `product/overview.md` (the sponsor section, `[viability]` beliefs) as declared; they are never invented. None declared → `none declared`, and the feature is measured for the user only.

## Provenance

Usage data carries its provenance like any other evidence: `real` (logged from people of the segment using the product) or `synthetic` (generated, simulated, or from internal testers acting as users). Only `real` data annotates a belief in `product/overview.md` — `— confirmed/contradicted/weakened by [analysis file] (date)` — and one short level with a small audience proposes `weakened` rather than `contradicted`. A `synthetic` run is a rehearsal of the calculation, never evidence about the segment.

## File format

```markdown
---
spec: product/specs/{file}
exposure-plan: product/exposure-plans/{file} | none
level: {level the metrics are set for}
status: designed | analyzed
---

# Metrics for: {feature name}

## Target audience
{Who, by behavior or role; source: overview segment + exposure level audience. Size if known. Initiator vs. participant when the feature is collaborative.}

## Expected frequency
{How often the problem shows up for this audience, and the evidence behind it — or `assumption`. Sets the retention window.}

## Acquisition
- **Signal:** {observable behavior}
- **Expanded definition:** {who counts, under which conditions}
- **Calculation:** users who {signal} / target audience, over {window}
- **Target:** {percent} · **Why:** {reason}
- **Events needed:** {event names and properties}

## Activation
- **Signal:** …
- **Expanded definition:** …
- **Signal threshold:** {the line between trying and getting value} · **Why:** {reason, tied to the spec's hypothesis} · **Excludes:** {what does not count}
- **Calculation:** …
- **Target:** … · **Why:** …
- **Events needed:** …

## Retention
- **Signal:** … per {expected frequency window}
- **Expanded definition:** …
- **Retention curve:** {cohort definition and window}
- **Calculation:** …
- **Target:** … · **Why:** …
- **Events needed:** …

## Satisfaction
- **Instrument:** {in-app survey / CSAT / NPS} · **Question:** … · **When it shows:** … · **Cut:** {e.g. 4+ stars}
- **Expanded definition:** …
- **Calculation:** users at or above the cut / target audience (response rate reported apart)
- **Target:** … · **Why:** …
- **Events needed:** …

## Business metrics
{From the overview / sponsor, as declared. `none declared` when there are none.}

## Exposure plan reconciliation
{One line per advance / stop criterion of the level: which AARS metric and target reads it.}
```

Save to `product/metrics/{YYYY-MM-DD-HHMM}-{spec-slug}.md` — one file per feature, timestamp = creation date, revised in place without renaming. `status:` moves `designed` → `analyzed` once an analysis of the level lands. When the next level is revealed, the same file is revised for it (`level:`, audience, targets) and goes back to `designed`; each analysis in `product/insights/` copies the definitions and targets it was read against, so earlier readings stay checkable.

The analysis is saved to `product/insights/{YYYY-MM-DD-HHMM}-metrics-{spec-slug}.md`, with the metrics file, the data source, the period, and `source: real | synthetic` in its header: per metric the numerator, the denominator, the window, the value, the target, and the result; the funnel conversions; the retention curve; the lowest metric against its target and the pattern it matches; the ranked hypotheses. Usage data enters from `product/data/` (exports, not edited).

## Anti-patterns

- Vanity metrics (sign-ups, visits, page views) as the signal of success
- Signals that are internal states ("understands", "finds it useful")
- A generic audience ("all users") as the denominator
- An activation threshold with no reason behind it
- A retention window that does not follow the frequency of the problem
- Satisfaction inferred from behavior
- Reading one metric in isolation, without the funnel
- Setting or moving the target after seeing the data — a moved target is recorded in `product/corrections.md` with the reason, never done silently
- Approximating a signal with another event without saying so
- Targets that contradict the advance / stop criteria of the exposure plan
- Estimating a number by reading the data instead of computing it
