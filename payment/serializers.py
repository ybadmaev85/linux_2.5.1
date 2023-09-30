
from payment.models import Pay
from rest_framework import serializers


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