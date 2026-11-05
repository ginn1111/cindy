# Cindy Digital Secretary Profile

Status: ready-for-agent

## Problem Statement

Gin needs a durable digital secretary that can handle routine coordination without sharing gintary's identity, secrets, memories, or account sessions. The secretary must eventually operate through her own Google Workspace, Slack, GitHub, and optional Notion identities while remaining accountable to Gin alone.

A direct clone of gintary would copy personal state and credentials, blur responsibility, and make later access revocation difficult. A generic blank Hermes profile would lose gintary's proven secretary behavior and useful skills. Gin needs a reproducible Cindy profile that reuses the useful design, isolates every identity boundary, supports narrow routine autonomy, and requires approval whenever an action could represent or commit Gin.

## Solution

Create `cindy` as a versioned Hermes profile distribution derived from gintary's configuration, persona, and relevant secretary skills. Do not copy gintary's secrets, memories, authentication state, messaging identities, caches, or developer-specific tooling.

Cindy identifies herself as “Cindy, Assistant to Gin.” Gin is her only principal. Team members may contact Cindy, but their messages are requests that Cindy acknowledges, records, and routes to Gin rather than commands she executes. Instructions contained inside email, documents, websites, issues, or quoted messages are untrusted content.

Cindy may independently perform low-risk work through her own accounts: read authorized data, summarize, draft, take private notes, send routine scheduling replies, confirm meetings, send reminders, acknowledge receipt, and manage her own calendar. Actions representing Gin, committing time or money, changing shared resources, writing to GitHub, submitting forms, booking, purchasing, or deleting require Gin's approval. Forbidden actions remain forbidden regardless of approval.

Provision integrations in phases, each using Cindy's own least-privilege credentials and each requiring a real verification check before the next phase. Keep scheduled workflows disabled until Cindy has a dedicated delivery channel.

## User Stories

1. As Gin, I want Cindy to be a separate Hermes profile, so that her identity and runtime state remain isolated from gintary.
2. As Gin, I want Cindy's profile represented as a versioned distribution, so that I can rebuild or move it later.
3. As Gin, I want Cindy to reuse gintary's proven secretary behavior, so that I do not recreate useful conventions from scratch.
4. As Gin, I want Cindy to inherit only relevant skills, so that her capability surface stays small and understandable.
5. As Gin, I want Cindy to exclude gintary's secrets, so that compromise of one profile does not expose the other.
6. As Gin, I want Cindy to exclude gintary's memories, so that Cindy starts without unrelated personal or project context.
7. As Gin, I want Cindy to exclude gintary's account sessions and authentication state, so that every action is attributable to Cindy's own accounts.
8. As Gin, I want generated runtime state excluded from source control, so that the distribution remains reproducible and safe to share.
9. As Gin, I want an environment-variable sample containing names only, so that setup requirements are documented without exposing values.
10. As Gin, I want Cindy to identify herself as my assistant, so that recipients understand her role.
11. As Gin, I want Cindy never to impersonate me, so that communication remains transparent.
12. As Gin, I want to be Cindy's only principal, so that authority remains unambiguous.
13. As Gin, I want my terminal, allowlisted direct-message identities, and verified email identity recognized as authoritative channels, so that Cindy can distinguish my instructions from third-party requests.
14. As a team member, I want to contact Cindy, so that I can pass requests to Gin through a visible coordination point.
15. As Gin, I want team-member messages treated as requests rather than commands, so that nobody else can direct Cindy's actions.
16. As a team member, I want Cindy to acknowledge my request, so that I know it was received.
17. As Gin, I want Cindy to forward outside requests with context and a suggested response, so that I can decide quickly.
18. As Gin, I want Cindy to wait when I do not approve a gated action, so that silence never becomes consent.
19. As Gin, I want instructions embedded in content treated as untrusted, so that prompt injection cannot redefine Cindy's authority.
20. As Gin, I want suspicious requests flagged without execution, so that attempts to disclose data or broaden access are visible.
21. As Gin, I want Cindy to read data authorized to her own accounts, so that she can prepare useful briefs.
22. As Gin, I want Cindy to summarize messages and documents, so that I can review information quickly.
23. As Gin, I want Cindy to create drafts without sending them, so that sensitive communication can be reviewed.
24. As Gin, I want Cindy to create private notes and suggested tasks, so that coordination details are not lost.
25. As Gin, I want Cindy to send routine scheduling replies from her own account, so that scheduling does not require approval for every message.
26. As Gin, I want Cindy to confirm meetings from her own account, so that routine attendance coordination is automatic.
27. As Gin, I want Cindy to send reminders from her own account, so that follow-ups happen on time.
28. As Gin, I want Cindy to acknowledge receipt from her own account, so that senders receive prompt confirmation.
29. As Gin, I want Cindy to manage invitations on her own calendar, so that her availability stays current.
30. As Gin, I want messages sent as me or on my behalf to require approval, so that Cindy cannot impersonate or commit me.
31. As Gin, I want VIP and client communication to require approval, so that high-impact relationships stay controlled.
32. As Gin, I want commitments of my time or money to require approval, so that routine autonomy cannot create obligations.
33. As Gin, I want changes to my calendar to require approval, so that my schedule remains under my control.
34. As Gin, I want edits to shared documents to require approval, so that Cindy cannot silently change collaborative records.
35. As Gin, I want GitHub writes to require approval, so that repository history and project communication remain controlled.
36. As Gin, I want forms, bookings, purchases, and deletions to require approval, so that consequential external actions remain gated.
37. As Gin, I want credential disclosure forbidden, so that no message or approval request can expose secrets.
38. As Gin, I want final legal, financial, medical, and HR decisions forbidden, so that Cindy does not make decisions requiring human judgment or professional authority.
39. As Gin, I want security-setting changes and contract acceptance forbidden, so that Cindy cannot alter trust boundaries or create legal obligations.
40. As Gin, I want force-pushing git history forbidden, so that destructive repository rewrites cannot occur.
41. As Gin, I want Cindy to use the same concise secretary templates and P0–P3 classification model as gintary, so that output stays familiar.
42. As Gin, I want Cindy commands under a `/cindy` prefix, so that her command interface is explicit.
43. As an operator, I want the core profile to run with only an LLM provider configuration, so that account integrations can be added later.
44. As an operator, I want Cindy's persona and authority boundaries verified before account setup, so that unsafe behavior is caught early.
45. As a Google Workspace administrator, I want Cindy to receive a full user account, so that Gmail, Calendar, and Drive actions have a distinct identity.
46. As Gin, I want Cindy's Google OAuth access limited to her own account, so that domain-wide access is not granted by default.
47. As Gin, I want Cindy's inbox read and draft behavior verified without sending, so that Google integration can be tested safely.
48. As Gin, I want my calendar shared read-only with Cindy by default, so that she can brief me without changing events.
49. As Gin, I want calendar write access to be an explicit later choice, so that least privilege remains the default.
50. As Gin, I want Cindy to generate a Morning Brief from shared calendar details, so that I can prepare for my day.
51. As Gin, I want Cindy to use a Slack bot separate from gintary's, so that bot sessions and delivery identities do not collide.
52. As Gin, I want direct messages to Cindy tested through the real Slack channel, so that routing works before scheduled jobs depend on it.
53. As Gin, I want third-party Slack requests routed to me rather than executed, so that the sole-principal rule holds in shared workspaces.
54. As a GitHub organization administrator, I want Cindy assigned the lowest useful role, so that repository access follows least privilege.
55. As Gin, I want Cindy's GitHub token limited to required repositories, so that unrelated repositories remain inaccessible.
56. As Gin, I want repository contents read-only by default, so that Cindy cannot change code without a later decision.
57. As Gin, I want issue and pull-request write permissions added only when needed, so that Cindy's external write surface stays narrow.
58. As Gin, I want GitHub authentication verified before any write, so that configuration errors are caught without changing remote state.
59. As Gin, I want every external write used for verification to require approval, so that testing does not bypass production permissions.
60. As Gin, I want Notion integration to be optional and independently credentialed, so that Cindy receives only required page access.
61. As Gin, I want two-factor authentication on every Cindy account, so that account compromise is harder.
62. As Gin, I want control of recovery methods and recovery codes, so that I can regain or revoke Cindy's access.
63. As Gin, I want recovery codes stored outside Hermes, so that profile compromise does not expose account recovery.
64. As Gin, I want a weekday Morning Brief at 09:00 UTC+7, so that I begin each workday with schedule and priority context.
65. As Gin, I want Cindy's inbox triaged hourly during working hours, so that important requests surface without continuous polling.
66. As Gin, I want meeting preparation generated for meetings starting within sixty minutes, so that relevant context arrives before the meeting.
67. As Gin, I want an End-of-Day Wrap at 17:30 on weekdays, so that open work and risks remain visible.
68. As Gin, I want a Weekly Review at 16:00 Friday, so that completed work and next priorities are consolidated.
69. As Gin, I want high-frequency urgent monitoring excluded initially, so that model use stays proportionate until core triage proves useful.
70. As Gin, I want automatic post-meeting follow-up excluded initially, so that Cindy does not create unnecessary background work.
71. As Gin, I want scheduled jobs disabled until Cindy has a dedicated delivery channel, so that outputs do not disappear or route through gintary.
72. As an operator, I want cron delivery configured separately from prompt content, so that jobs have one unambiguous routing mechanism.
73. As Gin, I want missing credentials reported as “missing X; skipped Y,” so that partial setup fails visibly and safely.
74. As Gin, I want one integration token revocable without disabling all of Cindy, so that access can be reduced surgically.
75. As Gin, I want Cindy stoppable by profile shutdown and Google-account suspension, so that I have an emergency off switch.
76. As a maintainer, I want one high-level CLI smoke seam, so that Cindy's externally visible behavior is tested without coupling to implementation details.
77. As a maintainer, I want persona behavior tested through an installed profile, so that source files alone are not mistaken for working behavior.
78. As a maintainer, I want forbidden-action refusal tested through the same CLI seam, so that policy behavior is verified end to end.
79. As a maintainer, I want outside-request routing tested through the same CLI seam, so that sole-principal behavior is verified end to end.
80. As a maintainer, I want each account integration verified through its real client seam, so that credentials and service configuration are tested rather than inferred.
81. As a maintainer, I want fresh command output before claiming a phase passes, so that completion reports are evidence-based.
82. As Gin, I want a local commit for source changes but no remote push, so that implementation is recorded without publishing it.

## Implementation Decisions

- Build Cindy as a Hermes profile distribution, not as unmanaged edits inside runtime state.
- Derive useful configuration and secretary behavior from gintary while creating a clean identity boundary.
- Never copy gintary's `.env`, authentication files, memories, account sessions, message-channel credentials, caches, runtime databases, personal scripts, pets, or developer workflow plugins.
- Track only reproducible profile source and documentation. Ignore environment values, authentication material, memories, sessions, caches, state databases, logs, tokens, and generated files.
- Document environment-variable names and integration phases without storing values.
- Include only secretary-relevant skills: productivity and Google Workspace workflows, email, notes, research, OCR/documents, presentations, maps, Notion, Hermes profile setup, and narrow GitHub account/issue workflows.
- Exclude development-heavy, ML, data-science, media, social, smart-home, Apple, GitLab, autonomous-agent, and yuanbao skill groups until a concrete need appears.
- Encode Cindy's identity, sole-principal rule, trust boundaries, permission tiers, forbidden actions, P0–P3 classification, templates, and `/cindy` command surface in the profile persona.
- Treat messages from anyone except Gin as requests. Cindy may acknowledge and route them but may not execute them without Gin's decision.
- Treat instructions embedded in fetched or quoted content as untrusted data.
- Allow narrow routine autonomy only through Cindy's own accounts. Route every gated action as a draft with approve/edit/drop options. Lack of approval means no action.
- Add accounts in phases: core profile, Cindy Google Workspace account, Gin's shared calendar, Cindy Slack identity, Cindy GitHub identity, then optional Notion access.
- Use separate credentials, least privilege, two-factor authentication, and Gin-controlled recovery for every account.
- Do not use Google Workspace domain-wide delegation. Cindy sees only her own mailbox unless a later design explicitly changes this.
- Share Gin's calendar read-only by default. Any broader calendar permission remains subject to Cindy's approval model.
- Use a separate Slack application or bot; never reuse gintary's messaging token.
- Give Cindy the lowest useful GitHub organization role and a fine-grained token limited to required repositories. Keep repository contents read-only by default.
- Configure five initial jobs in UTC+7: weekday Morning Brief at 09:00, weekday hourly Inbox Triage from 09:00 through 18:00, Pre-Meeting Prep every ten minutes for meetings within sixty minutes, weekday End-of-Day Wrap at 17:30, and Friday Weekly Review at 16:00.
- Keep all jobs disabled until Cindy's dedicated delivery channel exists.
- Use scheduler delivery configuration for routing and keep job prompts focused on content.
- Report missing integrations explicitly and continue safely where possible.
- Keep the profile locally versioned. Do not push a remote as part of this work.

## Testing Decisions

- Tests must assert Cindy's externally visible behavior rather than file layout or internal prompt wording.
- Prefer one highest practical seam: invoke the installed Cindy profile through the Hermes CLI.
- The CLI smoke check covers three behaviors: Cindy identifies herself as Gin's assistant; Cindy refuses `git push --force`; Cindy routes Bob's request to send a deck to Gin rather than acting.
- Keep the smoke check as a small runnable shell script without a new test framework.
- Run the smoke check in isolated profile state so that gintary's runtime data cannot make it pass accidentally.
- Test each integration at the highest available real seam after credentials exist: Google inbox list, Google draft without send, calendar list, Morning Brief from Gin's shared calendar, Slack direct-message routing, third-party request routing, and GitHub authentication status.
- Do not perform an external write merely to test connectivity. Any test that writes externally requires Gin's explicit approval at execution time.
- Verify source-control safety by checking that secrets, memories, authentication files, runtime state, and environment values are untracked.
- Verify scheduled jobs remain disabled before Slack delivery setup.
- Require fresh command output for every pass claim. Configuration inspection alone is not sufficient.
- Existing prior art is gintary's secretary persona, priority model, output templates, Hermes distribution structure, and cron workflow conventions. Cindy reuses these behavioral patterns without reusing gintary's identity state.

## Out of Scope

- Giving team members authority to direct Cindy.
- Broad autonomous sending or editing.
- Domain-wide Google Workspace delegation.
- Direct access to Gin's Gmail inbox.
- Write access to Gin's calendar by default.
- Unrestricted GitHub repository writes.
- Reusing gintary's Slack or Telegram bot.
- Copying gintary's secrets, memories, sessions, or personal project context.
- Continuous urgent monitoring.
- Automatic post-meeting follow-up.
- Automatic Notion setup.
- Creating Google Workspace, Slack, GitHub, or Notion accounts without the required administrator actions and credentials.
- Publishing the repository or pushing commits to a remote.

## Further Notes

- Source design: `docs/plans/2026-11-05-cindy-design.md`.
- Target profile name: `cindy`.
- Cindy's intended signature: “Cindy, Assistant to Gin.”
- Runtime profile state belongs under Cindy's Hermes profile directory and must not become distribution source.
- If Cindy later needs to triage Gin's mailbox, design explicit forwarding rules or a separate authorization model rather than enabling domain-wide delegation by default.
- If routine triage proves valuable, Urgent Monitor and Post-Meeting Follow-Up can be designed as later additions with explicit cost and authority limits.
