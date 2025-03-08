from django.contrib import admin
from .models import Usuario, Advogado, Comunidade, Postagem, Evento

admin.site.register(Usuario)
admin.site.register(Advogado)
admin.site.register(Comunidade)
admin.site.register(Postagem)
admin.site.register(Evento)