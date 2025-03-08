# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, AdvogadoViewSet, ComunidadeViewSet, PostagemViewSet, EventoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'advogados', AdvogadoViewSet)
router.register(r'comunidades', ComunidadeViewSet)
router.register(r'postagens', PostagemViewSet)
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]