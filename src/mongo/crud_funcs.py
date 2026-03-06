from src.exception.exception_handler import MongoError
from src.mongo.establish_connection import client


def create_db(db_name: str, username: str):
    try:
        mydatabase = client[db_name]
        collection = mydatabase["template"]
        collection.insert_one({"name": db_name})
        mydatabase.command('createUser', username, roles=[{"role": "userAdminAnyDatabase", "db": "admin"}], pwd="1234")
    except Exception:
        raise MongoError


def delete_db(db_name: str):
    try:
        client.drop_database(db_name)
    except Exception:
        raise MongoError


def rename_db(old_name: str, new_name: str):
    try:
        if old_name == new_name:
            return

        old_db = client[old_name]
        new_db = client[new_name]
        for collection in old_db.list_collection_names():
            old_collection = old_db[collection]
            new_collection = new_db[collection]
            documents = old_collection.find()
            if documents:
                new_collection.insert_many(documents)

        client.drop_database(old_name)
    except Exception:
        raise MongoError
