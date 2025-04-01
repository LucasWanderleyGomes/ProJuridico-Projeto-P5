from django.contrib import admin
from .models import Advogado

@admin.register(Advogado)
class AdvogadoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'oab', 'especialidade', 'escritorio', 'telefone')
    list_display_links = ('usuario', 'oab')
    search_fields = ('usuario__username', 'oab', 'especialidade')
    list_filter = ('especialidade', 'escritorio')
    autocomplete_fields = ['usuario']
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('usuario', 'telefone')
        }),
        ('Informações Profissionais', {
            'fields': ('oab', 'especialidade', 'escritorio')
        }),
    )