---
status: approved
scope: CINDY-8
owner: gintary
---

# Plan — CINDY-8

Spec: `docs/specs/CINDY-8.md` (issue #10).

1. Export both profiles: `hermes profile export gintary|cindy` to `~/backups/`.
2. Baseline commit of pending changes in the gintary profile repo (local only).
3. Merge in gintary profile, one commit per area: SOUL, config, skills, manifests. `.env` and Google OAuth files are untracked (mode 600).
4. Write `scripts/merge-into-gintary.sh` runbook here: stop runtimes, delete cindy, rename gintary to cindy, fix ginb SOUL and Kanban assignees, restart gateway.
5. Gin runs the runbook from a plain shell (not from a gintary session).
6. Verify per spec Testing Decisions via `hermes -p cindy`.
7. Archive this repo: README note, design doc marked superseded, close #1–#8 as superseded (approval needed).
