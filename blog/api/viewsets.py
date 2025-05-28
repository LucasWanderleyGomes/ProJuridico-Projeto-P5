from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from blog.models import BlogPosts, BlogPostLike
from blog.api.serializer import BlogPostsSerializer
from comunidade.models import Comunidade
from rest_framework.pagination import LimitOffsetPagination
from drf_yasg.utils import swagger_auto_schema


class CustomLimitOffsetPagination(LimitOffsetPagination):

    """
    Criação de paginação personalizada para os eventos

    """

    default_limit = 15 
    max_limit = 100 
class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gerenciar posts de blog dentro de comunidades.

    def get_queryset(self): permite apenas a listagem de postagens de valor ATIVO=TRUE
    def destroy(self, request, *args, **kwargs): gerencia a permissão de deletar post dos outros + deleção lógica
    def perform_create(self, serializer):
        comunidade_pk = self.kwargs.get('comunidade_pk')
        comunidade = get_object_or_404(Comunidade, id=comunidade_pk)
        serializer.save(usuario=self.request.user, comunidade=comunidade, ativo=True)
        - Salva o usuário logado como autor da postagem, adiciona a comunidade 1 (padrão)
    """

    permission_classes = [IsAuthenticated]
    serializer_class = BlogPostsSerializer
    pagination_class = CustomLimitOffsetPagination

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        comunidade_pk = self.kwargs.get('comunidade_pk')
        qs = BlogPosts.objects.filter(ativo=True)
        if comunidade_pk:
            return qs.filter(comunidade_id=comunidade_pk)
        return qs

    def get_object(self):
        comunidade_pk = self.kwargs.get('comunidade_pk')
        blogpost_pk = self.kwargs.get('pk')
        queryset = BlogPosts.objects.filter(ativo=True, comunidade_id=comunidade_pk)
        return get_object_or_404(queryset, pk=blogpost_pk)

    def perform_create(self, serializer):
        comunidade_pk = self.kwargs.get('comunidade_pk')
        comunidade = get_object_or_404(Comunidade, id=comunidade_pk)
        serializer.save(usuario=self.request.user, comunidade=comunidade, ativo=True)

    def destroy(self, request, *args, **kwargs):
        blogpost = self.get_object()
        if request.user != blogpost.usuario:
            return Response({'message': 'Você não tem permissão para apagar esse post!'}, status=status.HTTP_403_FORBIDDEN)
        blogpost.ativo = False
        blogpost.save()
        return Response({'message': 'Postagem apagada com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
    
    @swagger_auto_schema(operation_description="Desativar um blog post (soft delete).")
    def destroy(self, request, *args, **kwargs):
        blogpost = self.get_object()
        if request.user != blogpost.usuario:
            return Response({'message': 'Você não tem permissão para apagar esse post!'}, status=status.HTTP_403_FORBIDDEN)
        blogpost.ativo = False
        blogpost.save()
        return Response({'message': 'Postagem apagada com sucesso.'}, status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        method='post',
        operation_description="Curtir ou descurtir um blog post.",
        responses={200: "Curtida removida", 201: "Curtido com sucesso!"}
    )
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, comunidade_pk=None, pk=None):
        blogpost = self.get_object()
        usuario = request.user

        like_obj, created = BlogPostLike.objects.get_or_create(
            usuario=usuario, blogpost=blogpost
        )

        if not created:
            like_obj.delete()
            return Response({'message': 'Curtida removida'}, status=status.HTTP_200_OK)

        return Response({'message': 'Curtido com sucesso!'}, status=status.HTTP_201_CREATED)