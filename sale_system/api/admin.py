from django.contrib import admin

# Register your models here.
# importamos los modelos
from .models import Category, Product

# registramos los modelos
admin.site.register(Category)
admin.site.register(Product)
