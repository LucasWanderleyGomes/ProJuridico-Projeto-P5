from behave import then
import json

@then('o sistema deve retornar status {status_code:d}')
def step_verifica_status(context, status_code):
    """Step compartilhado para verificar status code"""
    assert context.response.status_code == status_code, \
        f"Esperado {status_code}, recebido {context.response.status_code}. Resposta: {context.response.text}"

@then('o JSON da resposta deve conter o campo "{campo}"')
def step_verifica_campo_json(context, campo):
    """Step compartilhado para verificar campos no JSON"""
    response_json = context.response.json()
    assert campo in response_json, f"Campo '{campo}' não encontrado na resposta: {response_json}"