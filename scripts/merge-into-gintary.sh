#!/usr/bin/env bash
# CINDY-8 runbook: delete old isolated cindy profile, rename gintary to cindy, fix references.
# Run from a plain shell, NOT from a gintary/cindy Hermes session. Stops on first error.
# Rollback: hermes profile import ~/backups/{gintary,cindy}-premerge-20261106.tar.gz
#           then restore secrets from ~/backups/secrets-premerge-20261106.tar.gz
set -euo pipefail
P=$HOME/.hermes/profiles
step() { printf '\n== %s\n' "$*"; }

[ -z "${HERMES_PROFILE:-}${HERMES_HOME:-}" ] || { echo "Run outside Hermes (HERMES_PROFILE/HERMES_HOME set)"; exit 1; }
# Detached launch from inside a session (survives gateway stop):
#   systemd-run --user --unit cindy-merge -E HOME=$HOME -E PATH=$PATH -E CONFIRM=YES \
#     bash -c 'bash /home/aioz/personal/cindy/scripts/merge-into-gintary.sh > ~/backups/cindy-merge.log 2>&1'
[ -d "$P/gintary" ] && [ -d "$P/cindy" ] || { echo "expect both $P/gintary and $P/cindy"; exit 1; }
ls ~/backups/gintary-premerge-*.tar.gz ~/backups/cindy-premerge-*.tar.gz ~/backups/secrets-premerge-*.tar.gz >/dev/null

step "Running gintary kanban workers (let them finish or reclaim first)"
for b in $(hermes kanban boards list --json 2>/dev/null | python3 -c 'import json,sys;print(" ".join(x["slug"] for x in json.load(sys.stdin)))'); do
  hermes kanban --board "$b" list --assignee gintary --status running 2>/dev/null | grep -E '^\S+ +t_' || true
done
[ "${CONFIRM:-}" = YES ] || { read -rp "Close all gintary TUI/desktop sessions and the dashboard, then type YES: " ok; [ "$ok" = YES ]; }

step "Stop dashboard (pid serving --open-profile gintary)"
pkill -f 'hermes_cli.main .*dashboard .*--open-profile gintary' || echo "no dashboard running"

step "Delete old cindy profile (irreversible apart from ~/backups export)"
hermes profile delete cindy -y

step "Rename gintary -> cindy"
hermes profile rename gintary cindy || { echo "rename failed; if dir moved, run: hermes profile migrate-identity gintary cindy"; exit 1; }

step "Fix in-profile references"
cd "$P/cindy"
sed -i 's#profiles/gintary/#profiles/cindy/#g' config.yaml skills/devops/hermes-profile-setup/references/data-fetching-cron-pattern.md
sed -i 's#^        - name: gintary$#        - name: cindy#' config.yaml
sed -i 's#^name: gintary$#name: cindy#; s#ginn1111/gintary#ginn1111/cindy#' distribution.yaml
grep -n 'name: cindy' config.yaml distribution.yaml
git add config.yaml distribution.yaml skills/devops/hermes-profile-setup/references/data-fetching-cron-pattern.md
git commit -qm "chore: rename profile gintary to cindy" && git log --oneline -1

step "Point ginb escalations at cindy"
sed -i 's/`gintary`/`cindy`/g' "$P/ginb/SOUL.md"
grep -c '`cindy`' "$P/ginb/SOUL.md"

step "Reassign gintary kanban cards to cindy (all boards)"
for b in $(hermes kanban boards list --json 2>/dev/null | python3 -c 'import json,sys;print(" ".join(x["slug"] for x in json.load(sys.stdin)))'); do
  for t in $(hermes kanban --board "$b" list --assignee gintary --archived --json 2>/dev/null | python3 -c 'import json,sys;print(" ".join(x["id"] for x in json.load(sys.stdin)))'); do
    hermes kanban --board "$b" reassign --reclaim "$t" cindy >/dev/null 2>&1 && echo "ok $b $t" || echo "SKIP $b $t (reassign refused)"
  done
done

step "Restart gateway"
systemctl --user restart hermes-gateway.service
sleep 5
hermes profile list
echo "DONE. Next: bash /home/aioz/personal/cindy/scripts/smoke.sh"
