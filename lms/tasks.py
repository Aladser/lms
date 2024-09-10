from datetime import datetime

import pytz
from celery import shared_task
from django.core.mail import send_mail

from authen_drf.models import User
from config import settings
from config.settings import EMAIL_HOST_USER
from lms.models import Course, UserSubscription


@shared_task
def send_course_updating_notification(course_id):
    """Отправляет отложенно почтовые уведомления об обновлении курса """

    course =  Course.objects.get(pk=course_id)
    subscriptions = UserSubscription.objects.filter(course=course)

    if subscriptions.count == 0:
        return "Нет пользователей для отправки уведомлений"

    subject = f"Обновлен курс {course}"
    message = (f""
               f"Название: {course.name}\n"
               f"Описание:{course.description}\n"
               f"Создан пользователем {course.owner}")
    email_list = tuple(subscription.user.email for subscription in subscriptions)

    response = send_mail(subject, message, EMAIL_HOST_USER, email_list)
    return f"Отправлены почтовые уведомления на обновление курса {course}" if response == 1 else response


@shared_task
def check_user_activities():
    """Периодическая задача проверки активности пользователя"""

    info = []

    datetime_now = datetime.now(pytz.timezone(settings.TIME_ZONE))
    for user in User.objects.all():
        if user.last_login is None:
            continue

        lastlogin_interval = (datetime_now - user.last_login).days
        info.append(lastlogin_interval)

    return info

