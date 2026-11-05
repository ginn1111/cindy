---
status: approved
scope: CINDY-6
owner: gintary
---

# Plan — CINDY-6 Connect Cindy's restricted GitHub identity

Spec: `docs/specs/CINDY-6.md`.

1. Confirm account and token exist; else block needs_input.
2. Set `GH_TOKEN` in Cindy `.env`; verify `gh auth status` (B1, B2, B7).
3. Read approved repo; attempt unapproved repo (B3, B4).
4. Ask Cindy to comment on an issue; verify approval request (B5).
5. Re-run smoke force-push refusal (B6). Commit source changes locally.
