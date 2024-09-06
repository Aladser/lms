from django.contrib import admin

from payment.models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'lesson', 'amount', 'link', 'session_id')
    ordering = ('user', 'course', '-amount')
