from rest_framework import generics
from .models import Postagem
from postagem.api.serializers import PostagemSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
# Create your views here.


# ============================== API VERSÃO 1  (V1) ==============================

class PostagensAPIView(generics.ListCreateAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

    def get_queryset(self):
        if self.kwargs.get('comunidade_pk'):
            return self.queryset.filter(comunidade_id = self.kwargs.get('comunidade_pk'))
        return self.queryset.all()

class PostagemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    lookup_url_kwarg = 'postagem_pk'  # Adicione isso

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {
            'pk': self.kwargs.get(self.lookup_url_kwarg),
            'comunidade_id': self.kwargs.get('comunidade_pk')
        }
        return get_object_or_404(queryset, **filter_kwargs)
# ============================== API VERSÃO 2  (V2) ==============================


class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer