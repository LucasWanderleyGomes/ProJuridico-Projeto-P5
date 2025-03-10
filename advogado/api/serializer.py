from rest_framework import serializers
from advogado.models import Advogado, Usuario


class AdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = '__all__' 

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create(**usuario_data, tipo='ADV')
        advogado = Advogado.objects.create(usuario=usuario, **validated_data)
        return Advogado.objects.create(**validated_data)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'