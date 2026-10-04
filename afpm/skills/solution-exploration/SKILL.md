---
name: solution-exploration
description: How to explore and compare solution alternatives for one opportunity before committing to one — what makes an alternative genuinely different, the current workaround as the baseline, the desirable / feasible / viable filter with who owns each judgment, the value proposition of the chosen alternative, and the solutions file format. Use when comparing solution options, evaluating ideas against evidence, writing a value proposition, choosing between features for the same problem, or deciding what to build for a framed opportunity.
---

# Solution Exploration

An opportunity is a problem for a segment; a solution is one of many answers to it. **Solution exploration** is the step between them: open a set of genuinely different answers, evaluate each against the evidence, and let the user choose which one goes on to be clarified and specified. It is the divergent level of the Opportunity Solution Tree — several solutions hang from one opportunity, and the first one that shows up is rarely the best.

The skill that runs it is `/explore-solutions`; it feeds `/design-solution-tests`, which tests the riskiest belief of each alternative that came out before anything is built (see the `solution-testing` skill). **Chosen means chosen for testing**, not for building: the exploration is not a spec and not a test design; it ends with a decision, the value proposition of what was chosen, and one line per alternative under test saying which belief has to be tested and why.

## Language

Write the solutions file in the language of the conversation. Filter ratings, the note `pain evidenced, relief not tested`, provenance labels, `status:` values, outcome values (`chosen`, `discarded`, `parked`), and belief tags are fixed English tokens, like `source:` values.

## The tree as files

```
product/overview.md          outcome + [product] beliefs
product/opportunities/       one problem for one segment, with signals  → [opportunity: {slug}] beliefs
product/solutions/           alternatives compared for one opportunity, and the ones chosen for testing → proposes [feature: {slug}] beliefs
product/tests/               solution tests: design, results, decision per alternative (see `solution-testing`)
product/ideas/               clarified idea briefs — the path without exploration → [feature: {slug}] beliefs
product/specs/ → product/exposure-plans/
```

One solutions file per exploration, named after the opportunity. The tests file that descends from it (`product/tests/`) tests the riskiest belief of each alternative under test; the spec is written from the solutions file and the analyzed tests file, and links them under *Alternatives considered* and *Tested before spec*. `/clarify-idea` is the path **without** exploration — an idea that arrives already decided; an idea brief written over an explored alternative inherits its comparison and value proposition by reference and declares whether the alternative was tested. Skipping the exploration is allowed and declared: the idea brief records `solutions explored: no (declared)`.

## A real alternative vs. a variation

An alternative is real when it uses a **different mechanism** to relieve the same pain: automate vs. delegate vs. remove the need vs. change the rule vs. make the workaround less painful. A variation is the same mechanism with another name, another screen, or more features on top.

| Real alternatives (different mechanisms)                       | Variations of one idea                           |
| -------------------------------------------------------------- | ------------------------------------------------ |
| Automatic meeting notes · a shared decision log people fill in · a policy that every meeting ends with decisions read aloud · a template in the tool they already use | Automatic notes · automatic notes with tags · automatic notes with search · AI-summarized automatic notes |

The test: if two alternatives would be killed by the **same riskiest belief**, they are one alternative. A good set has 3 to 5 entries, at least one that is **not new software** (a process, a policy, a template, a change in a tool people already use) and one that is **the smallest thing that could work**. Non-software alternatives are not filler: often they win, and when they lose, they say what the software has to beat.

## The baseline is the workaround, not "do nothing"

People with a real problem are already solving it — badly, expensively, with a spreadsheet, a group chat, an intern, or by absorbing the cost. That workaround is what every alternative competes against, and it appears in the file as the baseline, cited from the evidence (interviews, survey analyses, research on non-consumption). "Do nothing" is not a baseline: it hides the cost people already pay and makes any alternative look good. When no artifact says what people do today, the baseline is written as `assumption` — and it is the first thing to check, because an alternative that is not clearly better than the workaround will not be adopted no matter how well it is built.

## The triple filter

Each alternative is judged on three questions. Each judgment is one of `strong | mixed | weak | unknown`, cites the file and its provenance (`real` / `survey` / `secondary` / `synthetic` / `unverified`) or is marked `assumption`. `unknown` is honest; an invented `strong` is not.

| Filter        | The question                                                                 | What counts as evidence                                                                 | Who owns the judgment |
| ------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------- |
| **Desirable** | Does it relieve the pain the evidence shows, for the persona that suffers it, better than the workaround? | **Solution evidence**: someone reacted to this solution or to one very like it (a test in `product/tests/`, a validation interview with real users, usage of a close substitute), `real` / `survey` first. **Problem evidence** — insights and survey analyses about the pain — supports `mixed` at most, with the note `pain evidenced, relief not tested`; synthetic evidence makes it promising, never strong | PM — defends it |
| **Feasible**  | Can it be built or put in place within the brief's constraints?             | Facts in the overview's what-we-know section, constraints in the brief, something tech already said | Tech — the PM consults; without evidence the cell reads `to check with tech`, never a guess |
| **Viable**    | Does it move the business outcome the opportunity names?                    | Commercial: revenue, retention, upgrade signals, pricing research; internal: the sponsor's metric or a cost avoided, in the sponsor's words | PM — defends it, with the sponsor as the tertiary source |

**Usability is not a filter here.** There is nothing to try yet; when the riskiest belief of an alternative is about usability, it is tested with a prototype in `/design-solution-tests`, before the spec. It enters the comparison only when an alternative depends on a behavior the evidence says these users will not adopt — then it is the riskiest belief, not a column.

**Every alternative names its riskiest belief:** the one that, if false, kills it, stated so an instrument could prove it wrong. That belief is what `/design-solution-tests` tests next; the comparison table without it is a scorecard, not a decision aid.

## The value proposition of the chosen alternative

No canvas, no six boxes. Written against the persona that suffers the problem, in four lines the persona would recognize:

- **Pain relieved** — cited from evidence, not from the pitch.
- **Gain created** — what is different afterwards, in the persona's terms.
- **Replaces** — the workaround, and why they would switch (what the workaround costs that this does not).
- **Deliberately does not** — the scope it leaves out on purpose; this line keeps `/clarify-idea` from growing the idea back.

Then the beliefs the alternative carries, stated falsifiably, proposed to the registry as `[feature: {slug}] [risk]` — the opportunity's beliefs referenced from their registered line, never duplicated; beliefs of discarded alternatives never registered.

## What has to be tested

The file closes the decision with one line per alternative under test: which belief has to be tested and why it is the one that would kill it. Not the test itself — what is done, with whom, the signal, the threshold, and the decision rule are designed in `/design-solution-tests` and live in `product/tests/`; writing them here would design the test around the favorite before anyone looked at the evidence per belief. Once the tests exist, the frontmatter carries `tests: {file}`; once they are analyzed, each alternative gets its outcome (`chosen`, `discarded`, `parked`) with a link to the tests file, and desirability cells that now have solution evidence are revised with the new file and provenance.

## File format

```markdown
---
opportunity: {slug}
status: chosen | testing-several | back-to-research
chosen: {alternative slug(s), or none}
tests: {product/tests/{file}, added by /design-solution-tests}
---

# Solutions for: {opportunity title}

## What the evidence says now
{3 to 5 lines: which beliefs moved and with what evidence; what is still open.}

## Baseline: what people do today
{The current workaround, cited — or `assumption`, and what would check it.}

## Alternatives
### A1. {name} (`{slug}`)
{What it is, which part of the problem it attacks, for which persona (name, type), what it replaces.}
### A2. …

## Comparison
| Alternative | Desirable | Feasible | Viable | Riskiest belief |
|---|---|---|---|---|
| A1 | strong (survey, n=…, {file}) | to check with tech | mixed (assumption) | … |

## Decision
{What was chosen for testing, by whom, why. The recommendation if it differed, and the reason for the difference (logged in corrections.md).}

## To test
- A1 — {belief to test, quoted}: {why it is the one that kills it}. Designed in /design-solution-tests.
- A2 — …

## Value proposition: {chosen alternative}
- Pain relieved: …
- Gain created: …
- Replaces: …
- Deliberately does not: …

## Beliefs
- [opportunity: {slug}] [value] {referenced, as registered}
- [feature: {slug}] [value] {proposed}
- …

## Discarded or parked
- A3 — discarded: {reason}
- A4 — parked: {reason, and what would bring it back}

## Outcome
{Added by /analyze-solution-tests, per alternative under test: `chosen | discarded | parked` — {tests file}, result and provenance in one line.}
```

Save to `product/solutions/{YYYY-MM-DD-HHMM}-{opportunity-slug}.md`. Three statuses: `chosen` (one alternative goes on to `/design-solution-tests`), `testing-several` (two alternatives, each with the belief that decides between them, tested in `/design-solution-tests`), `back-to-research` (none chosen; the file names the belief of the agenda that needs an answer first). With `testing-several`, one value proposition per alternative under test. The spec comes after the tests: `/write-spec` reads the solutions file and the analyzed tests file. Going straight from `chosen` to `/write-spec` is allowed only when the riskiest belief already carries `real` or `survey` evidence about the solution itself, and the close says which.

## Anti-patterns

- Alternatives that are variations of the favorite — same mechanism, more features
- The favorite evaluated with more affection than the rest: a row of `strong` with thinner citations than its neighbors
- Choosing by aesthetics over utility — the alternative that demos well over the one the evidence favors
- Technical sophistication read as a signal of value — a harder build is not a better answer
- Feasibility judgments invented by the PM — `to check with tech` is the honest cell
- A comparison where everything comes out `strong` — then the filter measured nothing
- Skipping the baseline, or writing "do nothing" in its place
- Turning the exploration into a spec — journeys, stories, and acceptance criteria belong to `/write-spec`, after the tests
- Reading problem evidence as solution evidence — ten interviews about the pain make desirability `strong` only if somebody in them reacted to this solution
- Designing the tests inside the solutions file — a multi-week pilot named here is a late step; the cheapest first step is designed in `/design-solution-tests`
- Registering beliefs of discarded alternatives in the overview
- Demanding real interviews or a survey before exploring — synthetic and secondary evidence work, as long as every judgment says so in its provenance label
