#!/bin/bash

 echo "🚀 Création et démarrage du conteneur MongoDB..."
    docker run -d \
        --name mongodb \
        -p 27017:27017 \
        -e MONGO_INITDB_ROOT_USERNAME=admin \
        -e MONGO_INITDB_ROOT_PASSWORD=secretpassword \
        mongo


echo "🐍 Exécution du script Python..."
# quote this line if you don't use python venv
source ./NoSQL/bin/activate
python3 ./init.py

echo "✅ Script terminé."
