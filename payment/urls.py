from rest_framework.routers import DefaultRouter

from payment.apps import PaymentConfig
from payment.views import PayViewSet

app_name = PaymentConfig.name

router = DefaultRouter()
router.register(r'payment', PayViewSet, basename='payment')
urlpatterns = router.urls