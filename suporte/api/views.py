from rest_framework import viewsets
from suporte.models import Suporte
from .serializers import SuporteSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class SuporteViewSet(viewsets.ModelViewSet):

    """
    API para gerenciar solicitações de suporte dos usuários.
    
    Funcionalidades:
    - Listar todos os tickets de suporte
    - Criar uma nova solicitação
    - Filtrar por respondido/não respondido
    - Atualizar ou deletar um ticket
    """
     
    queryset = Suporte.objects.all()
    serializer_class = SuporteSerializer
    filterset_fields = ['respondido']  