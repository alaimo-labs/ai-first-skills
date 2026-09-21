---
name: opportunity-framing
description: How to frame a product opportunity — a problem for a segment, backed by signals, with no solution chosen yet — and keep it apart from solutions. Opportunity vs. solution vs. outcome, signals vs. proof, the value and viability beliefs of an opportunity, the research agenda, and the Opportunity Solution Tree as a file layout. Use when framing an opportunity, deciding whether something is a problem or a solution, working with an opportunity solution tree, or when an idea arrives as a solution and you need the problem underneath it.
---

# Opportunity Framing

An **opportunity** is a problem, need, or desire of a specific segment, stated from their side, with signals that it exists — and **no solution chosen yet**. It is the middle level of Teresa Torres's Opportunity Solution Tree: an *outcome* the business wants, *opportunities* that would move it if addressed, *solutions* that address one opportunity each, and *experiments* that test a solution. Teams that skip the middle level jump from "we want retention" to "let's build a dashboard" and never learn why nobody used it.

## Language

Write the brief in the language of the conversation. The belief tags, the provenance labels, and the `opportunity:` field values are fixed English tokens, like `source:` values.

## The tree as files

```
product/overview.md          outcome + [product] beliefs
product/opportunities/       one problem for one segment, with signals  → [opportunity: {slug}] beliefs
product/ideas/               candidate solutions, each with a parent opportunity (optional, declared) → [feature: {slug}] beliefs
product/specs/ → product/exposure-plans/
```

`product/overview.md` stays the single belief registry: opportunity beliefs are appended there with the `[opportunity: {slug}]` scope tag, and an idea brief that hangs from an opportunity inherits those beliefs by reference instead of re-registering them.

**The opportunity level is optional; skipping it is a decision, never an omission.** A team may take a decided feature straight to `/clarify-idea`. When it does, the idea brief says so — `opportunity: none (declared)` — and the belief the opportunity would have carried ("the problem X exists for Y") is registered explicitly as a `[feature: {slug}] [value]` belief, so the skipped level leaves a visible trace.

## Personas and the problem

Persona **type** (`primary | secondary | tertiary | negative`, from the `synthetic-personas` skill) and **suffering this problem** are independent dimensions. A `tertiary` persona may not suffer the problem and still be the one who answers the opportunity's viability belief — they pay for it, approve it, or block it. A `primary` persona of the product may have nothing to do with this particular opportunity. So the brief lists every persona with both: its type and whether it suffers the problem, and names the persona that is missing when nobody in the set suffers it.

**The filter at the opportunity level is relation to the problem, never type.** The type never rules a persona out of an opportunity; it only says which belief their evidence can inform (value for `primary`/`secondary`, viability for `tertiary`, scope for `negative`).

## Opportunity vs. solution vs. outcome

| It is…            | Sounds like                                     | Tell                                                   |
| ----------------- | ----------------------------------------------- | ------------------------------------------------------ |
| An **outcome**    | "Increase retention", "cut support cost"        | The business wants it; no user is named. Lives in the overview. |
| An **opportunity**| "Team leads lose the decisions made in meetings" | A segment and a behavior or cost; several solutions could address it. |
| A **solution**    | "A better whiteboard", "automatic meeting notes" | It can be built. Only one of many answers to the problem. |

The tell for a solution in disguise: it can be built. An opportunity can only be understood. When an opportunity arrives as a solution, park the solution as a *candidate idea* and dig underneath: "what would have to be true about these people for a better whiteboard to matter?" One opportunity may later spawn several ideas — whiteboard, live notes, live agenda, quick voting — and that is the point of framing it first.

## Signals vs. proof

A **signal** makes the problem more likely: support tickets, a line in a strategy deck, a competitor shipping something, a number in a brief, a synthetic interview. **Proof** is evidence with named provenance that meets the registry's hierarchy (`real` > `survey` > `secondary` > `synthetic`). Every signal in a brief carries a provenance label:

- `real` — observed behavior or words from real users, with the file.
- `survey` — from a survey analysis, with n.
- `secondary` — market evidence from `product/research/`.
- `synthetic` — from synthetic personas or interviews; a hypothesis, not evidence.
- `unverified` — stated by someone (a stakeholder, a deck, a number without a source). Numbers quoted in a brief are `unverified` until the source is named.

A brief full of `unverified` signals is a fine brief — it just has a longer research agenda.

## The beliefs of an opportunity

Two beliefs carry the risk before any solution exists, both stated so an instrument could prove them wrong:

- `[opportunity: {slug}] [value]` — the segment has this problem badly enough to act (pay, switch, work around it today). "They would like X" is not falsifiable; "they spend N hours a week on the workaround" is.
- `[opportunity: {slug}] [viability]` — solving it moves the outcome the business cares about: revenue, retention, or upgrade for commercial products; the sponsor's metric or a cost avoided for internal ones.

`[usability]` and `[feasibility]` belong to solutions and are usually premature here; register one only if it bounds the whole opportunity ("the data this needs is not captured anywhere").

## The research agenda

The payoff of a brief: for each belief, the cheapest instrument that could resolve it, in order of cost.

1. **Data the product already has** — logs, tickets, revenue by segment. Free; often ignored.
2. **Secondary research** (`/research-market`) — does the market show this problem is real and paid for? Cheap, never conclusive about *your* users.
3. **Survey** (`/design-survey`) — how many, how often, how much. Recruits the interview pool through its opt-in block.
4. **Interviews** (`/design-interview`) — why, and what people do today. Recruited among survey respondents who opted in, preferring those whose answers contradict a belief.

An agenda without a decision attached is a reading list: say what decision each belief unlocks and when the team needs it.

## Brief format

```markdown
---
status: framed | minimal | discarded
segment: {who, specifically}
personas: {slugs from product/personas/, or "none yet"}
---

# Opportunity: {title}

{One sentence: the problem, the segment, why now.}

## Segment and personas
- {persona name} ({type}) — suffers it / does not suffer it
- Missing: {the persona that would suffer it, if none in the set does — or "none"}

## Signals
| Signal | Provenance | Source |
|---|---|---|
| … | real / survey / secondary / synthetic / unverified | {file or who said it} |

## Business outcome
{Commercial: revenue, retention, upgrade. Internal: sponsor metric or cost avoided.}

## Constraints
{Budget, dates, compliance — facts that bound any future solution, not decisions about it.}

## Beliefs
{References to product/overview.md — the single belief registry. No independent list.}
- [opportunity: {slug}] [value] {belief as registered}
- [opportunity: {slug}] [viability] {belief as registered}

## Research agenda
| Belief | Instrument | Decision it unlocks | By when |
|---|---|---|---|

## Candidate ideas (not evaluated)
- {solutions that surfaced while framing — parked, not endorsed}
```

Save to `product/opportunities/{YYYY-MM-DD-HHMM}-{slug}.md`; the slug after the timestamp is the one the `[opportunity: {slug}]` tag uses. Three statuses: `framed` (went through `/frame-opportunity`), `minimal` (created by `/clarify-idea` after the user declared no parent — statement, segment, and the `[feature: {slug}] [value]` belief it references; no signals table, no research agenda; framing it for real still takes `/frame-opportunity`), and `discarded` (saved with the reason — that is product memory too).

## Anti-patterns

- A solution wearing the opportunity's clothes ("users need a dashboard")
- An outcome posing as an opportunity ("increase engagement") — no segment, no behavior
- A segment so broad nobody is excluded ("all users")
- Signals promoted to proof because they came with a number
- Asking the user to imagine the solution while framing the problem
- Framing forever: a research agenda with no decision and no date attached
- Skipping the level silently — the idea brief must say `opportunity: none (declared)`
- Filtering personas by type instead of by relation to the problem — a `tertiary` who does not suffer it can still answer the viability belief
