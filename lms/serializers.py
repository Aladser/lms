from rest_framework import serializers

from lms.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        return instance.lessons.all().count()



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

