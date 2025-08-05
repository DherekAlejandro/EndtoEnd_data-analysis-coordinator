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
    import traceback
    try:
        content = await file.read()
        print(f"[DEBUG] Archivo recibido: {file.filename}, tamaño: {len(content)} bytes", file=sys.stderr)
        # Convertir a base64 para evitar errores de decodificación
        import base64
        content_b64 = base64.b64encode(content).decode("utf-8")
        # Procesar la imagen y obtener el MedicalRecord (Pydantic)
        record = process_medical_image({
            "data": content_b64,
            "mime_type": file.content_type
        })
        print(f"[DEBUG] Resultado de process_medical_image: {record}", file=sys.stderr)
        if record is None:
            return {"error": "No se pudo procesar el archivo o el esquema es inválido", "debug": "El resultado de process_medical_image fue None. Revisa los logs del backend para más detalles."}
        # Convertir a ORM
        try:
            orm_record = MedicalRecordORM(**record.dict())
        except Exception as orm_exc:
            print(f"[ERROR] Fallo al convertir a ORM: {orm_exc}", file=sys.stderr)
            traceback.print_exc()
            return {"error": "Error al convertir a ORM", "debug": str(orm_exc)}
        # Guardar en la base de datos
        try:
            with get_session() as session:
                repo = MedicalRecordRepository(session)
                db_obj = repo.add(orm_record)
            return db_obj
        except Exception as db_exc:
            print(f"[ERROR] Fallo al guardar en la base de datos: {db_exc}", file=sys.stderr)
            traceback.print_exc()
            return {"error": "Error al guardar en la base de datos", "debug": str(db_exc)}
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        traceback.print_exc()
        return {"error": f"Error interno: {str(e)}"}
