from sqlmodel import SQLModel, create_engine, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def crear_tablas():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
