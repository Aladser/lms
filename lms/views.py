from datetime import datetime

import pytz
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from authen_drf.permissions import IsModeratorPermission, IsOwnerPermission
from libs.owner_queryset import OwnerQuerysetMixin
from lms.models import Course, Lesson, UserSubscription
from lms.paginators import CustomPagination
from lms.serializers import CourseSerializer, LessonSerializer
from lms.tasks import send_course_updating_notification


# --- КУРС ---
class CourseViewSet(OwnerQuerysetMixin, ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModeratorPermission]
        elif self.action in ['update', 'partial_update', 'delete']:
            self.permission_classes = [IsOwnerPermission]
        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def perform_update(self, serializer):
        course = serializer.save()

        datetime_now = datetime.now(pytz.timezone(settings.TIME_ZONE))
        last_updated_at = datetime_now - course.updated_at

        if last_updated_at.total_seconds() > 60*60*4:
            send_course_updating_notification.delay(course.pk)

        course.updated_at = datetime_now
        course.save()


# --- УРОК ---
# LIST
class LessonListAPIView(OwnerQuerysetMixin, generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CustomPagination


# RETRIEVE
class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerPermission]


# CREATE
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModeratorPermission]


# UPDATE
class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerPermission]


# DESTROY
class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerPermission]


# ----- УПРАВЛЕНИЕ ПОДПИСКОЙ ПОЛЬЗОВАТЕЛЯ НА КУРС -----
class CourseSubscriptionAPIView(APIView):
    """
    Управление подпиской пользователя на курс

    подписка определяется наличием записи в таблице UserSubscription
    """

    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        course = get_object_or_404(Course, id=kwargs['pk'])
        try:
            subscription = UserSubscription.objects.get(user=self.request.user, course=course)
            message = f'Удалена {subscription}'
            subscription.delete()
            return Response({'response': message})
        except Exception as e:
            if str(e) == "UserSubscription matching query does not exist.":
                subscription = UserSubscription.objects.create(user=self.request.user, course=course)
                return Response({'response': f"Добавлена {subscription}"})
            else:
                print(e)


