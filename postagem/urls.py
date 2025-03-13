from django.urls import path
from.views import PostagensAPIView, PostagemAPIView

urlpatterns = [
    path('postagens/', PostagensAPIView.as_view(), name='postagens'),
    path('postagens/<int:pk>', PostagemAPIView.as_view(), name='postagem'),
]