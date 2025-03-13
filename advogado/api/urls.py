from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvogadoViewSet, UsuarioViewSet

router = DefaultRouter()
router.register('advogado', AdvogadoViewSet)
router.register('usuario', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls))
]