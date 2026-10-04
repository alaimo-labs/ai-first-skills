---
name: build-solution-test
description: Build the material for one solution test already designed with /design-solution-tests — a prototype, a prompt with its input set and answer key, a facilitation script, a fake-door page, a capture sheet — exactly what the design asks for to produce its signal, and nothing more
argument-hint: "<tests file> <test id, e.g. T2>"
disable-model-invocation: true
---

# /build-solution-test

Build what one designed test needs to run, following the `solution-testing` skill. One test per run. **This skill never changes what the test measures, never runs the test, and never builds the product** — the signal and the threshold belong to `/design-solution-tests`, the run to the team, the product to a later stage, after the spec.

The split exists to protect the test: the material is built to produce the signal the design fixed, not the other way around. Whoever builds does not get to change what is measured.

Input: $ARGUMENTS

## Workflow

1. **Resolve the test.** The arguments name a file in `product/tests/` and a test id (`T1`, `T2`, …). With a file but no id, list the tests whose test status is `designed` and whose **Material needed** is not `none needed`, and ask which one. With neither, take the latest tests file and do the same. A test already `ready` → say so and ask whether to rebuild its material (the old material is replaced; the design stays). A test whose Material needed is `none needed` → say so and stop: there is nothing to build. No tests file → suggest `/design-solution-tests` in one line.

2. **Read the design as fixed.** Load the belief under test, the risk, the test type, what we do, with whom, the signal and threshold, the decision rule, and the **Material needed** line. Restate in two lines what the material must make observable — the signal — and who sees it. The signal and the threshold are not reopened here; if they look wrong, say so and point to `/design-solution-tests`, then stop.

3. **Build the minimum, by test type** — only what the Material needed line asks for:
   - **Prototype** (`usability-test`, `prototype-shown`, the front of a `wizard-of-oz`): a single self-contained page or screen flow (plain HTML or markdown screens, whatever the repo supports without new tooling) with only the steps the task needs; fake data clearly marked as such; no feature the test does not observe, no navigation to screens the task does not visit.
   - **Technical test** (`technical-test`): the prompt or script, the input set it runs on (or how to assemble it from real data, with how many items), the answer key or reference it is compared against, and how the metric is computed against the threshold.
   - **Concierge or Wizard of Oz**: the step-by-step script for whoever plays the system — what the participant sees at each step, what happens behind the scenes, how long each step may take.
   - **Fake door**: the copy and the call to action, and what the person sees after clicking (the honest message that it does not exist yet, and what is asked of them).
   - **Buyer conversation or price test**: the conversation guide, with the commitment or the condition to ask for, stated so it can be recorded yes or no.
   - **Every test**: a **capture sheet** — what to record per participant or per run so the signal and the threshold can be read later, with the provenance of each participant (segment member or stand-in) — and the recruitment message when the test needs participants, following the design's "with whom".

4. **Check the material against the design before showing it.** Two questions: does it produce the signal the test measures, as written? does it add anything the design did not ask for? Remove what the second question finds. If the material cannot produce the signal as designed — the task cannot be observed with a prototype at this fidelity, the answer key cannot exist, the metric cannot be computed from what is captured — **stop and say so**: the design goes back to `/design-solution-tests`. Never adjust the signal or the threshold here.

5. **Show the material, iterate, then save** to `product/tests/materials/{test-slug}/` once the user agrees — `test-slug` = `{test id}-{alternative slug}`, e.g. `t1-recap-de-decisiones`; one file per piece (prototype, prompt, input set, answer key, script, capture sheet, recruitment message). With approval, update the test in the tests file: the **Material** line gets the link and the test status becomes `ready`; when every test that needed material is `ready`, the file's `status:` becomes `ready` too.

6. **Close in one line:** run the test with the capture sheet, then `/analyze-solution-tests` with the filled sheets. If other tests in the file still need material, name the next one.

## Language

Material in the language of the conversation — it is shown to participants (or in the participants' language if the user says it differs). Test-type tokens and status values are fixed English tokens.
