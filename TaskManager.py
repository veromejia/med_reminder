#!/usr/bin/python3

import sys
from TaskModel import Base, Task
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import DBStorage, Patient, Prescription, Task, Task_x_prescription
from datetime import datetime
from crontab import CronTab

user = 'user_medreminder'
pas = 'pwd_medreminder'
db = 'db_medreminder'
cron = CronTab()

uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pas, db)

engine = create_engine(uri, pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

message = "1"

for task in session.query(Task).filter(
                Task.status_cd == "NEW0", Task.active == 1).all():
        message = "{}:  Access Date {}\n".format(task.name, datetime.now())
        myfile = open(
                '/home/nelson/Documents/medreminder_app/testPython/job.txt',
                'a+')
        myfile.write(message)
        myfile.close()
        """Proceding to create a new cron job to fire the alert"""
        cron = CronTab(user='nelson')
        job = cron.new(
                command='python3 /home/vero/Documents/medreminder_app/testPython/job.py',
                comment="medr{}".format(task.id_task))
        job.minute.every(1)
        cron.write()
        task.status_cd = "CRTD"
        session.commit()
print("The following cron's were created")
for item in cron:
    print(item)

session.close()
