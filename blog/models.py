from django.db import models

# Create your models here.


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True
    

class BlogPosts(Base):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    upload = models.FileField(upload_to='blog',null=True, blank=True)
    tags = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['id']

    def __str__(self):
        return self.titulo