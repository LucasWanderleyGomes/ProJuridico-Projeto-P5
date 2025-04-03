import os
import subprocess
import time
import django
from behave import *

def before_all(context):
    """Configuração global antes de todos os testes"""
    # Configura o Django
    os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
    django.setup()
    
    # Configurações da API
    context.url_base = "http://localhost:8000/api/v2"
    context.headers = {'Content-Type': 'application/json'}
    
    # Inicia servidor de teste
    context.server_process = subprocess.Popen(
        ["python", "manage.py", "runserver"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(3)  # Espera o servidor iniciar

def after_scenario(context, scenario):
    """Limpeza após cada cenário"""
    from django.contrib.auth import get_user_model
    User = get_user_model()
    User.objects.filter(
        email__in=["novo@teste.com", "admin@teste.com", "duplicado@teste.com"]
    ).delete()

def after_all(context):
    """Finalização após todos os testes"""
    if hasattr(context, 'server_process'):
        context.server_process.terminate()