from .views import DeliveryViewset
from rest_framework.routers import DefaultRouter


app_name = 'efi_world_api'
router = DefaultRouter()
router.register('delivery-details', DeliveryViewset, basename='delivery')
urlpatterns = router.urls
