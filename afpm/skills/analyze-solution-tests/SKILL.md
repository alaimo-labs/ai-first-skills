---
name: analyze-solution-tests
description: Analyze the results of solution tests against the thresholds set before they ran, decide per alternative whether it continues, changes, or is discarded, and update the tests file, the solutions file, and the belief registry with approval. Tests are designed with /design-solution-tests
argument-hint: "<tests file> [results: notes, counts, or capture sheets]"
disable-model-invocation: true
---

# /analyze-solution-tests

Turn the results of solution tests into a decision, following the `solution-testing` skill. The agent compares and proposes; the user decides. **This skill never runs a test, never invents a result, and never writes a spec.**

Input: $ARGUMENTS

## Workflow

1. **Resolve the tests file.** From the arguments, or the latest file in `product/tests/` with `status: designed` or `ready`. If none exists, suggest `/design-solution-tests` in one line. Read every test: belief, signal, threshold, decision rule, expected provenance, material link. Results come in as the filled capture sheets from `product/tests/materials/{test-slug}/` when the test had material, as notes or counts in the arguments, or by asking.

2. **Collect the results per test**, one test at a time: what was observed, with whom, how many, over what period. If the results are conversations or sessions (interviews, usability sessions with transcripts), suggest running `/extract-insights` on the transcripts first and take its file as the result for that test. Never invent or extrapolate a result: a test that did not run is reported as `not run`; a test with partial data is reported with what exists.

3. **Declare provenance per result.** Real people from the segment → `real`. Colleagues, classmates, teammates, acted roles, or synthetic personas → `synthetic`. Use the capture sheet's participant provenance when it exists; otherwise ask. Synthetic results are reported as a rehearsal in the Results section — useful to fix the test, never evidence about the segment — and they never annotate a belief.

4. **Compare against the threshold written before the test.** Per test: `passed`, `failed`, or `inconclusive` (too few people against the design's "with whom", the test did not run as designed, the signal was not captured, the material produced a different signal). The threshold is the one in the file. If the user wants to change it now, point out in one line that it was set before seeing the data; if they insist, apply it and record the change in `product/corrections.md` with the reason (approval required; create the file on first use; same shape `/review-evidence` keeps: a `## {YYYY-MM-DD}` heading with **Artifact**, **AI proposed**, **Human decided**, **Why**).

5. **Propose the decision per alternative**, applying the decision rule written in the test: `continue` (and whether it is ready for spec or goes to its next, bigger step), `change` (say what changes, and that the changed version needs its own test — the result applies to what was tested), or `discard` (with the reason, kept in the file as product memory). An `inconclusive` test proposes rerunning it as designed or redesigning it, not a decision on the alternative. With two alternatives under test, say which one the results favor and whether they can be combined. If the user decides differently from the rule, record it in `corrections.md` (approval required).

6. **Show every change in full, then update only with approval** — never ask to confirm content the user has not seen:
   - **The tests file:** the Results section (per test: observed, with whom and how many, provenance, result, decision) and the Decision section; the **Test status** of every test with a result becomes `analyzed` (a `not run` test keeps `designed` or `ready`, so the next analysis finds it); the file's `status:` becomes `analyzed` once at least one `real` result decided an alternative — a `synthetic`-only run leaves it where it was.
   - **The solutions file:** the outcome per alternative (`chosen`, `discarded`, `parked`) with a link to the tests file, and the `chosen:` field when it changes. Desirability judgments that now have solution evidence are revised with the new file and provenance — a `real` pass may move `mixed (pain evidenced, relief not tested)` to `strong`; a `synthetic` run moves nothing.
   - **`product/overview.md`:** for `real` results only, propose annotating the belief under test on its own line, `— confirmed/contradicted/weakened by [tests file] (date)`. A single small test proposes `weakened` rather than `contradicted` when the sample is small, and promising-in-conversation rather than `confirmed` when the sample is below the design's "with whom". Synthetic results propose nothing. No `product/overview.md` → skip this step silently.

7. **Close with the next step in one line:** the next, bigger test for an alternative that passed but is not ready for spec (name it and suggest `/design-solution-tests` to add it to the file); or, when an alternative is ready, `/write-spec` naming the solutions and tests files — it inherits what was tested, so it does not ask again what the tests settled; or, if every alternative was discarded, back to `/explore-solutions` on the opportunity, or to research, naming the belief that needs an answer (`/design-survey`, `/design-interview`). A `synthetic` run closes by saying what to fix in the test and that the real run is still pending.

## Language

Conversation and file updates in the language of the conversation. Result tokens (`passed`, `failed`, `inconclusive`, `not run`), decision tokens (`continue`, `change`, `discard`), status keywords (`confirmed`, `contradicted`, `weakened`), and provenance labels are fixed English tokens, like `source:` values.
