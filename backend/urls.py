
from django.contrib import admin
from django.urls import path, include
from postagem import urls
from processo import  urls
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
# from postagem.api.router import postagemRouter
from processo.api.router import processoRouter
from comunidade.api.urls import router as comunidadeRouter, eventos_router, blog_router
from contas.api.router import user_router
from suporte.api.urls import router as suporteRouter
from blog.api.router import blogPostRouter


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # path('api/v2/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v2/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("api/v2/auth/", include('djoser.urls')),
    path("api/v2/auth/", include('djoser.urls.jwt')),

    path("admin/", admin.site.urls),
    # path("api/v1/", include('advogado.api.urls')),
    # path("api/v1/", include('comunidade.api.urls')),
    # path("api/v1/", include("postagem.urls")),
    # path("api/v1/", include("processo.urls")),

   #  path("api/v2/", include(postagemRouter.urls)),
    path("api/v2/", include(processoRouter.urls)),
    path("api/v2/", include(comunidadeRouter.urls)),
    path("api/v2/comunidades/<int:comunidade_pk>/", include(eventos_router.urls)), # Rotas aninhadas para eventos
    path("api/v2/comunidades/<int:comunidade_pk>/", include(blog_router.urls)), # Rotas aninhadas para blog posts
    path("api/v2/", include(user_router.urls)),
    path("api/v2/", include('consulta.api.urls')),
    path("api/v2/", include('suporte.api.urls')),
    path("api/v2/", include(blogPostRouter.urls)),
    
    #path('api/', include('api.urls')),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
