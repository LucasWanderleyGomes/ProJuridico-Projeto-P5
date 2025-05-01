from rest_framework import generics
from blog.models import BlogPosts
from blog.api.serializer import BlogPostsSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from comunidade.models import Comunidade
from rest_framework import status

class BlogPostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BlogPosts.objects.all()
    serializer_class = BlogPostsSerializer

    def perform_create(self, serializer):
        comunidade_padrão = get_object_or_404(Comunidade, id=1)
        serializer.save(usuario=self.request.user)

    def destroy(self, request, pk=None):
        try:
            blogpost = self.get_object()
            blogpost.ativo = False
            blogpost.save()
            return Response({'message':'Postagem "apagada" com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'erro':'Postagem não encontrada.'}, status=status.HTTP_404_NO_CONTENT)
        
    def get_queryset(self):
        return BlogPosts.objects.filter(ativo=True)