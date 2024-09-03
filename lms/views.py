from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from authen_drf.permissions import IsModeratorPermission, IsOwnerPermission
from libs.owner_queryset import OwnerQuerysetMixin
from lms.models import Course, Lesson, UserSubscription
from lms.serializers import CourseSerializer, LessonSerializer


# --- КУРС ---
# VIEWSET
class CourseViewSet(OwnerQuerysetMixin, ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModeratorPermission]
        elif self.action in ['update', 'partial_update', 'delete']:
            self.permission_classes = [IsOwnerPermission]
        return super().get_permissions()


# --- УРОК ---
# LIST
class LessonListAPIView(OwnerQuerysetMixin, generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


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


# ----- ПОЛЬЗОВАТЕЛЬСКАЯ ПОДПИСКА НА КУРСЫ -----
class CourseSubscriptionAPIView(APIView):
    """управление подпиской пользователя на курс"""

    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        course = get_object_or_404(Course, id=kwargs['pk'])
        action = ''
        try:
            subscription = UserSubscription.objects.get(user=self.request.user, course=course)
            action = f'Удалена {subscription}'
            subscription.delete()
        except:
            subscription = UserSubscription.objects.create(user=self.request.user, course=course)
            action = f"Добавлена {subscription}"
        finally:
            return Response(action)


