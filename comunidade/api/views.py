from rest_framework import viewsets, mixins
from comunidade.models import Comunidade
from .serializers import ComunidadeSerializer
from postagem.api.serializers import PostagemSerializer
from postagem.models import Postagem
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response


class ComunidadeViewSet(viewsets.ModelViewSet):
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