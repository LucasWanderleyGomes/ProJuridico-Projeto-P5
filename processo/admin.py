from django.contrib import admin
from .models import Processo

@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_criacao', 'ativo')
    list_filter = ('categoria', 'data_criacao', 'ativo')
    search_fields = ('titulo', 'descricao', 'categoria')
    date_hierarchy = 'data_criacao'
    list_editable = ('ativo', 'categoria')
    fieldsets = (
        (None, {
            'fields': ('titulo', 'categoria')
        }),
        ('Descrição', {
            'fields': ('descricao',)
        }),
        ('Status', {
            'fields': ('ativo',),
            'classes': ('collapse',)
        }),
    )