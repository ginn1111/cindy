---
status: approved
scope: CINDY-4
owner: gintary
---

# Spec — CINDY-4 Connect Cindy's Slack identity and enforce request routing

Source: GitHub issue ginn1111/cindy#5 (parent #1); design `docs/plans/2026-11-05-cindy-design.md`.

## Problem

See issue #5. Depends on: CINDY-1.

## Preconditions

- External: Cindy Slack app installed; tokens held by Cindy only. Gin decision 2026-11-05: existing gintary app moved to Cindy (gintary Slack disabled, tokens removed from gintary .env).

## Scope

Cindy runtime `.env` Slack variables (untracked), `env.sample`, `distribution.yaml`, Cindy gateway/platform config.

## Non-goals

gintary Slack/Telegram config, cron delivery (CINDY-5).

## Desired behavior

- B1 Cindy must use Slack tokens distinct from gintary's.
- B2 Only Gin's Slack identity must be allowlisted as principal.
- B3 Gin DM must receive a reply.
- B4 Other-member request must be acknowledged and forwarded to Gin with context and suggested response; not executed.
- B5 Embedded instructions to disclose credentials, forward private files, or bypass approval must be flagged, not executed.
- B6 Slack credentials must stay untracked.

## Acceptance criteria

- [ ] B1 verified with fresh output.
- [ ] B2 verified with fresh output.
- [ ] B3 verified with fresh output.
- [ ] B4 verified with fresh output.
- [ ] B5 verified with fresh output.
- [ ] B6 verified with fresh output.
