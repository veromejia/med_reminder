#!/usr/bin/python3
"""module to clear all the crons and subcrons that
are running to send the message"""
from crontab import CronTab

cron = CronTab(user='vero')
exist = False


for item in cron:
    print(item)

print('Cleaning all crons.')
cron.remove_all()
cron.write()
print('Crons cleaned.')
