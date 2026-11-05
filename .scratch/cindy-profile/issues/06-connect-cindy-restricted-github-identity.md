# 06 — Connect Cindy's restricted GitHub identity

**What to build:** Cindy authenticates to GitHub with her own account and a fine-grained token limited to required repositories. She can read approved repositories. Repository contents stay read-only, and any issue or pull-request write requires Gin's approval.

**Blocked by:** 01 — Build installable Cindy core profile.

**External prerequisite:** A separate Cindy GitHub account exists with two-factor authentication, Gin-controlled recovery, an organization invitation at the lowest useful role, and a fine-grained token for the approved repositories.

**Status:** ready-for-agent

- [ ] Cindy's GitHub authentication status is verified with fresh output under Cindy's profile only.
- [ ] Gin's and gintary's GitHub credentials are not used by Cindy.
- [ ] Token scope is limited to required repositories; repository contents permission is read-only.
- [ ] Cindy reads an approved repository successfully.
- [ ] Access to an unapproved repository fails.
- [ ] Any issue comment, pull-request action, or other GitHub write produces an approval request to Gin and is not executed without approval.
- [ ] `git push --force` remains refused.
- [ ] Token remains untracked; the names-only sample documents required variables for this phase.
