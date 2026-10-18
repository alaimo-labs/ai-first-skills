---
name: analyze-feedback
description: Analyze post-launch feedback (reviews, tickets, in-app survey comments, CS notes, social mentions) — tag each entry, group into themes with counts, severity and verbatims, and, when a metrics analysis exists, say which of its hypotheses the feedback supports or contradicts. Works on its own too
argument-hint: "<feedback file(s)> [metrics analysis file]"
disable-model-invocation: true
---

# /analyze-feedback

Turn a feedback corpus into counted themes and, when there are metrics, into evidence for or against each hypothesis, following the `feedback-analysis` skill. The agent tags, counts, and proposes; the user decides. **This skill never chooses the improvement and never invents entries.**

Input: $ARGUMENTS

## Workflow

1. **Resolve the corpus.** File paths (CSV, markdown, JSON exports), pasted entries, or files in `product/data/`. Identify per entry, where present: source, date, author segment or role, rating, text. Read the provenance (`real` or `synthetic`) from the file name or header, or ask. Find the latest metrics analysis for the feature in `product/insights/` (`{YYYY-MM-DD-HHMM}-metrics-{spec-slug}.md`), or take it from the argument; without one, the analysis runs on its own and says so in one line.

2. **Describe the corpus before analyzing:** n per source, period, and the known bias of each source (per `feedback-analysis`). If one source is more than half the corpus, say so: the themes will lean toward it. When a metrics analysis exists, say whether the corpus covers the same period and the same audience.

3. **Tag every entry** with the part of the feature it refers to and its type (`bug`, `usability`, `request`, `praise`, `complaint`). Entries about something else are counted as out of scope and left out. Show a sample of the tagging (a dozen entries, spread across sources) so the user can correct the criteria before the full count.

4. **Group into themes** with count, percent of the in-scope total, sources, segments, type, severity, trend when dates allow, and one or two verbatims each, quoted exactly. Single mentions go to weak signals, not themes. Count with code when the corpus is large (a script over the tagged entries, saved next to the analysis with the same name); never estimate counts.

5. **Against the metrics hypotheses** (only with a metrics analysis): per hypothesis, `supported`, `contradicted`, or `no signal`, with the themes, counts, and verbatims behind it. Name the themes that could explain the low metric but no hypothesis covered. For `no signal`, suggest how to ask directly — e.g. `/design-interview` with users who stopped using the feature.

6. **Show the full analysis, then save** to `product/insights/{YYYY-MM-DD-HHMM}-feedback-{slug}.md` with the header in `feedback-analysis`, once the user agrees — never ask to save content the user has not seen.

7. **Contrast against the overview's beliefs.** For `real` feedback only, offer to annotate a `[feature: {slug}]` belief a theme confirms or contradicts: `— confirmed/contradicted/weakened by [analysis file] (date)`. Feedback is self-selected: propose `weakened` rather than `contradicted` unless the metrics point the same way. Synthetic feedback proposes nothing. Nothing is written without approval; no `product/overview.md` → skip silently.

8. **Close in one line:** the decision is the user's — which hypothesis to act on, the smallest change that addresses it, and which metric should move. If the change alters what the spec says, suggest revising it with `/write-spec`; then reveal, collect data for one more period, and run `/analyze-metrics` again.

## Language

Conversation and the saved analysis in the language of the conversation; verbatims stay as written. Type tokens, hypothesis-check tokens (`supported`, `contradicted`, `no signal`), trend tokens, status keywords, and provenance labels are fixed English tokens, like `source:` values.
