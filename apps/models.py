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