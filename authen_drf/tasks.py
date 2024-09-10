from datetime import datetime

import pytz
from celery import shared_task

from authen_drf.models import User
from config.settings import TIME_ZONE


@shared_task
def check_user_activities():
    """Периодическая задача проверки активности пользователя"""

    info = []

    datetime_now = datetime.now(pytz.timezone(TIME_ZONE))
    for user in User.objects.all():
        if user.last_login is None:
            continue

        lastlogin_interval = (datetime_now - user.last_login).days
        if lastlogin_interval > 30:
            user.is_active = False
            user.save()

        info.append(f"{user.email} - {user.is_active} - {lastlogin_interval}")

    return info
