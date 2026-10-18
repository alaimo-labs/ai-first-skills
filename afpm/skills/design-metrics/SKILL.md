---
name: design-metrics
description: From a spec and its exposure plan, define the four AARS metrics of a feature (acquisition, activation, retention, satisfaction) over the target audience — signal, expanded definition, signal threshold, calculation, target, and the events to instrument — before the level is revealed. Data is read later with /analyze-metrics
argument-hint: "<spec or exposure plan> [level]"
disable-model-invocation: true
---

# /design-metrics

Define how a revealed feature will be measured, following the `product-metrics` skill. The agent proposes; the user decides. **This skill never computes a metric, never reads usage data, and never invents a business metric** — reading the data belongs to `/analyze-metrics`.

It fills the gap after `/slice-feature`: the exposure plan says when to advance or stop each level, but not what counts as reaching the feature, getting value, coming back, or being satisfied — nor over which audience, nor with what target.

Input: $ARGUMENTS

## Workflow

1. **Resolve the feature.** From the argument — a spec in `product/specs/` or an exposure plan in `product/exposure-plans/` (each leads to the other by slug). Without a spec, say so in one line and suggest `/write-spec`. Without an exposure plan, continue for the whole feature, write `exposure-plan: none`, and say once that the target audience will be the spec's segment. When the plan has several levels and the argument does not say which, ask; recommend level 1 (or the next unrevealed level). If a metrics file for this spec already exists in `product/metrics/`, say so: revise it in place for the new level (its `status:` goes back to `designed`) rather than starting a second file.

2. **Load the evidence.** Read the spec (journey, stories, acceptance criteria, hypothesis and its refutation clause, the tested-before-spec section — found by meaning, since the spec's headings follow its language), the exposure plan (audience, duration, advance / stop criteria of the level), `product/overview.md` (segment, sponsor, business metrics, the `[feature: {slug}]` beliefs), the insights, survey analyses, and journeys the spec cites, and `product/corrections.md`. Facts that live in these artifacts are looked up, never asked.

3. **Set the target audience and the expected frequency first** — every metric depends on them. The audience: the overview's segment narrowed by the level's audience, by behavior or role, never "all users"; its size if known. In a collaborative feature, say whether initiators, participants, or both count, and propose separate readings when their behavior differs. The frequency: from the evidence (interviews, a survey analysis), naming the file; when nothing measures it, propose one and mark it `assumption`. It sets the retention window.

4. **Propose the four metrics, one at a time**, each with signal, expanded definition, calculation, target with its reason, and events needed — each proposal with a recommended answer the user accepts or changes. Push back, with the reason, on a signal that is an internal state or a vanity count. For **activation**, propose the signal threshold with its justification tied to the spec's hypothesis or to an open `[feature: {slug}]` belief, and say what it excludes (the line between trying and getting value). For **retention**, the window follows the expected frequency, plus the cohort definition for the curve. For **satisfaction**, propose the instrument, the question, the moment it shows, and the cut — never a behavioral proxy.

5. **Reconcile with the exposure plan.** For each advance / stop criterion of the level, say which metric and target reads it. If a target contradicts a criterion, say so and ask which one moves; never leave both. A criterion no metric reads is named too.

6. **Bring the business metrics** declared in the overview (the sponsor section, `[viability]` beliefs), as declared. None declared → write `none declared` and say once that the feature will be measured for the user only.

7. **Show the full file in the conversation, then save** to `product/metrics/{YYYY-MM-DD-HHMM}-{spec-slug}.md` with `status: designed` once the user agrees — never ask to save content the user has not seen. When the user changed a proposed signal, threshold, or target, offer to record it in `product/corrections.md` (approval required; create on first use; a `## {YYYY-MM-DD}` heading with **Artifact**, **AI proposed**, **Human decided**, **Why**). Offer, with approval, to add the one-line link to the metrics file in the spec, per `feature-specs` (label in the spec's language; next to the tested-before-spec section, or right after the hypothesis when there is none).

8. **Close in one line:** reveal the level and collect usage data with the events listed — name the events the product must log — and the satisfaction instrument live; then `/analyze-metrics` with the export, once the level's duration has run.

## Language

Conversation and the saved file in the language of the conversation. Metric tokens (`acquisition`, `activation`, `retention`, `satisfaction`), `status:` values, and provenance labels are fixed English tokens, like `source:` values; event names follow whatever the product's instrumentation uses.
