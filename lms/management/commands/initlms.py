from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from authen_drf.models import User
from libs.seed_table import seed_table
from lms.models import Course, Lesson
from payment.models import PaymentMethod, Payment


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = get_object_or_404(User, email='admin@test.ru')

        # Курсы
        course_list = [
            {'name': 'физика'},
            {'name': 'математика'},
            {'name': 'биология'},
        ]
        seed_table(Course, course_list)
        math = Course.objects.get(name='математика')
        biology = Course.objects.get(name='биология')

        # Предметы
        fractions_name = 'дроби'
        pow_name = 'степени'
        plants_name = 'пестики и тычинки'
        lesson_list = [
            {'name': fractions_name, 'course': math},
            {'name': pow_name, 'course': math},
            {'name': plants_name, 'course': biology},
        ]
        seed_table(Lesson, lesson_list)
        fractions_lesson = get_object_or_404(Lesson, name=fractions_name)
        pow_lesson = get_object_or_404(Lesson, name=pow_name)
        plants_lesson = get_object_or_404(Lesson, name=plants_name)

        # способоы платежей
        cash_name = 'наличные'
        non_cash_name = 'безналичные'
        payment_method_list = [
            {'name': cash_name},
            {'name': non_cash_name},
        ]
        seed_table(PaymentMethod, payment_method_list)
        cash = get_object_or_404(PaymentMethod, name=cash_name)
        non_cash = get_object_or_404(PaymentMethod, name=non_cash_name)

        # Платежи

        payment_list = [
            {'user':user, 'course': math, 'lesson': fractions_lesson, 'type':cash, 'value':100},
            {'user':user, 'course': math, 'lesson': pow_lesson, 'type': cash, 'value': 200},
            {'user':user, 'course': biology, 'lesson': plants_lesson, 'type': non_cash, 'value': 300},
            {'user':user, 'course': math, 'type': non_cash, 'value': 400},
            {'user':user, 'course': biology, 'type': non_cash, 'value': 500}
        ]
        seed_table(Payment, payment_list)
