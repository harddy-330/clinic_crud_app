from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from .database import Base
import enum

class GenderEnum(str, enum.Enum):
    Male = "Male"
    Female = "Female"
    Other = "Other"

class StatusEnum(str, enum.Enum):
    Scheduled = "Scheduled"
    Completed = "Completed"
    Cancelled = "Cancelled"

class Patient(Base):
    __tablename__ = "Patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(Enum(GenderEnum), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    phone = Column(String(15), unique=True, nullable=False)
    email = Column(String(100), unique=True)

    appointments = relationship("Appointment", back_populates="patient")


class Appointment(Base):
    __tablename__ = "Appointments"

    appointment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("Patients.patient_id"), nullable=False)
    doctor_id = Column(Integer)  # Simplified: Not implementing doctor CRUD for now
    appointment_date = Column(DateTime, nullable=False)
    reason = Column(Text)
    status = Column(Enum(StatusEnum), default="Scheduled")

    patient = relationship("Patient", back_populates="appointments")
