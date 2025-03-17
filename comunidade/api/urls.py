from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComunidadeViewSet
from postagem.views import PostagensAPIView, PostagemAPIView

router = DefaultRouter()
router.register('comunidades', ComunidadeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comunidades/<int:comunidade_pk>/postagens', PostagensAPIView.as_view() , name='comunidade_postagens'),
    path('comunidades/<int:comunidade_pk>/postagens/<int:postagem_pk>', PostagemAPIView.as_view(), name='comunidade_postagem'),
]
