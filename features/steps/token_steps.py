import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
import django
django.setup()

from behave import *
import requests
from django.contrib.auth import get_user_model

BASE_URL = "http://localhost:8000/api/v2"
HEADERS = {'Content-Type': 'application/json'}

@given('que eu tenho credenciais válidas')
def step_impl(context):

    User = get_user_model()
    user, created = User.objects.get_or_create(
        email="testes@gmail.com",
        defaults={
            'is_active': True,
            'is_staff': True
        }
    )
    if created:
        user.set_password('testes')
        user.save()
    
    context.auth_data = {
        "email": "testes@gmail.com",  
        "password": "teste"         
    }
    context.base_url = BASE_URL
    context.headers = HEADERS

@when('eu solicito um token')
def step_impl(context):
    url = f"{context.base_url}/token/"
    try:
        context.response = requests.post(
            url, 
            json=context.auth_data, 
            headers=context.headers,
            timeout=5
        )
    except requests.exceptions.ConnectionError as e:
        raise Exception(f"Falha ao conectar com a API: {str(e)}. Verifique se o servidor Django está rodando.")

@then('o sistema deve retornar um token válido')
def step_impl(context):
    print(f"\nDEBUG - Resposta da API: {context.response.text}")  # Para ajudar no debug
    assert context.response.status_code == 200, \
        f"Status code inválido: {context.response.status_code}. Resposta: {context.response.text}"
    response_json = context.response.json()
    assert 'access' in response_json, "Token de acesso não encontrado na resposta"
    assert 'refresh' in response_json, "Token de refresh não encontrado na resposta"

@given('que eu tenho credenciais inválidas')
def step_impl(context):
    context.auth_data = {
        "email": "testes@gmail.com",  
        "password": "senha_errada"     
    }
    context.base_url = BASE_URL
    context.headers = HEADERS

@then('o sistema deve retornar um erro de autenticação')
def step_impl(context):
    print(f"\nDEBUG - Resposta da API: {context.response.text}")  
    assert context.response.status_code == 401, \
        f"Esperado 401, recebido {context.response.status_code}. Resposta: {context.response.text}"