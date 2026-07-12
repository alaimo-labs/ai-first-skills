# Changelog

## v0.2.1 — 2026-07-12

- Human-readable `displayName` ("AI-First Product Manager" / "AI-First Product Builder") in both plugin manifests and marketplace entries — shown in the `/plugin` picker; install names (`afpm`, `afpb`) unchanged.

## v0.2.0 — 2026-07-12

- afpm: `/afpm-tutorial` workflow skill — guided step-by-step tour of the discovery loop with the user's own product; infers the current stage from `product/` contents (no state files), one stage per invocation. Companion written walkthrough in `afpm/TUTORIAL.md`, linked from the README.
- Initial scaffold: marketplace with `afpm` and `afpb` plugins.
- afpm: knowledge skills `synthetic-personas`, `synthetic-interviews`, `insight-extraction`, `persona-critique`, `exposure-plans`; workflow skills `/generate-personas`, `/interview-persona`, `/extract-insights`, `/critique-spec`, `/slice-feature`.
- afpb: knowledge skills `falsifiable-hypotheses`, `exposure-plans`; workflow skills `/formulate-hypothesis`, `/plan-exposure`.
- Commands migrated to user-invoked workflow skills (`disable-model-invocation: true`) for cross-client portability (Agent Skills open standard); the `commands/` directories are gone, slash invocation unchanged.
