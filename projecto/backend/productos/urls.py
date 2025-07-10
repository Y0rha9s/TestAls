from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

# Crear router para las APIs
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]