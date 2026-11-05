---
status: approved
scope: CINDY-5
owner: gintary
---

# Spec — CINDY-5 Activate scheduled secretary workflows

Source: GitHub issue ginn1111/cindy#6 (parent #1); design `docs/plans/2026-11-05-cindy-design.md`.

## Problem

See issue #6. Depends on: CINDY-2, CINDY-3, CINDY-4.

## Scope

Cindy cron jobs (profile `cindy`), job prompts, `deliver` routing to Gin Slack DM.

## Non-goals

Urgent Monitor, Post-Meeting Follow-Up, gintary cron jobs.

## Desired behavior

- B1 Five jobs must exist (UTC+7): Morning Brief weekdays 09:00; Inbox Triage weekdays hourly 09:00–18:00; Pre-Meeting Prep every 10 min for meetings within 60 min; End-of-Day Wrap weekdays 17:30; Weekly Review Friday 16:00.
- B2 Jobs must stay disabled until Slack delivery verified.
- B3 Routing must use `deliver`; prompts content-only, no placeholders.
- B4 Jobs must be recurring (no `repeat` on recurring schedules).
- B5 Each job manually triggered once must deliver to Gin's Slack DM.
- B6 Missing integration must yield "missing X; skipped Y".
- B7 Jobs must not act outside Cindy's routine-autonomy tier.
- B8 Urgent Monitor and Post-Meeting Follow-Up must not exist.

## Acceptance criteria

- [ ] B1 verified with fresh output.
- [ ] B2 verified with fresh output.
- [ ] B3 verified with fresh output.
- [ ] B4 verified with fresh output.
- [ ] B5 verified with fresh output.
- [ ] B6 verified with fresh output.
- [ ] B7 verified with fresh output.
- [ ] B8 verified with fresh output.
