from src.exception.exception_handler import AuthorizationError, DeploymentNotFound
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from src.rdbms import helper_functions
from src.functualities import deployments
from fastapi import APIRouter, status, Depends
from typing import Annotated
from fastapi import Body, Header
import secrets


router = APIRouter(prefix="/deployments")
security = HTTPBasic()


def authenticate(credentials: Annotated[HTTPBasicCredentials, Depends(security)], dep_id: str) -> bool:
    correct_username = helper_functions.get_username(dep_id)
    if correct_username:
        correct_username = correct_username.encode("utf-8")
        current_username = credentials.username.encode("utf-8")
        return secrets.compare_digest(current_username, correct_username)
    else:
        raise DeploymentNotFound


@router.post("", status_code=status.HTTP_201_CREATED)
def create_deployment(db_name: Annotated[str, Body()], username: Annotated[str, Body()],
                      credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if username == credentials.username:
        return deployments.create_deployment(db_name, username)
    else:
        raise AuthorizationError


@router.get("/")
def get_deployments(deployment_id: str, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if authenticate(credentials, deployment_id):
        return deployments.get_deployment(deployment_id)
    else:
        raise AuthorizationError


@router.put("/")
def rename(deployment_id: str, db_name: Annotated[str, Body(embed=True)],
           credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if authenticate(credentials, deployment_id):
        return deployments.rename(deployment_id, db_name)
    else:
        raise AuthorizationError


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete(deployment_id: str, username: Annotated[str, Header()],
           credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if authenticate(credentials, deployment_id):
        return deployments.delete(deployment_id, username)
    else:
        raise AuthorizationError


@router.get("/connection_string/")
def get_connection_string(deployment_id: str, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if authenticate(credentials, deployment_id):
        return deployments.get_connection_string(deployment_id)
    else:
        raise AuthorizationError
