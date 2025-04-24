import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
import django
django.setup()

from behave import given, when, then
import requests
from processo.models import Processo

BASE_URL = "http://localhost:8000/api/v2"
HEADERS = {'Content-Type': 'application/json'}

@given('que o endpoint de processos está disponível')
def step_endpoint_processos_disponivel(context):
    try:
        response = requests.get(f"{BASE_URL}/processos/", timeout=5)
        context.available = response.status_code < 500
    except requests.exceptions.RequestException:
        context.available = False
    assert context.available, "Endpoint de processos não está disponível"

@when('eu envio os dados de um novo processo:')
def step_envia_dados_processo(context):
    data = {row['campo']: row['valor'].strip('"') for row in context.table}
    context.response = requests.post(
        f"{BASE_URL}/processos/",
        json=data,
        headers=HEADERS
    )

@then('o processo deve ser criado no banco de dados')
def step_verifica_processo_banco(context):
    response_json = context.response.json()
    assert Processo.objects.filter(id=response_json['id']).exists(), \
        f"Processo com ID {response_json['id']} não encontrado no banco"