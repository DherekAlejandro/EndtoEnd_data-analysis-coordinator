from typing import Optional
import mimetypes
import google.generativeai as genai
from src.utilies.ia.schema import MedicalRecord
from src.utilies.ia.config import GENERATION_CONFIGS, SYSTEM
from pydantic import ValidationError
import base64

def get_mime_type(file_path: str) -> str:
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        raise ValueError("No se pudo determinar el tipo MIME del archivo.")
    return mime_type

def read_image_as_base64(file_path: str) -> str:
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def process_medical_image(image_path: str) -> Optional[MedicalRecord]:
    try:
        mime_type = get_mime_type(image_path)
        image_data = read_image_as_base64(image_path)

        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            contents=[
                SYSTEM + "\n\n" + MedicalRecord.schema_json(indent=2),
                {"mime_type": mime_type, "data": image_data}
            ],
            generation_config={
                "response_mime_type": "application/json"
            }
        )

        json_data = response.text
        medical_record = MedicalRecord.model_validate_json(json_data)

        return medical_record

    except FileNotFoundError:
        print(f"Error: El archivo {image_path} no se encontró.")
        return None
    except ValidationError as e:
        print(f"Error de validación del esquema Pydantic: {e}")
        print(f"Respuesta del modelo: {response.text}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None
