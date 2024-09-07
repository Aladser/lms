from django.db import models

from authen_drf.models import User
from config.settings import NULLABLE
from libs.truncate_table_mixin import TruncateTableMixin
from lms.models import Course, Lesson


class Payment(TruncateTableMixin, models.Model):
    user = models.ForeignKey(
        verbose_name='пользователь',
        to=User,
        on_delete=models.CASCADE,
        related_name='payments',
        **NULLABLE,
    )

    course = models.ForeignKey(
        verbose_name='курс',
        to=Course,
        on_delete=models.CASCADE,
        related_name='payments',
    )
    lesson = models.ForeignKey(
        verbose_name='урок',
        to=Lesson,
        on_delete=models.CASCADE,
        related_name='payments',
        **NULLABLE,
    )

    amount = models.PositiveIntegerField(
        verbose_name='стоимость',
    )
    session_id = models.CharField(
        verbose_name='id платежной сессии',
        max_length=255,
        **NULLABLE,
    )
    link = models.URLField(
        verbose_name="ссылка на страницу платежа",
        max_length=400,
        **NULLABLE,
    )

    date = models.DateTimeField(
        verbose_name='дата платежа',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('user', 'course', 'lesson', 'amount')

    def product(self):
        return f"{self.course.name}: {self.lesson.name}" if self.lesson else self.lesson.name

    def __str__(self):
        return f"{self.lesson} - {str(self.amount)}" if self.lesson else f"{self.course} - {str(self.amount)}"
