from rest_framework import serializers
from consulta.models import Consulta
from django.utils import timezone

class ConsultaSerializer(serializers.ModelSerializer):
    """
    Serializer para modelo de Consulta. atributos:
    - 'id'
    - 'nome_cliente' 
    - 'assunto' 
    - 'descricao' 
    - 'numero_processo'
    - 'criacao'
    - 'atualizacao'
    - 'ativo'

    """
    class Meta:
        model = Consulta
        fields = [
            'id', 'nome_cliente', 'assunto' ,'descricao', 'numero_processo', 'criacao', 'atualizacao', 'ativo'
        ]
        read_only_fields = ['criacao', 'atualizacao']

    def validate(self, data):

        return data
