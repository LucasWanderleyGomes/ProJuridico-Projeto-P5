from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import ComunidadeViewSet
from postagem.api.viewsets import PostagemViewSet
from blog.api.viewsets import BlogPostViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('comunidades', ComunidadeViewSet)

eventos_router = NestedDefaultRouter(router, r'comunidades', lookup='comunidade')
eventos_router.register(r'eventos', PostagemViewSet, basename='comunidade-eventos')

blogPosts_router = NestedDefaultRouter(router, r'comunidades', lookup='comunidade')
blogPosts_router.register(r'blogPosts', BlogPostViewSet, basename='comunidade-blogposts')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(eventos_router.urls)),
    path('', include(blogPosts_router.urls)),
]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ComunidadeViewSet
# from postagem.views import PostagensAPIView, PostagemAPIView
# from postagem.api.viewsets import PostagemViewSet
# from blog.api.viewsets import BlogPostViewSet
# from blog.views import BlogPostsAPIView, BlogPostAPIView

# router = DefaultRouter()
# router.register('comunidades', ComunidadeViewSet)
# router.register('eventos', PostagemViewSet)
# router.register('blogPosts', BlogPostViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('comunidades/<int:comunidade_pk>/postagens/', PostagensAPIView.as_view(), name='comunidade_postagens_list_create'),
#     path('comunidades/<int:comunidade_pk>/postagens/<int:postagem_pk>/', PostagemAPIView.as_view(), name='comunidade_postagens_retrieve_update_destroy'),
#     path('comunidades/<int:comunidade_pk>/blogPosts/', BlogPostsAPIView.as_view(), name='comunidade_blogPosts_list_create'),
#     path('comunidades/<int:comunidade_pk>/blogPosts/<int:blogPosts_pk>/', BlogPostAPIView.as_view(), name='comunidade_blogPosts_retrieve_update_destroy')
# ]
