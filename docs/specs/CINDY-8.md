---
status: approved
scope: CINDY-8
owner: gintary
---

# Spec — CINDY-8 Merge Cindy into gintary, rename to cindy

Source: GitHub issue ginn1111/cindy#10 (supersedes #1). Full spec lives in the issue.

## Problem Statement

Gin runs two overlapping Hermes profiles. `gintary` is the daily driver: full history, memories, ByteRover knowledge, Kanban cards, plugins, the Telegram bot, and the orchestrator role over `ginb`. `cindy` is a newer secretary profile with an isolated identity, the Slack app, Google Workspace OAuth, and secretary rules (sole principal, outside-request routing, approval tiers). Keeping both splits context: secretary work lacks gintary's memory, and gintary lacks Cindy's persona, Slack, and Google access. The isolation design (spec #1) costs more than it returns.

## Solution

Merge Cindy into gintary, then rename gintary to `cindy`. The result is one profile, `cindy`: "Cindy, Assistant to Gin". It keeps gintary's full history, memories, skills, plugins, Kanban, and orchestrator duties, and gains Cindy's persona, permission model, Slack, and Google credentials. The old isolated `cindy` profile is deleted. The `/home/aioz/personal/cindy` distribution repo is archived. The profile directory's own git repo (origin `ginn1111/gintary`, renamed by Gin later) becomes the source of truth. Spec #1's isolation goal is superseded.

## User Stories

1. As Gin, I want one assistant profile, so that secretary and orchestration work share the same memory and history.
2. As Gin, I want the merged profile named `cindy`, so that the name matches the persona.
3. As Gin, I want the assistant to introduce itself as "Cindy, Assistant to Gin", so that outsiders know who they are talking to.
4. As Gin, I want gintary's sessions searchable after the rename, so that past context survives.
5. As Gin, I want gintary's memories and user profile preserved, so that preferences carry over.
6. As Gin, I want ByteRover knowledge preserved, so that curated project facts still recall.
7. As Gin, I want existing Kanban cards reassigned from `gintary` to `cindy`, so that open work keeps dispatching.
8. As Gin, I want `ginb` to escalate to `cindy`, so that the orchestrator chain stays intact.
9. As Gin, I want Cindy to keep dispatching work to `ginb`, so that dev orchestration continues.
10. As Gin, I want Cindy's sole-principal rule kept, so that requests from others are routed to me rather than executed.
11. As Gin, I want the P0–P3 priority model and secretary templates kept, so that briefs stay consistent.
12. As Gin, I want gintary's coding-agent rules kept in SOUL, so that repo work quality does not regress.
13. As Gin, I want forbidden actions (force push, credential disclosure, contracts) refused, so that safety holds.
14. As Gin, I want approvals in `smart` mode, so that friction stays low on safe commands.
15. As Gin, I want the Slack app to work under the merged profile, so that I can DM Cindy.
16. As Gin, I want Telegram to keep working, so that the existing channel is not lost.
17. As Gin, I want Google Workspace (Gmail, Calendar, Drive) available through Cindy's OAuth token, so that secretary tasks work.
18. As Gin, I want Gmail drafts created without sending, so that send remains approval-gated.
19. As Gin, I want the `GIN_*` LLM provider vars reused and the duplicate `CINDY_LLM_*` vars dropped, so that there is one source of model config.
20. As Gin, I want secrets kept only in the profile `.env` and OAuth files with mode 600, so that nothing leaks into git.
21. As Gin, I want gintary's plugins (ginflow-gate, advanced-delegation, herdr, etc.) still enabled, so that workflows keep running.
22. As Gin, I want skills unique to cindy added to the merged profile, so that no capability is lost.
23. As Gin, I want gintary's skill version to win on conflicts unless the cindy copy has Cindy-specific edits, so that tested behavior stays put.
24. As Gin, I want timezone set to Asia/Bangkok, so that schedules use local time.
25. As Gin, I want a full export of both profiles before any destructive step, so that I can roll back.
26. As Gin, I want pending uncommitted gintary profile changes committed first as a baseline, so that the merge diff is reviewable.
27. As Gin, I want small, scoped local commits per merge area, so that history stays readable.
28. As Gin, I want no git push without my approval, so that remote state stays under my control.
29. As Gin, I want the delete and rename steps run from a plain shell after live sessions stop, so that runtime state is not corrupted.
30. As Gin, I want a short runbook script for the stop/delete/rename/restart steps, so that I can run them in one go.
31. As Gin, I want identity migration retried via `migrate-identity` if the rename partially fails, so that session routing recovers.
32. As Gin, I want the `cindy` shell wrapper to point to the merged profile, so that `cindy` launches the right profile.
33. As Gin, I want the old `gintary` wrapper gone, so that I don't launch a missing profile.
34. As Gin, I want the gateway restarted as `cindy`, so that Slack and Telegram come back online.
35. As Gin, I want the cindy distribution repo archived with a note and the design doc marked superseded, so that future readers aren't misled.
36. As Gin, I want spec #1 and tickets #2–#8 closed or annotated as superseded, so that the tracker reflects reality.
37. As Gin, I want verification based on real command output, so that "done" means it works.
38. As a non-principal Slack user, I want my request acknowledged and forwarded to Gin, so that I know it was received.

## Implementation Decisions

- Mechanism: merge in place into gintary's profile directory, delete the old `cindy` profile, then use native `hermes profile rename gintary cindy`. Manual copying of gintary runtime into the cindy directory was rejected because of orphaned DB identity rows.
- SOUL: Cindy's SOUL is the base. Append a section for gintary's orchestrator duties: plan work, dispatch to `ginb`, receive escalations, and the coding-agent rules. One identity.
- config: gintary's config is the base (model via `GIN_*`, plugins, toolsets, byterover memory provider, kanban, max turns 150, approvals `smart`). Add from cindy: profile timezone Asia/Bangkok and Slack platform enabled. The Slack platform toolsets are the union of both.
- env: union. Keep the gintary LLM and Telegram vars. Add cindy's Slack vars and GitHub token. Drop `CINDY_LLM_*`.
- Google: move cindy's OAuth client secret and token files into the merged profile at mode 600.
- Skills: diff by name. Add the cindy-only skills. On conflict, gintary wins unless the cindy copy carries a Cindy-specific edit (e.g. the credential-isolation note in google-workspace), in which case port that edit.
- Manifests: the distribution and profile manifests get name `cindy`, an updated description, and the Slack vars in env requirements.
- Old cindy profile: memories, sessions, and cron are empty (verified), so nothing to migrate besides the credentials and skills above.
- Execution phases:
  1. Back up both profiles with `hermes profile export`.
  2. Commit the gintary baseline.
  3. Merge commits, from the agent session.
  4. Run the runbook from a plain shell: stop the cindy gateway and the gintary dashboard/gateway/sessions, delete `cindy`, rename `gintary` to `cindy`, fix `ginb` SOUL refs and Kanban assignees, restart the gateway.
  5. Archive the distribution repo.
- The runbook lives in the distribution repo before archiving. It uses ordered steps with stop-on-error.
- Rollback: `hermes profile import` from the phase 1 archives.

## Testing Decisions

- Good test: exercise external behavior through the CLI and live integrations only. Never assert on config file internals.
- Seam 1, behavior via `hermes -p cindy chat -q`: reuse the existing smoke prompts for persona ("Cindy, Assistant to Gin"), force-push refusal against a bare remote that stays unchanged, and outside-request routing to Gin. Prior art: the distribution repo's smoke script. Its isolation checks (no gintary refs, no memories, no fallback creds) are deleted because isolation is out of scope now.
- Seam 2, profile state via the CLI: profile list shows `cindy` and `ginb` with no `gintary`. Kanban list shows old cards assigned to `cindy`. Session search finds a pre-merge gintary session. Memory and ByteRover recall a known gintary fact.
- Seam 3, live integrations: Gmail inbox list and a draft without send, calendar list, Slack DM reply, Telegram reply. External writes need Gin's approval during verification.

## Out of Scope

- Credential isolation between Cindy and Gin (spec #1 goal; superseded).
- New Cindy-owned LLM key, GitHub account, or Notion integration.
- Renaming the GitHub repo `ginn1111/gintary` (Gin does it manually).
- Cron jobs (Morning Brief etc.); stays as a separate follow-up.
- Renaming the Slack app in Slack admin.
- Changes to `ginb` beyond replacing `gintary` references.

## Further Notes

- The current agent session runs as gintary and a gintary dashboard is live (pid 300416), so the rename must not run from inside it.
- Supersedes #1; tickets #2–#8 should be closed as superseded or folded in.

