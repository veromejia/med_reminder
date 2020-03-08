#!/usr/bin/python3
"""Class Patient"""
from backend.models.patient import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import uuid


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    task_command = Column(String(60), nullable=False)
    task_comment = Column(String(60), nullable=False)
    last_dt = Column(DateTime, nullable=False)
    status = Column(String(60))
    tasks_x__prescription = relationship(
        'Task_x_prescription', backref='task')
