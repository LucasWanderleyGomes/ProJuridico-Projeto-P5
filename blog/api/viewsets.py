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
    queryset = BlogPosts.objects.filter(ativo=True)

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        comunidade_pk = self.kwargs.get('comunidade_pk')
        if comunidade_pk:
            return self.queryset.filter(comunidade_id=comunidade_pk)
        return self.queryset 

    def perform_create(self, serializer):
        comunidade_pk = self.kwargs.get('comunidade_pk')
        comunidade = get_object_or_404(Comunidade, id=comunidade_pk)
        serializer.save(usuario=self.request.user, comunidade=comunidade)

    def destroy(self, request, pk=None):
        try:
            blogpost = self.get_object()
            blogpost.ativo = False
            blogpost.save()
            return Response({'message':'Postagem "apagada" com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
        except BlogPosts.DoesNotExist:
            return Response({'erro':'Postagem não encontrada.'}, status=status.HTTP_404_NOT_FOUND)