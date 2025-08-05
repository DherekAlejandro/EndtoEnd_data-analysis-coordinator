from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os
import sys

# Cargar las variables del .env (solo útil en entorno local)
load_dotenv()

# Leer la URL desde variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Validar que la variable esté definida
if not DATABASE_URL:
    print("❌ Error: DATABASE_URL no está definida.")
    sys.exit(1)

# Crear el motor de conexión (echo=True para debug)
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)
