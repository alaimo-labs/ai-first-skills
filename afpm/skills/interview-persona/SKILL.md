---
name: interview-persona
description: Interview one of your synthetic personas — exploration mode (open discovery) or validation mode (feedback on an idea)
argument-hint: "<persona name> [exploration|validation] [topic]"
disable-model-invocation: true
---

# /interview-persona

Run a synthetic user interview, following the `synthetic-interviews` skill.

Input: $ARGUMENTS

## Workflow

1. **Resolve the persona.** Find the named persona in `product/personas/`. If no name given, list available personas and ask. If none exist, suggest `/generate-personas` first.

2. **Resolve the mode.** Exploration (open discovery) or validation (feedback on a specific idea). If not specified and not obvious, ask — one question, two options. In validation mode, also ask what idea/prototype/direction is being validated if not provided.

3. **Load product context** from `product/overview.md` (or equivalent).

4. **Set the scene** in one short message: who the persona is (one line), the mode, and that the user is now the interviewer. Then hand over — they ask the first question.

5. **Roleplay** per the `synthetic-interviews` skill and the mode-specific instructions (exploration-mode.md / validation-mode.md). Stay in character until the interviewer ends the interview. Interviewer coaching notes go outside the roleplay, clearly marked, and sparingly.

6. **On wrap-up:** offer to save the transcript to `product/interviews/{persona-slug}-{YYYY-MM-DD}.md` (header: persona, mode, topic, date) and suggest `/extract-insights` on it.
