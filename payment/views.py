from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from payment.models import Pay
from payment.serializers import PaySerializer


class PayViewSet(viewsets.ModelViewSet):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('payday', 'pay_method', 'is_paid')
