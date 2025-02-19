from django.contrib import admin
from .models import Usuario, Advogado, Cliente, Processo, ReuniaoConsulta, Honorario, RelatorioFinanceiro, Comunidade, Postagem, Evento

admin.site.register(Usuario)
admin.site.register(Advogado)
admin.site.register(Cliente)
admin.site.register(Processo)
admin.site.register(ReuniaoConsulta)
admin.site.register(Honorario)
admin.site.register(RelatorioFinanceiro)
admin.site.register(Comunidade)
admin.site.register(Postagem)
admin.site.register(Evento)