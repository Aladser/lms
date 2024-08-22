from django.contrib import admin

from lms.models import Course, Lesson, PaymentMethod, Payment


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'course')
    ordering = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ('name',)

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('id',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Payment._meta.get_fields()]
