import json
import random
from datetime import datetime, timedelta

# Préparer des données de base
users = ["admin", "seb", "sarah", "theo"]
actions = ["login_attempt", "file_access", "password_change", "logout", "config_change"]
statuses = ["success", "failed"]
base_time = datetime.utcnow()

def Generate_logs():
# Générer les logs aléatoires
    logs = []
    for i in range(2000):
        random_seconds = random.randint(0, 7 * 24 * 60 * 60)  # jusqu'à 7 jours
        random_time = base_time - timedelta(seconds=random_seconds)
        log = {
            "timestamp": random_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "ip": f"192.168.1.{random.randint(1, 254)}",
            "user": random.choice(users),
            "action": random.choice(actions),
            "status": random.choice(statuses)
        }
        logs.append(log)

    # Générer les logs avec plus de 5 échecs en moins de 10 min
    for i in range(100):
        random_seconds = random.randint(0, 7 * 60)  # jusqu'à 7 minutes
        random_time = base_time - timedelta(seconds=random_seconds)
        log = {
            "timestamp": random_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "ip": f"192.168.1.{random.randint(50, 53)}",
            "user": random.choice(users),
            "action": random.choice(actions),
            "status": "failed"
        }
        logs.append(log)


    # Générer les logs de ips inconnues

    for i in range(100):
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


