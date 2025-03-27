from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from consulta.models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Consulta.objects.filter(email_cliente=self.request.user.email)

    def perform_create(self, serializer):
        serializer.save(email_cliente=self.request.user.email)

class ConfirmarConsultaAPIView(APIView):
    def post(self, request, consulta_pk):
        try:
            consulta = Consulta.objects.get(pk=consulta_pk, email_cliente=request.user.email)
            if consulta.status != 'agendada':
                return Response(
                    {'erro': 'Só é possível confirmar consultas agendadas'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            consulta.status = 'confirmada'
            consulta.save()
            return Response({'status': 'Consulta confirmada com sucesso'})
        except Consulta.DoesNotExist:
            return Response(
                {'erro': 'Consulta não encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )

class ReagendarConsultaAPIView(APIView):
    def post(self, request, consulta_pk):
        nova_data = request.data.get('nova_data_hora')
        if not nova_data:
            return Response(
                {'erro': 'Nova data/hora não fornecida'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            consulta = Consulta.objects.get(pk=consulta_pk, email_cliente=request.user.email)
            consulta.data_hora = nova_data
            consulta.status = 'agendada'
            consulta.save()
            return Response({'status': 'Consulta reagendada com sucesso'})
        except Consulta.DoesNotExist:
            return Response(
                {'erro': 'Consulta não encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )