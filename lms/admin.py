from django.contrib import admin

from lms.models import Course, Lesson, UserSubscription


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'owner')
    ordering = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'updated_at')
    ordering = ('name',)

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    ordering = ('user', 'course')
