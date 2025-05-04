from django.contrib import admin
from .models import Postagem

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'comunidade', 'data_publicacao', 'ativo', 'upload')
    list_filter = ('comunidade', 'data_publicacao', 'ativo', 'upload')
    search_fields = ('titulo', 'conteudo', 'usuario__username')
    raw_id_fields = ('usuario', 'comunidade')
    date_hierarchy = 'data_publicacao'
    list_editable = ('ativo',)
    fieldsets = (
        (None, {
            'fields': ('usuario', 'comunidade', 'titulo', 'upload')
        }),
        ('Conteúdo', {
            'fields': ('conteudo',)
        }),
        ('Metadados', {
            'fields': ('ativo',),
            'classes': ('collapse',)
        }),
    )