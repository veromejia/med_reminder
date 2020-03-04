#!/usr/bin/python3
"""Class Prescription"""
from models.patient import Base, Patient
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime


class Prescription(Base):
    __tablename__ = 'prescription'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), nullable=False)
    medication = Column(String(120), nullable=False)
    frequency = Column(String(60), nullable=False)
    start_dt = Column(DateTime, nullable=False, default=datetime.utcnow())
    end_dt = Column(DateTime, nullable=False, default=datetime.utcnow())
    noti_type = Column(String(60))
    task_x_prescriptions = relationship(
        'Task_x_prescription', backref='prescription')
