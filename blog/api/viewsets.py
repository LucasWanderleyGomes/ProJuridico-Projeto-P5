from rest_framework import generics
from blog.models import BlogPosts
from blog.api.serializer import BlogPostsSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

class BlogPostViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = BlogPosts.objects.all()
    serializer_class = BlogPostsSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)