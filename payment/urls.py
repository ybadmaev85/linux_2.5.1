from rest_framework.routers import DefaultRouter
from django.urls import path
from payment.apps import PaymentConfig
from payment.views import PayViewSet, PaymentSuccessView, PaymentCreateAPIView

app_name = PaymentConfig.name

router = DefaultRouter()
router.register(r'payment', PayViewSet, basename='payment')
urlpatterns = [
        path('create/', PaymentCreateAPIView.as_view(), name='create'),
        path('success/', PaymentSuccessView.as_view(), name='success'),
              ] + router.urls