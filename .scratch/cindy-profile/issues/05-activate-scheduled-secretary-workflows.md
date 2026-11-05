# 05 — Activate scheduled secretary workflows

**What to build:** Cindy runs the initial secretary jobs on UTC+7 schedules and delivers results to Gin through her own Slack identity. Each job produces useful output when integrations exist and reports missing integrations explicitly otherwise.

**Blocked by:** 02 — Connect Cindy's Google Workspace account; 03 — Create Gin's calendar brief flow; 04 — Connect Cindy's Slack identity and enforce request routing.

**Status:** ready-for-agent

- [ ] Five jobs exist: Morning Brief weekdays 09:00; Inbox Triage weekdays hourly 09:00–18:00; Pre-Meeting Prep every 10 minutes for meetings within 60 minutes; End-of-Day Wrap weekdays 17:30; Weekly Review Friday 16:00. Times are UTC+7.
- [ ] Jobs remain disabled until Slack delivery to Gin is verified.
- [ ] Delivery routing uses the scheduler's delivery setting; job prompts describe content only and contain no unresolved placeholders.
- [ ] Recurring jobs are configured as recurring, not one-shot.
- [ ] Each job is manually triggered once and its output arrives in Gin's Slack DM, verified with fresh evidence.
- [ ] A job with a missing integration reports "missing X; skipped Y" instead of failing silently.
- [ ] No job sends, edits, books, purchases, deletes, or writes externally outside Cindy's approved routine-autonomy tier.
- [ ] Urgent Monitor and Post-Meeting Follow-Up are not created.
