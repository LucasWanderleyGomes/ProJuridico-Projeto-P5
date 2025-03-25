from django.db import models
from contas.models import User


class Advogado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    oab = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=100)
    escritorio = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.usuario.username
