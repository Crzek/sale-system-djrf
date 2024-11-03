from django.urls import path
# views de la api (app)
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view()),
    path(
        'categories/<int:categorie_id>/products',
        views.CategorieProductsView.as_view()
    ),
    path('products/', views.ProductListView.as_view()),
    path('clients/', views.ClientView.as_view()),
    path('clients/<int:client_id>/', views.ClientDetailView.as_view()),
    path('orders/', views.OrderCreateView.as_view()),
]
