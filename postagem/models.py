from django.db import models
from advogado.models import Usuario
from comunidade.models import Comunidade

# Create your models here.
class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True
class Postagem(Base):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comunidade = models.ForeignKey(Comunidade, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"

    def __str__(self):
        return self.titulo