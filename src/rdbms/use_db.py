import uuid
import datetime
from typing import Any
from sqlalchemy import select
from src.rdbms.create_tables import Deployment, Status
from src.rdbms.establish_connection import session


def create_deployment(username: str, db_name: str) -> str:
    db_id: uuid = uuid.uuid4()
    deployment = Deployment(id=str(db_id), db_name=db_name, status=1, username=username,
                            creation_time=datetime.datetime.now())
    session.add(deployment)
    session.commit()
    return str(db_id)


def get_deployment(db_id: str) -> dict[str, Any]:
    stmt = (select(Deployment, Status).join(Status)
            .where(Deployment.id == db_id))
    result = session.execute(stmt).one()
    if result:
        deployment, status = result
        dep_dict = deployment.__dict__.copy()
        dep_dict.pop("_sa_instance_state", None)
        dep_dict.pop("username", None)
        dep_dict["status"] = status.name
        return dep_dict
    else:
        raise Exception


def delete_deployment(db_id: str, username: str) -> str | None:
    stmt = select(Deployment).where(Deployment.id == db_id)
    deployment = session.scalars(stmt).one()
    if deployment:
        if deployment.username == username:
            deployment.status = 2
            session.commit()
            return deployment.db_name
    else:
        raise Exception


def rename_deployment(db_id: str, name: str) -> str | None:
    stmt = select(Deployment).where(Deployment.id == db_id)
    deployment: Deployment = session.scalars(stmt).one()
    if deployment:
        if name.startswith(deployment.username):
            old_name = deployment.db_name
            deployment.db_name = name
            session.commit()
            return old_name
    else:
        raise Exception
