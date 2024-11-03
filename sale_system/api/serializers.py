from rest_framework import serializers
# modelos
from .models import (
    Category,
    Product,
    Client,
    Order,
    OrderProduct
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    # sobreescribir metodo

    def to_representation(self, instance):  # intance -> data del objeto
        represent = super().to_representation(instance)
        print("instance*****", instance.image.url)  # objeto class
        print("represent*****", represent)  # {jsondata}

        # agregar valores adicionales
        # instance -> tiene los datos del objeto
        # se obtiene la url de la imagen correcta
        represent["image"] = instance.image.url

        return represent


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


"""serializers para tablas relacionadas"""


class CategoriesProductsSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField -> es un campo que se relaciona con el modelo
    # many=True -> para que se puedan obtener varios productos
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "products"]


class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ["product", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    # orderproducts -> es el nombre del campo que se relaciona con el modelo OrderProduct
    # many=True -> para que se puedan enviar varios objetos
    # no se le pasa read_only=True, porque se va a enviar desde el cliente
    orderproducts = OrderProductsSerializer(many=True)

    class Meta:
        model = Order
        fields = ["code", "client", "orderproducts"]

    # sobrescribir metodo
    # este metodo se ejecuta cuando se crea un objeto

    def create(self, validated_data):
        # pop -> elimina el campo orderproducts del diccionario
        list_orderproducts = validated_data.pop("orderproducts")
        # crear el objeto order
        order = Order.objects.create(**validated_data)
        # crear los objetos orderproduct
        for obj_orderproduct in list_orderproducts:
            # crear el objeto orderproduct, se le pasa el order y el orderproduct
            # **orderproduct -> desempaqueta el diccionario
            OrderProduct.objects.create(order=order, **obj_orderproduct)
        return order
