---
name: generate-personas
description: Generate a diverse set of synthetic user personas for your product — typed primary/secondary/tertiary/negative, mix on request — saved as markdown files ready for interviews and critiques
argument-hint: "[count, mix and/or focus, e.g. '2 primary, 1 tertiary, 1 negative for the B2B segment']"
disable-model-invocation: true
---

# /generate-personas

Create synthetic user personas for the current product, following the `synthetic-personas` skill.

Input: $ARGUMENTS

## Workflow

1. **Load product context.** Read `product/overview.md` if it exists; otherwise look for a README or similar product description. If no product context exists, suggest `/start-product` first (it also captures the unverified beliefs later stages test); if the user prefers to continue here, ask for the product name, a short description, and target users — then offer to save that as `product/overview.md`.

2. **Read existing personas** in `product/personas/` to avoid duplicates and to fill diversity gaps (the new set should complement, not repeat — including the type mix: note which types the existing set already covers). An existing persona without a `type:` line was created before the field existed: propose a type for it from its content and offer to write it in — with the user's approval, never silently.

3. **Determine count, mix, and focus.** If the arguments name a mix ("2 primary, 1 tertiary, 1 negative"), honor it to the letter — that count, those types. If they don't, **propose** a mix and get it confirmed before generating: derive it from the `mode:` line of the overview and the segment — a default of 4 (2 `primary`, 1 `secondary` or `tertiary`, 1 `negative`), with a `tertiary` whenever someone other than the user decides, pays, or approves (internal products: the sponsor; B2B: the buyer or admin). Show the proposal in one line ("2 primary, 1 tertiary, 1 negative — ok?") and wait for the answer. Never generate a set without at least one `primary` and one `negative`; if the requested mix lacks one, say so in one line and follow the request anyway. If a segment or focus was named, honor it.

4. **Generate the personas** per the `synthetic-personas` skill: archetype principles, full structure with the `type:` field, diversity requirements, in the language of the product context. A `negative` persona is a scope boundary, not a caricature: someone who looks like a user and is left out on purpose.

5. **Present the set** briefly — name, role, **type**, one-line perspective each — and ask for the review with two explicit questions per persona: does this persona belong to the product? Is the type the right one? A type change is applied on the spot. A discard is recorded in `product/corrections.md` with its reason (dated entry — artifact, what the AI proposed, what the human decided, why; create the file on first use). **Discard for not belonging to the product, never for taste or because "it looks like a stereotype"; if every persona belongs, none is discarded.**

6. **Save** each persona to `product/personas/{name-slug}.md`, with the type written literally as `- **Type:** {value}` right after the role line (label and value in English, whatever the language of the rest).

Close by suggesting next steps in one line: interview a persona (`/interview-persona`) or critique a spec with them (`/critique-spec`).

## Language

Conversation and the saved personas in the language of the conversation. The `type:` values (`primary`, `secondary`, `tertiary`, `negative`) are fixed English tokens in every language, like `source:` values.
