from rest_framework import viewsets, mixins
from comunidade.models import Comunidade
from .serializers import ComunidadeSerializer
from postagem.api.serializers import PostagemSerializer
from blog.api.serializer import BlogPostsSerializer
from postagem.models import Postagem
from blog.models import BlogPosts
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

class ComunidadeViewSet(viewsets.ModelViewSet):

    """
    API endpoint para gerenciar comunidades.

    def postagens(self, request, pk=None):
        
        Esse método retornará os detalhes dos eventos envolvidos na comunidade
    """
    permission_classes = [IsAuthenticated]
    queryset = Comunidade.objects.all()
    serializer_class = ComunidadeSerializer

    @swagger_auto_schema(
        operation_description="Listar postagens da comunidade.",
        responses={200: PostagemSerializer(many=True)}
    )
    @action(detail=True, methods=['get'])
    def postagens(self, request, pk=None):
        self.pagination_class.page_size = 20
        postagens = Postagem.objects.filter(comunidade_id=pk)
        page = self.paginate_queryset(postagens)

        if page is not None:
            serializer = PostagemSerializer(page, many=True, context={'request': request}) 
            return self.get_paginated_response(serializer.data)

        serializer = PostagemSerializer(postagens.all(), many=True, context={'request': request}) 
        return Response(serializer.data)