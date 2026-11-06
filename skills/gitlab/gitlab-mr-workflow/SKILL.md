---
name: gitlab-mr-workflow
description: "GitLab MR lifecycle: branch, commit, open, CI, merge, using glab CLI."
version: 1.0.0
author: gintary
platforms: [linux, macos]
metadata:
  hermes:
    tags: [GitLab, Merge-Requests, CI/CD, Git, glab]
    related_skills: [github-pr-workflow]
---

# GitLab Merge Request Workflow

Complete guide for managing MR lifecycle with `glab` CLI.

## Prerequisites

- `glab` CLI installed (`command -v glab`)
- Authenticated: `glab auth status`
- Inside a git repo with a GitLab remote

### Validate Remote is GitLab

```bash
REMOTE_URL=$(git remote get-url origin)
if ! echo "$REMOTE_URL" | grep -qiE "gitlab|\.git$"; then
  echo "ERROR: Remote does not look like GitLab"
  exit 1
fi
echo "Remote is GitLab — OK"
```

### Extract Owner/Repo for API calls

```bash
REMOTE_URL=$(git remote get-url origin)
# GitLab path format: git@gitlab.internal:group/subgroup/project.git
OWNER_REPO=$(echo "$REMOTE_URL" | sed -E 's|.*[/:]||; s|\.git$||')
echo "Project: $OWNER_REPO"
```

## Auth & Token Scopes

`glab auth status` to verify. Key scopes needed:

| Operation | Required Scope |
|-----------|----------------|
| View MRs | `read_api` |
| Create MR | `write_repository` (minimum) or `api` (full) |
| Merge MR | `write_repository` or `api` |

⚠️ `read_api` alone will 403 on MR creation with `insufficient_scope`.

If token needs upgrade: GitLab UI → Settings → Access Tokens → personal access token → check `write_repository` + `api`.

`glab` stores config at `~/.config/glab-cli/config.yml` (Snap: `~/snap/glab/*/.config/glab-cli/config.yml`).

---

## 1. Branch Creation

Standard git — same as any platform:

```bash
git fetch origin
git checkout aioz-develop && git pull origin aioz-develop
git checkout -b ci/merge-send-transfer
```

## 2. Making Commits

```bash
git add <files>
git commit -m "type(scope): short description

Longer body if needed"
```

## 3. Push Branch

```bash
git push -u origin HEAD
```

## 4. Create MR

### Minimal

```bash
glab mr create \
  --title "Descriptive title" \
  --description "## Summary\n\nWhat changed\n\n## Test Plan\n- [ ] CI passes" \
  --target-branch aioz-develop \
  --remove-source-branch \
  --label "merge"
```

### Using fill (auto-populate from commits)

```bash
glab mr create --fill --target-branch aioz-develop
```

`--fill` sets `push` to `true` and pushes the branch automatically.
Add `--fill-commit-body` to use full commit bodies in description (for multi-commit MRs).

### Key flag differences from gh CLI

| Action | `gh` | `glab` |
|--------|------|--------|
| Target branch | `--base BRANCH` | `--target-branch BRANCH` |
| Use current branch | (default) | (default — no `--current-branch` flag) |
| Draft | `--draft` | `--draft` |
| Fill from commits | N/A | `--fill` |
| Labels | `--label` | `--label` |
| Recover failed MR | N/A | `--recover` (from saved `mr.json`) |

### Recover from failed creation

`glab` writes a recovery file on failure:
```
/home/aioz/snap/glab/*/.config/glab-cli/recover/<namespace>/<project>/mr.json
```

Fix the issue (token scope, connectivity), then retry:
```bash
glab mr create --recover
```

---

## 5. Monitoring CI

```bash
# List MRs
glab mr list

# View MR details
glab mr view <MR-ID>

# Check pipelines
glab ci status
```

---

## 6. Merge MR

```bash
# Squash merge + delete source branch
glab mr merge <MR-ID> --squash --remove-source-branch

# Enable auto-merge (when all checks pass)
glab mr update <MR-ID> --merge-when-pipeline-succeeds
```

---

## 7. Complete MR Script

```bash
BRANCH=$(git branch --show-current)

glab mr create \
  --title "Merge $BRANCH into aioz-develop" \
  --description "## Summary\n\n$(git log --oneline origin/aioz-develop..HEAD --no-merges | sed 's/^/- /')\n\n## Test Plan\n- [ ] CI passes" \
  --target-branch aioz-develop \
  --remove-source-branch \
  --label "merge"
```

---

## Quick Reference

| Action | Command |
|--------|---------|
| List MRs | `glab mr list` |
| View MR | `glab mr view <ID>` |
| Create MR | `glab mr create --title "..." --target-branch X` |
| Create MR (fill) | `glab mr create --fill --target-branch X` |
| Merge | `glab mr merge <ID> --squash --remove-source-branch` |
| Close | `glab mr close <ID>` |
| Note | `glab mr note <ID> -m "comment"` |
| Checkout MR | `glab mr checkout <ID>` |
| Pipeline status | `glab ci status` |
| Recover | `glab mr create --recover` |

## Pitfalls

- `--current-branch` does NOT exist in glab (unlike gh). Source branch defaults to the current branch.
- `--base` is a gh flag. glab uses `--target-branch`.
- Token with only `read_api` scope will 403 on MR create. Upgrade to `write_repository` or `api`.
- For self-hosted GitLab, ensure `glab auth` configured with correct instance URL (`glab auth login --hostname gitlab.internal`).
- `--remove-source-branch` only works if source branch exists in remote.
