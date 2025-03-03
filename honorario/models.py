from django.db import models

# Create your models here.
class Honorario(models.Model):
    STATUS_HONORARIO_CHOICES = [
        ('PEN', 'Pendente'),
        ('PAG', 'Pago'),
    ]
    
    # advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    # processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=50)
    status = models.CharField(max_length=3, choices=STATUS_HONORARIO_CHOICES)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Honorário {self.valor}"
