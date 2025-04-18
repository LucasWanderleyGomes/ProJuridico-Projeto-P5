from django.db import models
from contas.models import User
from datetime import timedelta
from django.core.validators import MinValueValidator


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Consulta(Base):
    descricao = models.TextField(blank=True)  # Descrição/Detalhes da consulta
    nome_cliente = models.CharField(max_length=255)  # Nome do cliente
    numero_processo = models.CharField(max_length=50)  # Número do processo
    assunto = models.CharField(max_length=255)

    class Meta:
        ordering = ['criacao']
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f"Consulta {self.id} - Cliente: {self.nome_cliente} | Processo: {self.numero_processo}"
