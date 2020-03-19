#!/usr/bin/python3
"""Class task por prescription"""
from backend.models.patient import Base
from backend.models.prescription import Prescription
from backend.models.task import Task
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Task_x_prescription(Base):
    """class that represent Task_x_prescription table"""
    __tablename__ = 'task_x_prescription'
    task_id = Column(Integer, ForeignKey(
        'task.id'), primary_key=True, nullable=False,)
    prescription_id = Column(Integer, ForeignKey(
        'prescription.id'), primary_key=True, nullable=False,)
