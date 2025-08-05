from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class MedicalRecordORM(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
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
    recomendaciones: Optional[str] = None
    restricciones: Optional[str] = None
    vision: Optional[str] = None
    audiometria: Optional[str] = None
    notas: Optional[str] = None
