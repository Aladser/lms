from django.core.management import BaseCommand

from authen_drf.models import User
from libs.seeding import Seeding


class Command(BaseCommand):
    user_obj_list = [
        {
            'email': 'admin@test.ru',
            'first_name': 'Админ',
            'last_name': 'Админов',
            'is_superuser': True,
            'is_staff': True
        },
        {
            'email': 'users@test.ru',
            'first_name': 'Пользователь',
            'last_name': 'Обычный',
            'is_staff': True
        }
    ]

    password = '_strongpassword_'

    def handle(self, *args, **kwargs):
        Seeding.seed_users(User, self.user_obj_list, self.password)
