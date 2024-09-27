from datetime import datetime

import pytz
from celery import shared_task

from authen_drf.models import User
from config.settings import TIME_ZONE


@shared_task
def check_user_activities():
    """Периодическая задача проверки активности пользователей"""

    datetime_now = datetime.now(pytz.timezone(TIME_ZONE))
    disabled_users_list = []
    for user in User.objects.all():
        if user.last_login is None:
            continue

        lastlogin_interval = (datetime_now - user.last_login).days
        if lastlogin_interval > 7 and user.is_active:
            user.is_active = False
            user.last_login = None
            user.save()
            disabled_users_list.append(user.email)

    if len(disabled_users_list) != 0:
        return f"Деактивировано пользователей: {''.join(disabled_users_list)}"
    else:
        return "Нет деактивированных пользователей"
