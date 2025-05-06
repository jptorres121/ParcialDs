from sqlmodel import SQLModel, create_engine, Session

# ✅ Esta es tu URL de conexión a PostgreSQL. Cambia los datos reales
DATABASE_URL = "postgresql://usuario:contraseña@localhost:5432/mi_basedatos"

# 🔌 Crear engine de conexión
engine = create_engine(DATABASE_URL, echo=True)


def crear_tablas():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
