#!/usr/bin/python3

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.db_storage import DBStorage
from backend.models.prescription import Prescription
from backend.models.patient import Patient
from datetime import datetime
from twilio.rest import Client
import os

account_sid = "ACc5816629da2f5a693a90ad6dfdb5685e"
auth_token = "aa1b88d275ff37ded851157e3dfe7601"
client = Client(account_sid, auth_token)

db = DBStorage()

date = datetime.strptime(
    '{} {}'.format(sys.argv[2], sys.argv[3]), '%Y-%m-%d %H:%M:%S')
print(date)
for prescription in db.all_prescription():
    if prescription.start_dt == date and prescription.frequency == sys.argv[1] and prescription.end_dt > date and prescription.noti_type == 'phone':
        patient = db.all_patients_by_id(prescription.patient_id)
        client.messages.create(
            to=patient.phone,
            from_="+12063505601",
            body=prescription.medication)
"""
import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)"""
