from django.db import models
from cloudinary.models import CloudinaryField  # Para clodinary

# Create your models here.


class Category(models.Model):
    # __tablename__ = "categories"
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,  # clase padre que es la ForeignKey
        # nombre de la relacion
        related_name="products",
        # restriccion para que no se pueda eliminar la categoria si hay productos asociados a ella
        on_delete=models.RESTRICT
    )
    image = CloudinaryField("image", default="")

    def __str__(self) -> str:
        return self.name


class Client (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    code = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.code


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="orderproducts",
        on_delete=models.RESTRICT
    )
    product = models.ForeignKey(
        Product,
        related_name="orderproducts",
        on_delete=models.RESTRICT
    )
    quantity = models.IntegerField(default=1)
