from pymongo import MongoClient

def get_connexion():
    try:
        client = MongoClient("mongodb://admin:admin@192.168.5.190:27017/?authSource=admin")
        db = client["TPNoSQL"]
        return db
    except Exception as e:
        print(f"Erreur de connexion à MongoDB : {e}")
        return None
db = get_connexion()

