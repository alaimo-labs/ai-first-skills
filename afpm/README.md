# afpm — AI-First Product Manager

Agent skills for discovery and validation with synthetic users. Companion plugin for the [AI-First Product Manager](https://alaimolabs.com/es/courses/ai-first-product-manager) program by Alaimo Labs.

## Overview

This plugin gives your coding agent a product-discovery toolkit: frame opportunities before choosing solutions, compare solution alternatives against the evidence, test the chosen ones before building anything, create synthetic personas, interview them, extract insights, run critique panels over your specs, and slice features into exposure plans. It also bridges to real research: design interview guides and surveys, analyze the results, and derive evidence-based personas from the patterns. All artifacts are plain markdown files in your repo under `product/` — no external services.

Content is written in English; all deliverables come out in the language you work in.

## Install

From the `ai-first-skills` marketplace in Claude Code:

```
/plugin install afpm
```

The plugin also ships a portable [Agent Plugins](https://agent-plugins.org) manifest, so compatible clients (Cursor, VS Code, GitHub Copilot, ChatGPT & Codex, Kiro, OpenClaw, Hermes) can load it too — see the [repo README](../README.md#other-clients-portable-agent-plugins-format) for per-client instructions.

## Workflows

User-invoked skills — you trigger them as slash commands; they never auto-load.

| Workflow             | What it does                                                  |
| -------------------- | ------------------------------------------------------------- |
| `/start-product`     | Bootstrap `product/overview.md`: mode, context, sponsor (internal), ranked and tagged unverified beliefs |
| `/frame-opportunity` | Frame a problem for a segment — signals, beliefs, research agenda — before any solution |
| `/research-market`   | Secondary research/benchmarking, every claim provenance-tagged |
| `/generate-personas` | Generate a diverse set of synthetic personas — typed `primary`/`secondary`/`tertiary`/`negative`, mix on request or proposed |
| `/interview-persona` | Interview a persona — exploration or validation mode          |
| `/extract-insights`  | Extract actionable insights from transcripts (synthetic/real) |
| `/design-interview`  | Design an interview guide + recruitment plan (survey opt-ins first) for real-user research |
| `/test-interview-guide` | Pretest a guide against a persona and fix what breaks      |
| `/design-survey`     | Design a survey questionnaire with an interview opt-in block and a distribution plan (named channels, one link each, target n, dates), ready for any survey tool |
| `/analyze-survey`    | Analyze survey results: quant summary, themes, insights       |
| `/derive-personas`   | Derive evidence-based personas from real research patterns    |
| `/map-frictions`     | Map cognitive frictions across a journey's steps (MFC)        |
| `/explore-solutions` | Starts from an opportunity: 3–5 alternatives with different mechanisms vs. the current workaround, judged desirable / feasible / viable against the evidence (problem evidence alone never makes desirability `strong`); you choose which ones to test, it ends with the value proposition and the belief to test per alternative |
| `/design-solution-tests` | From a solutions file: the cheapest test that could refute the riskiest belief of each alternative under test — type by risk, with whom, material needed, signal, threshold, decision rule, expected provenance — before anything is built; a multi-week pilot is a next step, never the first |
| `/build-solution-test` | Build the material for one designed test — prototype, prompt + input set + answer key, script, fake-door copy, always a capture sheet — exactly what the design asks for; never changes the signal or threshold |
| `/analyze-solution-tests` | Read the results against the pre-set thresholds, decide per alternative (`continue` / `change` / `discard`), mark classroom or role-play runs `synthetic`, update the solutions file and (for `real` results) the belief registry |
| `/clarify-idea`      | The path without exploration — starts from one idea already decided: sharpen it via one-question-at-a-time brainstorming; names its parent opportunity, the exploration and the tests it came from, or declares none |
| `/write-spec`        | Draft an evidence-grounded spec: journey, stories, criteria — from an idea brief or straight from a tested alternative; what was tested is fixed, and a decision that changes it is flagged |
| `/critique-spec`     | Persona panel critiques a spec/PRD, with synthesis            |
| `/slice-feature`     | Turn a spec's hypothesis into an Exposure Plan                |
| `/review-evidence`   | Weekly sweep: new evidence vs. beliefs, drift report, corrections log |

## Knowledge skills

Model-invoked — the agent loads them automatically when the topic matches.

| Skill                  | Knowledge it carries                                              |
| ---------------------- | ----------------------------------------------------------------- |
| `opportunity-framing`  | Opportunity vs. solution vs. outcome, signals vs. proof, research agenda, the OST as files |
| `solution-exploration` | Real alternative vs. variation, the workaround as baseline, the desirable / feasible / viable filter and who owns each judgment, problem evidence vs. solution evidence, the value proposition, the solutions file |
| `solution-testing`     | Testing an alternative before building it: one belief per test, the cheapest test first, the test menu by risk (concierge, Wizard of Oz, prototype shown, usability test, technical test, fake door, buyer conversation), thresholds and decision rules written before the run, provenance of results, the tests file |
| `secondary-research`   | Provenance discipline, source hierarchy, lanes, belief mapping    |
| `synthetic-personas`   | Archetype principles, persona structure, the four persona types, diversity requirements |
| `synthetic-interviews` | In-character interview roleplay; exploration vs. validation modes |
| `insight-extraction`   | Focus areas, grounding rules, insight quality bar                 |
| `interview-guides`     | Discussion-guide design: goals → questions, funnel, non-leading; pretesting |
| `survey-design`        | Questionnaire craft, wording bias, scales, results analysis       |
| `cognitive-frictions`  | The MFC lens: four friction categories, severity, opportunity bar |
| `feature-specs`        | Spec structure: journey, stories, criteria, hypothesis, risk-tagged assumptions |
| `persona-critique`     | In-character document reviews and panel synthesis                 |
| `exposure-plans`       | Build ≠ reveal, belief decomposition, level design, validations   |

## File conventions

Artifacts live in your repo:

```
product/
├── overview.md          # product context, sponsor (internal), tagged + ranked belief registry
├── corrections.md       # log of human corrections to AI proposals (kept by /review-evidence)
├── personas/            # one file per persona (synthetic or derived), each with a `type:` — primary / secondary / tertiary / negative
├── interviews/          # transcripts, synthetic and real
├── interview-guides/    # guides for real-user interviews
├── surveys/             # survey questionnaires, each with its distribution plan
├── insights/            # extracted insights, survey analyses & critique panels
├── research/            # secondary research & benchmarks
├── journeys/            # user journeys + cognitive friction maps
├── opportunities/       # opportunity briefs: problem + segment + signals + research agenda, no solution yet
├── solutions/           # alternatives compared for one opportunity, the ones chosen for testing (with their value proposition), and after the tests the outcome per alternative
├── tests/               # solution tests: design (belief, type, with whom, signal, threshold, decision rule), results and decision per alternative
│   └── materials/       # per test: prototype, prompt + input set + answer key, script, capture sheet (written only by /build-solution-test)
├── ideas/               # clarified idea briefs — the path without exploration (each names its parent opportunity, or `none (declared)`, the exploration and the tests it came from)
├── specs/               # feature specs
└── exposure-plans/      # exposure plans
```

`overview.md` is the **single belief registry**: every unverified belief lives there — never in per-opportunity, per-idea, or per-spec lists — tagged by scope (`[product]`, `[opportunity: {slug}]`, or `[feature: {slug}]`) and risk (`[value]` / `[usability]` / `[feasibility]` / `[viability]`), ranked by impact × uncertainty. Internal products also record their **sponsor**: who funds the product and what they need to see to keep funding it.

The three scopes mirror an **Opportunity Solution Tree**: `overview.md` (outcome + product beliefs) → `opportunities/` (a problem for a segment, framed by `/frame-opportunity`) → `solutions/` (3–5 genuinely different alternatives for that problem, compared against the evidence by `/explore-solutions`; you choose which to test, it recommends) → `tests/` (the cheapest test that could refute each alternative's riskiest belief, designed by `/design-solution-tests`, its material built by `/build-solution-test`, its results read by `/analyze-solution-tests`) → `specs/` → `exposure-plans/`. Two sequences:

- **With exploration:** `/explore-solutions` → `/design-solution-tests` → `/build-solution-test` (once per test that needs material) → run the tests → `/analyze-solution-tests` → `/write-spec` → `/critique-spec` → `/slice-feature`. The spec inherits the opportunity, the persona, the value proposition, and the tested version from the solutions and tests files; a spec decision that changes what a test covered is flagged, and the belief is unverified again.
- **Without exploration** (the idea arrives decided): `/clarify-idea` → `/write-spec`, as before.

The middle levels are optional, but skipping them is a declared decision: the idea brief records `opportunity: none (declared)` and registers the problem it assumes as a belief, `solutions explored: no (declared)` when the problem was framed but the idea never competed with alternatives, or `solutions tested: no (declared)` when it competed but was never tested. Problem evidence is not solution evidence: ten interviews about the pain prove the pain, and the alternative's value belief stays open until someone reacts to the solution itself — that is what the tests are for. Runs with colleagues, classmates, or acted roles are rehearsals (`synthetic`) and never move a belief.

As evidence arrives, beliefs in `overview.md` get a status appended on the belief's own line — `— confirmed/contradicted/weakened by [file] (date)` (keywords stay in English, like `source:` values; no status = still unverified). Only evidence from real users confirms; synthetic evidence just makes a belief promising. `/review-evidence`, `/extract-insights`, `/analyze-survey`, and `/analyze-solution-tests` (for `real` results only) propose these annotations — you approve before anything is written.

## License

[CC BY-SA 4.0](../LICENSE) © [Alaimo Labs](https://alaimolabs.com). Use, adapt, and share freely — credit Alaimo Labs and keep derivatives under the same license.
