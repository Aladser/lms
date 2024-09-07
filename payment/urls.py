from django.urls import path

from payment.apps import PaymentConfig
from payment.views import *

app_name = PaymentConfig.name

urlpatterns = [
    path('success/', show_success_payment, name='success'),
    path('<int:pk>/status', PaymentStatusAPIView.as_view(), name='status'),
    path('create/', PaymentCreateAPIView.as_view(), name='create'),
    path('', PaymentListAPIView.as_view(), name='list'),
]
