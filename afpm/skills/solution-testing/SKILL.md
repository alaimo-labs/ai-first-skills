---
name: solution-testing
description: How to test a solution alternative before building it — problem evidence vs. solution evidence, the cheapest test that could refute the riskiest belief, the test menu by risk (concierge, Wizard of Oz, prototype shown, usability test, technical test, fake door, buyer conversation), thresholds and decision rules written before the run, provenance of results, and the tests file format. Use when deciding how to test an idea or alternative before a spec, designing a prototype test or concierge test, choosing a signal and threshold for an experiment without a product, analyzing solution test results, or deciding whether an alternative continues, changes, or is discarded.
---

# Solution Testing

A solutions file ends with alternatives chosen **for testing**, not for building. **Solution testing** is the step between the exploration and the spec: for each alternative under test, find the belief that would kill it, design the cheapest test that could refute that belief, run it, and decide with the result. Only what survives gets specified. Customer Development, Lean Startup, and Product Discovery agree on the order: alternatives → riskiest belief of each → the cheapest test that could refute it → run it → decide → then, and only then, specify.

Three skills run it, one per moment, like `/design-survey` and `/analyze-survey`: `/design-solution-tests` decides what is tested and how the result is read; `/build-solution-test` builds the material one test needs; `/analyze-solution-tests` turns the results into a decision. Separating design from build protects the test: the material is built to produce the signal the design fixed, not the other way around, and whoever builds does not change what is measured.

## Language

Write the tests file and the material in the language of the conversation (the material is shown to participants). Risk tags, test-type tokens, `status:` values, result tokens (`passed`, `failed`, `inconclusive`, `not run`), decision tokens (`continue`, `change`, `discard`), and provenance labels are fixed English tokens, like `source:` values.

## What a solution test is for

To refute, before building, the belief that would kill an alternative. **One belief per test.** What is validated is the belief, never the prototype: a prototype that "worked" says nothing unless the test said in advance which belief it was supposed to break and what signal would break it.

## Problem evidence vs. solution evidence

Interviews and surveys about the pain prove the **problem**: that it exists, for whom, how often, what it costs. They say nothing about whether a given solution relieves it — nobody in those conversations saw or reacted to the solution. The desirability of a solution has evidence only when someone **reacted to that solution or to one very like it**: used it, saw it and did something, committed to something. Without that, the alternative's value belief is open, no matter how many interviews the problem has behind it.

The rule in the solutions file follows from this: a desirability judgment that cites only problem evidence reads `mixed` at most, and says why ("pain evidenced, relief not tested"). It rises to `strong` only with evidence of a reaction to the solution.

## The test menu by risk

The four risk categories of `feature-specs`, with their default owners. Value and usability signals are behavioral; feasibility signals may be technical — they are not forced into user behavior.

| Risk | The question | Typical cheap tests | Signal |
| --- | --- | --- | --- |
| `[value]` | Do they want it? | **Concierge** (do it by hand for a few people), **Wizard of Oz** (simulate the system behind the scenes), **prototype shown** with a concrete commitment asked for (schedule, pay, bring their team), **fake door** | Behavior or commitment — never "I like it" |
| `[usability]` | Can they figure it out? | **Usability test**: a prototype and five people from the segment doing a real task | Task completion, where they get stuck, time |
| `[feasibility]` | Can it be built? | **Technical test** with real data or a known answer key (e.g. a prompt's accuracy against a key), a consultation with tech | A technical metric with a threshold (accuracy, time, cost). Owner: tech |
| `[viability]` | Does it work for the business? | **Buyer conversation** with whoever decides the purchase or with the sponsor, a **price test** | Commitment or an explicit condition from the one who decides |

Test-type tokens: `concierge`, `wizard-of-oz`, `prototype-shown`, `usability-test`, `technical-test`, `fake-door`, `buyer-conversation`, `price-test`. Another type is fine when none fits, named in the same style.

## The cheapest first (steps)

For each belief, the smallest and fastest test that could refute it. If it passes, the **next step** is a bigger test — more people, more time, more realism. A multi-week pilot is a late step, never the first one: it costs weeks to learn what a prototype shown to five people in an afternoon could have said. Each step is designed and analyzed separately, with its own threshold.

## Quality bar

Everything written **before** the test runs:

- **One belief per test**, quoted as it stands in the registry (`product/overview.md`). Not in the registry yet → it is registered first, with approval.
- **What is done, with whom** (segment and how many), **what material** it needs, **how long** it lasts.
- **What is measured and the threshold** — the line between pass and fail, in a number or an observable fact.
- **What is decided for each result**, per alternative: `continue`, `change`, or `discard`. A test whose result would not change the decision is not run.
- **Expected provenance.** With real people from the segment, `real`. With colleagues, classmates, or acted roles, `synthetic`: good for rehearsing the test, never for deciding — and it never annotates a belief.

## Reading the results

Each test comes out `passed`, `failed`, or `inconclusive` (too few people, the test did not run as designed, the signal was not captured); a test that did not run is `not run`. The threshold is the one written before the run; moving it after seeing the data is recorded in `product/corrections.md` with the reason, never done silently. The decision per alternative follows the rule written in the test; a decision that departs from the rule is recorded the same way.

`change` means the alternative continues in a different version — the changed version needs its own test, because the result applies to what was tested, not to what comes after. That is also why **what was tested is fixed downstream**: a spec that changes the mechanism, who does what, the behavior measured, or the segment of a tested alternative invalidates the result, and the belief is open again for the new version.

Only `real` results move beliefs: `— confirmed/contradicted/weakened by [tests file] (date)`. A single small test proposes `weakened` rather than `contradicted`.

## File format

```markdown
---
opportunity: {slug}
solutions: product/solutions/{file}
status: designed | ready | analyzed
---

# Solution tests for: {opportunity title}

## Why test
{2 to 4 lines: which alternatives are under test and what the evidence does not yet show about each solution.}

## T1. {alternative slug}: {short name of the test}
- **Test status:** designed | ready | analyzed
- **Belief under test:** {as registered in product/overview.md, quoted}
- **Risk:** [value] | [usability] | [feasibility] | [viability]
- **Test type:** {concierge | wizard-of-oz | prototype-shown | usability-test | technical-test | fake-door | buyer-conversation | price-test | ...}
- **What we do:** {steps}
- **With whom:** {segment, how many, how they are recruited}
- **Material needed:** {the minimum the material must have to produce the signal; what is deliberately left out} | none needed
- **Material:** {link to product/tests/materials/{test-slug}/, added by /build-solution-test; `none needed` when the test needs no material}
- **Duration:** {time box}
- **Signal and threshold:** {what is measured and the line}
- **Decision rule:** continue if … · change if … · discard if …
- **Expected provenance:** real | synthetic
- **Next step if it passes:** {the next, bigger test, or "ready for spec"}

## T2. …

## Results
{Added by /analyze-solution-tests. Per test: what was observed, with whom and how many, provenance, result `passed | failed | inconclusive | not run`, and the decision taken.}

## Decision
{Added by /analyze-solution-tests: what continues, what changes, what is discarded, and why.}
```

Save to `product/tests/{YYYY-MM-DD-HHMM}-{opportunity-slug}.md` — timestamp = creation date; the file is revised in place without renaming as tests become `ready` and results land. File `status:` moves `designed` → `ready` (every test that needs material has it) → `analyzed`. Each test carries its own `Test status` (`designed` → `ready` once its material exists → `analyzed` once its result is in the Results section); a file may be `analyzed` while a test that was `not run` stays `designed` or `ready`, so the next analysis finds it. Material lives in `product/tests/materials/{test-slug}/`, written only by `/build-solution-test`: a prototype, a prompt with its input set and answer key, a facilitation script, a fake-door page, and always a **capture sheet** — what to record per participant or per run so the signal and the threshold can be read afterwards.

## Anti-patterns

- Testing "the prototype" instead of a belief — a test with no belief has no threshold and no decision
- Starting with the big pilot, or with building the feature
- Opinion signals for value or usability ("they liked it", "it seemed useful") — behavior or commitment, or it is not a signal
- Setting or moving the threshold after seeing the data
- Treating a run with colleagues, classmates, or acted roles as real evidence — it is a rehearsal, labeled `synthetic`
- A test that, whatever its result, does not change the decision
- Designing the test around the favorite alternative instead of around its riskiest belief
- Building material the design did not ask for — every extra feature is something the test does not observe
- Adjusting the signal or the threshold while building the material — if the material cannot produce the signal, the test goes back to design
- Specifying an alternative whose tested version the spec then changes, without saying that the result no longer applies
