---
name: review-evidence
description: Weekly evidence review — sweep the product/ artifacts created since the last review against the unverified beliefs in product/overview.md, propose belief-status annotations, report what's drifting, and log human corrections to AI proposals
argument-hint: "[review window, e.g. \"last 2 weeks\"; defaults to since the last review]"
disable-model-invocation: true
---

# /review-evidence

The PM's weekly sweep. The other skills produce evidence — interviews, insights, survey analyses, research — but evidence that never updates a belief is filing, not learning. This workflow closes the loop: it reads the new artifacts, contrasts them against the unverified beliefs in `product/overview.md`, and proposes updates.

Input: $ARGUMENTS

## Workflow

1. **Establish the window and gather the evidence.** Read `product/overview.md` (the beliefs) and `product/corrections.md` if it exists — its most recent entry marks the last review; the arguments may override the window; if neither exists, this is the first review: cover everything and say so. Then list every artifact under `product/` created or modified in the window: prefer `git log` when the repo is under git; without git, fall back to the `{YYYY-MM-DD-HHMM}-` filename prefixes (and note that in-place revisions — a spec edited after a critique — are invisible to filenames alone).

2. **Contrast the new evidence against each belief.** For every belief, ask of the new artifacts: does any confirm it, contradict it, or leave it untouched? Cite the evidence file for every verdict — no verdict without a file behind it. Respect the provenance hierarchy, `source: real` > `survey` > `secondary` > `synthetic`:
   - Real interviews and survey results can confirm or contradict a belief (surveys within the limits their analysis states — small or self-selected samples weaken rather than confirm).
   - Secondary research raises or lowers a belief's priority, but market evidence cannot verify beliefs about your users (see the `secondary-research` skill).
   - Synthetic evidence never confirms a belief on its own. Supporting synthetic evidence makes the belief *promising* — say so in the report, propose no annotation. Contradicting synthetic evidence can at most propose `weakened`.

3. **Propose updates to the overview.** For each affected belief, propose an annotation appended on the belief's own line:

   ```
   - {The belief as written} — confirmed by [product/insights/2026-08-20-1430-onboarding.md] (2026-08-20)
   ```

   The three status keywords — `confirmed`, `contradicted`, `weakened` — are fixed English tokens (like `source:` values) so they stay consistent and searchable; the surrounding text follows the file's language. No status = still unverified. Annotations accumulate: when new evidence conflicts with an existing annotation, surface the conflict for the user to resolve — never silently overwrite. Show every proposed edit and get the user's approval before writing. Never delete a belief; only annotate it.

4. **Report what's drifting.** The pendings the loop tends to lose:
   - Beliefs with no evidence yet, from any source.
   - `source: synthetic` insights never verified against real users.
   - Specs in `product/specs/` with no matching critique (`{YYYY-MM-DD-HHMM}-critique-{spec-slug}.md` in `product/insights/`).
   - If `product/hypotheses/` exists: hypothesis files whose Outcome section is still empty — an experiment exposed but never scored.

5. **Ask the correction question:** "What did you correct this week of what the AI proposed, and why?" Append each correction to `product/corrections.md` — a single living file, no timestamp prefix, dated entries appended at the end (create the file on first use):

   ```markdown
   ## {YYYY-MM-DD}

   - **Artifact:** {file the correction applies to}
     **AI proposed:** {what}
     **Human decided:** {what instead}
     **Why:** {the reasoning — the valuable part}
   ```

   If there were no corrections, don't invent any — record the review anyway (a dated entry noting no corrections), so the next `/review-evidence` knows where the last one ended.

6. **Close with a one-screen summary:** belief status at a glance (confirmed / contradicted / weakened / promising / untouched), the drift report prioritized by what most blocks learning, and the suggested next step in one line — name the workflow to run on the top pending item: `/design-interview` or `/design-survey` to take a belief or a synthetic insight to real users, `/critique-spec` for a spec that skipped its panel, `/analyze-survey` for unanalyzed results. (Name these explicitly — user-invoked workflows never auto-load, so their names are not otherwise in context.)

## Language

Conversation, annotations, and `corrections.md` entries (field labels included) in the language of the conversation. The only exception is the three status keywords, which stay in English as fixed tokens.
