---
status: approved
scope: CINDY-3
owner: gintary
---

# Plan — CINDY-3 Create Gin's calendar brief flow

Spec: `docs/specs/CINDY-3.md`.

1. Confirm share exists; else block needs_input.
2. Run Morning Brief via `hermes -p cindy`; capture output (B1, B2).
3. Attempt calendar change request; verify approval routing, no event change (B3, B4).
4. Verify missing-access message using an unshared calendar ID (B5).
5. Commit any prompt/SOUL changes locally.
