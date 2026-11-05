---
status: completed
scope: CINDY-2
owner: gintary
---

# Spec — CINDY-2 Connect Cindy's Google Workspace account

Source: GitHub issue ginn1111/cindy#3 (parent #1); design `docs/plans/2026-11-05-cindy-design.md`.

## Problem

See issue #3. Depends on: CINDY-1.

## Preconditions

- External: Workspace admin creates `cindy@<domain>` full user + OAuth client; 2FA on; Gin holds recovery codes outside Hermes.

## Scope

Cindy runtime `.env` (untracked), `env.sample`, `distribution.yaml` env list, Google Workspace skill configuration, `scripts/smoke.sh` if a Google check is added.

## Non-goals

Domain-wide delegation, Gin mailbox access, sending email, calendar on Gin's account.

## Desired behavior

- B1 Cindy must authenticate as her own Google user only.
- B2 OAuth grant must belong to Cindy's own user only; no domain-wide delegation. Scope set: Gmail (read/modify/send), Calendar, Drive, Contacts read-only, Sheets, Docs — Gin decision 2026-11-05 ("take all"); gated actions stay governed by SOUL.md approval tiers.
- B3 Cindy must list recent messages from her inbox.
- B4 Cindy must create a draft that remains unsent.
- B5 Cindy must list events on her own calendar.
- B6 Missing Google credentials must yield "missing Google credentials; skipped Google actions".
- B7 No send during verification without Gin approval.

## Acceptance criteria

- [x] B1 verified with fresh output.
- [x] B2 verified with fresh output.
- [x] B3 verified with fresh output.
- [x] B4 verified with fresh output.
- [x] B5 verified with fresh output.
- [x] B6 verified with fresh output.
- [x] B7 verified with fresh output.
