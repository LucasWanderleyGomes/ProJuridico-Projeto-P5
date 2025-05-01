from rest_framework import generics
from postagem.models import Postagem
from postagem.api.serializers import PostagemSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from comunidade.models import Comunidade
from rest_framework import status

# Create your views here.


# ============================== API VERSÃO 1  (V1) ==============================

# class PostagensAPIView(generics.ListCreateAPIView):
#     queryset = Postagem.objects.all()
#     serializer_class = PostagemSerializer

#     def get_queryset(self):
#         if self.kwargs.get('comunidade_pk'):
#             return self.queryset.filter(comunidade_id = self.kwargs.get('comunidade_pk'))
#         return self.queryset.all()

# class PostagemAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Postagem.objects.all()
#     serializer_class = PostagemSerializer

#     def get_object(self):
#         if self.kwargs.get('comunidade_pk'):
#             return get_object_or_404(self.get_queryset(), comunidade_id = self.kwargs.get('comunidade_pk'), pk=self.kwargs.get('postagem_pk'))
#         return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('postagem_pk'))
    

# ============================== API VERSÃO 2  (V2) ==============================


class PostagemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    
    def perform_create(self, serializer):
        comunidade_padrao = get_object_or_404(Comunidade, id=1)
        serializer.save(usuario=self.request.user, comunidade=comunidade_padrao)

    def destroy(self, request, pk=None):
        try:
            postagem = self.get_object()
            postagem.ativo = False
            postagem.save()
            return Response({'message':'Evento "apagado" com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
        except Postagem.DoesNotExist:
            return Response({'erro': 'Evento não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        return Postagem.objects.filter(ativo=True)