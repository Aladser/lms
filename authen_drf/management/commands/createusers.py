from django.core.management import BaseCommand

from authen_drf.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # суперпользователь
        User.truncate()
        user = User.objects.create(
            email='admin@test.ru',
            first_name='Админ',
            last_name='Админов',
            is_superuser=True,
            is_staff=True
        )

        user.set_password("admin@123")
        user.save()

        # обычный пользователь
        user = User.objects.create(
            email='user@test.ru',
            first_name='Пользователь',
            last_name='Обычный',
            is_staff=True
        )

        user.set_password("user@123")
        user.save()
