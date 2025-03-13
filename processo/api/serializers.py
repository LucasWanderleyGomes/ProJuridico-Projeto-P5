from rest_framework import serializers
from processo.models import Processo

class ProcessoSerializer(serializers.ModelSerializer):
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