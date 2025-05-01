from rest_framework import serializers
from postagem.models import Postagem
from contas.api.serializer import UserReturnSerializer

class PostagemSerializer(serializers.ModelSerializer):

    usuario = UserReturnSerializer(read_only=True)
    
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
        read_only_fields = ['usuario', 'data_publicacao']