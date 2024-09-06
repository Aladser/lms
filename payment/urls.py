from django.urls import path

from lms.apps import LearningConfig
from payment.views import PaymentListAPIView, show_success_payment, PaymentCreateAPIView

app_name = LearningConfig.name

urlpatterns = [
    path('success/', show_success_payment, name='success'),
    path('create/', PaymentCreateAPIView.as_view(), name='create'),
    path('', PaymentListAPIView.as_view(), name='list'),
]
