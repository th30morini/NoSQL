import json
import random
from datetime import datetime, timedelta

# Préparer des données de base
users = ["admin", "seb", "sarah", "theo"]
actions = ["login_attempt", "file_access", "password_change", "logout", "config_change"]
statuses = ["success", "failed"]
base_time = datetime.utcnow()

# Générer 100 -> 2000 logs
logs = []
for i in range(10):
    random_seconds = random.randint(0, 7 * 24 * 60 * 60)  # jusqu'à 7 jours
    random_time = base_time - timedelta(seconds=random_seconds)
    log = {
        "timestamp": random_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ip": f"192.168.2.{random.randint(1, 254)}",
        "user": random.choice(users),
        "action": random.choice(actions),
        "status": random.choice(statuses)
    }
    logs.append(log)

# Sauvegarder dans un fichier JSON
output_path = "./logs/logs.json"
with open(output_path, "w") as f:
    json.dump(logs, f, indent=4)


