from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComunidadeViewSet
from postagem.views import PostagensAPIView, PostagemAPIView
from postagem.api.viewsets import PostagemViewSet
from blog.api.viewsets import BlogPostViewSet
from blog.views import BlogPostsAPIView, BlogPostAPIView

router = DefaultRouter()
router.register('comunidades', ComunidadeViewSet)
router.register('postagens', PostagemViewSet)
router.register('blogPosts', BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comunidades/<int:comunidade_pk>/postagens/', PostagensAPIView.as_view(), name='comunidade_postagens_list_create'),
    path('comunidades/<int:comunidade_pk>/postagens/<int:postagem_pk>/', PostagemAPIView.as_view(), name='comunidade_postagens_retrieve_update_destroy'),
    path('comunidades/<int:comunidade_pk>/blogPosts/', BlogPostsAPIView.as_view(), name='comunidade_blogPosts_list_create'),
    path('comunidades/<int:comunidade_pk>/blogPosts/<int:blogPosts_pk>/', BlogPostAPIView.as_view(), name='comunidade_blogPosts_retrieve_update_destroy')
]
