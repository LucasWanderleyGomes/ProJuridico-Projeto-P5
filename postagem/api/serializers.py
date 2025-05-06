from rest_framework import serializers
from postagem.models import Postagem
from contas.api.serializer import UserReturnSerializer

class PostagemSerializer(serializers.ModelSerializer):
    upload = serializers.SerializerMethodField()
    usuario = UserReturnSerializer(read_only=True)
    
    class Meta:
        model = Postagem
        fields = (
            'id',
            'usuario',
            'comunidade',
            'titulo',
            'conteudo',
            'upload',
            'likes',
            'data_publicacao',
            'criacao',
            'ativo'
        )
        read_only_fields = ['usuario', 'data_publicacao']

    def get_upload(self, obj):
        if obj.upload:
            return self.context['request'].build_absolute_uri(obj.upload.url)
        return None