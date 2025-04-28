from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from blog.models import BlogPosts
from blog.api.serializer import BlogPostsSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins

class BlogPostsAPIView(generics.ListCreateAPIView):
    queryset = BlogPosts.objects.all()
    serializer_class = BlogPostsSerializer

    def get_queryset(self):
        if self.kwargs.get('comunidade_pk'):
            return self.queryset.filter(comunidade_id = self.kwargs.get('comunidade_pk'))
        return self.queryset.all()

class BlogPostAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPosts.objects.all()
    serializer_class = BlogPostsSerializer
    lookup_url_kwarg = 'blogPosts_pk'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {
            'pk': self.kwargs.get(self.lookup_url_kwarg),
            'comunidade_id': self.kwargs.get('comunidade_pk')
        }
        return get_object_or_404(queryset, **filter_kwargs)