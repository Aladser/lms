import os

from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from authen_drf.models import User
from libs.seeding import Seeding
from lms.models import Course, Lesson
from payment.models import Payment


class Command(BaseCommand):
    user = User.objects.get(email=os.getenv('MY_MAIL_3')) if os.getenv('MY_MAIL_3') else User.objects.get(email='user@test.ru')
    admin = User.objects.get(email=os.getenv('MY_MAIL_1')) if os.getenv('MY_MAIL_3') else User.objects.get(email='admin@test.ru')

    # курсы
    math_name = 'математика'
    bio_name = 'биология'
    course_list = [
        {'name': 'физика', 'owner':user},
        {'name': math_name},
        {'name': bio_name},
    ]

    # уроки
    fractions_name = 'дроби'
    pow_name = 'степени'
    plants_name = 'пестики и тычинки'


    # тип оплаты
    cash_name = 'наличные'
    non_cash_name = 'безналичные'
    payment_method_list = [
        {'name': cash_name},
        {'name': non_cash_name},
    ]

    def handle(self, *args, **kwargs):
        # Курсы
        Seeding.seed_table(Course, self.course_list)
        math = get_object_or_404(Course, name=self.math_name)
        biology = get_object_or_404(Course, name=self.bio_name)

        # Предметы
        lesson_list = [
            {'name': self.fractions_name, 'course': math, 'owner':self.user},
            {'name': self.pow_name, 'course': math},
            {'name': self.plants_name, 'course': biology},
        ]
        Seeding.seed_table(Lesson, lesson_list)
        fractions_lesson = get_object_or_404(Lesson, name=self.fractions_name)
        pow_lesson = get_object_or_404(Lesson, name=self.pow_name)
        plants_lesson = get_object_or_404(Lesson, name=self.plants_name)

        # Платежи
        payment_list = [
            {'user':self.admin, 'course': math, 'lesson': fractions_lesson, 'amount':100},
            {'user':self.admin, 'course': math, 'lesson': pow_lesson, 'amount': 200},
            {'user':self.admin, 'course': biology, 'lesson': plants_lesson, 'amount': 300},
            {'user':self.admin, 'course': math,'amount': 400},
            {'user':self.admin, 'course': biology, 'amount': 500}
        ]
        Seeding.seed_table(Payment, payment_list)
