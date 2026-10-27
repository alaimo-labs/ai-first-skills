---
name: stakeholder-review
description: Have a stakeholder of the company that builds the product (CEO, legal, marketing, engineering, sales, the sponsor) read an update, brief, or results report in character and say what they would ask in the meeting, what they miss to decide, what worries them, and whether they would approve, ask for more, or stop. Asks a few basics first to get into character
argument-hint: "<document file or pasted text> [stakeholder role(s)]"
disable-model-invocation: true
---

# /stakeholder-review

Rehearse the meeting before it happens, following the `stakeholder-critique` skill. A stakeholder reads the document as they would receive it and reacts in character. **This skill never rewrites the document, never uses user personas as stakeholders, and never annotates a belief** — a synthetic stakeholder's reaction is preparation, not evidence.

Input: $ARGUMENTS

## Workflow

1. **Resolve the document.** A file path (an update, a brief, a results report, a spec), or pasted text. If nothing resolvable, ask.

2. **Get into character.** One stakeholder by default; up to three if the user names more. If a matching file exists in `product/stakeholders/`, use it and ask only what is missing. Otherwise get the three basics from `stakeholder-critique` — role, what they have at stake, how much they know about the project — one question at a time. Each question offers 3 or 4 example answers to pick from, the recommended one first, plus **Other** to type a custom answer; use the multiple-choice question tool when the client has one (it adds Other), otherwise a numbered list ending in "Other: write your own". Build the example answers from the role the user named, from what the document asks for, and — when `product/overview.md` says the product is `internal` — from its Sponsor section, whose stake is the recommended answer for the sponsor (e.g. for a CEO's stake: approve the budget for the next level · decide whether to announce it · weigh it against other priorities · Other). Never take a stakeholder from `product/personas/`.

3. **Read in character.** Each stakeholder reads only the document, plus what the user said they already know. The overview and stakeholder files only set up the character; anything else in the repo stays out. If the document does not say it, the stakeholder does not know it — and when it matters to their decision, they name it under what they are missing.

4. **React** in the per-stakeholder format of `stakeholder-critique`: first reaction, questions they would ask, what they miss to decide, what worries them, and what they do with the ask (`approve`, `ask-for-more`, or `stop`, with the reason). Demanding but reasonable — neither villain nor ally.

5. **Step out of character** and name, per stakeholder, the 2 or 3 things in the document that would most change their reaction — what to add, clarify, or answer, never a rewritten version. With more than one stakeholder, add a short synthesis: where they agree, and at least one tension where they pull in different directions.

6. **Save, with approval,** to `product/insights/{YYYY-MM-DD-HHMM}-stakeholder-review-{document-slug}.md`, with a header naming the document reviewed and the stakeholders (role, stake, how much they know). Offer to save each new stakeholder to `product/stakeholders/{role-slug}.md` (role, what they have at stake, how much they know; no date prefix, a living file updated in place) so the next review starts from it.

7. **Close in one line:** revise the document (the user does it, by hand or with their own skill) and run `/stakeholder-review` again with the same stakeholder to see whether the reaction changes.

## Language

Conversation, the in-character reactions, and the saved file in the language of the document. Decision tokens (`approve`, `ask-for-more`, `stop`) are fixed English tokens.
