from rest_framework import serializers
from consulta.models import Consulta
from django.contrib.auth import get_user_model
from django.utils import timezone

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = [
            'id', 'nome_advogado', 'oab_advogado', 'email_cliente',
            'data_hora', 'duracao', 'status', 'descricao', 'valor',
            'numero_processo', 'horario_fim'
        ]
        read_only_fields = ['status']

    def validate(self, data):
        if data['data_hora'] < timezone.now():
            raise serializers.ValidationError("Não é possível agendar no passado")
        return data