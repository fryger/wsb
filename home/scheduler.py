from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from apscheduler.events import (
    EVENT_JOB_EXECUTED,
    EVENT_JOB_SUBMITTED,
)
from .models import Reminders

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

register_events(scheduler)


def executed_listener(event):
    Reminders.objects.filter(task=event.job_id).delete()


scheduler.add_listener(executed_listener, EVENT_JOB_EXECUTED)

scheduler.start()
print("Scheduler started!")
