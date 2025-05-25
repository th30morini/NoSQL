Write-Host "🚀 Création et démarrage du conteneur MongoDB..."
docker run -d `
    --name mongodb `
    -p 27017:27017 `
    -e MONGO_INITDB_ROOT_USERNAME=admin `
    -e MONGO_INITDB_ROOT_PASSWORD=secretpassword `
    mongo

Write-Host "🐍 Exécution du script Python..."

# Active le venv si nécessaire (tu peux commenter cette ligne si pas de venv)
. .\NoSQL\Scripts\Activate.ps1

python .\init.py

Write-Host "✅ Script terminé."
