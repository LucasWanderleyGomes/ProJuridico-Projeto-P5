from rest_framework import viewsets, permissions
from consulta.models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Consulta.objects.all()
    
    # def get_queryset(self):
    #     return Consulta.objects.filter(cliente=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(cliente=self.request.user)
