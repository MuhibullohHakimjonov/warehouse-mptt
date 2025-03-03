from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]