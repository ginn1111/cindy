# git-rebase-recovery — session walkthrough

Session: Update remote repo and remote distribution for gintary profile.

## Situation

- Local branch `main` diverged from `origin/main` (1 local commit, 1 remote commit)
- Both touched `distribution.yaml`: local removed `installed_at`, remote updated `description`
- Working tree had 13 modified files (unrelated: auth.json, cron/jobs.json, caches, metadata)

## Steps taken

### 1. Assess divergence

```bash
git log --oneline origin/main..HEAD   # what local has that remote doesn't
git log --oneline HEAD..origin/main    # what remote has that local doesn't
git merge-base HEAD origin/main       # last common ancestor
```

### 2. Merge remote change into local distribution.yaml

Applied the remote description change onto local file via `patch` (editing `description` field in `distribution.yaml`), then committed the merge:

```bash
git add distribution.yaml
git commit -m "chore: merge description update from remote v1.2.0, drop installed_at"
```

### 3. Stash and rebase

```bash
git stash                    # full stash (not selective — rebase needs clean tree)
git rebase origin/main
```

**Pitfall:** `git stash -- path` only covers staged changes for that file, not all dirty files. Bare `git stash` is safer.

### 4. Conflict resolution

Conflict in `distribution.yaml` during pick of the first local commit. Read file, resolved by rewriting merged content with `write_file`, then staged:

```bash
git add distribution.yaml
```

### 5. Editor trap on `git rebase --continue`

Running `git rebase --continue` opened `nvim` (GIT_EDITOR default), which hung in foreground shell. Solution:

```bash
GIT_EDITOR=true git rebase --continue
```

### 6. Redundant commit detection

Rebase had 2 picks to apply. After resolving first pick's conflict, second pick's delta was already upstream (its distribution.yaml change was identical to what was merged in step 1). `git rebase --continue` failed saying `You must edit all merge conflicts` despite `git diff --name-filter --diff-filter=U` showing no unresolved files.

**Fix:** Detect the redundant commit via `git show <commit> -- distribution.yaml`, confirm it's already applied, then skip:

```bash
GIT_EDITOR=true git rebase --skip
```

Output: `dropping d33c278... chore: merge description update from remote v1.2.0, drop installed_at -- patch contents already upstream`

### 7. Push

```bash
git push origin main
# → Everything up-to-date
```

### 8. Stash cleanup

Stash pop failed because stash had untracked files that already existed in working tree. Dropped stale stashes sequentially:

```bash
git stash drop stash@{0}   # repeat for each stale entry
```

**Pitfall:** After dropping stash@{0}, the former stash@{1} becomes stash@{0}. Always drop from index 0.

## Key lessons

| Situation | Solution |
|---|---|
| Rebase needs clean tree | `git stash` (full) — not selective |
| Editor opens on continue | `GIT_EDITOR=true git rebase --continue` |
| Rebase won't continue after resolving | Check if next pick is redundant → `git rebase --skip` |
| Stash pop fails with existing files | Drop manually, do not force pop |
| Stale stashes accumulate | List with `git stash list`, drop from stash@{0} sequentially |
