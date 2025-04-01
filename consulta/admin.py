from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('nome_advogado', 'oab_advogado', 'email_cliente', 'data_hora', 'status', 'horario_fim')
    list_filter = ('status', 'data_hora')
    search_fields = ('nome_advogado', 'oab_advogado', 'email_cliente', 'numero_processo')
    date_hierarchy = 'data_hora'
    fieldsets = (
        ('Participante', {
            'fields': ('content_type', 'object_id')
        }),
        ('Informações da Consulta', {
            'fields': ('nome_advogado', 'oab_advogado', 'email_cliente')
        }),
        ('Agendamento', {
            'fields': ('data_hora', 'duracao', 'status')
        }),
        ('Detalhes', {
            'fields': ('descricao', 'valor', 'numero_processo'),
            'classes': ('collapse',)
        }),
    )
    
    def horario_fim(self, obj):
        return obj.horario_fim
    horario_fim.short_description = 'Término'