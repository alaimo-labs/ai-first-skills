---
name: test-interview-guide
description: Pretest an interview guide by running it against a synthetic persona — surfaces speculation, leading questions, dead ends, and coverage gaps in the guide, then revises it
argument-hint: "[guide file; defaults to the most recent] [persona name; defaults to the guide's participant profile]"
disable-model-invocation: true
---

# /test-interview-guide

Pretest an interview guide before it meets real participants. The persona is the instrument, not the subject: the deliverable is a diagnosis of the guide and a revision of it — **not** research findings.

Follow the pretesting section of the `interview-guides` skill for what counts as a defect, and the `synthetic-interviews` skill for the roleplay.

Input: $ARGUMENTS

## Workflow

1. **Resolve the guide.** A file in the arguments wins; otherwise take the most recent in `product/interview-guides/`. If none exist, suggest `/design-interview` first and stop.

2. **Resolve the persona.** A name in the arguments wins; otherwise match the guide's participant profile against `product/personas/` and say which one you picked and why. If nothing matches the profile, say so — a guide pretested against the wrong participant proves nothing — and ask the user to choose or to generate a fitting persona.

3. **Load context** from `product/overview.md` (or equivalent) and the persona file.

4. **Announce the run** in two or three lines: which guide, which persona, and that this is a pretest of the guide's design — no interviewing on the user's part, no evidence produced. Note they can interrupt at any point to probe a question themselves.

5. **Dry-run the guide.** Ask its questions in order, in character as the interviewer, and answer in character as the persona. Mark the two voices clearly. Rules for the run:
   - Follow the guide as written — including its probes, and including questions you can already tell are broken. The point is to observe the failure, not to repair it mid-run.
   - Answer as a real participant would on an ordinary day: partially attentive, sometimes vague, occasionally off-topic, not always sure why they do what they do. Never expand a thin answer into a helpful one; a thin answer is data about the question.
   - Keep the persona's `synthetic-interviews` fidelity rules — frustrations carry consequences, no politeness, no pitching back.
   - Skip the interviewer-coaching asides from `synthetic-interviews`. Defects get collected in step 6 instead of interrupting the run.

6. **Diagnose the guide**, out of character, against the failure taxonomy in `interview-guides`. For each finding: quote the question, quote the answer that exposes it, name the defect, and propose the rewrite. Cover coverage in both directions — a learning goal no question reaches, and a question serving no goal. Close with the two or three defects worth fixing first.

7. **Revise the guide in place.** Same file, no rename — the timestamp is the creation date. Apply the fixes the user approves, then append (or update) a dated `## Pretest notes` section recording which persona it was run against, what changed, and what was left alone on purpose.

8. **Close** with:
   - an offer to re-run the pretest on the revision (a second pass catches defects the first round's fixes introduced);
   - an offer to save the dry-run transcript — **off by default**. Say why: a transcript in `product/interviews/` reads as evidence, and this one isn't. If the user wants it, save to `product/interviews/{YYYY-MM-DD-HHMM}-pretest-{guide-slug}.md` with `source: synthetic` and `mode: pretest` in the header, and note it should not be fed to `/extract-insights`.
   - the honest limit, in two lines: this pretest catches structural defects — speculation, leading, redundancy, ordering, coverage. It cannot tell the user whether real people will understand the wording or open up, because a persona is more articulate and more cooperative than any real participant. A clean pretest means the guide is sound, not that it is validated.

## Rules

- Never save findings to `product/insights/` — that directory holds user evidence, and this is instrument QA.
- Never revise a question silently. Every change is proposed with the evidence that motivated it, and the user decides.
- All conversation, the dry-run, and the revised guide in the language of the conversation — and if the guide notes that the real interviews run in a different language, pretest in that language, since wording defects don't survive translation.
