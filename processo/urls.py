from django.urls import path
from .views import ProcessosAPIView, ProcessoAPIView

urlpatterns = [
    path('processos/', ProcessosAPIView.as_view(), name='processos'),
    path('processos/<int:pk>', ProcessoAPIView.as_view(), name='processo')
]