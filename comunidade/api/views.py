from rest_framework import viewsets
from comunidade.models import Comunidade
from .serializers import ComunidadeSerializer

class ComunidadeViewSet(viewsets.ModelViewSet):
    queryset = Comunidade.objects.all()
    serializer_class = ComunidadeSerializer
