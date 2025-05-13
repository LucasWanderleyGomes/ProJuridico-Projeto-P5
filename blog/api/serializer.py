from rest_framework import serializers
from blog.models import BlogPosts
from contas.api.serializer import UserReturnSerializer

class BlogPostsSerializer(serializers.ModelSerializer):
    upload = serializers.ImageField(required=False, allow_null=True)
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

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get("request")
        if instance.upload and request:
            rep["upload"] = request.build_absolute_uri(instance.upload.url)
        else:
            rep["upload"] = None
        return rep