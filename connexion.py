from pymongo import MongoClient
from statics import Project

def get_connexion():
    try:
        client = MongoClient(f"mongodb://{Project['admin_username']}:{Project['admin_mdp']}@{Project['ip_db']}:{Project['port']}/?authSource=admin")
        db = client["TPNoSQL"]
        return db
    except Exception as e:
        print(f"Erreur de connexion à MongoDB : {e}")
        return None

# Teste la connexion à la bdd
#print(f"mongodb://{Project['admin_username']}:{Project['admin_mdp']}@{Project['ip_db']}:{Project['port']}/?authSource=admin")
get_connexion()