from pymongo import MongoClient
from connexion import get_connexion
from hash_entry import add_log_hash
import json


db = get_connexion()
if db is None:
    print("La connexion à la base de données a échoué.")
else:
    collection = db["logs"]  

   
    with open("./logs/logs.json", "r") as file:
        data = json.load(file)  

 
    for entry in data:
        entry = add_log_hash(entry)

 
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)  

    print("Succès")