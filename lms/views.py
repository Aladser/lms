from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from authen_drf.permissions import IsModeratorPermission, IsOwnerPermission
from libs.owner_queryset import OwnerQuerysetMixin
from lms.models import Course, Lesson
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
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, IsOwnerPermission]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwnerPermission, ~IsModeratorPermission]
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

# DESTROY
class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # не вижу смысла в праве ~IsModeratorPermission, так модератор не может что-то создавать
    permission_classes = [IsAuthenticated, IsOwnerPermission]

# UPDATE
class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerPermission]
