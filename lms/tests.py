from http.client import responses

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authen_drf.models import User
from lms.models import Course, Lesson

user_params = {'email': 'admin@test.ru','first_name': 'Админ','last_name': 'Админов', 'is_superuser': True}
course_pk = 10
lesson_pk = 10
course_params = {'pk':course_pk, 'name': 'математика'}
lesson_params = {'pk': lesson_pk, "name": "test", "description": " описание test"}

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
        data = {
            "name": "test2",
            "description":"описание test2",
            "course":course_pk
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
