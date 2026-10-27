---
name: stakeholder-critique
description: How to have a stakeholder of the company that builds the product — CEO, product leadership, engineering, marketing, PR, legal and privacy, sales, customer success, finance, the sponsor — read an internal document (update, brief, results report, spec) in character and react as they would in the meeting. Stakeholder vs. persona, the three basics to get into character, reading only what is on the page, and the per-stakeholder format. Use when preparing a meeting with stakeholders, rehearsing how leadership or legal will read an update, anticipating stakeholder questions, or reviewing an internal document from a decision-maker's perspective.
---

# Stakeholder Critique

A stakeholder critique rehearses the meeting before it happens. Someone inside the company reads the document as they would receive it and reacts as they would in the room: what they would ask, what they are missing to decide, what worries them, and what they would do with the ask. The point is to find what is missing **before** the meeting, not in it.

The skill that runs it is `/stakeholder-review`.

## Language

Reactions and the saved file in the language of the document. The decision tokens (`approve`, `ask-for-more`, `stop`) are fixed English tokens, like `source:` values.

## Stakeholder vs. persona

| | Persona | Stakeholder |
| --- | --- | --- |
| Who | Uses, buys, or decides the purchase of the product | Works in (or for) the company that builds it |
| What they have at stake | Their problem, their money, their time | Budget, risk, reputation, their team's load, a promise to customers |
| Where they live | `product/personas/`, with a `type:` | `product/stakeholders/`, one file per stakeholder |
| Reviews with | `/critique-spec` (see `persona-critique`) | `/stakeholder-review` |

Examples of stakeholders: CEO or leadership, product leadership, engineering, marketing, communication or PR, legal and privacy, sales, customer success, finance. In an internal product, the overview's **sponsor** is a stakeholder.

**A stakeholder skill never reads or uses `product/personas/`.** A `tertiary` persona who approves the purchase is a buyer of the product, not someone in the company that builds it.

## The three basics to get into character

1. **Role:** what they do in the company.
2. **What they have at stake:** the decision they make or what worries them about this work — approve a budget, avoid a legal risk, announce it, protect the team's capacity, keep a promise to a customer.
3. **How much they know about the project:** followed it closely, knows it from a distance, or reads it for the first time.

When a basic is missing, ask for it — one question at a time, each with 3 or 4 example answers built from the role, the overview, and what the document asks for, the recommended one first, plus **Other** to write their own. The user never has to invent the answer from scratch.

## Reads only what is in front of them

The stakeholder reads the document, not the repo. What the document does not say, they do not know — except what the user said they already know (that is what "how much they know" sets). If a test result, a metric, or a decision lives in `product/` but not in the document, the stakeholder misses it and says so.

## Character rules

- Respond in character, in the document's language, without stepping out of the role in the in-character section.
- Read from what they have at stake: a CEO does not review acceptance criteria; Legal does not comment on screen design unless it touches data.
- Demanding but reasonable: ask what they would ask in a real meeting; never play the villain. Enthusiasm is earned by what the document says.
- Never correct the wording and never rewrite the document.

## Format (per stakeholder)

```markdown
### {Role} · {what they have at stake, in one line}

**First reaction:** {1–2 lines, in character}

**Questions I would ask in the meeting:**
- …

**What I'm missing to decide:**
- …

**What worries me or I would object to:**
- …

**What I do with the ask:** approve | ask-for-more | stop · {why, in one line}
```

Headings and labels follow the document's language; only the decision token stays in English.

## Out of character, at the end

Written as whoever prepares the meeting, not in character:

- Per stakeholder, the 2–3 things in the document that would most change their reaction — what to add, clarify, or answer, never a rewritten version.
- With more than one stakeholder, a short synthesis: where they agree, and where they pull in different directions — the tensions the PM has to resolve before the meeting.

## Not evidence

A synthetic stakeholder's reaction is preparation, not evidence: it never annotates a belief in `product/overview.md`.

## Anti-patterns

- Using user personas as stakeholders
- Reading the repo to fill in what the document does not say
- A caricatured stakeholder who rejects everything
- A complacent stakeholder who approves without asking
- Reviewing the wording instead of what they need to decide
- Rewriting the document
