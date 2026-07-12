---
name: extract-insights
description: Extract actionable product insights from one or more interview transcripts (synthetic or real)
argument-hint: "[transcript file(s) or persona name; defaults to the latest interview]"
disable-model-invocation: true
---

# /extract-insights

Extract insights from interview transcripts, following the `insight-extraction` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve sources.** If files or a persona were named, use those transcripts from `product/interviews/`. With no arguments, use the most recent transcript — or, if the current conversation contains a just-finished interview, use that directly. The user may also paste a transcript of a real interview.

2. **Extract** 3–5 insights per the `insight-extraction` skill: grounded in quotes, actionable, quantified when possible, prioritized by impact, in the transcript's language.

3. **Cross-interview synthesis.** When multiple transcripts are involved, flag insights that recur across interviewees.

4. **Save** to `product/insights/{slug}-{YYYY-MM-DD}.md` with a header listing sources and `source: synthetic` when applicable (include the one-time reminder that synthetic insights are hypotheses to verify with real users).
