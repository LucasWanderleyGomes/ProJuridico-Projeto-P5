from django.db import models

# Create your models here.
class Cliente(models.Model):
    # usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    cpf_cnpj = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.usuario.nome