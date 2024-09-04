from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authen_drf.models import User
from lms.models import Course, Lesson

user_params = {'email': 'admin@test.ru','first_name': 'Админ','last_name': 'Админов', 'is_superuser': True}
course_pk = 10
lesson_pk = 10
course_params = {'pk':course_pk, 'name': 'математика'}
lesson_params = {'pk': lesson_pk, "name": "степени", "description": "возведение в степень"}

class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(**user_params)
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(**course_params)
        lesson_params["course"] = self.course
        self.lesson = Lesson.objects.create(**lesson_params)

    def test_list(self):
        url = reverse('lms:lesson_list')

        response = self.client.get(url)
        received_lessons = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(received_lessons['count'], 1)

    def test_retrieve(self):
        url = reverse('lms:lesson_retrieve', kwargs={'pk':lesson_pk})
        response = self.client.get(url)
        received_lesson = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(received_lesson['name'], self.lesson.name)

    def test_create(self):
        url = reverse('lms:lesson_create')
        sent_lesson = {
            "name": "уравнения",
            "description":"что такое уравнения",
            "course":course_pk
        }

        response = self.client.post(url, sent_lesson)
        received_lesson = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(received_lesson['name'], sent_lesson['name'])

    def test_update(self):
        url = reverse('lms:lesson_update', kwargs={'pk':lesson_pk})
        sent_lesson = {'name': 'степени: продолжение','description': 'решение примеров'}

        response  = self.client.patch(url, sent_lesson)
        received_lesson = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(received_lesson['name'], sent_lesson['name'])
        self.assertEqual(received_lesson['description'], sent_lesson['description'])

    def test_delete(self):
        url = reverse('lms:lesson_delete', kwargs={'pk': lesson_pk})
        response  = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(**user_params)
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(**course_params)

    def test_course_subscription(self):
        url = reverse('lms:course_subscription', kwargs={'pk': course_pk})
        sent_response_str =  f'Добавлена подписка пользователя {self.user} на курс {str(self.course).title()}'

        response = self.client.post(url)
        received_response_str =response.json()['response']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(received_response_str, sent_response_str)

