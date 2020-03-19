#!/usr/bin/python3

from crontab import CronTab

cron = CronTab(user='vero')
exist = False


for item in cron:
    print(item)

print('Cleaning all crons.')
cron.remove_all()
cron.write()
print('Crons cleaned.')
