from datetime import datetime
from .scheduler import scheduler
from .mailer import email


def notify(user, data):
    if(email):
        email(user, data)


def set_scheduler(user, data):
    instance = (scheduler.add_job(
        notify, 'date', run_date=data['when'], args=[user, data]))
    return instance.id
