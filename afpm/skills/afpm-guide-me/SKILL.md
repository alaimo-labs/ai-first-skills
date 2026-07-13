---
name: afpm-guide-me
description: Guided step-by-step tour of the AFPM discovery loop with your own product — run it right after installing, and any time you wonder what's next; infers where you are from product/ and teaches the next step
argument-hint: "[status | stage name or number, e.g. 'status' or 'spec']"
disable-model-invocation: true
---

# /afpm-guide-me

Walk the user through the full AFPM discovery loop — with their own product, one stage per invocation. The guide produces no artifacts of its own beyond stage 0: every step's output is a standard `product/` artifact created by the user running the real commands.

Input: $ARGUMENTS

## The loop being taught

| # | Stage     | Command the user runs                    | Artifact                              |
| - | --------- | ---------------------------------------- | ------------------------------------- |
| 0 | Ground    | (this tutorial guides it)                | `product/overview.md`                 |
| 1 | Personas  | `/generate-personas`                     | `product/personas/*.md`               |
| 2 | Interview | `/interview-persona <name> exploration`  | `product/interviews/*.md`             |
| 3 | Insights  | `/extract-insights`                      | `product/insights/*.md`               |
| 4 | Spec      | `/write-spec`                            | `product/specs/*-{slug}.md`           |
| 5 | Critique  | `/critique-spec <spec>`                  | `product/insights/*-critique-*.md`    |
| 6 | Slice     | `/slice-feature <spec>`                  | `product/exposure-plans/*-{spec-slug}.md` |

Artifacts default to `product/…`; if this repo already has a place for product docs, that wins — detect and use it consistently.

## Workflow

1. **Parse the arguments.** `status` → show the stage map with what exists and what's next, then stop. A stage name or number → jump to that stage. Empty → infer the stage (step 2).

2. **Infer the current stage** from what exists (in the artifact locations detected above):
   - no `product/overview.md` (or equivalent product context) → stage 0
   - overview but no personas → stage 1
   - personas but no interview transcripts → stage 2
   - transcripts but no insight files (ignore `*-critique-*` files) → stage 3
   - insights but no specs → stage 4
   - a spec but no `*-critique-{spec-slug}*` for it → stage 5
   - critique but no `exposure-plans/*-{spec-slug}.md` → stage 6
   - exposure plan exists → wrap-up

3. **Acknowledge progress.** One or two lines: what the user has already built and where they are in the loop. On the first run, also frame the big picture in a short paragraph: AFPM is an evidence loop — every stage reads the previous stage's artifact, so every product decision stays traceable to a quote from an interview.

4. **Teach the current stage** (guidance per stage below): why it matters in one short paragraph, then exactly what to do.

5. **Stop.** For stages with a command, hand the user the exact command to run and end the turn — never run another workflow skill on their behalf; running the command themselves is how they learn it. Tell them to come back with `/afpm-guide-me` when the stage's artifact exists.

## Stage guidance

- **Stage 0 — Ground.** The goal is `product/overview.md`: product name, what it is, who it's for, and — the question that pays off later — what the user currently believes about their users but hasn't verified. Two paths to it:
  - **The repo already has product context** (README, specs, docs): read it, but treat it as hypothesis, not fact. Present what was inferred point by point, naming the source file for each ("from `docs/specs/README.md` I gather that…"), and ask the user to confirm or correct it before any of it goes into the overview. Documents can be stale, aspirational, or describe a direction that has already changed — only the user knows which. Then ask only for what the docs can't contain (the unverified beliefs above all).
  - **No context anywhere:** interview the user briefly (a few questions, not a form).

  Either way: draft the overview, show it, confirm, save. This is the context every other skill reads.

- **Stage 1 — Personas.** Explain in two sentences: synthetic personas are archetype hypotheses, not real users — their value is forcing you to look at your product through eyes that aren't yours. Hand them `/generate-personas` (default 3 is fine; they can name a segment focus). Suggest they check the set for diversity before accepting.

- **Stage 2 — Interview.** The heart of the tutorial: the user is the interviewer, not a spectator — the persona answers, but the questions are theirs. Recommend exploration mode first (open discovery about the problem space); mention validation mode in one line as "for when you have something specific to test." Hand them `/interview-persona <persona name> exploration`. Recommend interviewing at least two different personas before moving on — insights that recur across interviews are the credible ones. Remind them to save the transcript when the interview wraps up.

- **Stage 3 — Insights.** Explain: raw transcripts don't drive decisions, grounded insights do — each one tied to quotes, actionable, prioritized. Hand them `/extract-insights` (with no arguments it takes the latest transcript; naming several files or a persona pulls in more). Note the caveat the skill itself will raise: synthetic insights are hypotheses to verify with real users.

- **Stage 4 — Spec.** Explain in two sentences: this is where discovery turns into a bet — the spec picks one insight and commits to a feature, a user journey, critical stories with acceptance criteria, and a falsifiable hypothesis, all still traceable to interview quotes. Hand them `/write-spec` (it proposes the highest-impact insight to bet on; they can also name one). Tell them the hypothesis is the part to sweat — `/slice-feature` will decompose it later.

- **Stage 5 — Critique.** Explain: before building anything, let the personas attack the spec — cheaper than real users finding the same holes later. Hand them `/critique-spec <spec file>`. When the panel is done, have them actually revise the spec from the 2–3 highest-impact changes (offer to re-run the critique on the revision if they want a second pass).

- **Stage 6 — Slice.** Explain build ≠ reveal in two sentences: instead of shipping the whole feature and hoping, expose it in accumulative levels where each level tests one belief — so the hypothesis can fail cheaply and early. Hand them `/slice-feature <spec file>`.

- **Wrap-up.** Recap the trail they built: overview → personas → interviews → insights → spec → critique → exposure plan — every decision traceable back to evidence. Then:
  - Offer (optional, their call) to add a short section to the repo's `CLAUDE.md` noting that product discovery artifacts live under `product/` with `product/overview.md` as the product context, so future sessions respect the layout.
  - Point out the loop is repeatable — next feature, same trail — and that individual commands work standalone from now on.
  - Mention in one line that building the prototype and running the exposure plan is where the AI-First Product Builder plugin (`afpb`) picks up.

## Rules

- Never invoke another workflow skill; only name the command and let the user run it.
- Anything inferred from repo files is an assumption until the user confirms it — present it with its source and ask for confirmation/correction before writing it into an artifact.
- One stage per invocation — resist teaching ahead. Depth lives in the knowledge skills, which load themselves when the real commands run; the tutorial teaches the loop, not the disciplines.
- All conversation and stage 0/4 artifacts in the language of the conversation.
