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

    
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from postagem.models import Postagem
from postagem.models import Likes
from .serializers import PostagemSerializer
from comunidade.models import Comunidade
from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 15 
    max_limit = 100 

class PostagemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostagemSerializer
    pagination_class = CustomLimitOffsetPagination

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        comunidade_pk = self.kwargs.get('comunidade_pk')
        if comunidade_pk:
            return Postagem.objects.filter(ativo=True, comunidade_id=comunidade_pk)
        return Postagem.objects.filter(ativo=True)

    def get_object(self):
        comunidade_pk = self.kwargs.get('comunidade_pk')
        pk = self.kwargs.get('pk')
        queryset = Postagem.objects.filter(ativo=True, comunidade_id=comunidade_pk)
        return get_object_or_404(queryset, pk=pk)

    def perform_create(self, serializer):
        comunidade_pk = self.kwargs.get('comunidade_pk')
        comunidade = get_object_or_404(Comunidade, id=comunidade_pk)
        serializer.save(usuario=self.request.user, comunidade=comunidade)

    def destroy(self, request, *args, **kwargs):
        postagem = self.get_object()
        if request.user != postagem.usuario:
            return Response({'message': 'Esse usuário não tem permissão de apagar essa publicação!'}, status=status.HTTP_403_FORBIDDEN)
        postagem.ativo = False
        postagem.save()
        return Response({'message': 'Evento "apagado" com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, comunidade_pk=None, pk=None):
        postagem = self.get_object()
        user = request.user

        like, created = Likes.objects.get_or_create(usuario=user, evento=postagem)

        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        return Response({
            'liked': liked,
            'likes_count': postagem.likes.count(),
        }, status=status.HTTP_200_OK)