from rest_framework import generics
from postagem.models import Postagem
from postagem.api.serializers import PostagemSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
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
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer