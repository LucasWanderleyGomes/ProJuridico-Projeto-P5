from rest_framework import serializers
from comunidade.models import Comunidade
from postagem.api.serializers import PostagemSerializer
from blog.api.serializer import BlogPostsSerializer

class ComunidadeSerializer(serializers.ModelSerializer):
    """
    Serializer para comunidades, incluindo relações com postagens e blogposts.
    Atributos do modelo: - id(automatico)
    - nome
    - descricao
    - regras
    - data_criacao(automatico)
    - postagens(outra tabela - eventos)
    - blogPosts(outra tabela - posts do blog)

    """

    postagens = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    blogPosts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comunidade
        fields = ['id', 'nome', 'descricao', 'regras', 'data_criacao', 'postagens', 'blogPosts']
