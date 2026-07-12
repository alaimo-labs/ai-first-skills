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

2. **Draft the hypothesis** using the skill's structure: segment, observable behavior, underlying need, behavioral signal with threshold, timeframe, and refutation condition. Push back on opinion-based signals and vanity metrics — propose a behavioral alternative.

3. **Design the experiment:** smallest exposure that tests it, instrumentation (which events/records capture the signal in the prototype), and the advance/iterate/stop decision rule — all agreed before anything is built.

4. **Save** to `product/hypotheses/{slug}.md`.

Close in one line: if the exposure has several layers, suggest `/plan-exposure`; otherwise suggest building the smallest exposure now.
