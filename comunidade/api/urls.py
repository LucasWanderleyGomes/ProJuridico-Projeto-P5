from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import ComunidadeViewSet
from postagem.api.viewsets import PostagemViewSet
from blog.api.viewsets import BlogPostViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('comunidades', ComunidadeViewSet)

# urls criadas para lidar com os eventos dentro da comunidade
eventos_router = DefaultRouter()
eventos_router.register(r'eventos', PostagemViewSet, basename='evento')

# urls criadas para lidar com os posts do blog dentro da comunidade
blogPosts_router = NestedDefaultRouter(router, r'comunidades', lookup='comunidade')
blogPosts_router.register(r'blogPosts', BlogPostViewSet, basename='comunidade-blogposts')

# blog_router = DefaultRouter()
# blog_router.register(r'blogPosts', BlogPostViewSet, basename='blogpost')

urlpatterns = [
    path('', include(router.urls)),
    path('comunidades/<int:comunidade_pk>/', include(eventos_router.urls)),
    path("comunidades/<int:comunidade_pk>/", include(blogPosts_router.urls)),
    # path('comunidades/<int:comunidade_pk>/', include(blog_router.urls)),
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
