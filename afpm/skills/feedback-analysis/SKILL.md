---
name: feedback-analysis
description: How to analyze post-launch feedback — support tickets, store reviews, in-app survey comments, sales and Customer Success notes, social mentions — the bias of each source, tagging every entry, grouping into counted themes with severity and verbatims, weak signals, and checking the hypotheses of a metrics analysis against the themes. Use when analyzing reviews, tickets, NPS or CSAT comments, user feedback after a release, or when looking for why a feature metric is low.
---

# Feedback Analysis

After a feature is revealed, feedback arrives on its own: tickets, reviews, comments on the in-app survey, notes from sales and Customer Success. It is not an interview and not a survey — nobody chose who speaks. **Feedback analysis** turns that corpus into counted themes and, when there is a metrics analysis, into evidence for or against each of its hypotheses. The metrics say **what** is happening (see the `product-metrics` skill); the feedback says **why**.

It inherits the quality bar of `insight-extraction` (grounded, specific, prioritized, never invented) and the open-ended coding of `survey-design` (themes with mention counts and 1–2 verbatims each). The skill that runs it is `/analyze-feedback`; it works after `/analyze-metrics` or on its own (e.g. a batch of NPS comments).

## Language

Write the analysis in the language of the conversation; verbatims stay in the language they were written in. Type tokens (`bug`, `usability`, `request`, `praise`, `complaint`), trend tokens (`new`, `growing`, `stable`, `n/a`), hypothesis-check tokens (`supported`, `contradicted`, `no signal`), and provenance labels are fixed English tokens, like `source:` values.

## Sources and their bias

| Source | Who it over-represents |
| --- | --- |
| Support tickets | The most stuck — people who hit a wall and cared enough to write |
| Store reviews | The very happy and the very angry |
| In-app survey comments | Whoever saw the survey at that moment and bothered to type |
| Sales and Customer Success notes | Large accounts, and the account's champion rather than its users |
| Social mentions | The vocal, and whatever is easy to say publicly |
| Post-launch research sessions | Whoever accepted a session — usually the engaged |

**Those who abandon in silence appear in no source.** They show only in the metrics. That is why "nobody complained" never means "there is no problem", and why the feedback does not replace the metrics.

## Tag every entry

Each entry gets at least two tags: **what part of the feature** it refers to, and its **type** — `bug`, `usability`, `request`, `praise`, `complaint`. Keep, where present, the source, date, author segment or role, and rating. Entries that are not about the feature are counted as **out of scope** and left out of the analysis, saying how many. Show a sample of the tagging before the full count so the criteria can be corrected.

## Group into themes

Per theme: how many entries, what share of the in-scope total, which sources and segments it comes from, its type, its **severity** (frequency × intensity — how often it appears and how badly it blocks or angers), one or two verbatims quoted exactly, and its **trend** when the corpus has dates (`new`, `growing`, `stable`; `n/a` without dates). A theme with a single mention is a **weak signal**, not a theme. Count with code when the corpus is large; never estimate counts.

When one source is more than half the corpus, say so up front: the themes will lean toward its bias.

## Against the metrics hypotheses

When a metrics analysis with hypotheses exists, each hypothesis is checked against the themes:

- `supported` — which themes, how many entries, which verbatims.
- `contradicted` — what in the feedback goes against it.
- `no signal` — the feedback says nothing about it. It may be necessary to ask directly, e.g. interviewing people who stopped using the feature.

Name also the themes that could explain the low metric but no hypothesis covered. **The feedback does not choose the improvement**: it makes some hypotheses stronger and others weaker; the PM decides which one to act on.

## Provenance

Feedback from people of the segment is `real`; generated or simulated feedback, or comments from internal testers acting as users, is `synthetic`. Feedback is self-selected, so even `real` feedback proposes `weakened` rather than `contradicted` for a belief in `product/overview.md`, unless the metrics point the same way. `synthetic` feedback annotates nothing.

## File format

```markdown
---
source: real | synthetic
corpus: {file(s) in product/data/}
metrics-analysis: product/insights/{file} | none
period: {from} to {to}
---

# Feedback analysis: {feature or scope}

## Corpus
{n entries per source, period, out-of-scope count, known biases of each source.}

## Themes
### F1. {theme}
- **Entries:** {n} ({percent}) · **Sources:** … · **Segments:** …
- **Part of the feature:** …
- **Type:** bug | usability | request | praise | complaint
- **Severity:** {frequency × intensity}
- **Trend:** new | growing | stable | n/a
- > "{verbatim}"

## Against the metrics hypotheses
{Only with a metrics analysis. Per hypothesis: supported | contradicted | no signal, with the themes, counts and verbatims behind it. Themes no hypothesis covered.}

## Weak signals
{Single mentions worth watching.}
```

Save to `product/insights/{YYYY-MM-DD-HHMM}-feedback-{slug}.md`. The corpus enters from `product/data/` (exports, not edited).

## Anti-patterns

- Reading the feedback without counting
- Treating one striking verbatim as a theme
- Mixing out-of-scope entries into the counts
- Forgetting the bias of each source
- Concluding there is no problem because nobody complained
- Choosing the improvement from the feedback without going through the metrics
- Inventing or paraphrasing entries as if they were verbatims
