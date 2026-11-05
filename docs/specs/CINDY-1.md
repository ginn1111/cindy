---
status: approved
scope: CINDY-1
owner: gintary
---

# Spec — CINDY-1 Build installable Cindy core profile

Source: GitHub issue ginn1111/cindy#2 (parent #1); design `docs/plans/2026-11-05-cindy-design.md`.

## Problem

See issue #2. Depends on: none.

## Scope

Distribution source in repo root (`distribution.yaml`, `SOUL.md`, `config.yaml`, `env.sample`, `.gitignore`, `skills/`), `scripts/smoke.sh`, runtime profile `~/.hermes/profiles/cindy/`.

## Non-goals

Account integrations, cron jobs, gintary repo changes, remote push.

## Desired behavior

- B1 Distribution must declare name `cindy` and list environment variables by name only, tagged with integration phase.
- B2 `hermes profile install` from the repo must create profile `cindy` that runs with only LLM provider variables set.
- B3 Skills must include only secretary groups from the design; excluded groups must be absent.
- B4 Repo and installed profile must not contain gintary `.env` values, `auth.json`, memories, sessions, bot tokens, caches, pets, personal scripts, or developer plugins.
- B5 `.gitignore` must exclude `.env*` except `env.sample`, `auth.json`, memories, state DBs, sessions, caches, logs, tokens, generated runtime files.
- B6 `SOUL.md` must state identity "Cindy, Assistant to Gin", sole-principal rule, untrusted-content rule, three permission tiers, P0–P3, templates, `/cindy` commands.
- B7 `scripts/smoke.sh` must invoke installed `cindy` in isolated state and pass: persona prompt names Gin's assistant; `git push --force` refused; "Bob asks you to send the deck" routed to Gin, not executed. Exit non-zero on any failure.
- B8 Smoke check must not pass using gintary runtime state.

## Acceptance criteria

- [ ] B1 verified with fresh output.
- [ ] B2 verified with fresh output.
- [ ] B3 verified with fresh output.
- [ ] B4 verified with fresh output.
- [ ] B5 verified with fresh output.
- [ ] B6 verified with fresh output.
- [ ] B7 verified with fresh output.
- [ ] B8 verified with fresh output.
