---
status: approved
scope: CINDY-5
owner: gintary
---

# Plan — CINDY-5 Activate scheduled secretary workflows

Spec: `docs/specs/CINDY-5.md`.

1. Load `hermes-profile-setup` skill; create five jobs disabled with UTC cron equivalents (B1, B2, B4).
2. Review prompts for placeholders and delivery text (B3, B7).
3. Enable and manually run each job; capture Slack delivery (B5).
4. Run one job with a credential removed; capture missing message (B6).
5. List jobs; confirm excluded jobs absent (B8).
