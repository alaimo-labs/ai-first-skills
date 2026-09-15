# CLAUDE.md

Guidance for AI agents working in this repository. Single source of truth for structure and conventions.

## Project Overview

**ai-first-skills** — a marketplace of two Claude Code plugins for AI-first product work. They emerged from the Alaimo Labs programs, but are designed to work for any user in any context — course usage is incidental:

| Plugin | Course                                                                                 | Focus                                                                                                          |
| ------ | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `afpm` | [AI-First Product Manager](https://alaimolabs.com/es/courses/ai-first-product-manager) | Discovery and validation with synthetic users: personas, interviews, insights, critique panels, exposure plans |
| `afpb` | [AI-First Product Builder](https://alaimolabs.com/es/courses/ai-first-product-builder) | Hypothesis → prototype → exposure → evidence loop with coding agents                                           |

Owner: Alaimo Labs — info@alaimolabs.com — https://alaimolabs.com

## Repo Structure

```
ai-first-skills/
├── .claude-plugin/marketplace.json   <- root manifest listing both plugins
├── afpm/                             <- AI-First Product Manager plugin
│   ├── .claude-plugin/plugin.json    <- Claude Code manifest
│   ├── plugin.json                   <- portable Agent Plugins manifest (agent-plugins.org)
│   ├── skills/{skill}/SKILL.md       <- one folder per skill (+ optional reference .md files)
│   │                                    knowledge skills are model-invoked; workflow skills
│   │                                    carry disable-model-invocation: true (user-invoked)
│   └── README.md
├── afpb/                             <- AI-First Product Builder plugin (same layout)
├── ci-validate.py                    <- structural validator (run: python3 ci-validate.py)
├── .github/workflows/tests.yml       <- CI: validator on every PR/push
├── .github/workflows/release.yml     <- CI: on a vX.Y.Z tag, validates tag == version and publishes a GitHub release with the CHANGELOG section
├── CHANGELOG.md
├── CLAUDE.md                         <- this file
└── AGENTS.md                         <- pointer to this file for non-Claude agents
```

## Key Design Rules

- **Everything is a skill.** There is no `commands/` directory. Skills split into two kinds by who invokes them (Agent Skills is an open standard, so both kinds travel to other clients — Cursor, OpenCode, Codex — unlike Claude Code commands):
  - **Knowledge skills = nouns/concepts (model-invoked).** Methodology and formats Claude auto-loads when the topic matches (`synthetic-personas`, `exposure-plans`). They embed reusable disciplines. Descriptions must include trigger phrases ("Use when…"). No placeholders.
  - **Workflow skills = verbs (user-invoked).** User-triggered orchestration, run as slash commands (`/generate-personas`, `/interview-persona`). Frontmatter carries `disable-model-invocation: true` (never auto-loads; description stays out of context in Claude Code — other clients may ignore the flag) plus `argument-hint`; the body uses a single `$ARGUMENTS` placeholder.
- **Workflow skills may apply knowledge skills in the same plugin, never another workflow skill.** Orchestration composes disciplines; it doesn't chain other orchestrations.
- **English files, user-language output.** All skill content is written in English, but every skill instructs the agent to produce deliverables in the language of the conversation. Never hardcode Spanish content in files; never let output drift to English when the user writes in Spanish or any other language.
- **No cross-plugin references.** The two plugins install independently. `exposure-plans` exists in BOTH plugins by design — keep the two copies in sync manually when editing either. Suggest cross-plugin follow-ups in natural language only.
- **Intra-plugin references are fine** — a workflow skill may name a knowledge skill in the same plugin.
- **Standalone, product-agnostic.** Skills must work in any repo with only markdown files — no external tools or APIs. Artifacts live in the user's repo under `product/` (see File Conventions).
- **Audience-agnostic.** Skill content addresses anyone doing product work; the courses appear only in READMEs, as provenance. In interview-related skills, call the human "the interviewer" — "the user" collides with the product's users being researched.
- **Frontmatter:** every skill needs `name` (must match directory name) + `description`; workflow skills additionally need `disable-model-invocation: true` + `argument-hint`. Keep frontmatter lean (always loaded); detail goes in the body (loaded when triggered).
- **Dual manifests.** Each plugin carries two manifests: `.claude-plugin/plugin.json` (Claude Code) and a root `plugin.json` (portable [Agent Plugins](https://agent-plugins.org) 1.0.0 format, for clients like Cursor, VS Code, Copilot, Codex, Kiro). Shared fields (`name`, `version`, `description`, `author`, `homepage`, `license`, `keywords`) must stay identical in both — `ci-validate.py` enforces this. The portable manifest uses a closed schema: Claude-Code-only fields (`displayName`) stay out of it; the marketplace remains Claude Code's distribution channel and is not part of the portable format.

## File Conventions (user repos)

Skills read and write product artifacts in the user's working repo:

```
product/
├── overview.md          <- product context (name, description, mode, target users, sponsor if internal, known facts if existing, tagged + ranked unverified beliefs)
├── corrections.md       <- log of human corrections to AI proposals (living file; /review-evidence appends dated entries: artifact, what the AI proposed, what the human decided, why)
├── personas/{slug}.md   <- one file per persona
├── interviews/          <- interview transcripts, synthetic and real ({YYYY-MM-DD-HHMM}-{persona-or-interviewee-slug}.md)
├── interview-guides/    <- guides for real-user interviews ({YYYY-MM-DD-HHMM}-{slug}.md)
├── surveys/             <- survey questionnaires ({YYYY-MM-DD-HHMM}-{slug}.md; results analyses go to insights/)
├── insights/            <- extracted insights ({YYYY-MM-DD-HHMM}-{slug}.md; critiques: {YYYY-MM-DD-HHMM}-critique-{spec-slug}.md)
├── research/            <- secondary research / benchmarks ({YYYY-MM-DD-HHMM}-{slug}.md; source: secondary — market evidence, kept apart from user evidence in insights/)
├── journeys/            <- user journeys + cognitive friction maps ({YYYY-MM-DD-HHMM}-{slug}.md)
├── opportunities/       <- opportunity briefs: a problem for a segment, with signals, no solution chosen ({YYYY-MM-DD-HHMM}-{slug}.md; status: framed | minimal | discarded; research agenda; written by /frame-opportunity, minimal ones by /clarify-idea)
├── ideas/               <- clarified idea briefs ({YYYY-MM-DD-HHMM}-{slug}.md; carry `opportunity: {slug} | none (declared)`)
├── specs/               <- feature specs ({YYYY-MM-DD-HHMM}-{slug}.md)
├── hypotheses/          <- hypothesis + experiment docs ({slug}.md, no timestamp prefix; Outcome section appended when the experiment concludes — written by afpb)
└── exposure-plans/      <- exposure plans ({YYYY-MM-DD-HHMM}-{spec-slug}.md)
```

Every artifact except `overview.md`, `corrections.md`, personas, and hypotheses carries a `{YYYY-MM-DD-HHMM}-` prefix so listings sort chronologically. The timestamp is the creation date: revisions (e.g. a spec after a critique panel) edit the file in place without renaming.

**Overview fields.** `overview.md` opens with a `mode:` line — `{new | existing} · {commercial | internal}`, fixed English tokens like `source:` values. Internal products add a Sponsor section: who funds the product and what they need to see to keep funding it. Existing products add a what-we-know section — facts with their evidence named on the same line — kept apart from the unverified beliefs. `/start-product` builds all of this.

**Belief tags.** Every unverified belief in `overview.md` opens with two tags, fixed English tokens in any language (like `source:` values): scope — one of three: `[product]` (product-wide, written by `/start-product`), `[opportunity: {slug}]` (tied to a framed problem; written by `/frame-opportunity`), or `[feature: {slug}]` (tied to one bet; `/clarify-idea` and `/write-spec` append these to the same list — `overview.md` is the single belief registry, no opportunity brief, idea brief, spec, or hypothesis keeps its own assumptions list) — and risk — one of four: `[value]` (do they want it?), `[usability]` (can they figure it out?), `[feasibility]` (can we build it?), `[viability]` (revenue or sponsorship). `/start-product` and `/frame-opportunity` emit only `[value]`/`[viability]` (an opportunity has no solution to be usable or feasible yet); feature-level skills use all four. The default owner derives from the risk (value/viability → PM, usability → UX, feasibility → Tech) and is written down only when the real owner differs — documented in `feature-specs`. The belief text follows the file's language. The list is ranked by impact × uncertainty.

**The opportunity level (Opportunity Solution Tree).** The tree maps onto the files: `overview.md` holds the outcome and `[product]` beliefs; `opportunities/` holds problems for a segment with signals and a research agenda (`[opportunity: {slug}]` beliefs); `ideas/` holds candidate solutions, each naming its parent opportunity (`[feature: {slug}]` beliefs); then `specs/` → `exposure-plans/`. One opportunity may spawn several ideas, and an idea inherits its parent's beliefs by reference instead of re-registering them. **The opportunity is optional, but skipping it is declared, never forgotten:** `/clarify-idea` asks first which opportunity the idea answers — an existing one, `none (declared)` (recorded in the brief's `opportunity:` field, with the implicit problem registered as a `[feature: {slug}] [value]` belief), or "frame it first" (hands off to `/frame-opportunity`). Signals in an opportunity brief carry a provenance label (`real` / `survey` / `secondary` / `synthetic` / `unverified`); a signal is not proof — documented in `opportunity-framing`.

**Belief status.** An unverified belief in `overview.md` may carry an annotation appended on the belief's own line: `— confirmed/contradicted/weakened by [file] (date)`. The three status keywords are fixed English tokens (like `source:` values); the surrounding text follows the file's language, and a belief with no status is still unverified. Provenance hierarchy: `source: real` > `survey` > `secondary` > `synthetic` — only real/survey evidence confirms; synthetic evidence never does (supporting synthetic evidence makes a belief promising, with no annotation). Beliefs are annotated, never deleted, and only with the user's approval — `/review-evidence`, `/extract-insights`, and `/analyze-survey` propose these annotations; in afpb, a hypothesis doc cites the belief it tests and proposes the annotation when its experiment's Outcome lands (observed behavior from real exposure counts as real evidence).

Artifacts that can come from synthetic or real sources declare it in their header: interview transcripts and insights carry `source: synthetic | real | survey`; personas carry `source: derived` when built bottom-up from real evidence (`/derive-personas`) — synthetic and derived personas share `product/personas/`.

Workflow skills create these directories on first use. If the repo has an existing layout, skills adapt to it rather than forcing this one.

## Local Development & Testing

Never cut a release just to test a change. Two speeds:

- **Develop:** load the working copy directly in any test repo — no install, no cache, no version bump:

  ```bash
  cd ~/some-test-repo
  claude --plugin-dir /path/to/ai-first-skills/afpm   # repeat the flag for afpb
  ```

  Edit skills → start a new session with `--plugin-dir` → test. Disable the
  marketplace-installed copy in that repo first (`/plugin` → disable) so only
  one version of the plugin is loaded.

- **Release:** only when a change should reach users (see Versioning & Releases).
  Marketplace installs are cached copies pinned to the explicit `version` in
  `plugin.json` — pushing commits without a version bump changes nothing for
  installed users; that's intentional.

## Versioning & Releases

- `CHANGELOG.md` is the source of truth. Newest `## vX.Y.Z — YYYY-MM-DD` heading = released version.
- `marketplace.json` and all four plugin manifests (two per plugin: `.claude-plugin/plugin.json` + root `plugin.json`) carry the same version. No per-plugin versioning.
- Semver: breaking = major; new skills = minor; fixes/docs = patch.
- Run `python3 ci-validate.py` before committing structural changes. It also checks that the newest `CHANGELOG.md` heading matches the manifests.
- **GitHub releases are tag-driven.** Distribution needs only the manifest bump (marketplace installs are pinned to it); the release is provenance. After the version-bump commit lands on `main`:

  ```bash
  git tag -a vX.Y.Z -m "vX.Y.Z"
  git push origin vX.Y.Z
  ```

  `release.yml` then runs the validator with the tag (fails if it doesn't equal `v` + manifest version), extracts that version's section from `CHANGELOG.md` as release notes, and creates the release. Tag only commits where the manifests and changelog already agree. Locally, `RELEASE_TAG=vX.Y.Z python3 ci-validate.py` rehearses the tag check.
