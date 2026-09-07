---
name: start-product
description: Start product discovery — place the product on two axes (new/existing, commercial/internal) and capture its context plus a tagged, ranked list of unverified beliefs into product/overview.md, the context every other skill reads
argument-hint: "[product name or one-line idea; empty to be interviewed]"
disable-model-invocation: true
---

# /start-product

Create `product/overview.md` — the product context every other skill reads. The deliverable is small; the value is in the last section: the user's unverified beliefs, tagged and ranked, which the rest of the loop exists to test.

Input: $ARGUMENTS

## Workflow

1. **Check what already exists.**
   - `product/overview.md` already there → offer to review and update it instead of overwriting; never silently replace it.
   - The repo has product context (README, docs, specs): read it, but treat it as hypothesis, not fact. Present what was inferred point by point, naming the source file for each ("from `README.md` I gather that…"), and ask the user to confirm or correct before any of it goes into the overview — documents can be stale or aspirational; only the user knows which.
   - Nothing anywhere: start from the arguments (or ask for the idea in one line) and interview the user briefly — a few questions, one at a time, not a form.

2. **Place the product on two axes.** Before any probing, establish the mode — ask whatever the arguments or repo evidence don't already answer (confirm inferences instead of re-asking):
   - **New or existing?** New = not in anyone's hands yet — an idea or a prototype without users. Existing = live, with users, and the question is what comes next.
   - **Commercial or internal?** Commercial = external customers pay for it (or will). Internal = built for the organization's own people; nobody pays directly — someone sponsors.

   The axes decide which probes apply below, how the overview is structured, and the closing step.

3. **Ask only for what documents can't contain.** Facts found in the repo are confirmed, not re-asked. What always needs the user: who the product is for (as specifically as they can say — "PMs" is a segment, "PMs at 10-person startups who do research themselves" is a target) and the beliefs the probes below draw out.

4. **Probe value risk** — would anyone want this? — by the first axis, adding the internal probes when the product is internal:
   - **New:** does the problem actually exist — who has it badly enough to act? would they change from what they do today?
   - **Existing:** why do current users actually use it (not why it was built)? which segment gets the most value from it? why do the ones who leave, leave? what do we believe about the next bet?
   - **Internal (on top of the above):** would people abandon their current workaround for it? would anyone use it voluntarily, if nobody mandated it?

5. **Probe viability risk** — can this sustain itself? — by the second axis:
   - **Commercial:** would they pay? how much — and what would make it worth that price?
   - **Internal:** who funds this? what do they need to see to keep funding it? Capture the sponsor (name or role) in the overview — an internal product without a nameable sponsor is already at risk.

6. **In existing mode, separate what's known from what's believed.** "What we know" holds facts backed by evidence — usage data, revenue, support tickets, past research — each fact naming its evidence on the same line. "Unverified beliefs" holds the frontier: what the team assumes but has never checked. When the user states something as fact, ask what the evidence is; no evidence → it's a belief.

7. **Tag, rank, and cap the beliefs.** Push for 3–5 beliefs (hard cap 5 — more dilutes focus), each concrete enough that an interview or survey could prove it wrong. If the user blanks, the probes above are the prompts. A belief everyone would agree with isn't a belief, it's a platitude — sharpen it until it's falsifiable. Each belief line opens with two tags, fixed English tokens in every language (like `source:` values):
   - **Scope:** `[product]` — every belief this skill writes is product-wide. (Feature-level skills later append `[feature: {slug}]` beliefs to the same list; the tag exists so product bets and feature bets never blur.)
   - **Risk:** `[value]` (do they want it?) or `[viability]` (does it sustain itself — revenue or sponsorship?). The registry's risk vocabulary has four tokens — `[value]`, `[usability]`, `[feasibility]`, `[viability]` — but this skill emits only the two it probes; feature-level skills use the full set.

   Rank by impact × uncertainty: the belief that would change the product most if proven wrong, and has the least evidence behind it, goes first. Name belief #1 as the first to attack — in conversation and in the overview.

8. **Draft, show, confirm, save** to `product/overview.md` (no timestamp prefix — the overview is the one living artifact, edited in place):

   ```markdown
   # {Product name}

   mode: {new | existing} · {commercial | internal}

   {What it is, in 2–4 sentences.}

   ## Para quién / Who it's for

   {Target users, specifically.}

   ## Sponsor                          <- internal products only

   {Who funds it, and what they need to see to keep funding it.}

   ## Lo que sabemos / What we know    <- existing products only

   - {Fact — evidence named: metric, file, study}

   ## Creencias no verificadas / Unverified beliefs

   {Ranked by impact × uncertainty — the first is the next to attack.}

   1. [product] [value] {Belief — falsifiable}
   2. [product] [viability] {Belief}
   - …
   ```

9. **Close with the next step in one line, by mode:**
   - **New** → `/generate-personas`. If the beliefs raise market questions (does this already exist? what does it cost?), mention `/research-market` as an optional detour before the personas.
   - **Existing, with a concrete feature or bet in mind** → `/clarify-idea` to turn it into a brief.
   - **Existing, no specific bet yet** → attack belief #1: `/derive-personas` if the repo holds real evidence; otherwise `/design-interview` — the users exist and are reachable, so go talk to them about belief #1. Mention `/generate-personas` only as an optional rehearsal if the PM wants to practice the interview before facing real users.

## Language

Conversation and the saved overview in the language of the conversation (section headings included). The `mode:` values and the belief tags (`[product]`, `[feature: {slug}]`, `[value]`, `[usability]`, `[feasibility]`, `[viability]`) are fixed English tokens in every language, like `source:` values.
