---
name: generate-personas
description: Generate a diverse set of synthetic user personas for your product, saved as markdown files ready for interviews and critiques
argument-hint: "[count and/or focus, e.g. '3 personas for the B2B segment']"
disable-model-invocation: true
---

# /generate-personas

Create synthetic user personas for the current product, following the `synthetic-personas` skill.

Input: $ARGUMENTS

## Workflow

1. **Load product context.** Read `product/overview.md` if it exists; otherwise look for a README or similar product description. If no product context exists, ask for the product name, a short description, and target users — then offer to save that as `product/overview.md`.

2. **Read existing personas** in `product/personas/` to avoid duplicates and to fill diversity gaps (the new set should complement, not repeat).

3. **Determine count and focus** from the arguments. Default: 3 personas. If a segment or focus was named, honor it.

4. **Generate the personas** per the `synthetic-personas` skill: archetype principles, full structure, diversity requirements, in the language of the product context.

5. **Present the set** briefly (name, role, one-line perspective each) and ask for adjustments before saving.

6. **Save** each persona to `product/personas/{name-slug}.md`.

Close by suggesting next steps in one line: interview a persona (`/interview-persona`) or critique a spec with them (`/critique-spec`).
