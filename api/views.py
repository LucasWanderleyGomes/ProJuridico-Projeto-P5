# api/views.py
from rest_framework import viewsets, permissions, generics
from apps.models import Usuario, Advogado, Comunidade, Postagem, Evento
from .serializers import UsuarioSerializer, AdvogadoSerializer, ComunidadeSerializer, PostagemSerializer, EventoSerializer
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class AdvogadoViewSet(viewsets.ModelViewSet):
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComunidadeViewSet(viewsets.ModelViewSet):
    queryset = Comunidade.objects.all()
    serializer_class = ComunidadeSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [permissions.IsAuthenticated]