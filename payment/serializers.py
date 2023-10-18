
from payment.models import Pay
from rest_framework import serializers


class SuccessPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False}
        }


class PaySerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели платежа
    '''

    class Meta:
        model = Pay
        fields = (
            'user',
            'payday',
            'is_paid',
            'summa',
            'pay_method',
        )
        extra_kwargs = {
            'user': {'required': False}
        }