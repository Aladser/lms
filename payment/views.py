from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from requests import Request
from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authen_drf.permissions import IsModeratorPermission
from payment.models import Payment
from payment.serializers import PaymentSerializer
from payment.services import StripeService


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
        stripe_price = StripeService.create_price(payment.product_name, usd_amount)
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

class PaymentStatusAPIView(APIView):
    """Проверка статуса оплаты"""

    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        payment = get_object_or_404(Payment, id=kwargs['pk'])
        payment_status = StripeService.get_payment_status(payment).get("payment_status")
        return Response({'response': payment_status})
