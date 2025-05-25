from config_users import create_users
from insert_logs import send_logs
from logs_creators import Generate_logs
from pymongo import MongoClient

def init_db():

    Generate_logs()
    send_logs()
    #create_users()
    

init_db()