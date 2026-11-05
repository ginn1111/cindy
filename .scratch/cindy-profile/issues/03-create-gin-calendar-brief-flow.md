# 03 — Create Gin's calendar brief flow

**What to build:** Cindy reads Gin's shared calendar through her own Google identity and produces a Morning Brief for Gin without changing any of Gin's events. Calendar write permission stays off by default.

**Blocked by:** 02 — Connect Cindy's Google Workspace account.

**External prerequisite:** Gin shares his calendar with Cindy using "see all event details".

**Status:** ready-for-agent

- [ ] Cindy reads today's events from Gin's shared calendar with fresh output.
- [ ] Cindy produces a Morning Brief using the secretary template: calendar today, top priorities, follow-ups due, meeting prep needed, risks or conflicts, and recommended first action.
- [ ] Cindy cannot create, edit, accept, decline, or delete events on Gin's calendar with the default share.
- [ ] A request to change Gin's calendar produces a draft and an approve/edit/drop request to Gin, not a change.
- [ ] Missing calendar access produces a clear "missing Gin calendar access; skipped Morning Brief calendar section" result.
