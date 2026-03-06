from sqlalchemy import select
from src.rdbms.establish_connection import get_session
from src.rdbms.create_tables import Deployment, Status


session = get_session()


def get_username(deployment_id: str) -> str | None:
    stmt = select(Deployment.username).where(Deployment.id == deployment_id)
    return session.scalars(stmt).first()


def get_created() -> int:
    stmt = select(Status.id).where(Status.name == "CREATED")
    return session.scalars(stmt).first()


def get_deleted() -> int:
    stmt = select(Status.id).where(Status.name == "DELETED")
    return session.scalars(stmt).first()
