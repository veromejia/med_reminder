#!/usr/bin/python3
"""DataBase Storage"""
from backend.models.patient import Base, Patient
from backend.models.prescription import Prescription
from backend.models.task_x_prescription import Task_x_prescription
from backend.models.task import Task
from sqlalchemy import create_engine, update, and_, join, select
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
        """function to get the current session of the db"""
        return self.__session

    def all_patients(self):
        """function to get an specific patient identify by id"""
        patients = self.__session.query(Patient).order_by(Patient.id).all()
        return patients

    def all_patients_by_id(self, id):
        """function to get all the prescription of the table prescription"""
        patients = self.__session.query(Patient).filter(Patient.id == id).one()
        return patients

    def all_prescription(self):
        """function to get all the prescription of the table prescription"""
        new_prescription = self.__session.query(
            Prescription).order_by(Prescription.id).all()
        self.__session.close()
        return new_prescription

    def prescriptionXpatientID(self, id):
        """function to get a prescription per patient ordered by id"""
        prescriptions = Prescription()
        try:
            patient = self.__session.query(
                Patient).filter(Patient.id == id).one()
            prescriptions = patient.prescriptions
        except IndexError:
            prescriptions = Prescriptions()

        return prescriptions

    def all_task(self):
        """function that return all the tasks"""
        new_task = self.__session.query(Task).order_by(Task.id).all()
        return new_task

    def task_by_command(self, command):
        """return all task that have the same command"""
        query = self.__session.query(Task).filter(
            Task.task_command == command).all()
        return query

    def taskByPrescriptions(self, prescriptionID):
        records = []
        j = join(
            Task, Task_x_prescription, Task.id == Task_x_prescription.task_id)
        query = select(
            [Task]).select_from(j).where(
                Task_x_prescription.prescription_id == prescriptionID)
        result = self.__session.execute(query)
        for row in result:
            records.append(row)
        return records

    def all_new_tasks(self):
        """ return all the tasks with new status"""
        query = self.__session.query(
            Task).filter(Task.status == 'NEW0').all()
        return query

    def all_task_x_prescription(self):
        """ return all the tasks per prescription
        the of task_x_prescription table"""
        new_taskPrescription = self.__session.query(
            Task_x_prescription).all()
        return new_taskPrescription
        self.__session.close()

    def add_patient(self, patient):
        """ to add a new paptient in the database"""
        self.__session.add(patient)
        self.__session.commit()

    def add_prescription(self, prescription):
        """ to add a new paptient in the database"""
        self.__session.add(prescription)
        self.__session.commit()

    def add_task(self, task):
        """ to add a new task to the data base"""
        self.__session.add(task)
        self.__session.commit()

    def add_task_x_prescription(self, task_x_prescription):
        """ to add a new task per prescription in the database"""
        self.__session.add(task_x_prescription)
        self.__session.commit()
