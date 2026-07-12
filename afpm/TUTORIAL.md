# AFPM Tutorial — the discovery loop, step by step

This walkthrough takes you through the full AFPM loop with **your own product**: by the end you'll have a persona set, interview transcripts, grounded insights, a critiqued spec, and an exposure plan — all as markdown files in your repo, every decision traceable back to a quote.

Prefer to be guided in-session? Run `/afpm-guide-me` in Claude Code — it detects where you are from your `product/` directory and teaches one stage at a time. This document covers the same flow for reading ahead.

Two conventions apply throughout:

- Artifacts default to `product/…`; if your repo already has a place for product docs, that wins.
- Skill content is English, but everything the skills produce comes out in the language you work in.

## The loop

```
overview → personas → interviews → insights → spec → critique → exposure plan
```

Each stage reads the previous stage's artifact. That's the point of the method: nothing is invented at the moment of deciding — the exposure plan traces to the spec, the spec to an insight, the insight to a quote from an interview.

## Stage 0 — Ground: `product/overview.md`

Everything starts with product context, because every skill reads it. Create `product/overview.md` with:

- Product name and a short description
- Who it's for (target users, as specifically as you can)
- What you currently *believe* about your users but haven't verified

That last section is the engine of the whole loop — the interviews exist to test it.

## Stage 1 — Personas: `/generate-personas`

```
/generate-personas
```

Generates a diverse set of synthetic personas (default 3; you can ask for a count or a segment focus, e.g. `3 personas for the B2B segment`). Each is saved to `product/personas/{name-slug}.md`.

Synthetic personas are **archetype hypotheses, not real users** — their value is forcing you to look at your product through eyes that aren't yours. Review the set before accepting: if they all resemble your favorite customer, ask for adjustments.

## Stage 2 — Interview: `/interview-persona`

```
/interview-persona <persona name> exploration
```

This is the heart of the method — and **you are the interviewer**. The persona answers in character; the questions are yours. Start in *exploration* mode (open discovery about the problem space). *Validation* mode exists for later, when you have something specific to test.

Interview **at least two different personas** before moving on — insights that recur across interviews are the credible ones. When you end the interview, accept the offer to save the transcript to `product/interviews/{persona-slug}-{date}.md`.

## Stage 3 — Insights: `/extract-insights`

```
/extract-insights
```

Raw transcripts don't drive decisions; grounded insights do. This extracts 3–5 insights per the quality bar — each tied to quotes, actionable, prioritized — and saves them to `product/insights/`. With no arguments it takes the latest transcript; name several files or a persona to synthesize across interviews.

One caveat the skill will also give you: **synthetic insights are hypotheses to verify with real users**, not evidence to ship on.

## Stage 4 — Spec: your bet, in writing

No command for this one — this stage is yours. Pick the insight you'd bet on and write a short feature spec in `product/specs/{slug}.md`:

- **Problem** — citing the insight and its quotes
- **Proposed feature** — what you'd build
- **Who it's for** — which persona(s) it serves
- **Hypothesis** — explicit and falsifiable; the next stages depend on it:

> We believe *{users}* will *{behavior}* because *{motivation}*.
> We're wrong if *{observable signal}*.

## Stage 5 — Critique: `/critique-spec`

```
/critique-spec product/specs/{slug}.md
```

Before building anything, let the personas attack the spec — cheaper than real users finding the same holes later. Each persona reviews it in character; a synthesis surfaces agreements, design tensions, and the 2–3 highest-impact changes. Saved to `product/insights/critique-{spec-slug}-{date}.md`.

Then **actually revise the spec**. The critique isn't a report to file — it's an edit list. Re-run the panel on the revision if you want a second pass.

## Stage 6 — Slice: `/slice-feature`

```
/slice-feature product/specs/{slug}.md
```

Build ≠ reveal: instead of shipping the whole feature and hoping, expose it in accumulative levels where each level tests one falsifiable belief — so the hypothesis can fail cheaply and early. The result is an Exposure Plan in `product/exposure-plans/{spec-slug}.md`: 1–5 levels, each with a belief, an audience, a duration, and a validation signal.

## Where you've landed

```
product/
├── overview.md                       # your product, your unverified beliefs
├── personas/                         # who you talked to
├── interviews/                       # what they said
├── insights/                         # what it means (+ the critique panel)
├── specs/                            # what you're betting on
└── exposure-plans/                   # how you'll find out, layer by layer
```

The loop is repeatable — next feature, same trail — and every command works standalone from now on. Building the prototype and running the exposure plan is where the **AI-First Product Builder** plugin picks up.
