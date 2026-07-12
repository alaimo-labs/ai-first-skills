---
name: falsifiable-hypotheses
description: How to turn a product conviction into a falsifiable hypothesis with a measurable experiment — structure, quality bar, and behavioral success criteria. Use when formulating a hypothesis, designing an experiment, defining success criteria for a prototype, or when the user states a belief about users that hasn't been tested.
---

# Falsifiable Hypotheses

A conviction is something the team believes ("users want faster reports"). A hypothesis is a claim that evidence could prove wrong. Prototypes built without a falsifiable hypothesis produce demos, not learning.

## Language

Write hypotheses and experiment docs in the language of the conversation.

## Hypothesis structure

```markdown
# Hypothesis: {short name}

**We believe that** {specific user segment, characterized by behavior or role}
**will** {observable behavior}
**because** {the underlying need or pain}.

**We will know this holds if** {behavioral signal + concrete threshold}
**within** {timeframe}.

**We will know this failed if** {behavioral signal that refutes it}.
```

## Quality bar

- **Falsifiable.** Describable evidence could make the team say "this didn't hold". If no imaginable result would change the next decision, it's not a hypothesis — it's a plan wearing a costume.
- **One claim per hypothesis.** "Users will sign up AND invite teammates AND pay" is three hypotheses; test the load-bearing one first.
- **Behavioral signals over opinions.** "Users say they like it" is not a signal; "40% of users who open the report export it within the first session" is. Design the prototype to capture the behavior (events, persisted actions, completion of a real task) — see the course principle: signals beyond opinion-based feedback.
- **Segment characterized by behavior or role**, never "everyone" and never a traffic percentage.
- **Threshold set before the experiment runs.** Deciding what "good" looks like after seeing the data is the most common way teams fool themselves.
- **Time-boxed.** An experiment without an end date never concludes.

## From hypothesis to experiment

For each hypothesis, define before building:

1. **Smallest exposure that tests it** — what's the least product needed to elicit the behavior? (An exposure plan orders these when there are several layers — see the `exposure-plans` skill.)
2. **Instrumentation** — which events/records capture the signal, and where they'll be stored (analytics events, database rows, form submissions).
3. **Decision rule** — advance / iterate / stop, mapped to signal outcomes, written down in advance.

Save to `product/hypotheses/{slug}.md`. When the experiment concludes, append an **Outcome** section: observed signal, decision taken, and what was learned — this becomes the evidence trail for the final presentation.

## Anti-patterns

- Vanity metrics as signals (page views, sign-ups without activation).
- "Validate the prototype" as a goal — prototypes aren't validated, beliefs are.
- Moving the threshold after seeing results.
- Testing a hypothesis whose failure wouldn't change anything you'd do next.
