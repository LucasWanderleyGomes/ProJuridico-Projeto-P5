from rest_framework import serializers
from suporte.models import Suporte

class SuporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suporte
        fields = ['id', 'nome', 'email', 'telefone', 'mensagem', 'criado_em', 'respondido']
        read_only_fields = ['id', 'criado_em']