from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from requests import Request
from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated

from authen_drf.permissions import IsModeratorPermission
from payment.models import Payment
from payment.serializers import PaymentSerializer
from payment.services import StripeService


# --- ПЛАТЕЖ ---
class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['date']
    filterset_fields = ['course', 'lesson']

class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, ~IsModeratorPermission]

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.user = self.request.user
        payment.save()

        usd_amount = StripeService.convert_rub_to_usd(payment.amount)
        stripe_price = StripeService.create_price(usd_amount)
        session_id, session_url = StripeService.create_session(stripe_price)
        payment.session_id = session_id
        payment.link = session_url
        payment.save()


def show_success_payment(request: Request) -> HttpResponse:
    """Страница успешного платежа"""

    return render(
        request,
        'success_payment.html',
    )
