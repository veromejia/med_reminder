#!/usr/bin/python3
from pathlib import Path
from crontab import CronTab
from decimal import Decimal
import getpass
import os

crons = 0
os_user = getpass.getuser()
path = os.getcwd()

"""
cron contain cron tables of the operative system
from the given user
"""
cron = CronTab(user=os_user)
cron_command = 'python3 {}/taskmanager.py '.format(path)
job = cron.new(command=cron_command, comment="medr-taskmanager")
job.minute.every(1)
cron.write()

print("The following cron's were created: ".format(crons))
for item in cron:
    print(item)
