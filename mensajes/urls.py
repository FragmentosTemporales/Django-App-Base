from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MensajeViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'', MensajeViewSet, basename='mensaje')

urlpatterns = [
    path('', include(router.urls)),
]
