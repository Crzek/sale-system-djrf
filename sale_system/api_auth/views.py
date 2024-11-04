from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

# models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# serializers
from .serializers import UserSerializer

# authentication
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.authentication import TokenAuthentication

# permissions
from rest_framework.permissions import IsAuthenticated

# simple jwt
from rest_framework_simplejwt.authentication import JWTAuthentication
# tines mas opciones de autenticación
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

# vista para listar y crear usuarios


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    # permission
    permission_classes = [IsAuthenticated]


# con esto se puede obtener un token de acceso y refresh
# devuelve un json con el token y el usuario
class LoginView(APIView):
    def post(self, request):
        # obtener el username y password del request
        username = request.data.get("username")
        password = request.data.get("password")
        # autenticar el usuario
        user = authenticate(username=username, password=password)
        # si el usuario existe, crear un token de acceso y refresh
        if user:
            refresh = RefreshToken.for_user(user)
            context = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": user.username,
                "full_name": user.first_name + " " + user.last_name
            }
            return Response(data=context, status=200)

        # si el usuario no existe, devolver un error
        return Response({"error": "Credenciales inválidas"}, status=401)
