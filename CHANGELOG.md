# Changelog

## Unreleased

- afpm: new `feature-specs` knowledge skill (spec structure: evidence-cited problem, user journey, 3–5 critical user stories with observable acceptance criteria, falsifiable hypothesis, assumptions) and `/write-spec` workflow skill that drafts a spec from insights and personas. Stage 4 of `/afpm-guide-me` and TUTORIAL.md now point to `/write-spec` — every stage of the loop has a command.
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
