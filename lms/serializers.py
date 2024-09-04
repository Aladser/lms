from django.template.context_processors import request
from rest_framework import serializers

from authen_drf.serializers import UserDetailSerializer
from lms.models import Course, Lesson, UserSubscription
from lms.validators import LinkValidator


general_validators = [LinkValidator('description'), LinkValidator('name')]

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = general_validators

class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, source='lessons', read_only=True)
    lessons_count = serializers.SerializerMethodField(read_only=True)
    user = UserDetailSerializer(many=True, source='lessons', read_only=True)
    is_user_subscription = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        validators = general_validators

    def get_lessons_count(self, instance):
        return instance.lessons.all().count()

    def get_is_user_subscription(self, instance):
        auth_user = self.context.get('request').user
        return UserSubscription.objects.filter(user = auth_user, course=instance).exists()



