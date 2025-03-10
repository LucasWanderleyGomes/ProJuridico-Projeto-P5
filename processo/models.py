from django.db import models

class Processo(models.Model):
    categoria = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo