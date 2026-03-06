from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from src.rdbms.create_tables import Base, Status
from src.configuration.open_config import POSTGRES_URL


engine = create_engine(POSTGRES_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)


def get_session():
    return SessionLocal()


def create_tables():
    Base.metadata.create_all(engine)


def add_status():
    session = get_session()
    stmt = select(Status.name).where(
        Status.name.in_(["CREATED", "DELETED"])
    )
    existing_statuses = session.scalars(stmt).all()
    missing_statuses = []

    if "CREATED" not in existing_statuses:
        missing_statuses.append(Status(name="CREATED"))

    if "DELETED" not in existing_statuses:
        missing_statuses.append(Status(name="DELETED"))

    if missing_statuses:
        session.add_all(missing_statuses)
        session.commit()

    session.close()
