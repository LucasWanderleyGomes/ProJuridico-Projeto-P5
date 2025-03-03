from django.db import models

# Create your models here.

class Relatorio(models.Model):
    # advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=50)
    receita_total = models.DecimalField(max_digits=10, decimal_places=2)
    despesas_totais = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    data_geracao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Relatório {self.id} - {self.advogado.usuario.nome}"