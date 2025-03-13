from rest_framework import generics
from .models import Postagem
from postagem.api.serializers import PostagemSerializer
# Create your views here.

class PostagensAPIView(generics.ListCreateAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

class PostagemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer