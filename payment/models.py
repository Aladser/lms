from django.db import models

from authen_drf.models import User
from config.settings import NULLABLE
from libs.truncate_table_mixin import TruncateTableMixin
from lms.models import Course, Lesson


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
    )
    date = models.DateTimeField(verbose_name='Дата платежа', auto_now_add=True)
    value = models.PositiveIntegerField(verbose_name='Сумма')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('user', 'course', 'lesson', 'value')

    def __str__(self):
        return f"{self.lesson} - {str(self.value)}" if self.lesson else f"{self.course} - {str(self.value)}"
