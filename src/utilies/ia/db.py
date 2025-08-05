from sqlmodel import SQLModel, create_engine, Session
import os
import sys

def get_database_url():
    url = os.getenv("DATABASE_URL")
    if not url:
        print("[ERROR] La variable de entorno DATABASE_URL no está definida. Configúrala en Render o en tu .env local.", file=sys.stderr)
        raise RuntimeError("DATABASE_URL no definida")
    # Render puede entregar la URL sin el prefijo 'postgresql+psycopg2://', lo agregamos si falta
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql+psycopg2://", 1)
    elif url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg2://", 1)
    return url

try:
    DATABASE_URL = get_database_url()
    engine = create_engine(DATABASE_URL, echo=True)
except Exception as e:
    print(f"[ERROR] No se pudo crear el engine de la base de datos: {e}", file=sys.stderr)
    engine = None

def create_db_and_tables():
    if engine is None:
        print("[ERROR] Engine de base de datos no inicializado.", file=sys.stderr)
        return
    SQLModel.metadata.create_all(engine)

def get_session():
    if engine is None:
        raise RuntimeError("Engine de base de datos no inicializado.")
    return Session(engine)
