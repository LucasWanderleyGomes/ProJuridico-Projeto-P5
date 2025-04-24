from behave import given, when, then
import requests
from django.contrib.auth import get_user_model


def get_user_model_safe(context):
    if not hasattr(context, 'User'):
        from django.contrib.auth import get_user_model
        context.User = get_user_model()
    return context.User


@given('que eu tenho os seguintes dados válidos:')
def step_impl(context):
    User = get_user_model_safe(context)
    context.user_data = {
        "email": context.table[0]["email"],
        "username": context.table[0]["username"],
        "password": context.table[0]["password"]
    }

@when('eu envio uma requisição POST para "/api/v2/signup/"')
def step_impl(context):
    url = f"{context.url_base}/signup/"
    context.response = requests.post(
        url, 
        json=context.user_data, 
        headers=context.headers
    )

@then('o sistema deve retornar status 201')
def step_impl(context):
    assert context.response.status_code == 201, \
        f"Esperado 201, recebido {context.response.status_code}. Resposta: {context.response.text}"

@then('o usuário deve ser criado no banco com os campos:')
def step_impl(context):
    User = get_user_model_safe(context)
    user = User.objects.get(email=context.table[0]["email"])
    assert user.username == context.table[0]["username"]


@given('que já existe um usuário com email "{email}"')
def step_impl(context, email):
    User = get_user_model_safe(context)
    User.objects.create_user(
        email=email,
        username="usuario_existente",
        password="senha123"
    )

@when('eu tento cadastrar com o mesmo email:')
def step_impl(context):
    context.user_data = {
        "email": context.table[0]["email"],
        "username": context.table[0]["username"],
        "password": context.table[0]["password"]
    }
    context.response = requests.post(
        f"{context.url_base}/signup/",
        json=context.user_data,
        headers=context.headers
    )

@then('o sistema deve retornar status 400')
def step_impl(context):
    assert context.response.status_code == 400, \
        f"Esperado 400, recebido {context.response.status_code}"

@then('a resposta deve conter a mensagem "Já existe um usuário com este email"')
def step_impl(context):
    response_data = context.response.json()
    assert "Já existe um usuário com este email" in str(response_data), \
        f"Mensagem não encontrada na resposta: {response_data}"


@given('que eu tenho os seguintes dados de superusuário:')
def step_impl(context):
    User = get_user_model_safe(context)
    context.user_data = {
        "email": context.table[0]["email"],
        "username": context.table[0]["username"],
        "password": context.table[0]["password"],
        "is_superuser": context.table[0]["is_superuser"].lower() == "true",
        "is_staff": context.table[0]["is_staff"].lower() == "true"
    }

@then('o usuário deve ter "is_superuser" e "is_staff" como True')
def step_impl(context):
    User = get_user_model_safe(context)
    user = User.objects.get(email=context.user_data["email"])
    assert user.is_superuser is True, "is_superuser deveria ser True"
    assert user.is_staff is True, "is_staff deveria ser True"