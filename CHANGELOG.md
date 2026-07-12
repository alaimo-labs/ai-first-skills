# Changelog

## Unreleased

- Initial scaffold: marketplace with `afpm` and `afpb` plugins.
- afpm: knowledge skills `synthetic-personas`, `synthetic-interviews`, `insight-extraction`, `persona-critique`, `exposure-plans`; workflow skills `/generate-personas`, `/interview-persona`, `/extract-insights`, `/critique-spec`, `/slice-feature`.
- afpb: knowledge skills `falsifiable-hypotheses`, `exposure-plans`; workflow skills `/formulate-hypothesis`, `/plan-exposure`.
- Commands migrated to user-invoked workflow skills (`disable-model-invocation: true`) for cross-client portability (Agent Skills open standard); the `commands/` directories are gone, slash invocation unchanged.
