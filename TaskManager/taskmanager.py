#!/usr/bin/python3
from backend.models.db_storage import DBStorage
from backend.models.patient import Patient
from backend.models.prescription import Prescription
from backend.models.task import Task
from backend.models.task_x_prescription import Task_x_prescription
from datetime import datetime
from crontab import CronTab
from pathlib import Path
from decimal import Decimal
import getpass
import os


class TaskManager:
    path = '{}/TaskManager'.format(str(Path.home()))
    """propfile ='{}/db_properties.json'.format( path )"""

    def findMyTask(self, frequency, startDt):
        """find all the task by command in the task table"""
        db = DBStorage()
        task = db.task_by_command('python3 job.py {} {}'.format(
            frequency, startDt))
        return task

    def prescriptionsWithoutTasks(self):
        """ verify every prescription without task
        if there is not a task it is created and the relationship
        if there is a task just the relationship is created """
        db = DBStorage()
        patients = db.all_patients()
        task = []
        for patient in patients:
            if not patient.prescriptions:
                print('there is not prescription for pacient {}'.format(
                    patient.name))
            else:
                for prescription in patient.prescriptions:
                    if not prescription.task_x_prescriptions:
                        task = self.findMyTask(
                            prescription.frequency, prescription.start_dt)
                        if not task:
                            t = Task()
                            command = 'python3 job.py'
                            command = ' {} {}'.format(
                                command, prescription.frequency)
                            command = '{} {}'.format(
                                command, prescription.start_dt)
                            t.task_command = command
                            t.task_comment = 'medr-{}'.format(prescription.id)
                            t.last_dt = datetime.now()
                            t.status = 'NEW0'
                            db.add_task(t)
                            print('Task created succesfully')
                            db.add_task_x_prescription(
                                Task_x_prescription(
                                    task_id=t.id,
                                    prescription_id=prescription.id))
                        else:
                            t = task[0]
                            print("""One task match with the frequency {} and
                            the start date {}
                            proceding to set the configuration""".format(
                                prescription.frequency,
                                prescription.start_dt))
                            db.add_task_x_prescription(
                                Task_x_prescription(
                                    task_id=t.id,
                                    prescription_id=prescription.id))
                            print("""The relation between task and
                            prescription was established""")
    """
    ┌───────────── minute (0 - 59)
    │ ┌───────────── hour (0 - 23)
    │ │ ┌───────────── day of month (1 - 31)
    │ │ │ ┌───────────── month (1 - 12)
    │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
    │ │ │ │ │                     7 is also Sunday on some systems)
    │ │ │ │ │
    │ │ │ │ │
    * * * * *  command to execute
    """
    def createCron(self):
        """create the crons in the operative
        system to all the task with new status"""
        db = DBStorage()
        cron = CronTab()
        os_user = getpass.getuser()

        for task in db.all_new_tasks():
            args = task.task_command.split()
            date = datetime.strptime('{} {}'.format(
                args[3], args[4]), '%Y-%m-%d %H:%M:%S')
            if date <= datetime.now():
                path = os.getcwd()
                cron = CronTab(user=os_user)
                cron_command = '{} {} {} {} {}'.format(args[0], '{}/{}'.format(
                    path, args[1]), args[2], args[3], args[4])
                job = cron.new(command=cron_command, comment="medr-{}".format(
                    task.id))
                if Decimal(args[2]) == 1:
                    job.minute.every(59)
                elif Decimal(args[2]) >= 1:
                    job.hour.every(args[2])
                elif Decimal(args[2]) >= 0 and Decimal(args[2]) < 1:
                    minutes = args[2].split('.')
                    job.minute.every(minutes[1])
                cron.write()
                db.update_task_status(task.id, "CRTD")
                db.get_session().commit()

        print("The following cron's were created: ")
        for item in cron:
            print(item)
        db.get_session().close()

tm = TaskManager()
tm.prescriptionsWithoutTasks()
tm.createCron()

"""medreminderapp431@gmail.com
medreminder2020"""
