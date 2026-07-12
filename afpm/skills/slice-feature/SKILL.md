---
name: slice-feature
description: Turn a feature spec's hypothesis into an Exposure Plan — accumulative reveal levels that each test one falsifiable belief
argument-hint: "<spec file> [flags|incremental]"
disable-model-invocation: true
---

# /slice-feature

Generate an Exposure Plan for a feature spec, following the `exposure-plans` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the spec.** A file path (look in `product/specs/` first) or pasted content. If nothing resolvable, ask for the spec.

2. **Resolve the mechanism preference.** If the user passed `flags` or `incremental`, it's binding. Otherwise the skill recommends one.

3. **Build the plan** per the `exposure-plans` skill: locate or derive the hypothesis (confirm with the user if derived), decompose into sequenced falsifiable beliefs, 1–5 accumulative levels each with belief/audience/duration/validation, mechanism note, parallel validations, open questions. Same language as the spec.

4. **Save** to `product/exposure-plans/{spec-slug}.md`.
