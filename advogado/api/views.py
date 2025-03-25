from rest_framework import viewsets
from advogado.models import Advogado
from advogado.api.serializer import AdvogadoSerializer

class AdvogadoViewSet(viewsets.ModelViewSet):
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer
