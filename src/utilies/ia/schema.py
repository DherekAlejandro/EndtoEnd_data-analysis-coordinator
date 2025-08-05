from pydantic import BaseModel
from typing import Optional
from datetime import date

class MedicalRecord(BaseModel):
    nombre: str
    identificacion: str
    edad: int
    municipio: str
    enfasis_de_examen: str
    fecha: date
    peso: float
    talla: float
    imc1: str
    imc2: str
    tension: str
    observaciones: str
    resultados: str
    recomendaciones: Optional[str]
    restricciones: Optional[str]
    vision: Optional[str]
    audiometria: Optional[str]
    notas: Optional[str]