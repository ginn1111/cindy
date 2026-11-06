---
name: git-workflow
description: Common Git operations — rebase, stash management, conflict resolution, editor handling, divergence recovery, and push workflows.
---

# git-workflow

Common Git operations for Hermes profile repos and target-project repos.

## When to use

- Sync local branch with remote when divergent
- Rebase workflow (standard rebase, not interactive squash)
- Stash management (accumulated stashes, selective vs full stash)
- Rebase conflict resolution
- Redundant commit detection during rebase
- Push after rebase

## Rebase workflow

### Branch diverged from remote

```bash
git fetch origin
git stash              # stash ALL dirty files — bare, not selective
git rebase origin/main
```

**Pitfall:** `git stash -- <path>` only stashes staged changes for that path, not all unstaged changes. Rebase requires fully clean working tree. Use bare `git stash` when rebasing.

### Conflict resolution

1. Read conflicted file(s) with `read_file`
2. Resolve via `write_file` (rewrite with merged content)
3. `git add <resolved-files>`
4. If editor opens on `git rebase --continue`:
   - `GIT_EDITOR=true git rebase --continue` — bypass editor
   - Or `GIT_SEQUENCE_EDITOR=true GIT_EDITOR=true git rebase --edit-todo` to inspect remaining picks

### Redundant commit during rebase

A commit whose delta is already covered by a conflict resolution in an earlier pick will cause `git rebase --continue` to fail even after `git add`. Check staged changes:

```bash
git diff --cached --stat
```

If the commit's changes are already upstream, skip:

```bash
GIT_EDITOR=true git rebase --skip
```

### After successful rebase: push

Rebasing places local commits on top of remote → fast-forward push:

```bash
git push origin main
```

No `--force` needed for fast-forward. Use `--force-with-lease` only when history was rewritten and remote demands it.

## Stash management

### Clean accumulated stashes

Old stashes accumulate from repeated failed rebase attempts. Drop one at a time from the top:

```bash
git stash list            # view all
git stash drop stash@{0}  # drop sequentially
```

**Pitfall:** Dropping re-indexes. After `stash@{0}` is gone, the former `stash@{1}` becomes `stash@{0}`. Always drop from index 0.

### Stash pop with untracked file conflicts

`git stash pop` fails when pop restores untracked files that already exist. The stash is preserved and must be dropped explicitly:

```bash
git stash drop stash@{0}
```

## References

- `references/git-rebase-recovery.md` — session-specific walkthrough
