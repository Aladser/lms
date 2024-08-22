from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics

from payment.models import Payment
from payment.serializers import PaymentSerializer


# --- ПЛАТЕЖ ---
class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['date']
    filterset_fields = ['course', 'lesson', 'type']
