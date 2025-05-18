from pymongo import MongoClient
from connexion import get_connexion
from statics import Project

def create_users():
    db = get_connexion()
    
    try:
        db.command({"createUser": Project["ro_username"], "pwd": Project["ro_mdp"], "roles": [{"role": "read", "db": Project["table_name"]}]})
        print("Utilisateur readOnlyUser créé")
    except Exception as e:
        print(f"readOnlyUser déjà existant ou erreur : {e}")

    
    try:
        db.command({"createUser": Project["rw_username"], "pwd": Project["rw_mdp"], "roles": [{"role": "readWrite", "db": Project["table_name"]}]})
        print("Utilisateur readwrite créé")
    except Exception as e:
        print(f"rw déjà existant ou erreur : {e}")

create_users()