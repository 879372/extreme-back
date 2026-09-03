from rest_framework.routers import DefaultRouter
from .views import BillingSettingsViewSet, ChargeViewSet, ClientViewSet
router = DefaultRouter()
router.register("clients", ClientViewSet)
router.register("charges", ChargeViewSet)
router.register("billing-settings", BillingSettingsViewSet)
urlpatterns = router.urls
