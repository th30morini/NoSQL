from pymongo import MongoClient
from datetime import datetime, timedelta
from connexion import get_connexion

def detect_failed_attempts():
    db = get_connexion()
    collection = db["logs"]

    # 1. Récupérer tous les logs d'échec triés par IP et timestamp
    logs = list(collection.find(
        {"status": "failed"},
        {"ip": 1, "timestamp": 1}
    ).sort([("ip", 1), ("timestamp", 1)]))

    anomalies = set()

    # 2. Balayer les logs par IP avec une fenêtre glissante de 10 min
    from collections import deque
    window = deque()

    current_ip = None
    for log in logs:
        ip = log["ip"]
        ts = log["timestamp"]

        if ip != current_ip:
            window.clear()
            current_ip = ip

        # Ajouter log courant
        window.append(ts)

        # Retirer les entrées trop anciennes (> 10 min)
        while (ts - window[0]) > timedelta(minutes=10):
            window.popleft()

        if len(window) > 5:
            anomalies.add(ip)

    return anomalies

# Utilisation
suspicious_ips = detect_failed_attempts()
print("IPs suspectes avec +5 échecs en 10 minutes :")
for ip in suspicious_ips:
    print("-", ip)
