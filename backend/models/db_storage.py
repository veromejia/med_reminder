#!/usr/bin/python3
"""DataBase Storage"""
from backend.models.patient import Base, Patient
from backend.models.prescription import Prescription
from backend.models.task_x_prescription import Task_x_prescription
from backend.models.task import Task
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
import json


class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        with open('db_properties.json') as file:
            data = json.load(file)

            for prop in data['props']:
                user = prop['USER']
                pwd = prop['PWD']
                host = prop['HOST']
                database = prop['DB']
                """print('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, database))
                print ("")"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, database), pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def get_session(self):
        return self.__session

    def all_patients(self):
        patients = self.__session.query(Patient).order_by(Patient.id).all()
        return patients

    def all_patients_by_id(self, id):
        patients = self.__session.query(Patient).filter(Patient.id == id).one()
        return patients

    def all_prescription(self):
        new_prescription = self.__session.query(
            Prescription).order_by(Prescription.id).all()
        self.__session.close()
        return new_prescription

    def all_task(self):
        new_task = self.__session.query(Task).order_by(Task.id).all()
        return new_task
        """for task in self.__session.query(
                Task).order_by(Task.id).all():
            print("{}: {}".format(task.id, task.status))"""
        self.__session.close()

    def task_by_command(self, command):
        query = self.__session.query(Task).filter(
            Task.task_command == command).all()
        return query

    def all_new_tasks(self):
        query = self.__session.query(Task).filter(Task.status == 'NEW0').all()
        return query

    def all_task_x_prescription(self):
        new_taskPrescription = self.__session.query(Task_x_prescription).all()
        return new_taskPrescription
        self.__session.close()

    def add_patient(self, patient):
        self.__session.add(patient)
        self.__session.commit()

    def add_prescription(self, prescription):
        self.__session.add(prescription)
        self.__session.commit()

    def add_task(self, task):
        self.__session.add(task)
        self.__session.commit()

    def add_task_x_prescription(self, task_x_prescription):
        self.__session.add(task_x_prescription)
        self.__session.commit()
