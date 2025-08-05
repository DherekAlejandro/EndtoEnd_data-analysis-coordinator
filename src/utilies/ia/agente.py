from typing import Optional
import google.generativeai as genai
from src.utilies.ia.schema import MedicalRecord
from src.utilies.ia.config import GENERATION_CONFIGS, SYSTEM
from pydantic import ValidationError

def process_medical_image(image_data: str, mime_type: str) -> Optional[MedicalRecord]:
    try:
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

    except ValidationError as e:
        print(f"Error de validación del esquema Pydantic: {e}")
        print(f"Respuesta del modelo: {response.text}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None
