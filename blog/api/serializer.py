from rest_framework import serializers
from blog.models import BlogPosts

class BlogPostsSerializer(serializers.ModelSerializer):
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