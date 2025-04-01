from django.contrib import admin
from .models import Comunidade

@admin.register(Comunidade)
class ComunidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criacao')
    search_fields = ('nome', 'descricao')
    list_filter = ('data_criacao',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'descricao')
        }),
        ('Regras', {
            'fields': ('regras',),
            'classes': ('collapse',)
        }),
    )