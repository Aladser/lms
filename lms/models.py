from django.db import models

from authen_drf.models import User
from config.settings import NULLABLE
from libs.truncate_table_mixin import TruncateTableMixin


class Course(TruncateTableMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview_image = models.ImageField(verbose_name='превью изображение', upload_to='images/courses', **NULLABLE)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('name', )

    def __str__(self):
        return self.name


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
        **NULLABLE,
    )

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('name', )

    def __str__(self):
        return self.name

class PaymentMethod(TruncateTableMixin, models.Model):
    name = models.CharField(verbose_name='название', max_length=100)
    class Meta:
        verbose_name = 'способ оплаты'
        verbose_name_plural = 'способы оплаты'
        ordering = ('name', )

    def __str__(self):
        return self.name


class Payment(TruncateTableMixin, models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='пользователь',
    )
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='курс',
        **NULLABLE,
    )
    lesson = models.ForeignKey(
        to=Lesson,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='урок',
        **NULLABLE,
    )
    type = models.ForeignKey(
        to=PaymentMethod,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='тип',
        **NULLABLE,
    )
    date = models.DateField(verbose_name='Дата платежа', auto_now_add=True)
    value = models.PositiveIntegerField(verbose_name='Сумма')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('user', 'course', 'lesson', 'value')

    def __str__(self):
        return f"{self.course} - {str(self.value)}" if self.course else f"{self.lesson} - {str(self.value)}"
