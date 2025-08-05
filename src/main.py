from fastapi import FastAPI, File, UploadFile
from src.utilies.ia.agente import process_medical_image
from src.utilies.ia.schema import MedicalRecord
from src.utilies.ia.db import create_db_and_tables, get_session
from src.utilies.ia.models import MedicalRecordORM
from src.utilies.ia.repository import MedicalRecordRepository
from dotenv import load_dotenv
import sys

load_dotenv()

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        # Procesar la imagen y obtener el MedicalRecord (Pydantic)
        record = process_medical_image(content)
        if record is None:
            return {"error": "No se pudo procesar el archivo o el esquema es inválido"}
        # Convertir a ORM
        orm_record = MedicalRecordORM(**record.dict())
        # Guardar en la base de datos
        with get_session() as session:
            repo = MedicalRecordRepository(session)
            db_obj = repo.add(orm_record)
        return db_obj
    except Exception as e:
        import traceback
        print(f"[ERROR] {e}", file=sys.stderr)
        traceback.print_exc()
        return {"error": f"Error interno: {str(e)}"}
