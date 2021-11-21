from datetime import datetime
from .scheduler import scheduler
from .mailer import email
from .sms import sms


def notify(mail, phone, data):
    if(email):
        email(mail, data)
    if(sms):
        sms(phone, data)


def set_scheduler(mail, phone, data):
    instance = (scheduler.add_job(
        notify, 'date', run_date=data['when'], args=[mail, phone, data]))
    return instance.id
