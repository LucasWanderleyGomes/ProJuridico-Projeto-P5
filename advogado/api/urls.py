from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvogadoViewSet

advogadoRouter = DefaultRouter()
advogadoRouter.register('advogado', AdvogadoViewSet)

urlpatterns = [
    path('', include(advogadoRouter.urls))
]