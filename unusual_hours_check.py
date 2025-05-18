from pymongo import MongoClient
from connexion import get_connexion

def detect_unusual_hours():
    start_hour= 8
    end_hour=18
    db = get_connexion()
    collection = db["logs"]

    # Trouver tous les logs hors plage horaire autorisée
    unusual_logs = collection.find({
        "$expr": {
            "$or": [
                { "$lt": [ { "$hour": "$timestamp" }, start_hour ] },
                { "$gt": [ { "$hour": "$timestamp" }, end_hour ] }
            ]
        }
    })end_hour=18

    print(f"Connexions à des heures inhabituelles (hors 8h-18h) : {len(logs)}")
    for log in list(unusual_logs):
        print(f"- {log['timestamp']} | {log['ip']} | {log['user']} | {log['action']}")


