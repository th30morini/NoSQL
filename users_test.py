from pymongo import MongoClient
from pymongo.errors import OperationFailure

def test_onlyread():
    print('\n\n=============================TEST ONLYREAD=======================================\n\n')
    client = MongoClient("mongodb://onlyread:mdp@192.168.5.190:27017/?authSource=TPNoSQL")
    db = client["TPNoSQL"]
    collection = db["logs"]

    try:
        print("Lecture d'un document :")
        doc = collection.find_one()
        print(f"{doc}")

        print("\nTentative d'insertion d'un document :")
        collection.insert_one({"nom": "TestPython"})
        print("⚠️ Insertion réussie (ce qui ne devrait pas arriver)")
    except OperationFailure as e:
        print("✅ Échec d'insertion (comportement attendu) :")
        print(e)



def test_canwrite():
    print('\n\n=============================TEST CANWRITE=======================================\n\n')
    
    client = MongoClient("mongodb://canwrite:mdp@192.168.5.190:27017/?authSource=TPNoSQL")
    db = client["TPNoSQL"]
    collection = db["logs"]

    try:
        print("Lecture d'un document :")
        doc = collection.find_one()
        print(f"{doc}")

        print("\nTentative d'insertion d'un document :")
        collection.insert_one({"text": "I can write"})
        print("Insertion réussie (ce qui devrait arriver)")
    except OperationFailure as e:
        print("Échec d'insertion (ce qui ne devrait pas arriver) :")
        print(e)



test_onlyread()
test_canwrite()