import datetime
import uuid
from sqlalchemy import select
from src.rdbms.create_tables import Deployment
from src.rdbms.establish_connection import session


def create_deployment(username: str, db_name: str) -> str:
    db_id: uuid = uuid.uuid4()
    deployment = Deployment(id=str(db_id), db_name=db_name, status=1, username=username,
                            creation_time=datetime.datetime)
    session.add(deployment)
    session.commit()
    return str(db_id)


def get_deployment(db_id: str) -> Deployment:
    stmt = (select(Deployment).options(Deployment.id, Deployment.db_name, Deployment.status, Deployment.creation_time)
            .where(Deployment.id == db_id))
    return session.scalars(stmt).one()


def delete_deployment(db_id: str, username: str) -> str | None:
    stmt = select(Deployment).where(Deployment.id == db_id)
    deployment = session.scalars(stmt).one()
    if deployment.username == username:
        deployment.status = 2
        session.commit()
        return deployment.db_name


def rename_deployment(db_id: str, name: str) -> str | None:
    stmt = select(Deployment).where(Deployment.id == db_id)
    deployment: Deployment = session.scalars(stmt).one()
    if name.startswith(deployment.username):
        old_name = deployment.db_name
        deployment.db_name = name
        session.commit()
        return old_name
