import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
import django
django.setup()

from behave import given, when, then
import requests
from consulta.models import Consulta

BASE_URL = "http://localhost:8000/api/v2"
HEADERS = {'Content-Type': 'application/json'}

@given('que o endpoint de consultas está disponível')
def step_endpoint_consultas_disponivel(context):
    try:
        response = requests.get(f"{BASE_URL}/consultas/", timeout=5)
        context.available = response.status_code < 500
    except requests.exceptions.RequestException:
        context.available = False
    assert context.available, "Endpoint de consultas não está disponível"

@when('eu envio os dados de uma nova consulta:')
def step_envia_dados_consulta(context):
    data = {row['campo']: row['valor'].strip('"') for row in context.table}
    context.response = requests.post(
        f"{BASE_URL}/consultas/",
        json=data,
        headers=HEADERS
    )

@then('a consulta deve ser criada no banco de dados')
def step_verifica_consulta_banco(context):
    response_json = context.response.json()
    assert Consulta.objects.filter(id=response_json['id']).exists(), \
        f"Consulta com ID {response_json['id']} não encontrada no banco"