from rest_framework import viewsets, mixins
from comunidade.models import Comunidade
from .serializers import ComunidadeSerializer
from postagem.api.serializers import PostagemSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response


class ComunidadeViewSet(viewsets.ModelViewSet):
    queryset = Comunidade.objects.all()
    serializer_class = ComunidadeSerializer
    
    @action(detail=True, methods=['get'])
    def postagens(self, request, pk=None):
        comunidade = self.get_object()
        serializer = PostagemSerializer(comunidade.postagem_set.all(), many=True)
        return Response(serializer.data)