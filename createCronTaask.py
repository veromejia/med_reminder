#!/usr/bin/python3

import sys
from task import Base, Task
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from crontab import CronTab

host = 'localhost'
user = 'user_medreminder'
pas = 'pwd_medreminder'
db = 'db_medreminder'
uri = ''
cron = CronTab()

uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pas, db)
engine = create_engine(uri, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()
message = "1"
crons = 0
for task in session.query(Task).filter(Task.status == "NEW0").all():
        message = "{}:  Access Date {}\n".format(task.name, datetime.now())
        myfile = open('/home/nelson/Documents/medreminder_app/testPython/job.txt', 'a+')
        myfile.write(message)
        myfile.close()
        """Proceding to create a new cron job to fire the alert"""
        cron = CronTab(user='nelson')
        job = cron.new(
            command='python3 /home/nelson/Documents/medreminder_app/testPython/job.py',
            comment="medr-{}".format(task.id))
        job.minute.every(int(task.frequency))
        cron.write()
        task.status_cd = "CRTD"
        session.commit()
        crons = crons + 1

print("The following cron's were created: ".format(crons))
for item in cron:
    print(item)

session.close()
