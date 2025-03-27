from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultaViewSet, ConfirmarConsultaAPIView, ReagendarConsultaAPIView

router = DefaultRouter()
router.register('consultas', ConsultaViewSet, basename='consulta')

urlpatterns = [
    path('', include(router.urls)),
    path('consultas/<int:consulta_pk>/confirmar/', ConfirmarConsultaAPIView.as_view(), name='consulta-confirmar'),
    path('consultas/<int:consulta_pk>/reagendar/', ReagendarConsultaAPIView.as_view(), name='consulta-reagendar'),
]