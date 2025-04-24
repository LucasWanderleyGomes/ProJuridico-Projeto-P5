import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
import django
django.setup()

from behave import *
import requests
import json
from suporte.models import Suporte


BASE_URL = "http://localhost:8000/api/v2"  
HEADERS = {'Content-Type': 'application/json'}

@given('que a API de suporte está disponível')
def step_api_suporte_disponivel(context):
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        context.available = response.status_code < 500
    except requests.exceptions.RequestException:
        context.available = False
    
    assert context.available, "API não está respondendo"

@when('eu envio uma mensagem de suporte com:')
def step_envia_mensagem_suporte(context):
    data = {
        "nome": context.table.rows[0]['nome'].strip('"'),
        "email": context.table.rows[0]['email'].strip('"'),
        "mensagem": context.table.rows[0]['mensagem'].strip('"')
    }
    
    context.response = requests.post(
        f"{BASE_URL}/mensagens/",  
        json=data,
        headers=HEADERS
    )

@then('a mensagem é registrada com sucesso')
def step_mensagem_registrada(context):
    print(f"DEBUG - Resposta: {context.response.status_code} - {context.response.text}")  # Para ajudar no debug
    assert context.response.status_code == 201, \
        f"Esperado 201, recebido {context.response.status_code}. Resposta: {context.response.text}"
    response_json = context.response.json()
    assert 'id' in response_json, "Campo 'id' não encontrado na resposta"
    
    # Verifica persistência
    assert Suporte.objects.filter(id=response_json['id']).exists()