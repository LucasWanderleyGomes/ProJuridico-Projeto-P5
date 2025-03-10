from django.db import models
from advogado.models import Usuario
from comunidade.models import Comunidade

# Create your models here.
class Postagem(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comunidade = models.ForeignKey(Comunidade, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo