from rest_framework import viewsets, permissions
from consulta.models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gerenciamento de Consultas.
    - permissão para todos os métodos (no entanto, as permissões para criar estão sendo gerenciadas no FRONT.)
    
    """
    
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()
    
    # def get_queryset(self):
    #     return Consulta.objects.filter(cliente=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(cliente=self.request.user)
