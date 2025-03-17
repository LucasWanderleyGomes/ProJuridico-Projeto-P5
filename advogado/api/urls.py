from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvogadoViewSet, UsuarioViewSet

advogadoRouter = DefaultRouter()
advogadoRouter.register('advogado', AdvogadoViewSet)
advogadoRouter.register('usuario', UsuarioViewSet)

urlpatterns = [
    path('', include(advogadoRouter.urls))
]