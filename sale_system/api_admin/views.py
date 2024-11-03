from rest_framework import viewsets
# importamos modelos de la app api
from api.models import (
    Category,
    Product,
)
# importamos serializadores de la app api
from api.serializers import CategorySerializer, ProductSerializer
# Create your views here.

# ModelViewSet -> para listar, crear, obtener, actualizar y eliminar


class CatgoriViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
