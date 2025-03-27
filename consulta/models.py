from django.db import models

# Create your models here.
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from datetime import timedelta

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    participante = GenericForeignKey('content_type', 'object_id')

    nome_advogado = models.CharField(max_length=100)
    oab_advogado = models.CharField(max_length=20)
    email_cliente = models.EmailField()
    
    data_hora = models.DateTimeField()
    duracao = models.PositiveIntegerField(
        default=60,
        validators=[MinValueValidator(30)],
        help_text="Duração em minutos"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='agendada'
    )
    descricao = models.TextField(blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    numero_processo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['data_hora']
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f"Consulta {self.id} - {self.email_cliente} com {self.nome_advogado}"

    @property
    def horario_fim(self):
        return self.data_hora + timedelta(minutes=self.duracao)