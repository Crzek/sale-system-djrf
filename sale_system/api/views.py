from .models import Category, Product, Client, Order, OrderProduct
from rest_framework import generics
# serializers
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ClientSerializer,
    CategoriesProductsSerializer,
    OrderSerializer,
    OrderProductsSerializer
)

# models

# Create your views here.
# Para listar las categorias


class CategoryListView(generics.ListAPIView):
    # queryset es el conjunto de datos que se va a mostrar
    queryset = Category.objects.all()
    # serializer_class es el serializador que se va a usar
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ListCreateAPIView se puede listar y crear


class ClientView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# RetrieveUpdateDestroyAPIView se puede obtener, actualizar y eliminar


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    # lookup_url_kwarg es el nombre del parametro que se va a usar en la url
    # client_id -> id del cliente, que se para por el path (/clients/<int:client_id>)
    # de esta manera se puede obtener, actualizar y eliminar un cliente en especifico
    lookup_url_kwarg = "client_id"
    serializer_class = ClientSerializer

#         'categories/<int:categorie_id>/products',


class CategorieProductsView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    # lookup_url_kwarg es el nombre del parametro que se va a usar en la url
    # categorie_id -> id del cliente, que se para por el path (/clients/<int:categorie_id>)
    # de esta manera se puede obtener, actualizar y eliminar un cliente en especifico
    lookup_url_kwarg = "categorie_id"
    serializer_class = CategoriesProductsSerializer


# CreateAPIView -> para crear un objeto solo (POST)
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
