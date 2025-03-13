from rest_framework import viewsets
from advogado.models import Advogado, Usuario
from advogado.api.serializer import AdvogadoSerializer, UsuarioSerializer

class AdvogadoViewSet(viewsets.ModelViewSet):
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer