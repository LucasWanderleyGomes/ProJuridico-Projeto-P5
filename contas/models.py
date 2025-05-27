from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido')
        email = self.normalize_email(email)
        
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser deve ter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser deve ter is_superuser=True.")

        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': "Já existe um usuário com este email.",
        }
    )
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Obrigatório. 150 caracteres ou menos.',
        error_messages={
            'unique': "Já existe um usuário com este username.",
        }
    )
    descricao_pessoal = models.TextField(null=True, blank=True)
    cnpj = models.TextField(null=True, blank=True)
    data_de_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    insta = models.TextField(null=True, blank=True)
    whats = models.TextField(null=True, blank=True)
    linkedin = models.TextField(null=True, blank=True)
    contato = models.CharField(max_length=255, null=True, blank=True)

    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions",
        related_query_name="user",
    )

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'