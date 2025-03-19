from django.db import models

# Create your models here.
class Comunidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    regras = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comunidade"
        verbose_name_plural = "Comunidades"
        ordering = ['id']

    def __str__(self):
        return self.nome

