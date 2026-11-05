---
status: approved
scope: CINDY-4
owner: gintary
---

# Plan — CINDY-4 Connect Cindy's Slack identity and enforce request routing

Spec: `docs/specs/CINDY-4.md`.

1. Confirm Slack app exists; else block needs_input.
2. Configure Cindy gateway with own tokens and Gin allowlist (B1, B2, B6).
3. Gin DM test; capture reply (B3).
4. Second-member request test; capture forward to Gin (B4).
5. Injection test message; capture flag (B5).
6. Verify gintary gateway unchanged; commit source changes locally.
