from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuporteViewSet


router = DefaultRouter()
router.register('mensagens', SuporteViewSet, basename='suporte-mensagens')

urlpatterns = [
    path('', include(router.urls)),
]