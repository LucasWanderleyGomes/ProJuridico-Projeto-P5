from rest_framework import serializers
from contas.models import User
from rest_framework.validators import ValidationError

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        email_exists=User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("Esse email já está sendo usado")

        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop("password")  
        user = User(**validated_data)  
        user.set_password(password)  
        user.save() 
        return user 