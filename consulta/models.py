from django.db import models

# Create your models here.
class Consulta(models.Model):
    STATUS_REUNIAO_CHOICES = [
        ('AGE', 'Agendada'),
        ('REA', 'Realizada'),
        ('CAN', 'Cancelada'),
    ]
    
    # advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    # cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=200)
    motivo = models.TextField()
    status = models.CharField(max_length=3, choices=STATUS_REUNIAO_CHOICES)
