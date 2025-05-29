from rest_framework import viewsets, permissions
from consulta.models import Consulta
from .serializers import ConsultaSerializer
from rest_framework import filters

class ConsultaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gerenciamento de Consultas.
    - permissão para todos os métodos (no entanto, as permissões para criar estão sendo gerenciadas no FRONT.)
    
    """
    
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()
    filter_backends = [filters.SearchFilter]# permite uso de filtros
    search_fields = ['nome_cliente', 'assunto', 'descricao']  # agora a API aceita ?assunto=Negocios
    
    # def get_queryset(self):
    #     return Consulta.objects.filter(cliente=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(cliente=self.request.user)
