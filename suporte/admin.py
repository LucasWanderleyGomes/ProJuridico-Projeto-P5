from django.contrib import admin
from .models import Suporte

@admin.register(Suporte)
class SuporteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'criado_em', 'respondido')
    list_filter = ('respondido', 'criado_em')
    search_fields = ('nome', 'email', 'mensagem')
    date_hierarchy = 'criado_em'
    list_editable = ('respondido',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'email', 'telefone')
        }),
        ('Mensagem', {
            'fields': ('mensagem',)
        }),
        ('Status', {
            'fields': ('respondido',),
            'classes': ('collapse',)
        }),
    )
