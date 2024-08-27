from rest_framework import serializers

from authen_drf.models import User
from payment.serializers import PaymentSerializer


class UserDetailSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True, source='payments', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'payment', 'is_staff', 'is_active', 'groups')

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')
