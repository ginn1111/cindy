# 07 — Run final isolation and recovery verification

**What to build:** Gin has end-to-end evidence that Cindy runs with separate identities, keeps secrets out of source control, routes scheduled output correctly, preserves approval boundaries, and can lose one integration without disabling unrelated integrations. Gin also has concise operator notes for stopping Cindy and rotating or revoking access.

**Blocked by:** 05 — Activate scheduled secretary workflows; 06 — Connect Cindy's restricted GitHub identity.

**Status:** ready-for-agent

- [ ] Core smoke check passes again with fresh output.
- [ ] Source control contains no secrets, environment values, authentication files, memories, sessions, runtime databases, logs, or tokens.
- [ ] Google, Slack, and GitHub checks each show Cindy's own identity.
- [ ] Gin-only authority and outside-request routing still hold in Slack.
- [ ] Gated actions still produce approve/edit/drop requests instead of execution.
- [ ] Revoking or removing one integration credential produces a clear missing-integration result while unrelated integrations keep working.
- [ ] Operator notes explain emergency stop, Google account suspension, token rotation, and per-integration revocation without exposing secret values.
- [ ] Final work is committed locally; nothing is pushed.
