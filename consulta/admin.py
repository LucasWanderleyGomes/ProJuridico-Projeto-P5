from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'numero_processo', 'descricao', 'criacao', 'atualizacao')
    list_filter = ('criacao',)
    search_fields = ('nome_cliente', 'numero_processo')
    date_hierarchy = 'criacao'

    fieldsets = (
        ('Informações da Consulta', {
            'fields': ('nome_cliente', 'numero_processo', 'descricao')
        }),
        ('Status', {
            'fields': ('ativo',),
            'classes': ('collapse',)
        }),
    )

    