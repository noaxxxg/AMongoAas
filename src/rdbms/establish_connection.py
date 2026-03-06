from src.rdbms.create_tables import Base, Status
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/my_db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()

Base.metadata.create_all(engine)


def add_status():
    query = select(Status)
    value = session.scalars(query)
    session.add(Status(name="CREATED"))
    session.add(Status(name="DELETED"))
    session.commit()
