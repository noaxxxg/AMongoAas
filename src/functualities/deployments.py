from src.mongo.establish_connection import DATABASE_URL
from src.rdbms.create_tables import Deployment
from src.mongo import crud_funcs
from src.rdbms import use_db


def create_deployment(db_name: str, username: str) -> str:
    if db_name.startswith(username) and len(username) >= 3:
        crud_funcs.create_db(db_name)
        return use_db.create_deployment(username, db_name)
    else:
        raise Exception


def get_deployment(deployment_id: str) -> Deployment:
    return use_db.get_deployment(deployment_id)


def rename(deployment_id: str, new_name: str):
    old_name = use_db.rename_deployment(deployment_id, new_name)
    if old_name:
        crud_funcs.rename_db(old_name, new_name)
    else:
        raise Exception


def delete(deployment_id: str, username):
    db_name = use_db.delete_deployment(deployment_id, username)
    if db_name:
        crud_funcs.delete_db(db_name)
    else:
        raise Exception


def get_connection_string(deployment_id: str) -> str:
    return DATABASE_URL
