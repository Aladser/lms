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

        # Предметы
        math = Course.objects.get(name='математика')
        biology = Course.objects.get(name='биология')
        fractions_name = 'дроби'
        plants = 'пестики и тычинки'
        lesson_list = [
            {'name': fractions_name, 'course': math},
            {'name': 'степени', 'course': math},
            {'name': plants, 'course': biology},
        ]
        seed_table(Lesson, lesson_list)

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
        lesson_1 = get_object_or_404(Lesson, name=fractions_name)
        lesson_2 = get_object_or_404(Lesson, name=plants)
        payment_list = [
            {'user':user,'lesson':lesson_1, 'type':cash, 'value':100},
            {'user':user, 'lesson': lesson_1, 'type': cash, 'value': 200},
            {'user':user, 'lesson': lesson_2, 'type': non_cash, 'value': 300},
            {'user':user, 'course': math, 'type': non_cash, 'value': 400},
            {'user':user, 'course': math, 'type': non_cash, 'value': 500}
        ]
        seed_table(Payment, payment_list)
