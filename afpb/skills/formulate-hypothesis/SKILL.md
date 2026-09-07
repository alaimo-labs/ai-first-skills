---
name: formulate-hypothesis
description: Turn a product idea or conviction into a falsifiable hypothesis with behavioral success criteria and a decision rule
argument-hint: "<idea, belief, or feature you want to test>"
disable-model-invocation: true
---

# /formulate-hypothesis

Turn a conviction into a testable hypothesis, following the `falsifiable-hypotheses` skill.

Input: $ARGUMENTS

## Workflow

1. **Capture the conviction.** Restate what the user believes in one sentence and confirm it's the belief they most need to test. If several beliefs are tangled together, list them and ask which is load-bearing.

2. **Anchor it in the belief registry.** If `product/overview.md` exists (skip this step silently if it doesn't), find the registered belief the conviction corresponds to and cite it in the hypothesis doc's `Tests:` line. Conviction not registered yet → propose appending it to the overview's unverified beliefs, matching the scope and risk tag format already used in that file, with the user's approval.

3. **Draft the hypothesis** using the skill's structure: segment, observable behavior, underlying need, behavioral signal with threshold, timeframe, and refutation condition. Push back on opinion-based signals and vanity metrics — propose a behavioral alternative.

4. **Design the experiment:** smallest exposure that tests it, instrumentation (which events/records capture the signal in the prototype), and the advance/iterate/stop decision rule — all agreed before anything is built.

5. **Save** to `product/hypotheses/{slug}.md`.

Close in one line: if the exposure has several layers, suggest `/plan-exposure`; otherwise suggest building the smallest exposure now. When the experiment later concludes and the Outcome section lands in the doc, the cited overview belief gets its annotation proposed — see the `falsifiable-hypotheses` skill.
