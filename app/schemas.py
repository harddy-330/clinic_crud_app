from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime
from enum import Enum


class GenderEnum(str, Enum):
    Male = "Male"
    Female = "Female"
    Other = "Other"


class StatusEnum(str, Enum):
    Scheduled = "Scheduled"
    Completed = "Completed"
    Cancelled = "Cancelled"


class PatientBase(BaseModel):
    first_name: str
    last_name: str
    gender: GenderEnum
    date_of_birth: date
    phone: str
    email: Optional[EmailStr] = None

class PatientCreate(PatientBase):
    pass

class PatientOut(PatientBase):
    patient_id: int
    class Config:
     from_attributes = True

class AppointmentBase(BaseModel):
    appointment_date: datetime
    reason: Optional[str]
    status: Optional[StatusEnum] = StatusEnum.Scheduled
    doctor_id: Optional[int]

class AppointmentCreate(AppointmentBase):
    patient_id: int

class AppointmentOut(AppointmentBase):
    appointment_id: int
    patient_id: int
    class Config:
     from_attributes = True
