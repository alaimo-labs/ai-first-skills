# afpb — AI-First Product Builder

Agent skills for closing the product loop: hypothesis → prototype → exposure → evidence. Companion plugin for the [AI-First Product Builder](https://alaimolabs.com/es/courses/ai-first-product-builder) program by Alaimo Labs.

## Overview

This plugin gives your coding agent the experiment-design side of product building: turn convictions into falsifiable hypotheses with behavioral success criteria, and slice what you build into exposure plans that validate beliefs layer by layer. All artifacts are plain markdown files in your repo under `product/` — no external services.

Content is written in English; all deliverables come out in the language you work in.

## Install

From the `ai-first-skills` marketplace in Claude Code:

```
/plugin install afpb
```

## Workflows

User-invoked skills — you trigger them as slash commands; they never auto-load.

| Workflow | What it does |
|----------|--------------|
| `/formulate-hypothesis` | Turn an idea or conviction into a falsifiable hypothesis with an experiment design |
| `/plan-exposure` | Build an Exposure Plan — accumulative reveal levels testing one belief each |

## Knowledge skills

Model-invoked — the agent loads them automatically when the topic matches.

| Skill | Knowledge it carries |
|-------|----------------------|
| `falsifiable-hypotheses` | Hypothesis structure, behavioral signals, thresholds, decision rules |
| `exposure-plans` | Build ≠ reveal, belief decomposition, level design, validations |

## File conventions

Artifacts live in your repo:

```
product/
├── hypotheses/          # hypothesis + experiment docs (with Outcome sections)
├── specs/               # feature specs
└── exposure-plans/      # exposure plans
```
