---
status: approved
scope: CINDY-1
owner: gintary
---

# Plan — CINDY-1 Build installable Cindy core profile

Spec: `docs/specs/CINDY-1.md`.

1. Inspect gintary `config.yaml`, `SOUL.md`, `distribution.yaml`, skills tree; list personal/secret fields to strip (B4).
2. Bootstrap with `hermes profile create cindy --clone-from gintary` into a scratch name or inspect output; copy only allowed source into repo (B1, B3, B5).
3. Write `SOUL.md` from design permission model (B6); write `env.sample` names only (B1).
4. Write `scripts/smoke.sh` first; run it against uninstalled profile and confirm it fails (B7).
5. `hermes profile install /home/aioz/personal/cindy`; set LLM vars in Cindy `.env` only (B2).
6. Run `scripts/smoke.sh`; confirm pass with fresh output (B7, B8).
7. Secret scan: `git ls-files` and grep for token patterns; confirm none (B4).
8. Commit locally; do not push.
