from rest_framework import viewsets
from suporte.models import Suporte
from .serializers import SuporteSerializer

class SuporteViewSet(viewsets.ModelViewSet):
    queryset = Suporte.objects.all()
    serializer_class = SuporteSerializer
    filterset_fields = ['respondido']  # Permite filtrar por ?respondido=true/false