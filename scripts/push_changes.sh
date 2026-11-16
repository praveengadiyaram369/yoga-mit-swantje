#!/bin/sh
# Änderungen veröffentlichen (von überall aufrufbar): ./scripts/push_changes.sh
# Optional mit eigener Nachricht: ./scripts/push_changes.sh "Stundenplan aktualisiert"
cd "$(dirname "$0")/.." || exit 1
git add .
git commit -m "${1:-Website aktualisiert}"
git push -u origin main
