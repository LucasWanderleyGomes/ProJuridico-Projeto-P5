from django.db import models

# Create your models here.

class Processo(models.Model):
    STATUS_PROCESSO_CHOICES = [
        ('ABE', 'Aberto'),
        ('AND', 'Em Andamento'),
        ('CON', 'Concluído'),
    ]
    
    numero_processo = models.CharField(max_length=50)
    # advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    # cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS_PROCESSO_CHOICES)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.numero_processo
