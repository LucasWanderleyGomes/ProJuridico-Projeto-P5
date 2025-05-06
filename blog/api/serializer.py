from rest_framework import serializers
from blog.models import BlogPosts
from contas.api.serializer import UserReturnSerializer

class BlogPostsSerializer(serializers.ModelSerializer):
    upload = serializers.SerializerMethodField()
    usuario = UserReturnSerializer(read_only=True)
    class Meta:
        model = BlogPosts
        fields = (
            'id',
            'usuario',
            'comunidade',
            'upload',
            'titulo',
            'likes',
            'descricao',
            'criacao',
            'ativo'
            )
        read_only_fields = ['usuario', 'criacao']

    def get_upload(self, obj):
        if obj.upload:
            return self.context['request'].build_absolute_uri(obj.upload.url)
        return None