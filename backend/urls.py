
from django.contrib import admin
from django.urls import path, include
from postagem import urls
from processo import  urls
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('advogado.api.urls')),
    path('api/v1/', include('comunidade.api.urls')),
    path("api/v1/", include("postagem.urls")),
    path("api/v1/", include("processo.urls")),

    
    #path('api/', include('api.urls')),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]
