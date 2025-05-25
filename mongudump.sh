#!/bin/bash

CONTAINER_NAME="mongodb"
DB_NAME="TPNoSQL"
USER="admin"
PASS="secretpassword"
AUTH_DB="admin"
BACKUP_DIR="./dump_$(date +%Y%m%d_%H%M%S)"

mkdir -p "$BACKUP_DIR"

echo "🚀 Création du dump MongoDB..."

docker exec "$CONTAINER_NAME" mongodump \
  --username "$USER" \
  --password "$PASS" \
  --authenticationDatabase "$AUTH_DB" \
  --db "$DB_NAME" \
  --out /tmp/dump

docker cp "$CONTAINER_NAME":/tmp/dump "$BACKUP_DIR"

echo "✅ Sauvegarde terminée dans : $BACKUP_DIR"
