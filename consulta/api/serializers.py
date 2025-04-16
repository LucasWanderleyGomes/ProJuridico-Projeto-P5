from rest_framework import serializers
from consulta.models import Consulta
from django.utils import timezone

class ConsultaSerializer(serializers.ModelSerializer):
    # O campo 'horario_fim' não é mais necessário, já que removemos a duração
    # cliente = serializers.PrimaryKeyRelatedField(read_only=True)  # Removido, pois cliente é apenas um campo de texto agora.
    
    class Meta:
        model = Consulta
        fields = [
            'id', 'nome_cliente', 'descricao', 'numero_processo', 'criacao', 'atualizacao', 'ativo'
        ]
        read_only_fields = ['criacao', 'atualizacao']

    def validate(self, data):
        # Não há mais validação de data_hora, pois foi removido o campo data_hora
        return data
