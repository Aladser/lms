from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_course_updating_notification(subject: str, message: str, email_list:tuple):
    return send_mail(subject,message,EMAIL_HOST_USER,email_list)

