from behave import *
from contas.models import User
from consulta.models import Consulta
from django.test import Client 
from django.urls import reverse
import requests

@given('eu tenho as credenciais válidas')
def step_impl(context):
    context.auth_data = {
        "email" : "admin@gmail.com",
        "password" : "admin"
    }

@when('eu solicito um token')
def step_impl(context):
    url = f"{context.base_url}/token/"
    response = requests.post(url, json=context.auth_data, headers=context.headers)
    context.response = response

@then('o sistema deve retornar um token válido')
def step_impl(context):
    assert context.response.status_code == 200
    assert 'access' in context.response.json()
    assert 'refresh' in context.response.json()

@given('que eu tenho credenciais inválidas')
def step_impl(context):
    context.auth_data = {
        "email": "admin",
        "password": "senha_errada"
    }

then('o sistema deve retornar um erro de autenticação')
def step_impl(context):
    assert context.response.status_code == 401