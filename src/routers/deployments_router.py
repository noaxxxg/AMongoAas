from src.rdbms.create_tables import Deployment
from src.functualities import deployments
from fastapi import APIRouter
from typing import Annotated
from fastapi import Body, Header


router = APIRouter(prefix="/deployments")


@router.post("")
def create_deployment(db_name: Annotated[str, Body()], username: Annotated[str, Body()]):
    return deployments.create_deployment(db_name, username)


@router.get("/")
def get_deployments(deployment_id: str):
    return deployments.get_deployment(deployment_id)


@router.put("/")
def rename(deployment_id: str, db_name: Annotated[str, Body()]):
    return deployments.rename(deployment_id, db_name)


@router.delete("/")
def delete(deployment_id: str, username: Annotated[str, Header()]):
    return deployments.delete(deployment_id, username)


@router.get("/connection_string/")
def get_connection_string(deployment_id: str):
    return deployments.get_connection_string(deployment_id)
