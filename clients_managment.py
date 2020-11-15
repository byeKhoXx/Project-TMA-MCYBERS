from db_model.db_connection import db_connection
from db_model.client import Client

db = db_connection()

def new_client(name, ip):
    client = Client.get_client_by_name(name, db)
    if client is None:
        client = Client(name, ip)
        Client.insert_db(client, db)

def get_client_by_name(name):
    result = Client.get_client_by_name(name, db)
    return result


