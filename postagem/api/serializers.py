from rest_framework import serializers
from postagem.models import Postagem
from contas.api.serializer import UserReturnSerializer

class PostagemSerializer(serializers.ModelSerializer):
    upload = serializers.ImageField(required=False, allow_null=True)
    usuario = UserReturnSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    has_liked = serializers.SerializerMethodField()
    
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
            'likes_count',
            'has_liked',
            'data_publicacao',
            'criacao',
            'ativo'
        )
        read_only_fields = ['usuario', 'data_publicacao']

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    
    def get_has_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.likes.filter(usuario=user).exists()
        return False

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get("request")
        if instance.upload and request:
            rep["upload"] = request.build_absolute_uri(instance.upload.url)
        else:
            rep["upload"] = None
        return rep