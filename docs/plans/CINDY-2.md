---
status: completed
scope: CINDY-2
owner: gintary
---

# Plan — CINDY-2 Connect Cindy's Google Workspace account

Spec: `docs/specs/CINDY-2.md`.

1. Confirm prerequisite account exists; else block needs_input.
2. Load `google-workspace` skill; run its OAuth setup under profile `cindy` with minimal scopes (B1, B2).
3. Add variable names to `env.sample` and `distribution.yaml` (B1).
4. Verify inbox list, draft-unsent, calendar list with fresh output (B3–B5).
5. Unset credentials temporarily; verify missing-credential message (B6).
6. Commit source changes locally.
