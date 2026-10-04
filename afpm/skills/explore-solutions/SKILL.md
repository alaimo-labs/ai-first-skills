---
name: explore-solutions
description: Starting from one opportunity (a problem, not an idea), generate 3 to 5 genuinely different solution alternatives, evaluate each against the evidence with the desirable / feasible / viable filter, and help the user choose which one moves forward. Ends with the value proposition of the chosen alternative, never a spec
argument-hint: "<opportunity slug, or the problem in one line>"
disable-model-invocation: true
---

# /explore-solutions

Help the user compare ways of solving one problem before committing to one, following the `solution-exploration` skill. The agent proposes and evaluates; the user chooses. **This skill never writes a spec, never designs the tests, and never picks the winner on its own** — the tests belong to `/design-solution-tests`, the spec to `/write-spec`, the choice to the user.

It is the divergent step of the Opportunity Solution Tree: `/frame-opportunity` parks the solutions that surface as *candidate ideas, not evaluated*; without this step the first idea that shows up — the stakeholder's, or the PM's own — becomes a spec without ever competing. This skill opens the set and compares; **"chosen" means chosen for testing**: the alternatives that come out go to `/design-solution-tests`, and only what survives its tests reaches `/write-spec`.

Input: $ARGUMENTS

## Workflow

1. **Anchor on one opportunity.** Resolve the argument to a file in `product/opportunities/`: a slug matches the part after the timestamp; a one-line problem is matched against the briefs' statements. If several match, ask which. If none exists, say so in one line and offer two paths: run `/frame-opportunity` first (recommended — the exploration will have signals and beliefs to evaluate against), or continue from an insight in `product/insights/` stated as a problem for a segment, with the beliefs marked as pending registration. Never start from a solution: if the argument is one ("a better whiteboard"), treat it as a candidate for the set and ask for the problem underneath before going on. A brief with `status: discarded` is not explored — say why it was discarded and stop.

2. **Load the evidence first.** Read the opportunity brief (signals, beliefs, research agenda, constraints, *Candidate ideas (not evaluated)*), `product/overview.md` (mode, sponsor, the belief registry and the status annotation of each belief), `product/personas/` (type and whether each suffers this problem, per the brief), `product/research/`, `product/insights/` (survey analyses and interview syntheses — real, survey, and synthetic alike, each read with its `source:`), and `product/corrections.md`. Facts that live in these artifacts are looked up, never asked. Summarize in a few lines **what the evidence now says about the problem**: which of the opportunity's beliefs moved and with what evidence, which are still open. If the opportunity's `[value]` belief carries a `contradicted` annotation, say it **before generating anything** and ask whether to continue — exploring solutions to a problem the evidence says does not exist is the most expensive way to be wrong.

3. **Diverge: build the set of alternatives (3 to 5).**
   - Start with the candidate ideas parked in the opportunity brief and any the user brings. Every one of them enters the set — parked ideas exist to compete, not to be forgotten.
   - Propose the rest so the set covers **different mechanisms**, not variations of one idea (see the `solution-exploration` skill for the test). At least one alternative that is **not new software** — a process, a policy, a template, a change in a tool people already use — and one that is **the smallest thing that could work**.
   - Always include the **current workaround** as the baseline to beat, taken from the evidence: what people do today, cited from insights, interviews, or research. It is not counted among the 3 to 5. When no artifact says what people do today, write it as `assumption` and say so — it is the first thing to check.
   - For each alternative, one short paragraph: what it is, which part of the problem it attacks, for which persona (by name and type), and what it replaces.
   - Show the set and ask the user to add, merge, or drop before evaluating. One question at a time, each with a recommended answer. Merge two alternatives when they share a mechanism; drop one only with the reason written down (it goes to *Discarded or parked*).

4. **Converge: evaluate each alternative with the triple filter.**
   - **Desirable (value):** does it relieve the pain the evidence shows, for the persona that suffers it, better than the workaround? Separate **problem evidence** from **solution evidence**: interviews and surveys about the pain prove the problem, not that this solution relieves it. When the only evidence cited is about the problem, the cell reads `mixed` at most and says why — `pain evidenced, relief not tested`. It rises to `strong` only with evidence of someone reacting to this solution or to one very like it (used it, saw it and did something, committed to something), per the `solution-testing` skill.
   - **Feasible:** can it be built or put in place within the constraints the opportunity brief records? The PM does not own this judgment: without evidence, mark it `to check with tech` instead of guessing. Evidence here is a fact from the overview's what-we-know section, a constraint in the brief, or something tech already said.
   - **Viable:** does it move the business outcome the brief names — commercial: revenue, retention, upgrade; internal: the sponsor's metric or a cost avoided?
   - Each judgment is one of `strong | mixed | weak | unknown` and cites the file and provenance behind it (`real`, `survey`, `secondary`, `synthetic`, `unverified`) or is marked `assumption`. `unknown` is a valid, honest answer; a column where everything reads `strong` is a sign the favorite was evaluated with more affection than the rest — say so and re-check.
   - Name, per alternative, its **riskiest belief**: the one that, if false, kills it — stated so an instrument could prove it wrong.
   - Usability is not judged here: there is nothing to try yet. When the riskiest belief of an alternative is about usability, it is tested with a prototype in `/design-solution-tests`, before the spec. Mention it only when an alternative depends on a behavior the evidence says these users will not adopt.
   - Present the comparison table (alternatives in rows; desirable, feasible, viable, riskiest belief in columns), then **a recommendation with its reasons** — which alternative, why, and what would change the recommendation.

5. **The user chooses — for testing.** Three options, each valid: one alternative; two to test in parallel (one line per alternative: which belief has to be tested and why — the test itself is designed in `/design-solution-tests`, not here); or none — back to research, naming which belief of the agenda needs an answer first. If the user's choice differs from the recommendation, record the disagreement and its reason as an entry in `product/corrections.md` (with the user's approval; create the file on first use), in the same shape `/review-evidence` keeps — a `## {YYYY-MM-DD}` heading and one item with **Artifact** (this solutions file), **AI proposed** (the recommendation and its reasons), **Human decided** (the choice), **Why** (the user's reason) — that is how the next exploration learns what the AI weighs wrong.

6. **Value proposition of the chosen alternative**, without canvas ceremony, written against the persona that suffers the problem:
   - Pain it relieves (cited from evidence) and gain it creates.
   - What it replaces (the workaround) and why the user would switch.
   - What it deliberately does not do.
   - The beliefs it carries, stated falsifiably, proposed as `[feature: {slug}] [value|viability|usability|feasibility]` for the registry — slug = the chosen alternative's slug, which `/clarify-idea` and `/write-spec` reuse. The opportunity's own beliefs are referenced by their registered line, never duplicated. Write nothing to `product/overview.md` without the user's approval; beliefs of discarded alternatives are never registered. No `product/overview.md` yet → suggest `/start-product` in one line and keep the beliefs in the file, marked as pending registration.

   With two alternatives chosen for parallel testing, write one value proposition per alternative and register only the beliefs the tests will resolve.

7. **Show the full file in the conversation, then save** to `product/solutions/{YYYY-MM-DD-HHMM}-{opportunity-slug}.md` (timestamp = creation date; format in the `solution-exploration` skill) once the user agrees. Then offer, with approval, to annotate the opportunity brief: each entry under *Candidate ideas (not evaluated)* gets a link to this file and its outcome — `chosen`, `discarded`, or `parked`. Discarded alternatives stay in the file with their reason: that is product memory, and the next person who brings the same idea finds why it lost.

8. **Close with the next step in one line:** `/design-solution-tests` naming this file — with `chosen` or `testing-several` alike, the next step is to test the riskiest belief of each alternative under test before anything is specified. One exception: when the riskiest belief of the chosen alternative already carries `real` or `survey` evidence **about the solution** (someone reacted to it, not only to the problem), the close may go straight to `/write-spec`, saying which evidence allows it. If the value belief rests only on `synthetic` or `unverified` evidence, `/interview-persona` in validation mode is a cheap rehearsal of the test, never the test. With `back-to-research`, name the instrument instead (`/design-survey`, `/design-interview`, or `/research-market`, per the agenda).

## Language

Conversation and the saved file in the language of the conversation. Filter ratings (`strong | mixed | weak | unknown`, `to check with tech`, `assumption`, the note `pain evidenced, relief not tested`), provenance labels, `status:` values, and belief tags are fixed English tokens in every language, like `source:` values.
