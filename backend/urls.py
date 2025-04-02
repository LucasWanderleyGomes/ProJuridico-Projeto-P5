
from django.contrib import admin
from django.urls import path, include
from postagem import urls
from processo import  urls
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from postagem.api.router import postagemRouter
from processo.api.router import processoRouter
from comunidade.api.urls import router
from advogado.api.urls import advogadoRouter
from contas.api.router import user_router


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    # path('api/v2/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v2/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("api/v2/auth/", include('djoser.urls')),
    path("api/v2/auth/", include('djoser.urls.jwt')),

    path("admin/", admin.site.urls),
    # path("api/v1/", include('advogado.api.urls')),
    # path("api/v1/", include('comunidade.api.urls')),
    # path("api/v1/", include("postagem.urls")),
    # path("api/v1/", include("processo.urls")),

    path("api/v2/", include(postagemRouter.urls)),
    path("api/v2/", include(processoRouter.urls)),
    path("api/v2/", include(router.urls)),
    path("api/v2/", include(advogadoRouter.urls)),
    path("api/v2/", include(user_router.urls)),
    path("api/v2/", include('consulta.api.urls')),
    
    #path('api/', include('api.urls')),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]
