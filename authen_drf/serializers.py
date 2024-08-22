from rest_framework import serializers

from authen_drf.models import User
from payment.serializers import PaymentSerializer


class UserSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True, source='payments', read_only=True)

    class Meta:
        model = User
        fields = '__all__'
