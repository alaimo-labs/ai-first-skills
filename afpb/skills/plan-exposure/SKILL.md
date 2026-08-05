---
name: plan-exposure
description: Build an Exposure Plan for a hypothesis or spec — accumulative reveal levels, each testing one falsifiable belief
argument-hint: "<hypothesis/spec file or description> [flags|incremental]"
disable-model-invocation: true
---

# /plan-exposure

Generate an Exposure Plan, following the `exposure-plans` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the source.** A hypothesis file (`product/hypotheses/`), a spec file (`product/specs/`), or a description given inline. If nothing resolvable, ask. If a hypothesis file exists for this feature, use its hypothesis verbatim as the spec-level hypothesis.

2. **Resolve the mechanism preference.** `flags` or `incremental` if passed — binding. Otherwise the skill recommends one and names the driver.

3. **Build the plan** per the `exposure-plans` skill: sequenced falsifiable beliefs, 1–5 accumulative user-visible levels with belief/audience/duration/validation, mechanism fit note, parallel validations, open questions. Same language as the source document.

4. **Present and confirm.** Show the full plan in the conversation — never ask to save (or save) a plan the user hasn't seen. Walk them through the belief sequence and the levels; adjust until they own it.

5. **Save** to `product/exposure-plans/{YYYY-MM-DD-HHMM}-{slug}.md` (timestamp = creation date; revise in place without renaming) once the user agrees.

Close in one line: suggest building Level 1 and wiring the instrumentation defined in the hypothesis before revealing anything.
