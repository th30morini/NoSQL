# TP NoSQL B3 CybSec

Ce projet initialise une base de données MongoDB à l’aide d’un script Python local et d’un conteneur Docker MongoDB.

Avant de commencer, installer les outils suivants : Python (3.7+), pip, Docker. Ensuite, télécharge l’image MongoDB avec :  
`docker pull mongo`

Optionnel mais recommandé : créer un environnement virtuel Python  
```bash
python -m venv NoSQL
# Linux/macOS :
source NoSQL/bin/activate
# Windows PowerShell :
.\NoSQL\Scripts\Activate.ps1
```

Installe les dépendances Python :  
```bash
pip install pymongo
```

### Exécution :

#### Sur Linux/macOS :
```bash
chmod +x init.sh
./init.sh
```

#### Sur Windows PowerShell :
```powershell
.\init.ps1
```

Ce script lance le conteneur MongoDB (si nécessaire), attend que la base soit prête, puis exécute le script Python `init.py` qui crée des utilisateurs et insère des données.

### Vérification :

```bash
docker exec -it mongodb mongo -u admin -p secretpassword --authenticationDatabase admin
```

Dans le shell Mongo :
```js
use TPNoSQL
show users
db.logs.find().pretty()
```


