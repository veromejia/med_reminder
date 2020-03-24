#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.fields.html5 import DateField
from datetime import datetime
from wtforms.validators import *
from backend.models.db_storage import DBStorage
from backend.models.patient import Patient
from backend.models.prescription import Prescription


class PrescriptionForm(FlaskForm):
    """class to create the objects for prescription form"""
    patients = SelectField('Patients', choices=[])
    medication = StringField(
        'Medication', validators=[DataRequired(), Length(min=2, max=20)])
    frequency = FloatField(
        'Frequency', validators=[InputRequired()])
    start_dt = DateField('Start Date')
    end_dt = DateField('End Date')
    noti_type = SelectField(
        'choose one', choices=[('phone', 'phone'), ('e-mail', 'e-mail')])
    submit = SubmitField('CREATE')

    def createPatient(self):
        """function to create a new patient"""
        p = Prescription()
        p.patient_id = self.patients.data
        p.medication = self.medication.data
        p.frequency = self.frequency.data
        p.start_dt = self.start_dt.data
        p.end_dt = self.end_dt.data
        p.noti_type = self.noti_type.data
        return p

    def getPatients(self):
        """function to get the existent patients from the db"""
        if not self.patients.choices:
            db = DBStorage()
            options = []
            for patient in db.all_patients():
                options.append((patient.id, '{} {}'.format(
                    patient.name, patient.last_name)))
            self.patients.choices = options
            self.patients.default = 1

    def save(self):
        """function to save a new prescription for a given patient"""
        db = DBStorage()
        p = self.createPatient()
        db.add_prescription(p)

    def validateForm(self):
        """input validations"""
        isvalid = False
        inputs = []
        if self.patients.data and self.medication.data and self.frequency.data and self.start_dt.data and self.end_dt.data and self.noti_type.data:
            isvalid = True
        else:
            if not self.frequency.data:
                inputs.append('Frequency')
            if not self.medication.data:
                inputs.append('Medication')
        return isvalid, inputs

    def printObj(self):
        """print the given information"""
        return 'patient_id:{}, medication:{}, frequency:{}, start_dt:{},'
        'end_dt:{}, noti_type:{}'.format(
            self.patients.data,
            self.medication.data,
            self.frequency.data,
            self.start_dt,
            self.end_dt.data,
            self.noti_type.data)
