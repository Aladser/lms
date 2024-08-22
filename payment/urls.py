from django.urls import path

from lms.apps import LearningConfig
from payment.views import PaymentListAPIView

app_name = LearningConfig.name

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payment_list'),
]
