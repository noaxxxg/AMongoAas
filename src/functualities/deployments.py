from src.exception.exception_handler import NameInvalid, DeploymentNotFound
from src.configuration.open_config import MONGO_URL
from src.mongo import crud_funcs
from src.rdbms import use_db
from typing import Any


def create_deployment(db_name: str, username: str) -> str:
    if db_name.startswith(username) and len(username) >= 3:
        crud_funcs.create_db(db_name)
        return use_db.create_deployment(username, db_name)
    else:
        raise NameInvalid


def get_deployment(deployment_id: str) -> dict[str, Any]:
    try:
        return use_db.get_deployment(deployment_id)
    except DeploymentNotFound:
        raise DeploymentNotFound


def rename(deployment_id: str, new_name: str):
    try:
        old_name = use_db.rename_deployment(deployment_id, new_name)
        crud_funcs.rename_db(old_name, new_name)
    except DeploymentNotFound:
        raise DeploymentNotFound


def delete(deployment_id: str, username):
    try:
        db_name: str = use_db.delete_deployment(deployment_id, username)
        crud_funcs.delete_db(db_name)
    except DeploymentNotFound:
        raise DeploymentNotFound


def get_connection_string(deployment_id: str) -> str:
    return MONGO_URL
