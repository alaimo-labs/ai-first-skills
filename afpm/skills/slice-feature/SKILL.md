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

4. **Present and confirm.** Show the full plan in the conversation — never ask to save (or save) a plan the user hasn't seen. Walk them through the belief sequence and the levels; adjust until they own it.

5. **Save** to `product/exposure-plans/{YYYY-MM-DD-HHMM}-{spec-slug}.md` (timestamp = creation date; revise in place without renaming) once the user agrees.
