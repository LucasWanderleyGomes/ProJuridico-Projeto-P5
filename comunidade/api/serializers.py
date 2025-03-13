from rest_framework import serializers
from comunidade.models import Comunidade

class ComunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidade
        fields = ['id', 'nome', 'descricao', 'regras', 'data_criacao']
