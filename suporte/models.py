from django.db import models

class Suporte(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    respondido = models.BooleanField(default=False, verbose_name='Respondido?')

    class Meta:
        db_table = 'suporte'  

    def __str__(self):
        return f"{self.nome} - {self.criado_em}"