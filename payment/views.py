from pprint import pprint
from education.models import Сourse
import stripe
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

from payment.models import Pay
from payment.serializers import PaySerializer, SuccessPaymentSerializer
from payment.services import stripe_price_data


class PayViewSet(viewsets.ModelViewSet):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('is_paid', 'pay_method',)
    ordering_fields = ('payday', )


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data

        if data.get('course'):
            product = get_object_or_404(Сourse, pk=data['course'])
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': stripe_price_data(product),
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='http://localhost:8000/' +
                            reverse('payment:success') + '?session_id={CHECKOUT_SESSION_ID}')
            pprint(checkout_session.stripe_id)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if isinstance(product, Сourse):
            pay = Pay.objects.create(
                user=self.request.user,
                course=product,
                payment_amount=data['summa'],
                method=Pay.PAY_CARD,
                stripe_id=checkout_session.stripe_id,
                status=checkout_session['status'])
            pay.save()

        return Response({'payment_url': checkout_session.url}, status=status.HTTP_201_CREATED)


class PaymentSuccessView(generics.ListAPIView):
    serializer_class = SuccessPaymentSerializer
    queryset = Pay.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        session_id = self.request.GET.get('session_id')  # Получаем параметр session_id из URL
        if session_id:
            try:
                pay = Pay.objects.get(stripe_id=session_id)
                session = stripe.checkout.Session.retrieve(pay.stripe_id)
                pay.customer_email = session['customer_details']['email']
                pay.status = session['status']
                pay.is_paid=True
                pay.save()
                return super().get(request, *args, **kwargs)
            except Pay.DoesNotExist:
                return Response({'error': 'Платеж не найден'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'session_id не передан в URL'}, status=status.HTTP_400_BAD_REQUEST)


