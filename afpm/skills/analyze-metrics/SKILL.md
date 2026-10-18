---
name: analyze-metrics
description: Compute the four AARS metrics of a feature from usage data with the definitions in its metrics file, plus the funnel and the retention curve, mark which metric is below target, and propose ranked hypotheses for why. Metrics are designed with /design-metrics; feedback is read next with /analyze-feedback
argument-hint: "<metrics file> <usage data file(s)>"
disable-model-invocation: true
---

# /analyze-metrics

Turn usage data into the four AARS metrics and a first diagnosis, following the `product-metrics` skill. The agent computes and proposes; the user decides. **This skill never estimates a number it cannot compute, never moves a target, and never chooses the improvement.**

Input: $ARGUMENTS

## Workflow

1. **Resolve the inputs.** The metrics file in `product/metrics/` (from the argument, or the latest with `status: designed`); without one, suggest `/design-metrics` in one line. The usage data: a file path (CSV or JSON event export, or an aggregated table), pasted data, or files in `product/data/`. Read the data's provenance from its file name or header, or ask: `real` (people of the segment using the product) or `synthetic` (generated, simulated, or internal testers acting as users).

2. **Check the data against the definitions before computing.** Per metric: are the events and properties its signal needs present? Is the target audience identifiable (role, account, level)? Does the period cover the retention window? Is the satisfaction instrument's response in the data? Report the gaps per metric. A metric whose signal the data does not capture is reported as `not computable`, naming the missing event; it is never approximated with another event without saying so and getting approval — an approved approximation is labeled as such in the analysis.

3. **Compute with code, not by reading.** Write and run a script over the file with exactly the definitions in the metrics file: the four metrics over the target audience, the conversion between funnel stages (reached → got value → came back), and the retention curve by cohort over the expected-frequency window; for satisfaction, also the response rate and the share among respondents. Show the numerator, the denominator, and the window of each metric, so the user can check the calculation. Save the script next to the analysis (same name, script extension) so the numbers can be reproduced; `product/data/` stays untouched.

4. **Read against the targets.** Per metric: value, target, and `on target`, `below target`, or `not computable`. Name the metric lowest against its target and the pattern it matches (per `product-metrics`). Read the retention curve: flattening or still falling, directional when cohorts are few or small. Before diagnosing, check whether the low reading could come from the definition itself — a signal threshold too strict, a window that does not follow the expected frequency, an event logged inconsistently — and say so if it could. The target is the one in the file; if the user wants to change it now, point out in one line that it was set before seeing the data, and if they insist, record the change in `product/corrections.md` with the reason (approval required; a `## {YYYY-MM-DD}` heading with **Artifact**, **AI proposed**, **Human decided**, **Why**).

5. **Propose hypotheses for the low metric**, ranked by how much of the gap each could explain. Each is specific and verifiable, cites what in the data points to it (a step where people drop, a segment or role that behaves differently, a cohort), and names what would confirm or contradict it: which feedback themes, which source, or a direct question to users. No generic hypotheses ("the product is not good"). Read the business metrics declared in the metrics file alongside when the data carries them; a divergence is a finding of its own.

6. **Show the full analysis, then save** to `product/insights/{YYYY-MM-DD-HHMM}-metrics-{spec-slug}.md` once the user agrees — header with the metrics file, the level, the data source, the period, and `source: real | synthetic`; the definitions and targets it was read against; per metric numerator, denominator, window, value, target, result; the funnel; the retention curve; the lowest metric and its pattern; the hypotheses. With approval, set the metrics file's `status: analyzed`. A `synthetic` run is saved as a rehearsal and says so in its first line.

7. **Contrast against the overview's beliefs.** For `real` data only, if a result confirms or contradicts a `[feature: {slug}]` belief, offer to annotate it on its own line: `— confirmed/contradicted/weakened by [analysis file] (date)`. One short level with a small audience proposes `weakened` rather than `contradicted`. Synthetic data proposes nothing. Nothing is written without approval; no `product/overview.md` → skip silently.

8. **Close in one line:** `/analyze-feedback` with the feedback of the same period, naming the hypotheses it should test; if the definitions caused the low reading, `/design-metrics` to revise them; if every metric is on target, the exposure plan's advance criterion and `/design-metrics` for the next level.

## Language

Conversation and the saved analysis in the language of the conversation. Metric tokens, result tokens (`on target`, `below target`, `not computable`), status keywords (`confirmed`, `contradicted`, `weakened`), and provenance labels are fixed English tokens, like `source:` values.
