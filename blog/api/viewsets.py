from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from blog.models import BlogPosts
from blog.api.serializer import BlogPostsSerializer
from comunidade.models import Comunidade

class BlogPostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogPostsSerializer

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
