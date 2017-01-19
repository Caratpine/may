from webapp.extensions import celery
import smtplib
from email.mime.text import MIMEText
from .models import Reminder


@celery.task()
def log(msg):
    return msg


@celery.task(
    bind=True,
    ignore_result=True,
    default_retry_delay=300,
    max_retries=5
)
def remind(self, pk):
    reminder = Reminder.query.get(pk)
    print reminder.text
    print reminder.id


def on_reminder_save(mapper, connect, self):
    remind.apply_async(args=(self.id,), eta=self.date)



