from sqlmodel import Session
from .db import get_session
from .models import MedicalRecordORM

class MedicalRecordRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, record: MedicalRecordORM) -> MedicalRecordORM:
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return record
