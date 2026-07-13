---
name: critique-spec
description: Have your synthetic personas critique a spec, PRD, or product idea — individual in-character reviews plus a panel synthesis
argument-hint: "<spec file or idea> [persona names; defaults to all personas]"
disable-model-invocation: true
---

# /critique-spec

Run a persona critique panel over a document, following the `persona-critique` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the document.** A file path (look in `product/specs/` first), pasted content, or an idea described inline. If nothing resolvable, ask.

2. **Resolve the panel.** Named personas from `product/personas/`, or all of them by default (cap at 4 — if more exist, propose the 4 most relevant to this document and let the user adjust). If none exist, suggest `/generate-personas`.

3. **Critique.** Each persona reviews the document in character per the `persona-critique` skill: rating, strengths, concerns, suggestions — honest, literacy-aware, in the document's language.

4. **Synthesize** as the researcher: agreements, conflicts (design tensions), and the 2–3 highest-impact changes.

5. **Save** to `product/insights/{YYYY-MM-DD-HHMM}-critique-{spec-slug}.md` and offer the natural next step in one line (e.g., revise the spec, or slice it with `/slice-feature`).
