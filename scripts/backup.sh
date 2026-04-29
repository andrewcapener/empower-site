#!/bin/bash
# Backup script — mirrors live site and retains 30 days of snapshots

SITE_URL="https://empowereit.com"
BACKUP_DIR="$(dirname "$0")/../backups"
DATE=$(date +%Y-%m-%d)
SNAPSHOT_DIR="$BACKUP_DIR/$DATE"
LOG="$BACKUP_DIR/backup.log"
RETENTION_DAYS=30

mkdir -p "$SNAPSHOT_DIR"

echo "[$(date)] Starting backup of $SITE_URL → $SNAPSHOT_DIR" | tee -a "$LOG"

wget --mirror \
  --convert-links \
  --adjust-extension \
  --page-requisites \
  --no-parent \
  --quiet \
  --directory-prefix="$SNAPSHOT_DIR" \
  "$SITE_URL"

if [ $? -eq 0 ]; then
  echo "[$(date)] Backup complete — $SNAPSHOT_DIR" | tee -a "$LOG"
else
  echo "[$(date)] WARNING: wget exited with errors. Partial backup may exist at $SNAPSHOT_DIR" | tee -a "$LOG"
fi

# Prune backups older than 30 days
echo "[$(date)] Pruning backups older than $RETENTION_DAYS days..." | tee -a "$LOG"
find "$BACKUP_DIR" -maxdepth 1 -type d -name "????-??-??" -mtime +$RETENTION_DAYS -exec rm -rf {} \;

echo "[$(date)] Done." | tee -a "$LOG"
