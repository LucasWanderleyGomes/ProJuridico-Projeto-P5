from rest_framework import serializers
from postagem.models import Postagem


class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = (
            'id',
            'usuario',
            'comunidade',
            'titulo',
            'conteudo',
            'data_publicacao',
            'criacao',
            'ativo'
        )