from django.contrib.auth.models import AbstractUser
from django.db import models

from libs.truncate_table_mixin import TruncateTableMixin


# Create your models here.
class User(AbstractUser, TruncateTableMixin):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

