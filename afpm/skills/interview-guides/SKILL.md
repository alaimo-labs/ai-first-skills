---
name: interview-guides
description: How to design an interview guide (discussion guide) for real user research — from learning goals to open, non-leading questions, funnel structure, and probes. Use when designing an interview, writing interview questions, preparing a discussion guide, or planning research conversations with real users.
---

# Interview Guides

An interview guide turns what you need to learn into a conversation plan for real users. A good guide is a map, not a script: the interviewer follows the participant's energy and uses the guide to make sure nothing essential goes unasked.

## Language

Write the guide in the language of the conversation — and, if different, note the language the interviews themselves will run in.

## From goals to questions

Never start from questions. Work down this chain and keep it explicit in the guide:

1. **Learning goals** — 2–4 things you need to learn or decide. Pull them from real artifacts when they exist: assumptions in an idea brief or spec, synthetic insights awaiting verification, a hypothesis to test.
2. **Beliefs at risk** — for each goal, what do you currently believe, and what answer would prove you wrong?
3. **Questions** — each question exists to serve a goal. A question that maps to no goal gets cut, no matter how interesting.

## Question craft

- **Ask about the past, not the future.** "Tell me about the last time you…" beats "would you use…" — people are terrible predictors of their own behavior and generous liars about hypotheticals.
- **Open and non-leading.** "How do you handle X today?" not "Don't you find X frustrating?". If the question contains the answer you're hoping for, rewrite it.
- **Facts and stories over opinions.** Specific episodes ("walk me through last Tuesday") surface real workflows; opinions surface politeness.
- **Never pitch.** The moment the interviewer sells, the participant starts managing the interviewer's feelings and the data dies.
- **One thing per question.** Split double-barreled questions.

## Structure (the funnel)

```markdown
# Interview guide: {topic}

- **Learning goals:** {2–4, each traceable to an artifact or assumption}
- **Participant profile:** {who qualifies — recruit against a persona/segment}
- **Mode:** exploration | validation
- **Duration:** {target, typically 30–45 min}

## Warm-up (5 min)
Context questions that relax the participant and confirm they fit the profile.

## Main body (per learning goal, ordered general → specific)
For each goal: an opening question, follow-up probes ("what happened next?",
"why was that hard?", "how often?"), and — noted for the interviewer —
what belief this goal tests and what answer would falsify it.

## Stimulus (validation mode only)
When and how to show the idea/prototype — always AFTER the behavioral
questions, so the pitch can't contaminate them. Reaction questions that
ask for objections, not praise.

## Wrap-up (5 min)
"What should I have asked?", referrals to other participants, thanks.
```

## Quality bar

- Every question traces to a learning goal; every goal traces to a decision you'll make with the answer.
- Fits the duration: ~1 main question plus probes per 5 minutes. A 30-minute guide with 20 questions is a survey read aloud.
- The falsification note per goal is written down — interviewers hear what they hope for unless the guide says what "we were wrong" sounds like.
- In validation mode, behavior questions come strictly before the stimulus.

## Pretesting the guide

A guide is a draft until it has been run. Pretesting means running it end to end — against a colleague, a friendly participant, or a synthetic persona — and reading the *answers* for evidence that the *questions* are broken. The failures below are visible in the answers, which is why a dry run finds them and a re-read doesn't:

| Defect | How it shows up in the answers |
| ------ | ------------------------------ |
| **Speculation** | The answer is a prediction ("I'd probably…"), not a memory. The question asked about the future. |
| **Leading** | The answer reuses the question's own words and agrees with its premise. |
| **Double-barreled** | Only half the question gets answered — usually the easier half. |
| **Abstract or jargon wording** | A generic, category-level answer with no episode in it. |
| **Redundant** | The second question harvests the answer already given to the first. |
| **Dead end** | A one-liner with nowhere to go, because no probe was written for it. |
| **Missing probe** | The interesting thing appears in the answer and the guide moves on. |
| **Priming** | An early question plants a frame, and every later answer is shaped by it. |
| **Mistimed sensitivity** | A question about money, failure, or status lands before enough trust exists; the answer turns guarded or performative. |
| **Coverage gap** | A learning goal that no answer touched — or an answer that serves no goal, meaning the question should be cut. |
| **Overrun** | The run doesn't fit the stated duration. Cut questions rather than plan to rush. |

Fix the two or three highest-impact defects and re-run. Revise the guide in place: a pretest doesn't create a new guide, it improves the one you have.

**What a pretest cannot tell you.** It validates structure, not reception. A synthetic persona in particular will be more articulate, more cooperative, and more self-aware than any real participant, so it under-detects confusion, guardedness, and questions that simply fall flat. Treat structural findings as reliable and everything else as a hypothesis about the guide.

## Anti-patterns

- Questions that begin with "would you" / "do you think you'd…" — speculation, not evidence
- A script to recite instead of a map to navigate — probes matter more than the planned questions
- Guides with no participant profile (data from the wrong people is worse than no data)
- Asking for feature opinions ("do you like it?") instead of objections and current behavior
- Skipping the wrap-up referral question — recruiting the next participants is part of the interview
