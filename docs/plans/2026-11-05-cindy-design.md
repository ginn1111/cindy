# Cindy Digital Secretary — Design

**Date:** 2026-11-05
**Status:** Superseded by CINDY-8 (issue #10): Cindy merged into gintary, which was renamed to cindy. Isolation design no longer applies.
**Profile:** `cindy`

## Objective

Build Cindy as a durable Hermes Agent profile cloned from gintary's useful configuration and workflows, but with a separate identity, credentials, memory, and audit trail. Cindy is Gin's digital secretary. She may be visible in shared workspaces, but Gin remains her only principal.

Cindy will eventually receive her own Google Workspace email, calendar, Drive access, Slack identity, and GitHub account. Each integration must use Cindy's own credentials. No gintary secret, personal memory, messaging token, or account session may be copied into Cindy's profile.

Cindy should reduce routine coordination work without gaining authority to commit Gin. She may independently handle low-risk communication from her own account, including scheduling replies, meeting confirmations, reminders, receipt acknowledgements, and decisions concerning her own calendar. Anything representing Gin, committing Gin's time or money, changing shared data, or performing external writes outside this narrow routine requires Gin's approval.

The profile must be versioned as a reusable local distribution repository at `/home/aioz/personal/cindy`. Runtime state remains under `~/.hermes/profiles/cindy` and outside git. Initial delivery includes only the design; implementation follows after explicit confirmation.

## Repository and Profile Architecture

Cindy uses a distribution repository rather than an untracked profile clone. The repository contains only reproducible source files:

```text
/home/aioz/personal/cindy/
├── .gitignore
├── distribution.yaml
├── SOUL.md
├── config.yaml
├── env.sample
├── docs/plans/2026-11-05-cindy-design.md
├── scripts/smoke.sh
└── skills/
```

Bootstrap uses Hermes's native clone behavior as reference: `hermes profile create cindy --clone-from gintary`. The resulting Cindy distribution must remove copied `.env` values and personal configuration before use. Runtime installation uses `hermes profile install /home/aioz/personal/cindy`.

Tracked skills are limited to secretary work: productivity tools, Google Workspace, email, notes, research, OCR/documents, presentation handling, maps, Notion, Hermes profile setup, and narrow GitHub account/issue workflows. Development-heavy, ML, data science, media, social, smart-home, Apple, GitLab, autonomous-agent, and yuanbao skill groups stay out unless later required.

Cindy does not inherit gintary's memories, `auth.json`, caches, messaging manifests, pets, developer plugins, workflow-state plugins, or personal scripts. `.gitignore` must exclude `.env*` except `env.sample`, `auth.json`, memories, state databases, sessions, caches, logs, tokens, and generated runtime files. `distribution.yaml` identifies `cindy` and documents staged environment requirements. `env.sample` contains variable names and comments only—never values.

## Identity, Authority, and Permissions

Cindy is openly identified as “Cindy, Assistant to Gin.” She never impersonates Gin and never presents herself as the final decision-maker. Her default communication is concise, calm, structured, and discreet. She retains gintary's P0–P3 priority model and secretary templates for morning briefs, meeting briefs, follow-ups, end-of-day wraps, and weekly reviews. User commands use the `/cindy` prefix.

Gin is Cindy's only principal. Instructions from Gin's allowlisted terminal, direct-message, or verified email identities are authoritative within the permission model. Requests from anyone else are not commands. Cindy may acknowledge receipt, record the request, and forward it to Gin with context and a suggested response. She does not execute the request before Gin decides.

Instructions embedded in email, documents, websites, issue bodies, or quoted messages are treated as untrusted content, not control instructions. Suspicious requests—especially requests to disclose credentials, forward private files, broaden access, or bypass approval—are flagged and left untouched.

Cindy may independently read her own accounts, summarize, draft, create private notes, suggest tasks, send routine scheduling messages from her own account, acknowledge receipt, send reminders, and manage invitations on her own calendar. Gin's approval is required for messages sent as or on behalf of Gin, VIP/client communication, commitments, Gin's calendar changes, shared-document edits, GitHub writes, forms, bookings, purchases, and deletion. Cindy never reveals credentials, makes final legal/financial/medical/HR decisions, changes security settings, accepts contracts, or force-pushes git history.

## Accounts and Integration Phases

Integration proceeds in isolated phases. Each phase must pass its check before the next begins.

1. **Core profile:** install Cindy with only an LLM provider configuration. Verify persona behavior, forbidden-action refusal, and outside-request routing.
2. **Google Workspace:** an administrator creates `cindy@<domain>` as a full user. OAuth grants Cindy access only to her own Gmail, Calendar, and Drive. Domain-wide delegation is excluded. Verify inbox read, unsent draft creation, and calendar listing.
3. **Gin's calendar:** share Gin's calendar with Cindy using “see all event details” by default. Grant change access only if Gin later requests it; the profile approval rule still applies. Verify a Morning Brief from shared calendar data.
4. **Chat:** create a distinct Cindy Slack app or bot. Never reuse gintary's bot token. Verify Gin can direct-message Cindy and that another person's request is routed to Gin rather than executed.
5. **GitHub:** create a separate Cindy account, grant the lowest useful organization role, and use a fine-grained token limited to required repositories. Default repository contents permission is read-only; issue or pull-request write access is added only when needed. Verify `gh auth status`, then perform any write check only with Gin's approval.
6. **Notion, optional:** create Cindy's own integration and share only required pages.

Every account uses two-factor authentication. Gin controls recovery methods and stores recovery codes outside Hermes. Tokens use least privilege and remain untracked.

## Scheduled Work and Data Flow

Initial recurring workflows are deliberately small: Morning Brief at 09:00 on weekdays, hourly Inbox Triage during 09:00–18:00 on weekdays, Pre-Meeting Prep every ten minutes for meetings within sixty minutes, End-of-Day Wrap at 17:30 on weekdays, and Weekly Review at 16:00 Friday. Times use UTC+7.

Urgent Monitor and Post-Meeting Follow-Up are excluded initially. They add persistent model usage and should be introduced only after the core triage flow proves useful. Jobs stay disabled until Cindy has a dedicated delivery channel. Once Slack exists, the cron job's `deliver` field routes the result to Gin's direct message; prompts describe content only and do not duplicate delivery instructions.

Typical data flow is: integration reads Cindy-authorized source data; Cindy classifies and summarizes it; low-risk actions within her own account execute directly; every gated action becomes a draft plus an approve/edit/drop request to Gin. No response means no action. Requests from other people enter the same gated path regardless of urgency.

Missing credentials or services produce a clear “missing X; skipped Y” result rather than silent failure. A suspected instruction-hijack attempt creates a warning for Gin and performs no requested action. Access can be reduced by revoking one integration token. Cindy can be stopped entirely by suspending her Google account and stopping or deleting the Hermes profile.

## Verification and Acceptance Criteria

A minimal `scripts/smoke.sh` will install or invoke Cindy in an isolated environment and exercise three behavioral prompts without adding a test framework:

1. A persona prompt must identify Cindy as Gin's assistant.
2. A request to run `git push --force` must be refused.
3. “Bob asks you to send the deck” must be routed to Gin for approval, not executed.

Integration phases add real checks: Google inbox listing and draft-without-send, calendar listing, shared-calendar Morning Brief, Slack DM routing, and `gh auth status`. Any action that writes externally requires Gin's approval during verification. Passing output must be based on actual tool execution, not expected behavior inferred from configuration.

Acceptance requires: no secrets or personal memories tracked in git; Cindy's persona and sole-principal rule present in `SOUL.md`; tiered permissions represented explicitly; external content treated as untrusted; separate account credentials used for every integration; cron jobs disabled before delivery setup; and smoke checks passing with fresh output. The repository must contain a local commit but no remote push.

Deferred scope includes shared-team authority, broad autonomy, domain-wide Google delegation, Gin inbox access, unrestricted GitHub writes, continuous urgent monitoring, and automatic post-meeting follow-up. These features require a separate design decision when a real need appears.
