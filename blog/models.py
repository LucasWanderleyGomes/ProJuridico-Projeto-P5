from django.db import models
from comunidade.models import Comunidade
from contas.models import User

# Create your models here.


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True
    

class BlogPosts(Base):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(null=True, blank=True)
    upload = models.FileField(upload_to='blog')
    tags = models.CharField(max_length=255, null=True, blank=True)
    comunidade = models.ForeignKey(Comunidade, on_delete=models.CASCADE, related_name='blogPosts', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['id']

    def __str__(self):
        return self.titulo