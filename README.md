# AI-First Product Skills

Agent skills for AI-first product work, for coding agents (Claude Code and other Agent Skills-compatible tools). They emerged from the Alaimo Labs AI-First programs but are designed for anyone doing discovery, validation, and evidence-based product building:

- **[afpm](./afpm/README.md)** — AI-First Product Manager: synthetic personas, persona interviews, insight extraction, critique panels, exposure plans. Companion to the [AI-First Product Manager](https://alaimolabs.com/es/courses/ai-first-product-manager) course.
- **[afpb](./afpb/README.md)** — AI-First Product Builder: falsifiable hypotheses, experiment design, exposure plans. Companion to the [AI-First Product Builder](https://alaimolabs.com/es/courses/ai-first-product-builder) course.

Everything is standalone: plain markdown artifacts in your own repo, no external services required. Skill content is in English; deliverables come out in the language you work in.

## Install

### Claude Code

Add the marketplace, then install your course's plugin:

```
/plugin marketplace add https://github.com/alaimo-labs/ai-first-skills
/plugin install afpm   # or afpb
```

### Other clients (portable Agent Plugins format)

Each plugin also ships a root `plugin.json` in the portable [Agent Plugins](https://agent-plugins.org) 1.0.0 format, so any [compatible client](https://agent-plugins.org/compatible-clients) can load it. Where a client asks for a plugin directory, clone the repo first and point it at `afpm/` or `afpb/`:

```bash
git clone https://github.com/alaimo-labs/ai-first-skills.git
```

The steps below are taken from each client's official docs (linked); check them for the current flow.

**Cursor** — [docs](https://cursor.com/docs/plugins). Copy the plugin under `~/.cursor/plugins/local/` — Cursor watches the directory and loads it without a restart:

```bash
cp -R /path/to/ai-first-skills/afpm ~/.cursor/plugins/local/afpm
```

(Cursor's docs also suggest symlinking for development, but as of Cursor 3.8 symlinks pointing outside `plugins/local` are rejected — use a real copy.) Teams can instead import the repo from **Dashboard → Plugins → Add Marketplace → Import from Repo**; installed plugins then appear under **Customize** in the sidebar.

**VS Code** — [docs](https://code.visualstudio.com/docs/agent-customization/agent-plugins). Add the repo as a marketplace in `settings.json`, then install from the Extensions view (search `@agentPlugins`) or via **Chat: Open Customizations → Plugins**:

```json
"chat.plugins.marketplaces": ["alaimo-labs/ai-first-skills"]
```

To load a local checkout instead:

```json
"chat.pluginLocations": { "/path/to/ai-first-skills/afpm": true }
```

**GitHub Copilot CLI** — [docs](https://docs.github.com/en/copilot/concepts/agents/about-plugins). Run `copilot plugin install` (or the `/plugin install` slash command) and point it at a marketplace, repository, or local path — e.g. the cloned `afpm/` directory. For declarative setup, add the plugin to `enabledPlugins` in `~/.copilot/settings.json` (user) or `.github/copilot/settings.json` (repo).

**Kiro** — [docs](https://kiro.dev/docs/powers/installation/). Powers panel → **Add Custom Power** → **Import power from a folder** → select the cloned `afpm/` or `afpb/` directory → **Install**. (Kiro's "Import from GitHub" expects `plugin.json` at the repo root; this repo hosts two plugins, so use the folder import.)

**OpenClaw** — [docs](https://docs.openclaw.ai/plugins/bundles). Install the cloned plugin directory as a bundle, then restart the gateway:

```bash
openclaw plugins install /path/to/ai-first-skills/afpm
openclaw gateway restart
```

Verify with `openclaw plugins list` — the plugin should show `Bundle format: agent (Agent Plugins)`.

**Hermes** — [docs](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins#portable-agent-plugins-v1-packages). Install and enable via the CLI (portable packages install disabled by default):

```bash
hermes plugins install alaimo-labs/ai-first-skills
hermes plugins list
hermes plugins enable afpm   # or afpb
```

Plugin skills load namespaced (`agent-plugin-<slug>-<hash>`) to avoid collisions with built-in skills.

**ChatGPT & Codex** — [docs](https://developers.openai.com/plugins). In Codex CLI, add the repo as a marketplace source (`codex plugin marketplace add <source>`), or set up a personal marketplace: list the plugins in `~/.agents/plugins/marketplace.json` with `source.path` pointing at the cloned `afpm/`/`afpb/` directories. In the ChatGPT desktop app, marketplaces appear as sources in the Plugins Directory.

> **Note:** outside Claude Code, workflow-skill behavior may differ — some clients ignore `disable-model-invocation` (workflow skills may auto-load) or expose skill invocation differently than slash commands.

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

## License

[CC BY-SA 4.0](./LICENSE) © [Alaimo Labs](https://alaimolabs.com). Use, adapt, and share freely — credit Alaimo Labs and keep derivatives under the same license.
