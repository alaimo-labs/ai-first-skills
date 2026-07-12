# AI-First Skills

Agent skills for AI-first product work, for coding agents (Claude Code and other Agent Skills-compatible tools). They emerged from the Alaimo Labs AI-First programs but are designed for anyone doing discovery, validation, and evidence-based product building:

- **[afpm](./afpm/README.md)** — AI-First Product Manager: synthetic personas, persona interviews, insight extraction, critique panels, exposure plans. Companion to the [AI-First Product Manager](https://alaimolabs.com/es/courses/ai-first-product-manager) course.
- **[afpb](./afpb/README.md)** — AI-First Product Builder: falsifiable hypotheses, experiment design, exposure plans. Companion to the [AI-First Product Builder](https://alaimolabs.com/es/courses/ai-first-product-builder) course.

Everything is standalone: plain markdown artifacts in your own repo, no external services required. Skill content is in English; deliverables come out in the language you work in.

## Install

Add the marketplace in Claude Code, then install your course's plugin:

```
/plugin marketplace add <this-repo-url>
/plugin install afpm   # or afpb
```

## How it's organized

Everything is a skill ([Agent Skills](https://agentskills.io) format, portable across Claude Code, Cursor, OpenCode, Codex, and more), in two kinds:

- **Knowledge skills** carry methodology — the agent loads them automatically when the topic matches (e.g. `exposure-plans` when you discuss slicing a feature).
- **Workflow skills** are workflows you trigger yourself as slash commands — `/generate-personas`, `/interview-persona`, `/formulate-hypothesis`, etc. They never auto-load.

See each plugin's README for the full catalog, and [CLAUDE.md](./CLAUDE.md) for maintainer conventions.

## Validate

```bash
python3 ci-validate.py
```

Runs in CI on every push and PR.
