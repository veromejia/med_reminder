#!/usr/bin/python3
"""Class Patient"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class Patient(Base):
    """class that represent patient table"""
    __tablename__ = 'patient'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(120))
    phone = Column(String(15), nullable=False)
    prescriptions = relationship(
        'Prescription', backref='patient', cascade='all, delete-orphan')
