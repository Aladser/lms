from django.db import models
from django.db.models import SET_NULL

from authen_drf.models import User
from config.settings import NULLABLE
from libs.truncate_table_mixin import TruncateTableMixin

# -----КУРС-----
class Course(TruncateTableMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview_image = models.ImageField(verbose_name='превью изображение', upload_to='images/courses', **NULLABLE)
    owner = models.ForeignKey(User, verbose_name='Создатель', on_delete=SET_NULL, **NULLABLE)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('name', )

    def __str__(self):
        return self.name

# -----УРОК-----
class Lesson(TruncateTableMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview_image = models.ImageField(verbose_name='превью изображение', upload_to='images/lessons', **NULLABLE)
    video_link = models.CharField(max_length=255, verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='курс',
    )
    owner = models.ForeignKey(User, verbose_name='Создатель', on_delete=SET_NULL, **NULLABLE)

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('name', )

    def __str__(self):
        return self.name

# -----ПОЛЬЗОВАТЕЛЬСКАЯ ПОДПИСКА-----
class UserSubscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='подписка',
    )
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='курс',
    )

    class Meta:
        verbose_name = 'пользовательская подписка'
        verbose_name_plural = 'пользовательские подписки'
        ordering = ('user', 'course')

    def __str__(self):
        return f"подписка пользователя {self.user} на курс {str(self.course).title()}"
