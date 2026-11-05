---
status: approved
scope: CINDY-7
owner: gintary
---

# Spec — CINDY-7 Run final isolation and recovery verification

Source: GitHub issue ginn1111/cindy#8 (parent #1); design `docs/plans/2026-11-05-cindy-design.md`.

## Problem

See issue #8. Depends on: CINDY-5, CINDY-6.

## Scope

Whole Cindy repo and runtime profile; `docs/operations.md` operator notes.

## Non-goals

New integrations, history rewrite, remote push.

## Desired behavior

- B1 `scripts/smoke.sh` must pass with fresh output.
- B2 Tracked files must contain no secrets, env values, auth files, memories, sessions, DBs, logs, tokens.
- B3 Google, Slack, GitHub checks must each show Cindy's identity.
- B4 Gin-only authority and outside-request routing must hold in Slack.
- B5 Gated actions must produce approve/edit/drop, not execute.
- B6 Revoking one integration credential must yield missing-integration result while others still work.
- B7 Operator notes must cover emergency stop, Google suspension, token rotation, per-integration revocation, with no secret values.

## Acceptance criteria

- [ ] B1 verified with fresh output.
- [ ] B2 verified with fresh output.
- [ ] B3 verified with fresh output.
- [ ] B4 verified with fresh output.
- [ ] B5 verified with fresh output.
- [ ] B6 verified with fresh output.
- [ ] B7 verified with fresh output.
