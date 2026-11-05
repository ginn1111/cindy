---
status: approved
scope: CINDY-6
owner: gintary
---

# Spec — CINDY-6 Connect Cindy's restricted GitHub identity

Source: GitHub issue ginn1111/cindy#7 (parent #1); design `docs/plans/2026-11-05-cindy-design.md`.

## Problem

See issue #7. Depends on: CINDY-1.

## Preconditions

- External: Separate Cindy GitHub account with 2FA, Gin-controlled recovery, lowest useful org role, fine-grained token for approved repos.

## Scope

Cindy runtime `GH_TOKEN` (untracked), `env.sample`, `distribution.yaml`, Cindy `gh` config under her profile home.

## Non-goals

Gin's or gintary's GitHub credentials, repo content writes.

## Desired behavior

- B1 `gh auth status` under profile `cindy` must show Cindy's account.
- B2 Cindy must not use Gin's or gintary's credentials.
- B3 Token must be limited to approved repos with contents read-only.
- B4 Read of approved repo must succeed; unapproved repo must fail.
- B5 GitHub writes must produce approval request to Gin, not execute.
- B6 `git push --force` must be refused.
- B7 Token must stay untracked.

## Acceptance criteria

- [ ] B1 verified with fresh output.
- [ ] B2 verified with fresh output.
- [ ] B3 verified with fresh output.
- [ ] B4 verified with fresh output.
- [ ] B5 verified with fresh output.
- [ ] B6 verified with fresh output.
- [ ] B7 verified with fresh output.
