from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LearningConfig
from lms.views import *

app_name = LearningConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/<int:pk>/update', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/<int:pk>/delete', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('course/<int:pk>/switch_subscription', CourseSubscriptionAPIView.as_view(), name='course-subscription'),
] + router.urls
