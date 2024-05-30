import os
from dotenv import load_dotenv
from pymongo import MongoClient

class DatabaseConnectionError(Exception):
    def __init__(self, message: str = "Could not connect to the database"):
        self.message = message
        super().__init__(self.message)

def get_database():
    db_connection = os.getenv("DB_CONNECTION")
    database_name = os.getenv("DB_NAME")

    client = MongoClient(db_connection)
    try:
        db = client[database_name]
    except Exception as e:
        raise DatabaseConnectionError(e)

    return db

def insert_document(document):
    db = get_database()
    collection_name = os.getenv("COLLECTION_NAME")

    try:
        collection = db[collection_name]
        result = collection.insert_one(document)
        return str(result.inserted_id)
    except ConnectionError as e:
        raise DatabaseConnectionError("Could not connect to the database") from e
