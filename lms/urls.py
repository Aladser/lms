from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LearningConfig
from lms.views import *

app_name = LearningConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/update', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('course/<int:pk>/switch_subscription', CourseSubscriptionAPIView.as_view(), name='course_subscription'),
] + router.urls
