# 02 — Connect Cindy's Google Workspace account

**What to build:** Cindy uses her own Google Workspace identity to read her own Gmail, create an unsent draft, and list her own calendar. Access is granted through OAuth scoped to Cindy's account only, with no domain-wide delegation and no access to Gin's mailbox.

**Blocked by:** 01 — Build installable Cindy core profile.

**External prerequisite:** A Workspace administrator creates Cindy's full user account and provides OAuth client credentials. Gin controls recovery methods; two-factor authentication is enabled and recovery codes are stored outside Hermes.

**Status:** ready-for-agent

- [ ] Cindy authenticates with her own Google account; no gintary or Gin credentials are used.
- [ ] Granted scopes cover only Cindy's own Gmail, Calendar, and Drive; domain-wide delegation is not configured.
- [ ] Credentials live only in Cindy's untracked runtime environment; the names-only sample documents required variables for this phase.
- [ ] Cindy lists recent messages from her own inbox with fresh output.
- [ ] Cindy creates a draft and the draft is verified unsent.
- [ ] Cindy lists events from her own calendar with fresh output.
- [ ] When Google credentials are missing, Cindy reports "missing Google credentials; skipped Google actions" instead of failing silently.
- [ ] No message is sent during verification without Gin's explicit approval.
