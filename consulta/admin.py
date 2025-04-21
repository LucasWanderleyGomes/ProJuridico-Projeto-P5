from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'numero_processo', 'descricao', 'criacao', 'atualizacao', 'assunto')
    list_filter = ('criacao',)
    search_fields = ('nome_cliente', 'numero_processo', 'assunto')
    date_hierarchy = 'criacao'

    fieldsets = (
        ('Informações da Consulta', {
            'fields': ('nome_cliente', 'numero_processo', 'descricao', 'assunto')
        }),
        ('Status', {
            'fields': ('ativo',),
            'classes': ('collapse',)
        }),
    )

    # Remover o campo 'atualizacao' do 'fieldsets', pois ele é preenchido automaticamente pelo Django.
