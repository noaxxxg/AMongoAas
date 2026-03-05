from establish_connection import client


def create_db(db_name: str):
    try:
        mydatabase = client[db_name]
        collection = mydatabase["template"]
        collection.insert_one({"name": db_name})
    except Exception:
        raise Exception


def delete_db(db_name: str):
    client.drop_database(db_name)


def rename_db(old_name: str, new_name: str):
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
