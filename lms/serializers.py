from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import LinkValidator


general_validators = [LinkValidator('description'), LinkValidator('name')]

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = general_validators

class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, source='lessons', read_only=True)
    lessons_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        validators = general_validators

    def get_lessons_count(self, instance):
        return instance.lessons.all().count()


