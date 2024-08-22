from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from payment.models import Payment
from payment.serializers import PaymentSerializer


# --- ПЛАТЕЖ ---
class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']
