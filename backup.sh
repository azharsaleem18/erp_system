#!/bin/bash

# Set database credentials
DB_NAME="azhar_erp_sys"
DB_USER="postgres"
DB_HOST="db"
BACKUP_DIR="/backups"

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Backup database with timestamp
pg_dump -U $DB_USER -h $DB_HOST -F c -b -v -f "$BACKUP_DIR/db_backup_$(date +\%F_\%T).dump" $DB_NAME

# Keep only last 7 backups
ls -t $BACKUP_DIR/*.dump | tail -n +8 | xargs rm -f