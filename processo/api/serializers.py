from rest_framework import serializers
from processo.models import Processo

class ProcessoSerializer(serializers.ModelSerializer):
    """
    Serializa dados de um processo jurídico. atributos:
    - 'id'
    - 'categoria'
    - 'titulo'
    - 'descricao'
    - 'data_criacao'
    - 'criacao'
    - 'ativo'
    """
    
    class Meta:
        model = Processo
        fields = (
            'id',
            'categoria',
            'titulo',
            'descricao',
            'data_criacao',
            'criacao',
            'ativo'
        )