from rest_framework import serializers
from contas.models import User
from rest_framework.validators import ValidationError
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()

class CreateUserSerializer(UserCreateSerializer):

    """
    Serializer de criação de usuário com validação de e-mail único.
    
    - def validate(self, attrs):

    """

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'password', 'username']

    def validate(self, attrs):
         email_exists=User.objects.filter(email=attrs['email']).exists()

         if email_exists:
             raise ValidationError("Esse email já está sendo usado")

         return super().validate(attrs)

class UserReturnSerializer(serializers.ModelSerializer):

    """
    Serializer de retorno dos dados do usuário, com mais campos para serem consumidos pelo front-end.
    
    """

    class Meta:
        model = User 
        fields = [
            'id',  
            'email',
            'username',
            'is_superuser',
            'descricao_pessoal',
            'data_de_nascimento',
            'insta',
            'whats',
            'linkedin',
            'contato',
            'cnpj', 
        ]

        
# class SignUpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["email", "username", "password"]
#         extra_kwargs = {"password": {"write_only": True}}

#     def validate(self, attrs):
#         email_exists=User.objects.filter(email=attrs['email']).exists()

#         if email_exists:
#             raise ValidationError("Esse email já está sendo usado")

#         return super().validate(attrs)
    
#     def create(self, validated_data):
#         password = validated_data.pop("password")  
#         user = User(**validated_data)  
#         user.set_password(password)  
#         user.save() 
#         return user 