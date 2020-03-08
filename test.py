#!/usr/bin/python3
"""DataBase Storage"""
from backend.models.db_storage import DBStorage
from backend.models.patient import Base, Patient

x = DBStorage().all_patients()
y = DBStorage().all_prescription()
z = DBStorage().all_task_x_prescription()
zz = DBStorage().all_task()
