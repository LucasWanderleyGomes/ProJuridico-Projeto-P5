from rest_framework import serializers
from blog.models import BlogPosts
from contas.api.serializer import UserReturnSerializer

class BlogPostsSerializer(serializers.ModelSerializer):
    usuario = UserReturnSerializer(read_only=True)
    class Meta:
        model = BlogPosts
        fields = (
            'id',
            'usuario',
            'comunidade',
            'titulo',
            'descricao',
            'criacao',
            'ativo'
            )
        read_only_fields = ['usuario', 'criacao']