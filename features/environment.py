import os
import subprocess
import time

def antes_de_tudo(contexto):
    """Configurações executadas antes de todos os testes"""
    os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
    import django
    django.setup()
    
    contexto.url_base = "http://localhost:8000/api/v2"  
    contexto.cabecalhos = {'Content-Type': 'application/json'}
    
   
    contexto.servidor_teste = subprocess.Popen(
        ["python", "manage.py", "runserver"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(3)  

def depois_de_tudo(contexto):
    """Finalizações executadas após todos os testes"""
    if hasattr(contexto, 'servidor_teste'):
        contexto.servidor_teste.terminate()


before_all = antes_de_tudo
after_all = depois_de_tudo