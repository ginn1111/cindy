---
status: approved
scope: CINDY-3
owner: gintary
---

# Spec — CINDY-3 Create Gin's calendar brief flow

Source: GitHub issue ginn1111/cindy#4 (parent #1); design `docs/plans/2026-11-05-cindy-design.md`.

## Problem

See issue #4. Depends on: CINDY-2.

## Preconditions

- External: Gin shares calendar with Cindy at "see all event details".

## Scope

Cindy Morning Brief behavior in `SOUL.md`/skill prompts; read-only access to Gin's shared calendar.

## Non-goals

Calendar write access, cron scheduling (CINDY-5).

## Desired behavior

- B1 Cindy must read today's events from Gin's shared calendar.
- B2 Cindy must produce a Morning Brief with sections: calendar today, top priorities, follow-ups due, meeting prep needed, risks/conflicts, recommended first action.
- B3 Cindy must not create, edit, accept, decline, or delete Gin's events.
- B4 Requests to change Gin's calendar must produce draft + approve/edit/drop request.
- B5 Missing access must yield "missing Gin calendar access; skipped Morning Brief calendar section".

## Acceptance criteria

- [ ] B1 verified with fresh output.
- [ ] B2 verified with fresh output.
- [ ] B3 verified with fresh output.
- [ ] B4 verified with fresh output.
- [ ] B5 verified with fresh output.
