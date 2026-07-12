# afpm — AI-First Product Manager

Agent skills for discovery and validation with synthetic users. Companion plugin for the [AI-First Product Manager](https://alaimolabs.com/es/courses/ai-first-product-manager) program by Alaimo Labs.

## Overview

This plugin gives your coding agent a product-discovery toolkit: create synthetic personas, interview them, extract insights, run critique panels over your specs, and slice features into exposure plans. All artifacts are plain markdown files in your repo under `product/` — no external services.

Content is written in English; all deliverables come out in the language you work in.

## Install

From the `ai-first-skills` marketplace in Claude Code:

```
/plugin install afpm
```

New here? Run `/afpm-guide-me` — it walks you through the full discovery loop with your own product, one stage at a time. Or read [TUTORIAL.md](TUTORIAL.md) for the same flow on paper.

## Workflows

User-invoked skills — you trigger them as slash commands; they never auto-load.

| Workflow             | What it does                                                  |
| -------------------- | ------------------------------------------------------------- |
| `/afpm-guide-me`     | Guided tour of the discovery loop, resumable at any stage     |
| `/generate-personas` | Generate a diverse set of synthetic personas for your product |
| `/interview-persona` | Interview a persona — exploration or validation mode          |
| `/extract-insights`  | Extract actionable insights from interview transcripts        |
| `/critique-spec`     | Persona panel critiques a spec/PRD, with synthesis            |
| `/slice-feature`     | Turn a spec's hypothesis into an Exposure Plan                |

## Knowledge skills

Model-invoked — the agent loads them automatically when the topic matches.

| Skill                  | Knowledge it carries                                              |
| ---------------------- | ----------------------------------------------------------------- |
| `synthetic-personas`   | Archetype principles, persona structure, diversity requirements   |
| `synthetic-interviews` | In-character interview roleplay; exploration vs. validation modes |
| `insight-extraction`   | Focus areas, grounding rules, insight quality bar                 |
| `persona-critique`     | In-character document reviews and panel synthesis                 |
| `exposure-plans`       | Build ≠ reveal, belief decomposition, level design, validations   |

## File conventions

Artifacts live in your repo:

```
product/
├── overview.md          # product context
├── personas/            # one file per persona
├── interviews/          # transcripts
├── insights/            # extracted insights & critique panels
├── specs/               # feature specs
└── exposure-plans/      # exposure plans
```
