# afpm — AI-First Product Manager

Agent skills for discovery and validation with synthetic users. Companion plugin for the [AI-First Product Manager](https://alaimolabs.com/es/courses/ai-first-product-manager) program by Alaimo Labs.

## Overview

This plugin gives your coding agent a product-discovery toolkit: create synthetic personas, interview them, extract insights, run critique panels over your specs, and slice features into exposure plans. It also bridges to real research: design interview guides and surveys, analyze the results, and derive evidence-based personas from the patterns. All artifacts are plain markdown files in your repo under `product/` — no external services.

Content is written in English; all deliverables come out in the language you work in.

## Install

From the `ai-first-skills` marketplace in Claude Code:

```
/plugin install afpm
```

New here? Run `/afpm-guide-me` — it walks you through the loop below with your own product, one stage at a time, and picks up wherever you left off.

## The loop

```
overview → personas → interviews → insights → spec → critique → exposure plan
```

Each stage reads the previous stage's artifact — nothing gets invented at the moment of deciding: the exposure plan traces to the spec, the spec to an insight, the insight to a quote from an interview. Every command also works standalone; the loop is just the order that keeps the trail intact.

What the loop produces from synthetic personas is hypothesis, not evidence. `/design-interview`, `/design-survey`, `/analyze-survey` and `/derive-personas` are the bridge to real users.

## Workflows

User-invoked skills — you trigger them as slash commands; they never auto-load.

| Workflow             | What it does                                                  |
| -------------------- | ------------------------------------------------------------- |
| `/afpm-guide-me`     | Guided tour of the discovery loop, resumable at any stage     |
| `/start-product`     | Bootstrap `product/overview.md`: context + unverified beliefs |
| `/research-market`   | Secondary research/benchmarking, every claim provenance-tagged |
| `/generate-personas` | Generate a diverse set of synthetic personas for your product |
| `/interview-persona` | Interview a persona — exploration or validation mode          |
| `/extract-insights`  | Extract actionable insights from transcripts (synthetic/real) |
| `/design-interview`  | Design an interview guide for research with real users        |
| `/test-interview-guide` | Pretest a guide against a persona and fix what breaks      |
| `/design-survey`     | Design a survey questionnaire, ready for any survey tool      |
| `/analyze-survey`    | Analyze survey results: quant summary, themes, insights       |
| `/derive-personas`   | Derive evidence-based personas from real research patterns    |
| `/map-frictions`     | Map cognitive frictions across a journey's steps (MFC)        |
| `/clarify-idea`      | Sharpen a fuzzy idea via one-question-at-a-time brainstorming |
| `/write-spec`        | Draft an evidence-grounded spec: journey, stories, criteria   |
| `/critique-spec`     | Persona panel critiques a spec/PRD, with synthesis            |
| `/slice-feature`     | Turn a spec's hypothesis into an Exposure Plan                |

## Knowledge skills

Model-invoked — the agent loads them automatically when the topic matches.

| Skill                  | Knowledge it carries                                              |
| ---------------------- | ----------------------------------------------------------------- |
| `secondary-research`   | Provenance discipline, source hierarchy, lanes, belief mapping    |
| `synthetic-personas`   | Archetype principles, persona structure, diversity requirements   |
| `synthetic-interviews` | In-character interview roleplay; exploration vs. validation modes |
| `insight-extraction`   | Focus areas, grounding rules, insight quality bar                 |
| `interview-guides`     | Discussion-guide design: goals → questions, funnel, non-leading; pretesting |
| `survey-design`        | Questionnaire craft, wording bias, scales, results analysis       |
| `cognitive-frictions`  | The MFC lens: four friction categories, severity, opportunity bar |
| `feature-specs`        | Spec structure: journey, stories, acceptance criteria, hypothesis |
| `persona-critique`     | In-character document reviews and panel synthesis                 |
| `exposure-plans`       | Build ≠ reveal, belief decomposition, level design, validations   |

## File conventions

Artifacts live in your repo:

```
product/
├── overview.md          # product context
├── personas/            # one file per persona (synthetic or derived)
├── interviews/          # transcripts, synthetic and real
├── interview-guides/    # guides for real-user interviews
├── surveys/             # survey questionnaires
├── insights/            # extracted insights, survey analyses & critique panels
├── research/            # secondary research & benchmarks
├── journeys/            # user journeys + cognitive friction maps
├── ideas/               # clarified idea briefs
├── specs/               # feature specs
└── exposure-plans/      # exposure plans
```
