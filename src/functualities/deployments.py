from src.rdbms.establish_connection import session
from src.mongo.establish_connection import client
from src.rdbms.create_tables import Deployment
from typing import Annotated
from fastapi import Body
import datetime
import uuid


def create_deployment(db_name: Annotated[str, Body()], username: Annotated[str, Body()]) -> str:
    if db_name.startswith(username):
        db_id = uuid.uuid4()
        deployment = Deployment(id=str(db_id), db_name=db_name, status=1, username=username,
                                creation_time=datetime.datetime)


