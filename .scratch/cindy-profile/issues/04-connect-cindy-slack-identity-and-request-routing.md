# 04 — Connect Cindy's Slack identity and enforce request routing

**What to build:** Cindy has her own Slack app identity. Gin can direct-message Cindy and receive replies. Messages from other workspace members are acknowledged, recorded, and routed to Gin with context and a suggested response instead of executed.

**Blocked by:** 01 — Build installable Cindy core profile.

**External prerequisite:** A separate Cindy Slack app is created and installed in the workspace; its credentials are issued to Cindy only.

**Status:** ready-for-agent

- [ ] Cindy uses a Slack app and tokens distinct from gintary's; gintary's messaging channels remain unchanged.
- [ ] Gin's Slack identity is the only allowlisted principal.
- [ ] Gin direct-messages Cindy and receives a reply with fresh evidence.
- [ ] A message from another member is acknowledged and forwarded to Gin with context and a suggested response, and the request is not executed.
- [ ] A message containing embedded instructions to disclose credentials, forward private files, or bypass approval is flagged to Gin and not executed.
- [ ] Slack credentials remain untracked; the names-only sample documents required variables for this phase.
