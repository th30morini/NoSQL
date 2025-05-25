#!/bin/bash

USERNAME="admin"
PASSWORD="secretpassword"
AUTH_DB="admin"
DB_NAME="TPNoSQL"
DUMP_DIR="./dump_powershell/TPNoSQL"  # chemin vers le dossier dump BSON

echo "🚀 Lancement de la restauration MongoDB..."

mongorestore 
    --username "$USERNAME" \
    --password "$PASSWORD" \
    --authenticationDatabase "$AUTH_DB" \
    --db "$DB_NAME" \
    --drop \
    "$DUMP_DIR"


if [ $? -eq 0 ]; then
    echo "✅ Restauration réussie depuis $DUMP_DIR"
else
    echo "❌ Erreur lors de la restauration"
fi
