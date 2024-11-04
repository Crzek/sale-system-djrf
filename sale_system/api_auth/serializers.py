from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

# models de autenticación de django
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # campos que se van a mostrar
        fields = ["username", "email", "password", "first_name", "last_name"]
        # para que no se vea el password en la respuesta
        extra_kwargs = {"password": {"write_only": True}}

    # sobreescribir el método create para que se guarde el password
    def create(self, validated_data):
        # validated_data es el diccionario que contiene los datos validados
        # que vienen del cliente
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

# para modificar el Payload del JWT


class LoginSerializer(TokenObtainPairSerializer):
    # para que se pueda usar el método cls
    @classmethod
    def get_token(cls, user):
        # obtener el token
        token = super().get_token(user)
        # agregar claims (datos adicionales)
        token["username"] = user.username
        token["full_name"] = user.first_name + " " + user.last_name
        return token
