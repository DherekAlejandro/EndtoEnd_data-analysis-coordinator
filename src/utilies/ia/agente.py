from typing import Optional
import google.generativeai as genai
from utilies.ia.schema import MedicalRecord
from utilies.ia.config import GENERATION_CONFIGS, SYSTEM
from pydantic import ValidationError

def process_medical_image(image_data: str) -> Optional[MedicalRecord]:
    try:
        # Enviar la imagen y el prompt al modelo.
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            contents=[
                SYSTEM + "\n\n" + MedicalRecord.schema_json(indent=2),
                {"mime_type": "image/jpeg", "data": image_data}
            ],
            generation_config={
                "response_mime_type": "application/json"
            }
        )

        json_data = response.text
        medical_record = MedicalRecord.model_validate_json(json_data)
        
        return medical_record

    except FileNotFoundError:
        print(f"Error: El archivo {image_data} no se encontró.")
        return None
    except ValidationError as e:
        print(f"Error de validación del esquema Pydantic: {e}")
        print(f"Respuesta del modelo: {response.text}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None