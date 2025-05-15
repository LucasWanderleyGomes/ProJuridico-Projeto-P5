from rest_framework import serializers
from blog.models import BlogPosts
from contas.api.serializer import UserReturnSerializer

class BlogPostsSerializer(serializers.ModelSerializer):
    upload = serializers.ImageField(required=False, allow_null=True)
    usuario = UserReturnSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    has_liked = serializers.SerializerMethodField()

    class Meta:
        model = BlogPosts
        fields = (
            'id',
            'usuario',
            'comunidade',
            'upload',
            'titulo',
            'likes_count',
            'has_liked',
            'likes',
            'descricao',
            'criacao',
            'ativo'
            )
        read_only_fields = ['usuario', 'criacao']

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