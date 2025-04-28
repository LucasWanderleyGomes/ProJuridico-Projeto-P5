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


class ComunidadeViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]

    queryset = Comunidade.objects.all()
    serializer_class = ComunidadeSerializer
    
    @action(detail=True, methods=['get'])
    def postagens(self, request, pk=None):

        # paginação
        self.pagination_class.page_size = 10
        postagens = Postagem.objects.filter(comunidade_id=pk)
        page = self.paginate_queryset(postagens)

        if page is not None:
             serializer = PostagemSerializer(page, many=True)
             return self.get_paginated_response(serializer.data)

        serializer = PostagemSerializer(postagens.all(), many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def blogPosts(self, request, pk=None):
        self.pagination_class.page_size = 10
        blogPosts = BlogPosts.objects.filter(comunidade_id=pk)
        page = self.paginate_queryset(blogPosts)
        if page is not None:
            serializer = BlogPostsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = BlogPostsSerializer(blogPosts.all(), many=True)
        return Response(serializer.data)