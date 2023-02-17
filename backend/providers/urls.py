from pprint import pprint

from rest_framework.routers import DefaultRouter

from providers.views import ProductViewSet, ProviderViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product', )
router.register(r'providers', ProviderViewSet, basename='provider', )
urlpatterns = router.urls
