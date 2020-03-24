#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.fields.html5 import DateField
from datetime import datetime
from wtforms.validators import *
from backend.models.db_storage import DBStorage
from backend.models.patient import Patient
from backend.models.prescription import Prescription


class DashBoardForm(FlaskForm):
    """dashboard form"""
    patients = Patient()
    selectedid = ""

    def getPatients(self):
        """function that get the patients info from the wtforms"""
        db = DBStorage()
        self.patients = db.all_patients()

    def getPrescriptions(self):
        """function that get the prescription info from the wtforms"""
        db = DBStorage()
        prescriptions = db.prescriptionXpatientID(int(self.selectedid))
        return prescriptions

    def getTasks(self, prescriptionID):
        """function that get the task info from the wtforms"""
        tasks = []
        db = DBStorage()
        tasks = db.taskByPrescriptions(prescriptionID)
        return tasks
