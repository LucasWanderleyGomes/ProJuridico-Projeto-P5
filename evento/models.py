from django.db import models

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=200)
    # comunidade = models.ForeignKey(Comunidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome