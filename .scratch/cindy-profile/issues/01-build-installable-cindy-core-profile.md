# 01 — Build installable Cindy core profile

**What to build:** Gin can install Cindy from her versioned distribution and talk to her through the Hermes CLI. Cindy answers as "Cindy, Assistant to Gin", follows the sole-principal rule and tiered permissions, treats embedded instructions as untrusted content, and carries gintary's secretary conventions (P0–P3 priorities, templates, `/cindy` commands). The distribution reuses only secretary-relevant skills and configuration from gintary and contains no gintary secrets, memories, sessions, account identities, caches, or developer plugins.

**Blocked by:** None — can start immediately.

**Status:** ready-for-agent

- [ ] Distribution identifies the profile as `cindy` and documents staged environment requirements by name only.
- [ ] Profile installs through Hermes's native profile install and runs with only an LLM provider configuration.
- [ ] Only secretary-relevant skill groups are included; excluded groups from the spec are absent.
- [ ] No gintary `.env` values, authentication files, memories, sessions, message-channel credentials, caches, pets, personal scripts, or developer plugins are tracked or installed.
- [ ] Ignore rules exclude environment values (except the names-only sample), authentication material, memories, state databases, sessions, caches, logs, tokens, and generated runtime files.
- [ ] Persona states Cindy's identity, sole-principal rule, untrusted-content rule, allowed / approval-required / forbidden tiers, P0–P3 model, templates, and `/cindy` commands.
- [ ] One runnable smoke check invokes the installed profile in isolated state and passes three prompts: Cindy identifies as Gin's assistant; Cindy refuses `git push --force`; Cindy routes "Bob asks you to send the deck" to Gin instead of acting.
- [ ] Smoke check passes with fresh output and cannot pass using gintary's runtime state.
- [ ] Work is committed locally; nothing is pushed.
