from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('ADV', 'Advogado'),
        ('CLI', 'Cliente'),
        ('ADM', 'Administrador'),
    ]
    
    tipo = models.CharField(max_length=3, choices=TIPO_USUARIO_CHOICES)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    # Adicione related_name personalizado para evitar conflitos
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="usuario_groups",  # Nome único para o relacionamento reverso
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="usuario_permissions",  # Nome único para o relacionamento reverso
        related_query_name="usuario",
    )

    def __str__(self):
        return self.username
class Advogado(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    oab = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=100)
    escritorio = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.usuario.nome

class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    cpf_cnpj = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.usuario.nome

class Processo(models.Model):
    STATUS_PROCESSO_CHOICES = [
        ('ABE', 'Aberto'),
        ('AND', 'Em Andamento'),
        ('CON', 'Concluído'),
    ]
    
    numero_processo = models.CharField(max_length=50)
    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS_PROCESSO_CHOICES)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.numero_processo

class ReuniaoConsulta(models.Model):
    STATUS_REUNIAO_CHOICES = [
        ('AGE', 'Agendada'),
        ('REA', 'Realizada'),
        ('CAN', 'Cancelada'),
    ]
    
    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=200)
    motivo = models.TextField()
    status = models.CharField(max_length=3, choices=STATUS_REUNIAO_CHOICES)

    def __str__(self):
        return f"Reunião {self.id} - {self.advogado.usuario.nome} e {self.cliente.usuario.nome}"

class Honorario(models.Model):
    STATUS_HONORARIO_CHOICES = [
        ('PEN', 'Pendente'),
        ('PAG', 'Pago'),
    ]
    
    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=50)
    status = models.CharField(max_length=3, choices=STATUS_HONORARIO_CHOICES)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Honorário {self.id} - {self.advogado.usuario.nome}"

class RelatorioFinanceiro(models.Model):
    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=50)
    receita_total = models.DecimalField(max_digits=10, decimal_places=2)
    despesas_totais = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    data_geracao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Relatório {self.id} - {self.advogado.usuario.nome}"

class Comunidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    regras = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Postagem(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comunidade = models.ForeignKey(Comunidade, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=200)
    comunidade = models.ForeignKey(Comunidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome