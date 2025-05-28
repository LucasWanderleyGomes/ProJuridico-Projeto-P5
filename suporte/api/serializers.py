from rest_framework import serializers
from suporte.models import Suporte

class SuporteSerializer(serializers.ModelSerializer):

    """
    Serializa os dados de uma solicitação de suporte enviada por usuários, relatando algo visto no site ouapenas enviando alguma mensagem para o time.

    atributos: 
    
    'id'
    'nome'
    'email'
    'telefone'
    'mensagem'
    'criado_em'
    'respondido'

    """

    class Meta:
        model = Suporte
        fields = ['id', 'nome', 'email', 'telefone', 'mensagem', 'criado_em', 'respondido']
        read_only_fields = ['id', 'criado_em']