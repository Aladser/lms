from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentListAPIView, show_success_payment, PaymentCreateAPIView

app_name = PaymentConfig.name

urlpatterns = [
    path('success/', show_success_payment, name='payment-success'),
    path('create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('', PaymentListAPIView.as_view(), name='payment-list'),
]
