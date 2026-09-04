# Changelog

## v0.6.0 — 2026-09-01

- afpm: the memory loop closes — new `/review-evidence` workflow skill, the PM's weekly sweep (named `review-evidence` because bare `/review` collides with Claude Code's built-in review command, which wins the resolution). It lists the `product/` artifacts created or modified since the last review (`git log`, or filename timestamps without git), contrasts the new evidence against each unverified belief in `product/overview.md` respecting the provenance hierarchy (`source: real` > `survey` > `secondary` > `synthetic` — synthetic evidence never confirms a belief, it only makes it promising), and proposes per-belief annotations `— confirmed/contradicted/weakened by [file] (date)` (fixed English keywords; no status = still unverified; user approves before writing; beliefs are annotated, never deleted). It also reports drift (beliefs without evidence, synthetic insights without real verification, specs without critique, hypothesis files with an empty Outcome section when `product/hypotheses/` exists), asks what the human corrected of what the AI proposed this week, and appends it to the new `product/corrections.md` (single living file, dated entries: artifact, AI proposal, human decision, why — reviews are recorded even when there were no corrections). Closes with a one-screen summary and a suggested next step.
- afpm: `/extract-insights` and `/analyze-survey` feed the loop too — after saving, both contrast their findings against the overview's beliefs and offer to annotate the affected ones with the same convention, always with the user's approval. Real and survey evidence can confirm or contradict (surveys within their sample limits); synthetic insights only signal. The `insight-extraction` knowledge skill documents the feedback step.
- Belief-status convention and `product/corrections.md` documented in the File Conventions of `CLAUDE.md` and in the afpm README (which also lists `/review-evidence`).

## v0.5.1 — 2026-08-09

- Repo README: renamed the title to "AI-First Product Skills"
- Install instructions for the two clients newly listed as Agent Plugins-compatible: OpenClaw (`openclaw plugins install` + gateway restart) and Hermes (`hermes plugins install` + explicit enable); both plugin READMEs mention them
- Cursor install instructions now say to copy the plugin into `~/.cursor/plugins/local/` instead of symlinking — verified on Cursor 3.8.11 that symlinks pointing outside that directory are rejected (`loadUserLocalPlugin rejected`), while a copied directory hot-loads without a restart

## v0.5.0 — 2026-08-08

- Portable [Agent Plugins](https://agent-plugins.org) 1.0.0 support: each plugin now ships a root `plugin.json` conforming to the portable manifest schema, alongside the Claude Code manifest in `.claude-plugin/`. Compatible clients (Cursor, VS Code, GitHub Copilot, ChatGPT & Codex, Kiro) can load the plugins directly; the Claude Code marketplace flow is unchanged.
- READMEs: per-client install instructions for the portable format in the repo README, referenced from both plugin READMEs.
- `ci-validate.py`: validates the portable manifests against the closed 1.0.0 schema, enforces that shared fields stay in sync between the two manifests of each plugin, and flags duplicate JSON keys in all manifests.
- Fixed a duplicate `license` key in both `.claude-plugin/plugin.json` files that made the plugins report MIT instead of CC-BY-SA-4.0.

## v0.4.2 — 2026-08-05

- Licensed the repo under CC BY-SA 4.0: `LICENSE` file, License sections in the three READMEs, and `license: CC-BY-SA-4.0` in the marketplace and plugin manifests
- afpm + afpb: `/slice-feature` and `/plan-exposure` now present the full exposure plan and get the user's agreement before saving — they used to save without showing it

## v0.4.1 — 2026-08-04

- afpm: `/clarify-idea` now shows the full idea brief in the conversation before asking to save it — it used to ask for confirmation over a brief the user hadn't seen

## v0.4.0 — 2026-08-04

- afpm: removed `/afpm-guide-me` due to circular references and restrictive linear promotion
- afpm: cognitive friction mapping — new knowledge skill `cognitive-frictions` (the Cognitive Friction Map from Alaimo Labs: four friction categories — Transformation, Limiter, Standardizer, Evaluator points — with a per-step block of category-with-why, friction, problem, evidence metric, severity, and metric impact; evidence metrics must come from data already in the repo or be marked "not yet measured", never invented) and workflow skill `/map-frictions` (resolves the journey from a file, pasted text, or a spec's journey section — or elicits it actor/goal/steps when none exists — analyzes each step through the MFC lens, ranks frictions by severity as AI-opportunity candidates, and saves to the new `product/journeys/` directory). Hands off to `/clarify-idea`, `/write-spec`, or `/interview-persona`.
- afpm: new `/test-interview-guide` workflow skill — pretest an interview guide by running it end to end against a synthetic persona, then diagnose the _guide_ from the answers (speculation, leading questions, double-barreled wording, redundancy, dead ends, missing probes, priming, coverage gaps, overrun) and revise it in place with a dated `## Pretest notes` section. The persona is the instrument, not the subject: findings never land in `product/insights/`, and the dry-run transcript is not saved by default. `interview-guides` gains the pretesting discipline (defect taxonomy + what a synthetic pretest cannot tell you); `/design-interview` now closes by pointing here instead of suggesting a manual rehearsal.
- afpm: secondary research — new knowledge skill `secondary-research` (provenance discipline: every claim labeled `verificado`/`conocimiento del modelo`; source hierarchy; lanes: competitors, alternatives/non-consumption, pricing, positioning, trends; belief-impact mapping) and workflow skill `/research-market` (derives questions from the overview's beliefs, states the method up front — web vs model knowledge, parallel subagents when available — and saves to `product/research/` with `source: secondary`, kept apart from user evidence in `insights/`). `/start-product`, `/clarify-idea`, and `/write-spec` now read or suggest it; degrades gracefully in clients without web search or subagents.
- afpm: new `/start-product` workflow skill — bootstrap `product/overview.md` from scratch: reads existing repo context as hypothesis (user confirms before it's written), interviews for the rest, and pushes for 3–5 falsifiable unverified beliefs about the users. `/generate-personas` suggests it when no product context exists.
- afpm: real-research bridge — new knowledge skills `interview-guides` (discussion-guide design: goals → beliefs at risk → non-leading questions, funnel structure, falsification notes) and `survey-design` (questionnaire craft, wording bias, scales, plus results analysis: denominators, segment cuts, open-end coding); new workflow skills `/design-interview` and `/design-survey` (turn assumptions/insights into research instruments, saved to `product/interview-guides/` and `product/surveys/`), `/analyze-survey` (results → goal-by-goal analysis + insights with `source: survey`), and `/derive-personas` (cluster patterns across real interviews/surveys into evidence-based personas, `source: derived`, reconciled against the existing synthetic set). `/extract-insights` now archives external real transcripts into `product/interviews/` with `source: real`; the README points the way from synthetic to real.
- afpm: new `/clarify-idea` workflow skill — sharpen a fuzzy feature idea through evidence-grounded questioning (one question at a time, each with a recommended answer; facts come from `product/`, decisions stay with the user, unknowns become ranked assumptions). Saves the brief to `product/ideas/{YYYY-MM-DD-HHMM}-{slug}.md` and hands off to `/write-spec` or validation interviews.
- afpm: new `feature-specs` knowledge skill (spec structure: evidence-cited problem, user journey, 3–5 critical user stories with observable acceptance criteria, falsifiable hypothesis, assumptions) and `/write-spec` workflow skill that drafts a spec from insights and personas.
- afpm + afpb: dated artifacts now use date-first filenames — `{YYYY-MM-DD-HHMM}-{slug}.md` (critiques: `{YYYY-MM-DD-HHMM}-critique-{spec-slug}.md`) — so listings sort chronologically and same-day files don't collide. Applies to interviews, insights, critiques, specs, and exposure plans; the timestamp is the creation date and revisions edit in place without renaming. Only `overview.md` and personas stay undated.

## v0.3.0 — 2026-07-12

- afpm: renamed `/afpm-tutorial` → `/afpm-guide-me` — the skill is a resumable guide (run it after installing and any time you wonder what's next), not a one-shot tutorial. The old command no longer exists.

## v0.2.2 — 2026-07-12

- afpm: `/afpm-tutorial` no longer treats repo-derived product context as fact — it presents what it inferred (with sources) and asks the user to confirm or correct before writing the overview.

## v0.2.1 — 2026-07-12

- Human-readable `displayName` ("AI-First Product Manager" / "AI-First Product Builder") in both plugin manifests and marketplace entries — shown in the `/plugin` picker; install names (`afpm`, `afpb`) unchanged.

## v0.2.0 — 2026-07-12

- afpm: `/afpm-tutorial` workflow skill — guided step-by-step tour of the discovery loop with the user's own product; infers the current stage from `product/` contents (no state files), one stage per invocation. Companion written walkthrough in `afpm/TUTORIAL.md`, linked from the README.
- Initial scaffold: marketplace with `afpm` and `afpb` plugins.
- afpm: knowledge skills `synthetic-personas`, `synthetic-interviews`, `insight-extraction`, `persona-critique`, `exposure-plans`; workflow skills `/generate-personas`, `/interview-persona`, `/extract-insights`, `/critique-spec`, `/slice-feature`.
- afpb: knowledge skills `falsifiable-hypotheses`, `exposure-plans`; workflow skills `/formulate-hypothesis`, `/plan-exposure`.
- Commands migrated to user-invoked workflow skills (`disable-model-invocation: true`) for cross-client portability (Agent Skills open standard); the `commands/` directories are gone, slash invocation unchanged.
