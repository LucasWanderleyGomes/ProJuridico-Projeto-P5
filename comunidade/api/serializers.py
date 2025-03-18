from rest_framework import serializers
from comunidade.models import Comunidade
from postagem.api.serializers import PostagemSerializer

class ComunidadeSerializer(serializers.ModelSerializer):

    # relações com base na forma de primary keys (primary key related field) - ideal para sistemas 
    # com grande volume de registros, ideal para performance

    postagens = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comunidade
        fields = ['id', 'nome', 'descricao', 'regras', 'data_criacao', 'postagens']
