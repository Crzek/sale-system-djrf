from rest_framework.routers import DefaultRouter
from django.urls import path, include
# Views
from . import views

# Router
router = DefaultRouter()
# Register, categories
# basename -> nombre de la url
router.register(
    r'categories',
    views.CatgoriViewSet,
    basename='categories'
)
# Register, products
router.register(
    r'products',
    views.ProductViewSet,
    basename='products'
)
urlpatterns = router.urls
