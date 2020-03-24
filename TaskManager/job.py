#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.db_storage import DBStorage
from backend.models.prescription import Prescription
from backend.models.patient import Patient
from datetime import datetime
from twilio.rest import Client
from pathlib import Path
import smtplib
import ssl
import os

account_sid = "Mytwiliosid"
auth_token = "MytwilioToken"
client = Client(account_sid, auth_token)

db = DBStorage()


def sendmail(email, prescription, frequency):
    """ function to send a email usign prot 465 and a gmail account"""
    port = 465
    sender = 'medreminderapp431@gmail.com'
    password = 'myEmailPassword'
    recieve = email
    message = """
    Subject: medreminder
    Don't forget take your {} every {} hour
    Medreminder
    """.format(prescription, frequency)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)

"""
code to send a text message using twillio API
or an email using the prev sendmail function
"""
date = datetime.strptime(
    '{} {}'.format(sys.argv[2], sys.argv[3]),
    '%Y-%m-%d %H:%M:%S')
path = '{}/TaskManager'.format(str(Path.home()))
myfile = open('{}/job.txt'.format(path), 'a+')
for prescription in db.all_prescription():
    if prescription.start_dt == date
    and prescription.frequency == sys.argv[1]
    and prescription.end_dt > datetime.now():
        patient = db.all_patients_by_id(prescription.patient_id)
        if prescription.noti_type == 'phone':
            message = "Sending message to the patient:"/
            "{} prescription: {} Access Date: {}\n".format(
                patient.id, prescription.medication, datetime.now())
            myfile.write(message)
            client.messages.create(
                to=patient.phone,
                from_="12056516878",
                body="Don't forget take your {} every {} hours".format(
                    prescription.medication, prescription.frequency))
            message = "Message successfully sent to patient:"
            "{} acces date:\n".format(patient.id, datetime.now())
            myfile.write(message)
        else:
            message = "Sending email to patient:"
            " {} prescription: {} Access Date: {}\n".format(
                patient.id, prescription.medication, atetime.now())
            myfile.write(message)
            sendmail(
                patient.email,
                prescription.medication,
                prescription.frequency)
            message = "Email successfully sent to  patient:"/
            "{} acces date:\n".format(patient.id, datetime.now())
            myfile.write(message)
myfile.close()
