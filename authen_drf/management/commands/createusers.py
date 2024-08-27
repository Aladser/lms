from django.core.management import BaseCommand
from django.contrib.auth.models import Group

from authen_drf.models import User
from config.settings import MODERATORS_GROUP_NAME
from libs.seeding import Seeding


class Command(BaseCommand):
    moderator_email = 'moderator@test.ru'
    user_obj_list = [
        {
            'email': 'admin@test.ru',
            'first_name': 'Админ',
            'last_name': 'Админов',
            'is_superuser': True,
            'is_staff': True
        },
        {
            'email': moderator_email,
            'first_name': 'Модератор',
            'last_name': 'Средний',
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

        Group.objects.all().delete()
        moderators_group, created = Group.objects.get_or_create(name=MODERATORS_GROUP_NAME)

        moder = User.objects.get(email=self.moderator_email)
        moder.groups.add(moderators_group)
        moder.save()
