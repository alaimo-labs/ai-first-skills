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

1. **Resolve the persona.** Find the named persona in `product/personas/`. If no name given, list available personas (with their type) and ask. If none exist, suggest `/generate-personas` first. If the persona has no `type:` line (created before the field existed), propose one from its content and offer to write it into the file before starting — with the interviewer's approval; without it, proceed and treat the type as unknown.

2. **Resolve the mode.** Exploration (open discovery) or validation (feedback on a specific idea). If not specified and not obvious, ask — one question, two options. In validation mode, also ask what idea/prototype/direction is being validated if not provided.

3. **Load product context** from `product/overview.md` (or equivalent).

4. **Set the scene** in one short message: who the persona is (one line, type included), the mode, and that the user is now the interviewer. Then hand over — they ask the first question.

   **How this evidence reads, by type.** Interviewing a `negative` persona is useful — they say why not, and that bounds the scope — but their answers count neither for nor against a value belief of the target segment. A `tertiary` persona informs viability (who pays, approves, blocks), not desirability: their answers do not confirm or contradict value beliefs either. Say this in one line when the persona is `negative` or `tertiary`, and repeat it in the transcript header so `/extract-insights` reads it too.

5. **Roleplay** per the `synthetic-interviews` skill and the mode-specific instructions (exploration-mode.md / validation-mode.md). Stay in character until the interviewer ends the interview. Interviewer coaching notes go outside the roleplay, clearly marked, and sparingly.

6. **On wrap-up:** offer to save the transcript to `product/interviews/{YYYY-MM-DD-HHMM}-{persona-slug}.md` (header: persona, `type:` next to `source: synthetic`, mode, topic, date — plus the one-line reading warning when the persona is `negative` or `tertiary`) and suggest `/extract-insights` on it.

## Language

Conversation and the transcript in the language of the conversation. The `type:` and `source:` values are fixed English tokens in every language.
